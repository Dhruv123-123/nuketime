# P07: Drill-Rig Ride-Along. Free core-barrel memory pucks plus pay-per-hole grout-in thermistor strings

Date: 23 Oct 2026. Build candidate P07, model track. This builds on `M20-tg-and-mining-holes.md` (the ride-along idea first appeared there as a one-paragraph note; NBMG mining-well temperatures; Meikle 140-160 C rock), `M04-bht-corrections.md` (Horner rules and error ladder), `../../evidence/D06-mining-assessment.md` (NREL 2022: more than 2,000 mining holes a year in Nevada, no temperature duty, McGinness and Blue Mountain found by miners), `../../evidence/R13-mineral-claims-overlap.md` (30 USC 1022: a mining claim conveys no heat right), `../../evidence/R02-blm-noncompetitive.md` ($1/ac/yr leftover leases), `../../../hardware/evidence/H11-own-gradient-rig.md` and `H13-permits-and-secrecy.md` (NAC 534A, IM 2026-024, the leaks are permits, not sensors), and the prior hardware pick in `../../../hardware/MEMO.md`.

**Method note.** The shared web-search budget for this workflow turn was already used up before this agent's first query (all three searches were refused). So no new web sources were read. Everything here comes from sibling files in this repo (which cite primary sources) and from what I know. Every number not traced to a sibling file is marked (unverified). The NAC 534 section numbers in particular must be checked against the live code before any contract is signed.

---

## Bottom line

- **The idea is sound and cheap, and it is the only candidate so far that turns somebody else's drilling budget into our deep truth data.** Nevada's mining industry drills more than 2,000 holes a year to the same depths as geothermal gradient holes (NREL 2022, via D06), and almost none of them gets a usable temperature. A $250 memory puck that rides on the core barrel inner tube, plus a $2-4k grouted string in the few hot holes, gives us 150-600 m temperatures for about 1-3% of the cost of our own gradient hole.
- **Physics: it works, with one twist.** A puck that rides the core barrel mostly sees circulating fluid, not rock. The useful data come from three moments that happen anyway: (1) the free-fall of the inner tube down a hole that stood overnight or over a shift change (a partly recovered T(z) log of the whole fluid column), (2) the first minutes at the bottom before the pumps restart, and (3) end-of-hole survey runs. Several stand times per hole allow a Horner fit to about +/-2-5 C (M04). That is ample: a blind system at 500 m depth makes the hole 10-30 C hotter than background at 300 m.
- **The grouted string is the gold standard.** A fully grouted string cannot convect and has no in-hole flow, so after weeks to months it gives an equilibrated T(z) to +/-0.05-0.1 C. The mining industry already grouts vibrating-wire piezometers (which carry a thermistor) fully into exploration holes for pit-slope hydrology. That is the legal and practical precedent for our string (Mikkelsen and Green 2003; practice at Nevada mines is (unverified)).
- **Model value: it attacks ranks 1, 4 and 5, and partly 3.** Mining holes are placed for gold, not heat, and every hole is logged whether or not it is hot. That gives a pre-registered, effort-recorded detector that punches through cold groundwater lids. It is the closest thing to an unbiased "designed survey" we can get for free. My estimate: in mining-belt cells it narrows the lidded catch-rate factor (rank 1) by 30-45% of its log-width in two years, and by 15-25% statewide. It gives 30-60 paired truth holes for Sentinel reliability (rank 4), and it cuts the T at 0.5-2 km error (rank 5) by 30-50% in cells that have a hole.
- **Rights edge: strong, and it is the cleanest in the set.** A mining claim conveys no heat (30 USC 1022). So a hot hole on unleased BLM land is ours to nominate (or to take at $1/ac/yr if the parcel goes unsold), and the claim holder cannot block it. On patented claims and private land the heat belongs to the surface owner (NRS 534A.050), so we fold a geothermal option or ROFR into the same data contract. We give the claim holder a small carry, so they gain from telling us and not from nominating on their own.
- **Main risks:** (a) most Nevada exploration holes are RC (air), not core, so the core-barrel puck reaches only part of the pool (we add an RC drop-puck variant); (b) contractors and claim holders must sign, and juniors worry about disclosure; (c) NAC 534 plugging must accept a sensor string inside approved grout; (d) mining holes sit in mining belts, so the sample covers only part of the high-lambda map and needs a covariate-shift penalty.
- **Self-scores:** model_uncertainty_alpha 4, rights_alpha 4, buildability 4, cost_scale 4, moat 4.

---

## 1. Physics: what a ride-along puck actually measures

### 1a. The three useful moments in a core hole

Diamond core drilling (NQ 76 mm, HQ 96 mm holes) uses a wireline core barrel. The inner tube is lowered (free-fall or pumped down) through the drill rods, latches at the bit, cuts one run of 3 m or 6 m, and is pulled back up by an overshot on a wire. A typical Nevada core hole of 300-600 m takes 5-20 rig-days, and the inner tube makes 50-200 trips (unverified, standard practice). A puck mounted on the inner tube back end (where core orientation tools such as the Reflex ACT already ride on every run) sees:

1. **The descent profile.** Each trip, the puck falls through the fluid column inside the rods at about 1-3 m/s (unverified). With a 1 Hz or faster sample and a pressure sensor for depth, each trip is a fast T(z) log of the fluid in the rods. During drilling the column is well mixed and nearly isothermal, so most descent logs are weak. **But the first trip after the rig stood idle (shift change, overnight, weekend, repairs) is a partly recovered log of the whole hole.** Nevada rigs often run 12 h shifts or stop overnight, so a typical hole gives 3-15 such "stand logs" at different stand times (unverified).
2. **Bottom dwell before circulation restarts.** After the inner tube latches, there is usually a short pause before the pumps start. The puck records the bottom temperature rising toward rock temperature. With a slim puck (small thermal mass) the time constant is a few seconds to tens of seconds (estimate).
3. **Drilling-run temperature.** While drilling, the bottom temperature is the mud temperature plus a small offset. It mostly tracks the circulating fluid, but steps in it at constant pump rate flag hot fluid entering the hole. That is the **lost-circulation plus temperature-step signal**: when the bit hits an open, hot fracture, fluid is lost (driller notes it), and the bottom temperature jumps by 1-10 C and then drifts (estimate). Hot permeable fractures are exactly what the model's rank 2 (permeability class) lacks.

### 1b. Horner and recovery fit

For a line source, the temperature after the pumps stop follows

T(dt) = T_inf - A x ln((t_c + dt) / dt),

where t_c is the circulation time before the stop and dt is the time since the stop (Bullard 1947; Lachenbruch and Brewer 1959). We know t_c and dt to the second from the puck's own clock and accelerometer, which is the one thing legacy BHTs never had (M04: missing time since circulation is the main error). With 3 or more stand times at about the same depth, M04 gives about +/-2-5 C true error (Peters and Nelson 2009). The puck also gives the full early recovery curve, so we can fit a full cylinder-source model with mud and rock diffusivity rather than a straight Horner line.

### 1c. Is the signal big enough?

- Background Basin and Range gradients are about 30-45 C/km (M04, L09). A blind system with a lid can show 60-150 C/km below the lid (M18, M20: Florida Canyon water at 93-132 C at 230-240 m; NREL's central-Nevada prospect at about 10.5 F/100 ft, roughly 190 C/km, against 2-3 F/100 ft background).
- At 300 m with a 15 C surface: background is about 24-29 C, a lidded system is about 35-60 C. The difference is 10-30 C. A Horner-corrected puck reading at +/-3-5 C separates these at 2-6 sigma. A single uncorrected stand log (+/-8 C) still flags the hottest cases.
- The string (+/-0.1 C at equilibrium) measures the gradient below the lid to about +/-1-2 C/km over 100 m. That is good enough to fit curvature and Peclet number (rank 3) and to extrapolate to 1-2 km (rank 5).

### 1d. Why a grouted string beats an open hole

- **No convection.** Open water-filled holes over about 75-100 mm convect at gradients above a few tens of C/km, adding 0.01-0.5 C noise (estimate). Grout removes that.
- **No in-hole flow.** Open holes connect aquifers. Flow up or down the hole smears the profile, which is the same problem that plagues ranch wells (92% flow-disturbed share in the model's predictive checks). A grouted hole is sealed by rule, so the string reads the rock.
- **Equilibrium time.** Disturbance after drilling decays roughly as t_c/dt. For a hole drilled over 5-20 days, the error falls below 0.1-0.3 C after about 2-6 months (Lachenbruch and Brewer 1959 scaling, estimate). Continuous logging lets us fit the recovery and get a good estimate in 2-4 weeks.
- **Grout heat.** Neat cement heats the hole by several C for 1-3 days as it sets (unverified size). Bentonite or bentonite-cement grout adds little. We ignore the first week of data.

### 1e. RC holes (the bigger pool)

Most Nevada exploration metres are reverse circulation (air, sometimes with water injection), not core (unverified share, my guess 60-80%). The bit is a hammer, the hole is often dry above the water table, and there is no inner tube. Three fixes:

- **End-of-hole drop puck.** Before the rods are pulled, the driller drops a puck on a light wireline or on the gyro survey tool and leaves it at the bottom for 10-20 min. That gives one bottom temperature with known dt plus a descent log through any water column. Rig time about 15-25 min, which we pay for.
- **Ride with the gyro survey.** Many RC and core holes get an end-of-hole gyro survey. Strap the puck to the gyro. Zero extra rig time.
- **String the hot ones.** RC holes are plugged with grout too, so the string step is the same.

### 1f. Detection limits (one table)

| Reading | Depth | Error (1 sigma) | Main error source |
|---|---|---|---|
| Single stand log, unknown recovery | 0-600 m | +/-5-10 C, biased cold | Short stand time |
| Horner fit, 3+ stand times | bottom at each stand | +/-2-5 C | Mud diffusivity, hole deviation |
| LOC + temperature step flag | depth of fracture | flag (yes/no), 1-10 C step | Driller notes, pump-rate changes |
| RC end-of-hole drop puck, 15 min | bottom | +/-5-8 C | One time point only |
| Grouted string, 2-4 weeks, recovery fit | 0-600 m, 10-20 m spacing | +/-0.2-0.5 C | Fit model |
| Grouted string, 3+ months | 0-600 m | +/-0.05-0.1 C | Sensor drift, calibration |

All errors are my estimates from M04's ladder, (unverified) for this exact setup.

---

## 2. Prior art

- **Bottom-hole temperatures in oil wells (BHT).** The whole BHT correction field (Horner, Harrison, Cooper-Jones; M04) is built on readings taken during logging runs. We do the same with better metadata.
- **Core orientation tools.** Reflex ACT and Boart Longyear TruCore ride on every core run at the inner tube back end, with batteries and memory (industry standard; whether they log temperature is (unverified)). They prove the mounting, the shock environment and the driller habit. A partnership that adds a thermistor to one of them is the fastest path to scale.
- **Directional-survey tools.** Most magnetic and gyro survey tools have an internal temperature sensor for drift compensation. M20 flags whether contractors' clouds keep those readings as the single most valuable data-deal question. NREL used one claim holder's deviation surveys at a central-Nevada prospect and saw a clear thermal anomaly (74 holes, 151 F max; D06, L16). That is a proof of concept for the data, though with no stand time recorded.
- **Fully grouted piezometers.** Mines and geotech firms routinely grout vibrating-wire piezometers straight into boreholes (Mikkelsen and Green 2003). Each VW piezometer contains a thermistor. So many Nevada mines already own deep, equilibrated temperature points they do not use (inference, unverified). Asking for those is a free data deal.
- **Permafrost thermistor strings.** The Global Terrestrial Network for Permafrost uses grouted or sealed thermistor strings for long-term T(z). Lachenbruch's USGS Alaska work used sealed holes for climate reconstruction. Same idea, colder.
- **Geothermal TG completions.** 1970s-80s TG holes were completed with a 1 inch capped, water-filled pipe and re-logged (M20, L16). Our cheaper "string-lite" option copies this.
- **Australian and Canadian mineral holes.** Australia's hot-rock boom and its heat-flow mapping used temperature logs in mineral exploration holes (D06, SARIG, (unverified detail)).
- **Gap.** I know of no program that instruments mining exploration drilling for geothermal at scale in the US. Zanskar's public material shows its own TG holes and public data, not mining ride-alongs (D06, Z03; (unverified) as to its internal work). NREL's 2022 Mining G.O.L.D. report explicitly calls the mining data untapped (D06).

---

## 3. v1 design

### 3a. Puck-C (core barrel puck)

| Item | Spec | Unit cost (100 units, unverified) |
|---|---|---|
| Housing | 17-4PH stainless tube, 25 mm OD x 160 mm, rated 35 MPa (3,500 m water), O-ring endcaps; fits the inner tube head extension or a short adapter sub | $40-70 |
| Temperature | PT1000 thin-film in a thin-wall nose, 3-wire, ratiometric 24-bit ADC; +/-0.05 C after cal; time constant under 10 s in water | $15-30 |
| Pressure | 0-20 MPa silicon-on-insulator gauge, 150 C rated; gives depth to about +/-1-2 m | $60-150 |
| Motion | 3-axis accelerometer; tags trips, latch, drilling vibration and pump state | $5 |
| MCU and memory | AEC-Q100 grade-0 (150 C) low-power MCU, 8-16 MB flash or FRAM (2 weeks of 1 Hz data) | $15-30 |
| Battery | High-temperature Li-SOCl2 1/2AA or AA cell rated to 150 C | $15-30 |
| Data port | Two sealed contact pads or an IR window on the back cap | $5-10 |
| Assembly, potting, cal | Batch cal in a stirred bath at 5 points | $30-50 |
| **Total** | | **about $190-380** |

- **Power.** Sampling at 1 Hz with the ADC duty-cycled averages under 50 uA. A 1.2 Ah cell lasts more than 2 months at 150 C derating (estimate). Swap the cell at each hole.
- **Rating.** Grade-0 parts and the cell top out near 150 C. Holes hotter than that are already a discovery; the puck may die but the stand log before it dies says so.
- **Comms.** None downhole. At the rig, the driller's helper drops the puck in a dock (contact pads) when the inner tube comes up for core, or at shift end. The dock is a small rugged box with a cellular or Starlink-shared modem, or it syncs to a phone app. The app also asks the driller two taps per shift: "lost circulation? (Y/N, depth)" and "hole stood idle? (hours)". The puck's accelerometer cross-checks both.
- **Mounting.** v1: a short adapter sub between the inner tube head assembly and the inner tube, with the puck in a slot. v2: integrate into an orientation tool via the tool maker.

### 3b. Puck-R (RC drop puck)

Same electronics in a heavier 38 mm OD sinker body (1.5-2 kg) with a swivel, run on a 3 mm wireline or strapped to the gyro tool. Cost about $250-450. One per rig.

### 3c. String-T (the grout-in thermistor string)

Two options, chosen per hole:

- **String-T full (digital).** 30-60 sensor nodes at 10-20 m spacing, closer near the bottom and across the lid, on a 4-conductor armoured cable with FEP or PFA jacket and a steel or aramid strength member. Each node is a small potted capsule with a glass-bead NTC thermistor or a 150 C digital sensor and an address chip. Cable runs to a buried surface box (logger, lithium pack, Iridium SBD or LoRa link, solar trickle optional). One reading per sensor every 6 h. Lowered on a sinker bar through the rods or the open hole, then the driller grouts from the bottom up with a tremie as the plugging job requires. Parts: nodes $20-40 x 40 = $0.8-1.6k; cable $3-6/m x 300 m = $0.9-1.8k; surface box $300-500. **Total about $2-4k for 300 m, $4-6k for 600 m (unverified).**
- **String-lite (tube).** A 25 mm HDPE or 1 inch steel tube, closed at the bottom, water-filled, grouted in place, capped below grade in a small monument. We re-log it any time with the existing drop probe from the prior hardware pick. Parts about $2-4/m, so $0.6-1.2k for 300 m. Cheaper and re-loggable forever, but it is an open (if sealed) tube inside the plug, so it is more likely to need a monitoring-well waiver (section 6).
- **Add-on.** A VW piezometer at the bottom (about $500-900, unverified) gives head and earth-tide response, which feeds rank 2. Mines already know how to install these.

### 3d. Deployment and crew time

| Step | Who | Time |
|---|---|---|
| Sign contractor master agreement and claim-holder data/heat contract | Our landman + BD | 2-8 weeks per company (once) |
| Ship 4-6 pucks + dock to a rig | Us | Mail |
| Fit adapter sub, train helper (15 min video) | Driller | 30 min per rig, once |
| Dock pucks at shift end, two taps in app | Driller helper | 2-3 min per shift |
| RC drop at end of hole | Driller | 15-25 min per hole (paid) |
| Auto-flag hot holes, send to our geologist | Software | Same day |
| String install at plugging | Driller + our tech on site | 1-3 h rig time per hole, our tech 1 day including travel |
| Read strings remotely | Software | None |

### 3e. Payments and budget

- **Puck holes:** puck amortization $30-60 (lose about 1 in 20; batteries), driller incentive $100-200 per hole, data handling $20-50. **About $200-350 per hole**, which matches the brief.
- **Strung holes:** string $2-4k, rig time 1-3 h at $400-700/h ($0.4-2k), our tech $500. **About $3-6k per hole.** At the high end this is above the brief's $1-5k; String-lite brings it to $1.5-3k.
- **Year-1 program (Nevada):** 400-600 puck holes ($0.1-0.2M), 30-50 strings ($0.1-0.25M), 2 FTE field and data ($0.3M), 200 pucks and 30 docks built ($0.06-0.1M). **About $0.6-0.85M per year.** One of our own TG holes is $100-300k all-in (M29), so the whole program costs about 3-6 TG holes.

---

## 4. How it enters the model (SENTINEL-COX)

- **New THERMOS-B source types,** each with its own likelihood: (a) stand log with known dt and t_c (skewed lower-bound likelihood, bias prior from M04 learned on our own pairs); (b) Horner set (Gaussian, +/-2-5 C); (c) LOC+step flag (Bernoulli on "hot permeable fracture at z"); (d) String-T at equilibrium (Gaussian, +/-0.1 C, full T(z) with curvature). Strings also calibrate the puck bias, so each strung hole improves every puck reading in that basin.
- **A fourth CREAM-COX detection channel: "mining ride-along".** Every instrumented hole is a detector with a known depth and a known date, logged whether hot or not. Holes are placed by gold geology, so selection is close to ignorable after conditioning on mineral-prospectivity covariates (MRDS density, epithermal age, structure). We fit that propensity explicitly. This gives the model what it lacks: effort-recorded looks below the lid, not chosen for heat.
- **Lidded catch rate (rank 1).** For each hole that is hot at depth, we check which other detectors (springs, 2 m probes, USGS favorability, our GBM, Sentinel wells) also saw it. The ratio across many hot and cold holes is a direct estimate of P_det by mask class. This is the "designed two-detector survey" the model asks for, run on someone else's rigs.
- **GHOST Tier 1.** Simulate stand logs and strings in synthetic Nevadas, and rank the puck against the Sentinel by EIG per dollar before scaling.

---

## 5. How much it shrinks the ranked uncertainties (my estimates, untested)

Base numbers: 400-600 puck holes a year in about 50-100 projects (20-30% of Nevada's 2,000+ holes through 3-5 contractors, (unverified) capture rate). New ground covered: about 300-600 km2 a year of mining-belt terrain. If undiscovered systems cover about 0.3-1.5% of Nevada at the 500 m halo scale, and mining belts are 2-3x enriched (Blue Mountain, McGinness, Florida Canyon were all found by miners; D06), we expect **3-10 hot flags a year** and several hundred depth-censored cold holes.

| Rank | Uncertainty | Effect | Rough shrink |
|---|---|---|---|
| 1 | Detection gap / lidded catch rate (2-5x on N) | 15-25 hot holes and about 1,000 cold holes in 2 years, each checked against every other detector. Binomial error on the catch-rate ratio about +/-25% relative. | 30-45% of log-width in mining-belt cells; 15-25% statewide after a covariate-shift penalty. The 2-5x factor moves to about 1.6-3.5x. |
| 4 | Sensor reliability s/q by mask class | 30-60 strung holes give equilibrated truth. Pair each with nearby ranch wells and 2 m probes. Truth is not chosen by the sensors it tests. | 25-40%. It does not replace the 20/40 calibration campaign but adds 30-60 "accidental" sites to it, half of them cold controls for free. |
| 5 | T at 0.5-2 km | Holes reach 150-600 m (some 1 km). Strings give curvature for extrapolation. | 30-50% in cells with a hole; about 5-10% statewide. |
| 3 | Masking / lid thickness | Holes cut through the lid and show its base directly. | 30-50% locally. |
| 2 | Permeability class | LOC + temperature step marks hot open fractures; VW piezometer add-on gives tidal response. | 10-15%. |
| 6 | Upflow location | A hot hole gives a point inside or near the outflow plume; reversals give direction. | 10-20% locally. |

For the buyer metric (F5/F95 narrowing per 100 visits), 100 puck holes are worth fewer bits than 100 Sentinel visits each, but they cost about one tenth as much and they see below the lid. So per dollar I expect this to be the top or second item in the Tier 1 EIG ranking for mining-belt cells (to be confirmed in silico).

---

## 6. Legal access

- **Who owns the hole and the data.** The claim holder (the exploration company) owns the hole, the core and the data. The driller is its contractor. So the contract is three-way: claim holder consents and owns raw data jointly with us; the driller gets the per-hole fee; we get an exclusive licence for geothermal use plus the heat terms in section 7.
- **BLM surface.** Drilling on a claim is the claimant's 43 CFR 3809 notice or plan of operations, not ours. A puck adds nothing to the disturbance. A string left in a plugged hole is a permanent object on federal land. IM 2026-024 covers "battery sensors in small holes" under 10 ft (H13), not a 300 m string. So the surface box needs either BLM consent under the claimant's reclamation plan or a short geothermal NOI on our side, which is public (H13). Workaround: cut the cable 1 m below grade in a flush, buried connector (no surface box, no visible footprint) and read it on visits; this needs a field-office check (unverified).
- **Nevada plugging (NAC 534, the main item).** The State Engineer's rules require mineral exploration boreholes to be plugged with approved material (cement grout, bentonite grout or bentonite chips) and a plugging report filed (NAC 534; I could not fetch the exact sections this turn, so the section numbers and timing rules are (unverified); check NAC 534.4365-534.4371 and the "borehole" definitions at https://www.leg.state.nv.us/NAC/NAC-534.html). The two questions are: (1) does a fully grouted String-T still count as a plugged hole? The precedent of fully grouted VW piezometers at mines suggests yes or "yes with a waiver" (unverified). (2) Does String-lite (a capped tube) count as a monitoring well needing a waiver and a licensed driller? Probably yes (unverified).
- **NAC 534A / NDOM.** If the string is installed "for geothermal exploration", NDOM may treat the hole as a thermal gradient well that needs a $100 TG permit under NRS 534A.060 (red-team file). That permit is public (a leak), but filed data stays confidential for 5 years (NRS 534A.031) and temperature logs are required (NAC 534A.550). Lowest-leak design: the string is part of the claimant's hydrology and hole-abandonment program (it reads temperature as a by-product, like a VW piezometer). Get an attorney memo first (about $5-10k, H13).
- **Other states.** Utah, Idaho, Oregon and Arizona each have their own exploration-hole plugging rules (unverified). Start in Nevada only.

---

## 7. Rights edge

- **Federal land.** A mining claim gives no right to heat (30 USC 1022; R13). The claimant has no priority on a geothermal lease. A hot hole on unleased BLM land lets us nominate a block (padded with decoys, H13). If it goes unsold at auction, we take it noncompetitively at $1/ac/yr plus about $520 (R02). The claimant's 1005(e) mining-plan rule protects the claim, not a rival lessee.
- **Patented claims and private land.** The surface owner owns the heat unless reserved (NRS 534A.050). Many Nevada mines sit on checkerboard railroad land and patented claims. Our data contract includes a geothermal option or ROFR on all private and patented ground in the project, signed on day one, before any reading exists. Price it at $1-2/ac with a carry (fits the bank's terms).
- **The carry that buys silence.** The claim holder gets 10-25% of our net geothermal proceeds from any parcel its hole flagged (structure to be priced). That beats nominating alone: a junior has no geothermal team and no buyer list. Without it, the junior could nominate itself or sell the data to Zanskar.
- **Speed.** We see the hot hole the same day the driller docks the puck. No public filing exists. The edge window is the time from hot puck to nomination, which we control.
- **Size of the prize.** If 3-10 hot flags a year turn into 1-3 lockable prospects a year, and each prospect is worth $0.3-3M as an option at the anomaly stage (bank estimates, unverified), the rights value is $0.3-9M a year against $0.6-0.85M of spend.

---

## 8. Risks

1. **RC dominance.** If 70-80% of holes are RC with no water column, the core puck covers only the core minority. Puck-R and the gyro strap fix part of it, but RC bottom readings are single-point and noisier.
2. **Signing contractors and claim holders.** Juniors fear disclosure rules (NI 43-101, TSX-V) and dislike third parties on their data. Drillers fear any delay. The fee, the carry and "free hole temperature for your hydrology" must outweigh this. Expect 30-60% refusal (unverified).
3. **Geographic bias.** Mining belts (Carlin, Battle Mountain-Eureka, Getchell, Walker Lane) cover only part of the high-lambda map. The rank 1 estimate must carry a covariate-shift penalty, and it says little about the Snake River Plain or the Cascades.
4. **Plugging law.** NAC 534 may treat a tube as a well, or require cement types that complicate the string. Fallback: puck-only program plus VW-piezometer data deals.
5. **Copycats.** The puck is easy to copy. Zanskar or a survey-tool maker could offer the same. The moat is exclusive contracts and the install base, not the hardware.
6. **Hole depth.** Many holes stop at 150-300 m, above the reservoir. They still give gradient and lid data, but rank 5 depends on strings in the deeper holes.
7. **Gold cycle.** Drilling volume follows the gold price. At today's high gold prices drilling is strong (unverified), but a crash cuts the stream.
8. **Hot-hole safety.** Hot fluid in a hole is a driller hazard. A hot puck reading may cause the claimant to stop or plug fast, which shortens stand times.

---

## 9. Cheapest first test

**Weeks 0-8, about $15-30k.**

1. **Desk (weeks 0-3, about $5-8k):** attorney memo on NAC 534 plugging, String-T as plugged, String-lite as monitoring well, and NDOM's view (one email and one call to each office). Pull NDWR plugging and waiver records for fully grouted piezometers at Nevada mines.
2. **Data deal probe (weeks 0-4, $0):** ask 2 mines for their VW piezometer thermistor records and ask 2 survey contractors whether their clouds keep tool temperature. A yes from either is free equilibrated or semi-equilibrated deep data.
3. **Off-the-shelf pilot (weeks 2-8, about $8-15k):** buy 8-10 commercial 140-150 C stainless memory loggers (for example MadgeTech HiTemp140-class, unit price and pressure rating (unverified)) and strap them inside a short adapter sub on one cooperative junior's core program for 4 weeks. Pay $150/hole. Also do 5 RC drop runs.
4. **Truth check:** re-log 3-5 of the same holes with our drop probe before plugging, or grout one String-lite and log it at 2 and 6 weeks.

**Pass if:** at least 80% of runs give clean records; Horner fits from 3+ stands land within 3 C of the re-log; the driller time cost is under 5 min per shift; the claim holder signs a heat ROFR clause. **Fail if:** drillers refuse after the pilot, or the stand-log error exceeds 8 C after correction.

---

## 10. Self-scores (1-5)

| Axis | Score | Why |
|---|---|---|
| model_uncertainty_alpha | 4 | Direct, effort-recorded, below-lid truth for ranks 1, 4, 5, 3. Limited to mining belts. |
| rights_alpha | 4 | Claim conveys no heat; private ground option in the same contract; same-day private signal. Needs the carry to keep claimants loyal. |
| buildability | 4 | Puck is a simple memory logger, a few weeks to prototype; pilot can use off-the-shelf loggers. Strings need cable work and a legal memo. |
| cost_scale | 4 | $200-350 per puck hole, $3-6k per string, against $100-300k per TG hole. Volume is capped by mining drilling and capture rate. |
| moat | 4 | Exclusive contractor and claimant contracts plus the install base and the bias model learned from our own paired data. Hardware alone is copyable. |

---

## Sources

- NREL 2022, Mining G.O.L.D. (more than 2,000 Nevada mining holes per year; no temperature duty), via D06: https://docs.nlr.gov/docs/fy22osti/81946.pdf
- NBMG borehole temperature service (226 mining and 82 dewater wells), via M20: https://web2.nbmg.unr.edu/arcgis/rest/services/NV_Data/NVBoreholeTemperatures/MapServer/0
- NBMG well log service (442 TG boreholes), via M20: https://web2.nbmg.unr.edu/arcgis/rest/services/NV_Data/NVWellLogs/MapServer/0
- Meikle hot rock 140-160 C (E&MJ), via M20: https://www.e-mj.com/?p=5358
- Peters and Nelson 2009, BHT and Horner criteria, via M04: https://www.searchanddiscovery.com/abstracts/html/2009/hedberg/abstracts/extended/peters/peters.htm
- EGU2009-1250, Horner vs Cooper-Jones, via M04: https://meetingorganizer.copernicus.org/EGU2009/EGU2009-1250-3.pdf
- Lachenbruch, A.H., and Brewer, M.C., 1959, Dissipation of the temperature effect of drilling a well in Arctic Alaska, USGS Bulletin 1083-C (from memory; URL not checked this turn: https://pubs.usgs.gov/publication/b1083C) (unverified link)
- Bullard, E.C., 1947, The time necessary for a bore hole to attain temperature equilibrium, Geophysical Journal International 5(5) (from memory) (unverified)
- Mikkelsen, P.E., and Green, G.E., 2003, Piezometers in fully grouted boreholes, FMGM Symposium, Oslo (from memory) (unverified)
- 30 USC 1022 (Geothermal Steam Act exclusivity), via R13: https://www.law.cornell.edu/uscode/text/30/1022
- 30 USC 1003(c) and 43 CFR 3204 (noncompetitive leasing), via R02
- NRS 534A (ownership 534A.050, permits 534A.060, confidentiality 534A.031): https://www.leg.state.nv.us/NRS/NRS-534A.html
- NAC 534A (geothermal wells, records), via H11: https://www.leg.state.nv.us/NAC/NAC-534A.html
- NAC 534 (water wells and boreholes; plugging), not fetched this turn: https://www.leg.state.nv.us/NAC/NAC-534.html (section numbers unverified)
- BLM IM 2026-024 (casual use), via H13: https://www.blm.gov/policy/im-2026-024
- TG hole costs, via H11 and M29: https://openei.org/wiki/Thermal_Gradient_Holes
- Sibling files: M04, M18, M20, M29 (this folder); D06, L16, R02, R13 (../../evidence/); H11, H13 and MEMO.md (../../../hardware/)
