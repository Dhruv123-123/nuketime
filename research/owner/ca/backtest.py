"""Backtests on the site x snapshot panel. Question: does ML over the illegible public record (lab time
series, boring logs, activity text, neighbours) predict which open contaminated sites close within 5 years,
and how fast, better than what a buyer uses today?

Scorers
  L1  lookup: closure rate by case_type x county (train snapshots)
  L2  lookup: closure rate by case_type x status_at_T x years-open bucket  (the buyer's heuristic)
  S   LightGBM on structured fields only (what a spreadsheet join could give)
  F   LightGBM on everything (structured + EDF lab + geo + text + neighbours)
Splits
  temporal: train T <= 2013, test T in {2016, 2019}
  spatial: GroupKFold by county (5 folds) over all T
Kill bars (written to results/backtest.json as `verdict`)
  F - max(L1, L2) >= 0.05 AUC on the temporal test, and F - S >= 0.02 (the illegible-data increment).
Also: time-to-closure regression among closed sites, cost model on Cleanup Fund reimbursements if present.
"""
import json
import os

import numpy as np
import pandas as pd
from lightgbm import LGBMClassifier, LGBMRegressor
from scipy.stats import spearmanr
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import mean_absolute_error, roc_auc_score
from sklearn.model_selection import GroupKFold

from common import RESULTS, WORK, log

panel = pd.read_pickle(os.path.join(WORK, "panel.pkl"))
for c in ("county", "case_type", "agency", "status_at_T"):  # a few cases have no county; pandas 3 keeps NaN in str columns
    panel[c] = panel[c].fillna("Unknown").astype(str)
panel = panel.copy()
panel["yo_bucket"] = pd.cut(panel.years_open, [-1, 2, 5, 10, 20, 100], labels=["0-2", "2-5", "5-10", "10-20", "20+"]).astype(str)
META = {"gid", "T", "y", "ttc", "closed_ever", "closure_date", "open_date", "text_all", "yo_bucket"}
CAT = ["case_type", "county", "agency", "status_at_T"]
STRUCT = CAT + ["years_open", "n_status_changes", "n_regact", "n_regact_3y", "yrs_since_regact", "n_contam", "lat", "lon", "T"] \
    + [c for c in panel.columns if c.startswith("c_tok_") or c.startswith("m_tok_")]
STRUCT = [c for c in STRUCT if c in panel.columns]
FULL = [c for c in panel.columns if c not in META]
N_TXT = 30
PARAMS = dict(n_estimators=700, learning_rate=0.03, num_leaves=63, min_child_samples=50, subsample=0.8, subsample_freq=1,
              colsample_bytree=0.6, reg_lambda=5.0, verbose=-1, n_jobs=4)


def frame(df, cols, cats_from, txt=None):
    X = df[[c for c in cols if c not in CAT]].copy()
    for c in X.columns:
        X[c] = pd.to_numeric(X[c], errors="coerce")
    for c in CAT:
        if c in cols:
            X[c] = pd.Categorical(df[c].astype(str).fillna("nan"), categories=sorted(set(cats_from[c].astype(str).fillna("nan"))))
    if txt is not None:
        for i in range(txt.shape[1]):
            X[f"txt{i}"] = txt[:, i]
    return X


def text_blocks(train, test):
    tf = TfidfVectorizer(min_df=5, ngram_range=(1, 2), max_features=30000, sublinear_tf=True)
    A = tf.fit_transform(train.text_all.fillna(""))
    B = tf.transform(test.text_all.fillna(""))
    k = min(N_TXT, A.shape[1] - 1) if A.shape[1] > 1 else 0
    if k < 2:
        return np.zeros((len(train), 0)), np.zeros((len(test), 0))
    svd = TruncatedSVD(n_components=k, random_state=0)
    return svd.fit_transform(A), svd.transform(B)


def lookup(train, test, cols):
    kt = train[cols].astype(str).fillna("nan").agg("|".join, axis=1)
    ks = test[cols].astype(str).fillna("nan").agg("|".join, axis=1)
    m = train.y.groupby(kt).agg(["sum", "count"])
    prior = train.y.mean()
    rate = ((m["sum"] + 5 * prior) / (m["count"] + 5))
    return ks.map(rate).fillna(prior).to_numpy()


def lift(y, score, frac=0.1):
    k = max(1, int(len(score) * frac))
    idx = np.argsort(-score)[:k]
    return float(y[idx].mean() / max(y.mean(), 1e-9))


def prec_at(y, score, k=100):
    idx = np.argsort(-score)[:min(k, len(score))]
    return float(y[idx].mean())


def fit_scores(train, test):
    """Return dict of score arrays on test for L1, L2, S, F plus importances."""
    out = {}
    out["L1"] = lookup(train, test, ["case_type", "county"])
    out["L2"] = lookup(train, test, ["case_type", "status_at_T", "yo_bucket"])
    mS = LGBMClassifier(**PARAMS).fit(frame(train, STRUCT, train), train.y)
    out["S"] = mS.predict_proba(frame(test, STRUCT, train))[:, 1]
    ttr, tte = text_blocks(train, test)
    XF = frame(train, FULL, train, ttr)
    mF = LGBMClassifier(**PARAMS).fit(XF, train.y)
    out["F"] = mF.predict_proba(frame(test, FULL, train, tte))[:, 1]
    imp = pd.Series(mF.booster_.feature_importance("gain"), index=XF.columns).sort_values(ascending=False)
    return out, imp


def evaluate(y, scores, prefix=""):
    y = np.asarray(y)
    res = {}
    for k, sc in scores.items():
        if len(np.unique(y)) < 2:
            continue
        res[f"{prefix}auc_{k}"] = round(float(roc_auc_score(y, sc)), 4)
        res[f"{prefix}lift10_{k}"] = round(lift(y, sc), 3)
        res[f"{prefix}p@100_{k}"] = round(prec_at(y, sc), 3)
    return res


results = {"n_panel_rows": int(len(panel)), "n_sites": int(panel.gid.nunique()), "base_rate_by_T": panel.groupby("T").y.mean().round(3).to_dict(),
           "n_by_T": panel.groupby("T").size().to_dict(), "case_types": panel.case_type.value_counts().head(10).to_dict(),
           "has_edf_share": round(float(panel.has_edf.mean()), 3) if "has_edf" in panel else None}

# ---- temporal ------------------------------------------------------------------------------------------
train = panel[panel["T"] <= 2013].copy()
test = panel[panel["T"] >= 2016].copy()
log(f"temporal: train {len(train):,} (y={train.y.mean():.3f}) test {len(test):,} (y={test.y.mean():.3f})")
sc, imp = fit_scores(train, test)
results["temporal"] = evaluate(test.y, sc)
results["temporal"]["n_train"], results["temporal"]["n_test"] = int(len(train)), int(len(test))
for T, grp in test.groupby("T"):
    m = (test["T"] == T).to_numpy()
    results["temporal"][f"by_T_{T}"] = evaluate(grp.y, {k: v[m] for k, v in sc.items()})
lust = test.case_type.str.upper().str.contains("LUST").to_numpy()
if lust.sum() > 100:
    results["temporal"]["lust_only"] = evaluate(test.y[lust], {k: v[lust] for k, v in sc.items()})
if (~lust).sum() > 100:
    results["temporal"]["non_lust"] = evaluate(test.y[~lust], {k: v[~lust] for k, v in sc.items()})
if "has_edf" in test:
    he = (test.has_edf == 1).to_numpy()
    if he.sum() > 100:
        results["temporal"]["with_edf_only"] = evaluate(test.y[he], {k: v[he] for k, v in sc.items()})
results["feature_importance_top30"] = {k: int(v) for k, v in imp.head(30).items()}
imp_groups = {"edf": imp[[c for c in imp.index if c.startswith(("w_", "s_", "edf_"))]].sum(), "text": imp[[c for c in imp.index if c.startswith("txt")]].sum(),
              "geo": imp[[c for c in imp.index if c in ("n_fpt", "n_wells", "n_borings", "depth_max", "depth_med", "spread_km", "dtw_med_before", "dtw_n_before", "first_year", "n_fpt_3y")]].sum(),
              "neighbours": imp[[c for c in imp.index if c.startswith("nb_")]].sum(), "struct": imp[[c for c in imp.index if c in STRUCT]].sum()}
tot = sum(imp_groups.values()) or 1
results["importance_share"] = {k: round(float(v / tot), 3) for k, v in imp_groups.items()}
pd.DataFrame({"gid": test.gid, "T": test["T"], "y": test.y, "ttc": test.ttc, "county": test.county, "case_type": test.case_type,
              "lat": test.lat, "lon": test.lon, "years_open": test.years_open, "status_at_T": test.status_at_T,
              **{f"p_{k}": v for k, v in sc.items()}}).to_pickle(os.path.join(WORK, "pred_temporal.pkl"))

# ---- spatial (leave counties out) --------------------------------------------------------------------
folds = []
oof = {k: np.zeros(len(panel)) for k in ("L1", "L2", "S", "F")}
for i, (tr, te) in enumerate(GroupKFold(n_splits=min(5, panel.county.nunique())).split(panel, panel.y, groups=panel.county)):
    a, b = panel.iloc[tr], panel.iloc[te]
    sc_i, _ = fit_scores(a, b)
    for k in oof:
        oof[k][te] = sc_i[k]
    r = evaluate(b.y, sc_i); r["counties"] = sorted(b.county.unique())[:12]; r["n"] = int(len(b))
    folds.append(r); log(f"  spatial fold {i}: " + ", ".join(f"{k}={r.get('auc_'+k)}" for k in ("L1", "L2", "S", "F")))
results["spatial_folds"] = folds
results["spatial_pooled"] = evaluate(panel.y, oof)

# ---- time to closure (regression among sites that closed within horizon) ----------------------------
tr_c, te_c = train[train.y == 1], test[test.y == 1]
if len(tr_c) > 300 and len(te_c) > 100:
    ttr, tte = text_blocks(tr_c, te_c)
    mR = LGBMRegressor(**{**PARAMS, "n_estimators": 500}).fit(frame(tr_c, FULL, tr_c, ttr), tr_c.ttc)
    pr = mR.predict(frame(te_c, FULL, tr_c, tte))
    base = te_c[["case_type", "county"]].astype(str).fillna("nan").agg("|".join, axis=1).map(tr_c.ttc.groupby(tr_c[["case_type", "county"]].astype(str).fillna("nan").agg("|".join, axis=1)).median()).fillna(tr_c.ttc.median())
    results["time_to_close"] = {"n_train": int(len(tr_c)), "n_test": int(len(te_c)), "median_ttc_test": round(float(te_c.ttc.median()), 2),
                                "mae_model": round(float(mean_absolute_error(te_c.ttc, pr)), 3), "mae_lookup": round(float(mean_absolute_error(te_c.ttc, base)), 3),
                                "spearman_model": round(float(spearmanr(te_c.ttc, pr).correlation), 3), "spearman_lookup": round(float(spearmanr(te_c.ttc, base).correlation), 3)}

# ---- cost (Cleanup Fund reimbursed-to-date, 2020 active claims) --------------------------------------
cuf = pd.read_pickle(os.path.join(WORK, "cuf.pkl")) if os.path.exists(os.path.join(WORK, "cuf.pkl")) else pd.DataFrame()
if len(cuf) > 200:
    # Label: log10 reimbursed-to-date in the Oct 2020 Cleanup Fund capture (capped at the $1.5M per-occurrence
    # limit). Features as of 1 Jan T. Run at T=2010 (main) and T=2007 (check), with the full model, the
    # structured-only model and the case_type x county lookup, 5-fold leave-counties-out.
    results["cost"] = {}
    for Tc in (2010, 2007):
        c = panel[panel["T"] == Tc].merge(cuf, on="gid")
        c = c[c.reimb > 0].reset_index(drop=True); c["lr"] = np.log10(c.reimb)
        if len(c) < 200:
            continue
        rs = []
        for tr, te in GroupKFold(n_splits=min(5, c.county.nunique())).split(c, c.lr, groups=c.county):
            a, b = c.iloc[tr], c.iloc[te]
            ttr, tte = text_blocks(a, b)
            m = LGBMRegressor(**{**PARAMS, "n_estimators": 400}).fit(frame(a, FULL, a, ttr), a.lr)
            p = m.predict(frame(b, FULL, a, tte))
            mS = LGBMRegressor(**{**PARAMS, "n_estimators": 400}).fit(frame(a, STRUCT, a), a.lr)
            pS = mS.predict(frame(b, STRUCT, a))
            # counties are held out, so the lookup keys on case type x status x years-open (the L2 buyer heuristic)
            kcols = ["case_type", "status_at_T", "yo_bucket"]
            base = b[kcols].astype(str).fillna("nan").agg("|".join, axis=1).map(a.lr.groupby(a[kcols].astype(str).fillna("nan").agg("|".join, axis=1)).mean()).fillna(a.lr.mean())
            # structured + how much sampling had been done before T: reimbursed-to-date includes money spent before T,
            # so sampling volume is partly an accounting proxy for past spend rather than a read of the contamination
            VOL = STRUCT + [x for x in ("edf_n_samples", "edf_n_years", "edf_first_year", "edf_n_fpt_max", "n_fpt", "n_wells", "n_borings") if x in c.columns]
            mV = LGBMRegressor(**{**PARAMS, "n_estimators": 400}).fit(frame(a, VOL, a), a.lr)
            pV = mV.predict(frame(b, VOL, a))
            rs.append((spearmanr(b.lr, p).correlation, spearmanr(b.lr, pS).correlation, spearmanr(b.lr, base).correlation,
                       mean_absolute_error(b.lr, p), mean_absolute_error(b.lr, pS), mean_absolute_error(b.lr, base),
                       spearmanr(b.lr, pV).correlation, mean_absolute_error(b.lr, pV)))
        rs = np.nanmean(np.array(rs, dtype=float), axis=0)
        results["cost"][f"T{Tc}"] = {"n_sites_with_reimb": int(len(c)), "median_reimb_usd": float(c.reimb.median()),
                                     "share_at_cap_1.4M+": round(float((c.reimb >= 1.4e6).mean()), 3), "has_edf_share": round(float(c.has_edf.mean()), 3),
                                     "spearman_model": round(float(rs[0]), 3), "spearman_structured": round(float(rs[1]), 3), "spearman_lookup": round(float(rs[2]), 3),
                                     "mae_log10_model": round(float(rs[3]), 3), "mae_log10_structured": round(float(rs[4]), 3), "mae_log10_lookup": round(float(rs[5]), 3),
                                     "spearman_structured_plus_sampling_volume": round(float(rs[6]), 3), "mae_log10_structured_plus_sampling_volume": round(float(rs[7]), 3)}
else:
    results["cost"] = "no Cleanup Fund table parsed (cuf.pkl empty)"

# ---- verdict ---------------------------------------------------------------------------------------------
t = results["temporal"]
gain_lookup = t["auc_F"] - max(t["auc_L1"], t["auc_L2"])
gain_struct = t["auc_F"] - t["auc_S"]
sp = results["spatial_pooled"]
results["verdict"] = {
    "temporal_gain_over_best_lookup": round(gain_lookup, 4), "temporal_gain_over_structured_ml": round(gain_struct, 4),
    "spatial_gain_over_best_lookup": round(sp["auc_F"] - max(sp["auc_L1"], sp["auc_L2"]), 4),
    "spatial_gain_over_structured_ml": round(sp["auc_F"] - sp["auc_S"], 4),
    "passes_kill_bar": bool(gain_lookup >= 0.05 and gain_struct >= 0.02),
    "kill_bar": "F - max(L1,L2) >= 0.05 AUC (temporal) and F - S >= 0.02",
}
json.dump(results, open(os.path.join(RESULTS, "backtest.json"), "w"), indent=2, default=str)


def md():
    L = ["# California closure backtest\n", f"Panel: {results['n_panel_rows']:,} site-snapshots, {results['n_sites']:,} sites. "
         f"Base rate by T: {results['base_rate_by_T']}\n", "\n## Temporal (train T<=2013, test 2016+2019)\n",
         "| scorer | AUC | top-decile lift | P@100 |", "|---|---|---|---|"]
    for k, name in (("L1", "lookup case_type x county"), ("L2", "lookup case_type x status x years-open"), ("S", "LightGBM structured only"), ("F", "LightGBM everything")):
        L.append(f"| {name} | {t.get('auc_'+k)} | {t.get('lift10_'+k)} | {t.get('p@100_'+k)} |")
    L.append("\n## Spatial (leave counties out, pooled)\n\n| scorer | AUC | lift | P@100 |\n|---|---|---|---|")
    for k in ("L1", "L2", "S", "F"):
        L.append(f"| {k} | {sp.get('auc_'+k)} | {sp.get('lift10_'+k)} | {sp.get('p@100_'+k)} |")
    for key in ("lust_only", "non_lust", "with_edf_only", "by_T_2016", "by_T_2019"):
        if key in t:
            L.append(f"\n{key}: " + ", ".join(f"{k}={v}" for k, v in t[key].items() if k.startswith("auc")))
    L.append(f"\n## Importance share: {results['importance_share']}\n")
    L.append("Top features: " + ", ".join(list(results["feature_importance_top30"])[:20]))
    if "time_to_close" in results:
        L.append(f"\n## Time to closure (closed sites): {results['time_to_close']}")
    L.append(f"\n## Cost: {results['cost']}")
    L.append(f"\n## Verdict: {results['verdict']}\n")
    return "\n".join(L)


open(os.path.join(RESULTS, "backtest.md"), "w").write(md())
log(json.dumps(results["temporal"], indent=1)); log(json.dumps(results["verdict"], indent=1))
