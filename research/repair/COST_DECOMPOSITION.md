# Where repair time and money go, by stage and industry

**Legend.** Each figure carries the ids of the research notes it comes from. `[E]` marks my own estimate or inference. `[U]` marks a figure the agent recalled from memory and could not re-verify, because the shared search budget ran out for most agents.

**Stage keys.**
- N = notice
- Dx = diagnose
- U = understand (procedure, repair data)
- S = source parts. **S-search** is finding and buying the part. **S-exist** is the part's existence, price and certification.
- Dl = deliver parts
- L = repair labour
- I = inspect and sign off
- Non-chain = OEM margin, inventory, downtime

**The distinction that drives the whole answer.** "Sourcing" mixes two things.
- **S-search** (finding, quoting, ordering) is an information and transaction cost. A 10x knowledge gain can cut it.
- **S-exist** (the part exists, is certified, and has a price set by OEM rent or manufacturing capacity) is where most parts money and parts waiting time sits. A 10x knowledge gain does not touch it.

Most of the "parts" share below is S-exist.

---

## 1. Decomposition by industry

### Commercial aviation (MRO about $104-119B a year: m01, q01)

| Stage | Money | Time | Source |
|---|---|---|---|
| Mix of spend | Engines about 52% of MRO; components about 18%; airframe and line about 30% | — | m01 |
| Engine shop visit: materials and OEM piece-part repairs (S-exist) | **75-95% of direct cost**. Life-limited parts can be 50-60% of a life-limited-part visit | Piece-part availability is the top cause of longer turnaround (80% of survey respondents). Visits run 100-300+ days against a 30-60 day norm | m01, r02, o01, o03 |
| Engine labour (L, with Dx/U bundled in) | 10-15% on non-life-limited visits; 5-10% on life-limited visits (r02 corrects m01) | — | r02 |
| Airframe and line (L) | About 80% labour | Dispatch reliability is already 98.86% | r02, m01 |
| Dx (no-fault-found) | 30-60% of avionics removals turn out to have no fault. Historically about $22k per event (ATA 1995); about $20M a year for a 200-aircraft airline | NFF inflates spares pools and shop queues | m04, d03 |
| Aircraft on ground (outstation) | $10k-150k per hour (a 2008 Boeing figure, never audited) | Parts wait **50-70%** of an outstation AOG `[E]`; **over 90%** of an engine grounding `[E]` | m02 |
| U (repair outside the structural repair manual: OEM, DER or DOA disposition) | Small | Hours to days for an AOG; weeks to months for a permanent fix | m03 |
| Dl (couriers, next flight out) | Small next to the cost of AOG | Close to solved | l01 |
| I and records | NDT is roughly $11-18B globally | Gate on release. Records and trace problems (AOG Technics) | i01, i02, p02 |
| Non-chain | OEMs take 47% of the aero profit pool. Engine MRO margin 20-35%, against -5% to 10% on new engines. About $11B of supply-chain cost in 2025 `[U]`: $2.6B extra leases and $1.4B extra spares | ~350 aircraft (GTF) and ~700 aircraft parked for engine work | o01, m01, m05, l01 |

**Verdict: aviation.** Dx and U together are **at most about 5-15%** of engine cost. The NFF waste in avionics is the main exception. Time is S-exist plus shop capacity.

### Automotive (light-duty aftermarket about $414B: v05)

| Stage | Money | Time | Source |
|---|---|---|---|
| L | 48-57% of the dealer repair dollar at $186/hr; 27.3 labour hours per collision claim, and rising | Technician gap of about 20.8k a year | r02, s04, z03 |
| Parts (S-exist) | The rest, at retail markup. ADAS parts can be up to 37.6% of a collision bill | Mainstream parts arrive same day | s04, v05 |
| Dx and U | Data-access "tax" of about **$3.1B, under 1%** of the aftermarket. Unpaid diagnostic time of 2-4 hours before a dealer referral | Photo AI cut appraisal from days to minutes | v05, s05 |
| I (scans and calibration) | Scan about $157; calibration about $547 on about 30% of claims | 56% of calibrations are found late, on supplements | s04, s05 |
| Cycle time | — | Weeks overall; 37.5 days for EVs. Driven by parts, approvals and supplements | s04 |
| Fraud and opacity (Dx) | Strict fraud is about 2% of charges. Uninformed-customer premiums add 5-15%. Having an insurer pay adds 80% | — | z05 |

**Verdict: auto.** Information access was largely opened in 2013-14. The Dx and U share is a single-digit percentage.

### Heavy trucking and ag (dealer-locked)

| Item | Figure | Source |
|---|---|---|
| Ag harm | About $3B a year downtime plus $1.2B a year excess repair cost, so **about 70% is downtime** | v01, v04 (PIRG, an advocacy source) |
| Ag downtime driver | Waiting for a dealer technician with the only fully functional diagnostic tool. Hauling machines 30-60 miles. Only 6% of dealer-required fault codes say so | v04 |
| Ag labour premium | $130-200/hr, about $59/hr above independents | v04 |
| Ag downtime cost | $500-1,400 per breakdown day (ISU); $3,348 per farm per year | v04, v03 |
| Class 8 trucks | About $1,500 a day in lost revenue per truck. Direct repair and maintenance about $0.20/mile, about 9% of cost per mile `[U]` | e09 |
| Truck time | Bay queue, authorisation and parts back-orders. Coordination alone saves 1-3.4 days per event (Decisiv) | e09 |

**Verdict: ag and trucks.** This is the one domain where **Dx plus authorisation dominate time**. The lock is software permission, not knowledge.

### Appliances, consumer electronics and home service

| Stage | Figure | Source |
|---|---|---|
| Repair price ceiling | Consumers accept a repair at about 20% of new price (17-27%) | v02, q04 |
| Dx | **7-22% of common repair cost**, paid up front, which deters repair before a quote | v02, q04 |
| Call-out (L) | $75-150, about 10-25% of a mid-range machine `[U]` | s01 |
| Parts (S-exist) | Phone display about 42% of new-phone price; battery about 14%. Apple charges independents $270 for a screen it installs for $280 | v02, s02 |
| S and Dl wait | 5-10 working days for phones; up to 15 for white goods. Time and logistics each deter about 9-14% of non-repairers | v02 |
| Barriers (208k community repairs) | No parts 25%, parts too dear 18%, design 16%, **missing information 12%** | v07 |
| Home warranty | Contractor labour plus parts about 45% of revenue, about $246 per dispatch; parts about 22% of that | s06 |
| Marketplace | Angi spends about 49% of revenue on marketing | s06 |

**Verdict: consumer.** Dx and U are about 10-20% of the price. They matter most as **quote uncertainty that suppresses demand**. Apple's $29 battery programme did 11M replacements against 1-2M expected (s02, q04).

### Field service in general, including HVAC (vendor data, mostly Aquant)

| Item | Figure | Source |
|---|---|---|
| Failed visits | 25% of service cost at the median, 44-52% at the bottom, 14% at the best | m06, s03 |
| Causes of return visits | Parts or tools not on the truck **40%**; wrong diagnosis or missing skill **27%** | m06 |
| Unnecessary dispatches | 14-20% of truck rolls | m06 |
| Admin | About 18% of technician hours | m06 |
| Mean time to repair | 4.5 days median, mostly waiting between visits | m06 |
| Vendor-modelled savings from closing the knowledge gap | **10-26%** of service cost | m06, s03 |

### Industrial plants (SMRP/NIST)

| Item | Figure | Source |
|---|---|---|
| Wrench time | 25-35% hands-on. The other 65-75% is travel, parts, permits and waiting. Up to 20-30% may be diagnosis and planning (IDCON) | m07 |
| Direct spend vs losses | $57.3-74.5B maintenance spend against $119B of losses, of which **$100B is lost sales** | m07, q02, n03 |
| Spend mix | Labour about 37%; spare parts about 32% | n03 |
| Reactive share | 45-55% | m07 |
| Documented gains | 12-40% from planning, kitting and preventive maintenance | m07 |
| Downtime cost per hour | $36k (FMCG) to $2.3M (auto plant). Time to restart rose from 49 to 81 minutes | q02 |

### Industrial: energy

| Asset | Breakdown | Source |
|---|---|---|
| Offshore wind O&M ($135/kW-yr) | **Vessels and lift about 78%**; insurance about 14%; labour plus materials about 5%; inspection about 1% | m08, r02 |
| Wind time | Major component failures about 95% of downtime `[U]`. Faults are detected 5-6 months ahead | z10, m08 |
| Large transformers | Lead time 80-210 weeks (about 120 average). Dx takes hours to days. Unit costs $2-10M | e02 |
| Gas turbines | Hot-section hardware and lost margin dominate. A 2-5 day combustion inspection becomes weeks without spares. Planned-outage Dx is pre-computed | e01 |
| Nuclear | Downtime about $0.7-1.5M per day per GW. Operations about 60% of generation cost. Qualification is the long pole | e03, i05 |
| Solar inverters | 43% of tickets and 36% of lost energy. Truck rolls, manufacturer return-and-replace and lead times dominate | e07 `[U]` |

### Defence

| Item | Figure | Source |
|---|---|---|
| Lifecycle cost | O&S at least 70% of life-cycle cost; F-35 about $1.3-1.58T of $1.7-2T | q03, v10 |
| F-35 time | Not mission-capable for supply about 27%. Depot cycle 141 days at the OEM against 72 at government depots. 10,000+ components in backlog | z10, q03 |
| Knowledge friction | 60-day technical-data request loops. Part numbers held by the contractor | q03, h06 |
| Records | Missing or inaccurate data cost up to 9% of flight hours at one site | d03, h06 |
| NFF | Over $2B a year | m04 |
| Cannibalisation | 5.3M extra labour hours (FY96-00). Up to half not supply-driven (swap-to-diagnose) | z09, h06 |
| Submarines | 18,687 days and $4.17B: about 12,200 days idle waiting for capacity; 6,494 days of overrun | m11 |
| Overrun causes | Unplanned new work 4,100+ days; workforce 4,000+ days; parts second | m11 |

### Medical devices

| Item | Figure | Source |
|---|---|---|
| Service contracts | About 10% of purchase price per year on imaging | v06 |
| Downtime | About $6k/day for CT; about $15k/day for MRI | v06 |
| Labour rates | OEM $600-800/hr against independents at $150-200/hr | v09 |
| Dx | Fast. About half of faults are resolved remotely by OEMs | v06 |
| Savings from opening access | 20-40% of service spend | v06 |

### Data centres

| Item | Figure | Source |
|---|---|---|
| Repair cost | OEM on-site contracts 5-15% of equipment value per year; hyperscaler batched repair **about 0.75%** | m14 |
| Remaining time | N and isolation (silent data corruption, intermittents). 43% of returned drives had no trouble found | m14 |

### Other

| Domain | Figure | Source |
|---|---|---|
| Elevators | Labour and travel (route density) dominate; service is 91% of Otis segment profit | m10 |
| Semiconductor fabs | Downtime about $13.9M/hr company-wide (TSMC); Dx already instrumented | m09 |
| Wheelchairs | Median 7-14 days to repair, set by authorisation and vendors, not by component | s07 |
| Mining | Downtime dominates; maintenance about 30-50% of opex `[U]` | m13 |

### Non-chain cost pools (cross-industry)

| Pool | Figure | Source |
|---|---|---|
| OEM aftermarket | 20-25% of OEM revenue but 40-50% of profit; parts at about 50% gross margin | o02 |
| OEM services share | Services 60-77% of segment revenue in heavy-asset OEMs | o01 |
| Dealers | Parts and service are 10-35% of revenue but 40-64% of gross profit. PACCAR parts made $1.67B pretax against $0.87B on trucks | z03 |
| Sole-source rent | Markups up to 9,400% and 17-4,451% (DoD IG) | o05, p03 |
| PMA alternatives | Only about 30-40% cheaper | o05, p03 |
| Distributors | 30-45% gross margin | p04 |
| Inventory | 1-2 turns a year; up to 23% obsolete annually | o02, p05 |
| DoD excess inventory | 22-52% of secondary inventory value beyond requirements | p05 |
| Downtime | About $1.4T a year for the Fortune Global 500 (Siemens extrapolation) against $119B US manufacturing (NIST) | q02 |
| Business repair (macro) | About 23-28% of capex in Canada | z06 |

---

## 2. Do the four intermediate steps dominate?

**No, with three bounded exceptions.**

1. **Money.** In no domain is Dx plus U a large standalone cost line. They are billed inside labour or visit fees (r02).
   - S-search and Dl are small everywhere: aviation delivery is close to solved, auto parts arrive same day, and aircraft-parts search is cheap and digital (l01, p03, h01).
   - The big money sits in four places:
     - S-exist: OEM and certified part price, and life-limited parts (aviation 75-95%, phones).
     - Labour and truck rolls (auto, appliances, trades about 50%+).
     - Access: vessels and cranes (offshore wind 78%).
     - Non-chain downtime. This often exceeds the repair bill by 1.6x (NIST) to 2.5x (ag) to orders of magnitude (fabs, auto plants, transformers).
2. **Time.** Measured splits put waiting, not working, at the top: parts existence and lead time, capacity (docks, shops, cranes), approvals and funding, then labour (z10, m11, k03). The long poles are certified parts and capacity. Knowledge is not one of them.
   - GTF: the fault was fully understood, yet repairs took 250-300 days.
   - Navy: the service is its own OEM and shows the same delays.
   - Transformers: diagnosis takes hours; replacement takes 2-4 years.
3. **Exceptions where the four steps do dominate.**
   - **(a) Electronics and avionics NFF.** Misdiagnosis generates the parts and shop flow: 30-60% of removals, over $2B a year at DoD.
   - **(b) Dealer-locked equipment (ag, trucks, medical).** Dx and authorisation are the long pole; about 70% of ag harm is downtime waiting for the dealer. But the lock is cryptographic and legal permission, not knowledge. It is being opened by the FTC Deere order, which cut the tool price about 16x (v04), not by AI.
   - **(c) Consumer goods.** Paid diagnosis and quote uncertainty (7-22% of cost) suppress demand rather than inflating the cost of repairs that happen.

**Smaller exceptions where knowledge itself binds:**
- Tacit and plant-specific knowledge (legacy PLC code, retiring experts): e05, u02.
- Unplanned "new work" discovered when a system is opened: Navy 4,100+ days, 36% labour underestimates (m11, u02).
- Diagnosis that is wrong at scale: HVAC mis-charge, per NIST (s03).

## 3. Ceiling if Dx, U, S-search and Dl got 10x cheaper

The savings ceiling is about 0.9 × the share those four steps hold today.

| Domain | Share of direct cost held by the 4 steps today `[E]` | Ceiling on direct-cost saving | Downtime and time effect |
|---|---|---|---|
| Aviation engines | About 5-15% (inside labour) | **About 5-13%** | Small. Parts and shop slots bind |
| Avionics / defence electronics | About 30-50% via NFF knock-on effects | **About 25-40%** of component repair spend | Meaningful: fewer removals means smaller pools |
| Auto (mechanical and collision) | About 5-15% | **About 5-12%**, plus trust | Cuts supplements and late calibrations |
| Appliances and home service | About 15-30% (Dx plus repeat truck rolls) | **About 10-25%** (matches the vendor 10-26%) | Fewer second visits |
| Field service and HVAC | About 25-35% (failed visits, unneeded rolls) | **About 15-26%** | MTTR 4.5 days could fall materially |
| Industrial plants | About 20-30% of labour time (planning, search, Dx) | **About 10-25%** of maintenance cost | Restore time on the hard tail; worth the most per hour |
| Ag and trucks (if authorisation counts as "Dx") | Up to about 70% of total harm | **About 30-60%** of harm, but only with legal access | Large. Not achievable by knowledge alone |
| Medical devices | About 20-40% (access-driven) | **About 20-40%**, requires opened access | Moderate |
| Offshore wind | About 5% or less | **Under 5%** | Negligible. Vessels and weather bind |
| Transformers, nuclear, shipyards | Hours to days against months to years | **Under 5%** | Negligible. Capacity and qualification bind |
| Consumer phones | About 5-10% (screen and battery Dx is trivial) | **Under 10%** | — |

**Bottom line.**
- **Realistic ceiling on total repair cost: about 10-25% in labour-heavy field service, about 5-15% in parts- and access-heavy domains, and about 25-40% only in diagnosis-heavy electronics and access-locked niches.**
- That is consistent with every measured intervention:
  - AI copilots: 14-34% gains, concentrated in novices (d01, u05).
  - Remote and AR support: about 15% (d04).
  - Medical diagnosis AI: 20-45% (d02).
  - Collision costs rose 63% even after estimating was automated (s05).
- An order-of-magnitude system-wide gain is not available from cheaper knowledge. The documented roughly 10x cases came from other levers:
  - **Eliminating unnecessary work.** RCM/MSG cut structural inspection from about 4M to 66k man-hours (n02 `[U]`).
  - **Redundancy and batching.** Hyperscalers went from 5-15% of equipment value to 0.75% (m14).
  - **Standardised pre-positioned spares.** RecX restored a transformer in under a week against years (e02).
  - **Prediction plus logistics.** Delta cut cancellations about 100x, before LLMs (d01).
  - **Legal opening of access.** Deere tool price fell 16x (v04).
- The value released by cheaper knowledge also tends to go elsewhere:
  - **To buyers**: Protolabs' operating margin fell from about 20% to 5% (x04).
  - **To whoever holds sign-off, data or the parts channel**: h01, h07, h08.

**Evidence quality.** Most agents ran without web search. The flags that matter most:
- **Recalled from memory:** the wind 95% figure, the RCM man-hours, Siemens' $1.4T, IATA's $11B and the appliance call-out figures.
- **Vendor- or advocacy-sourced:** Aquant's field-service numbers (vendor) and PIRG's ag numbers (advocacy).
- **Estimates:** the stage percentages for AOG, and every share in section 3, are my own estimates.

Supporting raw notes are in `raw/` under each id (for example `raw/z10.md`, `raw/r02.md` and `raw/m01.md`).