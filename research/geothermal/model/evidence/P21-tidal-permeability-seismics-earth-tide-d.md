# P21: Tidal Permeability Seismics. Earth-tide and barometric dv/v mapping of fault-zone fracture compliance

Date: 23 Oct 2026. Build candidate P21, model track. This builds on `../MODEL.md` (SENTINEL-COX, ranked uncertainties), `M12-seismology.md` (large-N nodes, PoroTomo, PSET, "seismo-telluric" geophone add-on), `M30-permeability.md` (permeability classes, Hsieh 1987 well tides, Elkhoury 2006), `M27-fibre-das.md` (DAS on dark fibre, PoroTomo DAS), `P01` (Ranch Well Sentinel, well tidal fit), `P03` (E-MT node 2.0 with 3C geophone), `P06` (valley pressure and InSAR array) and `../../../hardware/MEMO.md` (18/25 kit, BLM IM 2026-024 casual use). It does not repeat them.

**Method note.** The shared web search budget for this workflow turn (200 calls) was used up before this agent started. All three searches I tried were refused, so **no new web pages were read**. Facts from repo files are cited by file (those files carry URLs). Papers I know are cited by author, year and journal and are marked (from memory, unverified) where I could not check details. All prices are my estimates (unverified). Numbers marked (calc) come from `P21_tide_calc.py` in this folder.

## Bottom line

Build it, but as **a mode of the node fleet we are already building (P03), plus one new box: a GPS-locked eccentric-mass source.** Do not build a separate seismic product.

What it is: put 30-60 three-component nodes across a candidate fault for 4-6 weeks. Measure tiny changes in seismic wave speed (dv/v) every hour, either from ambient noise or from a small repeating source. Then regress those changes against the computed earth-tide strain and the measured air-pressure load. Rock with open, fluid-filled cracks softens and stiffens under these loads 100 to 10,000 times more than tight rock. So the size of the tidal response at each node pair maps **where the fault zone is open**, along the fault and away from any well.

Four fixes to the brief:

1. **Depth is the honest limit, so say it plainly.** Ambient noise at 1-10 Hz on 4.5 Hz geophones samples roughly the top 20-500 m (calc). The coda of a 10-30 Hz source samples a similar shallow volume, a few hundred metres around the path. The reservoir is at 0.5-3 km. So P21 measures **near-surface fault-zone openness**, which is a proxy for deep permeability, not the deep value itself. It is still the only cheap way to rank fault strands for openness without a well. The deep part comes later from microseism-band (0.1-0.3 Hz) stacks on a few broadband reference nodes and from P01/P06 well tides.
2. **Use the lunar tides, not the solar ones.** Daily heating of the ground, traffic and pumps all run on solar time (S1, S2, K1 partly). Their signals swamp a tidal fit at those lines. The lunar lines M2 (12.42 h) and O1 (25.82 h) are clean. Separating M2 from S2 needs 14.8 days and O1 from K1 needs 13.7 days (calc). So **the minimum stay is 15 days, and 4-6 weeks is the design.**
3. **Barometric load is the bigger lever in most places.** A 1 kPa weather-front swing is a larger, broadband stress at shallow depth than the earth tide. A node with a barometer gives a second, independent compliance estimate from the same data. v1 puts a $3 barometer on every node.
4. **Active source on private land only. Passive nodes go anywhere.** A motorised vibrator is likely not casual use on BLM land (unverified; IM 2026-024 lists sensors, push rods and MT, not sources). So the source sits on the ranch whose heat we are optioning (P01 visit), and the passive nodes run out across the fault on open BLM or state land under casual use. Ambient-only mode is fully casual use.

Cost: about **$30-45k for a 60-node kit plus one source** (or about $8-12k for the source plus 30 extra nodes if the P03 fleet exists). Marginal cost about **$2.5-5k per target** at 6 weeks, mostly crew time. Self-score: model_uncertainty_alpha 3, rights_alpha 3, buildability 3.5, cost_scale 3.5, moat 3.5.

---

## 1. Physics case

### 1a. Why tidal dv/v sees open fractures

Seismic speed in rock depends on how stiff it is. In tight rock the stiffness barely changes with small loads. The ratio eta = (dv/v) / strain is about 1-10 for intact crystalline rock at depth (third-order elastic constants; from memory, unverified). Cracks change that. A thin, soft, fluid-filled crack closes a bit under compression and stiffens the rock a lot, then opens under tension. So damaged and fractured rock shows eta of about 10^3 to 10^5 (laboratory nonlinear elasticity; field values below; from memory, unverified). That is the 100-10,000x contrast this sensor uses.

Two features make it a permeability signal, not only a crack signal.
- **Fluid matters.** Under a tidal (slow) load, a crack connected to a fluid network can drain or fill. Its compliance then looks "drained" and is larger. An isolated or mineral-sealed crack does not. So a high, phase-lagged tidal response points to cracks that are open and **connected**, which is what a well needs.
- **Phase lag.** In a permeable, connected zone the dv/v response lags the strain by an amount set by diffusivity (the same physics as Hsieh 1987 for well water levels; M30). The lag gives a second number, roughly the hydraulic diffusivity D = k/(phi mu c). A lag of a few degrees at M2 over a 100 m zone points to D of about 0.01-1 m^2/s (calc, order of magnitude).

### 1b. Signal size

- Earth tide volumetric strain: about 2-5 x 10^-8 (textbook).
- Barometric load: 0.5-2 kPa over days (local weather).
- With eta = 1,000 (fractured fault zone), tidal dv/v is about 3 x 10^-5. With eta = 10, it is 3 x 10^-7.
- Stress sensitivity from barometric loads in shallow damaged rock, about 10^-8 to 10^-7 per Pa, gives 10^-5 to 10^-4 per kPa (calc; the Silver et al. 2007 and Niu et al. 2008 SAFOD values sit in this range, from memory, unverified).

### 1c. Detection limits (calc, `P21_tide_calc.py`)

I assume hourly dv/v noise per station pair of 10^-3 for ambient noise and 10^-5 for a stable active source, and that only 25% of pairs act independent.

| Setup | sigma of tidal dv/v amplitude | sigma(eta) | 3-sigma detection floor on eta |
|---|---|---|---|
| Ambient, small patch (100 pairs, 2 weeks) | 1.5e-5 | ~500 | ~1,500 |
| Ambient, 30 nodes, 4 weeks (400 pairs) | 5.5e-6 | ~180 | ~550 |
| Ambient, 60 nodes, 6 weeks (1,500 pairs) | 2.3e-6 | ~80 | ~230 |
| Active source, 30 receivers, 4 weeks | 2.0e-7 | ~7 | ~20 |

What this means:
- **Ambient noise alone** can find zones with eta above roughly 250-1,500. That is the open-fault-core class, not subtle contrasts. It is enough to say which of 2-4 strands is open.
- **The active source** gets down to eta of about 20. That separates "damaged but sealed" from "damaged and open", which is the more useful split. This is why v1 carries a source.
- Spatial mapping: each pair samples its path. With 60 nodes in a 2-3 line grid across and along the fault (spacing 50-150 m), pair-path tomography of eta gives cells of about 100-200 m along a 1-3 km fault segment.

### 1d. Depth of sensitivity

Surface waves sample roughly one third of a wavelength (calc):
- Vs 400-800 m/s basin fill: 5 Hz gives about 25-55 m; 1 Hz gives 130-270 m.
- Vs 1,500 m/s bedrock at the range front: 1 Hz gives about 500 m; 0.2 Hz gives about 2.5 km.

Coda waves at 1-5 Hz spread over a few hundred metres. So the dense node grid maps the **top 50-500 m** well. A few broadband reference nodes (or the microseism band on 2 Hz geophones) can add one coarse 0.1-0.3 Hz value for the 1-2 km depth range, with poorer precision. The model must treat P21 as a near-surface openness observation with a learned transfer to depth.

### 1e. Noise and how we beat it

| Noise | Size | Fix |
|---|---|---|
| Daily temperature in the top metres | dv/v 1e-4-1e-3 at S1 | Bury geophones 0.3-0.5 m; fit only M2, O1, N2; model S1/S2 as nuisance |
| Rain and soil moisture | dv/v up to 1e-3 over days | Rain gauge at hub; regress out; prefer dry season |
| Noise-source changes (traffic, wind, pumps) | Biases ambient dv/v | Use coda stretching (insensitive to source shifts), the active source, and drop wind hours (anemometer at hub) |
| Clock error | 1e-6 of a 1 s lag is 1 microsecond | GNSS PPS on every node (<0.1 microsecond); stretching method is clock-insensitive |
| Instrument drift | small | Fixed source position, fixed coupling, temperature-logged electronics |

Pumps: irrigation pumps break tidal fits in summer (P06). Run P21 in **Oct-Apr**, the same winter window as P06.

---

## 2. Prior art (all from memory, unverified)

- **Reasenberg and Aki 1974** (JGR): tidal changes of seismic speed measured with a repeating source near Quincy, California. First field claim.
- **Yamamura et al. 2003** (GJI): continuous ACROSS-type source in a tunnel at Aburatsubo, Japan. Tidal dv/v of about 10^-4 at shallow depth, so eta near 10^4-10^5 in near-surface rock.
- **Silver et al. 2007** (BSSA) and **Niu, Silver, Daley, Cheng and Majer 2008** (Nature 454:204): cross-well piezoelectric source at the SAFOD pilot hole, about 1 km deep. Travel-time precision near 10^-6. Stress sensitivity calibrated from barometric loads. Reported changes hours before two small earthquakes.
- **Takano et al. 2014** (GRL): tidal dv/v from ambient noise correlations on a small array in Japan. Showed passive noise can resolve tidal velocity changes.
- **Hillers et al. 2015** (JGR): tidal dv/v from high-frequency ambient noise on a dense array at the San Jacinto fault zone. Larger response near the fault damage zone.
- **Sens-Schonfelder and Eulenfeld 2019** (PRL): earth tides plus noise to probe in-situ nonlinear elasticity in northern Chile.
- **Takano et al. 2017-2019**: tidal sensitivity changed after large earthquakes, consistent with crack damage and healing (the seismic twin of Elkhoury et al. 2006 in M30).
- **ACROSS sources** (Kumazawa, Kunitomo and Japanese groups): eccentric-mass, phase-locked rotating sources used for months-long monitoring of volcanoes and fault zones. This is the source class v1 copies, scaled down.
- **Tsuji and co-workers (Kyushu)**: continuous dv/v monitoring with dense nodes and controlled sources in volcanic and geothermal areas in Japan.
- **PoroTomo, Brady NV** (M12, M27): 238 nodes for more than 2 weeks, vibroseis, 8.6 km DAS, with deliberate pumping changes. Data are public on GDR and the IRIS/EarthScope DMC. This is the free desk test.

What I did not find, from memory: any use of tidal dv/v to **rank undrilled geothermal targets** or fault strands before drilling. All uses I know are earthquake physics, volcano monitoring or reservoir monitoring at producing fields. So P21 is new as a pre-drill exploration tool (unverified that no one has done it).

Zanskar: it runs large-N passive seismic and DAS (M12, M13). I know of no tidal dv/v work there (unverified). Their passive-imaging hiring means they could copy it fast once they see it, so the edge is time plus the private calibration set.

---

## 3. v1 design

### 3a. System view

- **Receivers:** 30-60 3C nodes. Either the P03 E-MT node in "continuous seismic" mode, or a dedicated P21 node (below). Nodes buried 0.3-0.5 m. Layout: 3 lines across the fault (one at each end of the segment and one in the middle), plus 1 line along the hanging wall, spacing 50-150 m. Aperture 1-3 km.
- **Source (optional but planned):** one GPS-locked eccentric-mass vibrator on private land at the end of the line, within 0.5-2 km of the nodes.
- **Hub:** barometer, rain gauge, anemometer, temperature, LoRa gateway, Starlink or cellular backhaul. One per site.

### 3b. P21 receiver node (dedicated version)

| Part | Example | Cost (unverified) |
|---|---|---|
| 3C 4.5 Hz geophone set (3 elements in a sealed pod) | Geospace GS-11D class or Chinese 4.5 Hz equivalents | $60-150 |
| 24-bit, 4-channel ADC | TI ADS131M04 or ADS1256 | $10-25 |
| MCU | STM32 or ESP32-S3 | $8-15 |
| GNSS timing | u-blox M10 or LEA-M8T (PPS) | $20-60 |
| Storage | 128 GB microSD (250 Hz x 3 ch x 6 weeks is about 10 GB) | $15 |
| Barometer + temperature | Bosch BMP390 or similar | $3-5 |
| Battery | LiFePO4 12.8 V 12 Ah | $50-80 |
| Solar | 10 W panel | $20-30 |
| Radio (state of health only) | LoRa module | $10 |
| Case, cable, stake | IP67 box, PVC pod | $30-50 |
| **Total** | | **$230-440; about $300 at 100 units** |

- Size: hub box about 20 x 15 x 10 cm, about 2.5 kg with battery. Geophone pod about 10 cm, buried.
- Power: about 0.3-0.5 W continuous at 250 Hz (calc, typical for this class). 12 Ah at 12.8 V is about 150 Wh, so about 2 weeks on battery alone. The 10 W panel covers the rest in winter at Great Basin latitudes (unverified margin). 6 weeks is the design.
- Data: raw data stays on the card. LoRa sends daily health (battery, GNSS lock, RMS noise). Optional: the node computes hourly cross-correlations in the field and sends them over LoRa to the hub, so we see the tidal fit build up live (stretch goal).

If the P03 fleet exists, use those nodes and skip this build. The only change P03 needs is a continuous 250 Hz seismic mode (it records bursts by default) and a bigger card.

### 3c. Eccentric-mass source ("Mini-ACROSS")

- Mechanism: two counter-rotating eccentric masses on a steel frame bolted to a 0.6 x 0.6 m steel plate, set on a small concrete pad or anchored with 4 ground screws. Counter-rotation gives a vertical-only force.
- Drive: 0.75-1.5 kW brushless motor with a GPS-disciplined speed controller (phase locked to PPS).
- Force: F = m r w^2. With m r = 0.2 kg m, about 3.2 kN at 20 Hz and 12.6 kN at 40 Hz (calc). Sweep 10-40 Hz, phase coded.
- Schedule: one 15-minute sweep per hour (25% duty), so 24 independent travel-time samples per day.
- Power: about 400 W while running, about 2.4 kWh per day (calc). Options: (a) small inverter generator on propane, about one 20 lb tank every 2-3 days (unverified); (b) 1.5 kW solar plus 5-10 kWh LiFePO4 (about $3-5k, unverified); (c) ranch grid power at the barn or pump. Option (c) is often available on the ranch we are optioning.
- Range: with weeks of stacking, ACROSS-type sources are tracked over several km (from memory, unverified). For a scaled-down v1 I plan on 0.5-2 km.
- Weight: about 80-150 kg with plate, two-person carry in parts or a pickup tailgate lift.
- BOM: frame and plate $800-1,500; motor and controller $600-1,200; GNSS-disciplined controller board $200; masses and bearings $300-600; enclosure and safety guard $300; power $1-5k. **Total $3-9k** (unverified).
- Alternative small source: a piezo stack (as at SAFOD) only works over tens to about 100 m, or in a borehole. Use it in a ranch well (P01) for well-to-surface paths, not as the main source.

### 3d. Deployment and crew time per site

| Step | Crew | Time |
|---|---|---|
| Desk layout from fault maps, lidar, P03 MT and P06 data | 1 analyst | 0.5 day |
| Drive in, place 60 nodes (dig pod hole 0.4 m, stake panel, GNSS check) | 2 people | 1.5-2 days (about 15 min per node plus walking) |
| Install source on ranch pad (when used) | 2 people | 0.5 day |
| Mid-term check (swap cards on the source, fuel, fix any dead nodes) | 1 person | 0.5 day |
| Recover nodes | 2 people | 1-1.5 days |
| Processing (automated pipeline) | compute + 1 analyst | 1-2 days |
| **Total** | | **about 5-7 person-days in the field per site** |

Field cost per target (unverified): crew 6 person-days at about $400 per day is $2.4k; truck, fuel, propane about $0.5-1k; node wear and losses about $0.3-1k. **About $3-5k per target**, in line with the brief. Two kits in rotation give about 12-16 targets per winter season.

### 3e. Processing pipeline (software, in ObsPy and our own code)

1. Pre-process: remove instrument response, spectral whitening, drop wind and rain hours.
2. Ambient: hourly cross-correlations for all pairs in 1-4, 2-8 and 4-16 Hz bands. Measure dv/v by coda stretching against a 6-week reference. Active: deconvolve the source sweep, pick direct and coda windows, measure dv/v by stretching and by cross-spectral phase.
3. Forcing: compute the theoretical tidal strain at the site (solid earth plus ocean loading; tools such as SPOTL or pygtide, unverified tool names), and the barometric load from the hub barometer.
4. Regression: dv/v(t) = a_M2 strain_M2 + a_O1 strain_O1 + b P_baro(t) + nuisance (S1, S2, temperature, rain) + noise. Get eta (amplitude) and phase lag per pair, with posterior uncertainty (NumPyro, same stack as CREAM-COX).
5. Mapping: path-weighted tomography of eta and lag onto 100-200 m cells. Output: P(open, connected) per fault segment.
6. Feed to THERMOS-B: a censored likelihood for the permeability class (rank 2) and the "open strand" variable (rank 6), with a transfer function from shallow eta to deep class learned from the calibration set (section 6).

---

## 4. What it does to the model's uncertainties

These are my estimates (unverified), and the transfer from shallow openness to deep permeability is the key unknown.

- **Rank 2, permeability class (about 10x on MWe).** P21 gives a near-surface openness score per strand, with no well needed. If shallow openness and deep permeability class correlate at rho about 0.4-0.6 (unverified; M30 says recently slipped, critically stressed faults stay open, and those reach the surface), one P21 survey cuts the variance of log permeability class at that target by about **15-35%**. Combined with slip tendency (M30) and a P01 well tidal value at the same site, the joint cut could be about 40-50%. It works on the **80-90% of fault length that has no well** (calc, guess), which is where P01 and P06 cannot see.
- **Rank 6, which strand carries upflow.** Most targets have 2-4 candidate strands (range front, step-over, intra-basin fault). P21 picks the open one with ambient eta contrasts of 3x or more. I expect it to cut the entropy of "which strand" by about **30-50%**, and to shift dart (P02, P14) and gradient hole placement by hundreds of metres. That alone saves a share of wasted holes.
- **Rank 1, detection in lidded cells.** Small. Where the cold lid is thin (under about 300 m), an open fault zone shows through the lid as high eta even with no heat at the surface. That gives a weak extra "something is open here" detector with a different mask from the thermal tools. Maybe a **5-10%** better catch rate in thin-lid cells, mostly as a second detector for the two-detector survey design (rank 4).
- **Rank 4, sensor reliability.** P21 itself needs calibration: 10-20 known systems and 10-20 cold faults. That campaign doubles as evidence for the other sensors.
- **Ranks 3, 5, 7, 8, 9.** Little direct effect. Small help on 7 (basin depth from the same ambient data, M12).

EVSI view: the RNPV/ac target depends on P(permeability class >= Limited Distributed). P21 is most valuable on targets that already have heat evidence (P01/P02/P03) but an unknown strand, i.e. the step right before we choose where to drill or which BLM parcels to nominate. That is a narrow but high-value slot.

## 5. Rights edge

- **Ambient mode is fully casual use** under BLM IM 2026-024 (passive battery sensors in small holes; hardware MEMO). No notice, no filing while the land is unleased (43 CFR 3253.10(b), hardware MEMO). The data are ours.
- **The source sits on the optioned ranch**, so the visit that signs the ranch heat option (P01) also hosts the source. The private-land rights deal and the BLM parcel ranking come from one deployment.
- **Choosing which BLM parcels to nominate.** At a BLM auction, parcels are 640-2,560 acres. Knowing which strand is open lets us nominate and bid on the right section and skip the dry one. It also lets us lock the cheaper noncompetitive leftovers on the open strand that others pass over.
- **Buyer pitch.** Ormat and Fervo care most about flow per well. A strand-level openness map, tied to a calibration set, is the kind of permeability evidence that can move the price of a farm-out at anomaly stage, which the hardware MEMO said hardware does not usually do. Modest, but real.

## 6. Risks

1. **Depth transfer may be weak.** Shallow openness may not track deep permeability (a sealed shallow zone over an open deep one, or the reverse). Mitigation: calibrate on 10-20 known fields with well data (Brady, San Emidio, Desert Peak, Patua, Don A. Campbell, McGinness) and cold faults.
2. **Ambient precision may be poorer than assumed** in quiet rural valleys (low noise means weak correlations). Mitigation: active source; longer stays; use trains, highways and wind farms as sources.
3. **Solar-time noise leaks into the fit** (temperature, pumps). Mitigation: lunar lines only; winter; buried pods.
4. **Source permitting**: a vibrator on BLM land likely needs a notice of intent (unverified). Mitigation: private land only.
5. **Mixed signals from clay and sediments.** Unconsolidated basin fill is also very nonlinear (high eta) without being permeable. Mitigation: compare against the same lithology away from the fault; use phase lag (drained vs undrained); joint with P03 MT and IP.
6. **Easy to copy once published.** Zanskar has the seismic team. Mitigation: do not publish; the moat is the calibration set and the joint P01/P03/P21 data.
7. **The brief's "nodes already owned" is not yet true** (unverified). If the P03 fleet slips, buy 60 dedicated nodes ($18-26k).

## 7. First test

**Desk, weeks 0-6, about $0-2k (cloud compute).**
1. Pull PoroTomo Brady passive node data (238 nodes, March 2016, about 15 days) from GDR and the IRIS/EarthScope DMC (M12 lists the GDR link https://gdr.openei.org/submissions/1070 for the active tomography; the passive node archive is on the DMC, network code unverified).
2. Compute hourly dv/v for all pairs in 2-16 Hz. Fit M2 and O1 against computed tidal strain and against the local barometer.
3. **Pass test:** (a) eta resolved above noise for at least 20% of pairs; (b) the eta map is higher along the mapped Brady fault zone and fumaroles than off-fault, at more than 2 sigma; (c) the phase or size of the response changes with the PoroTomo pumping stages (known pressure change, a built-in check). 15 days is just enough to split M2 from S2.
4. **Second desk test:** San Emidio PSET (1,302 stations, about 180 h; M12, https://gdr.openei.org/submissions/1441) only if raw continuous data are available (unverified). 7.5 days is too short for clean M2/S2 separation, so use barometric loads there.
5. **Kill for the desk stage:** no fault-correlated eta at Brady after full processing. Then fall back to active-source-only, and test that in the field before any further spend.

**Field, winter 2026-27, about $15-25k.** Build one source and 30 nodes (or borrow P03 nodes). Run 4 weeks at one known blind system with wells (for calibration) and 4 weeks at one target with 2-3 candidate strands. Pass test: the known productive strand ranks top.

## 8. Self-scores (1-5)

- model_uncertainty_alpha: **3**. Real, direct openness signal for ranks 2 and 6 away from wells; capped by the shallow depth of sensitivity.
- rights_alpha: **3**. Casual-use passive mode; picks the right BLM parcel and ranch; helps price a farm-out.
- buildability: **3.5**. Nodes are standard; source is a known design scaled down; 8-12 weeks for a two-person team for v1. The processing is harder than the hardware.
- cost_scale: **3.5**. $3-5k per target; 12-16 targets per kit per winter. Not a per-km2 carpet, a per-strand test.
- moat: **3.5**. New for pre-drill use; the calibration set and the joint data are hard to copy; the method itself is not.

## Sources

Repo files: `M12-seismology.md`, `M27-fibre-das.md`, `M30-permeability.md`, `P01`, `P03`, `P06`, `../../../hardware/MEMO.md` (each carries its own URLs). URLs reused from them: https://gdr.openei.org/submissions/1070 (PoroTomo), https://gdr.openei.org/submissions/1441 (San Emidio PSET), https://seismosoc.org/wp-content/uploads/2018/06/WED.Monroe.1445.Matzel.pdf (Brady attenuation).

From memory, unverified (no web access this run): Reasenberg and Aki 1974 JGR; Yamamura et al. 2003 GJI; Silver et al. 2007 BSSA; Niu et al. 2008 Nature 454:204; Takano et al. 2014 GRL; Hillers et al. 2015 JGR; Sens-Schonfelder and Eulenfeld 2019 PRL; Hsieh, Bredehoeft and Farr 1987 WRR; Elkhoury, Brodsky and Agnew 2006 Nature; ACROSS source literature (Kumazawa, Kunitomo).
