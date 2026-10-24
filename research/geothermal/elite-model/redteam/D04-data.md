# D04 TWIN-WEST: red team, data-reality lens

Date: 24 Oct 2026. Reviewer: data-reality red team. The shared web-search budget was used up when this agent ran, so no new searches were made. Numbers come from the L-files (L02, L11, L12, L19, L36) and v1 evidence (M05, M08, M16, M18). My own estimates are marked (unverified).

## Verdict in one paragraph

TWIN-WEST is not refuted. Of the designs so far, it copes best with having only ~100-200 confirmed systems. It needs no class labels. Every cold well, reversal and dry hole counts as data. But it is a 1.9 x 10^8-voxel, ten-field state fed by perhaps tens of thousands of shallow, clustered, mostly single-point readings. In most of the West, the "reanalysis" will be the generator prior with a 3D look. Two parts still lean hard on the small label set: the generator's mixing weights and the discovery layer. Its flagship hindcast also has a leak in the generator inputs. Each flaw has an AI-leveraged fix. Score: 17/25.

## Flaws and fixes

**F1. The ERA5 analogy breaks on data density (serious).** ERA5 takes in millions of observations a day, and its dynamics carry information between them. A steady-state crust has no dynamics, so nothing moves information from where we measured to where we did not, except the prior and spatial correlation. Count what is really there. The Great Basin has 379 clean conductive wells, about one per 1,400 km2 (M05). The SMU node has about 14,000 equilibrium sites West-wide, clustered near known fields (M05). Prospect-scale MT covers under 2% of the ~1,430 FSS (M08). USMTArray is on a 70 km grid. Most cells will see no data below 300 m. Calling the output a "reanalysis" and selling it as a product overstates what it knows.
*Fix:* for every voxel, publish the information gain (KL from prior to posterior) and a "data-supported" mask. Sell and price only voxels above a set gain threshold. Elsewhere, sell the prior plus the OSSE answer to "what would one sensor tell you here". Show this in every map and data-room pack.

**F2. Operator residuals and rock physics rest on about five paired sites (serious).** The learned residuals are trained on FORGE, Coso, Brady, Kakkonda and Wairakei. Two are outside the US, and Coso data are largely Navy-restricted (unverified). Public places with both resistivity and measured temperature in the same spot are "the scarcest input in this whole problem" (M08). A flexible residual fitted on five sites will overfit those sites' geology.
*Fix:* keep the residuals low-capacity, with hierarchical shrinkage toward the pure-physics operator. Pretrain on global open well-plus-MT pairs (NZ, Iceland, Kenya), as the design's `global` row already says. Make the first OSSE batch buy pairs on purpose: each E-MT carpet tied to a TG hole gives a private resistivity-temperature label (M08). AI extraction of old MT reports with logs nearby can add maybe 20-50 more pairs (unverified).

**F3. The generator inherits label bias (serious).** The FSS enrichments (DTZ 4.8x and so on) and plume statistics were fitted on known systems. Known systems are mostly shallow outflow that leaked or was hit by accident: 100 C sat above ~300 m in nearly every historic case (M18). If the world generator learns its weights and plume shapes from these, it will under-produce deep, sealed blind systems like Big Blind (823 m) and Pumpernickel (760 m). Then no amount of assimilation can find them, because posterior support cannot exceed prior support.
*Fix:* tie the generator's play-type weights to physics, not counts. Sample permeability and sealing clocks from a wide range, and keep the max-entropy "unknown play" share at 10-20% or more. Fit the mixing weights through the discovery likelihood with per-mask detection rates (the PULSNAR-style SNAR subtypes in L19), so the shallow bias is modelled, not learned in. Check that synthetic Wests reproduce the M18 depth-to-100 C distribution once the historical search is replayed.

**F4. The discovery layer is weakly identified (serious).** It must fit q_c for three channels, by depth and mask class, from about 205 USGS systems (28 producing, 78 known, 99 probable; L36). Only about 13 have a documented first-signal year (M18). The effort data E_c(s,t) is patchy. NDWR and OSWCR well reports are dated. MRDS and MLRS mining records often lack dates and depths (unverified). The oil-company gradient programs that found Desert Peak are mostly proprietary.
*Fix:* AI agents extract first-signal year and type for all 205 systems from OSTI, GRC and NBMG text. Rebuild mining effort from dated imagery: historical aerials and Landsat from 1984 show drill pads and roads (unverified yield). Put informative priors on q_c from synthetic Wests with known truth. Report detection rates with their uncertainty, and let the count forecast widen to match.

**F5. The cheapest test leaks through the generator (serious, fixable).** The 2005 hindcast freezes observations. But the generator uses the INGENIOUS-era FSS polygons, Faulds' enrichments, NSHM 2023 and GeoDAWN magnetics. All of these postdate 2005, and several were drawn knowing Gabbs, Granite Springs and McGinness. That is feature-vintage leakage (L19). With only 7 test finds, one leaked prior could pass the test alone. Also, a random map puts 4 of 7 in the top 5% only about 0.02% of the time (calc). So the right bar is to beat an FSS-only baseline, not chance.
*Fix:* build a leave-one-out generator. Refit the enrichments without each test system. Have an agent re-map FSS only from geologic maps that existed before the freeze. Add a pass condition: beat the Faulds FSS ranking and the USGS 2008 favourability map at equal area.

**F6. Permeability observations are thin outside known fields (moderate).** Lost circulation, flow tests and helium cluster at developed fields. Rural Nevada seismic detection (Mc) is too coarse to see small swarms everywhere (unverified). So permeability will stay close to the prior in blind areas, as Krafla suggests (L11).
*Fix:* this is where OSSEs earn their keep. Let VOI target the permeability term with nodal seismic arrays, slim-hole tests and ranch-well chemistry.

**F7. Heads are not "hard" boundary conditions (moderate).** NWIS water levels sit in farmed valleys. Ranges and carbonate flow systems are nearly blank. Treat heads as soft data, and draw the regional carbonate flow from the USGS regional flow models as an uncertain prior.

**F8. The flow-disturbed wells are mostly single points (moderate).** Most of the 4,293 discarded wells (M05) are a gradient or a BHT, not a profile. The reversals and isothermal sections the design wants are in scanned field notes (M05).
*Fix:* run the D03 Stage 0 yield test first. Extract 1,000 random scans, measure how many give usable profiles, and size the 3D work from that number.

## Does it survive ~100-200 systems?

Yes, better than the label-trained designs. Temperature, resistivity and chemistry carry the physics, and they do not need system labels. The count, detection and play-weight parts still depend on the small set, so their error bars must stay wide and be shown. Keep the design. Fix F3 and F5 before the first test.

## Score (data lens)

Calibrated certainty 4. Data realism 3. Buildable in 6 months 2. Edge vs Zanskar 4. Drives rights and sensors 4. **Total 17/25.**
