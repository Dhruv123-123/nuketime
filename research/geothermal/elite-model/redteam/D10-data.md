# D10 CONCLAVE: red team, data-reality lens

Date: 24 Oct 2026. Reviewer: data-reality red team. The shared web search budget was used up, so no new searches were run. Facts come from D10 and evidence files L10, L20, L31, M05, M18, M19 and MODEL.md. My own estimates are marked (unverified).

## Verdict

CONCLAVE is not refuted. Its best data choice is right: fit stacking weights on thousands of well temperatures, not on tens of discoveries, and shrink toward E1 when data are thin. But the design multiplies the number of things that must be learned from the same small, clustered, leaky data. Ten experts, six targets and covariate-dependent weights all draw on about 100-200 confirmed systems and a few hundred clean deep wells. The extra layers add places for leakage and false confidence. They add little new information. Every flaw below has an AI-leveraged fix. Score: 14/25.

## Flaws and fixes

**F1. Weights are learned where wells are, and used where they are not (serious).** Stacking fits w_k(x) on held-out Y2/Y4 log scores at real wells. Those wells cluster near known systems. Only 379 of 22,535 Great Basin wells pass every quality test, at about 38 km mean spacing, and clean points sit within 3 km of only about 2% of the land (M05, Burns 2024). The target cells are far from labels, with low AOA. That is exactly where the weight model has no data. It must extrapolate B_k * z(x) along "distance to label" and "AOA", the two descriptors with the least support. The stacked map will look most confident in the places it is least tested.
*Fix:* cap the weight model's extrapolation. Weights at descriptor values outside the training hull revert to the Dirichlet prior (E1-centred), with that prior's spread carried into the band. Use importance-weighted log scores so far-field wells count more. Fit weight recovery on synthetic worlds with planted blind systems drawn from E4. Add our own wells: each sensor campaign places some holes in low-AOA cells purely to train the weights.

**F2. Effective sample size is far below "thousands of wells" (serious).** Wells come in clusters of tens to hundreds per field. After kNNDM folds and 10-20 km purges, the number of independent blocks is perhaps 50-150 (unverified). Ten experts times about 8-10 descriptors is about 100 weight parameters. That is close to one parameter per block.
*Fix:* start with 3-4 experts and 2-3 descriptors (province, AOA, modalities present). Grow only when a nested held-out test pays. Report effective sample size per fold.

**F3. The hindcast pass bar has no power (serious).** Test (b) scores post-2005 blind finds: Gabbs, Granite Springs, Big Blind, Pumpernickel, plus a few USGS "probable" systems. L31 lists 11 US blind cases in total, and only 3 found by a map. With 4-8 targets, "at least as many in the top 5%" cannot separate two models. Granite Springs results are not yet public (M18). Test (a) assumes "hundreds to low thousands" of wells first logged after 2005. Much of that is NDOM EXP and CalGEM wildcat data that sits in scanned files on request, not in digital form (M19). The real digital count may be low hundreds (unverified).
*Fix:* make (a) the primary test and grow its sample by running document AI on the 159 NDOM EXP wells and CalGEM's ~1,600 plugged wildcat TG holes first. Add the USGS per-well convective residuals (doi 10.5066/P9BZPVUC) as a dense secondary target. Treat (b) as a sign check, not a pass bar. Use rolling freezes (1980, 1990, 2005, 2015) to pool the 11 ladder cases.

**F4. Most rows have no true known_time (serious).** The bitemporal ledger needs "when was this public". SMU, NGDS and IHFC compilations carry publication dates of the compilation, not of each reading. NWIS and state well logs carry drill dates, not release dates. Confidential wells (676 still flagged in CalGEM) release later than they were drilled. Wrong known_time leaks future data into hindcasts in both directions.
*Fix:* an agent infers known_time from the earliest citing document, permit date plus statutory confidentiality (5 years in Nevada, NRS 534A.031), and archive scan dates. Each row gets a known_time interval. Hindcasts use the late end. The leakage red team re-runs scores with shifted intervals.

**F5. Satellite experts cannot be hindcast (serious for E8 and E9).** AlphaEarth embeddings start in 2017 (L20). EMIT starts in 2022 and NISAR in 2025. A 1990 or 2005 freeze cannot use them. Worse, 2017+ embeddings see well pads, roads and plants built after discovery, so they leak labels even in a 2015 freeze. E9 also retrieves analogues with these embeddings.
*Fix:* mask disturbed pixels using a pad and road detector, and test E8 and E9 only on forward pre-registered maps from 2026. Build a Landsat-only (1984+) surface expert for hindcasts. Give E8 weight in stacking only after it earns it on forward freezes.

**F6. Y3, Y5 and Y6 have almost no labels (serious).** Y3 needs failure-mode tags for dry holes. Completion reports rarely say "tight" or "outflow", and deep dry holes with usable logs number in the low hundreds (M19, unverified). Y5 has about 37 nameplate capacities against 248 zero-MW sites (M19, Trainor-Guitton 2025). Y6 needs temperatures near 4 km. Outside Utah FORGE and a few oil wells, the Great Basin has very few.
*Fix:* keep Y1 and Y2 as the only stacked targets. Treat Y3 as a latent filled by E4 physics and LLM-tagged reports, with tagger agreement reported. Fit Y5 from global size data (L17, M33) with the lookback haircut. Derive Y6 from the Y2 posterior plus the USGS 2025 EGS model, not from its own labels.

**F7. "The West" is mostly the Great Basin in disguise (moderate).** INGENIOUS layers, the 53-feature USGS release, the 1,430 FSS polygons and GeoDAWN all cover the Great Basin or parts of it. In Oregon, Idaho and the Cascades most experts abstain, labels are few and masks are thick. Stacking weights for those provinces cannot be fit.
*Fix:* transfer by province similarity, with wide bands. Use ICE-style in-context transfer (L10 shows it carries to Alberta and the UK) and buy or digitise state well files there before scoring.

**F8. E10 has no real label for "what rivals believe" (moderate).** Public layers are not what Zanskar sees. It has 370 sites and private holes.
*Fix:* fit E10 to revealed beliefs: BLM sale bids per parcel, nominations and lease relinquishments since 2008. Those are public and dated.

**F9. Checks on cited inputs.** Whether the ICE weights are public is not stated in L10 (unverified). The 132k NDWR report count needs checking. If no weights are public, retrain ICE on the 400k-reading US set (L20).

## Does it survive ~100-200 confirmed systems?

Yes, but only because its weights lean on well temperatures, and only if the expert bench is cut to what the data can rank. In the first six months, CONCLAVE is SENTINEL-COX plus E2 and E3, a small stacking layer, and an honest forward test. The rest is a roadmap.

## Scores

| Axis | Score |
|---|---|
| Calibrated certainty | 3 |
| Data realism | 2 |
| Buildable in 6 months | 2 |
| Edge vs Zanskar | 3 |
| Drives rights and sensors | 4 |
| **Total** | **14/25** |
