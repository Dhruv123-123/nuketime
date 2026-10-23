# P05: Pump-Cycle Mixing Sampler, an irrigation-well autosampler that turns one well into a mixing line

Date: 23 Oct 2026. Build candidate P05, model track. This builds on `../MODEL.md` (SENTINEL-COX, THERMOS-B, ranked uncertainties), `M07-geochem-databases.md` (leak tracers B, Li, Cl, SiO2, 3He; NURE silica loss; Gabbs Valley 32 C wells with chalcedony >110 C), `../../evidence/L15-geochem.md` (Fournier 1977, Giggenbach, GeoT, NMFk), `M23-hydrology-masking.md` (masks, 3-30 km outflow plumes), `M30-permeability.md` (specific capacity), `P01-ranch-well-sentinel-2-0-a-resident-well-.md` (resident string, pump-current clamp, pump-pull hook) and `P04-wellhead-clamp-fleet-no-entry-discharge-.md` (gauge-port tee, discharge T error budget, acoustic sounder, pump-efficiency hook). It does not repeat them.

**Method note.** The shared web search budget for this workflow turn was already used up when this agent ran. Both searches I tried were refused. No new web pages were read. Facts from repo files are cited by file. Standard literature I know is marked (from memory, unverified). Prices are my estimates (unverified). Numbers I computed are marked (calc). The Monte Carlo script is `P05_mixing_mc.py` in this folder.

## Bottom line

Build it, but as a **module that bolts onto the P04 gauge-port tee and the P01 resident node**, not as a separate product. And change the brief in four ways.

1. **The mixing signal mostly does not come from one pump cycle.** Deep warm water that has to leak up through a clay layer takes years to arrive, not hours (calc in 1b). Inside one cycle the mix changes only when the warm water enters through a fast path: a fracture or fault in the open interval, a warm gravel zone whose share shifts as drawdown grows, or warm water that rose up the idle borehole. So sample on three time scales: **first flush** (the water that sat in the casing while idle), **in-cycle** (log-time), and **season** (weekly, as regional drawdown deepens). The season trend is where most wells will show their spread.
2. **Recovery gives no chemistry.** When the pump is off, nothing comes out of the discharge. Recovery gives the free Theis recovery test (water level only). Chemistry is collected during pumping, plus the first-flush bottle on the next start.
3. **Continuous T and EC are the real mixing curve. Bottles are the calibration knots.** A flow cell logs T (0.01 C), EC and pH every 30 s. That gives thousands of points on the mixing curve per cycle. The bottles (24-48 per season) only need to anchor the EC-to-Cl/B/Li/SiO2 relation at the corners of that curve. An adaptive trigger fires an extra bottle when dEC/dt or dT/dt changes.
4. **Use several neighbour wells, not one.** Three to five wells in one basin, screened at different depths, give a spatial mixing line with a much bigger spread of warm fraction than any single well's time series. The Monte Carlo below shows that spread is what buys precision.

**Numbers.** BOM about **$900-1,400** per unit at 10 units, about $650-950 at 100 (unverified). Install about 1.5-2 crew-hours on the option visit (2 people), plus a 30-45 min carousel swap every 3-4 weeks. Lab cost per bottle about $40-80 commercial (ICP-OES cations plus Si, B, Li, plus IC anions; unverified), about $8-15 in our own lab at volume (unverified). All-in about **$2.5-5k per well-season** commercial lab, about $1.5-2.5k with our own lab.

**What it buys (my estimates, unverified).** At an instrumented warm well, the deep end-member temperature goes from a single-sample geothermometer that reads 58-88 C for a 150 C source (badly low, calc) to a mixing-line estimate of **+/-4 C** (1 sigma) when the warm fraction swings 4x, **+/-13 C** when it barely moves, versus **+/-20 C** from one sample plus one cold-well sample (calc, 1c). Model-wide, a 50-150 well program cuts rank 5 (T at 0.5-2 km) variance by about 20-35% in the instrumented basins and 5-10% program-wide. It adds a little to rank 2 (free pumping test, about 5% on top of P01/P04) and rank 3 (about 5-10%; a flat fraction is weak evidence). It does almost nothing for rank 1 by itself, because it only goes on wells we already flagged as warm.

## 1. Physics

### 1a. Why a mixing line beats a single bottle
- **Single-sample geothermometers fail on mixed water.** A 7.5% share of 150 C quartz-equilibrated water (SiO2 about 125 mg/L) in 15 C water with 30 mg/L SiO2 gives a mixed sample of about 37 mg/L. Read as one sample, chalcedony says 58 C and quartz says 88 C (calc, `P05_mixing_mc.py`). The real source is 150 C. Cation geothermometers fail the same way, because Mg from the cold water swamps them (Giggenbach 1988, from memory). This is why M07 lists mixing correction as the first fix for public chemistry.
- **Fournier silica-enthalpy mixing model.** If the deep water keeps its silica and heat on the way up, every mixed sample sits on a straight line between the cold point and the deep point in silica-versus-enthalpy space. Extend the line from the cold point until it hits the quartz solubility curve. That crossing is the deep temperature (Fournier 1977, Geothermics 5:41-50, https://doi.org/10.1016/0375-6505(77)90007-4; Truesdell and Fournier 1977, USGS J. Research 5:49-52, from memory, unverified). The same idea runs with Cl, B or Li as the mixing coordinate. These are conservative: they do not drop out or re-equilibrate. So they give each sample's warm fraction x, and test whether T and SiO2 really move on the same line.
- **What the time series adds.** One mixed sample plus one cold-well sample already defines a line. The series adds three things. (1) It fixes the cold end-member from the intercept of many points instead of one separate cold well, which is the largest error term. (2) It averages lab and natural scatter. (3) It tests the model: if T, SiO2, Cl, B and Li all line up with one x per sample, the two-end-member model holds. If T falls below the Cl-implied line, heat was lost on the way up (see 1d).
- **Signal size at 5% warm fraction (calc).** Deep water 150 C, Cl 500, B 5, Li 1 mg/L; cold water 15 C, Cl 20, B 0.1, Li 0.02 mg/L (typical Basin and Range values, unverified). The mix reads T 21.8 C, Cl 44, B 0.35, Li 0.07, SiO2 34.7. Cl doubles, B triples and Li triples. All are far above lab precision (2-5%). So **5-20% warm fractions are easy to see in conservative tracers**. The hard part is not detection. It is the lever arm for extrapolating to the deep end.

### 1b. What changes the mix during pumping (calc)
- **Leaky-aquifer timescale.** For a confined aquifer under a leaky clay (Hantush and Jacob 1955, from memory), the share of pumped water that comes from leakage rises on a time scale of about S B^2 / T. With S = 1e-4, T = 500 m2/d and leakage factor B = 1,000 m, that is about 0.2 days. So hydraulically the leakage share does rise within one cycle.
- **But the leaking water is the clay's own water at first.** With aquitard thickness 20 m, K' = b'T/B^2 = 0.01 m/d, a gradient of 5 m over 20 m, and porosity 0.3, deep water needs about **2,400 days** to cross the clay (calc). So diffuse leakage through a lid does not deliver new deep water in one cycle, or even one season.
- **Fast paths that do change the mix in a cycle:**
  - A fault or fracture in the open interval that carries warm water. Its share follows drawdown and is fast.
  - Several screened zones with different temperatures. As pumping level falls, the upper zones give less (or dewater in unconfined wells) and the deeper zones give more.
  - **Ambient borehole flow while idle.** A deep warm zone at higher head flows up the casing and out into a shallow zone while the pump is off. The first 30-120 s of pumping then brings out warmer, saltier water than the steady mix. That first-flush bottle is a cheap, sharp signal (the logic is the same as USGS depth-dependent sampling and well-bore flow logging, e.g. Izbicki and co-workers in California; from memory, unverified).
- **How far the pumped water comes from.** A big irrigation well (about 16,000 m3/d, 100 days, 100 m screen, porosity 0.25) only empties a cylinder of about **140 m radius** in a season (calc). The pressure cone reaches much farther (about 120 m after 1 day and about 670 m after 30 days in an unconfined aquifer with T = 1,000 m2/d, Sy = 0.15; calc). So the water samples a near-field zone, while the cone tells us the hydraulics of a larger area. This weakens the brief's claim that a flat fraction "means the source lies beyond the cone". A flat fraction more often means a fixed-geometry inflow (one fracture with a steady share). Treat it as weak evidence for a lid or distance, not strong.
- **Season-scale change is the bigger lever.** Regional drawdown through an irrigation season can be 3-20 m (unverified, basin dependent). That re-weights zones and fault inflow much more than one cycle does. Weekly bottles through the season catch it.

### 1c. Monte Carlo: how precise is the deep temperature? (calc, `P05_mixing_mc.py`)
Setup: deep 150 C quartz water, cold 15 C with 30 mg/L SiO2. Noise: lab 2% on SiO2 and Cl, 0.05 C on T, and natural cold-water scatter of +/-1.5 mg/L SiO2, +/-5% Cl and +/-0.3 C between samples. 2,000 runs each. Result is the median and the 16-84% band of the deep temperature.

| Sampling | Median T_deep | 1 sigma band |
|---|---|---|
| One mixed sample + one cold-well sample, x = 7.5% | 150 C | 130-169 C (+/-20) |
| 30 samples, flat x = 7.5% | 150 C | 137-164 C (+/-13) |
| 30 samples, x swings 5-10% | 150 C | 137-163 C (+/-13) |
| 30 samples, x swings 5-20% | 150 C | 146-154 C (+/-4) |
| 30 samples, x swings 2-5% | 149 C | 126-172 C (+/-23) |
| One sample, 30% of excess heat lost on the way up | 177 C | 150-204 C |
| 30 samples, x 5-20%, 30% heat lost | 178 C | 172-183 C |

What this says:
- **A 2x swing in x is not enough. A 4x swing is.** The brief's "about 30 points gives a mixing line" is right only when the warm fraction moves a lot. Neighbour wells (spatial line) and the season trend are how we get that spread.
- **Repeat sampling alone still helps** (+/-20 to +/-13 C), mainly by averaging the cold end-member.
- **Heat loss on the way up biases the answer high, and tight.** That is the dangerous case: precise and wrong. The fix is a second, heat-independent constraint (1d).

### 1d. Guarding against heat loss and silica re-equilibration
- **Cation end-member extrapolation.** Fit Na, K, Mg and Ca against Cl across the series. Extend each line to the same deep end and run Na-K and K-Mg (Giggenbach 1988) on the extrapolated deep water. This uses no temperature or enthalpy. If it agrees with the silica-enthalpy answer, heat loss is small. If silica-enthalpy reads high, use the silica-chloride form instead (deep SiO2 from the SiO2-Cl line at a Cl set by the cation fit). Under-sampled Mg is the weak point (Mg is near detection in the deep end), so the K-Mg extrapolation is noisy (unverified).
- **Silica can re-equilibrate in a cold aquifer** over months to years toward chalcedony. That pulls the mixed silica down and biases T_deep low (conservative). The fast-path waters this sampler is best at seeing (fracture inflow, first flush) have the shortest residence time, so they are least affected.
- **Heat loss is itself a signal.** The gap between the T line and the Cl line gives the share of excess heat lost. A big loss means slow travel through a conductive lid, which feeds rank 3 (lid present) and rank 6 (source not under the well).

### 1e. The free pumping test
- The pump-current clamp gives exact on/off times and an amperage proxy for Q. The P04 clamp-on flowmeter or pump curve gives Q itself. A water-level sensor gives drawdown. Cooper-Jacob on the drawdown and Theis recovery after shut-off give transmissivity T. Late-time flattening gives the leakage factor B (Hantush). These are standard (from memory).
- **Joint fit is the new part.** The hydraulic leakage curve says how much water comes from leakage and when. The chemistry says what that water is. Together they give a leakage rate times a deep end-member composition, which is a rough upflow flux of heat and solutes near the well. That is a direct, if local, number for rank 2 (flow) and rank 3 (lid). I know of no published joint inversion of an irrigation pumping test with hydrochemistry for geothermal (unverified). Integral pumping tests for contaminant plumes use the same idea of reading concentration through time while the capture zone grows (Bayer-Raich, Ptak and Teutsch, from memory, unverified).

## 2. Prior art
- **Mixing models:** Fournier 1977 (above); Truesdell and Fournier 1977 silica-enthalpy plot (from memory); Giggenbach 1988, GCA 52:2749 Na-K-Mg triangle (from memory); end-member mixing analysis (EMMA), Christophersen and Hooper 1992, WRR (from memory). All sit in L15.
- **Time-series chemistry in pumping wells:** contaminant hydrology does this routinely (integral pumping tests, nitrate and arsenic changing with pumping rate in public supply wells; from memory, unverified). I know of no geothermal exploration program that runs autosamplers on irrigation wells (unverified). Geothermal sampling of ranch wells is one-shot (M07, L15; Gabbs Valley in M03).
- **Commercial autosamplers:** Teledyne ISCO 6712 and Hach AS950 (24 bottles, peristaltic, about $5-10k each, from memory, unverified). They are built for storm water. They are too costly for a fleet and do not need a peristaltic pump here, because the well discharge is already pressurized.
- **Noble gases:** copper tube sampling (Weiss 1968, from memory) and passive diffusion samplers (Gardner and Solomon 2009, from memory, unverified). Crimping copper tubes automatically is not practical in v1, so the crew does it by hand.
- **Repo:** P04 gives the gauge-port tee and the discharge T error budget. P01 gives the resident node and the pump-current clamp. This module reuses both.

## 3. v1 design

### 3a. Layout
- **Tap.** A 1/2" NPT tee on the P04 gauge port or sample bib, so the rancher's gauge stays. Brass ball valve, then a 30-60 psi pressure regulator, then a 100 micron Y-strainer.
- **Flow cell.** About 250 mL acrylic or PVC cell with the 0.01 C glass-bead thermistor (shared with P04), a K=1 EC probe, a pH probe and a slot for a passive He diffusion sampler. A constant bleed of about 0.2-0.5 L/min runs through the cell and out a drain hose. This keeps the sensors at discharge temperature and the line fresh.
- **Sample path.** A 12 V latching solenoid valve (brass or 316 SS) after the cell. A 3-way valve sends the first 30 s to waste (purge), then turns to the carousel. A stepper-driven distribution arm (ISCO-style) rotates over 24 bottles of 125 mL HDPE in a ring about 45 cm across. Each bottle has a duckbill or float-valve cap so it seals when full and does not evaporate. Bottles are not acidified in the box. The lab splits and acidifies on return. Silica at under about 100 mg/L stays in solution in plain HDPE for weeks (unverified). Two carousels per site, so a swap is a lift-out and drop-in.
- **Water level.** Option A: a vented 0-30 m pressure transducer dropped down an existing sounding tube. Option B: the P04 acoustic sounder through the casing vent. Option C (no access): drawdown from discharge pressure plus pump curve (crude).
- **Trigger.** A split-core current clamp on one motor lead in the pump panel (no wiring change). The rancher or his electrician opens the panel. Pump-on starts the schedule.
- **Logger and comms.** ESP32-class board, 24-bit ADC for the thermistor, real-time clock, SD card, LTE-M/NB-IoT modem (about $3-5/month, unverified) sending 15-minute summaries and every bottle event. Satellite fallback (Swarm-class or similar, unverified availability) only where there is no cell signal.
- **Power.** Logging plus modem about 0.3-0.6 W average. Solenoid (latching) and stepper draw only during sampling, about 5-10 Wh per bottle event at most. A 20 W panel plus a 12 V 12 Ah LiFePO4 gives more than 5 days of autonomy (calc).
- **Box.** A 60 x 45 x 45 cm rotomolded case (cooler-style for thermal mass), about 18-22 kg loaded, strapped to the pump pad or a ground screw. White lid, vents with screens, lock. Bottles shaded inside.

### 3b. Schedule (24 bottles per carousel, 48 per season with one swap)
- **First flush:** bottle at 0-30 s after pump start on the first cycle after install and once a month after (borehole-flow signal).
- **In-cycle log-time:** 2, 10, 30 min, 2 h, 8 h, 24 h, 3 d, then each 4 days while running.
- **Adaptive:** extra bottle when EC changes by more than 3% or T by more than 0.1 C from the last bottled value. Cap of 4 adaptive bottles per week.
- **Season:** at least one bottle a week.
- **Optional step test:** where the pump has a VFD, ask the rancher for one 3-step rate change (for example 60, 80, 100% for 4 hours each). Different rates re-weight inflow zones and widen the x spread.

### 3c. Parts list (prices at 10 units, unverified)

| Item | Example | Cost |
|---|---|---|
| Tee, ball valve, regulator, strainer, fittings | brass, hardware store | $60-90 |
| Flow cell, bleed drain hose | PVC/acrylic, machined or printed | $30-60 |
| 0.01 C thermistor and 24-bit ADC | glass bead + ADS1220 class (shared with P04) | $40-80 |
| EC probe and interface | K=1 probe + EZO-class board | $150-250 |
| pH probe and interface | lab-grade gel probe + board | $100-170 |
| Latching solenoid and 3-way purge valve | 12 V brass/SS | $60-120 |
| Carousel: stepper, arm, ring, 24 bottles x 2 | NEMA 17, printed parts, HDPE 125 mL | $90-160 |
| Water-level transducer (vented, 30 m) | low-cost vented sensor or acoustic | $150-400 |
| Current clamp | split-core 100-200 A | $20-40 |
| Logger, RTC, SD, LTE-M modem | ESP32 + cat-M module | $70-120 |
| Solar 20 W, LiFePO4 12 Ah, charger | | $90-140 |
| Case, mounts, locks, cabling | rotomolded case | $80-150 |
| **Total** | | **about $940-1,780; target $900-1,400** |

Consumables: He diffusion sampler about $50-150 each (unverified), 2 copper tubes per site per season by hand (about $20-40 each, plus noble-gas lab at about $300-600, unverified; run only on the top wells).

### 3d. Lab
- Per bottle: Cl, SO4, F, Br (IC); Na, K, Ca, Mg, Si, B, Li, Sr (ICP-OES); alkalinity. 18O/2H on a subset.
- Commercial: about $40-80 per bottle (unverified). Own lab: a used ICP-OES plus IC plus autosampler, about $80-150k capex (unverified), marginal about $8-15 per bottle at a few thousand bottles a year. The own lab pays back at roughly 2,000-3,000 bottles (calc on the unverified prices), which is 50-70 wells x 48 bottles. It also keeps the data private.

### 3e. Crew time
- Install on the option visit: 2 people, about 1.5-2 hours (tee, cell, transducer drop, clamp, box). The P04 survey and the drop probe run in the same visit.
- Swap: 1 person, 30-45 min every 3-4 weeks. Routes cover 6-10 wells a day in one basin.
- Season: about 10-14 crew-hours per well including travel share (unverified).

## 4. How it moves the model

Inputs to THERMOS-B per instrumented well: a posterior on deep end-member T (and its Cl, B, Li), heat-loss share, warm-fraction time series x(t), transmissivity T, leakage factor B, and a first-flush borehole-flow flag. Each enters as its own censored likelihood (mixing-model class, with a heat-loss nuisance).

| Rank | Effect (my estimates, unverified) |
|---|---|
| 5 T at 0.5-2 km | Biggest effect. Deep end-member T to about +/-4-13 C where it works, versus about +/-20 C for a careful one-shot pair and +/-40-60 C (and biased low) for naive single-sample geothermometers. Instrumented-basin variance on T(0.5-2 km) down about 20-35%; program-wide 5-10% at 50-150 wells. The geothermometer says reservoir temperature, not the depth, so it pairs with P01 profile curvature for depth. |
| 3 Masking and lid | Heat-loss share and the leakage factor are new, direct lid indicators. About 5-10% on rank 3 in instrumented basins. A flat x is weak evidence (see 1b). |
| 2 Permeability | Free pumping test, plus the joint leakage-flux estimate. About 5% on top of P01/P04, which already get specific capacity. |
| 6 Upflow location | The deep end-member's Cl/B/Li ratios are a fingerprint. Matching that fingerprint across wells in a basin traces the plume back to its source. With 3-5 wells per basin, maybe 10-20% tighter upflow location than T alone. |
| 4 Sensor reliability | Running it on known systems (Newcastle UT, Raft River ID, Gabbs Valley NV area irrigation wells) gives the mixing-class s/q directly. |
| 1 Detection gap | Small by itself, since it only goes on flagged warm wells. It can turn "warm but ambiguous" wells into a confirmed hidden source (a hit) or a false alarm, which sharpens P_det in the calibration set. |

The brief said rank 5, rank 2 and rank 3. I agree on rank 5. Ranks 2 and 3 move less than the brief hoped, and rank 6 moves more.

## 5. Rights edge
- **A real gift to the rancher: an irrigation water-quality report.** Boron is a crop toxin (sensitive crops show damage at about 0.5-1 mg/L, from memory, unverified). Chloride, EC and sodium (SAR) set salt damage. A season of B, Cl, SAR and EC trends, plus the P04 pump-efficiency numbers, is something irrigators normally pay for. It gives a second reason to sign the heat option, and to keep the box running.
- **Private data, not in any public file.** NWIS, NURE and state files hold one-shot samples (M07). A season of 30-50 bottles per well with mixing analysis is a private asset. It also tells us which optioned parcels to exercise or extend and which to drop, before money goes to darts or holes.
- **Signs on the same visit** as the drop probe and P04, so it adds no new rights cost.
- **Limit:** water rights, not heat rights, govern the well. We sample water the rancher already pumps, so no new appropriation (state rules vary, unverified). Disclosure of the data is ours to control under the option terms (H06, unverified).

## 6. Risks
- **Most wells may not swing enough.** If 70% of warm wells show x moving less than 2x over a season, precision is only about +/-13 C there (still better than one-shot). Neighbour wells are the hedge.
- **Heat loss gives precise wrong answers.** Mitigation: cation extrapolation cross-check, heat-loss share as a nuisance in the likelihood.
- **Silica re-equilibration** biases low (conservative).
- **Fouling and scale.** Carbonate or iron scale in the solenoid and cell; sand. Strainer, bleed flow, monthly cleaning.
- **Heat and sample storage.** Box interiors can reach 40-50 C in summer. Cl, B, Li, Na, K are stable; pH and alkalinity drift, so trust the in-line pH. Carbonate can precipitate and take some Ca.
- **Rancher and electrical access.** Opening a pump panel for the clamp needs the owner (or an electrician). Some will refuse.
- **Lab turnaround and cost** before our own lab exists.
- **Overlap with P01/P04.** As a standalone product it is "too small"; as a module on them it is not.

## 7. First test
1. **Desk, 2 weeks, about $0.** Pull WQP/NWIS wells with 5 or more repeat samples in Basin and Range warm-well areas. Measure how much Cl, B and SiO2 vary over time in each well. That gives the real distribution of x swing and tells us if the 4x case is common. Also run the neighbour-well spatial mixing line on existing NBMG/NURE points around Gabbs Valley.
2. **Bench, 3 weeks, about $3k.** Build 2 units. Bench-test with two tanks (hot salty and cold fresh) mixed through a valve on a schedule. Check bottle stability at 45 C for 4 weeks.
3. **Field, 6-8 weeks, about $8-15k.** Put 2-4 units on irrigation wells near a known system with a known reservoir temperature: Newcastle (UT) or Raft River (ID) are the first picks, plus one cold control well. Pass if the mixing-line deep T falls within +/-15 C of the known reservoir temperature, and the cold control gives no false deep end-member.
