# P28: Parcel Structure Payloads. Drone mag + gamma, drone LiDAR, targeted SWIR, a neutron-gamma cart and a stop-and-go gravity rover

Date: 23 Oct 2026. Build candidate P28, model track. This builds on `M09-gravity-magnetics.md` (Nevada gravity base of about 71,000 stations on a 2 km grid from 1990, basement depth good to about +/-200-300 m only above 1.2 km; Earth MRI flew about 275,000 line-km of 200-400 m mag + radiometrics over Nevada; "dense ground gravity at fault corners" and "drone mag at 25-50 m lines" ideas), `M10-remote-sensing.md` (EMIT 60 m pixels miss the 1-500 m2 footwall patches; ranch-visit drone kit idea), `M11-structural-settings.md` (about 1,430 favorable structural settings, about 4-5 candidates per real system; automated FSS detector), `M21-shallow-temperature.md` (2 m noise floor about 1.2 C, 64% blank rate), `P09` (drone mag for steel collars), `P13` (drone fleet, Part 107 notes), `P23` (walk-along HVSR basin depth, +/-100-150 m with SPAC), `../../evidence/D10-satellite.md` (Kraal and Schwering 2024), `../../../hardware/evidence/H05-quantum-novel-sensors.md` (CG-6, MagArrow, drone gravity not field-ready) and `H13-permits-and-secrecy.md` (BLM IM 2026-024). It does not repeat them.

**Method note.** The shared web-search budget for this workflow turn was used up before this agent started. All 3 searches I tried were refused. So no new web pages were read. Sources are repo files (which carry URLs) or standard literature I know, marked (from memory, unverified). All prices are my estimates (unverified). Numbers marked (calc) come from my own script, `P28_calc.py`, in this folder.

## Bottom line

Build it, but as a **"structure day" kit that one 2-3 person crew runs on each short-listed block in one to three days**, not as five separate fleets. Change the brief in four ways.

1. **The gravity rover and the drone magnetometer carry almost all the value.** They answer the one question that decides which 640-acre block to nominate: *where exactly is the buried fault corner?* A Basin and Range fault with 25-300 m of throw under fill gives a 0.5-6 mGal gravity step (calc). A CG-6 class meter with RTK heights reads to about 0.01-0.02 mGal. A 200 m-wide magnetite-destroyed upflow zone in volcanic host gives a magnetic low of roughly 100-800 nT at drone height (calc, order of magnitude). Earth MRI's 200-400 m lines blur it, a drone at 40 m lines resolves it. Together they should cut the upflow position error from about +/-600-1,000 m to about +/-150-250 m. That moves P(upflow inside the block we nominate) from about 0.34-0.67 to about 1.0, and P(inside the right 500 m model parcel) from about 0.04-0.10 to about 0.4-0.6 (calc).
2. **Drone LiDAR is cheap and worth it, but only as a scarp-age and step-over tool.** 3DEP 1 m lidar already exists over much of the region (coverage unverified). The drone adds 5-10 cm detail on the target block only: small scarps under 0.5 m, fresh fissures, tufa and sinter mounds, and a terrain model for gravity corrections.
3. **SWIR imaging should be rented or contracted in v1, not bought.** A true 2.0-2.5 um drone line-scanner (the band that separates kaolinite, alunite, opal and smectite) costs about $120-250k (unverified). V1 uses a handheld point SWIR spectrometer on footwall samples (about $40-60k, or rent) and an airborne contractor or rental imager for blocks that pass the mag/gravity gate.
4. **Drop the cosmic-ray neutron cart from v1.** Its job (remove soil-moisture noise from 2 m data) is real but small, and the gamma spectrometer already gives a moisture proxy: wet soil lowers all gamma counts by roughly 1% per 1% of volumetric water (from memory, unverified). A cheap needle probe at each 2 m station measures the thermal conductivity directly, which is what the 2 m model actually needs. Keep the neutron cart as a v2 option for sites with irrigated or snow-covered ground.

**Cost.** V1 fleet capital is about **$330-480k** (below), or about **$200-260k** if the gravimeter is rented and SWIR is contracted. Operating cost is about **$150-400 per km2** for the drone channels and about **$8-20k per candidate block** for the full structure day including gravity (calc, unverified prices). That is less than 1% of a $0.3-1.5M gradient hole.

**What it shrinks.** Mostly rank 6 (upflow location) and rank 7 (basin depth). Some of rank 2 (fault recency, via LiDAR) and a little of rank 4 (2 m reliability, via the moisture proxy). It does not touch the top uncertainty, rank 1 (deep detection gap), except by sharpening the structural prior λ. So this is a **targeting and rights tool**, not a "how much is there" tool.

**Rights edge.** The bank nominates fewer, better blocks: about **1-2 blocks per prospect instead of 4-9** (calc), at the same 90% chance of holding the upflow. That cuts rent, bonus bids and, most important, the signal we leak to Zanskar and Ormat when we nominate. On private land it picks the right ranch among neighbours before we spend landman time.

## 1. Physics case: why each payload sees part of a blind system

A blind Basin and Range system is hot water rising on a buried fault corner (a step-over, a fault termination or an intersection) and then flowing sideways under a cold aquifer or a dry lid (`M11`, `M18`). None of these payloads sees the heat. They see the **plumbing frame** and **fossil or leaking alteration**. Their job is to put the expensive heat sensors (Sentinel wells, darts, E-MT) on the right strand.

### 1a. Stop-and-go gravity rover: basin depth and buried faults
- **Signal (calc).** Basin fill is about 0.4-0.5 g/cm3 lighter than bedrock. A slab step gives 0.042 x Δρ x throw mGal. Throw of 10 m gives 0.19 mGal; 25 m gives 0.47; 50 m gives 0.94; 100 m gives 1.9; 300 m gives 5.7 mGal.
- **Noise.** A Scintrex CG-6 has about 0.005 mGal repeatability (maker spec, from memory, unverified). The field error budget is dominated by heights and terrain. Net height coefficient is about 0.225 mGal/m, so 3 cm RTK gives about 0.007 mGal (calc). Drone LiDAR terrain at 10 cm keeps inner-zone terrain errors under about 0.01-0.02 mGal (judgement). So total station error is about 0.02-0.03 mGal, and buried faults with **5-10 m of throw or more** are visible at 100-200 m station spacing.
- **What it gives the model.** A local depth-to-basement surface and the trace of buried range-front faults, with their dip sense. Gravity alone has a density-depth trade-off (about +/-20-30% on depth). Tied to Sentinel well picks (`P01`) and walk-along HVSR (`P23`), local depth error falls to about +/-80-120 m (judgement, consistent with P23).
- **Depth.** Sees the whole fill column, 0-3 km. Resolution laterally is about the depth to the step.
- **Why a rover.** M09 found a walking crew does about 40-80 stations a day. A CG-6 on a self-levelling mount in a UTV, with RTK on the roof, can do about **120 stations in a 10-hour day** at 200 m spacing along two-tracks (calc: 3.5 min read, level and RTK, plus 1.5 min drive). The brief's 150-300 a day is a stretch target that needs a shorter 90 s read and denser roads (unverified).
- **Not airborne.** H05 found drone gravity drifts about 20 mGal. Ground is the only option today.

### 1b. Drone magnetometer: dikes, buried faults and magnetite-destruction lows
- **Signal (calc, order of magnitude).** Hot acid fluid turns magnetite into pyrite or clay. Take a vertical altered zone 200 m wide with a susceptibility drop of 0.02 SI in volcanic host. Seen from 30 m it gives a low of several hundred nT. Buried under 100 m of non-magnetic fill it is still about 100-400 nT. With a weaker contrast (0.005 SI) it is about 100 nT. A 100 m-wide zone at 200 m depth is still about 100 nT. The real numbers will be smaller (finite depth extent, field inclination about 65 degrees, remanence), so read them as "tens to hundreds of nT".
- **Noise.** OPM (optically pumped) sensors like the MagArrow resolve about 0.005 nT. Heading error and drone interference add about 1-3 nT. A base station removes the daily drift. So the low is far above noise **where the host is magnetic**.
- **Where it fails.** In carbonate, thick sediment and non-magnetic granite there is no magnetite to destroy. The model must mask the alteration term there (M09 rule 3). Here the mag channel still maps dikes and offsets of magnetic marker beds.
- **Why drone and not Earth MRI.** Earth MRI flies 200-400 m lines at 100-200 m height, which resolves bodies about 200-400 m across (M09). The demagnetized core of an upflow is often 100-300 m wide. A drone at 30-40 m height and 40 m lines resolves 50-100 m bodies. Precedent: Gabbs Valley's blind target sat on a magnetic low (L22); drone mag has mapped altered, demagnetized zones on volcanoes (EGU23-12771, via H05).

### 1c. NaI gamma spectrometer on the same drone: K, U, Th, radon and a moisture proxy
- **Signal.** Hydrothermal alteration moves potassium. Adularia and sericite add K. Argillic alteration strips it. Thorium barely moves, so the **K/Th ratio** flags alteration. Fault zones that leak gas show higher **radon daughters (Bi-214, the "U" window)**. These are the same channels as Earth MRI radiometrics, but at 30 m height the footprint is about 60-90 m across instead of several hundred metres (judgement: footprint radius about 2-3 times height).
- **Depth.** Gamma sees only the top 30-50 cm of soil. This is a **surface alteration and fault-gas** tool, not a depth tool.
- **Counting noise (calc).** A 2 L NaI at 30 m might see about 40-80 counts per second in the K window. That is 11-16% noise in 1 s and 4-7% in 10 s, which is about 70 m of flight at 7 m/s. So K/Th maps at about 50-100 m resolution are usable.
- **Moisture proxy.** Water in soil absorbs gamma rays. All windows drop by about 1% per 1% of volumetric water (from memory, unverified). The ratio of the 2 m-station gamma count to a dry-day baseline gives a free moisture estimate for the 2 m thermal model.
- **Radon is noisy.** Radon in air swings with pressure, wind and time of day. Use it only as a repeat-pass relative channel, and only in calm early mornings.

### 1d. Drone LiDAR: scarp age, step-overs, tufa and sinter
- **Signal.** Fault scarps degrade by slope diffusion. The scarp profile gives a "morphological age" κt, where κ is a diffusion constant fitted on dated shorelines. Hanks and others used Lake Bonneville shorelines for κ near 1 m2 per thousand years in the Basin and Range (from memory, unverified). With κt from a profile, a scarp can be put into age classes: Holocene, latest Pleistocene, or older.
- **Why drone and not 3DEP.** 3DEP QL2 lidar is about 1 m with about 10 cm vertical error (from memory, unverified). That is enough for scarps over 1 m. A drone at 60-80 m height gives 5-10 cm DEMs and resolves 20-50 cm scarps, the small fresh breaks at step-over tips that often carry upflow. It also maps tufa mounds, sinter terraces and fissures under sagebrush (multiple returns).
- **What it gives the model.** Fault recency per segment (rank 2 proxy), exact step-over and termination geometry (rank 6), and a terrain model that makes the gravity corrections better.

### 1e. Targeted SWIR on fault footwalls: small alteration patches
- **Signal.** Kaolinite, alunite, opal, smectite and buddingtonite have absorption features at about 2.16-2.21, 2.17 and 1.76, 2.21-2.26 um and 2.12 um. Kraal and Schwering (2024, Sandia, GRC Trans 48) found that the best blind-system clues are **1-500 m2 exposures in footwalls of Quaternary faults**, too small for ASTER (30-90 m) and EMIT (60 m) (`D10`, https://www.osti.gov/biblio/3009542).
- **Drone resolution.** A SWIR line-scanner at 50 m height gives about 3-5 cm pixels on a narrow swath. A 1 m2 patch is hundreds of pixels.
- **Depth.** Surface only. It finds **fossil or leaking** alteration. Fossil vs live is split by co-located gamma radon, 2 m probes and fluid chemistry (`M10`).
- **Precedent.** Columbus Salt Marsh was a new blind system found by 4 m airborne hyperspectral, then confirmed with about 100 two-metre probes (H05, M10).

### 1f. Cosmic-ray neutron cart (v2 only)
- **Signal.** Fast neutrons above the ground are slowed by hydrogen. A neutron counter on a vehicle maps area-mean soil moisture over a footprint of about 130-240 m radius to about 15-70 cm depth (Zreda, Desilets and Franz; Schrön and others, from memory, unverified).
- **Why it is v2.** The 2 m temperature anomaly depends on thermal conductivity and diffusivity over the top 2 m, which moisture changes. But the neutron cart only sees the top few decimetres, and M21's 1.2 C noise floor is mostly season and single snapshots, not moisture. A needle probe at the station, plus logging probes (`H01`), fixes more of the error for less money (judgement).

## 2. Concrete v1 design

### 2a. Parts list (prices are estimates, unverified)

| Item | Example class | Qty | Unit cost | Total |
|---|---|---|---|---|
| Heavy-lift drone, US-built, RTK, about 8-10 kg payload | Inspired Flight IF1200A or Freefly Alta X class | 2 | $30-45k | $60-90k |
| OPM magnetometer, towed bird, about 1 kg | Geometrics MagArrow II class | 1 | $35-50k | $35-50k |
| Mag base station (ground, OPM or proton) | GEM GSM-19 class | 1 | $8-15k | $8-15k |
| Drone gamma spectrometer, 2 L NaI or CsI, 1024 channels | Medusa MS-2000 / Radiation Solutions class | 1 | $30-60k | $30-60k |
| Drone LiDAR + RGB, survey grade | YellowScan Mapper+ / DJI-free class | 1 | $25-60k | $25-60k |
| Relative gravimeter | Scintrex CG-6 (buy used, or rent) | 1 | $90-130k buy; $1.5-3k/week rent | $0-130k |
| UTV + self-levelling, shock-isolated gravimeter mount, roof RTK | Polaris Ranger class plus custom mount | 1 | $25-35k | $25-35k |
| RTK GNSS base and rovers | Emlid Reach RS3 class | 3 | $2.5-3k | $8-9k |
| Handheld SWIR point spectrometer (0.35-2.5 um) | ASD TerraSpec / Spectral Evolution oreXpress class | 1 | $40-60k (or rent $3-5k/month) | $0-60k |
| Field laptop, rugged tablets, Starlink Mini, batteries, chargers, generator | | 1 set | | $15-25k |
| Trailer (drone ops, battery charging, gravimeter base) | | 1 | | $10-15k |
| **v1 total** | | | | **about $330-480k buy / $200-260k rent-heavy** |

V2 adds: SWIR line-scanner (HySpex Mjolnir S-620 or Headwall Micro-Hyperspec SWIR class, about $120-250k) and a cosmic-ray neutron cart (Hydroinnova / Finapp class, about $25-60k). V2 total about $500-750k. This matches the brief's $250-600k for a lean v1 and goes over it for the full fleet.

### 2b. Dimensions, power and comms
- **Drone mag + gamma flight.** The mag bird hangs 3-4 m below the drone on a cable to escape motor noise. The gamma crystal (about 4-6 kg with electronics, about 10 x 10 x 40 cm) rides on the airframe. Total payload about 6-8 kg. Flight 30 m above ground with terrain following from the LiDAR DEM, 40 m line spacing, 7 m/s, about 20-25 minutes per battery set (calc: about 9 line-km and 0.37 km2 per flight).
- **LiDAR flight.** 60-80 m above ground, 10 m/s, about 30 minutes per flight, about 1 km2 per flight with 50% overlap (calc).
- **Power.** Drone packs about 1-2 kWh per flight set. One 5-7 kW inverter generator in the trailer charges 4-6 sets in rotation. The gravimeter runs on its own batteries (about 10-12 h).
- **Comms.** Drones log on board and stream health by radio link. Starlink Mini in the trailer pushes raw files to the cloud each night. Gravity readings, RTK and tilt go to a tablet with live drift and Bouguer QC, so bad stations are re-read before leaving.
- **Software.** Open tools: Geosoft-free mag processing in Python (Fatiando a Terra `harmonica`, `verde`), gamma full-spectrum NASVD smoothing, PDAL for LiDAR, a scarp-diffusion fitter, and a joint gravity-mag-HVSR basement inversion that outputs **posterior samples of basement depth and fault position** for the model.

### 2c. Deployment method: the "structure day"
1. **Desk cue.** VOI-Bank ranks candidate blocks by EVSI per dollar. The automated FSS detector (M11) and Earth MRI give a prior fault corner with a +/-600-1,000 m error ellipse.
2. **Day 1, LiDAR first.** Fly a 3 x 3 km box (9 km2) centred on the corner. This takes about 9 flights, or most of a day (calc). Process overnight into a 10 cm DEM. Flag scarps, fissures, mounds.
3. **Day 2, mag + gamma.** Fly the same box at 40 m lines with terrain following from the new DEM: about 25 flights over 1.5-2 days with two drones (calc: about 5.5 km2 per drone-day).
4. **Days 1-3 in parallel, gravity rover.** One person drives a 200 m grid on every two-track and walks short legs (backpack mount) across the gaps. About 120 stations a day (calc), so about 250-350 stations over the box. Base station loops every 2-3 hours. HVSR points from the P23 kit at every 5th station.
5. **Day 3, SWIR ground truth.** Walk the footwall scarps flagged by LiDAR and the gamma K/Th anomalies, taking point SWIR spectra every 20-50 m and on every bleached patch.
6. **Night 3.** Joint inversion. Output a fault-corner location with an error ellipse, a basement-depth map with errors, scarp-age classes and an alteration point map. VOI-Bank re-ranks the block and either nominates (on BLM), sends a landman (on private land) or drops it.

**Crew time per site.** 2-3 people for 2-3 days per 9 km2 box, about 6-8 person-days. Fleet throughput is about 60-80 blocks per field season of 8 months (judgement).

### 2d. Cost per site and per km2 (calc, unverified rates)
- Mag + gamma: about $360/km2 (2 crew at $1.4k/day, $350 amortization, $250 processing, 5.5 km2/day). With two drones in parallel, about $200-250/km2.
- LiDAR: about $150/km2.
- Gravity: about $25-40 per station, so $7-12k per box.
- **Full structure day per 9 km2 box: about $10-20k all-in**, or about $1.1-2.2k per km2. The drone channels alone are about $350-500/km2, near the top of the brief's $100-300 range.

## 3. Legal access

- **BLM.** IM 2026-024 lists "ground geophysics (gravity, magnetics, EM, seismic, MT)", "drone and airborne surveys" and field mapping and hand sampling as casual use, with no notice or application (https://www.blm.gov/policy/im-2026-024; H13). Nothing here is left in the ground. A field office can still pull an activity out of casual use where it expects significant disturbance, most likely in sage-grouse habitat, WSAs and cultural sites (H13).
- **Off-road travel.** The UTV gravity rover must stay on existing roads and two-tracks in most BLM travel plans (from memory, unverified). Fill gaps on foot with a backpack mount. Do not drive cross-country.
- **Wilderness and WSAs.** Do not take off or land drones inside wilderness (motorized equipment ban, from memory). Fly from outside where line of sight allows, or skip.
- **FAA.** 14 CFR Part 107: visual line of sight, under 400 ft, aircraft under 55 lb (https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-107). A 3 x 3 km box can be flown from 2-3 take-off points within visual line of sight. A BVLOS rule (proposed Part 108) would roughly double daily coverage (from memory, unverified).
- **Hardware sourcing.** Use non-DJI, US-built airframes. The FCC covered-list and federal procurement limits on Chinese drones make DJI a supply and reputational risk (from memory, unverified).
- **Private land.** Fly and drive only with the owner's written OK, signed on the same visit as the heat option (H06 "logger as landman").
- **State trust land.** A right-of-entry or exploration permit is usually needed (R05, unverified per state).
- **Disclosure.** Data from unleased federal land need not be filed (43 CFR 3253.10(b), H13). The maps stay private until we nominate.

## 4. Prior art

- **Gravity and magnetics for blind systems** is standard. PFA phase 2 shot 237-415 new gravity stations per prospect (L01). USGS framed Granite Springs with gravity, ground mag, MT and a basement inversion (M09). Gabbs Valley's blind target was a concealed fault intersection found from gravity and magnetics (L22).
- **Drone mag** for volcanic alteration (EGU23-12771, via H05) and for mineral exploration is routine. **Drone gamma** is used in uranium and potash exploration and in nuclear site surveys (from memory).
- **LiDAR scarp mapping** is standard in paleoseismology (Qfaults, NSHM). Diffusion dating of Basin and Range scarps goes back to Wallace (1977) and Hanks and others (1984) (from memory, unverified).
- **Small-patch hyperspectral** for blind systems: Kraal and Schwering 2024 (AVIRIS-classic at 14 m) and Columbus Salt Marsh (ProSpecTIR at 4 m) (D10, H05).
- **Cosmic-ray neutron rovers** exist for soil moisture in farm fields (COSMOS rover work, from memory).
- **What is new here.** (a) All channels run together on one block, cued by an EVSI map, in 2-3 days. (b) The output is a set of posterior samples of fault-corner position and basement depth that feed straight into CREAM-COX and THERMOS-B, not a contractor's interpretation. (c) It is timed to the rights move (nominate or option the right 640 acres). Zanskar uses public gravity/mag HGM layers and runs large-N seismic arrays at prospects (Z03, M12). We found no sign that it runs drone mag, gamma or gravity rovers before nominating (absence of evidence).

## 5. Uncertainty reduced (which ranked uncertainty, and by how much)

| Rank | Today | With P28 | How (calc or judgement) |
|---|---|---|---|
| **6 Upflow location and footprint** | Fault corner from FSS + Earth MRI: about +/-600-1,000 m. P(in nominated 640-ac block) 0.34-0.67; P(in right 500 m parcel) 0.04-0.10 | +/-150-250 m. P(in block) about 1.0; P(in 500 m parcel) about 0.4-0.6 | Gaussian location error on square cells (calc). Biggest gain of this build. It also halves the darts and E-MT stations needed per site because they go on the right strand. |
| **7 Conductive background and position** | Basin depth +/-200-300 m (1990 grid, worse below 1.2 km). T(1.5 km) error about +/-10-14 C from depth alone | +/-80-120 m with gravity + HVSR + well ties. T(1.5 km) error about +/-4-6 C | Fill k = 1.2 vs basement 2.8 W/m/K, q = 0.1 W/m2 (calc). Overlaps with P23; P28 adds the lateral fault geometry HVSR lacks. |
| **2 Permeability class (fault recency, density)** | Qfaults recency classes, mapped by hand at different scales | Scarp-age class per segment, small breaks at step-over tips, alteration density | Recency is a weak proxy for permeability. Judgement: about 10-20% shrink of the rank-2 spread (10x on MWe to about 8x). |
| **4 Sensor reliability s/q** | 2 m noise floor about 1.2 C | about 1.0-1.1 C | Gamma moisture proxy plus LiDAR albedo, slope and aspect terms. Small (judgement). |
| **1 Detection gap** | λ from FSS + GBM | Sharper λ per block. Mag lows and K/Th as a second, mask-independent detector of fossil upflow | Helps the "designed two-detector survey". Judgement: under 10% of the rank-1 spread on N. |

**In-silico check to run (GHOST Tier 1).** Simulate 1,000 synthetic blocks with random fault corners, fill depth and host magnetism. Compare EVSI per dollar of (a) Sentinel + darts placed from the FSS prior, vs (b) a P28 structure day first, then Sentinel + darts. Pass if (b) wins in at least 60% of high-λ blocks.

**Net.** P28 shrinks ranks 6 and 7 a lot and rank 2 a little. It barely moves rank 1, which drives the regional "how much hidden" total. Its main value is that every later dollar (Sentinel visits, darts, E-MT, a gradient hole) lands on the right 500 m parcel.

## 6. Rights edge

- **Fewer blocks per prospect.** To hold the upflow with 90% confidence we need about 9 blocks (5,760 acres) at +/-600-1,000 m error, but 1 block at +/-400 m or better (calc). After a structure day, one or two blocks are enough. BLM leftover noncompetitive land costs $1/ac/yr, so the direct rent saving is small. The real saving is in **competitive auctions** (Utah EGS land clears at $111/ac on average, H12; Nevada auction prices about $40/ac, H06) and in **signal**: each nominated block tells Zanskar and Ormat where we look.
- **Decoy room.** With a tight ellipse we can nominate the one right block and spread decoys elsewhere at little cost.
- **Private land.** It picks which ranch to option first in a valley with several owners. At $1-2/ac, the saving is landman time, not option money.
- **Speed.** 2-3 days per block. A structure day can run in the gap between a Sentinel anomaly and a BLM nomination window, so we never wait months on a contractor.
- **Buyer package.** A buyer re-drills before committing capital (hardware MEMO). But a package with a 3D fault model, a dated scarp and an alteration map at the drill pad is easier to price than a heat anomaly alone (judgement).

## 7. Risks

1. **Non-magnetic hosts.** In carbonate and thick sediment the mag-low channel is dead. The eastern carbonate province, which the model expects to move up, is exactly where it fails.
2. **Gravity station geometry.** Road-bound stations miss the key fault crossing. Backpack legs fix it but are slow.
3. **Fossil vs live.** Mag lows, K/Th and SWIR minerals record old upflow too. Without heat data they create false positives.
4. **Commodity hardware, no moat.** Every payload is off the shelf. Contractors can fly the same kit. The moat is only the cueing (EVSI map) and the private data.
5. **Cost creep.** A full fleet with SWIR imager and neutron cart passes $600k. Most of the value is in gravity + mag + LiDAR.
6. **FAA and supply.** BVLOS limits slow coverage. US-built airframes cost 2-3x DJI.
7. **BLM field office calls.** UTV travel limits, sage-grouse timing, WSAs.
8. **Overlap with P23 (HVSR) and P03 (E-MT).** Basin depth is also measured by those. Double counting the rank-7 gain is a risk. The joint inversion must share one depth posterior.
9. **Radon and gamma noise.** Weather, moisture and surface lag (talus, playa crust) can mask K/Th signals.

## 8. First test

**Weeks 0-10, about $40-70k (rent everything).**
1. **Desk, weeks 0-2, about $0-5k.** Pull Earth MRI mag + radiometrics, 3DEP lidar and PACES gravity for **Gabbs Valley, Granite Springs and one cold control valley**. Run the joint inversion. Record the fault-corner ellipse and pre-register it.
2. **Field, weeks 3-8, about $35-60k.** Rent a CG-6 (about $2-3k/week), a drone mag + gamma package and a LiDAR drone, or hire one drone contractor. Run one structure day at each of the three sites.
3. **Pass if:** (a) the structure-day ellipse is at least 3x smaller in area than the desk ellipse at both known sites; (b) the known upflow (from published drilling) lies inside the 90% ellipse at both; (c) the control valley shows no false corner with a mag low and K/Th anomaly together; (d) cost is under $20k per site.
4. **Kill or shrink to gravity + mag only if:** the ellipse does not shrink by at least 2x, or the known upflow falls outside it at either site, or field offices bar the UTV rover from the needed two-tracks.

## Sources

- Repo: `M09-gravity-magnetics.md` (Saltus and Jachens OFR 90-404, https://pubs.usgs.gov/of/1990/0404/report.pdf; GeoDAWN DOI 10.5066/P93LGLVQ; Eastern Great Basin DOI 10.5066/P13VSMZ3), `M10-remote-sensing.md`, `M11-structural-settings.md`, `M21-shallow-temperature.md`, `P09`, `P13`, `P23`, `../../evidence/D10-satellite.md`, `../../evidence/L22-structural-ml.md`, `../../../hardware/evidence/H05-quantum-novel-sensors.md`, `H06`, `H12`, `H13`.
- Kraal and Schwering 2024, hyperspectral in the Basin and Range: https://www.osti.gov/biblio/3009542
- BLM IM 2026-024, casual use: https://www.blm.gov/policy/im-2026-024
- 14 CFR Part 107: https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-107
- Scintrex CG-6: https://scintrexltd.com/product/cg-6-autograv-gravity-meter/
- Geometrics MagArrow (via reseller): https://maverickdrone.com/products/geometrics-magarrow-mk2-magnetometer
- From memory, unverified: scarp diffusion dating (Wallace 1977; Hanks and others 1984), cosmic-ray neutron footprint (Zreda, Desilets, Franz; Schrön), gamma moisture attenuation, drone, gamma, LiDAR and SWIR imager prices, BLM travel-plan rules, proposed FAA Part 108.
- Own arithmetic: `P28_calc.py`.
