# M21: Shallow (2 m) temperature surveys as model evidence, and what 10-30 m pushes add

Date: 23 Oct 2026. Slice M21, model track. This builds on `../../../hardware/evidence/H01-*.md` (probe hardware, cost per station, the "heat carpet", BLM IM 2026-024 casual use), `M02` (Argenta miss), `M03` (Granite Springs GeoProbe holes), `M10` (2 m vs satellite physics), `M17` (the 2 m reliability matrix was never published) and `M18`/`M19` (blind case table, negatives). It does not repeat them. New here: **my own analysis of the public INGENIOUS 2 m compilation (3,800 stations, 55 survey areas)**. It gives the first numbers I know of for the blank-valley rate, the noise floor, the seasonal swing, and a rough sensitivity table. There is also a physics and history case (Olmsted 1977) for what 10-30 m depth adds.

Method note: 7 web searches and 3 page reads before the shared WebFetch budget ran out. Then I used direct downloads: the GDR 1391 2 m zip, USGS PP 1044-B and USGS OFR 86-123. The statistics below are my own calculations on the downloaded file (marked "calc"). Which area counts as "known hot" is my own reading (unverified).

## Bottom line

The public 2 m record is small and old: 3,800 stations in 55 areas, almost all in Nevada, mostly from 2007 to 2010. It is also mostly single snapshots. Only 143 stations (under 4%) were ever read twice. Even so, it is the best cheap "is it hot here" likelihood we have. In my analysis, 20 of 55 surveyed areas (36%) show a clear anomaly: at least 3 stations 3 C or more above the local background, or one station 5 C or more above it. The other 35 (64%) look blank, even though they were mostly chosen as prospects. The noise floor is about 1.2 C (robust SD within an area after background normalization). The seasonal wave at 2 m is about ±5 C, and the 1 m to 2 m gradient changes sign with the seasons. So a single reading cannot see anomalies below about 3 C, and the 1.5 m gradient channel is wasted unless it is corrected for season. The physics sets a hard limit: a 2 m probe only sees systems that leak more than about 0.5-1 W/m² near the surface (roughly 6-12 times background). A blind system under a cold aquifer or a thick dry lid (Granite Springs: under 3.5 C at 2 m over gradients above 220 C/km at depth, and Argenta) reads blank. Going deeper fixes most of this. At 10 m the annual wave is about 1% of its surface value. At 30 m it is gone, and a measured gradient gives heat flux to a few tens of mW/m². Olmsted (1977) found a **12 C anomaly at 30 m where 1 m showed only 3.3-3.7 C**. Inside the model, 2 m data should be a censored, noisy observation of a latent shallow heat-flux field. It needs an explicit detection probability that depends on lid thickness, water-table depth and station spacing. A "blank at 2 m" should count as weak evidence everywhere except where a 10-30 m push or a well shows the lid is thin. That detection-probability term is what turns "how much hidden hydrothermal is left" from a guess into a number with honest error bars.

## Findings

### F1. The public record: 3,800 stations, 55 areas, about 2-3% of the Great Basin, mostly 2007-2010 (calc)
- I downloaded GDR submission 1391, the INGENIOUS Great Basin compilation: `2m_temperature_probe_INGENIOUS_regional_data.zip`, 1.08 MB, shapefile plus xlsx. https://gdr.openei.org/submissions/1391 (catalog: https://catalog.data.gov/dataset/ingenious-great-basin-regional-dataset-compilation-a96d7/resource/47973857-756f-431b-a2a0-e7875a87a4f1)
- What is in it:
  - 3,800 stations: 3,636 in Nevada and 164 in California.
  - 55 named areas.
  - Survey groups: GBCGE (UNR Great Basin Center) 2,371; GTP (Geothermal Technical Partners) 734; GBCGE with the Navy GPO 455; Imageair with GBCGE 177; Navy GPO alone 63.
  - Each station has a 2 m temperature (T2m) and "2mDAB", the temperature above the local area background.
  - 1,573 stations also have 1 m and 1.5 m readings.
  - 747 rows are flagged "CD" (seasonally corrected to a date) and 3,053 are "MD" (as measured).
- Readings by year: 2009 had 960 and 2010 had 786. After 2013 there were only 50 to 320 a year, with 166 in 2021 (Granite Springs and Battle Mountain/Argenta). Most stations come from Kratt, Zehner, Skord, Coolbaugh and Shevenell papers.
- Spacing: the median nearest-neighbour distance per area is **614 m** (10th to 90th percentile: 240 m to 1,020 m).
- Footprint: the summed bounding boxes cover about 11,800 km², which is an upper bound. The Great Basin is about 500,000 km² (unverified round figure). So under about 2-3% of it has ever had a 2 m reading. **Almost all of the 2 m "map" is unobserved, not negative.**
- Only **143 stations have a repeat reading**, in 18 areas. Their median range in T2m across repeats is **7.4 C**. This is direct evidence that a single snapshot carries a seasonal error of several degrees.

### F2. Blank-valley rate: about 64% of surveyed areas are blank, despite prospect-biased siting (calc)
- An area counts as positive if it has at least 3 stations with DAB of 3 C or more, or any station with DAB of 5 C or more. By that rule, **20 of 55 areas (36%) are positive and 35 (64%) are blank.**
- Under looser rules: 35 areas have at least one station at 3 C or more, 20 have one at 5 C or more, and 13 have one at 10 C or more.
- The strongest anomalies (max DAB): Lee Hot Springs 54.7, McGee Mountain 54.1, Peterson 50.1, Emerson Pass 46.7, Salt Wells 36.2, Gerlach 33.5, Desert Queen 20.6, Gabbs Valley 19.3, Teels Marsh 17.4, Dead Horse Wells 16.7, Desert Peak 11.6, Silver Peak 10.1, Hawthorne 8.4, and Tungsten Mountain (Edwards Creek) 8.2.
- Blank areas include Dixie Valley (1.9), Dixie/Fairview (2.0), Smith Creek, Buena Vista, Owens Valley, Long Valley (1.5), Granite Springs (3.4), Battle Mountain/Argenta (3.3), Crescent Valley (3.45) and Columbus Marsh (3.5).
- This agrees with the "Boom and Bust" paper. Of about 11 areas surveyed, about 7 showed anomalies and 6 valleys came back blank, each with more than 20 probes at about 1 km spacing. https://openei.org/wiki/Boom_And_Bust_With_The_Latest_2M_Temperature_Surveys-_Dead_Horse_Wells,_Hawthorne_Army_Depot,_Terraced_Hills,_And_Other_Areas_In_Nevada
- Survey sites were picked because they looked promising (springs, faults, play fairway maps). So 36% is a **conditional hit rate given prospect-quality siting**, not a base rate. In a model it is a likelihood for P(2 m positive | system present, siting), not a prior.

### F3. Noise floor and the seasonal wave, measured from the public data (calc)
- **Within-area background noise.** The robust SD of DAB per area has a median of **1.19 C** (10th to 90th percentile across areas: 0.74 to 2.97 C). For DAB below 2 C the SD is 1.22 C. A 3 C threshold therefore sits about 2.5 sigma above background.
- **Raw T2m has a seasonal cycle.** In background stations (DAB below 1 C), a one-harmonic fit gives a mean of **16.1 C** and an amplitude of **5.0 C**. The scatter left after that fit is **2.4 C**, from latitude, elevation, albedo and soil differences across areas. So raw 2 m temperatures cannot be pooled across valleys. The per-area background (DAB) is the usable variable. This matches the physics estimate in H01 of about ±5 C at 2 m with a lag of about 50 days.
- **The 1 m to 2 m gradient is mostly season.** In background stations, T2m minus T1m swings with an amplitude of **4.5 C**. It peaks around 18 January (warm below in winter) and turns negative in summer: monthly medians run from +5.5 C in January to -5.1 C in July. Its raw correlation with DAB is only r = 0.29.
- **After a seasonal-harmonic fit, the gradient carries signal.** The median residual gradient is +0.4 C at DAB 1-3, **+1.5 C at DAB 3-6** and **+6.3 C at DAB 6 or more**, against a residual SD of 1.5 C. So season-corrected multi-depth data hold a second, partly independent heat-flux channel. The public dataset does not use it.
- UNR's own method work supports this. It found that albedo shifts 2 m temperatures by "up to several degrees C" and is corrected with ASTER albedo, and that anomaly contrast is smallest about two months after the coldest air (February-March). https://openei.org/wiki/Improvements_in_Shallow_(Two-Meter)_Temperature_Measurements_and_Data_Interpretation
- The Navy GPO at NAS Fallon (2001) listed the same set of corrections: seasonal drift, albedo, slope aspect and thermal diffusivity. It found Pirouette Mountain at 3-4 C above background over 3-5 km. https://en.openei.org/wiki/Two-Meter_Temperature_Surveys_for_Geothermal_Exploration_Project_at_NAS_Fallon
- A 1986 Geothermics review of Basin and Range shallow surveys reached the same view. Surveys worked best over areas under 2 km² around known upflow, and were less consistent over larger areas. Noise is cut by using mean annual temperatures instead of one-time readings, by physical simulation of ground temperature, or by statistical modelling. https://pubs.usgs.gov/publication/70014477

### F4. Detection record on blind systems: good where the system leaks, blind where it is capped (classification unverified)
**Hits** (a 2 m anomaly over a system later shown to be hot by holes or a plant):
- Desert Peak, a blind producing field: 11.6 C.
- Tungsten Mountain: 8.2 C in 2007 over at least 6 km. Ormat built a 24-26 MW plant there in 2017 (M18).
- SE Gabbs Valley: 19.3 C. Its TG holes reached 124.9 C at 152 m. https://www.usgs.gov/publications/discovery-blind-geothermal-system-southern-gabbs-valley-western-nevada-through
- Salt Wells: 36.2 C.
- Don A. Campbell: 6 km², 19.3 C above background (M18).
- Teels Marsh: 17.4 C, with no known springs. https://www.unr.edu/nevada-today/news/2008/researchers-make-geothermal-discovery-in-mineral-county
- Emerson Pass: 46.7 C.
- Dead Horse Wells: 16.7 C.

**Misses or weak reads:**
- **Granite Springs Valley.** 130 stations, max 3.4 C. Yet TG holes show gradients above 220 C/km and about 96 C at about 250 m (M03, GDR 969 https://gdr.openei.org/submissions/969). This is a clean false negative at 2 m.
- **Argenta / Battle Mountain.** 81 stations, max 3.3 C. Its ten TG wells to about 244 m were also cool (M02), so it is either a true negative or masked at both depths.
- **Columbus Marsh.** In this file the max is only 3.5 C. DRI describes a 4.1 × 1.7 km anomaly there (https://www.dri.edu/publication/3786). So detection depends on the threshold and on season-corrected processing.
- **Dixie Valley.** A producing field, but here 44 stations with max 1.9 C. The survey footprint probably did not cover the upflow (unverified). This shows that survey placement is part of detection.

**Rough sensitivity (calc, unverified classification):**
- About 0.7-0.85 for blind systems with hot fluid within about 100-150 m.
- Near 0 for systems with a cold lid thicker than about 200 m.
- This is the first number for the reliability matrix that M17 lists as never published. It needs the calibration campaign in M17 to firm it up.

**Anomaly footprints are 1.5-10 km²:** Teels Marsh about 2 miles of fault, Columbus about 7 km², Don A. Campbell about 6 km², Tungsten Mountain at least 6 km. At the public median spacing of 614 m, an anomaly of 2 km² or more gets at least 5 stations, so a missed footprint is rarely the cause of a miss. Burial depth is.

### F5. Physics: what depth each probe can "see"
- **Conductive offset.** The extra temperature at depth z from extra heat flux Δq is ΔT ≈ Δq·z/k (Olmsted 1977, fig. 1 logic). https://app.ingemmet.gob.pe/biblioteca/pdf/USGS-PP-1044-B.pdf
  - With k about 1 W/m/K and normal flux of 0.08 W/m², the conductive offset at 2 m is about 0.16 C, which is invisible.
  - To clear a 3 C threshold, a 2 m probe needs Δq of about 1.5 W/m² (calc). At a 1 C threshold, after logging and season fitting, it needs about 0.5 W/m².
  - Olmsted's own figure: in typical material, normal heat flow gives only 0.05 C between 0 and 1 m.
- **What 1 m and 2 m surveys can resolve.** They work where near-surface heat flow is "thousands or tens of thousands times" background, or where steam or hot water sits a few metres down. Results get worse as the thermal water leaking into shallow aquifers gets cooler, and as geology, water-table depth, topography and vegetation vary more (PP 1044-B conclusions).
- **Annual wave with depth.** With a damping depth d of about 2.2 m in dry alluvium (H01), the amplitude ratio is e^(-z/d):
  - 2 m: about 40%.
  - 5 m: about 10%.
  - 10 m: about 1%, so about ±0.15 C.
  - 20 m and below: under 0.01%.
  - (calc)
- **At 10-30 m a single gradient gives heat flux.** Season-free temperatures at two depths 10-20 m apart, read to ±0.02 C, give a gradient to about ±2 C/km. With k known to ±20%, that is heat flux to about ±0.02-0.05 W/m² (calc). This **lowers the detectable excess flux 10-50x compared with a one-shot 2 m probe**. It also makes the reading a quantitative label (W/m²) instead of a threshold flag.

### F6. Historical evidence that 20-30 m shows what 1-2 m misses
- **Upsal Hogback (Carson Desert), from Olmsted 1977 (PP 1044-B).**
  - In September 1975, temperatures at **30 m** in 20 shallow test wells showed an anomaly of **about 12 C** (from under 15 C to over 26 C).
  - At the same place, 1 m surveys in October and December showed only **3.3-3.7 C**.
  - Away from that maximum, "the correlation between the patterns at the two depths appears to be rather poor". A 1 m maximum north of the Hogback did not appear as a separate maximum at 30 m.
  - So 30 m holes give about 3.5x more contrast and change the drawn map.
- **Soda Lakes.** The same paper correlates 1 m with 20 m temperatures. Results were best near a fumarole and steam well where boiling water sits a few metres down, and "more equivocal" over the wider area.
- **Raft River (USGS OFR 86-123).** USGS augered holes to 30 m (100 ft) near The Narrows structure and contoured gradient times conductivity heat flux from them (their Table 2, Fig. 4), alongside 100-500 m and 1,500 m+ holes. So 30 m heat-flux holes were standard USGS practice in the 1970s. https://pubs.usgs.gov/of/1986/0123/report.pdf
- **Granite Springs (PFA, 2017).** It used 10 GeoProbe direct-push holes under 50 m before TG drilling (M03). That is a modern example of the 10-50 m tier.
- **Colorado** also has a public 2 m survey set, so the method is used outside Nevada. https://catalog.data.gov/dataset/shallow-2-meter-temperature-surveys-in-colorado-6d450

### F7. How cold lids and outflow fool the shallow tiers
- **Water table at 10-30 m.** A 2 m probe sits in the dry vadose zone. A 10-30 m push may reach the aquifer itself. If the aquifer carries a warm outflow tongue, the deeper push reads it directly as aquifer temperature, not a conductive tail. That is the strongest outflow detector short of a well.
- **Cold, fast aquifer (Argenta type, carbonate or recharge-fed).** Here the shallow tiers read cold at any depth above the aquifer base. Only a well, or MT/chemistry, sees through. The model must therefore carry lid thickness as a latent variable. A probe reading "cold" at 30 m while the water table is at 15 m is stronger evidence against a system than a cold 2 m reading over a 60 m dry lid.
- **Outflow, not upflow.** The shallow peak is often kilometres down-gradient of the upflow (Don A. Campbell, Granite Springs; M18). Probes at several depths along the hydraulic gradient let the model trace the plume back up-gradient.

## Datasets

| Name | Access | Coverage | Value for blind detection |
|---|---|---|---|
| INGENIOUS 2 m compilation (GDR 1391) | Free, CC-BY. https://gdr.openei.org/files/1391/2m_temperature_probe_INGENIOUS_regional_data.zip | 3,800 stations, 55 areas, NV and eastern CA, 2006-2021; 1,573 at three depths; 143 repeat stations | The only regional labelled shallow heat set. Gives positives, blank valleys and noise statistics. Use DAB, not raw T |
| Nevada PFA area geodatabases (Granite Springs GDR 969, Gabbs, Crescent Valley, Sou Hills) | Free, GDR / data.gov | A few hundred km² each | Raw 2 m data with corrections, plus co-located TG holes. **Paired 2 m and depth labels**, including the Granite Springs false negative |
| Argenta Rise 2 m (139 points) plus 10 TG wells (INGENIOUS) | Partly public (GRC/SGW; Battle Mountain rows in GDR 1391) | One basin | Double negative. A test of the masking term |
| USGS PP 1044-B (Olmsted 1977), Soda Lakes and Upsal Hogback | Free PDF | Carson Desert | Paired 1 m vs 20 m and 30 m maps. Best published depth-gain calibration |
| USGS OFR 86-123, Raft River 30 m auger holes | Free PDF | Raft River, ID | 30 m heat-flux values beside deep wells |
| NAS Fallon Navy GPO 2 m surveys | GRC 2001 abstract; data partly in GDR 1391 (GPO rows) | Navy land near Fallon | Correction methods; Pirouette Mountain anomaly with a gradient hole |
| Colorado 2 m surveys | Free, data.gov | Colorado | Out-of-Basin test set for transfer |
| UNR long-term 2 m monitoring stations | In GDR 1391 (StCode LT/B) and Coolbaugh/Sladek papers | A few dozen sites | Fit the seasonal model and the albedo correction |

## What dominates uncertainty

1. **Cold-lid and water-table geometry.** This decides whether a system can show at 2 m at all. It is not mapped at parcel scale. Granite Springs and Argenta show that it moves sensitivity from about 0.8 to about 0.
2. **Coverage.** About 97% of the Great Basin has no 2 m reading, and the covered 3% was chosen as prospects. Without an effort and detection model, "no 2 m anomaly" is mostly "never looked".
3. **Single-snapshot noise.** About ±5 C seasonal amplitude, 1.2 C within-area noise, and 2.4 C residual scatter between areas. Only 4% of stations were ever repeated. This fixes the detection threshold at about 3 C.
4. **Upflow vs outflow.** The anomaly location is often not the drill target. This is uncertainty in where, not in whether.
5. **Unpublished reliability matrix.** My 0.7-0.85 sensitivity (leaky systems) and the 64% blank-valley rate are first estimates from about a dozen labelled areas.

## What a sensor could fill

- **Season-free logging at 3 depths** (the prior H01 carpet). This cuts the noise floor from about 3 C to about 0.3-0.5 C, about 6-10x. It also turns the 1-2 m gradient into a usable heat-flux channel (F3).
- **A 10-30 m direct-push thermistor string: the "deep dart".** It gives season-free heat flux to ±0.02-0.05 W/m² and finds aquifer temperature and water-table depth at the same point. It is the missing middle tier between 2 m ($200-500) and TG holes ($150k+). It directly measures the lid-thickness variable that dominates uncertainty. A short push leaving a 1-inch rod or fibre in place under 10 ft fits casual use. A 10-30 m push may need a light permit. Under IM 2026-024 the "near-surface installations under 10 ft" clause is the limit, so 3 m is casual use and 10-30 m needs checking (unverified).
- **Pairing with ranch water wells** (H01 drop probe). Wells give 30-150 m temperatures for free where they exist. The deep dart fills the gaps between wells.
- **A calibration set.** Push 2 m loggers plus 20-30 m darts across about 20 known blind systems and 40 cold controls. That gives sensitivity and specificity per tier, which M17 needs.

## Implications for a better model

1. **Treat 2 m as a censored, noisy reading of a latent shallow heat-flux field, not as a feature.** Likelihood: DAB ~ N(f(q_shallow) + season(t; d, lag) + albedo + area offset, σ ≈ 1.2 C), with σ shrunk to about 0.3 C for logged stations. Do not feed raw T2m to LightGBM, which mixes the 2.4 C scatter between areas into the signal.
2. **Add a detection-probability layer: P(2 m positive | system present) = g(lid thickness, water-table depth, aquifer flow, spacing, threshold).** Set it near 0.8 for depth to hot fluid under about 100 m, and near 0 for a lid over about 200 m. Posterior blind probability is then roughly prior × (1 - P_detect) for surveyed blanks. The 35 blank areas then become graded evidence, not hard negatives. This is the occupancy-detection structure in M15 and M19, fed with real numbers.
3. **Use the season-corrected 1-2 m gradient as a second channel.** The 1,573 public three-depth stations can be refit now with a harmonic season model, and anomalies gain +1.5 to +6 C of residual gradient. This is cheap new signal from free data.
4. **Model depth tiers jointly.** 2 m, 10-30 m darts, water wells (M06) and TG holes (M03) are draws of one temperature-depth column with a lid and an aquifer (M16). A deep dart reading pins the lid, which re-weights every nearby 2 m blank. Value of information is highest for a dart in a 2 m-blank, high-favourability cell (Granite Springs type).
5. **Rank the next 2 m and dart campaigns by unobserved favourability.** About 97% of the Great Basin is unsampled. Point the carpet at high-structure cells with no 2 m data first (M11 FSS list). Then re-survey blank valleys only where the lid is thin.
6. **Use positives to locate upflow as well as detect it.** Fit outflow plume geometry along the hydraulic gradient to multi-depth data. This turns "hot cell" into a drill target and supports a higher step-up price when we farm out.
7. **Be honest about the count.** Public 2 m data alone cannot tell us how much is hidden. Only about 3% of the region is sampled, and sensitivity collapses under thick lids. The undiscovered-systems estimate should carry this detection term explicitly. This is a large, open, cheap-to-fill gap, and it is our edge over a public-layer-only model like Zanskar's GeoCore.

## Sources

- INGENIOUS Great Basin compilation, GDR 1391: https://gdr.openei.org/submissions/1391 ; file https://gdr.openei.org/files/1391/2m_temperature_probe_INGENIOUS_regional_data.zip
- OpenEI 2 m method improvements (Coolbaugh, Sladek et al.): https://openei.org/wiki/Improvements_in_Shallow_(Two-Meter)_Temperature_Measurements_and_Data_Interpretation
- Boom and Bust 2 m surveys: https://openei.org/wiki/Boom_And_Bust_With_The_Latest_2M_Temperature_Surveys-_Dead_Horse_Wells,_Hawthorne_Army_Depot,_Terraced_Hills,_And_Other_Areas_In_Nevada
- NAS Fallon 2 m (Navy GPO 2001): https://en.openei.org/wiki/Two-Meter_Temperature_Surveys_for_Geothermal_Exploration_Project_at_NAS_Fallon
- Shallow subsurface temperature surveys in the Basin and Range, review (Geothermics 15(3), 1986): https://pubs.usgs.gov/publication/70014477
- Olmsted 1977, USGS PP 1044-B: https://app.ingemmet.gob.pe/biblioteca/pdf/USGS-PP-1044-B.pdf
- Urban et al. 1986, USGS OFR 86-123 (Raft River): https://pubs.usgs.gov/of/1986/0123/report.pdf
- Gabbs Valley blind discovery: https://www.usgs.gov/publications/discovery-blind-geothermal-system-southern-gabbs-valley-western-nevada-through
- Granite Springs PFA data, GDR 969: https://gdr.openei.org/submissions/969
- Teels Marsh discovery (UNR 2008): https://www.unr.edu/nevada-today/news/2008/researchers-make-geothermal-discovery-in-mineral-county
- Columbus Salt Marsh (DRI): https://www.dri.edu/publication/3786
- Colorado 2 m surveys: https://catalog.data.gov/dataset/shallow-2-meter-temperature-surveys-in-colorado-6d450
