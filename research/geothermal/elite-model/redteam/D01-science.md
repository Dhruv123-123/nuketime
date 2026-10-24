# D01 SCX2: red team, scientific-validity lens

Date: 24 Oct 2026. Reviewer: science red team (identifiability, calibration, leakage, physics, honest validation). No web searches run. Facts come from D01 and the L-files. Paper names from memory are marked (unverified).

## Verdict

Not refuted. Score 16/25. SCX2 has the best validation stack in this program: bitemporal joins, SBC/TARP, kNNDM, CSEP, a design-based sample, a hashed ledger. But the model asks for far more latent structure than ~200 positives and ~10 dated blind finds can identify. Several "certainty" outputs would be prior echoes dressed as posteriors. Every flaw below has a fix. None is fatal.

## Flaws and fixes

**S1. The four-field product is not identified from counts (serious).** log lambda = a + log H + log P + log F + log C + Z_a(s). Four GP fields plus a residual GP plus archetype offsets, fit to a point pattern. A Cox likelihood sees only the sum. Any shift between H and P leaves the fit unchanged. So the headline "weakest link per parcel" output is set by the GP priors, not by data.
*Fix:* give each field its own measurement likelihood, so the count is not its only anchor. H is tied to E2 column tokens and Curie depth. P is tied to stress/seismicity and lost-circulation tags. F is tied to chemistry and heads. C is tied to MT conductor ensembles. Drop Z_a or give it a tight prior. Publish posterior-to-prior contraction per field per cell. Where contraction is near zero, the weakest-link label says "unknown" and the cell goes to the sensor list.

**S2. Column posteriors fed as likelihoods double-count the prior (serious).** An NPE returns p(theta | x), which already contains the Simformer training prior. Passing that into E3 as a "likelihood message" counts the prior twice. Well data also enter ICE-West (E1), the Simformer (E2) and the Diggle term (E3). The same datum is used up to three times. This yields narrow, overconfident posteriors.
*Fix:* write one explicit factor graph where each datum enters once. Use neural ratio or likelihood estimators (NRE/NLE), or divide out the training prior. Make ICE-West a prior, not an observation channel. Add a release test: refit with each source deleted and confirm the posterior widens by the expected amount.

**S3. SBC/TARP check the simulator, not the Earth (serious).** Passing SBC on synthetic worlds shows the network inverts its own simulator. Most training mass is 10^6 analytic Tier-1 runs. Only 2x10^4 are 2.5D and 5,000 are 3D. The network will learn Tier-1 shapes. MMD with a handful of tokens per cell has little power, so the OOD gate will rarely fire.
*Fix:* add fidelity as an input token and a Kennedy-O'Hagan discrepancy term learned from paired Tier-1/TOUGH3 runs. Use robust NPE methods (Ward et al. 2022 RNPE; Huang et al. 2023, unverified). The key gate is coverage on *real* held-out equilibrium logs, by depth band and archetype. D01 already lists this as gate 5. Make it gate 1. Run prior-predictive checks too: simulated token clouds must match real ones.

**S4. Archetype offsets cannot be learned from the label count (moderate).** Twelve classes, each with intensity offsets split by 120-160 C and >160 C. About 10 blind finds. Label switching and prior dominance are certain.
*Fix:* anchor archetypes with literature-extracted conceptual-model cards (the literature_text agent) as labelled training cases. Shrink offsets hierarchically under Moeck play types. Report archetype probability only where it moves more than X% from the prior.

**S5. Effort, Diggle and the residual GP compete for the same signal (serious).** Shared effort fit on springs, mines, O&G and water wells. But springs and wells cluster in valleys and along faults, so they track the open-pathway field. Effort will absorb part of the target. The Diggle term and Z_a(s) then fight over what is left. The resulting q_c vs N_hidden trade-off is the one D01 itself flags in risk 3.
*Fix:* model springs as a joint "species" sharing P and F fields, not as pure effort. Build effort from signal-blind proxies: road density, survey footprints, permit dates, AEF built-infrastructure direction. Use the planted-world SBC to measure bias in N_hidden. Do not quote N_hidden until the two-detector field survey has run.

**S6. The Freeze-2008 duel leaks (serious).** Four leaks.
(a) The 99 USGS "probable" systems are defined by a well above 85 C (L03). Most of those wells sit in pre-2008 files. Any model that ingests wells scores them high. Pooling them inflates capture. It does not test discovery.
(b) Pumpernickel's signal came from old holes that "failed" (L31). Its first signal predates 2008. Only the ML re-read is new.
(c) Anachronistic layers: Faulds' FSS polygons, AEF embeddings, lidar, GeoDAWN, INGENIOUS and the Burns/Sui priors were built after 2008. Some were built *with* labels. ICE and the VLMs were trained on post-2008 wells and text.
(d) The target list was picked in hindsight, and the duel's bars are not hashed.
*Fix:* define each target's first-signal date and deciding datum. Score only targets whose deciding datum has known_time > 2008. Tag each layer "built-with-labels". Retrain the FSS mapper and ICE with 2008 cut-offs or test-site neighbourhoods removed. Hash targets, bars and seeds before the run. Add decoy twins (planted synthetic systems with matched data) to spot memorised sites.

**S7. The pass bars are weak or underpowered (moderate).** With about 5 clean targets, "2x capture with bootstrap CI above 1" will almost never clear, even for a good model. Meanwhile CSEP N-test p > 0.05 and 85-95% coverage are passed by any wide model.
*Fix:* add proper scores: log score of target cells against baselines, CRPS for temperature, and sharpness reported beside coverage. Grow the test set from the thousands of censored cold and warm columns (temperature at depth as the target) rather than the handful of systems. Use multiple freezes and pool them with a paired permutation test.

**S8. Conformal FDR needs exchangeability it does not have (moderate).** Known systems are effort-biased. Unexplored cells are not exchangeable with them. "Stated FDR" on the buy list is not honest as written.
*Fix:* use weighted conformal with covariate-shift weights from the Cox P_det field, and print effective sample size. Or report the Bayesian expected FDR from the 4,000 draws, which is coherent with the model.

**S9. The crowd posterior is untestable as built (moderate).** "What rivals know" is a counterfactual.
*Fix:* score E5 as a forecaster of future BLM nominations and bids, which are public. If it cannot predict where nominations land next quarter, leak cost is noise.

**S10. Physics coupling (minor).** H and P are multiplied as independent fields. Convective heat needs a pathway, so they are coupled. The 7-depth ordinal bins can produce non-physical columns.
*Fix:* draw joint columns from E2 only, and add a coupling term H|P in the convective residual.

## What is strong

Bitemporal store, graded censored negatives, failure-mode ladder, design-based sample, hashed prospective ledger, real-log coverage gates, and "a miss names the component to fix". This is a validation-first design.

## Score (out of 25)

| Axis | Score | Why |
|---|---|---|
| Calibrated certainty | 3 | Right gates, but S1-S3 make some outputs prior echoes |
| Data realism | 3 | Latent structure far exceeds labels; anachronistic layers |
| Buildable in 6 months | 2 | Seven engines, 10^6 sims, re-picking and a POMDP in 6 months |
| Edge vs Zanskar | 4 | Effort, censored negatives and crowd posterior are real edges |
| Drives rights and sensors | 4 | Hurdle-routed sensing, lease clocks, Pandora stopping |
| **Total** | **16** | |
