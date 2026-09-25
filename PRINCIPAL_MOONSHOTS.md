# Principal moonshots: own the asset, not the contract

**For a world-class technical team that refuses to be a vendor. Market as of 25 September 2026. Evidence in `research/`; "general knowledge" marks standard facts not re-verified this session.**

The objection to the earlier lists is correct. A supplier qualification firm, a simulation platform, a safety-I&C vendor and a permitting product all sell to someone else's reactor, someone else's campus, someone else's grid. They earn well and they never control the outcome. A vendor's ceiling is its customers' ambition, and this sector's customers are slow.

The principal positions in energy are: own the reactor, own the fuel, own the electrons, own the compute, own the back end of the fuel cycle, or own a market that does not exist yet. Each has historically required a balance sheet or a decade. What has changed is that software and one clever piece of hardware can now make a startup the principal at a fraction of the historical cost, and the capital markets are funding exactly that (Valar $1B at $6B two years after founding; Crusoe $30.9B; Fervo $10B+; X-energy $1.1B IPO; General Matter $900M DOE task order and up to $4.2B of EXIM debt on a $50M seed).

Seven positions, ordered by how revolutionary they are against how plausibly a small, extraordinary team gets there.

---

## 1. The autonomous nuclear utility: own the plants, not the design

**The position.** A build-own-operate nuclear company that sells power directly to AI and industrial customers and never touches design risk: it licenses or acquires a proven reactor design and wins on the operating model, which is where every incumbent is weakest. The thesis: the reactor design is not the moat; the ability to license, build, fuel and *operate a fleet with almost no people* is.

**Why this is now possible for a startup.**
- Certified designs are available and under-used. NuScale's US460 has an NRC standard design approval (May 2025) and no US customer; its "up to 6 GW" partner ENTRA1 is a financial developer with a non-binding agreement. BWXT licensed its mPower design to Applied Atomics (August 2026). NANO bought the MMR out of the USNC bankruptcy. Holtec's SMR-300 and Westinghouse's AP300 are looking for fleet developers. The designs exist; the fleet operators do not.
- Operating cost is where the money is. Fixed O&M is $136–158/kW-year across the fleet. A plant operated with a fraction of the staff, on a fleet-wide safety case, with autonomous surveillance and monitoring, changes the economics more than any reactor-physics improvement. Part 53 (effective April 2026) and the proposed Part 57 are risk-informed and permit exactly that argument; the Army is procuring 20+ base reactors that must run without a 500-person staff; Radiant is testing 150-hour unattended operation.
- The customers want a counterparty, not a vendor. Microsoft, Amazon, Meta and Google signed roughly 9.8 GW of nuclear commitments, all with owner-operators (Constellation, Talen, Vistra, NextEra), none with reactor vendors. Meta paid Vistra for uprates and Constellation for Clinton; Google is funding a restart at Duane Arnold. The market has already decided that the buyer's counterparty is whoever owns and runs the plant.
- Government money goes to owners. DOE's loan office (Treasury + 0.375%) lends to project owners; the $17.5B AP1000 program requires an owner with $1B of equity per vehicle; Texas's $350M and New York's 1–5 GW mandate are looking for developers. Being the principal is the way to be eligible.

**The software and clever-hardware lever.** The company's product is the operating model: a fleet-wide structured safety case (so the second plant's application is a delta), a qualified autonomous-operations stack and safety platform (so staffing is a tenth of today's), and a modern analysis platform that squeezes every megawatt of margin out of the design. These are the three software companies in `SOFTWARE_MOONSHOTS.md`, built inside the principal instead of sold to it.

**Wedge.** Do not start with a plant. Start by becoming the owner-operator of a restart or an uprate (the DOE loan office funded three restarts and offers 80% financing for uprates), which puts the company on the NRC's books as a licensee with operating megawatts in 18–36 months. Then take the first licensed SMR design to a site with a state grant behind it.

**How big.** Constellation is $93B on 22 GW. A company operating 5 GW at a third of the O&M is worth a large fraction of that.

**Competition.** Constellation, Vistra, Talen, NextEra, Blue Energy (shipyard model, $380M, Constellation-backed), The Nuclear Company (AP1000 fleet, has not raised since May 2025), ENTRA1.

**What kills it.** A first-of-a-kind build blowup before the operating-model advantage is proven, or the NRC refusing the staffing case. Mitigation: the restart/uprate wedge produces operating revenue and regulatory standing before any new-build risk is taken.

---

## 2. Own the electrons: the AI power company

**The position.** A merchant power company whose product is firm, fast electricity for AI campuses, built from a physical book of flexible assets (batteries, reciprocating engines, curtailable contracts, uprated nuclear megawatts, demand-side flexibility) and a dispatch stack that turns them into a firm product. It signs the PPA. It owns the risk. It is the counterparty.

**Why now.**
- The value is in the contract, not the turbine. Hyperscalers pay above $100/MWh for firm clean power (Microsoft–Crane) and $60–70/MWh for existing nuclear (Amazon–Talen); behind-the-meter gas costs $100–165/MWh (Rabobank) against a $90 grid; PJM capacity is at the cap three auctions running with a 6.8 GW shortfall. There is a $15–75/MWh premium for firmness that the asset owner captures.
- The assets that can be built fast are the flexible ones. Reciprocating engines ship in 8–24 months, batteries in months, curtailable interconnection in 12–24 months versus 4–7 years for firm service; Duke found 76–126 GW of grid headroom at under 1% curtailment. A company that stacks these into a firm product is selling something the grid itself cannot.
- The capital is available to principals, not vendors: Blackstone put $1B into VoltaGrid, Brookfield launched a $10B AI infrastructure fund, Nvidia and six asset managers announced $500B of third-party capital platforms in August 2026, and PPL and Blackstone formed a merchant generation JV. All of it seeks operating companies with contracts.

**The software lever.** The dispatch and risk engine is the company. It co-optimizes a portfolio of assets and contracts against capacity, energy, ancillary and curtailment markets to deliver a firm product at the lowest physical cost, and it is what lets the company sign firm PPAs on a book of flexible assets. Constellation and Vistra run legacy versions of this on legacy fleets; nobody has built it for a portfolio designed around flexibility from the start.

**Wedge.** One 100–200 MW firm PPA to a neocloud in ERCOT or SPP, backed by a battery plus reciprocating-engine plus curtailable-interconnection book, financed against the PPA. Then uprated nuclear megawatts as the clean-firm core (Idea 1's wedge is the same asset).

**How big.** Vistra is $46B, Talen $14B on a few gigawatts of PPAs. The first AI-native power company with 5 GW of firm contracts is a top-tier independent power producer.

**Competition.** Constellation, Vistra, Talen, NextEra, VoltaGrid (engines only), Bloom (fuel cells only), the PPL–Blackstone JV. None is a portfolio-flexibility company.

**What kills it.** Gas price spikes on a book that leans on engines; an AI capex bust that leaves the company holding assets; permitting on the gas pieces (Oracle's New Mexico force majeure on 24 September 2026 was a pipeline permit). Mitigation: contracts with take-or-pay, a battery-heavy mix, and a migration to nuclear megawatts as they come.

---

## 3. Own the compute: dispatchable AI factories at stranded energy

**The position.** A compute company whose cost advantage is energy: it owns GPUs and generation together, places modular AI factories where power is stranded or curtailed (co-located at nuclear plants, at wind and solar with curtailment, at gas basins, at retiring coal sites with interconnection), and runs workloads that can pause, migrate and resume so the compute itself is a flexible load. It sells GPU-hours. It is Crusoe's thesis executed by a team that can out-engineer Crusoe on the flexibility.

**Why now.**
- Power, not chips or capital, is the gate: hyperscaler capex is ~$725B in 2026 and the gap between committed capital and energized megawatts is the widest on record; a neocloud that can energize faster wins customers. TeraWulf leased 401 MW to Anthropic at roughly $950M a year; Applied Digital contracted $36B over 15 years; Crusoe raised $3.9B at $30.9B in September 2026 and is now pushing factory-built modular sites.
- Flexible compute is the cheapest firm-looking load there is. Google already embeds 1 GW of demand response in its contracts by shifting ML workloads. A cloud designed from the scheduler up to checkpoint and migrate at grid signals can take conditional interconnection and cheap curtailed energy that no other load can use, and present the flat, curtailable profile that Texas SB6 and PJM now require.
- Stranded energy is enormous and cheap: curtailed renewables, off-peak nuclear, and gas at the wellhead all price far below the grid. Crusoe was built on flared gas; the general version is any energy that cannot reach load.

**The software and clever-hardware lever.** The scheduler that makes training and inference dispatchable (checkpointing, migration, priority tiers) is the software; the modular, liquid-cooled, grid-interactive AI factory that can be trucked to the energy is the hardware. Together they make the company the only compute buyer that can use energy nobody else can.

**Wedge.** One 20–50 MW modular factory co-located at a site with curtailed or off-peak energy and a conditional interconnection, selling dispatchable training capacity at a discount to the market. Then scale with the AI-native power company (Idea 2), which is the same company seen from the other side.

**How big.** Crusoe is $30.9B; CoreWeave is larger. The cheapest compute in the country is a very large company.

**Competition.** Crusoe, Nscale, CoreWeave, Applied Digital, TeraWulf, Core Scientific, IREN, Soluna, Verrus (Alphabet-backed flexible campuses).

**What kills it.** GPU depreciation faster than the power advantage pays back; tenant concentration; an AI demand correction. Mitigation: sell capacity under take-or-pay, keep the hardware modular so it can move to the next energy source, and let the power company (Idea 2) be the asset that survives a compute downturn.

---

## 4. Own the fuel: the enrichment and conversion company

**The position.** A nuclear fuel principal that owns conversion and enrichment capacity (and later deconversion), sells enriched product under long-term contracts to utilities and reactor developers, and becomes the domestic toll booth for a fuel cycle that the Russian import ban is forcing onshore.

**Why now.**
- The market has repriced: long-term uranium is $96.50/lb, an 18-year high; SWU is reported near $200, roughly triple (single source); the Russian ban is in force with waivers ending 1 January 2028; Urenco, Orano and Centrus cite 3–4 year lead times.
- Government is funding principals: DOE's $2.7B enrichment awards went to three companies including General Matter, a 2024 startup with a $50M Founders Fund seed, which then received up to $4.2B of EXIM debt. Centrus's $900M task order shows the contract structure. The Army's microreactor program and the DOE pilot reactors create HALEU demand that only two or three companies can serve.
- The back half is empty: no US commercial HALEU deconversion, no licensed transport packages above 5%, and Standard Nuclear's TRISO backlog went from zero to $577M in a year on microreactor demand.

**The clever-hardware lever.** Enrichment is a technology business; the incumbents run decades-old centrifuge platforms and General Matter's whole thesis is a modern one. The technical details are not for a memo, and the technology is subject to export controls and NRC and DOE oversight that shape everything about how the company is built. The business point is simpler: a team that can build a better separation platform owns a regulated monopoly with government offtake.

**Wedge.** Deconversion and transport packaging first (a certification program rather than a plant, and a step nobody has built), then conversion, then enrichment under DOE and EXIM financing.

**How big.** Urenco and Orano's enrichment businesses are multi-billion-dollar annual revenue franchises; a US principal with domestic preference and government offtake is comparable.

**Competition.** Centrus, Urenco USA, Orano (Project Ike, ~$5B), General Matter, GLE.

**What kills it.** Licensing time (a Part 70 facility is a multi-year program), proliferation policy, and the possibility that reactor demand for HALEU slips again. This is the most regulated position on the list and the one with the most government money behind it.

---

## 5. Own the back end: the spent-fuel company

**The position.** The private company that takes title to America's spent nuclear fuel, is paid by the federal government to do it, and then owns the feedstock for recycling into new fuel. Nobody in the United States is the principal for the back end of the fuel cycle; the government has failed at it for forty years and pays damages every day for the failure.

**Why now.**
- The liability is real and paid in cash: the federal government has paid on the order of $10B in damages to utilities for failing to take spent fuel under the standard contract, with projected liabilities of tens of billions more, at roughly $2M a day (general knowledge; verify current figures). A private counterparty that takes the fuel converts that liability into a revenue stream.
- The legal path cleared in 2025: in *NRC v. Texas* (June 2025) the Supreme Court held that only formal parties to NRC proceedings can challenge NRC licenses, which removed the collateral attack that had frozen private consolidated interim storage. The NRC has already licensed such facilities.
- Recycling is back on the policy table: DOE has a surplus-plutonium request for applications, $19M of recycling R&D, and gave Curio a letter of intent for a pyro-oxidation plant (June 2026); Oklo has a recycling program. The May 2025 executive orders direct DOE toward fuel-cycle expansion. The current administration is more favorable to reprocessing than any since 1977.
- Spent fuel is 95% unused energy and contains the plutonium and minor actinides that fast reactors (TerraPower, Oklo, Aalo) can burn. The company that owns the feedstock owns a future fuel supply that does not depend on enrichment.

**The clever-hardware and software lever.** Modern separation chemistry (pyroprocessing and advanced aqueous flowsheets) at a scale and safeguards standard the industry has not fielded commercially in the US, plus the digital safeguards, accountancy and licensing stack that makes a private facility acceptable to the NRC and the IAEA. The technical specifics are governed by nonproliferation controls and are not for a memo; the business is a regulated monopoly with a government-paid input.

**Wedge.** Consolidated interim storage, paid under DOE settlements and utility contracts, at a site that already hosts nuclear infrastructure and wants the work (several DOE sites and states have volunteered for nuclear-lifecycle campuses). Recycling follows the storage.

**How big.** The liability alone is tens of billions; the fuel value of the inventory is larger; the strategic value of owning the only domestic back end is not priced.

**Competition.** Holtec and Interim Storage Partners (licensed but stalled), Curio, Oklo, Orano (which runs the French back end).

**What kills it.** Politics. Consent-based siting is slow, reprocessing is contested, and a change of administration could reverse the policy. Mitigation: storage is bipartisan and paid; recycling is the option, not the wedge.

---

## 6. Own a market that does not exist yet: orbital compute

**The position.** Data centers in orbit: solar power with no night and no permits, cooling by radiation to space, no interconnection queue, no water, no neighbors, no moratoria. The company owns the satellites, the power and the compute, and sells the compute.

**Why now.**
- The terrestrial constraints are exactly the ones orbit removes: 4–7 years to firm power, transformers at 3–5 years, 75 projects and $130B blocked in a single quarter by local opposition, more than 100 moratoria, gas permits failing. Every one of those is a permit, a queue or a neighbor. Orbit has none.
- It has started: Starcloud (a Y Combinator company) launched a satellite with a data-center-class GPU in late 2025, and Google announced its Project Suncatcher research program for solar-powered orbital ML compute in November 2025 (general knowledge; verify current status). Launch cost is the bet, and it is falling on a public roadmap.
- The physics is a clever-hardware problem, which is the kind a world-class team wins: radiator mass per kilowatt, radiation-tolerant compute, high-bandwidth optical downlink, and a constellation architecture that keeps a training job coherent across nodes.

**Wedge.** Batch and training workloads that tolerate latency and value cheap, unconstrained energy, sold to a customer that has already said it wants this (the hyperscalers are studying it; a neocloud would buy it). A first cluster measured in hundreds of kilowatts is a demonstration; a first cluster measured in megawatts is a business.

**How big.** If launch costs follow their roadmap, orbital energy is the cheapest firm power available to compute anywhere, and the company that owns it owns a new layer of the cloud.

**Competition.** Starcloud, Google, SpaceX (which has discussed orbital compute), Lumen Orbit-style entrants. Early and thin.

**What kills it.** Launch cost stalls, radiator mass makes megawatt clusters impractical, or radiation kills the economics of commodity GPUs. This is the highest-variance idea on the list and the one where world-class engineers matter most.

---

## 7. Own a new heat source: next-generation geothermal as an owner

**The position.** A geothermal power company that owns its plants and sells firm clean power to AI customers, differentiated by a proprietary drilling or reservoir technology that opens hotter, deeper rock than the incumbents can reach. This is the one non-nuclear firm-power route where a startup has already become a principal at scale.

**Why now.**
- Fervo IPO'd in May 2026 at $27, raised $1.89B and trades above $10B; it has a 500 MW first phase permitted to 2 GW and Google as an anchor. XGS has 150 MW of Meta contracts on ~$26M raised. Sage has 150 MW with Meta. Quaise raised $134M for millimeter-wave drilling. The hyperscalers are buying geothermal at above $100/MWh (Jigar Shah).
- Geothermal keeps its tax credits through 2033 under the 2025 tax law; wind and solar do not. It is firm, it is clean, and it needs no fuel cycle, no NRC and no neighbors' consent.
- The binding constraint is drilling cost and rock temperature, which is an engineering problem, not a permitting one. Every 100°C of additional reservoir temperature multiplies the power per well.

**The clever-hardware lever.** A drilling or completion technology that reaches superhot rock (above 375°C, general knowledge) economically, or a reservoir-engineering method that makes ordinary rock produce like a hydrothermal field. Fervo's advantage was importing shale techniques; the next advantage is going where shale techniques cannot.

**Wedge.** One well pair that demonstrates the technology at a site with existing geothermal infrastructure, financed by a hyperscaler PPA the way XGS and Sage financed theirs.

**How big.** Fervo at $10B+ is the floor for the company that reaches superhot rock.

**Competition.** Fervo, XGS, Sage, Quaise, Eavor, Zanskar, Ormat.

**What kills it.** The drilling technology does not work at depth, or costs do not fall with scale. Deep-tech risk, but with a market that pays today.

---

## How these compare

| # | Position | What you own | Who pays | Capital to first revenue | Regulatory gate | Crowding | Revolutionary |
|---|---|---|---|---|---|---|---|
| 1 | Autonomous nuclear utility | Plants and PPAs | Hyperscalers, utilities, DOE loans | $20–50M equity, then project finance | NRC licensee status; staffing case | Medium | High |
| 2 | AI power company | Generation and contracts | Data centers | $20–50M equity, then project finance | State and RTO | Medium | Medium-high |
| 3 | Dispatchable compute | GPUs and generation | AI labs and enterprises | $30–80M, then debt | Interconnection | High | Medium-high |
| 4 | Fuel company | Enrichment and conversion | Utilities, DOE, developers | $50–150M with DOE and EXIM | NRC Part 70; export controls | Low (3–4 players) | High |
| 5 | Spent-fuel company | Fuel inventory and facilities | Federal government, utilities | $50–200M with settlements | NRC; consent-based siting | Very low | Very high |
| 6 | Orbital compute | Satellites, power, compute | AI labs | $50–150M | Spectrum and launch | Very low | Extreme |
| 7 | Geothermal owner | Plants and PPAs | Hyperscalers | $30–80M, then project finance | State permits | Medium | High |

## The honest trade

Principal positions cost more and take longer than vendor positions, and three of the seven (fuel, spent fuel, orbital) depend on government or on launch economics the founders do not control. What makes them possible for a small team today is that the capital markets and the government are now explicitly funding principals: DOE lends at Treasury plus 0.375% to owners, EXIM lent $4.2B to a seed-stage fuel company, Blackstone and Brookfield write billion-dollar checks to operating companies with contracts, and the hyperscalers sign 20-year PPAs with whoever owns the megawatts.

**If the team wants nuclear and autonomy, Idea 1 is the answer**: become a licensee through a restart or uprate, build the operating model as software, and be the owner that the hyperscalers actually sign with. Ideas 4 and 5 are the two toll booths on either side of it, and the same company could own all three in time.

**If the team wants the AI side, Ideas 2 and 3 are one company** seen from the power side and the compute side; start from whichever the first customer wants to buy.

**If the team wants to build something nobody has built, Idea 6.**
