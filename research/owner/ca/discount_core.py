"""Shared pieces of the assessor-roll discount test: GeoTracker case dates, treatment at each sale, FE OLS, the
hedonic model. Used by discount.py (LA County) and discount_other.py (San Francisco, Alameda)."""
import os

import numpy as np
import pandas as pd
from sklearn.neighbors import BallTree

from common import WORK

R = 6371.0
CLEAN = r"LUST|CLEANUP PROGRAM|MILITARY"


def case_dates():
    """Open and closure dates per GeoTracker case, the same rules as build_panel.py."""
    sites = pd.read_pickle(os.path.join(WORK, "sites.pkl"))
    sh = pd.read_pickle(os.path.join(WORK, "status_history.pkl"))
    sh["is_closed"] = sh.status.str.upper().str.startswith("COMPLETED") | sh.status.str.upper().str.contains("CASE CLOSED")
    ra = pd.read_pickle(os.path.join(WORK, "regact.pkl"))
    s = sites.set_index("gid")
    od = pd.concat([sh.groupby("gid").date.min().rename("a"), ra.groupby("gid").date.min().rename("b"), s.begin_date.rename("c")], axis=1).min(axis=1)
    s["open_date"] = od.reindex(s.index).fillna(s.status_date.where(~s.closed_flag))
    s["closure_date"] = sh[sh.is_closed].groupby("gid").date.min().reindex(s.index).fillna(s.status_date.where(s.closed_flag))
    s["clean"] = s.case_type.str.upper().str.contains(CLEAN, regex=True, na=False)
    s["ctype"] = np.where(s.case_type.str.upper().str.contains("LUST", na=False), "LUST",
                          np.where(s.case_type.str.upper().str.contains("CLEANUP PROGRAM", na=False), "Cleanup Program", "Military/other"))
    return s


def assign(ev, cp, parcels, radius_km=1.5):
    """Label each sale in ev (AIN, rec, CENTER_LAT, CENTER_LON) as open / closed_* / later / control.
    cp: AIN, gid, clean, ctype, open_date, closure_date for every matched case; parcels: AIN, CENTER_LAT, CENTER_LON."""
    any_case = set(cp.AIN)
    cc = cp[cp.clean].dropna(subset=["open_date"])
    m = ev[["AIN", "rec"]].reset_index().merge(cc[["AIN", "gid", "ctype", "open_date", "closure_date"]], on="AIN")
    m["open_at"] = (m.open_date <= m.rec) & (m.closure_date.isna() | (m.closure_date > m.rec))
    m["yrs_closed"] = (m.rec - m.closure_date).dt.days / 365.25
    m["later"] = m.open_date > m.rec
    m["rank"] = np.select([m.open_at, m.yrs_closed >= 0, m.later], [0, 1, 2], 3)
    m = m.sort_values(["index", "rank", "yrs_closed"]).drop_duplicates("index")
    lab = np.select([m.open_at, m.yrs_closed.between(0, 2), m.yrs_closed.between(2, 5, inclusive="right"), m.yrs_closed > 5, m.later],
                    ["open", "closed_0_2", "closed_2_5", "closed_5p", "later"], "other")
    ix = m["index"].to_numpy()
    ev = ev.copy()
    ev["treat"] = pd.Series(lab, index=ix).reindex(ev.index)
    ev["gid"] = pd.Series(m.gid.to_numpy(), index=ix).reindex(ev.index)
    ev["ctype"] = pd.Series(m.ctype.to_numpy(), index=ix).reindex(ev.index)
    mp = parcels[parcels.AIN.isin(cc.AIN)].drop_duplicates("AIN").dropna(subset=["CENTER_LAT"])
    tree = BallTree(np.radians(mp[["CENTER_LAT", "CENTER_LON"]].to_numpy(float)), metric="haversine")
    cand = ev[ev.treat.isna() & ~ev.AIN.isin(any_case) & ev.CENTER_LAT.notna()]
    d, _ = tree.query(np.radians(cand[["CENTER_LAT", "CENTER_LON"]].to_numpy(float)), k=1)
    near = pd.Series(d[:, 0] * R <= radius_km, index=cand.index)
    ev.loc[near[near].index, "treat"] = "control"
    return ev[ev.treat.notna() & (ev.treat != "other")].copy()


# ---- FE OLS -------------------------------------------------------------------------------------------------
def demean(X, fes, iters=50, tol=1e-8):
    X = X.copy()
    codes = [pd.factorize(f)[0] for f in fes]
    for _ in range(iters):
        delta = 0.0
        for c in codes:
            cnt = np.bincount(c)
            for j in range(X.shape[1]):
                mu = np.bincount(c, X[:, j]) / cnt
                X[:, j] -= mu[c]
                delta = max(delta, np.abs(mu).max())
        if delta < tol:
            break
    return X


def fe_ols(df, y, xs, fes, cluster):
    d = df.dropna(subset=[y] + xs).copy()
    M = demean(d[[y] + xs].to_numpy(float), [d[f].astype(str).fillna("na").to_numpy() for f in fes])
    Y, X = M[:, 0], M[:, 1:]
    keep = X.std(axis=0) > 1e-12
    X = X[:, keep]; names = [x for x, k in zip(xs, keep) if k]
    XtX_inv = np.linalg.pinv(X.T @ X)
    b = XtX_inv @ X.T @ Y
    e = Y - X @ b
    cl = pd.factorize(d[cluster].astype(str).fillna("na"))[0]
    S = np.zeros((X.shape[1], X.shape[1]))
    Xe = X * e[:, None]
    G = np.zeros((cl.max() + 1, X.shape[1]))
    np.add.at(G, cl, Xe)
    S = G.T @ G
    ng, n, k = cl.max() + 1, len(Y), X.shape[1]
    V = XtX_inv @ S @ XtX_inv * (ng / (ng - 1)) * ((n - 1) / (n - k))
    se = np.sqrt(np.diag(V))
    return pd.DataFrame({"coef": b, "se": se}, index=names), len(d)


TREATS = ["open", "closed_0_2", "closed_2_5", "closed_5p", "later"]


def hedonic(df, y="lp"):
    d = df.copy()
    for t in TREATS:
        d[f"t_{t}"] = (d.treat == t).astype(float)
    xs = [f"t_{t}" for t in TREATS if d[f"t_{t}"].sum() >= 5] + ["llot", "lsq"]
    res, n = fe_ols(d, y, xs, ["UseCode", "sale_year", "cell", "yb"], "cell")
    out = []
    for t in TREATS:
        k = f"t_{t}"
        nn = int(d.loc[d[[y, "llot", "lsq"]].notna().all(axis=1), k].sum())
        if k in res.index:
            b, se = res.loc[k, "coef"], res.loc[k, "se"]
            out.append({"treatment": t, "n": nn, "coef": round(b, 3), "se": round(se, 4), "pct": round(100 * (np.exp(b) - 1), 1),
                        "ci95_pct": f"[{100*(np.exp(b-1.96*se)-1):.1f}, {100*(np.exp(b+1.96*se)-1):.1f}]"})
        else:
            out.append({"treatment": t, "n": nn, "coef": None, "se": None, "pct": None, "ci95_pct": ""})
    return pd.DataFrame(out), n

