"""Download the LA County assessor roll (2006-2025) for commercial/industrial (C/I) and vacant (VAC) parcels
from the County's ArcGIS feature services (the old data.lacounty.gov Socrata dataset 9trm-uz8i moved there).

Writes data/la_roll/{year}.pkl, one row per (AIN, roll year). ~300k rows per year.
Usage: python fetch_la_roll.py [--jobs 16]
"""
import argparse
import json
import os
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import pandas as pd

from common import DATA, log

BASE = "https://services.arcgis.com/RmCCgQtiZLDCtblq/arcgis/rest/services"
TABLE = {range(2006, 2011): "Parcel_Data_2006_2010_Table", range(2011, 2016): "Parcel_Data_2011_2015_Table",
         range(2016, 2021): "Parcel_Data_2016_2020_Table", range(2021, 2026): "Parcel_Data_2021_Table"}
FIELDS = ["OBJECTID", "AIN", "RollYear", "UseType", "UseCode", "UseCodeDescChar1", "UseCodeDescChar2", "SQFTmain", "YearBuilt",
          "RecordingDate", "Roll_LandValue", "Roll_LandBaseYear", "Roll_ImpValue", "Roll_ImpBaseYear", "Roll_TotalValue", "Cluster",
          "SitusHouseNo", "SitusStreet", "SitusCity", "CENTER_LAT", "CENTER_LON"]
OUT = os.path.join(DATA, "la_roll")
os.makedirs(OUT, exist_ok=True)


def table_for(y):
    return next(t for r, t in TABLE.items() if y in r)


def get(url, params, tries=6):
    body = urllib.parse.urlencode(params).encode()
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, data=body), timeout=180) as r:
                d = json.loads(r.read())
            if "error" in d:
                raise IOError(d["error"])
            return d
        except Exception as e:  # noqa: BLE001
            if i == tries - 1:
                raise
            time.sleep(2 ** i)


def chunk(args):
    table, lo, hi = args
    url = f"{BASE}/{table}/FeatureServer/0/query"
    d = get(url, {"where": f"OBJECTID>={lo} AND OBJECTID<{hi} AND UseType IN ('C/I','VAC')", "outFields": ",".join(FIELDS),
                  "resultRecordCount": 2000, "returnGeometry": "false", "f": "json"})
    f = [x["attributes"] for x in d.get("features", [])]
    if d.get("exceededTransferLimit") or len(f) >= 2000:  # split until each window fits in one page
        mid = (lo + hi) // 2
        return chunk((table, lo, mid)) + chunk((table, mid, hi))
    return f


def fetch_table(table, jobs, step=8000):
    """Window by OBJECTID (indexed): a RollYear/UseType filter with ORDER BY makes the service scan the table."""
    url = f"{BASE}/{table}/FeatureServer/0/query"
    mx = get(url, {"where": "1=1", "outStatistics": json.dumps([{"statisticType": "max", "onStatisticField": "OBJECTID",
                                                                 "outStatisticFieldName": "mx"}]), "f": "json"})["features"][0]["attributes"]["mx"]
    with ThreadPoolExecutor(jobs) as ex:
        parts = list(ex.map(chunk, [(table, i, i + step) for i in range(0, mx + 1, step)]))
    return pd.DataFrame([x for p in parts for x in p])


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=16)
    a = ap.parse_args()
    for table in TABLE.values():
        df = fetch_table(table, a.jobs)
        df["RollYear"] = pd.to_numeric(df.RollYear, errors="coerce")
        for y, d in df.groupby("RollYear"):
            d.to_pickle(os.path.join(OUT, f"{int(y)}.pkl"))
        log(f"  {table}: {len(df):,} rows, years {sorted(df.RollYear.dropna().astype(int).unique())}")
