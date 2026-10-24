# D03 STRATA-West: red team, scientific validity lens

Date: 24 Oct 2026. Reviewer: science red-team agent. Scope: identifiability, calibration, leakage, physics consistency, and whether the certainty claims can be checked honestly. No web searches. Facts come from D03 and the L-digests. My own judgements are marked (unverified) where they need a check.

## Verdict in one line

Not refuted. The design is ambitious but sound in principle, and every flaw below has a credible AI-leveraged fix. As written, though, its certainty claims are stronger than its validation plan can support. The first test (Section 13) has a leak that would make it pass for the wrong reason. **Score: 16/25.**

## Flaw 1 (serious). The cheapest test leaks through its own inputs

Section 13 freezes at 2015 but feeds in GeoDAWN magnetics and AEF embeddings. GeoDAWN was flown in 2022 (unverified date). AEF exists only from 2017 onward (L20). So neither is legal for a 2015 freeze. AEF is worse than illegal. It sees roads, pads and disturbance. L20 shows this footprint leaks labels. Projecting out a "built-infrastructure direction" is a linear fix for a nonlinear signal. The Faulds FSS catalogue is also partly built from known systems, and some of those were found after 2015.

**Fix.** Have an agent write a freeze-legality card for every layer: when it was acquired, when it was published, and whether known systems shaped it. Swap in time-legal versions. Use pre-2015 aeromagnetic compilations instead of GeoDAWN. Train our own Landsat 5/7 embedding on 2000-2014 imagery instead of AEF. Rebuild the FSS mapping with an agent that sees only pre-freeze papers. Then run a second test with the illegal layers switched back in. The size of the gap is a direct measure of the leak.

## Flaw 2 (serious). Token density is a data-presence mask inside the backbone

The firewall (4.9) sends data-presence masks to the effort head only. But the backbone eats raw tokens. The number of tokens in a voxel *is* the data-presence mask. Drillers, MT crews and chemists swarm around known fields. Masked reconstruction will learn "dense data means hot". The lat/lon-only probe in the pass bar cannot catch this.

**Fix.** Add a probe that predicts labels from token counts per cell, by modality and by year. It must score AUC under 0.6. Train with density-matched subsampling: cap the tokens per km² so a field and a blank basin look alike in volume. Add a gradient-reversal adversary on token count in the latent. This is cheap and fully automatable.

## Flaw 3 (serious). The deep 3D latent is mostly not identifiable

Almost all real data is surface or shallow. Most wells are under 300 m. A 6 km voxel field has about 3x10^8 cells. In a hidden-system cell, the 2-6 km state is set by the Westlet prior, not by data. The physics core makes this worse in one way. A learned heat source and a learned permeability field trade off against each other. A hot deep source with low k and a cooler source with an upflow fault can fit the same shallow gradient. That is the classic Peclet non-uniqueness.

**Fix.** Use the synthetic stage to draw an identifiability map. For each voxel and data set, compute posterior contraction (prior variance over posterior variance) on Westlets that look like the real cell. Publish depth claims only where contraction passes a set bar. Elsewhere the map should say "prior". Sensors then target the low-contraction voxels, which turns the weakness into the EIG engine. Penalise the learned residual heat source. Bound it to radiogenic and basal-flux ranges. Report what share of variance the residual explains. If the residual explains most of it, "physics-consistent" is cosmetic.

## Flaw 4 (serious). Synthetic calibration checks only self-consistency

SBC and TARP on 1,000 Westlets (Section 7) will pass if the model matches its own simulator. That says nothing about Nevada. Westlet archetype frequencies and the simulated search history become priors that drive blind cells. DPS posterior sampling is also an approximation, and it tends to give too little spread (unverified for this setting).

**Fix.** Build at least two simulator families: Noddyverse plus FSS, and an independent agent-built family drawn from published conceptual models. Train on one and test on the other. Run prior-sensitivity sweeps on archetype base rates and report how much the buy list changes. Gate the final bands with spatial conformal calibration on real held-out blocks, not on synthetic ones. Run the MMD misspecification test (L28) per cell and route failures to the v1 column likelihood, as the design already proposes.

## Flaw 5 (serious). The discovery hindcast has no statistical power

Post-2015 blind finds in the Great Basin number about 4-10. The pass bar is "at least as many in the top 5% as LightGBM". With n near 6, a tie passes and a lucky one-find edge looks like skill. The designer has also named Big Blind and Pumpernickel in advance. Every design choice since then was made with those answers in sight. That is a forking-paths problem.

**Fix.** Move the main hindcast target from rare finds to thousands of post-freeze temperature readings. Many TG holes, water wells and geothermal wells were drilled after 2015. Score CRPS on each one, stratified by depth, with kNNDM blocks. Add the pre-drill-vs-outcome table (hundreds of rows). Keep discovery capture as a secondary test with exact binomial intervals. Pre-register the pass bars, the freeze year and the baselines on OSF before training. Hand the hold-out to a separate agent that holds the keys. Then add a forward test: the hashed ledger before each BLM sale is the only test nobody can tune to.

## Flaw 6 (moderate). Springs and sinter routed only to effort throws away real evidence

Springs and sinter are proof that heat reached the surface. Routing them only to P_det blinds λ to a strong existence signal. In a thinned Poisson model only the product λ·P_det is identified unless each side has covariates the other lacks. Putting a dual-meaning covariate on one side biases both.

**Fix.** Let springs enter both terms through a stated structural model. The existence side uses chemistry geothermometers and flux. The effort side uses "was it visible and visited". Run a sensitivity table across routing choices.

## Flaw 7 (moderate). Four uncertainty layers can double count

Aleatoric decoders, 8-16 ensemble members, 50-200 diffusion draws and a distance-aware head are stacked with no rule for combining them. Each layer is reasonable. Together they can overlap, giving bands that are too wide, or they can share a bias, giving bands that are too narrow. The PIT target of under 3% by depth band will have thin samples below 2 km.

**Fix.** Combine the layers once, then recalibrate the whole output end-to-end with spatially weighted conformal calibration per depth band. Report effective sample size per band. Where it is too small, say so instead of claiming a calibrated number.

## Flaw 8 (moderate). The crowd-posterior gap shares the backbone's errors

Fine-tuning the same backbone on public layers does not model what rivals know. Both RNPVs share the same bias, so the gap can look confident when it is not. The winner's curse lives exactly in this gap.

**Fix.** Calibrate the gap against what actually happens: BLM sale prices, nominations, and rival leases from MLRS. Treat the crowd model as a fitted model of observed bids, not as an assumption.

## Scores

| Axis | Score | Why |
|---|---|---|
| Calibrated certainty | 3 | Strong gates on paper. Synthetic SBC, a hindcast with low power and density leakage weaken them. |
| Data realism | 3 | Freeze-illegal layers in the first test; billions of tokens is an estimate (unverified). |
| Buildable in 6 months | 2 | Three freeze-year 1B backbones, 10^6 Westlets and a West-wide build in 6 months is very tight. Mini-STRATA is doable. |
| Edge vs Zanskar | 4 | Raw curves, depth and EIG are real differentiators if the test passes. |
| Drives rights and sensors | 4 | EVSI per sensor per cell is a direct link. Identifiability maps make it sharper. |
| **Total** | **16/25** | |

## What would raise it

Fix Flaws 1, 2 and 5 before the $10-20k test runs. All three are cheap. Then a pass means something.
