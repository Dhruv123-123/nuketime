# The fifth pick: heat-to-power, with the software sold alongside

Written 11 October 2026, from Dhruv's pasted chat about steam turbines, the turbine shortage, coal
repowering and a factory-built 1 to 10 MW heat-to-power block. The ask: find what is real in it, and
make it pitchable with a software layer sold alongside the hardware, where the software is the
broader, higher-leverage part. Model: `designs/island/island.py` (output in `results.txt`).

## The answer

**What is real:** the chat's core economics hold. The turbine-generator is about a tenth of the cost
of a small heat-to-power plant; the rest is custom engineering, boilers, water and crew. But the
chat's market, "every new heat source needs a power block", is the market that has already failed
small companies for 20 years. Industrial waste heat to power in the US is only about 9 GW of economic
potential (ORNL, 2015), and it competes with cheap grid power.

**What changed in 2026** is a new, urgent heat source with a buyer who pays data-centre prices for
every megawatt: the gas engines and aeroderivative turbines being installed behind the meter at AI
campuses. 46 US projects plan 56 GW of on-site generation (Cleanview, April 2026), almost all of it
simple cycle, throwing away 50 to 60 % of its fuel as hot exhaust. A bottoming block on that exhaust
adds 9 % to an engine and about 29 % to an aeroderivative with no extra fuel, no extra gas pipe, no
extra air-permit tonnage and no turbine slot. Our model puts that at about **8 GW of fuel-free
capacity, a $16B hardware market**, on the projects already announced.

**The pitch, in one line:** *the standard power block for every new heat source, starting with the
exhaust of AI campuses, run by the control room that operates every private power plant.*

- **Hardware (the grand vision):** a factory-built, waterless, unattended 2 to 10 MW bottoming block
  (organic Rankine cycle first) that ships with the engines in months and bolts onto 25 MW engine
  packages and 30 to 50 MW aeroderivatives. Later the same block takes heat from thermal batteries,
  repowered coal sites, microreactors and industry.
- **Software (the broader layer, sold first and to more people):** **Control Room**, a remote
  operations and dispatch service for private power plants. One control room runs many behind-the-
  meter plants (engines, turbines, batteries and our blocks) with a skeleton on-site crew, keeps
  uptime, optimises fuel and permit use, and gives lenders and tenants proof of availability. It is
  sold per MW per year to operators who will never buy a block.

The relationship to the earlier picks: PICK3 (nuclear-qualified manufacturer) is still the larger
nuclear bet. This is the stronger energy bet, and the better fit for an ML team, because its software
earns money on day one and its customers are signing gigawatt orders now. PICK4's law ("big gaps are
named") holds here too: this is named, and the edge has to be execution.

## What in the pasted chat checks out

| Claim in the chat | Verdict | Source |
|---|---|---|
| Small steam turbine-generators cost under $200/kW at 2 MW | **Roughly right, but old and partial.** $275/kW at 3 MW and $225/kW at 15 MW for the turbine-generator only, in early-2000s dollars | EPA biomass CHP catalog, citing NREL 2003 |
| The turbine isn't the expensive part | **True.** Installed waste-heat-to-power costs $1,800/kW (steam) to $3,000/kW (ORC) at 1 to 5 MW, and up to $7,000/kW for a real 2 MW cement project | ORNL/TM-2014/620 (2015), Table 5 |
| Small steam plants need a registered operator | **True for steam, state by state.** Minnesota requires constant attendance for high-pressure plants over 500 boiler hp (about 5 MW thermal); remote monitoring is allowed only for 51 to 500 hp with approval and a daily visit | Minn. R. 5225.1180 |
| Antora raised $550M after a 5 GWh system | **True.** $550M Series C (July 2026); 50 MW / 5 GWh at POET Big Stone City, commissioned in under 12 months. That system sells heat, not power | ESS News, 3 Aug 2026 |
| B&W signed $2.4B for 1.2 GW for Applied Digital | **True.** Four 300 MW gas boilers with Siemens Energy steam turbines, for Base Electron (Applied Digital's power arm), March 2026 | POWER, 9 Mar 2026 |
| Gas turbine backlogs stretch to 2032 | **Direction right, year unverified.** GE Vernova had 56 GW of slot reservations and about 10 GW left across 2029 and 2030 (April 2026) | Power Engineering, 23 Apr 2026 |
| Data centres are ordering gigawatts of engines | **True.** INNIO 1.5 GW (300 Jenbacher engines) to VoltaGrid; Wärtsilä over 1.6 GW in US data centres; Nscale 2 GW of Caterpillar engines; Crusoe 650 MW of aeroderivatives | INNIO, Feb 2026; Power Engineering, Apr 2026 |
| Coal plants' grid connections are the scarce asset | **True and quantified.** RMI estimates 250 GW of clean capacity could use surplus interconnection at fossil sites | RMI, Jan 2024 |
| sCO2 startups (Arbor, American Supercritical) | **True.** American Supercritical launched factory-built sCO2 bottoming blocks for gas turbine exhaust (Oct 2026), $8M pre-seed, no orders reported | Turbomachinery, 24 Sep and 6 Oct 2026 |

Two things the chat missed. First, the waste-heat-to-power graveyard: small ORC makers such as ElectraTherm
(absorbed by Bitzer) and Climeon stayed small, because industrial heat is scattered and dirty and the
power competes with the grid (our reading of ORNL's barriers list, not a sourced post-mortem). Second, Turboden (Mitsubishi Heavy Industries) already markets 5 to 60 MW ORC
"power augmentation" for data-centre engines and turbines, remote-monitored and water-free, with no
named customers yet. The hardware idea is named; nobody owns it yet.

## Why now: a megawatt at an AI campus is worth 20 times its fuel

The ORC companies failed because they sold electricity at grid prices. An AI campus buys capacity,
not energy. A bottoming megawatt avoids about $226k a year of gas (our model: 45 % engine, $4/MMBtu,
85 % capacity factor), which is a 9-year payback on fuel alone and would not sell. But that megawatt
also runs about 700 more GPUs, and a power-limited campus has no other way to get it: no new gas
pipe, no new permit tonnage, no new turbine slot. Inferred from GPU rental prices of roughly $2 an
hour, a megawatt of compute grosses on the order of $9M a year, about 20 times the cost of its fuel.
That ratio is the whole thesis, and testing it with real tenants is week one of the plan.

## The software: Control Room

**What it is.** A remote control room plus software that runs a behind-the-meter power plant as one
system: engines, aeroderivatives, batteries, bottoming blocks and the campus load. Three jobs:

1. **Run plants with a skeleton crew.** Remote supervision, alarm triage and ML fault prediction on
   engine and turbine data, so a 300 MW site needs a day crew instead of 24/7 shifts, meeting state
   attendance and insurer rules where they apply. This is what makes our own block "unattended".
2. **Dispatch to the binding constraint.** Choose which units run, at what load, hour by hour, to
   maximise delivered megawatts under fuel, gas-pipe, air-permit (annual tons of NOx) and
   reliability limits. Bottoming output is permit-free megawatt-hours, so the software is also how a
   block's value is proven.
3. **Prove availability.** Metered uptime and heat-rate records that tenants, lenders and insurers
   accept, the same "records complete by construction" idea as PICK3's moat.

**Who buys it, and why they buy it before any hardware:**

| Buyer | Example names | What they pay for |
|---|---|---|
| Behind-the-meter power providers | VoltaGrid, Base Electron (Applied Digital), PROENERGY, Enchanted Rock | Run more sites per operator; uptime evidence for tenants |
| Neoclouds and AI campuses building their own power | Crusoe, Nscale, xAI | A multi-vendor control room instead of one per OEM |
| Midstream companies selling power to data centres | Williams (Socrates for Meta) | Operations without building a power-plant workforce |
| Existing industrial CHP owners | 82.6 GW at about 4,400 US sites (DOE, 2016) | Same remote operations, later |
| Thermal battery and microreactor developers | Antora, Rondo, Aalo, Oklo | Operating the power side of their plants |

**How it is sold alongside the block.** Every block ships with Control Room, so every block sale
seeds a software customer. Control Room sells on its own to sites with no block, and its plant data
shows exactly which exhaust streams are worth a block, so it is also the hardware's lead list.

**Price and size.** About $8k to $15k per MW per year (assumption, to be validated). On the 56 GW
of planned data-centre BTM capacity plus 83 GW of industrial CHP, that is a $1.1B to $2.1B a year
market before thermal batteries and reactors.

## What the model says (`designs/island/`)

**Part A, bottoming potential.** With labelled assumptions (60 % engines, 30 % aeroderivatives,
recovery to about 120 °C, 20 to 25 % bottoming efficiency), the announced 56 GW of data-centre BTM
capacity could add 7.9 GW with no extra fuel: 3.1 GW on engines, 4.8 GW on turbines. At $2,000/kW
that is $15.9B of hardware.

**Part B, a negative result that shaped the software.** I first expected the software's big job to be
making the AI load follow the generators. A 24-hour, one-second simulation of a 312 MW islanded campus
(four 60 MW training jobs plus inference, 14 x 25 MW engines) says no:

| Strategy | Battery needed | Extra fuel | Compute deferred |
|---|---|---|---|
| No coordination, battery absorbs swings | 82 MW, $12.5M | none | none |
| Software shapes checkpoints, failures and restarts | 63 MW, $9.5M | $1.6M a year | 18 MWh a day |
| Plus GPUs filling communication dips (power floor) | 37 MW, $5.6M | $5.4M a year | 18 MWh a day |

A battery is cheaper than coordination: it saves $3M to $7M once but costs $1.6M to $5.4M of gas a
year. Transient control is a feature, not a business. So Control Room's value has to come from crew,
uptime and dispatch under constraints, which is where the plan tests it.

## Competition

| Who | What they do | Why there is still room |
|---|---|---|
| Turboden (MHI), Exergy, Siemens Energy, Baker Hughes | ORC and steam bottoming, 5 to 60 MW, project-engineered | Custom projects; no named data-centre wins; not sold with operations |
| American Supercritical ($8M pre-seed), Arbor ($55M) | sCO2 power blocks | Early hardware, no orders; sCO2 adds technical risk ORC does not |
| INNIO myPlant, Wärtsilä, Caterpillar | Remote monitoring of their own engines | Single-vendor; campuses mix engines, turbines, batteries |
| Emerald AI ($150M at $1.05B, Aug 2026) | Makes grid-connected data centres flexible | Grid flexibility, not operating islanded plants; the most likely entrant |
| GridCARE ($64M, May 2026) | Finds spare grid capacity for data-centre load | Grid-side, complementary |
| Enchanted Rock | Builds and operates its own gas microgrids | Operates only its own fleet; a partner or acquirer |

## Weak points

1. **Bridge power moves.** Much BTM capacity is meant to run until the grid arrives, then leave. A
   block must be skid-mounted and movable, or its payback depends on years the site may not have.
2. **Fuel payback is weak.** At 9 years on gas alone, the block sells only where MW are scarce. If
   turbine slots loosen by 2029, the premium shrinks.
3. **The software price is unproven.** Crew savings at a 300 MW site are perhaps $1.5M to $2.5M a year
   (assumption), which covers about $5k to $8k per MW. The rest must come from uptime and dispatch.
4. **Incumbents can bundle.** Turboden or Wärtsilä could sell a block plus monitoring; Emerald AI could
   extend to islanded sites.
5. **Hardware is capital-heavy.** A factory and inventory before revenue; start with a contract
   manufacturer or licensed ORC design.

## Eight-week plan

| Week | Do | Evidence it produces |
|---|---|---|
| 1 to 3 | Interview 15 BTM operators and campus energy leads (VoltaGrid, Base Electron, Crusoe, Nscale, PROENERGY, Williams, Enchanted Rock) | Whether a fuel-free MW is worth over $2,000/kW to them; who runs their plants now and at what cost |
| 1 to 2 | Get exhaust data (temperature, flow, hours) for three real engine and turbine fleets | Real bottoming uplift per site, replacing Part A's assumptions |
| 2 to 5 | Build Control Room v0 on one operator's engine data: anomaly detection, unit dispatch, availability report | A working demo on real data |
| 3 to 6 | Quotes from Turboden, Exergy and an Indian or Chinese ORC maker for a 5 MW skid, plus a contract manufacturer | True block cost and lead time; build-or-license decision |
| 4 to 8 | One paid Control Room pilot or a signed letter of intent for a block | First revenue or a committed buyer |
| 6 to 8 | Rerun the model with interview and exhaust data | Size of the real market and the software price |

## Kill criteria

- Fewer than 3 of 15 operators say they would pay over $1,500/kW for a fuel-free MW, or BTM plans
  shrink because grid connections arrive faster.
- Turboden or another incumbent already quotes a skid at under $1,500/kW in under 12 months.
- No operator will share plant data or pay for remote operations, because the OEMs' own monitoring is
  good enough.

## Sources

- ORNL/ICF, *Waste Heat to Power Market Assessment*, ORNL/TM-2014/620, March 2015: https://info.ornl.gov/sites/publications/files/Pub52953.pdf
- EPA, *Biomass CHP Catalog of Technologies*, ch. 6 (steam turbine costs, NREL 2003): https://www.epa.gov/sites/production/files/2015-07/documents/biomass_combined_heat_and_power_catalog_of_technologies_6._power_generation_technologies.pdf
- Minnesota Rules 5225.1180, attendance at high-pressure plants: https://law.cornell.edu/regulations/minnesota/Minn-R-5225-1180
- Power Engineering, "Data center power crunch lifts engines, aeroderivatives into larger role", 16 Apr 2026 (Cleanview 56 GW): https://www.power-eng.com/gas/data-center-power-crunch-lifts-engines-aeroderivatives-into-larger-role/
- Power Engineering, GE Vernova slot reservations, 23 Apr 2026: https://www.power-eng.com/gas/turbines/data-centers-drive-record-surge-in-ge-vernova-power-equipment-orders-as-turbine-slots-tighten-through-2030/
- INNIO, 1.5 GW VoltaGrid order, 11 Feb 2026: https://www.innio.com/en/news-media/press-releases/innio-secures-additional-major-order-from-voltagrid-1-5-gw-for-behind-the-meter-power-generation/
- POWER, B&W 1.2 GW for Applied Digital, 9 Mar 2026: https://www.powermag.com/babcock-wilcox-will-deliver-1-2-gw-of-gas-fired-capacity-for-applied-digital-data-centers/
- ESS News, Antora $550M, 3 Aug 2026: https://www.ess-news.com/2026/08/03/antora-raises-550-million-for-us-made-thermal-battery-storage/
- Turboden, data-centre power augmentation: https://www.turboden.com/datacenters
- Turbomachinery, American Supercritical sCO2 power blocks, 6 Oct 2026: https://www.turbomachinerymag.com/view/american-supercritical-launches-sco-power-blocks-for-gas-turbine-waste-heat
- RMI, *Clean Repowering*, 16 Jan 2024: https://rmi.org/resources/clean-repowering-a-near-term-ira-powered-energy-transition-accelerant/
- Pulse 2, Emerald AI $150M Series A, 25 Aug 2026: https://pulse2.com/emerald-ai-raises-150-million-series-a-at-1-05-billion-valuation-as-platform-targets-100-gw-of-untapped-u-s-grid-capacity/
- DCD, GridCARE $64M, 15 May 2026: https://www.datacenterdynamics.com/en/news/gridcare-raises-64m-in-series-a-funding-round/
- Data Center Frontier, "Power First: AI Data Centers Become Energy Systems" (load swings): https://www.datacenterfrontier.com/energy/article/55403280/power-first-ai-data-centers-become-energy-systems
- DOE, CHP Installation Database update, July 2017: https://www.energy.gov/cmei/amo/articles/department-energy-releases-updated-combined-heat-and-power-installation-database
