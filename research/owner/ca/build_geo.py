"""Per-site features from the county geo files (GeoXY, GeoZ, GeoWell, FieldPoints) -> work/geo_fpt.pkl
(gid, fpt, first_date, depth, lat, lon, cls, is_well, is_boring) and work/geo_dtw_year.pkl (gid, year, dtw_med,
n_meas). Both are dated so build_panel.py aggregates them using only records before each snapshot.
Column names are detected at run time.
"""
import os
import re

import numpy as np
import pandas as pd

from common import WORK, find_files, haversine_km, log, norm_cols, pick, read_table_from_zip, to_date, to_num

xy, zz, well, fp = [], [], [], []
for p in find_files("geo_by_county", r"\.zip$"):
    if os.path.getsize(p) < 300:
        continue
    kind = re.search(r"(GeoXY|GeoZ|GeoWell|FieldPoints)", os.path.basename(p), re.I)
    if not kind:
        continue
    kind = kind.group(1).lower()
    try:
        t = norm_cols(read_table_from_zip(p))
    except Exception as e:  # noqa: BLE001
        log(f"  {os.path.basename(p)}: {e}"); continue
    g = pick(t.columns, r"GLOBAL")
    if g is None:
        continue
    f = pick(t.columns, r"FIELD_?PT_?NAME", r"FIELD_?PT", r"FIELD_?POINT")
    base = pd.DataFrame({"gid": t[g].astype(str).str.strip(), "fpt": t[f].astype(str).str.strip() if f else ""})
    if kind == "geoxy":
        base["lat"] = to_num(t[pick(t.columns, r"^LAT")]) if pick(t.columns, r"^LAT") else np.nan
        base["lon"] = to_num(t[pick(t.columns, r"^LON")]) if pick(t.columns, r"^LON") else np.nan
        d = pick(t.columns, r"DATE")
        base["date"] = to_date(t[d]) if d else pd.NaT
        xy.append(base)
    elif kind == "geoz":
        d = pick(t.columns, r"MEAS.*DATE", r"GW.*DATE", r"DATE")
        base["date"] = to_date(t[d]) if d else pd.NaT
        c = pick(t.columns, r"^DTW", r"DEPTH_?TO_?W", r"DEPTH")
        base["dtw"] = to_num(t[c]) if c else np.nan
        zz.append(base)
    elif kind == "geowell":
        c = pick(t.columns, r"TOTAL_?DEPTH", r"WELL_?DEPTH", r"DEPTH")
        base["depth"] = to_num(t[c]) if c else np.nan
        d = pick(t.columns, r"INSTALL.*DATE", r"DRILL.*DATE", r"DATE")
        base["date"] = to_date(t[d]) if d else pd.NaT
        well.append(base)
    else:
        c = pick(t.columns, r"CLASS", r"TYPE")
        base["cls"] = t[c].astype(str).str.upper().str.strip() if c else ""
        fp.append(base)

xy = pd.concat(xy, ignore_index=True) if xy else pd.DataFrame(columns=["gid", "fpt", "lat", "lon", "date"])
zz = pd.concat(zz, ignore_index=True) if zz else pd.DataFrame(columns=["gid", "fpt", "date", "dtw"])
well = pd.concat(well, ignore_index=True) if well else pd.DataFrame(columns=["gid", "fpt", "depth", "date"])
fp = pd.concat(fp, ignore_index=True) if fp else pd.DataFrame(columns=["gid", "fpt", "cls"])
log(f"geoxy {len(xy):,}  geoz {len(zz):,}  geowell {len(well):,}  fieldpoints {len(fp):,}")

# One row per (gid, field point) with the first date the point appears in any dated geo table, so that
# build_panel.py can count only wells/borings that existed before each snapshot T. (An all-time count leaks
# the future: sampling and new wells stop when a case closes.) Undated points are dropped.
keys = ["gid", "fpt"]
fd = pd.concat([d[keys + ["date"]] for d in (xy, zz, well) if len(d)], ignore_index=True).dropna(subset=["date"])
fd = fd[(fd.date.dt.year >= 1970) & (fd.date.dt.year <= 2026)]
g = fd.groupby(keys).date.min().rename("first_date").to_frame()
if len(well):
    g = g.join(well.groupby(keys).depth.max())
if len(xy):
    g = g.join(xy.dropna(subset=["lat", "lon"]).groupby(keys)[["lat", "lon"]].median())
if len(fp):
    g = g.join(fp.drop_duplicates(keys).set_index(keys).cls)
for c in ("depth", "lat", "lon", "cls"):
    if c not in g:
        g[c] = np.nan if c != "cls" else ""
g["cls"] = g.cls.fillna("").astype(str)
g["is_well"] = g.cls.str.contains(r"MW|WELL|EW|PZ|PIEZ", regex=True).astype(int)
g["is_boring"] = g.cls.str.contains(r"SB|BOR|HP|DP|CPT", regex=True).astype(int)
geo = g.reset_index()
geo.to_pickle(os.path.join(WORK, "geo_fpt.pkl"))
if len(zz):
    z = zz.dropna(subset=["date", "dtw"]).copy()
    z["year"] = z.date.dt.year
    z.groupby(["gid", "year"]).agg(dtw_med=("dtw", "median"), n_meas=("dtw", "size")).reset_index().to_pickle(os.path.join(WORK, "geo_dtw_year.pkl"))
else:
    pd.DataFrame(columns=["gid", "year", "dtw_med", "n_meas"]).to_pickle(os.path.join(WORK, "geo_dtw_year.pkl"))
log(f"geo_fpt: {len(geo):,} dated field points at {geo.gid.nunique():,} sites")
