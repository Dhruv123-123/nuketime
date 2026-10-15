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
