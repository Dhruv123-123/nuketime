# P27: Thermal Calibration Chain (LST truth posts, frost/snow stakes, dawn-noon drone, night aircraft pod, tower stare)

Date: 23 Oct 2026. Build candidate P27, model track. This builds on `M10` (remote-sensing physics floor: about 10-20 W/m² per K of skin anomaly; stacking idea; snow as an integrator, "inference, untested"), `../../evidence/D10-satellite.md` (sensor specs, Coolbaugh 2007, Wei 2026, DOGAMI Summer Lake), `M21` (2 m record: 64% blank, about 0.5-1.5 W/m² floor), `P02`/`P13` (darts, 0.1-0.6 W/m² per point), `M23` (mask classes), `H13` (casual use under BLM IM 2026-024) and `MODEL.md` (SENTINEL-COX ranks). It does not repeat them. What is new here: (1) a concrete truth-post and stake design, (2) a per-pixel energy-balance fit with nuisance terms that have different day/night fingerprints, (3) a toy calculation of what calibration buys (`P27_calc.py`, this folder), (4) the snow calorimeter worked through to a detection floor, (5) the aircraft pod and tower in numbers, and (6) how the chain enters CREAM-COX as a wall-to-wall detector with a measured s/q per mask class.

**Method note.** The shared web-search budget was already used up when this slice ran. No new searches or fetches worked. Sources are the ones already read in M10, D10 and M21 (with URLs), plus papers and part prices I know from memory, marked (from memory, unverified). Toy-model outputs are marked (calc). Run with `python3 -I P27_calc.py`.

---

## Bottom line

- **The chain is worth building, but mostly as a snow-and-calibration machine, not as a skin-temperature hunter.** Skin temperature is still bound by M10 physics. My toy GLS fit (calc) says a 300-scene stack with no ground truth gives about **14 W/m² per pixel and about 3.6 W/m² over a 2 km² footprint (1 sigma)**. That is useless for blind systems. With the truth posts fixing the emissivity and moisture priors, and a drone thermal-inertia map, it drops to **about 4 W/m² per pixel and about 1 W/m² per footprint**. That means it catches about **half of the leaky fault-segment class** at 3 sigma and essentially none of the lidded classes.
- **Snow is the strong channel.** 1 W/m² melts **0.26 mm SWE per day** (calc; 3 W/m² gives 0.78 mm/day, matching the brief). For a 15-day snow event over a 2 mm/day background melt, each W/m² brings melt-out **about 1.9 days earlier**. Over about 10 winters × 4 events of Sentinel-2/Landsat history (2015-2026), with drift and aspect bias held to 0.5-1 day by the stakes, the floor is **about 0.3-0.55 W/m² per 20 m pixel and about 0.2 W/m² over a 2 km² footprint** (calc, with a 0.2 W/m² landform floor, judgement). That is **2 m-probe-class sensitivity, wall to wall, for free**, but only in snow-regime cells: northern Nevada, Oregon, Idaho, Utah, high valleys of NM and the Cascades foothills (unverified share, maybe 40-60% of Basin and Range valley cells).
- **Detection rates by mask class for a 2 km² footprint at 3 sigma (calc, `P27_calc.py`).** Leaky: 0.05 raw stack → 0.48 calibrated stack → 0.98 calibrated stack + snow. Thin dry lid: 0.00 → 0.01 → 0.50. Thick lid (>200 m): 0.00 → 0.00 → 0.02. Swept: 0 everywhere. The flux priors per class are judgement (unverified), but the pattern is robust. **Calibration raises the leaky catch rate by about 10x, and snow opens the thin-lid class.**
- **The middle rungs are for shape and conversion.** The dawn-noon drone gives apparent thermal inertia, which turns a probe or skin temperature into a flux. It also removes the basalt, dune and stream-mouth false anomalies that matched the real anomaly in size at Summer Lake (DOGAMI, via M10). The Cessna night pod maps 1,000 km² at 1.5 m in about **8.5 flight hours** (calc). That is **about $3-4k of flying** plus processing, so **$5-15k per 1,000 km²** all-in (unverified rates), within the brief's $5-30k. The tower stares at 1-4 km² every night for months across a fence line.
- **Hardware for the whole chain is about $200-230k** (BOM below, unverified prices), inside the brief's $150-250k. The satellite and snow layers then cost only compute to run across every parcel in the West.
- **Model effect (estimate, untested).**
  - Rank 4 (s/q per mask class): this is the main win. The chain gives a *measured* s and q for a wall-to-wall detector on the 20/40 campaign, and it does so cheaply. **About a 40-60% cut in the s/q spread for the remote detector** and about a 15-25% cut for the 2 m/dart detectors, because the posts also measure surface-offset nuisance at those sites.
  - Rank 1 (detection gap): **about 10-20%**. The chain sees every cell, so search effort stops being latent for the leaky and snow-visible classes. But it reads the same physical channel as 2 m probes and darts (conductive heat at the surface), so its misses are tied to theirs. It is a poor second detector for capture-recapture on N. The honest gain is the wall-to-wall occupancy map of the leaky and thin-lid classes, which pins down the "seen" half of the count.
  - Rank 6 (footprint and location): **about 30-50% cut for leaky and thin-lid targets** (pod and tower give 1-2 m shape; snow gives 20 m shape). It does nothing for lidded or swept targets.
  - Rank 7 (conductive background): **about 20-30% cut** from post k and flux-plate data plus the drone thermal-inertia map.
  - Rank 3 (mask class): a small but useful win. A cell that is warm at 3 m (dart) but blank in snow and skin is a "thick lid or swept" label. Maybe **10%**.
- **Rights edge.** Medium to strong. It ranks every 500 m parcel in snow country before any visit, with zero footprint and zero filing. Then the pod and tower confirm shape over a fence. This tells us *which* private ranch or BLM leftover parcel to lock. The snow layer flags the thin-lid class, which is the class that rival satellite TIR misses, at the time of the satellite pass, with no field cost.
- **Self-score:** model uncertainty alpha 3, rights alpha 4, buildability 4, cost/scale 5, moat 3. **Total 19/25.**

---

## 1. Physics case

### 1.1 Why the skin channel needs calibration, and what calibration can and cannot fix

Skin temperature residual against a local ring of pixels (so scene-wide atmosphere and forcing cancel) is, per scene s:

r_s = a_s·Δq + b_s·δε + c_s·δI + u + e_s

- **Δq** is the geothermal excess flux at the surface (W/m²). It acts like a steady heater at depth. Its skin effect is a = 1/h, with h about 10 W/m²/K at night and about 25 by day. So it is **warm at night, and about 2.5x less warm by day**.
- **δε** is the emissivity error. A 0.01 error gives about 0.7-0.8 K, almost the same by day and night. At night it is nearly the same shape as Δq. That is why a stack alone cannot separate them (calc: 300 uncalibrated scenes improve little on one scene).
- **δI** is a thermal-inertia or moisture texture anomaly: **warm at night, cool by day** (c = +1 night, about −2 day). That is the Summer Lake false anomaly.
- **u** is a persistent pixel offset (shading, shrub, soil) not in the fit. **e_s** is scene noise after ring differencing, partly autocorrelated through soil-moisture memory.

The three nuisance terms have different day/night fingerprints, but the priors decide the answer. Truth posts measure the skin with a contact-free radiometer, plus moisture, albedo and ground heat flux, at real pixels across the land-cover and mask classes. So they set the emissivity-error and inertia priors per class. The drone sets the inertia per pixel. Toy results (calc, priors unverified):

| Case | 1 sigma on Δq per 70 m pixel | 2 km² footprint |
|---|---|---|
| 1 night scene, no calibration | 15 W/m² | — |
| 300 scenes, no calibration | 14 W/m² | 3.6 W/m² |
| 300 scenes, post-calibrated priors | 6 W/m² | — |
| 300 scenes, posts + drone ATI | 4 W/m² | 1.05 W/m² |
| Tower, 120 pre-dawn stares + drone ATI | 3.3 W/m² (per 70 m-equivalent cell) | about 0.8-1 W/m² |

Calibration cannot beat the skin physics. Even perfect stacks need about 1 W/m² *at the surface* over a footprint. Lidded and swept systems deliver less than that (M21, M23). So skin is a leaky-class detector, and it is the shape tool for that class.

### 1.2 Snow as a weeks-long calorimeter

- Snow sits at 0 °C. The geothermal excess goes straight into melting the base. Melt is **0.26 mm SWE/day per W/m²** (334 kJ/kg latent heat; calc).
- Signal: melt-out date shift = 0.26 × D_on × Δq / M_bg, where D_on is days of cover and M_bg is the background melt rate. For thin valley-floor events (D_on 15 days, M_bg 2 mm/day): **about 1.9 days per W/m²**. For a seasonal northern pack (D_on 90 days, M_bg 5 mm/day): **about 4.7 days per W/m²** (calc), so seasonal-snow valleys are better.
- Noise: per-event timing noise of about 2.5 days (5-day Sentinel-2 revisit plus Landsat 8/9, clouds), and a persistent pixel bias from wind drift, aspect and shrub height. The stakes measure that bias directly (snow depth at the stake, snow-on from diurnal damping of the near-surface thermistors, time-lapse camera). With 40 events, the floor is **1.05 W/m² per pixel with a 2-day bias, 0.55 with 1 day, 0.33 with 0.5 day** (calc).
- Over a 2 km² footprint, with drift correlated over about 150 m and a 0.2-0.4 W/m² landform floor (judgement), the result is **0.2-0.4 W/m² at 1 sigma**. That is similar to a logged 2 m probe or a P13 dart cluster, but for every snow pixel since 2015.
- The same logic applies to **frost**. Clear-sky hoarfrost that clears earlier over warm ground is visible to the dawn drone and the tower camera. Sentinel-1 C-band and NISAR L-band freeze-thaw timing (backscatter drop on freezing, 6-12 day revisit) give a cloud-proof but weaker version. A 1 W/m² excess against early-winter ground heat release of about 5-15 W/m² delays frost onset by only a few percent (calc, judgement), so radar freeze-thaw is a sanity layer, not a detector.
- **Depth of sensitivity.** All of this reads flux at the surface. Under a dry conductive lid, z ≈ k·ΔT/q (P02/P13), a 0.2-0.6 W/m² footprint floor sees 100 °C fluid shallower than about 200-600 m. Swept (cold, flowing) aquifers stay blind.
- **Confounders.** Wind scour, sublimation, aspect, shrub height, dark soil, road and stock-tank heat, warm irrigation return water, and springs. Ring differencing, the lidar DEM, Sentinel-2 albedo, and the stake-measured bias model remove most of them. The rest goes in the landform floor.

### 1.3 Thermal inertia from the dawn-noon drone

- Two passes (pre-dawn and solar noon, same day, same path) give the diurnal amplitude ΔT. Apparent thermal inertia is ATI ≈ (1 − albedo)/ΔT, and with a post's flux plate and moisture it becomes a true thermal inertia P = √(kρc). With ρc from moisture, that gives **k per pixel**.
- k turns a 2 m probe or dart temperature into flux, and it turns a skin residual into Δq. It is the term that removed most of the uncalibrated error in §1.1.
- It is also the false-positive filter. Basalt, dunes and stream mouths are inertia anomalies (night warm, day cool). Geothermal heat is warm in both, but smaller by day.

### 1.4 Aircraft pod and tower stare

- **Pod.** A 640-pixel microbolometer with about 0.65 mrad IFOV at **about 2,300 m AGL** gives 1.5 m GSD and a 960 m swath. 1,000 km² with 20% sidelap is **about 1,300 line-km, about 8.5 h with ferry** (calc). It catches springs, seeps, warm fault traces and plume shapes at the leaky end. Single-flight noise is set by emissivity and inertia (3-10 K false anomalies at Summer Lake, DOGAMI), so the pod flies **on a winter night over snow** where possible. Snow has a near-uniform emissivity (about 0.99) and no inertia texture, which removes most of the false-positive library.
- **Tower.** A 10 m mast camera stares obliquely over 1-4 km² every pre-dawn for months. 120 stacked nights with a drone ATI map reach about 3.3 W/m² per 70 m-equivalent cell (calc), and the high-resolution daily visible frames give the exact melt-out and frost-clear pattern. It is the best footprint-shape tool for one target, and it sees across a fence.

---

## 2. Prior art

- **Coolbaugh et al. 2007, RSE**: night ASTER at Bradys, corrected for albedo, topography and thermal inertia. This is the template for the per-pixel energy-balance fit. https://doi.org/10.1016/j.rse.2006.09.001
- **Wei et al. 2026, Remote Sensing 18(9):1362**: annual-sinusoid fit on about 50 Landsat 8 scenes, +1-2 °C over fields with >100 °C at 100 m. This is the uncalibrated baseline that P27 improves on. https://doi.org/10.3390/rs18091362
- **Yuan et al. 2026, SGW**: solar/geothermal split of the Landsat stack. Two of four anomaly types were geothermal. https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Yuan.pdf
- **Romaguera et al. 2018**: needed ≥2 K residual in the Kenyan Rift. https://ris.utwente.nl/ws/files/72985263/Romaguera2018detecting.pdf
- **DOGAMI 2013, Summer Lake airborne night TIR**: 37 warm springs and a 6-8 K fault anomaly, plus 3-10 K false anomalies from basalt, dunes and stream mouths. This is the false-positive library the drone ATI must remove. https://www.oregon.gov/dogami/gtilo/data/supplemental/ARRA_Using_Airborne_Thermal_Infrared.pdf
- **Vaughan et al. 2012, JVGR**: ASTER captured only 30-45% of the Yellowstone heat budget. https://doi.org/10.1016/j.jvolgeores.2012.04.022
- **Silvestri et al. 2020**: ECOSTRESS, ASTER and Landsat 8 cross-calibration, with ECOSTRESS adding varied times of day. https://doi.org/10.3390/rs12010184
- **Snow-presence from cheap sensors.** Lundquist and Lott 2008 (WRR) used near-surface temperature loggers to time snow cover from the damped diurnal cycle (from memory, unverified). The stake design copies this.
- **Thermal inertia mapping.** The NASA HCMM mission (1978-1980) mapped apparent thermal inertia from day-night pairs. Kahle and others used it for geology at JPL (from memory, unverified).
- **Snow-free ground over geothermal areas** is known qualitatively at Yellowstone and Long Valley (unverified for the literature). I know of no systematic melt-out residual layer for the Great Basin (inference, as in M10).
- **Gap.** Nobody seems to publish a ground-calibrated, per-mask-class detection probability for any remote thermal method (M10 "no labelled negatives"). That gap is the product.

---

## 3. Concrete v1 design

### 3.1 LST truth post (60 units)

Two grades. **Gold** (20 units, on the 20 blind sites) and **silver** (40 units, one per cold control).

| Part | Gold | Silver | Note |
|---|---|---|---|
| IR skin radiometer, 8-14 µm, ±0.2-0.5 K | Apogee SI-111 or SI-411 class, about $650-800 | MLX90614-DCI/MLX90632 in a shielded housing, about $40-60, with a monthly gold cross-check | unverified prices |
| 5-depth thermistor string (2, 5, 10, 20, 50 cm, plus 100 cm on gold) | 0.02 K calibrated NTC, about $60 | same, about $40 | Gives ground heat flux from the gradient plus k |
| Soil moisture (5 and 20 cm) | TEROS 10 class, about $150 × 2 | capacitive, about $15 × 2 | |
| Albedo (up and down pyranometers) | Apogee SP-110 class, about $200 × 2 | photodiode pair, about $30 | |
| Ground heat flux plate at 5 cm | Hukseflux HFP01 class, about $600-800 | none (gradient × k from needle probe) | unverified |
| Air T/RH in shield, cup wind at 1.5 m | about $100 | about $60 | Sensible-heat term |
| Logger + LoRa + SD | ESP32/nRF52, about $60; Iridium SBD (RockBLOCK class) on 6 gold supersites, about $250 + about $15/month | ESP32 + LoRa, about $40 | Data-mule or ranch-gateway LoRa elsewhere |
| Power | 10 W panel + 12 Ah LiFePO4, about $90 | 5 W + 6 Ah, about $50 | Average draw under 0.1 W |
| Mast | 1.8 m galvanized pipe on a T-post, 1.5 m arm, radiometer at 45° off nadir viewing a 1-2 m² undisturbed patch | same | Removable, no concrete |
| **Unit cost** | **about $2,000-2,400** | **about $350-450** | Average about $950, inside the brief |

- **Sampling:** every 5 min, plus a 1-min burst ±20 min around each ECOSTRESS, Landsat and Sentinel-2 overpass (ephemeris loaded).
- **Install:** 2 people, about 1.5-2 h. Hand auger to 1 m for the string, flux plate cut into the pit wall, backfill in layers, needle-probe k at 3 depths (M16 kit). Service visit once per season, about 45 min.

### 3.2 Frost/snow stake (150 units)

- 1.5 m fibreglass stake, painted in 5 cm bands, with a 10 × 10 cm white/black target for camera scaling.
- Four thermistors: at −5 cm, 0 cm, +10 cm and +25 cm. Snow-on means the 0 and +10 cm channels stop swinging with the day (after Lundquist and Lott, from memory). Snow depth is read from which elevated channel is damped and from the camera.
- One trail camera per 3-4 stakes (40 cameras), hourly daytime frames, plus pre-dawn IR frames for frost.
- Cost: stake + logger about $60-80; camera about $80-120. **About $16-20k for all**.
- Install: 15 min per stake, 2-4 stakes per site (on-anomaly, edge, background), placed only in snow-regime sites (about 35-45 of the 60).

### 3.3 Dawn-noon drone kit (2 kits)

- DJI Matrice 350 + Zenmuse H30T (1280 × 1024 radiometric LWIR, about 50 mK NETD) or a Matrice 30T class, about $12-25k per kit (unverified). Two heated/ambient reference panels with thermistors, RTK base.
- Part 107 with night waiver-free operation (anti-collision lighting, rules since 2021, from memory). Flight at 120 m AGL gives 10-15 cm GSD and about 3-6 km² per dawn session with battery swaps.
- Crew: 1 pilot + 1 visual observer. Pre-dawn pass, then noon pass, same path. **One day per 1-3 sites**. In snow, an extra pass at the morning frost-clear time.

### 3.4 Night aircraft pod (1 unit)

- FLIR A700/A70 class 640 × 480 microbolometer, 24° lens, about $12-18k; VectorNav VN-300 class GNSS/INS, about $5-6k; a visible camera; a rugged PC; an external pod on an existing STC (step or strut mount) or the camera hatch of a rented survey Cessna 206. **About $35-50k hardware**, plus an FAA Form 337 field approval if no STC fits (unverified).
- Flight: 1.5 m GSD at about 2,300 m AGL, 200 km/h, commercial pilot, IFR-capable aircraft for night safety over dark terrain. **About 8.5 h per 1,000 km²**, about $3-4k flying at $350-450/h, plus about $2-8k processing and ground panels. **About $5-15k per 1,000 km²** (unverified).
- Fly on cold, calm, clear winter nights, ideally 1-3 days after a snowfall.

### 3.5 Tower stare (3 units)

- 10 m trailer-mounted telescoping mast, FLIR A400/A700 class on a pan-tilt, visible camera, 200 W solar + 2 kWh battery, LTE or Starlink Mini. **About $18-25k each**.
- Park on private ranch land looking over the target (often BLM next door). Stack pre-dawn mosaics every night for 2-6 months. One tower per top target, moved each season.

### 3.6 Software (the real product)

- A per-pixel Bayesian energy-balance fit run on ECOSTRESS night and day scenes, Landsat 8/9 day scenes, Sentinel-2 albedo and snow, Sentinel-1/NISAR freeze-thaw and soil moisture, and ERA5-Land and GOES forcing. It outputs Δq with a posterior, per pixel and per 500 m parcel, and P(seen | mask class).
- The posts set the nuisance priors per land-cover class. The stakes set the snow bias model. The drone sets per-pixel k. The pod and tower are high-resolution checks.
- Run across the whole West for compute only. Re-run on each new release (NISAR backfill, TRISHNA about 2027, SBG-TIR about 2029-2030).

### 3.7 Hardware total (unverified prices)

| Item | Count | Cost |
|---|---|---|
| Gold posts | 20 | about $44k |
| Silver posts | 40 | about $16k |
| Stakes + cameras | 150 + 40 | about $18k |
| Drone kits | 2 | about $40k |
| Aircraft pod | 1 | about $45k |
| Towers | 3 | about $65k |
| Needle probe, reference panels, spares | — | about $10k |
| **Total** | | **about $238k** (about $200k without the third tower) |

**Crew time per site (first visit):** 2 people for about 3-4 h (post, 2-4 stakes, k profile) plus about one-third of a drone day. **Per season after that:** about 1 h per site to service and download. The 60-site campaign takes about 4-5 weeks for a 2-person crew plus a drone pilot.

---

## 4. How it enters the model and what it shrinks

- **In CREAM-COX** the chain is a wall-to-wall detector D_rs that observes every cell, with detection probability s_rs(mask class, snow regime, land cover) and false-alarm rate q_rs(land cover). Unlike Sentinel visits, it has **no effort latent**: every cell is observed. The 20/40 campaign gives the posterior on s and q per mask class.
- **In THERMOS-B** the chain gives a censored likelihood on surface excess flux per parcel, Δq ± σ. This joins the dart and 2 m terms through the shared 1D column.
- **In VOI-Bank** the remote Δq posterior sets the prior for which parcels to visit, which raises EVSI/$ of every field visit.

| Rank | Effect | Size (estimate, untested) |
|---|---|---|
| 1 Detection gap | Full-coverage occupancy for leaky and snow-visible thin-lid classes. Misses are tied to the 2 m and dart channels, so it is a weak second detector for N. | About 10-20% narrower band on N |
| 4 s/q per mask class | Measured s/q for the remote detector, plus surface-offset nuisance for the 2 m and dart detectors at the same sites | About 40-60% (remote), 15-25% (ground) |
| 6 Footprint and location | 1-2 m shape (pod, tower) and 20 m shape (snow) for leaky and thin-lid targets | About 30-50% in those classes |
| 7 Conductive background | k per pixel from ATI, flux-plate truth | About 20-30% |
| 3 Mask class | Warm dart + blank snow and skin = thick lid or swept label | About 10% |
| 2, 5, 8, 9 | No direct effect | — |

**Regional total.** It mainly firms up the *seen* fraction. In the snow belt (northern NV, OR, ID, UT), it should move many cells from "unobserved" to "observed and blank to 0.4 W/m²". That narrows F5/F95 there but leaves the lidded tail, which is the large-N uncertainty, mostly to Sentinels, darts and E-MT.

---

## 5. Rights edge

- **Zero footprint before rights.** The satellite and snow layers need no visit, permit or filing. They rank every 500 m parcel in the snow belt before anyone knows we looked.
- **Over-the-fence confirmation.** A tower on a cooperating ranch can stare at the BLM parcel next door. An aircraft overflight needs no landowner consent (FAA Part 91). Shape is known before we nominate, file a state first-file, or take a leftover $1/ac/yr lease.
- **Ranch hook.** A post is a free weather and soil station (frost, soil moisture, evapotranspiration inputs). It can be traded for a heat option on the same visit as the P01 Sentinel.
- **Casual use.** Posts and stakes on BLM are small, removable and under the IM 2026-024 near-surface rules for the sensors in the ground (H13). The 1.8 m mast above ground is the part to check with each field office (unverified). Towers go on private land only. Drones may not take off or land in wilderness areas (from memory, unverified).
- **Limit.** The satellite layer is replicable by anyone with the same idea. The edge is speed, the calibration label set, and acting first on each new snow season.

---

## 6. Risks

- The skin channel is weaker than hoped. Even calibrated, it sees only the leaky half of the leaky class (calc). Most value depends on snow.
- Snow coverage of low valley floors is thin and irregular. In dry winters there may be few usable events. The southern targets (Imperial, AZ, southern NM) get no snow channel at all.
- Correlated nuisance (drift, sublimation, irrigation return water, stock tanks) may set the landform floor at 0.5 W/m² rather than 0.2.
- Producing fields used as "known blind" truth sites have changed surface heat since production started. Hindcast labels must use pre-production archives, or the s estimate is biased.
- ECOSTRESS lifetime on the ISS is uncertain. Landsat night scenes are rare. The night stack may be 100 scenes, not 300.
- Night flying over remote terrain has real safety risk. Use an IFR-capable aircraft and a commercial pilot.
- Masts on BLM may be ruled more than casual use.
- The moat is thin if a rival copies the snow layer. Zanskar could build it quickly.

---

## 7. First test (8-12 weeks, about $40-60k, unverified)

1. **Weeks 0-4, desk ($0-5k, compute).** Build the snow melt-out residual and the energy-balance stack over northern Nevada for 2015-2026. Pre-register predictions: on 5-8 known blind or low-leak systems with snow (for example Blue Mountain, McGinness Hills, Tungsten Mountain, Jersey Valley, Granite Springs 68-02; status unverified per system) versus 20 cold controls of the same landform, using pre-production winters where they exist.
2. **Weeks 4-8, build.** 6 gold posts, 14 silver posts, 50 stakes and 15 cameras. One drone kit.
3. **Weeks 8-12, install** on 6 blind and 14 cold sites before the first snow (November-December 2026). Fly dawn-noon drone passes on each.
4. **Winter 2026-27, read.** **Pass if:** (a) the snow residual separates the blind sites from controls at AUC ≥ 0.75 in hindcast and in the live season; (b) the stake-measured persistent melt-out bias is ≤ 1 day after the drift model; (c) the calibrated skin stack's residual matches post-measured ground flux within 2 W/m² at gold posts; (d) control blank rate ≥ 90%.
5. **Then** build the pod and towers, and fly one 1,000 km² winter night pod over the best snow-flagged valley.

**Kill or pivot:** snow landform floor > 0.6 W/m² at footprint scale; hindcast AUC < 0.65; fewer than 2 usable snow events per winter on > 70% of target valley floors. If the skin channel fails but snow works, drop the towers and pod and keep posts, stakes and the snow layer.

---

## Sources

- M10 and D10 in this repo, and the URLs therein: Coolbaugh 2007 https://doi.org/10.1016/j.rse.2006.09.001 ; Wei 2026 https://doi.org/10.3390/rs18091362 ; Yuan 2026 https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Yuan.pdf ; Romaguera 2018 https://ris.utwente.nl/ws/files/72985263/Romaguera2018detecting.pdf ; DOGAMI 2013 https://www.oregon.gov/dogami/gtilo/data/supplemental/ARRA_Using_Airborne_Thermal_Infrared.pdf ; Vaughan 2012 https://doi.org/10.1016/j.jvolgeores.2012.04.022 ; Silvestri 2020 https://doi.org/10.3390/rs12010184
- NISAR public release, July 2026: https://www.earthdata.nasa.gov/news/nisar-l-band-data-released-expanding-record-surface-changes
- ECOSTRESS: https://ecostress.jpl.nasa.gov/
- From memory, unverified: Lundquist and Lott 2008 (WRR, snow cover from temperature loggers); HCMM thermal inertia (NASA, 1978-80); part prices (Apogee, Hukseflux, METER, FLIR, DJI, VectorNav); FAA Part 107 night rules; aircraft rates.
- Toy model: `P27_calc.py` (this folder).
