# D05 HELM: red team on scientific validity

Lens: identifiability, calibration, leakage, physics consistency, and whether the certainty claims can be checked honestly. Verdict: **not refuted. Score 17/25.** The decision engine is sound. Most of its "honest certainty" claims are tested against HELM's own simulator, which is circular. Each flaw below has a fix.

## 1. The synthetic pass bar tests the code, not the world (serious)

C2 draws its synthetic worlds from "the belief's own prior". The desk test then asks whether HELM beats one-step EVSI on those worlds. When the model is exactly right, a multi-step Bayesian planner will beat a one-step one almost by construction. So the 1.3x bar is close to a unit test. SBC and TARP likewise check amortisation, not whether GHOST Tier 1 looks like Nevada.

**Fix.** Make the test worlds come from a different generator than the belief. Hold out whole simulators: plan with Tier 1 plus FNO, score on TOUGH3 worlds and on archetypes the hypothesis-tournament agents invent after the belief is frozen. Add an adversarial world agent that searches for worlds where HELM loses money. Report lift under these mismatched worlds as the headline number. Report the well-specified number only as a ceiling.

## 2. The Brown-Smith gap is relative to the model (serious)

The information-relaxation bound is the value of a planner told the truth *inside the model's world*. A gap under 25% means "we plan well against our own belief". It does not bound real regret.

**Fix.** Call it a planning diagnostic, not a certainty claim. Compute it only on synthetic and mismatched worlds. Never quote it to buyers.

## 3. The real-world replay has little power and a selection bias (serious)

Score = post-2005 blind finds inside locked acres. Three problems.
- **Few events.** Nevada blind discoveries after 2005 number in the tens at most (unverified, roughly 10-25). A 1.2x lift with a bootstrap CI above 1 on ~15 events is very unlikely to show even if true. No power analysis is given.
- **Discovery needs a driller.** A find counts only where someone later searched. A policy that copies industry taste scores well. A policy that locks truly hidden hot ground nobody drilled scores zero.
- **Off-policy.** The replay can only "buy" data that existed in 2005. The 2 m probes, E-MT nodes and ranch visits that are HELM's main edge cannot be replayed at all.

**Fix.** Make the primary statistical test a proper score on held-out temperature data, not finds. There are thousands of dated wells and TG holes, so log score on T(z) bins at post-freeze wells has real power. Weight finds by inverse search effort, using the thinned-count catch rate the belief already estimates. Add a small probability-sampled field audit: say 30 cells drawn at random from each HELM score decile, each with one cheap sensor. That is the only unbiased check of the low-score region, and it costs tens of thousands of dollars. Pre-register the power calculation.

## 4. Feature-vintage leakage through derived products (serious)

The crowd model and the stacked plug-ins use INGENIOUS, USGS 2025 favourability and Faulds favourable-setting maps. These products were built with knowledge of later discoveries. Their weights were tuned to known systems. A 2005 freeze that reads them leaks the answer. Purging labels within 10-20 km does not help, because the leak sits in the covariates. Plays also correlate along belts like the Walker Lane at scales over 20 km.

**Fix.** For every frozen year, rebuild covariates from primary layers with that known_time (wells, gravity, faults as mapped then). Treat any expert-weighted product as post-dated unless its weights are refit on vintage labels. Use whole-basin or whole-belt block holdouts, not radius purges. The red-team leakage agent should diff every feature against its source's publication date and fail the run on any mismatch.

## 5. Identifiability of several latents (moderate)

- **Exists vs detected vs effort.** In the thinned LGCP, intensity and catch rate trade off wherever effort is low. That is exactly where HELM wants to buy. The posterior there is mostly prior. The sensor calibration campaign (20 blind systems, 40 controls) is the right fix. It should come before any EVSI is trusted, not run in parallel.
- **Max-entropy "unknown play" weight.** Its weight is not identified from data. In practice it is an exploration knob. Fix: set it from the hindcast "surprise rate": the share of finds after each freeze date whose archetype the model could not represent at that date (for example, Big Blind-style systems with no surface sign).
- **Rival beliefs from bids.** With 37% of Nevada winning bids at the floor, bid amounts are censored and carry little signal. The number of informed bidders, which the winner's-curse term needs, is not identified. Fix: infer rival interest from who nominated what and when, not from prices. Treat informed-bidder count as a scenario axis.
- **Rung transitions** rest on tens of cases. Use a hierarchical prior shared with oil-and-gas appraisal ladders and the 0.5-0.7x haircut until the ledger fills.

## 6. Prior falsification double-uses data (moderate)

The robust Mahalanobis check compares real data with a prior fitted to those same data. It will rarely fail. Fix: run falsification only on data held out from the fit, by basin. Use many summary statistics with an FDR correction across basins, or the MMD test from L28.

## 7. DGSA pruning is prior-conditional (moderate)

Keeping the 5-10 latents that move RNPV *under the prior* can drop a latent that matters after data, such as mask class in a lidded basin. It can also drop shared play latents, which breaks the "cold hole lowers neighbours" logic. Fix: never prune shared latents. Re-run DGSA per basin after each major update.

## 8. Amortised flows extrapolate off the simulator (moderate)

Flows trained on Tier 1 output will give confident posteriors for real data that Tier 1 cannot produce. Fix: an off-manifold detector gate (classifier two-sample test or MMD) on every input. Fall back to an explicit likelihood when it fires. Use deep ensembles of flows and treat their disagreement as extra variance.

## 9. Minor issues

- **Conformal FDR** (Jin-Candes) needs exchangeable cells, but buy-list cells sit in under-explored ground. Fix: weighted conformal under covariate shift (Tibshirani et al. 2019) with spatial blocks.
- **Physics consistency.** All three buyer heads must price the same particle, with one physically consistent T(z) that allows outflow reversals.
- **The kill rule protects the planner.** Pre-register one: if real lift of (c) over (b) stays under 1.1x after the belief passes its T(z) coverage gate, revert to one-step VOI-Bank.

## What is genuinely strong

Hashed forecasts, failure-mode labels per hole, EVSI calibration in the ledger, oracle-belief arm (d) to split belief error from planning error, and an explicit unknown-play class. These are better validation habits than any public geothermal model, Zanskar included. EVSI calibration should be tested as a predictive check (PIT of each realised observation under `predict(action)`), not as a slope on 100 noisy points.

## Score

| Axis | Score |
|---|---|
| Calibrated certainty | 3 |
| Data realism | 3 |
| Buildable in 6 months | 2 (BEL, POMCPOW, BetaZero and the crowd model is a lot for 6-7 people) |
| Edge vs Zanskar | 4 |
| Drives rights and sensors | 5 |
| **Total** | **17/25** |
