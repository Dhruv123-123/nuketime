# Research return: multi-client airborne geophysics as a business model for mining exploration

**Search limitation:** the shared WebSearch budget was already used up when this agent started (limit of 200 searches per turn; 0 of my 3 searches ran). Everything below comes from direct WebFetch of primary pages and PDFs, plus my own knowledge. Any figure without a fetched source is marked "(estimate)" or "(unverified)". Coverage of mining-specific multi-client libraries is thin, and a follow-up message would let the searches run.

## Findings

### 1. The seismic multi-client model works at scale. TGS is the benchmark (sourced)
TGS Q4 2025 earnings release, produced financials:

| Metric (US$M) | FY2025 | FY2024 |
|---|---|---|
| Produced revenue | 1,509.6 | 1,435.2 |
| Multi-client sales | **883.8** | 805.8 |
| Contract sales | 625.8 | 629.4 |
| Organic multi-client investment | **446.8** | 348.6 |
| Produced EBITDA | 878.9 | 811.2 |
| Multi-client library net book value at year end | 1,149.3 | 1,196.8 |
| Straight-line library amortization | 240.8 | 204.9 |
| Accelerated library amortization | 248.9 | 103.9 |

- The key ratio is **sales-to-investment of 2.0x in FY2025**, which was TGS's stated annual goal. Every dollar spent acquiring speculative data returned about $2 of sales, counting prefunding plus late sales.
- Late sales of old ("vintage") data drive results. Q4 2025 multi-client unit revenue was US$270.3M, "driven by healthy sales of vintage data particularly in frontier areas."
- Q2 2026: multi-client sales were US$249.7M, against US$135.8M in Q2 2025. H1 2026 multi-client sales were US$462.5M on US$346.3M of investment. FY2026 multi-client investment guidance is about US$550M.
- TGS now reports produced revenue (recognised as surveys progress) and no longer publishes an explicit prefunding versus late-sales split. Historically, seismic prefunding ran at about 40–70% of investment (estimate).
- **Cautionary tale:** ION Geophysical, owner of the BasinSPAN multi-client libraries, filed Chapter 11 in April 2022 and sold assets. A multi-client library is a balance-sheet-heavy, cyclical asset that depends on licensing rounds and commodity cycles.

### 2. Mining-side multi-client airborne libraries barely exist. The working analogue is government co-funded data, released free
- **Geoscience BC QUEST (2007–08)** is the clearest proof of the "shared survey unlocks land rush" effect:
  - **Budget:** a C$5M program, including C$750k from the Northern Development Initiative Trust.
  - **Survey work:** Geotech flew helicopter VTEM; Sander Geophysics flew airborne gravity. Each survey covered about **46,000 km²**.
  - **Data release:** all data was published free in six releases during 2008.
  - **Industry response:** QUEST-West (about 40,000 km² more, with AeroTEM flown by Aeroquest) led to about **200,000 ha staked**. Five companies alone invested more than **C$12M** in the QUEST area in two years.
  - **Takeaway:** government-paid, free-release data creates value, but the government captures none of the upside. A private player that flies first and stakes first would capture it.
- **Xcalibur Smart Mapping**, the largest airborne contractor (40+ aircraft), runs government "Country Mapping" programmes:
  - **DRC:** more than **3 million line-km** over about 700,000 km² (about 35% of the country) across three years, with 8 aircraft mobilised and up to 12 at peak.
  - **Other programmes:** Egypt (national), Saudi Arabian Shield, Uganda, Nigeria, Angola, and AusAEM in Australia.
  - **Unknowns:** the fetched pages disclose no commercial terms, data ownership or resale model. For the DRC, the government and Xcalibur "will work together to maximise the value of the data". That wording hints at a data-monetisation or co-ownership deal, but it is unconfirmed.
  - **Ownership history:** Xcalibur took over CGG's Multi-Physics airborne business around 2019 (unverified).
- **Geotech** (VTEM, ZTEM; surveys in about 71 countries): its site makes no mention of multi-client or speculative surveys. Geotech has historically flown occasional speculative ZTEM/VTEM blocks for later licensing, but I could not source this (unverified).
- **CGG/Fugro airborne** held small multi-client airborne magnetics and gravity libraries, such as offshore and frontier basins, mostly oil and gas oriented (unverified). For context, CGG bought Fugro's Geoscience Division for €1.2B in 2012 and rebranded as Viridien in May 2024.
- **Net:** no TGS-equivalent exists for mineral airborne data. Explanations (estimate):
  - Mineral claims are small and fragmented, so there are few buyers per block.
  - Mining-district assessment rules push data into the public domain once confidentiality expires. Saskatchewan's GeoDS/MARS is the reason Terranox's ML input data exists at all.
  - Juniors are cash-poor.
  - The value sits in the land, not the data. That argues for survey-then-stake rather than survey-then-license.

### 3. Survey-for-equity, survey-for-land and proprietary-geophysics-to-own-projects
- **Ivanhoe Electric (NYSE American and TSX: IE)** is the best example of a geophysics company taking land positions on what it finds:
  - **Technology:** the proprietary Typhoon ground IP/EM system (I-Pulse lineage, successor to the 2009 Zeus system), claimed to reach more than 1.5 km deep and "5x deeper" than other equipment. A 72 km² fully 3D IP survey was run at Tintic.
  - **Projects:** it owns Santa Cruz copper in Arizona (PFS released September 2026; EXIM preliminary letter for US$1.1B of debt) and Tintic in Utah.
  - **Ma'aden JV:** a 50/50 exploration JV over about 50,000 km² of the Arabian Shield. Ma'aden paid US$127.1M for 9.9% of Ivanhoe Electric plus a US$20.4M top-up, and about US$66M funded the JV. Ivanhoe operates during exploration, and Ma'aden takes over at development. 1,345 km² of licences were added in September 2025.
  - **This is effectively "geophysics-for-equity" at sovereign scale:** the partner pays cash and land access, and the technology owner gets 50% of the discoveries.
  - **Third-party services:** subsidiary Computational Geosciences Inc. sells inversion and analytics services to third parties (no revenue disclosed).
  - **Caveat:** Typhoon is ground-based, not airborne.
- **Fleet Space (ExoSphere ambient-noise tomography), KoBold Metals and Earth AI** follow similar "own the tech, share the upside" patterns (unverified; the Wikipedia fetch failed). The Fleet Space amount, A$150M raised in 2025, is (estimate).
- Survey-for-royalty deals by airborne contractors are rare and anecdotal. Contractors occasionally take shares in juniors in lieu of cash during downturns (estimate/unverified). No sourced example.
- **Prospect-generator model:** EMX Royalty and Altius (unverified details) fund cheap early-stage work such as airborne surveys and data compilation, stake ground, then vend it out for cash, equity and retained royalties (often 1–3% NSR, estimate). This is the closest scalable template for an airborne survey and land-banking company.

### 4. Aggregated or shared mobilisation (cost-sharing to cut the ~US$100k ticket)
- Helicopter time-domain EM costs are typically about **US$150–250 per line-km**, with mobilisation and demobilisation of **US$15k–50k** for remote northern Saskatchewan (estimate). On a US$100k survey of about 400 line-km, mobilisation can be 20–40% of the cost (estimate).
- **Shared campaign model:** one aircraft mobilises once to the Athabasca, sells line-km slots to several claim holders, and flies speculative infill lines between client blocks. These lines go into a proprietary library, or into staking before a public release.
  - **Precedent:** Geoscience BC's bundled regional blocks; contractors' informal "piggy-back" pricing when already in an area (estimate).
- **Saskatchewan grant support:** the Targeted Mineral Exploration Incentive covers 25% of eligible costs, capped at **C$50k per year for uranium** (C$150k for other hard rock). Eligible work includes drilling, borehole and **ground** geophysics, and since 2025 most geological and geotechnical tasks; airborne is not listed. The 2026–27 budget is C$3.5M, and the program supported C$245.6M of project spend with C$8.7M in grants over 2018–2026.
  - **Gap:** airborne surveys appear ineligible. That leaves room to lobby, or to package airborne into eligible ground follow-up.

### 5. What this implies for a new venture (synthesis)
- **Option A: shared-mobilisation airborne campaigns with a speculative-data kicker.**
  - **Revenue:** slots sold at 30–50% below standalone cost (estimate); infill data licensed later.
  - **Risk:** small buyer pool, and assessment-filing rules eventually make data public. The TGS 2.0x sales-to-investment ratio is unlikely to transfer, because mining blocks have perhaps 3–10 potential buyers (estimate) against dozens of oil majors.
- **Option B: survey-then-stake, as a land bank or prospect generator.**
  - **Approach:** cheap drone or fixed-wing radiometrics, magnetics and EM over open ground, staked before release, then vended for equity and NSR.
  - **Evidence:** QUEST shows 200,000 ha staked off about C$5M of free data, so that value exists to capture.
  - **Upside:** best capture of upside; Ivanhoe/Ma'aden shows sovereign-scale capital will pay for it.
- **Option C: sovereign or regional "country mapping" with data co-ownership**, the Xcalibur DRC model. It brings large contracts (3M+ line-km) but is a services business with government counterparties.

## Sources
- TGS financial reports index: https://www.tgs.com/financial-reports
- TGS Q4 2025 earnings release: https://www.tgs.com/hubfs/Investor%20Relations/Q4%202025%20earnings%20release.pdf
- TGS Q2 2026 earnings release: https://www.tgs.com/hubfs/Investor%20Relations/Earnings%20Release%20Q2%202026.pdf
- TGS 2025 annual report (too large to parse): https://www.tgs.com/hubfs/Financial%20Reports/Annual%20Reports/2025%20Annual%20Report/TGS%202025%20Annual%20Report.pdf
- ION Geophysical: https://en.wikipedia.org/wiki/ION_Geophysical
- CGG/Viridien: https://en.wikipedia.org/wiki/CGG_(company)
- Fugro: https://en.wikipedia.org/wiki/Fugro
- Xcalibur home: https://xcaliburmp.com/
- Xcalibur Country Mapping: https://xcaliburmp.com/country-mapping-programme/
- Xcalibur DRC: https://xcaliburmp.com/democratic-republic-of-the-congo-launches-major-airborne-geophysical-and-geological-mapping-programme/
- Xcalibur Egypt: https://xcaliburmp.com/egypt-launches-first-nationwide-airborne-mineral-survey-in-42-years-with-xcalibur-smart-mapping/
- Geotech: https://geotech.ca/
- Geotech survey locations: https://geotech.ca/survey-locations/
- Geoscience BC 2008 annual report (QUEST): https://cdn.geosciencebc.com/pdf/GBC_Explorer_08.pdf
- Geoscience BC annual reports index: https://www.geosciencebc.com/updates/annual-reports/
- Ivanhoe Electric: https://www.ivanhoeelectric.com/
- Ivanhoe Electric Typhoon: https://www.ivanhoeelectric.com/technologies/typhoon/
- Ivanhoe Electric Ma'aden JV: https://www.ivanhoeelectric.com/electric-metals/saudi-arabia-maaden-jv/
- Computational Geosciences Inc.: https://www.ivanhoeelectric.com/technologies/computational-geosciences-inc/
- Saskatchewan TMEI: https://www.saskatchewan.ca/business/agriculture-natural-resources-and-industry/mineral-exploration-and-mining/targeted-mineral-exploration-incentive
- Saskatchewan Geological Survey: https://www.saskatchewan.ca/business/agriculture-natural-resources-and-industry/mineral-exploration-and-mining/saskatchewan-geological-survey
