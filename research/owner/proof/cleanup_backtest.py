"""Backtest: can public case records predict how long a contaminated site takes to close better
than the lookup a buyer would use?

Data: Pennsylvania DEP storage-tank cleanup incidents (Tank_Cleanup_Incidents.csv), as mirrored in
github.com/Eastern-Research-Group/UST (ust/sql/states/PA/Releases/). One row per incident x substance.
Label: incident closed ("Cleanup Completed") within 3 years of confirmation.
Split by time: train on incidents confirmed 1995-2007, test on 2008-2012 (all old enough that the
3-year outcome is known).
Features: substance, impact (soil / groundwater / ...), source and cause, notification source,
region, incident text (TF-IDF), and a spatial-history feature, the closure rate of earlier incidents
within ~5 km confirmed before the snapshot (the "neighbouring drill holes" of this problem).
Baselines: closure rate by impact x substance (what a buyer's rule of thumb looks like) and by county.
"""
import json
import sys

import numpy as np
import pandas as pd
from lightgbm import LGBMClassifier
from scipy.sparse import hstack, csr_matrix
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import roc_auc_score

SRC, OUT = sys.argv[1], sys.argv[2]
d = pd.read_csv(SRC, encoding="utf-8-sig", low_memory=False)
for c in ["SUSPECT_DATE", "CONFIRMED_DATE", "STATUS_DATE"]:
    d[c] = pd.to_datetime(d[c], format="%m/%d/%Y", errors="coerce")

join = lambda s: "|".join(sorted(set(map(str, s.dropna()))))
g = d.groupby("INCIDENT_ID").agg(
    confirmed=("CONFIRMED_DATE", "min"), suspect=("SUSPECT_DATE", "min"), status=("STATUS_CODE", "first"),
    status_desc=("STATUS_DESCRIPTION", "first"), status_date=("STATUS_DATE", "max"),
    region=("REGION", "first"), county=("COUNTY", "first"), lat=("LATITUDE", "first"), lon=("LONGITUDE", "first"),
    impact=("IMPACT_CODE", join), substance=("SUBSTANCE_CODE", join), n_subst=("SUBSTANCE_CODE", "nunique"),
    itype=("INCIDENT_TYPE", "first"), cause=("SOURCE_CAUSE_OF_RELEASE", "first"), notif=("SOURCE_OF_NOTIFICATION", "first"),
    discovered=("RELEASE_DISCOVERED", "first"), tank=("TANK", "first"), owner=("CLIENT_OWNER", "first"),
    text=("INCIDENT_DESCRIPTION", lambda s: " ".join(map(str, s.dropna().unique()))),
    comment=("COMMENT", lambda s: " ".join(map(str, s.dropna().unique()))),
).reset_index()
g = g[g.confirmed.notna()].copy()
g["closed"] = g.status_desc.astype(str).str.contains("Completed", case=False)
g["dur_yr"] = np.where(g.closed, (g.status_date - g.confirmed).dt.days / 365.25, np.nan)
g["y"] = (g.closed & (g.dur_yr <= 3)).astype(int)
g["year"] = g.confirmed.dt.year
g["owner_n"] = g.owner.map(g.owner.value_counts())  # repeat owners (chains) vs one-off
g["text_all"] = (g.text.fillna("") + " " + g.comment.fillna("")).str.lower()

train = g[(g.year >= 1995) & (g.year <= 2007)].copy()
test = g[(g.year >= 2008) & (g.year <= 2012)].copy()


def spatial_history(target, pool, radius_km=5.0):
    """Closure-within-3y rate of incidents within radius, confirmed before each target's date."""
    pool = pool.dropna(subset=["lat", "lon"]).sort_values("confirmed")
    P = np.radians(pool[["lat", "lon"]].to_numpy())
    pd_dates = pool.confirmed.to_numpy()
    py = pool.y.to_numpy()
    # outcome known only 3 years after confirmation; use only those confirmed >3y before target
    out_rate, out_n = [], []
    for lat, lon, t in zip(np.radians(target.lat.to_numpy(dtype=float)), np.radians(target.lon.to_numpy(dtype=float)), target.confirmed.to_numpy()):
        if np.isnan(lat):
            out_rate.append(np.nan); out_n.append(0); continue
        known = pd_dates <= (t - np.timedelta64(3 * 365, "D"))
        if not known.any():
            out_rate.append(np.nan); out_n.append(0); continue
        Q = P[known]
        dlat, dlon = Q[:, 0] - lat, Q[:, 1] - lon
        a = np.sin(dlat / 2) ** 2 + np.cos(lat) * np.cos(Q[:, 0]) * np.sin(dlon / 2) ** 2
        near = 6371 * 2 * np.arcsin(np.sqrt(a)) <= radius_km
        n = int(near.sum())
        out_rate.append((py[known][near].sum() + 1) / (n + 2)); out_n.append(n)
    return np.array(out_rate), np.array(out_n)


everything = g[g.year <= 2012]
for df in (train, test):
    df["nb_rate"], df["nb_n"] = spatial_history(df, everything)

cats = ["region", "county", "impact", "substance", "itype", "cause", "notif", "discovered", "tank"]
nums = ["n_subst", "owner_n", "nb_rate", "nb_n", "year"]
tf = TfidfVectorizer(min_df=5, ngram_range=(1, 2), max_features=20000)
Ttr = tf.fit_transform(train.text_all)
Tte = tf.transform(test.text_all)
svd = TruncatedSVD(n_components=30, random_state=0)
Str, Ste = svd.fit_transform(Ttr), svd.transform(Tte)


def frame(df, S):
    X = df[nums].copy().astype(float)
    for c in cats:
        X[c] = pd.Categorical(df[c].map(str), categories=sorted(set(train[c].map(str))))
    for i in range(S.shape[1]):
        X[f"txt{i}"] = S[:, i]
    return X


Xtr, Xte = frame(train, Str), frame(test, Ste)
m = LGBMClassifier(n_estimators=500, learning_rate=0.03, num_leaves=31, min_child_samples=40,
                   subsample=0.8, subsample_freq=1, colsample_bytree=0.8, verbose=-1).fit(Xtr, train.y)
p = m.predict_proba(Xte)[:, 1]


def lookup(cols):
    kt = train[cols].apply(lambda c: c.map(str)).agg("|".join, axis=1)
    ks = test[cols].apply(lambda c: c.map(str)).agg("|".join, axis=1)
    return ks.map(train.y.groupby(kt).mean()).fillna(train.y.mean()).to_numpy()


def top_decile_lift(score):
    k = max(1, len(score) // 10)
    idx = np.argsort(-score)[:k]
    return round(float(test.y.to_numpy()[idx].mean() / test.y.mean()), 2)


b1, b2 = lookup(["impact", "substance"]), lookup(["county"])
imp = pd.Series(m.booster_.feature_importance("gain"), index=Xtr.columns).sort_values(ascending=False)
res = {
    "source": "PA DEP storage-tank cleanup incidents via github.com/Eastern-Research-Group/UST",
    "n_incidents": int(len(g)), "n_train_1995_2007": int(len(train)), "n_test_2008_2012": int(len(test)),
    "closed_within_3y_rate_train": round(float(train.y.mean()), 3), "closed_within_3y_rate_test": round(float(test.y.mean()), 3),
    "auc_model": round(roc_auc_score(test.y, p), 3),
    "auc_lookup_impact_x_substance": round(roc_auc_score(test.y, b1), 3),
    "auc_lookup_county": round(roc_auc_score(test.y, b2), 3),
    "auc_neighbour_history_only": round(roc_auc_score(test.y[test.nb_rate.notna()], test.nb_rate.dropna()), 3),
    "top_decile_lift_model": top_decile_lift(p), "top_decile_lift_lookup": top_decile_lift(b1),
    "median_years_to_close_test_closed": round(float(test.dur_yr.median()), 2),
    "top_features_gain": {k: round(float(v)) for k, v in imp.head(10).items()},
}
json.dump(res, open(OUT, "w"), indent=2)
print(json.dumps(res, indent=2))
