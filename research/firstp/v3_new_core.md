# v3 new core sweep: idle assets, used equipment, spare parts, capacity (19 Oct 2026)

**Verdict: no pass.** 32 new ideas scored under the relaxed v3 tests (V3_SHAPE.md). Eight scored 16+ on paper, and the top four were web-checked. All four fell below 17 once checked:

| Checked idea | Paper | After checks | What killed it |
|---|---|---|---|
| Retired aero-engine cores turned into data-centre power units | 19 | **15** | FTAI already runs this at scale ($1.465B hyperscaler order) and sellers price the scarcity (S1). Borescope ML lift is unproven |
| Legacy 200mm fab tools, bought from closing fabs and requalified | 17 | **13** | Scarcity is real, but brokers price it (SurplusGLOBAL, Moov). There is no tool-log data to train on, so the ML leg is about 1 |
| Distressed operating solar, with an ML SCADA loss-finder | 17 | **14** | This is a yield-and-rerate business (L12). Fault ML is sold by vendors (L7). Precedent buyers won on asset management, not models |
| EV packs bought at scrap and ML-graded into second-life BESS | 17 | **13** | Second-life LCOS is worse than new ($234-278 vs $211/MWh). Redwood ($425M Series E) holds the rung |

The pattern is consistent with VERDICT.md. Even with the numbers loosened, **"unknown condition" assets are priced by insiders who already read the condition** (brokers, OEMs, lessors). The asset classes where scarcity has created a step-up (turbines, CFM56, 200mm tools) all repriced publicly in 2021-26, so S1 fails: you buy after the market knows. The best near-miss is #1. It is a real, large business, but the company that owns it is FTAI. A new entrant gets a smaller version where its edge comes from capital and teardown capacity, not ML.

A practical note: if Dhruv wants one thing from this sweep, it is #1's ML question, framed as a cheap test. Can borescope plus flight-history models price a run-out CFM56/CF6 core better than a broker's half-life method? Test it on public auction or teardown outcomes. Kill the idea if MAE is not at least 25% below the half-life baseline. It does not pass the rubric today.

## Scoring
Legs follow V3_SHAPE.md: S1 buy before it's known, S2 step-up 3x+, S3 ML lift over a simple baseline, S4 discovery a major part, S5 compounding own data. Each is scored 0-5, with 3 meaning "clearly present". Standing rules are respected: no prospecting or drilling, not Terranox, and the company owns the asset. "(memory)" marks figures that were not checked here.

| # | Idea (own the asset) | S1 | S2 | S3 | S4 | S5 | /25 | Main weakness |
|---|---|---|---|---|---|---|---|---|
| 1 | **Run-out aero-engine cores (CFM56, CF6-80) to power units / USM**: buy exhausted engines, use ML on borescope and shop records to pick the cores worth converting to 25-48 MW gensets versus parting out | 4 | 4 | 3 | 4 | 4 | **19** | FTAI and ProEnergy hold it; sellers price scarcity |
| 2 | **Legacy 200mm/150mm fab tools** from closing fabs, requalified and sold to mature-node and power-semi fabs | 3 | 4 | 2 | 4 | 4 | **17** | Brokers know the prices; no training data |
| 3 | **Distressed operating solar**: ML on SCADA finds recoverable losses, then buy from lenders or estates | 4 | 3 | 3 | 3 | 4 | **17** | Yield plus rerate; vendor ML (L7) |
| 4 | **EV packs at scrap price**: BMS-log ML grading, then second-life BESS | 4 | 3 | 4 | 3 | 3 | **17** | Economics lose to new LFP |
| 5 | **Mothballed small peakers** restarted for the PJM/MISO capacity price spike; ML on maintenance logs picks units cheap to restart | 3 | 4 | 2 | 3 | 3 | 15 | Capacity price is public; owners (LS Power and others) restart their own units; L4 |
| 6 | **Decommissioning-plant nuclear spares**: buy inventory from Pilgrim/Indian Point-type estates, ML-match it to the operating fleet's obsolescence list, then dedicate | 3 | 4 | 3 | 3 | 3 | 16 | Utilities share through pooled inventory programmes; small market (memory) |
| 7 | **Wind gearbox/main-bearing rotable pool**: buy used components, ML predicts remaining life, run an exchange pool for aging fleets | 3 | 3 | 3 | 3 | 4 | 16 | OEM and ISP service shops own it; mostly a service |
| 8 | **Aging wind farms out of PPA**: ML picks which to buy for repowering and PTC requalification | 3 | 3 | 3 | 3 | 3 | 15 | Repower decision is standard developer work; capital edge |
| 9 | **Gas-turbine hot-section used serviceable parts (7F/7E)**: ML on inspection images grades used blades and vanes | 3 | 3 | 3 | 3 | 4 | 16 | PSM (Hanwha), EthosEnergy, MD&A; OEM IP limits |
| 10 | **DLA/GSA surplus lots by weight**: ML reads NSNs to find obsolete legacy-fleet spares, resold to MRO and FMS customers | 4 | 4 | 3 | 4 | 3 | 18 | Demil and export-control limits; dealers already scan lots; small per lot |
| 11 | **Excess electronic-component inventory**: ML predicts which obsolete parts go short | 3 | 3 | 3 | 3 | 3 | 15 | Brokers (Fusion, Smith); cyclical; a trading business |
| 12 | **Abandoned telecom copper cable plant**: buy salvage rights; ML reads old outside-plant records to estimate recoverable copper | 3 | 3 | 3 | 4 | 2 | 15 | Telcos sell to salvage contractors; lead-sheath liability |
| 13 | **Industrial MRO surplus from closing plants**: ML crosswalks part numbers to demand | 3 | 3 | 3 | 3 | 3 | 15 | Radwell and EquipNet scale; low tail |
| 14 | **Used CNC machine tools**: ML on spindle and controller logs grades auction lots | 3 | 2 | 3 | 3 | 3 | 14 | Step-up about 2x; dealer market |
| 15 | **Used industrial robots**: grading and refurbishment | 3 | 2 | 2 | 3 | 3 | 13 | Low step-up; RDR and Eurobots |
| 16 | **Stranded new LFP/NMC cells** from bankrupt EV and battery makers, cycled and ML-graded into BESS | 3 | 3 | 3 | 3 | 3 | 15 | Insiders win (L10); falling cell prices |
| 17 | **Reserved-but-unused data-centre power contracts** resold to neoclouds | 2 | 3 | 2 | 3 | 2 | 12 | Contracts are non-assignable; yield (L12) |
| 18 | **Water rights for industrial and DC sites**: ML predicts change-of-use approval and firm yield | 3 | 3 | 3 | 3 | 2 | 14 | Vidler-type, small; L4 |
| 19 | **NRC-licensed facilities** (hot cells, fuel-fab sites) bought for transfer to advanced-nuclear firms | 3 | 3 | 1 | 2 | 2 | 11 | No ML; licence transfer is slow |
| 20 | **Idle test infrastructure** (wind tunnels, test stands, vacuum chambers) bought from labs and rented to defence and space startups | 3 | 3 | 1 | 2 | 2 | 11 | Service-like; no ML |
| 21 | **End-of-life satellites with fuel left**, bought and life-extended | 2 | 3 | 1 | 2 | 1 | 9 | Few assets; no ML |
| 22 | **Spent PGM catalysts**: ML predicts assay before purchase | 2 | 2 | 3 | 3 | 3 | 13 | Assay is legible; refiners' margin |
| 23 | **Retired steam turbines and generators** from coal closures, reused at DC gas sites | 3 | 3 | 2 | 3 | 2 | 13 | Brokers; fit-to-site engineering decides |
| 24 | **Used large electric motors/generators** (rewindable), ML condition grading | 3 | 2 | 3 | 3 | 3 | 14 | Like recertified transformers (killed, 12) |
| 25 | **Decommissioned teletherapy Co-60 and sealed sources**, recovered for resale | 2 | 2 | 1 | 2 | 1 | 8 | Liability; tiny |
| 26 | **Distressed BESS projects** from failed developers with degraded cells, re-optimised | 3 | 3 | 3 | 3 | 3 | 15 | Fire and safety liability; L10 |
| 27 | **Used mining haul-truck and loader fleet**, ML condition grading | 3 | 2 | 3 | 2 | 3 | 13 | Priced dealer market |
| 28 | **Robotics fleet that builds a manipulation data asset** (own robots doing paid industrial tasks; sell the data to labs) | 1 | 3 | 3 | 2 | 5 | 14 | No "buy before known"; labs collect their own data |
| 29 | **Ex-military engines and airframes** (T56, TF33) for power or USM | 3 | 3 | 2 | 3 | 3 | 14 | Demil rules; few units |
| 30 | **Tank and rail cars of unknown condition** from lessor run-offs | 3 | 2 | 3 | 3 | 3 | 14 | Lessors (GATX, Trinity) have the data |
| 31 | **Defence legacy-platform obsolescence spares**: buy out-of-production OEM lines and tooling, ML forecasts demand from fleet records | 3 | 3 | 3 | 3 | 3 | 15 | TransDigm-style; edge is pricing power, not ML |
| 32 | **Behind-the-meter backup gensets**: buy hospital and DC fleets, ML picks sites to aggregate for capacity | 2 | 3 | 3 | 2 | 3 | 13 | Service/VPP (Enchanted Rock); L12 |

Distribution: 1 at 19, 1 at 18, 3 at 17, 4 at 16, 10 at 15, and the rest at 14 or below. #10 (DLA surplus, 18) was not checked in depth. It ranks high on paper, but it is not venture-scale: Liquidity Services' whole GovDeals and GovPlanet marketplace is worth ~$0.8-1B (memory), and dealer margins are per lot. With S2 and size adjusted it is about 15. It is noted here so it is not rerun.

## Web checks of the top 4

### 1. Run-out aero-engine cores to power and USM: 19 -> 15 (S1 2, S2 4, S3 2, S4 3, S5 4)
- **Incumbent, same model, at scale.** FTAI launched FTAI Power to turn retired CFM56s into 25 MW turbines and won a **$1.465B initial purchase order from a US hyperscaler**. It guides $1.05B of 2026 Aerospace Products EBITDA, has 3,000 modules a year of CFM56 capacity, and targets 25% share ([GuruFocus Q2-26 call](https://www.gurufocus.com/news/8991870/ftai-aviation-ltd-ftai-q2-2026-earnings-call-highlights-record-module-production-and-power-business-breakthrough-drive-growth-amid-strategic-shifts), [MarketBeat](https://www.marketbeat.com/instant-alerts/ftai-aviation-q2-earnings-call-highlights-2026-07-30/)). ProEnergy turns CF6-80C2 cores into 48 MW PE6000s and has sold 21 units, more than 1 GW, for two DC projects ([IEEE Spectrum](https://spectrum.ieee.org/ai-data-centers), [DCD](https://www.datacenterdynamics.com/en/news/proenergy-offers-repurposed-jet-engines-to-data-cent/)). The rung is held, and the size proof is strong: this is a $1B+ EBITDA business.
- **Price gap (S1 and S2).** There is a step-up: an exhausted engine at $0.8-1.2M is said to yield $1.6-2.2M of USM ([avi-go](https://avi-go.com/news/articles/618666915b61cd98395db62da94c65ee), unsourced). Half-life CFM56-7B values are $3.8-7.1M (IBA via [Aerohaber](https://aerohaber.com/what-a-retired-boeing-737s-engines-are-actually-worth/)), and lease rates are about 34% above 2019. New LM6000 waits are 3-5 years ([AOL/WSJ syndication](https://www.aol.com/articles/data-centers-look-old-airplane-180002578.html)). But sellers know all of this. Aviation Week reports that asset managers part out earlier *because* engine values have risen ([AvWeek](https://aviationweek.com/mro/aircraft-propulsion/fast-5-engine-values-drive-earlier-aircraft-teardowns)), and GE now expects only 1.5-2% retirements in 2026, down from 3-4%. Supply is thin and priced, and the step-up is a 2x margin, not a buy-before-known.
- **ML versus baseline.** Published RUL work runs almost entirely on NASA's simulated C-MAPSS data ([FLAIRS 2024](https://journals.flvc.org/FLAIRS/article/view/135514), [arXiv](https://arxiv.org/pdf/1907.05146)). The only borescope-to-RUL claim found is a vendor page ([iFactory](https://ifactoryapp.com/industries/power-plant/gas-turbine-hot-gas-path-inspection-ai-borescope-analytics)). There is no evidence of lift over a broker's LLP/half-life method. FTAI's edge is shop capacity and PMA parts, not models.
- **Cheapest test:** model teardown outcomes versus the half-life baseline. Kill the idea if MAE is not at least 25% better.

### 2. Legacy 200mm fab tools: 17 -> 13 (S1 2, S2 4, S3 1, S4 3, S5 3)
- **The scarcity is real and old.** Used 200mm units fell from 7-8k a decade earlier to under 1,000, with prices up ~20% in six months in 2021 ([Asiae / SurplusGLOBAL CEO](https://cm.asiae.co.kr/en/article/2021031211110560910)). About 600-720 cores were available against demand for ~1,000 ([SemiEngineering](https://semiengineering.com/200mm-equipment-shortfall)), and shortages were expected to last years ([SemiEngineering](https://semiengineering.com/200mm-shortages-may-persist-for-years)). The secondary market is about 5-10% of equipment capex.
- **Incumbents.** SurplusGLOBAL, and Moov ($41M Series A led by Tiger Global, partly to buy inventory) ([Coverager](https://coverager.com/moov-raises-41-million/), [eeNews](https://www.eenewseurope.com/en/online-semiconductor-equipment-broker-moov-raises-more-funds/)). OEMs (AMAT, Lam, TEL) refurbish their own tools. Brokers price the scarcity, which fails S1.
- **ML.** Tool condition sits in fab-private logs that sellers rarely release. No public evidence of lift was found, so S3 is about 1.

### 3. Distressed operating solar: 17 -> 14 (S1 3, S2 3, S3 2, S4 3, S5 3)
- **Price gaps exist.** Sunnova's assets sold for a credit bid plus only $25M cash ([Norton Rose](https://www.nortonrosefulbright.com/en/news/f4c29d1e/norton-rose-fulbright-advises-goodfinch-and-sunstrong-in-acquisition-of-sunnova)). SunStrong claims a 94% production increase on a 25 MW portfolio bought from bankruptcy (vendor claim) ([SunStrong](https://sunstrongmanagement.com/partners/)). EFG Hermes ran ex-SunEdison assets 25% ahead of plan, while Foresight suffered long underperformance on similar assets ([Solar Power Portal](https://www.solarpowerportal.co.uk/efg_hermes_lauds_optimisation_team_as_ex_sunedison_portfolio_exceeds_expect)).
- **Why it fails.** The win is 25-90% more output, which is a yield and NAV rerate (L12), not a 3x step on a bought claim. Loss-finding ML is sold by vendors such as Raptor Maps and Power Factors (memory) (L7), and REC Power and others already buy underperforming assets as a business ([REC](https://recsolar.com/project-portfolio-acquisitions)).

### 4. EV packs at scrap, ML-graded into second-life BESS: 17 -> 13 (S1 4, S2 2, S3 3, S4 2, S5 2)
- **Buy-in is cheap:** negative to $24/kWh, typically $5-10, against ~$125/kWh deployed ([Compound thesis](https://compound.vc/thesis/thesis/2nd-life-batteries-for-storage)). But grading costs $70-100/kWh today ([NSF SBIR](https://nsf.elsevierpure.com/en/projects/sbir-phase-i-rapid-used-battery-testing-system-2/)). Over 15 years, second-life LCOS is **$234-278/MWh against $211 for new**, even with capex at 64-79% of new ([PMC study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10339184)). The proven state is not worth materially more once new LFP prices fall, so S2 is about 2.
- **ML is honest but commoditising.** Pulse-plus-ultrasound neural SoH is targeted at <2% error in <75s (SBIR above), and Stanford reports GPR on 200+ cells ([Stanford](https://pangea.stanford.edu/ERE/pdf/OnoriPDF/Journals/80%20PDF.pdf)). These are open methods (L11).
- **Rung held.** Redwood Energy runs a 63 MWh second-life microgrid for Crusoe and has 1+ GWh in its pipeline, backed by Redwood's $425M Series E ([Energy-Storage.news](https://www.energy-storage.news/redwood-energy-positions-second-life-bess-as-essential-infrastructure-for-us-data-centre-load-growth-domestic-manufacturing-needs/), [pv magazine](https://pv-magazine-usa.com/2025/06/30/redwood-crusoe-deploy-second-life-batteries-at-ai-data-center-for-63-mwh-storage/)).

## What this sweep adds to the map
- **L14 (proposed): condition-unknown used hardware is read by insiders.** The holders who can see condition (lessors, OEM shops, brokers, fab owners) also set the price. The buyer's information gap closes at the point of sale, so S1 tops out at about 2-3 wherever scarcity has made the asset worth chasing.
- Where the relaxed numbers do let a real company through, it is already built and capital-led (FTAI, Redwood, ProEnergy). Loosening the numbers turned up incumbents. It did not open empty rungs.
- The recommendation in VERDICT.md stands: option A (FTR book), B or C. No v3 core idea beats them.
