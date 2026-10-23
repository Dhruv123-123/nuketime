# MODEL.md: the hidden-hydrothermal model we will build

Date: 23 Oct 2026. This is the synthesis of six model designs and three judge reviews. The working name is **SENTINEL-COX**. It builds on the evidence slices `evidence/M01`-`M34` in this folder, `../MEMO.md`, and `../../hardware/MEMO.md`. It does not repeat them. No new web searches were run for this synthesis. Numbers come from the designs and the M-files, which cite primary sources. Anything that is my own arithmetic or not checked is marked (unverified).

## 1. One-paragraph summary

We use **VOI-Bank as the spine**: the model's job is to say what holding the right to an acre is worth in risked dollars, and which measurement or right to buy next per dollar. We **graft** five pieces onto it:
- **CREAM-COX** gives the count. It is a log-Gaussian Cox process thinned by the dated history of who found what, by which search channel, after how much drilling.
- **THERMOS-B** gives the observation layer. Every raw reading enters through its own noisy, censored likelihood, at the 1D-column level only (no 3D surrogate in v1).
- **GeoFM-West Stage 0** gives the main new data. AI extraction of scanned TG logs, driller reports and well files.
- **GHOST-SBI Tier 1** is a cheap analytic simulator. We use it for simulation-based calibration and to rank sensors before we build them.
- A **shared latent mask class** sits under all detectors. It replaces naive capture-recapture.

We keep the USGS and Coolbaugh totals **out** of the fit and use them only as checks. Then any "we narrowed the band" claim is honest.

## 2. Judge scoreboard

Three judges scored each design 1-5 on five axes (25 max per judge).

| Design | Judge 1 | Judge 2 | Judge 3 | Sum (/75) | Role in final model |
|---|---|---|---|---|---|
| VOI-Bank (decision-first active learning) | 21 | 20 | 19 | **60** | **Spine**: RNPV/acre target, EVSI/$ action engine, replay backtest |
| CREAM-COX (discovery-thinned LGCP + size marks) | 19.5 | 19 | 19 | **57.5** | Existence/count layer, effort layers, observation-strength map |
| THERMOS-B (Bayesian heat-and-flow hierarchy) | 18.5 | 17 | 15 | 50.5 | L4 per-source likelihoods, variance split, validation ladder |
| GHOST-SBI (simulator + amortized NPE) | 17.5 | 17 | 15 | 49.5 | Tier 1 column+plume simulator, in-silico sensor EIG, predictive checks |
| GeoFM-West (foundation model + document AI) | 14.5 | 17 | 16 | 47.5 | Stage 0 document extraction only, plus its extraction kill tests |
| HEATFIELD-PU (PINN + SAR-PU + conformal) | 15.5 | 15 | 14 | 44.5 | 2 m hold-out test of the masking operator; Sobol "sensor-shrinkable share" kill test |

Per-axis view (average of the three judges):

| Design | Calibrated certainty | Data realism | Buildable in 6 mo | Edge vs Zanskar | Drives rights + sensors |
|---|---|---|---|---|---|
| VOI-Bank | 3.2 | 4.0 | 3.7 | 4.2 | 5.0 |
| CREAM-COX | 4.0 | 3.0 | 4.2 | 4.2 | 3.8 |
| THERMOS-B | 4.0 | 2.7 | 1.7 | 4.2 | 4.3 |
| GHOST-SBI | 2.7 | 3.0 | 2.0 | 4.2 | 4.7 |
| GeoFM-West | 3.0 | 3.5 | 2.5 | 3.8 | 3.0 |
| HEATFIELD-PU | 2.8 | 3.0 | 2.7 | 3.0 | 3.3 |

All three judges arrived at the same hybrid on their own: a CREAM-COX count inside a VOI-Bank decision loop, fed by GeoFM document extraction, with THERMOS-B's cheap observation physics and GHOST's Tier 1 sensor ranking.

**What we cut from v1** (revisit after month 6, and only if the hindcast shows the simple core leaves lift on the table): the 3D FNO/TOUGH3 surrogate, RJ-MCMC and West-wide NUTS (THERMOS-B); NPE with DANN and population SBI (GHOST); the PINN, SAR-PU and conformal-as-primary (HEATFIELD); foundation-model pretraining (GeoFM).

## 3. Target variable

**Decision target (main output):** risked NPV per acre, RNPV/ac, for each 500 m parcel cell and each legal parcel. It is computed by a fixed, auditable GETEM-style economics layer (`evidence/M34_econ.py`). It is not learned from dollars.

RNPV/ac = sum over depth bins z in {0.5, 1, 1.5, 2, 3 km} and flow classes f in {<20, 20-40, 40-80, >80 kg/s} of
P(system exists and the cell is in its footprint) x P(T(z) first crosses Tmin(z, f, price) at z | exists) x P(f | exists, T) x E[MW/km2 | T, f, permeability class] x capture(stage) x P(build) x discount / 247, minus the 10-year holding cost.

**Physical event (what the ML predicts):** the T(z) curve crosses the **sloped economic line** above 3 km **and** the permeability class is "Limited Distributed" or better (about 40 kg/s per well; Libbey and Murphy SGW 2026, https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Libbey.pdf). At $100/MWh the line is about 109 C at 1 km, 120 C at 1.5 km, 130 C at 2 km and 152 C at 3 km (M34, calc). Price ($80/100/115), ITC, recovery factor Rg (0.08/0.16/0.25) and capture stage (sale at about $0.1M/MW, override at about $0.4M/MW, carry) are scenario inputs. The whole map can be re-priced without refitting.

**Secondary outputs per cell:** psi, the probability that a system exists within 2 km; T at 0.5/1/1.5/2/3 km (P10/P50/P90); permeability class; mask class; P(MWe >= 20) and P(MWe >= 50); P_det, the chance the system would already be known; and EVSI per dollar for each measurement type.

**Headline map for comparison with others:** P(T >= 150 C at <= 2.5 km AND permeable).

**Regional target:** undiscovered MWe per state and province, as mean, F95, F50 and F5 in USGS units. It is reported twice: "USGS-comparable" (above 90 C, no economic filter) and "bankable" (crosses Tmin, flow >= 40 kg/s), split by land tenure.

## 4. Inputs

| Dataset | Coverage | Role |
|---|---|---|
| USGS 205-system Great Basin inventory: 28 plant, 78 known, 99 probable (doi 10.5066/P13AXSYL) | Great Basin | Dated, channel-tagged discovered points. The 99 probable systems are a down-weighted class and a hold-out set |
| USGS 2008 identified systems (doi 10.5066/P1YJWMFC); M18 blind-case table with first-signal year and channel | West | Discovery history that pins the catch rates |
| **Dated search-effort layers**: NDWR Well Driller Reports, 146,235 reports (https://arcgis.water.nv.gov/arcgis/rest/services/NDWR/Well_Driller_Reports/FeatureServer/0); CA DWR OSWCR 1.1M (https://data.cnra.ca.gov/dataset/well-completion-reports); NDOM and UT DOGM wells with spud dates; MRDS/MLRS mining density by decade; OFR 99-425 TG holes (https://pubs.usgs.gov/of/1999/of99-425/webmaps/home.html); INGENIOUS 2 m stations by survey date (GDR 1391, https://gdr.openei.org/submissions/1391); settlement and homestead age | NV first, then CA, UT, ID, OR | Effort E_c(x, t) for 3 collapsed channels. **Effort is a latent with its own prior, not a fixed covariate** |
| **Stage 0 extracted documents**: NBMG WellLog scans (2,002 PDFs, 500+ T-logs on 442 TG holes); NDWR scans (about 90% of temperatures never keyed); CalGEM geothermal wells (4,346, of which 2,008 are TG holes); NDOM well files (938); SMU scanned archive; NI 43-101 mining text | NV, CA, UT | **Main new data.** Full T(z) curves and censored readings with an extraction-confidence score and township-range-section location error (±400-800 m) carried into the likelihood |
| Raw temperatures: Burns 2024 wells (22,535; 4,672 deeper than 50 m; 4,293 flow-disturbed wells kept as convective evidence); USGS heat-flow points with LOESS residuals (doi 10.5066/P9BZPVUC); NBMG BoreholeTemperature (10,991); NDWR 14,282 keyed temperatures; NV/UT oil BHTs (about 1,300); IDWR 739; INGENIOUS 2 m (3,800); OFR 99-425 (786) | Great Basin, then West | Per-source censored likelihoods (Section 5, L1) |
| USGS Great Basin 3D conductive temperature model v1.1 (doi 10.5066/P149FR54); IHFC 2024 (doi 10.5880/fidgeo.2024.014); Stanford Thermal Earth Model (GDR 1592) | Great Basin / West | Conductive background prior for each column |
| Hydrology: NDWR static water levels (146k heads), NWIS heads, carbonate-aquifer extent, basin-fill thickness from gravity (OFR 90-404), recharge | NV, then West | Mask-class prior and the direction of plume back-projection |
| Structure: Faulds FSS (>1,430, typed; DTZ about 4.8x, pull-apart about 2.2x); Qfaults and NSHM 2023 (doi 10.5066/P9W63WOZ); stochastic slip/dilation tendency; UNR catalog (Zenodo 11167510) with an Mc layer | Great Basin | Intensity covariates and permeability-class prior |
| Chemistry, phase 1: silica and Na-K-Ca from NBMG geochem (24,769 samples) and WQP. Phase 2: B, Li, He (doi 10.5066/P96Q13U3), produced waters (doi 10.5066/P9DSRCZJ) | Great Basin | Mixing-model likelihood for deep temperature and hot fraction |
| Geophysics, phase 2: MT conductance (doi 10.5066/P9TWT2LU), prospect EDIs, HELITEM AEM (doi 10.5066/P1UKDJSM), GeoDAWN magnetics and radiometrics (doi 10.5066/P93LGLVQ) | Patchy | Likelihood ratios with false-positive classes (brine, lacustrine clay, fossil cap) |
| **Frozen-label favorability**: our own LightGBM on the INGENIOUS layers, retrained with labels frozen at 1990, 2005 and 2008 | Great Basin | Intensity covariate. Its coefficient is learned, and it is residualized against effort (see Rule A) |
| USGS 2025 favorability rasters (https://www.sciencebase.gov/catalog/item/66e88690d34e0606a9db9b43; doi 10.5066/P14EET2C) | Great Basin | **Benchmark only** in hindcasts, because it was trained on later finds. In live 2026 runs it is allowed as a down-weighted covariate |
| Decision layers: parcel ownership (assessor, state trust, BLM MLRS), rights cost by tenure, access cost per site, transmission distance, NLR/ATB costs | Target states | RNPV and action costs. **Never used as features** |
| **Our sensor rows**: Ranch Well Sentinel visits, logging 2 m probes, 10-30 m darts, E-field MT nodes with a geophone | Grows weekly | Effort-tagged, pre-registered observations. They make detection identifiable |

## 5. Architecture

```
 PUBLIC DATA                STAGE 0 (GeoFM)              OUR FIELD ROWS
 rasters, faults,      scanned TG logs, driller     Sentinel profile, fluid, He,
 heads, effort,        scans, CalGEM/NDOM files ->  tidal logger, darts, E-MT
 discovery dates       T(z) curves + TRS loc. error  (pre-registered predictions)
        |                       |                            |
        v                       v                            v
 +-------------------------------------------------------------------------+
 | L1  OBSERVATION LIKELIHOODS (THERMOS-B L4, 1D only)                     |
 |  equilibrium log N(.,0.5-1C) | TG/cold hole: censored T(d)<x            |
 |  BHT: skewed lower bound + hierarchical bias + 2-5% junk mixture        |
 |  driller discharge: mixed-interval, sigma 2-5C | 2 m: flux+season       |
 |  silica/NaKCa mixing model | (phase 2: He, B/Li, MT with FP classes)    |
 |  location error ±400-800 m for TRS-located points                       |
 +-------------------------------------------------------------------------+
        |
        v
 +-------------------------------------------------------------------------+
 | L2  PER-CELL LATENT COLUMN (500 m), GHOST Tier 1 physics                |
 |  T_c(z) from basal q, k(z), basement depth                              |
 |  + upflow term (Bredehoeft-Papadopulos column, Peclet)                  |
 |  + outflow plume kernel along NDWR heads, L = rho c v b d / lambda      |
 |  latent MASK class m in {open, cold lid, swept, outflow tongue}         |
 |  permeability class in Libbey's 4 classes                               |
 +-------------------------------------------------------------------------+
        |  warm readings RAISE intensity; cold readings act via detection
        v
 +-------------------------------------------------------------------------+
 | L3  EXISTENCE + DETECTION (CREAM-COX), 2 km mesh, inlabru -> NumPyro    |
 |  lambda(s) = exp(a_prov + b*GBM_frozen_resid + beta.X + Z_GP(s))        |
 |  P_det(s,t) = 1 - exp(-sum_c q_c(mask, depth, leak) * E_c(s,t))         |
 |    3 channels: surface leakage | shallow wells+mining | TG + 2 m + ours |
 |  likelihood = thinned Poisson over dated finds + background integral    |
 |  size marks: lognormal-Pareto MWe | T_res, perm class, FSS type, beta   |
 +-------------------------------------------------------------------------+
        |  joint posterior draws (about 4,000)
        v
 +-------------------------------------------------------------------------+
 | L4  DECISION ENGINE (VOI-Bank)                                          |
 |  RNPV/ac per parcel (fixed M34 economics, scenario axes)                |
 |  actions: buy right | Sentinel visit | 2 m line | darts | E-MT | TG     |
 |           hole | drop | carry | sell                                    |
 |  score = EVSI(a)/cost(a) + lambda_glob * EIG(theta_glob)/cost(a)        |
 |  lock rule: buy wherever RNPV/ac > 3 x 10-yr holding cost               |
 |  batching: truck-route clusters; in-silico EIG ranks NEW sensors        |
 +-------------------------------------------------------------------------+
        |
        v
  land list, visit list, regional F95/F50/F5, sensor ranking, nightly refit
```

Key design choices:
1. **Two scales, one posterior.** The count lives on a 2 km mesh (L3). Temperature and parcels live on 500 m columns (L2), with a 250 m sub-grid inside favorable structural settings. Each column draws its intensity from the mesh cell around it.
2. **Warm evidence raises existence.** This fixes CREAM-COX's main gap. A warm or curved reading is a likelihood on the column. The column feeds a "system present" indicator back into the Cox intensity. Cold readings lower intensity only through the detection kernel for their depth and mask class.
3. **One mask class under every detector.** Profile, chemistry, He, 2 m and MT all draw their sensitivity from the same latent mask class. Two-detector agreement in the same cell then identifies detection **without** assuming the detectors are conditionally independent. This is what Lincoln-Petersen gets wrong: shared masking makes detectors fail together, and that biases N low.
4. **Channels collapsed to three**, so that about 60-80 confidently dated systems can identify the catch rates.
5. **Tier 1 simulator** (analytic column + plume + moving-aquifer sweep, about 1 ms per run) is used for three things: SBC on synthetic Nevadas, posterior-predictive checks, and in-silico EIG of sensors that do not exist yet.

Stack: Python, inlabru/INLA for a first Nevada fit in weeks, then NumPyro HMC with a Hilbert-space GP for the joint model. LightGBM for the frozen-label favorability. Claude-class VLM plus a classical curve tracer for Stage 0. One to four GPUs.

**Rule A (leakage).** USGS favorability was trained on detected systems, so it partly encodes P(detected). Used raw as an offset, it pushes hidden counts down in unexplored ground and leaks later finds into hindcasts. We therefore use our own frozen-label GBM, residualized against effort, with a learned coefficient.

**Rule B (circularity).** USGS 2008, Coolbaugh 2006 and NREL/UNR totals are never fitted as constraints. They are hold-out checks only.

## 6. Labels and negatives

No cell is ever "negative" because it is unlabelled. The point-process background integral, exp(-integral of lambda x P_det), does the work that negatives do in a classifier. Every reading is a graded, depth-censored observation with an effort tag (the M19 ladder):

- **G1 confirmed:** the USGS 28 plant + 78 known systems, plants in other states, and IDWR wells >= 140 F with convection evidence. They enter as dated, channel-tagged finds with size marks.
- **G1b probable:** the 99 USGS probable systems. They get a learned confirmation probability, and they are the main hold-out. They are only **partly** independent, because they were found from the same public layers.
- **G2 warm, open-ended:** for example the 697 isolated warm NDWR wells more than 10 km from known systems, and hot mining or dewatering wells. These are "T(d) >= x" lower bounds that raise intensity up-gradient.
- **G3 hard negatives:** equilibrated conductive logs deeper than 150 m in favorable settings. Sources: CalGEM TG holes (once extracted), NDOM EXP/P&A TG holes (124), the 54 of 82 OFR 99-425 prospects that never passed 10 F/100 ft, failed Phillips, Chevron and AMAX grids, the NVML 62, and Argenta. They count against heat to their logged depth only, not against structure.
- **G4 masked:** profiles with reversals or isothermal lids. They mean "unknown below the lid" and point up-gradient.
- **G5 shallow blanks:** 2 m blanks and wells shallower than 50 m. They enter only as weak effort, weighted by (1 - P_detect | mask).

Masks and guards:
- Plants, mines, steamfloods, waterfloods and salt domes are hard-masked out of the temperature and seismic data.
- Leases and permits (MLRS, NDOM, CalGEM) carry a "known to someone" flag.
- Hot springs and sinter never enter as inputs in blind-evaluation runs.
- Our own visits are pre-registered, and their rows stay private.

## 7. How certainty is quantified

- **Joint posterior draws** (about 4,000) over intensity, the Z field, catch rates q_c, effort error, mask states, column parameters, size marks, beta_size and beta_leak. Regional sums are built draw by draw. Cells are correlated through shared parameters, so the regional band is not falsely narrowed.
- **Variance split** (law of total variance, THERMOS-B). The band is divided into four parts: (a) count and detection, (b) masking and depth, (c) size and permeability, (d) Rg and economics. Parts (a)-(c) can be shrunk by our sensors. Part (d) is a scenario axis handed to the buyer.
- **Area of applicability** (Meyer and Pebesma). Cells far from training data in feature space get inflated variance, a visible flag, and a VOI bonus.
- **Labels on every map.** Sensor s/q tables carry the label "prior, unmeasured" until the calibration campaign reports.

## 8. How certainty is validated, in order of honesty

1. **SBC on 20+ synthetic Nevadas** built with the Tier 1 simulator and the **real** effort geometry. Rank statistics must be uniform, and the planted N_hidden must fall inside its 90% interval about 90% of the time. Identifiability check: the posterior/prior variance ratio on N must be below 0.8.
2. **Time-split hindcasts**, frozen at each system's real first-signal date. Blue Mountain (1984), McGinness (1982) and Don A. Campbell (1990) are scored from 1990-and-earlier freezes, **not** as post-2008 finds. Later freezes score Tungsten Mountain (2007), Gabbs (2015), Granite Springs (2016), San Emidio SW, Big Blind (2023) and Pumpernickel. Every freeze uses the frozen-label GBM, never the USGS 2025 raster.
3. **Spatial block CV** with blocks of 50-100 km, larger than the Z-field range, plus leave-one-province-out. No random CV is ever quoted alone.
4. **Area-capture, blind systems only.** Pool the about 10 dated blind finds with extracted warm-well and TG evidence. Report bootstrap CIs, never a pass/fail on n=9.
5. **Temperature calibration:** leave-one-out PIT and 90% coverage on equilibrium-logged wells. Inflate until coverage is 85-95% (the Molasse benchmark reached only 87%).
6. **2 m masking-operator test** (from HEATFIELD): hold out the 55 INGENIOUS 2 m areas (20 positive, 35 blank). Blanks with a predicted thick lid must not lower P_econ.
7. **Posterior-predictive checks** (from GHOST): the model must reproduce the 64% 2 m blank rate, the Nevada warm-well counts, the 92% flow-disturbed share of Burns wells, and the creaming curves by province.
8. **Replay backtest** (VOI-Bank; see Section 11).
9. **Prospective record.** Pre-register NV permit 1744 / Granite Springs 68-02 (about 503 m) before NBMG releases it. Then pre-register every field visit. At a 5-15% hit rate, plan on 500-800 visits before the upper bins of the reliability diagram can be read (about ±0.07 standard error per 30-outcome bin).

## 9. Regional total and comparison with USGS

In each posterior draw s:
- sample lambda and P_det(2026);
- sample the undiscovered pattern from intensity lambda x (1 - P_det);
- cluster the systems at 10 km (the USGS rule);
- draw each system's MWe as area x power density(T_res, permeability class) x Rg/0.16, conditional on "not yet detected", left-censored below 10 MW;
- sum by state, province and land tenure.

Total_s = sum over x of z_s(x) x (1 - D_s(x)) x MWe_s(x). Known systems drop out through the detection term, not by deleting cells. The total is reported per Rg scenario and once with detection held at its mean, so exploration uncertainty and production uncertainty stay separate.

**Comparison anchors (hold-out checks only, never fitted):**

| Anchor | Value | Source |
|---|---|---|
| USGS 2008 undiscovered, West | 30,033 MWe mean; F95 7,917; F50 23,739; F5 73,286 (F5/F95 = 9.3x nationally; 11.6x in each Basin and Range state) | https://pubs.usgs.gov/fs/2008/3082/pdf/fs2008-3082.pdf |
| USGS 2008 Nevada | 4,364 MWe undiscovered vs 1,391 MWe identified | same |
| NREL/UNR Great Basin hidden | 23 GW P50, 28.45 GW mean | https://www.osti.gov/pages/servlets/purl/3018341 |
| Coolbaugh 2006 Nevada count | 157 undiscovered vs 69 known | M33 |
| Our sanity arithmetic | (1.5-3) x 205 systems x 0.87 P(>=10 MW) x about 45 MW mean ≈ **12-24 GWe** Great Basin undiscovered | calc, (unverified) |
| USGS 2026 conditional Monte Carlo (DeAngelo et al.) | not yet published | add when released |

Expected direction against USGS (direction only, until the hindcast runs):
- Masked and data-poor provinces (SRP, Cascades, AZ/NM rift, eastern carbonate Great Basin, where undiscovered/identified ratios run 9-40x) should go **up**.
- Heavily drilled empty Nevada valleys should get tight, low bands.
- The uniform 11.6x F5/F95 should become local.

**Headline buyer metric:** how far each region's F5/F95 band narrows per 100 Sentinel visits (target under 4x in the first three states, untested), plus bankable hidden MWe on land we can still lock at $1-2/ac.

## 10. Ranked dominant uncertainties, and the measurement that shrinks each most

This ranking drives the sensor choice.

| Rank | Uncertainty | Why it matters | What shrinks it most (cheapest first) |
|---|---|---|---|
| 1 | **Detection gap / occupancy in unexplored favorable ground**, especially the catch rate for deep or lidded blind systems with no shallow outflow | Moves N_hidden 2-5x. Today it is one national band (F5/F95 = 11.6x). 97% of the Great Basin has no 2 m reading | Desk: Stage 0 extraction, which turns "never looked" cells into effort-tagged cells. Field: 300-800 pre-registered **Sentinel** visits in high-lambda, low-P_det cells, plus a stratified-random designed survey with two detectors per cell under the shared mask latent |
| 2 | **Permeability class / flow per well** | About 10x on MWe at fixed heat. Recovery factor 4-53%. Flow from 20 to 60 kg/s changes cost of power about 2x. This is Zanskar's admitted gap | Sentinel **pressure/barometer logger left 2-4 weeks** (earth-tide transmissivity and storativity); driller specific capacity; He R/Ra plus Ne from a diffusion sampler (open vs sealed faults); 3C geophone on E-MT nodes (focal mechanisms give local SHmax for slip tendency) |
| 3 | **Hydrologic masking state and lid thickness** | Moves shallow-sensor sensitivity from about 0.8 to about 0 (Argenta, Granite Springs, Kimama). Decides whether a blank means anything | Sentinel **0.01 C, 0.5 m T-P-EC profile** (shape, reversals, Peclet fit to about 1.5 cm/yr); head loggers for flow direction; 10-30 m darts; E-field MT for lids thicker than 200 m |
| 4 | **Reliability matrix of each cheap sensor (s/q per mask class, and how sensors fail together)** | s = 0.3 vs 0.7 swings VOI more than 2x. Nothing has been published. Until it is measured, every VOI ranking is driven by priors | **Calibration campaign** with the full kit: about 20 known blind systems and about 40 cold controls, fitted per mask class. This is the first field spend |
| 5 | **Temperature at 0.5-2 km** (shallow-to-deep extrapolation) | Almost no public data between 300 and 1,500 m. The Tmin line slopes, so a 20 C error is a 1.5-2 km error | Sentinel **sealed fluid bottle** (SiO2, Na-K-Ca, B, Li) through the mixing model; profile curvature; re-logging idle TG and oil wells (±16 C header to ±1 C profile); then one 150-500 m own-rig hole per top optioned parcel |
| 6 | **Upflow location and footprint area** | Ranch wells sit in basin centres and on fans, so they mostly sample outflow. MWe is linear in area, and MT outlines overstate it several-fold | Plume back-projection along NDWR heads; **darts at range-front structural targets**; a logging 2 m grid at 200-500 m plus an E-MT carpet at 100-250 m with temperature ties |
| 7 | **Conductive background and position error** (basal heat flow, conductivity, basement depth, TRS ±400-800 m locations) | ±300 m of basement is about ±18 C. A ±400-800 m location error is about the width of an upflow | Needle-probe conductivity on cuttings; ground gravity and HVSR at fault corners; GPS ties on re-logged wells |
| 8 | **Size tail and blind size/leakiness bias** (tail index 0.6-1.6, beta) | About 2x on GWe | Desk: an EIA-923 low-temperature power-density curve; every new confirmed system |
| 9 | **Recovery factor and production behaviour** | About 3x. Not fillable by cheap sensors | Scenario axis (Rg 0.08/0.16/0.25), priced into the farm-out |

**Sensor answer that follows from the ranking.** One instrument covers ranks 1, 2, 3 and 5 on a single visit, and the heat option is signed on that same visit. This is the **Ranch Well Sentinel**, an upgrade of the prior 18/25 drop probe:
- a 0.01 C T-P-EC profiler logging at 0.5 m steps;
- a sealed geothermometer bottle;
- a passive He/Ne diffusion sampler;
- a pressure/barometer logger left in the well for 2-4 weeks;
- natural gamma.

Rank 4 is not a new device. It is the first way to spend the Sentinel: the calibration campaign. Ranks 3 and 6 need the second build, **10-30 m push darts plus E-field MT nodes with a 3C geophone and an SP channel**. GHOST Tier 1 in-silico EIG must confirm this order per dollar before hardware money is spent beyond prototypes.

## 11. Cheapest first validation

**Desk (weeks 0-10, compute and API only, about $5k or less; unverified):**
1. **Week 1-2, quick checks.** Rank the 697 isolated warm NDWR wells by EVSI/$, and count how many of the 99 probable systems fall within 10 km of the top 100. Freeze and publish a Granite Springs 68-02 prediction.
2. **Week 1-6, Stage 0 extraction benchmark.** Run the VLM and curve tracer on the about 500 NBMG T-log scans. Score against OFR 99-425 gradients and SMU duplicates. Pass: median gradient error 10% or less, and 80% or more of logs give a usable curve.
3. **Week 2-8, Nevada fit.** Build dated effort layers and the frozen-label GBMs (1990/2005/2008). Fit the inlabru LGCP with thinning and the 1D column with four reading types (equilibrium/TG censored, BHT, driller, 2 m). Run SBC on 20 synthetic Nevadas and the predictive checks.
4. **Week 8-10, replay backtest.** Freeze at 2005. "Buy" readings from the public observation bank under $0.5M, $2M and $5M budgets. Lock land by the 3x rule. Count post-2005 blind finds inside locked acreage per dollar against three baselines: USGS top 1%/10%, random readings inside FSS, and variance-only acquisition. **All policies draw from the same bank, and we also replay on SBC synthetic worlds to correct for off-policy selection bias.** Report bootstrap CIs.

**Go for field spend if:**
- coverage is 85-95% on held-out logs;
- SBC recovers N in its 90% interval at least 85% of the time;
- the posterior/prior variance on N is below 0.8;
- the replay shows at least 1.5x systems per dollar over the best baseline, with a CI clearly above 1.

**Field (months 4-6):**
1. Build 5-10 Sentinel kits.
2. Run the calibration campaign: about 20 known blind systems and about 40 cold controls, two detectors per cell (Sentinel + a short E-MT or 2 m line).
3. Then visit about 100 stratified-random high-lambda, zero-effort cells on private and state land.
4. Every visit is pre-registered and signs the heat option.

## 12. Kill conditions

1. **Too small (main kill).** After the occupancy correction, the bankable hidden resource (crosses Tmin, flow >= 40 kg/s) on lockable private, state and leftover-BLM land in NV+UT+OR+ID+NM is below about **2 GWe P50**. Or fewer than about 30 undiscovered systems have P(MWe >= 20) of 0.5 or more. Then the bank cannot reach about 100 locked systems.
2. **No decision lift.** The replay shows the VOI policy beats "lock the USGS top 10%" by less than 1.2x systems per dollar at every budget, with CIs overlapping 1. Then switch to a pure land-first strategy and keep the model as a data-room tool.
3. **Not identifiable.** With the real effort geometry, the SBC posterior/prior variance on N stays above 0.8, even with 3 channels. Do not kill. Make the designed two-detector survey mandatory before any regional number is quoted.
4. **Calibration fails.** Held-out 90% T(z) coverage stays below 80% after inflation, or the psi reliability slope on the first 200 pre-registered visits is below 0.5 and does not improve after one refit. Then the model is sold as ranking only.
5. **Extraction fails.** Median gradient error stays above 20%, or fewer than 1,000 new depth-tagged readings fall more than 3 km from known systems, after two fix rounds. Then drop Stage 0 and rely on keyed data plus sensors.
6. **Sensor fails.** In the calibration campaign, the Sentinel's combined sensitivity is below 0.3 under lidded or swept masks in more than half of target provinces, and profile shape does not separate "lid" from "no system". Then shift budget to darts plus E-MT (about 10x cost per label).
7. **Sensors cannot move the answer.** The share of the regional band from sensor-shrinkable terms (parts a-c) is below 30%. Then probes create no alpha, and the company is a plain land bank.
8. **Rights cost breaks.** Ranch heat options cost more than $20/ac, or more than 70% of owners refuse. Then RNPV/ac rarely clears the lock rule.

Untested ML lift is never by itself a kill.

## 13. Caveats

- No web searches were run for this synthesis. Citations come from the design texts and the M-files.
- The VOI multiples, the s/q priors, the "12-24 GWe" arithmetic and the extraction yields are (unverified) until the desk test runs.
- The 1.5x lift test on about 10 blind systems cannot settle anything on its own. That is why evidence is pooled and CIs are reported.
