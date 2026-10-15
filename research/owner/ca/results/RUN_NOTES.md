# Run notes (cloud run, 15 Oct 2026)

Data: GeoTracker statewide zip, 232 county geo zips and 58 county EDF zips (4.4 GB, 230M+ lab rows) downloaded
from documents.geotracker.waterboards.ca.gov. EnviroStor (Cloudflare challenge) and the Cleanup Fund Web Archive
captures (connection reset) were not reachable; neither feeds the backtest, so the cost model did not run.

Fixes made before the numbers were produced:
- Panel restricted to cleanup cases (LUST, Cleanup Program, Military Cleanup/UST): 66,526 of 89,587 GeoTracker
  records. WDR permits, cannabis, produced-water ponds, land disposal and info-only records have no cleanup outcome.
- Leak 1: `site_history` (today's free text, can describe the closure) removed from the text features.
- Leak 2: geo features (well/boring counts, depths, spread, first/last year) were all-time counts; now built
  per snapshot from field points first seen before T. `last_year` and all-time depth to water dropped.
- Analyte map: added real PARLABEL codes for toluene (BZME), gasoline-range TPH (PHCG, GRO*), diesel-range TPH
  (PHCD, DRO*, DIESEL2), motor oil, PFOS_A, 1,1,1-TCA, 1,2-DCA, 1,1-DCE, EDB, naphthalene.
- pandas 3 keeps NaN in str columns: lookups and categoricals now fill NaN first; 6 site-snapshots lack a county.

Robustness: dropping `agency` (a present-day field and the top feature by gain) changes temporal AUC by under
0.005 (S 0.837, F 0.841; EDF subset S 0.816, F 0.843), so it is not what separates ML from the lookups.

## Cost model (added after the hunt thread pushed the archived Cleanup Fund claims)

Label: log10 "REIMB TO DATE" from the Oct 2020 Web Archive capture of active UST Cleanup Fund claims (3,779 claims,
1,530 with a figure; capped at the $1.5M per-occurrence limit, 11% of matched sites are at 1.4M+). Joined on
GLOBAL_ID to sites open at T. Features as of 1 Jan T. 5-fold leave-counties-out.

Changes to the cost block: run at T=2010 and T=2007; add a structured-only model and a "structured + sampling
volume" model; the lookup keys on case type x status x years-open (the case type x county lookup is a constant
when the county is held out, which gave a NaN Spearman).

| T | n | Spearman full / structured+volume / structured / lookup | MAE log10 full / struct+vol / struct / lookup |
|---|---|---|---|
| 2010 | 1,185 | 0.600 / 0.548 / 0.368 / 0.263 | 0.207 / 0.224 / 0.267 / 0.264 |
| 2007 | 1,195 | 0.542 / 0.479 / 0.320 / 0.234 | 0.230 / 0.249 / 0.288 / 0.268 |

Caution: reimbursed-to-date includes money spent before T, and the number of lab samples, years sampled and
field points before T are a direct record of that past spend. Those volume counts alone take the structured model
from 0.37 to 0.55 Spearman. What the lab record adds beyond them (concentrations, trends, text) is about +0.05
Spearman and -0.02 MAE log10. This is a cumulative-cost label, not a forward cost; a clean forward-cost test
would need dated reimbursements (the FY2024-25 payments file has no GLOBAL ID, so it could not be joined).
