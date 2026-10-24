# D08 UNDERCAST: red team, data-reality lens

Date: 24 Oct 2026. Reviewer: data-reality red team. No new web searches. Facts come from D08, L03, L10, M07, M08, M16 and the D07 data review. My own estimates are marked (unverified).

## Verdict

UNDERCAST is not refuted. Its best data idea is sound: supervise on every held-out reading, not on ~106 system labels. That is the one design so far that does not starve on 100-200 confirmed systems. But the readings it learns from sit almost all in the top 300 m, near towns, roads and known fields. At the depths that set value (1-3 km), the "reanalysis" is mostly the synthetic prior talking. The prior itself is tuned on a few dozen published field models, all of leaky, found systems. Every flaw below has an AI-leveraged fix. Score: 16/25.

## Flaws and fixes

**F1. Deep data is very thin, so the state below 1 km echoes the prior (serious).** In the LANL ICE set only 3% of readings are deeper than 4 km and over 95% of wells have one reading (L10). Burns 2024 kept 379 clean conductive wells out of 4,672 deeper than 50 m (L03). Water-well and TG data stop at 50-300 m. "Hide the deep half of each log" works only for the few hundred multi-depth logs, and those cluster at known fields.
*Fix:* make the per-voxel "data-driven share" (D08 risk 2) a hard gate, not a footnote. Compute it as the KL from prior to posterior per voxel. Never let a buy decision rest on voxels below a set share; route them to VOI for a TG or slim hole instead. Extend deep supervision with AI extraction of oil, mining and geothermal logs (NDOM, DOGM, CalGEM, SMU scans) and with geothermometer circulation depths (DeAngelo 2025, doi:10.5066/P14B8XOH) as deep soft anchors.

**F2. The synthetic prior learns its world from found, leaky systems (serious).** Westlets are seeded from Faulds' FSS templates and archetypes drawn from published conceptual models. Public natural-state models exist for perhaps 20-40 Western fields (unverified). Almost all were found by springs. Blind systems with cold lids, deep outflow and masking aquifers are the target, but they are 4-8 examples (Big Blind, Pumpernickel, McGinness, Gabbs, Granite Springs). The generator's mix of archetypes, their sizes and lid depths has no data to fit them. A diffusion prior trained on a wrong mix gives confident, wrong posteriors where data is thin, which is exactly F1's zone.
*Fix:* treat archetype frequencies and geometric hyperparameters as unknowns. Fit them by simulation-based inference against real held-out readings (posterior-predictive checks per tile), with agents searching the generator space. Import global analogs: NZ (GNS, Contact), Iceland, Kenya and Turkey natural-state models and MT-well pairs, extracted by agents from WGC and SGW papers.

**F3. Forward operators have few calibration pairs (serious).** MT to temperature needs MT and a measured log at the same spot. M08 calls these "the scarcest input in this whole problem". Prospect MT exists for a few dozen Great Basin areas, mostly private (Gabbs 59 stations, East Hawthorne 61). USMTArray is 70 km spacing and blind to caps. Permeability has almost no public labels: flow tests are confidential, lost circulation is sparse in driller logs. Helium isotopes exist at only a few hundred sites (M07). So the MT, permeability and helium decoders will be fit to tiny sets and the global analogs.
*Fix:* fit the rock-physics operators hierarchically, pooling Iceland, NZ and Kenya pairs with a West-specific offset and a false-conductor mixture. Make every own sensor campaign co-locate E-MT nodes with TG holes, so each campaign creates private pairs. Buy or license dead-company data rooms (bankrupt developers, expired DOE cost-share projects), extracted by agents.

**F4. Observations are spatially clustered and biased toward known fields (serious).** Deep logs, MT and chemistry pile up at Steamboat, Dixie, Coso, Roosevelt and Brady. Chemistry follows towns and roads (24,769 NBMG samples, M07). Held-out CRPS under kNNDM will be dominated by easy, data-rich tiles. A 15% CRPS win there says little about blind valleys.
*Fix:* weight the CRPS gate by inverse data density and report it on tiles with no system within 20 km. Add a "pseudo-blind" test: strip surface manifestations and shallow wells within 5 km of each of the ~106 known systems, then score recovery. That turns 100-200 systems into a usable blind set, with known leakage noted.

**F5. Point-in-time is hard to reconstruct (moderate).** Many sources are merged compilations with no per-record "known date" (the 2006 NBMG chemistry compilation, SMU heat flow, GDR uploads years after collection). Gabbs Valley MT is 2020, so a 2015 freeze must drop it. The pass bar (4) rests on two cells.
*Fix:* agents date each record from its source report, with a date-uncertainty field; drop records that cannot be dated from pre-freeze runs. Replace the two-cell bar with Molchan area capture over the pseudo-blind set plus 4-8 true blind finds, and pre-register each season.

**F6. West-wide coverage is uneven (moderate).** Nevada has NBMG, NDWR and GeoDAWN lines. Oregon, Idaho and Wyoming have far fewer logs; GeoDAWN covers only part of the Walker Lane; California's best data sit in CalGEM scans.
*Fix:* phase by data density (Nevada and western Utah first, as the plan already says). Use the data-driven share to set where the business acts, and price TG and E-MT campaigns in the thin states by EVSI.

**F7. Effort and size marks for the Cox and MW heads are thin (moderate).** As in D07, dated search effort by channel and size marks (~20 EIA-860 nameplates) are sparse.
*Fix:* one size slope with channel offsets under a global prior; use USGS 2008 per-system MWe triangles as noisy marks; keep MW/km2 as a physics output of the core, not a fitted head.

## Does it survive 100-200 systems?

Mostly yes. Temperature supervision runs on hundreds of thousands of readings, so the T(z) heads do not need system labels. The existence, archetype and MW heads do, and they inherit D07's thin-label problem. The real limit is not label count but the depth and placement of readings.

## Scores (out of 5)

- Calibrated certainty: 3. SBC on synthetics is good; real coverage below 1 km will be hard to prove.
- Data realism: 3. Shallow data is rich; deep, MT-T and permeability data are thin.
- Buildable in 6 months: 2. A Nevada thermal-only prior is feasible; full multi-operator SRA-West is not.
- Edge vs Zanskar: 4. 3D, depth-aware and raw-token supervised is a real step past 2D LightGBM.
- Drives rights and sensors: 4. Simulated-measurement EVSI is the right tool, if the share gate is enforced.

Total: 16/25.
