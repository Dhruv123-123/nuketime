# M11: Structural settings as a model term. How predictive structure is, and how to map it at scale with ML

Date: 23 Oct 2026. This file builds on `../../evidence/L22-structural-ml.md` (Faulds & Hinz 2015 shares, Gabbs Valley, Brady 3D, slip/dilation tendency method, Lund Snee & Zoback stress, INGENIOUS layers, Qfaults caveats) and `M02-ingenious.md` (Faulds et al. 2026: more than 1,430 favorable structural settings (FSS), setting-type enrichment table, Argenta Rise miss). It does not repeat them. New here: the older quantitative tests of structure (weights of evidence, GPS strain), the feature-importance results from the USGS ML work, how the FSS map was made and why it cannot scale as it stands, and a plan to automate it. Web budget used: 8 searches, 8 fetches. Several conference PDFs gave only abstracts, so some numbers are marked (unverified).

## Bottom line

Structure is the strongest proven *where-to-look* filter for Great Basin blind systems. It is not a *whether-it-is-hot* answer. Three independent tests agree. (1) Weights of evidence in 2002 gave young NE-striking faults a contrast of 2.52 for systems hotter than 160 °C, one of the best layers in the model. (2) GPS strain work in 2002 to 2007 found that geothermal sites cluster in transtensional zones, with most sites within 30 km of the main dextral slip belts. (3) The USGS ML models from 2023 rank "distance to nearest fault" as one of the top two features, with heat flow. Geodetic dilatation, oddly, ranks near the bottom. The FSS map turns this into a list. About 1,430 settings cover about 7.7% of the land and hold most of the 403 known systems. That is roughly a 10x squeeze on search area (calc). But only about one FSS in four or five is likely to hold a hot system (M02 base rate, unverified). So structure leaves about 4 to 5 candidates per real system, and something else must split them: heat, fluid chemistry or conductors. The biggest open opportunity in this slice is scale. The FSS map was drawn by hand by one university group over about a decade, only for the Great Basin, and it misses faults buried under valley fill. An automated FSS detector would do three things: (a) learn fault-network geometry from those 1,430 labels, (b) add buried faults from gravity, Earth MRI magnetics and passive-seismic basement depth, and (c) score each FSS for local stress. It could cover Oregon, Idaho, Utah, New Mexico, Arizona and rifts abroad in months. No public model does this. The sensor that helps most here is a cheap kit that finds buried faults (passive-seismic HVSR nodes plus drone magnetics). It sits alongside the existing pick: 2 m probes, the water-well drop probe and E-field MT.

## Findings

### F1. Older quantitative tests: structure is among the best single layers
- **Coolbaugh et al. (2002), weights of evidence, Great Basin geothermal GIS.**
  - Training sites: 20 high-temperature (>160 °C), 39 medium (100 to 160 °C), 48 low (70 to 100 °C) and 53 warm (37 to 70 °C), with at least 10 km between sites.
  - **Young (≤1.5 Ma) NE-striking faults gave a contrast of 2.52 (confidence 5.17) for >160 °C systems** and 2.57 for power systems. Contrast fell to about 0.9 to 1.3 for cooler systems.
  - NE faults were defined as N62°E ± 45°, perpendicular to the N28°W GPS extension direction. So "faults at a high angle to the extension direction" was already a crude dilation-tendency feature.
  - Other layers for comparison: water-table depth (contrast 3.06), isostatic gravity (2.60), boron (2.03) and young volcanic vents (~2.0). Heat flux and earthquakes scored lower.
  - Plain reading: structure is about as strong as the best hydrology and chemistry layers. It is strongest for the hottest systems, which are the ones a buyer pays for.
  - https://data.nbmg.unr.edu/public/Geothermal/GreyLiterature/Coolbaugh_GeothermalGIS_NV_2002.pdf
- **Blewitt, Coolbaugh, Holt, Kreemer, Davis and Bennett (2002), GRC Trans.**
  - The GPS strain-rate map reached a precision of "a few parts per billion per year" in places.
  - High interseismic strain correlated "significantly" with hot wells and power plants. No coefficient was given (unverified).
  - The paper listed "fault orientation relative to the strain tensor" as the next test. That is the step INGENIOUS later did as slip and dilation tendency.
  - https://researchconnect.stonybrook.edu/en/publications/targeting-of-potential-geothermal-resources-in-the-great-basin-fr/
- **Hammond, Kreemer, Blewitt et al. (2007), GRC Trans., GPS block model.**
  - Inputs: 132 GPS velocities (58 MAGNET, 13 continuous, 61 campaign), fitted with 62 blocks and 221 fault segments locked to 15 km.
  - Results: **most geothermal sites lie within 30 km of the dominant dextral slip zones.**
  - Counterexample: the Mohawk Valley fault has the fastest slip (~3.9 mm/yr dextral) but few geothermal systems.
  - Conclusion: "the component of normal extension is required". Transtension hosts heat; pure strike-slip does not.
  - Resolution limit: slip smears across faults within the 15 km locking depth. Only sums over fault clusters are robust. So GPS strain is a **regional (tens of km)** feature, never a prospect-scale one.
  - https://geodesy.unr.edu/publications/HammondEtAl_GRC_07.pdf
- **Faulds et al. (2012), GeoNZ.**
  - The setting shares from about 300 systems match the later 2015 counts (step-overs ~32%, intersections ~22%, terminations ~22%, accommodation zones ~8%, displacement transfer zones ~5%, pull-aparts ~4%, range-front mid-segments ~3%).
  - The Walker Lane takes about 20% of Pacific to North America plate motion, and about 1 cm/yr of dextral motion bleeds into NW Great Basin extension. Most of the Basin and Range strains at less than a few mm/yr.
  - The strain to geothermal link is stated as a "direct correlation" but only qualitatively.
  - https://gdr.openei.org/files/383/Faulds%20et%20al%202012%20GeoNZ%20Paper.pdf

### F2. Modern ML: "distance to fault" is a top feature, and geodetic dilatation adds little
- **Mordensky, Burns, Lipor and DeAngelo (2023), GRC Trans. 47, "Cursed?".**
  - **Heat flow and distance to nearest Quaternary fault were the two most important features in all three feature sets tested.**
  - **Shear strain rate** was of middling importance, similar to distance to magmatism.
  - **Dilatation strain rate** ranked as low as SHmax and seismic density, the two weakest 2008 features.
  - Adding the two strain features to the old 5-feature set gave no significant gain. Swapping them in for the two weakest features gave the best XGBoost result, but only at p = 0.06.
  - Median F1 was below 0.04. In tests, models recovered only about 2 to 4 of about 55 known positives at threshold.
  - Plain reading: a smooth regional raster that is correlated with existing layers adds little. The features that move models are local and sharp, like fault geometry and heat flow.
  - The paper did **not** test fault density, intersections or slip/dilation tendency. It names "fault intersection complexity" as future work. That gap is open.
  - https://par.nsf.gov/servlets/purl/10536404
- **The 2025 USGS Great Basin map with 16 features** captured 85% of producing systems in the top 10% of area (M02 F3). The jump from the 5-feature map came mostly from better labels and more layers, including FSS-type structure. The per-feature attribution in the 2025 paper was not in the abstract (unverified).
- **Smith et al. (2023), Bayesian neural network on the Nevada PFA** (L22 section 2.7) used "potential structures" and slip/dilation tendency among more than 12 features. https://pubs.usgs.gov/publication/70241433

### F3. How predictive is an FSS, in numbers (derived)
- **Area squeeze.** FSS cover about 7.7% of the Great Basin study area (Faulds et al. 2026, via M02). Suppose about 85 to 90% of known systems sit in FSS (Faulds & Hinz: ~88% in four geometries). Then the concentration is about 11x over random (calc: 0.88 / 0.077).
- **Hit rate per FSS.** About 1,300 FSS with no known system and about 240 to 360 undiscovered systems at 120 °C or hotter (M02 F2) give **about 0.2 to 0.25 per FSS** (unverified; it assumes undiscovered systems also sit in FSS).
- **What that means for spending.** To find one blind hot system from structure alone, we must screen about 4 to 5 FSS. At roughly $10k to $30k per FSS for a 2 m probe grid plus ranch-well chemistry plus an MT line (hardware memo ranges, unverified), screening costs **about $50k to $150k per discovery** (calc). The FSS list is long enough (about 1,300 unexplored) to feed a portfolio bank for years. This is not "too small".
- **Setting-type priors.** Displacement transfer zones (~4.8x) and pull-aparts (~2.2x) are enriched for hot systems (M02 table). Step-overs are common but slightly diluted. Use these numbers as the first prior weights.
- **Necessary, not sufficient.** Argenta Rise, the top INGENIOUS target, is a confirmed pull-apart. Several fault intersections there line up with low-resistivity zones and magnetic lows. Yet 139 two-metre points and ten TG wells gave no clear anomaly (Faulds et al. 2025, GRC 48; Jacinto et al. 2026). https://pubs.usgs.gov/publication/70271419

### F4. Why the current structural layers are biased and incomplete
- **Qfaults is uneven by state.** Mapping style, scale and completeness differ across state lines. This "creates bias between well-mapped and poorly mapped regions" (Hermant, Kiersnowski and Bellanger 2025, SGW). A model trained mostly in well-mapped Nevada will under-score Utah, Oregon or Idaho cells that simply have fewer mapped faults. https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=38029
- **Buried faults are missing by design.** Qfaults needs surface evidence. Faulds et al. (2026) say the FSS counts are minimums because of thin basin gravity and lake sediments that hide faults which have not ruptured in the Holocene (M02 F2). Gabbs Valley's productive structure was found from gravity and magnetics, not from mapped scarps (L22 section 2.3).
- **Slip and dilation tendency are upper bounds on regional stress.** The Ts/Td layers use a regional stress ratio and set dip to the value that maximises them (L22 section 2.5). SHmax rotates by up to 90° over tens of km at province edges (Lund Snee & Zoback 2020), and those edges are where clusters sit. Ts/Td computed on regional stress are therefore least reliable exactly where they matter most.
- **FSS mapping is manual.** The more than 1,430 FSS came from expert interpretation of 16 datasets by the UNR/USGS group across the Play Fairway and INGENIOUS projects (about 2014 to 2026). Outside the INGENIOUS footprint (central and southern Utah, Arizona, New Mexico's Rio Grande rift, Oregon's High Lava Plains, and rifts abroad), no comparable FSS inventory exists, as far as I found (unverified).
- **3D matters at the development step.** Siler et al. (2019, Geothermal Energy) and Siler & Pepin (2021) show that upflow sits where closely spaced, intersecting, critically stressed faults meet in 3D. A 2D FSS polygon cannot say which part of a 5 to 10 km step-over is open. https://pubs.usgs.gov/publication/70202167

### F5. Mapping structure at scale with ML: the pieces exist
- **Deep-learning fault detection from imagery.** TLS Geothermics trained CNNs to map Quaternary faults from remote sensing across the western US, regionally and at prospect scale with higher-resolution data (Hermant et al. 2025). No accuracy numbers were in the abstract (unverified). This makes fault maps consistent across state lines. https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Hermant.pdf
- **USGS NSHM 2023 earthquake-geology inputs and the western-US geologic deformation model** (Hatem et al. 2022, SRL; data DOI 10.5066/P9W63WOZ). These give consistent fault sections with slip rates for the whole western US. Slip rate is a direct "recent activity" feature, and recent slip keeps fractures from sealing. The section count and dip and rake fields were not shown on the landing page (unverified). https://www.usgs.gov/data/western-us-geologic-deformation-model-use-us-national-seismic-hazard-model-2023-version-10 ; https://www.usgs.gov/data/earthquake-geology-inputs-us-national-seismic-hazard-model-nshm-2023-version-10
- **Labels for an FSS detector.** The more than 1,430 Faulds FSS polygons, typed by setting, plus 403 known systems (GDR 1391 and the 2026 release; release status of the final FSS layer unverified). That is enough to train a geometry classifier, because the label is "is this fault geometry an FSS of type k", not "is it hot".
- **Inputs for buried faults.** Earth MRI magnetics and the 71,000-station gravity base (M09), 3DEP lidar for scarps (coverage percentage in Nevada unverified), NISAR L-band strain and creep (M10), and legacy seismic reflection lines (five were reprocessed at Reese River).

## Datasets

| Dataset | Access | Coverage | Value for blind detection |
|---|---|---|---|
| USGS Quaternary Fault and Fold Database | Free GIS download, usgs.gov/programs/earthquake-hazards/faults | US; uneven by state | Base fault traces, age and slip class. Biased across state lines; missing buried faults |
| NSHM 2023 earthquake-geology inputs and geologic deformation model (Hatem et al. 2022; DOI 10.5066/P9W63WOZ) | Free, ScienceBase | Western US | Consistent fault sections and slip rates across states. Recent-slip feature |
| Faulds FSS inventory (>1,430 settings, typed) | Earlier versions in GDR 1391; final 2026 layer release unverified | Great Basin (INGENIOUS area) | Training labels for an automated FSS detector; setting-type priors |
| INGENIOUS slip and dilation tendency, geodetic shear and dilation strain, seismic density (GDR 1391) | Free, CC-BY | Great Basin | Ready features. Ts/Td are regional-stress upper bounds |
| Faulds 2013 per-field Ts/Td (Patua, Tuscarora, McGinness Hills, Salt Wells, San Emidio, Neal) | Free, OSTI/GDR | Six fields | Positive examples of critically stressed fault geometry |
| UNR NGL / MAGNET GPS velocities and Kreemer strain models | Free, geodesy.unr.edu | Western US, ~10 to 30 km resolution | Regional transtension domain feature. Not prospect scale |
| Lund Snee & Zoback 2020 stress map and focal-mechanism catalogue | Free (paper supplements) | North America | Local SHmax rotations to redo Ts/Td |
| Coolbaugh 2002 WofE GIS and 2005 favorability map | Free, NBMG | Great Basin | Historical baseline. Contrast values give prior strength per layer |
| Earth MRI aeromagnetics; Nevada gravity base (M09) | Free, USGS | Large parts of NV and the Great Basin | Buried fault detection under basin fill |
| 3DEP lidar; NISAR L-band (public Jul 2026) | Free | Most of western US (coverage unverified) | Scarp mapping for CNNs; creep and strain on faults |
| Reese River / Argenta Rise structural package (gravity, mag, MT, 5 reprocessed seismic lines, 139 two-metre points) | Papers; data release unverified | One basin | Rare case of good structure with no shallow heat: a hard negative |

## What dominates uncertainty about blind resources (per this slice)
1. **Which FSS is open.** Structure narrows the search about 10x, but the per-FSS hit rate is only about 0.2 to 0.25. What makes one step-over hot and its neighbour cold is local stress, recent slip, mineral sealing and fluid supply. Regional layers do not resolve these.
2. **Missing buried structure.** FSS counts are minimums. The fraction of hot systems in FSS that are not yet mapped (under lake beds and alluvium) is unknown. It could be large, and it is also where land is cheapest.
3. **Local stress orientation.** Ts/Td use regional stress with 90° rotations possible over tens of km. Getting SHmax wrong flips which fault set is "open".
4. **Mapping bias across regions.** Uneven Qfaults by state, and an FSS inventory only inside the INGENIOUS footprint, mean the model cannot be trusted outside Nevada without re-mapping.
5. **Weak feature tests.** No published study has measured the separate lift from intersection density, FSS type or Ts/Td over "distance to fault". The ranking we rely on is partly expert opinion.

## What a sensor could fill
- **Buried-fault finder: passive-seismic HVSR nodes (new to the hardware pick).** A single 3-component seismometer left for 30 to 60 minutes gives the resonance frequency of the basin fill, and from that the depth to bedrock. A line of 20 to 50 stations across a valley shows steps in the bedrock, and those steps are buried faults. It needs no source, no cable and (likely) no permit under casual use. Unit cost is low if built on cheap geophones and a logger (hundreds to a few thousand dollars per node, unverified). It works on the same 2 m probe visit. It fills gravity's blind spot under lake beds, at a fraction of a rented gravimeter's cost (M09).
- **Drone magnetics on the same visit.** It maps magnetic lows from altered, demagnetised fault zones (Gabbs Valley, Reese River). Earth MRI gives the regional grid. A drone gives 50 m line spacing over one FSS.
- **Microseismic nodes for local stress.** Leave 10 to 20 cheap seismic nodes for 2 to 6 months over a high-ranked FSS. They record tiny earthquakes, and focal mechanisms give a local stress orientation. That fixes the biggest Ts/Td error, and quake locations light up active, open fault patches. The seismic nodes can share hardware with the E-field MT nodes (H03).
- **E-field MT across the structure (already picked).** Lay lines across the FSS axis and the intersection, not just over the score peak. Reese River showed conductors at fault intersections.
- **Soil-gas CO2, radon and helium along suspected fault traces (H04).** A cheap check of whether a buried fault leaks deep gas. It adds a fluid term on top of geometry.
- **Water-well drop probe (already picked).** Temperature-profile shape and chemistry decide whether a structurally good FSS carries heat (M02).

## Implications for a better model
1. **Make structure the area filter and prior, not the classifier.** Use FSS membership and type as a prior P(open permeable structure). Model heat and fluid presence as separate likelihood terms from our sensors. Then P(blind system) = P(structure open) × P(heat and fluid | structure) × P(detect | depth, hydrology).
2. **Build an automated FSS detector, and then run it everywhere.** Represent the fault network (Qfaults plus NSHM sections plus CNN-detected scarps plus buried faults from gravity, magnetics and HVSR) as a graph. Nodes are fault tips, intersections and bends. Edges are segments with strike, length, slip rate and Ts/Td. Train a graph neural network or a gradient-boosted model on local graph features, using the 1,430 Faulds FSS as labels. Validate by holding out whole basins. Then apply it to Utah, Oregon, Idaho, Arizona, New Mexico, the Salton and Imperial area, and abroad (Western Anatolia, the East African Rift, Andean arcs). This is the scale move. It gives us a target list that does not exist publicly outside the Great Basin.
3. **Replace "distance to fault" with sharp local features.** Use intersection density within 2 to 5 km, tip density, step-over overlap and width, the slip-rate gradient along strike (where slip dies out), Ts/Td recomputed on local stress, and fault age. Mordensky (2023) shows that the smooth features (dilatation strain, SHmax) add almost nothing, while local fault features are the strongest after heat flow.
4. **Keep geodetic strain only as a domain label.** Use it to split Walker Lane transtension from the low-strain east (Hammond 2007: normal component required; 30 km scale). Use it for sub-model selection, not as a per-pixel feature.
5. **Correct mapping bias explicitly.** Add a "mapping effort" covariate (state, map scale, lidar availability) so the model does not read "no mapped faults" as "no faults". Re-map faults with one consistent CNN pass across state lines.
6. **Treat Argenta-type sites as hard negatives for the heat term, not the structure term.** Good structure plus no heat should lower P(heat | structure) for similar FSS in that domain, without lowering the structure prior.
7. **Spend by value of information per FSS.** For each of about 1,300 unexplored FSS, the next measurement (HVSR line, drone mag, 2 m grid, ranch-well sample, MT line) should be the one that most cuts entropy on P(hot at 1 km). At about $50k to $150k per discovery from screening (F3, calc), structure-first triage across hundreds of FSS is affordable, and it locks cheap leases ahead of BLM auction competitors.
8. **The edge against Zanskar.** Zanskar's public story is heat flow and physics simulation (L22 section 3). A structure-first, buried-fault and local-stress layer, mapped by ML beyond Nevada and checked with our own HVSR, magnetic and seismic nodes, is a different and defensible data product. It also fits a portfolio bank that ranks many parcels rather than building a few plants.

## Sources
- https://data.nbmg.unr.edu/public/Geothermal/GreyLiterature/Coolbaugh_GeothermalGIS_NV_2002.pdf (Coolbaugh et al. 2002, weights of evidence)
- https://researchconnect.stonybrook.edu/en/publications/targeting-of-potential-geothermal-resources-in-the-great-basin-fr/ (Blewitt et al. 2002, GPS strain)
- https://geodesy.unr.edu/publications/HammondEtAl_GRC_07.pdf (Hammond et al. 2007, GPS block model)
- https://gdr.openei.org/files/383/Faulds%20et%20al%202012%20GeoNZ%20Paper.pdf (Faulds et al. 2012)
- https://par.nsf.gov/servlets/purl/10536404 (Mordensky et al. 2023, "Cursed?")
- https://pubs.usgs.gov/publication/70241433 (Smith et al. 2023)
- https://pubs.usgs.gov/publication/70271419 (Faulds et al. 2025, Reese River / Argenta Rise)
- https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=38029 ; https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Hermant.pdf (Hermant et al. 2025, CNN fault mapping)
- https://pubs.usgs.gov/publication/70202167 (Siler et al. 2019, 3D geologic mapping)
- https://www.usgs.gov/data/western-us-geologic-deformation-model-use-us-national-seismic-hazard-model-2023-version-10 (NSHM 2023 geologic deformation model)
- https://www.usgs.gov/data/earthquake-geology-inputs-us-national-seismic-hazard-model-nshm-2023-version-10 (NSHM 2023 earthquake geology inputs)
- https://www.usgs.gov/programs/earthquake-hazards/faults (Qfaults)
- https://geodesy.unr.edu/greatbasinstrain.php (UNR Great Basin strain / MAGNET)
- Cited through prior files: L22 (Faulds & Hinz 2015; Lund Snee & Zoback 2020; Siler & Pepin 2021; Faulds 2013 Ts/Td) and M02 (Faulds et al. 2026 FSS; Mordensky et al. 2025; Jacinto et al. 2026)
