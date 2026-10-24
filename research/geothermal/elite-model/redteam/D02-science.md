# D02 TRIBUNAL: red team, scientific-validity lens

Date: 24 Oct 2026. Reviewer: science red team (identifiability, calibration, leakage, physics, honest validation). No web searches run. Paper names are from memory; anything not checked is marked (unverified).

## Verdict

Not refuted. Score 16/25. The core move is sound: LLMs propose, a non-LLM judge scores. That is the right split. But "the judge sets the probabilities" is not enough on its own to make the numbers honest. LLM authorship still shapes the card priors, the hypothesis set and the test set. Each leak below has a concrete fix. None is fatal.

## Flaws and fixes

**S1. Card authors set their own evidence (serious).** A card's marginal likelihood depends on how wide its parameter priors are (Lindley's paradox). An agent can win by drawing a tight upflow polygon right where the hot data sit. And agents write cards *after* reading the same data the judge scores. That double-uses the data and inflates the evidence of fitted cards.
*Fix:* agents choose only discrete structure: archetype, fault ID, upflow anchor cell. Widths come from a fixed, versioned archetype prior library, not from the agent. Score cards on data the author never saw: split each prospect's facts into a "briefing" half and a "scoring" half (random, spatially blocked), or use leave-one-source-out predictive scores. That is what Bayesian stacking does (Yao et al. 2018, Bayesian Analysis) and it is safer than BMA when no card is true.

**S2. BMA is the wrong averaging rule here (serious).** BMA assumes one card is true (M-closed). Geothermal is M-open. With 5-20 observations, BMA weights snap to one card. The posterior then looks confident when it is not. The fixed 10% "unknown" card does not fix this. A "max-entropy" likelihood has no natural scale, so its evidence is set by an arbitrary density choice. It will be either always crushed or always winning.
*Fix:* use stacking or pseudo-BMA+ weights for the T(z) and upflow outputs. Give the unknown card a real generative model: the SENTINEL-COX regional posterior predictive itself. Then "unknown" means "nothing beyond the regional prior" and its likelihood is well defined.

**S3. NPE does not give evidence (moderate).** An amortised posterior estimator returns posteriors, not marginal likelihoods. Evidence needs a likelihood or ratio estimator plus importance sampling, or a direct evidence network. Also an MMD misspecification test (Schmitt et al. 2023, unverified ref) has little power with a few columns per prospect.
*Fix:* train neural likelihood estimators (NLE) or a dedicated evidence net per archetype. Check evidence accuracy on synthetic worlds against brute-force estimates. Replace per-prospect MMD with a posterior-predictive p-value on held-out facts, pooled per archetype.

**S4. Simulator fidelity differs across cards (serious).** GHOST Tier 1 is an analytic column plus plume. Some archetypes (B1 outflow, B7 conductive) fit that form well. Others (B2 range-hosted, B6 carbonate sweep) do not. A card whose simulator is a poor fit loses evidence for reasons of code, not geology.
*Fix:* add a per-archetype model-discrepancy term (Kennedy and O'Hagan 2001), learned from Tier 1 vs TOUGH3 runs on the same parameters. Compute is plentiful, so run a few thousand TOUGH3 pairs per archetype before the judge goes live.

**S5. Geo-blinding will not blind (serious).** Rotating coordinates does not hide geology. Fault patterns, rock units, gravity shapes, spring chemistry and well depths fingerprint a famous site. A "name the place" probe only catches explicit recall. Implicit recall still biases which card an agent writes. And the archetype library of 300-600 cards is drawn from GRC/SGW papers written *after* many test discoveries. That leaks outcomes into card priors.
*Fix:* (a) Build a no-LLM card enumerator: every archetype x every mapped fault x a grid of upflow anchors. Run the judge on it. The council's value is the gap between council and enumerator. Memory can only enter through that gap, so leakage is bounded and measurable. (b) Make "decoy twins": perturb real prospects or plant synthetic systems with matched data. A council that scores real cases better than their twins is remembering. (c) Time-filter the card library by publication date at each freeze. (d) For the cleanest test, fine-tune an open-weights model on an open corpus with post-freeze geothermal text removed (for example OLMo on Dolma, unverified feasibility). Compute is plentiful, so this is doable.

**S6. Calibration sets are far too small (serious).** Per-archetype isotonic or Venn-Abers recalibration needs dozens of outcomes per archetype. The hindcast has 11 successes over seven archetypes. Isotonic regression on 2-3 points is noise. Conformal selection (Jin and Candes 2023) also needs exchangeable calibration data. Spatially clustered prospects are not exchangeable.
*Fix:* pool calibration hierarchically across archetypes. Calibrate mainly on graded negatives and censored columns, which number in the thousands. Use synthetic planted worlds for card-weight calibration. Use weighted conformal with spatial-block weights, and report the effective sample size next to every FDR claim.

**S7. The cheapest test's pass bar is too easy at the wrong freeze (serious).** By luck, 7 of 11 successes in the top 10 of 40 has p about 0.0015 (hypergeometric; my arithmetic). But at the *deciding-signal* freeze, a hot well or flow test is already in the file. Any distance smoother will rank those prospects high. Bar 4 is also weak. A B1 outflow card puts mass up-gradient by construction, so "more mass up-gradient than on the first hole" passes even with no skill.
*Fix:* make the *first-signal* freeze the binding test. Require the council to beat the no-LLM enumerator and SENTINEL-COX there. For upflow, score the log density at the true upflow location against the prior's density, not a binary up-gradient check. Pre-register all bars, seeds and the 40 prospects, and hash them before any run.

**S8. Feature anachronism in old freezes (moderate).** Lidar, GeoDAWN, AlphaEarth, USMTArray and INGENIOUS layers did not exist in 1980-2005. Some were built using knowledge of the systems now being tested. A 1990 freeze that uses them is not a 1990 forecast.
*Fix:* tag every layer with known_time and a "built-with-labels" flag. Run old freezes only on period-correct data. Use modern layers only in the 2015 and 2020 freezes and in prospective CSEP scoring.

**S9. Upflow location is weakly identifiable (moderate).** Upflow offset trades off against permeability, mask and outflow length. Sparse shallow data cannot separate them. The "upflow density" will mostly echo the card prior.
*Fix:* report the posterior-to-prior KL for upflow per prospect. Where it is near zero, route the prospect to a sensor plan, not a buy. That makes the weakness a VOI signal.

## What is strong

The judge-not-debater rule follows the evidence (Huang et al. 2024; Smit et al. 2024). Censored columns, a failure ladder, SBC/TARP, pending DOE sites and CSEP ledgers are the right validation stack. The design already says the council drops to a tool if it fails to beat SENTINEL-COX. That is honest.

## Score (out of 25)

| Axis | Score | Why |
|---|---|---|
| Calibrated certainty | 3 | Judge split is right; BMA, small calibration sets and leakage need S1, S2, S5, S6 |
| Data realism | 3 | Sparse prospects leave weights near prior; anachronistic layers |
| Buildable in 6 months | 3 | Enumerator, NLE and discrepancy terms add work but are standard |
| Edge vs Zanskar | 4 | Upflow and failure-mode reasoning at scale is real if it beats the enumerator |
| Drives rights and sensors | 3 | Good routing; buy list FDR claims rest on thin calibration |
| **Total** | **16** | |
