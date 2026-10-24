# D06 HEARTHNET: red team, scientific-validity lens

Date: 24 Oct 2026. Reviewer: science red team (identifiability, calibration, leakage, physics, honest validation). No web searches run. Facts come from D06 and the L-files. Papers cited from memory are marked (unverified) where unsure.

## Verdict

Not refuted. Score 16/25. HEARTHNET has the right instincts: censored negatives, a dated evidence store, kNNDM, a pre-registration ledger, a fold-back path into SENTINEL-COX. But its headline certainty claims, a conformal FDR on a buy list and a firewalled c(x, t), are not valid as written. Each has a fix. None is fatal.

## Flaws and fixes

**S1. lambda and c are not separately identified (serious).** Labels see only lambda x c. A neural c with per-archetype outputs, and archetypes that are themselves latent for most cells, gives the optimiser a free trade: raise c, lower lambda, same loss. Fithian et al. 2015 identifies effort only when the extra "species" share effort but not intensity. D06's species are hot springs, mines and water wells. Springs sit on open faults. Water wells sit in valleys where B4-B6 masks live. They share intensity with the target, so the trick fails.
*Fix:* build effort only from signal-blind species (roads, survey footprints, permit dates, O&G holes drilled for other targets). Move springs to the geology side as a joint outcome. Anchor c with a design-based sample: the month-6 field campaign should visit randomly drawn high-prior, never-searched cells, not only known blind systems. Until then, report psi as a partial-identification interval over a plausible c range.

**S2. The adversarial firewall probe tests the wrong thing (serious).** "z_cell cannot predict effort (AUC <= 0.6)" forces geology to be independent of effort. They are not independent in truth: people drilled where geology looked good. The probe would strip real signal. Worse, the geology stream is itself an effort artifact. A BHT token exists only where someone drilled. Token count, ABSENT tokens and source mix all encode effort. So the firewall leaks through the inputs, whatever the probe says.
*Fix:* drop the marginal probe. In Westlets, where true geology and simulated effort are both known, test conditional independence: given true geology, z must not predict effort. On real data, compare maps made with and without data-presence features. Add data density as an explicit nuisance input to the c side only.

**S3. The temperature data are missing not at random (serious).** Wells were drilled where heat was expected. Dry holes are reported less often. The learned, era-dependent BHT bias can absorb geology, because era and province co-vary. H1 coverage on held-out wells will then look good while undrilled cells are biased.
*Fix:* fix BHT corrections with paired BHT/equilibrium sets (SMU, KGS, Harrison-style priors) instead of learning them freely. Weight training by inverse drilling propensity from the effort net. Report H1 coverage stratified by effort decile.

**S4. Conformal FDR claims cannot be honestly checked (serious).** Jin and Candès (2023) give FDR control when calibration units are exchangeable with test units and carry the same label. The buy-list label is "lacks a >=120 C system at <=1.5 km". That label exists only for drilled cells, a selected sample. Undrilled parcels are not exchangeable with them. Mondrian by province x archetype leaves cells with 0-3 calibration points. A 90% band needs at least 9. The synthetic-world FDR proves only that the network inverts its own simulator.
*Fix:* use covariate-shift weighted conformal (Tibshirani et al. 2019) with the effort model as the density ratio, and publish effective sample size per stratum. Merge strata until n_eff >= 20. State the buy-list FDR as a design-based estimate from cheap TG holes on a random draw of listed parcels, with a binomial CI. Call it "estimated", not "guaranteed", until that sample exists.

**S5. Hindcast leakage through pretraining and derived layers (serious).** Masked-token pretraining on 10^7 worldwide tokens will include post-2010 Nevada wells, the very readings the desk test scores. The conductive residual base (USGS Great Basin 3D, InterPIGNN), Faulds FSS polygons, AlphaEarth and the extraction VLMs were all built after 2010, some using labels. Westlets were designed knowing B3 is the blind archetype. Pumpernickel's first signal predates 2010 (L31), so it tests re-reading, not discovery.
*Fix:* pretrain per freeze date, or drop pretraining from the desk test (D06 already does for world data; extend it to Nevada tokens after 2010). Stamp known_time on derived layers and exclude them, or rebuild them from frozen inputs. Let the red-team agent run a canary test: plant fake post-freeze tokens and check they cannot move hindcast scores.

**S6. Physics consistency is partial (moderate).** Per-depth ordinal bins with a hard monotone decoder contradict the stated goal of seeing reversals. Real outflow plumes show reversals (L10). Bins at seven depths are not tied by heat transport, and the T head is not tied to the existence head.
*Fix:* decode T(z) through a parametric column (conductive plus Bredehoeft-Papadopulos advection, with an outflow-lens term) whose parameters the network predicts. Allow reversals only under outflow archetypes. Add a consistency loss: high psi must imply a hot T(z) somewhere within 2 km.

**S7. Generated-sensor EVSI is unvalidated (moderate).** A masked-token sampler is not a calibrated predictive. If it is overconfident, EVSI is too low; if it hallucinates spread, sensors look too valuable.
*Fix:* before any EVSI, check PIT calibration of generated readings against held-out real TG holes and MT soundings. Average over 100+ samples per sensor, not one pass.

**S8. The pass bar has almost no power (moderate).** Five blind finds plus two cold sites. "Median rank in top 5%" has a CI wider than the bar. Argenta and Reese River were chosen with hindsight.
*Fix:* hash the bar before the run. Add thousands of post-2010 well readings as a censored-likelihood test set. Use a permutation test against the GeoCore-style baseline. Treat the prospective ledger as the primary test.

**S9. The crowd-model edge is noise-dominated (moderate).** The difference of two noisy posteriors from 280 positives will mostly reflect ensemble noise.
*Fix:* pair ensemble members across the two models; act only where edge exceeds the paired spread.

## Scores

| Axis | Score | Note |
|---|---|---|
| Calibrated certainty | 3 | Good machinery; FDR and c claims overstated until S1, S4 fixed |
| Data realism | 3 | MNAR and anachronistic layers; extraction pipeline is solid |
| Buildable in 6 months | 2 | World pretraining, 10^5 Westlets, crowd model and EVSI with 4-5 people is too much; Nevada-only first is fine |
| Edge vs Zanskar | 4 | Censored negatives and an effort term are real gaps in GeoCore |
| Drives rights and sensors | 4 | Clean hook into VOI-Bank; sensor pricing needs S7 |
| **Total** | **16/25** | |

## Bottom line

Keep HEARTHNET as the encoder and calibration layer. Let SENTINEL-COX or an explicit factor graph own identifiability. Make the design-based field sample, not synthetic worlds, the source of every published certainty number.
