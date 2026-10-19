## Legacy airborne geophysical data as a substitute for new flights

### What I found
1. **Saskatchewan's assessment file already holds a large public archive of company-flown surveys, and the province requires the raw data.** I queried the province's own "Airborne Surveys" layer (Mineral_Assessment_File_Information/FeatureServer/2). It has **1,831 survey records, from 1,809 assessment files**, dated 1950s to 2023.
   - **By decade:** 1950s: 64, 1960s: 360, 1970s: 446, 1980s: 248, 1990s: 92, 2000s: 310, 2010s: 217, 2020s: 88.
   - **Methods** (counted by keyword): 1,334 mention EM, 1,178 magnetics, 646 radiometrics or scintillometers, 107 gravity. About 607 are uranium-related.
   - **Who flew them:** the top filers are SMDC (161 records), Gulf Minerals, Denison, Eldorado Nuclear, Mokta, SERU Nucléaire and Amok. These are the old uranium explorers.
   - **Post-2000:** 615 records, of which **335 are helicopter EM** (VTEM, ZTEM, AeroTEM, HeliTEM, GSEM, HeliSAM and similar). 257 of those state their line-km, and together they total **about 395,000 line-km**. The median survey is about 760 line-km. All post-2000 airborne records that state line-km add up to about 746,000 line-km.
   - **Examples from 2018–19:** NexGen flew ZTEM (1,514 lkm), HeliFalcon gravity gradiometry (1,503 lkm) and HeliSAM (907 lkm). Standard Uranium flew VTEM (1,557 lkm), and ALX Uranium flew radiometrics plus magnetics at 50 m spacing (4,449 lkm). The records note the media, for example "1 DVD, 3.08 GB".
   - **Gross footprint:** the post-2000 helicopter polygons sum to about 92,000 km², overlaps included. All post-2000 polygons sum to about 265,000 km². For scale, the Athabasca Basin is roughly 100,000 km² (estimate).
2. **What the rules require, and when the data goes public.** Under The Mineral Tenure Registry Regulations (Table 3), an airborne survey filing must include "a complete digital listing, as received by the holder from the contractor". Section 68 keeps a filing confidential only until the earliest of three things:
   - three years after the minister receives it;
   - the holder's written consent; or
   - the date the claim lapses or is terminated.

   Uranium juniors drop claims all the time, so a lot of recent raw helicopter EM becomes public quickly. The record counts for 2020–23 look low (about 88), mostly because of this three-year lag.
3. **A structural headwind.** Section 65(2), amended in 2024 by SR 62/2024, lets a holder book **1.5× the actual cost of an airborne geophysical survey** as assessment expenditure. Flying a new survey is therefore subsidised in the claim-maintenance currency. I could not confirm whether reinterpretation or re-inversion of legacy data earns any assessment credit (unverified). This matters for go-to-market: if it doesn't, a substitute product competes against a 1.5× credit.
4. **Government data is reconnaissance-grade, not target-grade.** NRCan's index of digital aeromagnetic data for Saskatchewan lists only **39 government surveys**: 18 mag, 15 mag-radiometric, 4 mag-EM, 1 gravity, 1 mag-gravity. By line spacing: 5 at 200 m, 2 at 250 m, 8 at 300 m, 9 at 400 m, 3 at 500 m, 9 at 800 m, 1 at 1000/500 m, 2 at 2000 m. The provincial compiled grids are at 800–3,200 m spacing and 300 m terrain clearance. Basement-conductor targeting usually needs helicopter EM at 100–200 m spacing (estimate), so the economically useful legacy data is the company assessment data, not the government data.
5. **Holdings elsewhere:**
   - **Canada (GSC / CAGDB):** over 11 million line-km of aeromagnetics as of 2006, from 700 to 1,000+ surveys (the two catalogue records disagree). Download is free through the Geoscience Data Repository.
   - **Australia:** Geoscience Australia's 14th-edition index (Oct 2025) lists 1,085 government surveys with over 34 million line-km. GA values this at about A$197M to re-acquire, roughly A$5.8/lkm for fixed-wing mag/radiometrics. AusAEM adds airborne EM at about 20 km line spacing; AusAEM02 alone was 55,675 lkm, plus 6,450 lkm of industry-funded infill.
   - **USA (USGS Earth MRI):** 68,375 lkm in SE Missouri (2018–19), 61,974 lkm in Illinois/Kentucky, 162,419 lkm on the Arizona copper belt, about 216,000 lkm over 38,400 km² in Michigan's Upper Peninsula, and about 162,000 lkm in Minnesota. These are mostly fixed-wing mag/radiometrics; there is little helicopter EM (one example is the 3,251 lkm Mojave survey). Downloads are free.
   - **Finland (GTK):** a national low-altitude survey at 200 m spacing and 30–40 m altitude, begun in 1972 and covering more than 80% of the country. I could not confirm how open the downloads are.
   - **Northern Ireland (Tellus, run jointly by GTK and BGS):** 80,458 lkm.
   - **Ontario:** over 85,000 assessment files. Ministry geophysical datasets cost C$0–25 each and include raw .xyz/.gdb profiles and 20–40 m grids. The current reporting system is MLAS. I could not source Ontario's confidentiality period.
   - **Other provinces, for comparison:** confidentiality is 1 year in Alberta, 3 years in Manitoba, 1 year in BC (extendable to 3–5) and 2 years in Nova Scotia.
6. **Re-inversion of legacy data does work, at least by company account.** In April 2026 Greenridge Exploration (Carpenter Lake, southern Athabasca margin, about 13 km from Arrow) had Computational Geosciences re-invert a **2014 VTEM survey**, jointly with Falcon gravity, magnetics and 2025 drill core. Unconstrained inversions "were unable to fully resolve the steep, shear-hosted conductors". Parametric plate inversion did resolve them, giving targets along more than 15 km of strike, "many… untested". The company says this extracts insight "without requiring new geophysical acquisitions". This is promotional and not independently checked. CGI has also run 3D inversion of ZTEM data on the Stewardson project.
7. **What a new flight costs, as a benchmark for what reuse saves:**
   - AeroTEM in BC, 2010: **C$125/lkm**, plus C$17,000 mobilisation and C$2,000/day standby; 1,070 lkm came to C$173,400.
   - Another 2010 BC survey: 754 lkm for C$99,894, about C$132/lkm.
   - These line up with the founder's "close to $100k" figure and the ~760 lkm median Saskatchewan helicopter survey.
   - A US consultant's deck on airborne EM for water projects (not mineral surveys) gives US$80–200/lkm plus US$10–50k mobilisation.
   - Replacement value of the post-2000 Saskatchewan helicopter archive: 395k lkm × US$125–200/lkm ≈ **US$50–80M (estimate)**. The full 1950–2023 archive is likely US$150M+ in today's money (estimate).

### Is there illegible value in old raw survey files?
Yes, in three layers.
- **Pre-1990 analog surveys (about 1,118 of the 1,831).** These are INPUT EM, early radiometrics and scintillometer surveys flown by the 1970s uranium rush companies. They exist only as scanned maps and reports. Turning profiles and anomaly picks into point data with ML or vision tools would yield conductor and radiometric anomaly databases nobody has organised. They are shallow-penetrating, so they suit near-surface and basin-margin targets more than deep unconformity targets.
- **2000–2023 digital surveys (about 600 records, ~395k helicopter lkm).** These are raw contractor files on DVDs and USB drives. Mentions of digital media appear in 652 records, 608 of them post-2000. They sit in the file system unstructured. They need levelling, merging across contractors and systems, and modern 3D or parametric re-inversion, which the Greenridge case suggests changes the targets.
- **The cross-survey layer.** Nobody seems to sell a merged, re-inverted, claim-indexed conductor model of the Athabasca built from all the off-confidential surveys. Saskatchewan's new GeoDS (2026) launches structured *drilling* data; airborne data is only "files to download" (from its FAQ).

### Venture read
- **Substitution works when:** recent EM exists over the ground (common in the Athabasca, given claim churn), the target is within the system's depth reach, and the buyer needs to prioritise targets before drilling.
- **It fails when:** there is no coverage at 100–200 m spacing, the needed depth is beyond the old systems (basement conductors more than 500–800 m under sandstone; estimate), or a regulator or vendor needs fresh data. The 1.5× credit also tilts juniors toward flying.
- **Possible product:** a "legacy geophysics refinery" across SMAD/GeoDS, Ontario, BC ARIS, Manitoba, Quebec and others. It would ingest and digitise, re-level and re-invert, then sell per-claim conductor and target packages at roughly US$5–20k. That undercuts a ~US$100k flight (pricing is an estimate).
- **Ways to monetise:** due diligence before staking or acquiring ground, survey design (fly only the gaps, cutting line-km 30–70%; estimate), and data licensing.
- **Risks:**
  - The buyers are cash-poor juniors.
  - Consultancies such as CGI and Mira already do re-inversion as bespoke service work.
  - Seequent (Oasis montaj/Geosoft) controls the software layer. It was bought by Bentley for about US$1.05B in 2021 (from memory, not re-checked).
  - The ML-targeting players are GoldSpot, VRIFY's DORA, KoBold (raised about US$537M in 2025 at about a US$3B valuation; from memory, not re-checked) and Earth AI. They were **not researched in this run** because the shared web-search budget ran out (200 searches per turn, shared by every agent). Treat their revenues and data strategies as unknown; a follow-up message can continue that part.

### Sources
- https://gis.saskatchewan.ca/egis/rest/services/Economy/Mineral_Assessment_File_Information/FeatureServer/2 (queried directly)
- https://donnees.iriu.ca/dataset/f4daf4f8-cb33-0ca3-c42f-65c201a51f34
- https://gis.saskatchewan.ca/arcgis/rest/services/Economy/Geophysical_Data_and_Indicies/MapServer/layers
- https://publications.saskatchewan.ca/api/v1/products/65749/formats/73149/download (Mineral Tenure Registry Regulations, s.65, s.68, Table 3)
- https://publications.saskatchewan.ca/api/v1/products/83742/formats/96932/download
- https://saskatchewan.ca/business/agriculture-natural-resources-and-industry/mineral-exploration-and-mining/saskatchewan-geological-survey/saskatchewan-mineral-assessment-database-smad
- https://saskatchewan.ca/business/agriculture-natural-resources-and-industry/mineral-exploration-and-mining/saskatchewan-geological-survey/saskatchewan-geoscience-data-management-project
- https://bac-lac.wayback.archive-it.org/web/20061102104000/http:/gdr.nrcan.gc.ca/aeromag/about_e.php
- https://open.canada.ca/data/en/dataset/752fe3fc-d871-5ae1-9bd9-2b6f65880a8d
- https://data.amerigeoss.org/dataset/feb31a68-580d-594b-863a-73e5c8132e9b
- https://data.gov.au/data/dataset/ded1a4c0-a5e8-4f87-901a-37786464eaca
- https://data.gov.au/data/dataset/b985ed86-0684-4693-bc35-14347f06d37e
- https://www.ga.gov.au/about/projects/resources/geophysical-acquisition-and-processing/airborne-electromagnetics
- https://resourcingtheterritory.nt.gov.au/news-and-events/news/2020/geoscience-australia-releases-ausaem-02-airborne-electromagnetic-survey
- https://www.usgs.gov/data/airborne-magnetic-and-radiometric-survey-southeast-missouri-and-western-illinois-2018-2019
- https://www.usgs.gov/data/airborne-magnetic-and-radiometric-survey-upper-peninsula-michigan-and-parts-northern-wisconsin
- https://www.usgs.gov/data/airborne-magnetic-and-radiometric-survey-cuyuna-iron-range-central-minnesota-2023-2025
- https://www.usgs.gov/data/airborne-electromagnetic-and-magnetic-survey-western-mojave-desert-california-2024
- https://space.fmi.fi/MAGN/iugg/iugg2004/iaga2004/IAGA2004GSF.pdf
- https://ckan.publishing.service.gov.uk/dataset/gsni-geoindex-magnetics
- https://www.mndm.gov.on.ca/en/print/mines-and-minerals/applications/ogsearth/geophysical
- https://www.geologyontario.mndm.gov.on.ca/mndmfiles/pub/data/records/GDS1089.html
- https://www.geologyontario.mndm.gov.on.ca/mndmfiles/pub/data/records/GDS1251.html
- https://data.ontario.ca/dataset/assessment-file-research-image-database
- https://ero.ontario.ca/public/2025-01/Appendix%201%20-%202025%20-%20Improving%20Ontario%E2%80%99s%20Mineral%20Exploration%20Assessment%20Work%20Regime.pdf
- https://training.energy.gov.ab.ca:443/Guides/Preparing_Mineral_Assessment_Reports_in_Alberta.pdf
- https://www.gov.mb.ca/iem/mines/pubs/assessment-report-guidelines.pdf
- https://www2.gov.bc.ca/gov/content/industry/mineral-exploration-mining/british-columbia-geological-survey/assessmentreports
- https://novascotia.ca/natr/meb/geoscience-online/about-assessment-reports.asp
- https://webfiles.thecse.com/Greenridge_Carpenter_Lake_Geophysical_Inversion_Results_-_April_8_2026.pdf
- https://cmic-footprints.laurentian.ca/filebrowser/download/156
- https://www.earthdoc.org/content/papers/10.3997/2214-4609-pdb.165.C_OP_04
- https://apps.nrs.gov.bc.ca/pub/aris/Report/32307.pdf/
- https://apps.nrs.gov.bc.ca/pub/aris/Report/29299.pdf/
- https://www.geosciencebc.com/?p=4293
- https://watercenter.colostate.edu/wp-content/uploads/sites/91/2024/04/Airborne-Electromagnetics-AEM-and-Insights-on-Recharge-Projects-in-Nebraska-and-Colorado-Abraham.pdf
