"""Stream every county EDF zip (lab results) into compact per-year aggregates, without extracting.

For each county writes work/edf/{County}_agg.pkl with one row per
    (gid, analyte, mclass, year): n, n_det, max_det, sumlog_det, n_fpt, n_fpt_det
restricted to the analytes in common.ANALYTES, and work/edf/{County}_all.pkl with one row per (gid, year):
    n_samples, n_fpt, n_params  (over all parameters, not only the mapped ones).
mclass is 'water' (MATRIX starting with W), 'soil' (S but not SG), or 'other'. Values are normalised to
ug/L (water) and mg/kg (soil); rows with unknown units keep their counts but no value.

Runs counties in parallel (CA_JOBS, default 3). Memory is bounded by the chunk size.
Usage: python build_edf.py [--counties Napa,Alpine] [--chunk 400000]
"""
import argparse
import os
import re
from multiprocessing import Pool

import numpy as np
import pandas as pd

from common import CODE_TO_ANALYTE, SOIL_UNIT_FACTOR, WATER_UNIT_FACTOR, WORK, find_files, log, pick, read_table_from_zip

OUT = os.path.join(WORK, "edf")
os.makedirs(OUT, exist_ok=True)
NONDETECT = {"<", "ND", "U", "<=", "NA", "N/A", "<RL", "<DL"}


def county_of(path):
    return re.sub(r"[_ -]?EDF\.zip$", "", os.path.basename(path), flags=re.I)


def one_county(args):
    path, chunk = args
    c = county_of(path)
    done = os.path.join(OUT, f"{c}_agg.pkl")
    if os.path.exists(done):
        return c, "cached"
    try:
        head = read_table_from_zip(path, nrows=5)
    except Exception as e:  # noqa: BLE001
        return c, f"unreadable: {e}"
    cols = list(head.columns)
    col = {
        "gid": pick(cols, r"^GLOBAL_?ID$", r"GLOBAL"),
        "fpt": pick(cols, r"FIELD_?PT_?NAME", r"FIELD_?PT", r"FIELD_?POINT"),
        "date": pick(cols, r"^LOGDATE$", r"LOG_?DATE", r"SAMP.*DATE", r"DATE"),
        "matrix": pick(cols, r"^MATRIX$", r"MATRIX"),
        "par": pick(cols, r"^PARLABEL$", r"PAR_?LABEL", r"PARAM"),
        "val": pick(cols, r"^PARVAL$", r"PAR_?VAL", r"RESULT"),
        "vq": pick(cols, r"^PARVQ$", r"PAR_?VQ", r"QUALIF"),
        "units": pick(cols, r"^UNITS?$", r"UNIT"),
    }
    missing = [k for k, v in col.items() if v is None and k in ("gid", "date", "par", "val")]
    if missing:
        return c, f"missing columns {missing}; header {cols[:30]}"
    use = [v for v in col.values() if v is not None]
    aggs, pairs, alls, allp = [], [], [], []
    units_seen = {}
    n_rows = 0
    for ch in read_table_from_zip(path, chunksize=chunk, usecols=use):
        n_rows += len(ch)
        d = pd.DataFrame({
            "gid": ch[col["gid"]].str.strip(),
            "fpt": ch[col["fpt"]].str.strip() if col["fpt"] else "",
            "par": ch[col["par"]].str.strip().str.upper(),
        })
        yr = pd.to_datetime(ch[col["date"]].str.slice(0, 10), errors="coerce", format="mixed").dt.year
        d["year"] = yr
        d = d[d.year.notna() & d.gid.notna()]
        d["year"] = d.year.astype(int)
        # all-parameter counts per (gid, year)
        alls.append(d.groupby(["gid", "year"]).size().rename("n_samples").reset_index())
        # field point / parameter names hashed to int64 so the distinct-tuple list stays small for Los Angeles
        allp.append(pd.DataFrame({"gid": d.gid, "year": d.year,
                                  "fpt": pd.util.hash_array(d.fpt.fillna("").to_numpy(dtype=object)),
                                  "par": pd.util.hash_array(d.par.fillna("").to_numpy(dtype=object))}).drop_duplicates())
        # mapped analytes only
        d["analyte"] = d.par.map(CODE_TO_ANALYTE)
        d = d[d.analyte.notna()].copy()
        if d.empty:
            continue
        mat = ch.loc[d.index, col["matrix"]].str.strip().str.upper() if col["matrix"] else pd.Series("W", index=d.index)
        d["mclass"] = np.where(mat.str.startswith("W"), "water", np.where(mat.str.startswith("SG"), "other",
                               np.where(mat.str.startswith("S"), "soil", "other")))
        val = pd.to_numeric(ch.loc[d.index, col["val"]].str.replace(",", ""), errors="coerce")
        vq = ch.loc[d.index, col["vq"]].fillna("").str.strip().str.upper() if col["vq"] else pd.Series("=", index=d.index)
        un = ch.loc[d.index, col["units"]].fillna("").str.strip().str.upper() if col["units"] else pd.Series("UG/L", index=d.index)
        for u, k in un.value_counts().items():
            units_seen[u] = units_seen.get(u, 0) + int(k)
        fac = np.where(d.mclass == "water", un.map(WATER_UNIT_FACTOR), un.map(SOIL_UNIT_FACTOR)).astype(float)
        d["v"] = val * fac
        d["det"] = (~vq.isin(NONDETECT)) & (d.v > 0)
        d["vdet"] = d.v.where(d.det)
        d["logv"] = np.log10(d.vdet)
        key = ["gid", "analyte", "mclass", "year"]
        a = d.groupby(key).agg(n=("v", "size"), n_det=("det", "sum"), max_det=("vdet", "max"), sumlog_det=("logv", "sum")).reset_index()
        aggs.append(a)
        pairs.append(d[key + ["fpt", "det"]].drop_duplicates())
    if not alls:
        return c, "no rows"
    allc = pd.concat(alls).groupby(["gid", "year"]).n_samples.sum().reset_index()
    ap = pd.concat(allp).drop_duplicates()
    allc = allc.merge(ap.groupby(["gid", "year"]).agg(n_fpt=("fpt", "nunique"), n_params=("par", "nunique")).reset_index(), how="left")
    allc.to_pickle(os.path.join(OUT, f"{c}_all.pkl"))
    if aggs:
        key = ["gid", "analyte", "mclass", "year"]
        a = pd.concat(aggs).groupby(key).agg(n=("n", "sum"), n_det=("n_det", "sum"), max_det=("max_det", "max"), sumlog_det=("sumlog_det", "sum")).reset_index()
        p = pd.concat(pairs).drop_duplicates()
        pf = p.groupby(key).agg(n_fpt=("fpt", "nunique")).reset_index()
        pfd = p[p.det].groupby(key).agg(n_fpt_det=("fpt", "nunique")).reset_index()
        a = a.merge(pf, how="left").merge(pfd, how="left").fillna({"n_fpt": 0, "n_fpt_det": 0})
        a["county"] = c
    else:
        a = pd.DataFrame(columns=["gid", "analyte", "mclass", "year", "n", "n_det", "max_det", "sumlog_det", "n_fpt", "n_fpt_det", "county"])
    a.to_pickle(done)
    pd.Series(units_seen).sort_values(ascending=False).to_csv(os.path.join(OUT, f"{c}_units.csv"))
    return c, f"{n_rows:,} rows -> {len(a):,} agg rows, {allc.gid.nunique():,} sites"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--counties", default="")
    ap.add_argument("--chunk", type=int, default=400_000)
    ap.add_argument("--jobs", type=int, default=int(os.environ.get("CA_JOBS", "3")))
    a = ap.parse_args()
    files = sorted(find_files("edf_by_county", r"EDF\.zip$"), key=os.path.getsize)
    if a.counties:
        want = set(a.counties.split(","))
        files = [f for f in files if county_of(f) in want]
    log(f"{len(files)} EDF files, {sum(os.path.getsize(f) for f in files)/1e9:.2f} GB")
    with Pool(a.jobs) as pool:
        for c, msg in pool.imap_unordered(one_county, [(f, a.chunk) for f in files]):
            log(f"  {c}: {msg}")
    aggs = [pd.read_pickle(os.path.join(OUT, f)) for f in os.listdir(OUT) if f.endswith("_agg.pkl")]
    alls = [pd.read_pickle(os.path.join(OUT, f)) for f in os.listdir(OUT) if f.endswith("_all.pkl")]
    pd.concat(aggs, ignore_index=True).to_pickle(os.path.join(WORK, "edf_agg.pkl"))
    pd.concat(alls, ignore_index=True).to_pickle(os.path.join(WORK, "edf_all.pkl"))
    log("wrote work/edf_agg.pkl and work/edf_all.pkl")
