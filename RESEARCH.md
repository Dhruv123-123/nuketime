# Company Ideas in Energy / Nuclear / Data Centers / SMRs / Construction

**Stress-tested against the market as of 25 September 2026.**

This document ranks eleven company ideas by how well they survive the four things most likely to go wrong in this sector over the next five years. It is built on five sourced briefings (in `research/`) covering the SMR landscape, data-center power, construction, the startup and investor map, and policy and economics. Every material claim in those briefings carries a source URL and date. Where a number rests on a single or secondary source, it is flagged there and here.

Nothing is literally bullet-proof. The goal is ideas whose demand comes from budgets that already exist, that do not depend on any SMR reaching commercial operation on time, that survive an AI capital-spending slowdown, and that a policy reversal in 2027 or 2029 cannot switch off.

---

## 1. The facts that constrain every idea

These are the load-bearing facts. If one of them changes, the ranking changes.

1. **No small modular reactor is under commercial construction in the United States.** The only SMRs under construction in North America are OPG's four BWRX-300 units at Darlington (first grid connection end-2030, already slipped a year) and TerraPower's Natrium at Kemmerer (construction started April 2026, completion 2030, slipped from 2028). Every hyperscaler SMR deal is a development or framework agreement. Only restarts and existing plants deliver nuclear electrons before 2030. Announced first-power dates for NuScale (2033), X-energy Long Mott ("early 2030s"), Holtec Palisades SMR (2031), Oklo Aurora (2028, DOE path only) and Rolls-Royce (mid-2030s) have all moved right in the last 18 months.
2. **The real FOAK cost datapoint is Darlington: about C$25,700/kW for the first unit and C$17,400/kW fleet average.** Lazard's July 2026 unsubsidized new-nuclear LCOE is $175–255/MWh, up ~20% year on year. No SMR contract price is public. A new entrant should assume FOAK SMR power costs two to three times new combined-cycle gas.
3. **Gas is no longer cheap or fast.** GE Vernova's gas backlog plus slot reservations is 116 GW, sold out through 2028 and filling 2029–30; Siemens Energy 69 GW; Mitsubishi 35 GW. Combined-cycle capex quotes for 2030–31 delivery are $2,000–2,600/kW versus $1,100–1,400/kW for 2026–27 completions. A utility paid $25M just to hold a 2030 turbine slot.
4. **Electrical gear is the binding physical constraint for data centers.** Large power transformers run 30–36 months (up to 60 for EHV), HV breakers ~125 weeks, MV switchgear 52–104 weeks. Wood Mackenzie projects a 30% power-transformer supply deficit in 2026. New OEM capacity (Hitachi, Siemens, Eaton) mostly lands 2027–28.
5. **Data-center load is real but overstated in queues by 5–10x.** ERCOT's large-load queue hit 438 GW in June 2026; Southern Company has 17 GW contracted against a 75 GW pipeline; PJM cut 4.4 GW from its forecast after vetting. Realistic incremental US data-center load by 2030 is 50–70 GW, not the 90–166 GW in utility forecasts. Hyperscaler capex guidance for 2026 is roughly $725B and capex now exceeds operating cash flow.
6. **Flexibility has become a condition of connection, not an option.** Texas SB6 requires curtailment (a July 2026 PUCT order made a 260 MW co-located data center shed full load within 30 minutes), PJM has an interim non-firm transmission product, SPP offers conditional service, and FERC issued show-cause orders to all six RTOs in June 2026. Firm grid service for a 300 MW+ site is 4–7 years; curtailable service is 12–24 months.
7. **Nuclear-grade supply chain and craft are the constraint everyone names.** Kiewit (August 2026) says NQA-1-certified components are the most critical constraint. Zachry (September 2026) says safety-related valves, heavy forgings and I&C "don't exist at the volumes SMR programs will need" and that the certified supplier count fell significantly over the past decade. The NRC's 2026 RIC panel called for "new supplier qualification pathways." Nuclear skilled-trade demand is projected to roughly double from 2025 to 2030 while construction as a whole is short ~439,000 workers and data centers pay a 30% premium for the same electricians.
8. **The nuclear work with money attached today is uprates, restarts, and long-lead procurement.** NRC expects ~30 uprate applications through 2030 (16 in 2027 alone); DOE's UPRISE targets 2.5 GW by 2027 and 5 GW by 2029 with up to 80% federal financing and names "utility engineering bandwidth, long-lead equipment, and staffing" as the bottlenecks. Three restarts (Palisades, Crane, Duane Arnold) carry $4.4B of DOE loans. DOE's $17.5B conditional commitment funds long-lead AP1000 components across five project vehicles. Uprates deliver 39–50% of near-term nuclear additions for under 25% of the capex.
9. **The durable policy is statutory; the fragile policy is executive.** Durable: 45Y/48E nuclear credits through 2033, 45U to 2032, Price-Anderson to 2065, Part 53 and the new-reactor GEIS as final rules, the ADVANCE Act, 23 states with large-load tariffs, Texas's $350M fund and New York's 1–5 GW mandate. Fragile: the DOE loan office's authority sunsets 30 September 2028; the 18-month NRC deadlines are policy, not statute; DOE-authorized pilot reactors have no commercial path without NRC; the D.C. Circuit vacated a DOE 202(c) emergency order on 11 September 2026; the Fed raised rates on 17 September 2026; Section 232 tariffs (50% steel and copper, 15% on some grid gear) remain.
10. **Capital is concentrating, not spreading.** Climate-tech VC was $26.1B in H1 2026 (+55%) on 25% fewer deals; reactor developers raised like defense primes (Valar $1B, Antares $470M, Blue Energy $380M, X-energy $1.1B IPO). Public nuclear corrected hard (Oklo −44%, NuScale −41% YTD; Fermi America −60% from IPO after its anchor tenant walked; Holtec's IPO postponed after a Palisades fuel-handling incident). The revenue that exists today is powered-capacity leasing (~$140–200/kW-month), bridging gas, TRISO fuel (Standard Nuclear's $577M backlog), and software sold to operating utilities.

---

## 2. The screen: what "bullet-proof" means here

Each idea was scored against six tests. An idea had to pass the first three to make Tier 1.

| Test | Question |
|---|---|
| **Budget exists today** | Is someone already spending this money, with a line item, in 2026? |
| **SMR-independent** | Does revenue survive if no SMR reaches commercial operation before 2033? |
| **Policy-independent** | Does it survive a Democratic House in 2027, a change of administration in 2029, or the DOE loan office lapsing in 2028? |
| **AI-capex-independent** | Does it survive a 30–50% cut in hyperscaler data-center spend? |
| **Normalization-proof** | Does it survive turbine and transformer lead times returning to normal around 2029–30? |
| **Incumbent-proof** | Can Bechtel, Kiewit, Westinghouse, GE Vernova, Schneider, Eaton, Constellation, or a $1B-funded startup crush it in 18 months? |

### Survival matrix

Y = survives, P = partially, N = does not.

| # | Idea | Budget today | SMR slip | Policy flip | AI bust | Gear normalizes | Incumbents |
|---|---|---|---|---|---|---|---|
| 1 | Nuclear supplier qualification & CGD network | Y | Y | Y | Y | Y | P |
| 2 | Nuclear-qualified inspection & craft passport | Y | Y | Y | Y | Y | P |
| 3 | Uprate & restart engineering specialist | Y | Y | Y | P | Y | P |
| 4 | Prefab MV substations & gear allocation | Y | Y | Y | P | N | P |
| 5 | Large-load curtailment compliance & settlement | Y | Y | P | P | Y | P |
| 6 | On-site generation permitting product | Y | Y | P | N | P | P |
| 7 | Nuclear construction-execution software | P | N | P | P | Y | P |
| 8 | Utility large-load intake & forecast validation | P | Y | Y | P | Y | P |
| 9 | HALEU deconversion & >5% transport packaging | P | N | P | Y | Y | Y |
| 10 | Sub-150 MW bridging power fleet | Y | Y | Y | N | N | N |
| 11 | Load-commitment and FOAK overrun cover | N | P | Y | N | Y | Y |

---

## 3. Ranked ideas

### Tier 1: existing budgets, independent of SMR timelines and executive policy

---

#### Idea 1. Nuclear supplier qualification and commercial-grade dedication network

**One line.** The shared qualification layer for the nuclear supply chain: pooled NQA-1 audits, commercial-grade dedication (CGD) engineering and testing sold across many buyers, a carried QA program that on-ramps ISO 9001 machine shops into safety-related work, and the only live registry of N-stamp, NPT, MO and NQA-1 holders.

**Why now, with evidence.**
- Kiewit (Construction Dive, 25 August 2026): NQA-1-certified components are "the most critical constraint"; tier-one contractors plan to do CGD themselves. They cannot cover Tier 2 and Tier 3 volumes.
- Zachry Nuclear (Chemical Processing, 8 September 2026): safety-related valves, heavy forgings and I&C "don't currently exist at the volumes SMR programs will need"; nuclear-certified supplier count "declined significantly over the past decade."
- NRC RIC 2026 "Critical Links" panel (Westinghouse, Doosan, Bechtel, ASME): obstacles are "limited global manufacturing capacity for nuclear-grade components, evolving quality assurance requirements, and the need for new supplier qualification pathways."
- Nuclear Scaling Initiative (March 2026): "steep decline" in N-stamp holders and NQA-1 programs; an ISO 9001 on-ramp is emerging; the chicken-and-egg demand problem is the core failure.
- Sandia's 2021 study had to hand-build the N-stamp dataset. No current public, queryable registry exists.
- NRC Inspector General (2022): DOE logged over 100 counterfeit/fraudulent/suspect items in one year while industry databases reported fewer than 10 since 2016; the NRC "does not have a process for collecting, assessing, and disseminating" this information.
- DOE's $17.5B AP1000 long-lead program (June 2026) procures standardized components across five SPVs for seven utilities. It needs programmatic supplier qualification and surveillance now.
- Demand that does not depend on SMRs: the 94-reactor operating fleet does CGD every year; ~30 uprates through 2030; three restarts; Darlington and Kemmerer are under construction; Palisades' restart delays were in steam-generator, decontamination and fuel-handling scopes that all pull qualified suppliers.

**Who pays and from what budget.** Reactor vendors' supply-chain teams (X-energy, TerraPower, Holtec, GEH, Westinghouse, Kairos), EPCs (Kiewit, Bechtel, Hyundai E&C, Fluor), module fabricators (BWXT, Holtec Camden, Blue Energy's shipyard), utilities' procurement engineering for uprates and outages, and the five DOE SPVs. State money subsidizes the supplier side: Indiana's 20% nuclear-manufacturing tax credit and Texas TANEO supply-chain reimbursement are open to manufacturers, not just reactor vendors.

**Revenue model.** Three layers. (a) Qualification services: NQA-1 audits, first-article and surveillance, priced per supplier (estimate $25–75k per initial qualification; treat as an estimate, not a sourced figure). (b) CGD packages: technical evaluations and critical-characteristic test plans per item class, reusable across buyers (this is where the IP compounds). (c) The registry: subscription access for utilities, EPCs, vendors and DOE, plus placement fees when a newly qualified shop wins an order. Services margins in the 30–40% range; registry and reusable evaluations at software margins.

**Competition.** Curtiss-Wright's QualTech NP (CGD services, a division inside a large company), NUPIC (the utilities' joint-audit consortium, members-only, does not serve new vendors), NIAC, Forged Operations (early-stage supplier-qualification SaaS, thinly documented), consultancies (Jensen Hughes, Sargent & Lundy), and in-house teams at Kiewit and Bechtel. None is a network with a data asset and none serves the new-entrant vendors who need it most.

**Moat.** Each audit performed once is sold to N buyers, which is a real network effect; the registry becomes the industry's reference; the CGD evaluation library is accumulated engineering IP; regulatory reputation takes years to build and is hard to copy.

**What kills it.** (1) ASME or NEI formalize an ISO 9001 pathway that makes qualification trivial. Unlikely before 2028 and audits would still be required. (2) Tier-ones fully internalize CGD. Kiewit says they will, but for their own projects only. (3) The company hires poorly: NQA-1 lead auditors and CGD engineers are scarce and this business is those people. (4) The nuclear new-build order book collapses. Even then, the operating fleet, uprates and restarts remain, which is why this passes the SMR-slip test.

**Capital.** $3–8M to first revenue. No plant. A dedication test lab later would be $10–20M and could be financed against contracts.

**90-day validation.** Sign three shared-audit pilots with two vendors and one EPC. Build registry v0 from ASME's public certificate-holder search and NRC docket documents. Recruit two NQA-1 lead auditors from the retiring cohort (about 25% of the nuclear workforce is retirement-eligible). Price a CGD package for one high-volume item class (small-bore safety-related valves) and sell it to two buyers.

---

#### Idea 2. Nuclear-qualified inspection and craft: mobile NDE, weld qualification, and a credential passport

**One line.** A bench of nuclear-qualified non-destructive examination (UT/RT/PT/MT Level II/III), QC inspectors and welder-qualification capability deployed to uprate outages, restarts and the handful of live construction sites, layered with a portable credential record (weld procedure qualifications, rad-worker, fitness-for-duty, site-specific quals) that makes crafts mobile across owners.

**Why now, with evidence.**
- DOE UPRISE (March 2026) names staffing as a top constraint; NRC expects 16 uprate applications in 2027 and 8 in 2028; all draw the same inspectors in 2027–28 as Darlington, Kemmerer, Hermes 2, Clinch River and Palisades.
- NCEA projects nuclear skilled-trade FTE demand rising from 8,200–9,100 in 2025 to 16,000–21,500 in 2030. DOE reports 63% of nuclear manufacturers found hiring "very difficult." 
- Construction-wide shortage ~439,000 (WSJ/ITIF), mostly electricians and pipe layers; data-center construction pays about 30% above typical and is pulling the same crafts.
- Hinkley Point C's latest slip is explicitly "lower-than-expected productivity in its electromechanical installation programme." Vogtle's Lake Charles module plant failed on weld-record integrity (workers entering colleagues' ID codes), not on welding physics.
- Public money for training exists but is fragmented: DOE's $100M nuclear safety training program (a further ~$50M round in 2025 and another anticipated in 2026), New York's $40M workforce fund, Vogtle trained ~30,000 workers and then dispersed them.
- Skillit is the only funded craft marketplace and is generic and data-center-first. No nuclear-specific credentialing platform was found.

**Who pays.** Utilities (outage and capital budgets), EPCs, module fabricators. Nuclear NDE is billed at premium day rates (estimate $1,200–2,500 per technician-day; estimate only).

**Competition.** Team Industrial Services, Mistras, Acuren, IHI Southwest, Westinghouse's inspection arm, union halls, and nuclear staffing firms. These are real incumbents. The edge is focus (nuclear-only), a training pipeline funded by the public programs above, and the credential passport, which none of them offers and which owners want because re-qualifying a welder at every site is dead time.

**Moat.** People and the credential data. Weaker than Idea 1, which is why it ranks second, but it is cash-flow positive within months and it compounds if the passport becomes the industry record.

**What kills it.** Mistras or Acuren stand up a nuclear-focused unit with the same pitch; union jurisdiction limits mobility in some regions; the company cannot recruit Level III examiners; margins compress to staffing-agency levels. It is a services business and a venture-scale outcome is uncertain.

**Capital.** $2–5M. Faster to revenue than anything else on this list.

**90-day validation.** Land one uprate outage subcontract and one construction-site QC contract. Build the passport around ASME IX welder continuity records and 10 CFR Part 26 fitness-for-duty status. Sign an MOU with one community college in the DOE program.

---

#### Idea 3. Uprate and restart engineering specialist

**One line.** A boutique engineering firm that delivers measurement-uncertainty-recapture and extended power uprate packages (licensing amendment requests, safety analyses, instrumentation upgrades, program management) to utilities under DOE's 80% financing, plus restart-scope engineering for the next shutdown units.

**Why now, with evidence.**
- DOE UPRISE lists "engineering schedule and bandwidth at utilities" as the first constraint. 
- NRC expects ~30 uprate applications through 2030 (~2.5 GWe): 18 extended, 10 MUR, 2 stretch. Research and Markets warns NRC resource limits could push 1–2 GW of them into the 2030s.
- Uprates supply 39–50% of near-term nuclear additions for under 25% of the pathway capex, a 2–4x capital-efficiency edge over FOAK SMRs. NRC has approved 172 uprates (~8 GW) historically.
- Buyers are already contracting for it: Meta–Vistra includes 433 MW of uprates; Constellation's Limerick uprate is $2.4B; PJM capacity has cleared at the cap three auctions running, which is what makes an uprate MW worth $325/MW-day before energy.
- Restarts: Palisades (fuel load August 2026, must deliver by March 2027 under its PPA), Crane (2027), Duane Arnold (Q1 2029, $1.9B DOE loan closed September 2026). The scopes that slipped Palisades (steam-generator tube refurbishment, primary decontamination, fuel-handling machine) are the scopes Crane and Duane Arnold face next.

**Who pays.** Utilities, with up to 80% federal financing under UPRISE and rate recovery. Each uprate is a multi-million-dollar engineering scope (estimate $5–20M of engineering per project; estimate only).

**Competition.** Strong: Westinghouse, Framatome and GE Vernova Hitachi own the NSSS analyses; Sargent & Lundy, Enercon and Jensen Hughes do balance-of-plant and licensing. All are saturated, which is the opening. Cameron's LEFM ultrasonic flow meter is effectively sole-source for MUR uprates, which is a second-source hardware angle worth a look but not the core.

**Moat.** Thin: people, speed, and fixed-fee packaging. This is a cash engine, not a platform. It is on the list because its revenue is the most certain of anything here and it survives every test except a deep AI bust (which would soften PJM prices and some utility appetite).

**What kills it.** NRC licensing staff fell (510 departures in 16 months, licensing −30 FTE in the FY2027 request) and review capacity, not utility appetite, may be the actual gate, pushing revenue right. Incumbents hire. The total addressable market is bounded (roughly 30 projects over five years).

**Capital.** $1–3M. Best run as part of a services roll-up with Ideas 1 and 2.

---

#### Idea 4. Prefab medium-voltage substations and electrical-gear allocation

**One line.** Assemble 15–38 kV switchgear, pad-mount and medium-power transformer skids and prefab e-houses for data centers and behind-the-meter generation with 20-week delivery, and run a marketplace for surplus and cancelled gear orders and slot rights, including inspection and certification of used equipment.

**Why now, with evidence.**
- MV switchgear at 15 kV runs 52–80 weeks, 38 kV 78–104 weeks, HV breakers ~125 weeks, power transformers ~128 weeks (Wood Mackenzie), with prices up 45–95% since 2019 by class. Wood Mackenzie projects 30% (power) and 10% (distribution) transformer deficits in 2026.
- "Under 10% of total cost and 100% of the bottleneck" (Build.inc, 2026). 30–50% of US data-center capacity planned for 2026 is delayed, with power gear the most-cited cause (secondary source; SemiAnalysis disputes the magnitude).
- Big capex (Hitachi $457M Virginia, Siemens Charlotte, Eaton $340M South Carolina) targets large power transformers, not MV assemblies. Solid-state transformer startups (Heron $178M, Amperesand, DG Matrix) are years from volume.
- Schneider's 2.5 MW prefab power modules (September 2026) and the Compass pod show buyers pay for speed. Powell Industries is the public comp for a mid-size switchgear builder and is thriving.
- Cancelled and re-bid data-center projects (75 projects / $130B blocked in Q1 2026 alone) strand ordered gear. Fermi America assembled a mixed fleet of F-class, SGT-800, 6B and TM2500 units from wherever it could. No venture-backed player runs the secondary market.

**Who pays.** Data-center developers and their electrical contractors (electrical is about half of data-center labor), behind-the-meter gas developers, utilities, and industrials.

**Revenue model.** Manufacturing margin of 15–25% on assemblies with a speed premium; brokerage commission plus inspection fees on the secondary market; reservation financing spread on slot rights.

**Competition.** Eaton, ABB, Siemens, Schneider, Powell, AZZ and regional switchgear shops. Hyperscale Power (March 2026) and other new entrants. The incumbents are capacity-constrained rather than absent.

**Moat.** Low for assembly (it is a factory); moderate for the marketplace if it becomes the venue of record. Speed of delivery is the product.

**What kills it.** OEM capacity lands in 2027–28 and lead times normalize by 2029–30, collapsing the premium. Section 232 tariffs on steel (50%) and copper (50%). As an assembler you inherit your suppliers' lead times on breakers, bushings and electrical steel. Capital intensity: $20–60M for a plant.

**Recommended shape.** Start with the marketplace and certification service (low capital, immediate), use the order flow to justify the assembly plant only with take-or-pay orders in hand, and plan to be through the capex payback before 2029.

---

### Tier 2: strong pull, but dependent on one regulatory or market mechanism

---

#### Idea 5. Large-load curtailment compliance and settlement platform

**One line.** The utility-facing telemetry, dispatch verification, settlement and audit layer that lets a colocation operator, neocloud or enterprise data center satisfy curtailment conditions (Texas SB6 30-minute shed, PJM non-firm transmission, SPP conditional service, MISO fast-track, AEP and Dominion tariffs) and get paid for demand response, with battery and generator controls so the site honors curtailment without touching workloads.

**Why now, with evidence.**
- Every fast interconnection path now requires curtailability: PUCT's first SB6 order (July 2026) made a 260 MW co-located data center shed full load within 30 minutes; PJM's interim non-firm product; SPP HILL agreements in ~90 days; FERC's June 2026 show-cause orders to all RTOs.
- Duke's study: 76–126 GW of headroom at 0.25–1% curtailment. Google has 1 GW of demand response embedded in its contracts. ERCOT flagged 3,200 MW of load at risk of tripping on disturbances, so ride-through compliance is a real engineering deliverable.
- The value of speed is enormous: at $140–200/kW-month lease revenue (TeraWulf/Anthropic and Applied Digital contracts), a 100 MW site earns roughly $15–20M per month, so 12 months earlier is on the order of $200M.
- Emerald AI ($150M at $1.05B, August 2026) targets hyperscaler workload orchestration and has five demos. The AI Energy Management Alliance (Google, Nvidia, Emerald, Camus, GridUnity, Voltus, Constellation, NRG, Anthropic; September 2026) will standardize protocols. The non-hyperscaler operator who cannot rewrite schedulers, and the compliance function utilities require, are the wedge.

**Who pays.** Data-center operators (speed to power), utilities (compliance verification), possibly RTOs.

**Competition.** Emerald AI (workload layer), Voltus, CPower and Enel X (DR aggregators), Camus and GridCARE (utility side), Schneider and Eaton power-management systems, Verrus (battery-first data centers). Crowding risk is medium-high.

**What kills it.** The alliance bundles compliance into its standard within 18 months; SB6's final rule (due 31 December 2026) softens curtailment; FERC's jurisdictional fight ends with a federal standard that favors incumbents' products. The advantage is time-boxed.

**Capital.** $5–10M. Move fast; this is a 24-month window.

---

#### Idea 6. On-site generation permitting and compliance as a fixed-scope product

**One line.** A firm that bundles air permitting (PSD/Title V), gas-pipeline lateral permitting, water rights, emissions-control packaging (SCR and oxidation catalyst specification, dispersion modeling) and community-benefit agreements into a fixed-scope, fixed-timeline package for 50 MW–1 GW behind-the-meter gas and fuel-cell projects, with software for state-agency application templates.

**Why now, with evidence.**
- Oracle sent a force-majeure notice on its 2.45 GW New Mexico Stargate campus on 24 September 2026 because the gas pipeline slipped ~6 months on permit denials and a Bloom fuel-cell air permit is pending. Chips and capital were not the problem.
- xAI ran 27 unpermitted turbines in Memphis, drew a Clean Air Act suit, and needed a year to get 41 permanent units permitted in Mississippi.
- Data Center Watch: 75 projects / ~$130B blocked or delayed in Q1 2026, 843 opposition groups in 49 states, more than 100 local moratoria by mid-2026. Opposition is bipartisan.
- Latitude estimates 25–33% of incremental data-center demand through 2030 will be behind the meter. Rabobank puts BTM gas at $100–165/MWh versus $90–95 grid, so a permit delay is expensive on both sides.
- Paces and Transect (funded siting and NEPA-screening startups) do not cover Clean Air Act permitting or NRC Part 51 environmental reports.

**Who pays.** Data-center developers, bridging-power fleet operators (VoltaGrid, ProEnergy, Solaris), hyperscalers, utilities building for data centers. Budgets are large because delay costs are tens of millions per month.

**Competition.** Trinity Consultants, ERM, Ramboll, Burns & McDonnell, Kimley-Horn and environmental law firms. Strong, capacity-constrained and hourly. The product is speed, standardization and performance-linked fees.

**What kills it.** A deep AI-capex cut removes the projects (this idea fails the AI-bust test). Moratoria spread faster than permits. Incumbents productize. It is a services business with a real but bounded ceiling.

**Capital.** $2–5M.

---

#### Idea 7. Nuclear construction-execution software

**One line.** Software built for the FOAK nuclear construction problem: design-completeness and drawing-hold risk scoring per work package before first concrete; module-fabrication QA with weld traceability, welder identity, digital travelers and non-conformance linkage; and an integrated schedule tied to Part 52 ITAAC, NRC inspection windows and N-stamp delivery dates.

**Why now, with evidence.**
- DOE Liftoff's decomposition of Vogtle's ~$15,000/kW says eliminating rework and delays is the single largest FOAK-to-NOAK lever (index ~65 versus ~35 for design standardization). Vogtle carried 180+ license amendment requests against its design certification. INL's nine lessons are, in order, finalize design, constructability review, real integrated schedule, contractor QA, risk assessment.
- Lake Charles failed on paperwork and identity, and the NRC found an inadequate QA program at the module facility "reducing the expected schedule advantage." Holtec (Camden), BWXT (bought Precision Components, July 2026), Blue Energy (shipyard) and Sheffield are ramping factories with the same exposure.
- nPlan (750,000 historical schedules) is at Sizewell C but was built for rail and highways. a16z's Big Ideas 2026 explicitly asks for factory-built reactor and data-center construction tooling. The five DOE AP1000 SPVs need component-level tracking and escrow-milestone verification.

**Who pays.** EPCs (Bechtel, Kiewit, Hyundai E&C, Fluor), module fabricators, owners (OPG, TVA, utilities), the DOE SPVs. Few buyers, large contracts.

**Competition.** Procore, Autodesk, Bentley Synchro, Hexagon (generic), nPlan (schedule), Forged Operations (quality), Palantir via The Nuclear Company, and vendors' in-house tools.

**What kills it.** Too few projects break ground. By 2028 the credible list is Darlington, Kemmerer, Hermes 2, Clinch River, possibly Palisades SMR and the first AP1000 vehicle. That is a customer base of under ten. Sales cycles are long and Bentley or Hexagon can bundle. Hedge by selling the module-QA product into data-center prefab (Schneider, Compass, Vertiv) and shipyards, which have the same weld-traceability problem at volume.

**Capital.** $5–15M.

---

#### Idea 8. Utility-side large-load intake and forecast validation

**One line.** The system of record for a utility's or RTO's large-load requests: identity, credit and site-control verification, cross-utility duplicate detection, realization scoring, take-or-pay tariff contract administration, and regulator-facing forecast audit reports.

**Why now, with evidence.**
- Camus's CEO: "five to 10 times more interconnection requests than data centers actually being built." One utility saw ~30% of 2024 load applications cancelled; the same project is bid into multiple utilities. Grid Strategies says utility forecasts are overstated by ~25 GW. PJM cut 4.4 GW after stricter vetting.
- 23 states have approved large-load tariffs; AEP Ohio's 85% take-or-pay is "weeding out uncommitted load"; Dominion GS-5 takes effect January 2027; Virginia now mandates review of Dominion's forecasting; FERC's show-cause orders required generation-adequacy reports within 30 days.
- GridUnity says transmission owners handle these processes in spreadsheets. GridUnity itself covers generator queues, not load.

**Who pays.** Utilities (rate-recoverable), RTOs, state commissions and consumer advocates (forecast audits).

**Competition.** GridUnity (likely to extend to load), Enverus (Pearl Street), Camus, utility CIS vendors, and consultancies (E3, Brattle) for audits.

**What kills it.** Utility sales cycles of 18–36 months and "death by pilot" (Heatmap, March 2026). FERC asserts jurisdiction and standardizes, which could route procurement through RTOs. Pearl Street's outcome (acquired by Enverus after raising ~$4M) shows how a good product in this lane gets absorbed if under-capitalized.

**Capital.** $5–10M and patience.

---

### Tier 3: bold, capital-intensive or timeline-dependent, but a monopoly if right

---

#### Idea 9. HALEU deconversion and >5% UF6 transport packaging

**One line.** The first US commercial capability to deconvert high-assay low-enriched uranium from UF6 to oxide or metal and to ship it in licensed Type B packages above 5% enrichment.

**Why now, with evidence.**
- Clean Air Task Force (October 2025) and the Nuclear Scaling Initiative (March 2026): no US commercial HALEU deconversion, no licensed transport packages for UF6 above 5%. NSI calls this "the lead time to the lead time."
- Enrichment is funded ($2.7B DOE awards to Centrus, General Matter and Orano; Centrus's 6,000 kg/yr cascade from 2029). Russian LEU waivers end 1 January 2028. TRISO-X opens in 2028. Standard Nuclear's backlog jumped to $577M on microreactor fuel. Radiant signed the first binding commercial HALEU offtake with Urenco. Four DOE-authorized microreactors went critical by July 2026 and the Army awarded up to $2.2B for base microreactors.

**Who pays.** DOE (HALEU Availability Program), enrichers, fuel fabricators, reactor developers.

**Competition.** Framatome/Orano, BWXT (defense deconversion), Centrus (could integrate), GLE. None has announced a commercial HALEU deconversion line.

**What kills it.** Microreactor demand slips again and HALEU volumes stay at a few tonnes a year, too small for a plant. A Part 70 facility license takes three or more years and $50–150M. Part 71 package certification is slow. DOE funds an incumbent instead. This fails the SMR-slip test; it is here because if HALEU demand materializes at all, the winner has a monopoly on a mandatory step.

**Capital.** $50–150M plus DOE cost share. A project-finance play, not a seed round.

---

#### Idea 10. Sub-150 MW bridging power fleet

**One line.** A fleet of reciprocating engines and small aeroderivatives leased on 3–7 year bridges to colocation and enterprise sites in the 20–150 MW range that VoltaGrid, Solaris and ProEnergy do not serve.

**Why now.** Rabobank: BTM gas at $100–165/MWh versus $90 grid; ProEnergy sizes bridges at 5–7 years; recips ship in 8–24 months versus 3+ years for turbines; Blackstone put $1B into VoltaGrid; Solaris financed at 7%. The anchors are 500 MW+; the 20–150 MW colo and enterprise tier lacks a fleet operator.

**What kills it.** Engine supply is spoken for (Caterpillar deliveries observed at up to ~46 months; INNIO's 1.5–2.3 GW went to VoltaGrid). Pipeline and air permits (Idea 6 exists because of this). Turbine lead times normalize around 2029–30 and strand the fleet unless contracts are long. A deep AI-capex cut removes the tenants. Capital of roughly $2M/MW means $200M for a 100 MW fleet.

**Recommended shape.** Only with an infrastructure-fund sponsor and engines under contract. Not a startup in the venture sense.

---

#### Idea 11. Load-commitment and FOAK overrun risk transfer

**One line.** Specialty underwriting (as a managing general agent with a reinsurer) for two exposures nobody insures: a developer's take-or-pay exposure under large-load tariffs (AEP Ohio 85% for up to 12 years, Dominion 85%/60%, Georgia 15-year minimums with collateral), and construction-overrun cover for 50–300 MWe nuclear projects, which DOE Liftoff explicitly lists ("overrun insurance") and which TerraPower had to source from Hyundai's balance sheet instead.

**What kills it.** Correlation: an AI bust triggers every take-or-pay claim at once. Adverse selection on nuclear overruns with almost no actuarial data. Needs a balance sheet. Slow to build. It is here because it is genuinely unbuilt and a financial-product company with the right reinsurer partner could own it.

---

## 4. What to avoid, and why

These categories are where the money and the hype are, and where a new entrant is most likely to lose.

- **A new reactor design or microreactor.** Valar ($1B at $6B), Antares ($470M), Aalo, Radiant ($300M+), Last Energy, Deep Fission, Terra Innovatum, NANO, Oklo ($3B cash), X-energy, Terrestrial, Kairos, TerraPower, plus Westinghouse's $80B government partnership. Public comps are down 40%+. BofA sees no meaningful SMR adoption before 2030–2040. No SMR is under commercial construction in the US. You would be the sixty-seventh company in a field where the capital requirement is now $300M+ and the first revenue is 2030+.
- **An AP1000 or large-LWR fleet developer.** The Nuclear Company, Blue Energy, Westinghouse/Brookfield, Constellation. Winners are decided by capital and political relationships. The Nuclear Company has not raised since May 2025.
- **A hyperscale powered campus.** Crusoe ($30.9B), Fermi America (−60%, tenant walked, lawsuit), Applied Digital, TeraWulf, Core Scientific, DayOne ($4.5B), NScale ($2B), plus Blue Owl, Brookfield, Blackstone and NextEra. Fermi is the cautionary tale: it went public on letters of intent.
- **Nuclear licensing or document-search generative AI.** Atomic Canyon, Nuclearn, Everstar, and now a free Microsoft + Nvidia permitting accelerator, INL automating safety-analysis reports, and Southern Nuclear's Copilot agents. The wedge narrowed from above within 18 months of the first startups.
- **Solid-state transformers.** Heron ($178M), Amperesand ($80M), DG Matrix ($60M), plus Siemens, Eaton and Hitachi. Years from volume and well-funded.
- **Fusion or next-generation geothermal as a developer.** Helion walked back its 2028 date; Fervo IPO'd at $10B+; XGS has Meta contracts but ~$26M raised against a $100M project. Capital-intensive and IPO-window-dependent.
- **Developer-side interconnection analytics.** Nira, Paces, Pearl Street (absorbed by Enverus), Neara, GridUnity. Crowded and already consolidating.
- **Generic demand response for data centers.** Emerald AI plus the alliance, Voltus, CPower. Only the compliance-and-settlement niche (Idea 5) is open, and only for a while.

---

## 5. Cross-cutting risks and how the picks hedge them

- **AI capital-spending cut.** Not evident today (H1 2026 hyperscaler capex $301B; Bloomberg's "half of 2026 capacity delayed" claim was rebutted on the numbers), but a 30–50% cut is the single biggest tail risk. Ideas 1, 2, 3 and 9 do not depend on data centers at all. Ideas 4, 5 and 8 are partially exposed. Ideas 6, 10 and 11 are fully exposed.
- **SMR timelines slip again.** The base case is that they do. Ideas 1–6 and 8 earn from the operating fleet, uprates, restarts, data centers and the grid regardless. Ideas 7 and 9 need new-build to happen.
- **Policy reversal in 2027 or 2029.** Nuclear is bipartisan and the credits are statutory through 2033. The exposures are the DOE loan office (sunsets 30 September 2028, and the $17.5B AP1000 commitment is conditional), the 18-month NRC deadlines (policy, not law), and NRC independence (which could swing back after an incident at a DOE-authorized pilot reactor). Ideas 1, 2, 3, 4 and 8 have no executive-branch dependency. Ideas 5, 6, 7 and 9 have partial dependency.
- **Equipment lead times normalize 2029–30.** GE Vernova will be at 24 GW/yr in 2028 and 30 GW in 2030; new transformer plants land 2027–28. Idea 4's assembly premium and Idea 10's fleet economics erode. Both should be structured to earn back capital before 2029.
- **Interest rates and tariffs.** The Fed hiked in September 2026; Section 232 tariffs of 50% on steel and copper and 15% on some grid gear persist through 2027. Capital-light services (Ideas 1, 2, 3, 6) are least affected; Ideas 4, 9 and 10 are most affected.
- **Incumbent response.** The strongest incumbents are in Ideas 3, 4 and 6 (saturated, not absent). The weakest incumbents are in Ideas 1 and 9 (fragmented or non-existent).

---

## 6. If you have to pick one

**Start Idea 1 (the supplier qualification and CGD network), and fold Ideas 2 and 3 into it as service lines within 18 months.**

The reasoning:

1. **Demand is quantified by five independent parties who do not talk to each other**: Kiewit, Zachry, the NRC's own RIC panel, the Nuclear Scaling Initiative, and DOE's long-lead program design. That is the strongest demand signal on this list.
2. **It is the only Tier 1 idea that passes every survival test.** The operating fleet, uprates, restarts and the two live construction sites need qualified suppliers whether or not a single SMR reaches commercial operation, whoever wins in 2028, and whatever hyperscalers spend.
3. **The incumbents are weak in exactly the way that matters.** Curtiss-Wright's QualTech is a division; NUPIC is a members-only utility club that new vendors cannot join; Forged Operations is early and software-only; the tier-ones will only serve themselves.
4. **It compounds.** Shared audits are a network effect, CGD evaluations are reusable IP, and the registry becomes the industry's reference dataset. Ideas 2 and 3 plug into the same customers and the same scarce people, which turns a services company into the nuclear supply chain's operating layer.
5. **It is cheap to test.** Three pilots and two hires prove or disprove it inside a quarter.

For the data-center side, the comparable pick is **Idea 5 (curtailment compliance)** if you want a software company and can move inside a two-year window, or **Idea 6 (on-site generation permitting)** if you want revenue now and accept a services ceiling. Idea 4's marketplace half is the lowest-capital way to touch the gear shortage without betting a factory on lead times that will eventually normalize.

---

## 7. Sources and method

Five research briefings, each with inline source URLs and dates, are in `research/`:

- `research/01-smr-advanced-nuclear.md`: developer-by-developer status, slips, fuel, restarts, uprates, supply-chain gaps, cost data.
- `research/02-data-center-power.md`: demand forecasts, phantom load, interconnection, bridging power, flexibility, nuclear deals, grid equipment, opposition, capital.
- `research/03-construction.md`: Vogtle and Darlington cost decomposition, modular construction evidence, workforce, QA and supply chain, construction tech, data-center and gas construction, permitting, contracting.
- `research/04-startup-landscape.md`: startup map with funding, failures, investor theses, incumbents, requests for startups, revenue evidence, crowded versus thin.
- `research/05-policy-economics.md`: federal and state law, NRC reform, loan office, data-center policy, LCOE and prices, international, risks.

Method: five parallel research passes (about 45 searches and 40 page fetches each, 2025–2026 sources prioritized, primary documents where available: SEC filings, NRC and DOE documents, Federal Register, ISO reports), followed by independent spot-checks of the hinge facts (reactor pilot program outcome, turbine backlogs, PJM auction results, transformer lead times, Part 53 status, Fermi America, Duke flexibility study, workforce figures, Heron Power, Atomic Canyon, restart status, forging capacity).

Known weak spots, flagged in the briefings: Valar's 2026 mega-rounds (secondary sources), the Army's $2.2B microreactor award (single source in one briefing, corroborated in another), SWU price (~$200, single source), Microsoft–Crane at ~$110/MWh (secondary), "fewer than 5,000 nuclear-certified welders" and "50,000 craft shortfall by 2030" (unverified recruiter and secondary claims), Bloom's Oracle and AEP figures (aggregator; Bloom's 10-K is primary for Brookfield only), and all unit-economics figures in Section 3 labeled as estimates. Mobile-turbine rental rates, secondary turbine prices, nuclear PPA strike prices, ERCOT Batch Zero classifications and demand-response compensation levels are not public and would need primary research before use in a financing document.
