"""Shared helpers for the California powered-brownfield experiment.

Every GeoTracker / EnviroStor file is read with column names detected at run time, because the public
downloads have changed names over the years. `pick` finds a column by regex; `read_table_from_zip`
streams a tab- or comma-delimited text file out of a zip without extracting it.
"""
import csv
import io
import os
import re
import sys
import zipfile

import numpy as np
import pandas as pd

DATA = os.environ.get("CA_DATA", os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))
WORK = os.environ.get("CA_WORK", os.path.join(DATA, "work"))
RESULTS = os.environ.get("CA_RESULTS", os.path.join(os.path.dirname(os.path.abspath(__file__)), "results"))
os.makedirs(WORK, exist_ok=True)
os.makedirs(RESULTS, exist_ok=True)

COUNTIES = [
    "Alameda", "Alpine", "Amador", "Butte", "Calaveras", "Colusa", "ContraCosta", "DelNorte", "ElDorado",
    "Fresno", "Glenn", "Humboldt", "Imperial", "Inyo", "Kern", "Kings", "Lake", "Lassen", "LosAngeles",
    "Madera", "Marin", "Mariposa", "Mendocino", "Merced", "Modoc", "Mono", "Monterey", "Napa", "Nevada",
    "Orange", "Placer", "Plumas", "Riverside", "Sacramento", "SanBenito", "SanBernardino", "SanDiego",
    "SanFrancisco", "SanJoaquin", "SanLuisObispo", "SanMateo", "SantaBarbara", "SantaClara", "SantaCruz",
    "Shasta", "Sierra", "Siskiyou", "Solano", "Sonoma", "Stanislaus", "Sutter", "Tehama", "Trinity",
    "Tulare", "Tuolumne", "Ventura", "Yolo", "Yuba",
]

# Snapshot years: at each T the model sees only information dated before 1 Jan T and predicts the
# 5-year outcome. The data download is dated Oct 2026, so T=2019 is the last snapshot with 5 years of outcome.
SNAPSHOTS = [2004, 2007, 2010, 2013, 2016, 2019]
HORIZON = 5

# Analyte codes as they appear in GeoTracker EDF PARLABEL (valid value list) plus common variants.
# `schema.py` writes the real top codes so the runner can extend this map if a code is missing.
ANALYTES = {
    "benzene": {"BZ", "BENZENE"},
    "toluene": {"TOL", "TOLUENE"},
    "ethylbenzene": {"EBZ", "ETHYLBENZENE"},
    "xylenes": {"XYLENES", "XYL", "XYLENES,TOTAL", "XYLENESTOTAL", "TXYL"},
    "mtbe": {"MTBE"},
    "tba": {"TBA"},
    "tphg": {"TPHG", "TPH-G", "TPHGAS"},
    "tphd": {"TPHD", "TPH-D", "TPHDIESEL"},
    "tce": {"TCE"},
    "pce": {"PCE"},
    "cis12dce": {"C12DCE", "CIS12DCE", "DCE12C", "C-1,2-DCE"},
    "vinylchloride": {"VC", "VINYLCHLORIDE"},
    "dioxane14": {"DIOXANE14", "14DIOX", "14DIOXANE", "1,4-DIOXANE"},
    "cr6": {"CR6", "CRVI", "CR+6"},
    "chromium": {"CR", "CHROMIUM"},
    "lead": {"PB", "LEAD"},
    "arsenic": {"AS", "ARSENIC"},
    "nitrate": {"NO3", "NO3N", "NO3NO2N", "NITRATE", "NO3-N"},
    "perchlorate": {"CLO4", "PERCHLORATE"},
    "pfoa": {"PFOA"},
    "pfos": {"PFOS"},
}
CODE_TO_ANALYTE = {c: a for a, cs in ANALYTES.items() for c in cs}

WATER_UNIT_FACTOR = {"UG/L": 1.0, "MG/L": 1000.0, "NG/L": 0.001, "PPB": 1.0, "PPM": 1000.0, "UG/L ": 1.0}
SOIL_UNIT_FACTOR = {"MG/KG": 1.0, "UG/KG": 0.001, "PPM": 1.0, "PPB": 0.001, "NG/KG": 1e-6, "G/KG": 1000.0}


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def pick(cols, *patterns, required=False):
    """First column whose upper-cased name matches any regex (searched in order)."""
    up = {c: re.sub(r"\s+", "_", str(c).strip().upper().lstrip("﻿")) for c in cols}
    for p in patterns:
        rx = re.compile(p)
        for c, u in up.items():
            if rx.search(u):
                return c
    if required:
        raise KeyError(f"no column matches {patterns} in {list(cols)[:40]}")
    return None


def norm_cols(df):
    df.columns = [re.sub(r"\s+", "_", str(c).strip().upper().lstrip("﻿")) for c in df.columns]
    return df


def sniff_delim(sample: str):
    first = sample.split("\n", 1)[0]
    return "\t" if first.count("\t") >= first.count(",") else ","


def zip_members(path, pattern=r"\.(txt|csv|tsv)$"):
    with zipfile.ZipFile(path) as z:
        return [n for n in z.namelist() if re.search(pattern, n, re.I) and not n.endswith("/")]


def read_table_from_zip(path, member=None, chunksize=None, usecols=None, dtype=str, nrows=None, encoding="latin-1"):
    """Read one text member of a zip as a DataFrame (or an iterator of chunks)."""
    z = zipfile.ZipFile(path)
    if member is None:
        cands = zip_members(path)
        if not cands:
            raise FileNotFoundError(f"no text member in {path}: {z.namelist()[:10]}")
        member = max(cands, key=lambda n: z.getinfo(n).file_size)
    raw = z.open(member)
    head = raw.read(65536).decode(encoding, errors="replace")
    delim = sniff_delim(head)
    raw.close()
    f = io.TextIOWrapper(z.open(member), encoding=encoding, errors="replace", newline="")
    kw = dict(sep=delim, dtype=dtype, quoting=csv.QUOTE_NONE if delim == "\t" else csv.QUOTE_MINIMAL,
              on_bad_lines="skip", engine="c", low_memory=False, nrows=nrows)
    if usecols is not None:
        kw["usecols"] = usecols
    if chunksize:
        kw.pop("low_memory")
        return pd.read_csv(f, chunksize=chunksize, **kw)
    return pd.read_csv(f, **kw)


def read_table(path, **kw):
    if path.lower().endswith(".zip"):
        return read_table_from_zip(path, **kw)
    with open(path, "r", encoding=kw.pop("encoding", "latin-1"), errors="replace", newline="") as f:
        head = f.read(65536)
    delim = sniff_delim(head)
    return pd.read_csv(path, sep=delim, dtype=kw.pop("dtype", str), encoding="latin-1", on_bad_lines="skip",
                       quoting=csv.QUOTE_NONE if delim == "\t" else csv.QUOTE_MINIMAL, low_memory=False, **kw)


def to_date(s):
    """Parse GeoTracker dates (MM/DD/YYYY, YYYY-MM-DD, with or without time)."""
    s = s.astype(str).str.strip().str.slice(0, 19)
    out = pd.to_datetime(s, errors="coerce", format="mixed")
    return out


def to_num(s):
    return pd.to_numeric(s.astype(str).str.replace(",", "").str.strip(), errors="coerce")


def haversine_km(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(np.radians, (lat1, lon1, lat2, lon2))
    a = np.sin((lat2 - lat1) / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin((lon2 - lon1) / 2) ** 2
    return 6371.0 * 2 * np.arcsin(np.sqrt(a))


def find_files(subdir, pattern):
    d = os.path.join(DATA, subdir)
    if not os.path.isdir(d):
        return []
    return sorted(os.path.join(d, f) for f in os.listdir(d) if re.search(pattern, f, re.I))


def county_file(subdir, county, kind):
    """Find e.g. data/geo_by_county/AlamedaGeoZ.zip whatever the exact casing/separator."""
    rx = rf"^{county}[_ -]?{kind}\.(zip|txt|csv)$"
    hits = find_files(subdir, rx)
    return hits[0] if hits else None
