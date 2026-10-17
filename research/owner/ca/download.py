"""Download the California inputs into $CA_DATA (default: research/owner/ca/data).

Layout written:
  statewide/GeoTrackerDownload.zip          sites.txt, status_history.txt, regulatory_activities.txt, ...
  geo_by_county/{County}{GeoXY,GeoZ,GeoWell,FieldPoints}.zip
  edf_by_county/{County}EDF.zip             lab results (4.6 GB for all 58 counties)
  envirostor/EnviroStor*.zip                DTSC cleanup sites, activities, aliases
  cuf/raw/*                                 Web Archive copies of UST Cleanup Fund reports (best effort)

The GeoTracker HTML pages sit behind Cloudflare and may answer 403 to scripts; the files themselves have
downloaded fine (they come from documents.geotracker.waterboards.ca.gov). So each file is tried as a
direct URL in a few known spellings, and the download pages (live, then Web Archive) are parsed for links
only to fill in names that the patterns miss. Nothing is extracted; every zip is integrity-checked.

Usage: python download.py [--only statewide,geo,edf,envirostor,cuf] [--counties Napa,Alpine] [--retries 3]
"""
import argparse
import os
import re
import sys
import time
import urllib.request
import zipfile
from html.parser import HTMLParser

from common import COUNTIES, DATA, log

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
GT = "https://geotracker.waterboards.ca.gov"
GTD = "https://documents.geotracker.waterboards.ca.gov"
ES = "https://www.envirostor.dtsc.ca.gov"
WB = "https://web.archive.org/web/2026id_/"

GEO_KINDS = ["GeoXY", "GeoZ", "GeoWell", "FieldPoints"]


class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            for k, v in attrs:
                if k.lower() == "href" and v:
                    self.hrefs.append(v)


def fetch(url, timeout=60):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def page_links(url):
    """All hrefs on a page, trying the live page then the Web Archive copy."""
    for u in (url, WB + url):
        try:
            html = fetch(u, timeout=90).decode("utf-8", "replace")
            p = Links(); p.feed(html)
            out = []
            for h in p.hrefs:
                h = re.sub(r"^https?://web\.archive\.org/web/\d+(id_)?/", "", h)
                if h.startswith("/"):
                    h = GT + h if "geotracker" in url else ES + h
                out.append(h)
            log(f"  parsed {len(out)} links from {u}")
            return out
        except Exception as e:  # noqa: BLE001
            log(f"  page {u}: {e}")
    return []


def download(url, dest, retries=3, min_bytes=200):
    if os.path.exists(dest) and os.path.getsize(dest) >= min_bytes:
        return True
    tmp = dest + ".part"
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=300) as r, open(tmp, "wb") as f:
                while True:
                    b = r.read(1 << 20)
                    if not b:
                        break
                    f.write(b)
            if os.path.getsize(tmp) < min_bytes:
                raise IOError(f"tiny response ({os.path.getsize(tmp)} bytes)")
            if dest.lower().endswith(".zip"):
                with zipfile.ZipFile(tmp) as z:
                    bad = z.testzip()
                    if bad:
                        raise IOError(f"corrupt member {bad}")
            os.replace(tmp, dest)
            log(f"  ok {os.path.basename(dest)} {os.path.getsize(dest)/1e6:.1f} MB  <- {url}")
            return True
        except Exception as e:  # noqa: BLE001
            msg = str(e)
            # 403/404, or the 127-byte JavaScript redirect stub geotracker.waterboards.ca.gov serves for files
            if "404" in msg or "403" in msg or "tiny response" in msg:
                log(f"  {url}: {msg}")
                break
            log(f"  retry {i+1} {url}: {msg}")
            time.sleep(2 ** (i + 1))
    if os.path.exists(tmp):
        os.remove(tmp)
    return False


def first_ok(cands, dest, retries):
    for u in cands:
        if download(u, dest, retries):
            return True
    return False


def link_for(links, basename):
    rx = re.compile(re.escape(basename) + r"$", re.I)
    for h in links:
        if rx.search(h.split("?")[0]):
            return h
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="statewide,geo,edf,envirostor,cuf")
    ap.add_argument("--counties", default=",".join(COUNTIES))
    ap.add_argument("--retries", type=int, default=3)
    a = ap.parse_args()
    only = set(a.only.split(","))
    counties = [c for c in a.counties.split(",") if c]
    for d in ("statewide", "geo_by_county", "edf_by_county", "envirostor", "cuf/raw"):
        os.makedirs(os.path.join(DATA, d), exist_ok=True)
    failed = []

    gt_links = page_links(GT + "/data_download_by_county/") + page_links(GT + "/data_download") if only & {"statewide", "geo", "edf"} else []

    if "statewide" in only:
        for name in ("GeoTrackerDownload.zip", "GeoTrackerPermittedUST.zip"):
            dest = os.path.join(DATA, "statewide", name)
            cands = [link_for(gt_links, name)] if link_for(gt_links, name) else []
            cands += [f"{GT}/data_download/{name}", f"{GTD}/data_download/{name}", f"{GT}/datadownload/{name}"]
            if not first_ok(cands, dest, a.retries):
                failed.append(name)

    if "geo" in only:
        for c in counties:
            for kind in GEO_KINDS:
                name = f"{c}{kind}.zip"
                dest = os.path.join(DATA, "geo_by_county", name)
                cands = [link_for(gt_links, name)] if link_for(gt_links, name) else []
                cands += [f"{GTD}/data_download/geo_by_county/{name}", f"{GT}/data_download/geo_by_county/{name}",
                          f"{GT}/data_download/geo_by_county/{c}_{kind}.zip", f"{GT}/datadownload/geo_by_county/{name}"]
                if not first_ok(cands, dest, a.retries):
                    failed.append(name)

    if "edf" in only:
        for c in counties:
            name = f"{c}EDF.zip"
            dest = os.path.join(DATA, "edf_by_county", name)
            cands = [link_for(gt_links, name)] if link_for(gt_links, name) else []
            cands += [f"{GTD}/data_download/edf_by_county/{name}", f"{GT}/data_download/edf_by_county/{name}",
                      f"{GT}/data_download/edf_by_county/{c}_EDF.zip", f"{GT}/datadownload/edf_by_county/{name}"]
            if not first_ok(cands, dest, a.retries):
                failed.append(name)

    if "envirostor" in only:
        es_links = page_links(ES + "/public/data_download")
        names = ["EnviroStorCleanupSites.zip", "EnviroStorHazardousWaste.zip", "EnviroStorICESites.zip"]
        names += [os.path.basename(h.split("?")[0]) for h in es_links if h.lower().endswith(".zip")]
        for name in dict.fromkeys(names):
            dest = os.path.join(DATA, "envirostor", name)
            cands = [link_for(es_links, name)] if link_for(es_links, name) else []
            cands += [f"{ES}/public/data_download/{name}", f"{ES}/public/data_download/{name.lower()}"]
            if not first_ok(cands, dest, a.retries):
                failed.append(name)

    if "cuf" in only:
        # UST Cleanup Fund reports (claim x reimbursed-to-date) exist only as live reports behind Cloudflare;
        # pull whatever the Web Archive captured and let build_sites.py parse what it can.
        try:
            cdx = ("https://web.archive.org/cdx/search/cdx?url=geotracker.waterboards.ca.gov/*&output=json"
                   "&filter=original:(?i).*(cuf|claim|cleanupfund|ustcf).*&collapse=urlkey&limit=400")
            rows = __import__("json").loads(fetch(cdx, 120).decode())[1:]
            log(f"  CDX: {len(rows)} CUF-like captures")
            with open(os.path.join(DATA, "cuf", "cdx_captures.tsv"), "w") as f:
                for r in rows:
                    f.write("\t".join(r) + "\n")
            for r in rows:
                ts, orig = r[1], r[2]
                if not re.search(r"(export|excel|xls|csv|report)", orig, re.I):
                    continue
                dest = os.path.join(DATA, "cuf", "raw", re.sub(r"[^A-Za-z0-9._-]+", "_", f"{ts}_{orig}")[:180])
                download(f"https://web.archive.org/web/{ts}id_/{orig}", dest, 1, min_bytes=1000)
        except Exception as e:  # noqa: BLE001
            log(f"  CUF archive query failed: {e}")
            failed.append("cuf")

    with open(os.path.join(DATA, "DOWNLOAD_LOG.md"), "a") as f:
        f.write(f"\n## {time.strftime('%Y-%m-%d %H:%M')} failed: {failed}\n")
    log(f"done. failed: {failed}")
    return 1 if any(x in failed for x in ("GeoTrackerDownload.zip",)) else 0


if __name__ == "__main__":
    sys.exit(main())
