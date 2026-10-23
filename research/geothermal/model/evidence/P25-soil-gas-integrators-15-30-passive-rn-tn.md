# P25: Soil-Gas Integrators (passive Rn/Tn + Hg + He + CO2 cups in every probe hole, plus buried breathing-fault nodes)

Date: 23 Oct 2026. Build candidate P25, model track. This builds on `M22` (gas tracers: He best, soil CO2/Hg/Rn/H2 weak over blind systems, "one-shot surveys over blind systems are close to noise"), `../../../hardware/evidence/H04` (soil-gas truck, miniRUEDI, Kumiva and Dixie Valley CO2), `H09` (H2/He seeps), `H13` (casual use under BLM IM 2026-024), `P01` (Ranch Well Sentinel, which already carries the dissolved He/Ne diffusion sampler in water), `P02` (3 m dart with a gas port at 2.8 m) and `MODEL.md` (SENTINEL-COX ranks). It does not repeat them. What is new here: (1) the *integrating* passive cup design and why integration fixes the noise M22 complained about, (2) the Rn/Tn twin-cup and soda-lime delta-13C tricks, (3) a concrete node BOM, (4) how the gas channel enters CREAM-COX as a second detector, (5) a toy noise calculation (`P25_calc.py`, this folder).

**Method note.** The shared web-search budget was already used up when this slice ran. No new searches or fetches worked. Sources below are the ones already read in M22 and H04 (with URLs), plus papers I know from memory, which are marked (from memory, unverified). Part prices are from memory and marked (unverified). Toy-model outputs are marked (calc).

---

## Bottom line

- **The idea is sound and cheap, but it is a segment selector and a mask classifier, not a heat finder.** A passive cup left 2-6 weeks at the bottom of a 2 m probe or 3 m dart hole averages out the barometric and moisture swings that make one-shot soil gas noisy. In my toy model, a 4-week integrating cup plus thoron normalisation raises the detection rate of a 2x radon anomaly from **0.38 (one-shot grab) to about 0.59**, and a 3x anomaly from **0.55 to about 0.85**, at a 10% false-alarm rate (calc, `P25_calc.py`). Spatial soil noise is what is left, and thoron removes part of it.
- **What it adds that nothing else in the stack adds.** It reads *gas transport*, which is a different physical channel from heat. So its misses are only partly tied to the thermal detectors' misses. That partial independence is what CREAM-COX needs to estimate the detection gap (rank 1) from a designed two-detector survey instead of from priors.
- **Signature table (the useful part).**
  - He-high + Rn/Tn-high + heavy delta-13C CO2 = **open, deep-rooted fault segment** (drill target, upflow side).
  - Hg-high + He-low + low CO2 = **sealed clay cap** over a hot reservoir (Long Valley pattern, Hinkle and Kilburn 1980). This is the "lidded" mask class the model fears most.
  - Everything flat + warm dart = **conductive lid or swept outflow** (hand off to P01 Sentinel and E-MT).
  - Rn-high + Tn-high, no He, light CO2 = **local soil uranium or biology** (false positive, flagged by the ratios).
- **Cost.** About **$45-75 per cup station including lab work in v1, falling to $20-35 with our own He/Ne quad and Hg analyser** (unverified). At one cup per 200-250 m that is **about $0.9-1.9k per km2** in v1, inside the brief's $1-3k. Adding a cup to a dart or probe hole we already drilled costs **about 5 minutes on install and 5 on pickup**. A breathing-fault node is **about $520-780** (unverified BOM below), deployed 20-50 per target.
- **Model effect (estimate).** Strongest on **rank 6 (upflow location)**: picks which 0.2-1 km fault segment leaks, about a 30-50% cut in the location/footprint spread at targets where the gas signal exists. Moderate on **rank 3 (mask class)**: the Hg/He pattern gives a direct "sealed cap" label, worth about a 15-30% cut in mask-class entropy at surveyed cells. Small-moderate on **rank 1 (detection gap)**: as a partly independent second detector it narrows the deep or lidded catch-rate band by roughly 10-25% (from 2-5x to about 1.8-4x on N), only if the calibration campaign shows the two detectors' misses are not strongly tied. Small on **rank 2 (permeability)**: node barometric lags measure shallow air permeability of the fault zone, a weak proxy for deep flow; maybe a 5-15% cut. All of these are estimates (unverified, untested).
- **Rights edge.** Pure casual use. Cups are smaller than the probe already in the hole, nothing is filed, and the cup leaves with us. It shrinks the number of 500 m parcels we must lock per target (better segment pick) and so the decoy budget. It does not create a new lockable area by itself.
- **Self-score:** model uncertainty alpha 3, rights alpha 3, buildability 5, cost/scale 4, moat 2. **Total 17/25.** Build it as an add-on to P02 darts and P01 Sentinel visits, not as a stand-alone program.

---

## 1. Physics case

### 1.1 Why one-shot soil gas fails and integration helps

Soil gas at 0.5-3 m is a mix of three things: gas made in the soil (root and microbe CO2, radon from local uranium), air pulled down by barometric pumping and wind, and a small deep flux pushed up along cracks. The deep part is what we want. M22 and H04 say it is weak over capped Great Basin systems (Kumiva "weak" and "suggestive"; Dixie Valley anomalies only near fumaroles).

Two of the noise sources change on time scales of hours to days:
- **Barometric pumping.** Weather fronts move pressure by 1-3% over 2-5 days. Falling pressure pulls deep gas up; rising pressure pushes air down. Radon and CO2 at 1 m can change 2-5x through one front (general knowledge from radon monitoring, unverified magnitude). A grab sample catches one random moment.
- **Moisture.** Rain closes soil pores. Gas builds up under a wet crust and then vents. Radon in soil gas often doubles after rain (unverified).

A cup that integrates over 4-6 weeks averages 8-15 weather cycles. If the swings are random over cycles, the noise drops roughly with the square root of the number of cycles. That is the core benefit. The part that does **not** average out is spatial: soil type, uranium content and permeability differ from hole to hole. Thoron fixes some of that (1.3).

**Toy model** (`P25_calc.py`): temporal noise log-normal with sigma_ln 0.6 and 3-day memory, spatial noise sigma_ln 0.5, thoron sharing 70% of the spatial term. Detection rate at a 10% false-alarm threshold:

| Anomaly | Grab | 28-day cup | Grab, Tn-normalised | Cup, Tn-normalised |
|---|---|---|---|---|
| 1.5x | 0.23 | 0.30 | 0.24 | 0.34 |
| 2.0x | 0.38 | 0.49 | 0.38 | 0.59 |
| 3.0x | 0.55 | 0.74 | 0.61 | 0.85 |

(calc; the inputs are assumed, not measured). Plain reading: integration plus thoron turns a "coin-flip" radon survey into a usable one for anomalies of 2x or more. It does not rescue anomalies under 1.5x. Note the toy model's grab survey shares one weather moment across all sites. Real grab surveys spread over days are worse.

### 1.2 What each channel sees, and its depth reach

| Channel | Passive format | What it marks | Reach and limit |
|---|---|---|---|
| **Rn-222** (3.8 d half-life) | CR-39 alpha-track film in a cup | Gas *moving* up an open crack; needs a carrier (CO2, steam, water vapour) to come from more than a few metres | Only metres by diffusion. A high reading means advection along a crack. Radon itself is local; it rides the carrier. (M22 finding 11) |
| **Rn-220, thoron** (55 s) | Second CR-39 film without the diffusion delay (twin-cup) | Local soil source and permeability, centimetres | Used as the denominator. High Rn/Tn = gas pushed from depth. |
| **Hg vapour** | Sulfur-impregnated activated carbon (SIAC) or gold-coated sorbent, behind a diffusion barrier | Hg boiled from a hot reservoir (>about 200 C) and condensed in a cool cap and soil above upflow (M22 finding 9) | Long-lived signal; records tens to thousands of years of venting, not just today. Mining noise is the big trap. |
| **He / Ne** | Copper tube with a gas-permeable membrane end; crimped shut on pickup | Deep crustal or mantle gas on an open fault. He does not react or adsorb. Ne corrects for air. | Air has 5.24 ppm He. Anomalies of +50 to +20,000 ppb were seen at Long Valley (M22 finding 6), so we need about 0.5-1% precision. An equilibrium tube only remembers the last few days unless the membrane is slowed (see 3.1). |
| **CO2 and delta-13C** (new add) | Soda-lime trap in the cup; weigh for flux, run the trapped carbonate for delta-13C | Total CO2 flux, and deep (about -3 to -6 per mil) versus plant (about -20 to -27 per mil) carbon (M22 finding 8) | Static-alkali traps are an old soil-respiration method (from memory). The delta-13C on the trap is the cheap integrated version of what Kumiva needed 14C for. Top cups get 14C. |

Depth of sensitivity: none of these "see" a reservoir at 1-2 km directly. They see whether a **path** from depth exists at this fault segment. He and Hg can originate at reservoir depth; Rn and CO2 tell us whether gas is moving up the path today.

### 1.3 Rn/Tn twin-cup

Two CR-39 chips sit in the cup. One is behind a thin diffusion barrier (a long narrow path or a membrane) that delays gas by a few minutes. Thoron (55 s) decays in the barrier; radon (3.8 d) passes. The other chip is open and sees both. Thoron = open minus delayed. This is the RADUET-type passive Rn/Tn discriminating detector design from Japan (Tokonami and co-workers, mid-2000s; from memory, unverified). Rn/Tn > local background marks gas brought from below the local soil. Thoron also tracks local soil permeability, so dividing by it removes part of the spatial noise in 1.1.

### 1.4 Breathing-fault nodes: what the time series adds

A node at 1.5 m on a candidate fault segment logs CO2, O2, H2, Rn, soil-gas pressure versus air pressure, temperature and moisture every 30 minutes for 4-12 weeks. Three tests use the series:

1. **Romanak process ratios.** Romanak and co-workers (2012, GRL, "process-based approach" to vadose-zone CO2 leak detection; from memory, unverified details) showed that plotting O2 against CO2, and CO2 against N2, separates plant respiration (CO2 gained = O2 lost, roughly 1:1), carbonate dissolution, and CO2 added from outside the soil (which dilutes N2 and O2 together). The node measures CO2 and O2; N2 is taken by difference with an Ar correction from occasional lab grabs. Points that fall off the respiration line are deep-sourced CO2, *without* needing a baseline year. That method was built for CO2 storage sites, where the same "is this deep or biological" question applies.
2. **Barometric response.** On a dead soil, gas concentration at 1.5 m follows the air pressure with a short lag and small swing. On an open fault connected to a deep gas reservoir, concentrations of CO2, Rn and He surge during pressure lows, and the soil-gas pressure lags air pressure more because the gas column is longer (barometric pumping theory, e.g., Nilson and co-workers 1991 JGR; Massmann and Farrier 1992 WRR; from memory, unverified). The lag and amplitude ratio also give the air permeability of the fault zone, which is a weak hint for rank 2.
3. **H2 bursts.** H2 events that line up with Rn and CO2 surges mark a live deep-rooted fault. Single H2 values are not trusted (microbes, steel; M22 finding 12).

### 1.5 Detection limits (honest)

- **Blind, capped systems give weak gas signals.** The literature in M22 and H04 is clear on this. The cups do not change the source strength. They lower the noise floor. Expect the cups to light up on maybe 30-50% of blind systems that have an open fault reaching within a few hundred metres of the surface, and on few that are fully sealed (unverified guess). For the sealed ones, the Hg-high/He-low pattern is the hope, and it is untested outside Long Valley.
- **Swept outflow (Argenta type)** carries heat sideways in a cold aquifer. Gas from below may be dissolved and carried away too. The cups mostly miss these; P01 Sentinel profiles and dissolved He in ranch wells are the right tool.
- **Mining districts.** Old Hg and Au workings poison the Hg channel over large parts of Nevada. Mask Hg within a few km of mapped mines and mill sites (NBMG mine database) and use He and Rn/Tn there.

---

## 2. Prior art

- **Uranium exploration did exactly this in the 1970s-80s.** Terradex "Track Etch" alpha-track cups were buried upside-down in shallow holes for about 3-4 weeks to integrate radon, and helium and radon soil surveys were run over buried deposits (from memory, unverified details). USGS also ran a vehicle-mounted He detector and a portable He sniffer for uranium (H04: https://pubs.usgs.gov/publication/70012488 ; https://pubs.usgs.gov/publication/70042909 ).
- **Geothermal soil He and Hg.** Hinkle and Kilburn 1980, Long Valley, USGS OFR 80-612: 551 soil samples, He +830 to +20,000 ppb, about plus or minus 30% reproducibility, He high on the Hilton Creek fault and low over altered ground where Hg was high (https://pubs.usgs.gov/of/1980/0612/report.pdf). Hinkle, Roosevelt Hot Springs soil He and Hg (https://digitalcommons.usu.edu/govdocs/47/). Matlick and Buseck 1975 on Hg at Long Valley; Varekamp and Buseck on soil Hg as a geothermal method (Geothermics, early 1980s; from memory). OpenEI method page: https://openei.org/wiki/Geothermal_Exploration_Using_Surface_Mercury_Geochemistry .
- **Soil CO2 over geothermal fields.** Dixie Valley (Bergfeld et al. 2001, https://pubs.usgs.gov/publication/70023687), Los Humeros 2,823-point grid (Jentsch et al. 2020, https://arxiv.org/pdf/2002.11515), Kumiva blind target with MT and soil gas (DOE/U of Utah, https://www.energy.gov/sites/prod/files/2015/06/f23/9-Magnetotellurics_Soil%20Gas%20Geochemistry_U%20of%20U.pdf), biological CO2 noise (Lewicki and Oldenburg, https://www.osti.gov/biblio/840238).
- **Passive samplers in industry.** Commercial passive soil-gas modules (W.L. Gore / Amplified Geochemical Imaging) are buried about 2-3 weeks for hydrocarbon and Hg exploration and for environmental sites (from memory, unverified that they have been used for geothermal). Passive Hg air samplers with SIAC sorbent exist for air monitoring (McLagan, Wania and co-workers, "MerPAS", mid-2010s; from memory). Noble-gas passive diffusion samplers for water (Gardner and Solomon 2009, Water Resources Research; from memory) are what P01 already uses in wells; P25 puts the same copper-tube idea in soil gas.
- **Fault radon and CO2 monitoring.** Continuous radon and CO2 stations on active faults are common in earthquake and volcano monitoring (Italy, Taiwan, Iceland; general knowledge, unverified specifics). Etiope and Martinelli 2002 reviewed carrier-gas transport of trace gases along faults (Physics of the Earth and Planetary Interiors; from memory).
- **Romanak** process-based CO2 method at storage sites (GRL 2012, Gulf Coast Carbon Center, U Texas BEG; from memory).
- **What is new in P25.** (a) Stacking four passive channels in one cup in the *same hole as a heat-flux dart*, so every gas point has a temperature and flux beside it; (b) using the ratios (Rn/Tn, Hg/He, delta-13C) as mask-class labels in a Bayesian occupancy model; (c) running it at carpet density on unleased land before any filing. I know of no published geothermal survey that did (a) to (c) together (unverified).

---

## 3. Concrete v1 design

### 3.1 Cup station ("the integrator")

**Form.** A 32 mm OD x 220 mm polypropylene canister with a screw cap, an open mesh bottom over a 20 mm sand plug, and a 1.5 m nylon pull cord with a tag. It drops to the bottom of a 2 m probe hole, a 3 m P02 dart hole beside the dart tube, or a stand-alone 1 m slide-hammer hole. A foam plug and 10 cm of bentonite chips seal the hole above the cup, so it samples soil gas, not air. In a P02 dart, the cup can sit in a 25 mm side hole 30 cm away, or be hung on the gas port line (inference).

**Contents, top to bottom** (prices are v1 per station including lab work; unverified):

| Item | Part | Hardware $ | Lab $ | Note |
|---|---|---|---|---|
| Rn/Tn twin chips | 2 x CR-39 chips, one behind a 5-10 mm delay path or membrane, one open | 3-6 | 10-20 (etch and count, commercial lab; or in-house etch bath + microscope camera later at about $2) | Exposure 2-6 weeks. Keep below about 90% humidity with a desiccant collar (CR-39 is moisture tolerant, but condensation on the chip is not). |
| Hg sorbent | 0.5 g SIAC or gold-coated sand in a PTFE-membrane sachet | 2-4 | 15-25 (thermal decomposition AA, Milestone DMA-80 class) | Diffusion-limited uptake, so mass/time = mean vapour. Field blank in every batch. |
| He/Ne tube | 6 mm copper tube, 15 cm, one end with a silicone or PTFE membrane | 6-10 | 30-60 (lab quadrupole He, Ne) | Crimp both ends on pickup with a cold-weld crimper. Membrane thickness picked so the equilibrium time is about 1/3 of the deployment (inference); otherwise it only remembers the last days. |
| CO2 trap | 5 g soda lime in a mesh bag, sealed until deployment | 1-2 | 10-20 (weigh; delta-13C on trapped carbonate by IRMS) | Integrated flux and source carbon. 14C only on the top 5% ($300-500; unverified). |
| Logger (1 in 5 stations) | iButton-class temperature + humidity button | 15-25 | 0 | Tells us if the cup flooded or cooked. |
| Canister, cord, tag, seal | | 4-6 | | |
| **Total per station** | | **about $16-30 hardware** | **about $65-125 lab in v1** | v1 total about **$45-75 if we run He/Ne and Hg in-house** (see 3.4) or $80-150 with outside labs |

The brief's "$15-30 cup" matches the **hardware**. The real per-station cost is driven by lab work, so the business case needs the in-house analysis line (3.4).

**Deployment.** 2-6 weeks, default 4. Install with the probe or dart: +5 minutes (drop, seal, GPS, photo). Pickup: +5 minutes per station plus driving, unless it rides on a dart service visit. Stand-alone 1 m hole with a slide hammer: about 15-20 minutes. Duplicate cups at 5% of stations and travel blanks in every batch. Density: one per probe or dart site (200-500 m), denser (50-100 m) across candidate range-front segments.

**Crew time per km2** at 250 m spacing (16 stations): about 2-3 crew-hours extra if riding on darts, about 6-8 crew-hours stand-alone (calc from the per-station times above).

### 3.2 Breathing-fault node

**Form.** A 1.6 m slotted PVC probe (25 mm) in a hand-augered 75 mm hole, sand pack at 1.2-1.6 m, bentonite seal above, a 150 mm buried PVC vault at 0.3 m for electronics, a small solar panel on a low stake (or battery only), and a flush cap. A micro-pump pulls about 100 mL from the probe every 30 minutes through the sensor cell and returns it (closed loop, so we do not pump down the soil).

| Item | Part (example) | $ (unverified) |
|---|---|---|
| CO2 0-20% NDIR | Senseair K33/K30 extended range or GSS SprintIR-6S | 90-180 |
| O2 | Galvanic cell (SGX / Alphasense O2-A2 class) or optical (Luminox LOX-02) | 40-220 |
| H2 | Electrochemical H2 cell (Alphasense H2-AF class) | 80-150 |
| Radon | Pulse ionization chamber module (Ecosense RD200M class) | 60-120 |
| Pressure | 2 x barometric (BMP390 class): one in the gas cell, one in air; plus 1 differential (SDP810 class) | 40-60 |
| Temp / moisture at 0.3, 1.0, 1.5 m | TMP117 + capacitance ring (as P02) | 20-30 |
| Pump, valves, cell | Micro diaphragm pump, 2 solenoids, 25 mL cell | 30-50 |
| MCU, LoRa, flash | STM32WL module (as P02) | 15-25 |
| Power | 6 Ah LiFePO4 + 5 W panel + charger, or 2 x Li-SOCl2 D for 4-week battery-only runs | 50-90 |
| Probe, vault, seals, cap | | 40-60 |
| Grab port | Septum for lab Ar/N2/He grabs | 5 |
| **Total** | | **about $520-780** prototype; about $350-500 at 500+ |

**Power** (unverified currents). Each 30-minute cycle: pump 20 s at about 0.3 W, NDIR warm-up and read 30 s at about 0.2 W, other sensors small, radon module about 0.1 W continuous. That is roughly 3-4 Wh/day, so solar is needed for runs past about 3 weeks, or the radon module is duty-cycled.

**Comms.** LoRaWAN to the P02/H01 hilltop gateway, 1-2 kB/day. Full record kept in flash; BLE dump on pickup.

**Deployment.** 2 people, about 45-75 minutes per node (auger, probe, seal, vault, panel). 20-50 nodes on the top 1-3 targets per season, spaced 50-200 m along and across the candidate segments, with 3-5 nodes on a cold reference segment. Run 4-12 weeks to catch 8-25 fronts.

### 3.3 Data product

Each cup gives: Rn, Tn, Rn/Tn, Hg mean vapour, He excess and Ne-corrected He, CO2 flux and delta-13C, plus quality flags (flooded, blank level, duplicate gap). Each node gives: Romanak process class per time step, barometric gain and lag for each gas, air permeability estimate, H2 event count. All are effort-tagged and pre-registered in VOI-Bank before install (same rule as P01 and P02).

### 3.4 In-house analysis line (the scale lever)

- **He/Ne:** a bench quadrupole with a getter and cryo-free inlet, or one of the H04/M22 truck He units, run at the base. Cost $15-60k (unverified). It drops He/Ne from about $30-60 to under $5 per tube at volume.
- **Hg:** a used thermal decomposition AA analyser, about $20-40k (unverified), drops Hg to about $2-4 per sample.
- **CR-39:** NaOH etch bath plus a microscope camera and a track-counting script, under $5k, drops Rn/Tn to about $2.
- **delta-13C** stays at an outside IRMS lab (about $10-20; unverified).
- Break-even is about 1,500-3,000 stations (calc from the gaps above). The whole line costs about $50-100k. That is small next to the value, so build it in season 1 if the first test passes.

---

## 4. How it enters the model and what it shrinks

**Model hook.** In CREAM-COX the cups are a second detector D_g with their own sensitivity s_g and false-positive rate q_g per mask class, under the same latent mask class as the thermal detectors. The joint likelihood for a cell with a dart and a cup is p(dart, cup | z, mask) with a correlation term rho between the two detectors' misses. The calibration campaign (rank 4: 20 blind systems, 40 cold controls) estimates s_g, q_g and rho. The Hg/He and Rn/Tn ratios enter as categorical evidence on the mask class (open / sealed cap / swept / conductive lid). Nodes enter only at target scale, as evidence on which segment is open (M22 implication 5).

| Rank | How P25 helps | Rough size (estimate, unverified) |
|---|---|---|
| **6 Upflow location and footprint** | Picks the leaking 0.2-1 km segment along a range front; nodes confirm with barometric surges and Romanak off-line points. Darts give heat; cups say where the path is. | 30-50% cut in the location spread at targets with a gas signal; little gain where there is none |
| **3 Masking / lid** | Hg-high/He-low = sealed cap; flat gas + warm dart = conductive lid; flat gas + cold dart near a warm well = swept. A direct label on mask class. | 15-30% cut in mask-class entropy at surveyed cells |
| **1 Detection gap** | A partly independent second detector in the same cell lets the occupancy model estimate the thermal miss rate from data. Gain depends on rho: if rho < 0.4, strong; if rho > 0.7, small. | About 10-25% narrower catch-rate band (2-5x to about 1.8-4x on N), if rho < 0.5 |
| **2 Permeability** | Node barometric lag and gain give fault-zone air permeability and "open versus closed"; weak link to deep kg/s. | 5-15% |
| **4 Reliability s/q** | Adds the gas detector to the 20/40 campaign at about $3-6k extra. | Its own s/q priors, not a cut on the thermal ones |

**Buyer metric.** At F5/F95 per 100 visits, the gas channel is cheap (about $50-100 per cell on top of a dart) and adds most where darts are ambiguous. I expect it to improve that metric by about 5-15% for the same spend (estimate, unverified). It is not the main driver; P01 and P02 are.

---

## 5. Rights edge

- **Casual use, no filing.** A cup in an existing 2 m or 3 m hole adds nothing to the footprint already argued under BLM IM 2026-024 (H13, P02). A stand-alone 1 m slide-hammer hole is the same class as the 2 m probe. The node is a hand-augered 75 mm hole under 2 m with a small vault and a low panel. That is still hand tools and battery sensors, but the panel is visible; use battery-only nodes on BLM if the H13 attorney memo says a panel is a "facility" (unverified).
- **Secrecy.** Cups are invisible and come out. Nodes are low and capped. Lab samples go under neutral sample IDs.
- **Edge.** Better segment picks mean nominating or leasing fewer, sharper 500 m parcels, and fewer decoys. On private land, a "soil health and CO2 survey" is another door-opener next to P02's free moisture probe (inference). The gas channel does not find new lockable land by itself; it sharpens what P01/P02 find.

---

## 6. Risks

1. **Weak source.** Blind, capped systems may emit too little gas for even an integrated cup. The toy model says anomalies under about 1.5x stay hidden.
2. **Detector correlation.** If gas misses the same systems the darts miss (rho > 0.7), the rank 1 gain mostly vanishes.
3. **Hg mining noise** across Nevada districts; mask near mines and mills.
4. **He membrane memory.** A too-fast membrane makes the He tube a snapshot of the last days, not an integrator. Needs a bench test.
5. **Moisture.** Flooded cups (wash bottoms, rain events) spoil CR-39 and soda lime. Site on interfluves; 1 in 5 cups carries a humidity button.
6. **Soil uranium and carbonate soils** fake Rn and CO2 anomalies; Tn and delta-13C handle most, not all.
7. **Lab cost and turnaround** until the in-house line exists.
8. **Animals, theft and pickup losses**, guess 5-10% (unverified).
9. **Node solar panel** may be read as more than casual use on BLM.
10. **Low moat.** Every method here is published. The moat is the paired dart + cup + calibration dataset and the placement model, not the hardware.

---

## 7. First test (6-8 weeks, about $10-18k, unverified)

1. **Bench, weeks 0-3 (about $2k).** Build 30 cups. Test the He tube equilibrium time in a He-spiked chamber, pick the membrane for a 7-10 day time constant. Test the Rn/Tn delay path against a thoron source (lab rental) or a thorium-rich sand.
2. **Field, weeks 3-8 (about $8-15k).** One known blind system with public 2 m and TG data (Granite Springs, the pre-registered 68-02 area, or Tungsten Mountain), plus one cold reference valley. 60 cups (40 on the system, 20 cold), 5% duplicates, 6 nodes (4 on the mapped upflow segment, 2 on a cold segment), all in P02 dart holes or 2 m probe holes where those exist. 4-week exposure.
3. **Pass if:** (a) duplicate-cup repeatability is better than about 25% on Rn/Tn, Hg and He-excess; (b) the gas score separates cups within 500 m of the known upflow fault from cold cups at AUC >= 0.7; (c) at least one node on the upflow segment shows Romanak off-line points or barometric surges that the cold nodes do not; (d) the gas score adds information beyond the dart flux (partial correlation, rho of misses < 0.6).
4. **Kill or shrink if:** AUC < 0.6 on a known system, or gas misses track dart misses (rho > 0.8). Then keep only the cheap Rn/Tn + He cup as a dart add-on and drop nodes.
5. Desk work in parallel (free): digitise OFR 80-612, OFR 80-613, OFR 78-246 and Roosevelt Hot Springs soil He/Hg surveys as weak labels and noise priors (M22 datasets table).

---

## Sources

Read in earlier slices (URLs checked there):
- Hinkle and Kilburn 1980, Long Valley soil He and Hg, USGS OFR 80-612: https://pubs.usgs.gov/of/1980/0612/report.pdf
- Hinkle, Roosevelt Hot Springs soil He and Hg: https://digitalcommons.usu.edu/govdocs/47/
- OpenEI, surface mercury geochemistry: https://openei.org/wiki/Geothermal_Exploration_Using_Surface_Mercury_Geochemistry
- Bergfeld et al. 2001, Dixie Valley CO2 flux: https://pubs.usgs.gov/publication/70023687
- Jentsch et al. 2020, Los Humeros CO2 and He: https://arxiv.org/pdf/2002.11515
- DOE / U of Utah, Kumiva MT and soil gas: https://www.energy.gov/sites/prod/files/2015/06/f23/9-Magnetotellurics_Soil%20Gas%20Geochemistry_U%20of%20U.pdf
- Lewicki and Oldenburg, biological CO2 noise: https://www.osti.gov/biblio/840238
- USGS mobile He detector and portable He sniffer: https://pubs.usgs.gov/publication/70012488 ; https://pubs.usgs.gov/publication/70042909
- Other USGS soil-gas reports (not read): https://pubs.usgs.gov/of/1980/0613/report.pdf ; https://pubs.usgs.gov/of/1978/0246/report.pdf

From memory, not checked in this slice (unverified): Romanak et al. 2012 GRL process-based CO2 method; Tokonami et al. RADUET Rn/Tn passive detector; Terradex Track Etch alpha-track uranium surveys; Gardner and Solomon 2009 WRR passive noble-gas diffusion sampler; McLagan/Wania MerPAS passive Hg sampler; Gore/AGI passive soil-gas modules; Nilson et al. 1991 and Massmann and Farrier 1992 on barometric pumping; Etiope and Martinelli 2002 on fault gas migration; Matlick and Buseck 1975; Varekamp and Buseck on soil Hg in geothermal areas. All part prices.

Toy calculation: `P25_calc.py` (this folder).
