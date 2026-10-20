# Repair from first principles: a meta review

*2026-10-20. 139 agents: 114 research questions, 7 claim judges, 2 cross-cutting syntheses, 3 shape generators, 1 ranker, 12 attackers (a killer and a rescuer for each of 6 finalists). Raw notes with sources for every research question are in `raw/` (114 files, about 1,640 cited URLs). Structured outputs are in `results.json`, and the two cross-cutting syntheses are in `COST_DECOMPOSITION.md` and `ANALOG_LAWS.md`.*

**Evidence caveat.** The shared web-search quota for the run ran out early. About 104 of the 114 research agents therefore worked by fetching known primary URLs (FTC, GAO, DoD IG, EU impact assessments, IATA, NREL, SEC filings, court rulings) instead of open searching. Where they could not fetch a source they used recalled figures, which they flagged. Figures marked *(recalled)* below have not been re-checked. Vendor-sourced numbers (Aquant) and advocacy-sourced numbers (PIRG) are labelled as such.

---

## Verdict

**Dhruv's chain is a good checklist, and the knowledge monopoly is real. But the evidence says it is mostly a monopoly over *permission*, not over *knowledge*. AI makes the knowledge cheap without removing the permission, so the 10x does not come from the four middle steps.**

- **Diagnosing, understanding, sourcing and delivering are typically 5-25% of a repair bill.** Engines are about 5-15%, autos 5-15%, field service 25-35%, offshore wind under 5%. Making all four 10x cheaper therefore cuts total repair cost by roughly **10-30%, not 10x**. Every measured AI intervention lands in that range: copilots give +14% on average and +34% for novices; remote assist about 15%; diagnostic AI 20-45%.
- **Most of the money and time sits in steps the chain leaves out.** These are deciding (repair, replace or defer), **authorising** (OEM software unlock, approved repair data, insurer or funding sign-off), **queueing for scarce capacity** (shop slots, dry docks, vessels, certified hands), and **whether a certified part exists at all**. A known fault can still take 250-300 days (Pratt GTF, about 700 aircraft parked). The Navy owns its yards and data and still lost 10,363 submarine days *(GAO)*.
- **Every documented 10x in repair came from a different lever:**
  - deleting unnecessary work (RCM/MSG: structural inspection from about 4M to 66k man-hours *(recalled)*);
  - redundancy and batching (hyperscalers repair for about 0.75% of capex a year against 5-15% under OEM contracts);
  - standard pre-positioned spares (RecX restored a transformer in under a week, against years);
  - a legal unlock (Deere's diagnostic tool fell from $3,160 to $195 a year, about 16x, after the FTC suit);
  - enough *verified* competitors (generics fall more than 95% once there are about 6 approved suppliers).
- **Making a part is already cheap. Getting it approved is not.** A TransDigm drive pin carried a markup of about 9,400%, which is rent, not manufacturing cost. The "AI parts factory" businesses that skipped certification went broke: Fast Radius had a 7.7% gross margin; Shapeways filed Chapter 7 in 2024; Desktop Metal filed Chapter 11 in 2025. The businesses that own approvals compound: HEICO has about 20,000 PMAs and adds about 400-550 a year, and TransDigm paid $2.2B for PMA houses in January 2026.
- **Inspection is the one claim the evidence mostly supports** (95 of 108 agents with a stance). In regulated assets, certified sign-off decides when a machine returns to service. It becomes *more* valuable as AI makes both alternative parts and forged paperwork cheap: AOG Technics put about 60,000 CFM56 parts with forged certificates into the fleet.
- **The industry is not "slop" or "built dumb". It is deliberately and rationally built to capture aftermarket rent.** Otis earns a 25.1% margin on service against 4.8% on new equipment. OEM aftermarket is 20-25% of revenue but 40-50% of profit. Deere's internal strategy was called "Control the Wrench". Rents like these are taken apart one choke point at a time, through mandates, second sources and outcome contracts. Ground-up rebuilds happened only where one owner controlled design and fleet (hyperscalers, the RCM era in aviation).

**What the evidence points at.** The company owns the **permission layer for machines the OEM has walked away from**: approvals, accepted evidence, certified sign-off and the parts pool, for orphaned and late-life fleets, with AI cutting the *cost per approval* by 5-10x. This review reached that conclusion independently, and it converges on the sibling thread's "machines immortal / HEICO for everything" shape. It sharpens that shape in three ways: **start in defence legacy platforms where the government owns or can compel the data; sell repair before new-make; and make the product cost per approval, not making parts.** The best finalist is the **Approval Factory** (about 15.5/25 from the killer and rescuer), with **Loopback Depot** (orphan defence electronics, 15.25) as its natural second line. The cheapest first test costs about $50k and takes 6-8 weeks (see the end of this memo).

---

## 1. Claim by claim

| # | Dhruv's claim | Verdict | Agent tally (stances) | What the evidence actually supports |
|---|---|---|---|---|
| C1 | Every repair runs notice → diagnose → understand → source → deliver → repair → inspect | **Mixed** | 92 mixed, 5 support, 1 contradicts | The functions are universal, but the order is not. High-value assets run on schedules, loops and swap-now-repair-later. Most of the time sits in steps the chain omits: **decide, authorise, queue for capacity**. First-time fix is about 77% (each failure brings about 2.5 more visits). No-fault-found is 14-60% of removals |
| C2 | Inefficiency comes from a knowledge monopoly | **Mixed** | 24 support, 84 mixed, 6 contradict | About 100 of 114 agents agree OEMs capture repair value. About 90 say it is enforced by **rights, keys, approvals, contracts**, not by what independents understand. Missing information explains only **12%** of 208k failed community repairs, against 59% for parts and design |
| C3 | With AI, the knowledge gap is gone | **Contradicted** | 110 contradict, 4 mixed, 0 support | AI collapses *codified* knowledge (GPT-4 alone scored 92% on clinical vignettes against 74-76% for physicians; novices +34%). It does not touch rights, cryptographic locks, sign-off, missing sensor data, tacit skill or capacity. Where AI diagnosis works at scale, it runs on **proprietary fleet data** (Bluon: generic AI 11% on replacement parts against 95% on its own 18M-job graph), so knowledge is re-enclosing |
| C4 | The four middle steps drop 10x, so all repair gets far more efficient | **Mostly contradicted** | 61 contradict, 52 mixed, 0 support | The four steps are 5-25% of cost, so the ceiling is 10-30% off direct cost. The big prize is **downtime** (often 70%+ of the loss), and it falls 10x only with non-information levers: verified competitors, pooled spares, redundancy, redesign, legal unlocks |
| C5 | Bespoke making of a specialised part is solved | **Contradicted** | 74 contradict, 9 mixed, 0 support | Making works for non-critical, low-volume, obsolete parts: Deutsche Bahn has printed 100k+ parts and cut lead times from months to days; a C-5 part cost $300 against a $10k quote. That is about 5-10% of a spares catalogue. For anything certified, the gate is **qualification, provenance and data rights** (A-10 rewing about $1.7B over 5+ years; FOGBANK about 5 years and $92M) |
| C6 | Inspection stays essential and must evolve for AI | **Mostly supported** | 95 support, 12 mixed, 1 contradicts | It is the return-to-service gate in every regulated sector, and the certified workforce is ageing (44% over 60). As a cost line it is often small (about 1% of offshore wind OPEX), but it decides timing and liability. "Evolving for AI" is real but early (EASA NPA 2025-07, ASNT NDE 4.0) |
| C7 | The industry is built to be inefficient and needs a rebuild | **Mixed** | 7 support, 4 contradict, 103 mixed | It is built for **rent capture at specific choke points**, not for stupidity. Execution gaps *within* the same structure are larger than the structural ones: cost per service event is $688 for leaders against $5,706 for laggards. Mature sectors improved without a rebuild: US nuclear outages fell from about 100 to about 30 days and capacity factor rose from 60% to 93% |

### Where Dhruv is right
1. **OEMs do capture repair.** F-35 sends 73% of components back to the OEM, even though government depots repair about twice as fast once enabled (72 days against 141). 91.8% of biomedical technicians have been denied service information. 84% of independent auto shops call data access their top issue. Deere's documents show the lock was deliberate.
2. **The knowledge-cost collapse is real for codified knowledge.** Brynjolfsson et al. found a 34% gain for novices. An LLM interpreted ultrasound error codes with 100% precision. Meta's GPU fleet needed a human in only 3 of 419 failures.
3. **Inspection is the gate and must change.**
4. **Orphaned machines are a real, growing pool.** OEMs walk away 8-16 years into a frame's life, and 10-15-year electronics sit inside 30-40-year assets.

### Where the evidence contradicts him
1. **Knowledge is never the last lock.** In 15 of the 18 historical cases where a repair or knowledge monopoly broke, the trigger was a change in **law or the standard of proof**, not knowledge spreading. Printed trade secrets appeared in 1555, and French guilds fell only in 1776-91. Public listings did not move real-estate commissions for about 20 years. YouTube came *before* the shrinking of DIY auto repair.
2. **The airplane example.** AOG time is mostly waiting for parts: an estimated 50-70% at outstations and over 90% for engine groundings *(estimates)*. Diagnosis and OEM disposition are hours to days, and engine labour is only 5-15% of a shop visit. The "send a team, send it back" loop is real, but it is not where the days go.
3. **The bespoke-part step.** See C5. The scarce layer is approval throughput: HEICO's roughly 500 approvals a year set the pace, not machine time.
4. **"Efficient repair makes everything efficient."** Cheap knowledge raises volume more than it cuts total cost (Jevons). Apple's $29 batteries did 11M replacements against 1-2M expected. Collision repair cost rose 63% *after* data opened. The scarce input becomes hands and capacity.

---

## 2. Where repair time and money actually go

Full tables are in `COST_DECOMPOSITION.md`. The key distinction is between **S-search** (finding and buying a part, an information cost) and **S-exist** (whether a certified part exists and what rent it carries). Almost all of the parts money and parts waiting is S-exist.

| Domain | Biggest cost | Share held by the four middle steps | Ceiling if they get 10x cheaper |
|---|---|---|---|
| Aero engines (about 52% of $104-119B MRO) | Materials and OEM piece parts, 75-95% of shop-visit cost | About 5-15% | About 5-13% |
| Avionics and defence electronics | No-fault-found removals: 30-60%, over $2B a year at DoD | About 30-50% | **About 25-40%** (the one place diagnosis drives the flow) |
| Auto | Labour, 48-57% at $186/hr | About 5-15% (data "tax" about $3.1B, under 1%) | About 5-12% |
| Field service and HVAC | Failed visits: 25% of cost at the median; 40% of returns are parts not on the truck, 27% wrong diagnosis | About 25-35% | About 15-26% |
| Industrial plants | Downtime ($100B of $119B US losses is lost sales); wrench time is only 25-35% | About 20-30% of labour | About 10-25% |
| Ag and trucks | Downtime waiting for a dealer tool, about 70% of harm *(PIRG)* | Up to 70% *if authorisation counts* | 30-60%, but **only with legal access** |
| Offshore wind | Vessels and lift, about 78% of OPEX | Under 5% | Under 5% |
| Transformers, nuclear, shipyards | Lead times of 80-210 weeks and capacity | Hours against years | Under 5% |
| Data centres | Already solved by redundancy (0.75% of capex) | — | — |

---

## 3. What every camp says

| Camp | Core view (sources in raw notes) |
|---|---|
| **Regulators** (FTC, EU Commission, Copyright Office, GAO) | The FTC found 8 restriction types and "scant evidence" for OEM safety claims (v01). EU impact assessments blame repair price against new goods, hassle and design ahead of information, and model only a 2-21% rise in repair take-up (v02). GAO has documented DoD data-rights gaps for about 30 years (v10, q03) |
| **Courts** | Kodak (1992) recognised aftermarket monopolies, but plaintiffs mostly lost afterwards. SIS v Intuitive was revived in Aug 2026. FTC v Deere ended in a 10-year compelled-access order in Jul 2026 (v08, v04) |
| **Right-to-repair campaigners** (iFixit, Repair.org, PIRG, Restart) | The lock is parts, pairing and software. Their own data show information is about 12% of failures (v07, u04) |
| **OEM executives and consultants** (GE, RR, Otis, Bain, McKinsey) | The aftermarket is the profit engine: services are 60-77% of segment revenue in heavy-asset OEMs. Outcome contracts (TotalCare) align OEMs with durability (o01-o04) |
| **MRO and field-service operators** | Turnaround is set by piece parts and capacity. 80% of MROs name piece-part availability as the top cause of longer turnaround (m01-m14) |
| **Insurers** (HSB, FM Global, IMIA) | Insurers drive inspection. IMIA says no independent qualifier for non-OEM parts exists (i04, e01) |
| **Investors and PE** | Roll-ups of HVAC, collision, fire and MRO earn returns on density and pricing, not on knowledge. Horizontal predictive-maintenance platforms (Predix, Uptake, C3) largely failed (x02, x03, x07) |
| **Academics** (Nowlan & Heap; Orr *Talking About Machines*; credence-goods literature; Vinsel & Russell) | Most failures are not predictable from age. Repair knowledge is social and tacit. Overcharging comes from information asymmetry, adding 5-15% (n02, u05, z05, z06) |
| **Contrarians** (steelman for OEM control) | Real points on emissions tampering and liability. Accidents (Alaska 261, Aloha 243) happened *with* the right knowledge in the manual (k01, k02, u03) |

---

## 4. History: eight laws for who wins when AI makes repair knowledge abundant

Full case table (18 cases, from guilds to shanzhai) is in `ANALOG_LAWS.md`.

1. **Knowledge is never the last lock.** Rent moves to permission: the right to install, sign, pair or connect.
2. **Monopolies fall when the standard of proof changes,** which takes months with a legal shock and decades without one. The biggest AI-era event will be a regulator accepting an AI-built equivalence package, a "bioequivalence for parts".
3. **The leveller does not keep the value.** Haynes sold for £114.5M while AutoZone earns about $2.4B a year. Stack Overflow questions fell 78%. Protolabs' operating margin went from about 20% to 5%.
4. **Price falls with the number of *verified* entrants.** One approved alternative takes about 30-40% off; about six take off more than 95%. Unverified abundance produces counterfeits instead (GAO's sting got 16 bad parts out of 16).
5. **Abundance creates a trust deficit,** so verification becomes the scarce layer, and then it gets attacked (Ranbaxy, AOG Technics).
6. **Incumbents re-lock and buy the breakers:** IBM bought PSI; TransDigm bought PMA houses for $2.2B; Caterpillar bought remanufacturers.
7. **Cheap knowledge raises volume (Jevons),** so value goes to certified hands, shop slots, rotable pools and uptime contracts.
8. **Independents win at the end of the lifecycle,** not the frontier. Examples are FTAI on 25-year-old engines, the roughly 40 CFM56 shops, Rochester Electronics, and orphaned inverters.

**Against the sibling thread's hypothesis:** "the monopoly migrates and the leveller doesn't keep the value" is strongly supported across all 18 cases. The orphan-parts house is supported. The "30-70% of OEM price" law is right only where approvals are rationed: price depends on the number of entrants, and AI that raises approval throughput could push it lower.

---

## 5. Company shapes: 15 proposed, 6 finalists, each attacked twice

Three lenses each proposed 5 shapes: own the scarce layer; AI-native operator; break the binding chain step. A ranker merged them into 6 finalists. Each finalist was then attacked by a *killer* agent and a *rescuer* agent, which scored it 1-5 on novelty, TAM, AI leverage, defensibility and feasibility. **The scores are harsher than the sibling thread's rubric and are not directly comparable to its 19/25.**

| Rank | Shape | Killer / Rescuer (of 25) | What it owns | Biggest killer | What lets it live |
|---|---|---|---|---|---|
| 1 | **Approval Factory**: AI-native approval house for sole-source and orphaned parts | 15 / 16 | Regulator-granted approvals (SAR, PMA, DER repairs) and a coupon-built allowables database | Government reviewers are the clock; DLA SARs are not exclusive, so there are no HEICO margins on that wedge | One regime for 3+ years, defence first. Get *paid to produce* TDP/SAR packages (depots, RSO, SBIR, 10 USC 3243 testing reimbursement). Win the long tail HEICO skips because it does not pay back engineering hours. Packages are human-signed, produced at machine cost |
| 2 | **Loopback Depot**: AI-native depot that eliminates no-fault-found removals in orphan defence and aviation electronics | 14.5 / 16 | Part 145 and DoD repair-source authority, accepted reconstructed TDPs, serial histories, rotable pool | Return-to-service needs data it does not have (OEM CMMs); the 50/50 depot law; prime-contractor IP | Skip F-35 at first. Buy a small legacy-avionics Part 145 shop. Partner with an organic depot under 10 USC 2474 so the work counts as organic. Work only where the government owns or has lost the data. Charge per triage plus an outcome premium |
| 3 | **Signet**: liable AI-native inspection and release authority | 15 / 15 | The accountable signature, method qualifications to POD standards, condition history | US boiler inspection is bundled free with insurance; independence rules forbid an inspect-then-repair funnel; Gecko owns capture | A neutral, robot-agnostic review and release body ("UL for AI-NDT") for owner-user pressure equipment (API 510/570/653, HRSGs). Priced per outage-day saved. Buy a small accredited inspection body |
| 4 | **Provenant**: provenance and equivalence authority for parts | 13.5 / 16 | Provenance graph, forgery corpus, lessor mandate | Regulators will not hand release authority to a private certificate authority; thin-tool trap (ProvenAir, FLYdocs) | "Carfax plus escrow for engine life-limited parts": buyer- and lessor-paid forensic trace dossiers, written into lease return conditions |
| 5 | **Late-Frame Turbine House**: independent owner-operator for mature gas turbines | 13 / 15 | Approved repairs, teardown feedstock, exchange pools, uptime contracts | ProEnergy and FTAI own the aeroderivative data-centre wedge; pools need $50-150M | Asset-light orphan-frame repair house (6B, Frame 5, W251/501D, old LM2500). **Repair before new-make.** Insurer-facing dossiers. This matches the sibling's re-ordered plan, step 1 |
| 6 | **Last Resort Power Depot**: service operator of last resort for orphaned inverters and BESS | 12.5 / 15 | FFF board library, refurbished pool, re-certification packs | Repowering is cheaper than repair; UL 9540 and fire-authority gates | A narrow "HEICO for power electronics" serving 20-40 orphaned central-inverter and PCS platforms. Sells where a like-for-like swap avoids interconnection re-study |

**Rejected:**
- *Grid recovery fleet / Gridstock* (pre-positioned standard transformers): the only shape with a demonstrated 10x (RecX), but it is capital-heavy, AI is secondary, and it fits infrastructure finance, not venture.
- *Fieldrun* (a multi-brand heavy-equipment uptime operator riding the Deere order): density and labour with no moat, and OEMs re-lock at telematics.

### The convergence
Shapes 1, 2, 5 and 6 are one business in four installed bases. Each owns **the approval, evidence and parts pool for an orphaned or late-life fleet**, and uses AI to cut the engineering cost per approval enough that the long tail becomes worth serving. Shapes 3 and 4 are the trust layer that business needs and would otherwise rent. This is the sibling thread's "HEICO for everything" arrived at from the repair literature, with three amendments:
1. **Enter through defence legacy platforms** (C-130, KC-135, H-60, A-10 avionics and spares), where the government owns or can compel the data. That removes the OEM-litigation killer, and the buyer pays for the package itself.
2. **Sell repair and approval packages before new-make parts.** Casting capacity and superalloy queues hold up new-make; braze, weld, coating and board repair do not.
3. **The KPI is engineering hours and reviewer hours per approval.** If AI cuts that 5-10x, parts selling 50-500 units become worth approving. That is the long tail HEICO and the depots skip, and the reason the business exists.

**Novelty, stated plainly.** Approval houses exist (HEICO, TransDigm's PMA units, Chromalloy, depot reverse-engineering cells, Physna for geometric search). Nobody is selling *cost per approval* as the product across the defence long tail. What is new is the throughput curve, not the category.

---

## 6. Cheapest first test (Approval Factory, about $50k, 6-8 weeks, no lab)

1. Pull DLA DIBBS award history for C-130 and KC-135 sole-source items coded AMSC C/D/P. Rank the 30 with the largest price spikes multiplied by demand value, and confirm what each code means for data rights.
2. Buy surplus units of 5 of them. Run AI-assisted reconstruction with outsourced CT to produce SAR-ready technical data packages.
3. Have a retired ESA engineer or DER review the packages. Log engineering hours against the usual roughly 300-1,000 hours per package.
4. Submit at least 2 real SARs. Pitch the packages to one Air Logistics Complex reverse-engineering office or the Rapid Sustainment Office for a paid follow-on.

**Kill criterion:** if AI does not cut engineering hours per accepted package by at least 3x, the cost-per-approval thesis fails, and the company is just another approval shop.

**Parallel cheap checks for the second lines:**
- *Loopback:* 12-24 months of removal records for one high-NFF LRU family, plus 20-30 repeat-NFF units on a rented intermittent-fault bench.
- *Turbine house:* 25 interviews with out-of-LTSA 6B, 7EA and W251 owners, plus two insurer letters on what evidence would make them accept a non-OEM repair.

---

## Files
- Page: https://claude.ai/artifact/8RTHub6xS7WuPpVfcs89XZ
- `MEMO.md`: this memo
- `COST_DECOMPOSITION.md`: stage-by-industry cost and time tables
- `ANALOG_LAWS.md`: 18-case history table and the eight laws
- `results.json`: all structured outputs (114 research summaries with per-claim stances, 7 claim verdicts, 6 finalists, 12 attacks)
- `raw/*.md`: full research notes with sources for each question (ids in `results.json`)
