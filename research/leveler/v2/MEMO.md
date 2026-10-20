# Hardware as Software: First-Principles Memo

## Verdict

The software analogy holds, but not in the way the thesis hopes. AI makes hardware **knowledge** cheap, like a compiler or an open-source library does. It does not make **parts** free. Copies cost metal. Checking a part takes physics time. And the right to install a part is a legal status tied to a named party.

All 14 principles reach the same conclusion. When knowledge is levelled, the money moves to the next scarce layer. In hardware that layer is one of four things: permission (approvals), evidence (test and operating history), installed base (fleets and service contracts), or scarce capacity (furnaces, foundries, grid connections). The party that did the levelling rarely keeps the value: MOSIS, Linux, Docker, Xometry and GE Predix all show this. The safety control you asked for sits at the qualified line or the owned fleet, and that is also where the moat sits.

So "nothing monopolistic" is half right. Knowledge monopolies break. Permission and capacity monopolies move to whoever owns the new chokepoint. The company should be that owner.

After 3 adversarial reviews each, this is what survives:

- **One clean survivor: Airfoil Foundry, revised 19/25.** Reshaped from the pitch into a quick-turn, high-mix hot-section casting foundry for out-of-contract E/F-class industrial turbines, funded by customer prepayments.
- **Two conditional survivors, both reshaped:**
  - **Orphan Silicon Works**, revised 16-17 as pitched and 17-19 as reshaped. It becomes a buyer of orphaned electronics product lines that already carry their approvals.
  - **Keel Forge**, revised 17-18. It buys one approved naval foundry and extends into turbine castings.
- **The earlier resurrection fleet (20/25) is still the anchor.** Nine of the 14 principles independently produced it again, and several finalists only make sense as its supply chain.

## The first principles

| # | Software mechanism | Hardware analogue | Law | Who captured value historically | What AI changes |
|---|---|---|---|---|---|
| 1 | Compiler to a frozen instruction set | A stack of compilers (design, process, machine code, evidence) aimed at a characterised process with published design rules, like a chip PDK | A compiler only creates abundance once someone freezes the target. The target owner keeps the value. | TSMC (69.9% of foundry, $122.5B), Intel, AWS. Not GCC, MOSIS or CAM copilots. | Cuts the labour of each compiler stage. The compiler becomes a commodity, so the characterised, approved target becomes the scarce thing. |
| 2 | Open source and shared libraries | A shared body of qualification evidence plus a cheap equivalence pathway (generic drug ANDA, FAA PMA, nuclear commercial-grade dedication) | Reuse creates abundance only where a copy can be checked as cheaply as it is made. That is the equivalence proof, not the drawing. | Red Hat ($34B), AWS, HEICO. Not the commons. Generic drug makers were squeezed. | Building a part's data package and equivalence argument gets cheap. Approval and capacity do not. |
| 3 | Cloud (pooled, metered, API) | An owned, qualified capacity fleet behind a compiler interface: foundry, rental fleet, firm power | When capacity becomes programmable, value goes to the owner of the pooled, qualified, scarce capacity. | AWS ($45.6B operating income), TSMC, United Rentals. Not Xometry. | Makes mixed physical capacity callable (auto-CAM, fixtures, a digital traveller per part). |
| 4 | Cheap testing and CI | Delta qualification: prove a change is no worse than an accepted baseline | Things get generic where proving a change safe costs less than making it. | The owner of the trusted judge (UL Solutions, Ansys at $35B) and operators who approve themselves (SpaceX McGregor). | Surrogate models, 100% per-part inspection, auto-drafted evidence. Physics clocks stay. |
| 5 | Zero-cost copying | A qualified design file whose copies inherit the first copy's evidence, plus standard modules riding Wright's law | When copying is near free, value goes to whoever owns the permission to install the copy and the base that uses it. | Red Hat and AWS; HEICO; solar asset owners. Printer makers lost value. | Rebuilding the first copy from a scan gets cheap. Per-build process signatures arrive. |
| 6 | Interfaces and APIs (IBM PC BIOS, POSIX) | Form-fit-function equivalence plus the right to substitute | When an interface opens, value goes to the substitution-rights holder or the fleet operator. | Intel and Microsoft, HEICO (24.1% FSG margin), AWS. Not Compaq or Phoenix. | Engineering per part falls from about $50-200k to $5-20k, which opens the long tail. |
| 7 | Package managers and lockfiles | A resolver of signed, application-scoped equivalence certificates | Margin tracks the number of signed substitutes you hold, not how many parts you list. | HEICO; Intel and Microsoft. npm and Supplyframe stayed thin. | Evidence 5-10x cheaper. Approval unchanged. |
| 8 | Over-the-air updates | A control layer plus permitted operating envelope on installed assets (GE PowerUp, Tesla brakes) | Value goes to whoever holds update authority: the keys plus the liability. | Tesla, GE on its own fleet. VW Cariad lost billions. Retrofitters got one-off fees. | Writing control code for orphaned platforms gets cheap, and each unit can be tuned with ML. |
| 9 | Telemetry and A/B tests | Operating hours turned into admissible evidence (ETOPS, NRC TSTF-425, Waymo with Swiss Re) | An operating hour has value only if someone prices it, so value goes to whoever owns asset, data and risk together. | Rolls-Royce TotalCare, HSB, Waymo. Predix and Uptake lost. | Pooling evidence across mixed units, and earlier near-miss detection. |
| 10 | SaaS and recurring revenue | Owned fleets selling output (power by the hour, PPAs) | Selling output turns hardware into finance. Predictability sets the cost of capital. | AWS, Rolls-Royce, Sunrun. SolarCity was squeezed by its cost of capital. | Lower cost variance, which tightens debt spreads. |
| 11 | Abundant builders (Copilot) | Captured craft plus a few qualified physical cells (the Mead-Conway, MOSIS, TSMC split) | When craft becomes abundant, value goes to the qualified capacity that turns designs into trusted parts. | TSMC, AWS, Ford's plant. Not bootcamps. | Novice-to-median lift (+34% for novices), with Hadrian training machinists in 60-90 days. |
| 12 | Monopoly breaking by clones | OEM aftermarket locks broken by reverse engineering (PMA, Lexmark, Deere) | The monopoly moves to the approval, the evidence and the fleet. | Intel and Microsoft, AWS, HEICO, fleet operators. The clone maker kept least. | Reverse-engineering throughput rises 10-100x. |
| 13 | Containers and virtualisation | A qualified recipe plus a verification envelope that travels between machines | Portability moves value to the owner of the certified recipe library, the capacity and the sign-off right. | AWS, TSMC, Red Hat. Docker Inc. and MOSIS stayed small. | ML signatures make "equivalent" a measurable, statistical claim. |
| 14 | Builder is its own gate (EULAs) | Owner-operator authority, ODA delegation, insurer as gate (HSB 1866, UL) | A gate stands wherever harm can cross an ownership boundary. Own the asset behind your fence and you become your own gate. | Red Hat (accountability), AWS, HSB, UL, Boeing's ODA. | Continuous evidence per unit, near-zero-cost QA paperwork, underwriting at small scale. |

### Meta-laws across all 14

1. **The leveller never keeps the value.** In every domain the free layer (compiler, commons, registry, marketplace, tool) earned the least. Value landed on the next unlevelled layer. In hardware that layer is permission, evidence, installed base or scarce capacity. AI hands incumbents the same knowledge, so knowledge is never the moat.
2. **Abundance comes from cheap verification, not cheap design.** Software got abundant because trusting a change cost less than writing it. Hardware verification is held to physics clocks: creep, fatigue, operating hours. AI cuts the labour around those clocks, not the clocks. Look for categories where anchor tests plus AI evidence bring time-to-acceptance close to time-to-design-change.
3. **The gate moves inside when you own the asset.** Software's builder was its own approver. In hardware the only clean way to get the same thing is to own and operate the asset behind your own fence: owner-operator authority, commercial-grade dedication, a bought ODA, a captive insurer. This is the only reliable escape from the gatekeeper-queue law.
4. **Hardware abundance looks like generic drugs, not zero.** Expect prices of about 30-70% of incumbent list (HEICO launches at about 70% of OEM price), not near-free. The margin goes to approval holders and operators, not to the people contributing designs.
5. **Owning output is a financing technology.** Once you sell output, the winner is whoever makes fleet cash flows most predictable. Telemetry and operating history lower the cost of debt. That compounds, and incumbents cannot copy it with AI.
6. **Every sharp idea converges on one stack.** An owned fleet, plus a private AI-built parts and evidence library, plus scarce capacity feeding it. This is vertical integration in physical industry with software as the internal compiler, which is your cofounder's preferred shape. The library is a private cost advantage, never the product.

## Survivors

### 1. Airfoil Foundry (revised 19/25; average across reviewers 18.7)

**Shape.** The pitch was "repair 6B/7EA hot sections, then climb to single-crystal." All three reviewers moved it to this:

- A quick-turn, high-mix hot-section casting foundry.
- It casts the low-volume, high-part-count parts that incumbent foundries won't take: stage-2/3 nozzles, shrouds and directionally solidified (DS) stage-1 buckets for out-of-contract 6B, 7EA, 7FA and SGT-800-class frames.
- Its customers are the independent service providers (ISPs), resurrection-style fleets, new turbine entrants, and OEM overflow under prepaid take-or-pay capacity reservations.
- Repair work is bought (one regional shop) as a cash bridge. It is not the core business.

**What it owns.**
- Vacuum DS and equiaxed furnaces, ceramic core and shell printing, coating, HIP, CT and NDT. All of it is scarce and on 2-3 year equipment lead times.
- A frozen process kit per alloy and geometry family.
- A reverse-engineered data-package library.
- A per-part-number acceptance record with owners and insurers. Industrial turbines have no FAA or PMA gate, so that record is the approval.

**Wedge.** Reverse-compile a scanned part into a data package in days. Print cores and shells so no hard tooling is needed. Cast batches of 20-200. Sell first to ISPs (PSM, EthosEnergy, Allied) that lack casting capacity, and to the sister resurrection fleet as the company's own first customer.

**Ladder.**
1. Equiaxed later-stage parts.
2. DS stage-1 buckets (years 4-7).
3. Single-crystal parts and aeroderivatives (upside, not the plan).
4. An open "casting foundry" for new turbine makers who don't want to depend on GE-owned CPP.

**Key numbers.**
- Howmet holds >50% of industrial turbine blades and says major new capacity arrives in 2028-2030 because some equipment takes 2-3+ years: https://www.tikr.com/blog/howmet-aerospace-hwm-stock-drops-elon-musk-turbine-production
- 110 GW of turbine orders against 60-70 GW of capacity. Prices heading to about $600/kW, +195% since 2019. Hot-section single-crystal blades are "the most persistent constraint": https://www.power-eng.com/gas/turbines/gas-turbine-prices-climb-195-as-supply-crunch-reshapes-power-development/
- GE is buying CPP for $11.75B (about 18-26x EBITDA). SpaceX is building its own blade foundry in Bastrop: https://www.turbomachinerymag.com/view/ge-aerospace-cpp-acquisition-spacex-turbine-blade-foundry
- Casting lead times 52-80 weeks (vendor release): https://www.daily-tribune.com/online_features/press_releases/ddm-systems-ceramic-3d-printing-targets-the-gas-turbine-casting-bottleneck-in-ai-data-centers/article_cd7a6cd0-24e0-5113-b0a7-8ffdccc75c12.html
- Printed cores are already in Safran production: https://www.lithoz.com/en/lithoz-has-installed-cerafab-s65-printers-to-build-casting-parts-for-safran-aircraft-engines/
- Gas turbine services market $27.1B (2025): https://www.gminsights.com/industry-analysis/gas-turbine-service-market
- Unit economics and capital, all estimates:
  - Non-OEM hot-section market about $2-3B.
  - $100M revenue needs a 3-5% share and DS parts.
  - A DS/SX line costs about $100-200M (not the $60M pitched) and is fundable through DPA Title III, DOE and customer prepayments.

**Killer and AI answer.** The killer is tacit single-crystal and DS yield knowledge held by Howmet, PCC and GE-CPP, with a 3.5-year ramp. The AI answer:
- Printed tooling removes the 6-12 month die step.
- Solidification surrogates plus per-pour signatures make each pour an experiment, which compresses the scrap-and-retry ramp.
- AI reverse-compilation makes it economic to run hundreds of part numbers at small batch sizes.

**Reviewer objections and answers.**

| Objection | Answer |
|---|---|
| The repair wedge is crowded and PE-held (Chromalloy/Veritas, PSM/Hanwha, EthosEnergy). | Don't compete there. Sell castings to those players. |
| The new-build aftermarket is locked into OEM service agreements for 10-20 years. | The OEMs inside those agreements need castings too. Sell capacity to them. |
| Incumbent capacity lands in 2028-30, around when this line qualifies. | Lock in prepaid offtake now. The installed base keeps growing hot-gas-path demand after the shortage eases. |
| Customer acceptance needs about 24k equivalent hours on a lead unit. | Place lead sets on baseload combined-cycle units (8,000 h/yr). Sell with insurer-backed warranties and AI borescope life monitoring. |
| Incumbents can buy the same printers, so D falls to 3. | The remaining edge is speed and the high-mix niche they deprioritise. |

**Revised score.** N4 T3 C4-5 A4 D3-4 = 19, a narrow pass. It holds only if prepaid offtake covers most of the line's capex and the first DS qualification lands within about 36 months.

**Cheapest feasibility test (10 weeks, about $200-300k).**
1. Interview 20 ISPs, peaker owners and new turbine builders. Ask for a written LOI or a prepaid capacity reservation at ≥60% of OEM price.
2. Scan one retired 7EA stage-2 nozzle, produce the data package in under 2 weeks, and cast 5 units through a partner foundry using printed cores. Run dimensional and metallurgical acceptance.
3. Get furnace and coater quotes and DPA/DOE program contacts.

**Kill if any of:** fewer than 3 buyers will prepay or sign an LOI; the partner pour fails acceptance twice; furnace delivery is >30 months with no grant path.

### 2. Orphan Silicon Works, reshaped (revised 16-17 as pitched, 17-19 as reshaped; conditional)

**Shape.** The pitch was a clean-room replacement-board foundry that files DLA source approvals and sells to primes. The reviewers found that DLA review runs at human speed. They also found that primes approve and capture the margin, and the government already runs chip emulation through DLA's GEM program and DMEA. The surviving version follows the HEICO ETG and TransDigm path:

- Buy orphaned avionics and defence-electronics product lines, with their type designs, NSNs, CAGE codes, approvals and installed base, from OEMs and primes exiting low-volume legacy work.
- As OEM of record it is already the approved source. The DLA queue disappears for those part numbers.
- AI re-implements the dead ICs and boards inside the owned designs, filed as internal Class II changes.

**What it owns.** The approvals, the type designs, a sole-source position on owned NSNs, an internal emulation-core platform qualified once for environment and EMI, and side-by-side equivalence evidence.

**Wedge.** One acquired line plus line-down programs at primes, starting with non-flight-critical naval, ground and test-equipment electronics where airworthiness assurance is not on the critical path.

**Ladder.** More acquired lines. Firmware variants on the emulation core. Program-level sustainment contracts. DLA alternate-source filings as a background pipeline.

**Key numbers.**
- F-22 DMS management about $100M/yr: https://www.navsea.navy.mil/Portals/103/Documents/NSWC_Crane/SD-18/PDFs/Resources/ResourcesDMSMS.pdf
- Virginia-class about 1,440 DMSMS issues: https://www.dsp.dla.mil/Portals/26/Documents/Publications/Journal/140701-DSPJ-01.pdf
- TransDigm part profits 17% to over 4,000%: https://fortune.com/2019/05/15/transdigm-pentagon-gouging
- DLA source approval takes 12-18 months: https://ndia.dtic.mil/wp-content/uploads/2023/dla/Reverse_Engineering.pdf
- Under 10% of DLA reverse-engineering projects completed; OEMs hold about 83% of sole-source spend: https://www.gao.gov/assets/gao-26-108018.pdf
- A second source cut GE 7FA part prices 60-70%: https://www.justice.gov/atr/case-document/file/768396/dl
- Reviewer rebuild:
  - The $15-25B market figure in the pitch is unsupported.
  - An approved part earns about $100-150k/yr, so $100M needs about 700-1,000 revenue-producing NSNs.
  - Qualification costs $100-500k per LRU, so capital to $100M is about $60-120M.

**Killer and AI answer.** The killer is approval queues plus tiny volume per part. The answer is to buy approvals instead of earning them, then use one qualified hardware platform so each dead part is a firmware variant needing only a functional equivalence proof. Electronics is the one sustainment domain where software-style verification partly survives: you can run the old and new boxes side by side.

**Remaining objections.** PE (Arcline) and HEICO compete for the same lines. Analog and RF parts don't carry over to vector testing. Cost-data scrutiny caps margins below TransDigm levels.

**Cheapest feasibility test (8 weeks, about $75k).**
1. Rank DLA backorders and DMSMS notices to find 30 orphan lines.
2. Talk to 10 line owners about sale terms.
3. Have one engineer plus AI tooling re-implement one real dead TTL/PAL board on an FPGA and prove equivalence over millions of vectors.

**Kill if:** no line can be bought at ≤6-7x EBITDA, or the board equivalence takes more than 4 engineer-weeks.

### 3. Keel Forge, reshaped (revised 17-18; conditional)

**Shape.**
- Buy one succession-driven or distressed foundry that already holds NAVSEA and prime approvals.
- Fund it with seller notes, asset-based debt, and Navy SIB or DPA capex money. Day-one revenue comes from its backlog.
- In year 1, aim AI only where no requalification is needed: ML-read radiography and ultrasonic and CT to triage defects, AI-guided weld repair within approved procedures, scheduling, and LLM-drafted first-article and traceability packages.
- Use the process-signature data to earn delta-qualification for gating and rigging changes later.
- Extend into gas turbine and power-generation castings so the ceiling reaches $1B+, and feed Airfoil and the resurrection fleet.

**What it owns.** Approved melt and press capacity in a sold-out market, a cross-plant pattern and recipe library, long-lead spare castings sold on availability contracts, and the evidence history.

**Key numbers.**
- Sustainment cost pressure (Abrams maintenance up $181.3M from FY2015 to FY2023): https://www.gao.gov/products/GAO-26-108113 ; https://news.usni.org/2025/09/25/gao-report-on-weapon-system-sustainment
- Capital appetite (Hadrian raised $1.37B at about $7.9B): https://seekingalpha.com/news/4627869-defense-startup-hadrian-raises-1_37b-at-7_9b-valuation-amid-pentagon-demand
- Reviewer rebuild:
  - A $30M-revenue plant at 10-14% EBITDA costs about $21-32M at 6-9x.
  - Rework, scrap and overtime are about 15-25% of COGS.
  - Halving those costs roughly doubles EBITDA.
  - The realistic lift is 5-10 margin points, not the 10-20 yield points pitched.

**Objections.**
- Approved plants trade at 8-12x, not 4-7x.
- The qualified process is frozen, so AI gating redesign triggers requalification.
- Naval castings alone are a $1-3B niche.
- PE and Re:Build-type roll-ups can buy the same plants.

**Answers.** Target distressed and succession sellers. Work only after the pour in year 1. Add turbine castings to the plan.

**Cheapest feasibility test (6 weeks, about $50k).** Get data rooms for 3 approved targets and measure rework hours as a share of COGS.

**Kill if:** the rework share is under 15%, or the price is above 7-8x EBITDA on every target.

**How the survivors fit together.** Airfoil and Keel Forge are both scarce-capacity suppliers for the resurrection fleet. The strongest company may be the fleet with Airfoil as its in-house hot-section foundry: one vertically integrated stack in which the fleet is the first customer, the evidence generator and the moat.

## Killed or below the line

- **Stampworks (17.3, not refuted, parked).**
  - Margin is overstated: realistic stamped-fab EBITDA is 16-21%, because welding is a small share of cost.
  - Transformer tanks are not the transformer bottleneck.
  - Strategics are taking the data-centre module rung.
  - It survives only as a NAVSEA-first heavy-weld shop. Pursue it only if a NAVSEA-qualified shop can be bought early.
- **Gridright (16).** Sellers know their interconnection rights are worth $700-1,000/kW. Owners can convert their own boilers. Accredited MW are 20-35% below nameplate, and the capacity cap is temporary. AI does not answer site competition. Its best use is as a deployment channel for the resurrection fleet.
- **RAID Power (16.7, one refutation).** Enchanted Rock and VoltaGrid already run this exact model. Truck-block supply is open to every competitor. There is no permission moat.
- **Gridiron (14.7, two refutations).** Remanufactured distribution gear already ships in 1-4 weeks from Maddox and Sunbelt Solomon. The "2-4 year queue" applies only to large units, so renting can't beat buying. Fold large-transformer rewind into the fleet as internal supply.

## Full ranking

| Idea | Sector | Total | One-line rationale |
|---|---|---|---|
| Airfoil Foundry | Gas turbine hot-section parts | 20 (rev 19) | Scarce furnaces plus evidence. Reshaped to a high-mix prepaid foundry. |
| Gridright | Coal/steam repowering | 19 (rev 16) | Real permission moat, but sellers price in hope and AI is not the unlock. |
| Orphan Silicon Works | Defence obsolete electronics | 19 (rev 16-17) | Survives as buyer of orphaned OEM-of-record lines. |
| Keel Forge | Naval castings/forgings | 19 (rev 17-18) | Bought approvals plus capacity. Yield claim overstated. |
| Stampworks | Robotic code-stamped fab | 19 (rev 17) | U-stamp is common. Moat only at NAVSEA rung. |
| Gridiron | DC electrical gear rental | 19 (rev 15) | Reman supply already instant. Rental can't beat buying. |
| RAID Power | Modular gas engine fleet | 18 (rev 17) | Model already run by funded fleets. D fails. |
| Rewound | Transformer rewind fleet | 18 | Good payback, but RESA/OEMs/rental fleets copy. |
| Isotope Equivalents | Nuclear spares bank | 18 | Own-approver fit. Ceiling small. |
| HotHour | Engine-hour utility | 18 | FTAI-proven, but capital competition for feedstock. |
| Mainline Silicon | Legacy control cards | 18 | Strong shape. Time to 3,000 SKUs too long. |
| Old Interconnect | Orphan solar POIs | 18 | Owned POIs scarce, but crowded hunt. |
| Nuclear Generics | Nuclear valves/pumps | 18 | Self-approving dedication. Fleet too small. |
| Orphan Compression | Legacy compressors | 18 | Proven asset class. AI lift marginal. |
| Breakerbank | Switchgear retrofill pool | 18 | High-power lab queues and crowded retrofill. |
| Jones Act Resurrection | US-flag shipping | 18 | Vetting age limits are the killer, not spares. |
| Exchange | Telecom COs to inference | 18 | Powered shells real. Heavily contested. |
| Flexgrid | DC backup as flexibility | 18 | Killers answered by contracts, not AI. |
| Lazarus Storage | Orphan BESS fleet | 18 | AI central, but distressed supply thin. |
| Nucleon Foundry | Nuclear components | 17 | ASME/NRC queues gate it. |
| Second Holston | Energetics plant | 17 | Real bottleneck, $300-800M capex. |
| Generic Ordnance | Second-source fuzes | 17 | LPTA pricing, lot-acceptance limits. |
| Standard Motor Architecture | Solid rocket motors | 17 | Each program qualifies its own motor. |
| Gridiron Rental | Large transformer rental | 17 | Shortage eases, fleet out-capitalised. |
| Shuttle Foundry | Mature-node fabs | 17 | China pricing and capital, not AI. |
| Ghost Fleet Autonomy | Unmanned logistics hulls | 17 | Crew removal is a regulator queue. |
| Hull PDK Foundry | Ship blocks | 17 | Barges are a commodity. Class process approval has no precedent. |
| Breakwater Power | Floating power | 17 | Host politics kill it (A=2). |
| Fenceline Rail | In-plant autonomous rail | 17 | Escapes FRA, but slow per-site sales. |
| Second Life Pipeline | Repurposed pipelines | 17 | Thin water tariffs, easement litigation. |
| Kilovolt | 800 VDC solid-state power | 17 | Balance-sheet circularity, funded rivals. |
| Foundry Zero | Non-Chinese cell line | 17 | Heavy capex, thin "fabless battery" market. |
| Grid Socket | Coal sites to thermal storage | 17 | Sites bid up. Thermal tech not AI (A=2). |
| Steam Commons | Industrial heat utility | 17 | Thin margins, R-stamp not a moat. |
| Blue Foundry | Allied drone components | 17 | Approvals shared with rivals, crowded. |
| Hartford Shield | Sabotage insurer-operator | 17 | Fronting appetite, copyable by Chubb/HSB. |
| Upgrade Capital | Nuclear uprate MW | 16 | Tiny single-unit pool. NRC topical queue. |
| Jointworks | Robot actuator foundry | 16 | Chinese price squeeze, captive OEMs. |
| Gatehouse Labour | Humanoid labour utility | 16 | Humanoid productivity not yet there. |
| Rotable Pool | Gearbox exchange | 16 | Orphan wind cohort being repowered away. |
| Tonne Utility | Autonomous haulage | 16 | Thin contract-mining margins, retrofit sold as service. |
| Iron Exchange | Heavy-iron aftermarket | 16 | No permission gate, so no moat (D=2). |
| Tributary Water | Small water utilities | 16 | Rate-case queues, PE roll-ups present. |
| Terminus PFAS | PFAS destruction hubs | 16 | Landfill and incineration set a low price ceiling. |
| Overwatch Utility | Shared counter-UAS | 16 | Statutory authority is a gate (A=2). |
| Grid Reserve | Strategic transformer spares | 16 | Low willingness to pay, Grid Assurance exists. |
| Steamworks | Owner-user boiler/CHP | 15 | Small tickets, copyable. |
| Rotable Grid | Substation component pool | 15 | No regulator, so no approval moat (D=2). |
| Ghost Wing | Retired military jets | 15 | Incumbent-gated task orders, $1B ceiling. |
| Heritage | Space electronics evidence | 15 | Small market, public databases overlap. |
| Reborn Jets | Orphan business jets | 15 | Avionics retrofits already exist (A=2). |
| Second Shift | Used robot cells | 15 | Commodity arms, field-install wall. |
| Flow Utility | Municipal pumps | 15 | ESCO in disguise, municipal procurement. |
| Liftwell | Elevator owner-operator | 15 | Open controllers already exist. Labour gate. |
| Codehome | HUD-code housing | 15 | Land, not design, binds. REIT-held. |
| Heatwell | Heat-pump thermal utility | 15 | LL97 softened, per-building contracts. |
| Garrison Water | Base water privatisation | 15 | Multi-year award queue, incumbents. |
| Substrate | Private HV substations | 14 | Infrastructure finance, no moat. |
| CoreBank | Reclaimed GOES | 14 | Reclaimed steel grades inferior. Moat only at $300M rung. |
| Free Rotor | Soviet-origin sustainment | 14 | Allied pool shrinking. |
| OrbitFab | Payload hosting fleet | 14 | Loft ahead. Weak economics. |
| Custody | Spent fuel ISFSIs | 13 | DOE damages repay actual costs, so no spread. |
| Munitions Reserve Utility | Private stockpile | 13 | Title and release authority are government. |
| Horsepower Utility | Locomotive leasing | 13 | Mature, oversupplied market. |

## Caveats

1. **Search budget.** The shared web-search budget ran out during scoring and verification. Most scores and many numbers come from the cited sources plus prior knowledge, flagged "est." or "recalled". Re-verify these before any pitch: Howmet capex, CPP multiples, HEICO ETG revenue, approved-plant EBITDA multiples, and furnace lead times.
2. **Same-model review.** Scorers and reviewers are the same model family. Reviews were adversarial but not independent of shared blind spots. No reviewer had customer conversations. The feasibility tests above are the real check.
3. **Window risk.** Airfoil, Keel Forge and the resurrection fleet all lean on a 2025-2030 shortage. Incumbent capacity (Howmet, Caterpillar tripling, OEM transformer plants) lands in 2028-30. Each survivor needs a case that holds after the shortage: installed-base aftermarket, approvals, prepaid offtake.
4. **YC fit.** All three survivors are capital-heavy and partly PE-shaped (acquisitions, debt, grants). That is honest about where hardware value sits, but the pitch must show AI as the reason the economics close, not just a layer on top of a roll-up.
5. **Thesis tension.** "Nothing monopolistic" conflicts with "own the chokepoint". The memo's answer is that AI ends knowledge monopolies and you should hold the permission or capacity position that replaces them, priced at generic levels (about 60-70% of OEM). Be ready to defend that framing to partners.
6. **Scope.** Per the rules, Terranox and any prospecting or drilling ideas were excluded. Tonne Utility is haulage only.
7. **The anchor was not re-verified.** The resurrection fleet (20/25) was not adversarially re-tested in this run. It was only regenerated independently by 9 of 14 principles. Give it the same 3-lens review before treating it as settled.