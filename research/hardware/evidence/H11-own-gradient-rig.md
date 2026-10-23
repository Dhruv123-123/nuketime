# H11: Our own cheap temperature-gradient hole machine

Research note: the web fetch and search budgets ran out partway through. Facts I could not check against a source are marked (unverified).

## Summary

- A gradient hole is the trusted proving step. It costs $0.3-1.5M per hole at 150-900 m (brief figure). But the drilling itself is cheap: OpenEI's figures for thermal gradient holes are $5-50/ft, median $16.50/ft, for holes under 500 ft. Most of the all-in cost is mobilisation, roads, the full crew, permits, logging and plugging. A light rig that we own attacks exactly those costs.
- Precedents for cheap rigs already exist. Earth AI owns its rig and targets about $100/m over 100,000 m. Borobotics built a 150 kg robot that one person sets up on 6-8 m2 and that drills to 250 m. A 150-250 m gradient hole for $30-60k all-in looks reachable (unverified until tested). That is roughly 10x more holes per dollar.
- Permitting got easier in 2026. On 28 April 2026 BLM published a categorical exclusion (CX) for geothermal exploration, covering core drilling and temperature gradient wells that disturb up to 10 acres. An earlier CX (January 2025) covers resource-confirmation drilling up to 20 acres. So a small-footprint hole needs no new EA (environmental assessment).
- The economics flip. At $0.5M per hole, 3 holes per prospect and a 20% hit rate, each discovery costs about $7.5M. A confirmed resource steps up by only about $0.1M/MW, so a 30 MW prospect is worth about $3M. That means negative margin. At $40k per hole the same maths gives $0.6M per discovery, about 5x margin. The rig is what makes the heat-rights bank work.
- The data stays ours. Holes on private ranch land, and our own logs filed under state confidentiality rules, build a deep-temperature dataset nobody else has. That compounds: every hole retrains the model, which picks the next hole better.

## Key facts with numbers

- **Drilling cost per foot.** Thermal gradient holes run $5.00 low, $16.50 median and $50.00 high per foot, and are "usually less than 500 ft deep" (https://openei.org/wiki/Thermal_Gradient_Holes). These are drilling-only, often old numbers. All-in costs for modern 150-900 m holes are $0.3-1.5M (brief). That is $300-1,600/m all-in, against $16-160/m for drilling alone.
- **Slim holes.** OpenEI and The Driller describe slim holes as a cheaper exploration tool that rigs from mining exploration can drill (https://openei.org/wiki/Slim_Holes, https://thedriller.com/articles/85554-slimhole-drilling-in-geothermal-exploration). In Nevada, typical gradient holes are drilled with mineral-exploration diamond core rigs (HQ/NQ wireline) or air rotary/RC rigs (unverified). Diamond coring contractors in Nevada charge about $100-250/m before mobilisation and standby (unverified).
- **Earth AI precedent.** It plans "approximately $100/metre" for 100,000 m with its own "mobile low disturbance" drilling. It claims costs "up to 80%" lower and 3-6 months from prospect to drill test. It raised a $20M Series B in January 2025 (https://www.mining.com/?p=1170737, https://www.mining-technology.com/news/earth-ai-20m-ai-driven-mineral-exploration-drilling/). It owns the rig, owns the tenements and owns the data. Same shape as our play.
- **Borobotics "Grabowski".** A 150 kg robot, 2.5 m long and 13.5 cm in diameter. It drills to 250 m, one person installs it on 6-8 m2, and it runs on electricity (about 288 kg CO2 per hole, 86% less than diesel) (https://www.heise.de/en/news/Fully-autonomous-drilling-robot-drills-efficiently-and-cost-effectively-10250703.html). It was built for heat-pump holes in soft and medium ground. Basin-and-Range bedrock is harder.
- **BLM CX, April 2026.** Published in the Federal Register on 28 April 2026. It covers geophysics, core drilling, temperature gradient wells, and the pads, roads and trails that go with them, for disturbance up to 10 acres. Activities with "extraordinary circumstances" (ESA species, cultural resources) are excluded (https://www.blm.gov/press-release/blm-takes-steps-accelerate-geothermal-energy-development).
- **BLM CX, January 2025.** Covers resource-confirmation drilling (core, gradient and resource wells) up to 20 acres on public land and split estate (https://www.thinkgeoenergy.com/new-categorical-exclusion-to-facilitate-permitting-of-geothermal-projects-in-the-us/).
- **BLM notice level.** Exploration on federal land is filed as a Notice of Intent to Conduct Geothermal Resource Exploration Operations (43 CFR 3250, Form 3200-9) and needs a bond. It can be done without a lease (unverified).
- **Nevada.** NAC 534A (revised April 2026) governs geothermal wells, including gradient wells, through the Division of Minerals. It requires a permit, a bond, filed logs and plugging (https://www.leg.state.nv.us/NAC/NAC-534A.html). Under the records sections (534A.540-560), filed well data is held confidential for a period (exact term unverified; https://regulations.justia.com/states/nevada/chapter-534a/miscellaneous-records-reports-and-other-requirements/section-534a-560). This is the same rule that makes old Nevada well files "leave confidentiality" over time. Our files will leave too, but years after we have acted on them.
- **Direct push and CPT.** A thermal cone penetration test (T-CPT) measures ground temperature and thermal properties as the cone is pushed (https://research.tudelft.nl/en/publications/thermal-cone-penetration-test-t-cpt/). Push depth is limited to soft sediment, typically 30-100 m, and stops at gravel or bedrock (unverified; https://en.wikipedia.org/wiki/Cone_penetration_test). Nevada's cheap shallow tool is the 2 m temperature probe survey, used in the Play Fairway projects (https://opennetzero.org/national-renewable-energy-laboratory-nrel/effectiveness-of-shallow-temperature-surveys-to-target-a-geothermal-reservoir-at-previously-exp). Both screen targets. Neither replaces a hole below the water table and the zone of seasonal and groundwater noise.

## Hardware design sketch

**What we build.** A light rig on a trailer or tracks, built for one job: 150-300 m vertical, 76-96 mm (NQ/HQ-ish) holes in alluvium and Basin-and-Range bedrock. The drilling method switches by ground type:
- Sonic or air hammer through alluvium.
- Diamond coring or downhole air hammer in rock.
- Water only, no mud, to keep it cheap and clean.

Automation handles rod handling, bit-weight control and drilling at night. That leaves one tech and one helper, against 3-4 on a contract rig. After drilling, we hang a fibre-optic DTS (distributed temperature sensing) cable or a string of thermistors in a grouted PVC tube. The hole is sealed per NAC 534A and reads equilibrium temperature remotely by cellular or satellite for weeks. No return visit to log it. The core or chips are scanned on site: XRF plus thermal conductivity. That turns gradient into heat flow, which is the number ML needs.

**Prototype cost (unverified):**
- Used small coring or RC rig base (LF70-class or similar): $150-350k.
- Automation and rod handler: $200-400k.
- Fibre DTS interrogator: $40-80k. Sensor strings: about $2k per hole.
- Support truck, water trailer, grout plant: $100k.
- Engineering for 12 months, 3 people: $0.6M.
- **Total about $1.1-1.5M.**

**Unit cost at scale.** About $0.4-0.6M per rig (unverified).

**Per hole, 200 m (unverified):**
- Consumables and bits: $4-8k.
- Grout and plugging: $3-5k.
- Sensor: $2k.
- Crew of 2 for 5-8 days: $8-12k.
- Rig depreciation: $5k.
- Permit and bond overhead: $2-5k.
- **Total about $25-40k all-in, or $125-200/m.** That is 10-20x below $0.3-1.5M.

**Throughput.** About 30-40 holes per rig per year. Five rigs give about 175 holes per year for about $6M per year.

**Time to prototype.** 9-12 months to the first own-rig hole. A contract-rig pilot can start in about 60 days.

## What data it unlocks that is not public

- **Equilibrium temperature at 150-300 m, with heat flow from measured conductivity, on a dense grid.** Public data is sparse 1970s-80s holes (the Chevron/Phillips archive), clustered where those companies looked.
- **Negatives.** Cold holes are the labels that public maps lack. Public ML maps score F1<0.10 because the input data is sparse and biased to positives.
- **Who doesn't have it.** Zanskar and Enverus use public data. Ormat and Fervo drill a few expensive holes on leases they already hold and keep the data inside their own projects. Nobody drills cheap blind holes across ranch land to train a model.
- **Confidentiality.** Logs filed with Nevada stay confidential for the statutory period (term unverified). Holes on private fee land with only a state well filing are the most private. Other states have their own terms; Utah, Oregon, Idaho and others need checking (unverified).

## How it compounds into owned assets

The sequence:
1. The model ranks cells.
2. We buy cheap rights first: ranch geothermal rights or option leases at $1-10/ac, state first-file at about $1/ac/yr, leftover BLM noncompetitive at $1/ac/yr.
3. We drill 2-3 of our own holes per block at about $35k each.
4. Hot blocks become "gradient-confirmed" packages. They carry a heat-flow anomaly map that a buyer would otherwise spend $1-3M and 2 years to make.
5. We sell to Ormat, Fervo, Invenergy or Zanskar for a carry or $/MWh override. Cold blocks are dropped cheaply, and their data still trains the model.

The step-up comes from cost per discovery, not the price per MW:

| | Conventional | Our rig |
|---|---|---|
| Cost per hole | $0.5M | $40k |
| Holes per prospect | 3 | 3 |
| Hit rate | 20% | 20%, rising as the model learns |
| Cost per discovery | $7.5M | $0.6M |

A 30 MW confirmed prospect at about $0.1M/MW is worth about $3M. The bank then earns about 5x on exploration spend instead of losing money. If the hit rate climbs from 20% to 35%, cost per discovery falls to about $0.34M.

Ten times more holes per dollar also means 10x more labels per year. That is the compounding moat.

## Risks and kill conditions

- **Hard rock.** Basin-and-Range volcanics and silicified zones can push costs back to $300+/m. Kill if the all-in cost exceeds $100k per 200 m hole.
- **Too shallow.** 150-300 m may be too shallow in places: lateral flow under the water table and outflow plumes can make shallow gradients mislead. Kill if shallow gradients predict deeper temperature poorly against legacy deep wells (R² < 0.6).
- **Buyers re-drill anyway.** Buyers may not trust our holes and re-drill, which leaves the step-up thin. Mitigation: use QA'd standard logs and invite a buyer to witness the pilot.
- **Fluid encounters.** Hitting artesian or hot fluid at shallow depth needs blowout control under NAC 534A. Drill in conservative zones first.
- **Copying.** Contract drillers can copy the low-cost model. The defence is the dataset and the rights, not the rig.
- **Short confidentiality.** If confidentiality periods prove short, we drill on private land and file the minimum.

## Cheapest first test

- **What.** Contract a small Nevada coring or RC rig to drill 3 holes of 150-200 m on private ranch land. Choose land near 2 legacy deep wells with known temperatures. Use DTS-lined, grouted completions and remote logging for 4 weeks.
- **Cost and time.** About $150-200k and 60-75 days (unverified quotes).
- **Pass:** all-in cost is $60k or less per hole, as a contractor baseline (our own rig should halve it), and gradients predict the legacy deep-well temperatures within ±10%.
- **Fail:** cost is above $120k per hole, or the predictions are off by more than 25%.
- **Cheaper pre-test.** A 2 m probe survey over the same block for $10-20k in about 10 days (unverified), to check that shallow and 200 m signals agree.

## Sources

- https://openei.org/wiki/Thermal_Gradient_Holes
- https://openei.org/wiki/Slim_Holes
- https://thedriller.com/articles/85554-slimhole-drilling-in-geothermal-exploration
- https://www.mining.com/?p=1170737
- https://www.mining-technology.com/news/earth-ai-20m-ai-driven-mineral-exploration-drilling/
- https://www.heise.de/en/news/Fully-autonomous-drilling-robot-drills-efficiently-and-cost-effectively-10250703.html
- https://www.blm.gov/press-release/blm-takes-steps-accelerate-geothermal-energy-development
- https://www.thinkgeoenergy.com/new-categorical-exclusion-to-facilitate-permitting-of-geothermal-projects-in-the-us/
- https://www.leg.state.nv.us/NAC/NAC-534A.html
- https://regulations.justia.com/states/nevada/chapter-534a/miscellaneous-records-reports-and-other-requirements/section-534a-560
- https://research.tudelft.nl/en/publications/thermal-cone-penetration-test-t-cpt/
- https://en.wikipedia.org/wiki/Cone_penetration_test
- https://opennetzero.org/national-renewable-energy-laboratory-nrel/effectiveness-of-shallow-temperature-surveys-to-target-a-geothermal-reservoir-at-previously-exp
- https://gdr.openei.org/files/344/GTPMcGeeFinalReportEE0002830.pdf (not read)
