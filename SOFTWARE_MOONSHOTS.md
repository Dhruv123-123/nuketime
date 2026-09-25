# Moonshots by software inroad or clever hardware, not construction

**For a world-class technical team that wants leverage, not a factory. Market as of 25 September 2026. Evidence in `research/`; items marked "general knowledge" are standard industry facts not re-verified this session.**

The principle behind this list: in nuclear and grid, the physical assets already exist and are wildly underused because the *analysis* that governs them is decades old and the *paperwork* that governs them is manual. Software that changes what an existing asset is allowed to do is worth as much as building a new one, and it ships in years rather than decades. Where hardware appears below, it is one clever component that removes a bottleneck, not a plant.

Nine ideas in four groups. Each has the pitch, why now, the hard bet, the wedge, the path to a very large company, competition, and what kills it.

---

## Group A: The nuclear software stack

The US fleet is 94 reactors governed by safety analyses written on 1980s codes, licensing bases kept in paper, and operations run by roughly 500–800 people per unit. Fixed O&M is $136–158/kW-year (Lazard v19), about $13–15B a year across the fleet. Sixty-six new reactor developers are each building the same analysis, licensing and control tooling from scratch. The NRC lost 510 staff in 16 months and now has 18-month deadlines. The stack below is three companies that could be one.

### 1. The margin engine: modern simulation that recovers power from the existing fleet

**Pitch.** A GPU-native, NQA-1-qualified multiphysics platform (coupled neutronics, thermal-hydraulics, fuel performance, structural) with best-estimate-plus-uncertainty methods, accepted by the NRC via topical report, whose first product is recovering the power margin that 1980s bounding analyses left on the table across the fleet.

**Why now.**
- Uprates are the most capital-efficient nuclear megawatts in existence (39–50% of near-term additions for under 25% of pathway capex), DOE's UPRISE offers 80% financing, and NRC expects ~30 applications through 2030. The gate is analysis: DOE names "engineering bandwidth at utilities" as the first constraint.
- The incumbent codes (RELAP5, TRACE, the vendor LOCA suites) are 30–40 years old and CPU-bound; best-estimate-plus-uncertainty is an NRC-accepted methodology (Regulatory Guide 1.157 and the CSAU framework, general knowledge), and DOE's open-source MOOSE/NEAMS ecosystem provides a modern numerical foundation nobody has commercialized and qualified at scale (general knowledge).
- The same platform is what 66 developers need for their safety analyses, and what the NRC needs to review them faster. TerraPower's SER came in 8 months early and Long Mott's environmental review under 12 months; the reviewers are the bottleneck now, and a code they have already accepted is the fastest thing to review.

**Hard bet.** Qualify a new code with the NRC. That is a 2–4 year topical-report program with a rigorous software QA regime (NQA-1 Subpart 2.7, general knowledge) and validation against the separate-effects and integral test databases. The engineering is numerical methods, GPU computing and verification and validation at a level the nuclear industry has never had.

**Wedge.** Measurement-uncertainty-recapture and non-safety analyses (thermal performance, fuel management, outage optimization) sold to two or three utilities for cash while the topical report runs. Then a fleet-wide extended-power-uprate methodology, priced as a share of the megawatts it creates.

**Path to very large.** A 5% average recovery across the fleet is ~5 GW, worth billions in PJM-cap capacity and energy revenue over 20 years. Then every new reactor's design analyses and every NRC review run on the same platform.

**Competition.** Westinghouse, Framatome and GE analysis groups (saturated, on legacy codes), Studsvik, and national labs (which do not sell qualified commercial software).

**What kills it.** NRC code review takes longer than the runway. Mitigation: the non-safety products are cash-generative from day one, and the platform is valuable to developers before the NRC accepts it.

### 2. The licensing compiler: the safety case as code

**Pitch.** A structured, machine-checkable safety case: requirements, design bases, analyses, PRA, ITAAC and regulatory commitments as linked, versioned objects, from which the safety analysis report chapters, license amendment requests and inspection plans are generated, and against which any design change is impact-analyzed automatically.

**Why now.**
- Vogtle carried 180+ license amendment requests against its certified design; each one required reanalysis, rework and a new regulatory review. That is the single most expensive failure mode in nuclear construction, and it is a traceability failure, not an engineering one.
- Part 53 took effect April 2026 and Part 57 for microreactors is proposed; 66 developers are writing the first applications under a new framework with no template. The NRC's 18-month clocks and staff losses shift the burden to application quality; a review is fast when the reviewer can follow every claim to its evidence.
- The operating fleet needs the same thing: subsequent license renewals to 80 years (over 95% of units plan it), 30 uprates and restarts all require licensing-basis reconstitution from paper.
- The existing tools are search (Atomic Canyon over ADAMS, Nuclearn for condition reports) and generic requirements managers (DOORS, Jama). Microsoft and Nvidia's free permitting accelerator is a document generator, not a safety-case model. Aalo claims a 92% permitting-time reduction using the generic stack, which is evidence of appetite, not of a product.

**Hard bet.** A domain model of the safety case rich enough to generate compliant submittals and to prove change impact, plus getting the NRC to accept structured digital submittals as the reviewed artifact (the NRC has been pursuing digital submittal initiatives; general knowledge). The engineering is formal-methods-grade modeling applied to regulatory text, which is why it needs world-class people and why nobody has done it.

**Wedge.** One Part 53 applicant's full application. The first accepted Part 53 application becomes the reference for the next sixty.

**Path to very large.** Every new reactor, every uprate, every renewal, and eventually the regulator itself. The company that holds the structured safety case of most of the fleet is the system of record for the industry.

**Competition.** Atomic Canyon, Everstar, Microsoft/Nvidia, Jama, IBM. None models the safety case; they model documents.

**What kills it.** The NRC never accepts the structured form and reviewers keep reading PDFs. Even then the internal value (change impact, generation) is large enough to sell.

### 3. Fleet automation: take 20% out of nuclear O&M

**Pitch.** The operations platform that lets an existing plant run with materially fewer people and fewer outage days: online monitoring in place of periodic surveillance tests, predictive maintenance with NRC-accepted methods, automated work-package generation, AI-assisted procedures, and eventually risk-informed staffing changes.

**Why now.**
- Fixed O&M is the fleet's largest controllable cost, $13–15B a year. Nuclear is the only generation source whose O&M is dominated by regulatory labor rather than fuel.
- The regulatory doors are open: online monitoring replacing calibrations has NRC-endorsed guidance (EPRI's on-line monitoring topical, general knowledge); 10 CFR 50.69 lets plants risk-inform component treatment (general knowledge); the NRC's March 2026 oversight revision cut baseline inspection hours 38%; Part 53 is explicitly risk-informed. About 25% of the nuclear workforce is retirement-eligible, so the utilities want this.
- The incumbents are thin: Nuclearn (70+ facilities, ~$10M raised) and Atomic Canyon are document-and-condition-report tools. Nobody has shipped the surveillance-replacement and staffing product.

**Hard bet.** Sensor fusion and anomaly detection good enough to be the safety-basis replacement for a surveillance test, with the qualification evidence to prove it plant by plant, plus the licensing work (Idea 2) to change the technical specifications. The engineering is industrial ML with a rigor standard closer to avionics than to SaaS.

**Wedge.** One plant, one system (a safety-related pump or valve population), one technical-specification change that eliminates a surveillance. Then the fleet of that design.

**Path to very large.** 20% of $13–15B a year is $2.5–3B a year of savings to share, and the same platform is the operations layer for microreactors that must run with near-zero staff (the Army's 20+ base reactors, Radiant's 150-hour unattended runs).

**Competition.** Nuclearn, Atomic Canyon, GE Vernova and Westinghouse digital groups, utility in-house teams.

**What kills it.** Plant-by-plant licensing changes are slow and utilities fear the regulator. Mitigation: start with non-safety systems where no license change is needed, and let the savings data pull the safety-related work.

---

## Group B: Clever hardware in nuclear (components, not plants)

### 4. The safety chip: one qualified protection platform for every new reactor

**Pitch.** A formally verified, FPGA-based reactor protection and safety I&C platform, qualified once with the NRC via topical report, sold as a product to the 66 developers who each currently plan to build or buy a bespoke system.

**Why now.**
- Safety I&C is sole-source and old: Westinghouse Common Q, Framatome TELEPERM, Rolls-Royce Spinline, plus Paragon, to which NuScale outsourced its highly integrated protection system. Zachry lists I&C among the things that "don't exist at the volumes SMR programs will need."
- Digital I&C is historically the longest licensing tail in a new plant (common-cause failure arguments, general knowledge). FPGA logic that is provably free of software common-cause failure and formally verified against its specification is the cleanest answer the NRC has ever been offered, and the NRC's new frameworks reward it.
- Microreactors cannot exist without it: the Army awarded up to $2.2B for base microreactors with the first in 2028; Radiant is running unattended tests; every DOE-authorized pilot reactor needs a control system now, under DOE rather than NRC authority, which is the fast demonstration path.

**Hard bet.** Formal verification of the safety logic at the hardware level, a diverse architecture that satisfies IEEE 603 and the NRC's digital guidance (general knowledge), and a separable autonomy layer so the safety case does not depend on the autonomy. The team is the team that ships flight-critical avionics.

**Wedge.** Control and protection for one DOE-authorized pilot reactor (five are critical, more in the Launch Pad pipeline). Convert the operating evidence into an NRC topical report any licensee can reference.

**Path to very large.** Sole-source on every new reactor once qualified, recurring software on autonomous fleets, and the hardware half of Idea 3 for the operating fleet.

**Competition.** The four incumbents and developers' in-house teams (Aalo builds its own).

**What kills it.** Developers ship their first unit with an incumbent's platform because the startup's qualification is not done. Mitigation: DOE-authorized demonstrations produce evidence before the NRC review starts.

### 5. The reactor-agnostic back half: factory-built power conversion and thermal storage

**Pitch.** A standardized, factory-built "energy island" (supercritical-CO2 or advanced steam turbine, molten-salt thermal storage, grid interface) that turns any high-temperature heat source into flexible, peaking-capable electricity. Sold to every Gen IV developer, every geothermal developer, and industrial heat users, so the reactor companies only have to build the reactor.

**Why now.**
- The balance of plant is roughly half of a nuclear plant's cost and every Gen IV developer (sodium, salt, gas-cooled: TerraPower, Kairos, X-energy, Aalo, Terrestrial and more) needs power conversion above 500°C, which no standard product provides. TerraPower built its own salt storage into Natrium to get 500 MW peak from a 345 MW reactor; that design decision is the reason Natrium has a utility customer.
- Flexibility is now worth more than baseload: PJM capacity is at the cap, ERCOT demands curtailment, and a reactor with storage sells peak capacity at $325/MW-day without ever cycling.
- Supercritical-CO2 turbomachinery is compact enough to be factory-built and truck-shipped (a fraction of steam-turbine size at the same power, general knowledge), which is the "clever hardware" that makes this a product and not a construction project.

**Hard bet.** Supercritical-CO2 turbomachinery and heat exchangers at 50–300 MW class with commercial reliability, plus salt-storage integration. The engineering is turbomachinery, materials at temperature and controls, done by people who have shipped turbines.

**Wedge.** A 10–50 MW unit for a DOE-authorized pilot reactor or a geothermal developer (Fervo, XGS and Sage all sell power above $100/MWh and would pay for higher conversion efficiency and dispatchability).

**Path to very large.** The back half of every advanced reactor and every enhanced geothermal plant in the West.

**Competition.** Echogen, Siemens Energy and GE (steam), Malta and Hyme (storage), and developers building in-house. Nobody sells the integrated flexible island as a product.

**What kills it.** It is capital-heavier than the software ideas and the first unit is a hardware program. Mitigation: geothermal customers exist today and pay today; nuclear developers follow.

---

## Group C: Data centers and the grid

### 6. Synthetic firm power: the load-shaping operating system

**Pitch.** The controls-and-contract product that presents a data center to the utility as a flexible load (curtailable in minutes, ride-through compliant) while delivering firm power to the tenant, by orchestrating on-site batteries, backup generators, UPS and workload placement together. The customer buys speed to power; the utility gets a guaranteed, verified, insurable curtailment.

**Why now.**
- Flexibility is now the price of admission: Texas SB6 (a July 2026 order made a 260 MW site shed full load in 30 minutes), PJM's non-firm transmission product, SPP conditional service in ~90 days, MISO's fast track, FERC show-cause orders to all six RTOs. Firm service is 4–7 years; conditional is 12–24 months.
- The headroom is large (76–126 GW at 0.25–1% curtailment, Duke) and the value of speed is extreme (a 100 MW campus earns $15–20M a month at contracted lease rates). ERCOT flagged 3,200 MW at risk of tripping on disturbances, so ride-through is a hard requirement.
- Emerald AI ($1.05B, five demos) owns the hyperscaler workload layer and just formed an alliance with Google and Nvidia to standardize signals. Verrus is building battery-first campuses. Nobody owns the electrical layer (UPS, BESS, gensets) plus the utility-facing verification and contract for the thousands of colos, neoclouds and enterprises that cannot rewrite schedulers.

**Hard bet.** Co-control of grid-forming storage, generators and load at millisecond scale so that a curtailment order is honored without the tenant noticing, plus the telemetry and settlement layer utilities accept as proof. The engineering is power electronics control and real-time systems.

**Wedge.** One neocloud or colo in SPP or ERCOT that gets conditional interconnection 3 years faster because the utility trusts the product. The interconnection agreement is the sales collateral.

**Path to very large.** The standard flexible-load interface for every non-hyperscaler data center, and the insurable curtailment guarantee that utilities require (Idea 11 in `RESEARCH.md` is the financial wrapper).

**Competition.** Emerald AI and its alliance (Voltus, Camus, GridUnity), Schneider and Eaton power-management systems, Verrus, Tesla Megablock as hardware. The window is about two years.

**What kills it.** The alliance standardizes the protocol and the incumbents bundle compliance. Mitigation: the electrical-layer control and the utility contract are harder to commoditize than the signal.

### 7. Rack-to-grid: the power-smoothing appliance

**Pitch.** A row-level energy buffer and converter (supercapacitor or high-cycle battery plus power electronics) that flattens the millisecond-to-second power swings of GPU clusters so a campus presents as a flat load, delivers grid ride-through, and cuts the oversizing of transformers, switchgear and generators.

**Why now.**
- GB200-class racks draw 120–150 kW and synchronized training steps swing whole-cluster power by large fractions in milliseconds (general knowledge; Nvidia has announced rack-level energy storage and 800 VDC distribution for its next platforms). Utilities and ERCOT see these swings as stability risks; the 3,200 MW trip-risk finding is the regulatory expression of it.
- Electrical gear is the bottleneck ("under 10% of cost, 100% of the bottleneck"); every transformer, breaker and genset is sized for peak, not average. A buffer that cuts peak-to-average by 20–30% is a shortage-relief device for the whole electrical chain.
- The site-level answers (Tesla Megablock, Heron's solid-state transformer) are big, slow and new-build only. A retrofit-capable row-level appliance for the installed AC base is a different product.

**Hard bet.** High-cycle-life storage chemistry or capacitor design at the right energy-to-power ratio, and grid-forming converter control that coordinates hundreds of units. The engineering is power electronics and electrochemistry.

**Wedge.** One AI training campus with a documented reduction in peak draw and a utility that credits it in the interconnection study.

**Path to very large.** A per-row product in every AI data center, and the enabling hardware for Idea 6.

**Competition.** Nvidia's ecosystem partners (Eaton, Vertiv, Delta, Schneider) on the 800 VDC roadmap, Tesla, Heron. Crowded with giants; the startup position is retrofit and control software.

**What kills it.** Nvidia's reference design absorbs the function and the OEMs ship it. Mitigation: the installed base and the control layer.

### 8. Unlock the installed grid: dynamic rating twins for transformers and lines

**Pitch.** Sensors and physics-plus-ML models that compute the real, weather- and load-dependent capacity of installed transformers, lines and substations, so utilities can connect more load on existing assets and defer replacements they cannot buy anyway.

**Why now.**
- Transformer lead times are 30–36 months (up to 60 for EHV) with a projected 30% supply deficit in 2026; HV breakers ~125 weeks. The fastest transformer is the one already installed, and most run below their true thermal capacity because ratings are static and conservative.
- The regulatory analog already exists for lines: FERC Order 881 required ambient-adjusted line ratings by July 2025 (general knowledge). Dynamic transformer rating is the obvious next step and the shortage is the forcing function.
- Utilities are stuck in "death by pilot" on grid-enhancing tech (Heatmap, March 2026; LineVision has not raised since 2022). What changes the calculus is large-load tariffs: 23 states now let utilities charge data centers for grid upgrades, and a data center that can be served on existing assets is a faster, cheaper customer the utility wants.

**Hard bet.** Thermal and ageing models accurate enough that a utility will operate above nameplate on them, validated with fibre and sensor data, packaged so that a regulator accepts the rating. The engineering is power-systems physics and ML.

**Wedge.** One utility with a data-center queue and a transformer-constrained substation; deliver 15–25% more connectable load on the installed transformer with a documented rating basis.

**Path to very large.** Every substation in load-growth territory, then the planning layer that tells utilities where the next gigawatt can connect without new iron.

**Competition.** LineVision, Smart Wires (lines), Hitachi and Siemens asset-monitoring suites, utilities' in-house engineering.

**What kills it.** Pilot purgatory. Mitigation: sell it as interconnection acceleration to the data-center developer, who has the budget and the urgency, and let the developer bring the utility.

---

## Group D: The inspector shortage as a software problem

### 9. Qualified automated defect recognition

**Pitch.** Machine interpretation of ultrasonic, radiographic and visual inspection data, qualified under the ASME Section V performance-demonstration framework and accepted by owners and the NRC, so that a Level III examiner reviews exceptions instead of every image.

**Why now.**
- NDE and QC inspectors are on every shortage list (NSI, DOE UPRISE); 30 uprates, three restarts and the live construction sites compete for the same people in 2027–28. Every outage generates tens of thousands of exams.
- Automated ultrasonic acquisition is already accepted for reactor-vessel exams and performance demonstration is the established qualification route (general knowledge); interpretation is still human.
- The Lake Charles lesson: the record is the product. Machine interpretation produces an audit-proof record by construction.

**Hard bet.** Qualification through blind performance-demonstration trials to the standard the industry uses for humans, on nuclear-specific flaw sets, plus the data acquisition partnerships (robotic crawlers, phased-array systems). The engineering is signal processing and ML with a regulatory-grade validation program.

**Wedge.** One exam type (piping welds by phased-array UT) at one outage vendor, run as a second reader alongside humans, with published agreement statistics.

**Path to very large.** Nuclear is the proving ground; aerospace, pipelines and shipbuilding have the same shortage and looser regulation.

**Competition.** Mistras, Acuren, Team, Westinghouse and Framatome inspection groups (all human-centric), plus generic industrial ML vendors without nuclear qualification.

**What kills it.** Owners will not accept machine interpretation of safety-related welds regardless of data. Mitigation: second-reader deployment first, and the shortage will do the persuading.

---

## How these fit together

| # | Idea | Type | Revenue in 24 mo | Capital to first revenue | Regulatory gate | Crowding |
|---|---|---|---|---|---|---|
| 1 | Margin engine | Software | Yes (non-safety analyses) | $5–15M | NRC topical report, 2–4 yrs | Low |
| 2 | Licensing compiler | Software | Yes (one applicant) | $3–10M | NRC digital-submittal acceptance (optional) | Low-medium |
| 3 | Fleet automation | Software | Yes (non-safety systems) | $5–15M | Plant tech-spec changes | Low-medium |
| 4 | Safety chip | Hardware+software | Yes (DOE pilot) | $10–25M | NRC topical report, 3–4 yrs | Medium |
| 5 | Reactor-agnostic back half | Hardware | Partial (geothermal) | $30–80M | None directly | Medium |
| 6 | Synthetic firm power | Software+controls | Yes (one campus) | $5–15M | Utility acceptance | High, 2-yr window |
| 7 | Rack-to-grid appliance | Hardware | Yes (one campus) | $15–40M | None | High (giants) |
| 8 | Dynamic rating twins | Software+sensors | Yes (one utility) | $3–10M | State PUC rating acceptance | Medium |
| 9 | Automated defect recognition | Software | Yes (second reader) | $3–8M | ASME/owner qualification | Low |

**The one to start.** Ideas 1, 2 and 3 are the same company at different ages: a modern, qualified analysis platform (1) produces the evidence; the structured safety case (2) carries it to the regulator; the operations platform (3) monetizes it on the fleet. Start with whichever the team's first ten hires are best at, but design the data model for all three from day one. That company becomes the nuclear industry's system of record for what a plant is allowed to do, which is the most valuable position in the sector and the one no construction company can take.

**If the team wants hardware.** Idea 4 (the safety chip) is the cleanest: one product, one qualification, sold to sixty developers who all need it and none of whom want to build it.

**If the team wants the data-center side.** Idea 6, fast, with Idea 7 as the hardware that makes the guarantee real, and Idea 8 as the utility-side wedge that turns the pitch from "trust us" to "here is the rating basis."

**What is deliberately not here.** Reactor designs (66 companies), licensing genAI search (commoditized from above within 18 months), solid-state transformers (Heron, Amperesand, DG Matrix), interconnection analytics for developers (consolidating into Enverus), and generic demand response (Emerald's alliance).
