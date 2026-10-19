# Lane H: operational and logistics waste around exploratory drill programs

Written 19 Oct 2026. Scope: coordination, logistics and business-model waste (not rig physics).
Caveat: the shared web-search budget ran out partway through this lane. Some planned checks did not run:
SRC lab service standards, Durin's later funding, DrillDocs/Rigminder/DrillLogix, the Bentley-Seequent price,
Major Drilling's downturn utilisation, and shared-camp examples in the Yukon. Those points are marked
(memory) or (gap). Every other number has a URL.

## 10-line summary
1. **Where the money goes.** CanAlaska's own MD&A (Athabasca) splits spend by category. The drill contractor
   line is 47-57% of exploration spend. Camp and operations is 11-13%. Geology, geochem and G&A together are
   about 17-20%. Coordination waste is spread thinly across all of these lines, not held in one of them.
2. **All-in cost.** Athabasca all-in cost per metre runs about CAD 525-1,650. Lows come from 43-101 budgets
   and press releases (CAD 525 per metre all-in; CAD 1.5M for 2,600 m). The high end is a 1,250 m budget
   of CAD 2.06M. The drilling contractor's own metre rate is only part of that.
3. **Labour is the binding constraint, not rigs.** Major Drilling (FY2026, to 30 Apr 2026) reported record
   revenue of CAD 889M and a 688-rig fleet. It says "labour is expected to remain our most significant
   challenge", calls the "pool of available experienced drillers drying up", and says it is adding trainees,
   which lowers productivity. A marketplace cannot create drillers.
4. **Pricing power is cyclical and contractual.** Contracts carry 6-month rate locks with quarterly reviews,
   cost-plus-15% consumables, and hourly standby. In upcycles prices "incrementally" rise. Contractor
   adjusted gross margin is only about 22%. There is no fat contractor margin to arbitrage away.
5. **Standby and idle time is real, but it is billed hourly and small per event.** In two filed contracts,
   standby is USD 110-175/hr, set against roughly USD 81-109/m drilling rates. Estimate: idle time is
   5-15% of contractor billings (estimate). Most of it comes from weather, ground conditions and waiting on
   the client's decisions.
6. **Assay lag exists but matters less for uranium.** Downhole gamma probes give eU3O8 in real time.
   CanAlaska's full geochem arrived about 2-6 months after programs ended (summer 2024: Sept to Mar 2025).
   Follow-up decisions in uranium mostly ride on probe and scintillometer data, not assays.
7. **Software layer is owned.** CorePlan (Perth) has more than 600 companies, more than 9,000 users,
   AU$6.1B of drilling works managed, and AU$9M raised from EVP. Seequent (Bentley) owns MX Deposit and Imago.
   Hexagon has CORE. Plods, invoicing and contractor management are a crowded tool market.
8. **No working "Uber for rigs" found.** The structural reasons: rigs are tied to crews, safety
   prequalification is required, demand is synchronised (everyone drills the Athabasca winter season
   together), and fly-in mob is per-camp rather than per-rig. The nearest venture bet is Durin. It is
   vertically integrated, building its own automated rigs (USD 3.4M seed, a16z/Lux, 2025), not a marketplace.
9. **Size of the waste.** Estimate: addressable coordination waste is about 5-12% of program cost. In
   Saskatchewan that is tens of CAD millions a year, and globally low hundreds of USD millions to about
   USD 1B. A company capturing even a large slice is a USD 30-150M/yr services or tool business. That
   fails rubric item 6.
10. **Verdict.** A standalone ops and logistics company fails the rubric. The only rubric-shaped version is
    a vertically integrated drill-for-equity operator. It uses its own crews and camps across many claims to
    capture land step-ups, so it only works once paired with targeting (Terranox-like). Durin is closest.

---

## 1. Cost structure of an Athabasca program (real splits)

**CanAlaska Uranium, nine months to 31 Jan 2026 (CAD 000s, gross exploration spend)**
Source: https://canalaska.com/wp-content/uploads/2026/03/2601-CVV-MDA-FS-FINAL.pdf (Table 4)

| Category | CAD 000 | Share |
|---|---|---|
| Drilling | 5,125 | 57% |
| Camp cost and operations | 1,018 | 11% |
| Geophysics | 779 | 9% |
| General and admin | 734 | 8% |
| Geology (staff and contract geologists) | 610 | 7% |
| Other | 425 | 5% |
| Geochemistry (assays) | 311 | 3.5% |
| **Gross** | **9,002** | |

**CanAlaska, fiscal year to 30 Apr 2024**
Source: https://www.canalaska.com/wp-content/uploads/2024/07/2404-MDA-and-FS-FINAL.pdf

| Category | CAD 000 | Share |
|---|---|---|
| Drilling | 4,931 | 47% |
| Geophysics | 2,201 | 21% |
| Camp and operations | 1,333 | 13% |
| G&A | 894 | 8.5% |
| Geology | 551 | 5% |
| Other | 337 | 3% |
| Geochemistry | 245 | 2.3% |
| **Gross** | **10,492** | |

Readings:
- The drilling line likely already includes the contractor's mob/demob, standby and consumables, since
  contractors bill these. Helicopter support probably sits in drilling or in camp and operations; the MD&A
  does not say which (inference).
- Assays are a tiny line (2-4%). Lab cost is not the problem; lab time might be (section 6).
- Camp plus G&A plus geology is about 25-30% of spend. Coordination overhead lives here: camp
  logistics, expediting, geologist days on site and admin.

**All-in cost per metre benchmarks (CAD)**
- Forum Energy Metals, Northwest Athabasca 43-101 (27 Jun 2024), proposed budget: "All in Drilling Costs
  $525 per metre, all in", 4,000 m for CAD 2.1M. A further 10% admin and 10% contingency sit on top. Source:
  https://sedar-filings-primary.thecse.com/00030569/2410081100293728.pdf (Table 5, p.55)
- UraEx South Dufferin (Skyharbour partner), summer 2025, camp plus helicopter: about CAD 1.5M for 2,600 m,
  which is about CAD 575/m (arithmetic). Source:
  https://skyharbourltd.com/news-media/news/skyharbours-partner-company-uraex-resources-commences-summer-2025-drilling-program-at-south-dufferin-uranium-project-athabasca-basin-saskatchewan
- Refined Energy, Dufferin West 43-101 recommendation (Jun 2025): 1,250 m for CAD 2,062,500, which is about
  CAD 1,650/m (arithmetic; probably includes fixed mob and camp over a short program). Source:
  https://www.globenewswire.com/news-release/2025/06/30/3107423/0/en/Refined-Energy-Corp-Files-43-101-Report-Drill-Program-Recommended.html
- National average from NRCan survey data, as reported by a third party: about CAD 284/m in 2024, up from
  CAD 173/m in 2017. This covers all of Canada and all commodities, and the third-party source returned 403
  when fetched, so treat it as indicative. In Saskatchewan, juniors are 70.6% of spend, mostly uranium.
  https://farmonaut.com/mining/mineral-exploration-spending-canada-nrcan-data

**Key point.** Short programs pay the highest per-metre cost: CAD 1,650/m for 1,250 m against CAD 525-575/m
for 2,600-4,000 m. Fixed costs (mob, camp set-up, heli positioning, permits) are amortised over few metres.
That fixed-cost overhead is the clearest coordination-waste target. Pooling programs would spread it.

---

## 2. Contract structure: what is billed, and how idle time is priced

Two filed contracts (SEC exhibits) give the anatomy. Both are older and outside Canada, so read them for
structure, not for current rate levels.

**Major Drilling and Kimber Resources, contract dated 9 Jan 2011 (Mexico, USD)**
Source: https://www.sec.gov/Archives/edgar/data/1294662/000117625611000743/exhibit2-32.htm
- Mob and demob: USD 4,000 lump sum each, per drill (road-access site).
- Core rates: USD 81/m (0-250 m), 86/m (250-500 m), 91/m (500-750 m).
- Volume penalty: if the 30,000 m minimum is missed, rates rise to 97-109/m below 10,000 m. Small
  programs pay about 20% more per metre by contract.
- Standby with crew: USD 110/hr (core) or 175/hr (RC). The same rate applies to moves, casing, reaming,
  re-entry and fishing.
- Consumables: muds, additives, core boxes and sample bags billed at cost plus 15%. Diamond bits above
  USD 9/m billed to the client. The contractor pays its own fuel.
- Rates fixed for 6 months, then reviewed every 3 months for labour, fuel and rod costs. If no agreement is
  reached, the contractor can walk on 30 days' notice. This is the clause through which upcycle pricing
  power is exercised.

**2004 drilling contract (Mongolia, USD)**
Source: https://www.sec.gov/Archives/edgar/data/1271554/000108503704001083/f10sbex1013.htm
- Mob and demob: USD 6,200 each. Coring 92.5-102.5/m.
- "Waiting time caused by Company decisions on holes": USD 120/hr. This is the explicit, billable price of
  the client's geologist not deciding. Client failure to supply agreed goods or services is reimbursed at
  field-cost rates, up to 10 hr per shift.

**Implications**
- Idle time is not hidden waste. It is invoiced hourly at roughly one metre-rate-equivalent per hour.
  A rig drilling about 30-60 m per 12-hr shift at about USD 90/m earns about USD 225-450/hr. Standby at
  USD 110-120/hr therefore recovers roughly 25-50% of productive revenue. The client pays for its idle
  time, but at a discount. Contractors absorb the rest and price it into metre rates (estimate).
- Common idle causes: weather or ice, waiting on the client's hole decisions, survey tools, moves,
  ground problems (fishing, reaming, casing), and helicopter availability on heli-supported rigs. From
  memory, field operators often quote 10-25% non-productive time on remote diamond programs (memory, no
  source found). Of that, the "waiting on client" share is the software-addressable part. Estimate: a third
  or less of non-productive time.
- In the Athabasca, mob is not USD 4-6k. Fly-in, winter-road or barge mobilisation of rigs, fuel and camp
  more likely runs into the tens to low hundreds of thousands of CAD per program (estimate; no primary
  number found). This drives the high per-metre cost of short programs.

---

## 3. Rig utilisation, labour, contractor margins and pricing power

**Major Drilling, Q4 and FY2026 (year to 30 Apr 2026, CAD)**
Source: https://www.majordrilling.com/major-drilling-announces-fourth-quarter-results-and-record-annual-revenue/
- Record revenue of 889.1M, up 22%. Canada-US revenue of 337.0M, up 23%. Q4 Canada-US revenue was up 66.5%.
- Fleet of 688 rigs (one added, 10 retired).
- Adjusted gross margin of 22.0% in Q4 (22.8% a year earlier). Gross margin for the year was 15.6% (17.9% a
  year earlier). Q4 net earnings were only CAD 8.2M on CAD 233.7M of revenue.
- Pricing: "rigs to continue to be gradually deployed into the field at incrementally higher prices";
  "the industry is nearing capacity in terms of labour, pricing should continue to improve".
- Labour: "labour is expected to remain our most significant challenge"; "pool of available experienced
  drillers drying up, we have increased the number of trainee drillers, which has and will continue to
  temporarily affect productivity". The shortage is worst in Canada, the US, Australia and Chile.
- Its Q2 FY2026 release (Dec 2025) noted Canadian activity was up sharply "despite ongoing pricing
  pressure", per a search summary (the page was not fetched). A third-party earnings page showed fleet
  utilisation of about 52% across about 697 drills, date unclear (gap). Even in a boom, about half of the
  largest fleet sits idle. The limit is crews, not iron.

**Interpretation for "rig availability gated uranium juniors 2023-26"**
- No primary source found that states rig shortages in the Athabasca. Junior releases frame it as
  "securing a reliable drill contractor". Examples: Aero Energy with Team Drilling, 3 Apr 2024
  (https://www.newsfilecorp.com/release/203976); Infini "locks in key contractors" (Rodren Drilling),
  19 Mar 2026
  (https://www.albanyadvertiser.com.au/business/bulls-n-bears/infini-locks-in-key-contractors-for-canadian-uranium-push-c-21994670).
  The scarce item is a crewed rig in the winter window. Major Drilling's own statement is that labour is
  the cap.
- Contractor margins are thin (about 22% adjusted gross, which does not cover depreciation, and low
  net). A disintermediating platform has little contractor margin to take. Upcycle pricing power is real
  but moderate: rate reviews every 3 months, plus the walk-away clause.

**Wages (CAD).** Job Bank (Nov 2025) puts the diamond driller helper national median at CAD 25/hr (range
18.25-40). Diamond drill operator medians are about CAD 33-35.55/hr. Sources:
https://www.jobbank.gc.ca/marketreport/wages-occupation/24610/AB ,
https://bc.jobbank.gc.ca/marketreport/wages-occupation/10437/ON . A Foraco fly-in heli posting offered
drillers CAD 36-40/hr and helpers CAD 27-30/hr, plus overtime and travel (search summary; dated). A crew of
3-4 per shift on 2 shifts is about 6-8 people per rig. Labour is a large share of the contractor's cost
(estimate).

---

## 4. Mobilisation, camps and shared logistics

- Athabasca access is by float or ski plane, helicopter, barge or winter road. The NW Athabasca project is
  reached from Uranium City (75 km), Stony Rapids (230 km) or Fort McMurray (300 km). Source: Forum 43-101
  (above), section 5.
- Programs commonly run "from a local contracting camp with helicopter support". Example: Terra Clean
  Energy, South Falcon East, budget CAD 2.0M.
  https://www.thenewswire.com/press-releases/1AXXF1qDO-terra-clean-energy-corp-drills-18-meters-of-0-03-u3o8-at-the-south-falcon-east-uranium-project.html
  The South Dufferin program used the same model. Third-party camps already exist (lodges and contractor
  camps rented per man-day), so camp sharing is partly happening through incumbents.
- Timing is a lever. Standard Uranium (Oct 2025) moved its 2026 Davidson River program (8,000-10,000 m, two
  diamond drills, starting May 2026) to favourable weather, saying the timeline adjustment "will decrease
  cost per metre" (search summary of
  https://www.barchart.com/story/news/35212974/standard-uranium-announces-expansion-of-davidson-river-drill-program-and-provides-update-on-private-placement-and-life-offering ;
  page body did not load). This shows weather and season planning visibly moving unit cost.
- Shared mobilisation across juniors: no documented Athabasca or Yukon example of pooled mobs, shared
  winter-road convoys or a "drill program as a service" was found before search ran out (gap). Informal
  sharing exists through the incumbents (memory):
  - Contractors chain rigs from one client's claim to the next nearby one.
  - Prospect generators run programs for many optionees (Skyharbour runs partner programs; CanAlaska
    operates JV programs for partners).
  - Lodge and camp operators sell man-days to several companies.
  The prospect-generator model is the de facto "drilling as a service" for juniors, and its economics come
  from land, not logistics.
- Permits: Saskatchewan programs need a Surface Exploration Permit, a Forest Product Permit, an Aquatic
  Habitat Protection Permit and Term Water Rights. Permits "may take up to three months". Fees are under
  CAD 200 per program plus camp fees of CAD 175-750/ha. Source: Forum 43-101, section 4.3. Permitting is a
  scheduling cost (lead time), not a cash cost.

**Why pooling is hard (analysis).**
- Demand is synchronised: everyone wants the same winter or summer window.
- Claims are scattered across the 100,000 km2 basin, so "adjacent" programs are often tens of km apart.
- Juniors guard target locations before results (disclosure and competitive secrecy).
- Contractors already capture the easy back-to-back savings.

---

## 5. Consumables and safety/regulatory overhead

- Consumables are passed through. In the Kimber contract, muds, additives and core boxes are billed at cost
  plus 15%, bits above USD 9/m go to the client, and the contractor pays fuel (source above). Major Drilling
  cites "higher labour, ramp-up, and consumable costs" as margin pressures (FY2026 release). No primary
  split of consumables share was found. Estimate: bits, rods, mud and fuel are 10-20% of contractor cost
  (estimate).
- Safety: Major Drilling reports a TRIFR of 0.85 (FY2026). Safety stoppages ordered by the client are free
  to the client under the Kimber contract. Regulatory cost is mostly permit lead time, and in uranium the
  radioactive sample handling and transport rules (memory). Software can do little here beyond compliance
  record-keeping, which CorePlan already sells.

---

## 6. Core logging and assay turnaround

**Evidence of lag (CanAlaska West McArthur, from its Jan 2026 MD&A, URL above)**

| Program | Program end | Full geochem assays |
|---|---|---|
| Summer 2024 | Sept 2024 (partial confirmation in Oct 2024) | Received in full Mar 2025, about 6 months |
| Winter 2025 | Apr 2025 | Jul 2025, about 3 months |
| Summer 2025 | Nov 2025 | Jan 2026, about 2 months |

- Other cases:
  - IsoEnergy and Purepoint (Dorado, Sep 2025): "Full assays from all holes remain pending" after
    partial results.
    https://www.barchart.com/story/news/34885529/isoenergy-and-purepoint-intersect-up-to-8-1-u3o8-at-dorado-project
  - Bedford Metals sent 218 core samples to SRC in 2026 and data was still pending (German-language stock
    sites, low quality).
    https://www.boerse-express.com/news/articles/bedford-metals-aktie-src-prueft-218-kernproben-913903
  - Infini (Oct 2025): rush samples above 5,000 cps were "delayed due to the high levels of radioactivity".
    This is a search snippet; the ASX PDF returned 404 when fetched.
  - Infini also cited "slower laboratory processing times across North America" (May 2026).
    https://www.mining-technology.com/news/infini-resources-begins-drilling-saskatchewan-uranium-sites/
- Booms bring backlogs, and this is not new. Northern Miner (21 Jan 2008): "Lengthy lab turnaround times
  have driven UEX to reprioritize its Athabasca uranium deposits."
  https://www.northernminer.com/company/030457875/page/3/
- SRC Geoanalytical (Saskatoon) is the de facto uranium lab of record. It moved into a purpose-built
  facility in 2021 "to improve sample flow and reduce the turnaround time" (https://www.src.sk.ca/node/1652).
  No published service-standard turnaround was found (gap). Few labs are licensed for high-grade
  radioactive core, which makes SRC a near-monopoly bottleneck in booms (memory).

**Why it matters less than it looks.** Uranium explorers steer drilling in real time with downhole gamma
probe eU3O8 and handheld scintillometers (SPP2, CT007-M). CanAlaska reports probe eU3O8 first and assays
later as confirmation, and picks assay samples from probe peaks (MD&A, Geochemical Assay Sampling
Procedures). Follow-up hole decisions therefore rarely wait on SRC. What waits are:
- disclosure and financing: juniors raise on assays, and 2-6 months of lag delays the next raise;
- pathfinder and clay geochemistry for non-mineralised holes. This is where "near-miss" vectoring
  information lives, and its lag does slow the next season's targeting (inference).

A faster or second radioactive-capable lab, or on-site hyperspectral and XRF, is a real opportunity.
It is lab-service or instrument shaped, not coordination software (see other lanes for core-scanning
physics).

---

## 7. Platforms and software already in the space (adversarial check)

| Player | What | Traction or funding | Read |
|---|---|---|---|
| CorePlan (Perth) | Digital plods, contractor and drill program management, invoice checking | First raise of AU$4M in Mar 2024 (77 customers incl. BHP Nickel West, FMG, AngloGold, DDH1). AU$5M follow-on from EVP on 3 Feb 2026: more than 600 companies, more than 9,000 users, AU$6.1B of works managed, revenue reportedly doubled in 2025. Sources: https://www.coreplan.io/newsroom/coreplan-raises-4-million-for-global-expansion , https://www.coreplan.io/newsroom/coreplan-secures-5m-in-follow-on-funding-from-evp-to-scale-drilling-program-operations | Owns "Plods/ops software". Only about AU$9M raised after years of operation, which signals a modest TAM. |
| Hexagon CORE | Digital drill plans and plods synced to mine planning | Inside Hexagon. https://hexagon.com/products/hexagon-azimuth-aligner | Incumbent |
| Seequent (Bentley) MX Deposit plus Imago | Drillhole and core data management, core imagery | Imago acquired Aug 2021 (price undisclosed). https://www.seequent.com/bentley-systems-announces-seequents-acquisition-of-imago/ . Bentley paid about USD 1.05B for Seequent in 2021 (memory). | Owns logging and data. The largest exit in the space is a geology-software company, not an ops one. |
| Durin (El Segundo) | Automated and remote-operated rigs, vertically integrated | Founded 2024. USD 3.4M seed in Apr 2025 at a USD 14M valuation (Lux, a16z, 8090, 1517, Bedrock). https://dealroom.co/companies/durin/ | Closest venture bet. Attacks labour (the real constraint) by owning rigs. Too early to judge. |
| "Uber for rigs" or drilling marketplace | Rig booking | None found. Search turned up only used-equipment sale listings. | Not owned, probably for structural reasons (section 4). |
| DrillDocs, Rigminder, DrillLogix | (unverified) | Not checked (search budget) (gap). DrillDocs is, from memory, an oil-and-gas drilling-data startup, not minerals (memory). | — |
| Coreshed | Core imaging and logging (memory) | Not verified (gap) | Likely subsumed by Imago, GeologicAI and similar |

Also relevant, from memory: GeologicAI, Minalyze, Corescan and others do core-scanning hardware
(another lane). Boart Longyear, Foraco and Major Drilling are the physical incumbents. Prospect generators
(Skyharbour, CanAlaska and peers) already run multi-partner programs.

---

## 8. Sizing the coordination waste (estimates)

All figures are estimates built on the splits above.

| Waste bucket | Share of program cost (estimate) | Addressable by software or coordination? |
|---|---|---|
| Client-caused standby (decisions, geologist, core handling, surveys) | 1-3% | Yes: real-time plods and remote QP sign-off. Partly owned by CorePlan. |
| Weather or ice standby and season mis-timing | 1-4% | Partly: scheduling. Standard Uranium's own timing shift shows the lever. |
| Fixed mob, camp and heli overhead on short programs (under 2,000 m) | 3-10% for small juniors (CAD 1,650/m against 525-575/m) | Yes, by pooling or batching. Blocked by secrecy and synchronised windows. |
| Small-program rate premium (contract volume tiers about 20%) | 2-5% | Yes, by aggregating demand across juniors (a buying group). |
| Invoice errors and over-billing | 1-2% (memory: industry anecdote) | Yes. CorePlan's core pitch. |
| Assay lag (time cost, not cash) | n/a cash. Delays financing and next-season targeting by 2-6 months. | Lab capacity or instruments, not software |

- **Total addressable:** about 5-12% of a junior program's cost (estimate), up to about 15-20% for very
  small single-rig programs.
- **Market math:**
  - Saskatchewan exploration spend is on the order of CAD 0.4-0.6B/yr in the uranium boom (memory), with
    about half on drilling. 5-12% gives CAD 20-70M/yr of waste in Saskatchewan.
  - Global non-ferrous exploration budgets are about USD 12-13B/yr (S&P Global, memory). Drilling is
    roughly 40-55% of that. 5-12% of drilling-heavy spend gives about USD 0.3-1B/yr of waste globally.
  - A company capturing 10-30% of that is a USD 30-300M/yr business. That ceiling fails rubric item 6
    (it lands in the "USD 100-400M/yr tool or service market" Dhruv rejects).

---

## 9. Scoring against the rubric

- **(1) Discovery is 80% of the work?** No. Coordination is not the hard, usually-failing step. Holes miss
  because of targeting, not logistics.
- **(2) Signal in illegible public data, with ML essential?** Weak. Scheduling and pooling is an operations
  research and marketplace problem. ML is a nice-to-have. One partial exception: SMAD assessment files
  contain decades of filed cost statements (metres, days, standby, contractor), which could build a public
  benchmark of what a program should cost (inference). That is still a tool.
- **(3) and (4) Cheap asset and step-up buyer?** Not for a pure ops company. Only if the ops company takes
  equity or claims in exchange for drilling (drill-for-equity, or "we drill your claims at cost for a
  carried interest").
- **(5) Ladder?** Ops software or buying group, then pooled camp and mob operator, then owning crews and
  rigs (Durin-like), then a drill-for-equity land company. The top rung is a land and discovery company,
  which converges on Terranox's own model and sits inside Dhruv's 2026-10-03 ban zone (noted, not filtered).
- **(6) Ceiling?** Low unless it climbs to the equity rung.

**Bottom line.** Coordination and logistics waste is real but modest: about 5-12% of program cost, with
fixed mob and camp on short programs and the small-program rate premium as the biggest pieces. It is
partly owned already by CorePlan, Seequent, Hexagon and the drilling majors. The binding constraint in the
2023-26 boom was experienced drill crews, which no platform can conjure. As a standalone new company, kill it.
The only salvageable shape is a vertically integrated "drilling operator that takes equity". That needs
better targeting to be worth anything, so it is a Terranox-adjacent move rather than a separate venture.
Durin is the closest live attempt, and it is too early to call.

## Open gaps (search budget exhausted)
- SRC published turnaround times and any 2023-26 backlog statements.
- Major Drilling, Boart Longyear and Foraco utilisation in the 2015-16 trough against 2024-26 (pricing
  amplitude across the cycle).
- Athabasca-specific mob/demob and heli-support line items from a recent assessment report (SMAD itself
  would have these).
- Durin's later rounds. Whether DrillDocs, Rigminder or DrillLogix exist in minerals.
- Any documented shared-camp or pooled winter-road arrangements in the Athabasca or Yukon.
