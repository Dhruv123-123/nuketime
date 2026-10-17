# Forward cleanup cost: blocked (no dated Cleanup Fund series reachable from the cloud run)

A forward cost label needs payments per claim with dates (or two reimbursed-to-date lists at least two years apart).
Nothing like that could be fetched from this environment on 16 Oct 2026, so no forward-cost model was run and no label
was made from the 2020 cumulative figure.

Checked:
- web.archive.org (CDX and captures): the egress proxy closes every connection (`ws_closed_mid_exchange`, 39 bytes);
  plain http answers "Blocked by egress policy". archive.org/wayback/available answers but gives no content.
- GeoTracker live Cleanup Fund reports (cuf_report?report=active / paymentspaid / paymentspend, cuf_claimapp_report):
  Cloudflare managed challenge (HTTP 403, cf-mitigated: challenge) for curl and for headless Chromium.
- GeoTracker bulk data_download: no Cleanup Fund file (GeoTrackerCUF, CUF, cuf_claims, CleanupFund, USTCF zips all 403).
- www.waterboards.ca.gov ustcf/ and ust/cleanup_fund/ program pages: Imperva/Incapsula bot challenge, no links.
- data.ca.gov CKAN: no Cleanup Fund dataset.

Route: a real browser session (Dhruv's) loading the paymentspaid export per fiscal year plus the active and claim
application lists; the per-claim payment ledger would then drop into data/cuf/ and the forward-cost model can run.
