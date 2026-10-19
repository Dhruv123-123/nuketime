# Sweep L6: drop "every first rung is already held" (19 Oct 2026)

## Verdict

Nothing survives. With L6 dropped, the best idea is still only 16/25: orphan patents with evidence of use, once Patlytics and the aggregators no longer count against it. It dies on the standing "too small" rule, because the whole brokered patent market is $158M a year, and on L1, because the proof is an opinion that only pays out through years of litigation. The occupancy penalty was rarely the real killer. In round 6 the occupants (LandGate, Shovels, Paces, Heatmap) killed ideas by **selling the signal to every buyer**, which is L2, not L6. In round 7 the PE roll-ups were the visible killer, but under them sat a zero-discovery frame, thin shop-scale data, and capex walls at rung 3. Taking the occupancy penalty off moves the round-7 ladders up only 1-2 points out of 30, and the rung-one occupants turn out to be weak against an ML entrant only where ML is not the edge. The most interesting finding is that crowded rungs *are* winnable by late entrants: Cloverleaf was founded in 2024 and had sold 7 GW of powered land by 2026. But the entrants who won did it with $300M of PE capital and utility relationships, not with ML, so relaxing L6 alone leaves the rubric's L1-L3 and the "ML must be the edge" rule as the binding constraints.

## How it was scored

- **Rubric:** the gold rubric (/25), with every law and standing rule kept except L6.
- **C5 (ladder):** now judged on whether the rungs above lead to the whole chain *and* whether a new entrant can still win rung one or skip to rung two. An occupant only lowers C5 if it is fast, funded *and* ML-capable.
- **Round-7 ideas:** these were originally scored on the /30 ladder rubric. They also get a ladder rescore, with the "is the rung open" criterion (their L5) set to "winnable if incumbents are PE roll-ups or slow".
- **Old scores:** shown as originally reported (scorer / verified mean).
- **Sources:** facts marked (memory) are from earlier rounds' JSON or prior knowledge. The URLs are from this sweep's web checks.

## 1. Old ideas rescored with L6 dropped

| # | Idea (source) | Old score | Occupant that killed it | New /25 (C1-C5) | Ladder /30 with L5 relaxed | Why it still dies |
|---|---|---|---|---|---|---|
| 1 | Orphan patents with evidence of use (hunt 9, round 6) | 14 /25 (verified 10-11) | Patlytics ($40M B, Apr 2026), TechInsights, Acacia, IV | **16** (3,3,3,4,3) | n/a | C5 rises from 1 to 3: Patlytics sells software and owns no patents, and Acacia and IV are slow. It still dies on L1, since the chart is an opinion and value comes through litigation, and on size, since the brokered market is $158M/yr and the median asset is $33-95k |
| 2 | Powered-land options (Cloverleaf, Tract, LandGate) | 14 /25 (verified 12.7) | Cloverleaf, Tract, LandGate | **15** (2,3,3,2,5) | n/a | C5 was already 4. The kill was C4/L2: LandGate sells headroom at every substation, and our own backtest scored AUC 0.721 against 0.727 for a lookup table. L3 also holds: farmers ask 5-10x, and SB6 gives capacity to whoever posts collateral |
| 3 | Entitled Acre (data-centre rezoning, Paces) | 14 /25 (verified 12.3) | Paces, LandTech | **15** (2,3,3,2,5) | n/a | Same as #2. Paces sells the screen to the buyers, so the moat is execution |
| 4 | Entitlement arbitrage on exurban land (Shovels/ReZone) | 14 /25 (verified 12.7) | Shovels/ReZone | 14 (2,3,3,2,4) | n/a | Unchanged. Shovels sells decisions for 600+ cities, which is an L2 kill, not L6 |
| 5 | Grid-queue attrition land options (PICK8) | 6 /10, then killed | Cloverleaf, Tract, GridCARE | 11 (2,3,1,1,4) | n/a | Our backtest found no edge over a lookup table (L2) |
| 6 | Back-to-birth engine LLPs (ProvenAir, flydocs) | 13 (verified 10) | ProvenAir, flydocs | 11 (2,2,2,2,3) | n/a | The proof sits in private operator records (14 CFR 91.417), so the owner is the informed party (L5/L3). The step-up is 5-30x at best |
| 7 | Lineage: dormant SBIR firms' Phase III rights (PICK8) | 5/10 red-team | Arlington Capital SBIR roll-up | 13 (2,3,2,3,3) | n/a | Arlington was never the real killer. Phase III needs a programme office that wants the product, and that step usually fails and is not abstracted |
| 8 | Brightfield: distressed C&I and community solar rescue (round 7) | 19 /30 (verified 15.7) | CleanCapital, Spruce, GoodFinch/SunStrong | 13 (3,2,2,3,3) | 16.7 | Step-up ~1.5-3x. Big distress clears as whole portfolios to DIP lenders (Sunnova went to GoodFinch by credit bid + $25M). ML only finds targets. End state is a ~$2B yieldco |
| 9 | Armature: MV motor repair roll-up | 19 /30 (verified 17.0) | IPS (Searchlight), Group CBS | 7 (1,1,1,1,3) | 18.5 | Zero discovery frame, and shop data of hundreds of teardowns a year is too thin. ABB, Siemens and WEG wall off the OEM rung |
| 10 | Recast: reverse-engineered obsolete spares | 18 (verified 16.3) | Chromalloy, PSM, EthosEnergy, Re:Build | 11 (2,2,2,2,3) | 17.3 | It is a job shop: every part needs its own qualification, and OEM long-term service agreements block the end state |
| 11 | Dedicate: reactor obsolete parts | 18 (verified 15.7) | Curtiss-Wright, Mirion/Paragon ($585M) | 10 (2,2,2,1,3) | 17.2 | Approved-vendor lists and NUPIC conservatism. Even a winnable rung earns services margins |
| 12 | Fluidline: DGA lab to transformer reman | 18 (verified 14.3) | Doble/ESCO, SDMyers | 7 (1,1,1,1,3) | 15.3 | The incumbents' DGA datasets are bigger, so the ML entrant starts behind on data, not just on share |
| 13 | Breakerline: reconditioned MV switchgear | 17 (verified 15.3) | RESA ($825M+), Shermco | 7 (1,1,1,1,3) | 16.8 | Data-centre buyers reject reconditioned MV gear, which kills demand whoever holds the rung |
| 14 | Bayline: fast-turn switchboard line | 17 (verified 15.3) | Giga Energy, Eaton | 7 (1,1,1,1,3) | 16.3 | The majors allocate breakers to their own lines (a supply kill) |
| 15 | Acceptance: NETA testing to substation-as-a-service | 17 (verified 16.0) | Shermco ($1.6B Blackstone), RESA | 6 (0,1,1,1,3) | 18.0 | It is a service and labour-bound, so it breaks the "own the thing" rule |
| 16 | AlloySort Yard / Sortera-type ML scrap upgrading | 15 /30 | Sortera ($45M, Nov 2025), TOMRA | 11 (3,1,2,1,4) | 16.5 | The spread is a commodity and the ML is buyable: TOMRA AUTOSORT PULSE sells LIBS alloy sorting to any yard |
| 17 | Quiet Fleet: zero-emission rental power | 17 (verified 14.7) | Aggreko, Anode, rental majors | 6 (0,1,1,1,3) | 16.0 | Capex and utilisation. Moxion went into Chapter 7 after raising $110M |
| 18 | Nodal: Texas batteries to REP to utility (thesis) | 21 self (verified 13.3) | Base Power (~$1B raised), Gridmatic | 9 (1,1,2,1,4) | 15.3 | Rung economics: ERCOT batteries earned ~$29/kW-yr in 2025 (Modo), and the optimisation uplift goes to any owner who switches optimiser |
| 19 | Loopworks: reactor test loops (thesis) | 18 self (verified 10.3) | Copenhagen Atomics, Kinectrics/BWXT, labs | 7 (1,1,1,1,3) | 12.3 | No demand: developers run their own loops, and four pilot reactors went critical without third-party loops |
| 20 | Overwatch: grid drone network (thesis) | 20 self (verified 13.0) | Skydio, Percepto, Voltair | 7 (1,1,1,1,3) | 14.5 | The why-now is false: Part 108 has sat at OIRA since 10 Jul 2026, and Skydio is both the supplier and a competitor |
| 21 | Nuclear-qualified contract manufacturer (PICK3) | Pick (open 4/5) | none (it was rated open) | 8 (1,1,1,1,4) | n/a | L6 never applied. Under the gold rubric there is no discovery rung, and the moat is qualification and execution |
| 22 | Heat-to-power bottoming blocks (PICK5) | Pick | Turboden, Exergy (ORC) | 8 (1,1,1,1,4) | n/a | The hardware is not ML-led, so it fails the ML standing rule rather than L6 |

**What the table shows.** Dropping L6 lifts exactly one idea by more than a point: orphan patents, where C5 goes from 1 to 3 and the total from 14 to 16. The round-7 ladders gain 1-2 points of 30 but still score 6-13/25 on the gold rubric, because a roll-up has no discovery rung (C1 ≤1) and no step-up (C2 ≤1).

## 2. New ideas that only make sense with L6 dropped

Each idea is a crowded but winnable rung where an ML-native owner-operator could plausibly beat PE or slow funded players. Scored /25 as C1, C2, C3, C4, C5.

| # | Idea | Rung-one occupants (why they can be beaten) | C1 | C2 | C3 | C4 | C5 | /25 | What kills it instead |
|---|---|---|---|---|---|---|---|---|---|
| N1 | **Queue-position buyer:** read cluster and facility study PDFs across PJM, MISO, SPP and ERCOT, buy stalled projects whose network-upgrade costs will fall as upstream projects withdraw, and sell energisable positions to data-centre developers | Paces, Enverus, IPP M&A desks (they screen but rarely buy positions) | 3 | 3 | 2 | 2 | 4 | **14** | L2: our attrition backtest scored 0.721 against 0.727 for a lookup table. L3: sellers are developers who read their own studies |
| N2 | **EV packs to second-life BESS:** buy salvage packs at $10-30/kWh, ML grades state of health from a short pulse test instead of a full cycle test, sell certified modules | B2U, Moment, Smartville, Redwood Energy (memory) | 3 | 2 | 3 | 2 | 3 | **13** | Cheap new LFP collapses the certified second-life premium, so the step-up is ≤2-3x |
| N3 | **Solar repower finder:** compute every US plant's performance ratio from EIA-923 monthly generation and NSRDB irradiance, buy 2010-16 underperformers and repower them | Altus, Greenbacker, Clearway, CleanCapital | 3 | 2 | 2 | 2 | 3 | 12 | L3: owners see their own SCADA and price the fix. Step-up ~1.5-2x |
| N4 | **Surplus-interconnection hunter:** add behind-the-meter gas or BESS at retiring fossil POIs (FERC Order 845 surplus service) and lease them to data centres | NextEra, Tenaska, plant owners | 2 | 3 | 2 | 1 | 4 | 12 | L3/L4: the plant owner holds the right and knows its value |
| N5 | **Untraceable flight engines to ground power:** buy CF6/CFM56 cores with broken back-to-birth trace (cheap for flight, irrelevant for ground power) and convert them for data centres | FTAI Power, ProEnergy (memory) | 2 | 3 | 1 | 2 | 4 | 12 | Standing rule: ML is not the edge. Conversion is the bespoke build, and FTAI holds 1,000+ CFM56 engines |
| N6 | **Aircraft part-out with ML teardown selection:** predict which retirements part out above the whole-asset price | AerSale (a later entrant that won), AAR, GA Telesis, FTAI | 3 | 2 | 2 | 2 | 3 | 12 | L5: the records are private and the seller is informed. Step-up 2-3x |
| N7 | **Distressed residential solar books after Sunnova/SunPower:** ML on servicing records to buy the books cheaply | GoodFinch/SunStrong, Spruce Power | 2 | 2 | 2 | 2 | 3 | 11 | Distress clears to DIP lenders by credit bid, so there is no cheap seller |
| N8 | **Orphaned OT/ICS software lines run by AI agents:** Constellation for industrial control software, with security patching as the wedge | Constellation, Valsoft, a wave of 2025-26 "AI roll-up" funds | 2 | 2 | 1 | 2 | 3 | 10 | No discovery rung: the assets are bought at broker multiples, and AI roll-ups are already crowded |
| N9 | **Wind-farm life extension (US NeXtWind)** | NeXtWind (EU), NextEra in-house | 2 | 2 | 2 | 2 | 3 | 11 | Merchant capture of $15-25/MWh is below the $25-45/MWh opex of 20-year-old turbines (round-7 data) |
| N10 | **ML-graded transformer reman, entering at rung two (data-centre spares pool)** | Sunbelt Solomon, regional reman shops | 2 | 2 | 2 | 1 | 3 | 10 | The lead-time premium is easing as Hitachi, Eaton and Cliffs capacity lands in 2026-28 |
| N11 | **Brokered mixed-scrap upgrading in batteries (black mass alloy sort)** | Redwood, Cirba, Ascend (post Li-Cycle) | 2 | 1 | 2 | 1 | 4 | 10 | A commodity spread, and the ML can be bought |
| N12 | **AI-verified alarm-monitoring roll-up:** buy recurring-revenue accounts and convert them to AI video verification | Pye-Barker, Brinks Home and other PE roll-ups | 1 | 1 | 1 | 1 | 3 | 7 | L1-L4: a pure roll-up with no discovery and a 1.3x re-rate |
| N13 | **HVAC/BAS contractor roll-up selling energy-savings-as-a-service** | Wrench, Apex and other PE roll-ups | 1 | 1 | 1 | 1 | 3 | 7 | Same as N12, and it is a service |
| N14 | **Independent elevator maintenance roll-up with predictive ML** | Otis, Kone, Schindler, TK plus PE independents | 1 | 1 | 1 | 1 | 3 | 7 | The OEMs control parts and codes, and it is a service |
| N15 | **Bridge-power gas fleets for AI campuses** | VoltaGrid (a fast later entrant that won), Aggreko, CAT dealers | 1 | 1 | 1 | 1 | 4 | 8 | Capital and turbine slots decide the winners, not ML |
| N16 | **Counter-UAS site defence for substations and data centres as an owned service** | Dedrone/Axon, DroneShield, Epirus | 1 | 1 | 1 | 1 | 3 | 7 | A service with defence-prime competition |
| N17 | **Used industrial robots refurbished into robots-as-a-service cells** | Formic, regional integrators | 1 | 1 | 1 | 1 | 3 | 7 | Rental economics, and ML is not core |
| N18 | **Used fab vacuum and cryopump reman, entering at subfab-as-a-service** | Edwards, Ebara, SurplusGLOBAL | 1 | 1 | 1 | 1 | 3 | 7 | The OEMs control parts and firmware |
| N19 | **Inspection-data owner (NDT crews feeding a refinery and pipeline integrity model)** | Mistras, Team, Acuren | 1 | 1 | 1 | 1 | 2 | 6 | It is a service, and owners keep the data |
| N20 | **Community-solar subscriber books bought from small developers, run with ML churn and credit models** | Arcadia, PowerMarket, Perch | 1 | 1 | 1 | 2 | 3 | 8 | The book is a contract stream at a market price, so there is no step-up |

The best new idea is N1 at 14/25. That is below the round-6 land ideas and below orphan patents at 16. No new idea scores 4 or more on C1, C2 or C3.

## 3. Top three, checked adversarially with web search

The top three overall are orphan patents (16), powered land / Entitled Acre (15, merged with the new queue-position buyer N1 because they are the same power-side bet), and distressed DG solar rescue (13, tied with N2 EV second-life; solar was chosen because it was round 7's top ladder idea). A short Sortera note is added because AlloySort was the most direct "occupied by a funded ML startup" case.

### 3.1 Orphan patents with evidence of use: refuted

- **Incumbent size and funding:** Patlytics raised a $40M Series B on 8 Apr 2026, led by SignalFire, about $65M in total. It serves over 40% of the Am Law 100 and markets automated EoU discovery ([Pulse 2](https://pulse2.com/patlytics-40-million-raised-for-ai-patent-lifecycle-platform-expansion/amp/), [AlleyWatch](https://alleywatch.com/2026/04/the-alleywatch-startup-daily-funding-report-4-8-2026/)). It sells software and does not buy patents, so on L6 alone the rung *is* winnable: an owner-operator that buys patents is a different business.
- **Market growth:** the secondary brokered patent market was $158M in 2024, flat with 2022 and 2023 ([IAM summary of RO 2025](https://www.iam-media.com/article/the-rules-of-the-game-may-have-changed-the-brokered-patent-market-still-alive-and-kicking), [RO 2025](https://www.richardsonoliver.com/publications/the-2025-richardson-oliver-patent-market-report)). No 2026 edition was found.
- **Has a second entrant won before?** Yes. Acacia, IV, RPX and Dominion Harbor coexist, but every one realises value through licensing or litigation campaigns over years.
- **Verdict: dead.** It is too small (flat $158M/yr), the proof is an opinion (L1 in its litigation form), and Patlytics now gives every buyer the same EoU signal, which makes the ML edge an L2 problem rather than L6.

### 3.2 Powered land and queue positions (Cloverleaf/Tract second entrant): refuted, with the best L6 evidence

- **Incumbent size and funding:** Cloverleaf raised about $300M at founding in 2024 from NGP and Sandbrook. It has sold more than 7 GW of powered land, including sites for Oracle and OpenAI, claims a 10 GW+ pipeline, and in Aug 2026 took a minority Nvidia investment (reported as several hundred million dollars) while exploring a sale with JPMorgan ([DCD](https://www.datacenterdynamics.com/en/news/nvidia-backs-data-center-powered-land-company-cloverleaf/), [BNN Bloomberg](https://www.bnnbloomberg.ca/business/company-news/2026/08/21/nvidia-invests-in-data-center-developer-cloverleaf-infrastructure/), [ESG Today](https://www.esgtoday.com/cloverleaf-infrastructure-raises-300-million-to-develop-low-carbon-data-center-sites/)). Tract holds 11,000+ acres around Reno with NV Energy commitments of 2 GW+, plus a 2.4 GW Hanover, VA park ([DCD Reno](https://datacenterdynamics.com/en/news/tract-acquires-8590-acres-in-reno-nevada-for-data-center-park), [DCD Virginia](https://datacenterdynamics.com/en/news/tract-announces-24gw-data-center-park-outside-richmond-virginia)).
- **Market growth:** data-centre land sales were ~$3.3B in Q1 2026, up 141% year on year. Texas power-ready sites fetch ~$800k/acre against $2.5-10k for unstudied land. In Northern Virginia powered land is ~$6M/acre against ~$4M for entitled land without power ([Bisnow](https://www.bisnow.com/news/national/data-center-development/data-center-sites-are-warping-the-market-for-developable-land-134771), [Data Center Knowledge](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)).
- **Has a second entrant won before?** **Yes, decisively.** Cloverleaf entered after Tract and others and sold 7 GW within about two years. The market is big enough for a third or fourth entrant, so L6 really is false here.
- **Verdict: dead anyway.** Cloverleaf won with $300M of PE equity and utility power agreements, not ML. The signal is sold (LandGate headroom, Paces screening), and our own queue backtest found no edge over a lookup table (L2). The Texas ~100x gap ($800k against $2.5-10k) goes to committed load and collateral under SB6, not to the study (L1/L3, round 4). It is fundable, but as a capital-and-relationships developer, which breaks the ML standing rule.

### 3.3 Distressed C&I and community solar rescue (Brightfield): refuted

- **Incumbent size and funding:** CleanCapital buys operating portfolios at a steady pace: 64 projects and 51.2 MW from Greenbacker (Jul 2025), 27 MW + 25 MWh from Pacifico, and 75.2 MW in NJ with distressed-credit fund CarVal ([Utility Dive](https://www.utilitydive.com/news/cleancapital-acquires-64-project-51-2mw-solar-portfolio-from-greenbacker/756419), [Proximo](https://www.proximoinfra.com/news/71336/CleanCapital-acquires-27MW-distributed-portfolio)). None of these was sold as distressed.
- **Where the distress went:** Sunnova's whole fleet went to its DIP lenders (Oaktree, Farallon and others) through GoodFinch/Solaris, for a credit bid plus $25M cash ([Solar Power World](https://www.solarpowerworldonline.com/2025/08/court-approves-sale-of-sunnova-to-goodfinch-management/), [Bloomberg Gov](https://news.bgov.com/esg/solaris-acquires-assets-of-bankrupt-solar-company-sunnova)). Big distress clears to creditors, not to a seed-stage buyer.
- **Market growth:** 6.5 GW of community solar was operating at the start of 2026, with 8+ GW in pipelines. No source discloses distressed $/W ([surgepv composite](https://www.surgepv.com/blog/community-solar-project-case-study-2mw), [pv magazine](https://pv-magazine-usa.com/2025/03/17/community-solar-up-42-ci-up-18-residential-down-25/)).
- **Has a second entrant won before?** Partly. GoodFinch won Sunnova as a newer platform, but it did so as a creditor vehicle.
- **Verdict: dead.** The rung is winnable on L6, but the step-up is ~1.5-3x, and ML only finds targets, with the fix being ordinary O&M (C2/C3). The end state is a yieldco that costs capital to grow.

### 3.4 Note: Sortera, the "funded ML startup holds rung one" case

Sortera raised $45M in Nov 2025, led by T. Rowe Price-advised accounts and VXI, with ~$55M+ raised in total. It runs Markle, IN and is building Lebanon, TN, for ~240M lb/yr ([ESG Today](https://www.esgtoday.com/?p=21942), [alcircle](https://www.alcircle.com/press-release/sortera-scales-solution-to-the-mixed-aluminium-problem-with-45-million-in-funding-and-a-new-tennessee-facility-116332)). TOMRA sells LIBS alloy sorting at 95-97% purity to any yard ([TOMRA](https://tomra.com/waste-metal-recycling/products/machines/autosort-pulse/)). CRU notes that sorting removes the ~40% extrusion and sheet share of zorba and leaves a high-silicon residual whose discount is unresolved ([CRU](https://www.aluminummarketupdate.crugroup.com/global-trade/value-added-products-update-initial-2026-premiums-offers/)). A third entrant could win share; this market has room. But the ML is purchasable, the margin is a commodity spread, and the residual problem eats into it. So L6 is not what kills it; C2 and C4 are.

## 4. What kills the rest, by law

| Killer | Ideas it kills once L6 is dropped |
|---|---|
| L2: the signal is already productised or a lookup table matches the model | Powered land, Entitled Acre, entitlement arbitrage, queue attrition, N1, orphan patents (Patlytics) |
| L3/L5: the seller or owner is informed and prices the hope | Back-to-birth LLPs, N3 solar repower, N4 surplus interconnection, N6 part-out, N7 resi books |
| L1: the proof is cheap and usually succeeds, or is an opinion | Orphan patents (litigation), Lineage (programme-office pull) |
| Standing rule: ML is not the edge, because capital, labour or qualification decides | Every round-7 roll-up, N5, N8, N12-N19, Cloverleaf-style powered land |
| Standing rule: too small | Orphan patents ($158M/yr market), Penstock small hydro |
| Rung economics or a false why-now (independent of who holds the rung) | Nodal (~$29/kW-yr), Overwatch (Part 108), Loopworks (no demand), N2 (cheap LFP), N9 (merchant wind price) |

## 5. Answers to the brief's question

1. **Does anything survive?** No. The best result is 16/25 (orphan patents) and the best new idea is 14/25 (queue-position buyer).
2. **Was L6 binding?** Seldom on its own. Across ~42 rescored or new ideas it was the sole decisive killer for none of them. In round 6 the "occupant" kills were really L2: the occupant sells the signal to everyone, so a second owner-operator has no information edge even if it can win share.
3. **The positive finding:** L6 is empirically false for big, fast-growing rungs. Cloverleaf (founded 2024, 7 GW sold), VoltaGrid, AerSale, GoodFinch and Sortera are all late entrants that won crowded rungs. In each case they won with capital, relationships or hardware. None won with ML on illegible data, and that pattern is the real constraint.
4. **The idea to keep in mind:** if Dhruv accepts a capital-and-relationships developer with ML as a tool, powered land and queue positions is the biggest crowded-but-winnable rung (a $3.3B-a-quarter land market growing 141% a year). But that breaks the "ML is what makes the pain solvable" rule, so it is not a pass.
