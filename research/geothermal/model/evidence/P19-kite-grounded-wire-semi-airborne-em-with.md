# P19: Kite, grounded-wire semi-airborne EM with a drone-towed receiver (lid-and-cap mapper to 0.5-1 km)

Date: 23 Oct 2026. Build candidate P19, model track. This builds on `M08-magnetotellurics.md` (Folsom 2024: MT at more than 1 km spacing misses alteration under 2 km²; free USGS Earth MRI HELITEM reaches about 400 m), `../../evidence/L14-geophysics.md` (Folsom 2024 and the BRIDGE report, East Hawthorne), `P03-e-mt-node-2-0-drone-placed-dc-coupled-te.md` (the E-node carpet and the road-side wire), `P18-coded-source-transmitter-casing-source-r.md` (the GPS-coded SiC transmitter, 5 km of wire on reels, 20 kW generator), `../../../hardware/evidence/H13-permits-and-secrecy.md` (BLM IM 2026-024 casual use) and `../MODEL.md` (SENTINEL-COX). It does not repeat them.

**Method note.** The shared web-search budget for this workflow turn was used up before this agent started. Both searches I tried were refused, so **no new web pages were read**. Prior-art claims below come from repo files (which carry URLs) or from literature I know; those from memory are marked (from memory, unverified). Prices are my estimates (unverified). Numbers marked (sim) come from `P19_kite_sim.py` in this folder. That script uses the open-source empymod code (Werthmuller 2017, Geophysics 82(6) WB9; https://empymod.emsig.xyz) to model a real finite grounded wire over a layered earth with a receiver 40 m up. Each run takes a few seconds. Numbers marked (calc) are my own arithmetic.

---

## Bottom line

Build it, as the second EM build after P18. It shares P18's transmitter, so the extra cost is mostly two drones and two towed sensor birds.

1. **The physics works, and the signal is large.** In the 1D model, a 2 km wire at 20 A gives a background vertical field of 0.9 nT at 2 km offset and 10 Hz. A 3 ohm-m clay cap under an 80 ohm-m cold lid changes that field by **440 pT (cap top 400 m), 270 pT (700 m) and 160 pT (1,000 m)** at 2 km offset, and by 20-60% of the background (sim). A cap whose top is 1,500 m deep still changes it by 70 pT, or 9-30% (sim).
2. **The whole question is low-frequency motion noise on a swinging sensor.** The deep signal lives at **3-30 Hz**. At 100 Hz and up, the same 1,000 m cap gives only about 10-17 pT (sim). So: if the bird's noise after motion correction is about **30-50 pT at 3-10 Hz**, depth of investigation (DOI) is about **0.9-1.2 km** for a strong cap. If motion noise forces us above about 30-100 Hz, DOI falls to about **0.5-0.7 km**. That is still past the free HELITEM layer (about 400 m), but it is no longer a 1 km tool. The first test is designed to settle this one number.
3. **It is a search tool, not a proof tool.** It maps conductance and depth-to-top of a conductor in a continuous carpet at 100-200 m line spacing. That fixes the Folsom gap, where MT at 0.5-1 km spacing misses caps under 2 km². It cannot tell clay from brine (no IP), and it cannot see heat. So it must be paired with P18/P03 IP and with Sentinel or dart temperature.
4. **Cost scale is the best in the EM stack.** About **$80-150k to build** (or $60-110k on top of an existing P18 transmitter), **6-10 weeks** for 2-3 people. In the field: **about $300-700 per km²** at 100 m lines, and about $150-300 per km² at 200 m lines, about **6-12 km² per crew-day** (calc, unverified). An MT carpet that resolves the same bodies costs about $6-12k per km².
5. **Rights edge.** Drone flights and ground EM are casual use under BLM IM 2026-024 (H13). So we fly whole valleys without a filing and nominate only the 1-3 km² over the conductor, plus a buffer. That cuts nomination and auction exposure by about 3-10x per target.

Model gain (my estimates, untested): **rank 1**, deep or lidded catch rate in surveyed valleys rises from about 0.1-0.2 to about 0.4-0.6, and Kite becomes the designed second detector the model already asks for; the lidded-class N band shrinks from about 2-5x to about 1.5-2.5x where flown. **Rank 6**, footprint area error drops from about 2-3x to about ±25-40%, and upflow location narrows to about 0.5-1 km. **Rank 3**, depth to cap top (the lid base) comes out at about ±15-25%, a strong cross-check on E-MT. Small help on rank 7. No help on ranks 2, 5, 8 and 9.

Self-score: model_uncertainty_alpha 4, rights_alpha 4, buildability 3, cost_scale 4, moat 3.

---

## 1. Physics case

### 1a. What a blind system looks like to EM
Most Basin and Range blind systems sit under a **cold, fresh, resistive lid** of alluvium and lake beds, 50-300 ohm-m (M23). Inside and above the reservoir, hot water turns volcanic glass and feldspar into **smectite clay**. Smectite is very conductive (1-10 ohm-m) and forms a "cap" over the upflow. Folsom et al. (2024) and the BRIDGE team used exactly this signature at East Hawthorne: "zones of low resistivity frequently occur over geothermal systems in the Basin and Range" (L14, https://www.osti.gov/biblio/2540220; https://www.osti.gov/biblio/3683813). The cap is often 1-3 km² across. Its top can be 200 m deep or more than 700 m deep. A thick lid is exactly the mask class where 2 m probes and ranch-well profiles go blind (rank 1, rank 3).

Two other signatures matter:
- **Cap doming.** The cap is usually shallowest over the upflow and dips away along the outflow. So a map of depth-to-conductor points at the upflow (rank 6).
- **Saline outflow tongue.** Warm saline outflow is also conductive. Its long, thin shape along the head gradient is a second footprint signal.

### 1b. How grounded-wire semi-airborne EM works
A long insulated wire is laid on the ground and grounded at both ends with stake clusters. The transmitter drives a coded current, 10-40 A, at chosen frequencies from about 1 Hz to 8 kHz. The current flows down the wire and back through the earth. Two things make the field we measure:
- the **primary field**: Biot-Savart from the wire and the ground current spreading out from the electrodes. Over a uniform earth at DC, the ground current makes no vertical field at the surface, so Bz is just the wire's own field (standard result);
- the **secondary field**: eddy currents induced in conductors, and current channelled into them. A buried cap adds a large secondary field.

The receiver is a 3-component magnetometer flown above the ground. It records the field at the transmitter frequencies, synced by GPS. Dividing by the measured current gives a **transfer function**, B/I, at each point and frequency. This is the DESMEX approach (Becken et al. 2020, Geophysics 85(6), E253-E267, doi 10.1190/geo2019-0336.1, from memory, unverified).

**Why it reaches deeper than airborne EM.** In helicopter TEM (HELITEM), the source flies with the receiver. Its moment is limited by what a helicopter can carry, and the depth is about 300-500 m (M08, L14). Here the source sits on the ground. It can be kilometres long and carry tens of amps. The receiver can then sit 1-4 km away, and depth grows with offset, like in land CSEM. The skin depth, delta = 503 sqrt(rho/f), is about 1.4 km in 80 ohm-m at 10 Hz and 0.45 km at 100 Hz (calc). So low frequencies plus large offsets reach 1 km.

### 1c. Forward model results (sim)
Set-up: a 2 km wire along x, 20 A; receivers 40 m above ground, broadside to the wire, 0.5-4 km out. Background earth: an 80 ohm-m lid over 60 ohm-m rock. Target: a 3 ohm-m, 300 m thick cap with its top at 200-1,500 m. All values are 1D. They are an upper bound for a small body (section 1d).

| Cap top | Best |ΔBz| at 1 km offset | at 2 km | at 3 km | Relative change at 2-3 km |
|---|---|---|---|---|---|
| 200 m | 1,450 pT (10 Hz) | 600 pT (3 Hz) | 330 pT | 73-91% |
| 400 m | 790 pT (10 Hz) | 440 pT (3 Hz) | 270 pT | 54-76% |
| 700 m | 320 pT (10 Hz) | 270 pT (3 Hz) | 190 pT | 33-55% |
| 1,000 m | 140 pT (10 Hz) | 160 pT (3 Hz) | 130 pT | 20-37% |
| 1,500 m | 50 pT (3 Hz) | 73 pT (3 Hz) | 71 pT | 9-20% |

- **Weak cap** (10 ohm-m, 150 m thick): 220 pT at 400 m depth, 120 pT at 700 m, 66 pT at 1,000 m, all at 2 km offset (sim).
- **Conductive playa lid** (10 ohm-m, 150 m thick, on top) with a cap at 700 m: the anomaly barely drops, 240 pT at 2 km (sim). Unlike DC methods, an inductive source is not shielded much by a thin conductive top layer at 3-10 Hz.
- **Horizontal components**: Bx anomalies are about 5-10x smaller than Bz (sim). Bz carries the depth signal. Bx and By help with lateral edges and with the 3D inversion.
- **The frequency trap.** For a cap at 1,000 m, the anomaly is 160 pT at 3-10 Hz but only about 9-17 pT at 100 Hz and under 1 pT at 300 Hz (sim). Deep sensing needs the 3-30 Hz band.

### 1d. Noise and detection limits
- **Sensor self-noise.** A good 3C fluxgate (Bartington Mag-03 class) has about 6-10 pT/√Hz at 1 Hz (from memory, unverified). A 3C induction coil is far quieter above about 10 Hz, below 0.1 pT/√Hz (from memory, unverified). With 10-30 s of stacking per point, self-noise is about 1-3 pT. That is not the limit.
- **Motion noise is the limit.** The sensor hangs in Earth's 50,000 nT field. A tilt of 1 microradian changes a component by about 50 pT (calc). The towed bird swings like a pendulum at about 0.2-1 Hz, with harmonics and rotor buffeting above that. DESMEX-style processing removes this with an onboard IMU, rotation into a fixed frame, and robust regression only at the transmitter frequencies (from memory, unverified). My planning numbers: after correction, about **20-50 pT at 3-10 Hz** and about **2-5 pT above 30 Hz** (unverified, the key test number).
- **Cultural noise.** 60 Hz power lines and their odd harmonics. We pick transmitter frequencies that sit between them, use pseudo-random codes, and stay about 1 km from big lines. Valleys with ranch power only are fine.
- **3D discount.** A 1-1.7 km wide cap gives a smaller anomaly than an infinite 1D layer. For a cap top at 700 m, I assume about 40-70% of the 1D value (unverified, to check with a 3D code such as custEM or SimPEG).
- **Resulting DOI (calc, using the table, the 3D discount and 30-50 pT noise):**
  - Cap top at 200-500 m: SNR 5-30 per point. A clear detection and a good outline.
  - Cap top at 700 m: SNR about 2-6 per point. Clear once 20-50 points are averaged over the body.
  - Cap top at 1,000 m: SNR about 1-3 per point. A detection from the coherent map, with depth to about ±25%.
  - Cap top at 1,500 m: detected only with low motion noise and long offsets. Not a v1 promise.
- **What it resolves.** In 1D, the method resolves conductance (thickness/resistivity) and depth to top much better than thickness alone. That is fine for us: depth to cap top approximates lid thickness, and conductance separates a real cap from a thin wet clay seam.

### 1e. What it cannot do
- **Clay vs brine vs fossil cap.** Inductive EM measures conductivity only. Saline basin water and lake clay look the same. This is the rank 4 trap. The fix is the IP from P18/P03 at the nominated block, and temperature from Sentinel visits, darts or a TG hole.
- **Heat itself.** A cap can be fossil. The model must treat a Kite conductor as a likelihood term on "hydrothermal alteration present" and must keep a fossil-cap class.
- **Caps that are not there.** Some low-temperature amagmatic systems have weak or no smectite cap. I assume 50-70% of blind targets above 130 °C have a cap mappable this way (unverified). The rest still need heat sensors.

---

## 2. Prior art (from memory, unverified unless a repo file is cited)

- **DESMEX (Germany, BGR and the University of Münster, 2016-2022).** Helicopter-towed 3C induction coils over 1-2 km grounded wires, 10-5,000 Hz, used for mineral exploration in the Harz and Thuringia. Reported depth near 1 km. Becken et al. 2020, Geophysics 85(6) E253; Smirnova et al. 2019, GJI; Steuer et al. 2020, J. Appl. Geophys. (from memory, unverified).
- **Drone versions.** The DESMEX group and Chinese groups (the Institute of Geology and Geophysics CAS, and Jilin University's ground-airborne frequency-domain EM, "GAFEM" and "UAV-SATEM") have flown grounded-wire systems with multirotor drones since about 2018-2022 (from memory, unverified). Mostly for mining, coal-mine water and hydrogeology.
- **GREATEM (Japan).** Grounded-source airborne TEM, flown by helicopter over volcanoes (Mt Bandai) and coasts. Mogi et al. 2009, Exploration Geophysics 40:1-7 (from memory, unverified). It is the closest prior use near geothermal systems.
- **US geothermal use.** I know of no published semi-airborne survey over a US blind geothermal system (unverified). US geothermal EM practice is MT plus HTEM. BRIDGE flew 1,877 line-km of HTEM (L14), and USGS Earth MRI flew 11,079 line-km of HELITEM, released free in Sep 2025 (DOI 10.5066/P1UKDJSM, M08).
- **Zanskar.** It uses public data, ML, seismology and its own wells (M13, M32). No sign of semi-airborne EM (unverified).

So the method is published and not secret. The edge is the cheap drone version, our own US geothermal application, the calibration library over known systems, and pairing it with rights.

---

## 3. Concrete v1 design

### 3a. System overview
- **Source:** the P18 trailer transmitter (2-20 kW SiC H-bridge, GPS-disciplined code generator, 20 kW diesel generator). Kite adds a 2-4 km wire layout and a current-sense channel.
- **Receivers:** two drones, each towing a "bird" with a 3C fluxgate, an IMU and RTK GPS, on a 15-25 m line below the drone.
- **Base station:** a ground 3C fluxgate 1-3 km from the wire for the natural-field reference, plus the current logger at the transmitter.
- **Processing:** transfer functions B/I per point and frequency, then a 1D inversion per point (empymod-based), then 3D on nominated blocks (custEM or SimPEG, free).

### 3b. Parts list (v1, prices unverified)

| Item | Spec | Qty | Cost |
|---|---|---|---|
| Transmitter | Reuse P18; standalone version = own SiC H-bridge 20 kW + GPSDO | 1 | $0 (or $10-15k) |
| Generator | 20 kW diesel, trailer-mounted (from P18) | 1 | $0 (or $10-15k) |
| Wire | 4 km of 10 AWG (about 3.3 ohm/km) insulated, on 2 powered reels | 4 km | $4-7k (part from P18) |
| Electrodes | 2 clusters of 10-20 steel stakes, foil pits, salt water, 30 m bus | 2 | $1-2k |
| Current monitor | Hall sensor + 24-bit logger, GPS-timed | 1 | $1-2k |
| Drones | Heavy-lift multirotor with MTOW under 55 lb (24.9 kg), 6-9 kg payload, 25-35 min endurance (for example Inspired Flight IF1200A or Freefly class) | 2 | $50-70k |
| Batteries | 6 flight sets per drone, plus a generator-run field charger | 12 sets | $12-18k |
| Bird housing | 1.0-1.2 m fibreglass body with tail fins, non-magnetic, 3-4 kg all-in, Kevlar 20 m tow line, quick release | 2 | $3-5k |
| Magnetometer | 3C fluxgate, DC-3 kHz, under 10 pT/√Hz at 1 Hz (Bartington Mag-03 class) | 2 (+1 base) | $25-40k |
| Optional coil | 3C air-core or mu-metal induction coil for 30 Hz-8 kHz (own wound) | 2 | $4-8k |
| IMU + GNSS | Tactical MEMS IMU with RTK GNSS in the bird | 2 | $6-14k |
| Logger | 24-bit, 6-8 channel, 8 kSa/s, GPS PPS, SD card, small LoRa telemetry for health | 3 | $3-6k |
| Ground station | Rugged laptop, LTE/Starlink, RTK base | 1 | $3-5k |
| Spares, tools, cases | | | $5-10k |
| **Total** | | | **$80-150k standalone; $60-110k on top of P18** |

### 3c. Dimensions, power, comms
- **Wire layout.** 2 km standard, 4 km for deep targets, laid along the shoulder of an existing road or ranch track from the powered reel at walking pace. Ends grounded at stake clusters at about 10-40 ohm.
- **Power.** 20 A into about 30 ohm of grounding plus 13 ohm of 4 km wire is about 860 V and 17 kW (calc). For 2 km and 20 A it is about 700 V and 14 kW. The P18 20 kW generator covers it. Burn is about 4-6 L of diesel per hour.
- **Waveform.** A square-wave or pseudo-random code with energy at 3, 7, 11, 31, 73, 211, 617, 1,777 and 5,113 Hz (all chosen to avoid 60 Hz harmonics). 10-30 s per stack.
- **Flight.** Drone at 45-60 m above ground, bird at about 30-40 m. Speed 5-7 m/s. Lines perpendicular to the wire, 100 m apart for nomination blocks and 200-400 m for reconnaissance.
- **Data rate.** 8 kSa/s x 6 channels x 24 bit is about 150 kB/s, so about 0.5 GB per flight onto SD. Telemetry carries only health and position. Data are processed each evening.
- **Timing.** Transmitter and bird both on GPS PPS. Transfer functions use the measured current.

### 3d. Deployment and crew time per site
Crew of 3: two remote pilots (Part 107) and one transmitter and wire tech. Truck plus the P18 trailer.
- Lay the wire and electrodes: 1.5-2.5 h for 2 km.
- Flights: one battery set is about 25-30 min and about 9-12 line-km. At 100 m lines, 1 km² is 10 line-km, so about 1 km² per flight. Each drone does 5-7 flights a day with hot-swapped batteries. Two drones give **about 8-12 km² a day at 100 m lines** or about 15-25 km² at 200 m lines (calc).
- Per wire setup: good coverage from about 0.5 to 3.5 km on each side of a 2 km wire, about 10-14 km² usable. So one setup a day, or two in a good day.
- Pull the wire: 1 h.
- **Cost per km²:** a crew-day of about $3.5-5k (3 people, truck, diesel, battery and drone wear), plus about $50-100/km² for processing. That is **about $350-700/km² at 100 m lines and $150-350/km² at 200 m lines** (calc, unverified).
- **FAA limits.** Part 107 needs visual line of sight. We fly from 2-3 launch points per setup, with a visual observer, and keep the drone within about 1-1.5 km. Beyond-line-of-sight rules (the proposed Part 108) would roughly double daily coverage when final (status unverified).

### 3e. Survey design in the model
1. **Reconnaissance carpet (200-400 m lines).** Fly whole high-lambda, low-P_det valleys, chosen by the VOI-Bank EVSI ranking. About 25-60 km² per crew-day.
2. **Nomination block (100 m lines).** Fly 5-15 km² around each conductor. Output: depth-to-top map, conductance map and a footprint polygon.
3. **Handoff.** P18 IP over the 1-3 km² core, then darts or a Sentinel visit for temperature, then rights.

---

## 4. How much it shrinks the model's uncertainties (estimates, untested)

| Rank | Today | With Kite in flown valleys | Why |
|---|---|---|---|
| 1 Detection gap, deep or lidded catch (2-5x on N) | Lidded class P_det about 0.1-0.2 (2 m probes and Sentinels go blind under lids over about 100-200 m; HELITEM stops near 400 m) | About 0.4-0.6, which is about 0.6-0.85 sensitivity on caps with top under about 800 m, times the 50-70% of targets that have a cap | Kite gives an independent second detector for the designed two-detector survey. It is a different physics from temperature, so the shared-mask class becomes estimable. The N band for the lidded class shrinks from about 2-5x to about 1.5-2.5x where flown |
| 6 Upflow location and footprint | Footprint area about 2-3x; ranch wells sample outflow | Area about ±25-40%; upflow to about 0.5-1 km from cap doming | Continuous 100 m line coverage resolves 1-3 km² bodies that 0.5-1 km MT misses (Folsom 2024) |
| 3 Lid thickness and masking | E-MT for lids over 200 m, static-shift bias ±20-40% (P18) | Depth to cap top ±15-25% | B-field data are free of galvanic static shift. Kite plus P18 loop TEM pins the E-MT carpet |
| 7 Conductive background | Mostly priors | Measured lid and basement resistivity on the carpet | Direct |
| 4 Sensor reliability per mask class | | Small: needs calibration over 20 known blind systems and 40 cold controls | Kite joins that campaign as one more detector |
| 2, 5, 8, 9 | | No change | No heat or permeability signal |

**In model terms.** Kite enters THERMOS-B and CREAM-COX as a new detector channel: a censored likelihood on "conductor present with depth-to-top d and conductance S" per 500 m parcel, with its own s/q per mask class learned in the calibration campaign. In GHOST Tier 1, it is a new sensor to rank. My guess is that it ranks above E-MT per dollar for detection when lids are 200-800 m, and below E-MT for depths over 1.2 km.

**Regional total.** If the lidded and deep share of undiscovered MWe is about 30-50% of the total (unverified), and Kite halves its band in the flown basins, the F5/F95 ratio for those basins could fall from about 11.6x toward about 6-8x. Combined with Sentinels on the unlidded share, the <4x buyer target looks reachable in flown basins (untested).

---

## 5. Rights edge

- **No filing to search.** Drone surveys and ground EM are casual use on BLM land under IM 2026-024 (H13, https://www.blm.gov/policy/im-2026-024). A wire on a road shoulder for one day fits "ground geophysics (EM)". We can carpet a whole valley and tell no one.
- **Small, sharp nominations.** We nominate only 1-3 km² (about 250-750 ac, plus a buffer, so one or two 640 ac parcels) instead of 10-30 km² of fault-zone guesswork. That means fewer parcels to win at auction, a lower signal to watchers, and spare cash for decoy parcels.
- **Private ranch heat.** The same footprint polygon tells us which ranch section to lock at $1-2/ac. The drone can fly across a ranch with a simple overflight letter, and the rancher conversation happens with a map in hand.
- **Better buyer package.** A footprint plus depth-to-cap map is what Ormat or Fervo would pay for at the farm-out step. It raises the carry or the $/MWh override we can ask (unverified).
- **Risks to the edge.** A field office can pull activities out of casual use where it expects significant disturbance, such as sage-grouse areas or wilderness study areas (H13). Wire on a county road may need a county encroachment note (unverified).

---

## 6. Risks

1. **Motion noise at 3-10 Hz.** If the corrected bird noise is above about 100 pT at 3-10 Hz, DOI drops to about 0.5-0.7 km. Mitigation: a longer tow line, a damped bird, a better IMU, more stacking (slower flight), or **hover-and-stare points** (land the bird or hold a hover for 60 s) for the deepest soundings.
2. **Non-uniqueness.** Clay vs brine vs lake clay vs fossil caps (rank 4). Kite must be paired with IP and temperature before any big rights spend.
3. **3D effects and equivalence.** 1D inversion of a small 3D body can misplace depth. Use 3D inversion on nomination blocks.
4. **FAA and weight.** It stays under 55 lb MTOW and in line of sight. That limits payload, endurance and daily coverage.
5. **Cultural noise.** Power lines, pipelines and fences channel current. Use frequency choice and stay away from big lines.
6. **Ground and cattle.** A surface wire on a ranch road can be cut or chewed by cattle. Check continuity live from the current monitor.
7. **Low moat.** The method is published. The moat is the calibration library over known systems, the speed, and the rights loop, not the hardware.
8. **Not every system has a cap.** Kite misses capless systems. That is acceptable, because the model treats each detector by mask class.

---

## 7. First test

**Week 0-1, bench and hover (about $2-5k after parts).** Fly the bird with the transmitter off over quiet ground. Measure the corrected noise spectrum, 1-1,000 Hz. Pass: below 50 pT at 3-10 Hz and below 5 pT at 30-300 Hz, after 20 s stacks.

**Weeks 2-4, a known-answer site (about $15-25k).** Fly East Hawthorne, NV, where BRIDGE flew HTEM and ran 61 MT stations (Folsom 2024, https://www.osti.gov/biblio/3683813). If land access fails, use another BRIDGE or Earth MRI HELITEM block over a known blind system. Lay a 2 km wire on an existing road. Fly about 30 km² at 100-200 m lines.
- Pass 1: the Kite conductor map in the top 400 m matches the public HTEM model (correlation of log-resistivity at least 0.7).
- Pass 2: below 400 m, the Kite depth-to-cap-top and conductance agree with the 3D MT model within 25%.
- Pass 3: Kite outlines the cap area within ±40% of the MT/HTEM outline.
- Pass 4: field rate of at least 8 km² per crew-day at 100 m lines.
- Kill or shrink: if noise forces the usable band above 100 Hz and Pass 2 fails, Kite becomes a 0.5-0.7 km tool. Keep it only for nomination blocks under thin lids, not for deep search.

**Months 2-4.** Join the 20/40 calibration campaign (rank 4): fly 10 known blind systems and 10 cold controls, to learn s/q per mask class.

---

## 8. Self-scores (1-5)

- **model_uncertainty_alpha: 4.** It hits rank 1 (deep and lidded catch, as an independent second detector), rank 6 (footprint) and rank 3 (lid depth) at the same time. It does not touch heat or permeability.
- **rights_alpha: 4.** No-filing search of whole valleys plus 1-3 km² nominations is a strong fit for the rights-bank model.
- **buildability: 3.** It is 6-10 weeks for 2-3 people on top of P18. The motion-noise processing is the hard part and may need months of tuning.
- **cost_scale: 4.** About $150-700 per km² beats MT by about 10x and contract HTEM on small blocks. Weaker than desk data or 2 m probes on cost per km².
- **moat: 3.** The method is published. The moat is the calibration library, the fleet speed and the pairing with rights.
