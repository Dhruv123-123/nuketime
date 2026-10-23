# P20: Plume Rover, a towed TEM sled on roads and two-tracks for shallow outflow plumes

Date: 23 Oct 2026. Build candidate P20, model track. This builds on `M23-hydrology-masking.md` (lateral outflow is one of four masks; plumes carry a signal 3-30 km; sample where the water goes, then walk up-gradient), `M08-magnetotellurics.md` (Earth MRI HELITEM, 11,079 line-km, ~400 m depth, DOI 10.5066/P1UKDJSM; the conductor non-uniqueness problem), `../../evidence/L14-geophysics.md` (BRIDGE: helicopter TEM 1,877 line-km in 12 days at ~2 km spacing; Folsom et al. 2024 HTEM vs MT at East Hawthorne), `P01` (Ranch Well Sentinel), `P03` (E-MT carpet), `P04` (wellhead clamps), `P18` (coded transmitter; its casing/stake plume-bearing work), `../../../hardware/MEMO.md` and `H13` (BLM IM 2026-024 casual use), and `../MODEL.md` (SENTINEL-COX ranks). It does not repeat them.

**Method note.** The shared web-search budget for this workflow turn was used up before this agent started. Both searches I tried were refused, so **no new web pages were read**. Prior-art facts below come from repo files (cited by file) or from my own knowledge of the literature, marked (from memory, unverified). Prices are my estimates (unverified). Numbers marked (sim) come from two scripts I wrote and ran for this file:
- `P20_ttem_sim.py`: a 1D layered-earth TEM forward model for a tTEM-like offset-loop geometry, with a linearised resolution analysis. It runs in about 3 s. Its homogeneous half-space check is within 8% of the analytic late-time formula.
- `P20_backproject_mc.py`: a Monte Carlo of how well a mapped conductive tongue can be traced back to its upflow apex.

---

## Bottom line

**Build it, but as two products in one: a road-mode screen on public land and a field-mode mapper on optioned ranches.** It is the cheapest way to turn "this ranch well is warm" (Sentinel) into "the upflow is about here, on that parcel" (a lockable target). That is the step where the bank makes its money.

1. **Physics works for the target class.** A warm chloride outflow tongue in Basin and Range alluvium is 10-30x more conductive than the fresh, cold alluvium above it (calc below). My 1D sim says a tTEM-like sled sees a strong tongue (4 ohm-m, 15 m thick) with a large margin to **about 80 m** depth, and a weak one (8 ohm-m, 10 m) to **about 50-60 m** (sim). Above about 40 m it pins tongue top to within about 1 m and conductance to about 10-30% (sim, linearised, 1D, optimistic). This matches the published tTEM depth of about 70 m (Auken et al. 2019, from memory, unverified).
2. **The main trap is playa.** A surface clay or brine layer 10-20 m thick, at about 3 ohm-m, cuts the signal from a tongue below it by 3-10x (sim). So the rover is a tool for alluvial fans, bajadas, valley-margin ranch land and terraces, not for playa floors. Playa floors belong to MT (P03) and wells (P01).
3. **Heat vs salt is not solved by TEM alone.** Going from 15 C to 60 C roughly halves water resistivity. The same drop comes from doubling the salt. The rover needs ties: every Sentinel and clamp well inside the survey gives fluid EC and T, so we can tell "warm and moderately salty" (geothermal) from "cold and very salty" (evaporite brine). This is in the design, not an add-on.
4. **The prize is rank 6.** My back-projection Monte Carlo says a road-mode survey (transects about 0.8-1.5 km apart) shrinks the 1-sigma upflow search area from a **~55 km² "ranch-well bearing" sector** to about **0.4-1.4 km²** (sim). After I inflate this 3x in distance for real-world tongue bends, splits and 3D effects, the honest gain is about **5-15x smaller search area** for systems that have a drivable tongue within about 80 m. Field mode (150 m lines on an optioned ranch) is about 2-3x better again.
5. **Rights edge is the strongest part.** The tongue usually points up-gradient to a **different owner's parcel**: the range-front BLM section, the neighbour's ranch, or the private half of a railroad checkerboard. Driving existing roads with a sled is ordinary vehicle use plus ground geophysics, which IM 2026-024 treats as casual use (H13; one open question below). Nothing is filed. We option the upflow parcel before anyone else knows it exists.

v1: a **commercial-grade tTEM clone** (2 x 4 m single-turn transmitter loop at 30 A, a 0.5 x 0.5 m receiver coil 9 m behind it, ~2-3 microsecond turn-off, 5 microsecond to 1 ms gates) on a non-metallic sled train, towed 8-10 m behind a UTV with RTK autosteer and a safety driver. Build cost about **$95-160k** for one rover (unverified) in **16-24 weeks** by 2-3 people, or about **4-6 weeks and ~$200-300k** if we buy a commercial tTEM system and only build the tow, autopilot and data stack. Running cost about **$40-60 per line-km** (calc). A 25-50 km² valley-floor block in road mode is **1.5-3 crew-days and about $4-9k**.

Self-score: model_uncertainty_alpha 3, rights_alpha 4, buildability 3, cost_scale 4, moat 3.

---

## 1. Physics case

### 1a. Why outflow tongues are conductive (calc, standard rock physics)
Bulk resistivity of clean, water-filled alluvium follows Archie's law: rho_bulk ≈ F x rho_w, with formation factor F about 5-10 for sands and gravels (textbook, unverified range). Water resistivity falls with temperature roughly as rho_w(T) = rho_w(25 C) x (25 + 21.5)/(T + 21.5) (the Arps rule, textbook).

| Water | TDS (mg/L) | T (C) | rho_w (ohm-m) | rho_bulk at F=8 (ohm-m) |
|---|---|---|---|---|
| Cold fresh valley aquifer | 300 | 15 | ~20 | ~150 (in practice 40-200 with silt) |
| Mixed, cooled outflow | 1,500 | 40 | ~2.8 | ~22 |
| Warm chloride outflow | 3,000-5,000 | 60-90 | ~0.5-0.9 | ~4-7 |
| Playa / evaporite brine | 30,000+ | 15 | ~0.25 | ~2 (plus clay) |

(calc; rho_w at 25 C from the usual ~6,000/TDS-in-mg/L rule of thumb, unverified.)

So the warm tongue is **10-30x more conductive** than the fresh, cold host. Great Basin geothermal fluids are typically 1,000-5,000 mg/L TDS, chloride-sodium type (from memory, unverified). The plume also often brings smectite alteration where it has run for a long time, which makes it even more conductive (and chargeable; P18).

### 1b. Why a towed TEM and not helicopter TEM or MT
- **Depth window.** A small offset-loop TEM sees about 3-80 m. That is exactly where outflow tongues live. M18 found nearly every historic blind find hit 100 C shallower than about 300 m, and many were tongues that reached shallow wells. A tongue at 20-80 m is the most common "blind but leaky" geometry.
- **Near-surface resolution.** HELITEM flies 30-40 m above ground with a large moment, so its first good gates start later and the top 10-20 m is smeared (from memory, unverified). A ground sled starts at about 5 microseconds and sees the top few metres. That matters because a thin fresh lid vs a playa crust is exactly the difference between "tongue" and "salt".
- **Density.** BRIDGE flew about 2 km line spacing, and 1 km over East Hawthorne (L14). Earth MRI flew regional lines at similar or wider spacing (M08, unverified spacing). A tongue is often 0.5-2 km wide. One AEM line crosses it once. The rover crosses it every few hundred metres.
- **Cost and coverage.** Earth MRI AEM is free where it exists, but it covers only parts of western NV, eastern CA, McDermitt and Railroad Valley (M08). Most of UT, ID, OR, NM, AZ and the rest of NV have no public AEM. There, a helicopter survey costs a mobilisation of tens of thousands of dollars plus about $150-250 per line-km (unverified). The rover costs about $40-60 per line-km with no mobilisation.
- **MT (P03) is the wrong tool for the top 80 m** (static shift, dead band, wide spacing). TEM is the right tool for that depth and also fixes MT static shift where they overlap (P18).

### 1c. Sim results (sim, `P20_ttem_sim.py`)
Geometry: transmitter moment 240 A·m² (30 A x 8 m²), receiver 9 m offset, both 0.4 m above ground, 24 gates from 5 microseconds to 1 ms. Noise: 3% plus a floor of 2 x 10^-9 V/m² at 100 microseconds that falls with time^0.5 (my assumption, tuned so that a 30 ohm-m half-space gives a depth of investigation of about 70-80 m, which is tTEM-like).

**Detectability ("chi-distance" = misfit between tongue and no-tongue model in noise units over 24 gates; about 7-8 or more is a clear detection):**

| Tongue top | 4 ohm-m, 15 m thick, in 40 ohm-m host | 8 ohm-m, 10 m thick |
|---|---|---|
| 10 m | 608 | 229 |
| 30 m | 110 | 49 |
| 45-50 m | 42 | 15 |
| 60-70 m | 19 | 5.6 |
| 80 m | 8.3 | (below) |
| 100 m | 4.2 | 2.5 at 90 m |
| 130 m | 1.8 | |

So the reach is **about 80 m for a strong tongue and 50-60 m for a weak one.** Deeper tongues need a bigger loop (v2 high-moment mode) or MT.

**Resolution (linearised posterior SD, 1D, priors: log-rho SD 1, top SD 50 m, thickness SD 30 m):**

| Tongue top | SD of top | SD of thickness | SD of ln(rho tongue) |
|---|---|---|---|
| 10 m | 0.3 m | 1.3 m | 0.04 |
| 25 m | 0.3 m | 1.7 m | 0.06 |
| 40 m | 0.9 m | 3.7 m | 0.15 |
| 60 m | 3.1 m | 9.4 m | 0.45 |
| 80 m | 6.2 m | 15 m | 0.76 |

These are optimistic (1D, perfect noise model, no 3D or lateral effects). In practice I would expect 2-3x larger. Above about 40 m, the tongue conductance (thickness/resistivity) is the robust number. That conductance is what feeds the model, because conductance x a fluid-resistivity tie gives a thickness of warm water.

**Playa screening (sim).** A 3 ohm-m surface layer over a tongue at 40 m: chi-distance falls from about 42 (no playa) to 35 (5 m playa), 17 (10 m) and 8 (20 m). So a thick playa nearly hides the tongue. Rule: **mark playa cells as "rover-blind" in the detection model**, do not treat them as negatives.

### 1d. Telling plume from playa salt (the EC/T tie)
Three tests, in order of strength:
1. **Fluid ties.** Every Sentinel (P01) and clamp well (P04) inside the block gives fluid EC, T and often Cl. From EC and T we get rho_w in place. The rover gives rho_bulk. Their ratio is the formation factor. If the ratio is in the normal 5-10 range and T is high, the conductor is warm water. If T is cold and EC is very high, it is brine. If rho_bulk is far below F x rho_w, there is clay (playa or alteration), which the P18 IP mode then splits.
2. **Geometry.** Playa salt is flat, surface-connected and bounded by the playa edge mapped on Sentinel-2 or Landsat. An outflow tongue is a lens below a resistive fresh lid, with a top that changes depth along its axis, a width that narrows toward one end, and an axis that follows the head gradient and crosses topography.
3. **Gradient.** Conductance should rise toward the source (hotter and saltier water near the upflow) while a playa brine peaks at the topographic low. The two gradients point in opposite directions in most valleys.

Honest note on the brief: it says the tongue "narrows and dives up-gradient toward the upflow fault". **Narrowing toward the source is the reliable cue.** The depth trend can go either way: in some systems the upflow rises along the fault and the tongue is shallowest near it; in others a cold-water lid thickens toward the range front. So the back-projection uses width taper and conductance gradient first, and depth trend only as a weak extra.

### 1e. Noise sources
- **Vehicle noise.** An electric UTV drive inverter switches at about 8-20 kHz. TEM gates of 5 microseconds to 1 ms fall in roughly the 1-200 kHz band. This is a real conflict (unverified level). Fixes: tow 8-10 m behind, ferrite and shielding on the drive cables, synchronous stacking, and a "coast mode" that cuts motor drive during measurement windows if needed. Fallback: a gas UTV, as the original tTEM used an ATV (from memory, unverified).
- **Cultural.** Fences, pipelines, power lines and steel well casings make coupling noise. The processing chain flags and drops soundings within about 20-50 m of known metal (standard tTEM practice, from memory, unverified). Ranch roads run along fences, so expect to lose 10-30% of soundings on some roads (unverified).
- **Sled motion.** Tilt and height changes are logged with an IMU and corrected in the inversion.
- **Natural (sferics).** Small for these early gates. Stacking handles it.

---

## 2. Prior art

- **tTEM (Aarhus University, HydroGeophysics Group).** Auken et al. 2019, *Geophysics* 84(1) E13-E22, "tTEM: a towed transient electromagnetic system for detailed 3D imaging of the top 70 m of the subsurface" (from memory, unverified details). Towed by an ATV at about 10-20 km/h; 2 x 4 m transmitter, offset receiver; depth about 70 m; made for groundwater mapping in Denmark. Sold and serviced by TEMcompany (Aarhus spin-off) (from memory, unverified). Price about EUR 150-250k (unverified).
- **tTEM in the US.** Stanford's Knight group and others ran tTEM in the California Central Valley for aquifer and recharge mapping (from memory, unverified). This shows the system works on US dirt roads and fields.
- **Related ground and water-borne systems.** FloaTEM (towed by boat on lakes and rivers), sTEM/walkTEM (static), and Geonics PROTEM and Zonge NanoTEM static ground TEM (from memory, unverified). Static TEM was the classic tool for shallow geothermal resistivity in the 1980s-90s (unverified).
- **Geothermal TEM.** Iceland (ISOR) uses central-loop TEM routinely for geothermal resistivity mapping, mostly static (from memory, unverified). BRIDGE used helicopter TEM over hidden systems in Nevada and found it the better *search* tool, while MT was better for targeting (Folsom et al. 2024, https://www.osti.gov/biblio/3683813, via L14).
- **Outflow plume conceptual models.** Lateral outflow with temperature reversals is the norm at Long Valley (Sorey et al. 1991) and Lassen (Sorey and Ingebritsen 1984, https://pubs.usgs.gov/publication/wri844278), via M23.
- **Gap we fill.** I know of no group running a towed ground TEM systematically along roads to map geothermal outflow tongues back to upflow, and none that pairs it with fluid ties and private land options (inference, unverified). Zanskar's public methods are ML plus seismology plus its own wells (Z files, M13); no towed EM is reported.

---

## 3. v1 design

### 3a. Layout
- **Sled train, about 14 m long, all non-metallic below the electronics.** Front sled carries the 2 x 4 m transmitter loop on a fibreglass and HDPE frame (loop wire 10-16 mm² copper, one turn). A rear sled 9 m behind the loop centre carries the 0.5 x 0.5 m receiver coil (multi-turn, with a low-noise preamp, bandwidth above 500 kHz) in a foam-damped box. Wide HDPE skids, about 0.4 m ground clearance for the loop. A wheeled version (fibreglass rims, no steel) for washboard two-tracks.
- **Tow:** 8-10 m Kevlar or nylon tow line and a non-metallic drawbar from the UTV hitch.
- **UTV:** electric UTV (about $25-35k, unverified) for quiet ranch work, with a gas UTV as fallback if the inverter noise test fails.
- **Speed:** 8-15 km/h on two-tracks, 15-20 km/h on graded roads. One sounding about every 10-20 m after stacking (tTEM-like, unverified).

### 3b. Electronics
- **Transmitter:** 48 V supply, SiC or MOSFET H-bridge, two moments: low (about 3 A, very fast turn-off, for the first 5-20 microseconds) and high (30 A, for late gates). Turn-off target about 2-3 microseconds with an active clamp and damping. GPS-disciplined timing, reusing the P18 code generator firmware.
- **Receiver digitiser:** 2-10 MS/s ADC with FPGA gate integration and stacking. A Red Pitaya-class board (14-bit, 125 MS/s, about $500-700, unverified) is fine for the prototype. The production board is a custom 18-24 bit front end.
- **Navigation:** two u-blox ZED-F9P RTK receivers for position and heading (about $250 each, unverified), an IMU for tilt, and a base station or NTRIP over cellular.
- **Autopilot:** an AgOpenGPS-style autosteer kit (open-source software, a steering-wheel motor, about $1.5-3k, unverified) plus cruise control. v1 always has a safety driver, who also watches for cattle and gates. v2 runs unattended on closed private ranch roads inside a geofence.
- **Compute and comms:** rugged mini-PC running real-time 1D inversion (laterally constrained, like Aarhus Workbench or SimPEG); LTE plus Starlink Mini for live upload; LoRa link to the base. Every sounding goes into the THERMOS-B / GHOST data store the same day.
- **Power:** transmitter average about 300-600 W at low duty, receiver and compute about 60-100 W. A dedicated 48 V LiFePO4 pack of about 5-7 kWh (isolated from the vehicle pack to keep noise off) runs a 10-hour day. Recharge overnight from the truck or a camp generator.

### 3c. Parts list and cost (v1, one rover, unverified estimates)

| Item | Cost |
|---|---|
| Electric UTV (or used gas UTV $12-18k) | $25-35k |
| Sled train: fibreglass/HDPE frames, skids, wheel option, tow gear | $6-12k |
| Transmitter (H-bridge, clamp, loop, 48 V pack 6 kWh, charger) | $8-15k |
| Receiver coil, preamp, digitiser, FPGA board | $5-12k |
| RTK x2 + base + IMU + autosteer kit | $4-8k |
| Mini-PC, LTE router, Starlink Mini, rugged cases | $3-5k |
| Engineering (EE contractor + firmware, 16-24 weeks) | $35-55k |
| Calibration: test-site day on a known layered site, plus static TEM rental to cross-check | $5-10k |
| Contingency (20%) | $15-25k |
| **Total, own-built** | **$95-160k** |
| Alternative: buy commercial tTEM and build only tow, autopilot, ties and data stack | **$200-300k** |

The brief's $50-250k range holds. The own-built path is cheaper but carries most of the build risk in the transmitter turn-off and receiver noise.

### 3d. Two operating modes
- **Road mode (public and county land).** Stay on existing roads and designated routes. Line spacing is set by the road network, about 0.5-2 km in Nevada valleys (unverified). Use it as the screen: find tongues near warm ranch wells, AEM conductors and LGCP high-lambda cells, and get a first bearing.
- **Field mode (optioned private ranch).** With the rancher's permission, drive pasture, fallow fields and ranch tracks at 100-200 m lines. This is the mapper that pins the apex and the tongue edges. It runs on the same visit as the Sentinel log and the option signing, or on a return visit.

### 3e. Crew time per site (calc)
- 2 people (driver and geophysicist/landman). Setup and calibration: 1 hour per day.
- Road mode block of 25-50 km²: 60-120 line-km (assumes 2-3 km of usable road per km²; unverified). At 40-60 line-km a day after fences, gates and turns: **1.5-3 days**.
- Field mode on a 10 km² ranch at 150 m lines: about 67 line-km, **about 1.5 days**.
- Plus 0.5 day per site to log 2-4 tie wells with the Sentinel kit if they are not already logged.
- Processing: same-day 1D inversion; 3D tongue fit and back-projection the next morning (automated).

### 3f. Unit cost (calc)
- Capex $130k over 3 years x 150 field days x 50 km = 22,500 line-km, about **$6 per line-km**.
- Crew $1,000/day, vehicle and fuel/charge $150/day, per diem $300/day, processing $200/day: about $1,650/day, or **about $33 per line-km** at 50 km/day.
- **Total about $40-60 per line-km.** Per site in road mode, **about $4-9k**. Commercial tTEM survey service is about $150-400 per line-km (unverified), and helicopter TEM about $150-250 per line-km plus mobilisation (unverified).
- At 120 field days a year, one rover covers about 40-80 sites a year.

---

## 4. How much it shrinks the model's uncertainties

### Rank 6, upflow location and footprint (main gain)
Monte Carlo (`P20_backproject_mc.py`): the apex is found by fitting the tongue's width taper and axis from crossings, then extrapolating to an assumed apex width of 0.4 km.

| Survey | SD along axis | SD across | 1-sigma search ellipse |
|---|---|---|---|
| Baseline: ranch wells only (bearing ±50°, range 1-8 km) | n/a | n/a | ~55 km² sector |
| Field mode, 150 m lines, 1-5 km of tongue | 0.44 km | 0.05 km | 0.07 km² |
| Field mode, 150 m lines, 2-4 km of tongue | 0.63 km | 0.09 km | 0.17 km² |
| Road mode, ~0.8 km transects, 1-6 km | 0.85 km | 0.14 km | 0.37 km² |
| Road mode, 1.5 km transects, 2-8 km | 1.52 km | 0.29 km | 1.38 km² |
| AEM-like, 2 km lines, 1-9 km | 0.98 km | 0.17 km | 0.51 km² |

The across-axis numbers are too good because the sim tongue is nearly straight. If I inflate both SDs by 3x for bends, split feeds and 3D effects (my judgment), road mode lands at about 3-12 km² and field mode at about 1-2 km². **That is about a 5-15x cut in upflow search area, for systems whose tongue is within about 80 m and on drivable ground.** If about 40-60% of blind Great Basin systems are outflow-visible this way (inference from M18 and M23, unverified), the model-wide rank-6 gain is about **3-6x on average**. Two notes: (1) where public Earth MRI AEM already covers the tongue, the rover adds less to rank 6 (about 1.5-2x, through density and near-surface detail), so deploy it first where there is no AEM; (2) the rover gives a much better prior for P02 darts and P03 carpets, which then confirm the apex.

### Rank 3, hydrologic masking and lid thickness (moderate)
The rover measures the thickness of the resistive fresh lid above the tongue to about 1-3 m where the tongue is above 40-60 m (sim). That is a direct reading of lid thickness, the input the Peclet fit on Sentinel profiles needs. It cannot see lids thicker than about 80 m. **Gain: maybe 1.5-2x narrower lid prior in rover cells.** It also marks playa cells as "rover-blind" so they are not wrongly counted as negatives.

### Rank 1, detection and occupancy (small to moderate)
A tongue mapped in a cell with no warm well is a new detection channel with its own catch rate. It is a third detector, not correlated with the Sentinel in the same way (different physics, different spatial support), which helps the designed two-detector survey separate occupancy from detection. **Gain: maybe 10-20% narrower on N in the outflow mask class** (my judgment, untested). It does nothing for deep or lidded systems with no tongue in the top 80 m, which is the hard part of rank 1.

### Rank 4, sensor reliability (small)
In the 20/40 calibration campaign, the rover is fast enough to map all 20 known blind systems and 40 cold controls in about 3-4 months for about $250-400k. That directly measures its own s/q per mask class.

### Rank 7 (small)
Shallow resistivity layering helps the conductive-background model a little (porosity and clay in the top 80 m). Not material.

### Not moved
Rank 2 (permeability class), rank 5 (temperature at 0.5-2 km), rank 8 (size tail) and rank 9 (recovery factor). A tongue says water flows, which hints at permeability, but it does not give a flow-per-well number.

### Visit ranking
The rover output (tongue conductance, axis and apex) goes straight into the VOI-Bank. It ranks which wells to log next and which parcels to option. This is where much of its value shows up: fewer wasted Sentinel visits.

---

## 5. Rights edge

- **The plume points to the next parcel.** The tongue is fed from up-gradient. The ranch well we logged sits in the outflow; the upflow is usually 1-8 km away on the range-front fault. That parcel is often another owner: a BLM section, a neighbour, or the private half of a railroad checkerboard in northern Nevada. We option it at about $1-2/acre (private) or take the leftover noncompetitive BLM lease at $1/acre/year, before any proof.
- **Nothing is filed.** Road driving is normal vehicle use. Ground geophysics on unleased BLM land is casual use under IM 2026-024 (H13), and data from unleased federal land need not be filed (43 CFR 3253.10(b), per the hardware memo). On county roads it is public right-of-way. On private land it rides on the option visit.
- **Open question (needs a written ruling).** IM 2026-024 lists ground geophysics, but does towing a sled count as "off-road travel" or "mechanized" if it leaves the road surface? Stay on the road surface in road mode. Ask one field office in writing, as P02 and P03 also recommend. Avoid closed routes, Wilderness Study Areas, sage-grouse leks in season and cultural sites (H13).
- **A buyer-legible map.** A 3D tongue model tied to well temperatures is something Ormat or Fervo geologists understand at once. It raises the price of an anomaly-stage package a little.
- **Low leak risk.** A UTV with a sled on a ranch road looks like a farm or survey job. Much less visible than a helicopter at 40 m.

---

## 6. Risks

1. **Depth limit.** About 80 m reach misses tongues under thick fresh lids and all deep upflows (Big Blind type). The rover is for the outflow class only.
2. **Playa blindness.** Thick surface clay or brine hides tongues; many valley floors are playa.
3. **Heat vs salt confusion** without enough tie wells; evaporite brines and connate water make false positives.
4. **Road network spacing** is too wide in some valleys; road mode then gives only a bearing, not an apex.
5. **Vehicle and cultural noise**: electric inverter noise, fences and pipes along every ranch road may drop 10-30% of data.
6. **Build risk** in the fast turn-off transmitter and the low-noise receiver; a commercial system removes it at about 2x capex.
7. **Legal grey zone** if a field office treats a towed sled as mechanized or off-road use.
8. **Tongue geometry is messy** (multiple feeds, bends, buried channels), so the apex can be wrong by more than the Monte Carlo says.
9. **Not unique.** tTEM is a known commercial method; a competitor could rent one. The moat is the ties, the land and the data, not the device.

---

## 7. First test

**Phase 0 (weeks 0-6, about $20-40k): rent before we build.** Rent or hire a commercial tTEM crew for 5-7 days (unverified price, about $15-30k). Run two valleys:
- **Known blind outflow:** Gabbs Valley, NV (BRIDGE: helicopter TEM, 2 m temperatures and TG holes; 124.9 C at 152 m, per the hardware memo and L14). The BRIDGE HTEM gives a free benchmark for the rover over the same tongue.
- **Cold control** valley of similar geology with ranch wells.
- Log 6-10 tie wells with the Sentinel kit in each.

**Pass:** (a) the rover maps a tongue that matches BRIDGE HTEM and the TG-hole temperatures; (b) the apex fitted from rover data alone lands within 1.5 km of the known upflow; (c) the control valley shows no false tongue after EC/T ties; (d) at least 40 line-km a day on real two-tracks; (e) under 30% of soundings dropped for noise.

**Then phase 1 (weeks 6-24, about $95-160k):** build v1, rerun Gabbs, then run the 20/40 calibration set.

**Kill:** reach under 50 m for a 4 ohm-m tongue in real data; apex error over 3 km at the known site; more than half of tie-checked conductors are brine, not heat; or a written BLM ruling that sled towing is not casual use (then field mode on private land only, which is still useful).

---

## 8. Self-scores (1-5)

- **model_uncertainty_alpha: 3.** Strong on rank 6 (5-15x search area for outflow systems), moderate on rank 3, small on ranks 1 and 4. Nothing on ranks 2 and 5.
- **rights_alpha: 4.** It points straight at the upflow parcel, often a different owner's, before any filing, and it runs on roads.
- **buildability: 3.** A tTEM clone is real but hard electronics (turn-off, receiver noise); 16-24 weeks for 2-3 people. Buying commercial makes it 4.
- **cost_scale: 4.** About $40-60 per line-km, about $4-9k per site, 40-80 sites per rover a year.
- **moat: 3.** The method is public and rentable. The moat is the tie wells, the tongue-to-upflow labels and the land we lock first.

---

## Sources

Repo files (read for this slice): `M08-magnetotellurics.md`, `M23-hydrology-masking.md`, `M31-new-data-2025-2026.md`, `P18-coded-source-transmitter-casing-source-r.md`, `../../evidence/L14-geophysics.md`, `../../../hardware/MEMO.md`.

Primary sources cited through those files:
- USGS Earth MRI airborne EM, Basin and Range: https://www.usgs.gov/index.php/data/regional-airborne-electromagnetic-and-magnetic-surveys-basin-and-range-province-nevada-oregon (DOI 10.5066/P1UKDJSM)
- Folsom et al. 2024, HTEM vs MT at East Hawthorne: https://www.osti.gov/biblio/3683813
- BRIDGE GDR 1682: https://gdr.openei.org/submissions/1682
- Sorey and Ingebritsen 1984 (Lassen outflow): https://pubs.usgs.gov/publication/wri844278
- Sorey et al. 1991 (Long Valley): https://openei.org/wiki/Conceptual_Model_At_Long_Valley_Caldera_Geothermal_Area_(Sorey,_Et_Al.,_1991)
- BLM IM 2026-024: https://www.blm.gov/policy/im-2026-024

From memory, not fetched (unverified): Auken et al. 2019, *Geophysics* 84(1) E13-E22 (tTEM); TEMcompany product line and prices; Central Valley tTEM work; Arps and Archie relations (textbook).

Scripts: `P20_ttem_sim.py`, `P20_backproject_mc.py` (this folder).
