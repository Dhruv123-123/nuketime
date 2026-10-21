# v3 / pricing: Nuclear CGD pricing, willingness to pay and the value-per-event model

Date: 2026-10-21. Topic: per-item dedication prices and premium, engineering hours, reverse-engineering (RE) and EQ/seismic costs, outage-day cost, frequency of part-driven outage extensions, inventory carrying cost, and a value-per-event model.

## 0. Evidence quality and method
- I used 6 WebSearch calls (the quota) and then WebFetch/curl against known URLs. I pulled PDFs as files and read them with pdftotext.
- **VERIFIED** means I read the figure in the source during this session, and the URL is given.
- **(recalled)** means the figure is from memory and was not checked here. Treat recalled figures as accurate to within about a factor of 1.5.
- **(estimate)** means my own arithmetic or assumption.
- Biggest gap: **no public source gives per-item dedication prices or engineering hours per technical evaluation.** EPRI says so implicitly: its 2024 global survey of CGD reports volumes and percentages, not dollars. These figures sit in vendor quotes and utility purchase-order data, so they have to come from customer interviews.

---

## 1. Volumes and behaviour: what EPRI 3002029261 (Nov 2024) actually says (VERIFIED)
Source: EPRI, *Commercial-Grade Item Dedication (CGD) Experience and Efficacy*, 3002029261, Nov 2024, PM M. Tannenbaum, with Apollo plus GmbH. Public download: https://restservice.epri.com/publicdownload/000000003002029261/0/Product
- About 40% of reactors worldwide use dedicated items regularly. Another ~40% have piloted CGD or done a few CGD procurements, and ~20% have never used it.
- 64% of surveyed licensees say their CGD volume is steady and 31% say it is increasing. 50% have more than 20 years of CGD experience.
- Licensees with more than 20 reactors report that **25-50% of all safety-related items procured involve CGD**.
- **Why licensees use CGD:** "Licensees reported that quality and lead time could be decisive in choosing to accept an item using CGD, while **cost was the least influential factor**." This is key for pricing: the buyer pays for speed and certainty, not for a lower unit price.
- **Duke Energy:** CGD is 25-50% of all safety-related procurements fleetwide (6 sites). The Central Receiving and Dedication Facility (CRDF) at Harris performs 95% of Method 1 tests in-house. It has a tri-axial shake table (in-house seismic), CMM arms, laser probes, 3D scanning and printing, and reverse engineering. "**Lead time is the primary issue** that drives Duke Energy to source CGIs. **Given more resources and personnel, Duke Energy would be performing more CGD**." Leadership is briefed monthly on cost savings and on "**the backlog of CGD still to be performed**." This is direct evidence of capacity-constrained, unmet demand.
- **Paragon Energy Solutions:** "generates between **70 and 100 new CGD plans each month**" and "performs approximately **1300 CGD jobs per year** (one job can include multiple lots of unique parts)." Digital devices are under 5% of jobs but increasing. Demand was "particularly strong immediately following the pandemic."
- **UCI (United Controls International):** uses Method 1 about 90% of the time. More than 75% of its CGIs come from distributors. It uses about 100 suppliers a year. Fuses are known to fail CGD testing often.
- **KHNP (Korea):** its KPI is approval of supplier CGD plans **within 14 days**. This is a benchmark for "fast" today, for plan approval alone.
- **NEK (Krško, Slovenia):** set up its CGD programme for about **$60,000 (1996 dollars)** in policy, procedures, training and surveys. By April 1998 it had 70 dedication packages.
- **Spain:** CGD is 50% or more of all safety-related procurements per year. One utility does 30% of CGD in-house and outsources 70%.

**Implied US volume (estimate):** Paragon alone does about 1,300 jobs a year. Add Curtiss-Wright, UCI, Westinghouse, Framatome, GE, Ultra and utility in-house labs (Duke CRDF and others). US fleet CGD is plausibly **8,000-20,000 dedication jobs a year**, of which perhaps 15-30% need a *new* technical evaluation rather than reuse of an existing plan.

## 2. Per-item dedication price and premium over commercial
- **No verified public per-item price was found.** The OSTI abstract (American Power Conference 1995, https://www.osti.gov/biblio/94221) says only that dedication "can also reduce overall procurement costs", meaning commercial-plus-dedication can beat N-stamp/Appendix B sourcing. It gives no numbers.
- **Recalled industry rules of thumb:**
  - A dedicated item costs **2-10x the commercial catalogue price**, and the multiple is far higher for cheap items: a $50-200 relay, fuse or fastener lot becomes $1,500-5,000 dedicated (recalled).
  - The cost is mostly fixed per lot: technical evaluation, sampling, tests, package, QA signature. So **the premium is roughly a fixed $2k-15k per lot plus 20-50% markup**, not a percentage of item value (recalled/estimate).
  - **New dedication (first-time technical evaluation plus testing):** $5k-50k. **Complex or digital (EPRI TR-106439/TR-107330 style, including software and EMI/RFI):** $100k-500k+ (recalled, d03).
  - **Re-dedication using an existing plan:** $1k-5k per lot plus test costs (estimate).
- **Implied premium vs alternatives (VERIFIED, ANS Nuclear News June 2020, Vickery, USA MCR project):** dedicated, reverse-engineered or alternate-source parts are priced against the *avoided design modification*, not against the commercial price. See §4.

## 3. Engineering hours per technical evaluation (recalled / estimate; nothing verified)
| Case | Engineering hours | At $150-225/h loaded | Calendar time today |
|---|---|---|---|
| Re-use existing CGD plan (same item, same application) | 4-16 h | $0.6k-3.6k | 1-4 weeks (queue plus test) |
| New technical evaluation, simple commodity (fastener, gasket, fuse, relay) | 20-60 h | $3k-13.5k | 4-12 weeks |
| New technical evaluation, complex mechanical or electrical (pump part, breaker, power supply) | 60-200 h | $9k-45k | 2-6 months |
| Equivalency evaluation (EPRI 1008256 / TR-107372) plus 50.59 screen for a non-like-for-like replacement | 40-300 h | $6k-68k | 1-6 months |
| Digital device dedication | 300-2,000+ h | $45k-450k | 6-18 months |
- Sources for the rates: utility loaded engineering rate ~$100-150/h, contractor procurement engineers $150-250/h (recalled).
- **Calendar time is mostly queue time**, not touch time. Duke's "backlog" and its "more resources and personnel" quote (EPRI 2024) support this. The AI-native thesis is to compress queue time plus authoring time. Test time (Method 1 lab work, 1-10 days per lot) and shipping are the physics floor.

## 4. Reverse engineering of obsolete parts: costs and the "avoided modification" price anchor (VERIFIED)
Source: B. Vickery, "Utilities Service Alliance's Material Cost Reduction project", *Nuclear News*, June 2020, pp. 40-44. https://wx1.ans.org/pubs/magazines/download/a_1204
- USA = 8 utilities, 9 stations, 14 reactors, >15,000 MWe. MCR project started January 2017. "**Over the past three years, USA documented nearly $30 million in savings for its members**."
- Documented savings per event, each priced against the alternative (OEM digital upgrade, design modification or expediting):
  - **Governor (HPCI/RCIC turbine EGM/EGR):** $7,851,998. Paragon refurbished the units, supplied spares, and reverse engineered the EGM and RGSC. This avoided the OEM digital replacement mod that other sites had already paid for.
  - **Butterfly valves:** $622,000. The OEM was out of business. Curtiss-Wright reverse engineered the seats and parts and ran a qualification test plan at Utah Water Research Lab and NWS Technologies.
  - **Voltage regulator, reverse engineered like-for-like vs digital upgrade:** $898,000.
  - **Five "353 controllers" from an alternative source:** $480,000.
  - **Reverse-engineered power supply (15 units/yr usage):** $329,280.
  - **Transponder circuit boards, OEM lead time "extremely long":** $26,599.
  - **40 Teflon rings plus 55 OEM seat ring discs** ("Because Paragon had previously dedicated these parts"): $81,683. This shows the value of reusing a dedication.
  - **Surplus valve found via shared inventory:** $48,762.
- Paragon case pages (VERIFIED, https://paragones.com/case-studies/commercial-nuclear-case-study/ and https://paragones.com/case-studies/instrumentation-control-case-study/):
  - Woodward governor RE solution "saves utilities **$500,000/site**".
  - Over $9M through the USA MCR via RE opportunities.
  - $1.25M per year from catalogue de-duplication: 25,000 suspect duplicate CATIDs, 8,600 consolidated.
  - Circuit-card repair management saves about $100k per site per year.
  - Sharing inventory saved $200k in 12 months.
  - The RAPID programme sold $4M of one utility's inventory.
- Curtiss-Wright: has reverse engineered more than 1,400 mechanical components (search snippet of the Nova Reverse Engineering brochure, https://cwnuclear.com/sites/default/files/Download-Library/Nova-Reverse-Engineering-Brochure.pdf, not fetched).
- **Typical RE cost (recalled):**
  - $20k-100k for a simple mechanical part (scan, materials and PMI, drawing, first article, dedication).
  - $100k-500k for an electronic module (schematic capture, component obsolescence within the module, EMI/RFI, seismic, possibly EQ).
  - Lead time 3-12 months, versus the $0.6M-8M avoided cost of a design modification or digital upgrade.
- **Pricing implication:** today, RE suppliers capture only a fraction of the avoided-mod value. An AI-native dedicator that cuts RE plus dedication from 6-12 months to weeks can price at 10-30% of avoided modification cost, or $50k-$1M per obsolete family (estimate).

## 5. EQ and seismic qualification costs (recalled; no figure verified)
- The searches found only vendor capability pages with no prices: Framatome EQ brochure, https://www.framatome.com/solutions-portfolio//app/uploads/2025/10/a1182-p-ge-g-en-1182-201901-environmentalqualification-containment-components.pdf; Curtiss-Wright QualTech NP, https://cwnuclear.com/brands/qualtech-np/equipment-qualification; Kinectrics EQ page. The test sequence is thermal and radiation ageing, then seismic, then LOCA/HELB simulation.
- **Recalled ranges:**
  - Seismic shake-table test (IEEE 344, triaxial random multi-frequency) per specimen: **$15k-75k**, plus fixture and report. Seismic qualification by analysis or similarity: $5k-30k.
  - Full 10 CFR 50.49 / IEEE 323 EQ programme (ageing, irradiation, seismic, LOCA): **$250k-1.5M per equipment type**, **9-24 months**. Real-time thermal ageing is the clock.
  - Radiation dose to 200+ Mrad at a gamma facility: $10k-50k.
- **Implication:** EQ items cannot be done "in days" by AI. They are outside the wedge except by similarity or analysis to existing qualified families. Seismic by similarity is in scope. Duke already owns a shake table, which shows utilities pay to bring this in-house for speed.

## 6. Cost of an outage day, forced outage or outage extension
### 6.1 Verified historical data points (from search snippets of the listed sources; I did not fetch the full pages)
- **San Onofre (2012-13):** prolonged outage cost $317M, "more than $1 million per day", plus $221M of replacement power. https://www.plantengineering.com/costs-mount-for-ca-nuke-outage/
- **Industry rule (2006 report):** replacement power for extended or unplanned outages is "over one million dollars a day". The **average extension lasted about 5 days**. https://www.plantengineering.com/?p=16300
- **Point Beach 2 (2005 8-K):** replacement power $400-500k/day through peak summer, up to $1M/day on high-demand days. https://www.sec.gov/Archives/edgar/data/783325/000010781505000117/wecwe8k0527.htm
- **Wolf Creek (2008):** about $265k/day for KCP&L's 47% share, including replacement power, so about $560k/day for the whole unit (estimate). https://www.power-eng.com/nuclear/great-plains-energy-announces-wolf-creeks-outage-extended/
- **1990s refuelling outages:** about $300k/day excluding replacement power, about $600k/day including it. https://www.power-eng.com/?p=53077
- **Point Lepreau (NB Power, 2024-25):** $1-1.5M/day combined replacement power plus repair. An earlier outage was extended by 150 days on a 98-day plan because of the main generator. https://amp.cbc.ca/news/canada/new-brunswick/nb-power-point-lepreau-nuclear-power-1.7259468
- **Parts-driven case (VERIFIED):** AECL paper (Mizuno, Tume, Prentice, "Strategic Provisioning of Replacement Parts for CANDU Power Plants", CNS, c. 2000) says: "an **obsolete analog control board** for the feeder-pump control system could not be replaced in time and lead to a **4 day shutdown** at a loss of approximately [$]1 million dollars per day." The OCR of the PDF reads "11 million"; the search snippet and the context support $1M/day. https://proceedings.cns-snc.ca/index.php/pcns/article/download/3626/3625/3661

### 6.2 2026 economics (estimate built on verified and recalled prices)
- **PJM capacity:** the 2026/27 BRA cleared at the cap of **$329.17/MW-day UCAP** RTO-wide ($256.75/MW-day ICAP equivalent). Nuclear was 21% of cleared resources. Forecast peak load rose by more than 5,400 MW year on year, driven by data centres. VERIFIED: https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2026-2027/2026-2027-bra-report.pdf and https://insidelines.pjm.com/pjm-auction-procures-134311-mw-of-generation-resources-supply-responds-to-price-signal/. The 2027/28 BRA (Dec 2025) cleared at about the cap again, ~$333/MW-day (recalled; see NRG deck https://www.nrg.com/assets/documents/insights/white-papers-and-webinars/webinars/pjm-bra-results-dec-2025.pdf, not fetched).
- **Energy:**
  - PJM West around-the-clock 2025-26 averages ~$45-65/MWh, with peak summer and winter days at $100-300+/MWh (recalled).
  - Nuclear PPAs with hyperscalers are ~$80-115/MWh (recalled): Constellation-Microsoft Crane 20-yr analyst estimates ~$100-115/MWh; Talen-Amazon Susquehanna 1,920 MW through 2042, ~$18B total value; Constellation-Meta Clinton 20-yr from 2027 (recalled).
- **Per-day loss, 1,100 MWe unit (26,400 MWh/day):**
  - Lost energy margin at $50-65/MWh market minus ~$10/MWh avoided variable cost: **$1.05-1.45M/day**.
  - If a PPA requires firm delivery, the owner buys replacement power at market, possibly with shaping and penalties. Loss is about market price × MWh: **$1.3-1.7M/day** normally, and **$2.5-8M/day** on scarcity days at $100-300/MWh.
  - Outage extension (refuelling outage critical path): add standing outage-crew cost. 1,000-2,000 supplemental workers plus tooling and vendor standby is ~$0.5-1.0M/day (recalled/estimate). **Total ~$1.6-2.5M per unit-day.**
  - Capacity: the $362k/day of capacity revenue (1,100 MW × $329.17) is not forfeited simply by being offline. But (a) a forced outage during a Performance Assessment Interval exposes the unit to PJM Capacity Performance non-performance charges (thousands of $/MWh; recalled), and (b) forced outages raise EFORd and so cut future cleared UCAP. Each 1 percentage point of EFORd on 1,100 MW at $329/MW-day is ~$1.3M/yr (estimate).
- **Rule for the model: $1.5M per unit-day base, $2.5M critical-path refuelling extension, $5M+ scarcity-day forced outage.**

## 7. How often a missing or late dedicated part extends an outage or causes a derate
- **No verified quantitative source** (EPRI, INPO or LER) was found. INPO data is not public. The LER database (lersearch.inl.gov) needs interactive querying; searching narratives for "obsolete", "commercial grade", "dedicat" and "spare not available" is a follow-up task.
- **Qualitative, verified:**
  - AECL: parts "will either become **critical path items during a plant outage** or may lead to an **unplanned shutdown**."
  - A 2004 utility-industry obsolescence presentation (search snippet of https://digital.library.unt.edu/ark:/67531/metadc780247/m2/1/high_res_d/840372.pdf; the fetch failed with HTTP 503) says utility surveys put about 25% of replacement-candidate components as obsolete, with a direct cost of over $1M per US plant per year.
  - Rolls-Royce: 20-25% of plant components are no longer OEM-supported, and a plant relies on more than 100,000 parts. https://www.reutersevents.com/nuclear/node/54822 (2015).
  - EPRI 2024 (Duke): lead time is the primary driver of CGD.
- **Fleet frequency estimate:**
  - US fleet: 94 units, capacity factor ~92-93%, forced loss rate ~1.5-2.5% (recalled). That is **~500-850 forced-outage-equivalent unit-days a year**.
  - Refuelling outages: ~45-50 a year (18/24-month cycles), median ~30-35 days (recalled). Average overrun is ~2-5 days on outages that overrun; assume half overrun. That is **~50-120 unit-days of extension a year**.
  - Share where part availability (including dedication or qualification lead time) is on critical path: no data, so assume **5-15% of forced-outage days** (repair waits on a part; restoration-time-driven) and **15-30% of refuelling extensions** (emergent discovery work waits on a qualified part).
  - Result: **~35-160 part-driven critical-path unit-days a year fleetwide.** Midpoint ~80 unit-days, or ~1.5 per site per year.
  - Add derates and LCO-driven shutdowns. A Technical Specification LCO with a 72-hour or 7-day completion time forces a shutdown if a safety-related spare is not available. Also add work-arounds: temporary mods, operator compensatory actions, 50.59 evaluations.
- At $1.5-2.5M/day, the part-driven critical-path value pool is **~$50-400M/yr fleetwide, midpoint ~$150M/yr** (estimate).

## 8. Inventory: safety-related inventory per site and carrying cost
- **VERIFIED (USA, 2020):** "USA nuclear plants have a combined total inventory value of **$860 million**. ... approximately **20 percent is over the maximum stocking quantity**." 9 stations / 14 reactors gives **~$96M per station** and ~$61M per reactor. (Vickery 2020, ANS link above.)
- **VERIFIED (Constellation 10-K, SEC XBRL):**
  - `InventoryRawMaterialsAndSuppliesNetOfReserves` = $1.216B (12/2023), $1.357B (12/2024), **$1.485B (12/2025)**.
  - `InventoryNet` = $1.736B (12/2025).
  - Source: https://data.sec.gov/api/xbrl/companyfacts/CIK0001868275.json. Constellation operates ~21-22 nuclear stations plus some gas and hydro, so **~$55-70M of M&S per nuclear station** (estimate). M&S rising ~10%/yr, which is consistent with lead-time-driven stocking.
- **FERC Form 1 account 154 (Plant materials and operating supplies):** not pulled. Regulated utilities (Duke, Dominion, Southern, TVA via its own filings) report it there. Follow-up.
- **Fleet M&S estimate:** 54 sites × $60-100M = **$3.2-5.4B**. The safety-related share is perhaps 30-50% (recalled), so $1-2.7B.
- **Carrying cost:** 15-25%/yr (cost of capital 7-9%, warehousing and handling 2-4%, shelf-life and obsolescence write-offs 3-8%, periodic re-inspection and maintenance of stored items 1-3%) (recalled, standard). That gives **$0.5-1.35B/yr fleetwide**.
- **Value of on-demand dedication to inventory (estimate):**
  - If a days-not-months dedication capability lets plants cut min/max on long-tail safety-related items by 10-20%, it frees $100-500M of working capital fleetwide (one-time).
  - It also cuts $20-125M/yr of carrying cost, or **~$0.4-2.3M/yr per site**.

## 9. Value-per-event model: what a utility would rationally pay
Notation: C_day = cost per critical-path unit-day; T_old and T_new = dedication or qualification time today and with the AI dedicator; p_cp = probability the item is on the critical path for its full delay; f = share of total delay attributable to dedication (versus manufacturing and shipping).

### 9.1 Emergent (forced outage, refuelling discovery work, LCO clock)
Value per event = C_day × p_cp × min(outage remaining, f × (T_old − T_new)) + avoided expedite/work-around costs.

| Case | C_day | Days saved on critical path | p_cp | Value/event | Rational WTP (10-30% capture) |
|---|---|---|---|---|---|
| Refuelling-outage emergent part, commercial equivalent in stock at distributor; today vendor dedicates in 2-3 wk with expediting, new = 3 days | $2.0M | 3-10 | 0.5 | **$3-10M** | $0.3-3M |
| Forced outage, obsolete board/part; today RE or temporary mod in 2-6 wk, new = 1 wk | $1.5M | 7-30 | 0.6 | **$6-27M** | $0.6-8M |
| LCO 72h/7-day clock, no SR spare; today forced shutdown or NOED request, new = dedicate commercial unit in 48-72h | $1.5M (plus avoided shutdown/startup transient ~$0.5-1M) | 2-7 | 0.3-0.5 | **$1-6M** | $0.1-1.5M |
| Derate (e.g. one feed pump/train out) | 30-50% × $1.5M | 7-30 | 0.7 | $2-15M | $0.2-4M |
- **Anchor check:** utilities already pay 2-5x expedite premiums (recalled). The AECL obsolete-board case (4 days × ~$1M) and the 2006 "average extension ~5 days × >$1M" both give **~$4-5M per event**. A per-event emergent fee of **$100k-500k** is well under 10% of the value and clears any procurement approval threshold.
- **Expected value per site per year (estimate):** ~1.5 part-driven critical-path unit-days × $1.5-2.5M × the share recoverable by faster dedication (40-60%, since manufacturing and shipping remain) ≈ **$1-2.2M/site/yr**. A **standby retainer of $250k-750k per site per year** for a guaranteed 72-hour emergent dedication SLA is rational, like insurance at 25-35% of expected loss avoided. The tail case is a multi-week forced outage worth $20M+.

### 9.2 Planned procurement (the bulk of volume)
Value per package = engineering hours saved × rate + carrying cost of inventory no longer needed (lead-time-driven safety stock) + avoided premium versus OEM/N-stamp price + avoided design modification (obsolescence cases).
| Case | Today cost | AI-dedicator target | Saving | WTP |
|---|---|---|---|---|
| Re-use plan, commodity lot | $1-5k, 2-6 wk | $0.5-2k, 3-5 days | $0.5-3k | price at parity or 10-30% below incumbents; win on lead time |
| New technical evaluation, commodity | $5-20k, 1-3 mo | $2-6k, 1 wk | $3-14k | $3-10k/package |
| New technical evaluation plus equivalency, complex | $20-70k, 2-6 mo | $8-25k, 2-3 wk | $12-45k plus carrying | $10-35k/package |
| Obsolete part, reverse engineering plus dedication instead of a design mod | $0.3-8M avoided mod (USA examples) | 4-10 wk | 10-30% of avoided mod | $50k-1M per part family |
- **Fleet-level planned pool (estimate):**
  - 8-20k jobs/yr × $3-15k average fee = **$25-300M/yr** of dedication fees (labour plus test plus QA), consistent with d03's $50-300M.
  - The RE/obsolescence pool: USA (14 of 94 reactors) documented ~$10M/yr of savings in 2017-19, so the fleet has ~$60-100M/yr of avoided-mod value addressable by RE (estimate, scaled).

### 9.3 Summary of annual value pools, US fleet (estimate)
| Pool | Fleet value/yr | Capturable revenue/yr |
|---|---|---|
| Emergent critical-path days avoided | $50-400M (mid ~$150M) | $15-80M (retainers plus per-event fees) |
| Planned dedication fees (labour, test, QA) | $25-300M | $25-150M at share |
| Obsolescence / RE vs design mods | $60-100M | $10-30M |
| Inventory carrying reduction | $20-125M | $5-25M (gain-share) |
| **Total** | **~$0.15-0.9B** | **~$55-285M** |
- Plus the margin on the dedicated part itself: dedicators typically resell parts at 20-50% markup over cost plus dedication (recalled).
- Not included: new builds and restarts (Palisades, Crane, Duane Arnold), SMR supply chains, and Canada, Korea and Europe (EPRI: Spain >50% of SR procurement via CGD).

## 10. Pricing recommendations (opinion)
1. **Planned dedication: price at parity with incumbents per package and sell on lead time.** EPRI says cost is the least influential factor; quality and lead time decide. Do not lead with a discount.
2. **Emergent dedication: an SLA tier.** 72-hour (or 5-day) guaranteed turnaround for $100k-500k per event, or a $250k-750k per site per year retainer that includes N emergent events. Anchor to $1.5-2.5M per unit-day, citing San Onofre, the 2006 industry rule and the AECL case.
3. **Obsolescence/RE: gain-share** of 10-30% of the documented avoided-modification cost. This mirrors the USA MCR "documented savings" accounting utilities already use.
4. **Inventory gain-share:** share the carrying cost saved when min/max drops because on-demand dedication is guaranteed.
5. **Watch-outs:**
   - Part 21 liability as the dedicating entity.
   - The NUPIC audit cycle before any utility can buy.
   - Test-lab throughput (Method 1) is the physics floor. "Days" needs an in-house robotic or accredited-lab network: Duke built the CRDF for this reason.
   - Paragon (being acquired by Mirion, ~$585M per sibling notes, recalled) and Curtiss-Wright already do 1,300+ jobs a year each and are the price setters.

## 11. Open data gaps and next steps
- Per-item dedication quotes. Ask 3-5 procurement engineers for recent purchase orders: commercial price vs dedicated price, and lead time.
- LER narrative search for "obsolete"/"spare"/"commercial grade" to count part-driven shutdowns and extensions in 2015-2025.
- FERC Form 1 account 154 for Duke, Dominion, Southern and Ameren nuclear sites.
- EPRI reports on CGD cost or effort benchmarks (the JUTG procurement engineering metrics) and INPO AP-913 equipment reliability data. Both are member-only.
- Data-centre PPA prices from 10-K/8-K disclosures (Talen, Constellation, Vistra-Comanche Peak).

## Sources (URLs)
- EPRI 3002029261 (2024): https://restservice.epri.com/publicdownload/000000003002029261/0/Product
- Vickery, Nuclear News June 2020 (USA MCR): https://wx1.ans.org/pubs/magazines/download/a_1204
- Paragon case studies: https://paragones.com/case-studies/commercial-nuclear-case-study/ ; https://paragones.com/case-studies/instrumentation-control-case-study/
- AECL CANDU provisioning paper (CNS): https://proceedings.cns-snc.ca/index.php/pcns/article/download/3626/3625/3661
- Reuters Events 2015 (obsolescence): https://www.reutersevents.com/nuclear/node/54822
- OSTI 94221 (APC 1995): https://www.osti.gov/biblio/94221
- PJM 2026/27 BRA: https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2026-2027/2026-2027-bra-report.pdf ; https://insidelines.pjm.com/pjm-auction-procures-134311-mw-of-generation-resources-supply-responds-to-price-signal/
- Outage-cost cases: https://www.plantengineering.com/costs-mount-for-ca-nuke-outage/ ; https://www.plantengineering.com/?p=16300 ; https://www.sec.gov/Archives/edgar/data/783325/000010781505000117/wecwe8k0527.htm ; https://www.power-eng.com/nuclear/great-plains-energy-announces-wolf-creeks-outage-extended/ ; https://www.power-eng.com/?p=53077 ; https://amp.cbc.ca/news/canada/new-brunswick/nb-power-point-lepreau-nuclear-power-1.7259468
- Constellation XBRL: https://data.sec.gov/api/xbrl/companyfacts/CIK0001868275.json
- EQ vendor pages (no prices): https://cwnuclear.com/brands/qualtech-np/equipment-qualification ; https://www.framatome.com/solutions-portfolio//app/uploads/2025/10/a1182-p-ge-g-en-1182-201901-environmentalqualification-containment-components.pdf
