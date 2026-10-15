"""Parse the statewide GeoTracker tables, EnviroStor, and the Cleanup Fund captures into work/*.pkl.

work/sites.pkl            one row per GLOBAL_ID: case_type, county, status, status_date, lat, lon, agency,
                          contaminants, media, site_history text, name
work/status_history.pkl   gid, status, date (sorted)
work/regact.pkl           gid, date, text
work/envirostor.pkl       DTSC sites with a GeoTracker alias where one exists (best effort)
work/cuf.pkl              gid, reimb_to_date (best effort; empty if no capture parsed)
"""
import os
import re

import numpy as np
import pandas as pd

from common import DATA, WORK, find_files, log, norm_cols, pick, read_table, read_table_from_zip, to_date, to_num, zip_members

sw = find_files("statewide", r"GeoTrackerDownload\.zip$")
assert sw, "statewide/GeoTrackerDownload.zip missing"
sw = sw[0]
members = zip_members(sw)
log("statewide members:", members)


def member(rx):
    m = [n for n in members if re.search(rx, os.path.basename(n), re.I)]
    return m[0] if m else None


# ---- sites -----------------------------------------------------------------------------------------
s = norm_cols(read_table_from_zip(sw, member=member(r"^sites")))
gid = pick(s.columns, r"^GLOBAL_?ID$", r"GLOBAL", required=True)
sites = pd.DataFrame({
    "gid": s[gid].str.strip(),
    "name": s[pick(s.columns, r"BUSINESS_NAME", r"SITE_NAME", r"^NAME$")] if pick(s.columns, r"BUSINESS_NAME", r"SITE_NAME", r"^NAME$") else "",
    "case_type": s[pick(s.columns, r"CASE_?TYPE", required=True)].str.strip(),
    "status": s[pick(s.columns, r"^STATUS$", r"STATUS(?!_DATE)", required=True)].str.strip(),
    "status_date": to_date(s[pick(s.columns, r"STATUS_?DATE", required=True)]),
    "county": s[pick(s.columns, r"^COUNTY", required=True)].str.strip().str.title(),
    "city": s[pick(s.columns, r"^CITY")] if pick(s.columns, r"^CITY") else "",
    "lat": to_num(s[pick(s.columns, r"^LAT", required=True)]),
    "lon": to_num(s[pick(s.columns, r"^LON", r"^LNG", required=True)]),
    "agency": s[pick(s.columns, r"LEAD_?AGENCY", r"AGENCY")].str.strip() if pick(s.columns, r"LEAD_?AGENCY", r"AGENCY") else "",
    "contaminants": s[pick(s.columns, r"CONTAMIN")].fillna("") if pick(s.columns, r"CONTAMIN") else "",
    "media": s[pick(s.columns, r"MEDIA")].fillna("") if pick(s.columns, r"MEDIA") else "",
    "site_history": s[pick(s.columns, r"HISTORY")].fillna("") if pick(s.columns, r"HISTORY") else "",
})
for c in [pick(s.columns, r"BEGIN_?DATE", r"OPEN_?DATE", r"LEAK_?REPORT", r"DISCOVER")]:
    if c:
        sites["begin_date"] = to_date(s[c])
        break
else:
    sites["begin_date"] = pd.NaT
sites = sites.drop_duplicates("gid").reset_index(drop=True)
sites["closed_flag"] = sites.status.str.upper().str.startswith("COMPLETED") | sites.status.str.upper().str.contains("CASE CLOSED")
log(f"sites: {len(sites):,}  case types: {sites.case_type.value_counts().head(8).to_dict()}")
log(f"status: {sites.status.value_counts().head(12).to_dict()}")
sites.to_pickle(os.path.join(WORK, "sites.pkl"))

# ---- status history --------------------------------------------------------------------------------
m = member(r"status_?history")
if m:
    h = norm_cols(read_table_from_zip(sw, member=m))
    sh = pd.DataFrame({
        "gid": h[pick(h.columns, r"GLOBAL", required=True)].str.strip(),
        "status": h[pick(h.columns, r"^STATUS$", r"STATUS(?!_DATE)", required=True)].str.strip(),
        "date": to_date(h[pick(h.columns, r"DATE", required=True)]),
    }).dropna(subset=["date"]).sort_values(["gid", "date"])
else:
    log("WARNING: no status_history member; reconstructing from sites only")
    sh = sites[["gid", "status", "status_date"]].rename(columns={"status_date": "date"}).dropna()
sh.to_pickle(os.path.join(WORK, "status_history.pkl"))
log(f"status_history: {len(sh):,} rows, {sh.gid.nunique():,} sites, {sh.date.min():%Y}-{sh.date.max():%Y}")

# ---- regulatory activities -------------------------------------------------------------------------
m = member(r"regulatory")
if m:
    r = norm_cols(read_table_from_zip(sw, member=m))
    g = pick(r.columns, r"GLOBAL", required=True)
    dcol = pick(r.columns, r"ACTION_?DATE", r"^DATE", r"DATE", required=True)
    textcols = [c for c in r.columns if c not in (g, dcol) and not re.search(r"ID$|LAT|LON|DATE", c)]
    ra = pd.DataFrame({"gid": r[g].str.strip(), "date": to_date(r[dcol]),
                       "text": r[textcols].fillna("").astype(str).agg(" ".join, axis=1).str.replace(r"\s+", " ", regex=True).str.strip()})
    ra = ra.dropna(subset=["date"]).sort_values(["gid", "date"])
else:
    ra = pd.DataFrame(columns=["gid", "date", "text"])
ra.to_pickle(os.path.join(WORK, "regact.pkl"))
log(f"regact: {len(ra):,} rows")

# ---- EnviroStor (best effort) ----------------------------------------------------------------------
es_rows = []
for p in find_files("envirostor", r"CleanupSites.*\.zip$") or find_files("envirostor", r"\.zip$"):
    for mm in zip_members(p):
        try:
            t = norm_cols(read_table_from_zip(p, member=mm))
        except Exception as e:  # noqa: BLE001
            log(f"  envirostor {mm}: {e}"); continue
        if pick(t.columns, r"ALIAS") and pick(t.columns, r"ENVIROSTOR_?ID|^ID$"):
            a = t[pick(t.columns, r"ALIAS_?NAME|^ALIAS$|ALIAS")].astype(str).str.strip()
            es_rows.append(pd.DataFrame({"es_id": t[pick(t.columns, r"ENVIROSTOR_?ID|^ID$")].astype(str).str.strip(),
                                         "alias": a, "src": mm}))
        elif pick(t.columns, r"ENVIROSTOR_?ID|^ID$") and pick(t.columns, r"^LAT"):
            es_rows.append(pd.DataFrame({
                "es_id": t[pick(t.columns, r"ENVIROSTOR_?ID|^ID$")].astype(str).str.strip(),
                "es_type": t[pick(t.columns, r"SITE_?TYPE|TYPE")].astype(str) if pick(t.columns, r"SITE_?TYPE|TYPE") else "",
                "es_status": t[pick(t.columns, r"^STATUS|CLEANUP_?STATUS")].astype(str) if pick(t.columns, r"^STATUS|CLEANUP_?STATUS") else "",
                "es_status_date": to_date(t[pick(t.columns, r"STATUS_?DATE")]) if pick(t.columns, r"STATUS_?DATE") else pd.NaT,
                "es_acres": to_num(t[pick(t.columns, r"ACRE")]) if pick(t.columns, r"ACRE") else np.nan,
                "lat": to_num(t[pick(t.columns, r"^LAT")]), "lon": to_num(t[pick(t.columns, r"^LON")]),
                "src": mm}))
es = pd.concat(es_rows, ignore_index=True) if es_rows else pd.DataFrame(columns=["es_id"])
es.to_pickle(os.path.join(WORK, "envirostor.pkl"))
log(f"envirostor: {len(es):,} rows from {es.src.nunique() if len(es) else 0} tables")

# ---- Cleanup Fund (best effort) --------------------------------------------------------------------
cuf_rows = []
cands = find_files("cuf", r"\.(tsv|csv|txt)$") + find_files("cuf/raw", r".*")
for p in cands:
    try:
        if re.search(r"\.xlsx?$", p, re.I):
            t = pd.read_excel(p, dtype=str)
        elif re.search(r"\.html?$|report", p, re.I) and not re.search(r"\.(tsv|csv|txt)$", p, re.I):
            tl = pd.read_html(p)
            t = max(tl, key=len) if tl else None
        else:
            t = read_table(p)
        if t is None or len(t) == 0:
            continue
        t = norm_cols(t)
        g = pick(t.columns, r"GLOBAL")
        v = pick(t.columns, r"REIMB", r"PAID", r"AMOUNT")
        if g and v:
            cuf_rows.append(pd.DataFrame({"gid": t[g].astype(str).str.strip(), "reimb": to_num(t[v]), "src": os.path.basename(p)}))
            log(f"  cuf parsed {os.path.basename(p)}: {len(t):,} rows")
    except Exception as e:  # noqa: BLE001
        log(f"  cuf {os.path.basename(p)}: {e}")
cuf = pd.concat(cuf_rows, ignore_index=True) if cuf_rows else pd.DataFrame(columns=["gid", "reimb", "src"])
if len(cuf):
    cuf = cuf.dropna(subset=["reimb"]).groupby("gid", as_index=False).reimb.max()
cuf.to_pickle(os.path.join(WORK, "cuf.pkl"))
log(f"cuf: {len(cuf):,} sites with a reimbursed-to-date figure")
