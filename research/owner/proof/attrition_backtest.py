"""Backtest: can public queue data predict which grid connection requests withdraw next year,
and so where interconnection capacity frees up?

Inputs: two Berkeley Lab "Queued Up" snapshots loaded by load_queues.py (a.pkl = end-2024,
b.pkl = end-2025). Every feature comes from the earlier snapshot; every label from the later one.

Test 1 (spatial): real end-2024 snapshot -> status in end-2025 snapshot. Leave-one-region-out,
so the model is always scored on a grid operator it never trained on.
Test 2 (temporal): train on an end-2023 snapshot rebuilt from withdrawal and online dates in the
end-2024 file (ERCOT, PJM, ISO-NE only, where those dates are ~100% filled), test on the real
end-2024 snapshot -> 2025 outcomes in the same regions.
Business metric: rank points of interconnection (POIs) by predicted MW withdrawn next year and
measure how much of the actually freed MW the top of the list captures, against the naive
ranking by MW queued.
"""
import json
import sys

import numpy as np
import pandas as pd
from lightgbm import LGBMClassifier
from sklearn.metrics import roc_auc_score

A, B, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
a = pd.read_pickle(A)
b = pd.read_pickle(B)
for d in (a, b):
    d["mw"] = d.mw.clip(lower=0)


def norm_poi(s):
    return (s.astype(str).str.lower().str.replace(r"[^a-z0-9 ]", " ", regex=True)
            .str.replace(r"\b(kv|substation|sub|switching station|station|tap|line)\b", " ", regex=True)
            .str.split().str.join(" "))


for d in (a, b):
    d["poi"] = d.region.astype(str) + "|" + norm_poi(d.poi_name)
    d["k2"] = d.region.astype(str) + "|" + d.entity.astype(str) + "|" + d.q_id.astype(str).str.strip()


def match_outcomes(snap, later):
    """Status of each snapshot project in the later file: exact key, then region+entity+q_id if unique."""
    l1 = later.drop_duplicates("key", keep=False).set_index("key").q_status
    out = snap.key.map(l1)
    l2 = later[~later.k2.duplicated(keep=False)].set_index("k2").q_status
    out = out.fillna(snap.k2.map(l2))
    return out


def features(snap, when, history):
    """Features known at `when`. `history` holds every project entered before `when` with its
    status at `when` ('withdrawn' or other) to compute local attrition rates."""
    f = pd.DataFrame(index=snap.index)
    f["age_yr"] = (when - snap.q_date).dt.days / 365.25
    f["log_mw"] = np.log1p(snap.mw)
    f["q_year"] = snap.q_date.dt.year
    f["has_dev"] = snap.developer.notna().astype(int)
    f["has_name"] = snap.project_name.notna().astype(int)
    f["hybrid"] = snap.type_2.notna().astype(int)
    for c in ["region", "type_clean", "service", "state"]:
        f[c] = snap[c].astype(str).astype("category")
    # crowding at the POI and county among projects active at `when`
    act = snap
    g = act.groupby("poi")
    f["poi_n"] = snap.poi.map(g.size())
    f["poi_mw"] = np.log1p(snap.poi.map(g.mw.sum()))
    f["poi_share"] = snap.mw / snap.poi.map(g.mw.sum()).replace(0, np.nan)
    f["poi_rank"] = g.q_date.rank(method="first").reindex(snap.index)  # place in line at the POI
    cty = snap.state.astype(str) + "|" + snap.county.astype(str)
    f["cty_mw"] = np.log1p(cty.map(snap.assign(c=cty).groupby("c").mw.sum()))
    # local attrition history: share of everything ever filed at this POI / county / entity withdrawn by `when`
    h = history.copy()
    h["wd"] = (h.status_at == "withdrawn").astype(float)
    for name, key in [("poi", h.poi), ("cty", h.state.astype(str) + "|" + h.county.astype(str)), ("ent", h.entity.astype(str))]:
        grp = h.groupby(key).wd.agg(["sum", "count"])
        k = snap.poi if name == "poi" else (cty if name == "cty" else snap.entity.astype(str))
        s, n = k.map(grp["sum"]).fillna(0), k.map(grp["count"]).fillna(0)
        f[f"{name}_wd_rate"] = (s + 2) / (n + 4)  # smoothed
        f[f"{name}_hist_n"] = n
    f["prop_slip_yr"] = (snap.prop_date - when).dt.days / 365.25
    return f


def poi_capture(df, score_col, label_mw_col, k_list=(25, 50, 100)):
    p = df.groupby("poi").agg(pred=(score_col, "sum"), freed=(label_mw_col, "sum"), queued=("mw", "sum"))
    tot = p.freed.sum()
    res = {}
    for k in k_list:
        res[f"top{k}_model"] = round(p.nlargest(k, "pred").freed.sum() / tot, 3)
        res[f"top{k}_naive_mw"] = round(p.nlargest(k, "queued").freed.sum() / tot, 3)
    res["pois"] = int(len(p))
    res["freed_mw_total"] = round(float(tot))
    return res


def lookup_baseline(train, test, cols):
    """Historical withdrawal rate of the project's cell (e.g. type x phase), learned on train only."""
    kt = train[cols].apply(lambda c: c.map(str)).agg("|".join, axis=1)
    ks = test[cols].apply(lambda c: c.map(str)).agg("|".join, axis=1)
    return ks.map(train.y.groupby(kt).mean()).fillna(train.y.mean()).values


model = lambda: LGBMClassifier(n_estimators=400, learning_rate=0.03, num_leaves=31, min_child_samples=30,
                               subsample=0.8, subsample_freq=1, colsample_bytree=0.8, verbose=-1)
results = {}

# ---------- Test 1: spatial, real snapshots ----------
T24 = pd.Timestamp("2024-12-31")
act24 = a[a.q_status == "active"].copy()
act24["later"] = match_outcomes(act24, b)
act24 = act24[act24.later.notna()].copy()
act24["y"] = (act24.later == "withdrawn").astype(int)
hist24 = a[a.q_date <= T24].copy()
hist24["status_at"] = hist24.q_status
X = features(act24, T24, hist24)
X["phase"] = act24.IA_phase_clean.astype(str).astype("category")
act24["p"] = np.nan
for reg in act24.region.unique():
    tr, te = act24.region != reg, act24.region == reg
    m = model().fit(X[tr], act24.y[tr])
    act24.loc[te, "p"] = m.predict_proba(X[te])[:, 1]
act24["base_p"] = np.nan
act24["phase"] = act24.IA_phase_clean.astype(str)
for reg in act24.region.unique():
    tr, te = act24.region != reg, act24.region == reg
    act24.loc[te, "base_p"] = lookup_baseline(act24[tr], act24[te], ["type_clean", "phase"])
act24["age_p"] = (T24 - act24.q_date).dt.days.fillna(0)
act24["p_mw"], act24["wd_mw"] = act24.p * act24.mw, act24.y * act24.mw
per_region = {r: round(roc_auc_score(g.y, g.p), 3) for r, g in act24.groupby("region") if g.y.nunique() > 1}
results["spatial_leave_one_region_out"] = {
    "n_projects": int(len(act24)), "withdrawal_rate_2025": round(act24.y.mean(), 3),
    "auc_model": round(roc_auc_score(act24.y, act24.p), 3),
    "auc_baseline_type_x_phase": round(roc_auc_score(act24.y, act24.base_p), 3),
    "auc_baseline_age": round(roc_auc_score(act24.y, act24.age_p), 3),
    "auc_model_by_region": per_region,
    "poi_capture_mw": poi_capture(act24, "p_mw", "wd_mw"),
}

# ---------- Test 2: temporal (ERCOT, PJM, ISO-NE) ----------
REG = ["ERCOT", "PJM", "ISO-NE"]
T23 = pd.Timestamp("2023-12-31")
h = a[a.region.isin(REG) & (a.q_date <= T23)].copy()
alive23 = (
    (h.q_status.isin(["active", "suspended"]))
    | ((h.q_status == "withdrawn") & (h.wd_date > T23))
    | ((h.q_status == "operational") & (h.on_date > T23))
)
snap23 = h[alive23].copy()
snap23["y"] = ((snap23.q_status == "withdrawn") & (snap23.wd_date <= T23 + pd.DateOffset(years=1))).astype(int)
hist23 = h.copy()
hist23["status_at"] = np.where((h.q_status == "withdrawn") & (h.wd_date <= T23), "withdrawn", "other")
hist23 = hist23[~((h.q_status == "withdrawn") & h.wd_date.isna())]
Xtr = features(snap23, T23, hist23)
te = act24[act24.region.isin(REG)].copy()
Xte = features(te, T24, hist24[hist24.region.isin(REG)])
cols = list(Xtr.columns)
for c in ["region", "type_clean", "service", "state"]:
    cats = pd.api.types.union_categoricals([Xtr[c], Xte[c]]).categories
    Xtr[c] = pd.Categorical(Xtr[c].astype(str), categories=cats)
    Xte[c] = pd.Categorical(Xte[c].astype(str), categories=cats)
m = model().fit(Xtr[cols], snap23.y)
te["p"] = m.predict_proba(Xte[cols])[:, 1]
snap23["type_clean"] = snap23.type_clean.astype(str)
te["base_p"] = lookup_baseline(snap23.assign(region=snap23.region.astype(str)), te.assign(region=te.region.astype(str)), ["region", "type_clean"])
te["p_mw"], te["wd_mw"] = te.p * te.mw, te.y * te.mw
imp = pd.Series(m.booster_.feature_importance("gain"), index=cols).sort_values(ascending=False)
results["temporal_train2023_test2024"] = {
    "n_train": int(len(snap23)), "train_withdrawal_rate": round(snap23.y.mean(), 3),
    "n_test": int(len(te)), "test_withdrawal_rate": round(te.y.mean(), 3),
    "auc_model": round(roc_auc_score(te.y, te.p), 3),
    "auc_baseline_region_x_type": round(roc_auc_score(te.y, te.base_p), 3),
    "auc_baseline_age": round(roc_auc_score(te.y, (T24 - te.q_date).dt.days.fillna(0)), 3),
    "auc_model_by_region": {r: round(roc_auc_score(g.y, g.p), 3) for r, g in te.groupby("region") if g.y.nunique() > 1},
    "poi_capture_mw": poi_capture(te, "p_mw", "wd_mw"),
    "top_features_gain": {k: round(float(v)) for k, v in imp.head(10).items()},
}

# list the POIs the spatial model expects to free most MW (as of the end-2025 snapshot use, rerun on b)
results["match_rate_end2024_active"] = round(len(act24) / int((a.q_status == "active").sum()), 3)
json.dump(results, open(OUT, "w"), indent=2)
print(json.dumps(results, indent=2))
