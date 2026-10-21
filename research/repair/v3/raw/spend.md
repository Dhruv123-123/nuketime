# Top-down spend: US and global nuclear parts, safety-related parts, CGD

Compiled 2026-10-21. "(recalled)" = from memory, not verified this session. Everything else has a source.

## 1. Fleet O&M envelope (sourced)

### NEI "Nuclear Costs in Context", 2025 cost data (published Aug 2026; EUCG data)
URL: https://www.nei.org/getContentAsset/47fa8caa-9b0d-4029-932c-07f902e82f4f/8d8ff8d6-b2ae-401b-a63c-f6b108e809d2/2024-Costs-in-Context-final.pdf (the URL says 2024, but it now serves the Aug 2026 edition)

| $/MWh (2025$) | Fuel | Capital | Operating | Total |
|---|---|---|---|---|
| 2012 | 9.96 | 15.24 | 30.52 | 55.72 |
| 2022 | 5.87 | 7.52 | 20.41 | 33.80 |
| 2023 | 5.60 | 7.44 | 20.43 | 33.47 |
| 2024 | 5.81 | 7.82 | 21.06 | 34.69 |
| 2025 | 5.95 | 9.69 | 20.82 | 36.46 |

- Capex: $7.59B in 2025, up from $6.10B in 2024 (2025$). This works out to $9.69/MWh, so implied fleet generation is about 783 TWh.
- **Operating cost ≈ $20.82 × 783 TWh ≈ $16.3B/yr.** NEI says operating costs cover licensing, security, maintenance and human resources.
- **Labour ≈ $8.8B (2025)**, "more than half of operating costs", a share that has held roughly steady since 2014.
- Non-labour operating ≈ $7.5B. This covers materials, contracted/outside services, NRC fees, insurance, INPO/NEI dues and other items.
- The operating-cost chart is broken down by *process* (EUCG categories), not by cost element. My readings from the chart for 2025, in $/MWh (approximate): Work Management (maintenance) ~5.3; Support Services ~6.8; Operations ~3.5; Loss Prevention (security etc.) ~2.8; Engineering ~1.4; Training ~0.5; Materials & Services (supply-chain process cost) ~0.3–0.5; Fuel Management small. Work Management ≈ 5.3 × 783 TWh ≈ **$4.1B**.
- Other 2025 figures: regulatory capex $270M; uprate capex $365M; capacity factor 92%; merchant plants $31.47/MWh vs cost-of-service $40.31/MWh; single-unit plants $45.77 vs multi-unit $34.36.

### EIA Electric Power Annual Table 8.4 (major IOUs, FERC Form 1 basis), mills/kWh
URL: https://www.eia.gov/electricity/annual/html/epa_08_04.html

| Year | Nuclear operation | Nuclear maintenance | Nuclear fuel | Total |
|---|---|---|---|---|
| 2020 | 10.05 | 5.78 | 6.10 | 21.92 |
| 2022 | 10.51 | 6.10 | 6.12 | 22.73 |
| 2023 | 9.52 | 6.36 | 6.12 | 22.00 |
| 2024 | 9.87 | 6.84 | 6.37 | 23.08 |

Applying these rates to the whole fleet (783 TWh): maintenance ≈ $5.4B; operation plus maintenance ≈ $13.1B. That is lower than NEI's $16.3B because Form 1 production O&M leaves out A&G and some support costs.

### FERC Form 1 nuclear maintenance accounts 528–532 (via PUDL `core_ferc1__yearly_steam_plants_sched402`, plant_type = nuclear)
Source: https://s3.us-west-2.amazonaws.com/pudl.catalyst.coop/stable/core_ferc1__yearly_steam_plants_sched402.parquet (Catalyst Cooperative PUDL; data from FERC Form 1 pp. 402–403). Column mapping: 528 = opex_engineering, 529 = opex_structures, 530 = opex_boiler (reactor plant equipment), 531 = opex_plants (electric plant), 532 = opex_misc_steam (misc nuclear plant). Form 1 covers only rate-regulated / FERC-jurisdictional owners, about 41% of US nuclear MWh. Constellation, Vistra and other merchant fleets do not file it. Some plants are double-counted across co-owners (e.g. Wolf Creek, Palo Verde), so treat the totals as ±5%.

| Year | Net gen (TWh) | 528 | 529 | 530 | 531 | 532 | **Maint 528–532 ($M)** | $/MWh maint | Prod O&M total ($M) | $/MWh total |
|---|---|---|---|---|---|---|---|---|---|---|
| 2018 | 304 | 360 | 121 | 561 | 333 | 429 | 1,805 | 5.93 | 7,244 | 23.80 |
| 2022 | 306 | 452 | 90 | 500 | 294 | 508 | 1,845 | 6.03 | 6,865 | 22.46 |
| 2023 | 298 | 431 | 84 | 447 | 275 | 736 | 1,973 | 6.62 | 6,818 | 22.86 |
| 2024 | 319 | 456 | 90 | 427 | 302 | 876 | 2,151 | 6.74 | 7,247 | 22.72 |
| 2025 | 320 | 440 | 92 | 465 | 366 | 895 | 2,258 | 7.05 | 7,578 | 23.66 |

- Scaled to the fleet: $7.05/MWh × 783 TWh ≈ **$5.5B/yr nuclear maintenance expense** (labour + materials + contractors), plus capitalised replacements.
- Per site, 2024 maintenance expense ranges widely. Diablo Canyon $384M (an outlier tied to its life extension); Cook $137M; ANO $120M; Oconee $98M; Brunswick $87M; Farley $84M; River Bend $82M; Surry $81M; McGuire $81M; Grand Gulf $79M; Fermi 2 $78M; Waterford $71M; Callaway $69M. **A typical site spends $50–120M/yr on maintenance expense.**
- Form 1 does not split materials from labour within 528–532. The M&S inventory (acct 154, p. 227) is reported by function and is not nuclear-specific, so I did not extract it.

## 2. Materials & supplies inventories (sourced, SEC XBRL)
SEC companyfacts API: https://data.sec.gov/api/xbrl/companyfacts/CIK0001868275.json (Constellation), CIK0001692819 (Vistra Operations).
- **Constellation** `InventoryRawMaterialsAndSuppliesNetOfReserves`: $1,216M (2023), $1,357M (2024), **$1,485M (2025-12-31)**. This is the pre-Calpine balance sheet; the Calpine deal closed in early 2026 (recalled). Constellation is mostly nuclear: ~22 GW nuclear, ~21 operated units at ~12–13 sites, plus minority stakes in STP and Salem (recalled). Some of the balance is fossil/hydro M&S. Implied M&S ≈ **$90–115M per nuclear site**.
- **Vistra Ops** M&S: $289M (2023) → $533M (2024). The +$244M step is mostly the Energy Harbor acquisition (Mar 2024: Beaver Valley 1/2, Davis-Besse, Perry; 3 sites, 4 units, ~4 GW), which gives **~$80M of M&S per nuclear site**.
- ScottMadden "Materials Management within U.S. Nuclear Generation Plants" (benchmark data from 2004–06): https://www.scottmadden.com/content/uploads/2018/07/Materials-Management-within-U.S.-Nuclear-Generation-Plants.pdf
  - Average on-site material at nuclear plants ~$40–43M (2004–06), growing 3.8%/yr. Median $35,409/MW.
  - **Inventory turnover 0.19–0.91/yr; ~995 days on hand**; ~$20M slow/non-moving stock per plant.
  - Median warehouse transaction value $45M/yr (all transactions: receipts, issues, returns).
- Fleet M&S inventory ≈ 54 sites × $80–110M ≈ **$4.5–6B**. At 0.3–0.5 turns/yr, warehouse issues come to **≈ $1.4–3.0B/yr**, which is a direct proxy for annual replacement-parts consumption.

## 3. Cost-element split (labour / materials / outside services)
- NEI/EUCG 2025: labour $8.8B ≈ 54% of operating costs; non-labour ≈ $7.5B (46%).
- OPG (Ontario) base OM&A, EB-2010-0008 rate filing: regular labour ~77%, materials ~6.7%, other purchased services ~8.4%, licences ~1.7% (via search summary). OPG also cites "direct labour for EUCG members is 52% of O&M" (EB-2007-0905). Source: https://archive.opg.com/pdf_archive/Regulatory%20Affairs/z8--EB-2010-0008/Exhibit%20F%20-%20Operating%20Costs/R092_F2-02-01_Tables.pdf (the direct fetch returned HTML, so I could not verify it).
- Rule of thumb for US fleets (recalled; consulting/EUCG talk): labour 50–55%, contractors/outside services 20–30%, materials 10–15%, other (fees, insurance, dues) 8–12%.
- Within non-labour $7.5B, my allocation (assumptions): NRC fees ~$0.45B (≈$5M/unit annual fee × 94, recalled); insurance (ANI/NEIL) ~$0.3B (recalled order of magnitude); INPO/NEI/EPRI dues ~$0.2B (recalled order of magnitude); **outside services ~$4.0–4.5B; O&M materials ~$1.5–2.5B**.

## 4. Safety-related share and CGD share
- **ENEC (Barakah)**: "roughly 20–30% of items and services at an operating plant are safety related (Quality Class Q)". https://www.enec.gov.ae/suppliers/supplier-education/general-requirements-for-working-at-barakah-npp/nuclear-related-products-and-services
- **EPRI 3002029261** (CGD experience & efficacy, Nov 2024), downloaded PDF: https://restservice.epri.com/publicdownload/000000003002029261/0/Product
  - p.17: "licensees surveyed indicate that for more than 20 reactors, between 25% and 50% of all safety-related items procured involve CGD (performed internally or outsourced)"; "One licensee reported that CGD is involved in more than half of all safety-related procurements."
  - Duke (11 units, 6 sites): centralised CRDF at Harris handles "25–50% of all safety-related procurements across the entire fleet"; 95% of Method 1 tests done in-house; "Lead time is the primary issue"; "Given more resources and personnel, Duke Energy would be performing more CGD"; maintains a CGD backlog.
  - "All NPPs in the United States utilize dedicated CGIs ... in some cases a majority of a utility's safety-related procurements."
  - Paragon: 70–100 new CGD plans/month; ~1,300 CGD jobs/yr; digital <5% of jobs but rising; ~120 approved commercial suppliers.
  - UCI: >75% of CGIs sourced from distributors; Method 1 ~90% of the time.
  - Spain: at one NPP CGD is ≥50% of SR procurements; CNAT does 30% of CGD in-house and outsources 70%.
  - Globally ~40% of reactors use CGD regularly, ~40% have piloted it or use it sparingly, and ~20% never use it. 31% of respondents report increasing CGD volume, 64% stable, 5% decreasing. Licensees say quality and lead time decide; cost is the least influential factor.
- Caveat: the 25–50% figure counts *items/procurements*, not dollars. Large ASME III / Code items and engineered equipment (pumps, valves, SGs, I&C systems) are mostly bought as basic components from App B OEMs. So CGD's share of SR *dollars* is probably below its share of SR line items. I use 15–40% by value.

## 5. Top-down estimate (US)

Assumptions: fleet 94 units / 54 sites (recalled), 783 TWh (2025, derived from NEI).

**(a) US nuclear parts/materials spend (non-fuel)**
| Component | Low | Central | High | Basis |
|---|---|---|---|---|
| O&M materials (expensed) | 1.5 | 2.0 | 2.5 | $7.5B non-labour minus services, fees and insurance; consistent with warehouse issues of $1.4–3.0B |
| Materials inside capex (replacement equipment, projects) | 1.5 | 2.3 | 3.0 | 20–40% of $7.59B capex |
| **Total parts & materials** | **3.0** | **4.3** | **5.5** | $B/yr |
| of which recurring replacement parts / MRO via warehouse | 1.5 | 2.2 | 3.0 | inventory $4.5–6B × 0.3–0.5 turns |

**(b) Safety-related parts spend**
Assumption: 25–40% of parts dollars are safety-related. That is slightly above ENEC's 20–30% item share, because SR items cost more per unit (premium pricing).
- On replacement parts/MRO ($1.5–3.0B): **SR ≈ $0.4–1.2B, central ~$0.7B**.
- Including SR capital equipment: **SR ≈ $0.8–2.0B, central ~$1.3B**.

**(c) CGD-routed spend and dedication premium pool**
- CGD share of SR spend by value is 15–40% (central 30%). CGD-routed SR parts spend is therefore **≈ $0.1–0.5B/yr (central ~$0.25–0.35B)**. Most of it is MRO-type parts (relays, breakers, fasteners, O-rings, gaskets, fittings, electronic modules, instruments), which fits the startup's target.
- **Dedication premium pool**: the difference between what the plant pays for the dedicated item (or its internal dedication cost) and the commercial price. Premiums run 2–10x on cheap parts and 30–100% on expensive ones (recalled, industry anecdote). Assume the premium is 40–65% of dedicated value: **≈ $50–300M/yr, central ~$150M.**
- Cross-check, bottom-up: ~8,000–15,000 US dedication jobs/yr (Paragon ~1,300, plus in-house CRDF-type labs at Duke, Southern, TVA, Dominion, Constellation, and other third parties such as Curtiss-Wright, Nuclear Logistics, AZZ/NLI, Sargent & Lundy (assumption)) × $5–25k/job (engineering + test + paperwork, recalled) ≈ $40–375M. This overlaps the top-down range.
- The **adjacent pool** is lead-time and outage value. EPRI says lead time drives CGD decisions more than price. The value of days rather than months shows up as avoided inventory carrying cost on the $4.5–6B of M&S (~8–10%/yr = $0.4–0.6B/yr carrying cost), plus avoided outage extensions and LCOs. This value is larger than the premium pool itself but is not counted above.

**Per site (54 sites):** maintenance expense $50–120M/yr; M&S inventory $80–110M; parts/MRO issues $30–55M/yr; SR parts $8–22M/yr; CGD-routed $2–9M/yr; dedication premium $1–5M/yr.

## 6. Global extrapolation
- US ≈ 97 GW of ~375–380 GW operating worldwide (~25%) (recalled, IAEA PRIS approx).
- Other markets: Western, Korean, Japanese and Canadian non-fuel O&M per MWh is similar to or higher than US; Chinese and Russian costs are lower and those markets are closed to a US dedicating entity.
- Global parts/materials ≈ 2.5–3.5× US, so **$8–18B**. Global SR parts ≈ **$2.5–6B**.
- CGD is regular practice at ~40% of reactors (EPRI), concentrated in the US, Canada (CSA N299 equivalent), Spain, Slovenia, Czechia, Korea (KEPIC), UAE, Mexico, Brazil, South Africa, Sweden, Switzerland and Argentina. Accessible non-US CGD pool is ~0.6–1.2× the US pool.
- **Global CGD-routed spend ≈ $0.2–1.0B; global dedication premium pool ≈ $0.1–0.6B/yr (central ~$0.3B).** About half of it is in the US.

## 7. Key uncertainties
1. No public cost-element (labour/materials/services) split for the US fleet; EUCG data is member-only. The materials share (10–15% of opex) is an assumption.
2. The SR share by dollars is unknown; ENEC's 20–30% counts items.
3. The EPRI 25–50% CGD figure counts procurements, not dollars, and is skewed toward heavy users that answered the survey.
4. Form 1 covers only ~41% of MWh, and merchant fleets may run leaner.
5. Inventory turnover comes from 2004–06 benchmarks.

## Sources
- NEI Nuclear Costs in Context (2025 data, Aug 2026): https://www.nei.org/getContentAsset/47fa8caa-9b0d-4029-932c-07f902e82f4f/8d8ff8d6-b2ae-401b-a63c-f6b108e809d2/2024-Costs-in-Context-final.pdf
- EIA EPA Table 8.4: https://www.eia.gov/electricity/annual/html/epa_08_04.html
- FERC Form 1 via PUDL: https://s3.us-west-2.amazonaws.com/pudl.catalyst.coop/stable/core_ferc1__yearly_steam_plants_sched402.parquet
- EPRI 3002029261: https://restservice.epri.com/publicdownload/000000003002029261/0/Product
- SEC XBRL companyfacts (Constellation CIK 1868275; Vistra Ops CIK 1692819): https://data.sec.gov/api/xbrl/companyfacts/CIK0001868275.json
- ScottMadden materials management benchmark: https://www.scottmadden.com/content/uploads/2018/07/Materials-Management-within-U.S.-Nuclear-Generation-Plants.pdf
- ENEC nuclear-related products: https://www.enec.gov.ae/suppliers/supplier-education/general-requirements-for-working-at-barakah-npp/nuclear-related-products-and-services
- OPG EB-2010-0008 (via search snippet only): https://archive.opg.com/pdf_archive/Regulatory%20Affairs/z8--EB-2010-0008/Exhibit%20F%20-%20Operating%20Costs/R092_F2-02-01_Tables.pdf
- NEA/EPRI 2025 LCOE (context only): https://smrintel.com/news/nea-epri-lcoe-report-2025-nuclear-lowest-cost
