"""San Francisco Assessor Historical Secured Property Tax Rolls (data.sf.gov wv5m-vpq2), non-residential parcels,
closed roll years 2007-2025. Writes data/sf_roll.pkl."""
import json
import os
import time
import urllib.parse
import urllib.request

import pandas as pd

from common import DATA, log

URL = "https://data.sf.gov/resource/wv5m-vpq2.json"
COLS = ["closed_roll_year", "parcel_number", "property_location", "use_code", "use_definition", "property_class_code",
        "property_class_code_definition", "year_property_built", "property_area", "lot_area", "current_sales_date",
        "assessed_land_value", "assessed_improvement_value", "assessor_neighborhood_code", "the_geom"]


def get(params, tries=6):
    for i in range(tries):
        try:
            with urllib.request.urlopen(URL + "?" + urllib.parse.urlencode(params), timeout=300) as r:
                return json.loads(r.read())
        except Exception:  # noqa: BLE001
            if i == tries - 1:
                raise
            time.sleep(2 ** i)


rows, off = [], 0
while True:
    page = get({"$select": ",".join(COLS), "$where": "use_code not in ('SRES','MRES')", "$order": "row_id", "$limit": 50000, "$offset": off})
    if not page:
        break
    rows += page
    off += len(page)
    log(f"  {off:,}")
df = pd.DataFrame(rows)
df["lon"] = df.the_geom.map(lambda g: g["coordinates"][0] if isinstance(g, dict) else None)
df["lat"] = df.the_geom.map(lambda g: g["coordinates"][1] if isinstance(g, dict) else None)
df.drop(columns=["the_geom"]).to_pickle(os.path.join(DATA, "sf_roll.pkl"))
log(f"sf roll: {len(df):,} rows")
