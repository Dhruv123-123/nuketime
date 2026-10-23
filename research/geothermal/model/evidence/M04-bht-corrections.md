# M04: Oil and gas bottom-hole temperatures (BHT) as noisy evidence in a blind-hydrothermal model

Slice M04, model track. Date: 23 Oct 2026. This file builds on `../../evidence/L09-temperature-at-depth.md`, which already covers the correction literature (Kehle, Harrison, SMU, Deming, Whealton, Burke, Schölderle, Waples) and the national ML maps (Stanford InterPIGNN, LANL In-Context Earth). It also builds on `D01` (Texas RRC), `D02` (Kansas/Oklahoma, 74,299 KGS wells with BHT), `D03` (Nevada/Utah well files) and `D04` (NGDS/SMU node). This file does not repeat those. It adds three things: (1) a quality ladder with error bars for each kind of temperature reading, (2) the western-versus-Texas/Gulf coverage picture, with the Great Basin cases where oil wells found blind systems, and (3) a concrete way to put noisy BHTs into a probabilistic model. Web budget used: 8 searches, 7 fetches.

## Bottom line

A raw BHT is a biased, noisy lower bound, not a measurement. Its error depends mostly on missing metadata (time since circulation, true depth, units), not on which correction formula you pick. Single corrected BHTs carry about +/-8 C (1 sigma) at best and +/-16 C (96%) in practice. Horner with three or more runs gets to about +/-2-5 C. Equilibrium logs get to under 1 C. In the western US the BHT record is thin (hundreds of wildcats per state in the Great Basin, against hundreds of thousands of wells in Kansas and Texas). But in the Great Basin the signals that matter are huge. Blind systems show up as 30-100 C anomalies, and two blind systems (Railroad Valley at 120-130 C, and the Black Rock Desert anomaly at 230 +/- 10 C) were found only because oil wildcats hit them. So for blind hydrothermal, noise of +/-15 C does not hide the signal. The real risks are false negatives from groundwater "masking" and gross data errors. The better model treats each BHT as a one-sided, heteroscedastic, outlier-prone observation. It learns the cold bias hierarchically by basin and era from paired calibration wells. It then spends our own sensor money on re-logging idle oil and water wells to equilibrium, which turns +/-15 C points into +/-1 C anchors where the model is most uncertain.

## Findings

### F1. Quality ladder: each kind of temperature reading has its own error bar
| Reading type | Typical error (1 sigma unless stated) | Source |
|---|---|---|
| Equilibrium (static) temperature log, weeks to months after drilling | < 0.5-1 C; probe precision 0.01 C | UGS NGDS summary (probe 0.01 C) https://geology.utah.gov/docs/geothermal/ngds/supplemental/summary_report/NGDS_data_summary.pdf ; 1 C figure is my judgement (unverified) |
| Horner-corrected BHT, 3+ runs with recorded times | +/-1-3 C fit scatter; about 2-5 C true error | Peters & Nelson 2009 AAPG Hedberg https://www.searchanddiscovery.com/abstracts/html/2009/hedberg/abstracts/extended/peters/peters.htm ; 2-5 C is L09 synthesis |
| Horner or Cooper-Jones on 2+ runs | methods agree within < 2 C only when shut-in < 10 h; error grows as shut-in time shrinks | EGU2009-1250 (18 wells, 71 BHT/time pairs, Italy) https://meetingorganizer.copernicus.org/EGU2009/EGU2009-1250-3.pdf |
| DST (drill-stem test) temperature | usually near formation temperature; used as the reference for corrections. About 2-5 C (unverified) | Harrison 1983 calibrated on DSTs (L09); Hermanrud 1990 via Peters & Nelson |
| Single corrected BHT, time since circulation known | about +/-8 C (1 sigma), measured against DSTs at the same depth | Hermanrud et al. 1990 as cited by Peters & Nelson 2009 |
| Single BHT, empirical depth correction (Harrison, Kehle), no metadata | about +/-16 C at 96% confidence; method-vs-method spread 8-20 C | Petroleum Geoscience 7(3):241 (2001) https://www.earthdoc.org/content/journals/10.1144/petgeo.7.3.241 ; Schölderle et al. 2022 https://www.mdpi.com/1996-1073/15/17/6367 |
| Raw (uncorrected) BHT | reads 22.2 +/- 10.2 C cold | Petroleum Geoscience 2001 |
| Rough "add 5 C/km" correction (Utah, no circulation data) | +/-5 C claimed | UGS NGDS summary (Salduro #1, Alpha Gov't #1) |

Plain reading: the error bar moves about 15x between a lone header BHT and a proper log. That spread is the main lever for a model. It also tells you what each dollar of re-logging buys.

### F2. Why the error is mostly metadata, and what kind of errors they are
- Schölderle et al. (2022) showed with Sobol sensitivity analysis that unknown input errors exceed the differences between correction methods. Thermal diffusivity alone moved one well by up to 8.3 K. P10-P90 bands were 10-14 K (L09).
- The error has three distinct parts, and a model should treat them differently:
  1. **A systematic cold bias.** It is always in one direction (BHT reads low). It grows with depth and with mud circulation, and shrinks with shut-in time. Harrison is roughly +9 C at 1.5 km and +13 C at 2.5 km (L09).
  2. **Random scatter** around the corrected value (the +/-8 to +/-16 C above).
  3. **Gross errors.** Examples are degrees F logged as C, wrong depth (measurement depth "generally not recorded", Whealton 2015), rounding, and measured-while-drilling values. LANL's In-Context Earth found its largest outliers were these flagged data-quality cases (L09). Kansas has a 214 F reading at 784 ft (D02). These need a heavy-tailed or mixture likelihood, not a Gaussian.
- A further part matters most in the Great Basin: **hydrologic disturbance.** In Railroad Valley, shallow interbasin flow in Paleozoic carbonates cools the upper section. USGS calls this a heat sink that can mask "deep geothermal resources" (Railroad Valley heat-flow paper, https://pubs.usgs.gov/publication/70205980). A correct BHT in a cooled aquifer is still a misleading BHT for what lies below.

### F3. Correction methods: what each needs, and when it fails
- **Harrison (1983):** depth only. Quadratic, calibrated on Oklahoma DSTs to about 3 km. Used by Stanford's 400,134-BHT national model. It can be worse than no correction in NY/PA above 1 km (Shope 2012 via Whealton 2015) (L09).
- **Kehle (1973), AAPG GSNA:** quartic in depth, built for the continental AAPG compilation (>20,000 BHTs, >10,000 wells). Commonly quoted form in feet and F: dT = 1.878e-3 z - 8.476e-7 z^2 + 5.091e-11 z^3 - 1.681e-15 z^4 (coefficients from memory, unverified). Same weakness as Harrison: one region's calibration, applied everywhere.
- **SMU gradient-dependent correction (Blackwell & Richards 2004):** adds -5 to +11 C by apparent gradient, valid 750-3,000 m, "not established" below 3-4 km (L09).
- **Horner (line-source) and Cooper-Jones / Brennand / Leblanc:** physics-based. They need two or more BHTs at one depth with recorded times since circulation stopped, or mud and rock properties. Reliability criteria: at least three runs, extrapolation smaller than the measured range, fit residuals within +/-1-3 C, no re-circulation between runs (Peters & Nelson 2009). Horner tends to under-correct when shut-in times are short (EGU2009-1250; Goutorbe, Lucazeau & Bonneville 2007, Geophys. J. Int., reached a similar view on an Australian set, unverified details).
- **Basin-specific regressions:** 12 equations for onshore Gulf provinces (Burke et al. 2018, USGS); GLS regressions for Appalachia (Whealton 2015); local depth-time equations that let one BHT plus one shut-in time be corrected (EGU2009-1250). Lesson: the correction is a function of place and era. A model should learn it, not assume it.
- **Static logging programs that calibrate corrections:** North Dakota Geological Survey has logged 25 temporarily abandoned oil wells to static temperature since 2014. It found that dynamic BHTs "often underestimate" true temperature and that gradients from them "vary wildly" (NDGS newsletter 2020, https://dmr.nd.gov/ndgs/documents/newsletter/2020Winter/Using_Static_Temperatures_to_More_Accurately_Predict_Geothermal_Gradients_in_the_Williston_Basin.pdf ; program story https://www.dmr.nd.gov/ndgs/documents/newsletter/2014Summer/Story%203%20Temperature%20Logging.pdf). This is a public precedent for exactly the calibration campaign we could run in Nevada and Utah.
- **Monte Carlo correction plus probabilistic kriging is now the state of the art in Europe.** EGU26-13093 (Bavarian Molasse) corrected 196 BHTs by Monte Carlo, combined them with 19 high-quality logs, and ran 3D Empirical Bayesian Kriging (300-5,000 m, 100 m voxels). It gave P10/P50/P90 grids and exceedance maps at 80 C and 100 C. Leave-one-out mean standard error was 5.6 K, and more than 87% of points fell inside the 90% interval (slightly overconfident) (https://meetingorganizer.copernicus.org/EGU26/EGU26-13093.html). Nobody has published this for the Great Basin (unverified that no one has).

### F4. Coverage: the West is thin; Texas, the Midcontinent and the Gulf are thick
| Region | BHT-bearing wells (approx.) | Source |
|---|---|---|
| Kansas | 74,299 wells with BHT, 212,089 readings; 6,950 wells with multiple BHTs | D02 (KGS bulk file, computed) |
| Texas | about 1.5M logs in the BEG archive plus RRC images since 2004; structured BHT only on G-1 gas completions since about 2011 | D01 |
| US national (digitized) | 400,134 unique BHTs (Stanford 2024); ~530,000 borehole temperatures in NGDS (2014); SMU node 30,000+ corrected BHT sites plus 14,000+ equilibrium sites | L09, D04 |
| Nevada | about 775 oil and gas wells in NDOM's document layer; logs of every wildcat are public | D03 |
| Western Utah (Great Basin counties) | 536 oil and gas wells, 315 wildcats, 49 proposed to 10,000 ft or deeper | D03 |
| Utah wells of opportunity (2013 UGS) | 26 wells with new logged BHTs (Black Rock Desert, Sevier Lake, Bonneville Salt Flats, Great Salt Lake) | UGS NGDS summary |
| Eastern NV and Millard County UT | DOE sedimentary feasibility well database; "temperature values are uncorrected" | GDR 1223 https://gdr.openei.org/submissions/1223 |

Plain reading: the Great Basin has roughly 1-2% of Kansas's BHT count. Most of Stanford's 400k BHTs sit in the Midcontinent, Appalachia and Texas (my inference from sources listed, unverified share). So national ML maps are tuned on sedimentary basins and are weakest exactly where blind hydrothermal systems live. In the West the other temperature sources carry more weight: 938 NDOM geothermal wells including 261 TG wells (D03), SMU equilibrium holes, mineral holes, 2 m probes and water wells.

### F5. In the Great Basin, oil wildcats have already found blind systems, and the signal dwarfs the noise
- **Railroad Valley, Nevada.** Bacon Flat-Grant Canyon oil field sits in a 120-130 C system at about 1,625 m (171 C was also reported by Hulen and others 1991). NBMG says the system would not have been known without petroleum exploration. Nearby Eagle Springs field averages about 93 C at 1,830 m (NBMG site description, https://data.nbmg.unr.edu/public/geothermal/sitedescriptions/nrailroadvalley.pdf). USGS heat flow is 49-76 mW/m2 across most of the basin but up to 234 mW/m2 over the Bacon Flat-Grant Canyon system (https://pubs.usgs.gov/publication/70205980). That is a 3-5x anomaly, far above any BHT error bar.
- **Black Rock Desert, Utah.** Pavant Butte 1 had a corrected BHT of 230 +/- 10 C, an apparent gradient of about 66 C/km against a typical 30-45 C/km. UGS projected more than 150 C under about 350 km2 at 3 km, and about 60 km2 above 200 C at 3 km (UGS NGDS summary; Gwynn et al., Stanford 2013, https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2013/Gwynn.pdf). This area later became part of the FORGE and Fervo Cape Station neighbourhood (context from L07, not re-verified here).
- **Wendover / Great Salt Lake Desert.** Hot brine wells suggest hydrothermal fluid rising along graben-margin faults (UGS NGDS summary).
- Implication: for big blind systems the BHT anomaly is +30 to +100 C, which is 2-6 sigma even for a +/-16 C single BHT. The noise mostly matters for (a) marginal 100-130 C binary targets, (b) false negatives where cold groundwater masks heat, and (c) gross errors that create fake anomalies. The model should be built around those three failure modes.

### F6. How to put noisy BHTs into a probabilistic model (a concrete design)
1. **Latent field.** Model true temperature T(x, z) as conductive background (heat flow, conductivity, sediment thickness, as in USGS Great Basin 3D model and INGENIOUS) plus a convective anomaly term. The anomaly term is what we sell. Give it a sparse, heavy-tailed prior (most places zero, a few places large), for example a horseshoe or spike-and-slab Gaussian process, so a single hot well can create a localized plume rather than being smoothed away.
2. **Observation model per reading type.** For a raw BHT: T_obs = T(x, z) - b + e. The bias b is positive and comes from a hierarchical prior: b ~ f(depth, time since circulation, mud type, decade, logging company, basin). Its parameters are learned from paired data (BHT vs DST, Horner, or later static log in the same well). Kansas (6,950 multi-BHT wells), the SMU 14,000 equilibrium sites, North Dakota's static program and our own re-logs are the training pairs. Noise e has a reading-type-specific sigma from F1.
3. **One-sided information.** A raw BHT with unknown shut-in time is close to a lower bound. Use a skewed likelihood (for example, a skew-normal or a shifted log-normal bias), not a symmetric one. This keeps a cold BHT from pulling the field down as hard as a hot BHT pushes it up, which is the correct physics.
4. **Gross-error mixture.** Each reading has a small prior probability (start at about 2-5%, unverified, learn it) of being junk (unit, depth or keying error), modeled as a broad Student-t or uniform component. The posterior junk probability per well is a useful output: it tells the team which scanned header to re-read.
5. **Masking state.** Add a latent "hydrologically cooled" indicator tied to carbonate aquifer maps, flow-path models and shallow-cold/deep-hot well shapes, so a cold shallow BHT in a known carbonate flow system is down-weighted for predictions below the aquifer (Railroad Valley lesson).
6. **Metadata recovery is a model input.** OCR of scanned headers (D01, D07) recovers time since circulation, run number, depth and units. Each recovered field moves a reading up the quality ladder (from +/-16 C to about +/-8 C, or to +/-3 C if it yields a Horner set). The model should carry "metadata present" flags so that improvements show up as narrower posteriors without retraining.
7. **Outputs that matter for land.** For each parcel, report P(T at 2 km >= 150 C), P(convective anomaly present), and the expected value of information (how much one equilibrium log or one 2 m probe line would shrink that probability's spread). Rank leasing and sensing by this value-of-information, not by mean temperature.
8. **Calibration check.** Use leave-one-out on wells with static logs and report coverage (the share inside the 90% band). EGU26-13093 got 87% for 90%, a sign that BHT error bars are usually set too tight. Inflate until coverage is right.

## Datasets
| Name | Access | Coverage | Value for blind detection |
|---|---|---|---|
| SMU NGDS node (GDR 1704) | Free, GDR, 21.6 GB | US; 30,000+ corrected BHT sites, 14,000+ equilibrium sites | Equilibrium sites are the best calibration pairs; western holes from 1970s-80s geothermal exploration |
| Stanford InterPIGNN (GDR 1592) | Free API and ArcGIS | CONUS 0-7 km, 18 km2 cells, 400k Harrison BHTs | Baseline to beat; residuals vs our wells flag anomalies |
| AASG/NREL BHT aggregation (GDR 252) | Free | National, state survey contributions | Raw-ish BHTs with some metadata; no accuracy assessment |
| KGS elog scan index with BHT | Free bulk ZIP | Kansas, 74k wells, 212k readings, 6,950 multi-BHT wells | Best public set to learn the bias model; not a blind-hydrothermal province |
| KGS DST database | Free bulk ZIP | Kansas | DST vs BHT pairs for bias learning |
| Texas RRC / BEG logs | Images; $10/scan BEG; G-1 BHT structured since about 2011 | Texas | Huge, mostly illegible; EGS and sedimentary more than blind hydrothermal |
| North Dakota static temperature program | NDGS newsletters, data on request (unverified) | Williston, 25 wells | Static-vs-BHT pairs; method precedent |
| NDOM oil, gas and geothermal well documents | Free, scanned | Nevada; about 775 O&G wells, 938 geothermal wells | Every wildcat log header public; the core western BHT source |
| Utah DOGM well files | Free, scanned PDFs | Utah; 536 wells in western Great Basin counties | Header BHTs need OCR; Pavant Butte-type anomalies |
| UGS NGDS wells-of-opportunity data | Free | 26 Utah wells | Fresh logged BHTs with stated error bars |
| GDR 1223 eastern NV / Millard UT well database | Free | Elko Basin, Railroad Valley, Steptoe, Millard Co. | Uncorrected temperatures, permeability and pressure from oil wells in basins with known blind heat |
| USGS Great Basin 3D temperature model (doi:10.5066/P149FR54) | Free | Great Basin | Conductive background to subtract |

## What dominates uncertainty (this slice)
1. **Missing metadata on each BHT** (time since circulation, true depth, units, mud). This sets whether a reading is +/-3 C or +/-16 C.
2. **Basin- and era-specific cold bias** that has never been calibrated in the Great Basin. Harrison was built in Oklahoma. Western carbonate and volcanic sections with lost circulation may behave differently (unverified).
3. **Hydrologic masking.** Cold aquifers over hot reservoirs give false negatives, and these are the blind systems we most want.
4. **Sparsity.** About 1,300 oil wildcats across Nevada and western Utah means most parcels have no BHT within 10-20 km. Here the BHT term contributes little and other sensors must carry the model.
5. **Gross errors** that create fake hot spots. One junk 200 C reading can trigger a lease spend.
6. **Deep extrapolation.** Corrections are not established below 3-4 km, and only ~3% of US data is deeper than 4 km (L09).

## What a sensor could fill
- **Re-log idle and temporarily abandoned oil wells, and deep water wells, to equilibrium.** Our ranch drop probe (prior hardware pick) can do this. Each log turns a +/-16 C point into a +/-1 C profile and gives a BHT-vs-static pair to calibrate the bias model. North Dakota's 25-well program shows it is doable with a state survey's budget. Target: 50-100 western wells (Nevada and western Utah wildcats with surviving casing, plus deep ranch wells). The full-profile shape also reveals convection (isothermal or inverted sections) and masking (cold top, hot bottom), which a single BHT can never show.
- **A slim, long-endurance memory gauge left in a shut-in well for days to weeks** to record the thermal recovery curve directly. This gives a true Horner or full-recovery fit and the in-situ thermal diffusivity that Schölderle found worth up to 8.3 K. It is a cheap logger on a wireline, built from the drop probe.
- **Fiber-optic DTS (distributed temperature sensing) in a single accessible deep well** per basin, as a "reference well" that anchors the bias model and the masking state.
- **2 m temperature probes and E-field MT nodes** (prior pick) fill the gaps between sparse wells, where F4 says the BHT term is nearly empty.
- **A software "sensor":** vision-model OCR of every scanned header in NDOM, Utah DOGM and NBMG archives (D03, D07). It is cheap and recovers the metadata that dominates uncertainty item 1.

## Implications for a better model
1. Never feed corrected BHTs to the model as exact numbers (Stanford and most ML maps do this). Feed raw BHT plus metadata, and let a learned, hierarchical bias model with skewed, heavy-tailed likelihoods do the correction. This alone should narrow honest error bars and cut false hot spots.
2. Use a quality ladder (F1) with per-type sigma. A model that weights a 1 C log and a 16 C header equally throws away about 15x of information.
3. Treat the convective anomaly as a sparse, heavy-tailed latent field. Big blind systems (Railroad Valley, Black Rock Desert) are 2-6 sigma signals even in single BHTs. The model must not smooth them away.
4. Add an explicit hydrologic masking variable for carbonate and basin-fill aquifers. It turns some "cold" wells into "unknown below the aquifer", which is where cheap rights on unloved acreage sit.
5. Learn the bias from Kansas, SMU equilibrium sites and North Dakota, then adapt it to the Great Basin with our own 50-100 re-logged wells. This is the only way to calibrate a western correction, and the data would be proprietary.
6. Rank where to log and where to lease by value of information. One equilibrium log near a lone hot BHT on cheap private ranch land is the highest-alpha single action this slice finds.
7. Check calibration with leave-one-out coverage and inflate error bars until the 90% band holds 90% of wells (the European model reached 87%).

## Sources
- Peters & Nelson 2009, AAPG Hedberg, criteria for BHT and Horner (cites Hermanrud et al. 1990, +/-8 C): https://www.searchanddiscovery.com/abstracts/html/2009/hedberg/abstracts/extended/peters/peters.htm
- EGU2009-1250 (Horner vs Cooper-Jones, 18 wells, 71 pairs): https://meetingorganizer.copernicus.org/EGU2009/EGU2009-1250-3.pdf
- EGU26-13093 (Monte Carlo BHT + 3D Empirical Bayesian Kriging, Molasse Basin): https://meetingorganizer.copernicus.org/EGU26/EGU26-13093.html
- EGU24-10641 (Monte Carlo BHT uncertainty, >300 wells): https://meetingorganizer.copernicus.org/EGU24/EGU24-10641.html
- Schölderle et al. 2022, Energies: https://www.mdpi.com/1996-1073/15/17/6367
- Petroleum Geoscience 7(3):241 (2001): https://www.earthdoc.org/content/journals/10.1144/petgeo.7.3.241
- Deming 1989 (citation): https://dggs.alaska.gov/pubs/id/32042
- Whealton et al. 2015 (GPFA-AB BHT corrections): https://gdr.openei.org/files/682/2_GPFA-AB_BHTCorrections.pdf
- NDGS static temperature program: https://dmr.nd.gov/ndgs/documents/newsletter/2020Winter/Using_Static_Temperatures_to_More_Accurately_Predict_Geothermal_Gradients_in_the_Williston_Basin.pdf ; https://www.dmr.nd.gov/ndgs/documents/newsletter/2019Winter/Williston_Basin_Static_Temperature_Logging_Program_Continues_to_Yield_Results.pdf ; https://www.dmr.nd.gov/ndgs/documents/newsletter/Summer%202015/Preliminary%20Results%20of%20the%20Williston%20Basin%20Heat%20Flow%20Study%20Using%20Temporarily%20Abandoned%20Oil%20Wells.pdf
- USGS Williston subsurface temperature grids: https://www.sciencebase.gov/catalog/item/6447fb08d34ee8d4aded3b87
- USGS Railroad Valley heat flow: https://pubs.usgs.gov/publication/70205980
- NBMG Railroad Valley site description: https://data.nbmg.unr.edu/public/geothermal/sitedescriptions/nrailroadvalley.pdf
- GDR 1223 eastern Nevada / Millard County well databases: https://gdr.openei.org/submissions/1223
- UGS NGDS data summary (Pavant Butte 1, wells of opportunity): https://geology.utah.gov/docs/geothermal/ngds/supplemental/summary_report/NGDS_data_summary.pdf
- Gwynn et al. 2013, Stanford Geothermal Workshop: https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2013/Gwynn.pdf
- AASG wells data (EGS test site task): https://www.osti.gov/biblio/1148807
- Prior repo files: ../../evidence/L09, D01, D02, D03, D04, D07; ../../../hardware/MEMO.md
- Goutorbe, Lucazeau & Bonneville 2007, Geophys. J. Int. 169 (Australian BHT method comparison): cited from memory, not fetched (unverified)
