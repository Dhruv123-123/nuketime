# P02: Logging Heat-Flux Dart (3 m casual-use dart with heater, moisture and gas port)

Date: 23 Oct 2026. Build candidate P02, model track. This builds on `../../../hardware/evidence/H01` (2 m heat carpet, LoRa probe BOM, crew rates), `H04` and `M22` (soil gas), `H05` (2-6 m robotic probe rig idea), `H13` (BLM IM 2026-024 casual-use reading), `M16` (needle-probe k), `M21` (the INGENIOUS 2 m analysis: 64% blank areas, 1.2 C noise, ±5 C seasonal wave, 10-30 m "deep dart" case), `M23` (masking) and `MODEL.md` (SENTINEL-COX ranks). It does not repeat them.

**Method note.** The shared web-search budget was used up before this slice started. No new web searches or fetches worked. Everything below comes from the repo evidence files, what I already know, and **my own simulation** (`P02_dart_sim.py`, in this folder). Part prices and some prior-art details are from memory and are marked (unverified). Simulation outputs are marked (calc).

---

## Bottom line

- **The upgrade that matters is depth plus gradient, not more sensors at 2 m.** A 3 m dart with six sensors, logged for 6-12 months and read as a *heat flux*, not a temperature, should lower the detectable excess heat flux from about **1.5 W/m² (one-shot 2 m, the ~3 C threshold) to about 0.1-0.2 W/m²**. That is roughly **8-15x better**. In 2 m "DAB" terms it is about **0.2-0.4 C equivalent**, well below today's ~3 C (calc plus judgement; the idealized simulation gives 0.06-0.09 W/m²).
- **Why it works.** At steady state, a heat-flux gradient does not care about the surface mean temperature. Albedo, slope and soil changes shift a 2 m *temperature* by several degrees (the 2.4 C between-area scatter in M21), but they barely change the *gradient*. The seasonal wave at 3 m is 18-35% of its surface value (calc), and it can be fitted out. Weather and year-to-year drift are shared by every dart in a valley, so most of that error **cancels between neighbours**. In my simulation a pair of darts in one valley, 12-month record, the deepest three sensors (2, 2.5 and 3 m), and heater-measured k at ±10% gave a flux-difference error of **12-25 mW/m²**. That works out to about **10-20 mW/m² per dart against a valley reference** (calc, 4-30 seeds).
- **What this does to depth reach.** For a dry, conductive lid over 100 C fluid (k 1.2 W/m/K, surface 15 C), a probe sees the heat if fluid sits shallower than z = k·ΔT/q_threshold. That gives **about 70 m for a one-shot 2 m probe, about 200 m for a logged 2 m probe, and about 700-1,000 m for the dart** (calc). This is the Granite Springs case: TG gradients above 220 C/km, which is about 0.26-0.33 W/m² if the heat is conductive to the surface, under a 2 m map that read under 3.5 C (M21). It is about 5-8 sigma for a dart and invisible to one-shot 2 m.
- **What it does not fix.** A cold, fast aquifer that sweeps heat sideways (Argenta type, the "swept" mask) stays blind, unless the water table is shallower than 3 m. The dart then cannot see below the aquifer. That case stays with the Sentinel well profile, He, and E-MT.
- **Blank-rate cut.** If 25-40% of the 35 blank INGENIOUS areas hide a conductive surface flux between 0.15 and 1.5 W/m² (unverified guess; Granite Springs is one), the blank rate drops from **64% to about 40-50%**. The blanks that stay become *calibrated* negatives with a known detection limit, which the model needs as much as hits.
- **Cost.** About **$140-210 per dart in prototype quantity, about $90-130 at 1,000+** (unverified part prices). Install is about **$90-140 per dart** with a 2-person crew (8-10 darts a day). That is about **$1k/km² at 500 m spacing and $4k/km² at 250 m**. Hardware is recovered and reused, so a second deployment costs about $2.5k/km² at 250 m. A 20-40 dart prospect test costs **$5-10k**, against $150-500k for one TG hole.
- **Rights edge.** On unleased BLM land it fits the IM 2026-024 casual-use list: a rod under 2 inches, an install under 10 ft, battery sensors in a small hole, no mechanized rig. **Nothing is filed before we nominate or take a leftover $1/ac/yr lease.** The IM runs to 30 Sep 2029, so this is a **3-year window** to carpet. On private land, the same dart is a **free 3-depth soil moisture and temperature probe** (the irrigation-scheduling door opener) traded for a heat option.
- **Self-score:** model uncertainty alpha 4, rights alpha 4, buildability 4, cost/scale 4, moat 3. **Total 19/25.**

---

## 1. Physics case

### 1.1 What the dart measures

Below the zone of daily swings, soil temperature is:

T(z,t) = T_s + G·z + (seasonal wave decaying as e^(-z/d)) + (weather and year-to-year transients from the surface) + (local non-conductive effects)

where G = q/k is the steady conductive gradient. The dart's job is to estimate G and k separately, and then report **q = k·G** with an error bar. That number enters the THERMOS-B column directly as a flux observation.

- **Damping depth d = sqrt(2κ/ω).** For κ of 0.3, 0.5 and 0.8 ×10⁻⁶ m²/s, d is 1.74, 2.24 and 2.83 m. The annual wave keeps e^(-z/d) of its surface amplitude: **32-49% at 2 m and 18-35% at 3 m** (calc). With a ±13 C surface wave, that leaves ±2.3-4.6 C at 3 m. It is still large, but **fitted per dart**: amplitude decay and phase lag between the six depths give κ directly (the classic amplitude and phase method).
- **Heater gives k.** The diffusivity κ comes from the wave, but flux needs k = κ·C. A line heater on the 2.0-3.0 m section runs at about 1.3 W/m for 4 hours. The late-time temperature rise follows ΔT ≈ (q'/4πk)·ln(t). At k = 1 W/m/K that is about **0.24 C per decade of time** (calc), easy to read at mK resolution. The late-time slope does not depend on contact resistance, so a thin sand-packed annulus is fine. The valid window runs from about r²/4κ ≈ 2-5 minutes to well before end effects of a 1 m heater (about a day) (calc). The test repeats each quarter, which also tracks how k changes with moisture.
- **Why k matters for detection, not just units.** Basin-fill k runs from about 0.4 to 2 W/m/K (dry sand to wet clay or gravel; unverified range). With no k, a low-k patch at normal flux gives a high gradient and looks like an anomaly. In my pair simulation the "no k" error was 28-52 C/km against 12-29 mW/m² with k (calc). The heater halves the false-alarm rate.

### 1.2 Noise budget (simulation)

`P02_dart_sim.py` solves 1D conduction to 12 m. The forcing is a ±13 C annual wave, AR(1) weather noise (σ 3 C, 3-day memory), ±0.5 C random year-to-year mean shifts, top-1.5 m k varying ±0-30% with moisture through the year, and sensors at ±0.01 C noise plus ±0.01 C fixed offset. True background flux is 80 mW/m².

| Estimator (12-month record) | Error | Note |
|---|---|---|
| Single dart, absolute gradient from mean profile | sd 57-84 C/km, bias +29 C/km | Weather and year-to-year drift leak in. **A lone dart is not a flux meter.** (calc, 40 seeds) |
| Single dart, my crude forced-boundary inversion | sd 120-200 C/km | Not robust. The unknown starting state below 3 m dominates. Dropped (calc) |
| Pair, same valley, logged 2 m probe (1, 1.5, 2 m), heater k | sd 29-43 mW/m² | (calc, 4-30 seeds) |
| Pair, 3 m dart, all six depths, heater k | sd 27-41 mW/m² | Shallow sensors add moisture noise (calc) |
| **Pair, 3 m dart, deepest three (2, 2.5, 3 m), heater k** | **sd 12-25 mW/m²** | Best layout. Per dart against a multi-dart valley reference: about 10-20 mW/m² (calc) |

Lessons for the design:
1. **The detector is differential.** Every valley gets 10-20% reference darts on cold ground, and the model reads q relative to the valley field. This matches the model's "dated effort, per-area offset" structure.
2. **Depth beats sensor count.** The upper sensors (0.5-1.5 m) are for fitting the wave and moisture, not for flux. Most of the gain over a logged 2 m probe comes from the 2.5-3 m pair.
3. **A full year is the robust record.** Three to six months will need a proper state-space (Kalman) inversion forced by the cap air sensor and by ERA5-Land or PRISM soil-temperature climatology. My quick attempt failed, so 3-6 month numbers are not yet earned (unverified).

**Real-world error not in the simulation** (so I set the field floor at 0.1-0.2 W/m², not 0.06-0.09):
- Infiltration after storms and snowmelt carries heat down. In desert interfluves recharge is small. **Do not site darts in washes**, on irrigated fields (for geothermal duty), or on playas with shallow water and evaporation.
- **Terrain.** Slope aspect changes the surface mean by 1-3 C (unverified), which bends gradients near range fronts. This needs a terrain correction from a DEM, as in classic heat-flow work.
- **Lateral variation** in the real background flux (±10-20 mW/m² inside a valley; unverified), plus lithology and k variation inside the 3 m column.
- **Thermal offset (rectification).** When k changes with moisture through the year, it biases the mean gradient. Permafrost workers know this well. It showed up in my simulation as a bias for single darts, and it cancels largely, but not fully, in pairs.
- **Vapour transport** in very dry, coarse soils.

### 1.3 Detection limit in model terms

| Probe | Excess flux at 3 sigma | Depth to 100 C fluid it can see under a dry conductive lid | Status |
|---|---|---|---|
| One-shot 2 m (public data) | about 1.5 W/m² (3 C) | about 70 m | M21 |
| Logged 2 m (H01 carpet) | about 0.5 W/m² | about 200 m | M21 |
| **3 m dart, v1** | **about 0.1-0.2 W/m²** (sim 0.06-0.09) | **about 400-1,000 m** | calc, this file |
| 10-30 m push or TG hole | about 0.02-0.05 W/m² | more than 1 km | M21 |

The 1-1.5 km reach only holds when the hot body is at least as wide as it is deep. A 2-3 km wide system at 500 m depth qualifies. A narrow fault plume at 1 km gives a smeared, weaker surface flux. The footprints in M21 (1.5-10 km²) mostly qualify.

### 1.4 Side channels

- **Soil moisture** at 0.3, 0.6 and 1.0 m. It fits the moisture-dependent k and flags infiltration events (these are its geothermal uses). It is also the farmer's product.
- **Soil gas port** at 2.8 m. A sand-packed slotted tip under a bentonite seal, with a 1/8" PTFE line to a septum in the cap. On revisits it lets us sample CO₂, ⁴He (with the truck He sniffer from M22 and M07), Rn and Hg. Gas at 3 m is far below the biological and barometric noise of the 1 m H04 sniffer probe (unverified magnitude). Per M22, it stays a segment-scale likelihood (which fault segment leaks), not a regional layer.
- **SP electrode**: a Pb-PbCl₂ tip electrode against a cap electrode. A vertical streaming-potential gradient averaged over months is experimental (unverified). Along fence lines we can wire darts into a true SP line, a standard method (M30, Corwin and Hoover).
- **Aquifer contact.** Where the water table is shallower than 3 m (valley floors, near springs), the tip sensor reads aquifer temperature directly. That is the strongest outflow-tongue detector short of a well (M21 F7).

---

## 2. Prior art (from memory unless a URL is given)

| Prior art | What it shows | Gap P02 fills |
|---|---|---|
| UNR/DRI 2 m probe (Coolbaugh, Sladek, Zehner, Kratt, 2006 onward) https://openei.org/wiki/2-M_Probe_Survey | One-shot 2 m RTD, $200-500 per station, found Teels Marsh, Emerson Pass and Gabbs | Snapshot, temperature not flux, ~3 C threshold (M21) |
| UNR long-term 2 m monitoring stations (in GDR 1391, StCode LT/B) https://gdr.openei.org/submissions/1391 | Seasonal model and albedo correction | Few sites, no k, no flux |
| Olmsted 1977, USGS PP 1044-B https://app.ingemmet.gob.pe/biblioteca/pdf/USGS-PP-1044-B.pdf | 30 m showed 12 C where 1 m showed 3.3-3.7 C | Depth wins. 3 m is the casual-use compromise |
| USGS Raft River 30 m auger heat-flow holes, OFR 86-123 https://pubs.usgs.gov/of/1986/0123/report.pdf | Gradient × k heat flux from shallow holes was 1970s standard practice | Needed a rig and a permit; ours is casual use |
| Kappelmeyer (1957) 1 m surveys; LeSchack and Lewis (1983, Geophysics) "Shallo-Therm" 1 m surveys with surface-energy-balance correction (unverified citation detail) | A modelled correction can pull signal out of very shallow data | One-shot. We log for a year and add depth |
| Dual-probe heat-pulse sensors (Campbell et al. 1991; Bristow et al. 1994, soil-physics literature) and ASTM D5334 needle probe | In-situ k, κ and C from small heaters | We reuse the line-source maths on a 1 m heater section of the dart |
| Ground-source heat-pump thermal response tests | Line-source k from a heated borehole, long-time ln(t) slope | Same maths at metre scale |
| Permafrost borehole thermistor strings (GTN-P networks) | Mature low-power multi-year logging; the "thermal offset" rectification effect | Mature tech we can copy |
| NASA InSight HP3 "mole" (2018-2021) | A self-hammering penetrator with a heater (TLM) for k. Designed for 3-5 m, it stalled at about 0.4 m because the regolith gave too little friction (Spohn et al., Grott et al. 2021, unverified detail) | **A warning.** A self-hammering mole is v3 research, not v1. Terrestrial alluvium has more confining friction but has gravel and caliche |
| Ag capacitance probes (Sentek Drill & Drop, AquaSpy, CropX; prices unverified) | Through-wall capacitance moisture rings in a PVC tube, 0.3-1.2 m | Our moisture channel copies this; it is the farmer-facing product |
| Zanskar | Uses TG wells, LBNL seismology and ML on public layers (Z03, M13) | No public sign of a mass shallow-flux carpet (unverified) |

**No one I know of has published a basin-scale network of logged, heater-calibrated 3 m heat-flux probes for blind geothermal.** The pieces are all mature. The new part is combining them and running them on casual-use land at scale.

---

## 3. Concrete v1 design

### 3.1 Layout ("drive-and-drop")

1. **Drive casing.** 1.75" OD (44.5 mm, under the 2" limit) threaded steel casing in three 1 m joints, with an expendable steel cone tip. It is driven to **2.95 m**, a 10 cm margin under 10 ft (3.048 m). It is reused.
2. **Sensor tube**, dropped inside the casing. It is 3/4" Sch 40 PVC (26.7 mm OD), 3.0 m long, with a sealed bottom plug. Inside is a flex-PCB or ribbon string carrying:
   - six TMP117 digital temperature sensors at 0.5, 1.0, 1.5, 2.0, 2.5 and 2.9 m, pressed to the wall with foam and thermal paste;
   - one constantan heater wire looped along 1.9-2.9 m (about 10 Ω);
   - three capacitance moisture ring pairs at 0.3, 0.6 and 1.0 m;
   - the gas line (1/8" PTFE) to a slotted 10 cm tip section;
   - an optional Pb-PbCl₂ SP electrode at the tip.
3. **Casing pulled** with a hand jack. The annulus (about 5 mm) is filled with dry fine silica sand at the bottom 0.3 m (gas tip). A 0.3 m bentonite-chip seal goes above it, then native cuttings, then a bentonite surface seal.
4. **Cap.** A flush, 100 mm potted cap holds the MCU and radio, batteries, an internal antenna, an air and surface temperature sensor, a QR tag and the gas septum. It is low profile, for vandalism resistance and stealth.

Why not drive the sensor rod itself: a 3 m, 3/4" sensor rod buckles in gravel. A steel rod also short-circuits the vertical gradient (carbon steel k ~45). Stainless (k ~16) would be acceptable (calc: a 3/4" Sch 40 stainless wall equals about a 3 cm soil radius in axial conductance), so a **"sacrificial stainless" v1-alt** for soft, fine ground is worth one test. Drive-and-drop is the default because the casing is reused and PVC is thermally neutral.

### 3.2 Electronics and power

| Item | Part (example) | Prototype $ (qty 100) | At 1k+ $ |
|---|---|---|---|
| MCU + LoRa | STM32WL module (RAK3172 or LoRa-E5 class) | 10 | 7 |
| Temperature | 6 × TMP117 (±0.1 C absolute, 7.8 mK LSB), bath-matched to ±0.01 C relative against a reference | 24 | 14 |
| Heater driver + heater wire | MOSFET, 1 m constantan | 4 | 2 |
| Moisture | capacitance-to-digital IC (FDC2214 class) + copper ring pads on the flex | 8 | 5 |
| SP / spare analog | ADS1220 24-bit ADC + Pb-PbCl₂ electrode (DIY) | 20 | 10 |
| Flex PCB string 3 m + connectors | | 20 | 10 |
| Flash 16 MB, RTC, BLE (service dump) | | 5 | 3 |
| Batteries | 2 × Li-SOCl₂ spiral D cell (Saft LSH20 class, 13 Ah, can deliver the ~0.4 A heater current) | 50 | 35 |
| Cap, potting, antenna, air sensor | | 15 | 10 |
| Sensor tube, plug, gas line, septum | | 12 | 8 |
| Consumables per hole: cone tip, sand, bentonite | | 8 | 6 |
| Calibration (bath) and assembly labour | | 20 | 10 |
| **Total per dart** | | **about $195** (range $140-210) | **about $120** (range $90-130) |

All prices are from memory (unverified). They are consistent with the H01 2 m BOM ($150 prototype, $45-70 at 10k) plus the heater, moisture, gas, deeper string and second battery.

**Power budget** (calc, unverified current figures):
- Sampling 6 T + 3 moisture every 15 minutes, with LoRa uplinks of a compressed summary 4 times a day: about 2-4 Wh per year.
- Heater tests: 1.3 W × 4 h = 5.2 Wh each. Quarterly that is about 21 Wh per year.
- Sleep: about 10 µA, or 0.3 Wh per year.
- Total: about 25 Wh per year against about 90 Wh usable in two D cells. **That is 3+ years**, enough to outlast the IM 2026-024 window.

**Comms.**
- **LoRaWAN store-and-forward.** Data rate is about 1 kB per day.
- An antenna at ground level cuts range to about 2-5 km (unverified), so the gateway goes on a range-front hilltop with line of sight. It is the H01 gateway (solar + LoRa + Starlink Mini or Iridium, about $1,500 prototype).
- Darts out of range keep a full year in flash and dump over BLE or LoRa when a truck drives by (the "data mule").
- A per-dart satellite modem (Iridium SBD class, about $250 plus a monthly fee; unverified) is used only for isolated sentinel darts.

### 3.3 Deployment and crew time

- **Kit.** A UTV or pickup on existing roads only (the travel plan). The hammer is a gas breaker or hammer-drill (Atlas Copco Cobra Combi class) or a 30 kg electric breaker on a power station ($1.5-8k; unverified). Add drive caps, a hand rod-jack ($0.8-1.5k; unverified), a cart for casing, and a GNSS receiver. The **on-road robot pusher** is an OHV-mounted percussion pusher. OHV-mounted direct push is explicitly on the IM casual-use list (H01), but a truck-mounted rig is not.
- **Time per site, 2-person crew**, about 40-60 minutes:
  - walk-in, 5-10 minutes;
  - drive to 2.95 m, 10-25 minutes, with a 1 m offset retry on refusal;
  - drop the tube, backfill and seal, 10 minutes;
  - pull the casing, 10 minutes;
  - cap, GNSS, photo, radio check and hole log, 5 minutes.
- **Rate and cost.** That gives **8-10 darts per day by hand, 20-30 per day with an OHV pusher** (unverified). At $800-1,200 per crew-day, install is $90-140 per dart.
- **Refusal** in caliche and fan gravel is the main field risk. Guess 10-30% of sites need a retry or a move (unverified).
- **Recovery.** Pull the sensor tube with the jack (10 minutes), refurbish for about $40, and redeploy. The batteries last 3 years, so most darts can stay for the full window.
- **Siting rules.** Use interfluves, not washes. Keep away from irrigation, playas, the shade of tall shrubs, and slopes steeper than 10° (unless they are terrain-corrected). Keep 10-20% of darts as valley references.

### 3.4 Data product

Each dart gives a flux q ± σ_q (W/m²), k ± σ_k, κ, wave amplitude and phase, depth to water if it is shallower than 3 m, moisture series, and gas-port samples. They are effort-tagged, carry a GPS position to ±2 m (which helps rank 7 position ties), and are pre-registered in the VOI-Bank before install.

---

## 4. How it shrinks the model's ranked uncertainties

These are estimates from the physics above and model judgement. No field data exist yet (unverified).

| Rank | Uncertainty | How the dart helps | Rough shrink |
|---|---|---|---|
| **1** | Detection gap / occupancy, deep or lidded catch rate (2-5x on N) | It raises the shallow-heat channel's sensitivity q_c under the **dry conductive-lid** mask from about 0 (for heat deeper than 70-200 m) to about 0.5-0.8 for heat within about 0.5-1 km. Dart blanks become calibrated negatives in high-λ cells. Two detectors per cell (Sentinel well plus darts) under the shared mask latent make P_det identifiable. | In carpeted provinces, about **30-40% of the rank-1 spread** on N. A province F5/F95 of about 11.6x could narrow toward 6-8x after about 1,000-3,000 darts. It does **nothing for the swept mask**. |
| **3** | Hydrologic masking / lid thickness | A dart flux that matches deep TG or well gradients means a conductive lid. High flux at depth with normal flux at 3 m means sweep. A water table shallower than 3 m gives aquifer temperature directly. | About **25-35%** of rank-3 variance where the vadose lid is thick and dry (most NV valleys). Little in shallow-water valleys. |
| **6** | Upflow location and footprint area (about linear in MWe) | A flux map at 250 m spacing outlines the conductive footprint. Flux peaks lie above the shallowest heat, which is closer to upflow than a ranch-well outflow sample. It checks MT outlines, which overstate area several-fold. | Footprint error about 3-5x → **about 1.5-2x** for systems with conductive expression. This is the strongest effect. |
| **7** | Conductive background and position error | In-situ k plus a valley background-flux field at ±10-20 mW/m² gives the local basal flux and ties legacy TRS ±400-800 m points to GPS-located flux. | About **30-50%** of local rank-7 variance. |
| 4 | Sensor reliability s/q per mask | It is the cheap second detector in the 20-blind and 40-cold calibration campaign. | Enables the design. Its own s/q is measured there. |
| 2 | Permeability class | Only weakly, through He/CO₂ at the gas port on fault segments. | Under 10% |
| 5 | Temperature at 0.5-2 km | Conductive extrapolation of q is valid only under the conductive mask. | About 10-20% where conductive |

**Likelihood for THERMOS-B.** Add reading type "D" (dart): q_obs ~ N(q_3m(column, mask) − q_ref(valley), σ_q² + σ_model²), with σ_q about 0.02 W/m² and σ_model about 0.03-0.05 W/m² until calibration. In P_det, the dart channel's q_c depends on mask: high for open or dry-lid, about 0 for swept, and "direct" when the water table is shallower than 3 m. That replaces the G5 rule that "2 m blanks are weak effort" for every dart-covered cell.

**Where EVSI per dollar is highest.** Darts go in 2 m-blank, high-λ cells with deep water tables and a structural target (Granite Springs type). There they flip G5 weak blanks into either hits or calibrated negatives. They come after the Sentinel in cells with wells, because a ranch-well profile is cheaper per metre of depth. The dart wins where there are no wells, which is most unleased BLM land.

---

## 5. Rights edge

- **Unleased BLM.** On my reading of H13, IM 2026-024 casual use needs **no notice or application**, while H01 described an optional NOI with a 15-day reply. Treat "no filing" as the default and file one decoy NOI to get a written ruling for this exact method. Note that "temporary placement" has no stated maximum duration. A field office could still call a 12-month install non-casual, especially in sage-grouse habitat, WSAs or cultural sites (H13). The carpet leaves **no public record**, so the anomaly is ours until we **nominate** (padded with decoy parcels) or grab a **leftover noncompetitive lease at $1/ac/yr** (R02). Window: until 30 Sep 2029, which is about 3 years at 2,000-5,000 darts a year.
- **Private ranches.** The dart doubles as a free soil moisture and temperature probe. For irrigation it reads only to 1 m usefully, and irrigated fields are bad geothermal sites, so the farmer value is mostly on **neighbouring dryland and pasture** and as a goodwill gift. It goes alongside the Sentinel well visit and helps sign the heat option ($1-2/ac) on the same visit.
- **State land.** It needs a right-of-entry, which names the parcel (H13). Avoid it unless the anomaly runs there.
- **Edge over Zanskar.** Zanskar buys at BLM auction after nomination. A dart carpet tells us which leftover or never-nominated parcels hold conductive flux, so we can take them for $1/ac/yr, and which nominated parcels to bid up or let go. That is a flux map Zanskar does not have, built on land where nothing is filed.

---

## 6. Risks

1. **Driving refusal** in caliche and fan gravel cuts the share of sites reaching 2.95 m. Range-front fans, the best structural targets, are the stoniest.
2. **Non-conductive near-surface noise** (infiltration, terrain, vapour, vegetation) may hold the real floor at 0.2-0.3 W/m², not 0.1. That would still be 5-7x better than one-shot 2 m.
3. **The swept mask stays blind.** If most hidden Great Basin systems are swept (Argenta type), the dart mostly adds calibrated negatives and footprint for leaky systems.
4. **Legal.** A field office may treat 3-12 month installs as beyond casual use, and IM 2026-024 could be withdrawn before 2029. Visible caps could leak the target to other crews.
5. **Comms.** Ground-level LoRa range may be short, so it will need more gateways or data-mule drives.
6. **Moat.** The hardware is easy to copy. The moat is the dataset, the pre-registered calibration, and the 3-year IM window used first.
7. **Simulation limits.** It is 1D, idealized, and runs few seeds. The single-dart inversion did not work, so 3-6 month records are unproven.

---

## 7. First test

**Desk, weeks 0-2, $0.** Rerun `P02_dart_sim.py` with real ERA5-Land and PRISM forcing for Granite Springs Valley. Add terrain and infiltration, and build the Kalman inversion for 3-6 month records. Check predicted noise against the UNR long-term 2 m stations in GDR 1391.

**Build, weeks 2-8, about $8-12k.** Build 30 darts, 1 gateway and the drive kit. Bath-calibrate the strings. Run the heater k check in a sand box against a needle probe (ASTM D5334 style).

**Field, months 2-8 (install November, read through May, then a full year), about $15-25k all-in.**
- **Line A, Granite Springs Valley:** 12 darts across the TG-hole anomaly (GDR 969, gradients above 220 C/km). This is the clean 2 m false negative (M21). Check land status first. If the anomaly is leased, use unleased margins or get the lessee's consent.
- **Line B, a cold control valley:** 12 darts.
- **Line C, a known leaky positive** (SE Gabbs Valley or Tungsten Mountain): 6 darts.

**Pass if all of the following hold:**
1. Granite Springs dart flux is at least 2x the control, at 4 sigma or more.
2. It agrees with the TG-hole q = k·G within 30%.
3. Heater k is within 15% of needle k on samples.
4. At least 80% of sites reach 2.9 m.
5. At least 90% of units report after 6 months.

**Kill (as a geothermal detector) if** Granite Springs reads indistinguishable from control after 12 months, or the field noise floor is above 0.4 W/m². Then the dart is only a logged 2 m probe at higher cost. Fall back to H01 plus 10-30 m pushes under a permit.

---

## Sources

- INGENIOUS 2 m compilation, GDR 1391: https://gdr.openei.org/submissions/1391
- Granite Springs PFA data, GDR 969: https://gdr.openei.org/submissions/969
- UNR 2 m method page: https://openei.org/wiki/2-M_Probe_Survey ; improvements: https://openei.org/wiki/Improvements_in_Shallow_(Two-Meter)_Temperature_Measurements_and_Data_Interpretation
- Olmsted 1977, USGS PP 1044-B: https://app.ingemmet.gob.pe/biblioteca/pdf/USGS-PP-1044-B.pdf
- USGS OFR 86-123 (Raft River 30 m holes): https://pubs.usgs.gov/of/1986/0123/report.pdf
- BLM IM 2026-024 (casual use): https://www.blm.gov/policy/im-2026-024
- Basin and Range shallow-survey review (Geothermics 1986): https://pubs.usgs.gov/publication/70014477
- Gabbs Valley blind discovery: https://www.usgs.gov/publications/discovery-blind-geothermal-system-southern-gabbs-valley-western-nevada-through
- From memory, not re-checked this slice (unverified): Campbell et al. 1991 and Bristow et al. 1994 (dual-probe heat pulse); ASTM D5334 (needle probe); LeSchack and Lewis 1983 (Geophysics, shallow thermal surveys); Kappelmeyer 1957; InSight HP3 mole results (Spohn et al.; Grott et al. 2021); Sentek, AquaSpy and CropX probe designs; component prices.
- Simulation: `P02_dart_sim.py` (this folder). Run with `python3 P02_dart_sim.py 0 30`.
