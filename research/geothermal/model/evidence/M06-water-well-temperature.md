# M06: Water-well logs and groundwater temperature as blind-system evidence

Slice M06, model track. Date: 23 Oct 2026. This file builds on `../../../hardware/evidence/H06-water-well-landman.md` (the rancher drop-probe deal, well-access risks, title traps), `../../evidence/L15-geochem.md` (geothermometers and WQP chemistry), `../../evidence/L02-blind-systems.md` (Gabbs Valley and the "10% complete" Nevada water-well audit) and `M04-bht-corrections.md` (the quality ladder for temperature readings). It does not repeat them. What is new: (1) live counts I pulled myself from the Nevada NDWR driller-report service, the California DWR well-completion API, the Idaho IDWR geothermal-well layer and the Water Quality Portal (WQP); (2) Zanskar's own 2025 statistic on how many blind systems water wells found; (3) a concrete way to use the shallow, noisy, single-point "driller temperature" in a model. Web budget used: 8 searches, 6 fetches, plus direct API queries.

## Bottom line

Shallow water wells are the largest and most under-used temperature dataset in the West. They are also the historical way blind systems were found: Zanskar's own review says accidental water-well drilling found "more than a third of known blind or hidden geothermal systems", and that this discovery channel slowed sharply after homesteading ended in 1976. The data exists but is thin and messy. Nevada has 146,235 driller reports online, and 14,278 of them (9.8%) carry a temperature value. That share jumped from about 4-6% before 2015 to about 24-26% after 2015, so Nevada now digitizes roughly 900 new well temperatures a year. California has 1.11 million digitized well-completion reports but no temperature field at all. The WQP holds about 54,000 groundwater-temperature sites across seven western states, but only 14% of Nevada's 18,993 WQP well sites have any temperature. In my own Nevada pull, 1,202 driller-report wells read 30 C (86 F) or more, and 697 of those sit more than 10 km from any WQP well at 35 C or more. Of those 697, 328 read 40 C or more. That is a ready-made list of warm-well anomalies that the public thermal-spring compilations do not show (unverified how many are already-known fields that WQP happens to miss). A better model should treat every water well, warm or not, as a censored, advection-biased temperature point. It should spend sensor money re-logging the warm, isolated ones to equilibrium and sampling their chemistry.

## Findings

### F1. Water wells found a large share of blind systems (Zanskar's own number)
- Edwards, Hoiland, Smith, DeReuil, Grujic, Lipscomb and Morrison (Zanskar), "A Look Into Geothermal Discoveries Across the Western United States", Stanford Geothermal Workshop 2025, SGP-TR-229 (https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Edwards.pdf).
  - They compiled 370 western US sites with moderate to high potential. 258 have surface features and **112 are blind or hidden**.
  - Accidental discoveries, mainly from water wells and mining, account for about half of utility-scale resources and most blind discoveries. **Water-well drilling alone found "more than a third of known blind or hidden" systems.**
  - The rate of these finds fell sharply after homesteading ended in 1976.
  - **Under 10% of the western US has any subsurface temperature data, and in 90% of the sampled 1 km2 cells the only wells are shallower than 20 m.** About two-thirds of Quaternary faults outside protected land have no temperature data within 1 km.
  - The historical hit rate is 0.181% per drill sample (49 blind systems from about 27,000 samples).
- Read-through. Zanskar has already compiled water-well temperatures. The open edge is not the public table. It is (a) warm wells that were never logged properly, (b) wells drilled since their compilation, and (c) owning the land around them.

### F2. Named cases where warm water wells revealed blind or hidden systems
| Case | How found | Now | Source |
|---|---|---|---|
| Lightning Dock, NM (Animas Valley) | 1948 agricultural wells under 30 m deep hit boiling water at 26.5 m. Kintzinger studied it in 1956. | Cyrq plant, about 4 MW from 2013, later expanded (now owned by Zanskar, per L02) | https://en.openei.org/wiki/Lightning_Dock_Area |
| Newcastle, UT (Escalante Valley) | Irrigation well drilling (about 1975, unverified year). The system is "blind (no surface expression)", with a plume into Escalante Valley along the Antelope Range fault and an aquifer at 85-95 m. | Direct use (greenhouses) | https://www.searchanddiscovery.com/abstracts/html/1990/rms/abstracts/1315c.htm ; https://pubs.usgs.gov/publication/70015244 |
| Raft River, ID | Irrigation wells in the 1950s (unverified detail; see H06) | 13 MW Ormat plant | H06 |
| Railroad Valley, NV | Oil wells found a 125 C system at Bacon Flat and Grant Canyon. Heat flow there reaches 234 mW/m2 against 49-76 mW/m2 across the rest of the basin. USGS says similar systems may be "masked by ground-water flow" in other carbonate-aquifer basins. | Not developed | https://pubs.usgs.gov/publication/70205980 |
| Gabbs Valley, NV | Play fairway work used "geothermometry from water wells" among its evidence. TG holes then confirmed about 124 C at 152 m. | Not developed | L02; https://www.usgs.gov/publications/discovery-blind-geothermal-system-southern-gabbs-valley-western-nevada-through |

### F3. Nevada: 146k driller reports, 9.8% carry a temperature, and the share is rising (my own API pull)
- The NDWR "Well Driller Reports" feature service is updated every business day from the Well Log database. It has a `temperature` field (in F; only 0.3% of values look like Celsius), plus depth drilled, static water level, yield, drawdown, owner and parcel number (https://arcgis.water.nv.gov/arcgis/rest/services/NDWR/Well_Driller_Reports/FeatureServer/0).
- Counts on 23 Oct 2026:

  | Item | Count |
  |---|---|
  | All driller reports | 146,235 |
  | With a temperature value | 14,282 (9.8%) |
  | Temperature 77 F (25 C) or more | 2,124 |
  | 86 F (30 C) or more | 1,202 |
  | 104 F (40 C) or more | 697 |
  | 140 F (60 C) or more | 279 |
  | Over 212 F | 21 |

- Reporting rate by completion era (wells with temperature divided by all wells):

  | Era | All logs | With temp | Share |
  |---|---|---|---|
  | 1980-1999 | 50,057 | 2,928 | 5.8% |
  | 2010-2014 | 11,338 | 503 | 4.4% |
  | 2015-2019 | 11,763 | 2,775 | 23.6% |
  | 2020-2026 | 14,280 | 3,726 | 26.1% |

  Something changed around 2015 (likely a new form or online filing; cause unverified). Nevada now adds about 900 driller temperatures a year.
- The 1,202 warm wells (30 C or more) have a median depth of 528 ft (161 m). By stated use they are domestic 382, monitoring 243, mining 110, municipal 94, test 92 and dewatering 83. They fall in 193 cells of about 10 km, and 91 of those cells hold a single warm well. They span 90 hydrographic basins.
- Apparent gradient. For 10,980 wells 50-1,000 ft deep, (T minus 15 C) divided by depth has a median of 20 C/km. 1,758 wells exceed 100 C/km and 851 exceed 200 C/km. These are crude: driller temperatures are usually pumped discharge water, which mixes the whole screened interval. They are still strong flags.
- **Isolated warm wells.** 697 of the 1,202 warm wells lie more than 10 km from any WQP well site at 35 C or more. Of those, 328 read 40 C or more. Top basins: 137B (76), 087 (43), 049 (31), 028 (23). My own analysis. Caveat: WQP misses many known fields, so some of these sit inside known areas like Moana (Reno). The next step is to screen them against the NBMG thermal springs and wells layer and the NDOM geothermal well table (D03).
- This matches the L02 audit, which found Nevada State Engineer water-well records "only 10% complete" for temperature plus depth.

### F4. California: 1.11 million digitized well reports, no temperature field
- The DWR Well Completion Reports resource on the California Natural Resources Agency CKAN has **1,111,251 records** (https://data.cnra.ca.gov/dataset/well-completion-reports, resource 8da7b93b). Fields include location, depths, perforations, static water level, drawdown and yield, plus a free-text `OTHEROBSERVATIONS` field. There is no temperature column. A text search of the remarks and the scanned logs for "hot", "warm" or degree values is the only route (unverified yield).
- USGS has published attributed subsets for selected areas (https://catalog.data.gov/dataset/attributed-california-water-supply-well-completion-report-data-for-selected-areas-der-2025).

### F5. Idaho keeps a curated thermal-well layer
- The IDWR GeothermalWells layer defines "low-temperature geothermal groundwater" as more than 85 F and under 212 F, and "geothermal" as 212 F or more. It stores min and max water temperature with date and source, plus well depth, use and discharge (https://gis.idwr.idaho.gov/hosting/rest/services/Groundwater/GeothermalWells/FeatureServer/0).
- Count on 23 Oct 2026: **739 wells, 179 of them at 140 F (60 C) or more.** My own query. Idaho regulates wells over 85 F as geothermal wells under its own rules (https://idwr.idaho.gov/wells/geothermal-wells/), so warm wells there are better documented than in Nevada.

### F6. Water Quality Portal (NWIS plus STORET): wide but sparse groundwater temperatures
- Counts of well sites with at least one "Temperature, water" result, from WQP response headers on 23 Oct 2026 (https://www.waterqualitydata.us/):

  | State | Well sites with temp | Results |
  |---|---|---|
  | CA | 15,880 | 54,586 |
  | AZ | 10,427 | 19,350 |
  | ID | 7,922 | 47,952 |
  | OR | 6,647 | 35,808 |
  | UT | 6,012 | 23,508 |
  | NM | 5,282 | 11,652 |
  | NV | 2,646 | 10,634 |

- Nevada has 18,993 WQP well sites, so only **14% have any temperature**. Nearly all of these are USGS NWIS sites (2,635 of 2,646).
- My Nevada and Utah pull:
  - **Nevada:** median site maximum 17.5 C. 937 sites are at 20 C or more, 352 at 25 C, 185 at 30 C, 69 at 40 C and 26 at 60 C. Median well depth is 43 m, and only 17% are deeper than 150 m. Most results date from the 2000s (6,278); there are only 170 from the 2020s.
  - **Utah:** median 15.0 C. 899 sites at 20 C or more, 231 at 25 C, 85 at 30 C and 22 at 40 C. Median depth is 76 m.
- Caveat: these are mostly single temperatures of pumped or bailed water taken during a water-quality sample. They are not profiles. WQP has also lagged on newer USGS data since the 2024 format change (unverified for these states).

### F7. Older compilations already exist and are partly stale
- **NBMG Great Basin Groundwater Geochemical Database v3.0:** 47,500 samples from 16,855 sites. More than 42,000 samples come from NWIS (downloaded 2005-2006). It also includes Mariner (over 400), Garside 1994 (over 450), the salvaged GEOTHERM (over 1,500 Nevada records) and the Geo-Heat Center (about 850). Temperature sits in a site sub-table (https://nbmg.unr.edu/Geothermal/GeochemDatabase.html). It was reused as the Utah FORGE Great Basin groundwater geochemical database (https://catalog-beta.data.gov/dataset/utah-forge-great-basin-groundwater-geochemical-database).
- **Geo-Heat Center / NBMG western thermal springs and wells:** 1,588 points across the western US, with TEMP_C, depth, chemistry and Na-K-Ca and SiO2 geothermometers. The state compilations mostly date from 1993-1994 (https://data.nbmg.unr.edu/Public/Geothermal/Data/GeothermalData/_metadata/HTML_Files/HotSpringsAndWells.html).
- **USGS legacy temperature logs in water wells**, for example western Utah (OFR 77-132, https://pubs.usgs.gov/publication/ofr77132) and the Nevada Test Site (DS 269, https://pubs.usgs.gov/publication/ds269). These are true profiles, but there are only hundreds of them.
- Read-through. The thermal-well lists were frozen around 1994-2006. Nevada alone has logged about 6,500 driller temperatures since 2015 that none of these compilations include.

### F8. Physics: why water-well temperatures mislead, and what that means
- Cold recharge and lateral flow can hide heat. The Railroad Valley USGS paper is the type case: a 125 C system sits inside the low-heat-flow "Eureka Low" (https://pubs.usgs.gov/publication/70205980). A cold well therefore does not prove there is no heat.
- Outflow plumes spread warm water tens of kilometres down-gradient (Newcastle's plume into Escalante Valley). A warm well therefore points at an upflow that may sit somewhere else, usually up the hydraulic gradient and on a fault.
- A driller temperature is a mixed discharge reading over the whole open interval. It is taken under pumping, sometimes after drilling heat or cooling, and with no stated method. Its error is probably +/-2-5 C, with occasional gross errors from units or a typo (unverified, by analogy with the M04 quality ladder).

## Datasets

| Dataset | Access | Coverage | Temperature content | Value for blind detection |
|---|---|---|---|---|
| NDWR Well Driller Reports | ArcGIS REST, free, updated daily (https://arcgis.water.nv.gov/arcgis/rest/services/NDWR/Well_Driller_Reports/FeatureServer/0) | 146,235 NV wells; mostly from 1984 | 14,282 single temperatures (F); about 26% of new wells | High. 1,202 warm wells, 697 of them isolated from known thermal water. Owner and parcel are included, which drives the rancher visit. |
| NDWR scanned well-log PDFs (WellLogReport link) | Free, per well | Same | Remarks such as "hot water" or "warm" in text (unverified frequency) | Medium. OCR could recover temperatures that were never keyed. |
| CA DWR Well Completion Reports (OSWCR) | CKAN API (https://data.cnra.ca.gov/dataset/well-completion-reports) | 1,111,251 reports | No field; free text only | Low to medium. Needs NLP on the remarks and scans. |
| IDWR GeothermalWells | ArcGIS REST (https://gis.idwr.idaho.gov/hosting/rest/services/Groundwater/GeothermalWells/FeatureServer/0) | 739 ID wells over 85 F | Min/max temp with date and source | Medium. Curated positives, good training labels. |
| Water Quality Portal (NWIS + STORET) | REST, free (https://www.waterqualitydata.us/) | About 54k well sites with temp in 7 states | Single temps, often repeated, with chemistry | High as a chemistry and temperature join. Low as profiles. |
| NBMG Great Basin groundwater geochem v3 | NBMG / Utah FORGE GDR | 16,855 sites, 47,500 samples | Site temperature plus full chemistry | High for geothermometers. Stale since 2006. |
| Geo-Heat Center thermal springs and wells | NBMG | 1,588 western points | TEMP_C plus geothermometers | Known positives (labels), not new targets. |
| USGS water-well temperature logs (OFR 77-132, DS 269, SMU heat-flow) | USGS Pubs, SMU node | Hundreds of profiles | Equilibrium profiles | Highest quality; few points. |
| UT Division of Water Rights, OR OWRD, NM OSE well logs | State portals | Each over 100k (unverified, H06) | Temperature field presence not checked here (unverified) | Unknown. Worth one API check per state. |

## What dominates uncertainty (this slice)
1. **Groundwater advection.** Cold recharge masks heat (false negatives), and outflow plumes move warm water away from the upflow (location error of up to tens of km). This matters more than measurement error.
2. **Whether a warm well is new information.** No one has yet joined the 697 isolated Nevada warm wells to the full list of known systems (Zanskar's 370 sites are not public). Novelty is the key unknown.
3. **Driller-temperature quality.** It is a single point with no method stated, taken from mixed pumped water. Error is probably a few C, with some gross errors. It is fine as a flag and poor as a gradient.
4. **Spatial selection bias.** Wells cluster in valleys, towns and farms. Ranges and fault footwalls have almost none. 90% of sampled cells have only wells shallower than 20 m (Edwards et al. 2025).
5. **Digitization gaps.** 90% of Nevada logs have no keyed temperature. California has no field at all. Other states were not checked here.

## What a sensor could fill
- **Re-log the isolated warm wells to equilibrium.** The H06 drop probe (T, P, conductivity) turns a +/-3 C mixed discharge reading into a 0.01 C profile. The shape of that profile tells conduction (linear) from upflow (convex) from outflow (a warm layer with cooling below, i.e. a temperature reversal). A reversal is the signature of a plume, and it tells you to look up-gradient. Nevada alone offers about 700 such wells, with owner and parcel already in the record.
- **Profile shape plus conductivity plus a water sample** gives Na-K-Ca, SiO2, B, Li and Cl/B geothermometers and mixing models, so each warm well yields a deep-temperature estimate, not just a shallow reading.
- **A time-series probe left in idle or monitoring wells** (243 of the warm Nevada wells are monitoring wells) separates seasonal and pumping effects from steady heat.
- **Fill the gaps between wells with 2 m probes** along the up-gradient fault, to find where the plume enters.
- New idea: **a "driller kit".** Give licensed Nevada drillers a free logging thermistor to run before casing, in exchange for the data. About 3,000-4,000 new wells a year are drilled in Nevada (from the counts above), and each would give a fresh bottom-hole and profile temperature at almost no cost (unverified uptake).

## Implications for a better model
1. **Ingest every water-well temperature, not just the warm ones.** Treat each as a heteroscedastic observation, with a quality class by source (equilibrium log, USGS sample, driller discharge temperature, text-mined remark) and a learned bias per class. Cold wells are information too, but treat them as censored, weak negatives because they may be masked.
2. **Add an advection layer.** Use the water table (NDWR static water level gives head at 146k points), hydraulic gradient and recharge areas to move warm-well evidence up-gradient toward the source fault. Use a simple "plume kernel" whose shape follows the head gradient instead of a round distance kernel.
3. **Build an "isolated warm well" feature and target list.** Anomaly equals well temperature minus the expected temperature at that depth from the regional background. Flag wells far from known systems. The Nevada list (697 wells, 328 at 40 C or more) is the first backlog for drop-probe visits.
4. **Text-mine the scans.** OCR the NDWR WellLogReport PDFs and the CA OSWCR remarks for words like "hot", "warm", "steam" and for degree values. This could multiply the warm-well set at near-zero cost (unverified yield).
5. **Use repeat-ingest as an edge.** Nevada adds about 900 driller temperatures a year, and the public thermal-well compilations stopped around 2006. A daily scraper of the NDWR service gives us new anomalies, with the owner's name, before anyone else looks.
6. **Calibrate on the positives.** Use Idaho's 739 curated thermal wells, the 1,588 Geo-Heat Center points and the named cases (Lightning Dock, Newcastle, Raft River) as labels to learn how far, and in which direction, warm wells sit from the upflow.
7. **Active learning.** Rank wells by expected information gain (high model variance multiplied by the chance the well is loggable without pulling the pump). Then send the field team, which signs the heat option on the same visit.

## Sources
- Edwards et al. 2025, Zanskar, SGW: https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Edwards.pdf
- NDWR Well Driller Reports service: https://arcgis.water.nv.gov/arcgis/rest/services/NDWR/Well_Driller_Reports/FeatureServer/0
- NV irrigation wells from NDWR database (USGS): https://catalog-beta.data.gov/dataset/irrigation-wells-from-the-nevada-division-of-water-resources-well-log-database
- CA DWR Well Completion Reports: https://data.cnra.ca.gov/dataset/well-completion-reports
- USGS attributed CA WCR: https://catalog.data.gov/dataset/attributed-california-water-supply-well-completion-report-data-for-selected-areas-der-2025
- IDWR GeothermalWells layer: https://gis.idwr.idaho.gov/hosting/rest/services/Groundwater/GeothermalWells/FeatureServer/0 ; https://idwr.idaho.gov/wells/geothermal-wells/
- Water Quality Portal: https://www.waterqualitydata.us/
- NBMG Great Basin Groundwater Geochemical Database: https://nbmg.unr.edu/Geothermal/GeochemDatabase.html
- Utah FORGE Great Basin groundwater geochem: https://catalog-beta.data.gov/dataset/utah-forge-great-basin-groundwater-geochemical-database
- Geo-Heat Center thermal springs and wells metadata: https://data.nbmg.unr.edu/Public/Geothermal/Data/GeothermalData/_metadata/HTML_Files/HotSpringsAndWells.html
- Lightning Dock: https://en.openei.org/wiki/Lightning_Dock_Area
- Newcastle UT: https://www.searchanddiscovery.com/abstracts/html/1990/rms/abstracts/1315c.htm ; https://pubs.usgs.gov/publication/70015244
- Railroad Valley heat flow: https://pubs.usgs.gov/publication/70205980
- Gabbs Valley: https://www.usgs.gov/publications/discovery-blind-geothermal-system-southern-gabbs-valley-western-nevada-through
- USGS western Utah well temperatures OFR 77-132: https://pubs.usgs.gov/publication/ofr77132
- USGS NTS groundwater temperatures DS 269: https://pubs.usgs.gov/publication/ds269
