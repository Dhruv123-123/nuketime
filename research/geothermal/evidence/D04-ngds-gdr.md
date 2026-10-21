# D04: DOE Geothermal Data Repository (GDR) and National Geothermal Data System (NGDS). What is in them, how big and how good they are, how ML uses them, and whether they are already "read"

*Method note: the shared WebSearch budget for this workflow ran out before this agent started. All findings below come from direct WebFetch of primary pages: GDR submission records, OSTI, USGS and Zenodo. Items from memory are marked (unverified). Fetched 2026-10-21.*

## 1. Bottom line

- **GDR is large but mostly not exploration data.** As of today it holds **764 TB, 1,423 datasets, 146 data providers and about 73.7M downloads** (https://gdr.openei.org/). Most of those bytes come from DOE R&D projects such as Utah FORGE, EGS Collab, PoroTomo and fiber/DAS "Data Lakes". It is a repository where DOE grantees are expected to deposit their data. It is not a systematic national inventory of prospects.
- **NGDS is the legacy national inventory, and it is now officially "retired".** GDR submission 1704 calls it "the now-retired National Geothermal Data System (NGDS)" (https://gdr.openei.org/submissions/1704). Its two main nodes were moved into GDR or Zenodo in 2025 and 2026 because of "institutional, financial, and technical instability" among NGDS and its contributors (https://zenodo.org/records/8125526).
- **The key well-temperature data is a known quantity.** The SMU node, now GDR 1704 (21.6 GB, 25 files), covers **more than 44,000 wells**. It includes **more than 30,000 corrected bottom-hole-temperature (BHT) sites from oil and gas wells** and **more than 14,000 equilibrium-temperature sites**, plus more than 6,000 related exploration documents: scanned field notes, reports and maps. ARRA grant DE-EE0002852 paid for it, and it was frozen in 2014.
- **The structured part has already been read, and Zanskar is helping curate it.** DOE-funded ML favorability work has been run on these data since about 2019: the Nevada ML PFA project, INGENIOUS, GeoThermalCloud, and USGS (Mordensky et al.). Zanskar itself appears on GDR as the lead of DOE project **EE0011649 "GEOGYM: A Multi-Site Benchmark Dataset to De-Risk and Optimize Geothermal Exploration."** In August 2026 it published a 7.4 GB data package for its own Lightning Dock field (https://gdr.openei.org/submissions/1856).
- **The unread part is the unstructured long tail.** That means the scanned field notes, reports and maps in GDR 1704 (about 19 GB of PDF and image archives by state), the AASG node tables (722.6 MB, republished), and the ~1,400 heterogeneous GDR project packages. These have not been fused into a single ML-ready, georeferenced corpus that is tied to land status. This is the Saskatchewan-SMAD analogue.

## 2. GDR: contents and size

| Metric | Value | Source |
|---|---|---|
| Total data | 764 TB | https://gdr.openei.org/ |
| Datasets | 1,423 | same |
| Data providers | 146 | same |
| Downloads | 73,676,088 | https://gdr.openei.org/about |
| Licence | CC BY 4.0 by default | same |
| Operator | OpenEI, built by the National Laboratory of the Rockies (NLR, formerly NREL; help address GDR.Help@nlr.gov) | same |
| Features | "Ask GDR" generative-AI search (labelled experimental); Data Lakes on AWS, GCP and Azure for TB-scale data | https://gdr.openei.org/data_lakes |

**What it contains.** It holds data from DOE Geothermal Technologies Office–funded projects. The featured collections are Utah FORGE, EGS Collab, Play Fairway Analysis (PFA), Data Lakes and District-Scale Geothermal. Many records are tiny. For example, submission 1215 is a 2 kB FORGE seismic detection text file (https://gdr.openei.org/submissions/1215). The TB volume is concentrated in a handful of seismic, DAS and fiber datasets.

**How much is exploration-relevant.** Keyword hits from GDR's own search, which counts submissions rather than wells: "machine learning" 92, "bottom hole temperature" 630, "heat flow database wells" 792. Exploration-relevant packages include:

- PFA projects: Nevada, Tularosa Basin, Denver Basin, Hawaii, New Mexico and others
- Nevada ML (submissions 1349–1353, 1402)
- INGENIOUS (1390, 1391)
- The 2013 Exploration Gap Assessment, a contiguous-US grid of 88,000 cells of 10×10 km scoring the availability of well, geologic-map, fault, geochemistry and geophysics data (https://gdr.openei.org/submissions/263)
- The AASG wells BHT compilation (submission 252)
- State compilations, for example the Colorado well database (1224) and the Texas counties beneath oil and gas fields (1291)
- Sedimentary-basin feasibility studies (1225)

**Quality.** Peer review is left to the submitting organization. Formats vary from project to project: shapefile, geodatabase, GeoTIFF, xlsx, PDF. There is no common schema across projects except the old NGDS/USGIN content models. Location and temperature accuracy are often not assessed. GDR 252 states that "location, name, temperature, and depth accuracy was not assessed beyond what the original service provided" (https://gdr.openei.org/submissions/252).

## 3. NGDS: history, contents and status

- **Origin.** It was funded under ARRA 2009 through DOE awards including DE-EE0001120, DE-EE0002850 and DE-EE0002852, and was established around May 2014 (https://en.wikipedia.org/wiki/National_Geothermal_Data_System; GDR 1704). The contributors were USGS, the SMU Geothermal Lab and the Association of American State Geologists (AASG). Arizona, Illinois, Kentucky and Nevada acted as hubs. Data types were "borehole temperature measurements, geothermal gradients, active faults, and geochemical analyses." It served data over WFS, WMS and CSW.
- **NGDS 2.0 (2020).** The Arizona Geological Survey carried out security upgrades under DOE EE0008761: Ubuntu 20.04, HTTPS, PostgreSQL, ArcGIS server and a **non-public API** (https://gdr.openei.org/submissions/1248). This was maintenance-level funding only.
- **Retirement and migration.** The geothermaldata.org portal returned HTTP 503 on two attempts today. The **SMU node was moved to GDR as submission 1704** (submitted October 2025, updated July 2026). The **AASG node's "Geothermal Features and Observations" tables were republished on Zenodo** (722.6 MB zip, v1.1.1, DOI 10.5281/zenodo.8125526) and indexed in GDR as submission 1805 (July 2026, award EE0002852). The stated reason was erratic access caused by "institutional, financial, and technical instability" (https://zenodo.org/records/8125526; https://gdr.openei.org/submissions/1805).
- **SMU node detail** (https://gdr.openei.org/submissions/1704):
  - More than 44,000 wells with heat flow or gradient data.
  - Corrected BHT database of more than 30,000 sites from oil and gas wells.
  - Equilibrium database of more than 14,000 sites, linked against the UND Global Heat Flow database.
  - More than 6,000 related exploration resources.
  - Archive sizes. Related reports, files and maps: NV 3.13 GB, OR 1.43 GB, MT 510 MB, ID 341 MB, WA 229 MB, TX 124 MB, other states 3.56 GB. Well data notes: NV 2.93 GB, OR 1.97 GB, MT 1.49 GB, ID 1.13 GB, other states 3.97 GB. Curated well data: only 360 MB.
  - **Interpretation:** about 95% of the bytes are scanned notes and documents, and only about 360 MB is tabular. Metadata errors exist: the "TX" notes archive is described as Montana data.
- **AASG BHT data.** BHTs typically come from wireline log headers. The 2013 NREL aggregation preferred corrected over measured values and did no accuracy assessment (GDR 252). From memory (unverified), the AASG state contribution is often quoted as millions of records, with hundreds of thousands of BHTs. I could not fetch a primary count.

## 4. Use in ML: who has already "read" it

| Effort | Data | Methods | Source |
|---|---|---|---|
| Nevada Geothermal ML / PFA (NBMG, Faulds et al.; DOE EE0008762; 2019–2022) | USGS gravity and magnetics, heat flow map with its well data, fault slip and dilation tendency, geochemistry, paleo-geothermal features, positive and negative training sites | ANN, ELM, Bayesian NN, PCA, NMFk; PyTorch code released (Results.zip 963 MB) | https://gdr.openei.org/submissions/1351 ; https://gdr.openei.org/submissions/1402 ; https://gdr.openei.org/submissions/1349 |
| INGENIOUS (UNR/GBCGE, NBMG, USGS, Utah and Idaho surveys; DOE EE0009254) | Great Basin regional features: 2-m temperature probes, seismicity density, geodetic strain, Quaternary faults and volcanics, well and spring temperature and chemistry, MT, gravity and magnetics, heat flow; about 117 MB compiled | Favorability prediction for "hidden" systems | https://gdr.openei.org/submissions/1391 |
| GeoThermalCloud (LANL/Stanford) | Nevada and SW New Mexico data fusion; 1.04 GB HDF5 training set | NMFk and neural network to "predict the location of hidden geothermal resources" | https://gdr.openei.org/submissions/1377 ; GDR 1297 |
| USGS retrospective PFA (Mordensky, Lipor, DeAngelo, Burns, Lindsey) | Western-US favorability features | Logistic regression vs XGBoost; "When Less Is More" (complex ML did not beat simpler models); feature importance | https://gdr.openei.org/submissions/1498 |
| Brady/Desert Peak AI exploration | Labelled training data | Supervised and unsupervised ML | GDR 1288, 1300, 1344 |
| BRIDGE (Sandia, 2025) | Airborne EM over top-ranked Nevada PFA prospects | Conceptual models; notes lower-ranked PFA prospects "may now merit exploration" | https://www.osti.gov/biblio/2540220 |
| Zanskar GEOGYM (DOE EE0011649) | Multi-site benchmark; Lightning Dock: 41 wells, 135 MT stations, 14,108 water analyses, 6,850-row operations table, 7.4 GB | Benchmark dataset for exploration ML | https://gdr.openei.org/submissions/1856 |

Baseline context: USGS 2008 estimated **9,057 MWe identified, 30,033 MWe undiscovered (mean), and 517,800 MWe EGS** (https://pubs.usgs.gov/fs/2008/3082/). The undiscovered 30 GWe of "blind" hydrothermal resource is the target of all the ML efforts above.

**Is it already "read"?**

- **The structured layers: yes, by multiple well-funded teams.** These are the heat flow map, Quaternary faults, gravity and magnetics, strain, and spring chemistry. They have been processed into Great Basin favorability rasters, and the rasters are public. One USGS conclusion matters here: model complexity adds little on these features ("When Less Is More"). That implies the marginal edge from ML on the *same* public layers is small.
- **The long tail: no.** Specifically:
  1. About 19 GB of scanned SMU field notes and reports, which are text- and figure-heavy and only partly digitized into tables.
  2. Oil and gas BHT data outside the Great Basin. The Great Basin is the focus of every ML study listed above. Other basins include Texas, the Rockies, the Williston and the Gulf Coast; for Texas, see GDR 1291.
  3. Cross-linking each datum to current land status: BLM lease availability, state trust land, private fee mineral or geothermal rights. None of the DOE efforts does this, because they are research products and not acquisition engines.

## 5. Data-quality issues relevant to an ML moat

- BHT bias. Log-header BHTs typically read low because of mud circulation, and corrections (Harrison, Kehle, etc.) are empirical. SMU supplies corrected values, but the method varies by state (unverified detail).
- Labels are sparse and positive-biased. Training sites are known systems, and negatives are sampled. The USGS retrospective explicitly flags expert-selection bias (GDR 1498).
- Metadata errors and mislabelled archives (GDR 1704), unassessed accuracy (GDR 252), and one portal down entirely (geothermaldata.org 503).
- Fragmentation. The data is spread across GDR, Zenodo, USGS ScienceBase, state surveys and SMU. Each is CC BY, so anyone can use it, but integration is real work.

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **The data resembles SMAD only in part.** SMAD is a single, legally mandated, report-rich archive. In the US geothermal stack, the *tabular* layer is well known and already ML-mined in the Great Basin; anyone can download the favorability rasters. The SMAD-like asset is the **unstructured, scanned SMU and AASG long tail (~19 GB of notes and reports) plus state oil-and-gas log libraries outside NGDS**, which LLM/vision extraction can turn into new temperature-at-depth points. This is plausible and fits "assume the tech works".
2. **Zanskar is not ignoring public data; it is shaping it.** As DOE's GEOGYM lead, Zanskar is publishing curated field data and defining the benchmark. A data-only pitch ("we read the GDR") does not differentiate.
3. **Where the gap is:**
   - **Geography.** Public ML work, and by press accounts Zanskar's discoveries (Big Blind NV, Lightning Dock NM), concentrate on Great Basin hydrothermal systems. The 30,000+ oil and gas BHT sites, and state log archives in Texas, Rockies and Williston-type sedimentary basins, are under-mined. This matters for **sedimentary and EGS-grade heat in Fervo-style plays**, where the right to own is often *private fee or state* geothermal rights. Those rights trade cheaply and are not visible on BLM's competitive-lease map. Zanskar's model is to explore, then develop and operate plants, which is capital-heavy.
   - **The Terranox gap is "land-first asset flipping".** That means fusing extracted data with land status, acquiring rights *before* any drilling at lease or option prices, and selling the de-risked position to developers or data-centre offtakers, rather than building plants.
4. **Risks:**
   - Public-data edge decays fast. Rasters and code are open, and the USGS shows diminishing returns from model complexity.
   - The moat must therefore be (a) new extracted data points from the unstructured corpus, (b) proprietary cheap ground truth, such as shallow 2-m probes or temperature-gradient holes, and (c) speed in land acquisition. Raw ML access is not a moat.
   - NGDS retirement means data access is fragile, which is mildly favourable: integration is a barrier to others.
5. **Scope is not "too small".** The USGS undiscovered hydrothermal mean of about 30 GWe, plus EGS of about 518 GWe, makes the ownable land universe very large. The constraint is the acquisition model, not the size of the resource.

## Sources

- https://gdr.openei.org/ (GDR statistics)
- https://gdr.openei.org/about
- https://gdr.openei.org/data_lakes
- https://gdr.openei.org/submissions/1704 (SMU NGDS node, 44,000+ wells, 30,000+ BHT sites, "now-retired NGDS")
- https://gdr.openei.org/submissions/1805 (AASG node preservation)
- https://zenodo.org/records/8125526 (AASG-GDS republication; instability quote)
- https://gdr.openei.org/submissions/1248 (NGDS 2.0)
- https://gdr.openei.org/submissions/252 (AASG BHT aggregation, NREL 2013)
- https://gdr.openei.org/submissions/263 (Exploration Gap Assessment)
- https://gdr.openei.org/submissions/1349 , /1351 , /1402 (Nevada ML PFA)
- https://gdr.openei.org/submissions/1391 (INGENIOUS)
- https://gdr.openei.org/submissions/1377 (GeoThermalCloud)
- https://gdr.openei.org/submissions/1498 (USGS retrospective PFA, Mordensky et al.)
- https://gdr.openei.org/submissions/1856 and https://gdr.openei.org/search?q=EE0011649 (Zanskar GEOGYM / Lightning Dock)
- https://gdr.openei.org/submissions/1215
- https://gdr.openei.org/search?q=machine+learning ; https://gdr.openei.org/search?q=bottom+hole+temperature
- https://www.osti.gov/biblio/2540220 (Sandia BRIDGE)
- https://pubs.usgs.gov/fs/2008/3082/ (USGS 2008 assessment)
- https://en.wikipedia.org/wiki/National_Geothermal_Data_System (secondary; history)
- https://www.zanskar.com/ (backers only)
