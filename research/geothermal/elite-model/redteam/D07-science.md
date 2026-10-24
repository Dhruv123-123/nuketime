# D07 PLAYBOOK: red team, scientific-validity lens

Date: 24 Oct 2026. Reviewer: science red team (identifiability, calibration, leakage, physics, honest validation). No web searches run. Facts come from D07, M33 and the L-files. Paper names from memory are marked (unverified).

## Verdict

Not refuted. Score 17/25. PLAYBOOK gives the program things it lacked: a count of what is left, element-level risk, play dependency and a lookback. The validation list is honest in shape (SBC, CSEP N-tests, reliability diagrams, decision replay, hashed forecasts). But the core discovery model [F] asks for far more parameters than about 60-120 dated Nevada systems can support. Element-level calibration cannot be done on the ledger as it stands. Two of the three pass bars could pass on noise. Every flaw has a fix. None is fatal.

## Flaws and fixes

**S1. The multi-channel hazard is not identified (serious).** h_ic = E_c x q_c x S^beta_c x L^gamma_c x g_c, per play, per channel. With 150-300 plays and 4-7 channels, most play-channel cells hold zero or one find. Three trade-offs are built in. q_c and the scale of E_c are confounded. N_p and q_c trade off, as in any capture model with no recaptures. beta_c and gamma_c both act on unseen latents (S, L) for every unfound system. So the posterior on N_remaining per play will mostly echo the priors.
*Fix:* fit [F] at province level first, with channel effects shared across plays. Anchor gamma_c with physics: leakiness is partly observed (spring discharge, outflow chemistry, heads). Anchor q_c with designed survey cells where effort is known exactly (our 2 m grids, the OFR 99-425 TG grids), like a removal-sampling design. Report prior-to-posterior contraction for N_p and each beta_c. Where contraction is under about 30%, print "prior-dominated" in the book.

**S2. Size marks are endogenous and missing not at random (serious).** Only about 18 Nevada fields have a size mark. Nameplate depends on when the field was built, on ITC policy and on developer choice, not only on the resource. The 78 known and 99 probable systems have no MW. Fitting beta_c on built fields learns "what got built", which M33 already flags (blind median 45 MW partly because only big blind fields get built).
*Fix:* make size a latent with a measurement model. Use AI extraction of flow tests, reservoir temperatures and geothermometers to give soft size marks to undeveloped systems. Model "built" as a separate selection step with its own covariates (price era, transmission).

**S3. Element calibration is not possible from the failure ledger (serious).** Pg = product of five element chances, each isotonically calibrated. But most dry-hole reports never name the failing element. Only the product, or a coarse outcome, is observed. The product also assumes independence. Heat and fluid, and pathway and freshness, are physically linked. Independence makes Pg too low for good prospects and too high for bad ones.
*Fix:* calibrate Pg and the coarse outcome class only. Treat the five-row card as a posterior decomposition, with contraction shown per element. Use physics to separate causes: an AI classifier on extracted temperature-log shape (conductive gradient = heat but no flow; reversal = outflow or lid; isothermal = convective). Model element dependence with a copula or a shared latent, as Van Wees 2008 does in oil (unverified detail).

**S4. The failure ledger is a biased sample (serious).** Holes were drilled where someone thought it was good. Failures are under-reported. Calibration on drilled ground does not transfer to undrilled ground.
*Fix:* weight by a modelled drilling propensity (the crowd posterior is already that model). Add a small design-based sample: our own TG holes at random points inside high-Pg strata. Even 20-30 such holes give an unbiased calibration check.

**S5. [E] and [F] use the same data twice (moderate).** Unfound locations are drawn from the Pg map. Pg is trained on evidence near known finds. [F] then uses the same finds. This narrows the posterior on N.
*Fix:* a cut posterior (modular Bayes; Plummer 2015, Jacob et al. 2017, unverified) so [E] feeds [F] one way, or a single joint factor graph where each datum enters once. Test by deleting each source and checking the posterior widens.

**S6. Monotone constraints break physics in masked plays (moderate).** "More heat flow cannot lower P(heat)" holds at the measured depth, not at target depth. Outflow plumes give high shallow heat flow over no upflow. Cold-aquifer lids (B4) and rain curtains (B5) give low shallow gradient over hot rock.
*Fix:* make the constraint apply to the column posterior P(T(z_target) crosses the line), not to raw heat flow. Or apply monotone constraints only within each mask class.

**S7. Evidence quality leaks the label (moderate).** Data density and kriging variance are highest near known systems, because surveys followed finds.
*Fix:* let quality act only as a shrinkage weight toward the play prior, never as a predictor. Ablate it in hindcasts. Use known_time of each survey, as the bitemporal store already allows.

**S8. The pass bars are weak (serious, easy to fix).**
- Bar 1: "count inside the 90% interval" passes for any wide interval. "Springs beta_c interval includes 0" passes for any vague posterior, and M33 drew that result from the same data, so it is circular.
- Bar 2: post-2008 MW is dominated by McGinness Hills (about 160 of 425 MW). One play decides the test.
- Bar 3: about 10 blind finds. A 2x lift with a bootstrap interval that excludes 1x is very unlikely at n=10, even if the model is good.
- Hindsight leak: the channel list (mining holes) was chosen because we know mining holes found McGinness, Blue Mountain and Don A. Campbell.
*Fix:* add a sharpness bar (90% interval width no more than about 2x the observed count). Score MW with CRPS and leave-one-system-out. Raise n: use the 99 probable systems, other provinces (Utah, Oregon, Idaho) frozen the same way, and TG-hole-level outcomes (thousands of holes) for Pg reliability. Pre-register the channel list, play splits and priors in a hashed file before fitting. Run a power analysis first, so a null result means something. Report both "conditional on realised effort" (science test) and "with forecast effort" (decision test).

**S9. The crowd model is not the crowd (moderate).** "Our model refit on public layers" is a guess at rival beliefs. Edge = difference of two noisy models, so winner's curse grows.
*Fix:* fit the crowd model to revealed preference: BLM all-bids prices, nomination timing, lease survival. Validate it by predicting next-sale bids.

**S10. The size haircut is ad hoc (minor).** The 0.5-0.7x factor comes from oil. Keep it a scenario axis; replace it with the lookback.

## What is strong

Bitemporal store, purge and embargo, SBC, CSEP scoring and the hashed lookback are best practice. Unfound systems as survival, not negatives, is correct. "The curve steps up when we deploy, else kill" is falsifiable.

## Scores

Calibrated certainty 3/5. Data realism 3/5. Buildable in 6 months 3/5. Edge vs Zanskar 4/5. Drives rights and sensors 4/5. Total 17/25.
