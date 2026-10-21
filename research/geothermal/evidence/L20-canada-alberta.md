# L20: Canadian geothermal (Alberta tenure and well data, Saskatchewan DEEP, BC, Eavor-Lite): literature review

**Method note:** The shared WebSearch budget for this run ran out before this agent's first query. Everything below comes from direct fetches of known primary URLs: King's Printer statute PDFs, alberta.ca, the AER, the Alberta lease spreadsheet, and Crossref, OpenAlex and Semantic Scholar DOI lookups for abstracts. Items not confirmed in a fetched primary document are marked **(unverified)**. Coverage of Saskatchewan and BC tenure is thinner than coverage of Alberta.

---

## 1. Alberta legal and tenure framework (primary documents read)

**Geothermal Resource Development Act, SA 2020, c G-5.5** (King's Printer consolidation current to June 11, 2025)
- The AER regulates geothermal development "below the base of groundwater protection". Shallow geo-exchange stays with Alberta Environment and Protected Areas.
- Regulations under the Act: Geothermal Resource Development Regulation AR 250/2021, and Geothermal Resource Development Rules AR 116/2022 (amended 2022–2026).
- The Act covers licences for wells and facilities. A licence transfer needs written AER consent, and the Act includes surface access and compensation provisions.
- Source: https://kings-printer.alberta.ca/documents/Acts/G05P5.pdf

**Geothermal Resource Tenure Regulation, AR 251/2021** (made under the Mines and Minerals Act; text read in full)
- **How you get a lease:** apply to the Minister (s.2) with the prescribed application fee and the first year's rental. Leases are issued on a **first-in, first-out basis through the Electronic Transfer System. There is no auction or bonus bid** (alberta.ca).
- **Rights conveyed (s.3):** "the **non-exclusive** right to explore for, develop and recover geothermal resources." The lease grants no minerals.
- **Size (s.4):** at most **9 sections** (about 23.3 km², 5,760 acres) per lease. The Minister sets the boundaries.
- **Term (s.5):** **5-year initial term.** A further **5-year intermediate term** follows if the holder files a geothermal assessment report that shows, in the Minister's opinion, that the lease is "potentially productive."
- **Continuation (s.6):** the productive parts continue **indefinitely**.
- The rental and fee amounts are set in the Mines and Minerals Administration Regulation (AR 262/97). I did not read those amounts **(unverified)**.
- Source: https://kings-printer.alberta.ca/documents/Regs/2021_251.pdf

**Mines and Minerals Act amendments:** the owner of the substance the energy is taken from (minerals, water) has the right to access and use that energy. This means **freehold mineral owners can hold geothermal rights**, not only the Crown. Landowner consent is required before a project proceeds.
- Source: https://www.alberta.ca/geothermal-resource-development

**Lease activity** (alberta.ca monthly tables, totalled by the fetch tool)

| Year | Applications | Leases issued |
|---|---|---|
| 2021 | 1 | 0 |
| 2022 | 74 | 31 |
| 2023 | 28 | 28 |
| 2024 | 17 | 32 |
| 2025 | 3 | 6 |
| 2026 to September | 7 | 0 |
| **Total** | **130** | **97** |

- **Demand peaked in 2022 and has collapsed since.** That is cheap entry: little competition, and no auction.
- The current downloadable lease list has **31 rows**:

| Holder | Leases | Area and zone |
|---|---|---|
| Renewable Geo Resources Ltd. | 16 | W5M, Tp 48–52, R21–26 (west of Edmonton); "to base Leduc" |
| Sprocket Energy Corp. | 8 | W5M, Tp 60–62, R18–20; "to base Beaverhill Lake" |
| 1212843 B.C. Ltd. | 3 | W6M, Tp 67–70; "below base Wabamun" |
| Novus Earth Energy | 2 | not recorded |
| Zest Resources | 1 | not recorded |
| Summation Energy | 1 | not recorded |

- Leases are granted **by stratigraphic zone**, so the same land can be split by depth, as with oil and gas tenure.
- Sources: https://www.alberta.ca/system/files/custom_downloaded_images/energy-list-of-geothermal-leases.xlsx and the map at https://gis.energy.gov.ab.ca/GeoView/geothermal

**AER Directive 089 (Geothermal Resource Development)**
- Current edition effective **Feb 7, 2025**. It replaces the edition of Aug 15, 2022.
- It brings geothermal under the Licensee Management Program (liability estimates and security deposits).
- It sets rules for **converting oil and gas wells to geothermal wells**.
- Source: https://www.aer.ca/regulating-development/rules-and-directives/directives/directive-089

**AER ST37 well list:** every well reported to the AER, through its life cycle. It is a public direct download: Geodatabase 1.23 GB, Excel 170 MB, Shapefile 532 MB.
- The page does not give a well count. The commonly cited figure is more than 450,000 wells drilled in Alberta **(unverified)**.
- Source: https://www.aer.ca/data-and-performance-reports/statistical-reports/st37

---

## 2. Peer-reviewed and government literature (10 sources)

**1. Grasby, Allen, Bell, Chen, Ferguson, Jessop, Kelman, Ko, Majorowicz, Moore, Raymond, Therrien (2012). *Geothermal Energy Resource Potential of Canada*. Geological Survey of Canada Open File 6914.** doi:10.4095/291488
- The national baseline. It compiles and digitises **more than 48 years of Canadian geothermal data**.
- In-place geothermal power exceeds **one million times Canada's electricity consumption**, though only a fraction can be developed.
- It names **the high exploration risk from deep-drilling cost** as the key economic constraint.
- In 2012 Canada had no geothermal power generation.

**2. Majorowicz & Grasby (2010). "Heat flow, depth–temperature variations and stored thermal energy for enhanced geothermal systems in Canada." *J. Geophys. Eng.* 7:232.** doi:10.1088/1742-2132/7/3/002
- New heat-flow maps and depth-temperature maps down to 10 km.
- Temperatures above **150 °C are reachable at less than 5 km** in western and northern Canada.
- Key insight: heat flow alone is not a good predictor. **A thick, low-conductivity sedimentary blanket over moderate heat flow** can match the high-heat-flow Cordillera. That is a non-obvious, multi-variable target, which suits ML.
- The recoverable fraction may be as low as **0.02** of the heat in place.

**3. Gray, Majorowicz & Unsworth (2012). "Investigation of the geothermal state of sedimentary basins using oil industry thermal data: case study from Northern Alberta exhibiting the need to systematically remove biased data." *J. Geophys. Eng.* 9:534.** doi:10.1088/1742-2132/9/5/534
- Evaluates three industry thermal datasets: bottom-hole temperatures (BHT), annual pool pressure tests, and drill-stem tests (DST).
- Shows **large systematic biases** in industry temperature data, which distort gradient maps.
- Once those biases are removed, the data are a usable first screen.
- **This is the core "illegible public data" problem a Terranox-style model would solve.**

**4. Weides, Moeck, Majorowicz, Palombi & Grobe (2013). "Geothermal exploration of Paleozoic formations in Central Alberta." *Can. J. Earth Sci.* 50.** doi:10.1139/cjes-2012-0137
- Study area: a 160 × 200 km block around Edmonton.
- Builds a 3D geological model from **formation tops in about 7,000 AGS wells**, and uses **more than 50,000 core analyses** for porosity and permeability.
- Devonian carbonates average 4.5% porosity (Nisku) to 8.7% (Wabamun). Permeability ranges from 3.5×10⁻¹⁵ m² (Wabamun) to 26×10⁻¹⁵ m² (Leduc).
- The Basal Sandstone Unit reaches **62 °C at 1.8 km and 122 °C at 3.5 km**.
- This shows how deep the open core and log archive goes.

**5. Weides & Majorowicz (2014). "Implications of spatial variability in heat flow for geothermal resource evaluation in large foreland basins: the case of the WCSB." *Energies* 7(4):2573–2594.** doi:10.3390/en7042573
- Heat flow in the WCSB ranges from **30 mW/m² in the south to about 100 mW/m² in the north**.
- **100–210 °C at 3–5 km** in the "hot" regions, which is enough for power.
- Formations shallower than 2 km suit direct use: above 50 °C for warm water, above 70 °C for district heating.
- First regional maps of temperature within each aquifer.

**6. Hofmann, Weides, Babadagli, Zimmermann, Moeck, Majorowicz & Unsworth (2014). "Potential for enhanced geothermal systems in Alberta, Canada." *Energy* 69:578–591.** doi:10.1016/j.energy.2014.03.053
- The abstract is elided by the publisher, so I could not read it. Per the title and author group, it assesses EGS in the Precambrian basement and deep sediments, including heat for oil-sands operations. The detailed conclusions are **(unverified)**.

**7. Banks & Harris (2018). "Geothermal potential of foreland basins: a case study from the WCSB." *Geothermics* 76:74–92.** doi:10.1016/j.geothermics.2018.06.004
- Builds a **workflow for using oil and gas well logs and cores to assess sedimentary geothermal resources** in western Alberta municipal districts.
- Reservoirs lie at **2,500 to more than 5,000 m**, with temperatures from **about 60 to more than 150 °C**.
- Estimated capacity: **about 6,100 MWt, or about 1,150 MWe, over 30 years**. About **800 MWe of that is high-grade (above 120 °C)**.
- **This is the most decision-relevant number: about 0.8 GWe of high-grade resource found from existing well data alone, in one region.**

**8. Huang, Hickson, Cotterill & Champollion (2021). "Geothermal assessment of target formations using recorded temperature measurements for the Alberta No. 1 Geothermal Project." *Applied Sciences* 11(2):608.** doi:10.3390/app11020608
- Uses BHTs and wireline logs from **"Alberta's extensive oil and gas database"** in Greenview and Grande Prairie.
- The Beaverhill Lake Group top lies at 3,104–4,094 m, at **87–123 °C**. The Precambrian top lies at 3,205–4,223 m, at 74–124 °C.
- The project needs **120 °C from permeable formations shallower than 4,500 m**.
- Alberta No. 1 (Terrapin Geothermics) has a 5 MW plan and **C$25.45M in federal funding**: https://www.thinkgeoenergy.com/conventional-geothermal-heat-power-project-in-alberta-canada-secures-government-funding/

**9. Ferguson & Grasby (2014). "The geothermal potential of the basal clastics of Saskatchewan, Canada." *Hydrogeology Journal* 22:143–150.** doi:10.1007/s10040-013-1061-5
- The publisher elided the abstract. The paper assesses the Deadwood and Winnipeg basal clastics, the same units DEEP targets. My recollection is that it finds the temperatures modest, with power possible only in the deepest southern areas, and direct use more widely viable **(unverified)**.

**10. Beckers, Rangel-Jurado, Chandrasekar, Hawkins, Fulton & Tester (2022). "Techno-economic performance of closed-loop geothermal systems for heat production and electricity generation." *Geothermics* 100:102318.** doi:10.1016/j.geothermics.2021.102318
- An independent check on Eavor-type closed loops. I could not read the abstract. My recollection is that closed loops are competitive for heat but **electricity is uneconomic at current drilling costs without large cost reductions** **(unverified)**.

---

## 3. Projects and companies

**DEEP Earth Energy Production (Saskatchewan, near Estevan; Williston Basin)**
- Holds about **39,120 ha (about 100,000 acres)** of geothermal rights, and cites potential of **about 200 MW**.
- Completed a **53-day production and injection test (March 2021)**, the first in Canada, and tested a horizontal, hydraulically stimulated well (November 2020). It increased its subsurface rights by **700%** in 2020.
- FEED for a **32 MW** facility was completed in June 2021.
- A **third-party resource review (September 2023)** supports Phases 1–2 for 40 years.
- A **5 MW** pilot was announced in October 2023.
- Funding:
  - **C$25.6M federal** (January 2019).
  - Private placements of **C$5.58M** (February 2021) and **C$4.52M** (July 2021), including C$3M from PHX Energy.
- Its deepest well is about 3.5 km at about 120 °C **(unverified)**.
- **Lesson:** DEEP took the Terranox approach of locking up a large land position early and cheaply, then de-risking it. It has spent more than 10 years and is still pre-commercial.
- Sources: https://deepcorp.ca, https://deepcorp.ca/news/, https://en.wikipedia.org/wiki/Geothermal_power_in_Canada

**Eavor-Lite (Rocky Mountain House, Alberta)**
- Two vertical wells connected by two multilateral legs at **2.4 km depth**. Built from August 2019 to February 2020 and operated 2019–2024.
- Eavor says it was "not intended to be commercially viable." Its goals were to match the thermodynamic model, demonstrate thermosiphon flow, and achieve more than 90% uptime.
- Lateral lengths of about 1.7 km and output figures **(unverified)**.
- Eavor's first commercial project is in **Geretsried, Germany**: drilling started July 2023, and Chubu Electric is a participant.
- **Lesson:** closed-loop technology removes the resource-discovery risk, which shrinks the value of an exploration and ownership model. Its economics depend on drilling cost (see Beckers 2022).
- Source: https://www.eavor.com/eavor-lite/

**Other Alberta projects**
- **Razor Energy / FutEra, Swan Hills:** a 21 MW hybrid of co-produced hot water and gas. Cost C$15–20M, with C$7M in grants. https://www.thinkgeoenergy.com/oil-and-gas-company-seeks-to-establish-the-first-hybrid-geothermal-power-project-in-canada/

**British Columbia**
- **Borealis GeoPower (Valemount):** first BC geothermal permit, June 2018.
- **Fort Nelson First Nation, Clarke Lake:** a mature gas field covering about **6,800 ha in 25 parcels**, with C$1M from NRCan (2019). Its stated advantage is reusing existing exploration data. https://www.thinkgeoenergy.com/permit-given-to-fort-nelson-geothermal-project-in-bc-canada/
- **Meager Creek:** the main volcanic-belt target, planned for green hydrogen rather than grid power. https://meagercreek.ca/
- BC tenure under the Geothermal Resources Act and the BC Energy Regulator **(not verified this run)**.

---

## 4. Key takeaways

1. **The data is excellent and open.**
   - Alberta's AER/AGS archive provides BHTs, DSTs, pool pressure tests, logs, tops (7,000 wells used in a single regional study) and more than 50,000 core analyses.
   - The literature consistently says the raw temperature data are **biased and need systematic correction** (Gray 2012). That is the illegibility a model removes.
2. **The resource is moderate-temperature but large.**
   - 100–210 °C at 3–5 km in hot zones (Weides & Majorowicz 2014).
   - About 800 MWe of high-grade resource in one west-Alberta study (Banks & Harris 2018).
   - These are hot sedimentary aquifers that need binary plants, not high-enthalpy Basin-and-Range systems.
3. **Tenure is cheap, but weak as an ownership right.**
   - Over-the-counter, first-come-first-served leases, no auction, 9 sections maximum, 5 + 5 years, continued indefinitely once producing.
   - But the lease is **non-exclusive** and zone-specific. Freehold mineral and water owners also hold energy rights.
   - Demand has collapsed: 3 applications in 2025.
4. **Commercial proof is thin.**
   - Canada still has no grid-scale geothermal plant (unverified as of October 2026).
   - DEEP, Alberta No. 1 and Razor have each taken 5–10 years and C$25M-scale grants.

---

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

**Where the shape fits**

- **The data asset is the closest analogue to the Saskatchewan Mineral Assessment Database.**
  - Hundreds of thousands of public, legible-but-messy well records with bias-prone BHT and DST data.
  - A decade of academic work (Gray, Weides, Banks & Harris, Huang) shows the signal is there but has only been mapped regionally and by hand.
  - A model that corrects BHTs, predicts temperature and permeability by formation, and ranks 9-section blocks has room to show a strong lift.
- **Acquisition is cheap and uncontested.**
  - Leases are first-come-first-served, with no bonus bidding. Applications fell from 74 in 2022 to 3 in 2025.
  - A company can stake many zone-specific leases before showing they have value. An assessment report that proves "potentially productive" adds 5 years, so **the proof step is written into the tenure**. That fits the Terranox step-up model well.
- **Exit buyers exist.** Eavor, DEEP-type developers, oil and gas operators (Razor/FutEra, Sprocket) and Alberta's large data-centre power demand **(unverified that this is a confirmed load)**.

**Risks that cap the shape**

1. **Non-exclusive tenure** (s.3): exclusivity has to come from the zone, from surface position or from licences, so ownership is weaker than with a mineral claim.
2. **Moderate temperatures** (mostly 80–150 °C) mean binary-cycle economics and lower value per MW.
3. **Closed-loop and EGS technology** (Eavor, Fervo-type) works without finding a natural aquifer, which reduces the scarcity value of the right.

None of these kills the shape. Together they argue for **Canada as a second jurisdiction, not the beachhead**, unless the thesis is co-produced or repurposed-well heat, which uses Directive 089's well-conversion rules.

**Gap vs Zanskar**

- Zanskar applies AI to US Great Basin data, mostly on BLM and federal land, aimed at blind hydrothermal systems (Big Blind) and buying plants (Lightning Dock).
- **Zanskar has no visible presence in Canadian sedimentary basins** (unverified; no Zanskar lease appears among the 31 rows in Alberta's lease list).
- Concretely, the gaps are:
  - (a) **the WCSB and Williston basins**, which have denser well data than Nevada, where Zanskar has to drill its own temperature-gradient holes;
  - (b) **over-the-counter staking** instead of BLM competitive lease sales, where Zanskar has to bid publicly and is visible;
  - (c) **freehold and Saskatchewan subsurface rights**, which can be bought privately and quietly.
- A Terranox-style company could be the "Zanskar of sedimentary basins": model hundreds of thousands of oil and gas wells, stake the best zone leases at near-zero cost, prove "potentially productive" with an assessment report, and sell blocks to developers. The weak points are non-exclusivity and low-temperature economics.

---

## Sources

- Geothermal Resource Development Act (Alberta King's Printer): https://kings-printer.alberta.ca/documents/Acts/G05P5.pdf
- Geothermal Resource Tenure Regulation, AR 251/2021: https://kings-printer.alberta.ca/documents/Regs/2021_251.pdf
- Alberta geothermal resource development page and lease tables: https://www.alberta.ca/geothermal-resource-development
- Alberta lease list (spreadsheet): https://www.alberta.ca/system/files/custom_downloaded_images/energy-list-of-geothermal-leases.xlsx
- Alberta geothermal map: https://gis.energy.gov.ab.ca/GeoView/geothermal
- AER Directive 089: https://www.aer.ca/regulating-development/rules-and-directives/directives/directive-089
- AER ST37 well list: https://www.aer.ca/data-and-performance-reports/statistical-reports/st37
- Grasby et al. 2012 (GSC Open File 6914): https://doi.org/10.4095/291488
- Majorowicz & Grasby 2010: https://doi.org/10.1088/1742-2132/7/3/002
- Gray, Majorowicz & Unsworth 2012: https://doi.org/10.1088/1742-2132/9/5/534
- Weides et al. 2013: https://doi.org/10.1139/cjes-2012-0137
- Weides & Majorowicz 2014: https://doi.org/10.3390/en7042573
- Hofmann et al. 2014: https://doi.org/10.1016/j.energy.2014.03.053
- Banks & Harris 2018: https://doi.org/10.1016/j.geothermics.2018.06.004
- Huang et al. 2021: https://doi.org/10.3390/app11020608
- Ferguson & Grasby 2014: https://doi.org/10.1007/s10040-013-1061-5
- Beckers et al. 2022: https://doi.org/10.1016/j.geothermics.2021.102318
- DEEP Earth Energy: https://deepcorp.ca and https://deepcorp.ca/news/
- Eavor-Lite: https://www.eavor.com/eavor-lite/
- Geothermal power in Canada (Wikipedia, secondary): https://en.wikipedia.org/wiki/Geothermal_power_in_Canada
- Alberta No. 1 funding (ThinkGeoEnergy): https://www.thinkgeoenergy.com/conventional-geothermal-heat-power-project-in-alberta-canada-secures-government-funding/
- Razor Energy Swan Hills (ThinkGeoEnergy): https://www.thinkgeoenergy.com/oil-and-gas-company-seeks-to-establish-the-first-hybrid-geothermal-power-project-in-canada/
- Clarke Lake permit (ThinkGeoEnergy): https://www.thinkgeoenergy.com/permit-given-to-fort-nelson-geothermal-project-in-bc-canada/
- Meager Creek: https://meagercreek.ca/
