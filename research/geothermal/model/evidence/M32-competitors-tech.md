# M32: Competitors and labs in geothermal exploration tech: what data and sensors each owns, and where the open gap is

Date: 23 Oct 2026. Slice M32, model track.

**Method note (read first).** The shared web-search budget for this run (200 calls per turn) was already used up when this agent started. Three direct fetches (a Fleet Space newsroom page, Zanskar's Lever jobs page and an ESG News Zanskar article) were blocked by the permission system, so this file made **no new web calls**. It rebuilds the competitor map from sourced sibling files (Z01-Z10, H10, L18, M08, M12, M13, M27) and from my own background knowledge. Anything from memory is marked (unverified). I name the sibling files so a reader can follow the URLs. I do not repeat their land and funding tables (Z07, Z08, Z09). This file covers only **technology, data and sensors**. A follow-up turn with fresh search budget should check the (unverified) rows, mainly Fleet Space geothermal work, Bedrock Energy, Geologica and "Geothermal Technologies".

## Bottom line

Sort every player by **what it owns in data and sensors**, not by how much money it has raised. That gives five groups:

1. **Zanskar** owns the best private *label set* for blind hydrothermal: about 370 systems, about 27,000 temperature samples, more than 5 million acres tested, plus its own gradient holes and LBNL large-N seismic work. It owns no proprietary sensor.
2. **Next-gen developers** own hardware for *access and production*, not for *exploration*:
   - Fervo: fiber/DAS and horizontal EGS drilling;
   - Quaise: gyrotron drill;
   - Eavor: loop tools;
   - Sage: pressure geothermal;
   - XGS: conductive loops.
3. **Incumbents** own deep, dense *proprietary archives* that never get resold: Ormat, Cyrq, Open Mountain, CTR and Calpine hold well logs, MT, flow tests and decades of TG holes around their fields.
4. **Software and service firms** own *tools* but not data. Their clients keep the data. This group includes Seequent, Teverra, SLB, Baker Hughes, Fleet Space, Phoenix/Zonge/Quantec and Microseismic.
5. **Shallow geoexchange drillers** (Dandelion, Bedrock Energy) collect thousands of shallow borehole thermal records, but in the wrong places: suburbs and cities in the US Northeast and Midwest (unverified).

The open slot has four parts that no one combines:

- (a) a **standing, owned, cheap sensor network** that measures temperature and fluid chemistry on **private and state ground** in the western US;
- (b) explicit **negative labels and an observation-effort record** ("we looked here and it was cold");
- (c) a model that turns that into a **calibrated "how much hidden MWe" posterior**, not just a favorability map;
- (d) a **neutral sales channel** that can sell to every buyer above, including Zanskar's rivals.

The data is the moat, because algorithms are already open (GeoCore is open source) and screening maps are free (INGENIOUS, GeoMap, USGS and NREL maps). Hardware matters only because it lowers the cost per label.

## Findings

### F1. Zanskar: the strongest data owner, and still sensor-light
- **Stack:**
  - GeoCore, a LightGBM model on an H3 grid using INGENIOUS layers. It is open-sourced at https://github.com/zanskar-geothermal/GeoCore.
  - A base-rate model: historic exploration found one blind system per ~550 holes (0.181%), and about two-thirds of unprotected Quaternary faults have no temperature data within 1 km.
  - A site-scale Bayesian / value-of-information loop, now sped up with neural-operator surrogates that run up to 10,000x faster than full physics.

  Source: M13, Z03.
- **Data owned:**
  - a private compilation of about 27,000 temperature samples and about 370 known systems;
  - its own TG and production holes (Big Blind, Pumpernickel, Lightning Dock);
  - Lightning Dock operating data, a plant bought from Cyrq in May 2024 (https://www.thinkgeoenergy.com/zanskar-acquires-lightning-dock-geothermal-power-plant-new-mexico/).
- **Sensors:** no proprietary sensor has been found (H10). The LBNL CRADA (OSTI 3015294, Jan 2026) used **large-N arrays of low-cost seismometers**, micro-earthquake tomography and "ambient fracture-seismic emissions" to guide well siting (M12; the page was not fetched, so unverified). A Zanskar co-author (Ian Warren) worked on PSET seismic plus cooperative MT/gravity inversion at San Emidio and Crescent Valley with Ormat and LBNL (OSTI 1986084; Z03).
- **Where it does not look:** it won nothing at auction outside Nevada. It does not visibly work private ranch land, state trust land or Texas fee land (Z04, Z06). It also has no stated geochemistry or hydrologic-masking term (M13).
- **Capital:** about $180M equity plus a $40M development facility (Z09). It builds its own plants, so it is a rival to Ormat and Invenergy and will not sell to them.

### F2. Fervo: hardware for drilling and production, data from its own field
- Fervo's own tech is horizontal EGS wells, in-well fiber-optic DAS/DTS and tuned PDC drilling. In 2021 it formed a Google AI/ML subsurface partnership (https://blog.google/outreach-initiatives/sustainability/google-fervo-geothermal-energy-partnership/; https://egi.utah.edu/wp-content/uploads/2023/09/09.45-Emma-McConville-Fervo_EGI_Sept-19-2023.pdf).
- It holds about 596k acres, assembled at about $4/acre in 2019-21 (Fervo 424B4, Z08), and raised about $1.77B in net IPO proceeds.
- Its exploration data is mainly **Cape and FORGE-area deep wells** plus the Milford public data. It does not run a regional exploration sensor network. It is a **buyer** of hot, drillable, permitted land.
- Its prospectus says rivals paid "hundreds of dollars per acre in 2025 for geothermal positions that failed to meet our development standards" (Z08). That is a buyer telling us it values **pre-screened, data-backed** parcels.

### F3. Quaise, Eavor, Sage, XGS, GreenFire, Mazama: access tech, not discovery tech
- **Quaise** uses a millimetre-wave gyrotron drill. Its Project Obsidian in Oregon targets 50 MW. It raised a $134M first close of its Series B in Jul 2026 (https://lasvegassun.com/news/2026/jul/07/quaise-energy-raises-134-million-in-initial-close-/).
- **Eavor** builds Eavor-Loop tools and runs Geretsried in Germany. It has raised about $529M (L18).
- **Sage** works on pressure geothermal and storage, and has a site at Ormat's Blue Mountain (Z07).
- **XGS** builds conductive closed loops in New Mexico and has a Meta PPA for 150 MW (Z07).
- **GreenFire** retrofitted a coaxial loop into a Coso well and got 1.2 MWe (L18).
- **Mazama** does superhot EGS at Newberry and reached 629 F (Z07).
- **Data they own:** a handful of deep wells each. Every techno-economic study finds that closed loops still need **hot, shallow, high-gradient** rock (L18). So all of them are **customers for temperature-at-depth data**, not makers of it.

### F4. Incumbent operators: the largest private archives, closed by design
- **Ormat:**
  - holds about 434k acres in the US (FY2025 10-K);
  - has 34 US prospects;
  - spends about $10k per desk evaluation and $1-5M of exploration per site (Z08);
  - designs and builds its own OEC turbines;
  - runs drilling and exploration in-house (unverified detail).

  It ran 3D MT at McGinness Hills with the University of Utah (M08) and PSET seismic at San Emidio and Crescent Valley with LBNL (M12). It historically found blind fields from **mining exploration holes**: McGinness Hills, about 160 MW, and Tungsten Mountain, 24 MW (https://investor.ormat.com/news-events/news/news-details/2017/24-MW-Tungsten-Mountain-Geothermal-Power-Plant-in-Nevada-Begins-Commercial-Operation/default.aspx). Its archive is huge but never resold.
- **Cyrq** pitches "modern data and technology" but publishes no ML (Z07). **Open Mountain** has 64 wells and is brownfield-first (Z08).
- **CTR** (Hell's Kitchen, Salton Sea) works on power plus lithium, has a 500 MW project with Baker Hughes, and agreed a SPAC deal with Plum IV in Mar 2026. Its data is private Salton Sea brine and well data (Z08; https://www.cthermal.com/).
- **Calpine** holds The Geysers (Z08).
- **Read-across:** incumbent data is the richest label source in the West. We can reach it only through farm-outs, data trades or buying old archives (M08 row "Operator / contractor MT ... buyable or tradeable", unverified).

### F5. Software and service vendors: they own tools, and the client owns the data
- **Seequent (Bentley).** Leapfrog Geothermal/Energy is the de facto 3D geological modelling package in geothermal. Seequent also owns Oasis montaj (Geosoft) for potential fields and Volsung for reservoir modelling. Sibling files show Leapfrog models at Granite Springs, about 280 km² down to 6 km (M17 template, from the Trainor-Guitton SGW 2023 paper). The Bentley ownership is from memory (unverified). It owns no exploration data of its own.
- **Teverra** sells physics-informed ML, play-fairway analysis, ConvertDeck and MMARCT. It has DOE and NSF SBIRs and owns no assets (Z07; https://teverra.com/).
- **SLB, Baker Hughes, Halliburton** sell logging and reservoir software. Baker Hughes partners with CTR and XGS and owns part of Baseload (Z07).
- **Sensor vendors:**
  - Phoenix (MTU-5C), Zonge, Quantec and Metronix for MT;
  - Silixa and Luna for DAS;
  - STRYDE and SmartSolo for nodal seismic;
  - Microseismic Inc. ran the PSET crews: 1,302 stations × 6 geophones × about 180 h at San Emidio (M12).

  Their data goes to the client (H10, unverified product lists).
- **Fleet Space (ExoSphere).** It sells satellite-linked ambient-noise seismic nodes, later with gravity added. It raised a $150M Series D at $800M+ and sells surveys to Rio Tinto and Barrick (H10; https://www.australianmanufacturing.com.au/fleet-space-raises-150m-to-accelerate-clean-energy-mineral-discovery/). It has marketed ExoSphere for geothermal (unverified; the fetch was blocked). It owns no ground and no labels. It is a **possible supplier** to us, and shows that dense passive seismic is now a commodity.

### F6. Mining-AI analogues: KoBold, Earth AI and similar
- **KoBold** builds its own hardware: Hyperpod (hyperspectral plus LiDAR), Korecam360 core imaging, MetaLab assay, and patents on large induction loops and compact muon detectors. It is valued at about $2.96B pre-revenue, and the value comes from **owning Mingomba**, not from the sensors (H10; https://sacra.com/c/kobold-metals/). Its data system (TerraShed) ingests every legacy record, so it is legacy-data-first (unverified name).
- **Earth AI** owns its own cheap rig, targeting about $100/m, and claims a 75% hit rate. It flips or joint-ventures the discoveries (https://www.mining-technology.com/news/earth-ai-20m-ai-driven-mineral-exploration-drilling/). **This is the closest shape to ours:** cheap labels from its own hardware, then sell the proven right.
- **Lesson:** the sensor is a cost-per-label tool. The asset (the right) captures the value.

### F7. Shallow geoexchange: Dandelion and Bedrock Energy (out of geography, but a data idea)
- **Dandelion** (a Google X spin-out) and **Bedrock Energy** (Austin, automated geoexchange drilling for commercial buildings) drill many 100-300 m vertical bores. Bedrock instruments its bores and models ground thermal response (all unverified; earlier files called them "irrelevant" (Z07)).
- They matter as **evidence that cheap, instrumented, repeated shallow boreholes can be industrialised**. Bedrock's pitch is software-driven automated drilling. That is the H11 "own gradient rig" idea already proven in soft ground. Their data is east of the Rockies and urban, so it is useless for Great Basin labels.

### F8. "Geologica", "Geothermal Technologies", Open Mountain and Cyrq
- **Geologica Geothermal Group** (San Francisco area) is a consultancy that does resource assessments and exploration programmes for developers (unverified; its domain was parked in Z07). **"Geothermal Technologies"** most likely means DOE's Geothermal Technologies Office. GTO is the biggest funder of exploration tech. Its FY2026 request is $150M, and in Sep 2026 it selected 21 EGS projects worth up to $99M (from sibling B05/L-files). GTO also funds the public layers everyone shares: Play Fairway Analysis, INGENIOUS and GeoDAWN airborne magnetics and lidar.
- **Public labs** (USGS, NREL/NLR, LBNL, UNR GBCGE, Utah FORGE/EGI) publish the shared screening layer. These include the USGS and NREL XGBoost/BNN favorability maps, INGENIOUS and USMTArray (about 1,711 MT stations on a 70 km grid; M08). Project InnerSpace's GeoMap is free (https://geomap.projectinnerspace.org/).
- **Effect:** screening at the 2-10 km cell size is a commodity. The edge sits below about 1 km cell size and in the labels.

### F9. The open gap, stated plainly
No player combines all four of these:

| Capability | Zanskar | Fervo / next-gen | Ormat and incumbents | Vendors / Fleet | Free public | **Open?** |
|---|---|---|---|---|---|---|
| Regional favorability model | Yes (open GeoCore) | Partial (Google) | In-house | Teverra | Yes (USGS/NREL/InnerSpace) | No, commodity |
| Private temperature labels at scale | Yes (~27k) | Own fields only | Yes, closed | No | Partial (NGDS, GDR) | Partly |
| **Negative labels and observation-effort map** | Implicit only | No | Implicit | No | No | **Yes** |
| **Owned standing sensor network on private and state land** | No | No | No | Sells to clients | No | **Yes** |
| Water-well chemistry and temperature on ranches | No (no geochem term) | No | Local only | No | USGS NWIS, sparse | **Yes** |
| **Calibrated hidden-MWe posterior with credible interval** | Flat 30 MWe × hit rate (M13) | No | Internal | No | USGS 2008 (30 GWe mean blind, wide range) | **Yes** |
| Neutral channel to all buyers | No (it builds plants) | No | No | n/a | n/a | **Yes** |
| Cheap proving step (own rig) | Contract rigs | No | Own drilling (unverified) | No | No | Partly |

## Datasets table

| Dataset | Owner | Access | Coverage | Value for blind detection |
|---|---|---|---|---|
| Zanskar temperature compilation (~27k samples, 370 systems) | Zanskar | Private. Base rates published (Stanford SGW 2025, M13) | Great Basin and wider West | High. Use the published base rates as priors |
| GeoCore code and features | Zanskar | Open, GitHub | INGENIOUS area | Medium. A baseline to beat, and the same features everyone has |
| INGENIOUS layers, PFA, GeoDAWN | DOE/UNR/USGS/NREL | Open (GDR) | Great Basin | Medium. The shared commodity screen |
| USMTArray deep MT | NSF/USGS | Open (IRIS/EarthScope) | Lower 48, 70 km grid | Low-medium. Crustal, not reservoir scale |
| Ormat/Cyrq/OME/CTR well, MT and TG archives | Operators | Closed. Reach via farm-out or trade (unverified) | Around about 60 fields | Very high labels, hard to get |
| PSET San Emidio / Crescent Valley (Microseismic, LBNL, Ormat) | DOE project | Partly on GDR/OSTI | 2 fields | High as a training set for seismic-to-permeability |
| Fervo Cape / FORGE DAS and well data | Fervo / DOE FORGE | FORGE open, Fervo closed | Milford, UT | Medium. Calibrates conductive gradients |
| Fleet ExoSphere surveys | Clients | Closed | Mining sites | Low for us. Shows the cost curve |
| Project InnerSpace GeoMap | Nonprofit | Free | North America | Medium. A sedimentary-basin screen |
| Geoexchange bore thermal data (Dandelion, Bedrock) | Companies | Closed | NE/Midwest, urban | Low. Wrong geography |

## What dominates uncertainty (this slice)

1. **Label bias and missing negatives.** Every open model trains on known systems and wells drilled where people already looked. No one publishes "looked and cold" maps. Without an observation-effort term, "no data" reads as "no resource", and the blind count stays wide (M13, M19).
2. **Size of each hidden system.** The industry uses a flat MWe per discovery (Zanskar uses 30 MWe). The size distribution, which is set by reservoir permeability and volume, dominates "how much" more than the count does.
3. **Closed incumbent archives.** The best labels in the West sit in Ormat and other operators' files. Whether we can reach them by trade decides how fast our model calibrates.
4. **Hydrologic masking.** Cold groundwater hides the upflow at the surface. No competitor models it explicitly, so shallow surveys may under-count by an unknown factor (M23).
5. **How fast competitors close the gap.** Zanskar or Fleet could add a sensor network in about 12-24 months if they wanted to. The window is set by their incentives, not by the tech (unverified judgment).

## What a sensor could fill

- **Owned cheap labels on private and state land.** The prior pick, a ranch water-well drop probe, fills exactly the cell no competitor touches. It logs T/P/conductivity and takes a sample for geothermometry, and the heat option is signed on the same visit. Each visit gives either a positive label or a dated, located **negative** label. That builds the observation-effort map that is the clearest missing data layer in F9.
- **A standing network, not one-off surveys.** Leave a small number of logging 2 m temperature probes (and later a continuous soil-CO2 or radon cell) in place for a whole season. This removes the seasonal noise that kills one-shot 2 m surveys and creates a time-series asset no vendor sells. It is like the multi-client library model in H10, applied to shallow heat.
- **Commodity passive geophysics at the price Fleet and LBNL proved.** E-field-only MT and large-N nodes are now cheap. Our edge is placing them by value of information on parcels we already optioned, and keeping the data.
- **A geochemistry channel.** Na-K-Mg, silica and Li/B ratios from water wells. Zanskar has no geochem term (M13), and incumbents use geochem only around their own fields.

## Implications for a better model

1. **Use Zanskar's own published numbers as priors.** That means one blind system per ~550 holes and two-thirds of Quaternary faults with no temperature data within 1 km. Then beat Zanskar on **likelihood**, by adding observation effort and negatives. Do not try to beat it on features.
2. **Add an explicit "searched-ness" layer to every cell.** Count holes, wells, springs sampled and our own probe visits, each weighted by depth. Model P(resource) × P(detected | searched). The undiscovered count is then the integral of P(resource) × (1 − P(detected)). This is what makes "how much hidden heat" defensible with a credible interval.
3. **Replace the flat MWe per discovery with a size distribution.** Fit it to the size distribution of known Great Basin systems (M01/M05) and condition it on permeability proxies. Report P10/P50/P90 hidden MWe per region, not a mean.
4. **Treat incumbent archives as a calibration target.** Offer Ormat, Cyrq or OME our screened ranch-land portfolio in exchange for anonymised TG and MT labels. Even 500 extra labelled holes would sharpen the likelihood a lot (unverified magnitude).
5. **Make the model buyer-facing.** Fervo, Mazama, XGS and Quaise need temperature at 2-5 km. Ormat and Invenergy need convective upflow at 0.5-2 km. Output both targets from one shared posterior so the same data room sells to both buyer types.
6. **Do not compete on algorithms or regional maps.** Both are open or free. Spend effort on labels, rights and calibration.
