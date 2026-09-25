# Moonshots: YC-scale companies in nuclear, power, and data centers

**For a founding team with top-five-in-the-world engineers in whatever field the company needs. Written against the market as of 25 September 2026. Evidence is in `research/`.**

The previous document (`RESEARCH.md`) asked "what survives everything." This one asks a different question: what is the biggest company a world-class technical team could plausibly build in this sector in the next five years, where the ambition is revolutionary and the path to first revenue is real.

The filter for this list:

- **It attacks a bottleneck that is physical or regulatory, not a sales problem.** Every idea here is aimed at something the industry cannot buy its way out of today: forgings, qualified welders, NRC review capacity, interconnection time, safety-grade I&C, rework.
- **World-class engineers change the odds.** If the idea would go equally well with average engineers, it is not on this list.
- **There is a wedge with revenue inside 24 months** and a defensible position if it works.
- **It is not a reactor company.** Sixty-six companies are designing reactors, $6.2B of venture money went into them in 2025, and every one of them is a customer for the companies below. The reasoning is at the end.

Seven ideas, ranked by ambition times doability. Each has: the pitch, why now, the hard technical bet (what the engineers actually do), the wedge, the ten-billion-dollar path, competition, the thing most likely to kill it, and what a YC partner will push on.

---

## 1. The nuclear component gigafactory ("Hadrian for nuclear")

**Pitch.** A highly automated, NQA-1-certified factory that makes the safety-related components the industry cannot buy: small-bore safety valves and pumps first, reactor coolant pumps second, and then reactor pressure vessels made by powder-metallurgy hot isostatic pressing and electron-beam welding instead of forging. Become the American forge, without a forge.

**Why now.**
- Japan Steel Works controls roughly 80% of the world's large nuclear forgings; lead times are 36 months at best and five-plus years in practice. There is no US ultra-large forging capacity. A single forge produces about four vessel sets a year. Westinghouse's entire export pipeline is underwritten on Doosan steel.
- Curtiss-Wright is the sole US supplier of reactor coolant pumps at 12–16 a year, enough for three or four AP1000s. Zachry says safety-related valves, forgings and I&C "don't currently exist at the volumes SMR programs will need." Kiewit calls NQA-1 components the most critical constraint.
- The advanced-manufacturing route is technically proven but not yet code-accepted at scale: Sheffield Forgemasters completed four thick nuclear-grade electron-beam welds on a full-size SMR vessel demonstrator in under 24 hours (February 2026); NuScale's vessel demonstration projected a 40% cost saving and under one year of fabrication; EPRI has compiled PM-HIP data on 316L, nickel alloys and Grade 91 toward ASME code inclusion and says the block is "lack of standards, ASME acceptance and regulatory approval." SMR vessels need 200–350 tonnes of steel and 8,000–12,000-tonne presses, not the 14,000-tonne class.
- Demand is contracted, not speculative: DOE's $17.5B conditional commitment funds long-lead components for up to ten AP1000s across five vehicles; Darlington and Kemmerer are under construction; BWXT just bought Precision Components (450 workers) and Oklo bought ARMEC because incumbents are buying capacity rather than building it; Indiana offers a 20% nuclear-manufacturing tax credit and Texas reimburses supply-chain investment.

**The hard technical bet.** Three things a world-class team does that a machine shop cannot: (1) qualify PM-HIP and electron-beam-welded pressure-boundary components under ASME Section III, including the material data packages, procedure qualifications and code cases, and get NRC acceptance; (2) build a factory where digital QA is native, so every weld, heat lot and inspection is traceable by construction rather than by paperwork, which is the exact failure mode that sank Vogtle's module plant; (3) design for manufacturability with the reactor vendors so the components are standard across designs.

**Wedge.** Small-bore safety-related valves. Zachry names them as the gap, they are the highest-count items on any SMR bill of materials, N-stamp scope is achievable in roughly 18 months, and every uprate and outage in the operating fleet buys them today. Then a second-source reactor coolant pump under license or clean-sheet. Then the vessel.

**Ten-billion path.** IEA puts nuclear investment at about $80B a year and rising. BWXT's nuclear operations run above $2B a year on legacy processes. DOE's long-lead program alone is $17.5B of components for ten reactors. If PM-HIP vessels arrive at 40% below forged cost and a fraction of the lead time, the company becomes the default vessel source for every SMR program in the West and the second source for large reactors.

**Competition.** BWXT, Curtiss-Wright, Doosan, JSW, Sheffield Forgemasters (UK, state-owned), Framatome (which just bought a valve business), and North American Forgemasters for smaller work. None is building an automated, code-qualified PM-HIP/EBW line in the United States.

**What kills it.** The ASME code-case and NRC acceptance path takes longer than the money lasts. Mitigation: the valve and pump business is conventional and cash-generative while the vessel qualification runs.

**What YC will push on.** Capital intensity (answer: valves first, $30–60M for the first line, government and state money for the vessel line) and whether reactor vendors will buy from a startup (answer: they already buy from startups when there is no alternative; Standard Nuclear went from zero to a $577M TRISO backlog in a year).

---

## 2. The uprate developer ("add ten gigawatts of nuclear without pouring concrete")

**Pitch.** Fund and execute power uprates across the 94-reactor US fleet in exchange for the incremental megawatts, the way a solar developer owns the panels on someone else's roof. The product is new nuclear capacity at a fraction of new-build cost and years faster, delivered by industrializing the engineering that utilities cannot staff.

**Why now.**
- DOE's UPRISE initiative (March 2026) targets 2.5 GW of uprates by 2027 and 5 GW by 2029 with up to 80% federal financing, and names the bottlenecks as utility engineering bandwidth, long-lead equipment and staffing. NRC expects around 30 applications through 2030, 16 of them in 2027.
- Uprates deliver 39–50% of near-term nuclear additions for under 25% of the capex, a two-to-four-times capital-efficiency edge over first-of-a-kind SMRs. NRC has already approved 172 uprates totalling about 8 GW, so the regulatory path is worn smooth.
- Buyers pay for it: Meta's Vistra deal includes 433 MW of uprates; Constellation's Limerick uprate is a $2.4B program; PJM capacity has cleared at the cap for three consecutive auctions ($325/MW-day for 2028/29) with a 6.8 GW shortfall, and Microsoft is paying more than $100/MWh for restarted nuclear.
- The saturated incumbents are the opening. Westinghouse, Framatome and GE own the NSSS analyses; Sargent & Lundy and Enercon do balance-of-plant. All are at capacity.

**The hard technical bet.** Extended power uprates are gated by safety analysis and by balance-of-plant hardware. A world-class computational team rebuilds the analysis stack: coupled neutronics, thermal-hydraulics and structural models with modern uncertainty quantification and surrogate modeling, so that the margin a plant actually has can be demonstrated rather than bounded with 1980s conservatism. On the hardware side: turbine, generator, condenser, feedwater and main-transformer upgrades procured as a standard kit across similar units (the fleet has only a handful of designs). The regulatory play is a fleet-wide topical report, so each subsequent application is a delta rather than a first.

**Wedge.** Measurement-uncertainty-recapture uprates (1.5–2%, mostly instrumentation and analysis) at two or three utilities as a paid engineering scope, to prove the analysis stack and build the NRC relationship. Then the first developer-funded extended power uprate under a tolling agreement.

**Ten-billion path.** Illustrative arithmetic, not a forecast: 10 GW of incremental capacity earning PJM-style capacity revenue of roughly $120–150/kW-year plus an energy margin is on the order of $2–4B a year of gross value, of which the developer keeps its negotiated share for 20 years. Ten gigawatts is about 10% of the fleet, within the historical envelope of what uprates have achieved on individual units.

**Competition.** The NSSS vendors and the utilities' own engineering. The structural difference is that no one else is offering to fund the uprate and take the megawatt risk.

**What kills it.** NRC review capacity, not utility appetite. The NRC lost 510 staff in 16 months and its FY2027 request cuts licensing headcount; analysts warn 1–2 GW of uprates could be pushed into the 2030s. Mitigation: standardized fleet-wide submissions reduce review hours, and the ADVANCE Act fee and deadline framework helps. Second risk: utilities refuse to share upside. Mitigation: the deal is structured like restarts already are (Google and Microsoft PPAs fund the work), and rate-regulated utilities can put the developer's capital outside the rate base.

**What YC will push on.** Whether this is a services firm in disguise. The answer is the balance-sheet model: the company owns the incremental megawatts.

---

## 3. The reactor operating system (qualified safety I&C plus autonomous operations)

**Pitch.** The first modern, NRC-qualified digital safety instrumentation-and-control platform, built on formally verified FPGA logic and designed from the start for autonomous and remote operation. Sold to the sixty-plus reactor developers who each currently plan to build their own, then to the Army's microreactor fleet, then to the operating fleet as a staffing-reduction product.

**Why now.**
- Every reactor developer needs safety-grade I&C and almost none has it. NuScale outsourced its highly integrated protection system to Paragon; the incumbents (Westinghouse Common Q, Framatome TELEPERM, Rolls-Royce Spinline) are decades-old platforms with multi-year qualification tails.
- Autonomy is now a requirement, not a research topic. Radiant's INL test campaign includes a 150-hour unattended run. The Army awarded up to $2.2B to five vendors for microreactors on bases with the first unit in 2028 and 20+ planned; a reactor on a base has no room for a 500-person operations staff. Part 53 (effective April 2026) and the proposed Part 57 for microreactors are explicitly risk-informed and technology-inclusive, which is the door for reduced staffing and remote operation.
- The operating fleet's largest controllable cost is people: Lazard puts fixed O&M at $136–158/kW-year, roughly $13–15B a year across the fleet. A platform that safely takes 20% out of that is a $2–3B-a-year value pool by itself.
- The NRC's staffing loss cuts both ways: a regulator with fewer reviewers strongly prefers one qualified platform reviewed once over sixty bespoke systems.

**The hard technical bet.** Formal verification of safety logic at the hardware level (FPGA rather than software, provably free of common-cause failure), a diverse-and-defense-in-depth architecture that satisfies IEEE 603 and the NRC's digital I&C guidance without the decades of legacy, and an autonomy layer that is separable from the safety layer so the safety case does not depend on the autonomy. The engineering is the same discipline that produces flight-critical avionics, done by people who have shipped those.

**Wedge.** Be the I&C and control vendor for one DOE-authorized pilot reactor (there are now five critical and a Launch Pad pipeline). DOE authorization is fast; it produces operating data and a demonstration under real conditions. Convert that into an NRC topical report that any licensee can reference.

**Ten-billion path.** Safety I&C on every new reactor (the platform is a few percent of plant cost but sole-source once qualified), the autonomy stack as recurring software revenue on microreactor fleets that need it to exist at all, and O&M reduction on the operating fleet priced as a share of savings.

**Competition.** Westinghouse, Framatome, Rolls-Royce, Curtiss-Wright, Paragon, Schneider (Triconex). Developers' in-house teams (Aalo builds its own). Atomic Canyon and Nuclearn are on the operations-knowledge side, not the safety-control side.

**What kills it.** NRC qualification of a novel platform takes longer than any customer can wait, and developers ship with an incumbent's I&C for their first unit. Mitigation: the DOE-authorization wedge produces the evidence before the NRC review starts, and the platform must be certifiable under existing guidance rather than needing new rules.

**What YC will push on.** Regulatory timeline. The honest answer is 3–4 years to a referenced topical report, with paid demonstration revenue from year one.

---

## 4. Qualified robots, not qualified welders (nuclear-grade robotic welding and inspection)

**Pitch.** Robotic weld cells for module yards and crawling field robots for site piping that carry their own ASME IX and Section III procedure qualifications, produce the weld record automatically from sensor data, and run integrated phased-array ultrasonic inspection in the same pass. The craft shortage becomes a machine-count problem.

**Why now.**
- The pipefitter, welder and NDE shortage is the constraint every source names, and it is getting worse: nuclear skilled-trade demand is projected to roughly double from 2025 to 2030, construction is short about 439,000 workers, and data centers pay a 30% premium for the same crafts. Hinkley Point C's latest slip is explicitly electromechanical installation productivity.
- The failure mode of modular nuclear construction was the weld record, not the weld: at Vogtle's Lake Charles module plant, sub-modules arrived with the wrong weld types, QA paperwork took longer to resolve than fabrication, and workers entered colleagues' ID codes on weld records. A robot that cannot forge a record fixes this by construction.
- Robotic welding is proven at nuclear-adjacent scale but not qualified for nuclear: Path Robotics signed a $600M shipbuilding deal with HII in August 2026 and makes no ASME III claims; Novarc has welded 1,000 km of pipe with no nuclear references. The qualification is the whole wedge.
- The customers are being built right now: Holtec's Camden campus, BWXT's expanded plants, Blue Energy's shipyard model, Darlington's module program, Kemmerer's 1,600-worker site, and the DOE long-lead program's five component vehicles.

**The hard technical bet.** Adaptive welding of thick-section, tight-tolerance nuclear joints (varying fit-up, heavy-wall austenitic and low-alloy steels, narrow-groove) with in-process sensing good enough to be the inspection record, plus mobile platforms that work on installed pipe in congested plant spaces. The engineering is welding metallurgy, real-time control and perception, and the qualification is procedure-by-procedure under ASME IX with owner and NRC acceptance.

**Wedge.** One module yard, one procedure family (say, stainless pipe butt welds), qualified and running with a documented productivity and first-pass-yield gain. Sell throughput and record integrity, not robots.

**Ten-billion path.** Nuclear is the proving ground and the highest-value niche; the same qualified cells go into shipbuilding (where Path just showed the market size), gas plants, LNG and process industries with the same craft shortage.

**Competition.** Path Robotics, Novarc, ABB and Fanuc integrators, and owners' conservatism. Path or Novarc could add nuclear qualification, so speed matters.

**What kills it.** Owners insist on human welders for pressure-boundary work regardless of data, and the company gets stuck in pilot purgatory. Mitigation: start in module yards (factory conditions, willing customers), publish the data, and let the shortage do the selling.

---

## 5. The grid-native data center developer ("twelve-month power")

**Pitch.** Build only AI campuses that are curtailable and battery-buffered by design, and use the new flexible-interconnection pathways to get energized in 12–24 months instead of 4–7 years. Sell time-to-power, which is now the most valuable thing in the data-center business.

**Why now.**
- Duke's analysis found the largest 22 US balancing areas could absorb 76–126 GW of new load if it can be curtailed 0.25–1% of the year. Every fast path now requires exactly that: Texas SB6 (a July 2026 order made a 260 MW site shed full load within 30 minutes), PJM's interim non-firm transmission product, SPP's conditional service with agreements in about 90 days, MISO's fast track. FERC's June 2026 show-cause orders push every RTO the same way.
- The value of speed is enormous. At the $140–200/kW-month lease rates in the TeraWulf–Anthropic and Applied Digital contracts, a 100 MW campus earns roughly $15–20M a month; getting it live three years earlier is worth over half a billion dollars on that site alone.
- Google has 1 GW of demand response embedded in its contracts and says the benefit is faster connection. Emerald AI ($1.05B valuation, five demos) proves the workload side; Verrus (Alphabet-backed) is early on the battery side; nobody has yet combined flexible interconnection, on-site storage, workload orchestration and a developer balance sheet into one company. Crusoe, a YC company, showed that "compute follows power" is a $30B idea.
- ERCOT flagged 3,200 MW of load at risk of tripping on grid disturbances; ride-through compliance is a hard engineering deliverable that a battery-first design solves.

**The hard technical bet.** A campus electrical architecture in which storage, on-site generation and GPU load are co-controlled so the site can honor a 30-minute full shed or a 1% annual curtailment without the tenant noticing, plus the interconnection engineering to qualify for conditional service. The engineering is grid-forming power electronics, controls and workload-aware power management, done by people who have built grid-scale storage and large industrial loads.

**Wedge.** One 50–100 MW campus on conditional service in SPP or ERCOT, energized in under 18 months, leased to a neocloud that cannot get power anywhere else. The interconnection agreement itself is the proof.

**Ten-billion path.** Crusoe's path, with a better physical thesis: the company that reliably converts flexible interconnection into leased megawatts becomes the developer of choice for every tenant that is not a hyperscaler, and then for hyperscalers.

**Competition.** Crusoe, Verrus, Applied Digital, TeraWulf, Fermi America, plus Brookfield, Blackstone and NextEra as capital. Fermi is the cautionary tale: it went public on letters of intent and lost 60% when its tenant walked.

**What kills it.** Capital intensity ($11–18M per MW all-in) and tenant concentration. Mitigation: the first campus should be sized so the equity check is venture-scale and the debt is project finance against a signed lease; the software and controls stack is the venture asset even if the real estate is financed separately.

---

## 6. The design-complete nuclear builder (the first fixed-price nuclear EPC since 2008)

**Pitch.** The biggest bet on this list. An engineering-procurement-construction company for nuclear plants that takes fixed-price risk because it has eliminated the thing that destroys nuclear budgets: rework from incomplete design. Every drawing is complete, every work package is constructability-checked, every schedule activity is linked to a licensing commitment before the first concrete is poured.

**Why now.**
- DOE's decomposition of Vogtle's ~$15,000/kW says the largest lever from first-of-a-kind to nth-of-a-kind is elimination of rework and delays (index ~65, against ~35 for design standardization). INL's lessons list, in order: finalize design before construction, constructability review, a real integrated schedule, contractor QA. Vogtle carried more than 180 license amendment requests against its certified design.
- No US EPC takes fixed-price nuclear risk. Westinghouse "does not provide construction services or assume any construction risk." TerraPower had to go to Hyundai E&C for completion, price and performance guarantees on up to eight Natrium units; Holtec did the same. That is a market signal: the guarantee is the product, and it is currently imported.
- The tools to do this did not exist in 2010: generative and parametric design at plant scale, automated clash and constructability checking, 4D schedule simulation with hundreds of thousands of historical schedules (nPlan is doing a generic version at Sizewell C), and digital fabrication records (Ideas 1 and 4). a16z's 2026 request for startups asks for exactly this.
- Government is willing to share the risk. The DOE loan office lends at Treasury plus 0.375%, Ontario put C$3B of public equity into Darlington's construction risk, and the UK built a regulated-asset model for Sizewell C. The missing counterparty is a builder that will stand behind a number.

**The hard technical bet.** Take a certified design (AP1000 Rev 20 is the obvious candidate, because the DOE long-lead program and seven utilities are lined up behind it) to 100% construction-ready engineering with a quantified design-maturity score per work package, then prove on the first project that rework is single-digit percent. The engineering is plant-scale systems engineering, construction simulation and program controls at a level that exists in aerospace and semiconductor fabs but has never been applied to a nuclear island.

**Wedge.** Owner's engineer with a design-completeness guarantee on one of the five DOE AP1000 vehicles, paid for the engineering and taking a performance fee against rework. Then fixed-price on balance-of-plant and modules. Then the whole plant, with a DOE or state backstop.

**Ten-billion path.** The 10-reactor AP1000 program is $80B; the executive-order target is 400 GW by 2050; every export program (Poland, Bulgaria, Ukraine, India's newly opened market) needs a builder. A builder who can do it at Darlington's fleet-average cost with a fixed price is the most valuable company in the sector.

**Competition.** Bechtel, Kiewit (nuclear revenue doubling yearly, targeting $1B), Fluor, Hyundai E&C, Zachry, Day & Zimmermann, and the Westinghouse-Brookfield partnership.

**What kills it.** One first-of-a-kind blowup. Fixed-price nuclear bankrupted Westinghouse in 2017. Mitigation: never take full-plant fixed price without a government risk-sharing layer, and earn the right to it through the owner's-engineer wedge.

**What YC will push on.** Whether a startup can be an EPC. The answer is that Crusoe became a $30B developer and Anduril became a prime; the software and controls IP is the company, and the balance sheet is rented from DOE, states and infrastructure funds once the data proves the rework claim.

---

## 7. The HALEU midstream (a regulated monopoly if it works)

**Pitch.** Own every step between the enrichment plant and the fuel fabricator for high-assay low-enriched uranium: deconversion from UF6 to oxide and metal, licensed Type B transport packages for enrichments above 5%, and metal-fuel fabrication for sodium reactors. The step nobody has built, for a fuel everyone has ordered.

**Why now.**
- Clean Air Task Force and the Nuclear Scaling Initiative both report there is no US commercial HALEU deconversion and no licensed transport package above 5%; NSI calls it "the lead time to the lead time."
- The upstream is now funded: DOE's $2.7B enrichment awards (Centrus, General Matter, Orano), Centrus's 6,000 kg/yr cascade from 2029, Urenco's LEU+ authorization, and Russian waivers ending 1 January 2028. The downstream is real: Standard Nuclear's TRISO backlog went from $0 to $577M in a year, TRISO-X opens in 2028, Radiant signed the first binding commercial HALEU offtake, five DOE-authorized reactors have gone critical, and the Army awarded up to $2.2B for base microreactors.
- Metal fuel for sodium reactors (TerraPower, Oklo, Aalo) has no commercial fabricator; Kemmerer's schedule slipped on fuel.

**The hard technical bet.** A Part 70 facility license and Part 71 package certification, both slow and both unforgiving, executed by a team that has done fuel-cycle chemistry and criticality safety at national-lab standard. This is the one idea on the list where the engineering risk is low and the licensing risk is the whole game.

**Wedge.** Transport packages first (a certification program, not a plant), sold to enrichers and fabricators who cannot ship what they make. Then deconversion under DOE's HALEU Availability Program cost share.

**What kills it.** Microreactor demand slips again and volumes stay too small for a plant. This idea fails the "SMR-independent" test on purpose: it is a bet that the HALEU economy happens, and if it does, this is a mandatory toll booth with no competitor.

---

## Why not a reactor company

The user's team could design a reactor. The evidence says not to:

- 66 companies are doing it across 15 countries. Valar raised $1B at $6B, Antares $470M, Blue Energy $380M, Radiant $300M+, Oklo has $3B of cash, X-energy IPO'd at $1.1B, and Westinghouse has an $80B government partnership. The capital bar for entry is now $300M+ before first revenue in 2030+.
- The public market has already re-priced the category: Oklo −44% and NuScale −41% year-to-date, Deep Fission's IPO downsized 75%, Holtec's IPO postponed. Bank of America sees no meaningful SMR adoption before 2030–2040.
- Every reactor company is gated by the same five things: vessels and components (Idea 1), uprate-class engineering capacity that the incumbents cannot supply (Idea 2), safety I&C (Idea 3), qualified welders (Idea 4), and fuel (Idea 7). The companies that own those gates sell to all 66 and win regardless of which reactor wins.

The exception would be a reactor whose entire design premise is manufacturability with existing LEU fuel and an existing supply chain, built in an existing shipyard or factory. Blue Energy and Aalo are already there with $380M and $136M+ respectively.

---

## How to pick between them

| # | Idea | Ambition | Doability in 5 yrs | Revenue in 24 mo | Capital to first revenue | Regulatory gate |
|---|---|---|---|---|---|---|
| 1 | Component gigafactory | Very high | High | Yes (valves) | $30–60M | ASME/NRC for vessels only |
| 2 | Uprate developer | Very high | High | Yes (MUR engineering) | $5–15M, then project capital | NRC review capacity |
| 3 | Reactor operating system | Very high | Medium-high | Yes (DOE pilot demo) | $10–25M | NRC topical report, 3–4 yrs |
| 4 | Qualified robots | High | High | Yes (module yard) | $10–20M | Owner acceptance per procedure |
| 5 | Grid-native DC developer | Very high | Medium | Yes (first campus) | $20–50M equity + project debt | Interconnection agreements |
| 6 | Design-complete builder | Extreme | Medium-low | Yes (owner's engineer) | $10–30M, then government backstop | None directly; FOAK risk |
| 7 | HALEU midstream | High | Medium | Partial (packages) | $50–150M with DOE share | Part 70 and 71, 3+ yrs |

**If the team is mechanical, materials and manufacturing:** Idea 1, with Idea 4 as the second product line. This is the single most defensible physical position in Western nuclear.

**If the team is computational, nuclear engineering and finance:** Idea 2. It is the fastest path to owning gigawatts and the one that converts the fleet's existing margin into money.

**If the team is controls, formal methods and avionics:** Idea 3. It is the platform play, and the Army's 20-reactor fleet plus the DOE pilots are the demonstration customers no one had two years ago.

**If the team is power electronics, grid and software, and wants the Crusoe path:** Idea 5.

**If the team wants to build the most important company in the sector and can stomach a decade:** Idea 6, entered through the owner's-engineer wedge, with Ideas 1, 3 and 4 as the eventual subsidiaries. That is the shape of the company that actually makes nuclear cheap.
