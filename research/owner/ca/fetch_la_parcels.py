"""LA County current parcel layer (public.gis.lacounty.gov LACounty_Parcel): lot area (Shape.STArea, sq ft) and
current use for every non-residential parcel, plus the parcel containing each LA County GeoTracker case point.

Writes data/la_parcels/area.pkl (AIN, UseType, UseDescription, lot_sqft, lat, lon) and
data/la_parcels/case_parcel.pkl (gid, AIN, lot_sqft, SitusAddress) via point-in-polygon queries.
"""
import json
import os
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import pandas as pd

from common import DATA, WORK, log

URL = "https://public.gis.lacounty.gov/public/rest/services/LACounty_Cache/LACounty_Parcel/MapServer/0/query"
OUT = os.path.join(DATA, "la_parcels")
os.makedirs(OUT, exist_ok=True)


def get(params, tries=6):
    body = urllib.parse.urlencode(params).encode()
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(URL, data=body), timeout=180) as r:
                d = json.loads(r.read())
            if "error" in d:
                raise IOError(d["error"])
            return d
        except Exception:  # noqa: BLE001
            if i == tries - 1:
                raise
            time.sleep(2 ** i)


def area_chunk(bounds):
    lo, hi = bounds
    rows, last = [], lo
    while True:
        d = get({"where": f"(UseType IS NULL OR UseType<>'Residential') AND OBJECTID>{last} AND OBJECTID<={hi}",
                 "outFields": "OBJECTID,AIN,UseType,UseDescription,Shape.STArea(),CENTER_LAT,CENTER_LON",
                 "orderByFields": "OBJECTID", "returnGeometry": "false", "f": "json"})
        f = [x["attributes"] for x in d.get("features", [])]
        if not f:
            break
        rows += f
        last = f[-1]["OBJECTID"]
    return rows


def case_parcel(r):
    d = get({"geometry": f"{r.lon},{r.lat}", "geometryType": "esriGeometryPoint", "inSR": 4326, "spatialRel": "esriSpatialRelIntersects",
             "outFields": "AIN,UseType,UseDescription,SitusAddress,Shape.STArea()", "returnGeometry": "false", "f": "json"})
    f = [x["attributes"] for x in d.get("features", [])]
    return [{"gid": r.gid, **x} for x in f[:1]]


if __name__ == "__main__":
    dest = os.path.join(OUT, "area.pkl")
    if not os.path.exists(dest):
        st = get({"where": "1=1", "outStatistics": json.dumps([{"statisticType": "max", "onStatisticField": "OBJECTID", "outStatisticFieldName": "mx"}]), "f": "json"})
        mx = st["features"][0]["attributes"]["mx"]
        step = mx // 40 + 1
        with ThreadPoolExecutor(20) as ex:
            parts = list(ex.map(area_chunk, [(i, min(i + step, mx)) for i in range(0, mx, step)]))
        a = pd.DataFrame([x for p in parts for x in p]).rename(columns={"Shape.STArea()": "lot_sqft", "CENTER_LAT": "plat", "CENTER_LON": "plon"})
        a.to_pickle(dest)
        log(f"parcel areas: {len(a):,}")
    sites = pd.read_pickle(os.path.join(WORK, "sites.pkl"))
    la = sites[(sites.county.str.upper().str.replace(" ", "") == "LOSANGELES") & sites.lat.between(33, 35.5) & sites.lon.between(-119.5, -117)]
    with ThreadPoolExecutor(24) as ex:
        res = list(ex.map(case_parcel, la.itertuples()))
    cp = pd.DataFrame([x for r in res for x in r]).rename(columns={"Shape.STArea()": "lot_sqft"})
    cp.to_pickle(os.path.join(OUT, "case_parcel.pkl"))
    log(f"LA cases: {len(la):,}; inside a parcel polygon: {cp.gid.nunique():,}")
