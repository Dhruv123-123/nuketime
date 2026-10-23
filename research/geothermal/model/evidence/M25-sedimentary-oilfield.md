# M25: Sedimentary-basin hydrothermal and oil-field heat (Texas, Gulf Coast, Williston, DJ, Great Basin oil wells, California)

*Research note, 2026-10-23. Method: built on L10 (sedimentary literature), L11 (co-production), D01 (Texas RRC), D02 (KS/OK), D03 (Great Basin wells) and M04 (BHT corrections). It does not repeat their content. I ran 8 web searches and 5 fetches. Then the shared web-fetch budget ran out ("100 per hour, shared by every agent"), so I could not open the NREL Blackburn simulation report or the SwRI Nevada talk. Facts from those, and facts from memory, are marked (unverified).*

## Bottom line

The oil patch gives us two different things, and the model has to keep them apart. **(1) Permeable-aquifer heat (hot sedimentary aquifers).** Temperature here is smooth and conductive. It is predictable from heat flow, rock conductivity and sediment thickness, and it is now free to look up (USGS PetroMod basin models, InnerSpace GeoMap). The real unknown is **transmissivity (kh)**: how much water the rock will actually deliver. **(2) Fault-fed convective heat inside sedimentary basins.** Examples are the Wilcox growth-fault highs in South Texas, the Wattenberg wrench-fault high in the DJ Basin, and the Railroad Valley, Blackburn and Pine Valley oil fields in Nevada. These are true blind hydrothermal systems found by accident by oil drillers, and they are exactly our product. A better model should give each grid cell a latent "regime" variable (conductive aquifer, fault-fed plume, or masked/perturbed). It should use the oil patch's huge, cheap data (more than 400k BHTs, produced-water chemistry, wellhead flow temperatures, and saltwater-disposal injection records) both to learn the conductive background and to find the residual plumes. It should also flag **human-made heat and cold**: steamflood fields in California are artificially hot, and waterfloods in the Permian and Williston are artificially cold. If these go in unflagged, the training labels are poisoned. The highest-alpha new idea in this slice is to treat **saltwater-disposal (SWD) wells as free permeability tests**. Texas alone has about 28,760 active injection and disposal wells (D01). Their reported injection rates and pressures measure kh at a scale that no hydrothermal ML model (including Zanskar's GeoCore) uses. The cheapest sensor that fills the remaining gap is a **clamp-on flowline temperature-and-rate logger** for pumpjacks and SWD lines. It turns every producing well into a continuous reservoir thermometer.

## Findings

### F1. BHT density: where the oil-patch thermometer is thick and where it is thin
| Basin / region | Temperature data (approx.) | Source |
|---|---|---|
| Onshore US Gulf Coast | >6,000 corrected-BHT wells calibrating a 500,000 km2 PetroMod 3D model; >400,000 km2 at 90-150+ C above 6 km | Gardner & Birdwell 2023, https://pubs.usgs.gov/publication/70271309 (via L10) |
| South Texas Wilcox growth-fault belt | >1,600 Kehle-corrected BHTs; largest anomalies sit on the Wilcox growth fault zone | UT Austin thesis, https://tdl-ir.tdl.org/handle/2152/46322 |
| Texas statewide | >50,000 BHTs in a 2013 assessment; about 1.5M scanned logs at BEG; structured G-1 BHT and flow temperature only for e-filed gas completions since about 2011 | L10, D01 |
| Denver-Julesburg | >20,000 BHTs, 54-224 C corrected | Birdwell et al. 2024, https://www.searchanddiscovery.com/abstracts/pdf/2024/91208rms/abstracts/ndx_birdwell02.pdf (via L10) |
| Williston (ND) | Thousands of BHTs; 25 wells re-logged to static temperature by NDGS since 2014 | M04 |
| Kansas | 74,299 wells with BHT, 6,950 with multiple BHTs | D02 |
| Alberta / WCSB | >500,000 wells, mostly single unequilibrated BHTs | L10 |
| Nevada + western Utah oil wells | about 775 NDOM O&G wells plus 536 western-Utah wells (315 wildcats) | D03 |
| California | CalGEM holds a very large well archive (count unverified) with logs online through WellSTAR (unverified). Many San Joaquin gradients are low, about 25-35 C/km (unverified) | (unverified) |
| National | about 400k BHTs (Stanford), about 530k NGDS borehole temperatures | M04, L09 |

Plain reading: in sedimentary basins the BHT field is 10-100 times denser than in the Great Basin. That is good for learning the **bias model** and the **conductive background**. But most of these wells sit where the heat is conductive and has no convective plume. They make excellent "negatives" and background labels, and poor positives.

### F2. Fault-fed plumes inside sedimentary basins are real, and oil wells are how they get found
- **South Texas Wilcox growth faults.** Using 1,600+ corrected BHTs, the thesis finds the largest subsurface temperature highs along the Wilcox growth-fault zone. It argues that geopressure (heat trapped under low-conductivity shale) cannot explain them. A coupled heat-and-fluid model (Smith 1983) suggests the growth faults carry upward flow of deep basinal fluid, possibly from deeper than 20,000 ft (6.1 km). The thesis gives no anomaly size in degrees (https://tdl-ir.tdl.org/handle/2152/46322). Lamont work on the Gulf of Mexico shelf also shows raised sediment temperatures along growth faults (https://www.ldeo.columbia.edu/~guerin/Thesis/PDFs/Chapter4.pdf ; https://scisoc.confex.com/crops/2008am/webprogram/Paper49657.html).
- **DJ Basin Wattenberg.** A ~62 C/km gradient (>200 C at about 3 km) sits between the Lafayette and Longmont wrench faults, with a matching vitrinite-reflectance high. The Colorado Geological Survey called the same area not anomalous (L10). This is a fault-controlled high hidden in a sedimentary basin, and the conclusion flips with interpretation.
- **Great Basin oil fields are blind geothermal systems.** Bacon Flat-Grant Canyon in Railroad Valley holds 120-130 C fluid at about 1.6 km, with heat flow up to 234 mW/m2 against a 49-76 mW/m2 background. NBMG says it would not be known without petroleum drilling (M04 F5). These oil reservoirs sit in fractured Paleozoic carbonate and basin fill against range-front faults (reservoir description from memory, unverified).
- **They are now generating power.** Transitional Energy and ElectraTherm put an ORC on an active oil well in the Grant Canyon field. DOE GTO gave follow-on funding in May 2022 (https://enkiai.com/geothermal/electratherm-oilfield-geothermal-grant-canyon/; secondary aggregator). An April 2026 IOGCC presentation by Gradient Geothermal lists four projects:
  - Pine Valley, NV: DOE Wells of Opportunity, about 4,200 bbl/d at 195 F (91 C), targeting 1 MW, air-cooled.
  - Blackburn field, Eureka County, NV: first installation, April 2022.
  - Williston, ND.
  - Pierce, CO (DJ Basin).

  The deck gives the ORC sled range as 170-300 F with at least 2,000 bbl/d. It cites about 500,000 usable US wells out of about 2.9M (https://oklahoma.gov/content/dam/ok/en/iogcc/documents/committees-councils/cro/Geothermal%20Operations%20IOGCC%20260423.pdf; company-stated). NREL ran reservoir simulation for one Nevada field (NREL/TP 88526, https://nrel.gov/docs/fy24osti/88526.pdf). I could not open it, so its content is unverified.
- Lesson for the model: in the Great Basin, "oil field" and "blind hydrothermal system" overlap. Hydrothermal heat helps mature the oil, and the range-front fault both traps the oil and carries the hot water (mechanism plausible, unverified as a general rule). Every Great Basin oil field and oil show is a candidate positive label. Hot water cuts and high produced-water temperatures in NDOM production reports (the TempF columns, D03) are direct evidence.

### F3. Co-produced water temperature is a lower bound that the model can invert
- Wellhead or flowline temperature is always below reservoir temperature, because the fluid loses heat on the way up. The loss shrinks as flow rate grows (Ramey 1962 wellbore heat transmission, classic result; citation from memory). A high-rate water producer at 4,000+ bbl/d reads within a few degrees of the reservoir. A 50 bbl/d stripper well can read tens of degrees low (magnitude unverified).
- So a wellhead temperature must enter the model through a **forward wellbore model**: T_wellhead = f(T_reservoir, rate, depth, time on production, geothermal gradient). It must not go in as a raw temperature. Rate comes from production reports (RRC, NDIC, NDOM, CalGEM). This turns tens of thousands of producing wells into thermometers without any new logging.
- Structured sources: RRC G-1 `FLOW_TEMP` and `WELLHEAD_FLOW_TEMP` (gas wells, about 2011 onward, D01); NDOM monthly production and injection with fluid TempF (D03); USGS National Produced Waters Geochemical Database v3.0. That database holds produced and deep formation water samples from 1879-2022, including geothermal waters, under a CC0 licence (https://www.usgs.gov/data/us-geological-survey-national-produced-waters-geochemical-database-ver-30-december-2023 ; https://doi.org/10.5066/P9DSRCZJ). Sample count and temperature-field coverage are unverified; v2.3 had on the order of 10^5 samples (from memory, unverified).
- Water volumes (scale check): US oil and gas fields produce on the order of 20-25 billion bbl of water a year, with the Permian the largest (Veil 2020, from memory, unverified). Most of it is too cool, or it comes from too many small wells. NREL's realistic near-term co-production figure is about 300 MWe (L11). Co-production is a **data source and a beachhead, not the prize**.

### F4. Produced-water chemistry is a free geothermometer network
- The USGS produced-water database carries major ions and often silica (field availability per sample unverified). We can compute silica, Na-K-Ca and K-Mg geothermometer temperatures and compare them with the measured or modelled reservoir temperature at the sampled depth.
- In a purely conductive basin, brines equilibrate with the reservoir rock, so the geothermometer roughly equals the local temperature. That check costs nothing and validates the data.
- Where the geothermometer is well above the local reservoir temperature, the water likely came up a fault from a hotter source. That is the fault-fed plume signal (inference, standard in geothermal geochemistry; oilfield brines need Mg and salinity corrections, so treat it as a soft feature).
- This is the sedimentary analogue of the spring and well geochemistry in M07, with 10-100 times more sample points in the oil basins.

### F5. Permeability: the binding unknown for aquifer plays, and the oil patch already measures it
- Heat-in-place overstates deliverable power by about 7x (Alberta's Virginia Hills: 190 wells, only 53 above 100 kWe) to "orders of magnitude" (Williston co-production) (L10, L11). In aquifer plays the model must predict **kh**, not only temperature.
- Free kh evidence, ranked by quality:
  1. Saltwater-disposal and waterflood injection records. These give monthly volumes and wellhead pressures per injection well (Texas has about 28,760 active injection/disposal wells, D01). Their ratio is an injectivity index, which maps to kh after a skin and friction assumption. Several states publish this data in bulk (Texas H-10 and UIC data, Kansas and North Dakota Class II records; bulk-access details unverified).
  2. DSTs, with pressure build-up, flow rate and kh (Kansas DST database, D02; header DSTs elsewhere).
  3. Water cut and water rate per producing well (production reports).
  4. Core plugs and log-derived porosity. ML now predicts porosity well from logs: XGBoost test R2 0.86-0.98 on two North Dakota wells (Stanford Geothermal Workshop 2026, https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Gyimah.pdf). Porosity is only a weak proxy for kh.
- Diagenesis can wreck permeability exactly where heat is highest. An example is the Lyons Sandstone in the DJ Basin, altered by hydrothermal fluids (L10). So the model must not assume that hot means permeable in sedimentary rock. In fault-hosted systems the opposite often holds: hot means a recent fluid path.

### F6. Human-made thermal perturbations: a label-poisoning trap
- **Steamflood fields in California (thermal enhanced oil recovery).** Large Kern County heavy-oil fields such as Kern River and Midway-Sunset have been steam-injected for decades (field facts from memory, unverified). Their logs and produced water are artificially hot. If they go in unflagged, they become false positives. USGS has compiled produced-water chemistry for Lost Hills, Belridge, Poso Creek, Midway-Sunset and Buena Vista (https://www.usgs.gov/data/produced-water-chemistry-data-collected-poso-creek-midway-sunset-and-buena-vista-oil-fields ; https://data.amerigeoss.org/dataset/historical-produced-water-chemistry-data-compiled-for-the-lost-hills-and-north-and-south-b-05f8), which can help flag them.
- **Waterfloods and cold disposal (Permian, Williston, Midcontinent).** Decades of injecting surface-temperature water cool the reservoir around injectors, so later BHTs in these units read cold. This is a false-negative source in the very basins that supply most training labels (mechanism standard; size unverified).
- **Salt domes (Gulf Coast).** Salt conducts heat about 2-3 times better than shale (approximate, from memory). It pulls heat into the dome, which makes the sediments above it look hot and the zone below look cool, with no fluid flow involved. This is conductive refraction, not hydrothermal. The model must include salt geometry, or the dome tops will rank as plumes.
- **Geopressure.** Low-conductivity, overpressured shale raises the gradient conductively. The Wilcox thesis argues this is not the whole story (F2). The model should include it as a conductive term so that only the leftover residual counts as advective.

### F7. How the model should treat permeable aquifers vs fault-hosted systems (design)
1. **Latent regime per cell and depth**, with three states: C = conductive (possibly a hot aquifer), F = fault-fed convective plume, P = perturbed or masked (steamflood, waterflood, cold recharge, carbonate flow). Give the regime a prior from geology: growth-fault, wrench-fault and range-front-fault maps, salt maps, EOR project polygons, and carbonate-aquifer maps.
2. **Physics per regime.**
   - C: temperature from a 1D or 3D conductive model with lithology-dependent conductivity, as in USGS PetroMod and M16. Uncertainty is mostly in heat flow and conductivity.
   - F: the C background plus a sparse, heavy-tailed plume term (M04 F6), with plume geometry tied to fault traces and, in the Great Basin, to lateral outflow along permeable basin-fill or carbonate layers.
   - P: inflate the noise and cut the weight of shallow or cold readings.
3. **Diagnostics that separate C from F.** These are features, and each one can come from free data:
   - Profile curvature and Peclet number from multi-depth BHTs or logs (Bredehoeft & Papadopulos 1965 type-curve method, from memory). A concave profile means upflow; convex means downflow.
   - Inverted or isothermal sections in a single well.
   - The gap between the geothermometer and the local reservoir temperature (F4).
   - Residuals from the conductive model that cluster along faults, not along lithology.
   - Vitrinite-reflectance highs that do not fit burial history (Wattenberg).
4. **Two separate value heads.** For C cells, sell "MW = T x kh x area", with kh from the SWD, DST and water-rate likelihoods (F5). For F cells, sell "P(plume) x plume size", as in the Great Basin model. Mixing them into one favourability score (as INGENIOUS and GeoCore style maps do) blends two kinds of value that cannot be compared.
5. **Transfer learning.** Learn the BHT bias model and the conductive background in data-rich sedimentary basins (Kansas, Texas, the DJ, the Williston, Alberta). Then carry the learned bias, not the background, to the Great Basin. Treat oil fields in the Great Basin as high-prior F cells.
6. **Wellhead temperatures enter through a forward wellbore heat-loss model** (F3), with rate and time on production as inputs. They then count as constraints on reservoir temperature with honest error bars.
7. **Anthropogenic masks are hard inputs.** Steamflood and waterflood unit polygons, injection volumes, and spud dates relative to flood start all go into the model. A BHT logged after a flood began gets a cold-bias term.

## Datasets
| Name | Access | Coverage | Value for blind detection |
|---|---|---|---|
| USGS National Produced Waters Geochemical Database v3.0 | Free, CC0, https://doi.org/10.5066/P9DSRCZJ | US produced, deep formation and geothermal waters, 1879-2022 | Geothermometers vs local temperature to flag fault-fed upflow; salinity for brine correction |
| USGS California oilfield produced-water sets (Lost Hills, Belridge, Poso Creek, Midway-Sunset, Buena Vista, Edison) | Free, ScienceBase | San Joaquin Valley | Flags steamflood-heated fluids; California negatives and controls |
| Texas RRC G-1 completion feed | Free nightly ASCII | Texas gas wells, about 2011 onward | Structured BHT, shut-in temperature, flow temperature, wellhead flow temperature |
| Texas RRC injection / UIC (H-10) records | Free online; bulk extract unverified | About 28,760 active injection and disposal wells | Injectivity, which gives kh at basin scale (new to geothermal ML) |
| NDOM production and injection tables (TempF) | Free Excel | Nevada geothermal and oil | Direct fluid temperatures in Great Basin oil and geothermal fields |
| NDIC / NDGS well files and static temperature logs | Free, partly paid subscription (unverified) | Williston | Static-vs-BHT pairs; water rates |
| Kansas KGS DST and BHT files | Free bulk | Kansas | Bias-model training; kh from DSTs |
| USGS Gulf Coast PetroMod model and Burke et al. 2018 BHT corrections | Free (USGS) | Onshore Gulf Coast | Conductive background to subtract; 12 province-specific corrections |
| South Texas growth-fault BHT study (1,600+ BHTs) | Thesis, free | Wilcox trend | Labelled fault-fed anomaly belt for training plume detection |
| USGS DJ Basin 3D model (>20,000 BHTs) | Abstract; data on request (unverified) | Denver-Julesburg | Wattenberg fault-controlled high; diagenesis caution |
| CalGEM WellSTAR well records and logs | Free online (bulk unverified) | California | Logs, injection (steamflood) volumes for masks |
| InnerSpace GeoMap | Free web tool | North America, isotherm depths | Commoditised baseline to beat; not a moat |
| GDR 1223 eastern Nevada / Millard County sedimentary well database | Free | Railroad Valley, Elko, Steptoe, Millard | Uncorrected temperatures, pressures and permeability in basins with known blind heat |

## What dominates uncertainty (this slice)
1. **Transmissivity (kh) for aquifer plays.** Heat is known to within about +/-10-20 C. Deliverable MW is uncertain by about 7x or more, because flow varies so much from well to well.
2. **Regime misclassification.** Salt refraction, geopressure, steamflood heat or a single junk BHT can look like a fault-fed plume. Waterflood cooling or cold aquifer recharge can hide a real one.
3. **Wellhead temperature to reservoir temperature conversion.** This depends on rate and time on production. The data exists, but nobody has joined it at scale.
4. **Anthropogenic history.** Flood start dates and injection volumes are on file but scattered. Without them, many BHTs have an unknown sign of bias.
5. **Deep extrapolation below 4 km.** Correction methods are not established there, and few wells reach that depth. This matters for EGS on the same acreage, less for hydrothermal.
6. **Data access cost and format.** Header BHTs are trapped in TIFFs (Texas, California, Nevada). The same is true for injection pressures in some states.

## What a sensor could fill
- **Clamp-on flowline logger** ("oilfield heat tap"): a strap-on RTD plus clamp-on ultrasonic flow meter, with a solar and cellular logger, on pumpjack flowlines, SWD inlet lines and water-transfer lines. It needs no wellbore entry and no permit, only operator consent. It gives continuous temperature and rate, which a wellbore heat-loss model inverts to reservoir temperature, and it also records water rate, a kh proxy. Each unit costs a few hundred dollars (unverified estimate). One technician could fit 50-100 wells a week. This is new compared with M04's downhole tools, and it covers producing wells that cannot be entered.
- **SWD falloff pressure logger**: a high-resolution wellhead pressure gauge left on a disposal well across a planned shutdown. A falloff test gives kh and skin directly. This is a cheap, permit-free (operator consent) permeability measurement in the formations that would host doublets.
- **Produced-water field kit**: field silica, Na, K and Mg tests plus a sample bottle program. It fills gaps in the USGS database at the exact wells we care about, for geothermometer-vs-temperature screening (F4).
- **Reuse of prior picks**: the drop probe and memory gauge (M04) for idle or temporarily abandoned wells, and 2 m probes and E-field MT nodes for Great Basin oil fields, where range-front plumes reach the basin fill.
- **Software sensor**: vision OCR of log headers and H-10 or UIC scans for BHT, shut-in time, injection rate and pressure.

## Implications for a better model
1. Add an explicit regime layer (C / F / P) with separate physics and separate value outputs. Do not let one favourability score mix aquifer MW with plume probability.
2. Treat every Great Basin oil field, hot oil show and high-temperature water cut as a high-prior plume label. Oil drillers have already found blind systems there (Railroad Valley, Blackburn, Pine Valley).
3. Use dense sedimentary basins to learn the BHT bias model and the conductive physics, then transfer the bias to the West (M04). Sedimentary wells are the best source of negatives and background labels.
4. Bring in permeability likelihoods that hydrothermal ML ignores: SWD injectivity, DST kh and water rates. This is the main data moat compared with Zanskar's GeoCore and INGENIOUS layers, which carry no kh term.
5. Model wellhead and produced-water temperatures through a forward wellbore model, and produced-water chemistry as geothermometer residuals. Both are free, dense and underused.
6. Hard-mask human-made heat and cold (steamflood, waterflood, disposal) and natural conductive tricks (salt, geopressure) before searching residuals for plumes.
7. Fault-fed plumes in sedimentary basins (South Texas Wilcox growth faults, DJ Wattenberg wrench faults, Great Basin range fronts) are a second blind-hydrothermal hunting ground with cheap tenure: Texas and Colorado treat the heat as a surface right, and Nevada and Utah private land is ranch-owned (D03, Gradient IOGCC deck). They deserve their own target list.
8. Scope check against "too small" kills: single co-production units are 0.1-1 MW, and these should be treated as a data and beachhead play only. Doublet aquifer projects are 5-30 MW (L10). Fault-fed plumes and portfolios are the sizes that matter, so rank by those.

## Sources
- https://pubs.usgs.gov/publication/70271309
- https://tdl-ir.tdl.org/handle/2152/46322
- https://www.ldeo.columbia.edu/~guerin/Thesis/PDFs/Chapter4.pdf
- https://scisoc.confex.com/crops/2008am/webprogram/Paper49657.html
- https://www.searchanddiscovery.com/abstracts/pdf/2024/91208rms/abstracts/ndx_birdwell02.pdf
- https://www.usgs.gov/data/us-geological-survey-national-produced-waters-geochemical-database-ver-30-december-2023
- https://sciencebase.gov/catalog/item/64fa1e71d34ed30c2054ea11
- https://www.usgs.gov/data/produced-water-chemistry-data-collected-poso-creek-midway-sunset-and-buena-vista-oil-fields
- https://data.amerigeoss.org/dataset/historical-produced-water-chemistry-data-compiled-for-the-lost-hills-and-north-and-south-b-05f8
- https://oklahoma.gov/content/dam/ok/en/iogcc/documents/committees-councils/cro/Geothermal%20Operations%20IOGCC%20260423.pdf
- https://enkiai.com/geothermal/electratherm-oilfield-geothermal-grant-canyon/
- https://nrel.gov/docs/fy24osti/88526.pdf (not opened; budget)
- https://www.energy.gov/node/4816607 (DOE Wells of Opportunity)
- https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Gyimah.pdf
- Prior repo files: L10, L11, D01, D02, D03, M04, M07, M16
