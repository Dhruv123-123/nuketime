"""Synthetic GeoTracker-shaped inputs so the pipeline can be exercised end to end without the real
download. Writes the same layout download.py produces into $CA_DATA. Not for results.

    CA_DATA=/tmp/cafake python make_fake.py && CA_DATA=/tmp/cafake SKIP_DOWNLOAD=1 ./run_all.sh
"""
import io
import os
import zipfile

import numpy as np
import pandas as pd

from common import DATA

rng = np.random.default_rng(1)
COUNTIES = {"Napa": (38.4, -122.3), "Alpine": (38.7, -119.8), "Sierra": (39.6, -120.5), "Alameda": (37.7, -122.1)}
CASE = ["LUST Cleanup Site", "LUST Cleanup Site", "LUST Cleanup Site", "Cleanup Program Site", "Military Cleanup Site"]
N = 1600


def z(path, members):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zz:
        for name, df in members.items():
            buf = io.StringIO(); df.to_csv(buf, sep="\t", index=False); zz.writestr(name, buf.getvalue())


sites, hist, acts, edf, geoz, well, fpts, xy = [], [], [], {}, {}, {}, {}, {}
for i in range(N):
    county = list(COUNTIES)[i % len(COUNTIES)]
    lat0, lon0 = COUNTIES[county]
    gid = f"T{i:07d}"
    opened = pd.Timestamp("1990-01-01") + pd.Timedelta(days=int(rng.integers(0, 365 * 28)))
    severity = rng.gamma(2.0, 1.0)  # hidden driver: high benzene, many wells, slow closure
    dur = max(0.5, rng.lognormal(np.log(4 + 2 * severity), 0.5))
    closed = opened + pd.Timedelta(days=int(dur * 365)) if rng.random() < 0.85 else pd.NaT
    status = "Completed - Case Closed" if pd.notna(closed) and closed < pd.Timestamp("2026-01-01") else "Open - Remediation"
    sdate = closed if status.startswith("Completed") else pd.Timestamp("2025-06-01")
    sites.append(dict(GLOBAL_ID=gid, BUSINESS_NAME=f"Site {i}", CASE_TYPE=CASE[i % 5], STATUS=status, STATUS_DATE=sdate.strftime("%m/%d/%Y"),
                      COUNTY=county.upper(), CITY="X", LATITUDE=lat0 + rng.normal(0, 0.05), LONGITUDE=lon0 + rng.normal(0, 0.05),
                      LEAD_AGENCY=rng.choice(["RB2", "LOP-Napa", "RB5"]), POTENTIAL_CONTAMINANTS_OF_CONCERN="Benzene, MTBE" if i % 3 else "Gasoline",
                      POTENTIAL_MEDIA_OF_CONCERN="Aquifer used for drinking water supply" if i % 2 else "Soil", SITE_HISTORY="leak found at former station"))
    hist.append(dict(GLOBAL_ID=gid, STATUS="Open - Site Assessment", STATUS_DATE=opened.strftime("%m/%d/%Y")))
    hist.append(dict(GLOBAL_ID=gid, STATUS="Open - Remediation", STATUS_DATE=(opened + pd.Timedelta(days=700)).strftime("%m/%d/%Y")))
    if status.startswith("Completed"):
        hist.append(dict(GLOBAL_ID=gid, STATUS="Completed - Case Closed", STATUS_DATE=closed.strftime("%m/%d/%Y")))
    for k in range(int(rng.integers(1, 6))):
        acts.append(dict(GLOBAL_ID=gid, ACTION_TYPE="Report", ACTION=rng.choice(["Site Assessment Report", "Corrective Action Plan", "Remediation progress", "Request for closure"]),
                         ACTION_DATE=(opened + pd.Timedelta(days=int(rng.integers(0, 3000)))).strftime("%m/%d/%Y")))
    nw = int(rng.integers(1, 3 + int(severity * 3)))
    for w in range(nw):
        fp = f"MW-{w+1}"
        fpts.setdefault(county, []).append(dict(GLOBAL_ID=gid, FIELD_PT_NAME=fp, FIELD_PT_CLASS="MW"))
        well.setdefault(county, []).append(dict(GLOBAL_ID=gid, FIELD_PT_NAME=fp, TOTAL_DEPTH=rng.uniform(15, 60), INSTALL_DATE=opened.strftime("%m/%d/%Y")))
        xy.setdefault(county, []).append(dict(GLOBAL_ID=gid, FIELD_PT_NAME=fp, LATITUDE=lat0 + rng.normal(0, 0.001), LONGITUDE=lon0 + rng.normal(0, 0.001), XY_SURVEY_DATE=opened.strftime("%m/%d/%Y")))
        for q in range(int(rng.integers(2, 14))):
            d = opened + pd.Timedelta(days=int(rng.integers(0, 365 * 12)))
            geoz.setdefault(county, []).append(dict(GLOBAL_ID=gid, FIELD_PT_NAME=fp, GW_MEAS_DATE=d.strftime("%m/%d/%Y"), DTW=rng.uniform(5, 30)))
            for par, scale in (("BZ", 50 * severity), ("MTBE", 20 * severity), ("TPHG", 500 * severity), ("TCE", 2)):
                yrs = (d - opened).days / 365.25
                v = scale * np.exp(-0.25 * yrs) * rng.lognormal(0, 0.6)
                det = v > 0.5
                edf.setdefault(county, []).append(dict(GLOBAL_ID=gid, FIELD_PT_NAME=fp, LOGDATE=d.strftime("%m/%d/%Y"), MATRIX="W", PARLABEL=par,
                                                       PARVAL=f"{v:.3f}" if det else "0.5", PARVQ="=" if det else "<", UNITS="UG/L"))
            if q == 0:
                edf[county].append(dict(GLOBAL_ID=gid, FIELD_PT_NAME=fp, LOGDATE=d.strftime("%m/%d/%Y"), MATRIX="SO", PARLABEL="BZ",
                                        PARVAL=f"{severity:.3f}", PARVQ="=", UNITS="MG/KG"))

z(os.path.join(DATA, "statewide", "GeoTrackerDownload.zip"), {"sites.txt": pd.DataFrame(sites), "status_history.txt": pd.DataFrame(hist), "regulatory_activities.txt": pd.DataFrame(acts)})
for c in COUNTIES:
    z(os.path.join(DATA, "edf_by_county", f"{c}EDF.zip"), {f"{c}EDF.txt": pd.DataFrame(edf[c])})
    z(os.path.join(DATA, "geo_by_county", f"{c}GeoZ.zip"), {f"{c}GeoZ.txt": pd.DataFrame(geoz[c])})
    z(os.path.join(DATA, "geo_by_county", f"{c}GeoWell.zip"), {f"{c}GeoWell.txt": pd.DataFrame(well[c])})
    z(os.path.join(DATA, "geo_by_county", f"{c}FieldPoints.zip"), {f"{c}FieldPoints.txt": pd.DataFrame(fpts[c])})
    z(os.path.join(DATA, "geo_by_county", f"{c}GeoXY.zip"), {f"{c}GeoXY.txt": pd.DataFrame(xy[c])})
os.makedirs(os.path.join(DATA, "cuf"), exist_ok=True)
pd.DataFrame({"GLOBAL ID": [s["GLOBAL_ID"] for s in sites[:600]], "REIMB TO DATE": rng.lognormal(12, 1, 600).round(0)}).to_csv(os.path.join(DATA, "cuf", "active_claims_2020.tsv"), sep="\t", index=False)
z(os.path.join(DATA, "envirostor", "EnviroStorCleanupSites.zip"), {"sites.txt": pd.DataFrame([dict(ENVIROSTOR_ID="E1", SITE_TYPE="State Response", STATUS="Active", STATUS_DATE="01/01/2020", LATITUDE=38.4, LONGITUDE=-122.3)]),
                                                                    "aliases.txt": pd.DataFrame([dict(ENVIROSTOR_ID="E1", ALIAS_TYPE="GeoTracker", ALIAS_NAME="T0000001")])})
import shutil
shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "ca_substations.csv"), os.path.join(DATA, "ca_substations.csv"))
print("fake data in", DATA, "sites", len(sites), "edf rows", sum(len(v) for v in edf.values()))
