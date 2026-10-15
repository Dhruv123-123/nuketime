"""Assemble the site x snapshot panel: for each snapshot year T, every case open on 1 Jan T, with
features built only from records dated before T and the label "closed within HORIZON years of T".

Writes work/panel.pkl. Columns:
  meta:     gid, T, county, case_type, lat, lon, agency
  labels:   y (closed within HORIZON years), ttc (years from T to closure, NaN if not closed in horizon),
            closed_ever, closure_date, open_date
  struct:   status_at_T, years_open, n_status_changes, n_regact, n_regact_3y, n_contam, has_gw (media),
            contaminant / media tokens (multi-hot, top 25), T
  text:     regact_text (activities before T) + site_history  (vectorised later in backtest.py)
  edf:      per analyte x matrix stats before T, plus n_samples_all, n_years_sampled, first/last sample year
  geo:      static well/boring counts, depth, spread, dtw_med_before_T
  nb:       neighbour closure rate within 3 km among sites whose 5-year outcome was known by T
"""
import os
import re

import numpy as np
import pandas as pd
from sklearn.neighbors import BallTree

from common import ANALYTES, HORIZON, SNAPSHOTS, WORK, log

sites = pd.read_pickle(os.path.join(WORK, "sites.pkl"))
sh = pd.read_pickle(os.path.join(WORK, "status_history.pkl"))
ra = pd.read_pickle(os.path.join(WORK, "regact.pkl"))
edf = pd.read_pickle(os.path.join(WORK, "edf_agg.pkl")) if os.path.exists(os.path.join(WORK, "edf_agg.pkl")) else pd.DataFrame()
edf_all = pd.read_pickle(os.path.join(WORK, "edf_all.pkl")) if os.path.exists(os.path.join(WORK, "edf_all.pkl")) else pd.DataFrame()
geo = pd.read_pickle(os.path.join(WORK, "geo_static.pkl")) if os.path.exists(os.path.join(WORK, "geo_static.pkl")) else pd.DataFrame(columns=["gid"])
dtw = pd.read_pickle(os.path.join(WORK, "geo_dtw_year.pkl")) if os.path.exists(os.path.join(WORK, "geo_dtw_year.pkl")) else pd.DataFrame(columns=["gid", "year", "dtw_med", "n_meas"])

# ---- open and closure dates --------------------------------------------------------------------------
sh["is_closed"] = sh.status.str.upper().str.startswith("COMPLETED") | sh.status.str.upper().str.contains("CASE CLOSED")
first_hist = sh.groupby("gid").date.min()
first_ra = ra.groupby("gid").date.min() if len(ra) else pd.Series(dtype="datetime64[ns]")
closure = sh[sh.is_closed].groupby("gid").date.min()
s = sites.set_index("gid")
open_date = pd.concat([first_hist.rename("a"), first_ra.rename("b"), s.begin_date.rename("c")], axis=1).min(axis=1)
# sites whose only record is the sites table: use status_date as the open date if still open (conservative)
open_date = open_date.reindex(s.index)
fallback = s.status_date.where(~s.closed_flag)
open_date = open_date.fillna(fallback)
closure_date = closure.reindex(s.index)
closure_date = closure_date.fillna(s.status_date.where(s.closed_flag))
s["open_date"], s["closure_date"] = open_date, closure_date
s = s[s.open_date.notna()]
log(f"sites with open date: {len(s):,}; closed ever: {s.closure_date.notna().sum():,}; "
    f"median years to close: {((s.closure_date - s.open_date).dt.days / 365.25).median():.1f}")


def tokens(series, top=25, minlen=3):
    toks = series.fillna("").str.upper().str.split(r"[,;/|]+")
    ex = toks.explode().str.strip()
    ex = ex[ex.str.len() >= minlen]
    keep = ex.value_counts().head(top).index
    out = pd.DataFrame(index=series.index)
    for k in keep:
        out["tok_" + re.sub(r"[^A-Z0-9]+", "_", k)[:24]] = toks.map(lambda L: int(any(t.strip().upper() == k for t in L)))
    return out, keep


contam_tok, contam_keys = tokens(s.contaminants, top=25)
media_tok, media_keys = tokens(s.media, top=8)
contam_tok.columns = ["c_" + c for c in contam_tok.columns]
media_tok.columns = ["m_" + c for c in media_tok.columns]
s["n_contam"] = s.contaminants.fillna("").str.count(r"[,;/|]") + (s.contaminants.fillna("") != "").astype(int)

# ---- EDF features at T --------------------------------------------------------------------------------
WATER_STATS = ["max_all", "max_3y", "logmean_3y", "frac_det_3y", "fptdet_3y", "yrs_since_det", "slope"]


def edf_features(T):
    if edf.empty:
        return pd.DataFrame(index=pd.Index([], name="gid"))
    e = edf[edf.year < T]
    if e.empty:
        return pd.DataFrame(index=pd.Index([], name="gid"))
    key = ["gid", "analyte", "mclass"]
    r3 = e[e.year >= T - 3]
    g = e.groupby(key)
    f = pd.DataFrame({"max_all": g.max_det.max()})
    g3 = r3.groupby(key)
    f["max_3y"] = g3.max_det.max()
    f["logmean_3y"] = g3.sumlog_det.sum() / g3.n_det.sum().replace(0, np.nan)
    f["frac_det_3y"] = g3.n_det.sum() / g3.n.sum().replace(0, np.nan)
    f["fptdet_3y"] = g3.n_fpt_det.sum()
    det = e[e.n_det > 0]
    f["yrs_since_det"] = T - det.groupby(key).year.max()
    # slope of log10(yearly max) per year over the 6 years before T, >=3 detected years
    w = det[det.year >= T - 6].copy()
    w["x"] = w.year.astype(float); w["y"] = np.log10(w.max_det)
    w["xy"] = w.x * w.y; w["xx"] = w.x * w.x
    gw = w.groupby(key).agg(n=("x", "size"), sx=("x", "sum"), sy=("y", "sum"), sxy=("xy", "sum"), sxx=("xx", "sum"))
    den = gw.n * gw.sxx - gw.sx ** 2
    f["slope"] = ((gw.n * gw.sxy - gw.sx * gw.sy) / den.replace(0, np.nan)).where(gw.n >= 3)
    f = f.reset_index()
    water = f[f.mclass == "water"].set_index(["gid", "analyte"])[WATER_STATS].unstack("analyte")
    water.columns = [f"w_{a}_{st}" for st, a in water.columns]
    soil = f[f.mclass == "soil"].set_index(["gid", "analyte"])[["max_all"]].unstack("analyte")
    soil.columns = [f"s_{a}_max" for _, a in soil.columns]
    out = pd.concat([water, soil], axis=1)
    if not edf_all.empty:
        ea = edf_all[edf_all.year < T].groupby("gid").agg(edf_n_samples=("n_samples", "sum"), edf_n_years=("year", "nunique"),
                                                          edf_first_year=("year", "min"), edf_last_year=("year", "max"),
                                                          edf_n_params_max=("n_params", "max"), edf_n_fpt_max=("n_fpt", "max"))
        ea["edf_yrs_since_last"] = T - ea.edf_last_year
        ea["edf_samples_3y"] = edf_all[(edf_all.year < T) & (edf_all.year >= T - 3)].groupby("gid").n_samples.sum()
        out = pd.concat([out, ea], axis=1)
    out.index.name = "gid"
    return out


# ---- neighbour history -----------------------------------------------------------------------------------
def neighbour_rate(target, T, radius_km=3.0):
    """Closure-within-HORIZON rate among sites whose HORIZON window ended before T (outcome known at T)."""
    pool = s[(s.open_date < pd.Timestamp(year=T - HORIZON, month=1, day=1))].dropna(subset=["lat", "lon"])
    pool = pool[(pool.lat.between(32, 42.5)) & (pool.lon.between(-125, -114))]
    if pool.empty or target.empty:
        return pd.Series(np.nan, index=target.index), pd.Series(0, index=target.index)
    py = ((pool.closure_date - pool.open_date).dt.days / 365.25 <= HORIZON).astype(float).to_numpy()
    tree = BallTree(np.radians(pool[["lat", "lon"]].to_numpy()), metric="haversine")
    tl = target[["lat", "lon"]].to_numpy(dtype=float)
    ok = ~np.isnan(tl).any(axis=1)
    rate = np.full(len(target), np.nan); n = np.zeros(len(target), dtype=int)
    if ok.any():
        idx = tree.query_radius(np.radians(tl[ok]), r=radius_km / 6371.0)
        r = np.array([(py[i].sum() + 1) / (len(i) + 2) for i in idx]); c = np.array([len(i) for i in idx])
        rate[ok] = r; n[ok] = c
    return pd.Series(rate, index=target.index), pd.Series(n, index=target.index)


# ---- build panel ----------------------------------------------------------------------------------------
rows = []
ra_sorted = ra.sort_values("date") if len(ra) else ra
for T in SNAPSHOTS:
    t0 = pd.Timestamp(year=T, month=1, day=1); t1 = pd.Timestamp(year=T + HORIZON, month=1, day=1)
    u = s[(s.open_date < t0) & (s.closure_date.isna() | (s.closure_date >= t0))].copy()
    u["T"] = T
    u["y"] = (u.closure_date.notna() & (u.closure_date < t1)).astype(int)
    u["ttc"] = np.where(u.y == 1, (u.closure_date - t0).dt.days / 365.25, np.nan)
    u["closed_ever"] = u.closure_date.notna().astype(int)
    u["years_open"] = (t0 - u.open_date).dt.days / 365.25
    hb = sh[sh.date < t0]
    last = hb.sort_values("date").groupby("gid").status.last()
    u["status_at_T"] = last.reindex(u.index).fillna("UNKNOWN").str.upper().str.slice(0, 40)
    u["n_status_changes"] = hb.groupby("gid").size().reindex(u.index).fillna(0)
    if len(ra):
        rb = ra_sorted[ra_sorted.date < t0]
        u["n_regact"] = rb.groupby("gid").size().reindex(u.index).fillna(0)
        u["n_regact_3y"] = rb[rb.date >= t0 - pd.DateOffset(years=3)].groupby("gid").size().reindex(u.index).fillna(0)
        u["yrs_since_regact"] = (t0 - rb.groupby("gid").date.max().reindex(u.index)).dt.days / 365.25
        txt = rb.groupby("gid").text.apply(lambda x: " ".join(x.tail(12)))
        u["regact_text"] = txt.reindex(u.index).fillna("")
    else:
        u["n_regact"] = 0; u["n_regact_3y"] = 0; u["yrs_since_regact"] = np.nan; u["regact_text"] = ""
    u["text_all"] = (u.regact_text + " " + u.site_history.fillna("")).str.lower().str.slice(0, 5000)
    u = u.join(contam_tok).join(media_tok)
    ef = edf_features(T)
    u = u.join(ef, how="left")
    u["has_edf"] = u.index.isin(ef.index).astype(int)
    if len(geo):
        u = u.join(geo.set_index("gid"), how="left")
    if len(dtw):
        d = dtw[dtw.year < T].groupby("gid").agg(dtw_med_before=("dtw_med", "median"), dtw_n_before=("n_meas", "sum"))
        u = u.join(d, how="left")
    u["nb_rate"], u["nb_n"] = neighbour_rate(u, T)
    log(f"T={T}: {len(u):,} open sites, closed within {HORIZON}y: {u.y.mean():.3f}, with EDF: {u.has_edf.mean():.2f}")
    rows.append(u.reset_index())

panel = pd.concat(rows, ignore_index=True)
drop = ["name", "city", "status", "status_date", "contaminants", "media", "site_history", "begin_date", "closed_flag", "regact_text"]
panel = panel.drop(columns=[c for c in drop if c in panel.columns])
panel.to_pickle(os.path.join(WORK, "panel.pkl"))
log(f"panel: {len(panel):,} rows x {panel.shape[1]} cols; sites {panel.gid.nunique():,}")
