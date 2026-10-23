# P03: E-MT Node 2.0, a drone-placed DC-coupled telluric + SP + 3C geophone node with a ranch magnetic reference

Date: 23 Oct 2026. Build candidate P03, model track. This builds on `../../../hardware/evidence/H03-mt-seismic-nodes.md` (E-node v1, BOM, cost per site, first test), `M08-magnetotellurics.md` (why E-only works, the 250-500 m spacing need, the conductor non-uniqueness problem), `M12-seismology.md` (the "seismo-telluric" geophone add-on), `M09-gravity-magnetics.md` (gravity basin depth is only ±200-300 m good), `M30-permeability.md` (SP as a flow signal), `../../../hardware/evidence/H13-permits-and-secrecy.md` and `V01-redteam-heat-stack.md` (BLM IM 2026-024 casual use, the "mechanised" grey area), `P01-ranch-well-sentinel-2-0-a-resident-well-.md` (the well robot this node pairs with) and `../MODEL.md` (SENTINEL-COX and the ranked uncertainties). It does not repeat them.

**Method note.** The shared web-search budget for this workflow turn (200 calls) was used up before this agent started. All searches were refused, so **no new web pages were read**. Sources below are either repo files (which cite URLs) or standard literature I know. Anything from memory is marked (from memory, unverified). All prices are my estimates and are (unverified) unless a repo file gives a source. The physics numbers marked (calc) are my own arithmetic from textbook formulas.

## Bottom line

Build it, but fix three things in the brief first.

1. **A single 1-1.5 kg spike cannot measure the E-field on its own.** MT and SP need two electrodes some distance apart. So v1 is a **hub plus two drone-laid wire legs**. The drone lowers the hub, then flies 40 m north and 40 m east, paying out a thin wire from a spool and dropping a small electrode dart at the end of each leg. That is the same wire-dispensing trick that fibre-optic FPV drones now use over many kilometres (from memory, unverified). Signal is not the problem: a 40 m dipole gets roughly 300x more natural MT signal than amplifier noise at 1 Hz in 10 ohm-m ground (calc, section 1a).
2. **Chargeability (IP) needs a current source.** Natural fields give no IP. v1 adds a **road-side IP transmitter**: a generator and transmitter driving 5-10 A into a 1-2 km wire laid along an existing road or ranch track. Every node within about 1-1.5 km records the full decay on its DC-coupled legs. This is the single most valuable upgrade over the prior pick, because **IP separates a smectite clay cap (chargeable) from basin brine (conductive but not chargeable)**. That is the main false-positive class in M08.
3. **A 4.5 Hz geophone cannot see deep basins with HVSR.** The resonance of 1-2 km of fill sits at about 0.1-0.2 Hz, below what a 4.5 Hz element can read well. So the geophone gives HVSR basin depth only for fill shallower than about 300-600 m. For deeper fill, **MT itself gives depth to resistive basement**, which is the better tool there. The model should treat basin depth as a joint MT + HVSR + gravity product.

With those fixes the node is about **$380-450 BOM at 1,000 units** (about $750-900 for a 30-unit prototype run), about **1.3 kg hub + 2 x 0.12 kg darts**, and runs **6 weeks** on LiFePO4 plus a small panel. A ranch base station (buried home-wound induction coils, fluxgate optional, RTK base, LoRa gateway, barometer, Starlink) costs about **$4-7k** and is given to the rancher as a farm RTK base and weather station. One carpet at 250 m spacing costs about **$1.5-3k per km² all-in** once the fleet exists, or about **$0.6-1.2k per km² at 500 m** (calc, section 4). Placement is about 120-200 sites per day with 2-3 drones under VLOS rules. The real bottleneck is recovery, which in v1 is on foot from roads.

My estimate is that in a carpeted cell it cuts **rank 7 basin depth error from about ±300 m to about ±100-150 m** (temperature error from about ±18 C to about ±6-9 C at 60 C/km), **rank 3 lid-thickness uncertainty by about 40-60%** for clay or conductive lids thicker than about 150-200 m, and **rank 6 footprint area spread from about 3x to about 1.5x**. Its biggest value is **rank 1**: it is a detector whose blind spot (no clay, low contrast) is different from the Sentinel's blind spot (cold-water lids). Run on the same cells, the two detectors let the model *estimate* the lidded catch rate instead of assuming it. About 25-40 carpets over 2 years should pin the lidded-system catch rate to about ±0.1, which I estimate shrinks the 2-5x band on N by about a third to a half (untested).

Self-score: model_uncertainty_alpha 4, rights_alpha 3, buildability 3, cost_scale 4, moat 3.

---

## 1. The physics: what each channel sees, how deep, and how well

### 1a. Telluric field (E) read against a shared magnetic reference: resistivity, cap depth, basin depth
- **Why E-only works.** MT measures the ratio of E to H at the surface. H varies slowly in space, so one magnetic station can serve many E sites. Kruglyakov and Kuvshinov (2019) showed in 3D synthetic tests that the "inter-site impedance" (E at each site, H at one reference) inverts about as well as full single-site MT, and the reference location matters little (via M08: https://earth-planets-space.springeropen.com/articles/10.1186/s40623-018-0972-8). The LPTR telluric logger matched a commercial ADU07 from 5 s periods up, with the magnetic reference some distance away (via H03: https://meetingorganizer.copernicus.org/EGU21/EGU21-16275.html).
- **Caution on reference distance.** The field match in EGU21-16275 starts at 5 s. At short periods (AMT, above about 10 Hz) over conductive valleys, H changes more over a few km (from memory, unverified). So the 5-10 km ranch mast works as a **remote reference and long-period H source**, and each carpet also gets one **portable coil set within about 1-3 km** for the short periods. EGU26-7264 (via M08) adds a handful of 3-component H sites to cut 3D "speckle". v1 follows that: 1 portable coil set per carpet plus the ranch mast.
- **Depth of investigation.** Skin depth is about 503 x sqrt(rho x T) m (textbook). In 10 ohm-m ground: 1,000 Hz gives about 50 m, 100 Hz about 160 m, 1 Hz about 1.6 km, 0.1 Hz about 5 km (calc). A smectite cap at 100-1,000 m needs about 1-1,000 Hz. A 1-3 km upflow root needs about 0.01-1 Hz. Six weeks of recording lets us stack the weak "dead bands" (1-5 kHz and 0.5-5 s; M08).
- **Signal versus noise on a 40 m dipole (calc, natural-field levels from memory, unverified).**
  - At 1 Hz, with a natural field of about 30 pT/sqrt(Hz) and 10 ohm-m ground, |Z| = sqrt(omega mu rho) is about 0.009 ohm. E is about 0.2 microV/m/sqrt(Hz), so a 40 m dipole sees about 8 microV/sqrt(Hz). A chopper front end plus Pb-PbCl2 electrodes is about 10-30 nV/sqrt(Hz) at 1 Hz (Petiau 2000, Pure Appl. Geophys.; from memory). **SNR about 300.**
  - At 2 kHz in the dead band, with about 0.05 pT/sqrt(Hz), E is about 16 nV/m/sqrt(Hz), so about 0.6 microV/sqrt(Hz) on 40 m. Amplifier noise there is about 5-10 nV/sqrt(Hz). **SNR about 60-100** before stacking.
  - So 40 m legs are plenty for signal. They are kept that long (not 5 m) for two other reasons: near-surface distortion (static shift) averages out over a longer dipole, and electrode drift and contact noise matter less relative to the signal.
- **What we get.** A 3D resistivity cube from about 30 m to 3+ km at 250 m (or 500 m) lateral pitch. The cap shows as a 1-10 ohm-m layer. Its top and base depth come out to about ±15-25% where it is well sampled (from memory, typical of 3D MT practice; unverified). Basin fill over resistive basement (carbonate, granite, older volcanics) gives depth to basement to about ±10-20% (from memory, unverified). That beats gravity's ±200-300 m (M09) for fill deeper than about 1 km.

### 1b. Chargeability (IP): the brine-versus-clay discriminator
- **The problem it solves.** In the Great Basin a shallow conductor can be a hot-system smectite cap, saline basin water, lake or playa clay, or a fossil cap (M08, V01). Resistivity alone gives maybe a 2-3x likelihood ratio (M08 estimate).
- **The physics.** Smectite has a very high cation exchange capacity, so it stores charge at grain surfaces and is strongly chargeable. Brine conducts by ions in the pore water and is barely chargeable. Revil and co-workers showed that normalised chargeability tracks smectite content and CEC, and Lévy and co-workers used IP at Krafla to map the clay cap separately from pore-water conduction (from memory, unverified; Revil et al. 2017-2019 Geophysics/JGR; Lévy et al. 2018-2019). So **resistivity + chargeability** splits "clay" from "salt water". Lake clay is still chargeable, so it does not remove that false positive. It does remove brine.
- **Signal (calc).** Transmitter 5 A into 10 ohm-m ground. At 1 km from a current electrode, E is about rho I / (2 pi r²), about 8 microV/m, so about 0.3 mV on a 40 m leg. A chargeability of 20 mV/V gives about 6 microV of decay. Natural noise per cycle on 40 m in the 1-10 Hz decay window is maybe 10-30 microV (estimate). Stacking about 2,000 cycles (2 s on, 2 s off, about 4-5 hours) cuts noise by about 45x to about 0.5 microV, so **SNR about 10**. Subtracting telluric noise using neighbour nodes and the reference adds more. Practical reach is about 1-1.5 km either side of the transmitter line, so a 5 x 5 km carpet needs 2-3 transmitter set-ups along roads.
- **Depth.** Distributed DCIP with 1-2 km offsets sees roughly the top 300-700 m (from memory, rule of thumb that depth is about 1/3 to 1/5 of the offset; unverified). That is the cap and lid range that matters for rank 3.
- **Prior art.** Combined MT + DC + IP on one distributed spread is standard in mining: Quantec Titan-24 and ORION 3D, and DIAS32 (from memory, unverified). The new parts here are cost, drone placement, weeks-long dwell and the co-located seismic.

### 1c. Self-potential (SP): a weak but free upflow channel
- **Physics.** Moving groundwater makes streaming potentials. Heat makes thermoelectric potentials. Corwin and Hoover (1979, Geophysics) reported SP anomalies of tens to hundreds of mV over geothermal areas (via M30; from memory, unverified). Upflow gives a positive anomaly over the rising zone.
- **The catch.** A true SP map needs every electrode tied by wire to one base electrode, or a leap-frog line. Isolated nodes only measure the **local DC gradient** across each 40 m leg. An anomaly of 100 mV over 500 m is about 0.2 mV/m, or about 8 mV per leg (calc). Paired Pb-PbCl2 electrodes drift about 0.1-1 mV per month and change about 0.2 mV per C of temperature difference (Petiau 2000; from memory, unverified). So SNR is about 3-10 for a strong anomaly and near 1 for a weak or lidded one.
- **How to use it.** Do not integrate gradients across the gaps between nodes. Invert the gradient field directly for buried current sources, as a weak likelihood. Log electrode temperature in the hub to correct the thermal drift. Treat SP as a bonus that costs nothing: it is the DC part of the same ADC channel.

### 1d. 3C 4.5 Hz geophone: shallow Vs, HVSR basin depth, microseismic catalogue
- **Ambient-noise Vs.** Cross-correlating noise between nodes 250 m to 3 km apart gives surface waves at about 0.7-5 Hz. Depth sensitivity is about one-third of a wavelength, so roughly 50-600 m (calc, for Vs 400-1,500 m/s). Hengill used about 500 nodes of this class to image low-velocity zones in the top 500 m (via H03: https://escholarship.org/content/qt5mj7r09n/qt5mj7r09n.pdf).
- **HVSR basin depth.** The H/V peak sits at f0 = Vs / (4H) (Nakamura 1989; Ibs-von Seht and Wohlenberg 1999 power law; from memory). With a 24-bit ADC, a 4.5 Hz element is usable down to about 0.5 Hz (from memory, unverified). With fill Vs of 400-800 m/s, that limits HVSR to **fill thinner than about 300-600 m** (calc). Option: fit 2 Hz elements to about 20% of hubs (about +$60 each, unverified) to reach about 0.2 Hz and about 1 km.
- **Microseismic.** 250 Hz sampling on a dense grid catches local events down to about M -0.5 to 0 inside the carpet (from memory, unverified). In 6 weeks most Great Basin carpets will catch only a handful. That helps rank 2 a little (locates active faults). Real focal mechanisms need the 3-6 month long-dwell subset from M12.
- **Coupling.** A dropped spike couples well below about 20 Hz in soft alluvium, which is the band we use. On caliche or bedrock it may sit loose. The hub reports tilt and an H/V quality flag by LoRa so the crew can re-drop.

### 1e. Detection limits in one table

| Quantity | v1 resolution (estimate) | Needs | Model input |
|---|---|---|---|
| Resistivity, 30 m to 3 km | ±10-20% in log rho near stations | 3-6 weeks, 1 coil set within 3 km | cap geometry, basin depth |
| Cap top / base depth | ±15-25% | cap >150-200 m thick, 3+ stations across | lid thickness (rank 3), cap base ~ 180-220 C isotherm |
| Depth to resistive basement | ±10-20% (±100-200 m at 1 km) | resistivity contrast >5x | basin depth (rank 7) |
| Chargeability | ±3-5 mV/V within 1-1.5 km of Tx line | road Tx, 4-5 h stacking | clay vs brine class |
| SP gradient | ±1-2 mV per 40 m leg | weeks of logging, temp-corrected | upflow source (weak) |
| Vs, top 50-600 m | ±5-10% | 2+ weeks of noise | fill thickness, fault offsets |
| HVSR f0 | ±5-10% where f0 > 0.5 Hz | 1+ day | basin depth < 300-600 m |
| Microseismic | M > -0.5 to 0 inside carpet | weeks | active faults (rank 2, weak) |

---

## 2. v1 design

### 2a. Layout
- **Hub (one per site).** It holds all electronics, the 3C geophone, battery and panel. It also carries the common electrode (a Pb-PbCl2 element in a porous ceramic ring about 20-25 cm down the spike).
- **Two legs.** The drone pays out 45 m of thin wire north and east and drops a dart electrode at the end of each. Ex = V(north dart) - V(hub electrode). Ey = V(east dart) - V(hub electrode). That is an L-dipole. The EDE and LPTR loggers used crosses (via H03). L is fine for MT and saves a third drop.
- **Fallback with no wire (v1b, for bad terrain).** Three 1.5 m spring-out legs. Signal is still adequate (about 0.3 microV/sqrt(Hz) at 1 Hz, calc), but static shift and drift are worse. Use it only where wire is not allowed.

### 2b. Parts list (per hub, at 1,000 units; all prices unverified estimates)

| Item | Part class | Cost |
|---|---|---|
| 8-ch 24-bit delta-sigma ADC, DC-coupled | ADS131M08 / ADS1278 class | $15 |
| Low-noise chopper front ends (2 E + 3 seismic), 10 GOhm input, input protection | LTC2057 / INA333 class | $20 |
| MCU, low power | STM32L4/U5 class | $6 |
| GNSS timing receiver + TCXO | u-blox M10 / timing class | $30 |
| LoRa radio | SX1262 module | $8 |
| 64 GB industrial microSD | | $15 |
| PCB, assembly, tilt sensor, temp sensors (hub electrode + air) | | $35 |
| 3C geophone, 4.5 Hz, 3 elements | SM-24 class | $90 |
| Battery: 4 x LiFePO4 32700 (about 77 Wh) + BMS | | $30 |
| 2 W solar ring on the cap | | $10 |
| Housing: 60 mm tube, shock mount, 250 mm steel spike, lifting loop | glass-filled nylon or aluminium | $40 |
| Electrodes: 1 hub + 2 dart Pb-PbCl2 in gel sleeves | own-made, Petiau type | $40 |
| Wire: 2 x 45 m, 0.3 mm insulated copper-clad aramid, breakaway links | | $8 |
| Spare and losses allowance | | $30 |
| **Total** | | **about $380-450** |

Prototype run of 30: about $750-900 each (unverified).

### 2c. Dimensions and mass
- Hub: 60 mm diameter x 350 mm body, plus a 250 mm spike. About 1.25-1.35 kg (batteries 0.6 kg, geophone 0.3 kg, housing and spike 0.35 kg, rest 0.1 kg).
- Dart: 20 mm x 200 mm, weighted tip, about 0.12 kg, with a hydrogel or bentonite sleeve for contact in dry soil. Contact resistance in dry alluvium may be 1-50 kOhm (from memory, unverified). That is fine with a 10 GOhm input, but noise rises, so the hub logs contact resistance daily.

### 2d. Power and storage
- Continuous: 3 seismic channels at 250 Hz, 2 E channels at 128 Hz. Night bursts: E at 4-8 kHz for about 10 minutes per hour. GNSS on during bursts and every 10 minutes for timing. IP windows are sampled at 1 kHz on a schedule.
- Draw about 80-120 mW average, so about 2-3 Wh per day (calc). The 77 Wh pack alone gives about 4-5 weeks. The 2 W panel adds about 4-6 Wh per day in Nevada sun (estimate), so 6+ weeks is easy and 3-6 months is possible for the long-dwell subset.
- Data: about 0.4-0.6 GB per day, about 20-25 GB per 6 weeks (calc). 64 GB card.
- Timing: GNSS PPS gives under 1 microsecond. The TCXO holds about 0.1 ppm between fixes, which is good enough for all bands once each burst is GNSS-locked (calc).

### 2e. Comms
- LoRa to the ranch mast gateway (5-15 km in open desert, line of sight; from memory, unverified). Each hub sends position, battery, tilt, contact resistance, daily H/V peak, a band-by-band MT coherence score and event triggers. Raw data stay on the card.
- The crew sees a live map of which sites are bad and re-drops them during the same deployment. Later, a compute-heavy neural inversion surrogate (M08 idea 6) runs on the LoRa summaries to say where to add nodes.

### 2f. Ranch base station ("farm RTK mast")
- 6 m mast with solar and battery, LoRa gateway, RTK GNSS base (NTRIP via Starlink for the rancher's tractors and sprayers), barometer and rain gauge.
- Buried: 3 home-wound induction coils in short trenches (about $400-800 each, H03) on a reference logger. A fluxgate is optional for periods longer than about 100 s, which we rarely need.
- Cost about $4-7k including Starlink kit (unverified). Rancher pays nothing. We keep a written data and access agreement.
- **Honest caveat on the gift.** Several western states already run free CORS/RTK networks, and many farm-equipment dealers sell RTK subscriptions. So the RTK gift is worth more on remote ranches with no cell coverage than near towns (unverified). The weather station and a water-well link to the P01 robot make the bundle stickier.
- **Portable coil set** (one per carpet, within 1-3 km): the same coils and logger on a tripod-free ground mount, about $2.5k (H03 figure).

### 2g. Road-side IP transmitter
- 5-7 kW generator, a 5-10 kW time-domain transmitter, and 1-2 km of insulated wire laid along an existing road or track, grounded at each end by stake clusters with salt water.
- Commercial transmitters cost about $30-60k (unverified). An own-built IGBT unit is a few weeks of work and about $5-8k in parts (estimate).
- Duty: 2 s on, 2 s off, alternating polarity, 4-6 hours per set-up, 2-3 set-ups per carpet.

### 2h. Drone kit and deployment method
- **Aircraft.** A heavy-lift multirotor under 55 lb total take-off weight so it stays under Part 107. That means about 5-8 kg of payload (unverified). Above 55 lb (for example agricultural spray drones) needs a 49 USC 44807 exemption, which many ag operators already hold (from memory, unverified). Prefer an NDAA-compliant US airframe, because of federal limits on Chinese drones (from memory, details unverified). Cost about $25-45k per aircraft with winch.
- **Payload.** A 3-hub magazine with release hooks, 6 darts and 6 wire spools with cutters. About 5 kg per sortie.
- **Per-site sequence.** Hover at 3-5 m and lower the hub on the winch until the spike touches, then release from about 0.5-1 m (no free fall, so no shock damage). Clip the wire start to the hub. Fly 45 m north, paying out wire at 2-3 m height. Cut and drop the dart from about 2 m. Return over the hub and repeat east. About 3-4 minutes per site (estimate).
- **Rate.** 3 sites per 15-minute sortie plus a 5-minute battery and magazine swap gives about 9 sites per hour, or about 60-75 per drone per 8 flying hours. Two to three drones with two pilots and a loader: **about 120-200 sites per day** (calc). That is the lower half of the brief's 150-300. An ag-class drone under 44807 carrying 15-20 hubs could reach 200-300.
- **VLOS.** Part 107 needs visual line of sight. That means about 1-1.5 km from the pilot for an aircraft this size (estimate). So the truck parks on roads and works a 2 x 2 km block, then moves. True BVLOS would need a waiver or the coming Part 108 rule (the NPRM came out in 2025; final status in late 2026 unverified).
- **Dropping objects.** 14 CFR 107.23(b) bans dropping objects only "in a manner that creates an undue hazard" (from memory). Lowering on a winch over empty range is very likely fine, but it goes in the lawyer's memo.
- **Recovery (the real bottleneck).** v1 recovers on foot: one person walks a line from the road, pulls the darts, reels the wire onto a hand spool, lifts the hub. About 6-10 minutes per site plus walking, so 40-60 sites per person-day within 1-2 km of a road (estimate). v2 adds drone recovery: the drone hooks the hub's loop, and a small motor in the hub reels the legs in first (snag risk to be tested).

### 2i. Crew time per site and per km²

| Step | Per site | Per km² at 250 m (16 sites) | Per km² at 500 m (4 sites) |
|---|---|---|---|
| Plan, load, fly, place | 4-7 drone-crew min | 1.5-2 crew-hours | 0.4-0.5 crew-hours |
| Remote QC and re-drops | 1 min | 0.3 hours | 0.1 hours |
| IP transmitter set-ups (shared) | about 2 min | 0.5 hours | 0.5 hours |
| Recovery on foot | 8-12 person-min | 2-3 person-hours | 0.6-1 person-hours |
| Processing (mostly compute) | 2 min human | 0.5 hours | 0.15 hours |

---

## 3. How it enters SENTINEL-COX

- **One latent mask class, two detectors.** MODEL.md puts one latent mask class (open, cold lid, swept, outflow tongue) under all detectors. The carpet gets its own sensitivity and false-positive rate per mask class, s_MT(m) and q_MT(m). Its blind spots differ from the Sentinel's. A cold-water lid hides heat from a ranch-well profile but not a clay cap at 300-800 m. A fault upflow with no smectite (common below about 150 C in carbonate hosts) is weak for MT but may be strong for the Sentinel. Different blind spots are what make a two-detector design identify the catch rate.
- **Physics likelihood, not a raw feature.** Following M08, resistivity and chargeability enter through a rock-physics model: rho(T, porosity, salinity, smectite fraction) and M_n(smectite, CEC). Latent classes are hot cap, fossil cap, lake clay, brine and nothing. The output is a likelihood ratio on "T at 1 km above the Tmin curve" per 500 m parcel, plus the cap-base depth as a soft tie to the 180-220 C isotherm where volcanic hosting makes that rule hold.
- **Basin depth into the 1D column.** MT basement depth, HVSR and ambient-noise Vs are fused with gravity (M09) into one basin-depth posterior per parcel, which feeds THERMOS-B's conductive column.
- **SP and microseismic** go in as weak likelihoods on upflow location (rank 6) and active-fault permeability class (rank 2).
- **Labels.** Each carpet later tied to a P01 well profile or a 10-30 m dart becomes a labelled resistivity-chargeability-temperature triple. After 20-30 such ties we hold the calibration set that M08 found missing everywhere.
- **GHOST Tier 1.** Before any build, simulate carpets on synthetic blind systems (fault upflow, cap, basin fill, brine aquifer, lid) and compute EIG per dollar against the Sentinel and darts. The P03 order (second build, after P01) should be confirmed there.

---

## 4. Costs

### 4a. Capital (fleet of 400 hubs, enough for one 25 km² carpet at 250 m or four 25 km² carpets at 500 m)
- 400 hubs x about $420 = about $170k.
- 3 drones with winches and magazines: about $90-130k.
- 2 portable coil sets + 1 own-built IP transmitter + generator: about $15-25k.
- Truck, charging trailer, spares: about $60-80k.
- Base masts: about $4-7k each, one per ranch hub.
- **Total about $350-420k** (unverified). This is above H03's $130k for 400 E-nodes because it adds drones, IP and geophones.

### 4b. Per deployment (6 weeks, 400 sites)
- Crew: 3 people x about 12 field days (placement about 3 days, recovery about 7 days, IP 2 days) at about $1.5k per person-day loaded, plus vehicles: about $55-70k.
- Losses: 5-10% of hubs to cattle, rodents chewing wire, flood or theft (estimate): about $10-17k.
- Fleet amortisation: about $350k over 16 deployments (8 per year x 2 years): about $22k.
- Compute and processing: about $5-10k.
- **About $90-120k per 400 sites, or about $225-300 per site** (calc).
- **Per km²: about $3.5-4.8k at 250 m spacing, about $0.9-1.2k at 500 m spacing** (calc).
- That is somewhat **higher** than the brief's "$1-2k per km²" at 250 m, because recovery on foot dominates. With drone recovery (v2) crew days fall by about half, giving about $2-3k per km² at 250 m. At 500 m, the brief's figure holds. Contract MT at 60 stations over 25 km² costs about $100-250k (M08), so we get 7x the stations, plus IP, Vs and seismicity, for about the same money.

### 4c. Smart spacing
Use VOI. Run a 500 m carpet over the whole fault setting first (about $25-30k for 25 km²). Then fill to 250 m or 125 m only over anomalies, which costs another $15-30k. That gets most of the information for about $40-60k per prospect.

---

## 5. How much it shrinks the model's dominant uncertainties

All numbers are my estimates (untested). Where they reduce a variance, they apply only to carpeted cells. The regional effect comes through the shared parameters (s/q per mask class, the resistivity-to-temperature map) that every cell uses.

| Rank | Uncertainty | Before (MODEL.md) | After 25-40 carpets | Mechanism |
|---|---|---|---|---|
| 1 | Detection gap, lidded catch rate | 2-5x on N; lidded catch rate essentially a prior | Catch rate for lidded systems estimated to about ±0.1; N band narrows by about 30-50% in log width for B&R states | Second detector with different blind spots, shared latent mask, same cells as Sentinel visits |
| 3 | Lid thickness, masking | Sensitivity 0.8 to 0 | Lid depth ±15-25% where lid >150-200 m and conductive; about 40-60% variance cut in carpeted cells | Cap and lid imaging; IP rules out brine "lids" |
| 6 | Upflow location and footprint | Area spread about 3x; ranch wells see outflow | About 1.5x; location to about ±150-250 m | 250 m cube, SP sources, conductive feeder to depth, Vs fault steps |
| 7 | Basin depth | ±300 m, about ±18 C | ±100-150 m at 1 km, about ±6-9 C | MT basement depth + HVSR + Vs fused with gravity |
| 4 | Sensor s/q per mask class | VOI swings >2x | Gives the MT row of the s/q table from the same 20 blind / 40 cold calibration campaign | Carpet a subset of the 60 calibration cells |
| 2 | Permeability class | about 10x MWe | Small: maybe 10-15% | Active-fault microseismicity, SP flow signal, fault offsets |
| 5 | T at 0.5-2 km | | Moderate where volcanic-hosted caps exist (cap base near 180-220 C); small in carbonate or sediment hosts | Cap base as a soft isotherm |

The headline: rank 7 gets a large local cut, rank 3 and rank 6 a medium cut, and rank 1 (the biggest term) gets a structural fix rather than just a narrower band, because it turns "assumed catch rate" into "measured catch rate".

---

## 6. Rights edge

- **On private ranches, option first, survey second.** A ranch heat option costs about $1-2 per acre, or about $250-500 per km² (calc). A 250 m carpet costs about $3.5-4.8k per km². So on private land, carpet only after signing. The carpet then tells us which 10-20% of optioned acres to carry and which to drop. That saves carrying cost and lets us price the carried acres as "MT-imaged", which is the data package buyers would otherwise pay $100-250k to commission.
- **On unleased BLM land, survey first and quietly.** MT and geophysics are casual use under IM 2026-024, with no notice and no filing (H13). So we image first and nominate only the best parcels, mixed with decoys. This is where the carpet earns most, because a BLM nomination or auction leaks our interest the moment we file.
- **The mast as the rancher hook.** A free RTK base, weather station and (with P01) well-health alerts give the rancher a reason to sign the heat option and allow weeks of nodes on the land. It works best on remote ranches.
- **The buyer package.** Resistivity, chargeability, Vs, basin depth and a baseline seismic catalogue on one grid, tied to temperature labels. The seismic baseline is also something a developer needs later for induced-seismicity permits (M12). This should raise the farm-out price or the override, not just cut our costs.
- **Honest limit.** This is a cost and selection edge, not a price-setting edge. The market for blind-heat rights is thin. So rights_alpha is 3.

---

## 7. Legal check (lawyer's memo, about $5-10k, bundle with the H13 memo)

1. **BLM IM 2026-024.** It lists "drone and airborne surveys" and "battery sensors placed in small holes (geophones, MT)" as casual use (H13). Ask: (a) does drone *placement* of ground sensors count as casual use; (b) is 45 m of surface wire left for 6 weeks "temporary" and minimal disturbance; (c) does a road-side IP transmitter with grounded stakes count as "ground geophysics (EM)". V01 flags that field offices can pull activities out of casual use for "significant disturbance".
2. **FAA.** 107.23(b) dropping objects; 107.31 VLOS; 107.35 one pilot, several drones; the 55 lb line and 44807; Part 108 BVLOS timing.
3. **Special areas.** Wilderness and Wilderness Study Areas ban motorised equipment and drone take-off and landing (from memory, unverified). Sage-grouse leks in spring have timing limits. Cultural sites need avoidance.
4. **Wildlife and livestock.** Thin wire on the ground for weeks may entangle birds or stock. Use bright, breakaway wire and keep a GNSS record of every leg.
5. **Lead.** Pb-PbCl2 electrodes are the standard for long-term stability, but a lost unit leaves lead on public land. Track every unit by LoRa, seal electrodes in breakaway capsules, or switch darts to Ag-AgCl on public land.
6. **State land and ranches.** Utah SITLA and other state lands have their own access permits. On ranches, a written access and data agreement signed with the heat option.

---

## 8. Prior art and why incumbents have not done it

- **MT contractors** (Quantec, Zonge, Phoenix, Enthalpion) sell crew-days on $60k+ kit. Dense cheap carpets would undercut their own pricing (H03).
- **Distributed MT + DCIP spreads** (Quantec Titan-24 / ORION 3D, DIAS32) already combine MT and IP on one array, with crews and cables on foot (from memory, unverified). We copy the idea, not the cost.
- **Low-cost telluric loggers** (LPTR, Münster EDE) prove E-only works and runs for months (H03).
- **Seismic nodes** (SmartSolo, STRYDE, Fleet Space ExoSphere) are commodity. Zanskar runs large-N passive seismic and has passive seismic permits near Cove Fort (M08, M12). No public sign that anyone runs dense MT + IP + seismic carpets from drones for geothermal (absence of evidence, unverified).
- **Drone node delivery** has been trialled for seismic nodes by oil majors and vendors (from memory, specifics unverified). Drone wire dispensing is proven by fibre-optic FPV drones (from memory, unverified).

The moat is not the node; anyone can build it in a year. The moat is the labelled resistivity-chargeability-temperature set and the rights it lets us pick.

---

## 9. Risks

1. **Recovery labour and losses.** Foot recovery dominates cost, and cattle and rodents damage wire. If losses exceed 15% or recovery exceeds 15 minutes per site, cost per km² roughly doubles.
2. **Great Basin systems without a smectite cap.** Many 130-180 C fault-hosted systems in carbonate or sediment have a thin or patchy cap (M08). Then MT sees structure and basin depth but not heat. The value then rests on rank 7 and rank 6.
3. **Lake clay false positives.** IP removes brine but not lake or playa clay. Shape and connection to depth must do the rest.
4. **Legal grey zone.** Drone placement, wire left for weeks and an IP transmitter may be ruled outside casual use by a field office (V01).
5. **Cultural noise.** Electric fences (pulsing about once a second), power lines, pipelines with cathodic protection and irrigation pumps degrade MT and IP. This matters most on the ranches where the mast lives.
6. **Short-period reference error.** With the reference 5-10 km away, AMT-band impedances over conductive valleys may be biased. v1 adds a near coil set per carpet for this reason.
7. **SP drift.** Electrode drift and temperature may swamp all but strong SP anomalies.
8. **Inversion over-reading.** 3D MT models can be over-read (Pahute Mesa, M08). Use ensembles and report uncertainty.
9. **Drone rules.** VLOS keeps the daily rate near 120-200 sites until BVLOS rules arrive.

---

## 10. Cheapest first test

**Desk, weeks 0-6, about $0-3k of compute.** In GHOST Tier 1, simulate MT + IP + HVSR on 50 synthetic blind systems with lids, brine aquifers and lake clay. Compute EIG per dollar for a 500 m carpet versus 10 Sentinel visits versus 10 darts in the same cell. Pass: the carpet beats darts per dollar in at least lidded cells, and the brine/clay split from IP lifts the cap likelihood ratio from about 2-3x to 5x or more.

**Bench and field, weeks 6-20, about $40-60k.**
1. Build 30 hubs (about $25k) and one portable coil set; borrow or rent one commercial 5-channel MT station; build or rent one IP transmitter.
2. Place by drone at a site with public MT and known temperature, for example Gabbs Valley (USGS 59-station 2020 MT, via M08) or the San Emidio fringe. Run 3-4 weeks.
3. Pass criteria:
   - Inter-site impedance within 10% in apparent resistivity and 5 degrees in phase of the commercial station (and public USGS sites) from 0.01 to 100 s at 80% or more of hubs. This is the H03 test, now with drone-placed legs.
   - Drone placement averages under 6 minutes per site, and at least 90% of hubs couple and log for 21+ days.
   - Chargeability resolves a 10 mV/V contrast within 1 km of the transmitter line.
   - HVSR depths agree with known well depths to fill within 20% where fill is under 500 m.
   - Losses under 10%.
4. Fail: worse than 20% or 10 degrees agreement, under 70% of hubs logging 21 days, or recovery over 15 minutes per site. Then fall back to hand placement with the same hub (still about 2x cheaper than contract MT) and drop the drone.

In parallel: the lawyer's memo (section 7), about $5-10k, 30 days.

---

## Sources

- Repo: `../../../hardware/evidence/H03-mt-seismic-nodes.md`, `H13-permits-and-secrecy.md`, `V01-redteam-heat-stack.md`; `M08-magnetotellurics.md`, `M09-gravity-magnetics.md`, `M12-seismology.md`, `M30-permeability.md`, `P01-ranch-well-sentinel-2-0-a-resident-well-.md`, `../MODEL.md`.
- Kruglyakov and Kuvshinov 2019, inter-site impedance: https://earth-planets-space.springeropen.com/articles/10.1186/s40623-018-0972-8 (via M08)
- LPTR low-cost telluric logger, EGU21-16275: https://meetingorganizer.copernicus.org/EGU21/EGU21-16275.html (via H03)
- Münster EDE logger: https://www.uni-muenster.de/Physik.GP/applied_geophysics/projects/ede.html (via H03)
- EGU26-7264, inter-station magnetic transfer functions: https://meetingorganizer.copernicus.org/EGU26/EGU26-7264.html (via M08)
- Hengill 498-node ambient noise, Wu et al. 2024: https://escholarship.org/content/qt5mj7r09n/qt5mj7r09n.pdf (via H03)
- Gabbs Valley MT 2020 (USGS): https://www.usgs.gov/data/magnetotelluric-data-gabbs-valley-region-nevada-2020 (via M08)
- OpenEI MT cost per station: https://en.openei.org/wiki/Magnetotellurics (via H03)
- BLM IM 2026-024: https://www.blm.gov/policy/im-2026-024 (via H13, V01)
- Zanskar passive seismic, Fishlake NF: https://www.fs.usda.gov/r04/fishlake/projects/66691 (via M08)
- From memory, not fetched this run (unverified): Petiau 2000 (Pb-PbCl2 electrodes, Pure Appl. Geophys. 157); Corwin and Hoover 1979 (SP in geothermal exploration, Geophysics 44); Revil et al. 2017-2019 and Lévy et al. 2018-2019 (IP of smectite, Krafla); Nakamura 1989 and Ibs-von Seht and Wohlenberg 1999 (HVSR); Quantec Titan-24/ORION 3D and DIAS32 (distributed MT+DCIP); 14 CFR 107.23, 107.31, 107.35; 49 USC 44807; Part 108 NPRM (2025).
