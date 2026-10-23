# P15: PACKSACK-CORE. A man-portable diamond corer for 100-200 m range-front bedrock holes, with sealed-core noble gas and alteration scanning

Date: 23 Oct 2026. Build candidate P15, model track. This builds on `MODEL.md` (ranks 1-9), `M08` (smectite below about 180 C, conductor non-uniqueness), `M18` (blind finds came from holes drilled for other things; Big Blind 121 C at about 823 m and Pumpernickel about 138 C at about 760 m are the deep kind), `M22` (He R/Ra is the one tracer that sees through a cold cap; McGinness 0.35-0.57 Ra; tritium and Ne corrections), `M23` (four mask classes, plume length L = rho c v b d / lambda), `P07` (ride-along memory pucks on mining core rigs), `P11` (slim-hole permeability wireline kit), `P14` (60 m thermal push rig, which stops at gravel and bedrock), `../../../hardware/evidence/H11` (own gradient rig, $25-40k per 200 m hole, BLM GEO CX of 28 Apr 2026) and `H13` (casual use, NOI leak). It does not repeat them.

**Method note.** The shared web-search budget was used up before this slice ran (0 of 3 searches went through). Everything below comes from the repo's earlier sourced notes, my own knowledge of the literature, and a new calc script, `P15_core_calc.py` (same folder). Drill model specs, prices, lab prices and state permit rules are **(unverified)** and must be checked before buying. Literature cited "from memory" gives authors, year and journal so it can be found; DOIs are marked unverified.

## Bottom line

- **What it is.** A modular, hydraulic, gas-engine diamond core drill in the "packsack" or "portable" class (Hydracore-, Winkie-, Shaw-, Discovery-type; none checked), broken into 8-14 loads that two people, a UTV trailer or a helicopter sling can move. It cuts **AQTK/BQTK wireline core (30-36 mm core in a 48-60 mm hole) to 100-200 m** in range-front bedrock and fault zones, on a pad of about 3 x 4 m, with no road and no sump pit. Every core run carries a memory temperature puck. Every hole ends as a grouted 25 mm tube for an equilibrium relog. At the collar, the crew **vacuum-seals short core lengths in steel canisters within 5-10 minutes** for pore-water He, Ne and 3He/4He, and **scans every 0.25-0.5 m of core with a handheld SWIR spectrometer and a thermal-conductivity needle**.
- **Why it matters.** It is the first tool in our stack that **samples the upflow itself**, not the outflow. Ranch wells (P01, P05) and pushes (P14) sit on fans and basin fill. The upflow sits on the range-front fault in bedrock, where pushes refuse and ranch wells are rare. Three of its signals **survive the hydrologic sweep** that hides temperature: (1) mantle He held in low-permeability matrix pore water next to the conduit, (2) clay and zeolite alteration that records past and present temperature, and (3) conductive heat in the dry rock above a deep water table. That is exactly what defeats the Big Blind-type lid.
- **Physics in three numbers** (calc, `P15_core_calc.py`). (a) Above a Big Blind-type reservoir top (121 C at 823 m), a conductive cap gives **+15 C at 150 m and +20 C at 200 m** over background. That is 100x the relog noise. (b) A BQ core sealed within 5 min loses about **10% of its pore He**, and the He/Ne ratio is biased by under 3%, which a Ne co-tracer corrects. (c) The diffusive He halo around an active conduit is about **6 m wide after 10 kyr and 18 m after 100 kyr**. So the hole must be aimed to **cross** the fault zone. An inclined hole does that.
- **Cost.** Kit about **$110-190k** (drill, rods, sealing kit, SWIR, k needle; unverified). Per 150 m hole about **$14-33k all-in** in my itemised calc (more than the brief's $8-20k, because I include He lab work, clearances and permits). Add $3-8k per hole for a helicopter where no track exists. That is **5-50x below a contract TG hole** ($150k-1.5M) and about 2x below the H11 own-rig figure, with no pad, road or mud pit.
- **Rights.** A core drill is mechanized, so it is **not casual use** on BLM land. It needs an NOI (public), but the April 2026 GEO categorical exclusion covers core drilling under 10 acres of disturbance, and our footprint is about 0.01 acre per hole. So: drill on **optioned private land, state trust land, and BLM land we already lease** (leftover noncompetitive at $1/ac/yr). Its rights job is to turn a cheap option into a **"located upflow" package** (core, He, T profile, alteration, fracture orientation) that a buyer can drill on. That raises the carry or override we can ask.
- **Self-scores:** model_uncertainty_alpha **4**, rights_alpha **3**, buildability **3.5**, cost_scale **3**, moat **3.5**.

## 1. Physics case

### 1a. Why range-front bedrock at 100-200 m is the right place to look
- **Where the upflow is.** Most Great Basin systems rise on range-front faults, step-overs and accommodation zones (Faulds settings, M11), then spill sideways into basin aquifers (M23 F3). The outflow plume can carry the shallow signal 3-30 km down-gradient. Ranch wells sample that plume. So the model's rank 6 band (upflow position 2-5 km) is a direct result of where the cheap sensors are.
- **Why pushes and 2 m probes cannot go there.** Fan gravel and bedrock refuse direct push (P14 section 1e). 2 m probes on bedrock see little because the rock is dry and conduction dominates only if heat reaches near the surface.
- **Why bedrock above a deep water table helps.** At range fronts the water table is often 100-300 m down (M23 F2, unverified range). Heat crossing dry, still rock moves by conduction. Conduction gives a clean, straight, readable gradient. The sweep that masks a basin happens **in the aquifer**, not in the dry rock above it. A 150-200 m hole into the footwall or hanging wall of the range-front fault can sit in the conductive zone over the upflow.
- **Big Blind-type case** (calc section 3 of the script). If a reservoir top sits at 823 m at 121 C, and the rock above is conductive, then:

| Hole depth | T with reservoir | Background (30 C/km) | Excess |
|---|---|---|---|
| 100 m | 27.9 C | 18.0 C | +9.9 C |
| 150 m | 34.3 C | 19.5 C | +14.8 C |
| 200 m | 40.8 C | 21.0 C | +19.8 C |

A Pumpernickel-type case (138 C at 760 m) gives +20 C at 150 m. A shallower 130 C top at 500 m gives +30 C at 150 m. These are big signals. The catch is the case where a cold aquifer **in the bedrock fractures** sweeps the top 300 m. Then temperature is weak, and the He and alteration channels carry the detection.

### 1b. Channel 1: memory BHT on every run, then an equilibrium relog
- Each wireline core run (3 m barrel) carries a 150 C memory puck (P07 design) in the inner-tube head. The run after a night or shift break gives a partly recovered bottom-hole temperature. Several shut-ins at increasing depth give a Horner-style series. Expected accuracy is about ±2-5 C on the raw series (P07 and M04 practice).
- At the end, a 25 mm closed-end steel or PVC tube is set to TD and the annulus is tremie-grouted with **bentonite, not cement**, to avoid hydration heat (P14 1b). A relog with a 0.002 C probe at 2 and 8 weeks gives an equilibrium profile good to about ±0.01-0.02 C. With core k every 5-10 m, that gives heat flow to about ±10% (calc assumption: k ±10%).
- **Curvature and reversals in bedrock** read fracture inflow and lateral outflow directly. A reversal at the water table in a range-front hole is a strong "upflow is here or up-dip" sign.

### 1c. Channel 2: pore-water He, Ne and 3He/4He from sealed core
- **Method (prior art).** Osenbrück, Lippmann, Sonntag and others (1998, Geochimica et Cosmochimica Acta 62, "Dissolved gases in the pore water of low-permeable rocks: a new method", DOI 10.1016/S0016-7037(98)00198-2, unverified) placed fresh core in evacuated, vacuum-tight containers on site. Pore-water gas out-diffuses into the headspace over weeks, then the headspace is measured on a noble-gas mass spectrometer. Rübel and others (2002, GCA 66, Opalinus Clay profiles at Mont Terri, unverified DOI 10.1016/S0016-7037(01)00859-1) and later Swiss and Canadian repository work (NAGRA, NWMO; from memory) made it routine. This is a proven, published method in clays and crystalline rock. **Nobody I know of has used it in geothermal exploration.**
- **Why He survives the sweep.** Mantle He (R/Ra 0.3-1+ in Great Basin systems, M22) rises with the deep fluid along the conduit. The matrix pore water in the wall rock exchanges with that fluid only by diffusion. My calc gives a halo half-width of about 2 m after 1 kyr, 6 m after 10 kyr, 18 m after 100 kyr and 40 m after 500 kyr (De = 1e-10 m2/s, assumed). If cold recharge later sweeps the fractures, the matrix keeps its He for a similar time scale. So the pore water is a **time-integrated record** of deep-fluid flow, not a snapshot of today's fracture water. A ranch well cannot give this; it mixes fracture water.
- **Signal.** Crustal pore water reads about 0.01-0.05 Ra and high 4He. Any matrix sample above about 0.1-0.2 Ra in the Great Basin carries a deep-fluid fraction (M22). Lab precision on R/Ra is about 1-3% (unverified). So 0.05 vs 0.02 Ra is easy to tell apart, and a profile of 4-6 samples across a fault gives the halo shape: a peak at the conduit, decaying over metres to tens of metres.
- **Loss on the way out** (calc section 1). Early-time out-diffusion from a cylinder: for a BQ core (radius 18 mm), 2 min to seal loses about 7% of He, 5 min about 10%, 10 min about 15%, 20 min about 21%. Ne is lost a little slower, so He/Ne is biased by -2% to -6%. **R/Ra is barely affected**, because 3He and 4He diffuse at similar rates (mass effect about 15% on D, giving under 1-2% on the ratio; unverified). So the protocol is: seal within 10 min, record the time, and correct concentrations with the Ne co-tracer and a one-parameter loss model. Use the core **centre**, and trim the outer 3-5 mm that drilling water touched.
- **Contamination.** Drilling water is air-saturated (R/Ra = 1). It invades fractured core. So: sample intact matrix pieces, not rubble; add a cheap tracer to the drilling water (for example a fluorescein or Br spike) and measure it in the canister rinse to flag invaded samples. Tritiogenic 3He is not an issue in deep matrix water, but one tritium sample per hole (from the drill water) is the check (M22 point 13).

### 1d. Channel 3: alteration scanning (SWIR and k needle)
- **Clay sequence as a thermometer.** Smectite is stable below about 150-180 C, mixed-layer illite-smectite forms at about 150-220 C, and illite and chlorite above about 220 C (Harvey and Browne 1991, Clays and Clay Minerals 39, Wairakei, from memory; M08). Zeolites add a low-T scale: mordenite and clinoptilolite below about 110 C, laumontite about 110-200 C, wairakite above about 200 C (textbook, unverified ranges). Opal, chalcedony, adularia and calcite habits add more (bladed calcite means boiling).
- **What SWIR sees.** The Al-OH band near 2200 nm, the water band near 1900 nm, and the shape of the 1400 nm band separate smectite, I/S, illite, kaolinite, alunite and some zeolites. Simpson and Rae (2018, New Zealand Journal of Geology and Geophysics 61, SWIR of clays in Taupo Volcanic Zone geothermal systems, from memory) showed SWIR tracks the smectite-to-illite transition in geothermal wells. The methylene blue test for smectite in cuttings (Gunderson and others, WGC 2000, from memory) is the cheap cross-check. Send 4-6 samples per hole for XRD to calibrate.
- **Why alteration survives the sweep.** Clay does not move when cold water arrives. A smectite cap above an I/S zone in a 150 m range-front hole says "this rock was over 150 C at some time". Combined with today's gradient and He, it tells active from fossil:

| Gradient excess | Matrix He R/Ra | Alteration | Reading |
|---|---|---|---|
| High | High | Smectite over I/S | Active upflow, conductive cap. **Best target** |
| Low | High | Smectite over I/S | Active deep flow, swept top. **Big Blind-type lid** |
| Low | Low | Smectite over I/S | Fossil system (false positive class for MT, M08) |
| High | Low | Little | Conductive high-heat-flow, tight. Possible EGS, not hydrothermal |
| Low | Low | None | True negative, to this depth |

- **Clay also calibrates MT.** The same smectite layer is what E-MT nodes (P03) image as a 1-10 ohm-m conductor. One core hole per MT line ties the conductor to a mineral and a temperature. This turns MT from a 2-3x likelihood ratio (M08) into something closer to 5-10x on that line (judgment, unverified).
- **k needle.** A 3.9 mm hole drilled in core and a line-source needle (METER TEMPOS TR-3 class, unverified model) gives k to about ±10% every 5-10 m. That turns gradient into heat flow and cuts the rank 7 error near the hole.

### 1e. Bonus channels at almost no cost
- **Fracture orientation.** A core-orientation tool (Reflex ACT class, rentable, unverified) on each run gives fracture strikes and dips. With local SHmax from the P03 geophone or the World Stress Map, we can test which fractures are critically stressed (Barton, Zoback and Moos 1995, from memory; P11). That is a direct permeability prior (rank 2).
- **Open-hole tests before grouting.** Run the P11 slim-hole packer or an airlift test on the open BQ hole. Get one transmissivity number per fault crossing. This needs a BQ hole (60 mm), not AQ.
- **pXRF option.** As, Sb, Hg, Tl, Cs and B are epithermal pathfinders (M22 point 9 on Hg). A rented pXRF on every 1 m gives a pathfinder profile (optional; $30-40k to buy).

### 1f. Detection limits and noise
- **Temperature:** excess over about 1 C at 150 m is detectable with the relog (noise ±0.02 C reading, ±10% k, and about ±0.5-1 C site surface-history residual; P14 numbers). The ±1 C floor is set by surface history and by the unknown k below TD, not by the probe.
- **Extrapolation to 1 km** (calc section 4, a toy Monte Carlo with an assumed chance of a deeper advective break): sd about **14 C** from a 150 m relog with core k, against about 20 C from a 60 m push tube and about 39 C from a single ranch-well reading. This toy model is only a ranking aid (unverified until the Tier 1 simulator runs it).
- **He:** detects a deep-fluid fraction of a few percent in matrix water, but only within the halo (about 5-40 m of the conduit). Miss rate is set by geometry: a vertical hole 50 m from the fault misses it. Inclined holes, planned from the fault trace and dip, cut the fault at 80-150 m.
- **Alteration:** strong for systems that reached over about 150 C at hole depth. Weak for 110-140 C amagmatic systems whose alteration is thin. Expect the alteration channel to be mostly silent for the lowest-temperature binary targets.

## 2. Prior art

- **Portable diamond drills.** Packsack and Winkie drills have been used in Canadian and Alaskan mineral exploration since the 1950s-60s for short holes. Modern modular hydraulic portable drills (Hydracore, Shaw, Discovery-class, and the small-rig line of the big drill makers; unverified models and specs) advertise helicopter-portable modules and AQ/BQ depths of 100-300 m. These are sold to mineral juniors, not geothermal explorers (from memory, unverified).
- **Slim-hole geothermal coring.** Sandia and DOE slim-hole programs (Finger and others, 1990s; OpenEI Slim Holes page, https://openei.org/wiki/Slim_Holes) showed that slim core holes give reservoir T and even flow tests at much lower cost than production-size holes. They used truck-mounted mining core rigs, not man-portable ones. Don A. Campbell's first heat came from **core holes** that found about 128 C from about 70 m (M18).
- **Pore-water noble gases from core.** Osenbrück 1998, Rübel 2002 and the NAGRA/NWMO repository work (above). Smith and others used out-diffusion methods for crystalline rocks (from memory). Mature in waste repository science. Not used in geothermal exploration as far as I know.
- **Hyperspectral core logging.** Mining uses truck- and lab-scale core scanners (HyLogger at CSIRO and state surveys, Corescan, TerraCore; from memory). GNS Science uses SWIR on Taupo geothermal core and cuttings (Simpson and Rae 2018). Handheld SWIR (TerraSpec Halo, oreXpress class) is standard in porphyry and epithermal work.
- **Thermal-conductivity on core.** Sass and Lachenbruch heat-flow practice used needle probes on core; Popov's optical scanning is the lab standard.
- **Gap and novelty.** Each piece exists. Nobody puts a man-portable corer, run-by-run BHT, a relog tube, sealed-core He isotopes and collar SWIR on **one hole at a range-front fault**, and feeds it to a mask-aware occupancy model. That combination is the novelty.

## 3. Concrete v1 design

### 3a. Drill and tooling (buy after one hired test, see section 8)

| Part | Spec | Cost (unverified) |
|---|---|---|
| Portable hydraulic core drill (Hydracore-class or similar) | Gas engine power pack 20-35 hp; mast and rotation head; rod clamp; split into 8-14 loads of 40-150 kg; AQTK to about 250 m and BQTK to about 150-200 m in hard rock (vendor claims to check) | $45-90k new, $25-50k used |
| Wireline rods | 200 m BQTK (or 250 m AQTK), 1.5 m or 3 m lengths | $16-30k |
| Core barrels, overshot, wireline hoist | 2 x 1.5/3 m BQTK inner tubes, overshot, 250 m hand or hydraulic wireline winch | $6-12k |
| Casing | 20-40 m of BW or NW casing for collars in broken rock, plus casing shoe | $3-6k |
| Bits and reamers | Impregnated diamond bits; 30-80 m per bit in volcanics and carbonates (unverified) | $400-900 each; stock 10: $5-8k |
| Water system | Triplex or piston pump, 2 x 1,000 L totes, a recirculating settling tank (no pit), polymer additive | $4-8k |
| Inclined-hole kit | Mast angle plate (45-90 deg), downhole survey shot (rent) | $1-3k |
| **Subtotal drill** | | **$80-157k** |

### 3b. Sensors and sampling

| Part | Spec | Cost (unverified) |
|---|---|---|
| Memory T pucks | 2 x 150 C stainless memory loggers in an inner-tube head adapter (P07 Puck-C) | $3-6k |
| Relog probe and winch | 0.002 C RBR-class probe on a 250 m marked cable; 25 mm tube | $3-5k |
| Core sealing kit | 16 stainless canisters (about 0.5-1 L, CF or Swagelok valve, copper-gasket lid), battery diaphragm vacuum pump plus a small rotary pump on the inverter, N2 flush bottle, timer app | $8-15k |
| Drill-water tracer | Br or fluorescein spike kit | under $0.5k |
| Handheld SWIR | 1350-2550 nm (NeoSpectra-class, about $5-8k) for every 0.25-0.5 m; rent a TerraSpec-class unit for calibration | $5-8k (or $60-90k for a full-range unit) |
| k needle | TEMPOS-class with TR-3 needle and a 3.9 mm core drill jig | $5-7k |
| Optional | pXRF rental; Reflex ACT orientation rental | $1-3k per month |
| **Subtotal sensors** | | **$25-42k** |

**Kit total: about $110-200k** (unverified). The brief's $60-150k holds only with a used drill and the cheap SWIR.

### 3c. Power
- Drill: 20-35 hp gasoline or diesel power pack (the drill's own).
- Camp and sensors: 2 kW inverter generator for the vacuum pump, laptop, SWIR and charging; sensors on their own batteries.
- Fuel: about 20-40 L per shift (unverified). One UTV run per day carries fuel and water.

### 3d. Comms and data
- Starlink Mini at camp, satellite messenger for safety.
- A tablet app logs each run: depth, run time, puck ID, canister ID and **seal time**, SWIR file IDs, core photos, recovery, RQD and fracture picks.
- Nightly upload into THERMOS-B column likelihoods: T(z) with sd (puck, then relog), k(z), alteration class by depth with confidence, He/Ne/R/Ra with a loss correction and an invasion flag, fracture orientations, and open-hole T (transmissivity).

### 3e. Deployment and crew time per site
- **Crew of 3:** driller, helper, and a geologist who runs the sealing, SWIR and k. The geologist is our staff; the driller can be a contractor at first.
- **Access:** UTV with a 1.5 t trailer (2-3 trips) on ranch tracks, or a helicopter with 8-14 sling loads (about 2-4 h of flying, unverified) where there is no track. No road building and no pad cutting. Footprint about 3 x 4 m plus a tote and a core rack.
- **Time per 150 m hole** (unverified rates):
  - mobilise and set up: 0.5-1 day;
  - drilling at 25-50 m per 10 h shift in hard volcanics and carbonates: 3-6 shifts;
  - surveys, open-hole test: 0.5 day;
  - set tube and grout: 0.5 day;
  - demobilise and reclaim: 0.5 day;
  - **total 5-8 days per hole, 2 holes per prospect cut across the fault, plus 1 relog visit by one person.**
- **Throughput:** about 25-35 holes a year per kit with one crew (unverified).

### 3f. Cost per hole (calc, `P15_core_calc.py` section 5)

| Item | $ per 150 m hole |
|---|---|
| Crew of 3, 6-8 days | 6,500-13,000 |
| Bits, reamers, shells | 1,500-4,500 |
| Rod and barrel wear | 600-1,500 |
| Water, additives, grout, tube | 800-2,000 |
| Fuel, UTV or truck | 400-1,200 |
| He lab, 4-6 canisters | 2,000-4,200 |
| XRD, tritium, water chemistry | 600-1,500 |
| Kit amortisation | 1,000-1,500 |
| Permit, bond and clearance share | 500-4,000 |
| **Total** | **about 14,000-33,000** |
| Helicopter where needed | +3,000-8,000 |

Cost per **located upflow** (a hole that lands in the He halo or the hot zone): about $180-790k at 15-40% hit rates and 3-5 holes per prospect. That is roughly one contract TG hole per located upflow, and that TG hole would usually be on the fan, not the fault.

## 4. How it shrinks the model's ranked uncertainties

Estimates from the physics above plus judgment. GHOST Tier 1 in-silico EIG must confirm them before buying hardware.

- **Rank 6, upflow location and footprint.** This is its main job. A hole that cuts the fault zone and shows a He peak plus a gradient excess pins the upflow to the hole's trace, about **±0.2-0.5 km**, against 2-5 km from outflow back-projection. Two holes across strike give a width. Combined with P14 transects (outflow) and E-MT (cap outline), I expect a **5-10x cut in the variance of upflow position** on drilled prospects, and a 2-3x cut in footprint area variance (clay cap extent ties the MT outline to a mineral, so MT stops overstating area).
- **Rank 5, T at 0.5-2 km.** An equilibrium 150-200 m bedrock log with core k cuts the 1 km extrapolation sd from about 39 C (ranch well) or 20 C (P14 push) to about **14 C** (toy calc). Clay geothermometry gives an upper bound on past T at hole depth. Pore-water He plus the sealed fluid geothermometers from nearby wells pin the deep end member. The sloped Tmin line means 14 C is about 0.5-1 km of depth error, against 1.5-2 km today. **About 2-3x on the rank 5 sd** where we drill.
- **Rank 2, permeability class.** He R/Ra in matrix next to the fault is a permeability label (M22, Banerjee 2011). Fracture orientation plus SHmax gives slip tendency on the real fractures. An open-hole test gives one transmissivity. Together I expect the 10x MWe band from permeability to drop to about **4-6x** on drilled prospects. This does not replace a flow test at reservoir depth.
- **Rank 1, detection gap for deep or lidded systems.** This is where the tool is unique. Its He and alteration channels fail under **different** masks than temperature does. Under the shared mask latent, that makes it the second detector that identifies q for the lidded class. A pre-registered set of **40-60 holes**: about 15-20 at range fronts of known blind systems (calibration, rank 4) and 25-40 at high-lambda, low-P_det range fronts where 2 m and ranch wells are blank. That gives a measured catch rate for the deep-only class, which today has one or two public examples (M18). I expect the 2-5x band on N for the **lidded, deep-only class** to narrow to about **1.5-2.5x** (cost about $0.6-2M). Effect on the total N band is smaller, because shallow-plume systems are already well caught.
- **Rank 3, masking state.** The table in 1d classifies the mask directly at each hole (conductive cap, swept top, fossil, none). In bedrock this is better than any other tool, but it is point data. Modest regional effect, strong local one.
- **Rank 4, sensor reliability.** Each calibration hole gives a ground-truth mask class under the cheap sensors nearby (2 m, darts, Sentinel, E-MT). It adds bedrock-truth rows the P14 rig cannot get.
- **Rank 7, conductive background.** k every 5-10 m on bedrock core, plus basement contact depth where the hole crosses it. About 2x on k error near the hole.
- **Ranks 8 and 9:** no direct effect.

**Variance share it can shrink.** If the THERMOS-B variance split puts about 30-40% of the RNPV/ac variance on drilled range-front prospects into upflow position, deep T and permeability (unverified share), this tool attacks most of that. It is a **prospect-scale** shrinker, not a regional one. Regional effect comes only through the catch-rate calibration (rank 1).

## 5. Rights edge

- **BLM land.** Mechanized drilling is outside IM 2026-024 casual use (H13). It needs an NOI (Form 3200-9) and a bond, and the NOI is visible to anyone who watches BLM records. The April 2026 GEO CX covers core drilling and TG wells under 10 acres of disturbance (H11), and the helicopter or UTV setup has almost no disturbance, so clearance should be fast (15-25 day BLM answer, plus cultural and biological surveys, about $10-30k per NOI, unverified). **Rule: drill BLM land only after we hold the lease** (leftover noncompetitive at $1/ac/yr, or after a nomination we already won).
- **Private ranch land (main use).** Sign the heat option first (about $1-2/ac). Then core the range-front fault on or next to the ranch. Low disturbance (no road, no pit, helicopter if needed) makes the rancher's yes easier. The relog tube can double as a groundwater monitoring point for the rancher.
- **State trust land.** Under the state lease or a right-of-entry permit (unverified per state).
- **State well rules.** In Nevada a geothermal TG or core hole needs an NDOM permit under NAC 534A, a bond, filed logs and plugging. The permit is public; the data stay confidential for a period (H11, term unverified). Other states have similar rules (unverified). **Do not file holes as mineral exploration to avoid this.** Where a real mineral explorer is already drilling, P07 is the honest route.
- **What it does for the rights price.** Today we sell options with an anomaly. A "located upflow" package (core, sealed He profile, equilibrium T, alteration column, fracture set, one transmissivity) is the thing a buyer's geologist needs to site a production-size well. It moves a prospect from "anomaly" toward "drill-ready". The memo's step-up is about $0.1M/MW at confirmation and less at anomaly stage. If this package moves us even partway, say from about $0.02-0.04M/MW to about $0.05-0.08M/MW on a 30 MW prospect (unverified, judgment), that is about **+$1M per prospect** for $50-150k of coring. It also lets us **drop bad options early** at $15-30k per hole, so we can carry more options per dollar.

## 6. Moat

- The drill is a commodity. Anyone can hire a portable driller.
- The moat is the **labelled set**: joint T, matrix He, alteration and fracture data at range-front faults of known blind systems and cold controls. Nobody has this. Zanskar drills its own wells, but on BLM auction land and at larger scale. A cheap bedrock tier on private land is a different layer.
- The **sealed-core He protocol** in geothermal is new and has real know-how (seal timing, invasion tracer, loss model). It is a few months of lead, not years.
- Holes on our own optioned land keep data private until the confidentiality clock runs out, long after we have acted.
- Score 3.5.

## 7. Risks

1. **Drilling in fault zones.** Broken, clay-rich fault rock causes lost circulation, caving and stuck rods. Portable drills have little pull-back force. Expect some holes to stop short of 150 m. Mitigation: casing advance, polymer muds, and aiming to cross the fault at 80-150 m, not at TD.
2. **He halo is narrow** (5-40 m). A hole that misses the conduit reads crustal He and gives a false negative. Mitigation: inclined holes planned from the mapped fault, two holes per prospect, and treat He as a "hit if present" channel in the likelihood.
3. **He loss and drill-water invasion** may be worse in fractured rock than the calc assumes. Mitigation: the paired 2 min vs 20 min seal test in the first holes measures it.
4. **Amagmatic, low-T systems (110-140 C) may have thin alteration** and low R/Ra, which weakens two of the three channels where many binary targets sit.
5. **Permit and disclosure.** Every hole is a public permit in Nevada and an NOI on BLM. This tips our hand unless we already hold the right.
6. **Speed claims of portable drills in hard rock** are vendor claims (unverified). If real rates are 15 m per shift, cost per hole roughly doubles.
7. **Lab bottleneck.** Noble-gas labs (Utah, LBNL, WHOI, GNS; M22) have queues and $300-700 per sample (unverified). 30 holes x 5 samples is 150 samples a year, which is fine, but turnaround may be months.
8. **Safety.** Remote helicopter-supported drilling needs real HSE planning and an experienced driller.

## 8. First test

**Step 0, desk and archive (weeks 1-4, about $5-10k).** Scan archived core and cuttings from known blind systems at the NBMG Great Basin Science Sample and Records Library and the EGI/UGS core archive (M20, L16) with a rented SWIR unit. Check that the smectite / I-S / illite pattern lines up with logged temperatures at 3-5 known systems (for example Don A. Campbell, McGinness, Desert Peak, if core exists; unverified). Pass if clay class predicts the T band in at least 70% of 0.5 m intervals against XRD. This tests channel 3 without drilling.

**Step 1, hired portable driller (weeks 4-14, about $60-110k).** Hire a portable diamond contractor (BC, Yukon or Alaska firms commonly do this work; Nevada availability unverified) for **3 holes**: 2 inclined holes across a mapped range-front fault next to a known blind system, on private land or land held by a cooperating partner, plus 1 cold control on the same fault type away from any system. Pre-register the predicted T at 150 m, the R/Ra, and the clay class for each hole. Measure:
- metres per shift and core recovery in fault rock;
- He loss: paired canisters sealed at 2 min and 20 min from adjacent core;
- puck BHT against the 2- and 8-week relog;
- SWIR class against XRD;
- matrix R/Ra at the known system against the control.

**Pass (buy the kit):** at least 120 m reached in 2 of 3 holes; He loss under 25% at 10 min; matrix R/Ra at the known system at least 3x the control; relog excess matches prediction within 5 C. **Fail:** portable rigs cannot pass fault zones, or He is fully invaded in fractured core. Then keep only the SWIR and k part and attach it to P07 (ride-along on mining rigs).

## 9. Self-scores (1-5)

| Axis | Score | Why |
|---|---|---|
| model_uncertainty_alpha | 4 | Directly attacks rank 6 (5-10x local), rank 5 (2-3x), rank 2 (about 2x), and gives the deep-only class its first catch-rate data (rank 1). Point-scale, not regional |
| rights_alpha | 3 | Not casual use, so it leaks on BLM; strong on optioned private land; raises package value and lets us drop options early |
| buildability | 3.5 | Off-the-shelf drill and sensors; integration is protocol work; needs a skilled driller; 8-14 weeks to the first hired holes, 4-6 months to own kit |
| cost_scale | 3 | $14-33k per hole is 5-50x below TG, but it is per site, about 25-35 holes per kit-year |
| moat | 3.5 | Drill is a commodity; the joint labelled set and the sealed-He protocol are new |

## Sources

Repo files (all sourced there): `MODEL.md`, `M08`, `M11`, `M18`, `M20`, `M22`, `M23`, `P07`, `P11`, `P14`, `../../../hardware/evidence/H11-own-gradient-rig.md`, `H13-permits-and-secrecy.md`.

Primary sources carried from those files:
- BLM IM 2026-024 (casual use): https://www.blm.gov/policy/im-2026-024
- BLM GEO categorical exclusion, 28 Apr 2026: https://public-inspection.federalregister.gov/2026-08235.pdf and https://www.blm.gov/press-release/blm-takes-steps-accelerate-geothermal-energy-development
- 43 CFR 3250 NOI: https://www.ecfr.gov/current/title-43/subtitle-B/chapter-II/subchapter-C/part-3200/subpart-3250
- Nevada NAC 534A: https://www.leg.state.nv.us/NAC/NAC-534A.html
- OpenEI Slim Holes: https://openei.org/wiki/Slim_Holes ; Thermal Gradient Holes: https://openei.org/wiki/Thermal_Gradient_Holes
- Banerjee et al. 2011 (deep fault-controlled He transport): https://www.usgs.gov/publications/deep-permeable-fault-controlled-helium-transport-and-limited-mantle-flux-two
- USGS western-US water and gas chemistry (Gregoire, Peek, Hurwitz 2024): https://doi.org/10.5066/P96Q13U3
- Lachmar et al. 2017 (Kimama smectite seal under the SRP aquifer): https://link.springer.com/10.1186/s40517-017-0086-8

From memory, not checked this session (unverified): Osenbrück et al. 1998 GCA 62; Rübel et al. 2002 GCA 66; Harvey and Browne 1991 Clays and Clay Minerals 39; Simpson and Rae 2018 NZJGG 61; Gunderson et al. 2000 WGC methylene blue; Barton, Zoback and Moos 1995 Geology 23; portable drill vendor specs and all prices.
