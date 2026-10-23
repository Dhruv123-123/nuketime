# P11: Slim-Hole Permeability Wireline Kit. Straddle packer, heat-pulse flowmeter, actively heated fibre, 40 mm televiewer and push-pull tracers

Date: 23 Oct 2026. Build candidate P11, model track. This builds on `M30-permeability.md` (Libbey and Murphy 2026 classes and MPWPI bands, Barton-Zoback-Moos critically stressed fractures, Dixie Valley, specific capacity, earth tides), `M20-tg-and-mining-holes.md` (NBMG TG and mining holes, re-entry logger idea), `M27-fibre-das.md`, `P01` (Ranch Well Sentinel: drop probe, tides, sounding-tube limit), `P07` (rig ride-along in mining core holes), `P09` (legacy hole rescue: most old TG holes are 3/4-1 inch pipe), `../../../hardware/evidence/H02-existing-well-logging.md`, `H13-permits-and-secrecy.md` (BLM IM 2026-024 casual use) and `../MODEL.md`. It does not repeat them.

**Method note.** The shared web-search budget for this workflow turn (200 calls) was used up before this agent started. Both searches I tried were refused. So no new web pages were read. Physics and prior art come from repo files (cited by file) and from standard literature I know; those items are marked (from memory, unverified). All prices are my own estimates (unverified). Numbers marked (calc) come from `P11_calc.py` in this folder.

---

## Bottom line

**Build it, but as a lean "permeability truth" kit for holes that actually fit, not a universal kit.** Three changes to the brief:

1. **The hole population is narrower than the brief says, so aim it at mining core holes and our own holes.** Old TG holes are mostly 3/4-1 inch grouted pipe (P09). A packer, flowmeter or televiewer cannot go down them and cannot see the rock through grout. Ranch wells are 150-200 mm, steel-cased and perforated over short intervals, so they need a second, larger packer and give only the screened interval. The real sweet spot is **open NQ/HQ (76/96 mm) core holes**: our own 150-500 m holes, and mining exploration holes in the days before they are plugged (P07 relationship). Mining geotech crews already run "through-the-rods" wireline packer (Lugeon) tests in exactly these holes (from memory, unverified), so the method is routine and the drillers know it.
2. **The best single tool is the actively heated fibre in a sealed liner, not the packer.** Univ. of Guelph work (Coleman et al. 2015, J. Hydrology; Maldaner et al. 2019, Water Resources Research; Read et al. 2014, GRL for the open-hole version) heats a hybrid fibre cable inside a blank flexible liner and reads where the rock carries water past the hole, every metre, with no pumping (from memory, unverified). That is a natural-gradient flux profile, which is what a blind-system model wants: it shows where water moves today, not where it can be forced. The packer then tests only the 3-6 zones the fibre flags, which cuts packer time from days to hours.
3. **Add a desk step that costs almost nothing: harvest existing packer data.** Mine EIS hydrogeology appendices (BLM ePlanning NEPA files for Nevada gold mines) and old DOE/USGS slim-hole reports contain hundreds of Lugeon and slug-test intervals with depths, often near hot dewatering fields (unverified count). They become training labels for the permeability-class model before the kit is even built.

**What it buys.** At each tested hole: a per-metre flowing-fracture map, interval transmissivity (about 1e-9 to 1e-3 m2/s), fracture orientation, a test of whether the flowing fractures are the critically stressed ones, in-situ thermal conductivity, lid groundwater flux, and a fracture surface-area estimate. Across the bank: a labelled set of 30-80 holes a year that links cheap surface proxies (structure type, He R/Ra, specific capacity, earth-tide T) to measured permeability class. That label set is the real alpha. It shrinks rank 2 at every cell, not only at drilled ones.

**Cost.** Full purchase kit about **$200-385k** (calc, unverified prices). Lean v1 that rents the DTS and televiewer, builds its own flowmeter and buys 4 liners: about **$85-200k** (calc). Field cost about **$3-6k per hole-day**, typically 1.5-3 days per 300 m hole (unverified). That fits the brief's band.

---

## 1. Physics: why each tool sees permeability

### 1.1 What we are trying to classify

The model's physical event needs the permeability class to be "Limited Distributed or better" (Libbey and Murphy SGW 2026, via M30: MPWPI 0.5-5 kg/s/bar for Limited Distributed, 5 to over 100 for Discrete and Enhanced Distributed). Thiem arithmetic (calc) maps this to reservoir transmissivity:

| Cold-water T (m2/s) | PI (kg/s/bar), cold | At 150 C (about 5x lower viscosity) |
|---|---|---|
| 1e-5 | 0.08 | about 0.4 |
| 1e-4 | 0.75 | about 3.7 |
| 1e-3 | 7.5 | about 37 |

So the class boundary sits near **T of about 1e-4 m2/s (cold-equivalent) over the open interval**. Every tool in the kit easily resolves that level. The hard part is not the measurement. It is that a 150-500 m slim hole samples the upper part of the system, not the 1-2 km reservoir. Section 4 deals with that.

### 1.2 Heat-pulse flowmeter (ambient and stressed vertical flow)

- **How it works.** A wire grid heats a thin sheet of water. Thermistors above and below time the warm slug. A rubber diverter forces borehole flow through the tool. USGS (Hess 1986; Paillet 1998, WRR) used it to find which fractures feed ambient flow in crystalline rock (from memory, unverified).
- **Range.** About 0.03 to 4 L/min (from memory, unverified). In a 60 mm hole that is 0.011 to 1.4 m/min (calc), well inside the tool's timing window.
- **What it detects.** Ambient flow appears when two fractures sit at different heads. With a 0.5 m head difference, a fracture of T = 1e-5 m2/s drives about 0.23 L/min into the hole, and T = 1e-6 drives about 0.02 L/min (calc). So the flowmeter alone resolves fractures down to about 1e-6 m2/s, and with a small pumping stress down to about 1e-7.
- **Geothermal bonus.** In an upflow zone the deep fracture sits at higher head. Upward ambient flow in an open hole is a direct sign that the deep feed is connected and overpressured relative to the lid. Downward flow is a recharge (mask) sign. This links rank 2 to rank 3 and rank 6.

### 1.3 Actively heated fibre-optic DTS (A-DTS)

- **How it works.** A hybrid cable carries fibres and copper conductors. We pass current through the copper (about 10-20 W/m) for 12-48 hours and read temperature every 0.25-1 m with Raman DTS. In still rock the rise follows the line-source law, about 2.6 K after 24 h at 15 W/m in rock of 2.5 W/m/K (calc). Where water flows past the hole, the rise is smaller.
- **Detection limit.** Advection takes 3% of the heat at a Darcy flux of about 6e-7 m/s (5 cm/day) and 10% at about 2e-6 m/s (17 cm/day), for a 3 cm radius (calc). Published Guelph work reports flux resolution in that range or a bit better (from memory, unverified). In a lid aquifer that is plenty. In tight rock below the lid, most of the hole will read "no flow", which is itself the useful answer: it marks the few fractures that carry the system.
- **Sealed liner matters.** In an open hole, flow runs up and down the hole and smears the signal (Read et al. 2014 used this to measure in-hole vertical flow instead). A blank flexible liner (FLUTe-type) presses the cable against the wall and stops cross-flow, so the signal is formation flux at each metre (Coleman 2015; Maldaner 2019; from memory, unverified). The liner itself also gives a transmissivity profile from its descent rate (Keller, FLUTe "T-profiler", from memory, unverified).
- **Extra outputs for free.** The no-flow sections give in-situ thermal conductivity every metre from the heating slope (rank 7). The passive DTS log before heating gives the equilibrated T(z) at 0.01-0.05 C resolution after stacking (rank 5).
- **Power.** 150 m at 10 W/m is 1.5 kW. 500 m at 20 W/m is 10 kW (calc). A 10 kW trailer genset covers it. That is the heaviest load in the kit.

### 1.4 Straddle packer (interval transmissivity and head)

- **How it works.** Two inflatable elements isolate a 1-3 m interval. Transducers above, inside and below. We run a slug or pulse test (fast, small water use) and, in good zones, a 30-60 min constant-rate injection. Standard analysis (Hvorslev, Cooper-Bredehoeft-Papadopulos, Bourdet derivative) gives T and storativity.
- **Range.** Pulse tests reach about 1e-10 m2/s; constant-rate tests cover about 1e-7 to 1e-3 m2/s (textbook, unverified). That spans the whole class range.
- **Head too.** The shut-in pressure in each interval gives the formation head. Head that rises with depth is a direct upflow sign. Across several holes, interval heads map the hydraulic gradient that the model needs for plume back-projection (rank 6).
- **Derivative shape gives class.** A flat derivative means radial flow in distributed fractures. A half-slope or bilinear derivative means flow through one dominant fracture or a channel (textbook, unverified). That is the Discrete versus Distributed signal, measured at hole scale.

### 1.5 40 mm acoustic televiewer

- **What.** ABI40-class acoustic televiewer (ALT, Mount Sopris QL40-ABI; from memory, unverified) gives a 360-degree image of the wall, so every fracture gets a dip and dip direction, plus aperture and breakouts.
- **Why it matters.** Barton, Zoback and Moos (1995, Geology; via M30) showed that the flowing fractures are the critically stressed ones. With the televiewer plus the A-DTS flow map we can test that in each hole. Breakouts and drilling-induced tensile fractures, if present, give the local SHmax direction directly. That fixes the stress input that makes slip-tendency layers noisy (M30 item 11: a 20-30 degree SHmax error flips the tendency). A slim hole at 300-500 m in Basin and Range rock may show few breakouts (unverified), so treat stress as a bonus.
- **Fluid.** Acoustic works in muddy water. An optical OBI40 is a later add-on for clear holes.

### 1.6 Single-well push-pull tracer test

- **How it works.** Inject a slug of water carrying bromide (conservative) plus one or two naphthalene sulfonates (stable to over 300 C, the standard geothermal tracers from Rose and Adams at EGI Utah; from memory, unverified) into the packed interval. Rest 1-24 h. Pump back and record recovery curves (Istok 1997; Haggerty 1998; from memory, unverified).
- **Outputs.** Tracers with different diffusion rates separate on the way back in proportion to fracture surface area per volume (matrix diffusion). A heat "push" (inject cool water and watch it warm on pull-back) gives a direct thermal surface-area estimate (Hawkins, Becker, Tester and co-workers, WRR 2017-2018 on thermally degrading tracers and heat exchange in fractured bedrock; from memory, unverified). Drift during the rest period gives lid groundwater speed.
- **Why it matters.** Fracture surface area governs thermal drawdown, which is what drives the recovery factor (rank 9). This is a weak link (shallow, small volume), but it is the only cheap direct measurement of it.

---

## 2. Prior art

| What | Who | Our difference |
|---|---|---|
| Heat-pulse flowmeter in fractured rock | USGS (Hess, Paillet, Williams), Mirror Lake NH and many others | Same tool, used in hot slim holes as an upflow/recharge sign |
| A-DTS in lined holes | Univ. of Guelph (Parker, Cherry, Coleman, Maldaner); Read et al. 2014 Rennes | First use as a geothermal permeability-class label (as far as I know, unverified) |
| Straddle packer, Lugeon tests | Mining geotech and hydrogeology firms; DOE/Sandia slim-hole programme in the 1990s (Finger, Combs; from memory, unverified) showed slim-hole injection tests can predict production well output | We pair it with flow maps and turn it into class labels across many holes |
| Televiewer plus flowing fractures | Barton, Zoback, Moos 1995; Hickman at Dixie Valley | Same physics, run cheaply in many prospect holes, not one deep well |
| Push-pull tracer | Istok, Haggerty, Hawkins and Tester; EGI tracers in geothermal fields | Small, shallow, single-well version for surface-area priors |
| Zanskar | Own wells, flow tests in its own development wells (M13) | They test after the lease and at full size. We test at slim-hole stage before the farm-out, across many prospects |

The DOE/Sandia slim-hole work is the key precedent for buyers. It argued that slim-hole injection and flow tests in fractured geothermal reservoirs predict large-hole productivity well enough to justify slim holes as an exploration tool (from memory, unverified; check the Sandia SAND reports by Finger and by Combs, Garg and Pritchett before using this in a pitch).

---

## 3. Concrete v1 design

### 3.1 Parts list

| # | Part | Spec | Price (unverified) |
|---|---|---|---|
| 1 | Logging winch | 500 m, 4-conductor 3/16 in armoured line, electric, depth encoder, on a trailer | $25-40k |
| 2 | Acoustic televiewer | 40 mm OD, 70 C rating (150 C version later), 1 cm vertical sampling | $45-65k, or rent about $0.5-1k/day |
| 3 | Heat-pulse flowmeter | 42 mm OD, rubber diverters for 48/60/76/96 mm. Own build: Ni-chrome grid plus two 0.001 C thermistors and a microcontroller, about $3-5k | $8-20k |
| 4 | Slim straddle packer | Passes 46 mm, seals 56-100 mm, 1/2/3 m spacers, N2 inflation, 3 vented pressure transducers (0.02% FS) | $15-30k |
| 5 | Large packer pair | Seals 150-200 mm for ranch wells and old water wells | $8-15k |
| 6 | Pumps and plumbing | 1.75 in submersible (up to about 10 L/min), positive-displacement injection pump, two mag flowmeters, 2 m3 tank | $6-10k |
| 7 | Hybrid heater cable | 500 m, 2 multimode plus 1 single-mode fibre, two 2.5 mm2 copper heater conductors, steel armour, about 8 mm OD | $8-15k |
| 8 | DTS interrogator | Raman DTS, 0.25-1 m spatial sampling, about 0.01 C after stacking | $40-90k, or rent $1-2k/day |
| 9 | Heater supply | 10 kW genset, constant-power controller, ground-fault protection | $6-10k |
| 10 | Blank flexible liners | Sized for NQ/HQ, 150-500 m, single or limited reuse | $2-5k each |
| 11 | Push-pull skid | Dosing pump, Br ion-selective electrode, field UV fluorometer, 48-bottle autosampler; lab HPLC for sulfonates at about $50-100/sample | $8-20k |
| 12 | Rig-up | Tripod, sheave, depth wheel, ruggedized laptop, satellite link, safety kit | $10-20k |

Totals (calc): full purchase **$199-385k**; lean v1 (rent DTS and televiewer, own flowmeter, 4 liners) **$85-200k**.

### 3.2 Dimensions, power and comms

- All downhole tools at 40-46 mm OD, so they pass a 48 mm (AQ) hole. The packer is the binding size: it seals 56 mm and up (BQ/NQ/HQ). That is the honest floor for the packer, not 36 mm. A 36-48 mm hole gets only the flowmeter, televiewer and fibre (without liner).
- Power: 10 kW genset for the heated fibre, 1-2 kW for the winch and pumps. Downhole tools run on wireline power.
- Comms: wireline telemetry to the surface laptop. Data uploads over Starlink-class satellite each night. Raw files are encrypted and stay in our own store. Nothing is filed with any agency for casual-use tests on unleased land (see H13).
- Temperature: v1 rated to 70 C downhole. Hot holes above about 70 C at depth need the 150 C televiewer and packer elements (+30-50% cost, unverified).

### 3.3 Deployment and crew time (300 m NQ hole)

| Step | Time | Notes |
|---|---|---|
| Rig up, passive DTS or probe T(z) log | 2-3 h | Hole must have stood at least a few days for an equilibrated log |
| Heat-pulse flowmeter, ambient, 10-20 stations | 3-4 h | Then repeat under a small pumping stress if water level allows |
| Televiewer log | 2-3 h | 1 cm sampling over 300 m |
| Install liner plus heater cable, heat 24 h, cool 12 h | 1.5 days elapsed, 3-4 h crew | Crew can do the next hole meanwhile |
| Pull liner, straddle packer on 3-6 flagged zones | 4-8 h | Slug or pulse test plus shut-in head per zone |
| Push-pull in the best zone | 6-24 h elapsed | Only at the top 20-30% of holes |
| Rig down | 1 h | |

Crew: two people, one trailer, one pickup. About **1.5-3 days per hole**, often overlapping two holes. Field cost about $3-6k per hole-day including staff, fuel, rentals and lab, so about **$5-15k per hole** (unverified). Compare: a single 300 m own slim hole costs about $80-200k (H11, unverified). The test adds about 5-10% to the hole and doubles what the hole tells us.

---

## 4. How much it shrinks the ranked uncertainties

### 4.1 The representativeness problem (the main physics risk)

A 300 m hole measures permeability in the upper outflow, the lid or the top of the upflow fault. The reservoir sits at 1-2 km. Permeability falls with depth (Manning and Ingebritsen 1999, via M30) and hole-scale tests sample a few metres of rock. So a single slim hole does not directly give the reservoir class. Three things still make it informative:

1. **Same fault, same stress.** If the flowing fractures at 300 m are the critically stressed set and lie on the range-front fault, the same fault at 1.5 km is likely open too (Dixie Valley logic, via M30). If the shallow fault zone is sealed with mineral fill and dry, the deep part is more likely sealed (fault-valve picture).
2. **Head and flow direction.** Upward head gradients and upward ambient flow show a connected deep feed. That is a link to depth that a static k value lacks.
3. **Calibration through the label set.** The model does not need each hole to answer the reservoir question. It needs a learned link from cheap proxies to class. 30-80 measured holes a year, plus harvested mine and DOE packer data, plus Libbey's 40 analog fields, give that link far more support than today's "distance to fault" proxy.

### 4.2 Estimated shrinkage (all rough, unverified, to be checked by GHOST Tier 1 EIG)

| Rank | Today | With P11 at a tested prospect | Across untested cells (via labels) |
|---|---|---|---|
| **2 Permeability class / flow per well (about 10x on MWe)** | 4-class prior from structure; MWe spread about 10x at fixed heat | Class entropy from about 1.9 bits to about 1.0-1.2 bits; MWe spread about 10x to about **3-4x** | After 50-100 labelled holes, proxy-to-class model error maybe 20-30% lower; MWe spread about 10x to **6-8x** |
| **3 Lid thickness and masking** | Peclet fit on ranch-well profiles | A-DTS gives the lid base where lateral flux stops, to about +/-5-10 m; lid flux to about 2x | Calibrates P01/P02 mask sensitivity in the 20/40 campaign |
| **7 Conductive background** | Needle probes on chips | In-situ conductivity every metre, about +/-5-10% | Small regional effect |
| **9 Recovery factor (scenario axis)** | Rg 0.08/0.16/0.25 spread, about 3x | Libbey RF tracks MPWPI, so a PI proxy plus a surface-area estimate moves a prospect's RF prior from about 3x to about 2x | Turns rank 9 from a pure scenario axis into a weakly data-driven prior |
| 5 Temperature at depth | Gradient extrapolation | Equilibrated 0.01 C DTS log; curvature gives vertical Darcy flux | Minor (P01, P07, P09 already cover this) |
| 6 Upflow location | Plume back-projection | Interval heads plus flow direction fix the gradient at each hole | Moderate where 3+ holes exist |

**Overall.** For a prospect that already has a hole, P11 is the strongest single tool in the candidate list for rank 2 and the only one that touches rank 9 with data. Regionally its effect is smaller because it only works where holes exist. My rough guess is that it cuts the permeability part of the regional F5/F95 band by about 15-25% in year one and more as labels accumulate (unverified). In the VOI-Bank logic its EVSI per dollar is highest at the **confirmation stage of the top 5-10% of prospects**, not at screening.

---

## 5. Rights edge

- **Casual use.** Logging and testing an existing hole without changing it is listed as casual use under BLM IM 2026-024 (H13). A flowmeter, televiewer or passive DTS log fits that cleanly. **Packer injection and tracer injection may not**: putting water and bromide into an aquifer could be read as "changing" the hole, and in Nevada it may need an NDEP UIC Class V or similar permit and a water-use check under NRS 534 (unverified). So v1 runs injection and tracer steps only on private land with an owner's consent, or in our own holes, or in mining holes under the operator's existing permits.
- **Farm-out value.** A pre-drill feed-zone map, measured interval transmissivity, flow-direction evidence and a Barton-Zoback test on the main fault are exactly what a buyer like Ormat or Fervo would otherwise pay for with its first well. This supports a higher carry at farm-out (for example asking a 5-10% carry instead of 2-5%, unverified). It also reduces our own risk of spending a full confirmation well on a hot-but-tight target, the most common failure mode (M30 item 6).
- **Speed.** The kit does not lock rights by itself. It raises the value of rights we already hold. It is a confirmation-stage tool and should be paired with P01 and P07, which carry the signing step.
- **Mining partnerships.** Testing a mine's exploration hole before plugging, for a free hydrogeology report, opens the 43 CFR 3204.12 claimant side door and the mining-hole data stream described in P07 and P08.

---

## 6. Risks

1. **Few holes fit.** Most old TG holes are 3/4-1 inch pipe; most ranch wells are cased and screened short. The test population is our own holes and mining holes before plugging. If we drill fewer than about 20 holes a year and mines do not cooperate, the kit sits idle. This is the main "too small" risk.
2. **Shallow is not reservoir.** 150-500 m permeability may correlate weakly with 1-2 km class. The label-set value then falls. Test early against fields with both slim-hole and production data.
3. **Hole stability.** Open NQ holes in altered, clay-rich fault zones squeeze or cave. Packers and liners can stick. Budget for lost-in-hole tools (about $15-30k each event, unverified).
4. **Temperature.** Hot holes above 70-85 C exceed v1 tool ratings. The holes we most want are the hot ones.
5. **Injection permits.** Tracer and injection tests may need UIC permits or water-right checks (unverified), which also leaks location.
6. **Crew skill.** Packer test interpretation and A-DTS processing need a trained hydrogeologist. Rent one from a mining hydro consultancy at first.
7. **Cost per hole.** At $5-15k per hole it is cheap relative to drilling, but expensive per cell relative to P01. It should never be used for screening.

---

## 7. First test

**Desk, weeks 0-6, under $5k:**
1. Harvest packer, Lugeon and slug-test intervals from Nevada gold mine EIS hydrogeology appendices (BLM ePlanning) and DOE/Sandia slim-hole reports. Target 300+ intervals with depth, T, temperature and structural setting. Fit a first proxy-to-T model and see whether structure type, He R/Ra (M22) and specific capacity (M30) predict measured T. Kill condition: no proxy explains more than about 10% of log T variance (then the label-set value is weak).
2. Run GHOST Tier 1 on 20 synthetic systems: does a 300 m hole's T profile plus head gradient update the 1.5 km class by at least 0.5 bits? If not, P11 drops to confirmation-only.

**Field, months 2-4, about $40-60k (unverified), rented tools:**
3. Rent a DTS, televiewer and packer from a mining hydro contractor. Test 3-5 existing open holes at a known blind system with production data (for example a mining-adjacent field or a hole near a producing Nevada field, with operator permission), and 2-3 cold controls. Pass if the measured shallow class ranks the known productive versus tight segments correctly in at least 4 of 5 cases.
4. Only then buy the kit and pair it with the first own slim holes.

---

## 8. Self-scores (1-5)

- **model_uncertainty_alpha: 4.** Strongest direct handle on rank 2 at tested prospects and the only data handle on rank 9. Held back from 5 by the shallow-versus-reservoir gap and the small hole population.
- **rights_alpha: 3.** Raises carry at farm-out and prevents bad confirmation wells. Does not itself sign or lock rights. Injection steps may not be casual use.
- **buildability: 4.** Almost all parts are off the shelf and rentable. A lean v1 is 6-10 weeks for a two-person team. Hard parts are interpretation skill and liner handling.
- **cost_scale: 3.** $85-200k lean kit, $5-15k per hole. Scales with drilling, not with cells.
- **moat: 3.** Methods are public. The moat is the accumulated label set of measured permeability class on hidden prospects, which nobody else is building at slim-hole stage across many prospects.

Sources cited by file: `M30-permeability.md` (Libbey and Murphy 2026: https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Libbey.pdf), `M20`, `P01`, `P07`, `P09`, `H13`. All other literature references in this file are from memory and unverified because no web search could be run this turn.
