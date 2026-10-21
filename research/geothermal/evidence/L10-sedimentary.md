# L10: Sedimentary geothermal / hot sedimentary aquifers (HSA): literature review

Scope: US Gulf Coast, Williston, Permian/Delaware, Denver-Julesburg (DJ), Alberta and Western Canada Sedimentary Basin (WCSB), resource-size papers, Project InnerSpace GeoMap, and reservoir-quality data from oil and gas wells. The review asks one question: is there a "Terranox-shape" opportunity in sedimentary basins, where public oil and gas well data is plentiful but hard to read and Zanskar is not playing?

Access note: nrel.gov and research-hub.nrel.gov failed DNS from this sandbox, and the Springer site redirected to a login. For those sources I used abstracts quoted in search results, and I flag them where relevant.

---

## 1. Primary-source summaries

### 1. Gardner & Birdwell (USGS), 2023. "Hidden system identification: Basin modeling as a tool for examining sedimentary geothermal resource potential." GRC Transactions v.47, pp. 1407-1414
- Built a PetroMod 3D basin model of the **onshore US Gulf Coast covering >500,000 km²**. It is calibrated to **corrected bottom-hole temperatures (BHTs) from >6,000 wells**, plus structural surfaces and lithology.
- Result: **>400,000 km² of moderate-to-high-temperature resource (90-150 °C and >150 °C) at <6 km depth**.
- The authors state the motivation directly: sedimentary systems "lack surface manifestations", and older work used naive linear extrapolation that ignored lithology-dependent conductivity and compaction. They describe the maps as first-order screening only. Pressure and porosity calibration is listed as future work.
- Relevance: the USGS has itself shown that legacy O&G data plus basin modelling can reveal "hidden" sedimentary heat. The permeability layer, which is what actually decides commerciality, is still left open.
- https://pubs.usgs.gov/publication/70271309

### 2. Birdwell, Gardner, Kinney, Petermann, Sullivan, Clement, Hagadorn & Eaton (USGS / DMNS / Mines), 2024. "A Preliminary Analysis of Geothermal Resources in the Denver-Julesburg Basin Evaluated using 3D Basin Modeling." AAPG Rocky Mountain Section
- **>20,000 BHTs from 2,000-20,000 ft**, corrected with a basin-specific Förster-type model. Corrected temperatures run **130-436 °F (54-224 °C)**, and the deepest wells reach about 24,000 ft.
- Heat flow is highly elevated in the Wattenberg field. In the Colorado Mineral Belt area, the **≥194 °F (90 °C) resource can be as shallow as 4,000 ft, and ≥302 °F (150 °C) as shallow as 7,000 ft**. Much of the rest of the basin may have no high-temperature resource in its sedimentary units.
- Caution on reservoir quality: pyrite and alteration geochemistry shows that hydrothermal fluid-rock interaction may have **degraded permeability in the Permian Lyons Sandstone** as recently as the late Miocene. The authors suggest EGS or closed-loop approaches where permeability is limited.
- https://www.searchanddiscovery.com/abstracts/pdf/2024/91208rms/abstracts/ndx_birdwell02.pdf

### 3. Mibei, Gold, Kolker, Dayo & Beckers (NREL), 2024. "Geothermal Reservoir Characterization at Wattenberg Area in Denver Basin." Geothermal Rising poster (abstract via search, PDF host unreachable)
- Estimated BHTs of about 160 °C imply a **gradient of ~62 °C/km and >200 °C at ~3 km**. The anomaly sits between the Lafayette and Longmont wrench-fault zones and lines up with a vitrinite-reflectance anomaly.
- Companion modelling (Akindipe et al., 2024) puts closed-loop laterals at 6 km, where temperatures approach 300 °C.
- Counterpoint: Morgan et al. (Colorado Geological Survey, 2009) found Wattenberg *not* anomalous on a new state gradient map. **Data interpretation alone moves the conclusion.** That is a direct argument that an ML/BHT-correction edge matters.
- https://nrel.gov/docs/fy25osti/90541.pdf ; https://nrel.gov/docs/fy25osti/90798.pdf ; https://www.searchanddiscovery.com/abstracts/html/2009/annual/abstracts/morgan04.htm

### 4. Crowell & Gosnold (UND), 2015. "Integrating geophysical data in GIS for geothermal power prospecting." Geosphere (GSA), sedimentary-basin themed issue
- A GIS favourability screen of the DJ, Williston and Michigan/Illinois-area counties. It ranks the **DJ Basin (about 155,000 km²) highest for "large-scale, economically feasible geothermal power"**.
- It notes that DJ operators produce about **7 bbl of hot water per bbl of hydrocarbon**.
- https://www.thinkgeoenergy.com/new-research-describes-large-geothermal-potential-in-wyoming-nebraska-and-colorado/

### 5. Gosnold and co-workers (UND), Williston Basin, 2011-2025
- Early heat-in-place estimates were **~10^20 J, "several GW" of electrical potential**. Gosnold & Crowell later showed the basin's water-to-oil ratio is only **1.22:1**. That gives co-produced potential of just **~3 MW (Madison) and ~4 MW (Red River) unitised fields**, "several orders of magnitude less than earlier estimates" (https://www.searchanddiscovery.com/abstracts/html/2013/90169rms/abstracts/gosn.htm).
- Mann & Gosnold's 2017 final report to the ND Industrial Commission finds **4.0 × 10^19 J available, or 1.36 × 10^9 MWh** by binary ORC. It notes that much of the needed infrastructure already exists as abandoned O&G wells (https://ndic.nd.gov/sites/www/files/documents/Renewable-Energy-Program/Grant-Rounds--Final-Reports/Approved-Projects/Grant-Rounds-29-20/FR-R-21-30.pdf).
- Geothermal aquifers sit at 3.0-4.5 km. The Red River and the Cambro-Ordovician Deadwood are the deepest and hottest.
- Lesson: **heat-in-place numbers are enormous, but deliverable power is set by flow and transmissivity, not heat**. Co-production rides on oil-field water cut. Purpose-built doublets or horizontal wells are needed for scale.

### 6. DEEP Earth Energy Production (Saskatchewan, Williston/Deadwood), 2019-2023: company releases and federal funding
- DEEP drilled Saskatchewan's deepest well, **3,530 m to the Precambrian**. A production/injection loop (Border-3 to Border-1) has run since July 2020 and delivers **~122 °C brine from ~3,500 m**, with the pump at 2,800 m. A second well, Border-4, about 7 km west, flowed similarly.
- The plant design uses **10 horizontal wells (6 producers, 4 injectors) for 20 MW** of ORC. The plan is phased, 5 MW then +20 MW, with a vision of **160 MW**.
- Funding: **C$25.6M federal (NRCan) toward a C$51.3M project**, plus small private placements (C$4.5M). Schedules have slipped. A 2023 report said the 20 MW phase was not fully financed.
- Tenure: secured through a **Saskatchewan "lease of space"** covering the top of the Winnipeg Formation to the base of the Deadwood. It runs **15 years, renewable 15**, while producing power. DEEP also won a subsurface-mineral permit block for brine minerals such as lithium.
- Relevance: this is **proof that the HSA play works in Terranox's home province**, and that tenure is obtainable by disposition.
- https://www.thinkgeoenergy.com/successful-tests-allow-deep-to-plan-20-mw-geothermal-power-plant-in-saskatchewan/ ; https://www.on-sitemag.com/construction/feds-fund-countrys-first-geothermal-electricity-plant-51-3m-project-will-create-100-construction-jobs/1003961819/ ; https://www.thinkgeoenergy.com/saskatchewan-geothermal-project-secures-mineral-rights-for-brine-from-wells/

### 7. Majorowicz & Weides, 2014. "Implications of spatial variability in heat flow for geothermal resource evaluation in large foreland basins: the case of the WCSB." Energies 7(4):2573-2594, doi:10.3390/en7042573
- Heat-flow and gradient maps across the WCSB, built from the large BHT/DST database. The mean sedimentary gradient is about 33 °C/km, ranging **20-55 °C/km**, and rises east to west. That gradient figure comes from a secondary citation in a Solid Earth comment: https://se.copernicus.org/preprints/se-2017-129/se-2017-129-SC1.pdf.
- Companion WGC 2015 work (Weides, Moeck, Majorowicz, Schmitt) found the Cambrian Basal Sandstone near Edmonton is only **~78-93 °C**, which suits heat rather than power.
- https://ideas.repec.org/a/gam/jeners/v7y2014i4p2573-2594d35347.html ; https://gfzpublic.gfz-potsdam.de/pubman/item/item_1193892_2/component/file_1193891/16051_Weides%20et%20al._Geothermal%20Assessment.pdf

### 8. Huang, Gosnold, Hickson & Benoit, 2020. "Using Oil and Gas Data to Assess Geothermal Resources Within the WCSB in Alberta." GRC Transactions v.44 (Alberta No. 1)
- **>500,000 O&G wells** have been drilled in Alberta, and the WCSB covers more than 1.4 million km². BHTs are mostly "single, unequilibrated" end-of-completion readings pulled from geoSCOUT.
- Economic threshold for the 5 MWe Alberta No. 1 project: **≥120 °C at ≤4,500 m**. They screened nine areas, including Swan Hills, Edson, Whitecourt and Rainbow Lake.
- Key quantitative warning: in a Williston well, extrapolating the shallow gradient predicts **~150 °C at 2,740 m against a measured 121 °C, a 30 °C error** that can make a project look viable when it is not.
- They argue that sedimentary geothermal exploration "has more in common with oil and gas exploration than with normal geothermal exploration": the hot water is "essentially everywhere below a target isotherm", and the real search is for **temperature × permeability**, with no surface manifestations.
- https://www.albertano1.ca/_files/ugd/b03f95_bce54336c0cc40f9a687718c0c503d11.pdf

### 9. Banks (ed.), Harris et al. (Univ. of Alberta / Alberta Innovates), 2022. "Geothermal Power from Co-Produced Fluids and Hydrocarbon Reservoirs Throughout the WCSB," final report (C$2.85M, 3 years, 16 peer-reviewed papers)
- **480 active Alberta fields**. Field-average temperatures run 25-126 °C, depths 1,520-4,578 m, and gradients 8-44 °C/km. **Only 20 fields exceed 95 °C**, the cold-climate minimum for power. 66% of geoSCOUT wells are 1-2 km TVD, and only 0.1% are deeper than 5 km.
- Earlier Banks & Harris (2018) "Deep Dive" across the Leduc, Swan Hills, Granite Wash and Gilwood: **~6,200 MWt and ~1,150 MWe (30-year)** in the participating municipalities, with more than 50% in the Hinton area.
- Virginia Hills (Swan Hills reef) case study: heat-in-place gives **29.9 ± 13 MWe**, or 1.71 MWe/km³. The **wellhead method gives only ~16 MWe** from 190 suspended wells, averaging **0.085 MWe per well**. The **heat-in-place method overstates by ~7×** because flow varies so much from well to well, and only a few wells are good. Of 190 wells, 53 exceed 100 kWe.
- Brine TDS runs 7 g/L (Leduc) to 345 g/L (Granite Wash). The main geochemical risk is calcite scaling, which is manageable.
- Retrofitting a gas well as a geothermal slim hole costs about C$75k, roughly **an order of magnitude cheaper than drilling a new 4.5 km well**.
- https://albertainnovates.ca/wp-content/uploads/2022/06/Geothermal-Power-from-Co-Produced-Fluids-and-Hydrocarbon-Reservoirs-Final-Report.pdf

### 10. Augustine & Falkenstern (NREL), 2014. "An Estimate of the Near-Term Electricity-Generation Potential of Coproduced Water from Active Oil and Gas Wells." SPE Journal (SPE-163142-PA). Abstract only
- A GIS of **2.5 million wells (~0.5 million active)** cross-referenced with temperature maps. Near-term market potential is only **~300 MWe** with marginal economics, against DOE's 2008 theoretical >5,000 MW.
- The UT "Future of Geothermal in Texas" report (ch. 3) cites this and concludes that **converting or repurposing wells and purpose-drilled sedimentary development beat co-production**.
- https://research-hub.nrel.gov/en/publications/estimate-of-the-near-term-electricity-generation-potential-of-cop/ ; https://repositories.lib.utexas.edu/bitstream/handle/2152/117192/Chapter3.pdf

### 11. Porro, Esposito, Augustine et al. (NREL), 2012. "An Estimate of Geothermal Energy Resource in Major US Sedimentary Basins" (GRC). Abstract only, PDF unreachable
- Volumetric heat-in-place (USGS Muffler method) for **15 basins**: Anadarko, Bighorn, Denver, Fort Worth, Great Basin, Green River, Hanna, Permian/Delaware, Powder River, Raton, Sacramento, San Joaquin, Uinta, Williston and Wind River.
- A later NREL (2020) report took Nevada, Utah, Colorado and Texas forward as having "attractive reservoir characteristics". Wyoming and Louisiana were dropped for low gradients.
- GeoVision (2019) cites up to **7.5 million GWh of heat** from these resources. The basin-level MWe figures are (unverified) here.
- https://research-hub.nrel.gov/en/publications/estimate-of-geothermal-energy-resource-in-major-us-sedimentary-ba/ ; https://nrel.gov/geothermal/resource-assessment-mapping.html

### 12. Gulf Coast geopressured: DOE/BEG Pleasant Bayou (1979-1994) and NREL 2012 recoverable estimate
- Pleasant Bayou (Brazoria Co., TX) flowed **20,000 bbl/d of 291 °F (144 °C) brine with ~23 scf/stb gas** (1989). It ran a **~1 MWe hybrid (gas plus heat) plant** that sold power to Houston Lighting & Power. DOE called the technology feasible but only marginally economic because of low temperatures.
- NREL (2012, NREL/PR-6A20-54999) defines the resource as >212 °F brine with a >0.7 psi/ft gradient and estimated the recoverable resource for identified Texas and Louisiana sites. Total gas-in-place estimates for the geopressured Tertiary have historically ranged **3,000-100,000 Tcf**, which shows how unconstrained the numbers are.
- https://www.searchanddiscovery.com/abstracts/html/1989/annual/abstracts/0368a.htm ; https://www.osti.gov/biblio/893428 ; https://www.osti.gov/biblio/1041361

### 13. Permian / Delaware & Val Verde
- An eight-county West Texas assessment (DOE-related) compiled **>8,000 temperature-depth records**, with BHTs of **120-180 °C** in deep Delaware and Val Verde wells (https://corpora.tika.apache.org/base/docs/govdocs1/291/291718.html).
- A UT thesis on Pecos County used 947 NGDS points to model **maximum temperatures of 195 °C at 3.5 km and 213 °C at 5 km** (https://repositories.lib.utexas.edu/items/01be6734-86ac-4892-a3f2-1c5e362b3409).
- The deep Delaware is known for "BHTs in excess of 150 °C" and deep gradients of 30 °C/km or more (https://archives.datapages.com/data/west-texas-geological-society/other-publications/004/004112/19_wtgs0040019.htm).
- The Permian also has the largest produced-water volumes in the US, and the oil-field disposal formations double as characterised injection targets (unverified quantification).

### 14. Project InnerSpace / UT Austin et al., 2023. "The Future of Geothermal in Texas" and GeoMap (2023-2025)
- A five-university report (Beard, Jones, Webber, Wisian, Young et al., January 2023, updated May 2023). It finds Texas subsurface heat "many thousands of times" what the state needs, and a map at 6.5 km shows much of Texas at or near the minimum temperature for power. A 2013 assessment based on **>50,000 BHTs** put Texas extractable energy at more than 2 trillion boe.
- GeoMap Beta launched 1 December 2023 at COP28, built with Google: "dozens" of datasets, Africa first. **GeoMap North America launched 4 June 2024 with >150 surface and subsurface layers, free to use.** It includes US isotherm-depth layers (e.g. depth to 200 °C) and ranks opportunities by transmission distance and heat and power demand. Later modules cover South America (with Petrobras well data, e.g. about 1,200 GW claimed for Argentina) and Oceania (about 1,600 GW claimed for Australia).
- Implication: **regional, coarse temperature-at-depth screening is now free and commoditised.** Any edge has to come from well-by-well data, permeability, and land.
- https://energy.utexas.edu/research/geothermal-texas ; https://repositories.lib.utexas.edu/bitstream/handle/2152/117244/FutureGeothermalTexasExecutiveSummary.pdf ; https://www.thinkgeoenergy.com/project-innerspace-launches-geomap-geothermal-prospecting-tool-for-north-america/ ; https://www.thinkgeoenergy.com/project-innerspace-launches-geomap-beta-geothermal-exploration-tool/

### 15. ML on oil and gas BHT data: Shahdi et al., 2021, Geothermal Energy (Springer), doi:10.1186/s40517-021-00200-4
- "Exploratory analysis of machine learning methods in predicting subsurface temperature and geothermal gradient", based on Appalachian-basin O&G well BHTs. **XGBoost and Random Forest gave the highest accuracy**, trained on corrected BHT labels (exact RMSE unverified; full text paywalled).
- Static-formation-temperature ML studies report that the Horner correction overestimates, while RF and kNN beat ANN (https://www.researchsquare.com/article/rs-131433/v1).
- https://geothermal-energy-journal.springeropen.com/articles/10.1186/s40517-021-00200-4/tables/1

---

## 2. Tenure and land regimes: where a cheap right can be bought before proof

| Jurisdiction | Who owns geothermal | How to acquire | Cost signal |
|---|---|---|---|
| **Texas** (SB 785, effective 18 June 2023) | **Surface estate owner** (even where minerals are severed), unless a contract says otherwise; dissolved minerals and hot brines are excluded | Private leases from surface owners; GLO for PSF lands | GLO El Paso tracts: **10-year primary term, $3/acre delay rental, 10% gross royalty**; Ormat's first state lease was about **$5/acre** |
| **Alberta** (Geothermal Resource Development Act, in force December 2021; Tenure Reg. 1 January 2022) | Rights go with owners of the substance (mostly Crown); landowner consent is required | Crown geothermal lease, **first-in-first-out** (no auction) | **C$625 application fee + C$3.50/ha first-year rental** |
| **Saskatchewan** | Crown subsurface; no dedicated geothermal act yet | "Lease of space" by formation interval (DEEP: 15+15 years) plus subsurface-mineral permits for brine | (unverified) |
| **US federal (BLM)** | Federal | Competitive geothermal lease sales | This is Zanskar's and Ormat's turf in Nevada and Utah |

Sources: https://capitol.texas.gov/tlodocs/88R/billtext/html/SB00785E.htm ; https://www.thinkgeoenergy.com/new-texas-legislation-defines-ownership-of-geothermal-energy/ ; https://www.thinkgeoenergy.com/texas-oil-gas-and-geothermal-lease-sale-nov-2-2022/ ; https://www.bennettjones.com/Blogs-Section/Geothermal-Resource-Development-Alberta-Energy-Issues-Guidance-for-Obtaining-Leases ; https://alberta.ca/geothermal-resource-development ; https://cascadeinstitute.org/wp-content/uploads/2025/06/Groundwork-FINAL.pdf

---

## 3. Cross-cutting findings

1. **The data is huge, public and messy.** Sources include >500k Alberta wells, 2.5M US wells, >6,000 calibration wells for one Gulf Coast model and >20,000 BHTs in the DJ. The BHTs are single and unequilibrated, and corrections disagree by **5-30 °C**. Wattenberg is called a hot spot by NREL but not anomalous by the CGS. Interpretation decides outcomes, which is the Terranox pattern.
2. **Temperature is solved and commoditised at the regional scale** (USGS PetroMod models, GeoMap's free isotherm layers). **Permeability and transmissivity are the binding constraint.** Heat-in-place overstates deliverable power by about 7× (Virginia Hills) to "orders of magnitude" (Williston co-production). Reservoir quality can be degraded by diagenesis (Lyons Sandstone).
3. **Reservoir-quality data sits in the same O&G archives.** That means core porosity and permeability, DSTs, production and water-cut histories, injection-well records, and logs, for example from Texas RRC, NDIC, AER/geoSCOUT and Saskatchewan IPDS (unverified for IPDS access). Almost none of the cited studies jointly model temperature, permeability and flow at the well level across a basin. Banks et al. did it for one field.
4. **Economic thresholds:** ≥120 °C at ≤4.5 km (Alberta No. 1), ≥95 °C cold-climate ORC minimum, and 150 °C for "high-temperature" in USGS cut-offs. The hot pockets are the Delaware/Val Verde at 120-180 °C, the DJ/Wattenberg at 160-200 °C at about 3 km, the Gulf Coast geopressured zone at 144 °C or more, Alberta's west/Hinton/Swan Hills, and the Williston Deadwood/Red River at about 120 °C at 3.5 km.
5. **Unit sizes are modest:** DEEP plans 5-25 MW per site. Virginia Hills is about 16-30 MWe. Alberta's Deep Dive found about 1,150 MWe across several municipalities. Scale comes from portfolios of many 10-50 MW sites and from direct heat, not from single 100 MW finds. This is a real "too small" risk at the asset level, mitigated by portfolio and by EGS/closed-loop upside on the same land.

---

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

- **Zanskar's lane** is Basin-and-Range *hydrothermal* (fault-hosted, blind convective systems such as Big Blind in Nevada at >100 MW claimed), bought mostly through **BLM competitive lease sales** in the western US. It raised a $115M Series C to build plants. No source found shows Zanskar targeting sedimentary basins (https://esgnews.com/zanskar-raises-115-million-to-scale-ai-driven-geothermal-discovery-and-power-plant-development/).
- **The gap:** sedimentary basins on private and provincial land (Texas, the Williston in ND/SK, Alberta/WCSB, the DJ) where:
  1. the data is *oil and gas* data (BHTs, DSTs, core perm, water cut, injection logs), which hydrothermal-trained models do not use;
  2. tenure is **cheap, non-competitive or first-come**: Alberta FIFO at C$3.50/ha, Texas surface-owner leases at single-digit $/acre after SB 785, and Saskatchewan formation-interval leases;
  3. the market has priced in "it's everywhere but too cool". The **right answer is to find the few permeable, hot fairways** (the top 53 of 190 wells; Hinton; Wattenberg; the deep Delaware) and lock them up first.
- **Terranox-native wedge:** Saskatchewan and the Williston. These are the same provincial tenure system, the same regulators, and the same data-wrangling muscle (assessment files ↔ well files). DEEP has proven 122 °C and commercial flow in the Deadwood but holds only one area. A model that ranks *temperature × transmissivity × existing wellbores* across SK, ND, Alberta and Texas, then files leases or leases of space ahead of proof, is a direct analogue.
- **Monetisation:** sell proven tracts to Fervo/Sage/Eavor-type developers, oil majors moving into geothermal, or data-centre offtakers in ERCOT and Alberta. Alternatively, develop small ORC plants. Optionality sits on the same acreage: **lithium/brine minerals** (DEEP already holds brine-mineral permits, but Texas SB 785 excludes brines from the geothermal right, so they need separate tenure), plus EGS or closed-loop at depth.
- **Risks to score honestly:**
  - Per-site MW are small (5-30 MW).
  - Permeability uncertainty is the dominant risk, and the ML must predict flow, not just temperature.
  - GeoMap has commoditised free regional screening, so the moat must be well-level reservoir-quality models plus land.
  - Texas surface-owner fragmentation makes aggregation laborious, though that is also why it is cheap.
  - Lithium buyers may compete for brine-rich acreage (unverified).
- **Bottom line:** the asset-owning HSA play is plausible and clearly differentiated from Zanskar's BLM hydrothermal strategy. The literature supports the idea that the edge sits in *permeability-aware* reinterpretation of O&G archives, and that is exactly where the current public tools stop.

---

## Sources
- https://pubs.usgs.gov/publication/70271309
- https://www.searchanddiscovery.com/abstracts/pdf/2024/91208rms/abstracts/ndx_birdwell02.pdf
- https://nrel.gov/docs/fy25osti/90541.pdf
- https://nrel.gov/docs/fy25osti/90798.pdf
- https://www.searchanddiscovery.com/abstracts/html/2009/annual/abstracts/morgan04.htm
- https://www.thinkgeoenergy.com/new-research-describes-large-geothermal-potential-in-wyoming-nebraska-and-colorado/
- https://www.searchanddiscovery.com/abstracts/html/2013/90169rms/abstracts/gosn.htm
- https://ndic.nd.gov/sites/www/files/documents/Renewable-Energy-Program/Grant-Rounds--Final-Reports/Approved-Projects/Grant-Rounds-29-20/FR-R-21-30.pdf
- https://www.thinkgeoenergy.com/successful-tests-allow-deep-to-plan-20-mw-geothermal-power-plant-in-saskatchewan/
- https://www.on-sitemag.com/construction/feds-fund-countrys-first-geothermal-electricity-plant-51-3m-project-will-create-100-construction-jobs/1003961819/
- https://www.thinkgeoenergy.com/saskatchewan-geothermal-project-secures-mineral-rights-for-brine-from-wells/
- https://ideas.repec.org/a/gam/jeners/v7y2014i4p2573-2594d35347.html
- https://gfzpublic.gfz-potsdam.de/pubman/item/item_1193892_2/component/file_1193891/16051_Weides%20et%20al._Geothermal%20Assessment.pdf
- https://se.copernicus.org/preprints/se-2017-129/se-2017-129-SC1.pdf
- https://www.albertano1.ca/_files/ugd/b03f95_bce54336c0cc40f9a687718c0c503d11.pdf
- https://albertainnovates.ca/wp-content/uploads/2022/06/Geothermal-Power-from-Co-Produced-Fluids-and-Hydrocarbon-Reservoirs-Final-Report.pdf
- https://research-hub.nrel.gov/en/publications/estimate-of-the-near-term-electricity-generation-potential-of-cop/
- https://repositories.lib.utexas.edu/bitstream/handle/2152/117192/Chapter3.pdf
- https://research-hub.nrel.gov/en/publications/estimate-of-geothermal-energy-resource-in-major-us-sedimentary-ba/
- https://nrel.gov/geothermal/resource-assessment-mapping.html
- https://www.searchanddiscovery.com/abstracts/html/1989/annual/abstracts/0368a.htm
- https://www.osti.gov/biblio/893428
- https://www.osti.gov/biblio/1041361
- https://corpora.tika.apache.org/base/docs/govdocs1/291/291718.html
- https://repositories.lib.utexas.edu/items/01be6734-86ac-4892-a3f2-1c5e362b3409
- https://archives.datapages.com/data/west-texas-geological-society/other-publications/004/004112/19_wtgs0040019.htm
- https://energy.utexas.edu/research/geothermal-texas
- https://repositories.lib.utexas.edu/bitstream/handle/2152/117244/FutureGeothermalTexasExecutiveSummary.pdf
- https://www.thinkgeoenergy.com/project-innerspace-launches-geomap-geothermal-prospecting-tool-for-north-america/
- https://www.thinkgeoenergy.com/project-innerspace-launches-geomap-beta-geothermal-exploration-tool/
- https://geothermal-energy-journal.springeropen.com/articles/10.1186/s40517-021-00200-4/tables/1
- https://www.researchsquare.com/article/rs-131433/v1
- https://capitol.texas.gov/tlodocs/88R/billtext/html/SB00785E.htm
- https://www.thinkgeoenergy.com/new-texas-legislation-defines-ownership-of-geothermal-energy/
- https://www.thinkgeoenergy.com/texas-oil-gas-and-geothermal-lease-sale-nov-2-2022/
- https://www.bennettjones.com/Blogs-Section/Geothermal-Resource-Development-Alberta-Energy-Issues-Guidance-for-Obtaining-Leases
- https://alberta.ca/geothermal-resource-development
- https://cascadeinstitute.org/wp-content/uploads/2025/06/Groundwork-FINAL.pdf
- https://esgnews.com/zanskar-raises-115-million-to-scale-ai-driven-geothermal-discovery-and-power-plant-development/
