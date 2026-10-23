# M02: INGENIOUS as a model baseline. What it measured, what it got right, where it failed, and what a better model needs.

Date: 23 Oct 2026. This file builds on `../../evidence/L04-ingenious.md` (project facts, permits, sites), `L03-ml-geothermal.md` (ML papers), `L22-structural-ml.md` (structure layers) and `Z03-data-methods.md` (Zanskar GeoCore). It does not repeat their project history. It looks at INGENIOUS as the **public baseline model a new heat-rights bank has to beat**. Web budget: 8 searches and 5 fetches worked. The GDR 1391 page and the two 2026 Stanford PDFs (Faulds, Jacinto) were blocked for direct fetch, so the 2026 numbers below come from the Stanford abstract pages, which loaded.

## Bottom line

INGENIOUS ($10M, DOE/UNR, 2021 to about 2026) built the best public prospectivity stack in any geothermal province: 16 regional layers, more than 1,430 mapped favorable structural settings (FSS) covering about 7.7% of the Great Basin, 403 known systems as labels, about 3,869 well heat-flow residuals as a continuous "hidden convection" target, and a USGS favorability map with 1,200 Monte Carlo realizations. At the regional scale it works well. The top 10% of map area holds 85% of producing systems, and hidden systems are found about as well as exposed ones (5 of 9 in the top 1%). At the prospect scale it is weak. Its highest-scoring target, Argenta Rise, gave **no clear thermal anomaly in 139 two-metre probe points or in ten temperature-gradient wells to about 244 m**, even though structure and MT looked right. The model predicts where permeable structure is. It does not predict whether hot water reaches the depth we can afford to measure. The main failure modes are a cool aquifer masking the heat, an upflow outside the array, and a reservoir too deep to see. A better model therefore needs three things INGENIOUS lacks: (1) a hydrology term for masking and outflow, (2) cheap measurements that see through the top 250 m (chemistry, temperature-profile shape, conductors at 0.5 to 2 km), and (3) honest negative labels from cold holes. These are exactly the gaps our own sensors can fill. The regional map is free and everyone uses it. The edge is the local posterior.

## Findings

### F1. The data stack (what is in it)
- **GDR submission 1391, "INGENIOUS - Great Basin Regional Dataset Compilation"** (CC-BY-4.0, DOI 10.15121/1881483, released 30 Jun 2022, modified Mar 2025). It covers NV, western UT, southern ID, SE OR and eastern CA. Layers: 2-m temperatures, Quaternary faults and volcanics, geodetic shear and dilation strain, heat flow, MT conductance, gravity and magnetics, paleo-geothermal deposits (sinter and tufa), seismicity density, spring and well temperatures and chemistry, thermal conductivity, and slip and dilation tendency. https://gdr.openei.org/submissions/1391 ; https://catalog.data.gov/dataset/ingenious-great-basin-regional-dataset-compilation
- **Labels.** Wells carry a "residual" attribute, which is measured heat flow minus a modelled conductive background. Mordensky et al. (2023) used **3,869** of these "convective signals", ranging from -91 to 11,105 mW/m² (see L03 section 1.7). https://par.nsf.gov/servlets/purl/10536406
- **Final structural layer (Faulds et al. 2026, Stanford SGW 51).** 16 regional datasets give **more than 1,430 FSS covering about 7.7% of the study area**. There are **403 known systems at 37 °C or hotter** and **120 training sites at 120 °C or hotter**. https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=38284
- **Older USGS western-US favorability rasters** (Mordensky et al. 2023, Geothermics 102662) used only five features: heat flow, distance to Quaternary fault, distance to Quaternary magma, seismic density and max horizontal stress. https://christopher-catalog-dev.app.cloud.gov/dataset/geothermal-resource-favorability-select-features-and-predictions-for-the-western-united-st

### F2. Which structural settings host hot systems (new numbers worth using as priors)
Faulds et al. (2026) give the share of each FSS type among all FSS, among the 403 known systems and among the 120 training sites at 120 °C or hotter. Dividing the training-site share by the FSS share gives a rough "enrichment" (my calculation; small counts):

| FSS type | Share of all FSS | Share of 403 known | Share of 120 hot (≥120 °C) | Enrichment (hot / all FSS) |
|---|---|---|---|---|
| Step-over | ~40% | ~27.5% | 34.2% | 0.86 |
| Fault intersection | 26.1% | 22.1% | 26.7% | 1.02 |
| Fault termination | 16.7% | 16.6% | 14.2% | 0.85 |
| Accommodation zone | 6.8% | 5.7% | 5.8% | 0.85 |
| Pull-apart | 2.3% | 2.7% | 5.0% (~6 sites) | **2.2** |
| Displacement transfer zone | 1.4% | 3.2% | 6.7% (~8 sites) | **4.8** |

- Plain reading: displacement transfer zones and pull-aparts are rare but punch far above their weight for hot systems. Step-overs are the most common setting, but per setting they are slightly less likely to host a hot system. Step-overs may also simply be under-explored, so this is a hypothesis.
- Faulds et al. say the counts are **minimums**. Basin gravity coverage is thin, and late Pleistocene lake sediments hide faults that have not ruptured in the Holocene. So the most prospective unmapped FSS lie under valley floors, which is also where the land is cheapest and the least explored.
- **Rough base rate (derived, assumption-heavy).** Suppose about one in four systems is already known (the assumption used in the NVML re-fit, L03). Then there are about 360 to 480 systems at 120 °C or hotter in total, so about 240 to 360 remain undiscovered. Spread over the roughly 1,300 FSS that do not yet host a known system, that is a prior of about 0.2 to 0.25 per FSS (unverified; it assumes systems sit in FSS). This is a large target list, not a small one.

### F3. Regional detection rates (what it got right)
- **USGS Great Basin favorability for the new national assessment** (Mordensky, Burns, Lipor and DeAngelo 2025, Geothermics 133:103450). It uses 16 features, a "much larger" training set and ordinal convective-strength labels, with 1,200 Monte Carlo cross-validation realizations published as P05 to P95 GeoTIFFs.
  - **85% of power-producing systems fall in the top 10% of area.**
  - **15 of 28 fall in the top 1%: 10 of 19 exposed and 5 of 9 hidden.**
  - 26 of 28 fall above the 80th percentile, against about half for earlier maps.
  - The map ranks systems with more convective heat flow higher.
  - https://pdxscholar.library.pdx.edu/ece_fac/862 ; https://pubs.usgs.gov/publication/70270953 ; data https://www.usgs.gov/data/geothermal-resource-favorability-select-features-and-predictions-united-states-great-basin (DOI 10.5066/P14EET2C)
- **Hidden systems are found about as well as exposed ones.** This is the most important "right" result for us. It means the regional prior is not just a hot-spring detector.
- **MW, not just favorability.** Trainor-Guitton et al. (2025, SGW 50) ran XGBoost regression on 37 nameplate capacities, 248 zero-MW sites and 48 features. Negatives were subsampled by geologic domain. P50 and P90 predictions feed NREL reV. The capacity and LCOE distributions came out "much narrower and lower" than temperature-only estimates. The abstract gives no total GW (unverified). https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=38132 ; https://research-hub.nrel.gov/en/publications/quantile-model-regression-of-nameplate-capacities-p50-and-p90-meg/
- **Value-of-information drilling.** At Granite Springs Valley, Trainor-Guitton, Siler and Ayling (2023) used temperatures as primary data and structural proxies as secondary data in geostatistics. They mapped P(economic T) and entropy to choose holes (L22 section 2.11). https://www.osti.gov/biblio/2217601
- **The predecessor's hits.** The Nevada Play Fairway found Granite Springs Valley (about 96 °C at about 240 m) and Gabbs Valley (L04 S1). So the method can find blind heat at TG depth.

### F4. Prospect-scale results (where it went wrong or stayed unresolved)
- **Argenta Rise (NV), the top predicted target.** Jacinto, Faulds, Earney, Glen, Hart-Wagoner, Lindsey and Peacock (2026, SGW 51):
  - Inputs were mapping, gravity, magnetics, MT, seismic reflection, a 2-m survey and **ten TG wells to about 244 m**.
  - Structure was confirmed: a pull-apart between the Argenta Rim and northern Shoshone Range faults.
  - MT shows **low-resistivity zones at about 1.5 km**, some aligned with faults.
  - **No clear thermal anomaly** showed up in either the 2-m survey or the TG wells.
  - The authors' reading: "structural and geophysical indicators can be decoupled from shallow temperature signatures". The resource may sit outside the array, under a cool aquifer, or deeper.
  - The earlier paper (Faulds et al. 2024) had already reported 139 two-metre points with no definitive anomaly. So the cheap screen gave the right "no shallow heat" answer before drilling, but it was overruled by the structural prior.
  - https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=38309 ; https://publications.mygeoenergynow.org/grc/1035050.pdf
- **Lund North (UT), eastern Great Basin.** It was picked from the preliminary favorability map and a legacy TG hole above 220 mW/m². New data cover gravity, MT, TEM, fluid chemistry, UAV lidar, paleomagnetism, aeromagnetics and a shallow temperature survey. These suggest a large east-dipping normal fault with a step-over geometry. TG drilling (up to 10 holes to about 800 ft) was authorized in Aug 2026. Results are not public yet. https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=38028
- **Buffalo Valley / Jersey Summit (NV).** Permitted (CX-031443, up to 10 holes). I found no public results. The only hits were 1976 USGS test-well data (Sass et al., OFR 76-85). https://pubs.usgs.gov/publication/ofr7685
- **Granite Springs Valley (NV).** Six more TG wells to 1,500 ft were permitted in May 2026. No new results found.
- **Score so far:** 1 of 4 detailed sites is a confirmed shallow anomaly (Granite Springs, inherited from the earlier Play Fairway), 1 is dry at TG depth (Argenta), and 2 are pending. That is too few sites to compute a prospect-scale hit rate. The one clean test of "top score leads to anomaly" failed.

### F5. Known weaknesses the authors themselves name
- Eastern Nevada and Utah (carbonate aquifer, older faults, low strain) "may not be fully accounted for" (Faulds and Richards 2023, L04 S4).
- East-west bias from elevation and strain-rate features. Smooth, interpolated inputs limit fidelity (NVML re-fit, L03).
- Magnitude is under-predicted because inputs are coarse compared with upflow zones a few km wide (Mordensky 2023).
- The FSS layer misses buried basin faults (Faulds 2026).
- Labels have survey bias. Heat-flow residuals exist only where someone drilled, mostly near known fields and mines.
- No slimholes were drilled (Task 5 removed), and TG holes are capped at 1,000 to 1,500 ft. So there is no ground truth for the 500 to 1,500 m depth where reservoirs like Big Blind (about 823 m) sit.
- I found no public final favorability map or developers' playbook.

## Datasets

| Dataset | Access | Coverage | Value for blind detection |
|---|---|---|---|
| INGENIOUS Great Basin Regional Compilation (GDR 1391) | Free, CC-BY, gdr.openei.org/submissions/1391 | NV, W UT, S ID, SE OR, E CA | Feature stack and heat-flow-residual labels. The baseline everyone, including Zanskar GeoCore, starts from |
| USGS Great Basin favorability P05-P95 (DOI 10.5066/P14EET2C) | Free, USGS ScienceBase | INGENIOUS area | A ready-made prior with uncertainty. Use it as a feature or prior, not as a target list |
| USGS western-US favorability (2023, 5 features) | Free | Western US | A coarse prior outside the Great Basin (OR, ID, NM, AZ) |
| Faulds et al. 2026 FSS layer (>1,430 settings) | Release status unverified. Earlier versions are in GDR 1391 | Great Basin | Permeability prior by setting type (DTZ and pull-apart enriched) |
| Argenta Rise 2-m (139 pts), 10 TG wells, MT, seismic | Partly in GRC and SGW papers. GDR release unverified | One basin | **Rare high-quality negative labels.** Also a test case for masking models |
| Granite Springs 3D Leapfrog and stochastic T model | Papers. Data on GDR partly from Play Fairway | ~280 km² to 6 km | A worked VOI example; a template for the local posterior |
| Lund North gravity, MT, TEM, chemistry, lidar | Utah Geological Survey and USGS (release unverified) | One basin, eastern GB | A test of the under-modelled eastern domain |
| Trainor-Guitton MW quantile model plus reV | NREL (data release unverified) | INGENIOUS area | Turns favorability into MW and LCOE, which a buyer can price |
| 1976 USGS Grass and Buffalo Valley test wells (OFR 76-85) | Free PDF | Two valleys | Old labels near a pending INGENIOUS site |

## What dominates uncertainty about blind resources (per this slice)
1. **Masking and lateral flow in the top 250 m.** Cool groundwater can hide a hot upflow from 2-m probes and 244 m TG holes (Argenta). This is the single largest gap between "favorable" and "found".
2. **Depth to the reservoir.** There is no public ground truth between about 300 m and 1,500 m. Conductive extrapolation from a shallow gradient is wide open when flow is present.
3. **Permeability at the specific fault.** FSS give a regional permeability prior, but which step-over or intersection is actually open is unknown. That is set by local stress, recent slip and mineral sealing.
4. **Label scarcity and bias.** 120 hot training sites, few confirmed negatives, and wells clustered where people already looked. PU-learning effects are large.
5. **Domain shift.** The eastern Great Basin carbonate terrain and areas outside the Great Basin are poorly represented in training.
6. **Input resolution.** Regional rasters are km-scale smooth, while upflow zones are about 1 to 3 km wide.

## What a sensor could fill
- **See through the cool aquifer: groundwater chemistry and isotopes.** Geothermometers (silica, Na-K-Ca), boron, lithium, chloride and **helium isotopes (3He/4He)** in ranch and stock wells can carry a deep-fluid signal even when temperature is masked. This plugs straight into the ranch drop-probe plan as a sampling add-on. Argenta-type sites are the test.
- **Temperature-profile shape, not just gradient.** A logging probe in existing water wells can resolve convex or concave temperature-depth curves. Those curves reveal lateral or vertical groundwater flow (a Bredehoeft-Papadopulos / Peclet-number fit). That tells us whether a "cold" hole is cold or just being flushed. It is a cheap upgrade to the drop probe's firmware and analysis.
- **Conductors at 0.5 to 2 km.** Argenta showed low-resistivity zones at about 1.5 km. E-field-only MT nodes, densely deployed, can map the clay cap or brine at reservoir depth, below the masking aquifer. This is already in the hardware pick. The new point is to place the arrays across the FSS and down hydraulic gradient, not just over the score peak.
- **Buried faults under valley floors.** Faulds 2026 says basin gravity coverage limits FSS mapping. A cheap, dense ground-gravity and magnetic traverse kit (or a rented relative gravimeter on a drone or ATV workflow) could map hidden step-overs and transfer zones in lake-covered basins. That is new target inventory no public map holds. The cost of a modern relative gravimeter is unverified, but it is likely well above $50k, so rent it before building one.
- **Hydraulic head and flow direction.** Water-level loggers in ranch wells give the groundwater gradient, so an outflow plume found down-valley can be traced back to its upflow.
- **Long-dwell temperature in our own shallow holes.** Months of logging at several depths remove seasonal noise and detect small advective anomalies that a one-off reading misses.
- **Deeper cheap holes (500 to 900 m).** INGENIOUS stopped at 1,000 to 1,500 ft. Our own light rig or a partner's rig sized for 500 m or more is the step that converts "unresolved" into "anomaly" (see hardware H11).

## Implications for a better model
1. **Use INGENIOUS and USGS as the prior, not the model.** Take the P50 favorability, its P05 to P95 spread, the FSS type and the 16 layers as input features or as a Bayesian prior. Everyone has these, Zanskar included (GeoCore runs LightGBM on the same stack), so they give no edge alone.
2. **Model two quantities, not one.** Separate (a) P(a hot permeable upflow exists in this FSS) from (b) P(it shows up in what we measure at depth d, given hydrology). Argenta was high on (a) and low on (b). A single favorability score mixes them, and that causes false "dry" calls and wasted holes.
3. **Add a hydrology and masking layer.** Use depth to water, recharge, hydraulic gradient, carbonate aquifer extent and basin-fill thickness from gravity. Train it on wells where temperature-profile curvature shows flow. This turns "cold at 244 m" from a negative into "masked, look deeper or down-gradient".
4. **Use continuous convective-residual targets plus graded negatives.** Regress the heat-flow residual (as USGS does) and add Argenta's ten TG wells and similar cold holes as *depth-tagged* negatives ("not hot above 244 m"), not as "no system". Use positive-unlabelled learning and score by area-capture curves (share of systems in top X% of area), not by F1.
5. **Use setting-type priors.** Weight displacement transfer zones (about 4.8x) and pull-aparts (about 2.2x) above step-overs, and refresh the weights as new hot sites come in. Then hunt buried FSS under lake-covered basins with our own gravity.
6. **Train domain-specific sub-models.** Walker Lane, the extensional western Great Basin, the low-strain carbonate east and the volcanic fields each need their own weights (the PCA and k-means clusters in L22).
7. **Close the loop with value of information.** For each leased or optioned parcel, pick the next measurement (chemistry sample, MT line, 2-m grid or 500 m hole) that most reduces entropy on P(economic T at 1 km). Granite Springs shows this works. It is also how we spend lease money only where the posterior moves.
8. **Count it as a race on the free map.** The top 1% of the USGS map is a public shopping list. Our parcels should come from where our private data (ranch-well chemistry and profiles, gravity under lake beds, MT conductors) lifts a cell from the 80th to 95th percentile into a confident target that public models still rank lower.

## Sources
- https://gdr.openei.org/submissions/1391 (blocked for fetch this session; contents via L04 and data.gov) ; https://catalog.data.gov/dataset/ingenious-great-basin-regional-dataset-compilation
- https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=38284 (Faulds et al. 2026, FSS)
- https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=38309 (Jacinto et al. 2026, Argenta Rise)
- https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=38028 (Hardwick et al. 2025, Lund North)
- https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=38132 (Trainor-Guitton et al. 2025, MW quantile)
- https://pdxscholar.library.pdx.edu/ece_fac/862 ; https://pubs.usgs.gov/publication/70270953 (Mordensky et al. 2025)
- https://www.usgs.gov/data/geothermal-resource-favorability-select-features-and-predictions-united-states-great-basin
- https://christopher-catalog-dev.app.cloud.gov/dataset/geothermal-resource-favorability-select-features-and-predictions-for-the-western-united-st
- https://par.nsf.gov/servlets/purl/10536406 (Mordensky et al. 2023, residual labels)
- https://publications.mygeoenergynow.org/grc/1035050.pdf (Faulds et al. 2024, Argenta 2-m)
- https://www.osti.gov/biblio/2217601 (Trainor-Guitton, Siler and Ayling 2023, VOI)
- https://pubs.usgs.gov/publication/ofr7685 (1976 Grass and Buffalo Valley test wells)
- Blocked this session (not read in full): https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Faulds.pdf ; https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Jacinto.pdf
