"""Per-site features from the county geo files (GeoXY, GeoZ, GeoWell, FieldPoints) -> work/geo_static.pkl
and work/geo_dtw_year.pkl (gid, year, dtw_med, n_meas) for time-aware use.

geo_static per gid: n_fpt, n_wells, n_borings, depth_max, depth_med, spread_km (bounding-box diagonal of
field points), first_year, last_year. Column names are detected at run time.
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

parts = []
if len(fp):
    parts.append(fp.groupby("gid").agg(
        n_fpt=("fpt", "nunique"),
        n_wells=("cls", lambda s: int(s.str.contains(r"MW|WELL|EW|PZ|PIEZ", regex=True).sum())),
        n_borings=("cls", lambda s: int(s.str.contains(r"SB|BOR|HP|DP|CPT", regex=True).sum()))))
if len(well):
    parts.append(well.groupby("gid").agg(depth_max=("depth", "max"), depth_med=("depth", "median"), n_well_rows=("fpt", "nunique")))
if len(xy):
    bb = xy.dropna(subset=["lat", "lon"]).groupby("gid").agg(lat0=("lat", "min"), lat1=("lat", "max"), lon0=("lon", "min"), lon1=("lon", "max"), n_xy=("fpt", "nunique"))
    bb["spread_km"] = haversine_km(bb.lat0.to_numpy(), bb.lon0.to_numpy(), bb.lat1.to_numpy(), bb.lon1.to_numpy())
    parts.append(bb[["spread_km", "n_xy"]])
dates = pd.concat([d[["gid", "date"]] for d in (xy, zz, well) if len(d) and "date" in d], ignore_index=True) if any(len(d) for d in (xy, zz, well)) else pd.DataFrame(columns=["gid", "date"])
if len(dates):
    dates = dates.dropna()
    parts.append(dates.groupby("gid").date.agg(first_year=lambda s: s.min().year, last_year=lambda s: s.max().year))
if len(zz):
    parts.append(zz.groupby("gid").agg(dtw_med_all=("dtw", "median")))
geo = pd.concat(parts, axis=1) if parts else pd.DataFrame()
geo.index.name = "gid"
geo = geo.reset_index()
geo.to_pickle(os.path.join(WORK, "geo_static.pkl"))
if len(zz):
    z = zz.dropna(subset=["date", "dtw"]).copy()
    z["year"] = z.date.dt.year
    z.groupby(["gid", "year"]).agg(dtw_med=("dtw", "median"), n_meas=("dtw", "size")).reset_index().to_pickle(os.path.join(WORK, "geo_dtw_year.pkl"))
else:
    pd.DataFrame(columns=["gid", "year", "dtw_med", "n_meas"]).to_pickle(os.path.join(WORK, "geo_dtw_year.pkl"))
log(f"geo_static: {len(geo):,} sites, columns {list(geo.columns)}")
