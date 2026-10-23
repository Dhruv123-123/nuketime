# P04: Wellhead Clamp fleet, a no-entry discharge temperature, flow and pump-state survey

Date: 23 Oct 2026. Build candidate P04, model track. This builds on `../MODEL.md` (SENTINEL-COX, THERMOS-B likelihood classes, ranked uncertainties), `M06-water-well-temperature.md` (146,235 NDWR driller reports, 9.8% with a temperature, 697 isolated warm wells, driller discharge sigma 2-5 C), `M23-hydrology-masking.md` (four masks, outflow plumes 3-30 km), `M30-permeability.md` (specific capacity to transmissivity), `P01-ranch-well-sentinel-2-0-a-resident-well-.md` (the resident Sentinel, which already names a pump-current clamp and a clamp-on flowmeter as sub-parts), and `../../../hardware/evidence/H06-water-well-landman.md` (drop probe, $1-2/ac option, SRHA trap, the "30% loggable" kill line). It does not repeat them.

**Method note.** The shared web search budget for this workflow turn was used up before this agent ran. All three searches I tried were refused. So no new web pages were read. Facts from repo files are cited by file. Facts from standard literature I know are marked (from memory, unverified). All prices are my own estimates and are (unverified). The heat-transfer numbers below are my own calculations, marked (calc).

## Bottom line

Build it. It is the cheapest way to put a real, dated, GPS-tied temperature on thousands of wells that have none, and it works on exactly the wells the drop probe cannot enter. Three changes make it better than the brief.

1. **Use the gauge port when there is one.** Most irrigation discharge heads carry a 1/4" or 1/2" NPT pressure-gauge tap, an air-release valve or a sample bib (unverified share, my guess 50-80%). Screwing a small immersion thermistor plus pressure transducer into that tap (with a tee, so the rancher's gauge stays) gives a 0.01-0.02 C reading with no well entry. The strap-on sensor is the fallback. On steel pipe it is already good to about 0.02-0.05 C (calc below). On PVC it needs a second sensor to correct heat leak and is good to about 0.1-0.3 C.
2. **Add an acoustic water-level sounder.** An echo sounder fires a sound pulse down the casing vent or a 1/2" port and times the echo off the water surface. Nothing enters the well. With the clamp's Q, it turns every visit into a specific-capacity test (drawdown between pump-off static and pump-on pumping level). That moves rank 2, not just ranks 1 and 6.
3. **Sell it as a free pump-efficiency test, and sign the heat option on the same visit.** Wire-to-water efficiency needs Q, discharge pressure, pumping water level and input kW. The kit measures all four. Utility-funded pump-test programmes exist in the West, such as the California Advanced Pumping Efficiency Program (APEP) and Pacific Northwest utility irrigation programmes (from memory, unverified), so farmers already know this test has value (about $150-400 retail, unverified). Our measurement of the temperature rise across the pump also uses the old thermodynamic method of pump testing (ISO 5198, from memory, unverified), so the heat-sensor and the rancher's product are the same physics.

**Numbers.** Handheld kit BOM about $5-9k. Two-person crew, 20-40 wells per crew-day in season. Marginal cost about $10-30 per well for a temperature-only pass, about $60-150 with a lab panel on flagged wells. A resident node is about $60-150 BOM (strap RTD pair + current clamp + LTE-M modem) or about $500-900 with a permanent clamp-on flowmeter and EC cell (all unverified). My estimate is that one season of 2-3 crews (about 6,000-12,000 wells across NV, UT, ID, OR, NM) adds 5-10x more temperature-observed 500 m cells than the Sentinel plan alone, cuts the rank 1 detection-gap band on N by about 15-30% (on top of the Sentinel plan), cuts rank 6 upflow-location error in instrumented basins from about +/-5-10 km to about +/-1-3 km, and removes the +/-400-800 m TRS error for every well it touches (rank 7). It is also the triage that tells us which 5-10% of wells earn a full Sentinel.

## 1. Physics: why a discharge temperature is a real reading

### 1a. What the pumped water is
- **Flow-weighted mix.** Pumped water is a mix of every inflow zone in the open interval. T_pump = sum(Q_i T_i) / sum(Q_i). It is not a profile, but it is a clean, well-defined average. The weights follow transmissivity of each screened layer, which the driller lithology log lets us guess (gravel high, clay low).
- **Depth it senses.** The open interval of irrigation wells is about 30-400 m (H06, unverified). So the clamp senses the top 0.1-0.4 km. It does not see the 0.5-3 km target directly. It sees outflow plumes and conductive halos that reach that depth.
- **What a blind system looks like at that depth.** Outflow tongues from blind systems run 3-30 km downhill along permeable layers (M23). The Play Fairway gradient holes at Gabbs Valley read 124 C at about 500 ft and Granite Springs 95 C (H06, citing UNR). Newcastle, Utah was found by irrigation wells, with a plume in an 85-95 m aquifer (M06). Raft River was found by irrigation wells in the 1950s (H06, unverified detail). Zanskar's review credits water wells with "more than a third of known blind or hidden systems" (M06). So excess temperatures of 5-60 C at 50-300 m are the signal class, and the plume tails at 1-5 C excess are where many wells are needed.

### 1b. Sensor error budget (calc)
Strap-on sensor under foam. The sensor reads the outer pipe wall. The wall sits between the water (strong coupling) and the air through the foam (weak coupling). The error is roughly (T_air - T_water) x (R_in + R_wall) / R_total.
- Inner convection, 8" pipe at 1.5 m/s: Re about 3e5, Nu about 1,200 (Dittus-Boelter), h about 3,600 W/m2/K, so R_in about 2.8e-4 m2K/W.
- **Steel wall** 8 mm: R_wall about 1.6e-4. Foam 50 mm closed-cell (k 0.035) plus outside film: R_out about 1.5. Error fraction about 3e-4. With 30 C between a sun-heated jacket and 15 C water, the bias is **about 0.01 C**. Axial conduction from bare pipe outside the foam dies off in about 1 cm, because the water holds the wall so tightly. So a 300 mm foam sleeve is plenty. **Steel accuracy is set by the RTD calibration, about +/-0.02-0.05 C.**
- **PVC wall** 10 mm (k 0.19): R_wall about 0.053. Error fraction about 3.5%. With 30 C between air and water, the bias is **about 1 C** uncorrected. Fix: a second sensor on the outside of the foam gives the heat flux, and the known R_wall/R_foam ratio removes about 85-90% of the bias. Residual about +/-0.1-0.3 C. Doubling the foam to 100 mm halves it again. Mark PVC readings as a lower-quality class in the likelihood.
- **Prior art for the two-sensor method.** Commercial "non-invasive" process thermometers use the same two-sensor heat-flux correction to replace thermowells (ABB NINVA / TSP341-N, Endress+Hauser iTHERM SurfaceLine; from memory, unverified).
- **Immersion via gauge port:** a 3 mm glass-bead thermistor in the flow. Accuracy +/-0.01-0.02 C after bath calibration. No heat-leak problem.

Pump and riser corrections. These are real physics, not noise, and the kit measures what is needed to remove them.
- **Pump heating.** All electrical input that does not become lift or pressure becomes heat in the water. Delta-T = g H (1/eta - 1) / c_w. At TDH 120 m and wire-to-water efficiency 0.6, delta-T is about **0.19 C**. At efficiency 0.45 it is about 0.34 C (calc). With measured kW, Q and head, the correction is good to about +/-0.03-0.05 C. For a line-shaft turbine the motor sits at the surface, so only pump and column losses heat the water.
- **Riser exchange.** Water climbs the column in about 1-3 min. For a 50 L/s irrigation well the thermal mass flow is about 200 kW/K and exchange with the annulus is about 30 kW/K at most, so the bias is under about 0.1-0.2 C at start and decays as the annulus equilibrates (calc, rough). For a 0.5 L/s solar stock well the water nearly equilibrates with the upper column and surface pipe, so stock-well readings can be biased by 1-3 C toward shallow temperature. They need their own quality class.
- **Wait time.** Read after the pump has run 30+ minutes. Irrigation wells run for days in season, so most visits catch a steady state.

### 1c. The residual, and what limits detection
- **Expected cold temperature.** T_exp = MAAT + ground-surface offset (about 1-3 C) + Gamma_bg x z_eff, where z_eff is the transmissivity-weighted mid-depth of the NDWR screen interval.
- **Noise of the residual.** MAAT and offset about +/-1 C. Background gradient in valley fill about 30 +/- 15 C/km, so about +/-1.5-2 C at 120 m. Recharge cooling near range fronts, and pump-history drift, add more. Total model-side sigma is **about 1.5-2.5 C per well** (my judgement). The measurement error (0.02-0.3 C) is now small next to this.
- **Compared to what we have now.** The driller value is sigma 2-5 C with gross errors and a date decades old (M06, MODEL.md L1). And 90% of NDWR wells have no temperature at all (M06). So the main gain is not precision per well. It is **new coverage**, dated, GPS-located and with known pump state.
- **Single-well detection limit.** A residual above about 4-5 C (2 sigma) flags a well. Outflow cores (10-60 C excess) are easy. Plume tails at 1-3 C need many wells along a flow line.
- **Spatial stacking.** Along a head gradient, a plume decays roughly as exp(-x/L), with L about 3-30 km (M23). Ten wells spaced 1-3 km along the flow path, each at sigma 2 C, fit the source position to about +/-1-3 km and the source excess to about +/-30% (calc, simple least squares on an exponential). This is the rank 6 back-projection.

### 1d. The time signals (the "vertical-connection hint")
- **Start transient.** The first 1-3 minutes purge the column. Then the reading moves from wellbore storage water to aquifer water. Then, over minutes to hours, it trends.
- **What the trend means.** A rise in T with log time means pumping is pulling more water from a deeper, warmer zone or along a leaky fault (vertical connection). A fall means cold lateral or shallow recharge is being drawn in. This is the "heat as a tracer" idea (Anderson 2005, Ground Water 43:951; Saar 2011, Hydrogeology Journal 19:31; from memory, unverified). It is a hint, not a fit, because the drawdown field is unknown.
- **Season trend (resident node only).** Over 100+ days of pumping, a well near an outflow plume can drift by 0.1-1 C as the capture zone grows into warmer or colder water (unverified magnitude). The direction tells which side of the plume the well sits on.
- **Rank 2 from the acoustic sounder.** Static and pumping water levels plus Q give specific capacity Q/s. Transmissivity is about 1.2-1.5 x Q/s (M30). One dated, measured value per well replaces the driller's rounded completion number.

## 2. v1 design

### 2a. Handheld kit "Clamp-H" (one per two-person crew)

| Part | Spec | Est. price (unverified) |
|---|---|---|
| Strap sensor pair | Two 4-wire PT1000 Class AA thin-film RTDs (or bath-calibrated 10k NTC), one in a copper shoe with thermal pad on the pipe, one on the foam outside. Ratchet band for 2-16" pipe. 300 mm x 50 mm closed-cell foam sleeve with a reflective Velcro jacket | $120-250 |
| Gauge-port probe | 1/4" and 1/2" NPT tee, 3 mm glass-bead thermistor immersed in flow, 0-300 psi transducer, rancher's gauge refitted on the tee | $150-300 |
| Readout | 24-bit ADC (ADS1220 class) with ratiometric reference resistor, Bluetooth to tablet | $80-150 |
| Clamp-on ultrasonic flowmeter | Transit-time, 2-24" pipe, steel/PVC/aluminium. Mid-tier portable. Field accuracy about +/-2-5% on a good straight run | $1,000-3,000 |
| Power reading | Optical pulse reader for the utility meter LED (gives kW with no panel work), plus a 3-phase split-core current clamp set as backup for on/off and current | $150-500 |
| Acoustic sounder | Echo water-level sounder for the casing vent or a 1/2" port | $1,500-3,000 |
| EC tee | Hose-bib adapter with a flow-through cell: 4-electrode EC plus thermistor | $200-400 |
| Sample kit | Filtered SiO2, cations (Na, K, Ca, Mg, Li, B), anions (Cl, SO4, HCO3) bottles, cooler | $10-20 per sample |
| Tablet app | GPS (phone-grade, +/-5 m), nameplate photo OCR, NDWR log match, QR tag for the well, option e-sign | $500 |
| Calibration | Stirred bath with reference thermometer, shared across kits | $1,500 (one-off) |

Handheld kit total: about **$5-9k**. Tools at low end (cheap TUF-2000-class flow modules, from memory) can get it to about $3k.

**Crew time per well.** Drive 5-15 min in a farmed valley. Set up 5-10 min (strap or port, flow clamp, meter reader, sounder). Read 10-15 min while the pump has already run 30+ min. Sample 5 min if flagged. Pack 5 min. **About 25-45 min door to door, so 15-25 wells per 10-hour day for full kits, 30-40 for temperature-plus-flow only.** If a pump is off, we ask the owner to start it and pay the power (about $5-20, unverified), then come back in 30 min.

**Season.** Irrigation wells run about May-September. At any given time perhaps 50-70% are on (pivots cycle; unverified). Stock and solar wells run in daylight all year. So a crew gets about 120 good field days a year.

### 2b. Resident node "Clamp-R"
- **Base (about $60-150 BOM).** Strap RTD pair, one current clamp (pump on/off and load), nRF9160-class LTE-M modem with GNSS, 3 W solar panel, 6 Ah LiFePO4, IP67 box zip-tied to the discharge head. Samples every 1 min when the pump is on, every 15 min when off. About 20-50 kB/day. About $2-5 per month of data (unverified). Where there is no cell signal, a LoRa link to a ranch gateway or a satellite IoT modem (Iridium SBD class) adds about $100-250.
- **Full (about $500-900 BOM).** Adds a permanent clamp-on ultrasonic transducer pair with an OEM flow module, an inline EC cell on the sample bib and a pressure transducer on the gauge port. This is a season-long pump test, logged.
- **Install** 30-45 min. No well entry and no electrical panel work: the current clamp is non-contact and the power is solar. That keeps us away from licensed-electrician rules.
- **What it adds over Clamp-H.** Hundreds of start transients per season, the season drift, and the pump-efficiency dashboard that keeps the rancher happy for the life of the option.

### 2c. Deployment method
1. **Desk list.** Pull every NDWR (and UT, ID, OR, NM) irrigation, stock and municipal well with a usable screen interval. Rank by EVSI per dollar with the SENTINEL-COX prior. Strip SRHA and railroad-severed tracts using GLO patent types (H06).
2. **Basin sweep.** One crew sweeps a whole irrigated valley in 3-10 days. It does not cherry-pick: it visits a pre-registered stratified sample so the reading can enter the model as designed effort.
3. **Same-day product.** The farmer gets a one-page pump report (efficiency, kW per acre-foot, water level, EC) on the spot. The heat option is offered on the same sheet (Section 5).
4. **Flag and promote.** Wells with residual above 2 sigma, a rising start transient, or a geothermometer above 80-100 C get a resident Clamp-R. The top 5-10% get a full Sentinel (P01) at the next pump pull.

### 2d. How it enters the model
- **New likelihood class in THERMOS-B L1: "clamp discharge".** T_obs = sum_i w_i T_c(z_i) + delta_pump + delta_riser + eps. The weights w_i come from the screen interval and the driller lithology. delta_pump comes from measured kW, Q and head. eps is about N(0, 0.02-0.05 C) for port or steel strap, N(0, 0.1-0.3 C) for PVC, and N(0, 1-3 C) for low-flow stock wells. This replaces "driller discharge, sigma 2-5 C".
- **Location.** GPS at the wellhead. This retires the +/-400-800 m TRS error for every visited well, and lets us re-locate the old driller value too.
- **Effort.** Each visit is logged as designed effort, with P_det for the clamp per mask class, so the Cox process does not read "visited and cold" as "empty" in lidded cells.
- **Transmissivity.** Q/s from the sounder enters the permeability layer as a direct observation (M30).
- **EVSI loop.** GHOST Tier 1 should rank the clamp against the Sentinel in-silico. My expectation is that the clamp wins on EVSI per dollar for the first pass in any basin and the Sentinel wins for the second.

## 3. Prior art
- **Water wells as heat probes.** Most early USGS Basin and Range heat-flow work used water wells (H06, unverified). The WQP holds about 54,000 groundwater-temperature sites in seven western states (M06). The IDWR layer stores min and max water temperature with use and discharge (M06). None of these logs the pump state, flow or screen weighting, and most are one-off.
- **Pump-efficiency testing.** Utility-funded irrigation pump tests (APEP in California, Pacific Northwest programmes; from memory, unverified) visit thousands of wells a year with a flowmeter and a sounder. They record no temperature for geothermal use. This is the closest operating model, and a possible partner or subcontractor.
- **Thermodynamic pump testing** (ISO 5198, from memory, unverified). It measures pump efficiency from a temperature rise of millikelvins. Our pump-heating correction uses the same idea in reverse.
- **Non-invasive process thermometers** (ABB, Endress+Hauser; from memory, unverified). They use the same two-sensor heat-flux correction.
- **Heat as a groundwater tracer** (Bredehoeft and Papadopulos 1965, WRR 1:325; Anderson 2005; Saar 2011; from memory). They supply the physics for the residual and the start transient.
- **Competitors.** Zanskar uses water-well data from public files (M06, M13) and drills its own wells. I found no record that anyone runs a fleet that measures discharge temperature at the wellhead for geothermal exploration (unverified, no search possible).

## 4. How much it shrinks the ranked uncertainties (my estimates, untested)

| Rank | What the clamp does | Rough shrink |
|---|---|---|
| 1 Detection gap / occupancy | 5-10x more observed cells per dollar than Sentinels. Each visit is designed effort with a calibrated P_det. Its sensitivity is about 0.3-0.6 for outflow-reaching cells and about 0 for lidded ones, so it is a strong second detector for the two-detector survey. | Band on N narrows by about **15-30%** on top of the Sentinel plan in Basin and Range valley fill. It does little in the Cascades and on the SRP lid. |
| 6 Upflow location / footprint | Dense, dated temperatures along heads let us back-project the plume. | Source position goes from about +/-5-10 km to **+/-1-3 km** in basins with 10+ wells on the flow line. |
| 7 Position error | GPS at the wellhead. | Removes the 400-800 m TRS error **for every visited well (100%)**. |
| 2 Permeability | Measured Q/s from the sounder, hundreds of logged cycles from Clamp-R. | About **5-10%** on the MWe band. These are shallow aquifers, so the link to reservoir k is weak. |
| 4 Sensor reliability | The clamp itself is cheap to calibrate. All 20 known blind systems and 40 cold controls in one season, at about $3-6k of field cost. | It makes the rank 4 campaign cheaper and larger. Sensitivity estimates get about 2x tighter. |
| 3 Masking / lid | The start-transient sign, EC and season drift give a mask hint. | About **5-10%**. The Sentinel profile shape is still the real tool. |
| 5 T at 0.5-2 km | Geothermometers on flagged wells. | About **5%**. Mixing with cold water blurs them. |

**Sensor-shrinkable share.** The clamp mainly attacks rank 1 and rank 6, which sit at the top of the "2-5x on N" swing. It helps keep the "sensor-shrinkable share > 30%" kill line safe.

## 5. Rights edge
- **More doors per day.** A drop-probe crew talks to 2-3 owners a day (H06). A clamp crew talks to 10-20. With the H06 sign rate of 30-50%, that is about **3-8 signed options per crew-day** instead of about 1.
- **Sign before we know.** The heat option is offered at the pump report, before the residual is computed. So we pay the "blind" price ($1-2/ac) on every farm in a valley, and we learn which ones matter afterwards. This is the bank's core asymmetry.
- **A product the rancher values.** A free pump-efficiency test (about $150-400 retail, unverified) and, for Clamp-R, a season of pump alerts. A 10-25% efficiency gain on a 100-200 hp irrigation pump is worth thousands of dollars a year in power (unverified). That keeps refusal low and supports the "rights < $20/ac, refusal < 70%" kill line.
- **Tenure fit.** Irrigated farms are deeded land, often fee simple, often with water rights recorded (so the owner is easy to find from NDWR). The SRHA screen still applies (H06). Solar stock wells on BLM allotments are often BLM range improvements, so data there needs the permittee and possibly BLM consent; they inform but do not give us rights (unverified).

## 6. Legal access
- **No entry into the well, no drilling, no water use.** We clamp onto a pipe the owner runs. Owner consent is all that is needed on private land (unverified per state; Nevada well rules govern drilling and plugging, not reading a pipe).
- **Gauge-port probe.** It does touch the water system, so we need explicit consent and a backflow-safe tee. Sample bibs are already there for this.
- **No electrical work.** Non-contact clamps and the utility meter's optical port only.
- **Public land.** Under BLM IM 2026-024 (hardware/MEMO.md), the sensors are casual use. But federal stock wells belong to BLM or the permittee, so access is by permission.

## 7. Costs per site and per area
- Handheld pass: about **$10-30 per well** (crew $1,000-1,400/day and truck, 30-40 wells). With a lab panel on 20% of wells, about $40-60 average. Full kit with sounder: about $60-150 per well.
- Resident Clamp-R: about $150-350 per well-season (base) or $700-1,200 (full), including install and data.
- In a farmed valley with about 0.2-1 well per km2 (unverified), this is about **$5-150 per km2** of valley floor, the cheapest temperature coverage in the stack.
- Year-1 programme: 3 kits ($15-27k), 25 Clamp-R base ($4k), 2-3 crews x 120 days ($250-400k), labs ($60-100k). About **$350-550k for 6,000-12,000 wells**.

## 8. Build time
- Weeks 0-3: buy flowmeter, sounder and meter reader. Build the strap pair and the port probe. Write the app (NDWR match, pump report, e-sign).
- Weeks 3-5: bench loop with steel and PVC pipe, sun lamp and a reference thermometer in the flow.
- Weeks 5-8: field pilot. Clamp-R board spin in parallel.
- **About 6-8 weeks to a field-ready v1, small team of 2-3.**

## 9. Risks
- **Few pumps are running when we come.** Irrigation season is short. Mitigate by paying for a start, and by using solar stock wells all year.
- **Background noise dominates.** Residual sigma 1.5-2.5 C means the clamp only sees strong outflow cores or plumes with many wells. Weak, lidded systems stay invisible. It is a screen, not a confirmer.
- **Mixing hides heat.** A long screen that pulls a lot of cold water dilutes a thin warm layer. A 2 m warm layer in a 100 m screen can drop to under 1 C of excess.
- **PVC and low-flow stock wells** give biased readings. They need their own classes, and some will be useless.
- **Selection bias.** Wells are where farms are: valley centres, not range fronts. Treat placement as effort so the Cox model is not fooled.
- **Copyable.** The hardware is simple. Zanskar or a pump-test firm could do the same. The moat is the dated data plus the signed options, and speed.
- **Utility meter access.** Not every meter has a readable pulse LED. The fallback is current plus nameplate voltage and an assumed power factor (about +/-10%).

## 10. First test (pre-registered)
1. **Bench, weeks 3-5.** Strap vs immersion on a recirculating loop with steel and PVC, sun-lamp swings of 20-40 C. Pass: steel bias < 0.05 C, corrected PVC bias < 0.3 C.
2. **Field, weeks 5-8, about $10-15k.** Sweep the Escalante Valley near Newcastle, Utah, where irrigation wells found a blind plume along the Antelope Range fault (M06). Pre-register: the residual map from about 60-100 wells should put the plume source within 2-3 km of the Newcastle field, and the start transients near the fault should rise. Control: about 40 wells in a nearby valley with no thermal records, picked from state files beforehand, with a residual false-alarm rate (>2 sigma) under 10%.
3. **Kill lines for P04.** Fewer than 40% of target wells give a usable reading in season. The Newcastle source is not recovered within 5 km. False alarms over 20% in the control valley. Same-day option sign rate under 15%.

## Sources
- Repo files cited above: `M06-water-well-temperature.md`, `M23-hydrology-masking.md`, `M30-permeability.md`, `P01-ranch-well-sentinel-2-0-a-resident-well-.md`, `../MODEL.md`, `../../../hardware/MEMO.md`, `../../../hardware/evidence/H06-water-well-landman.md`, and the URLs they hold (for example UNR Play Fairway news, https://www.unr.edu/nevada-today/news/2019/geothermal-success ; NDWR irrigation wells, https://catalog.data.gov/dataset/irrigation-wells-from-the-nevada-division-of-water-resources-well-log-database ; Newcastle, https://pubs.usgs.gov/publication/70015244 ; IDWR geothermal wells, https://gis.idwr.idaho.gov/hosting/rest/services/Groundwater/GeothermalWells/FeatureServer/0).
- From memory, not re-checked in this run (unverified): Bredehoeft and Papadopulos 1965, Water Resources Research 1:325; Anderson 2005, Ground Water 43:951; Saar 2011, Hydrogeology Journal 19:31; ISO 5198 (thermodynamic pump testing); the APEP pump-test programme; ABB and Endress+Hauser non-invasive thermometers.
