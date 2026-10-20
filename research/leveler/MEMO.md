# AI as the knowledge leveller for hardware: attack and survivors (20 Oct 2026)

**The ask (Dhruv, 20 Oct 2026):** the world needs a lot of infrastructure, and AI is the great knowledge leveller. So every part should become more generic and higher quality. AI made software widespread; it should break the technical barrier to hardware the same way, with safety as the control. "Through the advent of AI, there should be nothing monopolistic." Understand it, attack it, and find what survives.

**Inputs.** The earlier deep check on the parts-approvals house is `research/firstp/deep_parts_house.md`, on branch `claude/first-principles-87923l`. It scored 16/25, and it is not redone here. This memo adds three things:
- attacks on the general claim;
- new research on where the approval gate shrinks;
- a census of the US gas-turbine fleet from EIA-860 (2025 file), run with `eia860_ct_census.py`.

Scoring uses the V5 rubric: N numbers, T time, C ceiling, A AI-answers-the-killer, D defensibility. Each leg is 1-5; a pass needs 19 with no leg below 3. The frame is optimistic, per rule 8.

## Verdict

1. **The general claim fails as stated, and the reason is specific.** Hardware monopolies are not held by knowledge. They are held by four other things:
   - **permission**: approvals, data rights and certification;
   - **evidence**: test history, flight hours, equivalent operating hours (EOH);
   - **installed base and contracts**: long-term service agreements (LTSAs), lessor rules;
   - **scarce physical capacity**: castings, foundries.
   
   AI levels knowledge for everyone at once: HEICO, AMCA, Hadrian, and the Army's own depots. A company that only levels knowledge earns tool margins, and its gains go to whoever holds the permission and the machine.
2. **A sharper version survives.** *AI makes the knowledge to build a part nearly free, so profit moves to whoever holds the permission and owns the machine the part goes into.* The company to build is one that **is its own approver**. That rules out selling approvals to DLA, the FAA or OEMs, because their queues are 60-80% of the clock and AI does not touch them.
3. **There are three places where the approver is inside the company.**
   - **(a) You operate the fleet.** Your gate is your insurer.
   - **(b) Nuclear commercial-grade dedication.** The dedicating entity and the plant approve. There is no NRC review up front.
   - **(c) An FAA ODA with PMA authority.** You earn it in 2-4 years or buy a company that already holds one.
   
   All three are sourced in §3.
4. **Best survivor: a "resurrection fleet", 20/25 on paper (N4 T4 C5 A4 D3).**
   - **What it does:** buys old or poorly supported gas turbines cheaply, keeps them running with a parts library it reverse-engineers with AI, and sells firm power.
   - **The gap it exploits:** old heavy frames are listed at about **$83-110/kW**. A new turbine costs **$790-1,800/kW** and has a 3-6 year wait.
   - **The fleet:** the US has **988 simple-cycle gas turbines 30 or more years old (45.5 GW)**, held by 288 owners (EIA-860 2025).
   - **Proof the market values this:** FTAI Power holds a $1.465B hyperscaler order, and ProEnergy is reportedly exploring a $40-50B IPO.
   
   This is the Terranox shape outside minerals:
   - public data (EIA-860) names every unit;
   - AI makes the "orphan" unit supportable;
   - the company buys the asset others cannot keep running;
   - it owns the running megawatts.
5. **The parts-approvals company as first briefed stays at 16.** It becomes the parts arm of the fleet rather than the company itself.

## 1. The claim, stated so it can be attacked

Dhruv's claim has three parts:
- (i) AI collapses the cost of the knowledge needed to design, reverse-engineer and substantiate a part.
- (ii) Once that cost collapses, sole-source positions should dissolve, and parts get cheaper and better.
- (iii) Safety can be held constant by doing the work rigorously.

(i) is close to true already:
- The Army's Corpus Christi depot scanned, reverse-engineered and validated a Black Hawk tank fin in 43 days for about $3k, against $14k from the vendor ([Breaking Defense](https://breakingdefense.com/2025/10/dont-be-surprised-if-army-starts-3d-printing-its-own-parts-materiel-command-head/)).
- The earlier check estimated AI cuts PMA engineering from about $100k to $40-60k per part.

The attacks below are on (ii) and (iii), and on who captures the value.

## 2. Attacks on the general claim

| # | Attack | Evidence | Effect | AI-leveraged answer |
|---|---|---|---|---|
| A1 | **Knowledge is not the moat.** Most monopoly parts are simple. | TransDigm earns ~54% EBITDA on parts a job shop could make. The DoD IG found markups of 17-4,451%. Reverse-engineering a lawfully bought part is legal under the Defend Trade Secrets Act ([18 U.S.C. §1839(6)(B)](https://www.law.cornell.edu/uscode/text/18/1839)). The knowledge was never the barrier; the approval and the installed base were. | **Wounds.** Cheap knowledge alone moves no parts. | Aim the AI at the *evidence package*, not the design, and go where you hold the approval (§3). |
| A2 | **Levelling helps incumbents too.** | HEICO, AMCA ($1B valuation, AI qualification plus six factories), Hadrian ($7.87B; Red River Army Depot award with data rights, $80M ceiling, [army.mil](https://www.army.mil/article/291165)) and Army depots that approve their own parts under AR 750-1 all get the same tools. | **Wounds** a tool or service company. The edge lasts 2-4 years. | Own the output (approvals plus the machine), not the tool. |
| A3 | **Generic means the price collapses, and "nothing monopolistic" contradicts the profit.** | The second source at PSM cut GE 7FA part prices 60-70% ([DOJ 2015](https://www.justice.gov/atr/case-document/file/768396/dl)). HEICO earns by being one of two sources per part, at a 30-40% discount. | **Survives as a mission, not as a moat.** You profit during the transition, then from volume. | Be your own biggest customer (own the fleet), so a collapsing part price is a cost saving that stays with you. |
| A4 | **Safety runs through a queue you do not control.** | DLA source approval takes 12-18 months by DLA's own count ([NDIA 2023](https://ndia.dtic.mil/wp-content/uploads/2023/dla/Reverse_Engineering.pdf)). FAA approval takes 6-18 months. GAO found under 10% of DLA's reverse-engineering projects finished. No regulator uses AI to review packages, and none accepts digital evidence in place of tests yet (NRC AMT plan, NASA IMQCAM, FAA: research only). | **Kills** the "sell approvals to regulators fast" version on time. | Go where the approver is you (§3). |
| A5 | **The software analogy breaks.** Software had zero marginal cost, no gate and instant iteration. | Hot-section parts need castings with 18+ month lead times and rig tests costing $0.3-1M+. Chromalloy spent over $100M on one V2500 HPT PMA programme. | **Wounds** the hot section. Machined, fabricated and combustion parts are fine. | Start cold-section and combustion; use printed-core foundries for development castings. |
| A6 | **Demand per part is thin.** | An approved part earns ~$100-150k a year. The reachable DLA long tail is ~$0.6-1.2B, because Boeing, GE and others hold 83% of the sole-source spend. | **Wounds** size. | Be the demand: a fleet owner buys its own parts every outage, so there is no award risk. |
| A7 | **Incumbents counter.** | GE has a $43B heavy-duty gas-turbine services backlog, 70% of it with 10+ years to run. Lessors ban PMA parts. OEMs cut prices on parts under attack. TransDigm paid $2.2B for Jet Parts Engineering and Victor Sierra. | **Wounds**, but buying the attacker is also the exit. | Target units outside LTSAs: old frames and owner-operators. |
| A8 | **One failure ends you.** | FM Global clients see ~20 gas-turbine failures a year averaging ~$100M each, and blades cause over 75% of the losses ([ESD News](https://esdnews.com.au/a-new-approach-to-managing-evolving-risks-in-gas-turbine-technology/)). | **Wounds** hot-section non-OEM parts. | CT-scan every part, keep in-process records, start with combustion and cold-section parts, and give insurers a loss record, not a promise. |

**What the attacks leave.** The claim is right about the knowledge and wrong about where the money goes. Every sound attack points the same way: **hold the approval and the machine yourself.**

## 3. Where the approver sits inside the company (new research)

| Route | Who approves | Clock | Status |
|---|---|---|---|
| **Operate your own fleet** (power, engines) | You plus your insurer | Weeks per part | No regulator for stationary gas turbines. The plant owner is the approver (Turbomachinery Mag). |
| **Nuclear commercial-grade dedication (CGD) plus 10 CFR 50.59** | Dedicating entity plus licensee | Your own throughput | No up-front NRC approval; the NRC inspects afterwards and samples reverse-engineered replacements ([NRC ML19070A308](https://forms.nrc.gov/docs/ML1907/ML19070A308.pdf); [Perry inspection 2025](https://www.nrc.gov/docs/ML2516/ML25162A014.pdf)). Trap: swapping analog parts for digital ones can trigger a licence amendment. |
| **FAA ODA with PMA authority** | Your own designees | Days to weeks per part, *after* 2-4 years to earn the ODA (est.) | Real: Wencor has held one since 2009 ([MARPA](https://marpa.pmaparts.org/2009/10/05/marpa-member-wencor-latest-company-to-receive-oda-authority-from-faa/)), TIMCO holds one, and FAA Order 8100.15C came out 1 Oct 2025. AI answer to the 2-4 years: **buy a small PMA house that holds an ODA**, as the surety idea buys a shell carrier. |
| **Army depots and Navy BlueForge** (the government owns the data) | The government | Months | The depots compete with you and also buy from you. AML3D won ~US$1.84M for 5 obsolete submarine parts with Navy-supplied data ([ASX](https://announcements.asx.com.au/asxpdf/20260326/pdf/06xtqd98nvwtk6.pdf)). DLA posted a 417-NIIN mass sources-sought (Aug 2026). |
| **DLA Source Approval Request (SAR)** | DLA and the service engineering authority | 12-18 months | Unchanged. FY27 NDAA right-to-repair passed both committees, the House version with a presumption of government purpose rights, but is still in conference ([Defense Daily](https://www.defensedaily.com/hasc-approves-1-15-trillion-fy-27-ndaa-with-right-to-repair-reform/congress/)). The same provisions were stripped in conference in Dec 2025. Treat it as a binary catalyst, not a plan. |

## 4. Survivors

### S1. Resurrection fleet: own the turbines, own the parts, sell firm power. **20/25 on paper (N4 T4 C5 A4 D3), pass.**

**Shape.** Buy gas turbines that are old, idle or "orphaned": the OEM support is gone, slow or locked behind service agreements. Keep them running with an AI-built parts library that the company owns. Contract the megawatts to data centres and utilities, or sell refurbished units into the shortage. You are the operator, so the approval gate is your insurer.

**Why now.**
- **New turbines are sold out.**
  - GE Vernova holds 116 GW of gas backlog plus slot reservations (Q2 2026), and a heavy-duty unit ordered now arrives around 2031.
  - Siemens Energy has 69 GW firm and is booked to FY2028.
  - Wood Mackenzie expects turbine-only prices around $600/kW by 2027, up 195% on 2019. BNP Paribas puts heavy-duty at ~$790/kW and aeroderivatives at ~$1,800/kW ([WoodMac](https://www.woodmac.com/press-releases/gas-turbine-prices-soar-195-as-market-faces-supply-demand-crisis/); [GEV Q2](https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000147/gevpressrelease2q26.htm)).
- **Owners are already waiting on parts.** Owners of Alstom GT11/GT13 units report GE parts lead times of about 24 months, and a 25% expediting premium guarantees nothing ([CCJ](https://www.ccj-online.com/?p=22552)). Pratt FT4 operators cite hard-to-source parts.

**The mispricing (asking prices, low confidence).**

| Unit | Asking price | Price per kW | Share of new price |
|---|---|---|---|
| GE Frame 6B, 34-42 MW | $3.5-3.8M ([Genloop](https://www.genloop.energy/sell/ge-frame-6b)) | $83-110/kW | ~10% of a new heavy-duty unit |
| Used LM6000 aeroderivative | $22.6M ([SecondWatt](https://secondwatt.com/equipment/gas-turbines/ge-lm6000)) | ~$445/kW | ~25-50% of new |

Whole operating plants trade at ~50% of replacement cost (Enverus via [CESS](https://www.cess.co.uk/news/gas-turbine-demand-2026-private-treaty)).

The aeroderivative price already includes the expected value; the heavy-frame price does not. The reasons a heavy frame is cheap are support, parts and relocation, and that is the gap an AI parts library closes. This matches the cross-hunt law: the value sits where the seller cannot use the record (here, keep the unit supported).

**Fleet census (EIA-860, 2025 early release; our pull).**
- 2,666 simple-cycle gas turbines totalling 176.6 GW.
- **988 units are 30 or more years old, 45.5 GW**, owned by 288 entities. Of these:
  - 597 belong to utilities (30.3 GW), many of them co-ops and municipal utilities with thin engineering staff;
  - 254 belong to independent power producers (10.6 GW);
  - 716 are 20-120 MW.
- 167 units (6.4 GW) are out of service or on standby.
- 385 units (11.2 GW) were retired since 2015, and their fate is unknown.
- 68 units (4.35 GW) are planned to retire in 2025-32.

**Unit economics (estimates).** Take a 40 MW Frame 6B:
- Cost: buy for $3.5M, then spend $5-15M on refurbishment, balance of plant and controls, so about $9-19M all in (~$225-475/kW).
- Revenue: contracted at half of Solaris's ~$400k/MW-yr EBITDA, which comes from aeroderivative fleets ([Solaris Q2 2026](https://ir.solaris-energy.com/~/media/Files/S/Solaris-IR/press-release/sei-q2-2026-earnings-release.pdf)), it earns ~$8M a year.
- Payback is ~1-2.5 years.
- Behind-the-meter gas sells at ~$100-125/MWh ([Rabobank](https://www.rabobank.com/knowledge/d011532274-the-marathon-can-behind-the-meter-data-center-power-solutions-endure-the-decade-in-the-us); [Modo](https://modoenergy.com/research/us-data-center-onsite-gas-speed-to-power)). Even with simple-cycle heat rates around 11-12 MMBtu/MWh, fuel is ~$40-50/MWh at $3.5-4 gas.

**Ceiling.**
- FTAI Power guides $450M of Power EBITDA for 2027 from 100 converted CFM56 units ([MarketBeat](https://www.marketbeat.com/instant-alerts/ftai-aviation-q2-earnings-call-highlights-2026-07-30/)).
- ProEnergy has built 75 CF6-core packages since 2020 and is reportedly exploring a $40-50B IPO. That figure is press reporting and unverified ([Crypto Briefing](https://cryptobriefing.com/proenergy-50b-ipo-energy-capital-partners/)); ECP bought ~60% in 2024 for ~$275M.
- A 2-4 GW owned fleet at $200-400k/MW-yr is **$0.4-1.6B of EBITDA**.
- The parts library also sells to the other 44 GW of old units, and to FTAI and ProEnergy for their own feedstock.
- C = 5.

**Ladder.**
1. Sell parts and life extension to owners of old frames, for cash and to build the library. Start with combustion and cold-section parts on 7EA, 6B, 501D, GT11N and FT4.
2. Buy whole idle units and old peaker plants. The plant brings its own interconnection and air permit, which may be worth more than the turbine.
3. Own a fleet contracted to data centres and utilities.
4. Add printed-core castings for hot-gas-path parts, then a PMA/ODA house for aero cores. This is where the earlier "superalloy foundry" and "parts approvals" ideas become rungs of one company.

This is Charlie's vertical-integration-plus-software shape.

**What still bites, and the AI answers.**

| Killer | Answer | What is left |
|---|---|---|
| Supply of idle units is thin, and NRG and others are un-retiring peakers | Do not wait for idle units. Offer the 288 owners of the 45.5 GW old fleet a life-extension deal paid in a share of capacity revenue, or buy the plant. EIA-860 lists every one, with age, status and owner. | Sellers are starting to price in the hope (Enverus: 50% of replacement). |
| Aeroderivative conversion is crowded (FTAI, ProEnergy, APR Energy, Solaris) | Take heavy orphan frames, which those players do not touch, and sell them parts. | Hanwha/PSM, EthosEnergy and Sulzer already make non-OEM heavy-frame parts. The AI edge is breadth and speed across many orphan models, not being first. D = 3. |
| Insurer appetite for non-OEM hot-section parts | Start in combustion and cold section; CT plus in-process records on every part; build a fleet loss record. | Blades are >75% of losses, so the hot-gas path waits on that record. |
| Old frames are inefficient and slow to move | Run them as peaking and firm backup behind-the-meter, where speed beats efficiency. ProEnergy says bridge contracts last 5-7 years. | Batteries now beat gas turbines on cost at many data centres ([TechCrunch](https://techcrunch.com/2026/10/09/batteries-are-now-cheaper-than-natural-gas-turbines-used-at-many-data-centers/)). That caps the tail after about 2032. |

**Scores.**
- **N4:** payback ~1-2.5 years on contracted units (estimated).
- **T4:** first parts revenue in year 1 and first owned megawatts in year 2.
- **C5:** see Ceiling.
- **A4:** AI answers the "no parts, no support" killer, and the insurer gate is partly answered.
- **D3:** crowded, and the tools can be copied; the moat is fleet plus library plus contracts.

### S2. Nuclear obsolescence house (reverse-engineer and dedicate). **17/25 (N3 T4 C2 A5 D3), fail on size; a strong first rung.**
- **No NRC queue (A5).** The dedicating entity and the licensee approve, and the NRC inspects afterwards.
- **The problem is large.**
  - About 20% of plant equipment is obsolete (EPRI).
  - A plant runs on more than 100,000 parts.
  - More than 60% of nuclear-qualified manufacturers have left the market.
  
  Sources: [Reuters Events](https://www.reutersevents.com/nuclear/node/54822), [NEI Magazine](https://www.neimagazine.com/analysis/managing-obsolescence-5861125/).
- **Incumbents:** Westinghouse holds a library of ~55,000 dedication plans. Paragon claims ~$500k saved per site on an I&C case. Curtiss-Wright has a reverse-engineered relay installed under 50.59 at Susquehanna.
- **Size (C2).** No fleet-wide spend figure exists, and our estimate is under $1B a year. That is "too small" under rule 4 as a standalone.
- **Best use.** Make it the nuclear segment of S1's parts library, serving uprates, restarts and 80-year licences.

### S3. Defence second source where the government holds the data. **16/25 (N3 T3 C4 A3 D3).**
- **The customer approves its own parts.** Army depots under AR 750-1, Navy BlueForge licences and Air Force reverse-engineering multi-award contracts.
- **Contracts so far are small:** AML3D won $1.84M for 5 parts, and Hadrian's Red River ceiling is $80M.
- **Swing factor:** if FY27 NDAA right-to-repair survives conference, A and T each go up a point, for 18.
- **Best use.** A second market for S1's library and machine shops, not the wedge.

### S4. The parts-approvals house as briefed. **16/25, unchanged** (see `deep_parts_house.md`).
- New answer to its gate-time killer: buy a small PMA house that holds an ODA instead of waiting 2-4 years to earn one. That lifts A to about 4 for the FAA leg only.

## 5. The company, in one paragraph

AI makes the knowledge to rebuild a machine part nearly free. Until now that knowledge, together with the approval to use it, has kept old infrastructure dependent on the original manufacturer. The world is short of turbines until about 2031, and 45 GW of US peakers are over 30 years old. The company buys the old, under-supported machines that others cannot keep running, keeps them alive with a parts library it reverse-engineers and owns, and sells their power. Because it runs the machines, it approves its own parts, which the OEMs' regulators and service contracts never let a parts maker do. It starts with gas turbines and extends the same library to nuclear plants, aircraft engines and defence fleets. That is "nothing monopolistic", built as a business: the company still owns something. It owns the library and the fleet.

## 6. Cheapest feasibility tests (S1)

1. **Done in this pass: fleet census.** EIA-860 2025 gives 988 units, 45.5 GW, 288 owners. Next step, about a week: attach turbine model to each unit from state air permits or GADS-style public sources, so the "orphan" frames (501B/D, GT11N, FT4, Frame 5) can be counted.
2. **Owner pull, 3 weeks, ~$5k.** Make 15 calls to co-op, municipal and IPP owners of 30-year-old frames. Ask for parts lead times, prices and the parts they cannot get. Kill if fewer than 5 name a part with lead time of 12 months or more at a price above $50k.
3. **One part, 6 weeks, ~$40-60k.** Reverse-engineer one combustion part (a transition piece or liner for a 7EA or 501D) from scrap: CT scan, alloy ID, AI CAD, then a quote from a fabricator. Kill if cost plus margin is not 30% or more below the OEM or PSM price.
4. **Insurer, 2 weeks.** Talk to one turbine underwriter (FM Global or HSB) about non-OEM combustion parts with full CT and process records. Kill if they would load the premium by more than 20%.
5. **Price check, 2 weeks.** Get 5 broker quotes on used 6B, 7EA and 501D units. Kill if heavy frames actually trade above $300/kW, which would mean the mispricing is not real.

## Caveats
- One scorer. The frame is optimistic per rule 8.
- Used-turbine prices are asking prices from listing sites, not transactions.
- The ProEnergy IPO valuation is press reporting.
- Heavy-frame EBITDA per MW is assumed at half the aeroderivative fleet figure.
- EIA-860 2025 is an early release and has no turbine-model field.
- The FY27 NDAA conference outcome is unknown.
