# L01: Geothermal play-fairway analysis (PFA): the DOE GTO programme 2014-2021, validation drilling, hit rates, and what happened next

## TL;DR
- DOE's Geothermal Technologies Office (GTO) funded **11 PFA projects in Phase 1 (2014-15, desktop work on existing data), 6 in Phase 2 (2015-17, new field data) and 5 in Phase 3 (2017-21, validation drilling)**. The Phase 3 projects were Nevada/Great Basin (UNR), Snake River Plain (USU), Washington Cascades (WA DNR), Hawaii (UH) and Eastern Great Basin/Utah (U of Utah EGI). [DOE PFA page]
- Validation drilling was **shallow and cheap**: temperature-gradient (TG) holes of roughly 150-320 m, plus one ~618 m slim well and one 1,057 m deepening. NREL's 2023 best-practices report says **four teams drilled TG wells at seven plays and found anomalously high temperatures or gradients at four of them (~57%)**. The Utah team drilled nothing: its USGS driller pulled out at the last minute over the expected temperatures and H2S.
- The best result was a **genuinely blind system in SE Gabbs Valley, NV: 124.9 °C at 152 m, an anomaly at least ~2 km x 1 km, and P90/P50/P10 = 6/16/38 MWe**. A second probable blind system was found in N Granite Springs Valley, NV (~96 °C at ~240-250 m).
- **The researchers did not take the land. Industry did.** UNR's final report says the project "helped to stimulate the largest geothermal lease sale in Nevada history in September 2019" and that "several of the promising areas identified on our geothermal play fairway map … were leased." In that sale 102,403 acres drew bids. High bids summed to $426,955, or **about $4.17/acre**, and the highest bid was **$20/acre**. Most parcels sold at the $2/acre minimum. Ormat and Western States Environment & Resources each won 11 parcels.
- By 2026 the window had shut. BLM nominations went from 25,800 acres (2020) to more than 1 million acres (2025). 2026 sales cleared at **$701/acre (NM) and $1,207/acre (UT)**. Even the Nevada PFA's two "discoveries" (2018-19) had not been deep-drilled as of the final report: "final validation … awaits deeper drilling."

## Programme structure (DOE GTO)
- Method: adapted from oil and gas "common risk segment" mapping. Teams combine heat, permeability and fluid/seal evidence layers, each paired with a confidence layer, into favourability maps, then narrow from regional to prospect scale.
- Phase 1, 2014-2015: 11 projects covering the Aleutians/Cascades, Appalachian low-temperature, Cascades/central Cascadia, Eastern Great Basin, Hawaii, Modoc Plateau, Nevada, Rio Grande Rift/hydrogeologic windows (LANL), Snake River Plain, Tularosa Basin and Washington. Phase 2, 2015-2017: 6 projects. Phase 3, 2017-2021: 5 projects. Source: https://www.energy.gov/eere/geothermal/play-fairway-analysis and https://gdr.openei.org/pfa
- Funding was small. The Nevada project's total budget was **$2,824,992** over all phases ([2017 peer review deck](https://www.energy.gov/sites/prod/files/2017/12/f46/3_2_Play%20Fairway_Nevada%20Bureau%20of%20Mines%20and%20Geology_Discovering%20Blind%20Geothermal_Presentation.pdf)), with **$1.5M for Phase 3** ([ThinkGeoEnergy 2017](https://www.thinkgeoenergy.com/?p=32198)). Washington's Phase 2 cost **$0.7M** (GDR record via search; https://gdr.openei.org/submissions/994). Phase 1 was reportedly "up to $4M for 11 projects" (ThinkGeoEnergy; DOE FOA amount unverified).

## Primary sources reviewed

### 1. Faulds, Hinz, Coolbaugh, Ayling, Glen, Craig, McConville, Siler, Queen, Witter, Hardwick (2019/2021), *Discovering Blind Geothermal Systems in the Great Basin Region … All Phases*, DOE final report DE-EE0006731, OSTI 1724080, DOI 10.2172/1724080
URL: https://www.osti.gov/servlets/purl/1724080 (full text read); USGS record https://www.usgs.gov/publications/discovering-blind-geothermal-systems-great-basin-region-integrated-geologic-and
- **Phase 1:** 9 parameters were combined over a **96,000 km² (240 x 400 km)** transect of Nevada. Inputs were structural setting, age of Quaternary faulting, slip rate, regional strain rate, slip and dilation tendency, earthquake frequency, gravity, temperature at 3 km, and spring/well temperatures. Weights were set by experts. The map was benchmarked against **34 known systems hotter than 130 °C** and 14 power plants. It flagged **~375 favourable structural settings covering ~12% of the area (>11,000 km²)**, which is "target rich".
- **Phase 2:** 24 prospects were narrowed to 5: S Gabbs Valley, Granite Springs Valley, Sou Hills, Crescent Valley and Steptoe Valley. The narrowing **explicitly used land status, sage-grouse habitat, transmission within ~20 km, and "potential for industry collaboration"**. Teams collected 237-415 new gravity stations per area, bought and reinterpreted 540 km of legacy oil and gas seismic reflection lines, and ran 2 m temperature surveys (292 stations) and lidar. Geothermometry indicated more than 130 °C in all 5 areas. Ormat and US Geothermal supplied company water analyses, gravity and magnetics (728 Ormat gravity points, ~145 line-km of Ormat magnetics).
- **Phase 3:** 12 TG holes, about 150-250 m deep.
  - SE Gabbs Valley: 6 holes, with BHTs of **124.9 °C and 114.4 °C at 150 m** (holes 52-2 and 31-2). The anomaly is at least ~2 km N-S by ~1 km E-W. The system is completely blind, with no prior exploration. The resource estimate is **P90 6 MWe, P50 16 MWe, P10 38 MWe**, using 135/150/175 °C and 3/6/12 MWe/km² power densities.
  - N Granite Springs Valley: 6 holes, up to **~96 °C at ~240-250 m**, with isothermal (convective) segments. The site is on public land.
- **Hit rate:** 2 of 2 drilled sites returned positive anomalies, although capacity is unproven.
- **Aftermath (key quote, p. 60-61):** the project "helped to stimulate the largest geothermal lease sale in Nevada history in September 2019 … Several of the promising areas identified on our geothermal play fairway map (Figure 1) were leased for potential geothermal development." The wells were then capped. The team's stated position was "It's not our job to develop the resource" ([Renewable Energy World 2019](https://www.renewableenergyworld.com/?p=218009)).
- **Lessons learned:**
  - Each prospect splits into several structural targets at finer scale.
  - Basin prospects cannot be recognised without detailed geophysics.
  - The PFA must be re-run at each scale.
  - Weights of influence, incomplete data and few training sites were the main limits, and machine learning was flagged as the fix.

### 2. Faulds, Craig, Hinz, Coolbaugh, Glen, Earney, Schermerhorn, Peacock, Deoreo, Siler (2018), "Discovery of a blind geothermal system in Southern Gabbs Valley … through application of PFA at multiple scales," *GRC Transactions* 42
URL: https://pubs.usgs.gov/publication/70201803 ; https://publications.mygeoenergynow.org/grc/1033921.pdf
- The paper lists the collocated evidence: a displacement-transfer zone with fault intersections, Quaternary faults, intersecting gravity gradients, a magnetic low, a 2 m temperature anomaly, a low-resistivity zone, and geothermometry from water wells. Six TG holes reached about 120-124 °C at about 150 m. It is the first PFA-led blind discovery. Follow-up: Craig et al. (2021), *Geothermics*, "Discovery and analysis of a blind geothermal system in southeastern Gabbs Valley" (https://www.sciencedirect.com/science/article/abs/pii/S0375650521001371). The abstract was not read directly (403), so its numbers are taken from the final report above.

### 3. Steely, Cladouhos, Davatzes, Allen (Forson), Swyer, … Norman, Glen, Burns, Stelling, Tanner (2021), *Washington State Geothermal Play-Fairway Analysis, Phases 1-3*, DOE EE0006728, OSTI 1823116
URL: https://www.osti.gov/biblio/1823116 ; https://gdr.openei.org/submissions/1333
- Target areas were Mount Baker, the St Helens Seismic/Shear Zone and Wind River Valley. Phase 2 cost $0.7M and covered 1:24k mapping, 15 geophysical surveys and 2 passive-seismic surveys.
- **Phase 3, two cored holes:**
  - **MB76-31 (Mt Baker, 1,471 ft / 448 m):** a **64 °C/km** gradient and 141-159 mW/m² heat flow, more than twice the regional value. Core and image logs showed predicted permeability. This was a high-favourability site, so it counts as a positive result.
  - **MSH17-24 (St Helens, 1,053 ft / 321 m):** ~15 °C/km, which is background, and meteoric water. This was a low-favourability site, so it is also "consistent with the model."
- The authors call this "reasonably positive validation." **No commercial follow-up:** in 2025 Washington said it had "no plans for development of geothermal energy projects" ([ThinkGeoEnergy](https://www.thinkgeoenergy.com/washington-state-to-lead-collaborative-process-for-early-stage-geothermal-studies/)).

### 4. Shervais et al. (2020), "Play Fairway Analysis in Geothermal Exploration: The Snake River Plain Volcanic Province," Stanford Geothermal Workshop SGP-TR-216; Shervais et al. (2021) SRP PFA Final Report (GDR 1316)
URL: https://pubs.usgs.gov/publication/70211876 ; https://gdr.openei.org/submissions/1316
- This project is the clearest statement of the CRS method. It builds Common Risk Segment maps for **heat, permeability and seal**, each built from evidence x confidence layers, then combines them into a composite CRS map of southern Idaho using an automated ArcGIS/Python workflow.
- Prospects named were the western SRP, central-plain lineament intersections and the eastern margins. Mountain Home and Camas Prairie were studied in detail, and Camas Prairie was chosen for Phase 3.

### 5. Lachmar, Neupane, Garg, Shervais, Mink, et al. (2023), "Validation of Play Fairway Analysis of the geothermal potential of Camas Prairie, south-central Idaho, by an exploration well," *Geothermal Energy* 11, DOI 10.1186/s40517-023-00264-4
URL: https://geothermal-energy-journal.springeropen.com/articles/10.1186/s40517-023-00264-4 (abstract read via DOAJ/search)
- The USU Camas-1 well reached **618.3 m** and was drilled in fall 2018 and fall 2019. It hit a permeable zone at ~357.5 m with a maximum measured temperature of **~80 °C**. The well has moderate transmissivity and a lacustrine clay seal in the upper 314 m. Geothermometers indicate a reservoir of **~120 °C**.
- **Conclusion:** the PFA prediction of permeability and seal was "validated," but the resource is probably **too cool for power and is likely a direct-use/heating play**. Technically this is a hit; commercially it is a miss for electricity.

### 6. Lautze, Thomas, Hinz, Apuzen-Ito, Frazer, Waller (2017), "PFA of geothermal resources across the State of Hawaii: 1. Geological, geophysical, and geochemical datasets," *Geothermics* 70, DOI 10.1016/j.geothermics.2017.02.001; Ito et al. (2017) Part 2 (statistical method); Lautze, Ito, Thomas, Frazer, Martel, Hinz, Tachera, Hill, Pierce, Wannamaker, Martin (2020), Part 4, *Geothermics* 86:101798
URLs: https://www.soest.hawaii.edu/GG/FACULTY/ITO/Lautze_etal_Geothermics17_PlayFairway_I.pdf ; https://www.osti.gov/pages/biblio/1799234
- Heat, permeability and fluid were combined in a Bayesian or weighted probability-and-confidence framework. Part 4 added MT resistivity, density and topographic stress.
- **Top drilling targets were Lana'i and SE Mauna Kea.** Phase 3 deepened **Lana'i Well 10 from 427 m to 1,057 m** (May-July 2019, near-continuous core). It found a **42 °C/km gradient** (more than twice Hawaii background) and a **66 °C BHT** ([GDR 1411](https://gdr.openei.org/submissions/1411)). The result is anomalous but sub-commercial, with no industry follow-up found (unverified).

### 7. Wannamaker, Moore, Nash, Simmons, Maris, Mendoza (2020), *Play Fairway Analysis: Structurally Controlled Geothermal Systems in the Eastern Great Basin Extensional Regime, Utah*, OSTI 1695591
URL: https://www.osti.gov/biblio/1695591 (Phase 2: OSTI 1493758)
- Phase 2 covered Twin Peaks rhyolite, north of Cove Fort, and Crater Knoll, using MT, He isotopes and geology. Phase 3 refined a target in northern Cove Fort, with planned 2,000-3,000 ft holes.
- **The drilling was cancelled at the last minute** because the expected temperature and H2S were "outside the experience base of the USGS-RDP" driller. **The hit rate is 0 drilled.** The episode shows how a non-commercial operator struggles to drill hot targets.

### 8. Bennett, Nash, Barker (2020), *Convergence of Heat, Groundwater & Fracture Permeability: PFA Applied to the Tularosa Basin*, Ruby Mountain Inc./U of Utah, OSTI 1782479
URL: https://www.osti.gov/biblio/1782479
- The project reached Phase 2 only. It pointed to a possible system at White Sands Missile Range similar to McGregor Range, with DoD funding sought for TG drilling ([2017 deck](https://www.energy.gov/sites/prod/files/2017/12/f46/3_2_Play%20Fairway_Ruby%20Mountain_The%20Convergence%20of%20Heat%20Groundwater_Presentation.pdf)). The land is military, so it is **not acquirable** by a private rights buyer.

### 9. Pauling, Taverna, Trainor-Guitton, Witter, Kolker, Warren, Robins, Rhodes (2023), *Geothermal Play Fairway Analysis Best Practices*, NREL/TP-5700-86139
URL: https://www.nrel.gov/docs/fy23osti/86139.pdf (the host was unreachable from this environment; content comes from search-engine extracts, so treat details as lightly verified)
- Programme-wide: 5 teams were chosen for drilling. **4 completed TG drilling at 7 plays and found anomalously high temperatures or gradients at 4.** NREL also states that the PFA projects "directly informed several federal geothermal lease nominations."

### 10. Smith, Faulds, Brown, Coolbaugh, DeAngelo, Glen, Burns, Siler, Treitel, Mlawsky, Fehler, Gu, Ayling (2023), "Exploratory analysis of ML techniques in the Nevada geothermal PFA," *Geothermics* 111:102693
URL: https://pubs.usgs.gov/publication/70241433
- The study re-ran the Nevada PFA with Bayesian probabilistic neural networks (maps with confidence intervals) and PCA plus k-means. It used positive training sites and **negative sites: known drill holes with unsuitable conditions**. The 2020 preliminary version cited ~85 active systems as training sites and more than 12 features. The models found "previously unrecognized controls" on favourability. This is the bridge from expert-weighted PFA to ML.

### 11. Mordensky, Burns, Lipor, DeAngelo (2025), "Favorability Mapping for Hydrothermal Power Resource Assessments of the Great Basin," *Geothermics* 133:103450
URL: https://www.usgs.gov/publications/favorability-mapping-hydrothermal-power-resource-assessments-great-basin-usa
- This is the current USGS state of the art, built on INGENIOUS data. It uses **~10x more training sites**, positives weighted by convective upflow strength, and Monte Carlo cross-validation. It places **15 of 28 producing systems (54%) in the top 1% of map area and 26 of 28 (93%) above the 80th percentile**. Earlier PFA/2008 maps put only about half in the top 20%. Mordensky et al. (2023, *Geothermics* 102662) also found that **more complex ML does not necessarily beat simple models**: the "When less is more" result.
- The successor programme is **INGENIOUS** (UNR-led, DE-EE0009254, ~$10M, 2020-2025). It is building Great-Basin-wide favourability maps from 16 regional datasets and a "developers' playbook" ([ThinkGeoEnergy](https://www.thinkgeoenergy.com/ingenious-project-completes-geothermal-datasets-for-great-basin-region/?amp=1)). All of this output is public.

## Who leased or drilled the favourable zones afterwards
- **Sept 17, 2019 BLM Nevada sale** (BLM results summary, https://www.blm.gov/sites/blm.gov/files/NV_Geot_20190917_Comp_Sale_Results.pdf):
  - 142 parcels and 384,370 acres were offered. **37 parcels and 102,403 acres drew bids.**
  - High bids totalled **$426,955 (~$4.17/acre)**, and total receipts were $637,892. The highest bid was $20/acre, and most parcels went at the $2/acre minimum ([ThinkGeoEnergy](https://www.thinkgeoenergy.com/geothermal-lease-sale-in-nevada-results-in-bids-for-37-of-142-parcels/)).
  - Winners: Ormat 11 parcels, Western States Environment & Resources 11, Tim Tucker (individual) 5, Raser 3, Federal Abstract 2, Terra-Gen Dixie Valley 2, NGP Blue Mountain 1, and others ([ThinkGeoEnergy](https://www.thinkgeoenergy.com/details-on-results-and-key-bidders-of-recent-geothermal-lease-sale-in-nevada/)).
  - UNR credits PFA for stimulating this sale. **A parcel-level match of these leases to Gabbs or Granite Springs was not found (unverified).** Note that the Oct 2021 sale did not include Nye County, where Gabbs Valley sits.
- **No public record was found of deep drilling or a PPA at either Nevada PFA discovery as of 2026 (unverified).** The discoveries were made public in 2018-19, which effectively published the treasure map.
- **Market reprice ([GAO-26-108040, Sept 2026](https://files.gao.gov/reports/GAO-26-108040/index.html)):**
  - Nominations rose from 25.8k acres (2020) to more than 1M acres (2025), with 3.385M acres nominated over 2019-25. About 87% of offered acres were leased.
  - Revenue was $39.4M from 19 sales in 2020-25, including $24M in 2025 alone. 2026 sales cleared at **$701/acre (NM) and $1,207/acre (UT)**; Idaho in 2025 reached a $412/acre high bid.
  - Active leases went from 599 to 749 between March 2025 and March 2026.
  - Nomination to sale takes **335 days on average in Nevada** and 455 days BLM-wide; Oregon/Washington averages 1,595 days.
  - About 27% of nominated acres were rejected as duplicates, a sign of crowding.

## Synthesis: what PFA proved and did not prove
1. **Cheap shallow validation works as a filter.** Roughly 4 of 7 drilled plays were anomalous, and both Nevada Basin-and-Range targets were hot (96-125 °C at <=250 m). Holes cost a few hundred thousand dollars each against a $1.5M phase budget. For an asset buyer this is the analogue of a "drill-to-upgrade" step.
2. **Hit quality tracks province.** Great Basin extensional plays turned out hot and blind. Arcs (WA, HI) gave elevated gradients but were sub-commercial or constrained by land and politics. SRP gave a technical hit that was too cool for power. Utah was undrilled.
3. **Expert-weighted maps leave large ML upside.** The USGS 2025 ML model ranks 54% of producing systems in the top 1% of area, against ~50% in the top 20% for older maps. That is a step-change in how much land must be held per discovery.
4. **The publicly funded programme created value it could not capture.** Universities and USGS cannot hold leases. They published maps and data, and incumbents (Ormat, Terra-Gen) and land speculators bought rights at $2-20/acre.

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar
- **The thesis holds up empirically.** PFA shows that public legacy data can locate blind systems: 34 benchmarks, 375 favourable settings, and 2 of 2 Nevada TG hits. It also shows that **the land step-up is real and was left on the table**. Acreage that cleared at ~$4/acre in 2019 now clears at $700-1,200/acre, a 170-290x reprice. The ~$4/acre figure is the 2019 BLM average; 2026 prices are for different parcels and states. A Terranox-style company is exactly the missing actor that UNR said "it's not our job" to be.
- **The arbitrage window is narrowing on BLM land.** More than 1M nominated acres, 27% duplicate nominations and competitive auctions mean the *obvious* fairway cells are being contested. The edge has to come from (a) better-than-public ranking and (b) channels that are not public auctions:
  - private and fee geothermal rights (no federal auction; this matters in Nevada, Utah and Idaho checkerboard land);
  - state trust-land leases;
  - existing low-activity BLM leases bought or farmed-in from speculators and holders (e.g. the individuals and LLCs that won 2019 parcels at the minimum price);
  - provinces outside the Great Basin where nominations are still thin. Idaho nominations went from 280 acres (2020) to 180k (2025); NM from 4,468 (2024) to more than 400k (2025).
- **Data edge is plausible.** Public PFA and INGENIOUS layers are inputs everyone has. Terranox's analogue of the SMAD advantage would be the *illegible* layers:
  - scanned oil and gas BHTs and mud logs;
  - legacy TG holes in company files (e.g. Ormat and US Geothermal water analyses only reached the PFA through collaboration);
  - mining assessment drilling;
  - **negative training data** (dry or cool holes), which Smith et al. 2023 and Mordensky et al. 2025 show is critical.
- **Value-creation step:** a $1-2M TG programme over about 12 holes can move a prospect from "favourable cell" to "124 °C at 152 m, 6/16/38 MWe P90/P50/P10." That is a sellable, de-risked asset for Ormat, Fervo or utilities. It is an exact parallel to the Terranox claim-and-prove model.
- **Gap vs Zanskar:** Zanskar is vertically integrating. It discovers (Big Blind: ~250 °F at ~2,700 ft, the first industry-confirmed blind commercial system in more than 30 years), then develops and operates (Lightning Dock). That ties up capital in a handful of sites per year. PFA shows the region is target-rich, with dozens of promising sites and only 2 drilled because of budget. That creates room for a **capital-light portfolio landholder**: acquire many rights across many cells, run cheap TG upgrades, and sell or JV the proven state, collecting carry or royalty without building plants. Zanskar's model also does not prioritise non-BLM private and state rights or low-temperature direct-use and data-centre heat plays like Camas Prairie. Both are adjacent asset classes a rights-aggregator can own (scope assessment, unverified as to Zanskar's actual land strategy).
- **Risks the literature flags:**
  - Shallow anomalies do not equal commercial reservoirs. Neither Nevada PFA discovery has been deep-proven.
  - Sage-grouse and land-use deferrals affect ~148k acres.
  - Drilling hot targets needs a commercial rig (the Utah cancellation).
  - Arc and volcanic provinces underdeliver.

## Sources
- DOE GTO PFA overview: https://www.energy.gov/eere/geothermal/play-fairway-analysis
- GDR PFA portal: https://gdr.openei.org/pfa
- Faulds et al. final report (DE-EE0006731), OSTI 1724080: https://www.osti.gov/servlets/purl/1724080 ; https://www.usgs.gov/publications/discovering-blind-geothermal-systems-great-basin-region-integrated-geologic-and
- Nevada PFA 2017 peer review: https://www.energy.gov/sites/prod/files/2017/12/f46/3_2_Play%20Fairway_Nevada%20Bureau%20of%20Mines%20and%20Geology_Discovering%20Blind%20Geothermal_Presentation.pdf
- Faulds et al. 2018 GRC (Gabbs Valley): https://pubs.usgs.gov/publication/70201803
- Craig et al. 2021 Geothermics: https://www.sciencedirect.com/science/article/abs/pii/S0375650521001371
- Steely et al. 2021, Washington PFA final, OSTI 1823116: https://www.osti.gov/biblio/1823116
- Shervais et al. 2020 SRP PFA: https://pubs.usgs.gov/publication/70211876 ; SRP final report: https://gdr.openei.org/submissions/1316
- Lachmar et al. 2023 Camas-1: https://geothermal-energy-journal.springeropen.com/articles/10.1186/s40517-023-00264-4
- Lautze et al. 2017 Hawaii PFA I: https://www.soest.hawaii.edu/GG/FACULTY/ITO/Lautze_etal_Geothermics17_PlayFairway_I.pdf
- Lautze et al. 2020 Hawaii PFA (Geothermics 86): https://www.osti.gov/pages/biblio/1799234
- Lana'i Well 10 data: https://gdr.openei.org/submissions/1411
- Wannamaker et al. 2020 Utah PFA, OSTI 1695591: https://www.osti.gov/biblio/1695591
- Bennett, Nash, Barker 2020 Tularosa, OSTI 1782479: https://www.osti.gov/biblio/1782479
- NREL PFA Best Practices 2023: https://www.nrel.gov/docs/fy23osti/86139.pdf
- Smith et al. 2023 ML Nevada PFA: https://pubs.usgs.gov/publication/70241433
- Mordensky et al. 2025 USGS favorability: https://www.usgs.gov/publications/favorability-mapping-hydrothermal-power-resource-assessments-great-basin-usa
- BLM NV Sept 2019 sale results: https://www.blm.gov/sites/blm.gov/files/NV_Geot_20190917_Comp_Sale_Results.pdf
- ThinkGeoEnergy 2019 sale bidders: https://www.thinkgeoenergy.com/details-on-results-and-key-bidders-of-recent-geothermal-lease-sale-in-nevada/ ; https://www.thinkgeoenergy.com/geothermal-lease-sale-in-nevada-results-in-bids-for-37-of-142-parcels/
- GAO-26-108040 (Sept 2026): https://files.gao.gov/reports/GAO-26-108040/index.html
- Renewable Energy World 2019 (Faulds quotes): https://www.renewableenergyworld.com/?p=218009
- ThinkGeoEnergy 2017 Phase III funding: https://www.thinkgeoenergy.com/?p=32198
- INGENIOUS: https://www.thinkgeoenergy.com/ingenious-project-completes-geothermal-datasets-for-great-basin-region/?amp=1
- Zanskar Big Blind: https://www.thinkgeoenergy.com/zanskar-announces-discovery-of-big-blind-geothermal-site-in-western-nevada-usa/
- Washington no-development statement: https://www.thinkgeoenergy.com/washington-state-to-lead-collaborative-process-for-early-stage-geothermal-studies/
