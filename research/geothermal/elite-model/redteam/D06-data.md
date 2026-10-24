# D06 HEARTHNET: red team, data-reality lens

Date: 24 Oct 2026. Reviewer: data-reality red team. No new web searches were run. Facts come from D06, L05, L19 and v1 evidence. My own estimates are marked (unverified).

## Verdict in one paragraph

HEARTHNET is not refuted. Its temperature head trains on tens of thousands of readings, so it survives the label famine. Its existence, archetype, failure and buy-list heads do not, as written. With about 100-200 confirmed Western systems spread over 11 archetypes, several heads are fitted to single digits of labels, and the per-archetype label frequency c_a for blind types is set by assumption, not learned. The design also leaks effort through token density, and its 2010 hindcast has known_time values that mostly do not exist yet. Every flaw has an AI-leveraged fix. Most fixes move weight from rare binary labels to plentiful censored temperature readings and to synthetic worlds. Score: 15/25.

## Flaws and fixes

**F1. Per-archetype existence and c_a are not identifiable (serious).** D06 claims about 280 US positives. The USGS 2008 count is 241 identified moderate- and high-temperature systems (unverified recall). Either way, split across 11 archetypes, B1 holds most labels. B3 (capped basin) and B4-B6 (masked) hold perhaps 0-10 each. Big Blind is roughly the only confirmed B3-like blind commercial system in 30 years (L05). D06 writes "B3 c near 0.1", but nothing in public data can estimate that. PULSNAR needs labelled positives in each subtype to cluster on (L19). A PU loss with an unknown c and near-zero positives gives lambda times c, never lambda alone.
*Fix:* do not learn c_a for blind archetypes from labels. Fix it from two outside sources. (a) Synthetic Westlets with a simulated search history give c_a with known truth. (b) Edwards et al. (SGW 2025) report 370 sites, 112 blind, from about 27,000 samples (L05). Mine its tables and the Nevada TG-hole record (NBMG, NDOM) with an extraction agent to count blind finds per hole drilled by setting. Put these as tight priors on c_a. Report lambda for blind archetypes as prior-dominated, with that flag in the map.

**F2. The token count is inflated by non-thermal data (moderate).** "About 10^7 real tokens" is plausible only with gravity stations, water-well lithology and solute rows. Temperature-bearing tokens are much fewer. NDWR's 146k reports and CA OSWCR's 1.1M rarely record temperature (likely a few per cent, unverified). The Global Heat Flow Database 2024 has on the order of 10^5 sites (unverified). KGS 212k BHTs are in Kansas, a conductive setting. So masked-token pretraining mostly learns to interpolate gravity and chemistry.
*Fix:* weight the masked loss toward thermal tokens. Report the thermal token count per province before training. Run the AI extraction swarm first on sources with dense temperature (NBMG 2,002 scans, NDOM geothermal well files, UNU-GTP theses), not on the 1.1M CA logs.

**F3. Effort leaks through token density (serious).** D06 firewalls effort tokens from E3. But a well is both a geology token and an effort token. MT, gravity detail and 2 m surveys exist mainly where someone already suspected heat. A Perceiver that attends to 300 tokens in one cell and 3 in another already knows effort. The learned ABSENT token encodes it too. The probe (AUC 0.6 or below) tests only z_cell, and it will likely fail.
*Fix:* train with density-matched token thinning. Subsample each cell's context to a fixed token budget per modality, drawn at random each step. Add a gradient-reversal head that predicts effort from z_cell during training, not just a probe after it. Test on Westlets where the effort map is known and independent of geology.

**F4. known_time mostly does not exist (serious for the hindcast).** The bitemporal store is the right idea. But INGENIOUS layers, the USGS 3D thermal model, Faulds FSS polygons and many MT surveys were built after 2010 and often because of finds (L19, feature-vintage leakage). NBMG scans and NDWR logs carry report dates, not public-release dates. Pumpernickel was a previously abandoned prospect with old wells (L05), so it is not blind at a 2010 freeze.
*Fix:* an agent assigns known_time from report dates, survey metadata and citation dates. Uncertain values get the latest plausible date. Rebuild derived layers (strain, conductance, FSS) from pre-2010 inputs only, or drop them from the hindcast. Score Pumpernickel as "relabelled", not "blind".

**F5. Conformal guarantees go vacuous at this n (serious).** Mondrian calibration by province times archetype with 100-200 positives gives groups of 0-10. Below about 9 calibration points, a 90% split-conformal band is unbounded. Conformal selection needs calibration labels from the same distribution as candidates. Candidates are unexplored cells; labelled cells are explored ones. Weighted conformal under that shift gives extreme weights.
*Fix:* calibrate T(z) bands on the tens of thousands of censored temperature readings, where n is large. Derive the buy-list FDR from calibrated T(z) draws through the fixed M34 economics, not from existence labels. Pool Mondrian groups hierarchically. Check realised FDR on Westlets and on our own sensor visits (the month-6 campaign of 20 blind systems and 40 cold controls is the true calibration set; double it).

**F6. Global labels are thinner and more private than implied (moderate).** CFE, Pertamina, PHIVOLCS-era well data and most Philippine and Indonesian logs are not public (unverified). The 700 world fields figure is unverified. Most are volcanic arc systems, a different archetype from Great Basin.
*Fix:* keep only public, leave-one-country-out-positive sources (NZ GNS, Iceland ISOR, ThermoGIS/NLOG, OZTemp, Alberta). Use multilingual document AI on UNU-GTP theses, which publish many national well logs, as the main world label source.

**F7. Failure-mode and validation labels are tiny (moderate).** Public geothermal completion reports in Nevada and Utah number in the hundreds (unverified). Six failure classes on that is thin. The 2010 Nevada hindcast has about 5-7 blind finds. A "median in top 5%" bar on n=5 is a coin toss.
*Fix:* collapse the ladder to three classes until counts allow more. Replace the existence-rank bar with a temperature-log likelihood bar on thousands of post-2010 readings, which has power. Keep blind-find ranks as a reported, not gating, number.

**F8. The crowd model under-states the crowd (minor).** Zanskar holds a private 27,000-sample compilation (L05). A crowd model trained on public layers will see edge where Zanskar sees none.
*Fix:* infer rival belief from revealed actions. BLM nominations, lease bids and permits by date (MLRS) become crowd tokens.

## Does it survive 100-200 confirmed systems?

Yes, if it is re-ranked. T(z) is the head with real data volume and should be the spine. Existence for leaky systems is learnable. Existence for blind archetypes must be physics- and synthetic-prior driven and flagged as such. That is close to SENTINEL-COX, with better encoders.

## Scores

| Axis | Score |
|---|---|
| Calibrated certainty | 3 |
| Data realism | 2 |
| Buildable in 6 months | 2 |
| Edge vs Zanskar | 4 |
| Drives rights and sensors | 4 |
| **Total** | **15/25** |
