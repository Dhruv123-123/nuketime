"""Load two Berkeley Lab 'Queued Up' snapshots (end-2024 and end-2025) into one schema."""
import sys
import pandas as pd

DATES = ["q_date", "prop_date", "on_date", "wd_date", "ia_date"]
RENAME_2024 = {"IA_status_raw": "IA_phase_raw", "IA_status_clean": "IA_phase_clean", "fips_codes": "fips_code",
               "type1": "type_1", "type2": "type_2", "type3": "type_3", "mw1": "mw_1", "mw2": "mw_2", "mw3": "mw_3"}


def _dates(s):
    if pd.api.types.is_datetime64_any_dtype(s):
        return s
    num = pd.to_numeric(s, errors="coerce")
    out = pd.to_datetime(num, unit="D", origin="1899-12-30", errors="coerce")
    txt = pd.to_datetime(s.where(num.isna()), errors="coerce")
    return out.fillna(txt)


def load(path, year):
    d = pd.read_excel(path, sheet_name="03. Complete Queue Data", header=1)
    d = d.drop(columns=[c for c in d.columns if str(c).startswith("Unnamed")])
    if year == 2024:
        d = d.rename(columns=RENAME_2024)
    for c in DATES:
        d[c] = _dates(d[c])
    d["mw"] = d[["mw_1", "mw_2", "mw_3"]].apply(pd.to_numeric, errors="coerce").fillna(0).sum(axis=1)
    d["key"] = (d.q_id.astype(str).str.strip() + "|" + d.entity.astype(str) + "|" + d.q_date.dt.date.astype(str)
                + "|" + d.poi_name.astype(str).str.lower().str.strip())
    d["snapshot"] = year
    return d


if __name__ == "__main__":
    a = load(sys.argv[1], 2024)
    b = load(sys.argv[2], 2025)
    a.to_pickle(sys.argv[3])
    b.to_pickle(sys.argv[4])
    print(a.shape, b.shape)
