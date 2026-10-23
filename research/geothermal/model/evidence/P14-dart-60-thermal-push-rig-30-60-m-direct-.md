# P14: DART-60 Thermal Push Rig (30-60 m direct push, stay-behind logging tube, thermal piezocone, pore-water and He sample)

Date: 23 Oct 2026. Build candidate P14, model track. This builds on `M21` (2 m noise 1.2 C, 64% blank areas, Olmsted 1977: 12 C at 30 m under a 3.3-3.7 C 1 m signal, the "deep dart" tier), `M23` (four mask classes, Peclet physics), `M03`/`M18` (Granite Springs used 10 GeoProbe holes under 50 m before TG drilling; upflow still unlocated), `P02` (3 m casual-use dart, differential valley-reference idea, 10-20 mW/m2 per dart), `H11` (own gradient rig, T-CPT note), `H13` (BLM IM 2026-024 casual-use limits, NOI cost and leak) and `MODEL.md` ranks. It does not repeat them.

Method note: the shared web-search budget was used up before this slice ran (0 searches succeeded). Everything below comes from the repo's earlier sourced notes, my own knowledge of the literature, and a new calc script, `P14_push_sim.py`. Rig prices, CPT service rates and state permit rules are **(unverified)** and must be checked before buying.

## Bottom line

- **What it is.** A tracked direct-push rig (used GeoProbe 7822DT/8150LS class, or a small anchored CPT crawler) that pushes a **thermal piezocone** to 30-60 m in basin fill. On the way down it logs tip resistance, sleeve friction, pore pressure and temperature every 2 cm. It stops at 4-8 depths for **pore-pressure dissipation** (gives hydraulic K and the true static head) and a **heat-pulse test** (gives thermal conductivity k). On the way out it leaves a **closed-end 25 mm PVC/HDPE tube** grouted in the hole. We re-log that tube with a 0.002 C probe at 0.5 m steps after 2 and 8 weeks. One push per site also takes a **screened pore-water sample** at the water table for SiO2, Cl, B, Li, d18O/dD and dissolved He/Ne.
- **Why it matters.** It is the cheapest tool that **sees through both shallow masks and tells them apart**. In my three-scenario calc (`P14_push_sim.py`), a clay-lidded hot zone gives only +0.5 C at 2 m (below the 1.2 C noise of M21) but +8.6 C at 40 m and +14 C at 60 m. A cold aquifer sweep (8-35 m) reads **colder than background at 30 m** and only shows heat at 40-60 m, in the aquitard below. So **60 m, not 30 m, is the design depth**. That is mask rank 3 measured directly, at a point, with a physical number (lid thickness, aquifer base, sub-aquifer heat flux).
- **Noise.** Heat flux from the 15-60 m tube log is good to about **±14-16 mW/m2** (calc: 0.01 C reading noise, ±12% k, ±0.5 C site-specific surface-warming residual after subtracting a valley reference hole). That is about **20-40x better than a one-shot 2 m probe** in flux terms. It matches the brief's ±0.02-0.05 W/m2 with margin.
- **Upflow channel.** Thermal curvature alone only sees upward Darcy flux above about 3-5 cm/yr, because recent surface warming bends the top 50 m by 20-60 mC. But the **piezocone measures head directly**: static pore pressure at 4-8 depths gives the vertical hydraulic gradient to about ±0.005, and dissipation gives K. Gradient x K = vertical water flux. That is the upflow signal itself, and no other cheap tool in our stack measures it.
- **Cost.** Rig $60-250k (used to new, unverified). Per hole about **$1,200-2,500** all-in at 1-2 holes a day with a 2-person crew. A 6-10 hole prospect transect is **$10-25k**, against $150k+ for one TG hole. Start by **hiring a CPT contractor** for the first 20 holes ($15-30k, unverified) before buying anything.
- **Rights.** Over 10 ft and mechanized, so it is **not casual use on BLM** (needs an NOI, which is public). It runs on **optioned private land and state trust land first**. It is the "confirm before you pay for the next tier" step on land we already hold, plus a lateral plume reader from private inholdings next to unleased BLM.
- **Self-scores:** model_uncertainty_alpha 4, rights_alpha 2.5, buildability 4, cost_scale 3, moat 3.

## 1. Physics case

### 1a. Why 30-60 m works when 2 m does not
- **Seasonal wave is gone.** Damping depth is about 2-3 m (P02). At 15 m the annual wave is about 0.1% of the surface amplitude (±0.016 C, calc). So one log is a steady-state profile, not a snapshot.
- **Conductive gain with depth.** Excess temperature grows as dT = dq * z / k (Olmsted 1977, M21). An excess flux of 0.1 W/m2 (about 2x background) gives +4 C at 60 m in k = 1.5 W/m/K fill, but only +0.13 C at 2 m. The push reaches systems leaking 5-10x less than the 0.5-1 W/m2 a 2 m survey needs (M21).
- **Historical proof.** Olmsted (USGS PP 1044-B, https://app.ingemmet.gob.pe/biblioteca/pdf/USGS-PP-1044-B.pdf) found a 12 C anomaly at 30 m where 1 m showed 3.3-3.7 C, and the patterns at the two depths did not match. USGS used 30 m (100 ft) augered heat-flow holes at Raft River (OFR 86-123, https://pubs.usgs.gov/of/1986/0123/report.pdf). Granite Springs used 10 GeoProbe holes under 50 m (M03).

### 1b. Noise budget (calc, `P14_push_sim.py`, 4,000 draws)

| Interval logged | Flux error (1 sd) | Main terms |
|---|---|---|
| 15-30 m | 16 mW/m2 | k error dominates |
| 15-45 m | 15 mW/m2 | k error, surface-warming residual |
| 15-60 m | 14 mW/m2 | k error |

Assumptions: background 80 mW/m2, k = 1.5, readings ±0.01 C at 0.5 m steps, k known to ±12% (heat-pulse plus soil-behaviour type), and a ±0.5 C site-specific ground-surface warming step 40 years ago that is **left over after subtracting a valley reference hole** (unverified prior). Without the reference hole, a regional +1.5 C warming since about 1980 bends the gradient by up to about 30 C/km near the top and about 18 C/km at 40 m (calc, erfc model). So **every valley needs one or two cold reference pushes**, the same differential design as P02.

Other noise:
- **Push heating.** Friction warms the cone by roughly 1-5 C in dense sand. It decays in hours (Akrouch et al. 2016, ASCE JGGE, thermal cone test; unverified details). The tube log at 2 weeks avoids it.
- **Grout heat.** Cement grout hydration adds heat for days. Use **bentonite-only grout** (no cement) around the tube.
- **Convection in the tube.** In a 19-22 mm ID water-filled tube, free convection is weak at gradients under about 100 C/km (unverified rule of thumb). Hot holes (>200 C/km) may need fill with a gel or a baffled log.
- **Irrigation and land use.** Ag fields have a different surface history. Do not push in or next to irrigated fields for geothermal duty, or log a matching reference on the same land use.

### 1c. Lid vs sweep vs nothing (the rank 3 discriminator)

Three forward profiles from the calc script (surface 15 C):

| Depth | No anomaly | Clay lid over heat (0.35 W/m2) | Cold aquifer sweep 8-35 m over heat |
|---|---|---|---|
| 2 m | 15.1 | 15.6 | 15.1 |
| 20 m | 16.1 | 20.8 | 15.5 |
| 30 m | 16.6 | 23.8 | 15.5 (colder than background) |
| 40 m | 17.1 | 26.7 | 17.0 |
| 60 m | 18.2 | 32.5 | 23.2 |

- The **lid** case is a straight, steep conductive line from near the surface. The CPT log shows the clay (high friction ratio, high excess pore pressure). The tube gives heat flux. The model reads "lidded, sensor at 2 m blind, flux q".
- The **sweep** case is near-isothermal through the aquifer (CPT shows clean sand/gravel, fast dissipation, high K) and then a steep gradient in the aquitard below. **A 30 m push would call this "cold".** Only reaching the aquifer base reveals it. This is why the rig must reach 60 m in at least half its holes.
- **Nothing**: background line, clean. A cold 60 m log through the aquifer base is strong negative evidence, much stronger than a cold 2 m reading (M21 F7).

### 1d. Hydraulic channel: upflow, not just heat
- **Thermal Peclet.** Over a 40 m interval with 2 C across it, upward Darcy flux of 2, 5 and 10 cm/yr gives a curvature signal of 18, 44 and 88 mC (Bredehoeft and Papadopulos 1965 model, calc). Noise is about 10 mC from the probe and 20-60 mC from the surface warming residual. So the thermal method alone sees **>5 cm/yr** reliably.
- **Piezocone head.** Each dissipation test runs to equilibrium pore pressure u0. Static head at each depth comes from u0 and the depth to about ±0.1-0.2 m (unverified, depends on transducer and t100 time in clay). Over 40 m this gives a vertical hydraulic gradient to about ±0.005. Dissipation t50 gives K in sand to clay (Robertson CPT guide, from memory). Upward gradient x K = **vertical water flux, measured directly**. A confined warm aquifer with upward head under a clay lid is the textbook blind outflow geometry. The rig sees both the heat and the head on one push.
- **Pore water.** A screen-point sampler (GeoProbe SP16/SP22 class) at the water table pulls 1-2 L. Lab: SiO2 and cations for geothermometers, Cl and B (deep-fluid fraction), Li, d18O/dD, and **dissolved He and Ne in copper tubes or a diffusion sampler** (M22). Mixing models (P05) turn a warm, high-Cl, high-He shallow sample into "outflow from a deep source". Lab cost about $400-900 per sample (unverified).

### 1e. What it cannot do
- **Gravel.** CPT stops at coarse gravel and cemented layers. Range-front fans, where upflow faults sit, are the worst ground. Expected reach: 60 m in 30-50% of playa-margin and distal-fan sites, 30 m in 60-80% (unverified prior; measure in the first 20 holes). A hammered dual-tube (GeoProbe DT45 class) gets through some gravel but loses the cone data.
- **Bedrock or volcanic cover.** No push. Use TG holes or wells (P10-P12).
- **Thick fast aquifers deeper than 60 m** (Snake River Plain, eastern carbonate province). It reads cold. Those need wells, E-MT (P03) or chemistry.
- **Temperature at 1-2 km** (rank 5) only through extrapolation of the sub-aquifer gradient and the geothermometers.

## 2. Prior art (from memory unless a URL is given)

- **Thermal CPT.** TU Delft T-CPT (Vardon and others, 2019; https://research.tudelft.nl/en/publications/thermal-cone-penetration-test-t-cpt/) uses the cool-down of a friction-heated cone to get thermal conductivity. Akrouch, Briaud, Sanchez and Yilmaz (2016, ASCE JGGE) did the same for geothermal heat-pump design. Commercial cones from Fugro, Gouda and Pagani carry a temperature sensor as standard (unverified details). Nobody I know of uses CPT for geothermal *exploration* heat flux.
- **Direct push in geothermal.** Granite Springs PFA (Faulds and others, 2017) used about 10 GeoProbe holes under 50 m (M03). Ormat and others have used shallow "temperature gradient probes" in the Carson Desert (unverified).
- **Shallow heat-flow holes.** USGS 1970s 30 m holes (Olmsted 1977; Raft River OFR 86-123). Sass and Lachenbruch-era heat-flow practice used 50-150 m holes with k from core needle probes.
- **Hydrogeology.** Direct-push hydraulic profiling (Kansas Geological Survey HPT, Butler and others; the GeoProbe HPT tool) logs K continuously. Piezocone dissipation for K is standard in geotechnics (Robertson and Cabal, CPT Guide, Gregg Drilling).
- **Heat as a groundwater tracer.** Bredehoeft and Papadopulos (1965) for vertical flux; Anderson (2005, Groundwater, "Heat as a ground water tracer") review.
- **Gap.** Nobody combines push heat flux, piezocone head, K, k and pore-water He in one hole and feeds it to a mask-aware occupancy model. That combination is the novelty, not any single part.

## 3. Concrete v1 design

### 3a. Rig (buy after the hired-contractor test)
- **Option A (preferred): used GeoProbe 7822DT or 6712DT class**, tracked, about 2.5-4 t, 1.9 m wide, fits on a 7 m gooseneck behind a 1-ton truck. Hydraulic push about 13-20 t with percussion hammer. With 2-4 screw anchors it can push a 10 cm2 or 15 cm2 cone. Price: used $60-150k, new $200-300k (unverified).
- **Option B: anchored CPT crawler** (Pagani TG63-150 class, 15 t with anchors, about 2 t machine). $120-250k with the data system (unverified). Better cone data, no hammer.
- **Rods and tooling:** 70 x 1 m CPT rods ($150-250 each, unverified, $10-18k), friction reducer, rod wiper, 4 screw anchors, screen-point sampler, dual-tube backup tooling.
- **Water:** 400 L tank for grout and decon.

### 3b. Thermal piezocone (DART-T cone)
- Standard 15 cm2 piezocone body (qc, fs, u2, inclination) from a cone vendor, with:
  - **Precision thermistor** behind the tip (±0.01 C after cal, 24-bit ADC).
  - **Heater sleeve**: 50-100 W nichrome band behind the friction sleeve plus a second thermistor 10 cm up. A 5-10 min heat pulse at each stop and a 10-20 min decay gives k (line-source analysis, same as a needle probe, ±10-15%).
  - **Digital cable or memory cone.** Cable through the rods is simplest for v1.
- Cost: base piezocone $15-30k plus about $3-8k of custom heater and thermistor work (unverified). Keep two cones.

### 3c. Stay-behind tube and logging
- **Tube:** 25 mm OD closed-end PVC or HDPE with an expendable steel tip, pushed in a 38 mm rod string, rods pulled, annulus tremie-grouted with bentonite slurry from the bottom up. About $3-5/m ($200-300 per hole).
- **Logging probe:** an RBR solo T or similar 0.002 C probe ($2-4k, unverified) on a 70 m marked cable and hand winch. 0.5 m steps, 30 s per stop, about 70 min for 60 m. Two re-logs at 2 and 8 weeks, done by one person on a ranch visit.
- **Optional resident string:** 8-12 calibrated thermistors on a 1-wire bus with a LoRa/cellular logger at the cap (about $400-700 per hole). It gives a year of data and shows any warming trend. Use it on 1 in 5 holes.
- **Cap:** locking flush-mount cap, a GPS tie (RTK, ±2 cm), photo.

### 3d. Power and comms
- Rig: diesel (about 40-75 hp). Cone and laptop run from the rig's 12 V. Heater: 100 W from the rig.
- Field data: CPT laptop. Upload over Starlink Mini or cellular at camp. The tube logger (optional) sends daily over LoRa to a solar gateway or a cellular modem.
- Data go straight into the THERMOS-B column likelihood as: T(z) with sd, q with sd, k(z), K(z), head(z), lithology (SBT), water table, aquifer base, and chemistry.

### 3e. Deployment and crew time per site
- Crew of 2 (operator + geo-tech). Truck plus gooseneck, roads and ranch tracks only.
- One 60 m hole with full tests: set-up and anchors 45 min; push with 6 heat-pulse/dissipation stops 3-4 h; screen-point water sample 1 h; tube and grout 1 h; decon 30 min. **About 1 hole a day at 60 m, 2 a day at 30 m.**
- Prospect pattern: a 6-10 hole transect along the head gradient from the 2 m / ranch-well anomaly toward the range front, plus 1-2 valley reference holes. **4-8 field days per prospect.**

### 3f. Cost per hole (calc, owned rig, unverified unit costs)

| Item | $ per hole |
|---|---|
| Crew (2 people, about $1,200/day incl. per diem) | 600-1,200 |
| Rig amortization ($150k over 5 years, 120 holes/yr) and maintenance | 250-400 |
| Tube, tip, bentonite | 250-350 |
| Cone wear and rod loss | 100-300 |
| Fuel and mobilization share | 100-300 |
| Lab chemistry and He (one sample per hole) | 400-900 |
| **Total** | **about 1,700-3,450, or 1,200-2,500 without chemistry on every hole** |

Hired CPT service for the first test: about $2.5-4k/day plus $2-5k mobilization (unverified). Twenty holes in 2-3 weeks: $40-80k all in, or $15-30k if we push only 30 m and skip the heat pulse.

## 4. How it shrinks the model's ranked uncertainties

These are model-side estimates (calc from the physics above plus judgment). They need the Tier 1 GHOST EIG run to confirm.

- **Rank 3, masking and lid thickness (sensitivity range 0.8 to 0).** This is the rig's core job. Each 60 m hole classifies the mask (lid, sweep, none) and measures lid thickness and aquifer base directly. In the 20/40 calibration campaign (rank 4), one push per known system and per cold control gives per-mask-class sensitivity for 2 m and Sentinel readings. I expect the prior range on "2 m sensitivity under lids" (0.8 to 0) to narrow to about ±0.15 per class after 30-40 holes. That is roughly a **3-5x cut in the rank 3 variance where the rig can reach**, and it is the term that sets how much weight a 2 m blank gets across all of Nevada.
- **Rank 1, detection gap (2-5x on N).** The rig directly tests "2 m blank, high lambda" cells: with ±15 mW/m2 it detects excess flux >0.05 W/m2 at 3 sigma. A pre-registered set of 60-100 pushes in such cells gives an observed catch rate for lidded systems that the LGCP thinning can use. I expect the 2-5x band on N to narrow to about **1.5-2.5x** in push-friendly basins (Carson Desert, Granite Springs, Buena Vista, Dixie, Smoke Creek), combined with Stage 0 and Sentinels. Less effect in gravel-heavy or carbonate valleys.
- **Rank 6, upflow location.** Head gradient plus T along a 6-10 hole transect traces an outflow plume back up-gradient. Expect upflow position error to fall from 2-5 km (ranch-well outflow sampling) to about **0.5-1.5 km** where pushes reach the confined aquifer (calc, judgment). That is the "Granite Springs gap" in M03.
- **Rank 7, conductive background and k.** In-situ k every 5-10 m and lithology at cm resolution remove most of the k error in nearby water-well and TG gradients. About a **2x cut in k error** (from ±25-30% to ±12%).
- **Rank 2, permeability.** Only a little: shallow K and head, not reservoir K. Pore-water He R/Ra near faults is a weak deep-permeability hint (M22).
- **Rank 5, T at 0.5-2 km.** Modest. Sub-aquifer gradient and geothermometers give an extrapolation that beats a 2 m reading by a lot but cannot replace a 150-500 m hole.

## 5. Rights edge

- **BLM land:** the rig is mechanized and over 10 ft, so it is outside IM 2026-024 casual use (H13). It needs an NOI (Form 3200-9, 15-day answer, $10-30k consultant clearances, public). So **do not use it on unleased BLM before a lease.** Use 2 m and 3 m darts (P02) and E-MT there.
- **Private ranch land (main use):** sign the heat option first ($1-2/ac), then push. The push is the "proof step" that decides whether we exercise, extend or drop the option, at about 1% of a TG hole's cost. It lets us hold more options per dollar, because we confirm cheaply before paying the next option fee. It can also be offered as a free **water-table and soil survey** to the rancher (depth to water, K, water quality), which helps get the option signed.
- **Edge pushes:** in checkerboard and private inholdings next to unleased BLM, pushes on the private side read the lateral plume and head direction under the BLM land. That supports a quiet BLM nomination without filing anything on BLM first.
- **State trust land** (UT SITLA, NM SLO, AZ, ID, OR): run under the state lease or a right-of-entry permit (unverified for each state).
- **State well rules.** A 60 m hole drilled to measure geothermal temperature may count as a thermal gradient well or a monitoring well under state law (Nevada NDOM NAC 534A and NDWR rules), which means a permit, a licensed driller or a waiver, and a public record (unverified, check before the first push in each state). On land already optioned, this disclosure costs little. Do not misclassify holes to avoid it.

## 6. Moat

- The hardware is ordinary: anyone can hire a CPT truck. The moat is **(a)** the labelled set of joint heat-flux, mask class, head and He readings across known blind systems and controls, which no one has, **(b)** the thermal cone and tube protocol tuned for exploration, and **(c)** pushes on our own optioned land, where data stays private. Zanskar drills its own wells but works mostly at BLM auction scale. This is a different, cheaper tier on private land. Score 3.

## 7. Risks

1. **Gravel refusal** near range fronts, where the upflow is. It could cut 60 m reach to under 30% of sites. Measure in the first 20 holes.
2. **Permit status** of 30-60 m holes in each state may require a licensed driller and public filing (unverified).
3. **Surface-warming and land-use history** biases gradients in the top 50 m unless reference holes are good.
4. **Heat-pulse k on a moving rig** may be noisier than ±12%, which is the largest term in the flux budget.
5. **Fast deep aquifers** (SRP, carbonate province) mask below 60 m; the tool reads cold there.
6. **Sage-grouse and cultural rules** limit tracked access even on private land with federal nexus (unverified).
7. **Logistics:** one rig is one hole a day. It cannot carpet a region; it must be steered by EVSI from cheaper tiers.
8. **Rig capital** of $60-250k is idle if the hired test shows poor reach.

## 8. First test (6-10 weeks, about $40-80k, unverified)

1. **Desk (weeks 0-2):** pick 4 known lidded or masked systems in push-friendly fill (Granite Springs, Upsal Hogback/Soda Lake area, Dixie Valley margin, a Buena Vista or Smoke Creek target) and 8 cold controls in the same basins, on land with a willing owner or state access. Pre-register predictions from the current model. Check each state's well rules.
2. **Hire a CPT contractor (weeks 3-6):** 20 holes (1-3 per site, plus 1 reference per basin) with a standard piezocone, temperature, dissipation stops and stay-behind tubes. Add our own clip-on heater for k on half of them.
3. **Re-log tubes** at 2 and 8 weeks.
4. **Pass bar:** ≥50% of holes reach 40 m; flux repeatability between paired holes ≤30 mW/m2; all 4 known systems show excess q ≥3 sigma or a correct mask class; ≤1 of 8 controls is a false positive. If it passes, buy a used rig and build the thermal cone. If reach is under 30%, switch to a light sonic/auger rig (H11) or keep only the hired-service mode.

## 9. Self-scores (1-5)

| Axis | Score | Why |
|---|---|---|
| model_uncertainty_alpha | 4 | Directly measures the rank 3 mask and lid, the calibration for rank 4, and helps ranks 1, 6, 7. Limited by gravel reach. |
| rights_alpha | 2.5 | Not usable on unleased BLM without a public NOI. Strong on optioned private and state land as cheap proof before the next payment. |
| buildability | 4 | Rig and cone are off the shelf; heater cone and tube protocol take 4-8 weeks. Hired-service test can start in weeks. |
| cost_scale | 3 | $1.2-2.5k per hole; $10-25k per prospect. 100x cheaper than a TG hole, but 10x dearer than a dart. |
| moat | 3 | Data and protocol, not hardware. |

## Sources

- Olmsted 1977, USGS PP 1044-B (1 m vs 30 m, Upsal Hogback): https://app.ingemmet.gob.pe/biblioteca/pdf/USGS-PP-1044-B.pdf
- USGS OFR 86-123, Raft River 30 m heat-flow holes: https://pubs.usgs.gov/of/1986/0123/report.pdf
- TU Delft thermal CPT: https://research.tudelft.nl/en/publications/thermal-cone-penetration-test-t-cpt/
- BLM IM 2026-024 casual use: https://www.blm.gov/policy/im-2026-024
- 43 CFR 3250 (NOI): https://www.ecfr.gov/current/title-43/subtitle-B/chapter-II/subchapter-C/part-3200/subpart-3250
- INGENIOUS 2 m data (GDR 1391): https://gdr.openei.org/files/1391/2m_temperature_probe_INGENIOUS_regional_data.zip
- From memory, no URL checked this run (unverified): Bredehoeft and Papadopulos 1965 (Water Resources Research); Anderson 2005 (Groundwater, heat as a tracer); Akrouch et al. 2016 (ASCE JGGE, thermal cone test); Robertson and Cabal, Guide to CPT (Gregg Drilling); Butler and others, KGS hydraulic profiling; Faulds and others 2017 Granite Springs PFA report.
- Calc: `P14_push_sim.py` in this folder.
