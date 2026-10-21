# B03: Geothermal PPA prices 2022-2026 and the implied value of a proven resource

**Method note.** The shared WebSearch budget for this run was used up before this agent started, so no new search queries were run. Everything below comes from direct fetches and downloads of primary documents: Fervo's 424B4 prospectus (SEC, May 2026), Ormat's FY2025 10-K and Q2-2026 10-Q (SEC), CPUC decisions D.21-06-035 and D.24-02-047, the CPUC 2026 Padilla Report and the 2025 RPS Annual Report, and Meta's and Latitude Media's pages. It also uses sourced numbers from sibling file B01. Items from memory that I could not re-fetch are marked (unverified). "(calc)" marks my own arithmetic.

## 1. Headline: geothermal PPA prices went from $60-80 to above $100/MWh

The cleanest primary statement is in **Ormat's FY2025 10-K** (filed 26 Feb 2026):

> "Ormat has signed several PPAs for new capacity and for existing capacity renewal across its U.S. geothermal fleet at prices **above $100 per MWh**, compared to PPAs executed at levels generally **between $60 per MWh and $80 per MWh during the prior five years**." It attributes the change to "direct demand from hyper-scalers and constrained availability of firm, dispatchable generation."

- Ormat's realized average electricity price across the fleet was **$92.6/MWh in 2025** and **$94.3/MWh in 2024**. This average blends in Kenya and Hawaii (Puna), which are high-price, so the US legacy contracts sit lower. The fleet generated 7,493,287 MWh in 2025.
- Ormat's recent new contracts (10-K and Q2-2026 10-Q):
  - **Feb 2026:** a long-term portfolio PPA for **up to 150 MW of new geothermal for Google**, through NV Energy's Clean Transition Tariff (CTT).
  - **Jan 2026:** a **20-year PPA with Switch** for about 13 MW from Salt Wells (Fallon, NV).
  - The Hawaii PUC approved a new fixed-price Puna PPA running to 2052.
- **Prices are not disclosed for any of these.**
- The Blue Mountain acquisition (20 MW, Jun 2025, $88.7M) put a **$16.8M liability on the books for a below-market NV Energy PPA** that expires end-2029 (B01, from the Ormat 10-Q). That is direct evidence that legacy geothermal PPAs now sit well below what new contracts clear at.

## 2. Fervo: about $90-100/MWh implied, and $115/MWh used as the planning price

The **Fervo 424B4** (May 2026) shows:

- **658 MW of binding PPAs.** Buyers are SCE, Google/NV Energy, Clean Power Alliance, Desert Community Energy, CalChoice and Shell, all on **"similar 15 year contracted terms."**
- **About $7.2B "potential revenue backlog."** This is calculated "using expected energy output, as defined in each PPA, over the entire term ... and reflects contracted pricing (including any escalators or indexation)."
  - About **$5.7B** of the backlog is with utilities.
- Pricing "is generally fixed for the duration of the contract," with some index escalators.
- **Implied average price (calc):** $7.2B ÷ (658 MW × 8,760 h × 15 yr × capacity factor):
  - **~$100/MWh at 83% CF**
  - ~$93/MWh at 90% CF
  - ~$88/MWh at 95% CF
  - These are nominal, escalators included.
- Fervo's own **illustrative EGS unit economics** use **"firm-power pricing of approximately $115 per megawatt hour."** The other assumptions are 83% CF, $160/kW-yr O&M and a $30/MWh tax credit. On those inputs Fervo gives **EBITDA of $650-700k per MW-yr without tax credits and $850-950k per MW-yr with them.**
- Under the OBBBA amendments, 45Y/48E credits stay at 100% for projects that **begin construction by end-2033**, fall to 75% and 50% for 2034-35, and end from 2036.
- Cape Station capex is about **$7,000/kW** (FOAK, per 50 MW GeoBlock). The long-run target is $3,000/kW.

SCE/CPA detail from the CPUC 2025 RPS Annual Report (Table 11, Table 14, Table 16):

| Buyer | Project | Size | Term | COD |
|---|---|---|---|---|
| SCE | Millard County UT geothermal (Fervo Cape Station) | 336 MW | 15 yr | 2028 |
| SCE | Millard County UT geothermal (Fervo Cape Station) | 62 MW | 15 yr | 2027 |
| Shell Energy NA | Beaver County UT geothermal | 31 MW | — | 2026 |
| San Jose Clean Energy | Imperial County geothermal | 24.5 MW | 20 yr | 2028 |

- The Fervo 424B4 gives the Shell contract a 15-year delivery term. The RPS report table lists 20 years.
- Fervo's SCE PPAs **require firm end-to-end transmission** to the delivery points (424B4). That is a real cost for out-of-state supply.
- The headline "320 MW SCE" figure (Jan 2024 press release) could not be re-fetched; the page came back empty. The CPUC table above is the primary record of the SCE contracts.

**Google 3 GW Geothermal Framework Agreement** (424B4, signed 19 Mar 2026):

- It is **not a PPA**. Fervo must propose at least 1 GW within two years and up to 3 GW through 2033.
- Google has ROFRs, exclusivity, and **audit rights over Fervo's project costs and pricing methodology**.
- Either party can terminate if no definitive offtake is signed by 19 Mar 2028.
- Implication: the hyperscaler is negotiating **cost-plus style visibility**, not paying a blind premium.

## 3. California regulatory pull: the CPUC firm clean mandate

- **D.21-06-035** (24 Jun 2021) ordered 11,500 MW of new net qualifying capacity.
  - It includes a **minimum of 1,000 MW of "firm resources with zero on-site emissions"** (CF of at least 80%, not weather-dependent, generating rather than storage), plus 1,000 MW of long-duration storage.
  - Both were first due in 2026.
  - The 2021 proposal had specified "at least 1,000 MW of geothermal." The final order made it technology-neutral firm clean, but in practice the category is geothermal.
- **D.23-02-040** moved the long-lead-time (LLT) deadline to **1 Jun 2028**.
- **D.24-02-047** (15 Feb 2024) lets LSEs extend to **no later than 1 Jun 2031** if they cover the gap with generic capacity.
  - This keeps the LLT demand alive for another five years rather than letting it lapse.
- **CPUC 2023 Preferred System Plan** (D.24-02-047, Table 4, 25 MMT core case): new geothermal of **0.8 GW (2026), 1.1 GW (2028), 1.5 GW (2030), 2.0 GW (2033-2045)**.
  - The high-gas-retirement sensitivity reaches **5.1 GW by 2039**.
  - The decision also adds **Central Nevada geothermal potential** to the planning maps. That puts Nevada resources inside California's planning demand.
- **AB 1373 central procurement:** the CPUC later found need for DWR central procurement that reportedly includes **up to ~1 GW of geothermal** (D.24-08-064, Aug 2024) (unverified; could not fetch).
- **What CA buyers pay:**
  - **2026 Padilla Report:** IOU weighted-average 2025 RPS *expenditure* on geothermal was **8.2¢/kWh ($82/MWh)**; SCE alone was 6.9¢. The CCA geothermal weighted average was **6.5¢/kWh**. Both are mostly legacy contracts.
  - **New 2025 geothermal contract prices are redacted** ("Only 1/2 Contracts"), which confirms that per-deal prices are confidential.
  - **2025 RPS Annual Report:** average price of all IOU/CCA/ESP RPS contracts executed in 2024 was **8.1¢/kWh, up from 5.9¢/kWh real in 2023**, a general market step-up.

## 4. Nevada: the Clean Transition Tariff and Google

- The PUCN approved NV Energy's CTT in **mid-May 2025** (Latitude Media, 15 May 2025).
- The first deal is **115 MW from Fervo's Corsac Station for Google**.
  - Google funds a specific new resource through a long-term arrangement with NV Energy, so other ratepayers carry no added rate burden.
  - **No $/MWh or premium is disclosed.** Interconnection is "the primary bottleneck." COD is two to five years out.
- The second CTT deal is **Ormat's up to 150 MW** for Google (Feb 2026), with deliveries 2028-2030 (sibling files).
- **The CTT matters because it is a regulator-approved product for a buyer paying a premium for a named geothermal asset.** That is exactly the buyer a Terranox-shape company wants at the end of its chain.
- The CTT tariff ESA price itself (PUCN docket 24-06014) is not public in anything I could fetch (unverified that it is fully confidential).

## 5. Meta

- **Meta-Sage** (26 Aug 2024): **up to 150 MW**, first phase online in 2027, location "east of the Rockies." **No price disclosed** (about.fb.com).
- **Meta-XGS** (Jun 2025): up to 150 MW in New Mexico (PNM territory). Price undisclosed (from sibling files; the Business Wire fetch failed).
- **Meta's 300 MW of geothermal signed so far has no disclosed price.** These are framework or "up to" deals with next-generation technology developers.

## 6. Cost benchmarks

- Lazard LCOE+ (2024-2025) puts unsubsidized geothermal at roughly **$64-109/MWh** (unverified; not re-fetched).
- DOE's Enhanced Geothermal Shot target is **$45/MWh by 2035** (sibling L-files).
- New PPAs at $100-115/MWh are therefore at or above the top of the historical LCOE band. Today the binding constraint on new geothermal is scarcity of developable sites, not price.

## 7. Implied value per MW of a proven resource (calc)

The inputs:

- **Energy per MW:** 8,760 h × ~83-90% CF ≈ **7,300-7,900 MWh per MW-yr**.
- **Contract revenue:** at $100-115/MWh, that is **$0.73-0.91M per MW-yr**.
- **Fervo's EBITDA framing:** $0.65-0.95M per MW-yr.

| Layer | Basis | $/MW (calc unless noted) |
|---|---|---|
| PV of EBITDA, 15-yr PPA, 8% | $0.65-0.95M × 8.56 | **$5.6-8.1M** |
| PV of EBITDA, 30-yr life, 8% | $0.65-0.95M × 11.26 | **$7.3-10.7M** |
| Less capex: EGS FOAK $7.0M/MW (Fervo) | | **~$0.3-3.7M/MW** residual for the resource plus development rights |
| Operating hydrothermal plant M&A (Ormat buys 2018-2025, B01) | | **$4.3-5.6M/MW EV** |
| Pre-PPA development portfolio (USG 2017, B01) | | **~$0.1M/MW** |
| Fervo public equity per PPA-MW (May 2026 IPO, B01) | | **~$11.6M** |
| Royalty-only claim: Centaurus $5/MWh (Fervo 424B4) | $5 × ~7,600 MWh ≈ $38k/MW-yr, 20 yr at 8% | **~$0.37M/MW** |
| Value of the price step-up alone | +$30/MWh (from $70 to $100) × 7,300 MWh = $219k/MW-yr, 20 yr at 8% | **~$2.1M/MW** |

**Key reads:**

1. **The PPA price step-up alone adds about $2M per MW** to any resource that can be contracted now.
   - A 50 MW proven hydrothermal resource gains about $100M from repricing alone.
   - Hydrothermal capex is likely below EGS at roughly $4-6M/MW (unverified), so a proven, contract-ready hydrothermal resource is plausibly worth **$1-4M/MW** to a developer before construction.
   - Pre-proof dirt was valued at about **$0.1M/MW** (USG). The gap between the two is the step-up a Terranox-shape company captures.
2. **The value is realized at the PPA.** The lift runs from about $0.1M/MW for unproven, uncontracted land to about $11.6M per PPA-MW in public markets. What converts land into value is a *contractable* MW: a resource proven enough, with a transmission and interconnection path, to sign a 15-20 yr PPA.
3. **Prices are almost always confidential**, including in the CPUC Padilla redactions, Google's CTT, Meta, SCE and Google's audit-rights GFA. Buyers pay for certainty of MW and COD more than for a headline $/MWh.

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **The buyer side is strong and price-insensitive at the margin.**
   - Ormat itself reports new US geothermal PPAs at **>$100/MWh, up from $60-80**.
   - Fervo's backlog implies ~$90-100/MWh, and it plans on $115.
   - Hyperscalers (Google 3 GW GFA, Google/Ormat 150 MW, Google/Fervo 115 MW, Meta 2 × 150 MW), NV Energy's CTT, and California's 1 GW firm clean requirement (extendable to 2031; PSP 1.1-2.0 GW new geothermal) all want MW they can contract.
   - "Too small" does not apply: each proven 50 MW is worth tens to roughly $100M+ of step-up.
2. **The bottleneck is proven, interconnectable sites, not money.**
   - Ormat must fill a 150 MW Google portfolio with *new* capacity by 2028-2030.
   - Fervo must propose 1 GW to Google within two years.
   - Both need more resources than their own exploration pipelines produce. A company that finds blind resources from public data, locks up BLM, state and private rights cheaply (Fervo paid about **$4/acre** in 2019-21), proves them to PPA-grade, and sells or JVs them to Ormat, Fervo, utilities or CTT customers sits exactly at the price-setting point.
3. **The best exit product is a "PPA-ready MW" package, not a lease.**
   - The package is a resource, a temperature and flow case, a transmission path, and a land and permit stack.
   - Selling at the pre-PPA stage captures roughly $1-4M/MW. Retaining a royalty instead (Centaurus-style $5/MWh, about $0.37M/MW) is a lower-risk tail that keeps ownership upside.
4. **Gap vs Zanskar.**
   - Zanskar uses AI to find blind systems and then **develops and operates them itself**: it bought Lightning Dock in NM and raised venture money to drill and build. That means it consumes capital per MW, works one pipeline at a time, and competes with Ormat and Fervo for the same PPAs.
   - The open gap is to be the **neutral origination and asset-ownership layer that supplies everyone** (Ormat, Fervo, Sage, XGS, utilities, CTT hyperscalers, even Zanskar). It would cover the whole Basin & Range plus CA and NV LLT-eligible geography, plus Utah/NM/east-of-Rockies sedimentary plays where Meta/Sage/XGS are buying.
   - Its edge would be breadth of public data turned into rights, faster than the developers can do it themselves. Value is booked at the PPA-readiness step-up, without carrying $5-7M/MW of construction.
   - Today's PPA pricing ($100+/MWh) and the 2033 tax-credit construction deadline create a time-boxed window (2026-2033) in which developers will pay most for contract-ready sites.
5. **Risks to price.**
   - Prices are confidential, so a buyer can claim lower resource values.
   - Firm transmission requirements (SCE) and interconnection queues cut what a remote resource is worth.
   - Credits step down after 2033.
   - If EGS hits $45/MWh and $3,000/kW, PPA prices could fall back toward $70-80. Even then, a proven hot site keeps value as an EGS host.

## Sources

- Fervo Energy 424B4 prospectus (May 2026): https://www.sec.gov/Archives/edgar/data/1853868/000162828026034849/fervoenergy-424b4.htm
- Fervo SEC filing index (CIK 1853868): https://data.sec.gov/submissions/CIK0001853868.json
- Ormat FY2025 10-K: https://www.sec.gov/Archives/edgar/data/1296445/000129644526000006/ora-20251231.htm
- Ormat Q2-2026 10-Q: https://www.sec.gov/Archives/edgar/data/1296445/000129644526000014/ora-20260630.htm
- CPUC D.21-06-035 (Mid-Term Reliability): https://docs.cpuc.ca.gov/PublishedDocs/Published/G000/M389/K603/389603637.PDF
- CPUC D.24-02-047 (2023 PSP; LLT extension to 2031): https://docs.cpuc.ca.gov/PublishedDocs/Published/G000/M525/K918/525918033.PDF
- CPUC 2026 Padilla Report: https://www.cpuc.ca.gov/-/media/cpuc-website/industries-and-topics/documents/energy/rps/2026/2026-padilla-report.pdf
- CPUC 2025 RPS Annual Report: https://www.cpuc.ca.gov/-/media/cpuc-website/industries-and-topics/documents/energy/rps/2025/2025-california-renewables-portfolio-standard-rps-annual-report.pdf
- Latitude Media on CTT approval (15 May 2025): https://www.latitudemedia.com/news/the-clean-transition-tariff-won-approval-in-nevada-whats-next-for-fervo/
- Meta-Sage announcement (26 Aug 2024): https://about.fb.com/news/2024/08/new-geothermal-energy-project-to-support-our-data-centers/
- Sibling file B01 (M&A $/MW comps): /home/user/nuketime/research/geothermal/evidence/B01-step-up.md
