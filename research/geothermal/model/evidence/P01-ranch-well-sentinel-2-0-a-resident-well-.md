# P01: Ranch Well Sentinel 2.0, a resident well robot

Date: 23 Oct 2026. Build candidate P01, model track. This builds on `../../../hardware/MEMO.md` and `../../../hardware/evidence/H06-water-well-landman.md` (the drop probe, the $1-2/ac option deal, the SRHA title trap, the 30% loggable kill line), `M06-water-well-temperature.md` (146,235 NDWR driller reports, 697 isolated warm wells), `M23-hydrology-masking.md` (four masks, Peclet physics), `M30-permeability.md` (Libbey and Murphy recovery factors, tides, specific capacity) and `../MODEL.md` (SENTINEL-COX, THERMOS-B, ranked uncertainties). It does not repeat them.

**Method note.** The shared web search budget for this workflow turn (200 calls) was already used up when this agent started. All three searches I tried were refused. So no new web pages were read. Physics and prior art below come from the repo files (cited by file) and from standard literature I know. Items from memory are marked (from memory, unverified). All prices are my estimates and are (unverified) unless a repo file gives a source.

## Bottom line

Build it, but change the brief in two ways.

1. **A flowmeter inside a sounding tube measures nothing.** The water in a 3/4" or 1" sounding tube is a dead-end column. It shares temperature with the well through the thin PVC wall, but no water flows through it. So the heat-pulse flowmeter and the resident micro-winch profiler cannot both live in the tube with a thermistor string. v1 therefore has **two install modes**. *Mode T (tube, no pump pull, most wells):* a 48-node 0.01 C thermistor string, a high-resolution pressure sensor, a barometer, a pump-current clamp and a clamp-on flowmeter on the discharge pipe. *Mode O (open bore: idle, windmill, abandoned, or pump being serviced):* the same string plus heated "thermal dilution" nodes and a hydrophone tail. The full 0.5 m T-P-EC profile and the heat-pulse flowmeter run stay on the install-visit drop probe, as in the prior pick.
2. **The best hook is to pay for the rancher's next pump pull.** Pumps get pulled every few years anyway (about $1-2.5k, unverified). If we pay for it, we fit a new sounding tube and strap a permanent string beside the drop pipe. The rancher gets a free service. We get a permanent, open-bore install and a stronger reason to sign the heat option. This turns the 30% "loggable" kill line from H06 into a solvable cost.

With those changes the unit is cheap (about **$0.9-1.3k BOM at 100 units, $1.6-2.2k at 10**) and **about $350-700 per well-season** all-in. It is the right tool to turn a ranch well from "one noisy driller temperature" into four model inputs that no public file holds: an equilibrium T(z) with vertical Darcy flux (Peclet), aquifer transmissivity and storage, inflow-zone temperatures, and a mask class label. My estimate is that a fleet of about 150-300 units over two seasons cuts the variance of rank 3 (masking and lid flux) by about 40-60% in instrumented basins, rank 2 (permeability) by about 15-25% on MWe, and rank 5 (T at 0.5-2 km) by about 20-35%, and it is the instrument the rank 4 calibration campaign (20 blind / 40 cold) needs. The pump-efficiency app is worth real money to irrigators, which makes the rights edge better than the prior probe, not just equal.

## 1. The physics: what a resident unit sees that a one-hour visit cannot

### 1a. Equilibrium temperature and vertical flow (rank 3, rank 5)
- **Drilling and pumping disturb the bore.** A one-visit log in a well that pumped that morning reads the pumped water, not the rock. A resident string sees the well relax to equilibrium between pump cycles and averages away free convection in the casing. Free convection noise in 6-8 inch casing is about 0.01-0.1 C at a few metres (from memory, unverified). It is random in time, so 1,000+ samples over months average it down by about 30x.
- **Peclet fit (Bredehoeft and Papadopulos 1965, WRR 1:325; from memory).** Steady vertical Darcy flux q bends a conductive profile. The Peclet number is Pe = rho_w c_w q L / lambda.
  - Calc: with L = 100 m, lambda = 2 W/m/K, rho_w c_w = 4.18 MJ/m3/K, Pe = 1 at q of about 4.8e-9 m/s (**about 15 cm/yr**). This matches the M04 note that a 100 m profile is advection-dominated at about 15 cm/yr.
  - Calc: across 100 m at 50 C/km the profile spans 5 C. At Pe = 0.3 the departure from a straight line is about 0.15-0.2 C. A string with 0.01 C relative precision and 30+ nodes in the water column resolves Pe to about +/-0.05, so **q to about +/-1-2 cm/yr**. That is good enough to split "conductive" from "recharge-swept" from "upflow-fed".
- **Why this matters to the model.** In THERMOS-B the lid term is now a free parameter in many cells. Sensitivity runs from 0.8 (leaky) to near 0 (lidded) in MODEL.md. A measured q with an error bar turns the 1D column into a constrained fit. The column model can then push T(z) to 1-2 km with an honest error bar instead of a guess.
- **Seasonal noise is not a problem below about 15 m.** The annual thermal skin depth is about sqrt(kappa P / pi), about 3.2 m for kappa = 1e-6 m2/s. Below about 15 m the annual wave is under 1% (calc). Most water tables sit 10-100 m down (H06), so the string mostly starts below it.

### 1b. Every pump cycle is a free drawdown and recovery test (rank 2)
- The pump-current clamp gives the exact on and off times. A clamp-on ultrasonic flowmeter gives Q to about 2-5% (from memory, unverified). Without it, the current plus the pump curve gives Q to about +/-20%.
- The pressure sensor reads drawdown and recovery. Cooper-Jacob recovery gives transmissivity T = 2.3 Q / (4 pi delta-s), where delta-s is the drawdown change per log cycle of time (standard; from memory). A season holds hundreds of cycles, so we can stack them and also watch for skin and boundary effects (a fault barrier or a recharge boundary shows as a slope change).
- This replaces the single, often rounded driller specific capacity (M30) with a measured T, good to about a factor of 1.5 (my judgement).

### 1c. Earth tides, air pressure and passing quakes give T and storage with no pumping (rank 2)
- **Tides.** Hsieh, Bredehoeft and Farr (1987, WRR 23:1824; from memory, also cited in M30) showed that the phase lag and amplitude of the M2 and O1 tides in well water level give transmissivity and storage. The method works best for T from about 1e-6 to 1e-3 m2/s. Above that the well tracks the aquifer with no lag, and we get only a lower bound. Tidal head amplitudes in confined aquifers are about 1-10 mm (from memory, unverified). A sensor with about 2 mm resolution sampled each minute for 30+ days fits the M2 amplitude to about 0.1 mm by harmonic least squares (calc, assuming white noise).
- **Air pressure.** A barometer in the surface box gives barometric efficiency. Its frequency response says whether the aquifer is confined, leaky or open, which is a direct read on the lid (rank 3).
- **Quakes.** Large distant quakes shake water levels (hydroseismograms, Cooper et al. 1965; from memory). Elkhoury, Brodsky and Agnew (2006, Nature 441:1135; cited in M30) showed that shaking can raise permeability and shift the tidal phase. A unit sampling pressure at 10 Hz on a trigger catches these for free. A well that shows a large, long-lived tidal phase shift after shaking sits in connected fractures, which is the "permeability class" signal we want.
- **Honest limit.** All of this measures the shallow aquifer (30-300 m), not the reservoir at 1-2 km. It informs permeability class through a learned transfer, and most strongly in wells within about 1-2 km of a range-front fault or in an outflow aquifer.

### 1d. Pump-on temperature profiles show where warm water enters (rank 6, rank 3)
- When the pump runs, water moves up or down the casing from each screened or open zone to the intake. The string's temperature changes along the bore mark where water enters and how warm it is. This is the standard "pumping temperature log" idea, done automatically every cycle.
- Detection: a 0.05 C step between neighbouring nodes during pump-on, repeated over cycles (my judgement).
- It tells us which zone carries the warm water. That matters because ranch wells sample outflow, not upflow (rank 6). The inflow-zone temperature plus the head gradient helps back-project the plume.

### 1e. Heated nodes measure flow past the well in open bores (Mode O)
- A full heated cable (active DTS) needs about 5-20 W per metre (from memory, unverified). That is 1-2 kW for a 100 m string, which a solar node cannot supply.
- So v1 uses **thermal point dilution**: each node carries a small heater (about 1 W for 60 s, about 60-100 J). The rate the pulse decays, compared with the node's still-water decay, gives water speed past the node. Four pulses a day on 48 nodes is about 5-7 Wh/day (calc), which is easy.
- In open bores this gives a flow profile through the well (horizontal flow past screens and vertical flow in the bore). In a sounding tube it gives only an effective thermal conductivity of tube plus annulus plus gravel pack. That is mostly water convection, so **we do not claim in-situ rock conductivity from the string.** Rock conductivity comes from a needle probe on cuttings or core (rank 7).

### 1f. What the hydrophone tail adds (small)
- It hears pump start, cavitation and cascading water (a water-level clue and a well-health alert). In idle open wells it can record local micro-earthquakes as tube waves (from memory). It is a $40 add-on. Expected model value is small, so it is optional.

### 1g. Detection limits in one table
| Quantity | v1 resolution (estimate) | Needs | Model input |
|---|---|---|---|
| Relative T between nodes | 0.005-0.01 C | bath calibration, months of averaging | T(z) curve |
| Absolute T | +/-0.05-0.1 C | TMP117-class sensor, reference bath | T(z) offset |
| Vertical Darcy flux q | +/-1-2 cm/yr at L = 100 m | >= 30 nodes in water | lid flux, mask class |
| Transmissivity (pump cycles) | factor about 1.5 | Q from clamp-on meter | perm prior |
| T and S (tides) | factor about 2, best 1e-6 to 1e-3 m2/s | >= 30 days, 1 min sampling | perm, storage, confinement |
| Inflow zones | 0.05 C step | pump-on profiles | outflow zone, plume back-projection |
| Flow past node (Mode O) | about 0.1-10 m/day (unverified) | heater nodes | flow, mask |

## 2. Prior art (what exists, what we add)
- **Point loggers.** Solinst Levelogger and In-Situ Level TROLL record P, T and sometimes EC at one depth for about $1-3k (H06). They do not give a profile, flow, pump context or a modem by default.
- **USGS heat-pulse flowmeter.** Hess (1986) and Paillet's later work made the heat-pulse flowmeter a standard USGS borehole tool for low vertical flows (from memory, unverified). It needs an open bore and a diverter. We keep it for open-bore install visits only.
- **Active and passive DTS in hydrogeology.** Fibre DTS, including heated-cable active DTS, is used to map flow in boreholes (Read et al. 2014; Bense et al. 2016 review; from memory, unverified). Interrogators cost about $20-100k (from memory, unverified). Our thermistor string trades fibre's metre-scale coverage for a $500 string that can stay in a ranch well for months.
- **Tidal and barometric analysis.** Hsieh et al. 1987; Rojstaczer (1988) on barometric response; Cooper et al. 1965 on seismic oscillations (all from memory). USGS NWIS has continuous water-level wells, but these are research and monitoring wells, not ranch wells near geothermal targets.
- **Heat as a groundwater tracer.** Anderson (2005, Ground Water 43:951) reviews the method (from memory, unverified).
- **Permafrost thermistor strings.** GTN-P borehole strings show multi-year resident thermistor strings are routine and stable to about 0.01-0.02 C (from memory, unverified).
- **Ag pump monitoring.** Commercial products monitor ranch pumps and tanks for about $300-1,000 (H06, unverified). California's Advanced Pumping Efficiency Program (APEP, run with Cal Poly ITRC) has long paid for ag pump efficiency tests (from memory, unverified). So pump efficiency is a known, valued service to irrigators.
- **What is new here.** Nobody we found combines a resident T string, pump-cycle hydraulics, tides and a modem in private ranch wells, chosen by a geothermal model and tied to a heat option. Zanskar works on BLM land with its own holes (H06, M13).

## 3. v1 design

### 3a. Down-hole string (both modes)
- **Nodes.** 48 nodes per standard string (32 or 64 as options). Each node is a small PCB with a TMP117-class digital sensor (about +/-0.1 C absolute, 0.0078 C resolution; from memory, unverified) and a tiny RISC-V or ARM microcontroller (about $0.10-0.50) that talks on a shared RS-485 bus. Each node also has a 1 W heater resistor (used only in Mode O).
- **Size.** Overmolded nodes 11-12 mm OD, about 30 mm long, on a 6 mm 4-core polyurethane cable with a Kevlar strength member. It fits a 3/4" schedule 40 sounding tube (about 20.9 mm ID) with room to spare.
- **Spacing.** Dense near the water table and in the expected inflow zone: 1 m spacing for the first 16 nodes, then 3-5 m. Standard length 200 m, cut to the well's driller log.
- **Bottom tail.** A 16 mm stainless sinker (0.5 kg) holding a pressure sensor. v1 uses a Keller 36XiW-class sensor, 0-10 bar, about 0.2 mbar (2 mm water) resolution (from memory, unverified). It sits 5-10 m above the pump intake so drawdown never leaves it dry. A low-cost MS5837-30BA sits beside it as a cross-check.
- **Optional.** Inductive EC cell (Mode O only, about $150, unverified). Piezo hydrophone and preamp, about $40.

### 3b. Surface box (on the well cap or pump control box)
- IP67 box about 200 x 150 x 100 mm. Cable enters through the vent or sounding port with a split gland, so no well modification is needed.
- Logger: low-power microcontroller, 32 GB SD card (keeps all raw data for 12 months), BMP390-class barometer (about 0.03 hPa, which is about 0.3 mm water; from memory), GPS for time and position.
- Pump inputs: split-core current clamp on one pump leg (about $15). Optional clamp-on ultrasonic flowmeter on the discharge pipe (about $150-300, unverified). Optional discharge pressure gauge.
- **Comms:** LTE-M or NB-IoT module (about $30-40, plus about $2-5 per month data; unverified). Where there is no cell signal, Iridium SBD (about $250-300 module plus about $15-30 per month for a daily summary; unverified). The daily message carries a few kB: tide fit, pump cycles, temperature summary and alerts. Raw data is pulled on the recovery visit or over LTE.
- **Power:** most electric pumps already have 240 V at the control box, so the default is a small AC supply with a 12 Ah LiFePO4 backup. For windmill or solar-pump wells, a 20 W panel on a short mast plus the same battery.
- **Power budget (calc):** string read every 10 min (under 0.5 Wh/day), pressure at 1 Hz with a 10 Hz quake trigger buffer (about 0.5-1 Wh/day), modem (about 0.5-1.5 Wh/day), heater pulses in Mode O (about 5-7 Wh/day). Total about 2-3 Wh/day in Mode T and 8-10 Wh/day in Mode O. The 154 Wh battery lasts about 2-8 weeks with no charge.

### 3c. Rancher app
- Pump-on hours, starts per day, flow, specific capacity trend, water level and drawdown, kWh per acre-foot, pump efficiency trend, alerts for falling water level, short-cycling, dry running and failed pump.
- Why it is worth money: a 50-100 hp irrigation pump running about 2,000 h/yr uses about 75-150 MWh, roughly $8-20k/yr. A 10% efficiency fix is worth about $1-2k/yr (calc from unverified tariffs). That is more than the unit costs.

### 3d. Parts list and cost (estimates, unverified)
| Item | 10 units, each | 100 units, each |
|---|---|---|
| 48 sensor nodes (sensor, MCU, PCB, heater, overmold) | $480 | $260 |
| 200 m cable with Kevlar member | $350 | $220 |
| Pressure sensor + sinker + cross-check sensor | $500 | $330 |
| Surface logger, barometer, GPS, SD, enclosure | $180 | $90 |
| LTE-M modem + antenna (Iridium option +$300) | $60 | $40 |
| Battery, AC supply, solar kit | $150 | $100 |
| Current clamp | $15 | $10 |
| Calibration (bath time, labour) | $150 | $60 |
| Assembly and test labour | $200 | $90 |
| **Core unit (Mode T)** | **about $2.1k** | **about $1.2k** |
| Clamp-on flowmeter (irrigation wells) | +$250 | +$150 |
| EC cell + hydrophone (Mode O) | +$190 | +$120 |

The brief's $0.7-1.5k core is reachable at about 100-300 units. A 32-node, 120 m string for stock wells comes in about $250 lower.

### 3e. Deployment and crew time
- **Before the visit:** screen title (SRHA, railroad check) from GLO patents (H06). Pick the well from the EVSI-per-dollar list (MODEL.md first validation step 1). Pre-cut string spacing to the driller log.
- **Install visit, Mode T, 2 people, about 2.5-3.5 h on site:** 45 min drop-probe 0.5 m T-P-EC profile and water sample (prior kit); 45-60 min string install and box mount; 20 min app setup with the rancher; 30-45 min option paperwork and signing. A team can do about 2 installs a day with driving.
- **Install, pump-pull mode:** add a pump contractor for 4-6 h at about $1-2.5k (unverified), paid by us. Use only on high-EVSI wells or as the rancher's sweetener.
- **Recovery or move:** 1 h. Most units move after 3-4 months, so each unit serves about 3 wells a year. High-value wells keep a unit for 12 months.
- **Cost per well-season (calc):** hardware amortized over 3 years and about 9 deployments is about $130-250; crew time about $250-350 for install plus recovery; data and power about $20-60; spares and losses about $50. **Total about $450-700 per well-season** in Mode T, consistent with the brief. Pump-pull installs cost about $1.5-3k.

## 4. How it feeds the model
- **New THERMOS-B likelihood per well:** equilibrium T(z) with a node covariance; q with an error bar; aquifer T and S; barometric confinement class; inflow-zone depths and temperatures. These enter as a censored, advection-aware column reading rather than a single driller temperature (M06).
- **Mask label.** Profile shape (convex, concave, isothermal, reversal) plus q plus confinement becomes a direct observation of the latent mask class that sits under all detectors.
- **Calibration of other sensors (rank 4).** At each Sentinel well we also log the one-visit drop probe on day 1 and compare. That gives the one-visit probe's error by mask class, so the 300-800 later single visits each carry a known reliability.
- **GHOST in-silico check.** Before buying 100 units, run GHOST Tier 1 with the Table 1g noise levels and confirm EIG per dollar beats the one-visit probe in at least the lidded and swept mask classes.

## 5. How much it shrinks the ranked uncertainties (estimates, untested)
| Rank | Now | With 150-300 Sentinels over 2 seasons | Rough shrink |
|---|---|---|---|
| 1 Detection gap / occupancy | P_det under masks mostly a prior | Each Sentinel turns a "blank" cell into "masked, not empty" or "truly cold". Feeds the mask-class P_det | 10-20% of the N band in surveyed basins |
| 2 Permeability class (about 10x MWe) | Fault proxies plus rounded driller specific capacity | Measured T, S and fracture response at about 1-2 per 100 km2 of target ground; a learned transfer to class | 15-25% of log-variance on MWe in instrumented cells; 5-10% regionally |
| 3 Masking / lid thickness | Sensitivity 0.8 to 0, largely free | q to +/-1-2 cm/yr plus confinement from barometry | 40-60% of mask variance at instrumented cells; about 20-30% within about 5-10 km along the aquifer |
| 4 Sensor reliability s/q | Untested priors | Sentinel is the reference for 20 blind / 40 cold | It is the instrument; removes the "VOI swings >2x" for single-visit probes |
| 5 T at 0.5-2 km | Advection bias of tens of C | Advection-corrected gradient | sigma of T(1 km) from about +/-35 C to about +/-20-25 C at the well |
| 6 Upflow location | Outflow only | Inflow-zone temperatures plus heads tighten plume back-projection | 10-20% smaller search area per anomaly |

Net effect on the buyer metric (F5/F95 per 100 visits): Sentinels are not the cheapest visit, but they are the visits that tell us what the cheap visits mean. My guess is that 10-20% of the 300-800 visits as Sentinels makes the target of under 4x F5/F95 reachable about one season earlier than single visits alone (untested).

## 6. Rights edge
- **Same visit, stronger offer.** The prior pick gave a one-hour well check. Sentinel leaves a device that saves an irrigator about $1-2k/yr in power (calc, unverified tariffs). That is a better reason to sign a $1-2/ac option than a lab report.
- **Sticky renewals.** The unit stays 3-12 months and the app stays forever. Renewals and option extensions to neighbours happen at the kitchen table, not cold.
- **Pump-pull sweetener.** Paying a $1-2.5k pump service on a 5,000-acre ranch is about $0.2-0.5/ac, still far below the $40/ac BLM auction comparison (H06).
- **Private data.** Readings on private land are not filed anywhere. On unleased federal land, data need not be filed (hardware MEMO, 43 CFR 3253.10(b)).
- **Limit.** The edge depends on ranches with fee-simple heat. The SRHA screen still applies, and water-right rules on geothermal fluid in some states still apply (H06).

## 7. Risks
1. **No sounding tube and no open annulus** in many wells. Mitigation: pump-pull mode, target idle and windmill wells, and stock wells with removable caps. Kill if under 30% of target wells are installable without a pump pull and pump pulls cost over $3k.
2. **The shallow aquifer does not predict reservoir permeability.** The rank 2 gain may be smaller than claimed. Test with the 20 blind / 40 cold wells before scaling.
3. **In-casing convection** may swamp the 0.01 C target in large-diameter wells. Mitigation: months of averaging, foam baffles in Mode O, prefer 4-6 inch wells.
4. **Pump vibration and tangling** if a string is fed down an annulus beside a running pump. Only install in tubes or during pump pulls.
5. **Rancher trust.** A device on the well is intimate. Clear data-sharing terms, and the rancher owns their pump data.
6. **Comms gaps** in remote valleys. Iridium fallback adds about $300 and monthly cost.
7. **Sensor drift** over 12 months. Recalibrate at each move; the barometer and pressure sensor cross-check each other.
8. **Copyable hardware.** The moat is the dataset and the signed ranches, not the device.

## 8. Cheapest first test
- **Weeks 0-6, about $15-25k (unverified).** Build 4 units (2 Mode T, 2 Mode O). Bath-calibrate to 0.01 C relative. Bench-test the heated nodes in a flow column.
- **Weeks 6-14.** Install in 4 ranch wells: 2 near a known blind or hidden system (for example warm NDWR wells from the M06 list near Gabbs Valley or Granite Springs) and 2 in a cold control valley. Run each for at least 60 days.
- **Pass bars:** (a) M2 tide fitted with SNR over 5 in at least 2 of 4 wells; (b) pump-cycle T within a factor of 2 of a contractor step test on at least one well; (c) Peclet q repeatable to +/-2 cm/yr across months; (d) the warm wells show a distinct mask or q signature from the controls; (e) at least 2 of 4 ranchers sign the heat option and want the unit to stay.
- **Kill:** M2 not visible in any well; q not repeatable; or no rancher will sign with the unit offered.

## 9. Self-scores (1-5)
- model_uncertainty_alpha **4**: directly hits ranks 3, 4 and 5 and part of 2. Limited by sampling the shallow aquifer.
- rights_alpha **4**: a real money-saving device on the well, with renewals built in.
- buildability **4**: all parts are off the shelf. A small team can build 10 units in about 8-12 weeks.
- cost_scale **3**: about $450-700 per well-season is fine for hundreds of wells, but it is about 3-5x a one-visit log, so it cannot be the only visit type.
- moat **3**: dataset plus ranch relationships compound; the hardware itself is easy to copy.

## Sources
- Repo: `../../../hardware/MEMO.md`, `../../../hardware/evidence/H06-water-well-landman.md`, `M04-bht-corrections.md`, `M06-water-well-temperature.md`, `M23-hydrology-masking.md`, `M30-permeability.md`, `../MODEL.md`.
- Libbey and Murphy, SGW 2026 (via M30): https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Libbey.pdf
- Edwards et al. (Zanskar), SGW 2025 (via M06): https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Edwards.pdf
- NDWR Well Driller Reports service (via M06): https://arcgis.water.nv.gov/arcgis/rest/services/NDWR/Well_Driller_Reports/FeatureServer/0
- Solinst Levelogger price page (via H06): https://fondriest.com/solinst-levelogger-5-ltc-water-level-conductivity-loggers.htm
- From memory, unverified (no web budget): Bredehoeft and Papadopulos 1965 (WRR 1:325); Hsieh, Bredehoeft and Farr 1987 (WRR 23:1824); Elkhoury, Brodsky and Agnew 2006 (Nature 441:1135); Cooper et al. 1965 (JGR); Rojstaczer 1988 (JGR); Hess 1986 (Can. Geotech. J.) heat-pulse flowmeter; Read et al. 2014 and Bense et al. 2016 on DTS in hydrogeology; Anderson 2005 (Ground Water 43:951); TI TMP117 datasheet; Keller 36XiW datasheet; California APEP program.
