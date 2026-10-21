# D01 - Texas Railroad Commission (RRC) well records as a geothermal data source

Topic: what the RRC (plus BEG and TWDB) actually holds, how much of it is digitised, how it can be accessed in bulk, where temperature lives inside it, and how illegible it is.

Method note: the shared WebSearch budget for this run was used up before this agent began, so this file is built from **direct fetches of primary pages** (RRC, BEG, TWDB, SMU, DOE GDR, Cornell LII copy of the Texas Administrative Code) and from **parsing two RRC technical manuals locally**. The UT Austin repository holding *The Future of Geothermal in Texas* (2023) returned HTTP 503 on every attempt, so numbers from that report are not cited here. Anything not checked against a fetched source is marked (unverified).

---

## 1. Scale: how many wells

- **431,492 oil and gas wells are monitored by the RRC as of 31 Aug 2026**: 273,371 active and 158,121 inactive. Active wells: 155,036 producing oil, 82,573 producing gas, 28,760 injection/disposal, 35,762 service, 6,012 other, and 990 storage/brine. Among inactive wells, 7,639 + 4,678 have operators whose P-5 has been delinquent for more than 12 months (an orphan pipeline). Source: RRC "Wells Monitored by the Railroad Commission, As of August 31, 2026" (PDF parsed locally). https://www.rrc.texas.gov/media/pp4jbxif/august-2026.pdf
- These are *currently monitored* wells only. The full historical wellbore population is much larger. It includes plugged wells and dry holes, and pre-API wells carry "dummy API numbers" in the Full Wellbore file (field `WB-DUMMY-API-NUMBER`). Commonly cited figures for total wells ever drilled in Texas are ">1 million" (unverified; not confirmed against a fetched source in this run).
- **Physical log archive: about 1.5 million logs** at the Bureau of Economic Geology (BEG) Geophysical Log Facility. The collection combines the RRC log collection, industry donations and BEG research logs. The BEG has cared for RRC logs since a 1985 requirement. https://www.beg.utexas.edu/about/facilities/geophysical-log-facility

Read-across: Texas probably has the largest pool of deep "free" boreholes of any US state. The Saskatchewan Mineral Assessment Database (SMAD) analogue that Terranox uses has roughly 10^4 reports. Texas has about 10^6 boreholes with about 1.5M log images.

## 2. What is digitised, and in what form

### 2a. Structured (machine-readable) data. Free and bulk.
RRC "Data Sets Available for Download" (all free, served via `mft.rrc.texas.gov`): https://www.rrc.texas.gov/resource-center/research/data-sets-available-for-download/

| Dataset | Format | Cadence | Geothermal relevance |
|---|---|---|---|
| Full Wellbore | EBCDIC and ASCII (legacy mainframe tape layout) | Weekly | API, total depth, casing, perfs, formation-at-completion depth, plugging. **No temperature field** |
| Wellbore Query Data | ASCII | Monthly | Index |
| Statewide API Data | ASCII and dBase | Twice weekly | API, lease, completion and plug dates |
| Well Layers by County (Digital Map Data) | Shapefile | Twice weekly | Well locations |
| Drilling permit master/trailer (with lat/long) | ASCII | Nightly/monthly | Locations, permitted depth |
| **Completion Information in Data Format** | ASCII | **Nightly** | Packets for G-1, W-2, P-4, G-5, G-10, P-15, W-12 and **L-1** submitted or approved the previous day |
| Imaged Completion Files | PDF/TIFF | Nightly | Attachments |
| Directional Survey Applications | PDF | Nightly | Well paths |

**The Full Wellbore file has no temperature field.** I parsed the RRC "Oil and Gas Well Bore System Magnetic Tape User's Guide" (91 pp., last updated May 2019) locally. It has 26 segment types: root, completion, remarks, tubing, casing, perfs, liner, formation, squeeze, location, plugging, 14B2, H-15, and others. None of them holds a temperature or BHT field. Its only log reference is `WB-LOG-FILE-RBA`, a pointer to a log record "in a file separate from the database". https://www.rrc.texas.gov/media/cx2i4xrm/wba091_well-bore-database.pdf

**Important exception: the G-1 gas-well completion form *does* carry BHT as structured data.** The RRC "Completion Data Subscriptions" manual (rev. 1 Nov 2017) defines these G-1 columns: `BOTTOM_HOLE_TEMP`, `BOTTOM_HOLE_DEPTH`, `AVG_SHUTIN_TEMP`, `FLOW_TEMP` and `WELLHEAD_FLOW_TEMP`. The W-2 and casing records add `ELECTRIC_LOG_RUN` (a log-type code: induction, acoustic, neutron, density, and so on) and `LOG_WAS_HELD_CONFIDENTIAL`. They also have `TOP_CEMENT_DETERMINE_CODE`, whose value 2 means the top of cement was determined by a **temperature survey**. That flags wells with a temperature log on file. https://www.rrc.texas.gov/media/ltudbyql/cmpldatasubscriptions_usermanual_20171101.pdf
- Caveat: this feed is a **nightly delta** of electronically filed packets. Online completion filing started in **February 2011** (see the imaged-records menu below), so structured G-1 BHTs exist only for e-filed gas completions from about 2011 on. The feed also covers only gas wells, not oil wells. A historical back-file would have to be built by scraping the Online Completion Query (https://webapps.rrc.texas.gov/CMPL/publicHomeAction.do) or by accumulating the nightly drops. Whether RRC sells a historical bulk extract is unverified.

### 2b. Images (the illegible part)
RRC Imaged Records menu: https://www.rrc.texas.gov/resource-center/research/research-queries/imaged-records/imaged-records-menu/
- **Oil and gas well logs: July 2004 onward**, in the Neubus viewer (https://rrcsearch3.neubus.com/search-profile?profileId=15).
- **Logs received before July 2004 are at the BEG Geophysical Log Facility, not online at RRC.**
- Oil and gas well records (completion packets and so on): 1964 onward (Neubus profile 17). Dry hole files: 2000 onward. District office records before 1980 without an API number: separate series. Historical W-1X/W-3X/W-10/G-10: microfilm.
- Volume download of well records, dry hole files, well logs and P-17 images goes through Energy-Depot (https://energy-depot.us/) at Texas Public Information Act pricing. The landing page itself showed placeholder text when fetched.
- RRC's own well-log page says logs are "stored and delivered in an image file format called TIFF". Monthly well-log inventory spreadsheets cover July 2006 to September 2026. https://www.rrc.texas.gov/oil-and-gas/research-and-statistics/obtaining-commission-records/oil-gas-well-records-gis-well-logs/
- **BEG: about 1.5M logs, "raster TIFF scans only. The Bureau does not currently offer LAS files." $10.00 per log scan**, ordered by email, indexed in the CONTINUUM database. Some Austin and Midland holdings are not yet catalogued. https://www.beg.utexas.edu/about/facilities/geophysical-log-facility
  - Implied cost to buy the whole BEG raster archive at list price: 1.5M x $10, about **$15M**. That is an upper bound before negotiating a bulk or academic deal; the bulk price is unverified.

### 2c. TWDB
- **BRACS** (Brackish Resources Aquifer Characterization System): a relational MS Access database (latest zip dbBracs_Public_01272025). Its geophysical well logs come in **TIFF, PDF and LAS**, "quality varies from poor to excellent". They are obtained by mailing TWDB an empty drive, and staff copy a whole county onto it. https://www.twdb.texas.gov/innovativewater/bracs/database.asp ; https://www.twdb.texas.gov/innovativewater/bracs/welllogs.asp
- **Groundwater Database (GWDB)**: water wells, springs and *converted oil/gas tests*, with water levels and water quality. Full download is pipe-delimited text plus a shapefile, updated nightly. The page does not say whether water temperature is recorded (unverified; it often is). https://www.twdb.texas.gov/groundwater/data/gwdbrpt.asp
- Relevance: shallow (<1-2 km) and mostly freshwater or brackish. Useful as near-surface gradient control and for finding warm springs, not for deep resources.

### 2d. Commercial digitised layer
- TGS sold its North American Well Data Products business (A2D, which holds the "North American well log library") to **Enverus** on **8 July 2026** for **USD 100M at close + USD 15M earn-out**. The business had **USD 27M revenue in 2025**. This puts a market price on "digitised legacy logs": a roughly $100M asset earning $27M a year, now consolidated under one data vendor. https://www.tgs.com/well-data
- S&P Global (IHS), Enverus and others sell LAS-digitised curves and header BHTs for Texas (counts unverified).

## 3. Where temperature lives, and how illegible it is

1. **Log headers (BHT, "max recorded temp")**: on essentially every wireline log run. For RRC logs from mid-2004 on, the header exists only as a **TIFF image**. Before that, the BHT is on a BEG raster scan or on paper. It is **not in any free structured RRC table**. Extracting it needs OCR or vision on scanned headers. Headers are semi-standard forms, a tractable vision task.
2. **G-1 BHT field**: structured but gas-only and roughly 2011 onward.
3. **Temperature surveys** (cement-top logs): flagged by `TOP_CEMENT_DETERMINE_CODE=2` and attached as images. These are high-value near-equilibrium curves.
4. **LAS curves**: not offered by RRC or BEG. They exist from operators and commercial vendors, and partly in TWDB BRACS.

Rule 16 (16 TAC §3.16) frames access: an electric log must be filed within 90 days of drilling completion and "each log filed with the commission shall be considered public information". Operators can ask for delayed filing, which keeps a log **confidential for 3 years** (5 years on state submerged lands). The rule says logs are to be filed "electronically in a digital format the commission accepts" but **does not mandate LAS**. https://www.law.cornell.edu/regulations/texas/16-Tex-Admin-Code-SS-3-16
- **That is the same 3-year release mechanic as Saskatchewan's assessment files.** The confidentiality window rolls off continuously, so fresh deep logs become public every month.

## 4. Literature that extracts temperature from Texas well data

- **Richards and Batir (SMU), "Analysis of Geothermal Resources in Three Texas Counties"** (DOE EE0008971, 2020). They added BHTs and grew well sites from **532 to 5,410** (about 10x) in Crockett, Jackson and Webb counties. Deep temperatures came out "hotter than previously calculated", with **150 °C at 2.6-5.1 km (Webb), 3.0-5.4 km (Jackson) and 2.7-8.0 km (Crockett)**. https://gdr.openei.org/submissions/1291
  - The point for us: a 10x density increase came from *manual* BHT harvesting in just 3 of 254 counties. That shows both the latent value and how much labour the illegibility costs.
- **Richards, Batir and Schumann (SMU/NREL), East Texas Deep Direct-Use feasibility** (Longview, Eastman Chemical). It used "oil and gas well headers (BHT)" and equilibrium wells for heat flow, at reservoir depths of 2,100-3,400 m. https://gdr.openei.org/submissions/1073 ; part 2: https://gdr.openei.org/submissions/1135
- **Johnston, Kolker, Rhodes and Taverna (NREL), Sedimentary Geothermal Feasibility**, which includes the Texas Gulf Coast. They used BHT and well data to screen basins, and picked Texas prospects for further analysis. https://gdr.openei.org/submissions/1225 (DOI 10.2172/1660196)
- **Blackwell et al. (2011), Temperature-at-Depth Maps for the Conterminous US**: the national baseline, built largely on AAPG and industry BHTs. SMU says Permian drilling reaches 26,000 ft (8 km), with typical wells at 4,000-10,000 ft. https://www.smu.edu/dedman/academics/departments/earth-sciences/research/geothermallab/datamaps/temperaturemaps
- **SMU Node of the NGDS (borehole temperatures) is offline**. Access is by email request only. https://www.smu.edu/dedman/academics/departments/earth-sciences/research/geothermallab/datamaps/ngds-project
- Standard BHT correction literature (Harrison et al. 1983; Kehle 1971 AAPG Geothermal Survey; Waples et al. 2004 Gulf of Mexico calibration) and recent ML-on-logs temperature papers for Texas were **not verified in this run** (search budget exhausted). Treat them as (unverified) leads for the other literature-review agents.

## 5. Access friction, summarised

| Layer | Free? | Bulk? | Machine-readable? | Temperature? |
|---|---|---|---|---|
| RRC wellbore, API, permits, shapefiles | Yes | Yes (MFT) | Yes, but EBCDIC/fixed-width legacy | No |
| RRC completion data (G-1/W-2/L-1) | Yes | Nightly deltas only | Yes (ASCII) | **G-1 BHT, about 2011 onward, gas only** |
| RRC log images (2004 onward) | View free; bulk at PIA pricing | Via Energy-Depot | TIFF raster | BHT on header image |
| BEG log archive (about 1.5M, pre-2004) | $10/scan | By order | TIFF raster, **no LAS** | BHT on header image |
| TWDB BRACS | Yes | Ship a drive | TIFF/PDF/some LAS | Shallow |
| Enverus/S&P digitised | No ($$) | Yes | LAS + header tables | Yes, licence-restricted |

---

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **Texas is the cleanest analogue to SMAD anywhere in US geothermal.** It has a legal duty to file, a 3-year confidentiality roll-off into public information, and about 1.5M logs plus about 430k currently monitored wells. The data is public but mostly **raster TIFF headers**, and nobody, including RRC and BEG, has turned BHTs into a free statewide structured table. Terranox's core skill is turning illegible public filings into a ranked prospect map, and here the illegible layer is huge and the free structured layer is almost empty. Two cheap seeds exist: G-1 BHTs (structured, from about 2011) and the `TOP_CEMENT_DETERMINE_CODE=2` temperature-survey flag.
2. **The data cost is bounded and buyable.** The ceiling is about $15M at the $10/scan list price for the entire BEG archive, and in practice it is much less with a targeted first pass (deep wells only, filtered by total depth from the free Wellbore file) or a bulk deal. Enverus paying about $100M for TGS's A2D log library suggests a proprietary digitised Texas BHT and temperature layer is itself a saleable asset. That is a fallback value floor, not the business.
3. **The gap vs Zanskar.** Zanskar's public story is Great Basin *hydrothermal*: blind systems like Big Blind in Nevada, BLM leases, and the Lightning Dock plant in NM. Texas is different on almost every axis. It is sedimentary, there is little federal land, and geothermal ownership is private and state, with heat attached to the surface estate under 2023 Texas legislation (unverified in this run; see the UT *Future of Geothermal in Texas* Ch. 14). Data density there comes from oil and gas boreholes, not gradient holes. The fetched sources show no sign that Zanskar is assembling Texas well-log temperature data or Texas private geothermal rights (absence unverified). The open lane is a "Zanskar for sedimentary basins": harvest BHTs from millions of TIFF headers, find hot sedimentary aquifers and EGS-grade hot spots near the ERCOT load and data-centre build-out, **then lock up surface and geothermal rights or leases from private landowners and the state (GLO / University Lands) before the map is public**, and flip proven acreage to Fervo-style EGS developers, oil majors pivoting to geothermal, or data-centre offtakers.
4. **Asset-ownership fit.** With private and fragmented ownership, the "buy before proof" step is negotiated surface or heat-rights options rather than cheap BLM auctions. That is more deal work, but it also means less price discovery and therefore a larger step-up. Orphaned and inactive wellbores (about 158k inactive, more than 12k with delinquent operators) are a second asset class: re-entry candidates whose plugging liability can be negotiated. Treat this as a hypothesis to test with legal agents.
5. **Risks to flag (not kills).** BHTs are biased low and need correction, which is a solved but noisy problem. Mid-temperature sedimentary resources (about 150 °C at 3-5 km per SMU) favour EGS or binary plants over flash plants. Some G-1 data covers only post-2011 e-filings. None of this makes the idea too small. Texas grid demand and the size of the dataset argue for a large market.

---

## Sources
- RRC Wells Monitored, 31 Aug 2026: https://www.rrc.texas.gov/media/pp4jbxif/august-2026.pdf
- RRC Well Distribution Tables index: https://www.rrc.texas.gov/oil-and-gas/research-and-statistics/well-information/well-distribution-tables/
- RRC Data Sets Available for Download: https://www.rrc.texas.gov/resource-center/research/data-sets-available-for-download/
- RRC Well Bore Database Magnetic Tape User's Guide (May 2019): https://www.rrc.texas.gov/media/cx2i4xrm/wba091_well-bore-database.pdf
- RRC Completion Data Subscriptions User Manual (Nov 2017): https://www.rrc.texas.gov/media/ltudbyql/cmpldatasubscriptions_usermanual_20171101.pdf
- RRC Imaged Records Menu: https://www.rrc.texas.gov/resource-center/research/research-queries/imaged-records/imaged-records-menu/
- RRC Research Queries: https://www.rrc.texas.gov/resource-center/research/research-queries/
- RRC Well Records / GIS Well Logs: https://www.rrc.texas.gov/oil-and-gas/research-and-statistics/obtaining-commission-records/oil-gas-well-records-gis-well-logs/
- RRC Neubus Well Logs: https://rrcsearch3.neubus.com/search-profile?profileId=15
- 16 TAC §3.16 (Cornell LII): https://www.law.cornell.edu/regulations/texas/16-Tex-Admin-Code-SS-3-16
- BEG Geophysical Log Facility: https://www.beg.utexas.edu/about/facilities/geophysical-log-facility
- TWDB BRACS database: https://www.twdb.texas.gov/innovativewater/bracs/database.asp
- TWDB BRACS well logs: https://www.twdb.texas.gov/innovativewater/bracs/welllogs.asp
- TWDB GWDB: https://www.twdb.texas.gov/groundwater/data/gwdbrpt.asp
- TGS sale of well data business to Enverus (8 Jul 2026): https://www.tgs.com/well-data
- SMU/DOE GDR 1291, Three Texas Counties: https://gdr.openei.org/submissions/1291
- SMU/DOE GDR 1073 and 1135, East Texas DDU: https://gdr.openei.org/submissions/1073 ; https://gdr.openei.org/submissions/1135
- NREL GDR 1225, Sedimentary Geothermal Feasibility: https://gdr.openei.org/submissions/1225
- SMU temperature maps: https://www.smu.edu/dedman/academics/departments/earth-sciences/research/geothermallab/datamaps/temperaturemaps
- SMU NGDS node (offline): https://www.smu.edu/dedman/academics/departments/earth-sciences/research/geothermallab/datamaps/ngds-project
- UT Austin Future of Geothermal in Texas (landing; PDFs returned 503): https://energy.utexas.edu/research/geothermal-texas
