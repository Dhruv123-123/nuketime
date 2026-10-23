# P10: Slickline Trailer plus Deep Grab. Our own 3 km memory T-P logging unit and gas-tight sampler for idle oil, gas, geothermal and TG wells

Date: 23 Oct 2026. Build candidate P10, model track. This builds on `../../../hardware/evidence/H02-existing-well-logging.md` (SMU tools and trailer, BHT error, orphan and idle well counts, the "Thermal Census" fleet sketch), `M04-bht-corrections.md` (error ladder; Railroad Valley and Black Rock found by oil wildcats; about 1,300 western oil BHTs), `M20-tg-and-mining-holes.md` (442 scanned NBMG TG holes), `M22-gas-isotopes.md` (He R/Ra as the permeability tracer), `M23-hydrology-masking.md` (Kimama lid, 4.5 then 72-75 C/km), `M25-sedimentary-oilfield.md` (Railroad Valley, Blackburn, Pine Valley as blind systems), `../../evidence/D03-great-basin-wells.md` (NDOM 775 O&G and 938 geothermal wells; 536 western Utah wells), `../../evidence/A04-orphan-wells.md` (wellbore transfer, Blackburn BLM precedent), and `P07` (ride-along pucks). It does not repeat them. What is new here: a concrete v1 build, crew time per well, the sampler problem in a stagnant cased well (and the fix), the oil-and-gas lessee's co-production preference right (a trap the brief missed), the EPA "temperature log = mechanical integrity" hook, a reachable-well count for the West, and a small calculation (`P10_calc.py`) that shows where the model value saturates.

**Method note.** The shared web-search budget for this workflow turn was used up before this agent's first query (all three searches were refused). No new web sources were read. Everything comes from sibling files in this repo (which cite primary sources) and from what I know. Every number not traced to a sibling file or a URL below is marked (unverified). Prices of used slickline units, memory gauges and samplers in particular need a quote.

---

## Bottom line

- **Build it, but as the deep rung of the kit, not the lead product.** A used trailer slickline unit with a 3.5-4.5 km drum, a 5,000 psi lubricator, two 177 C quartz memory T-P gauges in a heat shield, and a slim positive-displacement sampler costs about **$170-280k all-in for v1** (lean version about $100k by renting pressure control). Then about **$2-3k per well** marginal (field about $1.2-1.9k plus lab about $0.9k). A two-person crew (one hired certified slickline operator plus our field geologist) logs **one 3 km well a day with a sample, or 1.5 wells a day without**.
- **Physics is strong for temperature, weak-to-fixable for the sample.** An idle well that has stood six months or more is close to thermal equilibrium. A down-log at about 9 m/min gives T(z) to about +/-0.05-0.2 C, against +/-8 C (1 sigma) for a corrected BHT and +/-16 C (96%) for a header BHT (M04). That is a 15-50x tighter reading at 1-3 km, exactly where the model's rank 5 is widest. The sampler is harder: fluid sitting in a cased idle well is old completion brine that has rested against steel for years. Its H2 is mostly from casing corrosion, and its gases may have swapped with the gas cap. So **H2/Ar is unusable from a stagnant cased well, CO2/Ar is doubtful, and He R/Ra plus cation and silica geothermometers are usable only after a small purge from the perforations** (Section 3). The v1 fixes this with a slickline swab or bailer purge of 1-3 perforation-interval volumes, then the sampler at the perforations.
- **The western pool is real but thin.** Nevada has about 775 O&G wells on record and only 63 documented orphans; western Utah has 536 wells (D03, H02). Most are plugged. My count of **open, reachable wells that sit in or next to high-lambda cells in the West is about 600-2,500** (Section 6, unverified): Railroad Valley, Pine Valley and Blackburn producers and shut-ins, western Snake River Plain gas wells in Payette County (Idaho), Uinta and Paradox margin shut-ins, CalGEM long-term idles near the Salton Trough, Coso, Long Valley and Kern margins, idle geothermal observation and slim holes (NDOM 938 permitted geothermal wells), and open research and TG holes. Beyond the West, Texas alone has about 160,000 inactive wells, California 15,922 long-term idles, and the USGS lists 117,672 documented unplugged orphans (H02). So the asset is not "too small". The western part is a calibration and anchor set, and the sedimentary part is a scale market.
- **Model value: rank 5 most, then ranks 3, 1 and 2.** In cells that hold a logged well, the T at 1.5 km error falls from about 11-13 C to under 1 C. Across the whole Nevada-Utah map, I estimate the rank 5 log-width shrinks by **20-30%** in two years, rank 3 (lid end depth) by **15-25%** in basins with deep wells, rank 1 (deep or lidded catch rate) by **10-20%** through a designed "deep well under a shallow blank" test, and rank 2 by **5-15%** from purged He R/Ra plus shut-in pressure and a bail-down test. The BHT cold-bias calibration that the brief leans on saturates after about 10 paired wells per basin (Section 4c). After that, every extra log only helps its own cell and its neighbours.
- **Rights edge: real, but the brief overstated it.** An oil and gas lease does not carry the federal geothermal right. But a federal oil and gas lessee who produces hot fluid can apply for a **noncompetitive geothermal lease for co-production** on its own lease (30 USC 1003(c) as amended by EPAct 2005, unverified wording). So the operator is a partner to sign, not someone to go around. The clean edges are: (a) the **unleased BLM and state parcels next to** a hot logged well, which we nominate or take as leftover $1/ac/yr leases before anyone sees the log; (b) **private fee land** where the surface or mineral owner holds the heat (Texas SB 785; Nevada and Utah per state law, unverified detail), optioned on the same visit; (c) a **wellbore option plus carry** with the operator, sweetened by a free log that counts as a mechanical-integrity test (40 CFR 146.8(c)) and helps against plugging deadlines (Texas SB 1150, 2027 onward).
- **Self-scores:** model_uncertainty_alpha 3.5, rights_alpha 3, buildability 4, cost_scale 3, moat 3.

---

## 1. Why it detects blind upflow

### 1a. What an equilibrium log at 1-3 km sees that nothing shallow sees

Blind systems are mostly "heat is there, but a lid or moving water hides it at the surface" (M23). Three cases matter:

1. **Cold aquifer lid.** At Kimama on the eastern Snake River Plain the gradient is 4.5 C/km down to about 950 m, then 72-75 C/km below it, with 125-140 C geothermometers deeper (Lachmar et al. 2017, https://link.springer.com/10.1186/s40517-017-0086-8). A 2 m probe, a ranch well, an E-MT node above the conductor, and every shallow-gradient method read "cold" here. Only a hole through the lid reads the truth. A 1-3 km idle well that crosses the lid gives the kink depth directly (rank 3) and the gradient below it (rank 5).
2. **Regional carbonate sweep.** In east-central Nevada ("Eureka Low") deep interbasin flow carries heat sideways, so shallow heat flow is low (M23). Railroad Valley is inside this belt, yet Bacon Flat-Grant Canyon holds 120-130 C fluid at about 1.6 km with heat flow up to 234 mW/m2 (M25, M04). The heat is found only by deep wells.
3. **Outflow tongue and reversal.** Hot water riding a permeable layer gives a temperature reversal (hot above cool). A single BHT cannot see a reversal. A full profile can, and the depth of the hot layer plus the gradient below it points back toward the upflow (rank 6).

### 1b. Sensitivity and detection limits

| Quantity | Our v1 | Legacy alternative | Gain |
|---|---|---|---|
| T at a depth, idle well at equilibrium | +/-0.05-0.2 C (quartz gauge, depth +/-1-2 m) | Single corrected BHT +/-8 C (1 sigma); header BHT +/-16 C (96%) (M04) | 40-100x on the point; full curve instead of one point |
| Gradient over a 200 m interval | +/-0.5-1 C/km | Two BHTs: +/-50 C/km or worse | Kink and curvature become visible |
| Lid end (kink) depth | +/-10-30 m where the well crosses it | Not observable | New observable |
| Reversal amplitude | 0.2 C detectable | Not observable | New observable |
| Conductive vs convective test (Peclet) | Fit to vertical Darcy flux of about 1-10 cm/yr over 500 m (Bredehoeft-Papadopulos, estimate) | Not observable | New observable |
| Formation pressure at perforations | +/-0.02% FS quartz (about +/-1 psi) | Old DSTs, sparse | Head, and with a bail-down, kh |
| He R/Ra after purge | +/-2-5% (lab) | Springs only | Deep permeability label in a cell with no spring |

**Noise sources and fixes.**
- **Not yet at equilibrium.** Disturbance decays roughly as circulation time over time since disturbance (Lachenbruch and Brewer 1959). A well shut in for six months after normal production is within about 0.1-0.5 C (estimate). We log only wells idle six months or more, and we repeat a 200 m section at total depth (TD) to check drift.
- **Convection inside the casing.** Water in 5.5-7 inch casing convects above a few tens of C/km, adding about 0.01-0.3 C wiggle (estimate). This is far below the 10-100 C signal we hunt. We smooth over 10-20 m.
- **Flow behind casing or between perforations.** This shows as a step or an isothermal section. It is a nuisance for heat flow but is itself the integrity finding the operator wants. We flag it and down-weight that interval.
- **Gas-filled sections.** A gauge in gas couples poorly to the wall. We slow to 3-5 m/min in gas and fit the gauge's lag. Below the fluid level the reading is clean.
- **Gauge lag.** Quartz gauges have time constants of tens of seconds (unverified). At 9 m/min that is a 3-6 m depth lag, corrected by deconvolution with a pair of up and down passes.

### 1c. What the deep grab adds, and where it fails

The sampler is a 1.5-1.75 inch, 300-600 ml positive-displacement bottle with a clock or pressure trigger, a floating piston and a nitrogen pre-charge so the sample stays above bubble-point pressure on the way up. This is the same design idea as the Leutert PDS and the Kuster flow-through samplers used in geothermal wells for decades (names from memory; specs and prices unverified).

| Tracer | What it tells the model | Works in a stagnant cased well? | With a perforation purge? |
|---|---|---|---|
| He R/Ra, 4He excess, Ne | Deep permeable path, mantle helium (rank 2, rank 1) (M22) | Partly. He survives, but air from the annulus and years of exchange with the gas cap dilute it | Yes, the best tracer here |
| Na-K, Na-K-Ca, K-Mg, Na-Li, Li-Mg geothermometers | Reservoir T where the fluid last equilibrated (rank 5) | Doubtful: completion brine, kill fluid and corrosion products | Yes, if 1-3 interval volumes come from the formation |
| Silica (quartz, chalcedony) | Reservoir T to about 250 C (rank 5) | Doubtful, cement and casing scale add silica | Yes, with care |
| CO2/Ar, H2/Ar, CH4/CO2 gas geothermometers (Giggenbach 1991) | Reservoir T and redox | **H2 no** (steel corrosion makes H2). CO2/Ar doubtful | CO2/Ar yes if the sample is single-phase; H2/Ar only in flowing or freshly swabbed wells |
| Stable isotopes, tritium, 14C | Recharge age, mixing with young water | Doubtful | Yes. Tritium also flags contamination |

So the brief's claim that the sampler gives "true He/R/Ra, H2/Ar and CO2/Ar" needs the purge step. In flowing producers (Railroad Valley oil wells with hot water cut, Idaho gas wells with produced water) the problem mostly goes away, because the fluid is fresh from the formation.

---

## 2. Concrete v1 design

### 2a. Parts list (v1, prices estimated, unverified unless noted)

| # | Item | Spec | Est. cost |
|---|---|---|---|
| 1 | Used trailer slickline unit | Single drum, hydraulic drive, diesel power pack (about 25-40 hp), 15,000 ft (4.6 km) of 0.092 inch or 0.108 inch wire, mechanical plus encoder depth counter, weight indicator. SMU's own 7,600 m memory reel trailer weighs about 1,700 kg (H02) | $60-150k used |
| 2 | Refit | New wire (H2S-rated alloy if sour wells), new encoder, digital weight and depth logger, LED lights, ground rods, spill kit | $15-30k |
| 3 | Pressure control | 2.5-3 inch ID lubricator, 3 x 8 ft sections, 5,000 psi, manual wireline valve (BOP), stuffing box, gin pole or small hydraulic mast, quick unions for common wellheads | $20-40k (or rent at about $300-600/day) |
| 4 | Tool string | Rope socket, 2 x 5 ft stem bars, knuckle joint, spring or mechanical jars, tubing-end locator, gauge cutter and impression block (to drift the well first) | $6-12k |
| 5 | Memory gauges x2 (redundant, run in tandem) | Quartz T-P memory gauges rated about 177 C and 10-15 ksi, 1 s sampling, multi-million-point memory, high-T lithium batteries. Brands: Kuster, Spartek, Metrolog, ProbeSensonix, Weatherford Quantum (H02) | $20-50k for two |
| 6 | Heat shield (Dewar) | For wells above 177 C (Black Rock-type, about 230 C at 3.8 km per M04); keeps gauges below rating for 8-12 h (SMU 400 C/10 h tool shows it can be done, H02) | $8-20k |
| 7 | Memory gamma-CCL tool | Natural gamma plus casing collar locator for depth control and lithology tie | $8-15k |
| 8 | Deep Grab sampler x2 | 1.5-1.75 inch OD, 300-600 ml, floating piston, N2 pre-charge, clock trigger, 175-200 C seals (FFKM), titanium or Inconel 718 body. Custom build at a machine shop to the Leutert-type design | $3-8k each custom (brief); $15-30k each commercial (unverified) |
| 9 | Purge kit | Slickline swab cups and a 2 inch, 10-20 ft dump bailer, 500 gal poly tank for purged fluid, transfer manifold | $4-8k |
| 10 | Sample handling | Transfer bench, copper tubes and clamps for noble gases (M22), evacuated gas bulbs, filters, field pH/EC/alkalinity kit | $3-6k |
| 11 | Tow vehicle | Used 1-ton 4x4 diesel pickup, 14,000 lb gooseneck capacity | $40-60k |
| 12 | Safety | H2S monitors, SCBA x2, fire extinguishers, first aid, PPE | $5-8k |
| 13 | Comms and data | Starlink mini plus satellite messenger, rugged laptop, gauge interface, GPS (cm-level with a cheap RTK puck for wellhead ties, helps rank 7) | $4-7k |
| | **Total v1** | | **about $200-450k at the top of every range; about $170-280k typical; about $100k lean (rented pressure control, one gauge pair, own-built sampler)** |

The brief's $80-200k fits the lean end. The typical figure is higher because of the second gauge, the heat shield and the truck.

### 2b. Dimensions, power, comms

- **Trailer:** about 16-20 ft gooseneck, 2.4 m wide, about 3,500-5,500 kg loaded (estimate). It reaches ranch roads in Railroad Valley and Payette County. No CDL needed under 26,001 lb combined GVWR if sized carefully (unverified for each state).
- **Drum:** 15,000 ft of 0.092 inch wire, breaking strength about 1,500-1,800 lb (unverified). A 3 km string of tools weighs about 60-90 lb plus wire, so the safety factor is fine for vertical wells. Deviated wells need more stem.
- **Power:** the diesel power pack runs the drum hydraulics. A 2 kW inverter on the truck runs the laptop and sample bench. Gauges run on their own batteries for 20-100 h (SMU battery about $150 per 20 h, H02).
- **Comms:** none downhole (memory mode). Field data sync over Starlink each evening into the THERMOS-B ingest. A cellular or Iridium check-in every 30 min for lone-worker safety.

### 2c. Deployment method, step by step

1. **Desk screen (before the visit).** From NDOM, UT DOGM, IDL, CalGEM and RRC files: well status, idle date, casing and tubing sizes, perforations, last fluid level, H2S flag, deviation. Rank wells by EVSI per dollar using the frozen model (VOI-Bank). Pre-register the expected T(z) and its band for each well before logging (keeps the s/q calibration honest, rank 4).
2. **Contract (before the visit).** Operator signs a data and access agreement: we bring our own insurance and certified operator, they get the integrity log, a fluid level, a shut-in pressure and a temperature leak screen. We get the data, exclusive for 2-3 years, plus a ROFR or option on the wellbore for geothermal use and an agreed carry if their co-production right is used (Section 5).
3. **Rig up (1-1.5 h).** Bleed-check, install lubricator on the master valve, pressure-test it, hang the tool string.
4. **Drift run (0.5-1 h, first visit only).** Gauge cutter to TD to make sure the tubing or casing is clear.
5. **Down-log (2-6 h).** Two quartz gauges plus gamma-CCL, continuous at about 9 m/min below the fluid level, slower in gas. Stop 10 min at TD.
6. **Repeat section (0.5 h).** Pull 200 m, re-log down. If drift is more than 0.1 C, mark the well "not at equilibrium" and plan a re-log.
7. **Purge (1-3 h, only where we sample).** Swab or bail 1-3 interval volumes from the perforations into the tank. Track EC on surface; stop when EC is stable.
8. **Sample run (1.5-3 h).** Sampler to the perforations, clock-trigger, pull, transfer to copper tubes and bottles on site.
9. **Rig down (1 h).** Leave wellhead as found. Haul purged fluid per operator's disposal (usually their SWD).

### 2d. Crew time per site (from `P10_calc.py`)

| Depth | Log only | Log plus purge-free sampler run | Add purge |
|---|---|---|---|
| 1 km | 5.1 h | 6.7 h | +1-2 h |
| 2 km | 7.3 h | 9.7 h | +1-3 h |
| 3 km | 9.4 h | 12.6 h | +2-3 h |

So: about 1.5 wells a day for log-only at 1-2 km, one 3 km well a day with a sample, and two days for a 3 km well with purge and sample. Marginal cost about $1.2-1.9k field per well plus about $0.9k lab when sampled. A season of 150 field days gives about 120-200 wells per unit.

---

## 3. Prior art

- **SMU Geothermal Lab** built and ran exactly this class of tool: a $5k e-line T tool (0.1 C, 4,000 m cable) and a $45k 400 C memory tool on a 7,600 m hydraulic slickline trailer (H02, https://smu.edu/-/media/site/dedman/academics/programs/geothermal-lab/documents/ttool-equipment-techniques.pdf).
- **North Dakota Geological Survey** logged temporarily abandoned oil wells for static temperature profiles of the Williston Basin from about 2014 (H02, https://www.dmr.nd.gov/ndgs/documents/newsletter/2019Winter/Williston_Basin_Static_Temperature_Logging_Program_Continues_to_Yield_Results.pdf). That is proof that operators let a third party log idle wells.
- **USGS and Sass-era heat-flow work** in the Great Basin relied on logging holes of opportunity (Sass et al. 1971; Lachenbruch and Sass 1977, cited in M23).
- **Project Hotspot (Kimama)** shows what one deep log through a lid reveals (https://gdr.openei.org/files/1442/EE0002848_%20Final_Report_Shervais.pdf).
- **Midcontinent calibration**: 33 equilibrium logs against about 500 BHTs left a gradient scatter of +/-5 C/km after Harrison (Blackwell, https://www.searchanddiscovery.com/abstracts/html/2004/annual/abstracts/Blackwell.htm). BHTs miss the hottest gradients, which are the ones we want.
- **Geothermal downhole sampling** with positive-displacement and flow-through bottles is routine in geothermal well testing (Kuster, Leutert, from memory, unverified). Nobody runs it as a regional exploration survey across idle oil wells.
- **Gap:** no company runs a fleet that logs idle western oil, gas, geothermal and TG wells to equilibrium for exploration. Service companies log for production, and the logs belong to the operator. Zanskar and Enverus buy BHT archives with the same 10-30 C error (H02). Zanskar drills its own holes in Nevada, which is the closest rival data stream.

---

## 4. How much it shrinks the model's ranked uncertainties

### 4a. Rank 5: temperature at 0.5-2 km (largest effect)

- **In a cell with a logged well:** T at 1.5 km goes from about 11-13 C (one uncalibrated BHT, predictive sd) to under 1 C. Extrapolation to the 3 km Tmin threshold (152 C at 3 km at $100/MWh, MODEL.md) goes from about +/-25 C to about +/-8-12 C, because we now have the gradient, not just a point.
- **Across Nevada plus western Utah:** about 1,300 oil BHTs, mostly 10-20 km apart (M04). If we log 150-300 open wells in two years in the 15-25% of high-lambda cells that hold them, and the column model spreads each log over about 5-10 km along structure, I estimate **the map-wide rank 5 log-width falls by 20-30%** (unverified, needs the GHOST Tier 1 sim to confirm).
- **Through TG and slim holes:** open TG and geothermal observation holes are shallow (100-600 m) but sit at prospects. Re-logging them years after drilling gives true equilibrium where the 1970s-80s logs were taken days after drilling. This is the M20 "full profile" prize, with our own truth.

### 4b. Rank 3: where the lid ends

- Each deep well that crosses a lid gives the kink depth to +/-10-30 m and a Peclet fit above it. With 20-40 such wells across the ESRP margin, western SRP, Railroad Valley and Pine Valley, we can calibrate the lid-thickness prior (and tie it to the E-MT conductor depth from the P03 nodes). I estimate **lid-thickness sd falls from about +/-400 m to about +/-150 m in basins with deep wells**, which is **15-25% of rank 3's total width**. It does nothing for ranges and pediments with no wells.

### 4c. The BHT cold-bias calibration saturates fast (new finding)

`P10_calc.py` treats the basin-era BHT bias as a normal-normal hierarchy (prior sd 8 C, per-pair scatter 6 C, both estimates). The bias sd falls from 8.0 C to 2.5 C at 5 pairs and 1.8 C at 10 pairs, then barely moves (1.3 C at 20, 0.9 C at 40). But a single corrected BHT keeps about 8 C of random scatter, so its predictive sd only drops from 11.3 C to about 8.1 C. **Plain reading: 5-10 paired wells per basin captures almost all of the "recalibrate every BHT" value. After that, a log helps only its own neighbourhood.** So the EVSI ranking should spend the first 10 logs per basin on calibration pairs and then switch to logging wells in high-lambda, low-P_det cells.

### 4d. Rank 1: deep or lidded catch rate

- The 2-5x on N comes from not knowing how often a deep system sits under a shallow blank. A deep idle well in a cell where the 2 m probes, ranch wells or shallow TG holes read cold is a direct test of P(hot at depth | shallow blank). It is one of the two detectors in the "designed two-detector survey" the model wants.
- Oil wells are not placed at random with respect to heat (oil follows structure and maturity), so they need a covariate-shift weight. They were not placed for heat either, which is what makes them useful as a nearly heat-blind sample.
- With 60-120 such "under-blank" wells, I estimate **10-20% of rank 1's log-width** shrinks, mostly in the carbonate and SRP provinces.

### 4e. Rank 2: permeability class

- Purged He R/Ra marks open deep paths (M22). Shut-in pressure plus a slickline bail-down and recovery gives a rough kh at the perforations (estimate: order-of-magnitude, enough to split Limited Distributed from Tight). Operator production and water-cut history adds real flow data on producers.
- I estimate **5-15% of rank 2** in logged cells. Rank 2 is mostly a fault-zone question, and oil wells sit in basin fill and carbonates, so this is a modest share.

### 4f. Rank 4: sensor reliability

- Each deep log next to ranch wells, darts and E-MT nodes gives a truth label for those shallow sensors. Ten to twenty such pairs feed the 20/40 calibration campaign. Modest but cheap: about **5-10% of rank 4**.

### 4g. Effect on the regional total

The SRP, the eastern carbonate province and the Railroad Valley-Pine Valley belt are where the model expects hidden MWe to move up (MODEL.md). Those are exactly the places with deep wells and cold shallow data. So this unit is the most direct test of the model's biggest expected upward revisions. If 5 of the first 50 logs read more than 20 C above their pre-registered median at 1.5 km, the F5/F95 band in those provinces should narrow and shift up (estimate).

---

## 5. Rights edge

**What is true.**
- A federal oil and gas lease does not convey the geothermal right. Geothermal is leased separately under the Geothermal Steam Act (R01, R02).
- **But** a federal oil and gas lessee producing hot fluids can get a **noncompetitive geothermal lease for co-production** on that lease (30 USC 1003(c), added by EPAct 2005 section 222; check exact text and 43 CFR 3200 rules, unverified). Blackburn already used a BLM pathway for well conversion (A04). So on the lease itself, the operator holds the inside track.
- A mining claim conveys no heat right (30 USC 1022, P07). Same logic for the land around the oil lease: **adjacent unleased BLM parcels are open** to our nomination, or to a leftover $1/ac/yr noncompetitive lease after an auction with no bids (R02).
- Private and state land follow state law. Texas SB 785 (2023) gives the surface owner the heat (H02, R07). Nevada and Utah details vary (R06, unverified).

**How we use it.**
1. **Log, then lock the ring.** A hot log tells us about a 5-10 km footprint along structure. We nominate or first-file the unleased federal and state cells in that ring, and option private ranch heat at $1-2/ac, before the operator or anyone else sees an interpretation. The operator gets raw integrity numbers; the interpretation is ours (contract term).
2. **Partner, do not bypass, on the lease.** Offer the operator a free log and a carry or $/MWh share if they use the co-production right, in return for a wellbore option and data rights. They gain from telling us.
3. **Plugging pressure is the sweetener.** Texas SB 1150 forces 15-year-idle wells to plug or return to use from 1 Sep 2027 (H02). EPA rules list a temperature log as one way to show external mechanical integrity for injection wells (40 CFR 146.8(c), https://www.ecfr.gov/current/title-40/chapter-I/subchapter-D/part-146/subpart-A/section-146.8). For SWD and idle-well operators, our log has a compliance value. That buys access at no cash cost.

**Leaks.** A hot log is known to the operator, the operator's landman, and anyone who reads a sundry notice if one is filed. Nevada makes O&G log headers public (NAC 522, D03). So we lock the ring within days of a hot log. Data we take on unleased federal land need not be filed (43 CFR 3253.10(b), hardware MEMO), but this is a log on someone else's lease, so the contract, not that rule, protects us.

---

## 6. Is the western well pool big enough? (the "too small" test)

| Pool | Open and reachable (estimate, unverified) | Relevance to blind hydrothermal |
|---|---|---|
| Railroad Valley, Pine Valley, Blackburn, other NV producers and shut-ins | 80-200 | Highest. Known blind heat (M25) |
| NV and UT wildcats left open (TA or unplugged orphans; NV 63 and UT 72 documented orphans, H02) | 30-100 | High. Many in high-lambda basins |
| Western Snake River Plain gas wells, Payette County ID | 15-40 | High. Lidded province with high heat flow |
| Uinta and Paradox margin shut-ins, UT | 300-1,500 | Medium. Sedimentary heat, some fault-fed |
| CalGEM long-term idles in hot margins (Salton, Coso, Kern, Long Valley edges) out of 15,922 long-term idles statewide | 100-500 | Medium to high |
| Idle geothermal observation and slim holes (NDOM 938 permitted; CalGEM; UT) | 100-300 | High for step-outs; prospect itself often leased |
| Open TG and research holes | 50-200 | High, shallow |
| **West total** | **about 600-2,500** | |
| Texas, Gulf, Midcontinent, orphan pre-plug logging (10,257 orphans plugged with federal money through FY2025, H02) | 10,000+ | Sedimentary and EGS siting, the scale market |

A pool of a few hundred high-relevance wells in the West is enough for calibration (Section 4c says 5-10 per basin buys most of the bias gain) and for direct tests in the provinces where the model expects upward moves. Scale comes from the sedimentary and pre-plug market, which also suits Fervo-, Sage- and XGS-type buyers.

---

## 7. Risks

1. **Equilibrium is rarer than hoped.** Many "idle" wells were worked over or flowed recently. Mitigation: six-month filter and the TD repeat check. Kill if more than 50% of logged wells fail the drift check.
2. **Sampler returns casing brine.** Mitigation: perforation purge and tritium plus EC checks; use flowing producers first. Kill the sampler (not the logger) if fewer than 40% of purged samples pass tritium and charge-balance checks.
3. **Operator refusal and liability.** H02's kill: fewer than 20% yes after 50 asks. Mitigation: own insurance, certified operator, compliance-value offer.
4. **Lost tool in the hole.** Fishing a slickline string can cost more than the job. Mitigation: drift run, jars, insurance, and never log wells with known collapsed casing.
5. **Co-production preference lets the operator take the lease.** Mitigation: lock the ring, carry the operator.
6. **Thin western pool and selection bias.** Oil wells sit in basins, not on range-front faults. Mitigation: covariate-shift weights in CREAM-COX; this is a deep anchor, not a full-coverage detector.
7. **Safety and permits.** H2S, pressure, remote sites. Some states may want a sundry notice for wireline work on federal leases (BLM Form 3160-5, unverified). Hire an experienced operator for year one.
8. **Kill rule from H02 still holds:** if most logs fall within 5 C of calibrated BHTs, the edge shrinks to direct logs only.

---

## 8. Cheapest first test

**Phase 0 (desk, 2 weeks, about $0):** Pull NDOM, UT DOGM, IDL and CalGEM status tables; list open wells idle six months or more in high-lambda cells; pre-register predicted T(z) and bands from the frozen model for the top 40.

**Phase 1 (rent first, 4-6 weeks, about $30-50k):** Rent a slickline unit with operator for 10-12 days and buy or rent one pair of 177 C memory gauges plus one sampler. Target 10-15 wells in Railroad Valley-Pine Valley and Payette County with one or two operators. Pass if: (a) 10 or more logs pass the drift check; (b) 3 or more differ from calibrated BHTs or the model's pre-registered median by more than 8 C at 1-2 km; (c) 1 or more operator signs a wellbore option or carry; (d) 3 or more purged samples pass tritium and charge balance. Then buy the used unit (weeks 6-14) and refit.

**Build time:** about 8-14 weeks for v1 (used unit search and refit 4-8 weeks, sampler build 4-6 weeks in parallel, gauge lead time 2-8 weeks, unverified).

---

## 9. Self-scores (1-5)

| Axis | Score | Why |
|---|---|---|
| model_uncertainty_alpha | 3.5 | Best direct hit on rank 5 and the lid end (rank 3) in exactly the provinces the model expects to move up. Docked because the western pool is thin and the bias calibration saturates fast |
| rights_alpha | 3 | Ring-locking around a hot log and private-heat options are real. Docked for the co-production preference and NV header disclosure |
| buildability | 4 | Off-the-shelf oilfield kit, rent-first test, 8-14 weeks, a two-person crew. Needs one certified operator |
| cost_scale | 3 | $170-280k per unit, $2-3k per well, 120-200 wells per unit-year. Fine, but each well is not cheap compared with a 2 m probe |
| moat | 3 | The data is private and operator relationships compound. The method is public and service firms could copy it |

## Sources

- SMU Geothermal Lab tool and trailer specs: https://smu.edu/-/media/site/dedman/academics/programs/geothermal-lab/documents/ttool-equipment-techniques.pdf (via H02)
- SMU BHT calibration: https://smu.edu/dedman/academics/departments/Earth-Sciences/Research/GeothermalLab/DataMaps/GeothermalMapofNorthAmerica/BHTCallibrationPoster (via H02)
- Blackwell Midcontinent comparison: https://www.searchanddiscovery.com/abstracts/html/2004/annual/abstracts/Blackwell.htm
- ND static temperature logging program: https://www.dmr.nd.gov/ndgs/documents/newsletter/2019Winter/Williston_Basin_Static_Temperature_Logging_Program_Continues_to_Yield_Results.pdf
- Peters and Nelson 2009 (Horner error): https://www.searchanddiscovery.com/abstracts/html/2009/hedberg/abstracts/extended/peters/peters.htm (via M04)
- Lachmar et al. 2017, Kimama: https://link.springer.com/10.1186/s40517-017-0086-8 ; Project Hotspot: https://gdr.openei.org/files/1442/EE0002848_%20Final_Report_Shervais.pdf (via M23)
- USGS DR1167 orphan wells: https://pubs.usgs.gov/publication/dr1167/full (via H02)
- California idle wells: https://www.fractracker.org/2024/05/california-must-improve-management-of-idle-wells (via H02)
- Texas SB 1150 analysis: https://capitol.texas.gov/tlodocs/89R/analysis/html/SB01150F.htm (via H02)
- Weatherford Quantum memory gauge: https://www.weatherford.com/drilling-and-evaluation/wireline-products/cased-hole-formation-evaluation/quantum-150c-piezo-memory-gauge/ ; ProbeSensonix: https://probesensonix.com/downhole-memory-gauges (via H02)
- 40 CFR 146.8 mechanical integrity: https://www.ecfr.gov/current/title-40/chapter-I/subchapter-D/part-146/subpart-A/section-146.8 (from memory, not re-read this turn)
- Railroad Valley heat sink: https://pubs.usgs.gov/publication/70205980 (via M04)
- Kennedy and van Soest helium: https://escholarship.org/content/qt67p1z91d/qt67p1z91d.pdf (via M22)
- Unsourced (unverified): 30 USC 1003(c) co-production wording; Leutert and Kuster sampler specs and prices; used slickline unit prices; gauge time constants; western open-well counts in Section 6.
