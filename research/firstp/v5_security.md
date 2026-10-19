# V5 security and defense-tech sweep (19 Oct 2026)

Frame: `V5_OPTIMIST.md`. Assume the technology works and judge the numbers and the clock. Each vertical killer needs an AI counter-move with its effect on the numbers stated. Scores are N/T/C/A/D, each out of 5. An idea passes at 19+ with no leg below 3. Rules as before: no prospecting or drilling, and we own the product, the supply or the qualified position, not a service.

What died before in this sector, and why that matters here:
- Orphan sole-source parts (13-15) and DLA surplus spares (15-17) died on L2 (DIBBS, SAM and FLIS are public), on L6 (small PMA shops and DLA second-sourcers hold the rung), and because requalification dominated the cost.
- The SBIR-to-program-of-record NewCo (14) died because the gate is program-office pull, not discovery.
- The energetics line was excluded on a safety flag. It is treated here only at the level of a business (capacity, contracts, qualification), with no process chemistry.

V5 changes two things in this sector. First, requalification is the killer, and AI can now be scored as compressing it. Second, the market moved. The FY27 request has about $70.5B for missiles and munitions plus $1.6B for secondary and tertiary suppliers. The Office of Strategic Capital (OSC) asks for $20.2B in credit. Hadrian raised at $7.87B and Castelion at $13B. Capital is no longer what holds the rung in defense hardware. Qualification, and the time it takes, is.

## Ranked table (37 ideas)

| # | Idea (one line) | Vertical killer(s) | AI counter-move, with quantified effect | Rough numbers | N | T | C | A | D | Sum |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Breakout: an AI-native second source for sole-source defense spares** (become the 2nd approved source on thousands of high-spend NSNs, then add FAA PMA: a HEICO built for DoD) | Source approval (SAR/RPPOB) takes 12-18 months; reverse engineering (RE) costs ~$100-250k per NSN; incumbents cut price where they meet competition; small lot sizes | CT scan, alloy ID and a generative technical data package (TDP) cut RE cost from ~$150k to ~$20-30k per NSN. Auto-drafted SAR packages take submission from ~6 months to ~4-6 weeks. A first-pass-complete package should cut rejection loops. A prioritizer on DIBBS/FPDS award history picks NSNs where sole-source price × annual buy is largest | DLA Aviation $5.2B sales FY24; DLA revenue $51.8B FY25. TransDigm sales ~$8.8B at 54% EBITDA; the IG found margins of 17-4,451% on sole-source spares. $100M = ~770 NSNs at $130k/yr | 4 | 4 | 5 | 4 | 4 | **21** |
| 2 | **Second Source Munitions: the sub-tier of energetic and electromechanical munition components** (initiators, igniters, thermal batteries, safe-and-arm/fuzes, CAD/PAD, gas generators) | Qualification takes 3-5 yrs (MIL-STD-1316/1901 safety review, lot acceptance); primes pick suppliers; explosives licensing; incumbents are single sources | Model-based qualification (digital twin of environmental tests, auto-built qualification data packages) cuts physical qualification test articles ~30-50% and qualification time from ~4 to ~2 yrs. Build-to-print of government-owned TDPs gives revenue in year 1-2. Vision QC and automated lot acceptance cut direct labour ~40% | $70.5B missiles and munitions FY27 request; $1.6B line for secondary and tertiary suppliers; missile buys up 188%. Sub-tier is ~10-15% of BOM, so ~$7-10B/yr (derived) | 4 | 4 | 4 | 4 | 4 | **20** |
| 3 | **Lazarus Silicon: AI-recreated drop-in replacements for obsolete ICs in fielded weapons** (own a catalogue of form-fit-function parts, priced on value) | NRE of ~$1-2M and 12-24 months per part; QML/screening; low volumes; Rochester's licensed die bank | Datasheet, die imagery and golden-unit vectors go to RTL to FPGA or structured ASIC, with auto-generated test and equivalence checks. NRE falls to ~$150-300k and ~3 months, so a part needing only ~$400k of lifetime buy is now worth doing (before, ~$3M) | Rochester ~$275M revenue (est.). DoD sustainment is ~70% of lifecycle cost (vendor claim). Charge $250k-1M NRE plus $500-5,000 per unit, against board redesigns costing $1-10M | 4 | 4 | 4 | 4 | 4 | **20** |
| 4 | **Modular energetics plants (RDX/HMX, TNT, IMX fill) under government-funded facility contracts** | Capex of $400-600M per plant; siting and safety; one buyer; lot qualification | Continuous small-volume production with AI process control cuts energetic held in process ~90%, which shrinks quantity-distance siting and lets one plant be several modules. Staffing falls to ~1/3. In-line process analytics cut lot acceptance testing time | Nitradyn: $581M for an IMX-104 plant (8M lb/yr). Repkon: $435M TNT plant. Holston is the only RDX source. Army munitions $36.6B FY27. Critical Materials Group seed $10.3M | 4 | 3 | 4 | 4 | 4 | **19** |
| 5 | **AI-run sovereign foundry for qualified castings** (submarine valves and pumps, turbine hot section, munition bodies) | First-article qualification (NAVSEA, OEM) takes 4-6 pour iterations; tooling lead times; pattern-maker labour; PCC/Howmet hold aero | Solidification simulation plus ML gating design gets first-time-right pours, cutting FAI loops from ~5 to ~2. Printed sand moulds remove tooling (lead time 20 weeks to 3). AI X-ray/CT inspection. ~50% fewer people per ton | Congress gave >$5B to the submarine industrial base FY18-25 (260 suppliers, many sole source). Hadrian $7.87B (machining). Rangeview has Navy and Kratos work; Fabri $13.5M; Radian Forge $2.5M | 3 | 4 | 5 | 4 | 3 | **19** |
| 6 | Bearings and precision motion second source (RBC/Timken-style aero-defense bearings) | Bearing qualification; incumbents' installed base | AI fatigue and life modelling cuts endurance test hours ~40% | RBC Bearings is a $10B+ company built on this niche (memory) | 4 | 3 | 4 | 3 | 3 | 17 |
| 7 | Thermal batteries and munition power sources as a single product line | EaglePicher sole source; ~$300-500M market | Electrochemical modelling cuts the cell-stack development matrix ~60% | Sole-source Navy HARM award; small TAM. Fold into #2 | 4 | 4 | 3 | 3 | 3 | 17 |
| 8 | Ammonium perchlorate second source | AMPAC is the sole North American source; $100M expansion; small TAM | Process twin for qualification | ~$300-500M market (estimate). Fold into #4 | 3 | 3 | 3 | 4 | 4 | 17 |
| 9 | Space-qualified multi-junction solar cells, third US source (vs Spectrolab, Rocket Lab/SolAero) | AIAA S-111 qualification; germanium substrates; duopoly | Accelerated-life ML cuts qualification ~12 to ~6 months | Proliferated LEO adds demand; market ~$1-2B (estimate) | 3 | 3 | 3 | 4 | 3 | 16 |
| 10 | Rad-tolerant COTS through AI lot screening ("upscreened" parts with a certificate) | Customer trust; liability | ML on test and beam data predicts single-event latch-up by lot, cutting beam time ~70% | Rad-hard market ~$1.9B (2026); Zero-Error, Magics | 4 | 4 | 3 | 3 | 2 | 16 |
| 11 | Legacy circuit-card depot turned product (AI RE of boards, sold as a new LRU) | Depot work is a service; OEM data rights | Board X-ray to schematic to BOM refresh, cutting RE cost ~70% | Overlaps #1 and #3 | 3 | 4 | 3 | 4 | 3 | 17 |
| 12 | NDAA-compliant drone propulsion stack (magnets, motors, ESCs) | Price against China; crowded | Motor design optimisation | Drone Dominance $1.1B, 200k+ sUAS; OSC $820M to PDW; Hoverfly, Unusual Machines | 3 | 5 | 3 | 2 | 2 | 15 |
| 13 | Low-cost interceptors and cruise missiles | Crowded with funded leaders | Design automation | Castelion $13B, Anduril, Zone 5 | 3 | 4 | 5 | 2 | 2 | 16 |
| 14 | AI-run solid rocket motor factory | Crowded; Anduril/Adranos at full rate | Process control | Ursa Major, X-Bow, Firehawk ($60M C), Anduril ($43.7M DPA) | 3 | 4 | 4 | 3 | 2 | 16 |
| 15 | Rare-earth magnet plant | Crowded; $900M+ per 10kt plant | Process ML | Vulcan $620M OSC loan, $2B valuation; MP has the same target | 2 | 3 | 5 | 2 | 2 | 14 |
| 16 | Gallium/germanium recovery from US industrial residues (not mining) | L9 policy premium (export pause ends 27 Nov 2026); small market | Hydromet process ML | DoW $150M into ATALCO; Found Industries; Supra $2M | 3 | 3 | 3 | 3 | 3 | 15 |
| 17 | Germanium-free chalcogenide IR optics plus thermal cores for drones | Teledyne FLIR scale; China price | Freeform optical design automation | Thermal market ~$5-8B (estimate) | 3 | 4 | 4 | 3 | 3 | 17 |
| 18 | Titanium powder from scrap for defense AM | IperionX ahead; capex | Alloy ML | US has no primary sponge since 2020 | 3 | 3 | 4 | 2 | 3 | 15 |
| 19 | Tungsten penetrator feedstock from scrap | China export controls (L9); niche | Sorting ML | ~$1B US (estimate) | 3 | 3 | 3 | 3 | 3 | 15 |
| 20 | Antimony trisulfide and primer chemicals from recycling | Tiny market | — | <$100M | 3 | 3 | 2 | 2 | 3 | 13 |
| 21 | Owned microgrids on DoD installations (energy-as-a-service) | A yield business (L12) | Dispatch ML | Ameresco holds it | 3 | 3 | 3 | 3 | 2 | 14 |
| 22 | AI-native OT security for utilities | Software crowd (Dragos, Claroty) | Agentic triage | Not ownership of a scarce thing | 3 | 4 | 4 | 2 | 2 | 15 |
| 23 | Owned substation physical-security and drone-detection network, sold as a service | Utility capex cycles | Sensor fusion | DroneShield, Dedrone/Axon | 3 | 3 | 3 | 3 | 2 | 14 |
| 24 | Commercial space domain awareness constellation | Crowded (LeoLabs, Slingshot) | — | — | 2 | 3 | 4 | 2 | 2 | 13 |
| 25 | AI-native shipyard for unmanned surface vessels | Saronic, Blue Water | Robotic welding | — | 2 | 4 | 5 | 2 | 2 | 15 |
| 26 | Second source for submarine valves and pumps | Same as #5; NAVSEA qualification | As #5 | Fold into #5 | 3 | 3 | 4 | 4 | 3 | 17 |
| 27 | GOES electrical steel second source | $1B+ capex; L9 | — | Cleveland-Cliffs sole | 2 | 2 | 4 | 2 | 3 | 13 |
| 28 | Hypersonic ground-test capacity sold by the hour | Small market; government ranges | — | ~$1B | 3 | 3 | 2 | 3 | 3 | 14 |
| 29 | SBIR-to-program-of-record product factory | Program pull (died as N9) | Proposal agents | — | 2 | 3 | 3 | 2 | 2 | 12 |
| 30 | Sovereign PAN carbon-fibre precursor for missiles | Hexcel/Toray; capex | — | — | 2 | 2 | 4 | 2 | 3 | 13 |
| 31 | Chip-scale atomic clocks and assured PNT hardware | Microchip near-sole; niche | MEMS design ML | ~$0.5-1B | 3 | 3 | 3 | 3 | 3 | 15 |
| 32 | Non-China cells for military batteries (BB-2590 class) | Cell scale economics | — | — | 2 | 4 | 3 | 2 | 3 | 14 |
| 33 | Munitions demil with recovery of energetics | Small; permits | — | — | 3 | 3 | 2 | 2 | 3 | 13 |
| 34 | Beryllium and specialty alloy second source | Materion; toxicity | — | — | 2 | 2 | 3 | 2 | 3 | 12 |
| 35 | Qualified fasteners and fittings second source | Low price per unit; PCC/TransDigm | As #1 | Fold into #1 | 4 | 4 | 3 | 4 | 3 | 18 |
| 36 | Owned counter-UAS layer at critical infrastructure (sensors plus effectors, subscription) | Legal authority to mitigate | Fusion | — | 3 | 3 | 4 | 2 | 2 | 14 |
| 37 | Space-qualified electronics boards second source (power conditioning units, star-tracker electronics) | Crowded bus makers | — | — | 3 | 3 | 3 | 3 | 2 | 14 |

Five ideas pass, at 21, 20, 20, 19 and 19, all with every leg at 3 or above. Several near-misses (#6, #7, #8, #11, #26, #35) are better treated as product lines inside the winners than as separate companies.

---

## 1. Breakout: AI-native second source for sole-source defense spares (21: N4 T4 C5 A4 D4)

**Thesis.** TransDigm makes ~$8.8B of sales at ~54% EBITDA, mostly by being the only approved source on proprietary aerospace parts. The DoD IG found margins of 17-4,451% on 46 sole-source parts it sold to DLA. DoD has a formal path to break these monopolies: SAR and Alternate Offer, plus DLA Aviation's RPPOB reverse-engineering programme. The path stalls because each NSN costs ~$100-250k and 12-18 months of engineering. Breakout makes that engineering nearly free. It then *owns approved-source status* on thousands of NSNs, each a small, durable, qualification-locked franchise. That is HEICO's model (FAA PMA), pointed at DoD first and then at commercial aviation.

**Market.** DLA Aviation had $5.2B of sales in FY24, and DLA revenue was $51.8B in FY25, most of it not hardware. Service-direct depot buys and primes' spares programmes add more. Working assumption: **~$10B/yr of sole-source or limited-source hardware spares** across DLA and the services. This is derived, not sourced, so it is check #1. Commercial PMA (HEICO's Flight Support Group) roughly doubles the pool once the same engine runs on FAA parts.

**Price.** Enter 25-40% below the incumbent's price. That leaves 45-55% gross margin, because sole-source prices carry 2-40x margin over cost.

**Unit economics per NSN.** The prioritizer (DIBBS awards, FPDS and FLIS, all public) selects NSNs with ≥$200k annual buy and price/weight or price/complexity outliers.
- Cost to qualify: CT, materials and TDP ~$15k, SAR package ~$5k, first articles ~$10k, so **~$30k against ~$150k legacy**.
- Win ~50-70% of the buy. **Average revenue ~$130k per NSN per year** at ~45% gross margin, or ~$58k of gross profit. Payback is under 1 year after approval.
- The pipeline turns the clock into a throughput problem. At 400 submissions/yr and ~60% approval, about 240 NSNs are added per year.

**AI counter-moves, in numbers.**
- (a) RE cost falls ~5x, so the number of economic NSNs grows from those with >$1M buy (a few thousand) to those with >$200k (an estimated 5-10x more).
- (b) Packages are complete on first pass, so fewer government rejection loops. Assume approval median falls from 15 to ~9 months. This is a hypothesis, check #2.
- (c) Lights-out 5-axis cells (or Hadrian-style contract machining at first) put labour at <15% of COGS.

**Timeline to $100M.**
- Year 1: build-to-print on already-competed NSNs for a past-performance record. ~$3M, plus the first 150 submissions.
- Year 2: ~120 approvals, $15M.
- Year 3: $40M.
- Year 5: ~800 NSNs, **$100M+**.
- Year 7: add PMA. ~$300M at 25% operating margin, against TDG/HEICO multiples of 25-30x EBITDA, gives a credible $2-5B path. Ceiling is $10B+ (TransDigm and HEICO are each tens of billions; memory, verify).

**Capital path.** Seed $15M (CT lab, prioritizer, first 150 packages). Series A $50M (2 machining cells, AS9100). Series B $150M (scale, PMA). About $215M to cash-flow positive. That is raisable in the 2026 market (Hadrian $1.37B Series D). OSC loans could fund cells.

**Competitors.** HEICO (commercial PMA, some defense). Small RE shops (Elevate Systems, Novineer's NoviVision AI-RE). Intropy ($11M seed, spares software). SkySelect ($9M, procurement). TransDigm is the target, not a competitor. Nobody is visibly running AI-RE at volume *and* holding the approvals.

**Kill risks.**
1. Government engineering support activities (ESAs) remain the bottleneck at 12-18 months whatever the package quality. That halves the ramp, and the T leg goes to 3.
2. Incumbents cut prices on attacked NSNs. TransDigm has done this. It also gives DLA leverage, but it shrinks the prize per NSN.
3. Data-rights or IP litigation over RE'd proprietary designs.
4. Average buy per NSN is smaller or lumpier than $130k.
5. The previous kill (L2, L6) still applies if ordinary RE shops get the same AI tools. The defence is volume of approvals held, which takes time to copy, so D stays at 4, not 5.

**Cheapest test.** Pull 3 years of DIBBS sole-source awards for one FSC group (e.g. 1560 airframe structural parts). Size it as NSN count × annual $ at ≥$200k. Price RE of 5 sample parts with a CT vendor. ~$40k, 6 weeks. Kill if fewer than 2,000 NSNs clear $200k/yr across DLA.

---

## 2. Second Source Munitions: sub-tier components (20: N4 T4 C4 A4 D4)

**Thesis.** Missile and munition prime contractors cannot meet a 188% jump in demand because sub-tier parts are single-sourced, and the FY27 request names $1.6B for secondary and tertiary suppliers. The company owns qualified production of the small energetic and electromechanical parts every round needs: initiators and squibs, igniters, thermal batteries, safe-and-arm devices and fuzes, cartridge- and propellant-actuated devices, gas generators. These parts are cheap per unit, safety-critical and slow to qualify, so whoever qualifies first holds the position for the whole programme life.

**Market.** $70.5B for missiles and munitions in the FY27 request (Army $36.6B, Navy $22.6B, Air Force $11.3B). At ~10-15% of BOM in these sub-tier families, that is **~$7-10B/yr** (derived), plus allied (FMS and European rearmament).

**Price and unit economics.** Initiators ~$50-500, fuzes and S&A devices $500-5,000, thermal batteries $2k-20k (estimates; check). Expect 35-45% gross margin at rate. One line of 50-100k units/yr gives ~$25-60M revenue. Capex is ~$40-80M per explosives-licensed product line and is largely fundable by DPA Title III or IBAS (Anduril got $43.7M of DPA money for SRMs).

**AI counter-moves.**
- (a) Model-based qualification: a physics twin of shock, vibration, thermal and aging, used to plan the minimum physical test matrix and auto-build qualification data packages. Assume ~30-50% fewer qualification articles and a 4-yr qualification cut to ~2.
- (b) Build-to-print first. The Army owns many fuze and initiator TDPs, so revenue starts in years 1-2 while proprietary qualifications run.
- (c) Automated lot acceptance (vision, X-ray and electrical) and agentic production planning cut direct labour ~40%, so a 60-person site does what a ~100-person site does.

**Timeline.** Year 1-2: first build-to-print awards, $5-15M. Year 3: 2-3 qualified lines on programmes of record. Year 5-6: **$100M**. Year 8: $400M+.

**Capital.** Seed $20M, A $75M, B $150M, plus DPA/OSC money of $50-150M.

**Competitors.** L3Harris/Aerojet, Chemring (Pacific Scientific EMC), EBAD, Kaman/Arotech fuzing, EaglePicher, Reynolds Systems. Anduril and Firehawk integrate vertically for their own needs. Few venture-backed pure-play sub-tier companies.

**Kill risks.**
1. Primes refuse a startup because of qualification risk on the programme. Mitigation: DoD now funds second sources directly.
2. A ceasefire or budget reversal: the FY27 $350B reconciliation part is not enacted.
3. An explosives incident.
4. Being "ancillary" caps the ceiling at about Chemring scale (low $B) unless the platform spans many families. That is why C is 4.

---

## 3. Lazarus Silicon: AI-recreated drop-in obsolete ICs (20: N4 T4 C4 A4 D4)

**Thesis.** Fielded systems are 20-50 years old. Their chips last ~10 years. Today an obsolete IC means a lifetime buy, an aftermarket gamble (counterfeits) or a board redesign costing $1-10M. Rochester Electronics (~$275M revenue, estimate) remanufactures only where the original maker licensed it. For everything else, Lazarus makes a functional clone and owns the catalogue. Each part is a sole-source position on a platform with decades left.

**Market.** DoD and allied DMSMS resolution for electronics, plus the same problem in commercial aviation, nuclear instrumentation and control, rail signalling and industrial control. Working assumption: ~$3-5B/yr spent resolving electronic obsolescence across these (estimate; check against the DMSMS SD-22 and IDA D-5770 cost factors).

**Price.** NRE of $250k-1M per part to the programme (versus $1-10M to redesign), plus $500-5,000 per unit.

**Unit economics.** AI NRE cost ~$150-300k. Gross margin on units 60%+. A good part earns $1-3M of lifetime revenue.

**AI counter-moves.** Datasheet parsing, die delayering imagery, golden-unit vectors, then RTL. Formal equivalence and auto-generated test benches. The part goes to an FPGA or structured ASIC (SkyWater rad-hard 90nm for space). This takes NRE from ~$1-2M and 12-24 months to ~$150-300k and ~3 months. The breakeven lifetime buy falls ~6x, which opens the long tail of parts the market ignores today.

**Timeline.** Year 1: 20 parts for DMSMS offices via SBIR or OTA, $3M. Year 3: 200 parts, $30M. Year 5-6: 800+ parts, **$100M**.

**Capital.** ~$100M total (test labs, QML screening partner). No fab.

**Competitors.** Rochester, GDCA, Teledyne e2v HiRel, and boutique FPGA-emulation houses.

**Kill risks.**
1. Qualification authorities require full re-test per platform, which raises NRE.
2. Analog and mixed-signal parts resist the AI method, leaving maybe half the long tail.
3. OEM IP claims against the clones.

---

## 4. Modular energetics plants under government-funded facility contracts (19: N4 T3 C4 A4 D4)

**Thesis.** The US has one RDX source (Holston), one military nitrocellulose source (Radford) and, until Repkon's plant (due ~Nov 2028), no TNT production. The Army is paying private firms to build plants: Nitradyn got $581M for an IMX-104 plant of ~8M lb/yr, and Repkon $435M for TNT. The Army also wants an RDX/HMX centre of excellence at Blue Grass. That one comes with *no* government operating funds, and bidders must price over 5 and 10 years. So the government carries most of the capex, and the startup owns the operator position and the offtake. Business level only.

**Market.** Plant contracts of ~$0.4-0.6B each. Revenue: if a plant of ~8M lb/yr sells at $15-30/lb (an estimate; check against the Nitradyn award), that is ~$120-240M/yr. Three to five plants gives a $0.5-1B revenue company. NATO demand adds to that.

**AI counter-moves.**
- Continuous, small-volume production under AI process control cuts in-process energetic inventory by ~90%. That shrinks siting distances, so the plant becomes modules on smaller sites. Capex per lb of capacity is assumed ~30% lower (to verify).
- Staffing falls to ~1/3.
- In-line analytics shorten lot acceptance.

**Timeline.** 2-3 yrs to pilot-lot revenue; first plant around 2029; **$100M around year 6**. T is 3.

**Capital.** Seed/A of $10-60M (CMG's seed was $10.3M), then facility money from the government.

**Competitors.** BAE (Holston and Radford operator), Nitradyn (Paligen + Dyno Nobel JV), Repkon, Nitro-Chem, CMG, plus European suppliers (Eurenco, Nammo, Chemring).

**Kill risks.**
1. Awards go to incumbent-backed JVs, not startups.
2. One buyer sets the price.
3. Safety or permitting delays.
4. Demand falls after the war.

---

## 5. AI-run sovereign foundry for qualified castings (19: N3 T4 C5 A4 D3)

**Thesis.** Castings and forgings are the named bottleneck for submarine production. More than $5B went to the submarine industrial base in FY18-25, and the FY26 NDAA flags castings and forgings. They are also a bottleneck for turbine engines and munitions. The foundry owns qualified part numbers, as Breakout does, but upstream.

**Market.** The US defense share of castings and forgings is an estimated ~$10B+/yr (check). Turbine superalloy castings are a ~$10B+ global market held by PCC and Howmet.

**AI counter-moves.**
- Simulation plus ML gating design cuts first-article pour iterations from ~5 to ~2, saving ~6-9 months per part number.
- Printed sand moulds remove tooling, cutting lead time from ~20 weeks to ~3.
- CT/X-ray AI inspection.
- ~50% fewer workers per ton.

**Unit economics.** Gross margin of 30-40% on Navy and Kratos-type work. Capex is ~$30-50M per foundry.

**Timeline.** First revenue in year 1 (replacement castings for repair and overhaul, as Rangeview is doing). **$100M by year 5-6**.

**Capital.** ~$150-250M to 3 foundries.

**Competitors.** Rangeview, Fabri ($13.5M), Foundry Lab, Radian Forge ($2.5M), J.F. Lehman's Forged Solutions roll-up, PCC and Howmet. Hadrian could integrate upward.

**Kill risks.**
1. The space is crowded with near-identical startups, so D is 3.
2. Metallurgy qualification by NAVSEA stays slow.
3. Margins look like a job shop's unless the foundry holds sole-qualified positions.

---

## Sources
- DLA FY25 annual report: https://www.dla.mil/Info/Annual-Report ; DLA Aviation fact sheet: https://www.dla.mil/Customer-Support/Brochures/Details/Article/4281979/aviation-fact-sheet/
- DoD IG on TransDigm (DODIG-2019-060): https://media.defense.gov/2019/Feb/27/2002093709/-1/-1/1/DODIG-2019-060.PDF ; TransDigm FY25 Q4: https://www.sec.gov/Archives/edgar/data/1260221/000126022125000078/exhibit991tdg2025q4earning.htm
- DLA RPPOB/SAR timelines: https://ndia.dtic.mil/wp-content/uploads/2024/dla/Tue_Breakout_SAR_RPPOB.pdf ; GAO-19-586: https://www.gao.gov/products/GAO-19-586
- FY27 munitions: https://breakingdefense.com/2026/04/the-pentagon-wants-a-188-percent-bump-for-missile-procurement-can-industry-deliver/ ; https://www.janes.com/defence-intelligence-insights/defence-news/industry/pentagon-budget-2027-us-navy-bolsters-munitions-funding
- OSC: https://www.everycrsreport.com/reports/IF13215.html ; https://defensescoop.com/2026/04/06/pentagon-office-strategic-capital-loan-program-budget-increase/
- Energetics: https://thedefensepost.com/2026/09/14/nitradyn-insensitive-munitions-production-kentucky/amp/ ; https://san.com/cc/army-awards-435m-contract-for-kentucky-tnt-plant-first-in-decades/ ; https://newsite.thedefensepost.com/2026/03/17/us-explosives-hub-kentucky/ ; https://www.janes.com/defence-intelligence-insights/defence-news/industry/critical-materials-group-announces-usd103-million-in-seed-funding-to-advance-energetics-production
- AP: https://www.newmarket.com/news/2025/04/newmarket-corporation-announces-approval-of-ampac-expansion/
- Hadrian: https://news.bloomberglaw.com/private-equity/defense-startup-hadrian-valued-at-7-87-billion-in-new-round ; Castelion: https://raising.fi/news/castelion-series-c-august-2026
- SRM: https://thedefensepost.com/2026/02/24/anduril-solid-rocket-motor-production/amp/
- Vulcan: https://executivegov.com/articles/osc-vulcan-reelement-ndfeb-magnet ; Ga/Ge: https://projectblue.com/blue/news-analysis/1401/
- Castings: https://submarinesuppliers.org/wp-content/uploads/2026/02/2026-016-SIBC-Talking-Point-IA.pdf ; https://thedefensepost.com/2026/08/05/us-navy-rangeview-maintenance/amp/ ; https://www.tectonicdefense.com/fabri-announces-its-raised-13-5m-for-new-age-casting/
- Rochester: https://bitscale.ai/directory/rochester-electronics-llc ; Rad-hard market: https://www.marketsandmarkets.com/ResearchInsight/radiation-hardened-electronics-market-size.amp
- Drone Dominance: https://www.suasnews.com/2026/04/department-of-war-launches-phase-two-of-1-1bn-drone-dominance-programme/
- Spares AI startups: https://runwaygirlnetwork.com/2026/04/press-release-novineer-launches-ai-reverse-engineering-with-am-craft/ ; https://aifunding.me/companies/intropy

Unverified and derived numbers to check before use: the ~$10B sole-source spares pool, the $7-10B munitions sub-tier, the $3-5B electronics DMSMS figure, energetics $/lb, the castings and forgings market, and HEICO, TransDigm and RBC market values (memory). Each sweep is one scorer with web search, not a panel.
