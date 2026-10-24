# D04 TWIN-WEST: red team, scientific validity lens

Date: 24 Oct 2026. Reviewer: science red-team agent. Scope: identifiability, calibration, leakage, physics consistency, and whether the certainty claims can be checked honestly. No web searches. Facts come from D04 and the L-digests. My own judgements are marked (unverified) where they need a check.

## Verdict in one line

Not refuted. TWIN-WEST is the most physically honest design so far, because every reading is a likelihood on one state. But its validation plan mostly tests the model against itself, its count layer has a classic identifiability trap, and its first test can be passed by luck or by tuning. Each flaw has an AI-leveraged fix. **Score: 16/25.**

## Flaw 1 (serious). The validation is an "inverse crime"

Gate 1 draws a "true" West from the Westlet generator and inverts it with surrogates trained on the same generator. SBC, TARP and the 70% recovery target will pass if the code is bug-free. They say nothing about Nevada. The quoted coverage numbers (EKI 94.7%, DSI 92-93%; L10-L12) are also in-simulator results.

**Fix.** Build OSSE truths from a different world. An agent rebuilds published, calibrated natural-state models (Wairakei, Ohaaki, Brady, Desert Peak, Coso, Krafla; old TOUGH2 decks from OSTI) on a different mesh and code. Run TWIN-WEST blind on synthetic data drawn from those. Report coverage on "foreign truths" next to "own truths". The gap is the misspecification cost, and it is a number we can publish.

## Flaw 2 (serious). The cheapest test leaks and can be tuned to pass

Section 13 freezes keyed data at 2005. But the generator is not frozen. The Faulds FSS catalogue and its enrichments (DTZ 4.8x, pull-apart 2.2x) were fitted on known systems, including post-2005 finds like McGinness and Don A. Campbell (unverified which were in the training set). The 8 FSS templates, the Qfaults update and GeoDAWN magnetics are post-2005 too. Worse, Section 13 says a fail means "widen the generator", then re-run. That is a garden of forking paths. After three loops the hindcast is a training set.

**Fix.** An agent writes a freeze-legality card per layer and per generator choice: acquired, published, and shaped by which known systems. Refit FSS enrichments with post-freeze systems removed. Put the 2015 and later finds in a lockbox: hash the scoring script and the generator version before any look. Allow generator changes only on the 1980-2005 window. Run once with illegal layers switched back on; the gap measures leakage.

## Flaw 3 (serious). The pass bar is weak and the sample is tiny

Seven blind cases, 4 needed in the top 5% of Nevada. Random gets 0.35 expected. But random is the wrong baseline. Most blind cases sit in mapped FSS polygons, so a Faulds favourability map alone may pass (unverified). With n=7 the 95% interval on a 4/7 hit rate runs from about 18% to 90% (calc). That cannot separate TWIN-WEST from INGENIOUS.

**Fix.** Make the baseline Faulds plus INGENIOUS favourability plus v1's column model, and require a margin over them. Grow n. Every well drilled after the freeze is a test point (thousands of T readings), every NBMG geothermal permit is a dated event, and the CSEP N/L/S tests run on counts. Add the Zanskar-public "GeoCore" wells as a held-out set.

## Flaw 4 (serious). Count and detection rate trade off

The discovery layer fits the number of hidden systems N and detection rates q_c together. In capture and occupancy models, N and detection are confounded unless effort varies strongly in time and space. Effort here is also endogenous: people drilled where springs were warm. Effort is caused by surface leakage, which also drives q_c. So "searched hard and found nothing" can mean no systems or low q.

**Fix.** Use the dated record as a depletion curve (Leslie / catch-per-unit-effort): the slope of finds against cumulative effort pins q. Put informative priors on q from the M18 blind-case table. Add an effort model that depends on surface leakage, so the confounding is in the likelihood, not hidden. Run an OSSE that asks: can we recover N within 30% when truth is known? If not, report N as prior-dominated.

## Flaw 5 (serious). Permeability and deep heat are not identified

Most data are under 300 m. A hot deep source with tight rock and a cooler source with an open fault give the same shallow gradient. P(upflow) uses a Darcy flux threshold, so it rests on the least identified variable. Krafla shows k spread over two orders of magnitude even with many wells (L11).

**Fix.** Publish a posterior-contraction map by depth and variable. Claim depth or P(upflow) only where contraction passes a bar; elsewhere say "prior". Point the OSSE engine at low-contraction cells. That turns the weakness into the sensor plan.

## Flaw 6 (moderate). Ensemble methods understate spread

ES-MDA with 64 members on about 1.9e8 voxels is rank-poor. It assumes near-Gaussian updates, but faults and plumes are near-binary. ES-MDA is known to collapse spread (Emerick and Reynolds 2013, unverified for this setting). With 64 members, P(upflow) moves in 1.6% steps, too coarse for a 2% tail. Overlapping tiles can also count the same reading twice.

**Fix.** Assign each reading to one tile (partition of unity). Run three samplers on the same tiles (ES-MDA, DPS, delayed-acceptance MCMC with the true simulator) and report their disagreement as extra spread. Use importance resampling for rare upflows.

## Flaw 7 (moderate). Surrogate error and learned residuals can eat the signal

FNO error of about 7% relative L2 on unseen faults (L11) is roughly 10-15 C at 200 C (calc), far above log noise of 0.5-1 C. It is structured, not white noise, so adding it as noise miscalibrates. The learned observation residuals and the GP discrepancy term also face the Kennedy-O'Hagan problem: a flexible discrepancy can absorb a real anomaly (Brynjarsdottir and O'Hagan 2014).

**Fix.** Train a spatial error model on the surrogate. Verify accepted samples with the true simulator (delayed acceptance). Bound the discrepancy prior and test in OSSEs whether it hides planted systems. Train BHT and residual nets only on pre-freeze, non-test wells.

## Flaw 8 (minor). Steady state is the default

Many Great Basin systems are transient fault pulses. A steady prior may score a young pulse as impossible. D04 already plans transient draws. Make the share a learned hyper-parameter and test it on known young systems.

## What holds up

Censored likelihoods on cold holes, flow-disturbed wells as data, effort in the likelihood, the crowd posterior and pre-registered hashed forecasts are all strong. Granite Springs 68-02 is a good first live test if hashed before results.

## Score

| Axis | Score |
|---|---|
| Calibrated certainty | 3 |
| Data realism | 3 |
| Buildable in 6 months | 2 |
| Edge vs Zanskar | 4 |
| Drives rights and sensors | 4 |
| **Total** | **16/25** |
