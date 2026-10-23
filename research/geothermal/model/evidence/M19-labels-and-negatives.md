# M19: Labels and negatives. Where positive labels come from, where the missing negatives live, and how their absence bends every public model

Date: 23 Oct 2026. Slice M19, model track. This file builds on `M01` (USGS 2008 grid of 278 positive cells, "unlabelled = negative"), `M02` (INGENIOUS 403 known / 120 hot sites), `M13` (Zanskar's 370-site inventory, 1 blind system per ~550 holes), `M14` (Caraccioli expert-negative bias, PU learning, censored regression), `../../evidence/L13` (IFC and Wall & Dobson success rates), `../../evidence/L16` (Sass 1999 industry TG holes) and `../../evidence/D03` (NDOM well table, confidentiality law). It does not repeat their PU-learning theory. What is new here: (1) my own parse of the **CalGEM statewide geothermal well file** (4,346 wells, 2,008 TG holes, ~1,600 plugged holes outside any named field), which no prior file used; (2) a cross-tab of the **NDOM well table by type, status and field**, which isolates the 159 wells drilled outside any field; (3) the Wall & Dobson Nevada permit funnel (292 TG permits, 134 drilled, 31% project success) as the size of the "tried and failed" pool; (4) a concrete label schema with five label grades instead of two. Web budget used: 8 searches, 8 fetches. The NBMG ArcGIS server failed TLS, so NBMG's own well layer is covered only through NDOM.

## Bottom line

Every public geothermal favorability model is trained on the wrong question. Positives are "places where someone noticed hot water", and about 60% of known Great Basin systems were noticed because water reached the surface. Negatives are either missing (USGS 2008: every one of ~710,000 unlabelled cells called negative), hand-picked (NVML: 62 expert negatives, shown to bias the map), or shallow cold wells that only prove "cold above 20 to 250 m" (Zanskar GeoCore). The real negatives do exist, and they are public: the **plugged temperature-gradient holes and failed exploration wells** that state regulators already hold. In California alone CalGEM lists **2,008 TG holes, 1,586 of them plugged**, plus about 2,190 geothermal wells not assigned to any named field. Nevada's NDOM lists **159 wells drilled outside any field (124 TG holes, 61 of them plugged)**, all past the 5-year confidentiality window, plus 786 Phillips/Chevron industry TG holes in USGS OFR 99-425. These holes are "hard negatives": they sit exactly where an expert thought a system might be, which is the decision boundary a blind-system model must learn. Nobody has turned them into a graded, depth-tagged label set. Doing so (roughly 3,000 to 5,000 depth-censored labels across CA, NV, UT, OR) is the single cheapest model upgrade available, and our ranch-well probe plus a slim re-logging tool for still-open holes turns the rest of "unlabelled" into "searched to depth d, max T = x". That is the label set Zanskar does not publish and INGENIOUS does not have.

## Findings

### F1. Positive label sets: four lists, different definitions, none built for blind systems
- **USGS 2008 identified systems.** Williams et al. 2008 (Fact Sheet 2008-3082) assessed 248 identified moderate- and high-temperature systems (90 °C or hotter) in 13 states (count per L02; some USGS text says 241, unreconciled). The point file is "Identified Moderate and High Temperature Geothermal Systems", DeAngelo and Williams 2010, doi:10.5066/P1YJWMFC, https://sciencebase.gov/catalog/item/get/6606f534d34e4df16bd58277 . Gridded to 2 km cells this became the **278 positive cells** used in 2008 and again in Mordensky et al. 2023 (data release doi:10.5066/P9V1Q9XM, https://data.usgs.gov/datacatalog/data/USGS:63090a9cd34e3b967a8c19c4).
- **Faulds / INGENIOUS known geothermal systems (KGS).** 403 KGS at 37 °C or hotter and 120 "training sites" at 120 °C or hotter (Faulds et al. 2026, SGW 51, https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Faulds.pdf). The 37 °C threshold was chosen because it is "hot to the touch" (Coolbaugh 2003). 17.1% of KGS have no favourable structural setting; they are "mostly isolated hot or warm wells in basins". The paper names **no negative or control set at all**.
- **Zanskar inventory.** 370 sites at 90 °C or hotter, 258 with surface features and 112 blind (M13). Not released as a file.
- **Producing fields.** About 60 to 65 named fields across CA and NV (CalGEM file has 23 named geothermal fields; NDOM has 63 field codes, many of them sub-areas). EIA-860 lists the generating plants (unverified exact count, roughly 90 to 100 geothermal generators). Producing fields are the only labels with a measured outcome (MW), and Trainor-Guitton et al. 2025 used 37 nameplate capacities against 248 zero-MW sites (M02).
- **The blind share in the labels.** About 39% of known Great Basin systems are blind (Faulds and Hinz 2015, via L02), while about 75% of all resources are thought to be blind (Coolbaugh et al. 2007). So the positive set under-represents the target class by roughly half. A model trained on it learns "springs plus structure", not "heat under a cold lid".

### F2. The negative pool is large, public and unused: CalGEM (my parse)
Source: CalGEM Geothermal Wells, CC BY, https://catalog.data.gov/dataset/calgem-geothermal-wells (CSV from https://gis-cnra.hub.arcgis.com/datasets/cadoc::calgem-geothermal-wells ; REST https://gis.conservation.ca.gov/server/rest/services/WellSTAR/Wells/MapServer/1). Downloaded 23 Oct 2026.
- **4,346 geothermal wells.** By type: 2,008 temperature gradient, 618 developmental steam, 482 injection, 406 developmental water, 254 commercial low-temperature, 249 non-commercial low-temperature, 140 exploratory water, 106 observation, 41 exploratory steam.
- **By status:** 2,039 plugged, 1,377 active, 341 cancelled, 297 idle, 175 unknown, 26 relinquished.
- **TG holes:** 1,586 plugged, 160 cancelled, 138 unknown, 92 active, 30 idle. **Exploratory water wells:** 86 plugged, 25 idle. **Exploratory steam:** 33 plugged of 41.
- **Not assigned to any named field:** about 2,190 wells (about 1,600 plugged). Counties: Imperial 954, Lake 398, Sonoma 196, Mono 112, San Bernardino 77, Mendocino 63, Lassen 57, Siskiyou 57, Modoc 53. Many Imperial and Lake holes are field-margin step-outs; the Lassen, Modoc, Siskiyou, Mono, San Bernardino and Inyo holes are mostly true wildcat prospects (inference).
- **676 wells still flagged confidential**, 3,670 not. Well records (temperature logs, completion reports) are in CalGEM's WellSTAR and GeoSteam online records (https://www.conservation.ca.gov/calgem/geothermal/geosteam/Pages/geothermal_owr_help.aspx), as scanned files.
- What this means: a plugged TG hole outside a field is the closest thing to a real negative that exists. Each has a known location, depth and (in the scanned record) a temperature log. That is roughly 1,600 hard negatives in one state, against 23 named fields.

### F3. Nevada: NDOM's "EXP" wells are the state's failed-prospect list (my parse)
Source: NDOM "Geothermal Production And Well Data, 09/29/2026" (ArcGIS item dcccb7e35aee4885aa4e2aed84b505cf, https://www.arcgis.com/sharing/rest/content/items/dcccb7e35aee4885aa4e2aed84b505cf/data). D03 gave the status totals; the cross-tab is new.
- **Type by status (938 wells):** TG holes: 122 expired, 70 plugged and abandoned (P&A), 55 in use, 9 pending, 5 shut-in. Observation wells: 43 P&A. Industrial production: 6 P&A, 75 shut-in. Industrial injection: 10 P&A, 31 shut-in.
- **159 wells carry field code EXP (exploration, no field):** 124 TG (61 P&A, 55 expired permits, 4 in use), 29 observation (13 P&A), 5 production-class. Operators: Ormat 56, Standard Steam 28, NBMG 21, Nevada Geothermal Power 12, Rockwood Lithium 10, City of Wells 5, Magma Energy 4. Completed mostly 2005 to 2019 (43 in 2006-2010, 26 in 2016-2020). Counties: Elko 34, Nye 25, Pershing 18, Mineral 18, Esmeralda 17, Humboldt 17, Lander 14. Land: 125 BLM/USFS, 34 private.
- All are past the 5-year confidentiality window (NRS 534A.031), so their completion reports and **temperature logs (required, NAC 534A.550)** are public on request from NDOM (D03).
- **Field-margin P&A wells** are a second negative class: SEM (San Emidio) 9, SDL 9, COM 12, BHS 6, STW 5. These are "edge of a known system" negatives, which teach the model where a system ends.

### F4. Nevada permit funnel: the size of the "tried and failed" pool (Wall and Dobson 2016)
Wall, A.M. and Dobson, P.F. 2016, "Refining the Definition of a Geothermal Exploration Success Rate", SGW 41, https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2016/Wall2.pdf
- Nevada 2005-2015: **292 TG permits, about 158 expired or cancelled, 134 drilled.** 32 projects did exploration drilling; only **10 went on to production permits**.
- Success: exploration drilling 42% per well, **31% per project**; production drilling 40%; combined about 16 to 21%.
- **Survivorship bias in the standard numbers:** the IFC study (about 60% exploration-phase success, https://www.thinkgeoenergy.com/global-study-on-success-of-drilling-geothermal-wells-by-ifc/) used mostly large developed fields; only 7 of 57 fields had fewer than 10 wells. Nevada counts idled wells as successes unless plugged.
- The authors found **"no single repository of project information"**. That is still true. So about two-thirds of drilled Nevada prospects 2005-2015 (about 22 projects) are negatives-at-project-level that no public model uses.

### F5. Older negatives: the 1970s-80s industry TG archive
- Sass et al. 1999, USGS OFR 99-425 (https://pubs.usgs.gov/of/1999/of99-425/webmaps/home.html): 786 holes, 82 prospects (L16). 54 of 82 prospects never exceeded 10 °F/100 ft. These are "looked, mostly lukewarm" prospects, the right material for graded negatives.
- Chevron and Phillips evaluated more than 100 prospects; DOE bought data for only "several hundred" holes. The rest of the CalEnergy archive appears unreleased (L16, inference). This is the largest private negative archive in the Great Basin and is a data-purchase target.
- DOE Industry-Coupled Program (1977 onward, 14 sites in NV and UT) required data release (L16). Several sites (e.g. those that never produced) are documented failures with logs at OSTI.

### F6. Other places negatives live
| Source | What kind of negative | Access |
|---|---|---|
| Oil and gas dry holes with BHTs (NV NDOM 775 wells, UT DOGM 536 Great Basin wells, SMU/AASG BHT compilations) | Deep, mostly cool, mostly in basins: "easy negatives" (D03, M04) | Public; logs scanned |
| Mining exploration holes | Shallow, dense, usually unlogged for T; occasionally the reason a blind system was found (McGinness Hills) | Mostly private (L16) |
| Water wells (state well logs, USGS NWIS temps) | Very shallow; cold readings are censored, not negative (M06) | Public |
| BLM geothermal leases relinquished or terminated (MLRS/LR2000) | Weak project-level negative: someone held it and walked away | Public but needs serials to be joined to drilling |
| GRC Transactions and Stanford SGW case papers | Narrative negatives (e.g. Argenta Rise: 139 two-metre probes and 10 TG wells, no anomaly, M02/M11) | Public, unstructured |
| OSTI DOE final reports (play fairway, ICP, GTP cost-share wells) | Failed or sub-commercial wells with full logs | Public, PDF |
| Washington PFA hole MSH17-24 | A deliberate negative-control hole | GDR 1333 (M03) |

### F7. How the missing negatives bias every public model
1. **Unlabelled treated as negative (USGS 2008, Mordensky 2023).** About 2,600 unlabelled cells per positive. Blind systems sitting in favourable but unexplored cells are trained as "no", which pushes the map toward known, spring-bearing districts. F1 below 0.04 to 0.10 in every model (M14, L03).
2. **Expert negatives (NVML, 62 sites).** Picked because they are obviously cold, often deep oil wells in basins. The model learns "basin centre vs range-front fault", a boundary everyone already knows (Caraccioli et al. 2023, https://pubs.usgs.gov/publication/70251035).
3. **Shallow cold wells as negatives (Zanskar GeoCore, depth thresholds 10 and 150 m; Z03).** These are right-censored observations, not negatives. Under a cold aquifer (Railroad Valley, Argenta) they create false negatives exactly over blind systems (M06, M13).
4. **No negatives at the decision boundary.** The useful negative is "good structure, someone drilled, still cold to 500 m". Only exploration holes provide that. Without them, models cannot separate step-overs that host heat from step-overs that do not, which is why INGENIOUS's 1,430 favourable settings cover 7.7% of the Great Basin and still cannot rank within that 7.7% (M02).
5. **Survivorship in outcome data.** Success-rate and MW models trained on developed fields overstate success and ignore the 69% of drilled Nevada projects that stopped (F4).
6. **Label-definition drift.** Positives at 37, 39, 90, 120 or 150 °C, cells at 2 km or 250 m, systems or wells. Mixing them blurs the target. Cold labels have no definition at all.

### F8. A five-grade label scheme that uses all of this
Instead of positive/negative, give each observation a temperature-at-depth constraint and an effort tag:
- **G1 Confirmed system:** producing or flow-tested at 120 °C or more (producing fields, ~120 INGENIOUS hot sites).
- **G2 Warm, open-ended:** T at depth d above background, system not bounded (KGS 37-120 °C, warm water wells, warm TG holes). Left-censored "at least T".
- **G3 Hard negative:** exploration TG or slim hole in a favourable setting, equilibrated log, conductive (straight) profile, gradient near background to depth d of 150 m or more (CalGEM plugged wildcat TG, NDOM EXP P&A, Sass lukewarm prospects). Right-censored "at most T to depth d", with a likelihood that also covers deeper heat.
- **G4 Masked / ambiguous:** cold but curved or reversed profile, or under a known cold aquifer. Not a negative; flags outflow.
- **G5 Searched-absent at shallow depth:** 2 m probes, shallow water wells. Weak effort-weighted evidence only.
- Train a censored regression for T at 500 m and 1.5 km, plus a detection (effort) model, as in M14/M15. The G3 set is what makes the effort model identifiable.

## Datasets table

| Dataset | Access | Coverage | Value for blind detection |
|---|---|---|---|
| CalGEM Geothermal Wells (WellSTAR layer 1) | Free CSV/REST, CC BY; logs in GeoSteam/WellSTAR scans | CA, 4,346 wells, 2,008 TG | ~1,600 plugged holes outside named fields: largest public hard-negative pool |
| NDOM Geothermal Production and Well Data (09/29/2026 xlsx) | Free; logs on request (public after 5 yr) | NV, 938 wells, 63 field codes | 159 EXP wells, 61 P&A TG; field-margin P&A wells as edge negatives |
| USGS OFR 99-425 industry TG holes | Free xls | NV/UT/OR, 786 holes, 82 prospects | Graded labels; 54 prospects never above 10 °F/100 ft |
| CalEnergy / Chevron / Phillips unreleased TG archive | Private; buy or swap for carry | 100+ prospects | Biggest private negative set in the Great Basin |
| USGS identified systems (doi:10.5066/P1YJWMFC) | Free shapefile | US, ~248 systems | Standard positive set; spring-biased |
| Mordensky & DeAngelo 2023 features and labels (doi:10.5066/P9V1Q9XM) | Free | Western US 2 km grid, 278 positive cells | Baseline to beat; shows the PU problem |
| INGENIOUS KGS and training sites (GDR 1391, Faulds 2026) | Free | Great Basin, 403 KGS, 120 hot | Better positives; no negatives |
| NVML / Nevada PFA ML (GDR 1351) | Free | NV, 83 pos / 62 expert neg | Example of biased negatives |
| Utah DOGM well file; NV NDOM oil and gas wells | Free; scanned logs | UT 536 Great Basin wells; NV 775 | Deep basin BHT negatives (easy negatives) |
| BLM MLRS geothermal lease case files | Free | Federal land | Relinquished leases as weak project negatives |
| Wall & Dobson 2016 permit funnel | Paper | NV 2005-2015 | Base rate: 31% project success after drilling |

## What dominates uncertainty

1. **Depth censoring of cold holes.** Most TG holes are 100 to 300 m (median 300 ft in OFR 99-425). Whether "cold at 150 m" means "no system" or "masked system" decides whether a hole is G3 or G4. Without the full T-z curve, this is unknown.
2. **Unknown share of the negatives that are actually masked positives.** If even 5 to 10% of plugged wildcat TG holes overlie blind systems under cold aquifers, hard-negative training suppresses exactly the targets we want.
3. **Selection of where people drilled.** Exploration holes are concentrated near springs and known fields (Imperial, Lake counties). The negative set is spatially biased too, just in a different direction from the positives.
4. **Digitisation.** Temperatures sit in scanned PDFs. Until the logs are extracted, each hole is only "drilled, abandoned", which is a weak project-level label.
5. **Missing private archive.** The CalEnergy/Chevron/Phillips remainder and post-2005 private TG data that was never filed (BLM does not require reporting of off-lease exploration, D03).

## What a sensor could fill

- **Turn censored negatives into real ones.** A slim wireline temperature logger (0.01 °C, 25 to 50 mm OD, 300 to 600 m cable) re-logs every **still-open** TG, observation and idle exploration well at equilibrium: CalGEM has 92 active and 30 idle TG holes and 25 idle exploratory water wells; NDOM has 55 in-use TG and 114 in-use observation wells. Decades after drilling, these holes are fully equilibrated, so one log gives a clean conductive-or-curved profile. This converts G4/G5 into G3 or G2. It is the same instrument as the ranch-well drop probe from the hardware pick, with a longer cable and a slim-hole sonde. (Access needs operator or landowner permission; unverified how many are physically open.)
- **Effort tags for the occupancy model.** Every probe visit, positive or not, is logged as "searched to depth d, max T, profile shape". This is the effort data that makes PU learning identifiable (M15). Publishing nothing and keeping these labels private is the moat.
- **Profile-shape sensing.** Logging up and down at 0.5 m spacing resolves reversals that flag outflow. That splits "cold, no system" from "cold lid over a system", which is the largest single source of false negatives (M06, M13).
- **Cheap deepening.** Where a hard negative sits in a top-ranked structural setting, an E-field MT node line (hardware pick) tests whether conductive clay cap exists below the cold hole. A cap with no heat at 200 m becomes G4, not G3.

## Implications for a better model

1. **Build the hard-negative table first.** Join CalGEM (2,008 TG), NDOM (261 TG, 159 EXP), OFR 99-425 (786), Utah DOGM and OSTI case reports into one table with location, depth, status, and (after text extraction of scanned logs) max T and profile shape. Target: 3,000 to 5,000 depth-tagged observations. Cost is mostly LLM document extraction, which is cheap for us.
2. **Replace binary labels with the five-grade censored scheme (F8).** Model T at depth with Tobit-style likelihoods; never call a shallow cold hole "no system".
3. **Fit an exploration-effort model jointly.** Use drill-hole density, spring proximity, roads and lease history to estimate P(found | system). The hard negatives make it identifiable, because they are places with high effort and no find.
4. **Validate on blind hold-outs, not hot springs.** Hold out by region (spatial blocks) and score on blind systems only (Zanskar's 112, or the 49 found by drilling). Report how many G3 holes the model wrongly ranks high: that is the false-positive rate that costs money.
5. **Use field-margin P&A wells to learn system size.** Plugged step-outs at San Emidio, Steamboat, Salt Wells and similar give the edge of known systems. That trains the model on footprint (1 to 5 km), which also sets how big a land block to lock.
6. **Buy the private negative archive.** Offer CalEnergy successors and defunct-operator estates a carry or override for their TG files. A failed operator's cold holes are worth little to them and a lot to a model.
7. **Feed the leasing engine.** A cell with a G3 hard negative at depth in a top setting should be dropped from the lease list; a cell with only G5 shallow negatives should not. This directly cuts wasted lease spend in the BLM noncompetitive and ranch-option programme.

## Sources
- CalGEM Geothermal Wells: https://catalog.data.gov/dataset/calgem-geothermal-wells ; https://gis-cnra.hub.arcgis.com/datasets/cadoc::calgem-geothermal-wells
- NDOM geothermal well data: https://www.arcgis.com/sharing/rest/content/items/dcccb7e35aee4885aa4e2aed84b505cf/data
- Wall and Dobson 2016: https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2016/Wall2.pdf
- IFC 2013 global drilling study summary: https://www.thinkgeoenergy.com/global-study-on-success-of-drilling-geothermal-wells-by-ifc/
- Faulds et al. 2026, SGW: https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Faulds.pdf
- USGS identified systems: https://sciencebase.gov/catalog/item/get/6606f534d34e4df16bd58277
- Mordensky and DeAngelo 2023 data release: https://data.usgs.gov/datacatalog/data/USGS:63090a9cd34e3b967a8c19c4
- Caraccioli et al. 2023: https://pubs.usgs.gov/publication/70251035 ; https://par.nsf.gov//servlets/purl/10536402
- Sass et al. 1999 OFR 99-425: https://pubs.usgs.gov/of/1999/of99-425/webmaps/home.html
- Williams et al. 2008: https://pubs.usgs.gov/fs/2008/3082
- Shevenell and Calvin, NV resource utilisation (DOE peer review): https://www.energy.gov/sites/default/files/2014/02/f7/analysis_shevenell_calvin_resource_utilization_nevada.pdf
