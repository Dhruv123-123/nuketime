"""Proof-of-concept counts for the cofounder's two questions: are there enough BUILT-OUT industrial
contaminated sites (not gas stations), and is "infrastructure already on the parcel" real?

1. Industrial-class pool (Cleanup Program, Military Cleanup, Military UST) open at T=2019 and open today, within
   300 m / 1.5 km / 3 km of a >=115 kV and >=230 kV substation, by county.
2. results/top_industrial_2016.csv: top 100 non-LUST sites by p_F at T=2016 within 3 km of a >=230 kV substation.
3. Former and operating power plants (EIA-860, data/eia860/) joined to GeoTracker sites within 500 m and 1 km.
Writes results/builtout.md, results/builtout_pool_by_county.csv, results/top_industrial_2016.csv,
results/plants_x_geotracker.csv. Needs work/sites.pkl and work/pred_temporal.pkl (run backtest.py first).
"""
import os
import re
import zipfile

import numpy as np
import pandas as pd
from sklearn.neighbors import BallTree

from common import DATA, RESULTS, WORK, find_files, log, read_table_from_zip

R = 6371.0
IND = r"CLEANUP PROGRAM|MILITARY CLEANUP|MILITARY UST"

sites = pd.read_pickle(os.path.join(WORK, "sites.pkl"))
sites = sites[sites.lat.between(32, 42.5) & sites.lon.between(-125, -114)].copy()
raw = read_table_from_zip(find_files("statewide", r"GeoTrackerDownload\.zip$")[0], member="sites.txt")
raw["GLOBAL_ID"] = raw.GLOBAL_ID.str.strip()
addr = raw.drop_duplicates("GLOBAL_ID").set_index("GLOBAL_ID")[["BUSINESS_NAME", "STREET_NUMBER", "STREET_NAME", "CITY"]]
sites = sites.join(addr, on="gid")
sites["open_today"] = ~sites.status.fillna("").str.upper().str.startswith(("COMPLETED", "HISTORICAL", "NEVER", "INFORMATIONAL"))

sub = pd.read_csv(os.path.join(DATA, "ca_substations.csv"), encoding="utf-8-sig")
sub = sub[(sub.Type.astype(str).str.upper() == "SUBSTATION") & sub.Max_Voltage.notna()]


def nearest(df, kv):
    s = sub[sub.Max_Voltage >= kv]
    tree = BallTree(np.radians(s[["Lat", "Lon"]].to_numpy()), metric="haversine")
    d, i = tree.query(np.radians(df[["lat", "lon"]].to_numpy(dtype=float)), k=1)
    return d[:, 0] * R, s.Name.to_numpy()[i[:, 0]], s.Max_Voltage.to_numpy()[i[:, 0]]


for kv in (115, 230):
    sites[f"d{kv}"], sites[f"sub{kv}"], sites[f"kv{kv}"] = nearest(sites, kv)

pred = pd.read_pickle(os.path.join(WORK, "pred_temporal.pkl"))
ind_mask = sites.case_type.str.upper().str.contains(IND, regex=True, na=False)
p19 = set(pred.loc[pred["T"] == 2019, "gid"])
pools = {"open_at_2019": sites[ind_mask & sites.gid.isin(p19)], "open_today": sites[ind_mask & sites.open_today]}

# ---- 1. pool counts ---------------------------------------------------------------------------------------
L = ["# Built-out industrial sites near substations (California)\n",
     "Industrial class = GeoTracker case types Cleanup Program Site, Military Cleanup Site, Military UST Site "
     "(gas-station LUST cases excluded). Substations: CEC/HIFLD, Type SUBSTATION, by max kV. 300 m is the "
     "\"substation on or beside the parcel\" proxy (GeoTracker gives a point, not a parcel boundary).\n"]
tab, bycounty = [], []
for name, pool in pools.items():
    for kv in (115, 230):
        for r_km in (0.3, 1.5, 3.0):
            m = pool[f"d{kv}"] <= r_km
            tab.append({"pool": name, "kV": f">={kv}", "radius_km": r_km, "sites": int(m.sum()),
                        "cleanup_program": int((m & pool.case_type.str.contains("Cleanup Program")).sum()),
                        "military": int((m & pool.case_type.str.contains("Military")).sum())})
            vc = pool[m].county.value_counts()
            for c, n in vc.items():
                bycounty.append({"pool": name, "kV": kv, "radius_km": r_km, "county": c, "sites": int(n)})
tab = pd.DataFrame(tab)
L.append(f"\nIndustrial-class sites open at T=2019 (with coordinates): {len(pools['open_at_2019']):,}; open today: {len(pools['open_today']):,}.\n")
L.append("\n## 1. Pool size by substation distance\n\n| pool | substation | within | sites | of which Cleanup Program | Military |\n|---|---|---|---|---|---|")
for _, r in tab.iterrows():
    L.append(f"| {r['pool']} | {r['kV']} kV | {int(r.radius_km*1000)} m | {r.sites:,} | {r.cleanup_program:,} | {r.military:,} |")
bc = pd.DataFrame(bycounty)
bc.to_csv(os.path.join(RESULTS, "builtout_pool_by_county.csv"), index=False)
for name in pools:
    for kv, r_km in ((115, 0.3), (230, 3.0)):
        t = bc[(bc.pool == name) & (bc.kV == kv) & (bc.radius_km == r_km)].head(15)
        L.append(f"\nTop counties, {name}, >={kv} kV within {int(r_km*1000)} m: " + ", ".join(f"{c} {n}" for c, n in zip(t.county, t.sites)))

# ---- 2. top industrial at 2016 ----------------------------------------------------------------------------
p16 = pred[(pred["T"] == 2016) & ~pred.case_type.str.upper().str.contains("LUST", na=False)].merge(
    sites[["gid", "BUSINESS_NAME", "STREET_NUMBER", "STREET_NAME", "CITY", "status", "d230", "sub230", "kv230"]], on="gid")
p16 = p16[p16.d230 <= 3.0].sort_values("p_F", ascending=False)
top = p16.head(100)[["gid", "BUSINESS_NAME", "STREET_NUMBER", "STREET_NAME", "CITY", "county", "case_type", "status_at_T", "status",
                     "years_open", "p_F", "p_S", "p_L2", "y", "ttc", "d230", "sub230", "kv230", "lat", "lon"]].rename(
    columns={"status": "status_today", "d230": "dist_km_230kV", "sub230": "substation", "kv230": "substation_kV"})
top.to_csv(os.path.join(RESULTS, "top_industrial_2016.csv"), index=False)
L.append(f"\n## 2. Top industrial sites at T=2016 (non-LUST, within 3 km of >=230 kV)\n\nPool {len(p16):,} sites, realised 5-year closure "
         f"{p16.y.mean():.3f}. Top 100 by the full model: closure {top.y.mean():.2f}, median time to close {top.ttc.median():.1f} y; "
         f"top 100 by lookup L2: {p16.sort_values('p_L2', ascending=False).head(100).y.mean():.2f}. Median distance to the substation "
         f"{top.dist_km_230kV.median():.2f} km. List: `top_industrial_2016.csv`.\n")

# ---- 3. power plants x GeoTracker -------------------------------------------------------------------------
ez = sorted(find_files("eia860", r"eia860\d{4}\.zip$"))[-1]
year = re.search(r"eia860(\d{4})", os.path.basename(ez)).group(1)
with zipfile.ZipFile(ez) as z:
    pf = [n for n in z.namelist() if n.startswith("2___Plant")][0]
    gf = [n for n in z.namelist() if n.startswith("3_1_Generator")][0]
    plant = pd.read_excel(z.open(pf), sheet_name=0, header=1)
    gens = {sh: pd.read_excel(z.open(gf), sheet_name=sh, header=1) for sh in ("Operable", "Retired and Canceled")}
plant = plant[(plant.State == "CA") & plant.Latitude.notna()].copy()
g = []
for sh, d in gens.items():
    d = d[d.State == "CA"].copy()
    d["sheet"] = sh
    stat = d.get("Status", pd.Series("", index=d.index)).astype(str)
    d["is_retired"] = (sh != "Operable") & ~stat.str.upper().str.startswith("CN")  # drop canceled-before-built
    d["is_operable"] = sh == "Operable"
    g.append(d[(d.is_operable | d.is_retired)])
g = pd.concat(g)
mwcol = [c for c in g.columns if str(c).startswith("Nameplate Capacity")][0]
g["mw"] = pd.to_numeric(g[mwcol], errors="coerce")
g = g.reset_index(drop=True)
g["mw_op"] = g.mw.where(g.is_operable, 0.0)
g["mw_ret"] = g.mw.where(g.is_retired, 0.0)
g["ret_year"] = pd.to_numeric(g["Retirement Year"], errors="coerce") if "Retirement Year" in g else np.nan
agg = g.groupby("Plant Code").agg(mw_operable=("mw_op", "sum"), mw_retired=("mw_ret", "sum"), retire_year=("ret_year", "max"),
                                  tech=("Technology", lambda s: s.value_counts().index[0] if s.notna().any() else ""))
plant = plant.merge(agg, left_on="Plant Code", right_index=True, how="inner")
plant["plant_status"] = np.where(plant.mw_operable > 0, np.where(plant.mw_retired > 0, "partly retired", "operating"), "retired")
FOSSIL = r"Coal|Natural Gas|Petroleum|Other Gases|Nuclear|Wood|Waste|Geothermal"
plant["thermal"] = plant.tech.str.contains(FOSSIL, regex=True, na=False)
log(f"EIA-860 {year}: {len(plant):,} CA plants with lat/lon and an operable or retired generator")

tree = BallTree(np.radians(sites[["lat", "lon"]].to_numpy(dtype=float)), metric="haversine")
idx, dist = tree.query_radius(np.radians(plant[["Latitude", "Longitude"]].to_numpy(dtype=float)), r=1.0 / R, return_distance=True)
pairs = []
for (_, pr), ii, dd in zip(plant.iterrows(), idx, dist):
    for i, d in zip(ii, dd):
        s = sites.iloc[i]
        pairs.append({"plant_code": pr["Plant Code"], "plant_name": pr["Plant Name"], "plant_status": pr.plant_status, "technology": pr.tech,
                      "thermal": bool(pr.thermal), "mw_operable": pr.mw_operable, "mw_retired": pr.mw_retired, "retire_year": pr.retire_year,
                      "plant_county": pr.County, "gid": s.gid, "site_name": s.BUSINESS_NAME, "case_type": s.case_type, "site_status": s.status,
                      "site_open_today": bool(s.open_today), "dist_m": round(d * R * 1000)})
px = pd.DataFrame(pairs).sort_values(["plant_code", "dist_m"])
px.to_csv(os.path.join(RESULTS, "plants_x_geotracker.csv"), index=False)

L.append(f"\n## 3. Power plants (EIA-860 {year}) x GeoTracker\n\nSource: https://www.eia.gov/electricity/data/eia860/xls/eia860{year}.zip "
         "(2___Plant, 3_1_Generator Operable and Retired sheets; canceled projects dropped). EIA-860 only lists plants with a generator "
         "reported since about 2001, so plants demolished before then are missing. Status: operating = all MW operable; partly retired; "
         "retired = no operable MW. Thermal = coal, gas, oil, nuclear, biomass, waste, geothermal (solar/wind/hydro/storage excluded).\n")
L.append("| plants | radius | plants | with a GeoTracker case | with an OPEN case | with an open cleanup (LUST/Cleanup/Military) case | MW at plants with an open case |\n|---|---|---|---|---|---|---|")
for lab, sel in (("all", plant), ("thermal", plant[plant.thermal]), ("thermal, retired or partly retired", plant[plant.thermal & (plant.plant_status != "operating")])):
    for rm in (500, 1000):
        q = px[(px.dist_m <= rm) & px.plant_code.isin(sel["Plant Code"])]
        op = q[q.site_open_today]
        cl = op[op.case_type.str.upper().str.contains(r"LUST|CLEANUP|MILITARY", regex=True, na=False)]
        mw = sel[sel["Plant Code"].isin(op.plant_code)]
        L.append(f"| {lab} | {rm} m | {len(sel):,} | {q.plant_code.nunique():,} | {op.plant_code.nunique():,} | {cl.plant_code.nunique():,} | "
                 f"{(mw.mw_operable + mw.mw_retired).sum():,.0f} |")
q = px[(px.dist_m <= 1000) & px.thermal]
L.append("\nThermal plants with a GeoTracker case within 1 km, by plant status x case status (plants):\n")
ct = q.assign(case=np.where(q.site_open_today, "open case", "closed case")).groupby(["plant_status", "case"]).plant_code.nunique().unstack(fill_value=0)
L.append("```\n" + ct.to_string() + "\n```\n")
ft = q[q.site_open_today].groupby("technology").plant_code.nunique().sort_values(ascending=False)
L.append("Thermal plants with an open case within 1 km, by main technology: " + ", ".join(f"{k} {v}" for k, v in ft.items()))
ex = q[q.site_open_today & (q.plant_status != "operating")].drop_duplicates("plant_code").head(15)
L.append("\nExamples (retired/partly retired thermal plant, open case within 1 km): " + "; ".join(
    f"{r.plant_name} ({r.technology}, {r.mw_retired:.0f} MW retired) - {r.site_name} [{r.case_type}, {r.site_status}, {r.dist_m} m]" for r in ex.itertuples()))

# ---- 4. summary paragraph ----------------------------------------------------------------------------------
def n(pool, kv, r_km):
    return int(tab[(tab["pool"] == pool) & (tab.kV == f">={kv}") & (tab.radius_km == r_km)].sites.iloc[0])
oc = px[px.site_open_today & px.case_type.str.upper().str.contains(r"CLEANUP PROGRAM|MILITARY", regex=True, na=False)]  # industrial class, no LUST
oc_th = oc[oc.thermal & (oc.dist_m <= 1000)]
oc_ret = oc_th[oc_th.plant_status != "operating"]
L.append(f"""
## 4. How many open contaminated sites are plausibly built-out industrial with a live substation?

Of {len(pools['open_today']):,} industrial-class cleanup cases open today, {n('open_today', 115, 0.3):,} sit within 300 m of a >=115 kV
substation ({n('open_today', 230, 0.3):,} for >=230 kV), {n('open_today', 115, 1.5):,} within 1.5 km and {n('open_today', 115, 3.0):,} within 3 km
(>=230 kV within 3 km: {n('open_today', 230, 3.0):,}). Power plants are the cleanest test of "infrastructure already on the parcel": of
{int(plant.thermal.sum()):,} California thermal plants in EIA-860, {oc_th.plant_code.nunique():,} have an open Cleanup Program or military case within
1 km ({oc_th.gid.nunique():,} distinct cases), and {oc_ret.plant_code.nunique():,} of the {int((plant.thermal & (plant.plant_status != 'operating')).sum()):,}
retired or partly retired thermal plants do ({oc_ret.gid.nunique():,} cases), several of them the plant's own cleanup case (Moss Landing,
Humboldt Bay, Burbank/Magnolia, Alamitos). On this evidence the "on the parcel" set in California is in the low hundreds: roughly
{n('open_today', 115, 0.3):,} industrial cases beside a >=115 kV substation plus about {oc_th.plant_code.nunique():,} power-plant sites with an open case,
with overlap; the "near power" set (within 1.5 km of >=115 kV) is about {n('open_today', 115, 1.5):,}. Caveats: GeoTracker gives one point per
case, so large sites (refineries, bases, plants) whose point is a centroid are undercounted at 300 m; the substation layer omits many
plant switchyards; "open today" includes inactive and transferred cases; and nothing here checks parcel size, zoning or interconnection
capacity.
""")
open(os.path.join(RESULTS, "builtout.md"), "w").write("\n".join(L) + "\n")
log("\n".join(L))
