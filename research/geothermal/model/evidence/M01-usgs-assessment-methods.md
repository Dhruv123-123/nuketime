# M01: How USGS counts undiscovered hydrothermal heat, and where its error bars come from

Slice M01, model track. This builds on `research/geothermal/evidence/L05-usgs-assessment.md` and `L02-blind-systems.md`. Those files already give the headline numbers (9 GWe identified, 30 GWe undiscovered, the 2025 favorability map, and 135 GWe of EGS). This file does not repeat them. It covers the **machinery**: how the undiscovered number is made, where the F95-F5 band comes from, and which inputs move it most.

Fetch notes: the USGS 2008 fact sheet PDF and the pubs.usgs.gov record for Williams et al. 2009 were blocked by the fetch tool's permission gate, so I worked from their abstracts (usgs.gov mirror) and the prior L05 extracts. The DeAngelo et al. SGW 2026 PDF was blocked by robots.txt, so I used its USGS abstract. Where I describe a method step that I could not confirm in text, it is marked (unverified).

## Bottom line

The USGS "30 GWe undiscovered" is not a measurement. It is **a count times a size**. The count is the number of systems a 2008 favorability model says should exist, minus the ones already known. The size of each missing system is borrowed from the size distribution of the known ones. The very wide band (F95 7.9 GWe to F5 73.3 GWe, a 9x spread) comes mostly from **one shared, region-blind multiplier**. My arithmetic on the published table shows that Nevada, Idaho, Oregon and Utah have *identical* fractile-to-mean ratios (F95 = 0.228x mean, F50 = 0.743x, F5 = 2.637x, so F5/F95 = 11.6x). The state numbers are a share-out of one uncertain national total. They are not separate local estimates. So **no local data narrows the band anywhere today**. Everything that matters sits in three places: (1) how many systems really exist per unit of favorable ground, which depends on a positive-unlabelled training set that calls every unexplored cell "negative"; (2) whether hidden systems are as big as known ones; (3) the recovery factor (0.08-0.25) and temperature-at-depth (heat flow), which convert a system into MWe. The 2023-2026 USGS reassessment rebuilt the favorability map (XGBoost, 16 layers, about 10x more labels from heat-flow wells) and a new list of 205 identified and probable systems. It will then run "conditional statistics" (count per favorability bin) through a Monte Carlo. That is the same structure with better inputs. A better model for us is the same count-times-size frame done **locally**, with an explicit **detection-probability (exploration-coverage) term**, and with our own probe measurements used as new labels. The single sensor input that would move the estimate most is **cheap, dense, true-negative and true-positive temperature-gradient labels in unexplored, high-favorability cells**. That is exactly what the ranch water-well drop probe and the 2 m probes produce.

## Findings

### F1. The 2008 undiscovered estimate is "expected systems minus known systems", times a size borrowed from known systems
- The 2009 methods paper says the estimate rests on: (a) how much undiscovered systems resemble identified ones; (b) exploration history and where exploration happened relative to the undiscovered resource, plus the success chance of standard techniques; (c) physical limits on how systems form and last. Source: Williams, Reed, DeAngelo & Galanis (2009), GRC Trans. 33, abstract, https://www.usgs.gov/publications/quantifying-undiscovered-geothermal-resources-united-states (full record https://pubs.usgs.gov/publication/70158979, blocked to me).
- The spatial part: 725,442 grid cells of 2 km x 2 km; **278 cells held known systems and were labelled positive; "all the unlabeled cells were assumed to be negative."** 28 models were built with weights-of-evidence and logistic regression, from 9 feature sets of 5 types (Quaternary faults, magmatism, heat flow, seismicity, stress). Expert choices of bins and buffers (for example, "within 4 km of a feature") made the linear methods act non-linearly. Source: Mordensky et al., SGW 2022, describing Williams & DeAngelo 2008, https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2022/Mordensky.pdf ; Williams & DeAngelo 2008, https://openei.org/wiki/Mapping_Geothermal_Potential_In_The_Western_United_States
- Turning the map into a count. The sum of the per-cell probabilities in a region gives the expected number of systems. Subtracting the known ones gives the undiscovered count. Each undiscovered system then takes a power value drawn from the identified-system distribution, which comes from the volume (heat-in-place) Monte Carlo. (The exact sampling and any shift toward smaller sizes are unverified because I could not read the full 2009 paper. The structure matches the abstract's three constraints and the L05 notes.)
- The identified-system Monte Carlo: triangular distributions on reservoir temperature and volume, a recovery factor Rg uniform on **0.08-0.20 (fractured) or 0.10-0.25 (sediment-hosted)**, a temperature-dependent conversion efficiency, and 30-year life. Source: Williams, Reed & Mariner 2008, OFR 2008-1296, https://pubs.usgs.gov/of/2008/1296 . Circular 790 (1979) used Rg = 0.25 and got 72-127 GWe undiscovered. **Cutting Rg alone cut the national undiscovered figure about 3-4x** between 1979 and 2008.

### F2. The published bands are one shared multiplier, not local knowledge (my arithmetic on the USGS table)
| Region | F95/mean | F50/mean | F5/mean | F5/F95 |
|---|---|---|---|---|
| US total | 0.264 | 0.790 | 2.44 | 9.3x |
| Nevada | 0.228 | 0.743 | 2.637 | 11.6x |
| Idaho | 0.228 | 0.743 | 2.637 | 11.6x |
| Oregon | 0.228 | 0.743 | 2.637 | 11.6x |
| Utah | 0.228 | 0.743 | 2.637 | 11.6x |
| California | 0.287 | 0.841 | 2.243 | 7.8x |

Inputs come from USGS FS 2008-3082 Table 1 (as copied in L02/L05). The four Basin-and-Range states share the same shape to three decimals. That is close to a lognormal with sigma about 0.77 (mean/median = 1.345, against exp(sigma^2/2) = 1.345). California is narrower only because The Geysers and the big known fields anchor it. The national band is narrower than each state's band because the states are added with some independence. **Meaning: the USGS band reflects uncertainty about the national ratio of hidden systems to favorability, and about system size. It says nothing site-specific.** The same 11.6x band applies to a well-drilled corner of Nevada and to empty eastern Oregon. This is the biggest weakness to attack. (The analysis is mine. The exact algorithm that produced the shared ratios is unverified.)

### F3. The labels are the binding limit, not the algorithm
- In the 2023 re-run of the 2008 problem with 9 methods (expert weights-of-evidence and logistic regression, plain logistic regression, XGBoost, SVMs, an ANN), **every method scored F1 < 0.10**. The cause is missing true negatives and severe class imbalance. Mordensky et al. 2023, Geothermics 110, 102662, https://pubs.usgs.gov/publication/70240475
- The 2022 class-weighting work suggests that the **number of naturally occurring systems may be larger than even the 2009 F5 (5%-probability) estimate**. So the upper tail is probably too low, not too high. Source: SGW 2022 Mordensky, link above.
- The fix USGS adopted: labels from **departures from conductive heat flow at wells**. A well counts as convective if its measured heat flow sits well above the conductive trend. This gives ordinal labels and about 10x more training sites. DeAngelo et al. 2023, heat-flow data https://doi.org/10.5066/P9BZPVUC ; Mordensky et al. 2025, Geothermics 133, 103450, https://pubs.usgs.gov/publication/70270953 ; rasters https://www.sciencebase.gov/catalog/item/66e88690d34e0606a9db9b43
- 2025 favorability result: 26 of 28 power-producing systems sit above the 80th percentile, and 15 of 28 sit in the top 1% of area. Blind and exposed systems are predicted equally well (L05 S8). The map is the median of **1,200 Monte Carlo cross-validation realizations**, with P05-P95 rasters, so the new favorability uncertainty is **model and split variance only**. It does not include label noise or the bias from where wells were drilled.

### F4. The 2026 hydrothermal update keeps the count-times-size frame with a new inventory
- DeAngelo, Burns & Mordensky (2026, conference paper, USGS Index 70273870): Monte Carlo analysis of identified resources in **explored** regions. Undiscovered resources are estimated by **conditioning on the favorability map** ("conditional statistics" of systems per favorability level). Systems are clustered at 10 km. "Electric-grade" means a well above **85 °C with evidence of convection**. Inventory: **28 systems with operating plants + 78 other known electric-grade systems + 99 newly identified probable systems = 205**, each ranked by confidence. A companion data release gives developed and likely total capacity with uncertainty. https://www.usgs.gov/publications/conventional-hydrothermal-power-producing-systems-great-basin-usa
- Inference (unverified until the numbers are published): the explored regions set the systems-per-favorability rate, and that rate is then applied to unexplored high-favorability ground. **The explored/unexplored boundary and the confidence ranking of the 99 "probable" systems therefore become first-order drivers of the new undiscovered number.** Promoting 99 probable systems to real ones roughly doubles the 106 confirmed systems. If the probable systems are real and sit in high-favorability cells, the rate per bin goes up, and so does the undiscovered estimate.
- For comparison, NREL/UNR regression of nameplate MW on 48 features gave Great Basin hydrothermal at **28.45 GW (MSE), 23 GW (P50), 79.5 GW (P90)**, matching the USGS 30 GWe (Trainor-Guitton et al. 2025, https://www.osti.gov/pages/servlets/purl/3018341). Coolbaugh et al. 2006 estimated **157 undiscovered Nevada systems at ≥100 °C against 69 known (3.2x)**, https://www.usgs.gov/publications/prediction-and-discovery-new-geothermal-resources-great-basin-multiple-evidence-a

### F5. The temperature-at-depth input: heat flow dominates
- For the USGS 3D temperature model behind the 2025 EGS assessment: "the influence of uncertainty in surface heat flow is by far the largest" (Williams & DeAngelo 2011, quoted in Burns et al. SGW 2024). Thermal conductivity is next: base 2.7 W/m/°C, range 2.4-3.0. Radiogenic heat is 1.89 ± 0.95 µW/m³. Burns et al. 2024, https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2024/Burns.pdf
- Calibration wells: 22,535 shrank to 5,717 after groundwater wells were removed. Of 4,672 wells deeper than 50 m, only **379** fell within ±7.5 °C/km of the conductive model. The other **4,293 were "non-conductive"**, which means disturbed by water flow, often up or down. That is a huge unused pool of convective-signal labels (Burns 2024).
- Convection breaks the conductive model: "measured temperatures in areas with substantial deep convective transport of heat will not match predicted values well." Hydrothermal systems occupy "only a few percent of the total area of the Great Basin."

### F6. The ranking of what would change the estimate most (my synthesis)
1. **Systems per unit of favorability in unexplored ground (the detection gap).** The rate learned in explored areas is applied to unexplored ones. If exploration coverage is wrongly modelled, the count can be off by 2-5x. The 2022 class-weighting result says it is probably too low. Drives the count. Biggest effect.
2. **Size of hidden systems compared with known ones.** Known systems were found because they leak to the surface, which favours bigger, hotter, more permeable ones. If blind systems are, say, half the size, the MWe halves. If they are the same size (as Big Blind at about 121 °C, and McGinness Hills, suggest), it holds. A factor of about 2.
3. **Recovery factor Rg (0.08-0.25).** Linear in MWe, about 3x across its range, and history shows it moved the national number 3-4x. It is set by production histories, not exploration data.
4. **Temperature cut-off and heat flow.** The 85-90 °C electric-grade threshold, and binary-plant efficiency at 100-150 °C. Moving the cut-off from 150 °C to 100 °C adds many small systems. Better heat-flow maps move the reservoir temperature.
5. **Clustering and definition rules** (10 km grouping, what counts as "probable"). These are bookkeeping, but they change the count by tens of percent.

## Datasets

| Dataset | Access | Coverage | Use for blind detection |
|---|---|---|---|
| USGS 2025 Great Basin favorability (median + P05-P95, 16 features, labels) | Free, ScienceBase https://www.sciencebase.gov/catalog/item/66e88690d34e0606a9db9b43 ; https://doi.org/10.5066/P14EET2C | CA, ID, NV, OR, UT (Great Basin) | Prior map; the P05-P95 spread shows where the model is unsure, which is where a probe adds value |
| Mordensky & DeAngelo 2026 zone-classification data (53 features) | Free, https://sciencebase.gov/catalog/item/6927454dd4be02716f722cb3 | INGENIOUS region | Richer feature stack and labels |
| USGS conductive heat-flow and convective-residual maps | Free, https://doi.org/10.5066/P9BZPVUC | Great Basin | Labels; the convective residual is the target variable |
| USGS 205-system Great Basin inventory with capacity and uncertainty (companion to DeAngelo 2026) | Free data release (DOI not retrieved; unverified) | Great Basin | Positive labels with confidence ranks; the 99 "probable" systems are prime targets for land and probes |
| USGS EGS 3D temperature model and calibration wells | Free, https://doi.org/10.5066/P149FR54 ; https://doi.org/10.5066/P14LU7WD | Great Basin, 1-6 km | Conductive baseline. The 4,293 "non-conductive" wells are candidate convective labels |
| USGS 2008 national favorability and system tables | Free, https://pubs.usgs.gov/fs/2008/3082 ; https://pubs.usgs.gov/of/2008/1296 | Western US, 13 states | Baseline outside the Great Basin (NM, CO, AZ, WA, MT, WY), where no ML update exists yet |
| NREL/UNR INGENIOUS MW regression and reV supply curve | Free, https://www.osti.gov/pages/servlets/purl/3018341 | Great Basin | Converts favorability into MW and LCOE |

## What dominates uncertainty
- **Positive-unlabelled labels.** Every unexplored cell is called "negative". That biases the count down and inflates false negatives exactly where blind systems are.
- **No exploration-coverage (detection probability) term.** The band is one national multiplier. Local data does not narrow it.
- **Size distribution of blind systems**, which is borrowed from surface-leaking systems that are biased toward large ones.
- **Recovery factor** (0.08-0.25), which is fixed by a handful of production histories.
- **Heat-flow accuracy** for temperature at depth, which is the largest single term in the USGS temperature model.
- **Confidence of "probable" systems** in the 2026 inventory (99 of 205).

## What a sensor could fill
- **True negatives and true positives in unexplored high-favorability cells.** A temperature-gradient reading in an existing ranch water well, or a 2 m probe line, turns an "unlabelled" cell into a labelled one. This attacks driver 1 directly. Each reading also gives a local detection-probability update, so the band can be narrowed cell by cell instead of nationally.
- **Re-reading "non-conductive" wells.** Logging the about 4,300 disturbed wells, where reachable, with a T-P-conductivity drop probe separates up-flow (convective, hot) from down-flow (cold recharge). That is a cheap, large-N convective-label set.
- **Fluid chemistry at the same visit** (conductivity, and optionally a grab sample for Si, Na-K-Ca geothermometers) gives a reservoir-temperature estimate. That attacks the size and temperature drivers (2 and 4) before any drilling.
- **E-field MT nodes** over high-favorability cells give clay-cap conductance, which tests whether a system is big (driver 2).
- **Recovery factor (driver 3)** needs flow tests or production data, which a sensor cannot supply cheaply. Leave it as a priced-in scenario range.

## Implications for a better model
1. **Rebuild the USGS "count times size" frame as a hierarchical Bayesian model on a grid.** Each cell gets P(system | features) from the USGS 2025 XGBoost raster (used as a prior) times P(detected | exploration coverage). Coverage comes from well density, spring surveys, and gradient-hole and mining-hole density (D03, D06, L16). Hidden systems = expected minus detected, with a **per-cell posterior instead of one national multiplier**. That gives a local band, which the business needs to price individual leases.
2. **Treat it as positive-unlabelled (PU) learning** with a fitted label frequency, not "unlabelled = negative". Fit the label frequency as a function of exploration coverage. This directly tests the 2022 USGS hint that the true count is above the F5.
3. **Model blind-system size explicitly** as the known distribution times a detectability bias, P(surface leak | size, depth, cap). Fit it on known blind systems (McGinness, Desert Peak, Blue Mountain, Tungsten Mountain, Big Blind, the play-fairway finds).
4. **Use the convective-residual label (well heat flow minus conductive trend) as the main regression target**, with our own probe readings added as new rows. Each new reading is an active-learning query. Choose wells and probe sites where the posterior variance times land optionality is highest.
5. **Report MWe as scenario-conditional on Rg** (0.08 / 0.14 / 0.25) so that the exploration uncertainty (which we can shrink) is kept apart from the production uncertainty (which we cannot).
6. **Extend outside the Great Basin.** NM, CO, AZ, WA, MT and WY still run on the 2008 map with the same 11.6x band. There, a few hundred probe readings could change the regional number most, and land is least competed for.
7. **Validate against the 2026 USGS inventory.** Hold out the 99 "probable" systems and check that the model ranks them high. That gives an honest, publishable lift metric that buyers (Ormat, Fervo) will trust.

## Sources
- Williams et al. 2008, USGS FS 2008-3082: https://pubs.usgs.gov/fs/2008/3082 (PDF fetch blocked)
- Williams, Reed & Mariner 2008, OFR 2008-1296: https://pubs.usgs.gov/of/2008/1296
- Williams & DeAngelo 2008, GRC: https://openei.org/wiki/Mapping_Geothermal_Potential_In_The_Western_United_States
- Williams et al. 2009, GRC 33: https://www.usgs.gov/publications/quantifying-undiscovered-geothermal-resources-united-states ; https://pubs.usgs.gov/publication/70158979 (blocked)
- Coolbaugh et al. 2006: https://www.usgs.gov/publications/prediction-and-discovery-new-geothermal-resources-great-basin-multiple-evidence-a
- Mordensky et al. SGW 2022: https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2022/Mordensky.pdf
- Mordensky et al. 2023: https://pubs.usgs.gov/publication/70240475
- Mordensky et al. 2025: https://pubs.usgs.gov/publication/70270953 ; data https://www.sciencebase.gov/catalog/item/66e88690d34e0606a9db9b43
- Burns et al. SGW 2024: https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2024/Burns.pdf
- DeAngelo, Burns & Mordensky 2026: https://www.usgs.gov/publications/conventional-hydrothermal-power-producing-systems-great-basin-usa ; SGW 2026 PDF https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Deangelo.pdf (robots-blocked)
- USGS EGS FS 2025-3027: https://pubs.usgs.gov/fs/2025/3027/fs20253027.pdf
- Trainor-Guitton et al. 2025: https://www.osti.gov/pages/servlets/purl/3018341
