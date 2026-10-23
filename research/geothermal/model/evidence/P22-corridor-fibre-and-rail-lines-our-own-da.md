# P22: Corridor Fibre and Rail Lines (our own DAS box, rented Brillouin DTS, dark telecom strands, ploughed ranch fibre, and freight-train node lines)

Date: 23 Oct 2026. Build candidate P22, model track. This builds on `M27-fibre-das.md` (Brawley, Reno, PoroTomo, Long Valley, route owners, the "fibre scout" trailer and route-atlas ideas, DTS in wells), `M12-seismology.md` (DAS is a structure tool; every seismic "blind find" is retrospective; Vp/Vs sign depends on setting; free catalogs), `M21-shallow-temperature.md` (2 m noise floor, seasonal wave, 0.5-1.5 W/m2 detection limit, 64% blank rate), `P03` (E-MT nodes) and `../../../hardware/` (H01, H03, H11, H13, MEMO: casual use under BLM IM 2026-024). It does not repeat them. New here: (1) a concrete own-build phase-OTDR DAS bill of materials, (2) the physics and a Monte Carlo of what a **year of DTS on fibre already buried about 1 m deep** can and cannot see, (3) freight trains as a free repeating seismic source, (4) a v1 deployment plan with crew time, (5) how much each part shrinks the ranked model uncertainties, and (6) the rights edge along rail checkerboard.

**Method note.** The shared web-search budget for this run was already used up when this slice started (0 searches, 0 fetches succeeded). Everything below comes from repo files (with their URLs), from memory of the literature, and from my own calculation (`P22_dts_calc.py`, marked "calc"). Anything from memory that I could not re-check is marked (unverified). Citations from memory give authors, journal and year so they can be checked later.

## Bottom line

P22 is really three instruments that share one asset, a **route atlas plus strand-access contracts**:

1. **DAS on dark strands (the strong part).** One owned interrogator at one amplifier hut reads about 40-50 km each way, so 80-100 km per hut (unverified; an inline amplifier blocks DAS backscatter, so each hut is its own segment). Weeks of traffic and train noise give a 2D Vs section to 1-3 km (Brawley reached 3 km in two days; M27), plus a microseismic catalog several magnitude units below the regional network along the line. This is the cheapest known way to get **basin depth and buried range-front faults** across dozens of valleys. Own-build cost is about **$30-45k** in parts (BOM below) against $100-300k to buy (M12, unverified).
2. **Year-long DTS on the same buried cable (the honest-but-limited part).** My calc shows instrument noise is not the limit. With a year of 6-hourly reads, even 1-2 C single-read noise averages to 0.03-0.05 C on the mean, and the **annual-wave phase lag gives the true burial depth of every metre of cable to about 1-2 cm** (calc). The real limit is the natural scatter of mean annual ground temperature (albedo, snow, moisture, road shoulder). With 0.2-0.8 C residual after an along-line detrend, the 3-sigma detectable excess flux is **about 0.6-2.3 W/m2, or 7-28x background** (calc). That is the same class as a season-corrected 2 m probe (M21). So DTS **does not see lidded systems**. Its value is different: it is a **continuous, effort-free, unbiased transect** that crosses every valley on the route, with a known detection function. That is exactly the "designed detector with known P_det" that rank 1 needs, and it costs almost nothing extra once the strand is lit.
3. **Freight-train node lines (the cheap targeted part).** Union Pacific's Overland Route across northern Nevada carries tens of trains a day (unverified count, perhaps 30-60). Each train is a strong 1-20 Hz moving source that repeats. A 3-5 km line of 30-60 3C nodes laid at right angles to the track records train energy that has passed through the ground between track and node. Interferometry on train coda gives Vs, attenuation (Q) and, with repeats, tiny velocity changes from earth tides and barometric loading. This grades a **stepover or fault intersection** that DAS or gravity flagged. Two people, two field days, about $3-6k per line (calc from rental guesses, unverified).

The **rights edge** is real but narrower than the brief says. No land access is needed for DAS or DTS on carrier fibre. The data are private and do not have to be filed. Railroad checkerboard and ranch parcels next to a line can be optioned before anyone else sees the result. The catch is that a **lot of railroad-grant mineral estate is severed and held by a successor company**, and who holds geothermal under a reserved railroad mineral estate is a legal question to check state by state (unverified; see R06, R08).

**Scores (1-5):** model uncertainty alpha 3.5, rights alpha 3, buildability 3, cost/scale 4.5, moat 4. The main risk is **strand access**, not physics. The first test is a phone and email campaign plus one week on the public Imperial Valley data, not a hardware build.

## 1. Physics case

### 1.1 DAS on buried telecom fibre
- **What it measures.** Axial strain rate along the fibre, every 1-10 m, with a gauge length of about 5-20 m, from about 0.01 Hz to kHz (M27 F2). A buried, gel-filled loose-tube cable in conduit couples well enough for surface waves (Reno, conduit, city noise: bedrock depth matched earlier studies; M27).
- **Depth reach.** Surface-wave depth sensitivity is about one third to one half of the wavelength. For 3 km depth at Vs 2.5 km/s, you need about 0.3-0.4 Hz. Road traffic is mostly above 2 Hz. Trains add strong energy down to below 1 Hz plus quasi-static loading. Brawley reached 3 km with overtones and spatial stacking (Rodríguez Tribaldos et al.; Cheng et al. 2023, JGR, doi 10.1029/2022JB025240). In quiet rural Nevada, plan on **2-6 weeks** per segment for stable long-period dispersion (unverified, extrapolated from M27).
- **What it sees that matters for blind upflow.**
  - **Basin depth** (sediment Vs 0.3-1.5 km/s versus bedrock 2.5-3.5 km/s). This sets the conductive part of T at 1-3 km, because low-conductivity basin fill acts as a thermal blanket. It is rank 7 and feeds rank 5.
  - **Buried range-front fault position and throw, stepovers and damage zones.** A damage zone shows as a narrow slow strip and as scattered or converted waves at a lateral jump (Atterholt et al. 2022, GJI, Long Valley, "fault zone imaging with DAS", unverified detail). This is rank 6 (where upflow is) and part of rank 2 (permeability).
  - **Microseismicity.** DAS with thousands of channels detects events well below the network Mc within a few km of the line (Lindsey et al. 2017 GRL; Ajo-Franklin et al. 2019 Sci. Rep., Sacramento 27 km dark fibre, unverified detail). Nevada network Mc in the gaps is about 1.5-2.5 (M12). A DAS line may reach Mc about 0 near the line (unverified). Active small faults are a direct permeability signal (M12 F4).
  - **Sealed caps.** Brawley's blind field showed as **fast, low Vp/Vs**. The model must keep the sign of a velocity anomaly setting-dependent (M12, M27).
- **What it cannot see.** Temperature at depth. Anything more than a few km off the line. Broadside waves (single component).

### 1.2 Year-long DTS at about 1 m (calc in `P22_dts_calc.py`)
- **Instrument.** Telecom fibre is single-mode, so the tool is Brillouin (BOTDR single-ended, or BOTDA if a loop-back strand exists). Typical spec is about 1 m sampling, 1-2 m resolution, 25-50 km range, about 0.5-2 C per read at long range (unverified vendor class). Brillouin also senses strain, but a loose-tube cable is almost strain-free over a year.
- **Burial depth.** Long-haul fibre is normally ploughed or trenched at about 0.9-1.2 m (unverified typical spec). The depth varies along the route and is not mapped. **The annual wave fixes this.** With damping depth d about 2.2 m (calc, diffusivity 0.5e-6 m2/s), the wave at 1 m has about 7.7 C amplitude (for 12 C at the surface) and a phase lag of z/d radians. A one-harmonic fit to a year of reads gives z to 0.5-2 cm (calc, white noise; real drift will be worse, perhaps 5-10 cm, unverified). So every metre is self-calibrated for depth and diffusivity. No other cheap shallow tool gets this.
- **Signal.** A steady excess flux dq gives a 1 m mean-annual offset of about dq*z/k + dq/h, about **1.07 C per W/m2** at z = 1 m, k = 1 W/m/K, h = 15 W/m2/K (calc). Normal flux (0.08 W/m2) gives 0.08 C, which is invisible. Only anomalies count.
- **Noise.** Year-mean read noise is 0.01-0.05 C (calc). The real noise is the mean-annual ground-surface temperature: road shoulder, albedo, snow, irrigation, vegetation and soil moisture. After removing a 1-2 km along-line running background and a Landsat-albedo term, I assume 0.2-0.8 C residual (unverified; M21 found 2.4 C raw between areas and 1.2 C within an area for one-shot 2 m reads, and a year of data plus depth correction should beat that).
- **Detection limit.** 3-sigma excess of 0.6-2.4 C, so **dq about 0.56-2.25 W/m2, or 7-28x background** (calc). This is the "leaky" class: about the same as a well-processed 2 m survey. It will miss Granite Springs- and Argenta-type lidded systems (M21). **It is a footprint and occupancy tool for leaky systems, not a lid-penetrating tool.**
- **Bonus channels.** (a) Warm groundwater crossing under the cable shows as a step, not a smooth bump. (b) A heated-cable test is not possible on telecom fibre, but on our own ploughed hybrid cable (copper plus fibre) it gives conductivity every metre (M27 F4). (c) Snow-melt timing on the surface (from Sentinel-2) cross-checks hot strips.

### 1.3 Freight trains as a source
- **Prior art.** Brenguier et al. 2019 (GRL, "Train traffic as a powerful noise source for monitoring active faults with seismic interferometry") showed trains give strong, repeatable correlations for fault monitoring. Pinzon-Rincon et al. 2021 (SRL, "Humming trains in seismology") showed train "hum" from regular car spacing is a narrow-band source down to the upper crust. Dou et al. 2017 (Sci. Rep.) used traffic and DAS for near-surface Vs. All from memory (unverified details).
- **Why it helps.** Ambient noise in rural Nevada is weak and one-sided. A train is a known, moving, repeating line source. A node line at right angles to the track sees the same source path many times a day, so you can stack per-train and average out the rest. It gives Vs and Q to a few hundred metres to perhaps 1-2 km (unverified depth). Repeat trains over weeks also allow dv/v tracking against earth tides and barometric load, a weak handle on **fracture compliance**, which is permeability (rank 2, unverified as a field method here).
- **Limits.** Depth beyond about 1-2 km is doubtful. Rail lines run where the ground is flat and often follow valley axes, not across range fronts, so pick crossings with care.

## 2. Prior art and who does it now
- **Geothermal DAS on telecom fibre:** Brawley/Imperial Valley (LBNL, Zayo, DOE GTO, data public), Reno (UNR, 12 km), Reykjanes (Jousset et al. 2018, Nat. Commun., unverified detail), Long Valley on US-395 (Caltech; Biondi et al. 2023, Sci. Adv., "upper-crust lid", unverified detail), PoroTomo Brady (trenched). All retrospective (M12, M27).
- **Commercial DAS vendors:** Silixa (iDAS, Carina), Luna/OptaSense, Febus, AP Sensing, Sintela, ASN, Treble/Fotech (unverified as current list). Rail and pipeline DAS for intrusion and train tracking is routine. **Nobody uses corridor fibre as an exploration product for geothermal leasing.** Zanskar has a DAS-processing intern role (M12) and an LBNL large-N CRADA; no public corridor programme.
- **Rail ROW fibre:** much western long-haul fibre was laid in railroad rights-of-way. Sprint's original network was built on Southern Pacific ROW (the name is often said to come from "Southern Pacific Railroad Internal Network Telecommunications", unverified). The UP Overland Route through Nevada carries several carriers' cables (unverified).
- **Home-built DAS:** many university labs build phase-OTDR systems from a narrow-linewidth laser, an acousto-optic modulator, an EDFA and a fast digitizer; it is a standard thesis project (unverified as to any specific open-source design). Performance is a few dB worse than top commercial units, but good enough for 1-20 Hz surface waves over 20-40 km (unverified).

## 3. v1 design

### 3.1 DAS box "Corridor-1" (own build)
| Part | Spec | Cost (unverified) |
|---|---|---|
| Narrow-linewidth laser | 1550 nm, <1-5 kHz linewidth, low drift (fibre laser or RIO-type) | $6-15k |
| Pulse modulator | AOM, 80-200 MHz, 20-100 ns pulses, high extinction | $2-4k |
| Booster EDFA + pre-amp EDFA | 20-23 dBm out; low-noise pre-amp; ASE filter | $4-7k |
| Receiver | Coherent (IQ, 90-degree hybrid + 2 balanced detectors) or 3x3 coupler phase demod | $3-6k |
| Digitizer | 2 ch, 14-bit, 250-500 MS/s, PCIe streaming | $5-9k |
| Compute | GPU PC, 2x 20 TB disks, GPS-PPS timing | $4-6k |
| Optics, circulators, couplers, APC jumpers, OTDR/fusion-splice access, 19-inch ruggedized case | | $2-4k |
| Power and comms | 48 V DC from hut (or 400 W solar + 5 kWh LiFePO4 if outside), Starlink / LTE | $1-3k |
| **Total** | | **about $27-54k, planning number $40k** |
- **Power:** about 150-300 W. **Data:** raw 1-5 TB/day per 50 km at 1-2 kHz. Edge code keeps (a) 1-50 Hz decimated strain for 30-second windows around triggers, (b) hourly noise cross-correlations (GB per week), (c) a continuous 50 Hz event stream. Upload via Starlink, raw kept on disk for 30 days.
- **Software:** phase unwrap and gauge-length differencing, then standard DAS interferometry (DASPy-type or our own; unverified tool names), and surface-wave inversion seeded with gravity basin depth.
- **Calibration:** run it side by side with a rented commercial unit on the same strand for one week, and on the public Imperial Valley record for software checks.

### 3.2 DTS
- **Rent, do not build,** for v1. A Brillouin BOTDR on a single dark strand, about $3-10k/month (unverified). For a year, buying a used unit ($60-150k, unverified) may be cheaper. One unit can share the hut with the DAS box through a WDM or on a second strand.
- Reads every 6 hours. Store per-metre temperature. Fit mean, annual and semi-annual harmonics, phase lag (depth) and a slow drift term.

### 3.3 Our own ploughed fibre on optioned ranches
- **Cable:** direct-bury armoured hybrid (12-24 single-mode + 2 multimode + copper pair), about $1.5-3/m (unverified).
- **Laying:** vibratory cable plough behind a rented tractor or skid-steer, 1.0 m depth, 2-5 km/day on ranch roads (unverified). Cost about **$3-6k/km** including cable (unverified).
- **Use:** on our own optioned land across a top target. Multimode strands give Raman DTS (better temperature, about 0.1 C), the copper pair allows heated-cable conductivity tests, and single-mode gives DAS. Permanent, owned, no carrier needed. **Only on private land with the landowner's written consent tied to the heat option.** Ploughing on BLM is not casual use.
- **Design rule:** lay it **across** the range front and down the plume path (rank 6), 3-8 km long.

### 3.4 Train node lines
- 30-60 3C nodes (SmartSolo IGU-16HR 3C or similar; rent about $10-25/node/day or buy about $1.5-3k each, unverified), at 50-100 m spacing on a 3-5 km line at right angles to the track, starting 50 m from the ROW fence.
- Record 5-10 days (100+ trains). GPS-timed, self-contained, no cables.
- Place on optioned private land, or on BLM as casual use (battery sensors in small holes under 10 ft; confirm geophones are covered in the IM 2026-024 lawyer's note, H13/MEMO).
- Pair with the E-MT nodes (P03) on the same line: same crew, same day.

### 3.5 Deployment and crew time
| Task | Crew | Time | Notes |
|---|---|---|---|
| Route atlas and carrier outreach | 1 BD person | 4-8 weeks to first strand | NTIA/BEAD filings, NDOT/UDOT fibre plans, UNR NSL/LBNL partners, carrier NDAs |
| Hut install (DAS + DTS) | 1 tech | 1 day per hut, then remote | Carrier escort; OTDR check; 48 V tap |
| Hut service | 1 tech | half day per month | Disk swap, health check |
| Node train line | 2 people | 1 day lay + 1 day pickup | Plus 0.5 day QC |
| Ploughed ranch fibre, 5 km | 2-3 people | 2-3 days | Plus splice and end boxes |

### 3.6 v1 scope (12 months)
- **3-4 huts**, about 300 km of dark strand on I-80 (Lovelock-Winnemucca-Battle Mountain, crossing Humboldt, Buena Vista, Grass, Reese River and Crescent valleys), US-95 (Fallon-Hawthorne-Tonopah, Walker Lane) and US-50 (Fallon-Austin, Dixie and Edwards Creek edges). Route choices unverified until the atlas is built.
- DAS 4-6 weeks per hut, then the box moves. DTS stays 12 months.
- **8-12 train node lines** on the UP Overland Route where it crosses mapped stepovers.
- **2 ploughed ranch lines** (5 km each) on the best optioned targets.
- **Budget:** DAS box $40k; DTS rent/buy $60-120k; strand access $0.5-5k per km-year, so $150k-1.5M for 300 km (very uncertain; research-partner access may be near free, M27); nodes $40k; ploughing $50k; staff separate. **Planning total $0.35-0.8M for year one**, or about **$1-3k per km-year** if research-partner access works and $5k per km-year if strands must be leased (unverified).

## 4. How much it shrinks the model's ranked uncertainties

Coverage check first. 300 km of line, with structure resolved about ±1.5 km, covers about 900 km2, under 0.2% of the Great Basin. That is "too small" if used only as a local map. It is **not** too small as a **calibration and design instrument**, which is how it enters SENTINEL-COX:

| Rank | How P22 enters | Rough shrink (unverified, my estimate) |
|---|---|---|
| 1 Detection gap / occupancy | DTS is a second detector with a **known detection function** (dq > 0.6-2 W/m2, depth-calibrated) laid along a line that was not chosen for geothermal promise. Every crossed cell gets an effort-free leaky/not-leaky reading. Combined with Sentinels in the same cells, it gives the designed two-detector survey CREAM-COX wants and pins the leaky-class fraction of the latent mask. | 10-25% cut in the log-variance of N for the leaky class; little on deep lidded catch rate. Stops the 2-5x being one free parameter. |
| 7 Conductive background and position | DAS basin depth on 30-60 valley crossings, used to **calibrate the gravity-to-basin-depth inversion** for every valley in the region (density contrast and depth model per setting). DTS gives soil diffusivity every metre. | Basin depth error in crossed valleys from about ±40-50% to ±10-15%; regional gravity calibration perhaps ±40% to ±25%. Cuts conductive T at 2 km error by about a third in calibrated valleys. |
| 6 Upflow location / footprint | DAS fault positions and damage zones; DTS footprint width where leaky; ploughed ranch fibre down the plume path; train lines on stepovers. | Large locally (fault position from ±500-1,000 m to ±100-200 m on crossings), small regionally. |
| 2 Permeability class | Microseismicity on the line (active faults), damage-zone width, train Q and dv/v. All are permeability likelihoods, not flow numbers. | Modest: perhaps a 1.3-2x likelihood ratio on "Limited Distributed or better" at crossed structures. The 10x MWe spread mostly stays for wells and pressure loggers. |
| 3 Lid thickness | DTS does not see through lids. DAS basin depth bounds the lid from above. | Small. |
| 4 Sensor reliability | Line passes over known systems (Brady, Desert Peak, Beowawe on I-80, unverified). These are free calibration crossings for the DTS detection function. | Useful: adds known-positive and known-negative calibration at near-zero cost. |

**EVSI view.** The best $ per bit is the DAS on research-partner strands: a valley line for about $10-30k (M27) against $50-200k for a nodal carpet. DTS adds rank 1 information for the cost of the rental. The Tier 1 GHOST sim should confirm that DTS EVSI per dollar beats an equal spend on Sentinel visits; my guess is it does only where Sentinels have no wells to visit (empty valleys).

## 5. Rights edge
- **No land access, no permit, no filing.** Carrier fibre sits in carrier or DOT ROW. Our data are private. BLM never sees it. Under IM 2026-024, node lines are casual use on open BLM land (to confirm).
- **Option first, then light.** Because the route is fixed and public-ish, we can option ranch and checkerboard parcels in a 3-5 km band along the line **before** turning it on, at ranch heat-option prices (~$1-2/ac, B/R files). Along I-80 the UP land-grant checkerboard means every other section is private, so a corridor touches many private parcels.
- **Caveat on the checkerboard.** Railroad-grant lands were often sold with minerals reserved to the railroad's land company and its successors (unverified current holder). Whether "minerals" includes geothermal is state law and deed wording (R06, R08). Each parcel needs a title check before the option counts.
- **Leftover BLM noncompetitive.** A DAS fault or DTS anomaly next to unleased BLM land can be nominated or picked up at $1/ac/yr where noncompetitive rules allow (R02). The data are not shown to anyone.
- **Leak risk.** Carrier staff and research partners will know a strand was used. A research partner may want to publish. Contracts must give us a 2-3 year embargo and keep coordinates confidential.

## 6. Risks
1. **Strand access.** Carriers may refuse, charge long-haul IRU prices, or offer only aerial or lit routes. This decides the whole project.
2. **Rural noise is weak.** Depth reach to 3 km may need many weeks, or fail away from rail.
3. **DTS background scatter.** If mean-annual ground temperature residual is above 0.8 C (road shoulder, irrigation), DTS only sees systems already found by 2 m surveys.
4. **Home-built DAS performance.** Laser phase noise and fading may cost range. Fallback: rent a commercial unit.
5. **Data volume and processing talent.** TB/day and a DAS seismologist are needed. Zanskar is hiring the same people.
6. **Route geometry.** Highways and rail follow valley axes in places, not across range fronts.
7. **Checkerboard title.** Severed railroad minerals may hold the geothermal right.
8. **Retrospective-only evidence.** No DAS line has yet found an undrilled field (M12).

## 7. First test (weeks 0-8, about $10-20k)
1. **Desk, weeks 0-4.** Build the route atlas v0 for NV: NTIA/BEAD middle-mile filings, NDOT fibre plans, rail ROW, carrier maps under NDA. Score each segment for burial, darkness, hut access and valley crossings, and overlay CREAM-COX lambda and P_det. Email UNR NSL, LBNL and two carriers for a 1-hut research strand.
2. **Desk, weeks 2-6.** Run our pipeline on the public Imperial Valley DAS data and reproduce the Brawley Vs section. Run `P22_dts_calc.py` on real hourly air temperature and a synthetic Brady-type flux map to get the GHOST Tier 1 EVSI for DTS.
3. **Field, weeks 6-8.** One train node line (30 nodes, 3 km) across the UP Overland Route near a known system crossing (for example near Brady/Desert Peak or Beowawe, unverified track geometry). Pass if train correlations give a stable Vs profile to 500 m+ in under 5 days and resolve the known fault.
4. **Go/no-go:** one strand signed at under $5k per km-year (or free as a research partner), Brawley reproduced, and the train line passes. Then order the DAS parts.

## Sources
- Repo: `M27-fibre-das.md` (Brawley https://escholarship.org/uc/item/1gg2w5qf ; Reno https://par.nsf.gov/biblio/10502387 ; LBNL dark fibre https://energygeosciences.lbl.gov/2020/12/16/field-access-allows-first-ever-geothermal-basin-characterization-using-dark-fiber/ ; ThinkGeoEnergy https://www.thinkgeoenergy.com/research-explores-the-use-of-telecom-fiber-for-geothermal-seismic-sensing/), `M12-seismology.md` (San Emidio PSET https://gdr.openei.org/files/1386/WarrenFinalReport.pdf ; Zanskar roles), `M21-shallow-temperature.md` (2 m statistics, GDR 1391), `P03`, `../../../hardware/MEMO.md` (IM 2026-024).
- From memory, not re-checked this run (unverified): Brenguier et al. 2019 GRL (train traffic interferometry); Pinzon-Rincon et al. 2021 SRL (humming trains); Dou et al. 2017 Sci. Rep. (traffic DAS); Ajo-Franklin et al. 2019 Sci. Rep. (Sacramento dark fibre); Lindsey et al. 2017 GRL; Atterholt et al. 2022 GJI; Biondi et al. 2023 Sci. Adv.; Jousset et al. 2018 Nat. Commun.
- Own calculation: `P22_dts_calc.py` (this folder).
