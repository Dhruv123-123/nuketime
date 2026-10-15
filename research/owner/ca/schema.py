"""Write work/SCHEMA.md: columns and three sample rows of every input table, plus value counts of the EDF
code columns (PARLABEL, MATRIX, UNITS, PARVQ) so the analyte map in common.py can be checked."""
import os
import zipfile

import pandas as pd

from common import ANALYTES, CODE_TO_ANALYTE, DATA, WORK, find_files, log, read_table_from_zip, zip_members

out = [f"# Input schema ({pd.Timestamp.now():%Y-%m-%d})\n"]


def show(title, df):
    out.append(f"\n## {title}\n\ncolumns ({len(df.columns)}): " + ", ".join(map(str, df.columns)) + "\n")
    out.append("```\n" + df.head(3).to_string(max_colwidth=40) + "\n```\n")


def zip_tables(path, nrows=3):
    for m in zip_members(path):
        try:
            df = read_table_from_zip(path, member=m, nrows=nrows)
            show(f"{os.path.relpath(path, DATA)} :: {m}", df)
        except Exception as e:  # noqa: BLE001
            out.append(f"\n## {path} :: {m}\n\nfailed: {e}\n")


for p in find_files("statewide", r"\.zip$"):
    zip_tables(p)

geo = sorted(find_files("geo_by_county", r"\.zip$"), key=os.path.getsize)
for kind in ("GeoXY", "GeoZ", "GeoWell", "FieldPoints"):
    hits = [p for p in geo if kind.lower() in os.path.basename(p).lower() and os.path.getsize(p) > 500]
    if hits:
        zip_tables(hits[len(hits) // 2])

edf = sorted([p for p in find_files("edf_by_county", r"\.zip$") if os.path.getsize(p) > 5000], key=os.path.getsize)
if edf:
    p = edf[len(edf) // 2]
    zip_tables(p)
    cnt = {}
    n = 0
    for ch in read_table_from_zip(p, chunksize=500_000):
        ch.columns = [str(c).strip().upper() for c in ch.columns]
        for c in ("PARLABEL", "MATRIX", "UNITS", "PARVQ"):
            if c in ch.columns:
                cnt[c] = cnt.get(c, pd.Series(dtype=float)).add(ch[c].str.strip().str.upper().value_counts(), fill_value=0)
        n += len(ch)
        if n > 3_000_000:
            break
    out.append(f"\n## EDF code value counts from {os.path.basename(p)} (first {n:,} rows)\n")
    for c, s in cnt.items():
        s = s.sort_values(ascending=False)
        out.append(f"\n### {c} (top 80 of {len(s)})\n\n```\n" + s.head(80).to_string() + "\n```\n")
    if "PARLABEL" in cnt:
        labels = cnt["PARLABEL"].sort_values(ascending=False)
        mapped = {a: [c for c in cs if c in labels.index] for a, cs in ANALYTES.items()}
        out.append("\n### analyte map check (codes from common.ANALYTES present in this county)\n\n```\n")
        for a, cs in mapped.items():
            out.append(f"{a:14s} {cs}\n")
        out.append("```\n")
        unmatched = [c for c in labels.head(150).index if c not in CODE_TO_ANALYTE]
        out.append(f"\nTop codes not in the map (check for missed analytes): {unmatched[:60]}\n")

for p in find_files("envirostor", r"\.zip$"):
    zip_tables(p)

for p in find_files("cuf", r"\.(tsv|csv|txt)$"):
    try:
        from common import read_table
        show(os.path.relpath(p, DATA), read_table(p, nrows=3))
    except Exception as e:  # noqa: BLE001
        out.append(f"\n## {p}\n\nfailed: {e}\n")
raw = os.path.join(DATA, "cuf", "raw")
if os.path.isdir(raw):
    out.append("\n## cuf/raw captures\n\n" + "\n".join(f"- {f} ({os.path.getsize(os.path.join(raw, f))} B)" for f in sorted(os.listdir(raw))) + "\n")

open(os.path.join(WORK, "SCHEMA.md"), "w").write("".join(out))
log(f"wrote {os.path.join(WORK, 'SCHEMA.md')}")
