# P12: Pump-Puller Open-Hole Sonde. Log every ranch well the day its pump comes out, through local pump contractors

Date: 23 Oct 2026. Build candidate P12, model track. This builds on `../../../hardware/MEMO.md` and `../../../hardware/evidence/H06-water-well-landman.md` (drop probe, $1-2/ac option, SRHA title trap, 30% loggable kill line), `../../../hardware/evidence/H02-existing-well-logging.md` (SMU tool costs, hired logging $5-40k), `M06-water-well-temperature.md` (146,235 NDWR reports, 697 isolated warm wells), `M21-shallow-temperature.md` (64% blank 2 m areas), `M23-hydrology-masking.md` (masks, plumes), `M30-permeability.md` (specific capacity as a free permeability layer), `P01-ranch-well-sentinel-2-0-a-resident-well-.md` (resident string, the "pay for the next pump pull" hook, Mode O), `P05` (mixing sampler) and `P07-drill-rig-ride-along-free-core-barrel-me.md` (the contractor ride-along business pattern). It does not repeat them. P01 treats a pump pull as something **we pay for** on chosen wells. P12 is the reverse: it rides on the **pump pulls that already happen** for repair, at wells we did not choose.

**Method note.** The shared web search budget for this workflow turn (200 calls) was used up before this agent ran. Both searches I tried were refused, so no new web pages were read. Facts from repo files are cited by file. Standard literature I know is marked (from memory, unverified). Prices are my estimates and are (unverified). Numbers I computed are marked (calc).

---

## Bottom line

**Build it. It is cheap, quick, and it is the best "designed second detector" in the set, because the place and time of a pump failure has nothing to do with our model.** But fix three things in the brief.

1. **"Within an hour of the pull" is not the best open-hole T(z). It is a stirred one.** Pulling 50-150 m of drop pipe and a pump drags water and drops the water level by about 2-5 m (calc, 1c). The good news hides in the reason the pump came out: **a failed pump means the well has stood idle since it failed**, often for days (unverified). That column has already relaxed toward rock temperature. So the protocol is: drop a $300 pressure logger first, then do a fast down-log of T/EC/gamma in the first 10-15 minutes (the lower column is the least stirred), then camera, then the flowmeter last. If the new pump arrives the next day (common, unverified), do a second down-log before the pump goes back in. That second log, after 12-24 h of no pumping, is the gold one.
2. **The pump pull is also a free slug test.** If the check valve holds, the pipe comes out full of water. That removes 7-9% of the casing's area times the submerged length, so the water level drops 2-5 m at once and then recovers (calc). A pressure logger parked below the water level records that recovery. Hvorslev or Bouwer-Rice then gives hydraulic conductivity K, no pump test needed. This is the strongest new rank 2 input in P12, and the brief missed it.
3. **The heat-pulse flowmeter does not measure formation Darcy flux. It measures borehole cross-flow.** Its floor is about 0.04 L/min (Hess 1986, from memory, unverified). In a 6 inch casing that is about 1,000 m/yr of water velocity, far above the cm/yr formation flux that bends a Peclet profile (P01 1a). What it does see is water entering one aquifer zone and leaving at another because their heads differ. **Upward ambient cross-flow from a deep zone means an upward head gradient**, which is what a discharge area over an upflow looks like. It also lets us correct the T log for the in-hole flow that ruins most water-well temperatures (the model's "92% flow-disturbed" check). So it serves rank 3 and rank 6, not rank 2 directly.

Also: natural gamma is a **clay and lithology** tool, not a smectite detector. Smectite is often lower in potassium than illite, so a high-gamma bed is "clay or volcanic ash", not "geothermal cap". A smectite cap at 50-300 m is also rare above blind Great Basin systems, which mostly sit under cold aquifers, not under clay caps (M23). Gamma earns its place by fixing lithology and depth ties for the conductivity column (rank 7) and by catching uranium-rich travertine or altered zones (weak). The **camera is a stronger direct sign** than the brief implies, but only for **gas** (CO2 bubbles entering at a perforation or fracture) and **silica scale**. Calcite scale and iron bacteria are common in plain cold Basin and Range water, so calcite alone is weak.

With those fixes, a v1 sonde costs about **$14-18k as a prototype and $8-11k at 20 units** (unverified), and a logged well costs about **$400-650 all-in** (calc, 5). One contractor fleet in Nevada could log **150-600 wells a year**, and the six target states perhaps 750-3,000 (unverified, 6). The model gain, my estimate: over two seasons in Nevada it narrows the lidded catch-rate factor (rank 1) by about 15-30% of its log-width, sensor reliability per mask class (rank 4) by about 25-40% (because effort is known and independent of heat), lid and mask class (rank 3) by about 20-35% in basins with 15 or more logs, conductive background and position (rank 7) by about 15-25% locally, and permeability class (rank 2) by about 10-20%. The rights edge is good: a trusted local contractor is the best messenger for a heat option, and the contractor sees the warm well first, before any filing.

**Self-scores:** model_uncertainty_alpha 4, rights_alpha 4, buildability 4, cost_scale 4, moat 4.

---

## 1. Physics: what one open-hole visit can and cannot see

### 1a. Why a failed-pump well is close to equilibrium
- While a pump runs, warm water from the inflow zone flows up the drop pipe and casing and heats the casing and near rock above it. The rock skin around a 6 inch hole relaxes on a time of about r^2/kappa. With kappa = 1e-6 m2/s: r = 0.1 m gives about 3 h, and a 0.5 m skin gives about 3 days (calc).
- A pump that **failed** has not run since it failed. If the contractor comes 2-10 days later (typical, unverified), the column is within about 0.05-0.2 C of rock temperature below about 20 m (calc from the times above, my judgment on amplitude). That is far better than a log taken in a well that pumped this morning, which is what H06 and P01 drop-probe visits often get.
- A **planned** replacement (pump still working) is disturbed. Tag it in the data and down-weight it. THERMOS-B already takes per-source censored likelihoods, so this is one extra source class, not a new model.

### 1b. What the pull itself does to the column
- Pulling pipe at about 0.1-0.3 m/s (unverified) drags water and mixes it over a few metres near the pipe. The large-scale gradient survives. Fine detail (inflow steps of 0.01-0.1 C) is smeared in the top part of the column most.
- Free convection in a 6-8 inch casing adds about 0.01-0.1 C of random noise over a few metres (P01, from memory). That sets the real floor. **0.001 C resolution is cheap and fine to keep, but the usable accuracy of a single log is about 0.02-0.1 C.** That is still 10-100x better than a driller's single temperature (M06).
- Fast response matters more than resolution. A glass-bead thermistor with a 0.2-0.5 s time constant at 3-5 m/min smears a step over only a few cm.

### 1c. The pull as a free slug test (rank 2)
- Removed volume per metre of submerged pipe, if the check valve holds: 1.25 inch Sch 40 pipe (OD 42 mm) in a 6 inch casing (ID about 154 mm) is about 7.5% of the casing area. 2 inch pipe in an 8 inch casing is about 9%. With 30-60 m of pipe below water, the level drops about 2-5 m. The pump and motor (4 inch by 1.5-2 m) add about 0.5-0.7 m (calc).
- Hvorslev time lag T0 = r_c^2 ln(L/R) / (2 L K). For r_c = 0.077 m, a 30 m open interval, R = 0.08 m: K = 1e-5 m/s gives T0 of about 1 minute; K = 1e-7 m/s gives about 1.6 h (calc). Both fit inside the contractor's 1-3 h on site.
- So a $300 pressure logger dropped in first gives K to about a factor of 2-3 (my judgment; slug tests are noisier than pump tests and see mostly the near-well zone). When the new pump starts, the contractor's normal run-in gives a second, step-drawdown point if they read the water level (many do, unverified). Together these replace the rounded driller specific capacity (M30) with a measured number on the same well.
- If the check valve leaks, the pipe drains on the way up and the level barely moves. The pressure trace tells us which case we have.

### 1d. Heat-pulse flowmeter: cross-flow and corrected T(z)
- The tool heats a thin sheet of water and times the heat pulse to a thermistor above or below. A rubber skirt diverts flow through the tool. Range about 0.04-4 L/min (Hess 1986; Paillet's USGS work; from memory, unverified).
- In an idle well with two or more open zones, water runs from the high-head zone to the low-head zone inside the casing. In a discharge area (often over an upflow or its outflow plume) the deep zone has the higher head, so flow is **upward**. In a recharge area it is downward. The sign and size of ambient cross-flow at 3-6 stations is a direct, cheap mask label for THERMOS-B (rank 3) and points uphill along heads toward the upflow (rank 6).
- The flow log tells us which parts of the T log are isothermal flow segments and which are rock-controlled. Without it, the model must guess (the 92% flow-disturbed share in MODEL.md). With it, the flow-free segments go into the Peclet fit and the flow segments give inflow temperatures. **Inflow temperature at the deepest zone is the best single number** a water well gives us, because it is the water closest to the source.
- The flowmeter must run last, after the slug recovery has mostly finished (1c), or it reads recovery inflow instead of ambient flow. If the pressure logger shows the level still rising, the reading is tagged and both are fitted together.

### 1e. Fluid EC, camera, gamma
- **EC log:** steps in EC mark inflow zones of different water. A deep inflow that is warmer and saltier (higher Cl, B) than the shallow water is a leak signal (M07, P05). EC is cheap and always on.
- **Camera:** gas bubbles entering at a fracture or perforation (CO2, sometimes H2S smell at the wellhead) are the strongest visual sign. Silica scale (glassy, white, hard) on the pump or casing is rare in cold water and is a good flag. Calcite scale, iron bacteria and corrosion are common and weak. The camera also inspects the **pump that came out**: the contractor photographs scale on the pump intake and motor with a phone. That is free and often the clearest scale sample of all. We ask for a scraping in a bag (geochem lab, about $50-150, unverified).
- **Natural gamma:** works through steel casing with about 20-40% loss of counts (from memory, unverified). It gives clay, ash and sand beds to match the driller lithology log and to pick thermal conductivity for the column (rank 7), plus a depth tie between the log and the driller log.

### 1f. What it cannot see
- One snapshot cannot give earth tides, a season of pump cycles, or months of averaging. That is P01's job. P12 finds the wells worth a P01.
- It sees only wells that exist, which sit mostly on valley floors near farms and towns. Those sample outflow plumes, not upflows (rank 6), and they are biased toward irrigated basins. The model must carry this as a covariate shift.
- Wells with an inner liner, packed annulus or a collapsed hole may not take the sonde. Expect 10-20% refusals at the hole (unverified).

---

## 2. Prior art

- **USGS borehole geophysics in water wells** is mature. Keys (1990, TWRI Book 2 Ch. E2) and Williams and Paillet's USGS work set the standard suite: fluid temperature, fluid resistivity/EC, natural gamma, caliper, heat-pulse flowmeter, and camera or optical televiewer (from memory, unverified). Commercial slim tool makers (Mount Sopris/ALT QL40 series, Robertson Geologging) sell exactly these sondes, stackable on one 4-conductor wireline (from memory). A hired water-well geophysical log with mobilization runs about $1.5-5k per well (unverified); H02 gives $5-40k for oilfield-grade logs.
- **Pump contractors already lower cameras.** Downhole video inspection is a normal pump-contractor service, sold at a few hundred dollars per well (unverified). They own reels, tripods and truck power. So the deployment habit and the skill are already there. We add sensors to a thing they already do.
- **Geothermal finds in water wells.** Zanskar says accidental water-well drilling found more than a third of known blind systems (M06). Gabbs Valley 124.9 C at 152 m came from a play fairway hole at water-well depth (hardware MEMO). Basin and Range heat-flow work by Sass and others used open water wells and mineral holes (from memory). Nobody, as far as I know, uses the **repair flow** of pump pulls as a sampling channel (unverified; no web budget to check).
- **Business pattern:** P07 (drill rig ride-along) shows the same "pay the trade that is already on site" structure. P12 is the water-well twin of P07: lower depth, far more sites, and private land where the heat right is cheap.

---

## 3. The v1 design

### 3a. Sonde (one string of screw-together sections, 42 mm OD)

| Section | Contents | Length | Parts and notes | Proto cost | At 20 units |
|---|---|---|---|---|---|
| Cable head + electronics | STM32-class MCU, RS-485 or simple DSL modem over the cable, 64 GB flash, 3-axis accelerometer (tilt), real-time clock, power regulator | 0.35 m | 316L stainless housing, rated 30 bar (300 m); field-replaceable o-rings | $900 | $450 |
| Fluid T + EC + P | Fast glass-bead thermistor (0.2-0.5 s) plus a reference Pt1000; 24-bit ratiometric ADC (ADS124S08-class) gives 0.0005-0.001 C resolution; 4-electrode EC cell, 10 uS/cm-100 mS/cm; Keller-class piezoresistive pressure 0-30 bar, 0.05% FS for depth | 0.35 m | Sensors in a slotted bottom nose so they lead on the down-log | $1,300 | $650 |
| Natural gamma | 25 x 75 mm CsI(Tl) crystal with a SiPM readout, counts in cps calibrated to API at a test pit | 0.45 m | No PMT high voltage; SiPM board about $300 | $1,800 | $900 |
| Heat-pulse flowmeter | Flat wire heater grid, two thermistors 25 mm above and below, rubber petal skirt for 4-8 inch casing (spring arms) | 0.5 m | Pulse about 15-30 J; skirt is a wear part (spares about $40) | $1,600 | $700 |
| Camera | 1080p down-view plus one side view on a mirror, LED ring, sapphire window; records to local flash, sends stills and low-rate preview up the cable | 0.3 m | Optional on stations; contractor may use own camera instead | $1,100 | $500 |
| **Sonde total** |  | **about 1.95 m, about 7-8 kg** |  | **$6,700** | **$3,200** |

Power: 14.4 V Li-ion pack in the electronics section (about 40 Wh) or down the cable. Average draw about 2-4 W while logging; flowmeter pulses add peaks. A 3 h job uses well under 20 Wh (calc).

### 3b. Surface kit (fits in one truck-bed case)
- Battery winch, 300 m of 4-conductor 4.8 mm (3/16 in) armoured cable with slip ring, level-wind and depth encoder: about $3-4.5k proto, $2-3k at 20 (unverified).
- Folding tripod with sheave that clamps to 4-12 inch casing, or a sheave that hangs on the contractor's pump-hoist mast: about $600.
- Rugged Android tablet with our app: live T/EC/gamma/depth plot, camera preview, GPS tie to the wellhead (phone GNSS about 3-5 m; good enough against TRS +/-400-800 m errors), photos of the pump, the owner's consent and the option sign-up screen: about $600-900.
- Drop-in pressure logger (Keller DCX- or HOBO-class) with 0.01-0.02% FS and barometric pair, on its own light line: about $500-900 for the pair.
- Disinfection kit (chlorine solution, spray, wipes, bagged cable guide) so we meet potable-well practice: about $100 per year.
- Sample bottles for a deep inflow grab: a cheap motorised 250 mL point sampler is a v1.5 option (about $1-2k). In v1 the contractor fills bottles from the first discharge of the new pump (first flush; P05) and bags a scale scraping.
- **Kit total:** about **$14-18k prototype, $8-11k at 20 units** (calc, from the rows above plus spares and calibration), matching the brief's $10-20k.

### 3c. Comms and data
- Tablet syncs over LTE when back in signal. No live link is needed on site.
- Each job uploads: raw log, flowmeter stations, slug-recovery trace, camera clips, pump photos, GPS, owner consent, NDWR well log number (looked up from GPS against the NDWR layer in M06).
- Our server runs the QC script within 24 h: thermistor lag correction, depth match with gamma to the driller log, slug fit, flow-segment flags, and a THERMOS-B likelihood. Hot flags go to the landman queue the same day.

### 3d. Protocol on site (contractor crew of 2, with the pump already out)
1. Get the owner's signature on the tablet (data consent; heat-option interest checkbox). 2 min.
2. Drop pressure logger to 5 m below water. 3 min. (It records the slug recovery from the moment the pipe left the water if dropped as the last pipe joints come up.)
3. Set the sheave and run the **down-log** at 3-5 m/min to the bottom (T, EC, P, gamma, tilt). 100-200 m of water column takes 20-40 min.
4. **Up-pass with camera** at 6-10 m/min, stopping at EC steps, gamma kicks and any visible inflow. 15-25 min.
5. **Flowmeter stations** at 3-6 depths picked by the app from the down-log (above and below each inflow step). About 3-5 min each, 15-25 min total.
6. Photograph the pump, intake and motor; bag any scale. 5 min.
7. Pull out, disinfect, pack. 5-10 min.
- **Total contractor time: about 60-110 min** (calc), most of it while the contractor would otherwise be waiting for parts, pipe inspection or a helper.
- **If the pump goes back the next day:** repeat step 3 only (20-40 min) before reinstall. This is the best equilibrium log of the set.
- **If the well is high-EVSI** (from the model's list), the contractor straps a P01 string to the new drop pipe on reinstall. P01 becomes free to install on these wells, since the pump is already out.

### 3e. Deployment and the contractor deal
- Give each partner contractor one kit on loan. Train in one day.
- Pay **$300-500 per accepted log** (the brief's range) plus **$250-1,000 bonus when a log becomes a hot flag** and a **small override share (for example 2-5% of our override) on any option that leads to a sale** (my design; unverified rates).
- The owner gets a free well report: casing condition video, water level, specific capacity / K, water EC and arsenic flags if sampled, and a contractor note. This report helps the contractor sell the repair and future service. That is why the contractor wants the kit.

---

## 4. How big is the sample?

- Nevada has 146,235 driller reports since 1984 (M06). Many are monitor or replaced wells. I assume about 40-70k active pumped wells (unverified). A submersible pump lasts about 7-15 years (from memory, unverified). That gives about **3-10k pump pulls a year in Nevada** (calc).
- About 25-40% are rural, outside Reno, Las Vegas and Pahrump suburbs (unverified). That is about 1-4k rural pulls a year.
- If 3-5 partner contractors capture 15% of those: **about 150-600 logs a year in Nevada** (calc). Utah, Idaho, Oregon, New Mexico and Arizona rural pulls could be 4-6x more (unverified), so **750-3,000 logs a year** in the West with 20-40 kits.
- For scale: MODEL.md plans 300-800 pre-registered Sentinel visits. P12 alone can match that count each year at a lower cost per site, but at wells we did not choose. The two are complements: P12 gives breadth and an unbiased effort record; Sentinels go where EVSI is high.
- **Selection bias to model:** hot and scaling water kills pumps faster, so warm wells may be over-represented among pulls (my judgment). That helps detection. The model must include "pump failure rate rises with T and TDS" as a known effort term, or it will overstate the share of warm ground.

---

## 5. Cost per logged well (calc)

| Item | Per log |
|---|---|
| Contractor fee | $300-500 |
| Kit amortized ($9-15k over 2 years and 150-300 logs) | $30-100 |
| Consumables, disinfection, skirt wear, data | $20-40 |
| Our QC, interpretation, admin | $40-80 |
| Hot-flag bonus, spread over all logs (about 3-5% flag rate) | $10-30 |
| **Total** | **about $400-650** |

Against: hired water-well geophysics at about $1.5-5k (unverified), P01 at $450-700 per well-season, a Sentinel visit at a few hundred dollars plus crew travel, and a gradient hole at $0.3-1.5M (hardware MEMO). Mobilization is near zero because the contractor is already there.

Per km2 it is not a grid tool. One log covers the 500 m model parcel and its share of a basin's head and mask field. At 15-30 logs per basin, the basin-level mask class and lid parameters get a real fit (section 6).

---

## 6. Model value: how much it shrinks the ranked uncertainties

All numbers are my estimates (unverified). They should be confirmed by the GHOST Tier 1 in-silico sensor ranking before money moves.

| Rank | What P12 adds | Shrinkage after 2 seasons in NV |
|---|---|---|
| **1 Detection gap / lidded catch rate** | A detector whose effort is random with respect to heat, recorded to the minute (who, where, when, depth reached). This is the "second detector" the model needs to break the occupancy-vs-detection tie, and it reaches below 2 m lids at 50-300 m depth. | 15-30% of the log-width of the catch-rate factor in Nevada; 5-15% elsewhere in year 1 |
| **2 Permeability class** | Slug-test K on every well, cross-flow head differences, inflow zone count, plus step-drawdown on reinstall. Shallow, so it constrains fault-zone and outflow permeability, not the reservoir. | 10-20% on the shallow k-proxy layer; less on MWe |
| **3 Masking / lid thickness** | Flow-corrected T(z), inflow temperatures, cross-flow sign, EC layering. A mask-class label on each logged well. | 20-35% in basins with 15+ logs |
| **4 Sensor reliability s/q per mask class** | Hundreds of paired readings: our open-hole log vs the same well's driller temperature, vs 2 m probes nearby, vs NURE/WQP chemistry. Many will sit in or near the 20 known blind systems and 40 cold controls by chance; we also ask partner contractors to call us for any pull in those cells. | 25-40% on the s/q matrix for water-well-class detectors |
| **5 T at 0.5-2 km** | Better shallow gradients and inflow temperatures for the column; feeds geothermometers via first-flush bottles. | 10-20% where a hot flag is found |
| **6 Upflow location** | Cross-flow and head direction in many wells across a basin point back up the plume. | 5-15% (wells sit in outflow) |
| **7 Conductive background, position error** | Gamma lithology for conductivity; GPS ties that replace TRS +/-400-800 m positions for each logged well. | 15-25% locally; removes position error on logged wells |

The biggest value is rank 1 and rank 4 together. Those two set the 2-5x spread on N in MODEL.md. A random-effort detector with hundreds of draws a year is the cheapest way I know to pin them. A rough check: if 2-5% of rural Nevada wells sit inside a 3-30 km outflow plume of an undiscovered system (my assumption from M23 plume sizes), 300 logs a year give 6-15 plume hits a year (calc). That is enough to fit a catch rate with a useful error bar in two years.

---

## 7. Rights edge

- **Private land first.** Ranch wells sit on fee land. In Nevada the heat usually belongs to the surface owner, but **screen SRHA patents first** (hardware MEMO, H06). The option costs about $1-2/ac (hardware MEMO, Raser comparison).
- **The contractor is the trusted messenger.** Ranchers trust the person who keeps their water running. The contractor shows the free well report and says "these folks pay for the heat option, they paid for your log". Our landman closes within 1-2 weeks. I would not ask the contractor to sign leases themselves; whether a contractor can present a lease form without a licence varies by state and should be checked (unverified; get it in the H13 attorney memo).
- **First sight.** We see the warm well before any filing. NDWR well logs are public, but our log is not. On private land nothing needs filing for a water-well log done for well service (unverified; check NAC 534 and NDOM rules in the H13 memo before any "geothermal" wording appears on the paperwork).
- **Neighbour federal land.** A hot plume on a ranch often points to the range front, often BLM. That feeds nominations or leftover $1/ac/yr parcels.
- **Upside over the H06 drop probe:** the owner is already paying for a service, the contractor is already on site, and the report is useful to them. Expect a higher sign rate than cold door-knocking (my judgment).

---

## 8. Moat

- Rural pump contractors are few per basin (often 2-6, unverified). Exclusive or first-call agreements with the best one or two in each target basin, plus the override share, are hard for a rival to undo quickly.
- The data set (flow-corrected open-hole logs, slug K, scale photos) does not exist in any public file.
- Zanskar drills its own wells and buys at BLM auctions. It has no private-land ranch channel that we know of (Z04, Z05; unverified now).
- Hardware itself is copyable. The moat is the network and the paired data.

---

## 9. Risks

1. **Contractors will not wait an hour.** They bill by job, and a helper waiting is lost money. Mitigation: pay per log, run the log while they inspect pipe or wait for parts, keep the core log (steps 2-3) under 40 min, and make the owner report sell more repair work.
2. **Disturbed logs.** Planned replacements and pulls within hours of pumping give poor T(z). Mitigation: tag time since last pumping (ask the owner, read the old pump controller), and down-weight in THERMOS-B.
3. **Well hygiene and liability.** Anything lowered into a drinking-water well must be disinfected; a stuck sonde in a customer's well is a real cost. Mitigation: disinfection kit, weak-link release on the cable head, centralizers, insurance, never log a well with visible casing collapse on camera first pass.
4. **Licensing and data rules.** Some states regulate who may work on a well (pump installer licence) and what counts as a geothermal test (Nevada TG permit, NRS 534A, per P07). Mitigation: the contractor is the licensed party and the log is part of well service; attorney memo before launch.
5. **Selection and location bias.** Pumps fail where wells exist: valley floors, towns, farms. Model the effort and the pump-failure-vs-temperature link explicitly.
6. **Sample too thin in empty basins.** Remote basins with few wells give few pulls. P12 does not cover them; darts, 2 m probes and E-MT (P02, P03) do.
7. **Gamma and camera read less than hoped.** Smectite caps are rare at these depths; calcite scale is common. Keep them for lithology and gas, and expect the flowmeter and T/EC to carry most of the value.

---

## 10. First test (8-12 weeks, about $40-60k, unverified)

- **Build:** 3 kits in 8-10 weeks. Buy the winch, cable, camera module and pressure loggers; build the T/EC/P/gamma/flowmeter sections. Calibrate T in a stirred bath against a reference PRT (target 0.01 C accuracy, 0.001 C resolution), EC with standards, gamma at a known calibration pit or with a K-salt pad.
- **Bench check in one known well:** an open, idle monitoring well near a known warm area (for example Fallon or Gabbs Valley wells from the M06 list), logged 3 times: before a mock pull, 10 min after pulling a dummy string, and 24 h later. That measures the pull disturbance directly.
- **Field:** sign 2-3 contractors in one or two Nevada basins that contain both NDWR warm wells (M06 list of 697) and cold controls. Target 25 logs in 8 weeks.
- **Pass bars:**
  - (a) At least 20 logs in 8 weeks from 2-3 contractors, with median added contractor time under 90 min.
  - (b) Repeat down-logs (same well, minutes apart) agree to 0.05 C below 20 m; the 24 h log differs from the 10 min log by less than 0.3 C in failed-pump wells.
  - (c) Slug recovery fitted in at least 60% of logs; K within a factor of 3 of the driller specific capacity converted to K.
  - (d) Flowmeter detects ambient cross-flow in at least 30% of multi-zone wells, and its sign agrees with nearby head data where it exists.
  - (e) At least one log shows a flow-corrected gradient or inflow temperature that the driller value missed by over 5 C, or gas or silica scale on camera.
  - (f) At least 3 owners agree to a heat option or a landman meeting, and cost per log under $700.
- **Kill:** under 10 logs in 8 weeks (contractors will not do it), or the pull disturbance is so large (over 1 C below 20 m) that failed-pump logs are no better than driller values.

---

## 11. Self-scores (1-5)

| Score | Value | Why |
|---|---|---|
| model_uncertainty_alpha | 4 | A random-effort, high-count detector that hits ranks 1 and 4, the two that set the 2-5x spread on N, plus 3 and 7. Snapshot only, and outflow-biased, so not a 5. |
| rights_alpha | 4 | Trusted messenger on private fee land at $1-2/ac, first sight before any filing. Leases still need our landman. |
| buildability | 4 | All parts are standard slim-logging parts. 8-10 weeks for 3 kits with 2 engineers. The hard part is signing contractors, not hardware. |
| cost_scale | 4 | $400-650 per log, near-zero mobilization, 750-3,000 logs a year possible in the West. |
| moat | 4 | Exclusive contractor network per basin plus paired data. Hardware is copyable. |

---

## Sources

- Repo files cited by name above (they hold the primary URLs): hardware MEMO, H02, H06, H13, M06 (NDWR ArcGIS layer https://arcgis.water.nv.gov/arcgis/rest/services/NDWR/Well_Driller_Reports/FeatureServer/0), M07, M21, M23, M30, P01, P05, P07, Z04, Z05.
- SMU temperature tool costs (via H02): https://smu.edu/-/media/site/dedman/academics/programs/geothermal-lab/documents/ttool-equipment-techniques.pdf
- From memory, unverified (no web budget): Hess 1986, Can. Geotech. J. (heat-pulse flowmeter); Keys 1990, USGS TWRI Book 2 Ch. E2 (borehole geophysics for groundwater); Paillet and Williams USGS flowmeter work; Hvorslev 1951 (USACE WES Bull. 36) and Bouwer and Rice 1976 (WRR 12:423) slug tests; Bredehoeft and Papadopulos 1965 (WRR 1:325); Mount Sopris/ALT QL40 and Robertson Geologging tool catalogues; submersible pump life ranges from industry practice.
