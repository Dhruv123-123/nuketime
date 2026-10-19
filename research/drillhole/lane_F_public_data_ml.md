# Lane F: Is ML or software on public data what makes the drill-hole pain solvable?

Written 19 Oct 2026. Currency marked per figure. "(memory)" means not re-verified this session; "(estimate)" means my arithmetic or judgement.
Research note: the shared web-search budget ran out partway through this lane. Items marked "unverified" below could not be checked, and a follow-up pass could close them.

## Summary (the 10 lines that matter)

1. **The public archives are huge, and the logs are illegible.** BC's ARIS holds 41,500+ reports (~$4B of exploration spend). After a dedicated BCGS effort, only **205 reports, 2,034 holes** have been turned into structured logs and assays, about 0.5% ([BCGS GF2026-11](https://cmscontent.nrs.gov.bc.ca/geoscience/PublicationCatalogue/GeoFile/BCGS_GF2026-11.pdf)).
2. **The pattern repeats everywhere.** Ontario indexes 164k holes, but mostly as collars plus a flag saying "has assays"; the logs stay in assessment-file PDFs. WA's structured data is complete only from 2007 and sparse before 2000. Saskatchewan's public compilation has 20,145 holes with collars and depth picks only, and no lithology or assays.
3. **So the signal that would make holes cheaper sits in PDF free text, and no government database extracts it.** That covers ground conditions, lost circulation, abandoned holes, core recovery, clay alteration and casing depth. This is the one place where ML is load-bearing, not a nice-to-have.
4. **Holes that never reach their target are a real, unpriced loss.** CanAlaska's 2012 Cree East program: only 10 of 15 holes reached target depth, because of intensely altered Athabasca sandstone. VerAI/Conquest 2024: 2 of 9 holes failed to reach the target horizon. Athabasca drilling costs roughly C$640/m or more (Fission PLS, 2016).
5. **Value of information (picking the fewest holes) is the biggest lever.** On synthetic data, Stanford's Intelligent Prospector matched a 16-point grid with 7-10 measurements. No commercial product exists; KoBold does it in-house. It is only real if priors are calibrated on labelled public hole outcomes, which needs point 3 first.
6. **Re-using old core is mostly a physical and logistics problem, and Australia already industrialised it.** The NVCL/HyLogger network has scanned ~6,200 cores, 1,680 km. ML only ranks which holes to re-scan. That fails "solvable only with ML".
7. **"Predict what the hole hits" is already owned.** Depth to the unconformity is ordinary geostatistics in Leapfrog. Hit prediction is the core product of KoBold, VerAI, Earth AI, ALS GoldSpot, and Terranox itself.
8. **The incumbents are real but thin on legacy logs.** ALS bought GoldSpot's consulting and tech arm for ~C$24M (2022), a services business. Datarock sells core-photo ML priced per metre. Seequent bought Imago (2021). KoBold's own CEO said TerraShed holds about 3% of all geological data.
9. **Verdict.** ML on public data makes one thing solvable that was not before: a basin-scale, hole-level dataset of outcomes and drilling difficulty extracted from scanned logs. Every downstream wedge (difficulty, VOI, re-use) depends on it. Standalone, it is a data/tool business and fails rubric item 6.
10. **In the Athabasca it is the same moat as Terranox (SMAD plus ML).** A "new company" here would be a Terranox competitor or feature. The only variant with a large ceiling is to own the rights and use VOI to drill fewer holes, and KoBold, VerAI and Earth AI already crowd that model.

---

## Part 1. Inventory of public drillhole and assessment databases

Legend for "Legibility": **S** = structured logs and assays downloadable; **C** = structured collars/index only, logs in PDFs; **P** = PDF/scan only.

| Jurisdiction | System | Holes / reports | Format and legibility | Access terms | Source |
|---|---|---|---|---|---|
| Saskatchewan | SMAD (Sask. Mineral Assessment Database) | Report count not found (unverified). Holds drill hole records and logs, geophysical, geochemical and assay reports | P: off-confidential reports, mostly scanned PDF (memory) | Free online (memory) | [saskatchewan.ca SMAD page](https://saskatchewan.ca/business/agriculture-natural-resources-and-industry/mineral-exploration-and-mining/saskatchewan-geological-survey/saskatchewan-mineral-assessment-database-smad) (page returned 503 this session) |
| Saskatchewan | Saskatchewan Drillhole Database / Minerals and Quaternary Drillhole Compilation | **20,145** holes, "not an exhaustive list". Started as pre-2007 uranium holes | C: collar, length, dip/azimuth, depth to base of Quaternary, base of Phanerozoic, base of Athabasca, top of basement. **No lithology or assays.** Storage location field (Regina or La Ronge) | Sask. Standard Unrestricted Use Data Licence v2.0 | [GeoAtlas metadata](https://gisappl.saskatchewan.ca/WebDocs/Geo_Atlas/MetaData/Minerals_and_Quaternary_Drillhole_Compilation.html); [GIS layer](https://gis.saskatchewan.ca/arcgis/rest/services/Economy/Mineral_Exploration/MapServer/3/iteminfo) |
| Saskatchewan | Athabasca basement DDH compilation (EXTECH IV) | **8,167** holes; ~35% have basement lithology. Last updated 2007 | C: depth to sandstone and unconformity, up to 3 basement lithology codes, assessment file number | No constraints, with a disclaimer | [metadata](https://gisappl.saskatchewan.ca/WebDocs/Geo_Atlas/MetaData/Athabasca_basement_DDHs_Compilation.html) |
| Saskatchewan / GSC | Athabasca Basin Uranium Geochemistry Database | Drill-core geochemistry taken from SMAD reports, **2000-2011 only** | S (for that window) | GSC Open File | [publications.gc.ca](https://publications.gc.ca/site/eng/9.958442/marcXml.html?MODS=1) |
| Saskatchewan | Subsurface Geological Laboratory, Regina (core) | ~35,000 wells, ~590,748 m core, 4.8M cutting vials, mostly oil, gas and potash; some Precambrian Shield and northern core. Athabasca 1975-81 mapping samples stored there | Physical | Open with restrictions; sampling needs authorisation | [AAPG Explorer](https://explorer.aapg.org/story/articleid/144/core-values-70-years-of-canadian-history); [Encyclopedia of Sask.](https://esask.uregina.ca/entry/subsurface_geological_laboratory.html); [SGS facilities](https://www.saskatchewan.ca/business/agriculture-natural-resources-and-industry/mineral-exploration-and-mining/saskatchewan-geological-survey/services-research-and-facilities) |
| Ontario | Ontario Drill Hole Database (ODHD) plus Assessment File Database (OAFD) | **164,000+** holes (June 2026). OAFD covers 70+ years | C: location, company, hole number, orientation, depth, overburden, yes/no flags for Au/Ag/Cu/Zn/Pb/Ni/PGE assays, OAFD cross-reference. Logs and assays stay in OAFD PDFs | Open (Ontario open data) | [data.ontario.ca](https://data.ontario.ca/dataset/ontario-drill-hole-database); [ODHD description](https://www.geologyontario.mndm.gov.on.ca/ODHD_Description.html) |
| BC | ARIS plus BCGS Assessment Report Drillhole DB | **41,500+** reports since 1947 (~$4B spend). Structured DB: **205 reports, 2,034 holes, 41,602 lithology entries, 211,995 samples, 9.2M determinations** | P for ARIS (paper/PDF). S for the ~0.5% digitised. The schema includes casing depth, reduced, cemented, plugged and drill contractor fields | 1-year confidentiality; free PDFs; GeoPackage | [BCGS GF2026-11](https://cmscontent.nrs.gov.bc.ca/geoscience/PublicationCatalogue/GeoFile/BCGS_GF2026-11.pdf) |
| Quebec | SIGEOM / e-SIGEOM Examine (GM reports); "Sondages" dataset | Count not found (unverified) | C plus P: drill-hole layer on Données Québec, updated in real time; GM reports as PDFs. Diamond drilling makes up >50% of the database's estimated value | Free download | [Données Québec Sondages](https://www.donneesquebec.ca/recherche/dataset/sondages); [SIGEOM FAQ](https://sigeom.mines.gouv.qc.ca/signet/classes/I3202_faq?l=f); [MRNF](https://mrnf.gouv.qc.ca/en/mines/geology/geoscience-databases) |
| Manitoba | Assessment files plus 5 core libraries (The Pas, Thompson, Lynn Lake, Flin Flon, Winnipeg) | ~260,000 m Precambrian core. A 2001 drillhole DB had ~2,400 holes. **Bakers Narrows library closed after wildfire damage** | P and physical. Master logs held as paper at regional offices (2000s report) | Access on request; sample results must be returned | [MB drillcore](https://www.gov.mb.ca/iem/geo/drillcore/index.html); [GS-39 (2002)](https://www.gov.mb.ca/iem/geo/field/roa02pdfs/GS-39.pdf) |
| Yukon | Assessment Report Footprints plus H.S. Bostock Core Library | 7,500+ reports since the 1950s; core of 27,000+ boxes from ~275 properties | P with spatial index (holes and metres per report) | 5-year confidentiality | [yukon.ca](https://yukon.ca/en/science-and-natural-resources/mining/find-mining-assessment-reports); [core library](https://yukon.ca/en/yukon-geological-survey-core-library) |
| Nunavut | NUMIN via NunavutGeoscience.ca | Count not found; no drillhole layer confirmed | P (report downloads) | Free | [nunavutgeoscience.ca](https://nunavutgeoscience.ca/en/) |
| W. Australia | WAMEX plus Company Mineral Drillhole DB (MDHDB); MINEDEX is mines and deposits, not holes | WAMEX 120,000+ reports (105,000 downloadable). MDHDB **3M+ holes**, 11M surface samples | S from 2007 (digital submission mandatory); **pre-2000 sparse**, earliest 1997. Collar is always present; assays, geology and surveys "may" be. No QC on assays | 5-year confidentiality; full SQL DB on request | [WA gov](https://wa.gov.au/service/natural-resources/mineral-resources/access-company-mineral-drillhole-and-surface-geochemistry-database); [WAMEX](https://dmp.wa.gov.au/WAMEX-Minerals-Exploration-1476.aspx) |
| South Australia | SARIG / SA Geodata | 300,000+ holes (minerals, petroleum, water); 38,713 with core in the library | C/S: basic metadata as CSV; spatial search capped at 4x4 degrees | CC-BY 4.0 | [SARIG catalog](https://catalog.sarig.sa.gov.au/dataset/mesac537); [GSSA](https://energymining.sa.gov.au/industry/geological-survey/products-and-services/map-viewers-databases-and-services/mineral-drilling-and-geochemistry) |
| Queensland | GSQ Open Data Portal (replaced QDEX) | ~61,000 open-file company reports, text-searchable (2020-era figure); Exploration Data Centre catalogue of 11,600+ holes | P made text-searchable, plus a geochem DB (3.24M records in 2014) | No registration required | [GSQ portal](https://www.business.qld.gov.au/industries/mining-energy-water/resources/minerals-coal/online-services/gsq-open-data-portal); [geochem](https://www.business.qld.gov.au/industries/mining-energy-water/resources/geoscience-information/maps-datasets/digital-data/exploration-geochemistry) |
| NSW | DIGS (reports) plus MinView (holes) | 140,000+ non-confidential holes in MinView, mostly post-2000; ~8% have core held. Londonderry holds 1.13M m of core | C in MinView; DIGS PDFs are the "point of truth" because not all DIGS data has been extracted | Free core access with 7 days' notice | [NSW core libraries](https://www.resources.nsw.gov.au/geological-survey/drillcore-libraries/wb-clarke-geoscience-centre-londonderry-drillcore-library); [DIGS guide](https://www.resources.nsw.gov.au/sites/default/files/2022-11/finding-what-you-need-in-digs-shortguide.pdf) |
| Australia (national) | AuScope NVCL (HyLogger hyperspectral) | **6,200+ cores, 1,680 km scanned** | S: mineralogy spectra of legacy core held by state surveys | Open | [AuScope NVCL](https://www.auscope.org.au/nvcl) |
| USA | NURE (DOE, 1970s-80s), held by USGS | HSSR geochemistry reformatted (OFR 97-492). Borehole radiometric logging ("LIL") is a NURE category; download not confirmed | S for HSSR; some data on microfiche only | Public domain | [OFR 97-492](https://pubs.usgs.gov/publication/ofr97492); [USGS NURE report](https://pubs.usgs.gov/unnumbered/70273823/report.pdf) |
| Finland | GTK drillhole DB plus Loppi National Drill Core Archive | **28,857** holes; ~3.6-4M m of core | C/S via map service; a digital core archive project (MinMatka NDCAF) is under way | Open map services; research visits charged | [GTK WFS layer](https://gtkdata.gtk.fi/arcgis/rest/services/GTKWFS/MapServer/7); [GTK archive](https://www.gtk.fi/en/current/gtks-geological-sample-archive-one-of-the-largest-in-the-world-contains-around-4-million-metres-of-drill-cores-and-millions-of-other-samples/); [NDCAF](https://projektit.gtk.fi/minmatka/en/ndcaf/) |
| Sweden | SGU Malå core collection | **22,000+** boreholes, ~4M m; logs exist for ~8,000 more holes whose core is gone | C plus partial S: many cores have logs, geophysics and chemistry; "scanning in progress" | SEK 1,000/day to examine; new samples allowed, with analyses due back within 6 months; licence unclear (CC0 vs fee records conflict) | [SGU drill core](https://www.sgu.se/en/mineral-resources/mineral-exploration-in-sweden/drill-core-collection/) |
| Brazil | SGB-CPRM litoteca network (10 units); RIGEO | Count not found | Physical plus PDF reports; no national public drillhole DB found | Loans for research | [SGB litotecas](https://sgb.gov.br/documents/d/guest/regimento_rede_de_litotecas) |
| Chile | Sernageomin basic-exploration information | Released data from 99 projects, including drillhole databases (2019). Can request data up to 4 years back. Newer regulation (Decree No. 9) | S for the released projects; coverage thin | Public under Law 20,285; advanced-exploration data confidentiality was proposed at 3 years (not confirmed as law) | [Reporte Minero](https://www.reporteminero.cl/noticia/noticias/2019/09/sernageomin-publico-informacion-geologica-de-99-proyectos-de-exploracion); [Carey](https://www.carey.cl/en/regulations-on-the-delivery-of-general-information-obtained-from-basic-geological-exploration-works) |

### What the inventory says
- **Structured coverage is a thin skin over a PDF body.** Where governments digitised, they captured collars and sometimes assays. Ontario's flags and Saskatchewan's depth picks are the typical result. Downhole free text (driller's notes, recovery, "hole lost", "lost circulation at 212 m", "casing left", "reduced to BQ") is essentially never structured. BC's new schema is the exception (casing, reduced, cemented, plugged, contractor), and it covers 2,034 holes.
- **WA is the counter-example, and it shows the cutoff.** Mandatory digital submission since 2007 produced 3M+ holes. Everything older, which includes the Athabasca's 1970s-90s first wave by analogy, stays in report PDFs.
- **The Athabasca specifically:** about 20k collars with unconformity depths are public and structured. Basement lithology covers ~2,900 holes (35% of 8,167, estimate). Drill-core geochemistry covers only the 2000-2011 window. Pre-2000 and post-2011 logs and assays, and every drilling-difficulty record, are PDF-only in SMAD.

---

## Part 2. The four software problems, and who already does them

### (a) Re-using old holes: re-logging and re-assaying legacy core, re-entering known holes
- **The physical asset exists and is cheap.** Government core libraries hold core at no charge to the user. Examples: Saskatchewan (Regina, plus La Ronge storage per the drillhole compilation field), Ontario, Manitoba (~260k m), Yukon (27k boxes), NSW (1.13M m), SA (38.7k holes), GTK (3.6-4M m), SGU (4M m). Access ranges from free to SEK 1,000/day.
- **Who already does it.**
  - Australia's NVCL has industrialised hyperspectral re-logging of public core: 6,200 cores, 1,680 km ([AuScope](https://www.auscope.org.au/nvcl)).
  - SGU says scanning is "in progress"; GTK has a national digital core archive project.
  - Datarock re-logs historic core *photos* for RQD and fracture frequency and markets exactly that ("validate older logging, fill in data gaps"), priced by metres processed ([Datarock](https://datarock.com.au/Platform/), [help](https://help.datarock.com.au/knowledge-base/datarock-core)).
  - Seequent/Imago manages core imagery ([Bentley 2021](https://www.businesswire.com/news/home/20210805005551/cs)).
  - Corescan does commercial hyperspectral core imaging ([Petroleum News](https://www.petroleumnews.com/pnarchpop/291458615.shtml)).
- **Is ML load-bearing?** Only for *triage*: reading old logs to rank which library holes are worth a modern SWIR, clay or multi-element pass, for example holes that stopped short of the unconformity or were never assayed for pathfinders. The value itself comes from the physical scan or assay. Verdict: **nice-to-have**. Software is the planning layer for a lab or service business.
- **Athabasca caveat (unverified).** How much 1970s-90s Athabasca *exploration* core the province holds, versus core kept by companies or discarded, could not be confirmed. The Regina lab is described as mainly petroleum and potash. Many Athabasca holes are on Cameco/Orano ground and their core is company-held (memory).
- **Re-entering or deepening old holes.** Athabasca juniors do wedge and deepen holes; the Sask compilation even carries a wedge-hole flag ([metadata](https://gisappl.saskatchewan.ca/WebDocs/Geo_Atlas/MetaData/Minerals_and_Quaternary_Drillhole_Compilation.html)). Historic holes with casing left in place could in principle be re-entered. I could not verify any examples or costs this session (unverified). It is an engineering opportunity, not an ML one.

### (b) Predicting drilling difficulty, cost and depth to target from old logs
- **The pain is real.** CanAlaska Cree East (2012): "only ten of fifteen holes reached their target depth, mostly because of extremely difficult drilling conditions related to intensely hydrothermally altered aureoles in the overlying Athabasca sandstone" ([CanAlaska](https://canalaska.com/canalaska-uranium-winter-drilling-update/), via search snippet; the page itself was bot-blocked). Stallion Moonlite 2026 lists two holes as "Lost" in clay-altered, brecciated sandstone ([Barchart](https://www.barchart.com/story/news/1555752/stallion-uranium-recommences-drilling-at-moonlite-project)). VerAI/Conquest: 2 of 9 holes "failed to reach the target horizon beneath thick Nipissing diabase" ([Newsfile](https://www.newsfilecorp.com/release/240334/Conquest-Drill-Testing-of-VerAI-AIgenerated-Targets-Identifies-Potential-VMS-System-at-Its-BelfastTeckMag-Project)).
- **The irony.** The alteration halo that makes a target attractive is exactly what destroys holes. Difficulty and prospectivity are correlated, so a difficulty model is also an alteration map.
- **The cost of a failure.** Fission PLS 2016: at least $6.5M for 10,105 m in 34 holes, so ≥$643/m (currency not stated; CAD assumed) ([CMJ](https://canadianminingjournal.com/news/uranium-fission-sets-6-5m-drill-program)). The repo's earlier work used C$500-700/m to the unconformity (memory, ANALOG_ATLAS). A 500 m hole abandoned at 350 m wastes ~C$225k and still needs re-drilling (estimate).
- **Where the signal sits.** Free-text driller and geologist notes in SMAD PDFs: core recovery, "lost circulation", "hole abandoned", "cemented", "reduced to BQ", casing depths, days per hole. None of this appears in the Sask compilation (no such fields), ODHD (no such fields) or WA's MDHDB (collar, assay, geology, survey). BC added casing, reduced, cemented and plugged fields, but for only 2,034 holes ([GF2026-11](https://cmscontent.nrs.gov.bc.ca/geoscience/PublicationCatalogue/GeoFile/BCGS_GF2026-11.pdf)).
- **Who does it.**
  - Oil and gas has a mature ML rate-of-penetration and lost-circulation literature ([Petroleum Science 2024 review](https://cup.edu.cn/petroleumscience/wqwz/2024/2024Issue5/2024sygcyjx4/060900a7dafb48a7b3461e3605951bc1.htm)).
  - Mining work is lab-scale or blasthole only ([Kahraman ANN diamond-drill ROP](https://unpaywall.org/10.1007%2FS11063-015-9424-7); [copper mine XGBoost](https://link.springer.com/article/10.1007/s13369-023-08360-0)).
  - I found **no commercial product** predicting exploration diamond-drill difficulty from public legacy logs. Drilling contractors (Foraco, Major, Boart, local Athabasca drillers) carry this as tacit knowledge (estimate).
- **Depth to target is solved without ML.** Unconformity depth is a structured field on ~20k Sask holes and is routinely gridded in Leapfrog or by the SGS (memory). ML adds little.
- **Is ML load-bearing?** For difficulty, **yes**: the labels exist only as unstructured text across thousands of scanned reports. Without extraction there is no training set. The ceiling is small, though: it is a planning tool for contractors and juniors.

### (c) Predicting what a hole will hit before drilling
- This is the core product of every AI-exploration company.
  - KoBold: TerraShed plus Machine Prospector. The CEO said TerraShed holds ~3% of all geological data ([Singularity Hub](https://singularityhub.com/2023/08/30/ai-is-turbo-charging-the-search-for-electric-vehicle-battery-metals)).
  - VerAI: $24M Series B in 2025; earn-in model; claims are unverified ([Mining Technology](https://www.mining-technology.com/features/ai-critical-mineral-discovery/)).
  - Earth AI: $20M Series B in Jan 2025; drills its own targets at a claimed ~$100/m; self-reported 75% "discovery success" ([Mining Technology](https://www.mining-technology.com/news/earth-ai-20m-ai-driven-mineral-exploration-drilling/)).
  - ALS GoldSpot: acquired for ~C$24M in Dec 2022, run as an ALS consulting division, and includes Geotic core logging ([ALS](https://www.alsglobal.com/fr/News-and-publications/2022/12/ALS-acquires-the-ExplorTech-Division-of-Earthlabs-Inc)).
  - Academic: Bayesian deep learning for 3D Cu prediction and drill targeting ([arXiv 2609.09246](https://arxiv.org/pdf/2609.09246)).
  - **Terranox** does exactly this on SMAD for Athabasca uranium.
- **Verdict:** owned. A new company here is a Terranox competitor, not a new wedge. Kill as a standalone idea.

### (d) Choosing the minimum set of holes (value of information)
- **Academic state of the art.** Stanford's Intelligent Prospector (Mern & Caers, GMD 2023) frames drilling as a POMDP. On a **synthetic 2D** problem it reached the accuracy of a 16-measurement grid "after just 7 to 10 measurements" (~40-55% fewer, my arithmetic). It made the correct mine/abandon decision in >90% of single-body cases, but wrongly abandoned ~32% of profitable multi-body cases ([GMD](https://gmd.copernicus.org/articles/16/289/2023/gmd-16-289-2023.html)). v2.0 (2024) handles an uncertain prior ([arXiv 2410.10610](https://arxiv.org/abs/2410.10610v1)). A Stanford thesis covers sequential VOI for greenfield drilling ([purl](https://purl.stanford.edu/pm892rp3036)).
- **Industry.** KoBold describes this loop: models quantify uncertainty and decide what to measure and where to drill next ([Singularity Hub](https://singularityhub.com/2023/08/30/ai-is-turbo-charging-the-search-for-electric-vehicle-battery-metals)). It is not sold as a product. I found no commercial VOI drill-planning tool. Seequent and Leapfrog do not ship VOI (memory).
- **Is ML load-bearing?** The VOI maths is decades old. What has blocked it in practice is the *prior*: you need calibrated base rates of "given these features, what did past holes find?". Those base rates exist only in the public archives' PDFs. So VOI becomes solvable once (b)/(c)-style extraction yields labelled hole outcomes across a whole basin. The ML is the extraction, and the VOI is ordinary decision theory on top. Verdict: **passes, conditionally**.

---

## Part 3. Candidate wedges

Program cost basis (estimate): a typical Athabasca junior program is 5,000-15,000 m at C$500-700/m, so C$3-10M ([CMJ Fission](https://canadianminingjournal.com/news/uranium-fission-sets-6-5m-drill-program); repo memory). Holes run roughly 300-1,000 m to the unconformity (memory).

### W1. Basin-scale legacy log and outcome extraction ("structured SMAD/ARIS/OAFD")
- **Dataset:** SMAD PDFs (Sask), ARIS 41.5k reports (BC), OAFD (Ontario), pre-2007 WAMEX, DIGS (NSW), Yukon/Nunavut reports. Vision-language and OCR models turn them into hole-level tables: lithology, alteration, assays, recovery, difficulty events and final outcome.
- **Decision changed:** where the ground has already been tested and failed, so you avoid re-drilling a known miss. It also creates the training set for W2-W4.
- **Money per program (estimate):** avoiding even one redundant hole saves C$200-500k. The bigger value is as an input to the other wedges.
- **Is ML necessary?** **Yes, clearly.** BC's survey reached 205 of 41,500 reports by hand-scale effort ([GF2026-11](https://cmscontent.nrs.gov.bc.ca/geoscience/PublicationCatalogue/GeoFile/BCGS_GF2026-11.pdf)). LLM extraction is ~100% accurate on clean PDFs but ~70% on image scans ([arXiv 2405.05438](https://arxiv.org/html/2405.05438v1)), so there is real technical headroom.
- **Who owns it:** ALS GoldSpot (digitisation services), KoBold TerraShed (internal), the surveys themselves (slowly), and Terranox for SMAD. Generic AI borehole digitisers exist in geotech ([Civils.ai](https://civils.ai/blog/ai-borehole-log-digitiser-for-geotechnical/)).
- **Rubric:** passes item 2. As a data-licensing business it fails item 6; geoscience data and software is a tool market. In the Athabasca it *is* Terranox's moat, so it does not count as a new company.

### W2. Drilling-difficulty and lost-hole predictor (Athabasca first)
- **Dataset:** difficulty events extracted from SMAD logs, joined to the 20,145-hole compilation (sandstone thickness, unconformity depth) and to the uranium geochemistry DB (clay and alteration intensity).
- **Decision changed:** collar location (step out of the worst clay-altered sandstone, angle the hole), rig size and rod string, a planned casing or cementing program, mud choice, and contingency budget. It is also a go/no-go input when the target sits under a known bad-ground zone.
- **Money per program (estimate):** if 1 in 3 holes fail as at Cree East, a 10,000 m program loses perhaps 15-25% of metres, about C$1-1.6M. A model that halves that saves **C$0.5-0.8M per program**. A contractor using it to bid fixed-price contracts gains margin.
- **Is ML necessary?** **Yes for the labels**, which sit in free text only. The model itself is modest tabular ML.
- **Who owns it:** nobody commercially found. Contractors hold it as tacit knowledge; oil and gas has analogues.
- **Rubric:** passes item 2 cleanly. Fails item 6 standalone: the buyer pool is ~60 Athabasca juniors plus contractors (repo memory), so it is a $1-10M/yr tool (estimate). Best as a feature of W4, or as a way in to drilling contractors.

### W3. Legacy-core triage and re-assay (the "drill in the library first" service)
- **Dataset:** extracted logs (W1) plus core-library holdings (Sask compilation storage-location field; Ontario, Manitoba and Yukon libraries; NVCL elsewhere). Rank holes where modern SWIR, clay or pathfinder analysis would change a target ranking.
- **Decision changed:** replace a speculative first hole (C$200-500k) with re-sampling of existing core at a small fraction of the cost (estimate; the per-sample cost of modern assay or SWIR was not verified this session).
- **Money per program (estimate):** C$0.2-1M, if one first-pass hole is avoided.
- **Is ML necessary?** **No.** Ranking is helpful, but the value is the physical analysis, and NVCL already does this at national scale in Australia. In the Athabasca the binding constraint is whether the core is in the library at all (unverified).
- **Who owns it:** NVCL/HyLogger, Corescan, Datarock (photos), SGU and GTK scanning programs, and ALS (labs plus GoldSpot).
- **Rubric:** fails item 2. It does match item 3 (old holes are a near-free asset). Weak as a company.

### W4. Value-of-information drill planner that stops programs early
- **Dataset:** basin priors calibrated on labelled public hole outcomes (W1) plus the difficulty and cost model (W2), feeding a sequential POMDP planner of the Intelligent Prospector type.
- **Decision changed:** next-hole placement; when to **stop** and drop a property, the largest single saving; and the minimum holes needed to prove or disprove a target before an earn-in milestone.
- **Money per program (estimate):** the synthetic result implies 40-55% fewer measurements to reach the same confidence ([GMD 2023](https://gmd.copernicus.org/articles/16/289/2023/gmd-16-289-2023.html)). Even 20-30% fewer holes on a C$5M program is **C$1-1.5M**. Abandoning a dead property one season earlier saves the whole season's C$3-6M.
- **Is ML necessary?** **Conditionally yes.** The decision theory is old. Calibrated priors from public data, which need W1's extraction, are what make it trustworthy rather than a toy. It has not been demonstrated on real data; the published wins are synthetic, and the method wrongly abandoned ~1/3 of profitable multi-body cases.
- **Who owns it:** KoBold (in-house, not sold) and Stanford Mineral-X (academic). No commercial product found.
- **Rubric:** passes item 2 conditionally. As software sold to juniors it fails item 6. The large-ceiling version is to **own the ground and drill fewer holes per proven target** (rubric items 3-5), but that is the KoBold, VerAI, Earth AI and Terranox model, so it is crowded and sits close to Terranox.

### W5 (killed). Pre-drill "what will it hit" or depth-to-target predictor
- Depth to the unconformity is structured and ordinary geostatistics. Hit prediction is owned by Terranox, KoBold, VerAI, Earth AI and ALS GoldSpot. ML is not what newly makes it solvable here, so it fails item 2 for a *new* company.

### W6 (adjacent, speculative). Public hole-outcome base-rate dataset for pricing earn-ins and drill risk
- **Dataset:** W1 outcomes aggregated into hit rates by target type, depth and alteration, for each basin.
- **Decision changed:** how majors, streamers and flow-through financiers price an earn-in or a drill program. This ties to rubric item 4 (a buyer paying for the proven state).
- **Is ML necessary?** Yes, the same extraction dependency as W1.
- **Who owns it:** nobody visible. MinEx Consulting publishes aggregate discovery statistics (memory), but not hole-level base rates.
- **Rubric:** passes item 2. The market (insurers and financiers of drill risk) is unproven; flagged for the owner/insurance lanes rather than scored here.

### Wedge scorecard

| Wedge | Dataset | Decision changed | C$ saved per program (estimate) | ML makes it solvable at all? | Incumbent | Standalone ceiling |
|---|---|---|---|---|---|---|
| W1 Legacy extraction | SMAD/ARIS/OAFD/WAMEX PDFs | Skip known misses; feeds everything | 0.2-0.5M direct | **Yes** | ALS GoldSpot, KoBold internal, Terranox (SMAD) | Tool/data (fails 6) |
| W2 Difficulty predictor | SMAD free-text plus Sask compilation | Collar, rig, casing, contingency | 0.5-0.8M | **Yes** (labels only in text) | None found | Small tool (fails 6) |
| W3 Library core triage | Logs plus core-library holdings | Re-sample instead of first hole | 0.2-1M | **No** (physical value) | NVCL, Corescan, Datarock | Service |
| W4 VOI planner | W1 priors plus W2 cost model | Next hole and stop/continue | 1-1.5M; up to a full season | **Conditionally** (priors) | KoBold internal, Stanford | Large only if you own the ground (crowded) |
| W5 Hit prediction | Collars, geochem, geophysics | Where to drill | n/a | No (owned) | Terranox, KoBold, VerAI, Earth AI | Killed |
| W6 Outcome base rates | W1 aggregated | Pricing earn-ins and drill risk | n/a (financier side) | Yes | None found | Unproven |

---

## Part 4. Honest answer to the lane question

- **Is ML on public data what makes the drill-hole pain solvable?** Partly. It makes one thing newly possible: turning decades of scanned logs into labelled, hole-level data on outcomes and drilling difficulty. Governments have not done it (BC ~0.5%; Ontario and Saskatchewan collar-only; WA pre-2007 gap), and incumbents do not sell it. Every lever that makes holes *fewer* (VOI, W4) or *less likely to fail* (difficulty, W2) depends on that extraction.
- **Does it make holes cheaper per metre?** No. Per-metre cost is rigs, fuel, helicopter and winter roads, and camp. Software does not touch it. Earth AI's ~$100/m claim comes from its own rig hardware, not data ([Mining Technology](https://www.mining-technology.com/news/earth-ai-20m-ai-driven-mineral-exploration-drilling/)).
- **Do incumbents already extract this signal?** For targeting, yes (KoBold, VerAI, Earth AI, ALS GoldSpot, Terranox). For drilling difficulty and lost holes, no; I found no evidence anyone extracts it. For VOI with public-data priors, only KoBold claims it, internally.
- **The structural problem for Dhruv's rubric.** The ML-necessary pieces (W1, W2) are tools with a small buyer pool. The large-ceiling piece (W4 plus owning the ground) is the AI-explorer model that Terranox, KoBold, VerAI and Earth AI already run. So in this lane the honest conclusion is that the best ideas are **Terranox features** (difficulty-aware, VOI-optimised drill planning on top of its SMAD extraction), not a new company. The exception is if someone takes W1+W2+W4 to *other* basins and jurisdictions as their own explorer, and that is a Terranox clone. Relative to the 2026-10-03 rule: W2-W4 are drilling-adjacent software, not prospecting picks.

### Open items (search budget exhausted; follow-up needed)
- SMAD total report count, scan quality, and Saskatchewan's confidentiality period for assessment work.
- How much Athabasca exploration core is actually held by the Sask government (La Ronge versus Regina) versus by companies.
- Documented Athabasca re-entries of historic holes and their cost.
- Per-sample cost of modern SWIR plus multi-element re-assay of library core.
- Corescan's current corporate status; Datarock's funding; Seequent's revenue.
