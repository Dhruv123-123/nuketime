"""The discount test in two more counties, and the industrial-class (Cleanup Program) pool across counties.

San Francisco: Assessor Historical Secured Property Tax Rolls 2007-2025 (data.sf.gov wv5m-vpq2, fetch_sf_roll.py).
  Sale event = a roll year in which current_sales_date moves forward (sale year >= roll year - 2); price = assessed
  land + improvement value that roll year. Same screens as LA.
Alameda: current parcel layer only (Land, Imps, LatestDocumentDate), so one observation per parcel: the latest
  recorded document since 2006, price = (Land + Imps) / 1.02^(2025 - document year) (Prop 13's 2% cap undone).
  The latest document is not always a sale, so this is the roughest of the three.
GeoTracker cases are matched to the nearest parcel point (SF) or the polygon centroid (Alameda) within 40 m, or within
150 m when the street number and name match. Then discount_core.assign / hedonic, as for LA.
Appends an "Other counties" section to results/discount.md.
"""
import json
import os
import re
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd
from sklearn.neighbors import BallTree

from common import DATA, RESULTS, WORK, log
from discount_core import R, assign, case_dates, hedonic

s = case_dates()
sites = pd.read_pickle(os.path.join(WORK, "sites.pkl"))
raw_addr = None


def addr_table():
    from common import find_files, read_table_from_zip
    t = read_table_from_zip(find_files("statewide", r"GeoTrackerDownload\.zip$")[0], member="sites.txt")
    t["gid"] = t.GLOBAL_ID.str.strip()
    t["num"] = t.STREET_NUMBER.fillna("").astype(str).str.extract(r"(\d+)")[0]
    t["street"] = t.STREET_NAME.fillna("").astype(str).str.upper().str.extract(r"([A-Z0-9]+)")[0]
    return t.drop_duplicates("gid").set_index("gid")[["num", "street"]]


def match_cases(parcels, county_names, parcel_num, parcel_street):
    """parcels: AIN, CENTER_LAT, CENTER_LON plus address columns. Returns cp (AIN, gid, match) for GeoTracker cases."""
    global raw_addr
    if raw_addr is None:
        raw_addr = addr_table()
    c = sites[sites.county.str.upper().str.replace(" ", "").isin(county_names)].dropna(subset=["lat", "lon"]).join(raw_addr, on="gid")
    pp = parcels.dropna(subset=["CENTER_LAT"]).reset_index(drop=True)
    tree = BallTree(np.radians(pp[["CENTER_LAT", "CENTER_LON"]].to_numpy(float)), metric="haversine")
    idx, dist = tree.query_radius(np.radians(c[["lat", "lon"]].to_numpy(float)), r=0.150 / R, return_distance=True, sort_results=True)
    rows = []
    for (gid, num, street), ii, dd in zip(c[["gid", "num", "street"]].itertuples(index=False), idx, dist):
        pick = None
        for i, d in zip(ii, dd):
            a_ok = isinstance(num, str) and num == pp.at[i, parcel_num] and isinstance(street, str) and street == pp.at[i, parcel_street]
            if a_ok:
                pick = (i, "address"); break
        if pick is None and len(ii) and dd[0] * R <= 0.040:
            pick = (ii[0], "nearest<40m")
        if pick:
            rows.append({"gid": gid, "AIN": pp.at[pick[0], "AIN"], "match": pick[1]})
    cp = pd.DataFrame(rows).join(s[["case_type", "open_date", "closure_date", "status", "clean", "ctype"]], on="gid")
    return cp, len(c)


def finish(ev):
    ev = ev.copy()
    ev["sale_year"] = ev.rec.dt.year
    ev["lp"] = np.log(ev.price)
    ev["lpl"] = np.log(ev.land.where(ev.land > 0))
    ev["llot"] = np.log(ev.lot_sqft.where(ev.lot_sqft > 100))
    ev["lsq"] = np.log1p(ev.SQFTmain.fillna(0))
    ev["yb"] = pd.cut(ev.YearBuilt.where(ev.YearBuilt > 1800), [1800, 1940, 1960, 1980, 2000, 2030], labels=False).fillna(-1).astype(int)
    ev["cell"] = (np.floor(ev.CENTER_LAT / 0.009)).astype("Int64").astype(str) + "_" + (np.floor(ev.CENTER_LON / 0.0109)).astype("Int64").astype(str)
    return ev


# ---- San Francisco ------------------------------------------------------------------------------------------
sf = pd.read_pickle(os.path.join(DATA, "sf_roll.pkl"))
sf = sf.rename(columns={"parcel_number": "AIN", "lat": "CENTER_LAT", "lon": "CENTER_LON", "property_class_code": "UseCode"})
sf["RollYear"] = pd.to_numeric(sf.closed_roll_year, errors="coerce")
for c in ("assessed_land_value", "assessed_improvement_value", "lot_area", "property_area", "year_property_built", "CENTER_LAT", "CENTER_LON"):
    sf[c] = pd.to_numeric(sf[c], errors="coerce")
sf["rec"] = pd.to_datetime(sf.current_sales_date, errors="coerce")
sf["total"] = sf.assessed_land_value + sf.assessed_improvement_value
sf["cls"] = np.select([sf.use_code.isin(["COMM", "COMR", "COMO", "COMH"]), sf.use_code == "IND"], ["Commercial", "Industrial"], "Other")
sf = sf.dropna(subset=["AIN", "RollYear"]).drop_duplicates(["AIN", "RollYear"]).sort_values(["AIN", "RollYear"])
g = sf.groupby("AIN")
sf["prev_rec"], sf["prev_total"], sf["prev_year"] = g.rec.shift(), g.total.shift(), g.RollYear.shift()
e = sf[(sf.prev_year == sf.RollYear - 1) & (sf.rec > sf.prev_rec) & (sf.rec.dt.year >= sf.RollYear - 2)]
e = e[(e.total > 0) & (e.total >= 0.1 * e.prev_total) & (e.total != e.prev_total) & (e.cls != "Other")].copy()
e = e.rename(columns={"total": "price", "assessed_land_value": "land", "lot_area": "lot_sqft", "property_area": "SQFTmain", "year_property_built": "YearBuilt"})
sfp = sf.drop_duplicates("AIN", keep="last").copy()
sfp["pnum"] = sfp.property_location.fillna("").str.extract(r"^\S+\s+0*(\d+)")[0]
sfp["pstreet"] = sfp.property_location.fillna("").str.extract(r"^\S+\s+\S+\s+([A-Z0-9]+)")[0]
cp_sf, nc_sf = match_cases(sfp, {"SANFRANCISCO"}, "pnum", "pstreet")
ev_sf = finish(assign(e, cp_sf, sfp[["AIN", "CENTER_LAT", "CENTER_LON"]]))
log(f"SF: events {len(e):,}; cases {nc_sf:,}, matched {cp_sf.gid.nunique():,} ({cp_sf.match.value_counts().to_dict()}); treat {ev_sf.treat.value_counts().to_dict()}")

# ---- Alameda ----------------------------------------------------------------------------------------------
AL = "https://services5.arcgis.com/ROBnTHSNjoZ2Wm1P/arcgis/rest/services/Parcels/FeatureServer/0/query"
al_path = os.path.join(DATA, "alameda_parcels.pkl")


def al_get(params, tries=6):
    body = urllib.parse.urlencode(params).encode()
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(AL, data=body), timeout=180) as r:
                d = json.loads(r.read())
            if "error" in d:
                raise IOError(d["error"])
            return d
        except Exception:  # noqa: BLE001
            if i == tries - 1:
                raise
            time.sleep(2 ** i)


def al_chunk(lo):
    d = al_get({"where": f"OBJECTID>={lo} AND OBJECTID<{lo + 4000} AND (UseCode LIKE '3%' OR UseCode LIKE '4%')",
                "outFields": "APN,UseCode,Land,Imps,LatestDocumentDate,Shape__Area,CENTROID_X,CENTROID_Y,SitusStreetNumber,SitusStreetName",
                "returnGeometry": "false", "f": "json"})
    return [x["attributes"] for x in d.get("features", [])]


if not os.path.exists(al_path):
    mx = al_get({"where": "1=1", "outStatistics": json.dumps([{"statisticType": "max", "onStatisticField": "OBJECTID", "outStatisticFieldName": "mx"}]),
                 "f": "json"})["features"][0]["attributes"]["mx"]
    with ThreadPoolExecutor(16) as ex:
        parts = list(ex.map(al_chunk, range(0, mx + 1, 4000)))
    pd.DataFrame([x for p in parts for x in p]).to_pickle(al_path)
al = pd.read_pickle(al_path).rename(columns={"APN": "AIN"})
x, y = al.CENTROID_X.astype(float), al.CENTROID_Y.astype(float)  # web mercator
al["CENTER_LON"] = np.degrees(x / 6378137.0)
al["CENTER_LAT"] = np.degrees(2 * np.arctan(np.exp(y / 6378137.0)) - np.pi / 2)
al["lot_sqft"] = al.Shape__Area * np.cos(np.radians(al.CENTER_LAT)) ** 2 * 10.7639  # mercator area -> true sq ft
al["rec"] = pd.to_datetime(al.LatestDocumentDate, unit="ms", errors="coerce")
al["land"] = al.Land.astype(float)
al["price"] = (al.Land + al.Imps).astype(float) / 1.02 ** (2025 - al.rec.dt.year)
al["UseCodeDescChar1"] = np.where(al.UseCode.str.startswith("3"), "Commercial", "Industrial")
al["SQFTmain"], al["YearBuilt"] = np.nan, np.nan
al["pnum"] = al.SitusStreetNumber.fillna("").astype(str).str.extract(r"(\d+)")[0]
al["pstreet"] = al.SitusStreetName.fillna("").astype(str).str.upper().str.extract(r"([A-Z0-9]+)")[0]
ea = al[(al.rec.dt.year >= 2006) & (al.price > 0)].copy()
cp_al, nc_al = match_cases(al, {"ALAMEDA"}, "pnum", "pstreet")
ev_al = finish(assign(ea, cp_al, al[["AIN", "CENTER_LAT", "CENTER_LON"]]))
log(f"Alameda: parcels {len(al):,}, latest-document events since 2006 {len(ea):,}; cases {nc_al:,}, matched {cp_al.gid.nunique():,} "
    f"({cp_al.match.value_counts().to_dict()}); treat {ev_al.treat.value_counts().to_dict()}")

# ---- models and pool ----------------------------------------------------------------------------------------
la = pd.read_pickle(os.path.join(WORK, "la_hedonic.pkl"))
res = {"Los Angeles": {"all": la["hedonic"], **la["by_type"]}}
L = ["\n## Other counties (San Francisco, Alameda) and the industrial-class pool\n",
     f"San Francisco: {len(ev_sf):,} commercial/industrial sale events 2007-2025; {cp_sf.gid.nunique():,} of {nc_sf:,} cases matched to a parcel "
     f"({cp_sf.match.value_counts().to_dict()}). Alameda: {len(ev_al):,} parcels whose latest document is 2006 or later (one cross-section, "
     f"price = current assessed value deflated at 2%/yr to the document year); {cp_al.gid.nunique():,} of {nc_al:,} cases matched.\n"]
for name, ev in (("San Francisco", ev_sf), ("Alameda", ev_al)):
    res[name] = {}
    h, n = hedonic(ev)
    res[name]["all"] = h
    L.append(f"\n### {name}, all case types (n = {n:,})\n\n" + h.drop(columns=["se"]).to_markdown(index=False))
    for ct in ("LUST", "Cleanup Program"):
        sub = ev[(ev.treat == "control") | (ev.ctype == ct)]
        if (sub.treat != "control").sum() < 20:
            continue
        hh, nn = hedonic(sub)
        res[name][ct] = hh
        L.append(f"\n{name}, {ct} (n = {nn:,}): " + ", ".join(f"{r.treatment} {r.pct}% {r.ci95_pct} (n={r.n})" for r in hh.itertuples()))
    ppsf = ev.assign(ppsf=ev.price / ev.lot_sqft.where(ev.lot_sqft > 100)).dropna(subset=["ppsf"])
    L.append(f"\n{name}, median $ per lot sq ft by treatment: " + ", ".join(f"{k} {v:.0f}" for k, v in ppsf.groupby("treat").ppsf.median().items()))

pool_rows = []
for ct in ("Cleanup Program", "LUST", "all"):
    for t in ("open", "closed_0_2", "closed_2_5", "closed_5p"):
        bs, ws, ns, parts = [], [], 0, []
        for cty, d in res.items():
            h = d.get(ct)
            if h is None:
                continue
            r = h.set_index("treatment").loc[t]
            se = r.get("se")
            if se is None or pd.isna(r.coef) or pd.isna(se) or se <= 0:
                continue
            bs.append(r.coef); ws.append(1 / se ** 2); ns += int(r.n); parts.append(f"{cty} {100*(np.exp(r.coef)-1):.1f}% (n={int(r.n)})")
        if bs:
            b = np.sum(np.array(bs) * ws) / np.sum(ws); se = np.sqrt(1 / np.sum(ws))
            pool_rows.append({"case class": ct, "treatment": t, "n": ns, "pooled %": round(100 * (np.exp(b) - 1), 1),
                              "95% CI": f"[{100*(np.exp(b-1.96*se)-1):.1f}, {100*(np.exp(b+1.96*se)-1):.1f}]", "by county": "; ".join(parts)})
pool = pd.DataFrame(pool_rows)
L.append("\n### Pooled across counties (inverse-variance weights on the M1 coefficients)\n\n" + pool.to_markdown(index=False))
pool.to_csv(os.path.join(RESULTS, "discount_pool.csv"), index=False)
md = open(os.path.join(RESULTS, "discount.md")).read()
md = md.split("\n## Other counties")[0].rstrip() + "\n" + "\n".join(L) + "\n"
open(os.path.join(RESULTS, "discount.md"), "w").write(md)
log("\n".join(L))
