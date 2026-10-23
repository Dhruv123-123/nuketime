# M05: Heat-flow and thermal-gradient databases (SMU/NGDS, IHFC Global Heat Flow Database 2024, USGS Great Basin heat flow, Blackwell maps). Point density, shallow advective disturbance, and how blind systems hide between points

Slice M05, model track. Date: 23 Oct 2026. This file builds on `../../evidence/D04-ngds-gdr.md` (what GDR/NGDS and the SMU node hold), `../../evidence/L09-temperature-at-depth.md` (BHT corrections and national temperature-at-depth maps), `../../evidence/L02-blind-systems.md` and `M04-bht-corrections.md` (BHT error model, Railroad Valley). It does not repeat them. It adds: (1) the IHFC 2024 global database and its quality flags, (2) the USGS 2022-2024 Great Basin heat-flow and 3D temperature work, with hard counts of how many wells survive quality filters, (3) a density calculation of how much of the Great Basin is actually "seen" by clean heat flow, and (4) how advection both creates and hides blind systems in these maps. Web budget used: 7 searches, 9 fetches (one fetch blocked by robots.txt).

## Bottom line

Public heat-flow data in the Great Basin look dense but they are not. USGS started from **22,535 wells**, removed groundwater wells to get **5,717**, kept **4,672** deeper than 50 m, and found that **4,293 of those (92%) fell outside a ±7.5 °C/km conductive band**. Only **379 wells** met every quality test (Burns et al. 2024). Spread over a Great Basin of roughly 540,000 km² (unverified area), 379 clean points means one per ~1,400 km², a mean spacing of about **38 km**. A hydrothermal "thermal halo" is only **a few km** wide (Burns et al. 2024). So even with no clustering, clean points sit within 3 km of only about **2% of the land**. And the points are clustered: they were drilled preferentially near known hydrothermal systems, which cover only "a few percent" of the Great Basin. The global IHFC database (91,182 points, 2024 release) has the same problem in a worse form: only about **46% of entries have any quality assessment**, and the convection flag is **"unspecified" for 32,737 of ~40,500 assessed entries**. The public maps (Blackwell/SMU 2011 at ~8 km cells; USGS 2022 LOESS conductive maps) deliberately smooth out or down-weight exactly the convective outliers that a blind-system hunter wants. In practice the maps are a conductive background with large holes. Blind systems hide in three places: (a) gaps between points, (b) under shallow cold-water "rain curtains" and interbasin carbonate flow that suppress the shallow gradient (the Eureka Heat Flow Low), and (c) as downweighted "outlier" residuals that nobody has followed up. For the model, this means: use the database as noisy, biased, censored observations of a latent field, not as truth. Build the USGS-style residual for every hole. Give every grid cell an explicit "how well have we looked here" term. Then spend our own sensors where that observation term is weakest and the structural prior is strong. That is the alpha. Zanskar uses the same public points. Nobody has published a map of where the public points are blind.

## Findings

### F1. The IHFC Global Heat Flow Database, 2024 release: big, but mostly unflagged

- The release has **91,182 heat-flow values** from **71,934 locations** and **1,586 publications**, with 62 metadata fields. About 57% of values are continental and 43% marine (ESSD 2026, https://essd.copernicus.org/articles/18/4639/2026/). ThinkGeoEnergy gives 54,553 continental and 36,629 oceanic, and the dataset DOI **10.5880/fidgeo.2024.014** (https://www.thinkgeoenergy.com/ihfc-publishes-2024-global-heat-flow-database/; IHFC portal https://ihfc-iugg.org/products/global-heat-flow-database/data).
- The quality scheme has three parts. The **U-score** grades uncertainty from the coefficient of variation. The **M-score** (M1-M4, or Mx when unknown) grades method quality. The **P-flags** mark perturbations such as convection or fluid flow, topography, climate and sedimentation. A lowercase flag means the perturbation was "recognized but not corrected".
- Only **~46% (41,922 points) have had any quality assessment**. **86.8% have no U-score (Ux)**, and only **2.4% are U1**. **53.8% are Mx** (method quality unknown), and only **2.7% are M1**.
- On the convection/fluid-flow flag, **1,485 entries are corrected**, **2,465 are recognized but uncorrected**, **3,827 are "unrecognized"**, and **32,737 are "unspecified"**. Put simply, for about four out of five assessed points, the database does not tell you whether groundwater moved heat at that site. That is the single most important flag for blind-system work.
- Coverage: at 0.5° x 0.5°, only **7.9% of Earth's surface** and **12.8% of continental cells** have at least one value. North America is described as well sampled, with low interpolation standard deviation (<3-5 mW/m²). But at 0.5° (~45-55 km), "well sampled" is two orders of magnitude coarser than a hydrothermal halo.
- Implication: the IHFC set is good for the regional conductive background and for priors outside the US (Turkey, East Africa, Indonesia, Andes). It is useless for spotting individual blind systems. Its flags should be treated as missing-not-at-random.

### F2. SMU node and the Blackwell maps: many sites, coarse map, smoothing by design

- The SMU node (now GDR 1704) covers 44,000+ wells: 30,000+ corrected-BHT sites and 14,000+ equilibrium sites, plus 6,000+ scanned documents (see D04). The structured table is only ~360 MB. Most of the information about gradient shape is still in scanned field notes: isothermal sections, reversals, multiple logs over time (D04).
- Blackwell et al. (2011) built the third-generation US heat-flow and temperature-at-depth map from **~35,000 sites**, mostly oil and gas, on cells of about 8 km. Stanford's hold-out test found the SMU/NREL temperature maps had a **49.5 °C MAE** (L09). In the Great Basin, the oil and gas BHT share is tiny (M04: about 1-2% of Kansas's BHT count). So the western part of these maps rests on 1970s-80s geothermal TG holes and USGS research holes.
- Blackwell (1983) says the regional Nevada compilation then had only **93 heat-flow measurements**. He noted that geothermal exploration had drilled **10-100x more holes** that were *not* in the regional compilations. He put the northern Basin and Range average at about **85 ± 10 mW/m²**, and argued it is closer to **100 ± 10** once sampling bias is removed. The Battle Mountain High runs **100-150 mW/m²**. The SMU node later absorbed many of those company holes, but the bias he described remains: holes cluster where companies already suspected heat (https://smu.edu/-/media/site/dedman/academics/programs/geothermal-lab/documents/hfinnbr.pdf).
- Blackwell (1983) also reported that **temperature-gradient reversals are "very common"** in exploration holes, which means transient lateral flow. The Black Rock Desert shows **40-60 mW/m² on valley axes** and **80-100 at the margins**, which Mase and Sass explained as downflow in valleys and upflow at the margins. Ranges are "too sparse to test" (same source; Mase 1980, https://data.nbmg.unr.edu/public/Geothermal/GreyLiterature/Mase_HeatFlowBlckRckDsrt_1980.pdf).
- On the Snake River Plain, about **75% of the heat entering the aquifer is carried away** by the regional aquifer, leaving ~25% to be measured conductively (Blackwell 1983). A heat-flow map there understates the deep heat by about 4x. SMU/NREL later found **75% more power potential at 3.5 km** than the 2011 map (L09).

### F3. USGS Great Basin conductive heat flow (2022-2024): the honest numbers

- The USGS data release "Heat flow maps and supporting data for the Great Basin, USA" (DOI **10.5066/P9BZPVUC**, https://www.usgs.gov/data/heat-flow-maps-and-supporting-data-great-basin-usa) compiles SMU (2021) and USGS (Sass et al. 2005) wells. It fits an iterative, weighted 2D LOESS that **down-weights points far from the local trend**, so the map shows conductive background and not convection. It ships three maps: equal weights, gradient-quality weights and conductivity-quality weights. Each well gets a **"residual" attribute**: its departure from background, which USGS says "may help identify" fluid influence (DeAngelo et al. 2023, Stanford Geothermal Workshop, https://pubs.usgs.gov/publication/70240144). No uncertainty map is published.
- Burns et al. (2024, Stanford Geothermal Workshop; https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2024/Burns.pdf; USGS record https://pubs.usgs.gov/publication/70252068) built the 3D temperature model on that map, with a 4 km grid and 1-6 km depths. Key counts:
  - **22,535** wells with temperature data, cut to **5,717** after removing groundwater wells as likely convective.
  - **4,672** of those are deeper than 50 m.
  - **4,293 of 4,672 (92%)** fall outside the ±7.5 °C/km conductive band, so most are "substantially convective".
  - Only **379 wells** met all evaluation criteria.
  - Temperature data were "collected preferentially near hydrothermal systems", which occupy "a few percent" of the Great Basin. Convective halos are "a few kilometres" across.
  - Heat flow is the largest uncertainty in the model. Radiogenic heat production is **1.89 ± 0.95 µW/m³**, and conductivity is 2.4-3.0 W/m/K.
- Sass et al. (2005, USGS OFR 2005-1207, https://pubs.usgs.gov/publication/ofr20051207) is the supporting data for 1970-1990 USGS regional heat-flow studies. It is the backbone of the "clean" research-grade set. (I could not fetch the full report for a site count.)
- Railroad Valley shows the size of the signal: basin heat flow is 49-76 mW/m², with up to **234 mW/m²** over Bacon Flat-Grant Canyon, a 3-5x anomaly that oil wells found by accident (https://pubs.usgs.gov/publication/70205980; M04).

### F4. Density arithmetic: how much of the Great Basin is actually seen

Assume a Great Basin area of about 540,000 km² (unverified round number), and halos of about 3 km radius (the "few km" of Burns et al. 2024). If points were spread evenly with no overlap:

| Point set | Count | Mean spacing | Share of area within 3 km |
|---|---|---|---|
| Blackwell 1983 regional Nevada heat flow | 93 | ~76 km | ~0.5% |
| USGS 2024 wells passing all criteria | 379 | ~38 km | ~2% |
| Non-groundwater wells >50 m | 4,672 | ~11 km | <25% (upper bound) |
| Non-groundwater wells, any depth | 5,717 | ~10 km | <30% (upper bound) |
| All wells with temperature | 22,535 | ~5 km | far less than it looks, because of clustering and shallow, advectively disturbed water wells |

Because of clustering near known systems, the real coverage of the "unknown" land is well below these upper bounds (my inference; unverified number). A practical reading: across **most of the Great Basin, no deep, clean, conductive measurement lies within one halo-width of a given spot**. The heat-flow layer in INGENIOUS and the Nevada PFA is interpolated across those gaps. So it carries the regional trend (the Battle Mountain High, the Eureka Low) and almost no information about whether a specific range-front step-over hides a system.

### F5. How blind systems hide in and between the points

1. **Between points.** At 10-40 km spacing, a 2-6 km halo is simply missed. Faulds and others estimate that **~39% of known Great Basin systems are blind**, and about **75% of total resources** are blind (Coolbaugh et al. 2007, cited in https://www.energy.gov/sites/default/files/2015/06/f23/Track2_Hydrothermal_1.7_Blind_Systems_in_the_Great_Basin_Faulds.pdf). About 90% of known systems sit in favorable structural settings, and that project counted about 200 such settings in one 240 x 400 km transect. Most of those settings have no clean heat-flow point on them.
2. **Under a cold lid.** Shallow cold groundwater, lateral outflow and valley downflow suppress or erase the shallow gradient. The Black Rock Desert valley axes read 40-60 mW/m². The Snake River Plain aquifer takes ~75% of the heat. Carbonate interbasin flow in east-central Nevada is tied to the Eureka Heat Flow Low (Blackwell 1983). A 50-150 m hole in such a setting reads "cold", and the database then reports a *negative* that is really a *masked* positive.
3. **As thrown-out outliers.** USGS removes groundwater wells, down-weights high residuals, and keeps 379 of 4,672 wells. That is correct for a conductive EGS map. For a blind-hydrothermal hunter, it means the hot outliers are filed as noise. The residual field in DOI 10.5066/P9BZPVUC is a ready-made, under-used candidate list.
4. **Offset by outflow.** Lateral outflow plumes put the shallow thermal peak kilometres downstream of the upflow zone. A single hot TG hole can sit over an outflow tongue, not over the drillable upflow. Gabbs Valley was found by play fairway mapping, then 2 m probes, then ~150 m TG wells that read ~120 °C (https://www.usgs.gov/publications/discovery-blind-geothermal-system-southern-gabbs-valley-western-nevada-through). The shallow sensors confirmed it. The regional heat-flow map did not find it.
5. **Hidden in time.** Gradient reversals are "very common" (Blackwell 1983), and many 1970s-80s holes were logged once, soon after drilling. Their reported gradient mixes drilling disturbance with real flow. The raw logs that show this are in the SMU scanned notes (D04), not in the tables.

## Datasets

| Dataset | Access | Coverage | Value for blind detection |
|---|---|---|---|
| IHFC Global Heat Flow Database, Release 2024 (DOI 10.5880/fidgeo.2024.014) | Free download, GFZ Data Services; IHFC portal | Global, 91,182 values, ~54.6k continental | Regional conductive prior, especially outside the US. Flags are mostly missing (convection flag unspecified for ~81% of assessed points). Low value for spotting individual systems |
| SMU node of NGDS (GDR 1704) | Free, GDR, 21.6 GB | US, 44,000+ wells; 14,000+ equilibrium sites | Best US site list. The scanned field notes (about 95% of bytes) hold gradient shape, reversals and repeat logs. High value if digitized |
| USGS Great Basin heat flow maps and supporting data (DOI 10.5066/P9BZPVUC) | Free, ScienceBase | Great Basin; SMU + Sass 2005 wells; three conductive maps; per-well residual | Per-well **residual** is a direct convective-anomaly label. High value as a training signal and candidate list |
| USGS 3D temperature model, Great Basin (Burns et al. 2024) | Free, USGS data release | 4 km grid, 1-6 km depth | Conductive baseline to subtract. It misses convection by design |
| USGS OFR 2005-1207 (Sass et al. 2005) | Free, USGS Pubs | Great Basin research holes, 1970-1990 | Highest-quality equilibrium logs with measured conductivity. Calibration anchor |
| Blackwell et al. 2011 SMU heat-flow and temperature-at-depth maps | Free, SMU / GDR | Conterminous US, ~35,000 sites, ~8 km cells | Legacy baseline. Too smooth for blind work. 49.5 °C MAE on Stanford hold-out (L09) |
| NBMG grey literature (Sass 1976, Mase 1980, Blackwell 1983) | Free PDFs, data.nbmg.unr.edu | Nevada valleys | Hand-drawn isotherms and hydrologic interpretations. Good for labelling cold-lid areas |
| INGENIOUS / Nevada PFA heat-flow layers (GDR 1391, 1351) | Free, GDR | Great Basin | Already used by Zanskar and others. No edge on its own |

## What dominates uncertainty

- **Spatial coverage, not measurement error.** At ~38 km spacing of clean points against a halo of a few km, the main unknown is "was anyone looking here", not "is this reading 5% off".
- **Advective masking of shallow holes.** Most holes are shallower than 150-200 m, and 92% of holes deeper than 50 m are non-conductive. A cold reading in a valley or carbonate terrain is weak evidence of absence. We do not know how many masked systems exist, and this unknown is large.
- **Missing quality flags.** About 54% of IHFC values have no assessment, and the convection flag is mostly unspecified. In the US sets, many holes have estimated rather than measured conductivity.
- **Sampling bias.** Holes were drilled near known or suspected systems. That inflates the apparent heat flow there (Blackwell 1983) and leaves "unknown" land with almost no data. A naive model learns "no data = no heat".
- **Thermal conductivity.** Heat flow equals gradient times conductivity. In the Great Basin, conductivity ranges about 2.4-3.0 W/m/K under basins, and more in alluvium versus carbonate. This adds about ±10-20% to heat flow (inference from the Burns ranges).
- **Outflow geometry.** A hot shallow point does not mark the upflow. The offset can be several km.

## What a sensor could fill

1. **A dense, deep-enough, equilibrium gradient at halo scale.** The gap is 10-40 km spacing against a few-km target. Cheap 2 m probes (already chosen, H-files) find shallow halos where there is no cold lid. They need a deeper partner wherever valleys or carbonate aquifers mask the signal.
2. **Re-logging existing holes (ranch water wells, mineral holes, old TG holes).** The ranch-well drop probe (prior pick) should log **full T(z) profiles at 0.5-1 m steps with ±0.01 °C resolution**, not a single bottom reading. The *shape* (isothermal sections, reversals, curvature) tells you whether water is moving heat in or out. That is the masked-positive signature the databases lack. Re-logging 1970s-80s holes decades later also gives true equilibrium.
3. **Conductivity on site.** A needle-probe or optical-scanning conductivity unit on cuttings or core turns each of our gradients into heat flow. That is the number the models and the IHFC M-score need.
4. **Below the cold lid.** A low-cost 150-300 m DTS-instrumented hole (H11) placed in a "cold" valley next to a strong structural setting tests the masking hypothesis directly. E-field-only MT (prior pick) maps the conductive clay cap and the outflow geometry, which tells you where to place that hole.
5. **Groundwater flow sensing.** A borehole flowmeter or a fibre heat-pulse (active DTS) in water wells measures the Darcy flux. With it, we can correct shallow gradients for advection (Bredehoeft-Papadopulos-style fitting) instead of throwing the wells away. That would turn the 17,000+ discarded groundwater wells back into usable data.

## Implications for a better model

1. **Treat heat-flow points as observations, not as a map.** Model a latent conductive background plus a sparse, heavy-tailed convective anomaly (as in M04). Each hole is an observation with its own forward operator: depth, conductivity method, time since drilling, and a hydrologic-masking term that can be large in valleys and carbonate terrain.
2. **Use the USGS residual as a label.** Ingest DOI 10.5066/P9BZPVUC. The per-well residual becomes a positive or soft-positive label and a candidate list. Combine it with the structural-setting prior (Faulds ~200 settings per transect). A high-residual well in a good setting with no known system and no lease is a direct acquisition target.
3. **Add an explicit "observation strength" layer.** For each cell, compute the probability that an existing system *would have been seen* by existing data. Base it on the distance to the nearest clean or deep hole, hole depth versus likely lid thickness, aquifer type, and 2 m coverage. Posterior blind probability then equals prior favorability times (1 - detection probability), plus adjustments from actual hits. This is the step that gives "how much hidden hydrothermal is there" with honest error bars. It also gives a ranked map of where public data are blind, which nobody has published.
4. **Do not train on interpolated heat-flow rasters.** INGENIOUS and PFA use smoothed heat-flow layers, which leak the regional trend and suppress halos. Use raw points with distance features and kernel encodings, or a GP field, instead.
5. **Correct for preferential sampling.** Model the drilling locations as a point process that depends on prior belief (as in Diggle-style preferential sampling; method from geostatistics, not sourced here). Otherwise the model learns that undrilled land is cold.
6. **Digitize the SMU scanned logs.** Run OCR and figure extraction on the ~19 GB of field notes to recover full T(z) curves, reversals and repeat logs. That gives the hydrologic-masking feature for thousands of holes at near-zero cost, a data edge Zanskar has not published.
7. **Use the IHFC 2024 set for priors outside the US.** It supports the "and beyond" part of the plan: a global conductive background and a list of regions where coverage is under 13% of cells.
8. **Plan sensor placement by value of information.** Our 2 m probes, ranch-well profiles and MT nodes should go where the observation-strength layer is weakest and structural favorability is highest. That is where one measurement moves the posterior most and where land is still cheap.

## Sources

- IHFC Global Heat Flow Database 2024 description, ESSD 18, 4639 (2026): https://essd.copernicus.org/articles/18/4639/2026/ (preprint https://essd.copernicus.org/preprints/essd-2025-341)
- ThinkGeoEnergy on the 2024 release, DOI 10.5880/fidgeo.2024.014: https://www.thinkgeoenergy.com/ihfc-publishes-2024-global-heat-flow-database/
- IHFC data portal: https://ihfc-iugg.org/products/global-heat-flow-database/data
- DeAngelo et al. 2023, New maps of conductive heat flow in the Great Basin: https://pubs.usgs.gov/publication/70240144
- USGS data release, heat flow maps and supporting data, Great Basin (10.5066/P9BZPVUC): https://www.usgs.gov/data/heat-flow-maps-and-supporting-data-great-basin-usa
- Burns et al. 2024, Updated 3D temperature maps for the Great Basin: https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2024/Burns.pdf ; https://pubs.usgs.gov/publication/70252068
- Sass et al. 2005, USGS OFR 2005-1207: https://pubs.usgs.gov/publication/ofr20051207
- Blackwell 1983, Heat flow in the northern Basin and Range: https://smu.edu/-/media/site/dedman/academics/programs/geothermal-lab/documents/hfinnbr.pdf
- Mase 1980, Black Rock Desert heat flow: https://data.nbmg.unr.edu/public/Geothermal/GreyLiterature/Mase_HeatFlowBlckRckDsrt_1980.pdf
- Railroad Valley heat flow (USGS): https://pubs.usgs.gov/publication/70205980
- Faulds et al., Blind systems in the Great Basin (DOE 2015 peer review): https://www.energy.gov/sites/default/files/2015/06/f23/Track2_Hydrothermal_1.7_Blind_Systems_in_the_Great_Basin_Faulds.pdf
- Gabbs Valley blind-system discovery (USGS): https://www.usgs.gov/publications/discovery-blind-geothermal-system-southern-gabbs-valley-western-nevada-through
- Prior repo files: D04, L09, L02, M04, H11.
