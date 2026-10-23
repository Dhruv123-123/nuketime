# M20: Thermal gradient (TG) hole archives and mining holes with temperatures: volume, digitization state, and AI extraction

Slice M20, model track. Date: 23 Oct 2026. This file builds on `../../evidence/L16-gtc-holes.md` (USGS OFR 99-425: 786 industry TG holes, 82 prospects; DOE Industry-Coupled Program; NREL Mining G.O.L.D.), `../../evidence/D06-mining-assessment.md` (mining-hole discoveries, no Nevada filing duty, directional-survey temperatures), `../../evidence/D07-scanned-logs.md` (raster-log economics, header OCR cost), `M05-heat-flow-databases.md` (SMU node, 379 clean Great Basin points) and `M06-water-well-temperature.md` (NDWR driller temperatures). It does not repeat them. What is new here: (1) live counts I pulled myself from the NBMG NGDS services: 2,002 scanned well-log PDFs, 442 distinct industry TG boreholes with scanned logs, by company, and zero LAS files; (2) the NBMG borehole-temperature layer (10,991 records) split by source and use, including the hot "mining" water wells; (3) hot-rock evidence from producing Carlin-trend gold mines; (4) a concrete AI pipeline to turn scanned T-z plots and field sheets into full temperature profiles, and why the full profile (not one gradient) is the real prize; (5) TG archives as a source of trustworthy NEGATIVE labels. Web budget used: 9 searches, 8 fetches (3 blocked: NBMG grey-literature index, NBMG Garside gradient report .doc, PMC VeerNet page), plus about 12 direct ArcGIS REST queries.

## Bottom line

The 1970s-80s industry TG archive is real, large, and still mostly illegible. The public tables carry one number per hole (a straight-line gradient), but the scanned PDFs behind them carry full temperature-depth curves, repeat logs, thermal conductivity and lithology. NBMG alone serves 2,002 scanned log PDFs, 773 of them on 442 distinct industry TG boreholes (AMAX, Chevron, Getty, Sunoco/Aminoil, Anadarko, GSI/GRI, Geonomics and others), and 0 of 2,002 have a LAS file. USGS OFR 99-425 adds 786 mostly Phillips holes as single gradients, and the rest of the Phillips/Chevron archive (100+ prospects) appears never to have been released. Mining holes are the bigger, faster-growing pool: more than 2,000 Nevada holes a year, almost none with a public temperature, but their direct signals are strong where they show up (Florida Canyon water wells at 132 C by air lift; Meikle mine rock at 140-160 C). For the model, the move is to (a) digitize every scanned T-z curve into a full profile with a vision model plus physics checks, (b) treat each source with its own error model, (c) use the dense, cold, failed-prospect TG grids as rare high-quality NEGATIVE labels, and (d) fill the mining gap with a ride-along memory thermometer that rides in the mining driller's survey or core run. Compute is cheap (well under $1 per PDF). Access and linkage to coordinates is the hard part. This is not too small: it is the cheapest way to add hundreds to thousands of high-grade temperature profiles in exactly the Great Basin terrain where M05 shows clean public points sit about 38 km apart.

## Findings

### F1. NBMG already scanned the Nevada industry TG logs, but only as PDFs (my REST queries)
- The NBMG "WellLog" NGDS service lists **2,002 log records**. Every one has a `ScannedFileURL` (PDF). **None has a LAS file** (query `LASFileURL <> ''` returns 0). Source: https://web2.nbmg.unr.edu/arcgis/rest/services/NV_Data/NVWellLogs/MapServer/0 (queried 23 Oct 2026). The scanning was done in 2012-13 for the AASG NGDS project (source field values "NBMG, May'13" etc.).
- By well type: **773 records are on "Thermal Gradient" wells**, on **442 distinct TG boreholes**. The rest are industrial production, injection and observation wells (Brady, Dixie Valley, Steamboat and others).
- By log type: 326 "Temperature Log", 56 "Temperature", 34 "Sub-Surface Temperature Survey", 69 "Lithology Log | Temperature Log", 18 "Temperature And Lithologic Logs", 16 "Temperature/Lithology", plus thermal conductivity sheets. So roughly **500+ scanned temperature curves** exist in this one service.
- By company keyword (all log types): Brady Power Partners 133, **AMAX Exploration 154** (two spellings), Geothermal Services Inc 75, **Chevron 187** (three variants, some with Geonomics), Getty Oil 54, Earth Power 32, Columbia Mining 35, Sunoco/Aminoil 17, Anadarko 15, plus Ormat, Oxbow, True Geothermal. **Phillips does not appear**, which fits L16: Phillips data went through CalEnergy to DOE/INEEL and USGS released only gradients.
- TG wells by county: Washoe 155, Pershing 150, Elko 146, Churchill 143, Humboldt 81, Lander 43, Eureka 33. Elko and Lander are gold country with few known plants, so these holes cover terrain the plant-centred datasets miss.
- Each record carries township-range-section, depth, log date, and a link to a PDF such as `.../geothermal/logs/27-007-80001/27-007-80001_TEMP.pdf` (Elko, GSI/GRI hole 29-80-RV1, 500 ft, logged 1980). The structure is regular, so batch download and parsing is simple.

### F2. The NBMG borehole-temperature layer is mostly water wells, and its mining subset is small but very hot (my REST queries)
- **10,991 temperature records.** By source: NDWR driller logs 7,368, Great Basin Geochemical Database 3,105, NBMG/NDOM oil-gas 518. Units are all C. Source: https://web2.nbmg.unr.edu/arcgis/rest/services/NV_Data/NVBoreholeTemperatures/MapServer/0
- 1,297 records are at or above 50 C and 408 at or above 100 C (most at known systems).
- By use: **226 "Mining" wells and 82 "Dewater" wells**. 53 mining wells are at or above 35 C. 41 mining/dewater/exploration wells are at or above 50 C.
- Example: Pegasus Gold water wells 6 and 7 (Quinn River Valley, Pershing County, T31N R33E sec 3, 750-785 ft) report **93 C and 132 C by air lift** (1996). This is the Florida Canyon mine that NREL cites (223 F, 160 gpm). It shows the public table can confirm mining heat when a water-well permit happened to be filed.
- Eureka County mining wells cluster at **50-60 C** (about 20 wells). That is the Carlin trend dewatering field.
- **The table has no industry TG holes at all.** The AMAX/Chevron/Getty temperatures live only in the PDFs of F1 and in the SMU node. So the "public Nevada temperatures" most people query skip the best-quality pool.

### F3. Carlin-trend gold mines show hot rock at depth that no heat-flow map uses
- Barrick's Meikle underground mine (Goldstrike complex) has rock at **140-160 C (280-325 F)** in the Lower Rodeo zone. It needs heavy refrigeration to keep air near 80 F. Source: E&MJ, https://www.e-mj.com/?p=5358
- Turquoise Ridge (Getchell trend) is another known hot mine (Cassinerio and Muntean 2011, https://nbmg.unr.edu/staff/pdfs/CassinerioMuntean_TurqRidge_GSN2011.pdf; temperature detail not fetched, unverified).
- NBMG keeps a geothermal site description for the Carlin area (https://data.nbmg.unr.edu/Public/Geothermal/SiteDescriptions/Carlin.pdf; not fetched).
- These are deep (several hundred m to over 1 km), equilibrated rock temperatures inside operating mines. They are better data than most TG holes, and they are not in SMU or USGS compilations (inference from M05's source list).
- Mines measure this for ventilation design and safety. The data exist in mine-engineering files and are private.

### F4. Mining-hole volume dwarfs geothermal drilling, but temperature capture is accidental
- More than **2,000 mining holes a year in Nevada**, vs 31 geothermal wells in 2017 (NREL 2022, via D06). Over 40 years that is on the order of **80,000+ holes** (computed, assumes a flat rate).
- No Nevada rule requires a temperature log or reporting hot fluid (NREL 2022). Temperature exists in three accidental forms: (a) directional-survey tool sensors (unequilibrated, digital at the contractor), (b) driller and geologist logs ("hot water", "steam", "hot rods"), (c) water-supply and dewatering permits (F2).
- The directional-survey market is dominated by a few contractors and cloud platforms (for example IMDEX/Reflex). Whether their cloud stores tool temperature by default is (unverified). This is the single most valuable data-deal question in this slice.

### F5. DOE Industry-Coupled and UGS/EGI archives are public but also scanned
- The DOE Industry-Coupled Program (1977-82, 14 sites in NV and UT) required data release for unrestricted use (L16). Its reports are on OSTI and UNT Digital Library as scanned PDFs, for example https://digital.library.unt.edu/ark:/67531/metadc1055320/m2/1/high_res_d/5053058.pdf, and at NBMG, for example Hill 1979 Soda Lake gradient holes (https://data.nbmg.unr.edu/public/Geothermal/GreyLiterature/Hill_SodaLake_GradientHoles_1979.pdf) and Katzenstein 1976 San Emidio (https://data.nbmg.unr.edu/public/Geothermal/GreyLiterature/Katzenstein_SanEmidioWells_Results_1976.pdf).
- Utah: the UGS/EGI "Temperature Gradient Database" (2004, CC-BY, maintainer G. Nash, EGI) links to a UGS web page. The hole count is not given (https://data.amerigeoss.org/dataset/utah-forge-temperature-gradient-database-a5814). The EGI archive holds about 500 reports and cores from 180+ geothermal holes (L16).
- NBMG also sells Garside's 1994 low-temperature assessment (OF1994-02d, 108 pp, originally ASCII/Lotus disk; https://pubs.nbmg.unr.edu/Nevada-low-temp-geotherm-CD-p/of1994-02d.htm) and has a Garside "Gradient" project report online as a .doc (https://nbmg.unr.edu/staff/GarsideL/2020_Webpage/Geothermal/Gradient/Final_Rpt.doc; blocked by TLS, content unverified). Its title suggests NBMG has already compiled a Nevada gradient-hole list that may go beyond the REST service.

### F6. AI extraction: what works now
- **Header and field-sheet text** (hole ID, location, depth, date, "max temp", gradient) is a form-reading task. Vision-language models handle it at about $0.0001-0.001 per page (D07).
- **T-z curves** are the hard part, but much easier than oil-field raster logs: one curve, often hand-plotted on graph paper, with a few labelled axes. A workable pipeline: (1) a VLM finds axes, tick labels and units; (2) a classical step fits the pixel-to-value transform from the ticks; (3) a segmentation model or color/line tracing extracts the curve; (4) the VLM also reads any tabulated depth-temperature columns, which many 1970s sheets include; (5) physics checks: temperature must be within plausible ranges, the gradient near the bottom must match the gradient reported in OFR 99-425 or SMU for the same hole, and repeat logs must converge with time.
- Published curve-digitizing work exists for raster well logs: VeerNet (Journal of Imaging 2023, 9(7):136, https://www.mdpi.com/2313-433X/9/7/136; accuracy figures not retrieved because the PMC fetch was blocked). KIT/LBNL (EGU26-5223, https://meetingorganizer.copernicus.org/EGU26/EGU26-5223.html) digitized legacy Upper Rhine logs for ML but gave no accuracy numbers. The USGS/DARPA CriticalMAAS competition released training data for AI extraction from scanned geologic maps (https://www.usgs.gov/data/training-and-validation-data-ai-critical-mineral-assessment-competition-ver-20-july-2025). Nobody has published a benchmark on scanned geothermal T-z plots (as far as I found).
- **Built-in validation.** For the 786 OFR 99-425 holes, USGS already published the bottom gradient. If the same holes' PDFs are found (SMU node scans, INL), the extracted curve can be scored against that gradient automatically. That gives a free test set.
- **Mining text.** Use NREL's vocabulary ("steam, geysering, hot pipe, increased mud temperatures, artesian flow, boiling", plus sinter/opal/chalcedony) over NBMG mining-district files and county reports. A VLM can also read degree values written in drill-log margins.

### F7. Why full profiles beat one gradient
- A straight-line bottom gradient hides the shape. Shape is the blind-system signal: an isothermal top then a steep bottom (cold groundwater lid over heat), a reversal (lateral outflow from a nearby upflow), or a convex curve (upflow in the hole). Blackwell (1983, via M05) says reversals are "very common" in Nevada exploration holes.
- A reversal at hole A points toward a source tens to hundreds of meters to km away, in the direction of flow. That is a direction vector, not just a scalar. One extracted profile can move the posterior over a whole cell.
- Repeat logs on the same hole (often 2-3 runs over weeks) let us estimate the equilibrium gradient and the drilling disturbance, so the error bar shrinks from roughly ±20-30% to a few percent (estimate, unverified).

### F8. TG archives are the best source of true negative labels
- Phillips drilled 623 holes and Chevron 83 across 82 prospects (L16). Only a handful of those prospects became plants. Most of the remaining dense grids say "we looked hard and it was not hot enough at 100-500 m."
- That is the negative label geothermal ML lacks: M05 and Mordensky et al. (2023, F1 < 0.10) show models fail on features and labels, and random "no known system" negatives are polluted by undiscovered blind systems.
- Caveat: "cold at 150 m" is not "cold at 1.5 km", especially under a groundwater lid. So negatives must be depth-aware (censored), not hard zeros.

## Datasets

| Dataset | Access | Coverage | Value for blind detection |
|---|---|---|---|
| NBMG WellLog NGDS service (NV_Data/NVWellLogs) | Free ArcGIS REST + PDF links | 2,002 scanned logs; 773 on 442 industry TG boreholes; 0 LAS | Very high. Full T-z curves, conductivity, lithology from AMAX, Chevron, Getty, Sunoco, GSI and others; ready to bulk-digitize |
| NBMG BoreholeTemperature service (NV_Data/NVBoreholeTemperatures) | Free ArcGIS REST | 10,991 single readings; 226 mining + 82 dewater wells | Medium. Mining subset flags hot mine water (Florida Canyon 132 C, Carlin trend 50-60 C) |
| USGS OFR 99-425 industry TG holes | Free, pubs.usgs.gov | 786 holes, 82 prospects, NV/UT/OR, one gradient each | High as validation targets and negative labels; profiles need the original scans (INL/CalEnergy) |
| SMU node scanned field notes (GDR 1704) | Free, 21.6 GB | 44,000+ US wells; about 95% of bytes are scans (M05) | Very high if digitized; overlaps NBMG |
| DOE Industry-Coupled reports (OSTI, UNT, NBMG grey literature) | Free scanned PDFs | 14 NV/UT sites, 1977-82 | Medium-high. Profiles and gradient maps around now-producing fields; good training analogues |
| UGS/EGI TG database and EGI archive | Free web / archive visit | Utah; 180+ geothermal holes, about 500 reports | Medium-high for Utah blind targets (unverified count) |
| Unreleased CalEnergy/Phillips/Chevron, Union, Republic, Hunt files | Private or orphaned (inference) | 100+ prospects | Very high. Buy, or find via INL and successor companies (CalEnergy is now BHE) |
| Directional-survey temperatures (mining contractors and claim holders) | Private, data deal | Likely tens of thousands of NV holes (unverified) | Very high volume, low per-hole quality (unequilibrated) |
| Mine ventilation / rock-temperature records (Meikle, Turquoise Ridge, others) | Private, mine engineering | Deep, equilibrated | High, few points but deep and exact |
| NREL GDR 1279 mining public-data source list | Free, CC-BY | Seed list of archives | Pipeline seed |

## What dominates uncertainty

1. **How much of the industry archive was never released.** We know 786 + 442 holes. The CalEnergy archive covered 100+ prospects, and other companies (Union, Republic, Hunt, Sunoco) drilled too. The real total could be 2-5x larger (unverified). This is the largest swing in data volume.
2. **Location error.** Most 1970s holes are located only by township-range-section (about ±400-800 m), sometimes with only a hole number on a prospect map. Halos are a few km wide (M05), so this is usually fine, but it hurts direction-of-flow inference.
3. **Equilibrium.** Single logs soon after drilling, and all mining survey readings, are disturbed. Error depends on the time since circulation, which is often not recorded.
4. **Depth censoring.** Median TG hole depth is about 300 ft (L16). A cold lid can mask heat below. A "cold" hole is only a lower-bound negative.
5. **Selection bias.** Holes were drilled where companies already suspected heat. Without modelling that choice, the data overstate heat near prospects and leave the rest blank.
6. **Whether mining contractors' clouds keep tool temperatures** (F4). If yes, the mining pool is huge and digital. If no, it is mostly text hints.
7. **Extraction accuracy on hand-drawn plots.** Untested. It can be measured cheaply against OFR 99-425 gradients.

## What a sensor could fill

- **Ride-along memory thermometer for mining drills (the new idea from this slice).** A small, rugged temperature logger (like a downhole memory gauge, about $200-500 in parts, unverified) clipped into the core-barrel inner tube or the survey tool run, recording T every few seconds. The mining driller does not change their work. We log bottom-hole temperature on every run and, with stops, a crude T-z profile. Offer it free to claim holders and drill contractors in exchange for the data and a geothermal right-of-first-refusal or royalty swap (D06). Over 2,000 holes a year in Nevada means thousands of new deep temperature points a year at near-zero drilling cost. Equilibrium correction uses the known circulation time, which the logger records itself.
- **Re-entry logger for old TG holes.** Many 1970s-80s TG holes were completed with small water-filled pipe (unverified share still open). A slim (under 1 inch) thermistor or fiber probe on a reel can relog them now, 40+ years after drilling, so they are fully equilibrated. This turns a disturbed old log into a research-grade one and tests whether the old gradient was right. It fits the prior hardware pick (ranch drop probe): same reel, smaller probe.
- **Mine-wall and dewatering-water loggers.** Inside operating hot mines and on dewatering pump discharge, simple loggers give deep equilibrated temperatures and flow. Mines already monitor this, so a data deal may be enough.
- **Targeted new 2 m probes and shallow TG holes** where extracted profiles show reversals pointing off-hole. The profile tells us which direction to walk.

## Implications for a better model

1. **Make the profile the unit of data, not the gradient.** Extract full T(z) curves from the 500+ NBMG scanned temperature logs first, then SMU and DOE scans. Feed the model profile-shape features: bottom gradient, curvature, reversal depth and size, isothermal-lid thickness. Use reversals as directional evidence in a 2D/3D advection-aware field.
2. **Use a source-specific observation model.** One likelihood per source: equilibrated TG log (σ about 0.1-0.5 C), single early log (bias toward cold or hot depending on circulation), mining survey tool (large, time-dependent bias), air-lift water temperature (mixed-zone average), driller text ("hot", "warm": ordinal, not numeric), mine rock temperature (deep, accurate). Let the model learn each bias with the repeat logs and re-entry relogs as calibration.
3. **Add depth-censored negatives.** Encode each cold TG hole as "T at depth d is below x" and let the conductive extrapolation carry the uncertainty downward. Use failed Phillips/Chevron prospects as the main negative set. This should cut the false-positive rate that random negatives cause.
4. **Model the drilling decision.** Fit a propensity model for "where did 1970s companies drill" from what they could see then (hot springs, early heat flow, geology). Use it to correct the bias in F-score evaluation and in the prior.
5. **Self-scoring extraction.** Score the AI digitizer against the 786 published gradients and against NBMG holes whose temperature also appears in SMU. Report extraction error as one more term in the observation model, not as a pass/fail gate.
6. **Treat epithermal-gold geology as a feature and mining data as a stream.** Young (under 7-10 Ma) epithermal deposits, hot mine water and hot mines (Meikle 140-160 C) are features. The ride-along logger makes mining drilling a live data stream that Zanskar does not have, as far as its public material shows.
7. **Gap vs Zanskar.** Zanskar uses the public points (M05) and its own wells. The scanned NBMG/SMU profiles are free to anyone but unextracted. The mining stream needs relationships, not money. Both are edges we can own first.

## Sources
- NBMG WellLog NGDS service (queried 23 Oct 2026): https://web2.nbmg.unr.edu/arcgis/rest/services/NV_Data/NVWellLogs/MapServer/0
- NBMG BoreholeTemperature NGDS service (queried 23 Oct 2026): https://web2.nbmg.unr.edu/arcgis/rest/services/NV_Data/NVBoreholeTemperatures/MapServer/0
- USGS OFR 99-425, industry TG profiles, Great Basin: https://pubs.usgs.gov/of/1999/of99-425/webmaps/home.html
- NBMG grey literature examples: https://data.nbmg.unr.edu/public/Geothermal/GreyLiterature/Hill_SodaLake_GradientHoles_1979.pdf ; https://data.nbmg.unr.edu/public/Geothermal/GreyLiterature/Katzenstein_SanEmidioWells_Results_1976.pdf ; https://data.nbmg.unr.edu/public/Geothermal/GreyLiterature/Trexler_GeothermalAssssmtNV_1982.pdf
- NBMG grey-literature directory index (blocked, not read): https://data.nbmg.unr.edu/public/Geothermal/GreyLiterature/
- NBMG Garside gradient report (blocked by TLS, not read): https://nbmg.unr.edu/staff/GarsideL/2020_Webpage/Geothermal/Gradient/Final_Rpt.doc
- Garside 1994, NBMG OF1994-02d: https://pubs.nbmg.unr.edu/Nevada-low-temp-geotherm-CD-p/of1994-02d.htm
- NBMG Carlin geothermal site description (not fetched): https://data.nbmg.unr.edu/Public/Geothermal/SiteDescriptions/Carlin.pdf
- DOE Industry-Coupled era report (UNT): https://digital.library.unt.edu/ark:/67531/metadc1055320/m2/1/high_res_d/5053058.pdf
- Utah FORGE / UGS TG database: https://data.amerigeoss.org/dataset/utah-forge-temperature-gradient-database-a5814
- Meikle hot rock (E&MJ): https://www.e-mj.com/?p=5358
- Turquoise Ridge geology (Cassinerio and Muntean 2011): https://nbmg.unr.edu/staff/pdfs/CassinerioMuntean_TurqRidge_GSN2011.pdf
- Blue Mountain mining-to-geothermal history (NNBW 2004): https://nnbw.com/news/2004/oct/24/states-newest-mining-bonanza-hot-water
- VeerNet raster-log digitization (J. Imaging 2023): https://www.mdpi.com/2313-433X/9/7/136 (PMC page blocked: https://pmc.ncbi.nlm.nih.gov/articles/PMC10381386)
- KIT/LBNL legacy log reconstruction, EGU26-5223: https://meetingorganizer.copernicus.org/EGU26/EGU26-5223.html
- USGS AI for Critical Mineral Assessment training data: https://www.usgs.gov/data/training-and-validation-data-ai-critical-mineral-assessment-competition-ver-20-july-2025
- NREL Mining G.O.L.D. (via D06/L16): https://docs.nlr.gov/docs/fy22osti/81946.pdf
- Sibling files: L16, D06, D07 (../../evidence/), M05, M06 (this folder)
