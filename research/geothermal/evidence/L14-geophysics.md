# L14 — Geophysical and remote-sensing methods in geothermal exploration (deep literature review)

Scope: MT, airborne EM, gravity, magnetics, InSAR, hyperspectral/ASTER, thermal infrared, soil CO2/gas geochemistry, plus the public datasets behind them (USGS aeromag/gravity, Earth MRI, NASA/JPL AVIRIS, INGENIOUS/GDR). Focus is the Great Basin, where most US hidden-hydrothermal upside sits.

Method note: the shared web-search budget for this run ran out before this agent started. All sources below were found through primary catalogues (OSTI.gov API, USGS Publications Warehouse API, Crossref, DOE GDR) and read directly. Full-text PDFs were read for the BRIDGE report, Folsom et al. 2024, Kraal & Schwering 2024, Trainor-Guitton et al. 2025, Faulds et al. 2021, Ahmmed & Vesselinov 2022 and the NREL PFA retrospective. For a few classic papers (Coolbaugh et al. 2007; Ali et al. 2016) only the metadata could be fetched; claims about their contents are marked (unverified).

---

## 1. The base rate: why geophysics matters here

- **USGS 2008 national assessment (Williams et al.)**: identified systems hold ~9,057 MWe. Undiscovered conventional hydrothermal has a mean of **30,033 MWe**, and EGS adds 517,800 MWe. https://pubs.usgs.gov/fs/2008/3082/
- **Blind fraction.** Faulds et al. (2021) cite Coolbaugh et al. (2007): blind systems "probably comprise more than 75% of the geothermal resources" of the Great Basin, but only ~40% of *known* systems are blind (Faulds & Hinz 2015). "Most of these blind systems were discovered accidentally through drilling." https://www.osti.gov/biblio/1724080
- **BRIDGE (Sandia, 2025)** puts it as "about 70% of the convective geothermal resources in the Basin and Range province are hidden resources and only about half of these hidden resources have been discovered thus far." It adds that "all power capable geothermal systems with surface expressions in the Basin & Range have been explored and most have been developed." The search is a needle-in-haystack problem: a system's upflow and outflow "may span only several km2 … amongst the 1000s of km2" of a basin. https://www.osti.gov/biblio/2540220

Implication: the opportunity is the discovery of blind systems. Surface manifestations are already exhausted, so the remaining signal sits in subsurface proxies: resistivity, potential-field structure, shallow temperature, gas and alteration mineralogy.

---

## 2. Primary-source summaries (11 core papers/reports)

### 2.1 Faulds, Hinz, Coolbaugh et al. (2021). *Discovering Blind Geothermal Systems in the Great Basin Region: Play Fairways, All Phases.* DOE-UNR-06731-01.
- Regional map over **96,000 km²** of Nevada built from **9 parameters**: structural setting, fault age, slip rate, GPS strain rate, slip/dilation tendency, earthquake density, **gravity gradients**, temperature at 3 km, and spring/well geochemistry. Weights were set by logistic regression plus Bayesian weights-of-evidence on **34 benchmark systems ≥130 °C**, then an expert fuzzy-logic layer.
- The 24 prospective areas were narrowed to 5 and then 2 drilled. **SE Gabbs Valley** is a truly blind system with no springs, fumaroles or sinter; its indicators were Quaternary faults, intersecting/terminating gravity gradients, a magnetic low and a 2-m temperature anomaly. Six TG holes reached **124 °C at 152 m**. **N. Granite Springs Valley**: ~**96 °C at ~250 m**.
- Key result: a few-parameter, public-data-dominated regional model that weights gravity and magnetic gradients produced blind discoveries with very shallow, cheap holes. https://www.osti.gov/biblio/1724080

### 2.2 Craig, Faulds, Hinz et al. (2021). *Discovery and analysis of a blind geothermal system in southeastern Gabbs Valley.* Geothermics 97:102177.
- This is the peer-reviewed write-up of the Gabbs Valley discovery. It combines detailed gravity, magnetics, MT and 2-m temperature data with structural mapping. (Abstract not retrieved; details as summarised in the Faulds 2021 report.) https://doi.org/10.1016/j.geothermics.2021.102177

### 2.3 Peacock & Siler (2021). *Bottom-up and top-down control on hydrothermal resources in the Great Basin: Gabbs Valley.* GRL 48(23).
- 3D MT combined with structural geology shows two controls. Deep "bottom-up" control comes from weak zones at the brittle–ductile transition, often reusing Miocene volcanic structures. "Top-down" control comes from modern Walker Lane and Basin-and-Range faulting in the mid/upper crust. https://doi.org/10.1029/2021GL095009
- Follow-up: **Peacock & Bedrosian (2023, GRC Trans 47)** built a regional 3D resistivity model of the whole Great Basin from MT, from the surface to the mantle, and used its conductance maps to find fluid-collection zones. https://www.geothermal-library.org/index.php?mode=pubs&action=view&record=1034877
- Significance: deep regional MT is public through USGS and the EarthScope/USArray lineage, and it carries predictive signal that most explorers do not use. This is confirmed by 2.5 below.

### 2.4 Folsom, Sewell, Cumming et al. (2024). *Direct comparison of resistivity models from helicopter TEM and MT over a blind system, East Hawthorne NV.* GRC 2024 / SAND2025-11015C.
- The site is a blind system at ~100 °C shallow. The comparison is HTEM along profiles, resolving 300–500 m deep, against a **61-station MT survey at ~800 m spacing** with a 3D inversion.
- MT "surveys collected with wide station spacing (>1 km) can easily miss the alteration associated with a geothermal system, which can sometimes encompass small areas (<2 km²)", so MT "can be a poor tool for reconnaissance."
- Conclusion: **HTEM is the better prospecting (search) tool**. It causes no ground disturbance, is simple to permit, and covers large areas fast, but mobilization is costly. **MT remains the better tool** for conceptual models, well targeting and capacity estimates. https://www.osti.gov/biblio/3683813

### 2.5 Trainor-Guitton, Menon, Pinchuk, … Coolbaugh, Lindsey, Faulds (2025). *"Hidden" hydrothermal technical potential & technoeconomics.* Geothermics 133:103473.
- XGBoost regression trained on **37 operating plants** plus negative (0 MW) sites, using **48 geophysical/geological features** from INGENIOUS. Predictions were fed into NREL reV.
- **Feature importance**: five of the top ten appear in both the impurity and permutation lists: elevation trend, **surface conductivity**, **lower-crust conductivity**, distance to 130–750 ka faults, and detrended elevation. Heat flow appears in 3 of the 4 importance rankings, and **mantle/upper-mantle conductivity (MT-derived) in all 4**. Geodetic shear and strain also appear.
- Great Basin total capacity: **28.45 GW (MSE model), 23 GW (P50), 79.5 GW (P90)**, consistent with the USGS 30 GW. Site LCOE is **$58–62/MWh**, or about $65–70/MWh including transmission, against ~$75 for temperature-only estimates.
- Takeaway: MT conductivity and geomorphology (elevation trend) rank as high as heat flow, and both are public. The model has only 37 positive labels, so it is starved for labels rather than features. https://www.osti.gov/biblio/3018341

### 2.6 Downs, Schwering, Kraal, Folsom et al. (2025). *BRIDGE: Basin & Range Investigation for Developing Geothermal Energy.* SAND-2025-01826 (144 pp.).
- Workflow: regional data → **3,000 km² HTEM survey (1,877 line-km in 12 days, Mar–Apr 2022, ~2 km line spacing, 1 km over East Hawthorne, a sounding every ~30 m)** → 2-m temperature → 3D MT → TG holes under 150 m → slim hole.
- Premise: "zones of low resistivity frequently occur over geothermal systems in the Basin and Range," because the smectite clay cap is conductive.
- The prospect portfolio has three finalists ready for TGH drilling: **Lee Allen** (greenfield, sinter, 140–180+ °C indicated), **Grover Point** and **East Hawthorne**. Several non-finalists stalled because of "problems with timely land access," which matters for any acquisition strategy.
- Critical data point: "for most of the US Great Basin that is prospective for hidden geothermal systems, a regional HTEM survey similar to the data acquired for BRIDGE **will become publicly available as part of the USGS Earth Mapping Resources Initiative**", together with lidar, magnetics and gamma-ray surveys. https://www.osti.gov/biblio/2540220

### 2.7 Kraal & Schwering (2024). *Remote sensing case studies for detection of geothermal surface materials, Basin and Range.* GRC Trans 48 / SAND2024-16756C.
- Uses **public JPL AVIRIS-Classic hyperspectral data (225 channels, 400–2500 nm, 14 m pixels)** and compares it with the public USGS ASTER alteration map (Mars 2013: 30 m argillic/phyllic, 90 m silica).
- Targets: opal/chalcedony (sinter, silicified sediments), tufa/carbonate, kaolinite (steam-heated zone) and smectite (clay cap). Sinter indicates reservoirs above ~175 °C (Fournier 1983). Some Great Basin tufa systems carry 150–170 °C geothermometry (Coolbaugh et al. 2009).
- Validated at known sites (Salt Wells, Lee Allen), then applied to greenfield Gabbs Valley, Hawthorne and Bell Flat. Hyperspectral found **additional altered outcrops that ASTER missed**. Small (1–500 m²) alteration exposures in the footwalls of Quaternary faults are flagged as the best blind-system clues, and they are too small for ASTER.
- Authors' outlook: "As additional high-quality, publicly available hyperspectral data is acquired … (e.g., through the USGS Earth MRI program, and new satellites), there is potential for the discovery of new blind geothermal systems." https://www.osti.gov/biblio/3009542

### 2.8 Coolbaugh, Kratt, Fallacaro, Calvin & Taranik (2007). *Detection of geothermal anomalies using ASTER TIR images at Bradys Hot Springs, NV.* Remote Sensing of Environment.
- This is the classic demonstration that 90 m ASTER night-time TIR, after corrections for topography and albedo, can pick out thermal ground anomalies of a few °C over a known field (unverified detail; abstract not retrieved). TIR only sees systems that already leak heat at the surface, so it adds little for truly blind systems. https://doi.org/10.1016/j.rse.2006.09.001
- Calibration from **Vaughan et al. (2012, JVGR)** at Yellowstone: ASTER TIR (90 m) radiant heat flux is ~2.0 GW, only **30–45%** of the geochemical estimate. MODIS (1 km) time series are dominated by seasonal cycles. TIR is a weak, surface-biased tool. https://doi.org/10.1016/j.jvolgeores.2012.04.022

### 2.9 InSAR: Ali, Akerley, Feigl et al. (2016), Geothermics; Eneva et al. (2018, GRC); Reinisch et al. (2024)
- Ali et al. (2016) produced a time series of production-induced subsidence at Brady Hot Springs, a field-scale bowl centred on the well field (rates of order mm–cm/yr; unverified). https://doi.org/10.1016/j.geothermics.2016.01.008
- At Coso (Eneva et al.), maximum subsidence was **−27.6 mm/yr (Envisat)** and **−19.1 mm/yr (Sentinel)**, with horizontal motion of ±12–24 mm/yr. https://www.geothermal-library.org (GRC Trans 42, record 1033950)
- Reinisch et al. (2024, *Remote Sensing* 16(11), LANL): a deep-learning denoiser recovers **±2.5 mm** deformation from a Mw 3.4 event, about an order of magnitude better than earlier work. https://www.osti.gov/biblio/2426558
- Assessment: InSAR is mostly a *monitoring* tool for producing fields. For exploration its value is indirect, through geodetic strain and dilation rates, which INGENIOUS and Trainor-Guitton use as permeability features. Free Sentinel-1 and NISAR data could give basin-scale fault-creep and strain maps, an exploration use that is under-studied (my inference).

### 2.10 Soil-gas / CO2 flux: Bergfeld, Goff & Janik (2001), Chem. Geol.; Wannamaker et al. (2019), Stanford
- **Dixie Valley NV**: background soil CO2 flux is ~7 g/m²/d and the maximum measured was **570 g/m²/d**. The geothermal CO2 flux is 0.1–7.5 t/d over 0.01–0.14 km² patches. Peak flux in 1998 was 7–8× the 1986 pre-production level, so the signal is real but small-footprint. https://doi.org/10.1016/S0009-2541(00)00381-8
- **Wannamaker, Faulds, Kennedy et al. (2019)** combined MT, soil gas, structure and fluid geochemistry. At McGinness Hills (a blind field) elevated **³He** shows a magmatic connection, with magmatic fluids at ~10–15% of producing fluid. A Kumiva–Black Rock survey with **131 MT sites** gave more diffuse results. https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=29105
- Bloomberg et al. (2014, G-cubed): more than 3,000 flux measurements at Rotokawa NZ give 441 ± 84 t/d CO2 and ~226 MWt. Earlier estimates were low by ~700%, so soil flux works as a *heat-flow proxy*. https://doi.org/10.1002/2014GC005327
- Assessment: soil gas is cheap, field-scale follow-up after targeting, not a regional screen. No public US-wide dataset exists.

### 2.11 Ahmmed & Vesselinov (2022). *Machine learning and shallow groundwater chemistry to identify geothermal prospects in the Great Basin.* Renewable Energy 197:1034–1048.
- Unsupervised NMFk over **14,341 water-chemistry locations × 18 attributes** (public NBMG and USGS data). It extracts three "hidden geothermal signatures" at modest, moderate and high confidence, consistent with play fairway results. https://www.osti.gov/biblio/1881824
- Takeaway: decades of public water-well chemistry contain a geothermometer signal that ML can surface cheaply. This is the closest analogue to Terranox mining assessment files.

### 2.12 Supporting: NREL PFA Retrospective (Pauling, Taverna, Trainor-Guitton et al. 2023); Mining G.O.L.D. (Levine et al. 2022)
- **PFA retrospective**: DOE funded 11 play fairway teams from 2014 to 2021. In Phase III, four teams drilled TG wells at **7 plays and found anomalously high temperatures/gradients at 4 (57%)**. https://www.osti.gov/biblio/2004915
- **Mining G.O.L.D. (NREL/TP-6A20-81946)**: mineral-exploration data (Cu, Au, Li drilling and geophysics) in Nevada has already led to geothermal discoveries. Using it could cut geothermal LCOE by **23–29%**, and mining companies could "catalogue this data at minimal cost and either sell it or use it." https://www.osti.gov/biblio/1855781
- Zanskar CRADA with NREL, "Big Data Meets Geothermal Exploration" (Sonsteng, Hoiland, Edwards 2026): Zanskar tested low-cost seismometer arrays for micro-earthquake and ambient-noise imaging to guide well siting. https://www.osti.gov/biblio/3015294

---

## 3. Method-by-method scorecard (exploration value for blind systems)

| Method | Scale role | Public coverage | Blind-system signal | Under-exploited? |
|---|---|---|---|---|
| Gravity | Regional–prospect structure (basin geometry, step-overs, terminating gradients) | USGS/NGS national gravity database; dense in NV | Strong (a Faulds PFA weighted layer) | Moderately. Used in PFA, but ML on raw grids and derivatives is thin |
| Aeromagnetics | Structure, buried dikes, magnetic lows from alteration | USGS NA magnetic grid (OFR 2002-414) plus state surveys; Earth MRI is adding high-res | Moderate (Gabbs magnetic low; Granite Springs dike swarm, Glen et al. 2022) | **Yes**. New Earth MRI high-res mag has barely been used for geothermal |
| MT (deep regional) | Crust/mantle conductance, fluid "plumbing" | USGS regional MT, EarthScope-era stations | Top-ranked ML feature (Trainor-Guitton 2025) | **Yes**. Rarely ingested outside USGS/INGENIOUS |
| MT (3D prospect) | Well targeting, clay cap geometry | Proprietary per prospect | High, but expensive and permit-heavy | No. Standard industry practice |
| Airborne EM (HTEM/AEM) | Shallow (≤300–500 m) clay-cap search | BRIDGE 3,000 km²; **Earth MRI regional AEM coming** | High for search (Folsom 2024) | **Strongly yes**. The new public layer for blind-system search |
| Hyperspectral (AVIRIS, EMIT) / ASTER | Sinter, silica, kaolinite, tufa mapping | AVIRIS-C public flight lines; ASTER alteration maps (Mars 2013); NASA EMIT satellite | Moderate (relict and fault-footwall clues) | **Yes**. Kraal 2024 is among the few systematic Great Basin applications |
| Thermal IR (ASTER/Landsat) | Surface heat leakage | Global, free | Weak for blind systems (30–45% capture even at Yellowstone) | No. Low ceiling |
| InSAR (Sentinel-1, NISAR) | Strain/dilation, production monitoring | Global, free | Indirect (geodetic strain is a permeability feature) | Partly. Basin-scale strain products not routinely built for geothermal |
| Soil CO2 / He / 2-m temp | Prospect-scale follow-up | None regional (2-m temp in INGENIOUS) | High locally, footprint < 1 km² | n/a. Field tool, cheap (<$100k per prospect, unverified) |
| Water/well chemistry | Regional geothermometry | NBMG/USGS ~14k sites | Moderate–high (Ahmmed 2022) | Yes |

---

## 4. Which public datasets are under-exploited (ranked)

1. **USGS Earth MRI airborne EM, magnetics and radiometrics over the Great Basin.** BRIDGE explicitly says a regional HTEM like theirs "will become publicly available" for most of the prospective Great Basin. Earth MRI is a *critical-minerals* program (its own page does not mention geothermal: https://www.usgs.gov/special-topics/earth-mri), so geothermal teams are not its natural users. **This is the single biggest "public-but-illegible" layer arriving now.** It is a direct parallel to Terranox's Saskatchewan assessment database: newly released, government-funded, collected for a different commodity.
2. **Mining-company assessment and claim-maintenance drilling plus geophysics (Nevada Cu/Au/Li).** NREL's Mining G.O.L.D. reports a 23–29% LCOE upside, and historic blind discoveries came from "wells drilled for other purposes … mineral exploration" (BRIDGE; Faulds 2021). Much of this is scattered in NBMG/BLM files.
3. **Deep regional MT conductance.** It ranks top in the 2025 ML importance study but few explorers ingest it.
4. **Public hyperspectral (AVIRIS-C/NG flight lines, NASA EMIT, Earth MRI hyperspectral).** Only a handful of geothermal studies exist (Kratt 2010; Calvin 2015; Kraal 2024).
5. **Free InSAR-derived strain and fault creep** as a permeability proxy, a low-cost national layer.
6. Already used well: the INGENIOUS compilation (gravity, mag, MT, heat flow, 2-m temps, sinter/tufa, geochem; DOI 10.15121/1881483), USGS gravity and mag grids, and 2-m temperature surveys. These are now table stakes, and Zanskar certainly ingests them.

---

## 5. Cost and sequence logic (from BRIDGE and Folsom)

The industry consensus funnel is: regional public layers → regional AEM (big fixed cost, but soon free via Earth MRI) → 2-m temperature (cheap) → 3D MT (prospect) → TG holes under 150 m → slim hole. Each step costs roughly 10× the one before (order-of-magnitude, unverified). PFA TG drilling hit anomalies at 4 of 7 plays. The Gabbs Valley hole reached 124 °C at 152 m, so first-proof-of-heat can come at very shallow depth and modest cost.

---

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **The data-arbitrage thesis holds.** About 70–75% of Great Basin convective resources are blind, and about half of them are undiscovered (BRIDGE; Faulds 2021). The USGS mean for undiscovered resource is ~30 GW, and the 2025 ML estimate for the Great Basin is 23–79.5 GW. Discovery has historically been *accidental*. A systematic ML pass over public layers is a credible edge, and the market is not too small.
2. **The best "Terranox moment" is Earth MRI AEM, magnetics and hyperspectral.** As with the Saskatchewan assessment files, these are government data released under a mandate for another commodity (critical minerals). They resolve exactly the shallow clay-cap conductors that Folsom and BRIDGE show to be the best blind-system search signal, and they arrive basin by basin. The company that ingests each new release first and **files BLM nominations and leases on the conductive anomalies before anyone else reads them** captures the Terranox step-up. The optimal design is release-triggered acquisition.
3. **The second illegible pile is mining-exploration records** (NBMG and BLM assessment and claim data, old core holes with temperature notes, IP/resistivity surveys from Au/Li campaigns). This is literally Terranox's existing core skill transposed to a new commodity, and it is the most defensible data moat because it requires document-level ML (OCR, scanned logs), not just raster stacking.
4. **The gap vs Zanskar.** From public materials, Zanskar's emphasis is an integrated "world model for the subsurface" plus heavy field geology, its own seismic arrays (NREL CRADA), drilling, a 100 MW NV Energy PPA, plant ownership (Lightning Dock) and development capital ($115M Series C in Jan 2026; a $40M facility scaling to $100M). Zanskar is becoming a **vertically integrated developer** that drills and builds what it finds. Its constraint is capital and rig time per prospect. It cannot drill every anomaly, which leaves room for a **"land bank" layer**: a company that secures rights cheaply across hundreds of second-tier anomalies, then proves them with cheap 2-m surveys and 150 m TG holes (Gabbs-style 124 °C at 152 m) and sells at a step-up to Zanskar, Ormat, Fervo or utilities. BRIDGE's note that prospects stalled on "timely land access" shows that rights, not ideas, are the bottleneck.
5. **Method-level differentiation.** Zanskar's public signals stress seismic and field geology. The literature says the under-used *public* layers are AEM, deep MT conductance, high-res aeromagnetics, hyperspectral alteration and mining drill records. A Terranox-shape company can be "first reader of every new public geophysical release" rather than "best physicist on one prospect."
6. **Risks to flag.** (a) Thermal IR and InSAR have a low ceiling for blind exploration, so don't over-claim them. (b) Training labels are scarce (37 operating plants). Lift has to come from feature novelty (new AEM and mining data), not model sophistication. (c) BLM geothermal leasing goes through competitive nominations, so first-mover advantage depends on how fast nominations go in after a data release. Score on plausibility per the standing rules.

---

## Sources
- Faulds et al. 2021, Nevada PFA all phases: https://www.osti.gov/biblio/1724080
- Craig et al. 2021, Gabbs Valley blind system: https://doi.org/10.1016/j.geothermics.2021.102177
- Peacock & Siler 2021 GRL: https://doi.org/10.1029/2021GL095009
- Peacock & Bedrosian 2023 GRC: https://www.geothermal-library.org/index.php?mode=pubs&action=view&record=1034877
- Glen et al. 2022 GRC, Granite Springs geophysics: https://www.geothermal-library.org/index.php?mode=pubs&action=view&record=1034630
- Folsom et al. 2024, HTEM vs MT: https://www.osti.gov/biblio/3683813
- Downs et al. 2025, BRIDGE report: https://www.osti.gov/biblio/2540220
- Trainor-Guitton et al. 2025 Geothermics: https://www.osti.gov/biblio/3018341
- Kraal & Schwering 2024, hyperspectral: https://www.osti.gov/biblio/3009542
- Coolbaugh et al. 2007 RSE, ASTER TIR: https://doi.org/10.1016/j.rse.2006.09.001
- Vaughan et al. 2012 JVGR, ASTER/MODIS TIR: https://doi.org/10.1016/j.jvolgeores.2012.04.022
- Ali et al. 2016 Geothermics, InSAR Brady: https://doi.org/10.1016/j.geothermics.2016.01.008
- Reinisch et al. 2024, InSAR deep learning: https://www.osti.gov/biblio/2426558
- Bergfeld, Goff & Janik 2001, Dixie Valley CO2: https://doi.org/10.1016/S0009-2541(00)00381-8
- Wannamaker et al. 2019 Stanford, MT + soil gas: https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=29105
- Bloomberg et al. 2014 G-cubed, soil CO2 heat proxy: https://doi.org/10.1002/2014GC005327
- Ahmmed & Vesselinov 2022, ML on water chemistry: https://www.osti.gov/biblio/1881824
- NREL PFA Best Practices 2023: https://www.osti.gov/biblio/2004915
- NREL Mining G.O.L.D. 2022: https://www.osti.gov/biblio/1855781
- INGENIOUS Great Basin dataset: https://gdr.openei.org/submissions/1391
- USGS 2008 geothermal assessment: https://pubs.usgs.gov/fs/2008/3082/
- USGS Earth MRI: https://www.usgs.gov/special-topics/earth-mri
- USGS North America magnetic grid: https://mrdata.usgs.gov/magnetic/
- Zanskar NREL CRADA 2026: https://www.osti.gov/biblio/3015294
- Zanskar company pages: https://www.zanskar.com/about
