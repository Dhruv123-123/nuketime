# D01 SCX2: red team, data-reality lens

Date: 24 Oct 2026. Reviewer: data-reality red team. The shared web budget was used up before my searches ran, so numbers come from repo evidence (M05, M06, M08, M18, M19, D01's L-file citations). Anything I did not check is marked (unverified).

## Verdict

SCX2 is not refuted. Its core is the right shape for a world with only 100-200 confirmed western systems. Most of its parameters are fit from non-label data: tens of thousands of temperature readings, simulations, and effort records. Only a few weights rest on system labels. But the design overstates how much each component can learn. Three places break on contact with the real data. The four-field product is not identifiable from presence labels. The conformal buy list and the Freeze-2008 pass bar have too few positives to mean anything. Several "always-on" layers (AlphaEarth, lidar, ICE) leak in hindcasts. All have AI-leveraged fixes. Score: 15/25.

## Where the data is too thin

**F1. Four fields, one label stream (serious).** log lambda = H + P + F + C, each a GP, "weights learned hierarchically across provinces". Presence points identify only the sum. With about 200 systems, about 11 archetypes and four GP fields, the split between "heat" and "pathway" is set by priors, not data. The "weakest link" display, the design's main sales feature, would then be prior made to look like a finding.
*Fix:* give each field its own data. Heat learns from the about 22,535 Great Basin temperature wells (Burns 2024, via M05) and censored TG holes. Pathway learns from AI-extracted lost-circulation notes, flow tests, He R/Ra and slip data. Cap learns from MT and airborne EM. Existence labels then fit only the 4-8 coupling weights. Report the posterior-to-prior contraction per field, and grey out any field that did not move.

**F2. Column engine will mostly run on its fallback (serious).** Only 379 Great Basin wells pass every USGS quality test, about 38 km apart. Under 10% of the West has any subsurface temperature. In 90% of sampled 1 km cells the only wells are shallower than 20 m (Edwards 2025, via M06). The Simformer gets one or two shallow censored tokens for most cells. That is correct behaviour for amortised inference, but it means the 10^6-run simulator bank mostly returns the prior. Value comes only from the few percent of cells with deep data.
*Fix:* accept it and price it. Use the Simformer's expected information gain per cell as the sensor-routing signal. Spend the 10^6 runs on what a 2 m probe, dart or re-log would add, not on what is already there. Report "cells with real column evidence" as a headline number.

**F3. The MT "West-wide atlas" does not exist at prospect scale (moderate).** USMTArray has about 1,711 stations on a 70 km grid. It sees 2-200 km, not clay caps. Prospect MT covers a few dozen areas, mostly private (M08). A trans-D atlas over public EDIs is a deep-heat prior, not a cap field.
*Fix:* rename it a deep-conductor prior. Feed the cap field from Earth MRI airborne EM (about 400 m depth) where flown, plus our own E-node carpets. Every carpet tied to a TG hole becomes a private resistivity-to-temperature label.

**F4. Archetype and failure labels per class are tiny (moderate).** About 39% of known Great Basin systems are blind, and about 60% were found by surface discharge (M19). Split by B1-B7 plus EGS, magmatic and rift, most blind classes get 0-10 cases. The failure ladder needs flow-test outcomes that M29 says no public table links to pre-drill data.
*Fix:* fit archetypes on simulation plus about 300-600 conceptual-model figures extracted from GRC/SGW. Pool classes hierarchically. Treat failure modes as partly observed latents built from AI-tagged NDOM (159 out-of-field wells) and CalGEM (1,586 plugged TG holes) records.

## Where the validation cannot see

**F5. The Freeze-2008 duel has about 3-5 real targets (serious).** Gabbs Valley, Granite Springs and Big Blind are genuine map-first finds. Pumpernickel had 1970s O&G and federal holes before 2008 (M18). San Emidio SW is a step-out from a known field, so the distance smoother gets it for free. Granite Springs 68-02 may still be unconfirmed (unverified). "2x the XGBoost capture in the top 5% with CI above 1" on 3-5 points is a coin toss. With 3 targets, 2 against 1 gives a bootstrap CI that spans 1. The 99 probable systems help, but they are mostly springs, which SCX2 bans from the existence term, so they test the wrong class.
*Fix:* make the main score a temperature score, not a discovery count. Hold out post-2008 TG, NDOM and NBMG logs (thousands of depth-censored readings) and score log-likelihood of T(z) at 0.5-1 km. Add a synthetic-world score on GHOST worlds with real effort geometry. Keep blind capture as a reported line, not a pass bar.

**F6. Conformal FDR has no resolution (serious).** Conformal p-values have a floor of 1/(n+1). With about 10 blind calibration positives, the smallest p is about 0.09. BH at 10% FDR then can reject almost nothing. The "conformal false-discovery guarantee" on the buy list is empty.
*Fix:* run conformal selection on a measurable outcome: "T at 1 km above 120 C", calibrated on thousands of held-out wells by kNNDM block. State existence FDR only from the design-based field sample in section 6, which grows by about 40-100 cells a year.

**F7. Hindcast leakage through "timeless" layers (serious, fixable).** AlphaEarth embeddings start about 2017. 3DEP lidar and GeoDAWN are post-2010s. All three show well pads, roads, pipelines and plants at fields found after 2008. Projecting out one "built" direction will not remove a 64-d pad signature. ICE (4.7 C MAE) was pretrained on wells drilled after every freeze. LST and EMIT show surface disturbance too.
*Fix:* for each freeze, mask a 2 km buffer around every post-freeze pad from MLRS, NDOM and CalGEM permits, or drop these layers from hindcasts. Retrain ICE-West per freeze on known_time-filtered wells, which is cheap at its size. Let the leakage agent run a "predict discovery date from features" probe. If it beats chance, the layer leaks.

**F8. known_time is ambiguous (moderate).** Industry knew the 786 Phillips/Chevron TG holes around 1980. The public got them in 1999 (OFR 99-425). The NBMG scans were public for decades but unread.
*Fix:* store two dates: industry_known and public_known. Run the crowd model on public_known and the rival model on industry_known.

**F9. The crowd posterior underestimates Zanskar (moderate).** Zanskar holds its own TG holes, a 370-site inventory (M13) and digitised archives. A "public-only" refit is a floor on rival knowledge, not an estimate of it. Leak cost will then read too low near Zanskar's acreage.
*Fix:* add a rival-knowledge term fit from where Zanskar and Ormat nominate, bid and permit. Treat their acreage as a positive-only signal of their private posterior.

**F10. Seismic re-picking is limited by stations, not by algorithm (minor).** Rural Nevada spacing is tens of km outside the 2006-08 Transportable Array window. Focal mechanisms for M<1 events need close stations.
*Fix:* re-pick the TA window hard and use those mechanisms as the stress prior. Elsewhere use GNSS strain plus fault geometry.

## Survives 100-200 systems?

Yes, if labels are demoted. SCX2 already uses censored columns, graded negatives and effort. The fixes above move all calibration and gating onto temperature and onto synthetic and design-based samples. System labels then set only a few weights and the province N_hidden check.

## Score (out of 25)

| Axis | Score | Why |
|---|---|---|
| Calibrated certainty | 3 | Right tools (SBC, TARP, kNNDM). FDR and pass bar too thin as written. |
| Data realism | 2 | MT atlas, four-field split and duel targets overstate the data. |
| Buildable in 6 months | 2 | Seven engines on 8-10 people; the Cox core and duel are doable. |
| Edge vs Zanskar | 4 | Censored negatives, effort and extraction are real edges. |
| Drives rights and sensors | 4 | Pandora value, leak routing and sensor-by-hurdle are well tied. |
| **Total** | **15** | |
