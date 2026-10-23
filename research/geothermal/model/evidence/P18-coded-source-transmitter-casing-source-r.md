# P18: Coded-Source Transmitter, with three source modes (ranch-well casing, carpet dipole for IP/CSAMT/TEM, pipeline cathodic-protection piggyback)

Date: 23 Oct 2026. Build candidate P18, model track. This builds on `P03-e-mt-node-2-0-drone-placed-dc-coupled-te.md` (the E-node carpet, which already budgets a "road-side IP transmitter" for $15-25k but does not design it), `P01-ranch-well-sentinel-2-0-a-resident-well-.md` (the ranch-well visit), `M08-magnetotellurics.md` (the conductor non-uniqueness problem and inversion sensitivity to static shift), `M23-hydrology-masking.md`, `../../../hardware/evidence/H03-mt-seismic-nodes.md` (which lists pipelines and cathodic protection as an MT *noise* source), `H13-permits-and-secrecy.md` and `V01-redteam-heat-stack.md` (BLM IM 2026-024 casual use), and `../MODEL.md` (SENTINEL-COX and its ranked uncertainties). It does not repeat them.

**Method note.** The shared web-search budget for this workflow turn was used up before this agent started. All searches were refused, so **no new web pages were read**. Sources below are repo files or standard literature I know. Those from memory are marked (from memory, unverified). Prices are my estimates (unverified). Numbers marked (calc) are my own arithmetic. Numbers marked (sim) come from `P18_casing_sim.py` in this folder: a coarse 3D finite-volume DC solver I wrote and ran for this file (about 20 s per run).

---

## Bottom line

Build it. It is the source half of the P03 carpet, so it is not optional if we want IP at all. But be honest about which mode carries the value.

1. **The carpet dipole mode (IP + CSAMT + loop TEM) is the main value.** Normalised chargeability splits smectite clay cap from basin brine, which is the main false-conductor trap (rank 4). Loop TEM at about 1 in 8 node sites fixes E-MT static shift, which otherwise biases cap and lid depth by roughly ±20-40% (rank 3). These are standard, well-proven methods. The new parts are the cheap own-built GPS-coded transmitter and the fact that P03 nodes already sit there to record it.
2. **The casing mode is real but smaller than the brief hoped.** My sim shows a steel ranch casing used as a buried electrode gives about the **same** plume signal as a plain stake at the wellhead when the warm saline tongue is shallow (150-250 m). It roughly **doubles** the azimuthal plume anomaly when the tongue is deeper (400-500 m) under a resistive cold lid (anomaly about 16% with a stake, about 36% with the casing, at 2 km). It gives almost nothing when the lid itself is conductive (5-8%). So the casing mode is a **niche booster for deep outflow under fresh cold lids**, which is exactly the mask class the Sentinel cannot see through. Worth it, because the clamp costs about $100 and the visit already happens.
3. **The cathodic-protection (CP) piggyback is the cost-scale wildcard.** A pipeline rectifier pushing 10-30 A into a deep anode bed is a free, kilometre-scale, deep current source. At 10 km it still gives about 1 microV/m (calc), which 1 hour of coded stacking reads easily. It needs operator buy-in, so treat it as optional upside for cells near pipelines.

v1 is one trailer kit: a **2-20 kW own-built SiC H-bridge transmitter with a GPS-disciplined code generator**, a 20 kW diesel generator, 5 km of wire on two powered reels, stake-cluster and casing clamps, and a 100 m TEM loop. About **$22-38k** all-in (unverified), built in **8-12 weeks** by two people. Per site: casing mode about **$1.5-2.5k** (one crew-day), carpet IP/CSAMT about **$3-6k per 25 km² carpet** on top of the P03 node cost.

My estimates of model gain (untested): **rank 4**, the clay-vs-brine likelihood ratio rises from about 2-3x (resistivity only) to about **6-10x**, so the shared false-positive mask class splits in two; **rank 3**, lid and cap depth bias from static shift drops from about ±20-40% to about **±10%**; **rank 6**, plume bearing back to upflow narrows from about ±45-60° (heads only) to about **±15-25°** where the casing or stake signal works, which cuts the upflow search area about 2-3x; **rank 7**, small help on conductive background. It does not move ranks 2, 5, 8 or 9.

Self-score: model_uncertainty_alpha 3, rights_alpha 3, buildability 4, cost_scale 3, moat 3.

---

## 1. Physics case

### 1a. Why a controlled source at all
Natural-field MT (P03) gives resistivity only. A conductor in the Great Basin can be a hot-system smectite cap, saline basin water, playa or lake clay, or a fossil cap (M08, V01). Resistivity alone cannot tell them apart. A controlled current source adds three things that natural fields cannot:
- **Chargeability (IP).** Only an on/off current makes the decay curve.
- **Known geometry.** We know where the current goes in, so we can pick where it goes in: at the bottom of a casing, or across a carpet.
- **Absolute, distortion-free depth control.** A loop TEM sounding measures the magnetic field, which near-surface lumps do not distort. So it pins the true resistivity under each site and removes the MT static shift.

### 1b. Mode A: ranch-well casing as a buried electrode
**Idea.** Steel casing is a long, very conductive electrode. Current clamped onto the wellhead runs down the steel and leaks out along its length. So the current starts at 100-400 m depth, below the cold fresh lid, inside the warm saline outflow if the well taps it. E-nodes 0.5-3 km away see an E-field pattern that is stretched along the conductive tongue. The direction of the stretch is the bearing back toward upflow. This is the old **mise-à-la-masse** idea, "charging" the conductor, applied to an outflow plume.

**Casing as an electrode (calc).**
- Grounding resistance of a line electrode, R = rho / (2 pi L) x ln(2L/a). For a 250 m, 6-inch casing in 30 ohm-m ground, R is about **0.17 ohm**. In 60 ohm-m it is about 0.33 ohm. That is far lower than a stake cluster (10-50 ohm). So almost all the transmitter voltage drops at the far return electrode and in the wire, and the casing end is never a shock hazard.
- How far the current runs down the steel before leaking out. Steel conductance per metre of 6-inch casing (7 mm wall) is about 2 x 10^4 S·m. The leakage decay length is about **280 m in 3 ohm-m, 510 m in 10 ohm-m and 1,240 m in 60 ohm-m** (calc). So in a resistive cold lid, current runs most of the way down a 100-400 m casing. In the conductive plume it leaks out quickly, which is what we want: the plume takes the current.
- Corrosion. A unipolar 10 A for 8 hours would dissolve about 80 g of iron from the casing (Faraday, calc). The coded waveform is bipolar and zero-mean, so net loss is near zero. We still state it in the landowner letter.

**Simulation (sim).** `P18_casing_sim.py` solves the 3D DC problem on a 100 m grid (padded to about ±10 km, 4 km deep). Background 30 ohm-m. Cold fresh lid 60 ohm-m (or 8 ohm-m in the conductive-lid case). A warm saline tongue of 3 ohm-m, 1.2 km wide and 100 m thick, runs 6 km from the well toward +x. The return electrode sits 9 km away at right angles. I compare (a) casing source and (b) stake at the wellhead, each with and without the tongue. The metric is the max/min over azimuth of |E| (tongue) / |E| (no tongue) on rings of nodes, which is how strongly the pattern points along the tongue.

| Case | ring 0.6 km | ring 1 km | ring 2 km |
|---|---|---|---|
| Tongue 150-250 m, resistive lid: casing / stake | 1.41 / 1.44 | 1.63 / 1.44 | 1.64 / 1.53 |
| Tongue 400-500 m, resistive lid: casing (equipotential limit) / stake | 1.10 / 1.05 | 1.21 / 1.12 | **1.36 / 1.16** |
| Tongue 400-500 m, conductive 8 ohm-m lid: casing / stake | 1.05 / 1.06 | 1.07 / 1.08 | 1.08 / 1.04 |
| Tongue 150-250 m, conductive 8 ohm-m lid: casing / stake | 1.22 / 1.27 | 1.24 / 1.25 | 1.24 / 1.21 |

The model is coarse. The casing is smeared over a 100 m cell, which makes it leak too easily near the top. So the real steel case sits between my "1x" and "100x conductance" runs, and the deep-tongue casing gain is probably near the upper number. Read the table as order-of-magnitude.

**What it says.**
- A tongue within about 250 m of the surface shows a strong 40-60% azimuthal anomaly with **either** source. Here the stake is enough, and the casing is just a lower-resistance electrode.
- A tongue at 400-500 m under a resistive lid gives a 12-16% anomaly with a stake and about 20-36% with the casing. That roughly **doubles the signal**, and it is the case where the stake anomaly gets close to the geological noise floor (about 5-10%, my estimate for unmodelled 3D heterogeneity).
- A conductive lid (clay or brine above the tongue) screens both sources. That case belongs to IP and MT, not to the casing mode.

**Signal vs noise (calc).** |E| is about 1-5 microV/m per amp at 1-2 km (sim). At 10 A, a 40 m P03 leg sees about 0.4-2 mV. A 20% anomaly is 0.1-0.4 mV. The natural telluric noise on 40 m is about 8 microV/sqrt(Hz) near 1 Hz (P03). One hour of coded stacking in a narrow band gives about 0.13 microV. So **instrument and natural noise are not the limit**. The limit is geology we did not model. That is why v1 uses several sources at each ranch (2-4 casings plus stakes) and inverts them jointly, rather than trusting one bearing.

### 1c. Mode B: carpet dipole for time-domain IP, CSAMT and loop TEM
- **IP physics.** Smectite has a high cation exchange capacity, so it stores charge on grain surfaces and is strongly chargeable. Brine conducts through the pore water and is barely chargeable. Revil and co-workers showed that normalised chargeability (Mn = M x sigma) scales with surface conductivity, with a near-constant ratio R = Mn / sigma_surface of about 0.1 for clay-rich rocks (from memory, unverified; Revil 2012-2017, Water Resources Research and Geophysics). Lévy et al. (2018, GJI 215:1558) showed smectite controls conductivity in the Krafla cores. Lévy et al. (2019, GJI 218:1469) used field ERT + TDIP at Krafla to map clay separately from pore-water conduction (both from memory, unverified). Rule for the model: **high sigma + high Mn = clay (cap or playa); high sigma + low Mn/sigma = brine.**
- **IP signal (P03 calc, kept).** About SNR 10 within 1-1.5 km of the line after about 4-5 hours of 2 s on/off stacking at 5 A. v1 runs 10-20 A, so the reach grows to about 1.5-2.5 km and the stacking time drops by 4-16x.
- **Coding.** Instead of plain on/off, v1 sends a pseudo-random binary sequence (m-sequence), so one transmission gives the full impulse response, IP decay and many frequencies at once. Prior art: Ziolkowski's MTEM (Ziolkowski, Hobbs and Wright 2007, Geophysics) and He Jishan's 2^n-sequence "wide-field EM" (WFEM), which Chinese crews use widely for geothermal (both from memory, unverified). New here: several of our sources run **orthogonal codes at the same time** (CDMA), so casing, dipole and CP sources can share one node deployment without taking turns.
- **CSAMT.** A 1.5 km dipole at 15 A, read 6 km away in 10 ohm-m ground, gives about 0.17 microV/m far-field E (calc), about 7 microV on a 40 m leg, against about 0.13 microV noise after 1 hour of stacking: SNR about 50. CSAMT fills the MT "dead bands" (1-5 kHz and 0.5-5 s) where natural signals are weak. The near-field limit means it reaches about 1-1.5 km depth at 6-8 km offset (rule of thumb, unverified).
- **Static shift fix by loop TEM.** E-field data at a site are scaled up or down by small near-surface lumps. This "static shift" moves log-resistivity curves up or down and biases depth by about sqrt(shift). A factor-2 shift means about ±40% depth error. A central-loop TEM sounding measures dB/dt, which this galvanic distortion does not affect. So one TEM sounding pins the shift at that site (Sternberg, Washburne and Pellerin 1988, Geophysics 53:1459; from memory, unverified). v1 drives a 100 x 100 m loop from the same transmitter at about 1 in 8 node sites and reads it with a small air-core coil. Joint MT + DC inversion with a shared near-surface model handles the sites in between.

### 1d. Mode C: pipeline cathodic-protection piggyback
- **Physics.** Impressed-current CP rectifiers push about 5-50 A from an anode bed (often a deep vertical bed 30-150 m) to the pipe (from memory, unverified). That is a deep, strong, fixed current source. It is also a known **noise** source for MT (H03). Coding it turns the noise into signal.
- **Signal (calc).** 20 A in 30 ohm-m gives about 10 microV/m at 3 km and about 1 microV/m at 10 km. One hour of coded stacking reads 1 microV/m on a 40 m leg at SNR about 300. So one rectifier lights up a radius of about 10 km.
- **How.** Operators already run GPS-synchronised current interrupters on rectifiers for close-interval surveys, typically on/off duty of about 4:1 (from memory, unverified). We supply a solid-state interrupter that runs our pseudo-random code at about 80% "on" duty, so the pipe stays protected under the PHMSA rules (49 CFR 192 Subpart I; from memory). The operator's CP technician installs it. In return, the operator gets a stray-current and interference map from our carpet, which they otherwise pay for.
- **The catch.** The return path is the pipe itself, through coating holidays along many kilometres. Its geometry is partly unknown. We model the pipe (route from NPMS) as a leaky line with fitted leakage. Only cells within about 10 km of a CP rectifier benefit. In Nevada the pipelines run mainly along the I-80 and US-95 corridors, which do cross the Humboldt and central Nevada geothermal belts (from memory, unverified).

### 1e. Detection limits

| Quantity | v1 resolution (estimate, unverified) | Works when | Model input |
|---|---|---|---|
| Plume bearing from casing/stake source | ±15-25° | tongue < ~500 m, >5x contrast, resistive lid, 2+ sources | rank 6 back-projection direction |
| Lid base over a conductive tongue | ±15-20% | resistive lid over conductive tongue | rank 3 lid thickness |
| Normalised chargeability | ±3-5 mV/V, Mn/sigma class | within 1.5-2.5 km of the dipole | rank 4 mask class (clay vs brine) |
| Static shift factor | ±10% per TEM site | 1 TEM per ~8 nodes | rank 3, rank 7 |
| CSAMT resistivity | ±10-15% in log rho, 1-5 kHz and 0.5-5 s bands | 6-8 km offset, 10-20 A | fills MT dead bands |
| CP-source resistivity | ±10-20% | within ~10 km of a coded rectifier | regional deep conductivity |

---

## 2. v1 design

### 2a. Transmitter (own build)
| Part | Spec | Cost (unverified) |
|---|---|---|
| Power stage | Full H-bridge from two 1200 V, 100-200 A SiC half-bridge modules, isolated gate drivers, 1,000 µF film DC bus | $1.5-3k |
| Front end | 3-phase rectifier + soft-start + DC bus up to 800 V; buck stage for low-voltage casing mode | $1-2k |
| Control | GPS-disciplined timing (u-blox F9T class), FPGA or MCU code generator (m-sequences, square wave, TEM ramp), 24-bit current logger on a precision shunt and Hall sensor | $0.8-1.5k |
| Protection | Ground-fault and insulation monitor, over-current trip, e-stop on a hand radio, interlock on the electrode boxes | $0.6-1.2k |
| Enclosure | Ruggedised 19-inch case, forced air, about 35 kg | $0.5-1k |
| Comms | LoRa link to the P03 node net, Starlink Mini for status upload | $0.6k |
| **Transmitter subtotal** | 2-20 kW, 0-800 V, 0-25 A, bipolar, code-agile | **$5-9k** |

Commercial units for comparison: Zonge GGT-10/30, Phoenix TXU-30, IRIS VIP-10000, at about $40-120k (from memory, unverified).

### 2b. Rest of the kit
| Part | Spec | Cost (unverified) |
|---|---|---|
| Generator | 20 kW diesel, trailer mount (used is fine) | $6-15k |
| Wire | 5 km of 10-12 AWG insulated stranded wire on two powered reels, ATV or truck-bed payout | $3-5k |
| Return electrodes | 2 x 10 steel stakes, aluminium foil pits, salt + bentonite, insulated boxes with interlock | $0.5-1k |
| Casing clamp | Heavy cable clamp + magnetic shoe + stainless band, wire-brush pad, 4-wire contact-resistance check | $0.1-0.3k |
| Isolation kit | Lock-out/tag-out set, clamp-on ammeter, insulation tester (to confirm the pump circuit is isolated) | $0.5-1k |
| TEM | 100 x 100 m loop (400 m wire), small air-core dB/dt coil, uses the node ADC or a P03 coil-set channel | $1.5-3k |
| Safety | Warning signs, temporary fencing for the stake areas, radios | $0.5k |
| Trailer | 12 ft utility trailer | $3-4k |
| **Kit total** | | **$22-38k** |

### 2c. Deployment

**Mode A, casing (private ranch, same day as a Sentinel visit).**
1. Pick 2-4 steel-cased wells on the ranch. Prefer windmill, solar or idle wells with no grid power. For grid-powered pumps, lock out the breaker and check with the insulation tester that the pump ground bond does not carry our current into the house ground. If it does, skip the well.
2. Clamp onto clean steel at the wellhead. Check contact resistance.
3. Lay 2-5 km of return wire along a ranch track to a stake cluster or to a second steel-cased well (casing-to-casing gives the lowest resistance: 20 A at under 100 V).
4. Transmit 2-4 hours per well with orthogonal codes. P03 nodes on the ranch and on nearby BLM land record.
5. Crew: 2 people, about 1 day for 2-4 wells. Cost about **$1.5-2.5k per ranch** (labour, fuel, consumables).

**Mode B, carpet (any land; source on private or state land where possible).**
- 2-3 dipole set-ups per 5 x 5 km carpet for IP (1-1.5 km lines along roads), 1-2 far set-ups at 6-8 km for CSAMT, plus 3-4 TEM loops per day.
- Crew: 2 people, about 2-3 days per carpet. About **$3-6k per carpet** on top of the P03 node cost, or about $120-240 per km².

**Mode C, pipeline CP.**
- One visit per rectifier with the operator's CP technician to fit our interrupter. It runs for 1-4 weeks while a P03 carpet is out. Cost about **$0.5-1k per rectifier** (our time) plus the stray-current report we owe the operator.

### 2d. Data path
The transmitter logs its true current waveform with GPS time. Nodes are GPS-timed and know the code seeds. Each node cross-correlates its E legs against each code on board, and sends a quick-look impulse response by LoRa for QC. Full data are picked up with the nodes. The inversion is a joint 3D DC/IP + CSAMT + MT + TEM fit (SimPEG can do casing, DC/IP, TEM and MT; Heagy and Oldenburg 2019 modelled steel casings in SimPEG, Computers & Geosciences; from memory, unverified). Outputs feed THERMOS-B as: plume bearing with uncertainty, lid thickness with uncertainty, and a per-conductor class probability (clay cap / playa clay / brine / resistive).

---

## 3. How much it shrinks the model's ranked uncertainties (estimates, untested)

| Rank | What changes | Rough size |
|---|---|---|
| **4 Reliability per mask class** | The shared "conductive" false-positive class splits into clay and brine. Clay-vs-brine likelihood ratio rises from about 2-3x to about 6-10x. If about 30-50% of conductive anomaly cells are brine (unverified), that share of follow-up money is not wasted. It also lets the 20/40 calibration campaign fit E-MT reliability per class instead of one blurred number. | VOI swing from this class cut by about a third (estimate) |
| **3 Lid and cap thickness** | Loop TEM removes static shift. Casing/stake DC sees the base of a resistive lid over a conductive tongue. | Depth bias from about ±20-40% to about ±10%; lid-thickness spread down about 30-50% in carpeted cells |
| **6 Upflow location** | Casing/stake source gives bearing along the tongue; heads give the gradient direction. Two independent directions. | Bearing from about ±45-60° to ±15-25° where it works (about 50-60% of outflow cases, my guess). Upflow search area down about 2-3x |
| **7 Conductive background** | CP and CSAMT sources give regional deep conductivity cheaply | Small |
| **1 Detection gap** | Indirect. Better mask-class split makes two-detector agreement (Sentinel + E-MT) more identifiable | Small, through rank 4 |
| 2, 5, 8, 9 | Not addressed | None |

Overlap warning: P03 already claims the IP split (rank 4). P18 is the hardware that makes that claim real. Do not count the rank-4 gain twice. P18's own new gain is the casing/plume bearing, the static-shift fix and the CP cost scale.

---

## 4. Rights edge
- **Private land needs no filing.** The transmitter, wire and electrodes stay on the ranch we are optioning. Current flows under neighbouring BLM land, where P03 nodes sit as casual use under IM 2026-024. That keeps the "active" part of the survey off federal land, which is the main grey area V01 and P03 flagged.
- **Same visit as the option.** The casing mode runs on the same day as the Sentinel visit, so a ranch's bearing and clay/brine class are known before we pay option money beyond the first $1-2/ac.
- **Stops spending on brine valleys.** The main saving is not rights money (cheap anyway). It is the follow-up spend (darts, carpets, slim holes at $0.3-1M) that would otherwise chase a brine conductor.
- **Pipeline deals.** A CP data swap gives a reason to talk with pipeline operators, who also hold rights of way over large private land. Small, but real.

---

## 5. Risks
1. **Many ranch wells are PVC-cased.** Newer stock wells often use plastic casing (unverified). Mode A then falls back to a wellhead stake, which the sim says is nearly as good for shallow tongues.
2. **Pump and house grounding.** Grid-powered pumps bond the casing to the house ground. Current can then leak into the building ground. Mitigation: lock-out, isolation test, skip if bonded. This needs a written safety procedure and maybe an electrician on the first jobs.
3. **Electrical safety.** Up to 800 V at the far stakes. Step-voltage zones must be fenced and attended. Insurance cost is unknown.
4. **The casing gain is modest.** The sim says it doubles the anomaly only for deep tongues under resistive lids. If most target outflows are shallow, Mode A adds little over a stake.
5. **Cultural noise.** Fences, pipelines and power lines channel current and give false bearings. Joint inversion of several sources and fence mapping are needed.
6. **CP operators may say no.** Changing rectifier behaviour touches compliance. Upside only; the plan does not depend on it.
7. **BLM field offices** may still call a grounded transmitter on federal land "not casual use". Mitigation: keep sources on private or state land.
8. **Lake and playa clay are still chargeable.** IP removes the brine trap, not the playa-clay trap. That one needs temperature or geochemistry.

---

## 6. Prior art (from memory, unverified unless noted)
- **Mise-à-la-masse and casing sources.** "Fluid flow tomography" at Japanese geothermal fields used a production well casing as the current electrode (Ushijima and Mizunaga, Kyushu University, 1990s-2000s). Rucker and co-workers used well casings as "long electrodes" for 3D resistivity at Hanford (Geophysics, about 2010). Heagy and Oldenburg (2019) and Yang, Oldenburg and Heagy (2016) modelled steel-cased wells for DC and EM.
- **IP for clay caps.** Lévy et al. 2018 and 2019 (GJI) at Krafla; Revil's normalised-chargeability work.
- **Coded sources.** MTEM (Ziolkowski et al. 2007); WFEM 2^n sequences (He Jishan).
- **Static shift by TEM.** Sternberg, Washburne and Pellerin 1988, Geophysics 53:1459.
- **Distributed DC/IP + MT.** Quantec Titan-24 and ORION 3D; DIAS32 (mining).
- **Zanskar** does not, to our knowledge, run controlled-source surveys on private ranch wells (M13, M32; unverified).

---

## 7. First test (8-14 weeks, about $40-60k including the kit)
1. **Weeks 0-8: build and bench.** Build the transmitter. Run 10-20 A coded into a dummy load and a test field. Pass: current waveform matches the code to better than 0.5%; GPS timing to better than 1 µs.
2. **Weeks 6-10: desk pre-registration.** Pick a site with a mapped shallow outflow plume and several steel-cased private wells. Candidates: **Lightning Dock (NM)**, whose outflow is mapped by many shallow wells, or **Raft River (ID)** (unverified that suitable steel casings exist). Write down the predicted bearing from heads and from published maps before going out.
3. **Weeks 10-14: field.** 30 P03 nodes on a 250 m grid. Mode A on 3 casings plus 3 wellhead stakes. Mode B: 2 IP set-ups, 1 CSAMT set-up, 6 TEM loops. Also run IP over one known brine valley and one known clay-cap system.
4. **Pass marks.** (a) Casing/stake bearing within ±25° of the mapped plume axis on at least 2 of 3 wells. (b) Mn/sigma separates the known brine conductor from the known clay cap by at least 3x. (c) TEM-corrected MT cap depth matches well data to ±15%.
5. **Kill.** Bearing error >45° on all wells and IP class overlap >50%. Then drop Modes A and B and fall back to P03 natural-field MT only.

---

## Files
- `P18_casing_sim.py`: 3D finite-volume DC solver, casing vs stake over a cold lid + warm saline tongue. Run `python3 -I P18_casing_sim.py [lid_base plume_top plume_base rho_lid casing_L conductance_scale]`.
