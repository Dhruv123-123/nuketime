# P13: Drone Dart Carpet (drone-dropped 1 m year-long thermal darts, plus a heavy-lift "sherpa" drone that places and recovers all sensors)

Date: 23 Oct 2026. Build candidate P13, model track. This builds on `P02` (3 m logged heat-flux dart, its noise simulator and its "differential detector" lesson), `P03` (drone-placed E-MT node, drone kit, FAA notes), `../../../hardware/evidence/H01` (2 m carpet, LoRa BOM), `H13` (BLM IM 2026-024 casual use), `M21` (INGENIOUS 2 m analysis: 64% blank rate, about 1.2 C noise, 2.4 C between-area scatter) and `MODEL.md` (SENTINEL-COX ranks). It does not repeat them.

**Method note.** The shared web-search budget was already used up when this slice started, so **no web searches or fetches ran**. Everything comes from repo files, what I already know, and two pieces of my own arithmetic: a pair-noise simulation (`P13_dart1m_sim.py`, which reuses the P02 forward model) and an energy-balance penetration estimate (section 2). Prices, drone specs and prior-art details are from memory and marked (unverified). Simulation results are marked (calc).

---

## Bottom line

- **The idea works, but not as briefed. Two numbers in the brief are wrong.**
  1. **A drop from 20-40 m cannot drive a dart 1 m into desert basin fill.** A 3 kg dart dropped from 30 m carries about 0.9 kJ. Getting a 25 mm rod 1 m into medium-dense alluvium takes about 5-10 kJ (calc, section 2). That drop reaches about 0.15 m in medium ground and about 0.45 m in loose sand. **Fix:** drop from the Part 107 ceiling (100-120 m AGL), use a 20 mm stainless shaft with a heavy steel head (about 4 kg total), and log the real penetration with an on-board high-g accelerometer. Expected depth: **about 1.0 m (stopped by the head collar) in loose-to-medium valley fill, 0.6-0.8 m in medium, and 0.35-0.5 m in dense fan gravel. Caliche stops it** (calc, rough).
  2. **The "steady offset" (the fitted 1 m annual-mean temperature) is not a 0.3-0.5 C detector in the field.** In my simulation, the pair difference has a noise of 0.2 C *if every site had the same surface mean temperature*. Real sites differ by roughly 0.5-1 C because of albedo, shrub cover and slope aspect. No harmonic fit can remove that, so the offset noise rises to **about 1 C** (calc, with a 0.7 C site prior that is unverified). **The detector that works is the 0.3-1.0 m gradient times k**, because the surface offset cancels in a gradient. Its per-pair noise is about **190 mW/m²** (calc). That gives **about 0.4-0.6 W/m² excess flux at 3 sigma per dart** against a valley reference. This is about the same as a logged 2 m probe (P02: about 0.5 W/m²), 3x better than a one-shot 2 m probe (about 1.5 W/m²), and 3-5x worse than the P02 3 m dart (0.1-0.2 W/m²).
- **Its value is area, not sensitivity.** An upflow footprint of 1.5-10 km² (M21) holds 6-250 darts at 1 per 4-25 ha. Site errors are mostly independent, so a footprint-average reaches **about 0.1-0.25 W/m²** for footprints of 2 km² or more (calc, sqrt-N scaling, judgement). That is P02-class sensitivity for wide systems, at a fraction of the cost, and with **no vehicle off existing roads**.
- **Depth reach.** Under a dry conductive lid over 100 C fluid (k 1.2 W/m/K), one dart sees fluid shallower than **about 200 m**. A cluster over a wide footprint sees down to **about 400-800 m** (calc, same z = k·ΔT/q formula as P02). Swept (cold, fast aquifer) masks stay blind, as for every surface method.
- **Cost (all unverified).** The dart is about **$60-80 at 1k units** and about $130-160 as a prototype. One drop costs about $15-25 per dart, because one crew can drop 100-150 a day. Recovery on foot is the biggest cost, at **$30-45 per dart in v1**. All-in, a deployment is about **$80-110 per point**. That gives **about $350-450/km² at 1 per 25 ha, $550-700/km² at 1 per 16 ha, and $2.0-2.7k/km² at 1 per 4 ha.** Against a logged 2 m carpet at the same spacing this is **about 2.5-3x cheaper in v1**. It is **4-6x cheaper in v2**, where the sherpa drone also does recovery. The brief's "1/5-1/10 the cost" needs v2.
- **Model value.** This is the cheap, stratified-random, effort-tagged first pass that CREAM-COX wants for **rank 1** (detection gap), with calibrated P_det per dart. It also gives a coarse **rank 6** footprint (200-500 m pixels) and a real **rank 7** product (κ from the annual wave to about 1-3%, plus a basin background-flux field). It is weak on rank 2 (permeability) and rank 5 (deep temperature).
- **Rights edge.** A crew can carpet about **1,500-4,000 km² per season** of unleased BLM and state land under casual use, filing nothing. The output is a private basin-wide heat map, timed for leftover BLM $1/ac/yr parcels and state first-file. One limit is that the year-long record means **only about two full carpet cycles fit inside the IM 2026-024 window**, which ends 30 Sep 2029.
- **Self-score:** model uncertainty alpha 3.5, rights alpha 4, buildability 4, cost/scale 4.5, moat 2.5. **Total 18.5/25.**

---

## 1. Physics case

### 1.1 What a 1 m year-long dart measures

Below the daily zone (about 0.3 m), the annual-mean soil temperature is T̄(z) = T̄_s + (q/k)·z. The annual wave decays as e^(-z/d), and its phase lags by z/d. Here d = sqrt(2κ/ω), which is 1.7-2.8 m for κ of 0.3-0.8 ×10⁻⁶ m²/s, so **at 1 m the wave is still 60-70% of its surface size** (±8-9 C). With three sensors over 0.3-1.0 m and 12 months of data, a harmonic fit (mean plus annual plus semi-annual terms) gives:

- **κ** from the amplitude ratio and the phase lag between sensors. This is the classic Horton-Wierenga-Nielsen method. In my simulation it is within 1.3% (1 sigma) under ideal physics (calc). With real moisture changes, assume 5-10%.
- **k = κ·C.** Volumetric heat capacity C is about 1.3-2.5 MJ/m³/K, set mostly by moisture. With a soil-type prior and the dart's moisture context, k is good to about **±15%** (judgement). There is no heater. P02's heater does better (±10%), but it needs a big battery and a wired annulus, which a dropped dart cannot have.
- **Annual-mean temperatures at three depths.** Their slope is the conductive gradient G. Their level is T̄_s + G·z (the "offset").

### 1.2 Noise simulation (`P13_dart1m_sim.py`, 16 seeds, pair of darts under shared weather)

Forcing and physics are the same as P02: a ±13 C annual wave, AR(1) weather (3 C, 3-day memory), ±0.5 C interannual shifts, top-1.5 m k varying 0-30% with moisture, k varying about 30% between sites, and TMP117-class sensors (±0.01 C). I added a **site surface-mean offset of sd 0.7 C** (unverified prior; M21 measured 2.4 C between *areas*, and within one valley on one landform it should be smaller), plus a ±5 cm sensor-spacing error from the penetration log.

| Estimator, 12-month record, dart pair | Noise (1 sigma) | Comment |
|---|---|---|
| Harmonic-fit 1 m offset, no site surface offset | 0.22 C | This is the brief's "0.3-0.5 C" number. It is only true on a uniform surface. |
| **Harmonic-fit 1 m offset, with site surface offsets** | **0.97 C** | The surface mean dominates. A single 1 m offset is about as noisy as a one-shot 2 m reading. |
| 2 m 12-month mean, with site offsets (reference) | 0.98 C | The same problem affects 2 m logged probes read as temperatures. |
| **Gradient 0.3-1.0 m × k (k ±15%)** | **189 mW/m²** | Site offsets cancel. This is the estimator to use. |
| P02 3 m dart, deep pair (reference) | 31 mW/m² | Depth wins. P13 trades about 6x sensitivity per point for about 3-6x lower cost per point and no vehicle. |
| κ from amplitude ratio | 1.3% | Ideal physics. |

**Per dart against a valley reference** (10-20% of darts on cold ground): about 130-190 mW/m² at 1 sigma, so **about 0.4-0.6 W/m² at 3 sigma**. In 2 m-equivalent temperature terms (k about 1), that is about **0.8-1.2 C per dart at 3 sigma**, and **about 0.3 C for a cluster of 8-16 darts** over one footprint. With covariates (Landsat or ECOSTRESS land-surface temperature, NDVI, albedo and DEM aspect), part of the surface offset can be modelled, and the offset estimator becomes a useful second channel. If the covariates explain half the site variance (unverified), the offset noise falls to about 0.5 C.

**Signal size.** A Granite Springs-type flux (0.26-0.33 W/m², from M21/P02) is about 1.5-2 sigma per dart and **5-8 sigma for a 16-dart cluster**. A 2 m-visible anomaly of 3 C or more (about 1.5 W/m²) is more than 8 sigma per dart. Detecting those is easy. The real task is finding the 0.2-1.5 W/m² band that one-shot 2 m surveys miss.

**The brief's validation test (r ≥ 0.8 against 2 m probes)** is easy to pass where anomalies exist. If the true 2 m anomaly varies by 3 C across a transect and the dart noise is about 1 C equivalent, r is about 0.95 (calc). It should be pre-registered as **"r ≥ 0.8 on transects with a 2 m range above 3 C, and a matched blank rate on controls"**, so it is not passed trivially.

### 1.3 Error sources the simulation leaves out (they set the field floor)

- **Infiltration and rectification** in the top 1 m are stronger than at 3 m. Do not site darts in washes, on playas or on irrigated land.
- **Short penetration.** At 0.6 m the gradient baseline shrinks to about 0.35-0.45 m, which roughly doubles the noise. The accelerometer log tells us which darts are short, and the model down-weights them.
- **Stainless shaft conduction.** A 20 × 2 mm 304 tube has about the axial conductance of a 2-3 cm soil annulus (P02 estimate). It is the same for every dart, so it cancels in a pair. It is calibrated in the field test.
- **Terrain.** Slope and aspect shift the surface mean by 1-3 C (unverified). The gradient estimator mostly removes this. Near range fronts, a DEM correction is still needed.
- **Year-to-year drift and wildfire.** A burn scar changes albedo for years. Flag burns from MTBS or satellite.

---

## 2. Penetration: the make-or-break physics

**Energy balance (calc, rough).** E needed to reach depth z is about η·(q_c·A·z + f_s·π·D·z²/2), with a dynamic factor η of about 1.5 (judgement). q_c is cone tip resistance and f_s is sleeve friction. The q_c and f_s values are typical textbook CPT ranges from memory (unverified).

| Ground | q_c, f_s | E to 1 m, 25 mm rod | E to 1 m, 20 mm rod | Depth: 3 kg from 30 m (0.9 kJ) | Depth: 4 kg from 120 m (about 4.5 kJ) |
|---|---|---|---|---|---|
| Loose sand, silt, eolian | 2 MPa, 20 kPa | 2.6 kJ | 1.9 kJ | about 0.45 m | 1.0 m (head stop) |
| Medium valley alluvium | 8 MPa, 60 kPa | 9 kJ | 6.6 kJ | about 0.15 m | about 0.7-0.8 m |
| Dense, gravelly fan | 20 MPa, 120 kPa | 22 kJ | 15 kJ | under 0.1 m | about 0.35-0.45 m |
| Caliche, bedrock, cobbles | refusal | - | - | bounce | refusal |

- Air drag on a slender finned dart is small. Terminal velocity is several hundred m/s, so a 120 m drop lands at about 47 m/s (calc).
- Sandia's empirical Young penetration equation predicts deeper penetration than this energy balance in soft soil (from memory; SAND97-2426, unverified). The truth will come from **drop tests**, which are the first gate (section 7).
- **Buckling.** A 1.2 m, 16 mm fibreglass rod under a 3 kg head buckles at about 0.9 kN (Euler, calc). That is far below the 3-6 kN impact load. So the shaft must be a **20 × 2 mm stainless tube** (Euler load about 6 kN, calc), or fibreglass at 25 mm or more with lower penetration. **The brief's fibreglass dart does not survive the impact.**
- **Shock.** Average deceleration is about 120-300 g, with short peaks near 1,000 g. Potted small electronics survive this routinely (artillery fuzes survive far more; from memory). Cells are potted, and the battery is axial.
- **Implications.** (a) The carpet fits **valley floors and distal fans**, which are mostly fine-grained. (b) Range-front proximal fans, where many upflows sit, will often stop short. For those, use P02 drive-and-drop darts or the v2 vibro-driver (section 3.6). (c) Plan for **about 15-30% short or refused drops** (judgement) and log them as effort with lower P_det, not as failures.

---

## 3. Concrete v1 design

### 3.1 The dart ("D1")

| Part | Spec | $ at 1k (unverified) |
|---|---|---|
| Shaft | 304 stainless tube 20 mm OD × 2 mm wall × 1.15 m | 14 |
| Tip | Hardened 4140 ogive, 20 mm, press-fit and potted | 4 |
| Head / ballast / stop collar | 2.4 kg steel puck, 70 mm diameter, which also stops penetration at 1.0 m | 6 |
| Tail fins | 4 glass-nylon fins on the head, break-away | 2 |
| Temperature | 3 × TMP117 on a thin flex string at 0.25, 0.60 and 0.95 m below the collar, foam-pressed to the wall, plus 1 in the head for air and surface. Bath-matched to ±0.01 C relative | 14 |
| MCU + radio | STM32WL LoRa module (RAK3172 class) | 7 |
| Penetration log | ADXL375 ±200 g accelerometer (integrated to give depth ±5 cm), plus a low-g tilt sensor | 9 |
| Flash, RTC | 4 MB | 2 |
| Battery | 1 × Li-SOCl₂ AA (2.4 Ah, about 8 Wh) | 4 |
| Potting, antenna (helical in the head), QR + UHF RFID tag, assembly, calibration | | 10 |
| **Total** | **about 4.0 kg, 1.2 m** | **about $72 (range $60-80); prototype run of 50: $130-160** |

**Power.** Three sensors sampled every 30 minutes, plus one LoRa summary a day, plus sleep, comes to about 1-2 Wh per year (calc). One AA cell lasts 3+ years, so a dart can sit through two seasons if recovery slips.

**Comms.** The antenna is about 5 cm above the ground, so its range to a ridge gateway is only 1-3 km (unverified). Two layers:
1. Darts in sight of the P02/H01 ridge gateway (solar + LoRa + Starlink Mini) uplink daily summaries.
2. Every dart keeps its full record. **The sherpa drone flies a monthly "data-mule" pass at 60-120 m with a LoRa gateway on board.** This collects all records and gives a health check, at about 1 drone-hour per 25 km².

### 3.2 The sherpa drone and dispenser

- **Airframe (pick one in the build sprint).**
  - (a) A **US-built heavy lifter under 55 lb total**, Freefly Alta X class (from memory, unverified). Payload about 8-10 kg at our weights, so **2 darts per sortie**. Part 107 only. About $25-40k with RTK and a payload release.
  - (b) An **ag-class 20-40 kg payload lifter** (Hylio AG-class built in the US, or a DJI FlyCart-class aircraft), carrying **6-8 darts per sortie**. Over 55 lb, so it needs a **49 USC 44807 exemption**, which ag operators get routinely (unverified). About $20-45k. DJI may be hit by the FCC Covered List and NDAA actions (unverified, check this). Prefer US or allied.
  - **Recommendation: (b) under 44807, with a US airframe.** Ship (a) first while the exemption is pending.
- **Dispenser.** A rotary magazine of 6-8 vertical tubes with servo latches. The fins hold the dart straight. An RTK-tagged release fires at 100-120 m AGL over the pre-planned point. Drift is under about 2-3 m in light wind (calc, judgement).
- **Other payloads on the same frame.** E-MT node hub with wire legs (P03), soil-gas cups, 2 m probe tubes lowered by winch. The release and RTK stack are shared.

### 3.3 Deployment method and crew time

- **Siting.** Use a stratified-random design inside high-λ, low-P_det cells (from VOI-Bank), plus 10-20% reference darts on cold ground of the same landform. Avoid washes, playas, irrigated fields, slopes over 10°, sage-grouse leks in season, wilderness and WSAs, and cultural sites (H13). Pre-register every point in VOI-Bank with its effort tag before the drop.
- **Drop day.** Two people (one pilot, one loader/visual observer) work from a truck on an existing road. Each launch point covers about 3 km² under VLOS. With magazine (b): a 12-15 minute sortie drops 6-8 darts, then a 5 minute swap. That gives **about 100-150 darts per crew-day**, or about **0.1-0.15 person-hours per dart**. At 1 per 16 ha that is **about 15-25 km² per crew-day**.
- **Recovery v1 (on foot).** Pull-out needs about 3-6 kN (shaft friction, plus a year of set-up; calc and judgement). A walker carries a 4 kg lever jack with a collar clamp. With 200-500 m between darts, a person recovers about **25-40 darts per day, or 0.2-0.3 person-hours per dart.** The 20 mm hole is backfilled by boot. Darts are located by GPS plus the RFID tag.
- **Recovery v2 (sherpa recovery).** The drone lands over the head and clamps the collar. A **self-reacting geared winch of about 6 kN, under 4 kg, at about 1 cm/s** (around 60 W from the flight pack) pulls the dart, using the landing gear as the reaction frame (calc). This is unproven, but the engineering is ordinary. It cuts recovery to about 0.05-0.1 person-hours per dart.
- **Turnaround.** Refurbish (new cell, re-pot the head, re-check the bath calibration) for about $10-15. Expect 3-4 deployments per dart, with about 10% lost per cycle to cattle, floods and theft (unverified).

### 3.4 Cost per point and per km² (v1, unverified inputs)

| Item | $ per dart-deployment |
|---|---|
| Dart amortized over 3 cycles, plus 10% loss | 25-30 |
| Drop (2 people at $1.2-1.5k/day plus drone amortization, 100-150 a day) | 12-20 |
| Recovery on foot (v1) | 30-45 (v2: 8-15) |
| Refurbish, data, QA | 12-18 |
| **All-in** | **about $80-110 (v2: $55-80)** |

**Per km²:** about $350-450 at 1 per 25 ha, $550-700 at 1 per 16 ha, $2.0-2.7k at 1 per 4 ha. **Fleet capital:** 1,000 darts ($70-80k), 2 drones with dispensers ($60-90k), bath and calibration rig ($5k), gateways ($5k), for a total of **about $150-180k**. A 300-dart pilot costs about $70-90k (unverified).

**Throughput.** One drop crew plus 2-3 walkers carpets about **1,500-4,000 km² per year at 16-25 ha spacing**. That covers the high-λ cells of roughly 10-20 Great Basin valleys per season.

### 3.5 Data product per dart

Each dart reports: q ± σ_q (gradient × k), k and κ ± σ, 1 m offset ± σ (covariate-corrected), the wave amplitude and phase, penetration depth and tilt, a quality flag, RTK position (±0.05-2 m, which helps rank 7), and the effort tag. These enter THERMOS-B as a **censored flux likelihood with a per-dart detection limit**. They enter CREAM-COX as a detector with known P_det(lid depth, mask class).

### 3.6 v2 options (later builds)
- A **drone-landed vibro-driver** (a 1-2 kW eccentric vibrator, with the drone as the reaction mass) to push 1.5-2 m darts into dense fans. Speculative, but vibratory driving is very efficient in granular soil (judgement).
- A **gas-cup dart**: a hollow-tip version with a membrane and a sorbent cartridge for passive He, CO₂ or Hg over the year, recovered with the dart. It adds M22 segment-scale data at about +$15 per dart.

---

## 4. Prior art (from memory unless a URL is given; all unverified)

- **1 m temperature surveys for geothermal.** Olmsted (1977), USGS Professional Paper 1044-B, used **1 m** temperatures in Nevada geothermal areas and found that seasonal and surface corrections dominated, which is the same lesson as section 1.2 (https://pubs.usgs.gov/publication/pp1044B). Kappelmeyer (1957) and LeSchack and Lewis (1983) did shallow surveys. Coolbaugh, Sladek, Kratt and others built the modern 2 m method (GRC Transactions 2007 onward). All of these are **one-shot** readings. None used year-long gradients with κ fitted per probe.
- **Annual-wave diffusivity.** The amplitude, phase and harmonic methods for κ from soil temperature are standard (Horton, Wierenga and Nielsen, 1983, Soil Sci. Soc. Am. J. 47:25-32).
- **Air-dropped ground sensors.** In the Vietnam-era Igloo White program, ADSID seismic spikes were dropped from aircraft and buried themselves. Planetary penetrators include NASA Deep Space 2 (Mars, 1999, lost on arrival) and the Japanese Lunar-A design. **Free-fall penetrometers** (for example the BlueDrop at Virginia Tech) use impact deceleration to log soil strength. That is the basis for our accelerometer depth log, and a free soil-strength channel.
- **Drone-placed sensors.** Drone delivery of seismic nodes has been trialled by vendors and oil majors (P03, unverified). Agricultural drones drop sensors and seeds. **I know of no drone-dropped, year-long thermal carpet for geothermal** (absence of evidence).
- **Zanskar** uses large-N passive seismic and its own wells, not shallow-thermal carpets (M13, M32). Fervo and Ormat use conventional 2 m and TG work (judgement).

---

## 5. How much it shrinks the model's ranked uncertainties (judgement, untested)

| Rank | Effect | Size |
|---|---|---|
| **1 Detection gap / occupancy** | Gives a cheap stratified-random first pass with an effort tag and a known per-dart P_det. Conductive-lid blind systems with a lid under about 200 m (single dart), or under about 400-800 m for wide footprints (cluster), become detectable. Blanks become **calibrated negatives**. The SBC variance ratio on N falls because effort is designed, not opportunistic. | In carpeted basins, the 2-5x band on N narrows to about **1.5-3x**, and posterior sd of log N falls about **25-40%**. Region-wide, the effect is about 10-20% per season of carpet. Swept-aquifer systems are not helped. |
| **6 Upflow location and footprint** | Gives a 200-500 m pixel flux map. The footprint centroid lands within about 300-500 m, and the area within about ±50% for footprints of 2 km² or more. | Footprint-area uncertainty is **roughly halved** where conductive. That matters for P(MWe ≥ 20). |
| **7 Conductive background and position** | κ per dart, k to ±15%, and a valley background-flux field with sd about 50 mW/m² per dart, averaged to about 15 mW/m² per 4 km². RTK ties. | The background-flux prior narrows about **2x** inside carpeted valleys. |
| **4 Sensor reliability s/q per mask class** | The cheapest way to run the 20 known blind + 40 cold-control calibration as **areas**: 20-40 darts each, about 1,800 darts, about $150-200k. That gives s/q per mask class with real sample sizes. | VOI swings caused by s/q uncertainty (more than 2x) fall to about 1.3-1.5x for the "conductive lid" class. |
| **3 Masking / lid thickness** | Indirect. A blank carpet next to a warm ranch-well outflow points to the swept class. A weak, wide anomaly points to a thick conductive lid. | Small to moderate. It classifies the mask but does not measure lid thickness. |
| 2, 5, 8, 9 | Negligible. The darts are too shallow for permeability or deep temperature. | - |

**Sensor-shrinkable share.** This adds roughly 5-10 points to the share of variance on N that a sensor can shrink (judgement), mainly through rank 1 in the conductive class.

**EIG per dollar.** Per point, the P13 dart carries about 1/5-1/10 of the EIG of a P02 3 m dart (sensitivity is about 6x lower, but footprints are wide), at about 1/3-1/6 of the cost. **So EIG/$ is roughly equal per point. P13 wins on area-per-week and on "no vehicle off road".** Use it as a first pass. Then put P02 darts and Sentinels on the hits and short-drop areas. GHOST Tier 1 must confirm this order.

---

## 6. Rights edge

- **Legal footing.** BLM IM 2026-024 lists "drone and airborne surveys", "battery sensors placed in small holes" and near-surface installs under 10 ft as casual use, with no notice (https://www.blm.gov/policy/im-2026-024; H13). A 20 mm, 1.2 m dart fits these words. Two questions go into the H13/P03 lawyer memo: (a) does *dropping* a sensor count as casual use, and (b) can a field office treat 1,000+ darts as "significant disturbance"? FAA: 14 CFR 107.23(b) allows dropping objects if there is no undue hazard to people or property. Under 107.39, keep away from people. Use 44807 for the heavy lifter (https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-107). State trust land in UT, NM and AZ needs a right-of-entry permit (unverified). Private ranches need an access letter, which doubles as the heat-option conversation.
- **Speed and secrecy.** We file nothing. Darts are flush, 70 mm and earth-coloured. The drone is visible for minutes, not weeks. A private map of 1,500-4,000 km² a season lets us nominate or lease **only the hot 500 m parcels**, spread across decoys, before anyone else has a reading. Leftover BLM parcels at $1/ac/yr and state first-file then lock them for cents per acre.
- **Ranch hook.** The same dart is a free **3-depth soil temperature probe for the rancher** (frost and planting dates). Leave 5-10 reference darts on each ranch as the gift that opens the heat-option talk.
- **Window limit.** Each carpet takes 12 months. Installs in spring 2027 give reads in 2028. A second carpet in 2028 gives reads in 2029, against an IM that ends 30 Sep 2029. **Start the first carpet by spring 2027 or lose half the window.** A 6-month Kalman read (P02 notes this is not yet earned) would double the cycles.

---

## 7. First test (weeks 0-14, about $60-90k, unverified)

1. **Weeks 0-4, drop gate ($8-12k).** Build 30 dummy darts with only the accelerometer and tilt. On a private ranch, drop 5 per soil class (loose, medium, dense fan, caliche-margin) from 60, 90 and 120 m. Dig out a sample. **Pass if median depth is 0.8 m or more in valley fill, and at least 70% of drops are usable (0.6 m or more, tilt under 10°) across all classes.** If it fails, pivot to the v2 vibro-driver, or to P02 drive-and-drop with a drone only for logistics.
2. **Weeks 2-10, build.** Make 120 instrumented darts, calibrate them in a bath, and fit a magazine to one airframe. File the 44807 exemption and the casual-use memo.
3. **Weeks 10-14, field.** Drop 60 darts on a Granite Springs-style transect with an existing 2 m dataset (pre-registered next to well 68-02, H01/M21). Drop 40 darts on cold controls of the same landform. Put 20 darts beside logged 2 m probes. Read monthly by data-mule. The **6-month interim read** uses a Kalman inversion forced by ERA5-Land. The **12-month read** gives the pre-registered result: **r ≥ 0.8 against 2 m on transects with a range above 3 C; per-dart 3-sigma flux of 0.6 W/m² or less against the valley reference; control blank rate of 90% or more.**
4. Run the recovery time trial (v1 on foot). Bench-test the v2 winch on 10 darts.

**Kill or pivot:** median penetration under 0.6 m in valley fill; per-dart noise over 0.3 W/m² at 1 sigma in the field; recovery cost over $60 per dart; or a BLM field office ruling that drops are not casual use.

---

## 8. Risks

1. **Penetration shortfall** in dense fans and caliche, which are exactly the range-front upflow zones. The brief's 20-40 m drop does not work at all.
2. **The brief's fibreglass shaft buckles.** Stainless adds a small axial-conduction bias, and k cannot be measured in place.
3. **Surface-mean offsets** wreck the "offset" estimator. Only the gradient estimator is robust, and it is about 6x noisier than P02's 3 m dart.
4. **Recovery** is the dominant cost and the slowest step. The v2 drone winch is unproven.
5. **12-month latency** fits only about 2 cycles in the IM 2026-024 window.
6. **Regulation.** "Dropping" may be ruled outside casual use. The 44807 exemption, DJI/FCC limits and BVLOS limits apply.
7. **Losses** from cattle, floods, theft, wildfire and burrowing animals.
8. **Swept and lidded masks** stay blind. It helps rank 1 only for the conductive class.
9. **Copyable.** A drone and a spike are easy to copy. The moat is the calibrated P_det and the private map, not the hardware.

---

## Sources

- Repo: `P02-logging-heat-flux-dart-3-m-casual-use-da.md` and `P02_dart_sim.py` (forward model), `P03-e-mt-node-2-0-drone-placed-dc-coupled-te.md`, `M21-shallow-temperature.md`, `../../../hardware/evidence/H01-shallow-temp-probes.md`, `H13-permits-and-secrecy.md`, `MODEL.md`.
- New calc: `P13_dart1m_sim.py` (this folder). Run it with `python3 P13_dart1m_sim.py 0 16`.
- BLM IM 2026-024, casual use: https://www.blm.gov/policy/im-2026-024
- 14 CFR Part 107 (107.23(b), 107.39, 107.51): https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-107
- Olmsted, F.H., 1977, Use of temperature surveys at a depth of 1 meter in geothermal exploration in Nevada, USGS PP 1044-B: https://pubs.usgs.gov/publication/pp1044B (URL from memory, unverified)
- Horton, Wierenga and Nielsen, 1983, Evaluation of methods for determining the apparent thermal diffusivity of soil near the surface, SSSAJ 47:25-32 (unverified citation details)
- Young, C.W., 1997, Penetration Equations, Sandia SAND97-2426 (unverified)
- Coolbaugh et al., 2007, A method for rapid shallow temperature surveys (2 m), GRC Transactions (unverified)
- Drone prices and specs (Freefly Alta X, Hylio, DJI FlyCart 30), FCC Covered List status, 49 USC 44807 practice: from memory, unverified.
