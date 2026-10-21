# L15: Geothermometry and fluid-geochemistry databases as a signal for blind geothermal systems

**Scope.** This file covers four things:
- public spring, well and groundwater chemistry: USGS, NWIS/Water Quality Portal, NBMG/GBCGE, USGS Produced Waters;
- the geothermometer physics that turns that chemistry into a temperature signal;
- the published ML-on-geochemistry literature;
- what all of this means for a Terranox-shape "find it, lock the right, sell the proven state" company.

**Method note.** The shared WebSearch budget for this run was already used up when this agent started. Every source below was reached by direct fetch:
- DOI metadata and abstracts from Crossref, OpenAlex and Semantic Scholar;
- primary pages at USGS, OSTI, ScienceBase and GitHub.

Where only metadata, and not an abstract, could be read, the file says so. Claims I could not retrieve are marked (unverified).

---

## 1. Primary sources reviewed

### 1.1 Williams, Reed & Mariner (2008). USGS OFR 2008-1296, *A review of methods applied by the USGS in the assessment of identified geothermal resources*
I read the full text from the PDF.
- **Why geothermometry matters.** Chemical geothermometers on "hot springs, fumaroles, geysers, and **shallow water wells**" are the standard tool to "estimate the subsurface temperature of a geothermal prospect area before any deep wells are drilled."
- **Which geothermometers the USGS assessment uses.**
  - Silica: Giggenbach (1992) smoothed chalcedony-to-quartz curve for 20–210 °C, and quartz above 210 °C.
  - Cation: **K-Mg (Giggenbach 1988)** is "generally the preferred cation geothermometer". Na-K-Ca is used for Cl-rich waters or where Mg is missing.
- **Why the old cation method was dropped.** The older Na-K-Ca-Mg approach produced a discontinuity and **under-reported systems in the 100–130 °C band**. That band is exactly where many blind Basin-and-Range targets sit.
- **Basin-and-Range caution.** Waters there are predominantly Na-HCO3, not the Na-Cl waters the classical geothermometers were calibrated on, so "extra caution" is needed.
- **Equilibration times (Barton 1984).** Na-K-Ca: ~100 years at 150 °C. Quartz: tens of years at 100 °C.
- **QC rule.** Analyses with a charge-balance error above 10% are used only as a last resort. This is an automatable QC rule for a data pipeline.
- **Headline totals (Fact Sheet 2008-3082).** Identified 9,057 MWe; undiscovered (mean) 30,033 MWe; EGS 517,800 MWe.

### 1.2 Fournier & Truesdell (1973), *An empirical Na-K-Ca geothermometer for natural waters*, GCA 37(5):1255–1275
- The foundational empirical cation geothermometer, with 1,000+ citations (DOI 10.1016/0016-7037(73)90060-4).
- I could read metadata only, not the abstract. Its role and limitations are described in 1.1.

### 1.3 Fournier (1977), *Chemical geothermometers and mixing models for geothermal systems*, Geothermics 5:41–50
- Introduced silica-enthalpy and mixing models for estimating a deep hot end-member from cooled, diluted spring or well water (DOI 10.1016/0375-6505(77)90007-4; ~1,070 citations).
- This is the conceptual basis for reading a **diluted, mixed signal in an ordinary groundwater well** as evidence of a hidden upflow. That reading is the key move for blind systems.
- I could read metadata only.

### 1.4 Giggenbach (1988), *Geothermal solute equilibria. Derivation of Na-K-Mg-Ca geoindicators*, GCA 52:2749–2765
- Introduced the Na-K-Mg ternary ("Giggenbach diagram") and the K-Mg geothermometer (DOI 10.1016/0016-7037(88)90143-3; ~2,050–2,120 citations).
- The ternary separates "fully equilibrated", "partially equilibrated" and "immature" waters. That classification works as a ready-made **label or feature** for ML.
- I could read metadata only.

### 1.5 Spycher, Peiffer, Sonnenthal, Saldi, Reed & Kennedy (2014), *Integrated multicomponent solute geothermometry*, Geothermics 51:113–123
- Multicomponent geothermometry (GeoT) computes saturation indices of many minerals at once. It numerically optimizes for the temperature where they converge, and corrects for dilution and gas loss (DOI 10.1016/j.geothermics.2013.10.012).
- This is the physics-based alternative to single-ratio geothermometers, applied in the Great Basin (e.g., Dixie Valley; unverified for the specific case study).
- I could read metadata only.

### 1.6 Kennedy & van Soest (2007), *Flow of mantle fluids through the ductile lower crust: helium isotope trends*, Science 318:1433
I read the abstract (DOI 10.1126/science.1147537).
- **Regional trend.** Minimum ³He/⁴He in surface fluids across the northern Basin and Range rises systematically east to west, from crustal to mantle values, tracking active extension and shear strain rates.
- **Local anomalies.** Superimposed local high-³He/⁴He anomalies indicate "hidden magmatic activity and/or deep fluid production with locally enhanced permeability, identifying zones with high resource potential, particularly for geothermal energy development".
- **Why it matters here.** Helium isotopes in ordinary water wells are a direct permeability tracer for blind systems. They are under-sampled and cheap to add.

### 1.7 Ahmmed & Vesselinov (2022), *Machine learning and shallow groundwater chemistry to identify geothermal prospects in the Great Basin, USA*, Renewable Energy 197:1034–1048
The citation comes from the GeoThermalCloud repository. The dataset and results come from the project's public notebook and the OSTI final report.
- **Data.** **14,258 Great Basin water points** (OSTI report: 14,342) with **18 attributes**:
  - measured temperature;
  - quartz and chalcedony geothermometer temperatures;
  - pH and TDS;
  - Al, B, Ba, Be, Br, Ca, Cl, HCO3, K, Li, Mg, Na;
  - δ¹⁸O.
- **Very sparse.** Temperature has 13,894 values, TDS 1,740, Al 1,362 and δ¹⁸O 1,471.
- **Method.** Unsupervised NMFk (non-negative matrix factorization plus customized k-means). The optimal model has **3 signatures**:
  - **B (high prospectivity):** quartz, chalcedony and Al, at 5,201 locations;
  - **C (intermediate):** temperature, Mg, Ca, HCO3, pH, Ba and Be, at 2,801 locations;
  - **A (low):** TDS, B, Br, Na, Cl, K, Li and δ¹⁸O, at 6,256 locations.
- **Read-through.** This is the largest published ML-on-water-chemistry geothermal study in the US. Its discrimination is weak: ~36% of points land in the "high" class. It shows that the regional chemistry layer is public, assembled and already ML-processed, but **coarse**.
- Sources: https://github.com/SmartTensors/GeoThermalCloud.jl/blob/master/GreatBasin/notebook/GreatBasin.md ; https://www.osti.gov/biblio/3003965

### 1.8 Vesselinov, Ahmmed, Mudunuru, Pepin, Burns, Siler, Karra & Middleton (2022), *Discovering hidden geothermal signatures using non-negative matrix factorization with customized k-means clustering*, Geothermics 106:102576
- This is the methods paper for NMFk. Its case study is SW New Mexico: **44 locations, 18 attributes**, mixing geochemistry (geothermometer temperatures, ions) with geology and geophysics. Numbers are per the OSTI summary.
- **Result.** It identified low- and medium-temperature hydrothermal signatures and "one new highly prospective site".
- I could read metadata only (Elsevier 403). Details are taken from the OSTI summary at https://www.osti.gov/biblio/3003965.

### 1.9 Mudunuru, Ahmmed, Rau, Vesselinov & Karra (2023), *Machine Learning for Geothermal Resource Exploration in the Tularosa Basin, New Mexico*, Energies 16(7):3098
I read the abstract (DOI 10.3390/en16073098).
- **Method.** NMFk applied to DOE GDR play-fairway data. Per OSTI: **120 locations, 21 attributes**, including geochemistry.
- **Result.** Prospects "consistent with the existing Tularosa Basin's PFA studies".
- **Read-through.** This is validation by agreement with experts, not by drilling.

### 1.10 Frash, Ahmmed, Mudunuru, Vesselinov, Karra et al. (2024), *GeoThermalCloud* DOE final reports (PNNL-34975, OSTI 3003965; LA-UR-24-33027, OSTI 2480434)
- **Tools.** The open-source GeoThermalCloud stack on top of the SmartTensors unsupervised-ML platform, used to fuse sparse geochemistry, geology and geophysics.
- **Sites.** SW NM, Great Basin, Tularosa, Utah FORGE, Hawaii, Brady and McGregor Range.
- **Contributors.** LANL, PNNL, Chevron, Google, Stanford and Julia Computing.
- **Read-through.** The national labs have **open-sourced the "ML on geochemistry" layer**. It is not a moat.

### 1.11 Siler, Pepin, Vesselinov, Mudunuru & Ahmmed (2021), *Machine learning to identify geologic factors associated with production in geothermal fields: Brady, Nevada*, Geothermal Energy 9:17
I read the abstract (DOI 10.1186/s40517-021-00199-8).
- **Method.** NMFk on 14 3D geologic characteristics.
- **Result.** Production wells preferentially sit on macro-scale faults and a local fault step-over.
- This is not geochemistry itself, but it is the same toolchain. It shows that the permeability control (structure) is what geochemistry must be paired with.

### 1.12 Supervised ML geothermometers (the "learned geothermometer" literature)
- **Can (2002), Geothermics 31(6):751–760.** The first ANN-improved Na/K geothermometer (DOI 10.1016/S0375-6505(02)00044-5). Metadata only.
- **Pérez-Zárate, Santoyo, Acevedo-Anicasio, Díaz-González & García-López (2019), Computers & Geosciences 129:49–68.** I read the abstract (DOI 10.1016/j.cageo.2019.05.004).
  - Inputs: gas ratios ln(H₂S/CO₂), ln(CH₄/CO₂) and ln(H₂/CO₂). Targets: measured bottomhole temperatures. Split: 80/10/10.
  - The best net was 3-8-1.
  - On an external test with **13 Olkaria (Kenya) samples**, mean error was **2–11%**.
- **Tut Haklidir & Haklidir (2020), Natural Resources Research.** Prediction of reservoir temperature from hydrochemistry in Western Anatolia geothermal systems (DOI 10.1007/s11053-019-09596-0; ~85–93 citations).
  - The abstract is publisher-elided.
  - Reported to compare a deep neural network against linear and other regressors, with the DNN best (unverified: exact metrics and sample count).
- **Varol Altay, Gürgenç, Altay & Dikici (2022), Geothermics 104:102476.** A metaheuristic-optimized ANN predicting reservoir temperature from hydrogeochemistry across Anatolian fields (DOI 10.1016/j.geothermics.2022.102476). Metadata only. Metrics are unverified.
- **Read-through.** Learned geothermometers are a mature niche, mostly Turkish and Mexican, trained on volcanic and high-enthalpy fields. **None targets low-signal, diluted Great Basin groundwater wells for blind-system detection.** That is an open niche.

### 1.13 Mordensky, Lipor, DeAngelo, Burns & Lindsey (2023), *When less is more…*, Geothermics 110:102662
I read the abstract (DOI 10.1016/j.geothermics.2023.102662).
- **Study.** Nine favorability maps for the western US on the USGS 2008 assessment data, comparing weights-of-evidence and logistic regression with XGBoost, SVM and ANN.
- **Core difficulty named by the authors.** There are "no negative examples and severe class imbalance". XGBoost beat expert-decision baselines.
- **Read-through.** The binding constraint is labels and feature quality, not algorithms. A cheaper, denser *geochemical* label set (geothermometer temperatures at tens of thousands of wells) partly attacks the label shortage.

### 1.14 DeAngelo, Burns & Mordensky (2026), *Conventional hydrothermal power-producing systems of the Great Basin*, Stanford SGW 51 (USGS pubs 70273870)
I read the abstract.
- **Inventory for the new USGS assessment.** **205 systems**: 28 with operating plants, 78 known electric-grade and 99 newly identified "probable" electric-grade.
- **Classification rule.** Electric-grade means a measured well temperature above 85 °C plus evidence of convection. Points are clustered into systems at 10 km.
- **Read-through.** Most of the 99 "probable" systems are recognised from public well and spring data. That is the hit list everyone now has.

### 1.15 Lautze, Thomas, Hinz, Apuzen-Ito, Frazer & Waller (2017), *Play fairway analysis of geothermal resources across the State of Hawaii: 1. Geological, geophysical, and geochemical datasets*, Geothermics (DOI 10.1016/j.geothermics.2017.02.001)
- A state-wide compilation in which groundwater-well chemistry (Cl/Mg, silica, temperature anomalies) is a core "heat" and "fluid" indicator.
- The Ahmmed et al. 2020 NMFk analysis of these data appears in the GeoThermalCloud publication list.
- I could read metadata only.

### 1.16 Data infrastructure (primary database pages)
- **Water Quality Portal: Read et al. (2017), Water Resources Research 53:1735, DOI 10.1002/2016WR019993.**
  - Abstract: ">290 million records from >2.7 million sites in groundwater, inland, and coastal waters".
  - It integrates USGS NWIS and EPA WQX from "over 400 state, federal, tribal, and local agencies" (https://www.waterqualitydata.us/).
  - This is the national raw feed. Most of it is non-geothermal domestic, irrigation and monitoring wells, but many records carry temperature, SiO₂, Na, K, Mg, Cl, B and Li, which is enough to compute geothermometers at scale.
- **USGS National Produced Waters Geochemical Database (Blondes, Morrissey, Rowan, Thordsen, Kharaka, Engle et al.).**
  - v2.3 covers oil and gas well waters from **1905–2014**: inorganic chemistry, isotopes and well and rock properties. It has been superseded by v3.0 (2023) (https://www.sciencebase.gov/catalog/item/59d25d63e4b05fe04cc235f9).
  - Sample count: ~165k samples in v2.3 (unverified).
  - This is the sedimentary-basin equivalent: brine chemistry plus BHT for Permian, Williston, Gulf Coast and Uinta geothermal (and lithium) screening.
- **NBMG / Great Basin Center for Geothermal Energy (UNR).** Holds the Nevada geothermal spring and well chemistry compilations, including the Great Basin groundwater geochemical compilation that likely underlies the Ahmmed & Vesselinov dataset (unverified: exact provenance and record counts). The NBMG and NGDS (geothermaldata.org) servers returned HTTP 503 during this run.

---

## 2. Synthesis: what the geochemistry literature says

1. **The physics is mature and public.** Silica, K-Mg, Na-K-Ca, Giggenbach ternary, mixing models and multicomponent GeoT are all published and sit in USGS methodology since 2008.
2. **The data are public but illegible.**
   - WQP holds 290M+ records at 2.7M+ sites, and the USGS produced-water database spans more than a century.
   - Both are noisy: charge-balance failures, missing Mg or SiO₂, Na-HCO3 waters outside calibration ranges, and mixed or diluted fluids.
   - Turning them into geothermometer temperatures needs QC rules (CBE >10%), mixing correction (Fournier 1977) and equilibrium screening (Giggenbach 1988). This is the same "make the archive legible" problem Terranox solves for SMAD.
3. **ML on geochemistry is open-source but low-resolution.** The LANL/PNNL GeoThermalCloud work, on 14k Great Basin points, 44 SW NM points and 120 Tularosa points, is unsupervised. It is validated only against expert play-fairway maps, and its "high" class covers a third of the points. No paper reports a drilled, held-out test of a geochemistry-based ML ranking.
4. **Blind systems leave weak chemical fingerprints, but the fingerprints exist.**
   - By definition there are no springs. Diluted outflow, elevated silica or K-Mg temperatures, B, Li and ³He/⁴He anomalies can still show up in ordinary water wells down-gradient.
   - The Gabbs Valley play-fairway discovery cited "geothermometry from water wells" among its collocated evidence (see L01/L02).
   - Kennedy & van Soest (2007) show that He isotopes flag hidden deep permeability.
5. **Zanskar's public disclosures do not lean on geochemistry.** For Big Blind (no surface manifestations, ~250 °F at ~2,700 ft) and Pumpernickel (~280 °F at ~2,500 ft, ~20 MWe Phase 1), Zanskar cites an "AI-prediction engine" and stochastic reservoir modelling on legacy geology and shallow wells. Neither public write-up mentions geothermometry or water chemistry.

---

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **Geochemistry is the cheapest "public-but-illegible" layer and maps one-to-one onto the Terranox engine.**
   - Tens of millions of WQP/NWIS groundwater analyses, the century-long produced-waters database, and state-survey spring and well files can be converted at near-zero marginal cost into a national grid of **geothermometer temperatures, mixing-corrected deep-fluid estimates and anomaly scores**.
   - The physics is settled (USGS uses K-Mg plus Giggenbach-silica), so ML lift here is plausible: it is denoising, QC, mixing deconvolution and fusion, not inventing new science.
2. **The value is labels, not features.** Mordensky et al. (2023) name "no negative examples and severe class imbalance" as the core ML failure. A screened geothermometer temperature at each of ~10⁴–10⁵ wells is a weak, cheap label at scale. That is the bottleneck every structural/heat-flow favourability model (including USGS's and plausibly Zanskar's) is starved of.
3. **Cheap proof steps exist below a TG hole.**
   - Re-sampling existing domestic, stock and irrigation wells for SiO₂, K, Mg, B, Li and ³He/⁴He costs hundreds of dollars per sample (unverified cost). It needs no drilling permit and can run before the lease is filed.
   - That gives a Terranox-like company a stealth, pre-acquisition confirmation step: rank cells, sample wells quietly, then nominate BLM parcels or option private and state rights, and only then drill TG holes.
4. **Gap vs Zanskar.**
   - Zanskar is a vertically integrated developer: $115M Series C, Lightning Dock, a 100 MW NV Energy PPA, and several 20 MW plants planned. Its disclosed discovery stack is AI plus stochastic reservoir modelling plus its own drilling.
   - It does not publicly exploit (a) national groundwater and produced-water chemistry as a screening and label layer, (b) a **land-bank-and-flip** model, or (c) sedimentary-basin brines, where geochemistry co-maps temperature and lithium value (see L12).
   - A Terranox shape can own many cheap rights across the 99 USGS "probable" systems plus chemistry-flagged blind cells. It can upgrade them with water sampling and TG holes, then sell proven states to Ormat, Fervo, Cyrq, Zanskar itself, or data-centre developers. That is ownership, not a tool.
5. **Risks to price in.**
   - The ML-on-geochemistry layer is already open-source (GeoThermalCloud), so the moat must be data cleaning, proprietary resampling and speed on land.
   - Basin-and-Range Na-HCO3 waters violate geothermometer calibration assumptions.
   - The strongest geochemical anomalies (hot springs) are already known and leased.
   - The blind-system signal sits in diluted, mixed waters where false-positive rates are unpublished.

## Sources
- https://pubs.usgs.gov/of/2008/1296/ (Williams, Reed & Mariner 2008; full PDF read)
- https://pubs.usgs.gov/fs/2008/3082/
- https://doi.org/10.1016/0016-7037(73)90060-4 (Fournier & Truesdell 1973)
- https://doi.org/10.1016/0375-6505(77)90007-4 (Fournier 1977)
- https://doi.org/10.1016/0016-7037(88)90143-3 (Giggenbach 1988)
- https://doi.org/10.1016/j.geothermics.2013.10.012 (Spycher et al. 2014)
- https://doi.org/10.1126/science.1147537 (Kennedy & van Soest 2007)
- https://github.com/SmartTensors/GeoThermalCloud.jl (publication list) and https://github.com/SmartTensors/GeoThermalCloud.jl/blob/master/GreatBasin/notebook/GreatBasin.md (Great Basin dataset and results)
- https://doi.org/10.1016/j.geothermics.2022.102576 (Vesselinov et al. 2022)
- https://doi.org/10.3390/en16073098 (Mudunuru et al. 2023)
- https://www.osti.gov/biblio/3003965 ; https://www.osti.gov/biblio/2480434 (GeoThermalCloud final reports)
- https://doi.org/10.1186/s40517-021-00199-8 (Siler et al. 2021)
- https://doi.org/10.1016/S0375-6505(02)00044-5 (Can 2002)
- https://doi.org/10.1016/j.cageo.2019.05.004 (Pérez-Zárate et al. 2019)
- https://doi.org/10.1007/s11053-019-09596-0 (Tut Haklidir & Haklidir 2020)
- https://doi.org/10.1016/j.geothermics.2022.102476 (Varol Altay et al. 2022)
- https://doi.org/10.1016/j.geothermics.2023.102662 (Mordensky et al. 2023)
- https://pubs.usgs.gov/publication/70273870 (DeAngelo, Burns & Mordensky 2026)
- https://doi.org/10.1016/j.geothermics.2017.02.001 (Lautze et al. 2017)
- https://doi.org/10.1002/2016WR019993 (Read et al. 2017, Water Quality Portal) ; https://www.waterqualitydata.us/
- https://www.sciencebase.gov/catalog/item/59d25d63e4b05fe04cc235f9 (USGS Produced Waters Geochemical DB v2.3)
- https://zanskargeothermal.substack.com/p/zanskar-reveals-big-blind-the-discovery
- https://www.thinkgeoenergy.com/zanskar-validates-ai-based-discovery-method-with-drilling-at-pumpernickel-geothermal-site-nevada/
- https://www.zanskar.com/news
