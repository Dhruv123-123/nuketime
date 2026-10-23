# P06: Valley Pressure-and-InSAR Array. Tides, borrowed pump interference and poroelastic deformation as a valley-scale permeability map

Date: 23 Oct 2026. Build candidate P06, model track. This builds on `../MODEL.md` (SENTINEL-COX, THERMOS-B, ranked uncertainties), `M30-permeability.md` (Libbey and Murphy permeability classes, tides via Hsieh 1987, specific capacity), `M23-hydrology-masking.md` (four masks, plume length L = rho c v b d / lambda), `M10-remote-sensing.md` (NISAR public since 20 Jul 2026, OPERA DISP-S1, InSAR as a strain layer), `P01-ranch-well-sentinel-2-0-a-resident-well-.md` (resident string, tidal fit arithmetic, pump-current clamp, pump-pull hook), `P03-e-mt-node-2-0-drone-placed-dc-coupled-te.md` (DC-coupled E/SP node), `P04` (gauge-port tee, acoustic sounder) and `P05` (pump-cycle sampler), plus `../../../hardware/MEMO.md`. It does not repeat them.

**Method note.** The shared web search budget for this workflow turn (200 calls) was used up before this agent started. All three searches I tried were refused, so **no new web pages were read**. Facts from repo files are cited by file. Standard papers I know are cited by author, year and journal and marked (from memory, unverified) where I could not check details. All prices are my estimates (unverified). Numbers marked (calc) are my own arithmetic; the script lines are reproduced in section 2.

## Bottom line

Build it, as the **valley-scale layer that sits on top of the P01 Sentinel fleet**, not as a separate product. A Sentinel tells us about one well. This array tells us how the wells talk to each other, and that is the thing the model cannot get any other cheap way.

Four changes make it better than the brief.

1. **Split the year in two.** In winter (about Nov-Mar) the irrigation pumps are off. The wells are quiet, so earth tides and barometric response give clean T and S at each well. In summer the pumps run. They wreck the tide fit but become free interference tests. So one install yields two different experiments per year. **The pilot should go in this winter (Nov 2026).**
2. **Replace the pivot current clamp with a no-entry "pump-state tag".** Putting a current transformer on a motor lead means opening a 480 V panel. That needs an electrician and spooks ranchers. A $25-40 magnetic tag stuck to the pump head or panel door (accelerometer plus magnetometer) logs on/off time to the second. Pump rate comes from the nameplate, one clamp-on ultrasonic flow reading per season, and OpenET monthly water use. Pumps on neighbouring land we do not tag become "unknown sources" that the inversion fits (Harp and Vesselinov style, below).
3. **Corner reflectors are cheap if we build them, but the L-band ones must be big.** A 0.9 m trihedral is plenty for Sentinel-1 C-band (about 29.5 dBsm, calc). For NISAR L-band the same reflector gives only about 17 dBsm, too weak against a bright desert pixel. A 1.5-2.0 m reflector gives 26-31 dBsm (calc). So v1 uses about 10-15 DIY reflectors per valley ($350-900 each built), and only 3-5 of them large dual-band. That cuts the brief's $60-100k for 50 sites to about **$25-45k** (unverified). Most of the valley is already measured by free OPERA DISP-S1 and NISAR stacks; reflectors only pin the wells and fault crossings where fields decorrelate.
4. **Drop the tidal streaming-potential channel from v1.** The signal is tiny. A 1 cm tidal head (about 100 Pa) with a coupling of roughly 1-10 mV per 0.1 MPa gives about 1-10 microvolts (calc, from memory coupling range). Daily ionospheric (Sq) telluric fields put roughly 0.1-1 mV on a 100 m dipole at the same periods (unverified). Leave SP to the P03 E-node and treat any tidal SP as a bonus.

What it buys, in plain terms (section 4 has the arithmetic):
- **Rank 3 (flushing speed of the masking aquifer):** the Darcy speed v = K x i is today known to about 10x (driller specific capacity, guessed gradient). Tides plus interference plus mm-levelled heads put it within about 2-3x in instrumented valleys. That is roughly a **60-80% cut in the variance of log v**, and the plume length L scales directly with v.
- **Rank 8 (one system or several):** a direct yes/no test of whether two warm wells share a pressure field. I expect a usable answer in **about half to two-thirds of instrumented valleys**.
- **Rank 6 (upflow location):** better v and head maps let the model back-project outflow plumes to their source. Footprint offset error might drop from about 3-30 km to about 1-5 km (calc, via L).
- **Rank 2 (permeability class at depth):** only partial. Shallow fault-zone T and anisotropy are a proxy for deep permeability. Expect about **10-25% variance cut** on rank 2 per instrumented system, more where a shut-in TG or oil well reaches 300 m to 2 km.

Cost: about **$30-55k per valley** for v1 (40 pressure nodes, 15-25 pump tags, a barometer hub, 10-15 reflectors, two crew-weeks), falling to about $20-30k at scale (unverified). Self-score: model_uncertainty_alpha 3.5, rights_alpha 3, buildability 4.5, cost_scale 4, moat 3.5.

## 1. Physics: why it works and where it does not

### 1a. Earth tides and air pressure give T and S at each well (winter mode)
- The solid Earth tide squeezes rock by an areal strain of roughly 1-2 x 10^-8 (M2). In a confined aquifer the head response is about h = B Ku eps / (rho g). With Skempton B about 0.5 and undrained bulk modulus Ku about 10 GPa, that gives about **0.5-1 cm** of head (calc). Real confined wells show about 1-20 mm (from memory, unverified range).
- Hsieh, Bredehoeft and Farr (1987, Water Resources Research 23:1824) showed that the **phase lag and amplitude ratio** of the tidal response give transmissivity T and storativity S. The method resolves T best at about 1e-6 to 1e-3 m2/s (M30, P01). Above that the well follows the aquifer with no lag and we get a lower bound, which is still a useful "high permeability" label.
- Barometric efficiency gives a second, independent handle on storage. Acworth, Halloran, Rau, Cuthbert and Bernardi (2016, Geophysical Research Letters 43:11671) give a frequency-domain method that uses both the Earth tide and the air tide at S2 to get compressible storage (from memory, unverified page). Open Python tools exist: **HydroGeoSines** and **PyGTide** (Rau and others; from memory, unverified). We do not need to write the core maths.
- **The confinement test is itself a label.** A well with no tide and a near-1 barometric efficiency is unconfined or poorly cased. A well with a strong tide and a big phase lag sits in a tight, confined zone. A well with a strong tide and no lag sits in a confined, highly permeable conduit. Each class maps to a mask class in THERMOS-B.
- **Fault zones show up.** Xue et al. (2013, Science 340:1555) tracked fault-zone permeability in the Wenchuan drill hole from the tidal phase over months. Elkhoury, Brodsky and Agnew (2006, Nature 441:1135) showed that distant quakes raise permeability and shift the tidal phase (both cited in M30). Allègre et al. (2016, JGR) used tides to get fault-zone anisotropy (from memory, unverified). So tides are a proven fault-permeability tool, just never used to rank geothermal land.
- **Sampling arithmetic (from P01).** With about 2 mm resolution, 1-minute samples and 30 days, the M2 amplitude fits to about 0.1 mm under white noise. Real noise is red, so plan on **45-60 days**. M2 (12.42 h) and O1 (25.82 h) are clean of the 24 h and 12 h human and solar lines after about 15 days. Use M2 and O1. Avoid K1, S1 and S2 for the hydraulics, because barometric and pump noise piles up there.

### 1b. Borrowed pumps give connected T and S between wells (summer mode)
- A pump turning on is a step source. Theis drawdown at distance r after time t is s = Q/(4 pi T) W(u), with u = r^2 S / (4 T t).
- For a typical irrigation well, Q = 50 L/s (about 800 gpm). After 12 hours (calc):

| Aquifer type | T (m2/s) | S | Drawdown at 500 m | at 2 km |
|---|---|---|---|---|
| Confined fractured | 1e-3 | 1e-4 | 6 m | 13 cm |
| Confined sand | 5e-3 | 5e-4 | 1.2 m | 2.5 cm |
| Leaky / semi-confined | 1e-3 | 1e-3 | 43 cm | below 1 mm |
| Unconfined alluvium | 5e-3 | 0.1 | below 1 mm | below 1 mm |

- The reach of a periodic signal (the distance where its amplitude falls by e) is sqrt(D P / pi), with diffusivity D = T/S (calc):

| Aquifer | daily cycle | weekly cycle | season (1 yr) |
|---|---|---|---|
| Confined (D = 10 m2/s) | 0.5 km | 1.4 km | 10 km |
| Leaky (D = 1 m2/s) | 0.17 km | 0.44 km | 3.2 km |
| Unconfined (D = 0.05 m2/s) | 0.04 km | 0.1 km | 0.7 km |

- **Plain reading.** In confined or fractured rock, every pump within 2-4 km is a test signal we can read with a 1 mm sensor. In open, unconfined alluvium the signal dies within a few hundred metres. So the array is strongest exactly where we care: **range-front fault zones, bedrock and confined basin aquifers**. It is weak on the open valley floor, and there the InSAR leg takes over.
- **This is a known method, just never used for geothermal.** Periodic pumping tests: Rasmussen et al. (2003, Journal of Hydrology), Renner and Messar (2006, Geophysical Journal International). Oscillatory hydraulic tomography: Cardiff, Bakhos, Kitanidis and Barrash (2013, WRR 49:5395) and Bakhos et al. (2014). **Using uncontrolled supply-well pumping as the source:** Harp and Vesselinov (2010-2011, LANL; "Identification of pumping influences in long-term water level fluctuations", Groundwater) separated the drawdown from many water-supply wells in long records (all from memory, unverified details). Vesselinov is the same researcher behind the NMFk geothermal work cited in the geochem files.
- **The pump tag is what makes it cheap.** If we know the exact on/off time of each pump, the unknown is only the response function, a linear regression (like the barometric deconvolution of Rasmussen and Crawford 1997, Groundwater; from memory). Without tags, the inversion must also guess the timing, which is much harder.

### 1c. InSAR gives storage and barrier faults across the whole valley (season mode)
- When a confined aquifer drains each summer and refills each winter, the land moves down and up by mm to cm. Skeletal storage is S_ke = (change in thickness) / (change in head). Pairing InSAR with even a few head records turns the deformation map into a storage map.
- **Faults show up as steps.** Amelung, Galloway, Bell, Zebker and Laczniak (1999, Geology 27:483) showed in Las Vegas Valley that Quaternary faults bound the subsiding areas, because they act as groundwater barriers. Hoffmann, Zebker, Galloway and Amelung (2001, WRR 37:1551) got seasonal storage from InSAR and heads there. Chen, Knight and Zebker (2016-2017, WRR) estimated heads from InSAR in the San Luis Valley, Colorado (all from memory, unverified pages).
- **Why that matters for heat.** A fault that is a barrier to cross-flow can still be a conduit along its plane. That is the classic Great Basin geothermal fault zone (low cross-fault, high along-fault permeability; M30, M11). A step in seasonal deformation across a mapped or buried fault, with a matching head jump across it in the pressure array, flags the fault as a sealed-across, open-along structure. That is a structural score no public layer has.
- **Free data does most of the work.** OPERA DISP-S1 gives North American Sentinel-1 displacement time series. NISAR L-band (public since 20 Jul 2026) keeps coherence better over shrub and fields (M10). The reflectors only fix three weak spots: irrigated fields that decorrelate each season, tying InSAR to the exact wellhead, and a reference point that does not move.
- **Reflector size (calc).** Trihedral RCS = 4 pi a^4 / (3 lambda^2). C-band (5.55 cm): a = 0.7 m gives 25 dBsm, 0.9 m gives 29.5 dBsm. L-band (24 cm): 0.9 m gives 17 dBsm, 1.5 m gives 26 dBsm, 2.0 m gives 31 dBsm. A rough rule is to beat the pixel clutter by 15-20 dB. So 0.9 m serves C-band; dual-band sites need 1.5-2 m. Garthwaite (2017, Remote Sensing 9:648, Geoscience Australia) gives the standard design rules for multi-frequency reflectors (from memory, unverified).
- **Detection floor.** Single-pixel stacks reach about 1-3 mm per epoch and well under 1 mm/yr in velocity with years of data (M10, D10). Seasonal pumping signals in confined Great Basin basins are often 5-30 mm (unverified range). That is plenty. Natural blind systems themselves do **not** deform measurably unless produced. So InSAR here is a hydrology tool, not a heat detector.

### 1d. What the combined data constrain
The array feeds a valley groundwater model (MODFLOW 6, a few km grid with fault "horizontal flow barrier" cells) solved by ensemble methods (PEST++ IES or ES-MDA) with the tidal T/S, interference responses, heads and InSAR storage as data. Out come posterior fields for:
1. **T and S fields**, with uncertainty, including along-fault and cross-fault T for each mapped fault.
2. **Darcy speed v = K i** in the aquifer that masks the heat. This is the "sweep strength" M23 asks for, and the v in L = rho c v b d / lambda.
3. **Connectivity between warm wells**: do they share a pressure response to the same pump, the same barometric lag, the same seasonal head trend? Shared response is evidence for one system (rank 8).
4. **Flow paths**: with v and heads, back-project warm-water plumes up-gradient to the likely upflow (rank 6), handed to GHOST Tier 1 as the plume velocity.

## 2. Prior art and what is new
- **Tidal hydraulics:** Hsieh et al. 1987; Rojstaczer 1988 (JGR); Cutillo and Bredehoeft 2011 (Groundwater); Acworth et al. 2016; McMillan et al. 2019 (WRR, global tidal compilation) (from memory, unverified). Tidal monitoring of geothermal reservoirs has been done in producing fields for decades (unverified; I recall Cerro Prieto and Geysers-era papers but could not check).
- **Opportunistic interference:** Harp and Vesselinov (LANL), the oscillatory-tomography group (Cardiff, Barrash, Kitanidis).
- **InSAR + aquifer:** Amelung 1999, Hoffmann 2001, Chaussard et al. 2014 (JGR), Chen et al. 2016; in geothermal fields mostly production monitoring (Ali et al. 2016 at Brady, cited in M10/D10).
- **Low-cost loggers:** the open "Cave Pearl" Arduino logger designs and many university projects show $50-150 loggers with MS5803-class sensors (from memory, unverified). Commercial vented or absolute loggers (Solinst Levelogger, In-Situ Level TROLL, Van Essen Diver) run roughly $600-2,000 each (unverified).
- **What nobody has done (that we found in repo files):** run a dense, tagged, two-season pressure array plus InSAR on private ranch wells chosen by a geothermal model, to price permeability, mask sweep and connectivity before buying rights. Zanskar's stated gap is permeability (M30, M13), and its work is on BLM auction land, not ranch wells.

## 3. Concrete v1 design

### 3a. The pressure node ("Tide Node")
| Part | Choice | Cost at 10 / at 200 (unverified) |
|---|---|---|
| Pressure sensor | Absolute, digital, 0-20 bar or 0-10 bar range, 24-bit. Two grades: (A) Keller 4LD-9LD class OEM (about 0.02-0.05% FS accuracy, finer resolution, low drift); (B) TE MS5803-14BA / MS5837-30BA (0.2 mbar = 2 mm water resolution, more drift). Resolution matters more than accuracy, because drift is fitted out. Grade A in key wells, B elsewhere. | A: $180-350 / $120-200. B: $25-40 / $12-20 |
| Housing | 19 mm OD, 316 stainless or Delrin tube, 250 mm long, epoxy-potted. Fits a 3/4" sounding tube and 1" access ports. | $40 / $15 |
| Cable | 4-core PUR, Kevlar strength member, 30-200 m, pre-marked every metre. Carries power and I2C/RS-485. | $0.8-1.5/m |
| Water temperature | 0.01 C thermistor in the probe tip (doubles as a slow P01-style check) | $10 / $5 |
| Top box | Low-power MCU (STM32L4 or nRF52), 2x microSD, GPS for time (PPS once a day), BMP390 barometer (relative noise about 0.03 hPa = 0.3 mm water), 3-axis accelerometer (pump vibration at the well itself) | $45 / $25 |
| Power | 3x D-cell lithium (about 50 Wh) or 2 W panel + LiFePO4 | $35-60 |
| Radio | LoRa 915 MHz to a valley hub (5-15 km line of sight in open basins) | $15 / $8 |
| Enclosure | IP67 box, strapped to casing or inside the well house, with a vented cap for the sounding tube | $20 / $10 |
| **Total** | | **Grade B node about $250-350 at 10, $120-180 at 200. Grade A about $450-650 at 10, $250-350 at 200.** |

- Sampling: pressure and barometer every 1 minute (all year); 1 s burst for 10 minutes after the node's own pump-vibration trigger; 10 Hz for 30 minutes after a regional M5+ quake time from the hub (hydroseismogram, P01).
- Power budget: about 30-80 microamps average (calc, for 1-min samples and hourly LoRa). Two years on D-cells.
- Installed depth: at least 5-10 m below the lowest summer pumping level (so it never goes dry), above the pump intake. The install visit uses the P04 acoustic sounder or a tape to find the level.

### 3b. Pump-state tag
- Magnet-mount puck, 60 mm. Accelerometer and magnetometer (motor field and vibration), coin or AA lithium, LoRa. On/off times to about 1 s.
- Optional: one clamp-on ultrasonic flow reading per season with a shared $1.5-3k meter (unverified price) to set Q. Monthly Q cross-checked with OpenET consumptive use per field.
- Cost: $25-40 at 100 (unverified).

### 3c. Valley hub
- Solar 20-40 W, LTE-M or Iridium SBD backhaul, LoRa gateway, reference barometer (Grade A), and a u-blox ZED-F9P dual-band GNSS for time and as a geodetic monument co-located with a reflector. About $800-1,500 (unverified).

### 3d. Corner reflectors
- **Standard (C-band):** 0.9 m inner-leg trihedral, 3 mm aluminium sheet or 2 mm galvanised steel with drain holes, on a 50 mm pipe set 1 m into concrete (or a helical ground screw for no-concrete installs on rancher land). Aimed to the ascending and descending Sentinel-1 look (two reflectors back-to-back, or one rotatable). About $350-600 built (unverified).
- **Dual-band (C + NISAR L):** 1.5-2.0 m trihedral, bolted panel kit. About $1,200-2,500 built (unverified). 3-5 per valley.
- Placement: at 6-10 pressure-node wells, on both sides of 2-3 target faults (paired 200-500 m apart), and 2 on bedrock as stable references.

### 3e. Deployment and crew time
| Task | Crew | Time per site |
|---|---|---|
| Pressure node in a sounding tube or open port (find level, lower probe, strap box, test LoRa) | 2 | 45-90 min |
| Node in a shut-in TG or oil well (needs wellhead fitting; P01 cautions) | 2 | 2-4 h |
| Pump tag | 1 | 10 min |
| Standard reflector with ground screw | 2 | 1.5-2 h |
| Dual-band reflector with concrete | 2 | 4-6 h, return trip to aim |
| RTK GNSS tie of each wellhead (needed for mm-level heads across the valley) | 1 | 20 min |

A 40-node, 20-tag, 12-reflector valley is about **8-10 crew-days**, which is about two crew-weeks with driving. Retrieval or service: one day per valley per season. The install visit is also the option visit (hardware MEMO, H06).

### 3f. Network size and layout
- 20 nodes is the floor for one fault-bounded basin, 40 is the v1 target, 100-200 for a full valley at 300-800 m spacing near targets.
- Lay out in three groups: (1) a line across each target range-front fault, 4-6 wells on each side; (2) every warm well in the valley (P01 and M06 lists); (3) cold controls spread up-gradient and down-gradient.

### 3g. Software
- Tidal fit: HydroGeoSines / PyGTide pipeline, outputs T, S, BE and their posteriors per well per season.
- Interference: tagged-pump regression deconvolution (response functions per pump-well pair), then Theis/Hantush fits for each pair.
- Valley model: MODFLOW 6 + PEST++ IES, priors from driller specific capacity (P04) and the frozen-label GBM. InSAR enters as S_ke x delta-h per pixel.
- Output to THERMOS-B: per-cell posteriors for aquifer v, lid T/S, fault cross and along T, and a "same-system" probability for each warm-well pair. GHOST Tier 1 can then score the array in-silico against P01 alone before we build 40 nodes.

## 4. How much it shrinks the ranked uncertainties

All of these are first estimates (calc and judgement, untested). Tier 1 EIG must confirm them.

| Rank | What the array adds | Before | After, instrumented valley | Variance cut |
|---|---|---|---|---|
| 3 Masking / flushing speed | T, S, head gradient to mm, so v = K i | log v uncertain to about 10x (1 sigma about a factor 3-5) | about 2-3x | **60-80%** on log v; lid sensitivity term much tighter |
| 8 One system or several | Shared pressure response, shared barometric lag, shared seasonal trend among warm wells | prior P(same system) about 0.5 for wells 2-6 km apart | resolved to under 0.2 or over 0.8 in about 50-65% of pairs | about 40-60% of the "split vs merge" term |
| 6 Upflow location | v and heads for plume back-projection; barrier faults | offset 3-30 km (M23) | about 1-5 km | **50-70%** on offset in valleys with good confined response |
| 2 Permeability class (deep) | Fault-zone T and anisotropy at 50-300 m; connected T over km; deep TG/oil wells add direct reservoir T | about 10x in MWe (MODEL) | proxy only | **10-25%** per system; 30-40% where a 0.3-2 km well is in the array |
| 1 Detection gap | Indirect: tells P_det which warm wells are swept outflow vs local | | | small, about 5-10% |

**Regional effect.** If one valley costs about $30-55k and there are perhaps 60-120 target valleys in NV+UT+OR+ID with enough wells (unverified count), a full program is about $3-6M over 3-4 years. That is cheap next to one confirmation well. Because ranks 2, 3 and 6 multiply MWe (permeability), sensitivity (masking) and footprint, I would expect the regional F5/F95 band to narrow by roughly 15-30% from this layer alone, on top of P01 (judgement, untested). This mostly helps the *bankable* number (P50 on lockable land), which is the main kill line.

## 5. Rights edge
- **No filing at all.** Everything runs on private wells under the heat option, signed on the install visit. No BLM notice, no state permit. InSAR is from orbit. Reflectors sit on optioned ranch land.
- **A second reason for the rancher to say yes.** The rancher gets a free, live well-level and pump-efficiency record, and a warning when a neighbour's pumping is drawing them down. In Nevada, where water rights fights are constant, that is valuable to a rancher (judgement, unverified).
- **A second product for the buyer.** A geothermal developer must show its production and injection will not harm existing water rights, and water-right protests have slowed Nevada projects (unverified specific cases). A multi-season, pre-development baseline of every ranch well in the valley is exactly what a developer needs for that filing. It also tells them whether injection will short-circuit to production, through the barrier-vs-conduit fault map. This is a reason a buyer pays more for our package than for an anomaly alone. It lifts the c4 "step-up" weak spot from the hardware MEMO a little, which hardware so far had not done.
- **Private data, time moat.** Two seasons of pressure data can only be bought with two seasons. A copier starting later is always a year behind in that valley.
- **Leak risk.** Ranchers talk. Reflectors are visible. Keep reflectors modest and on optioned land only. Do not install in a valley until the options there are signed.

## 6. Risks
1. **Unconfined valleys are deaf.** No tide and short-range interference in open alluvium. Mitigation: pre-screen valleys by driller logs (clay lids, artesian or near-artesian wells, bedrock wells). Kill line below.
2. **Access in pumped wells.** Many sounding tubes are blocked or absent (H06's 30% loggable line). Use idle, windmill, monitoring and domestic wells too; use the P01 pump-pull hook.
3. **Red noise from pumping.** Summer tides will be unusable in many wells. That is why the design is two-season.
4. **Shallow aquifer is not the reservoir.** Rank 2 gain is a proxy. Deep TG and shut-in oil wells are the only direct handle, and access to them is slower (operator consent, NDOM rules; unverified).
5. **InSAR decorrelation and atmosphere** in irrigated fields. Reflectors and NISAR L-band reduce it, but the storage map will have holes.
6. **Sensor drift and casing effects** (well-bore storage, poor casing seal) can fake phase lags. Use the barometric response to flag bad wells, and the Hsieh well-bore correction.
7. **Visible gear** tips off copiers. Mitigation in section 5.
8. **Price figures are unverified.**

## 7. Cheapest first test (this winter)
- **Where:** one valley with a known blind or semi-blind system, heavy groundwater irrigation and confined zones (candidates, unverified: Smith/Mason Valley near Wabuska; Carson Desert near Soda Lake / Salt Wells; Railroad Valley, which adds oil wells), plus one cold control valley.
- **What:** 20 Grade-B nodes, 4 Grade-A nodes, 10 pump tags, 1 hub, 4 standard and 1 dual-band reflector. Install Nov-Dec 2026, read tides through March, read interference April-August 2027.
- **Cost and time:** about $15-25k in parts and about 3 crew-weeks (unverified). Build of the first 10 nodes: 4-6 weeks.
- **Pass bars:**
  1. M2 SNR over 5 in at least 50% of nodes in the known valley in winter.
  2. Tidal T within a factor 2 of a contractor or driller pump test in at least 3 wells.
  3. In summer, at least 5 pump-well pairs over 1 km apart give a clean, tag-timed response.
  4. The valley model predicts held-out heads to within 0.3 m and gives a v posterior narrower than 3x.
  5. At least one InSAR step across a mapped fault matches a head jump in the array.
  6. At least half of hosts sign the heat option and agree to keep the node.
- **Kill:** fewer than 30% of wells show a tide in the known confined valley, and no pump pair over 1 km responds. Then the array shrinks to a few nodes added to P01, and the InSAR leg goes desk-only with free OPERA and NISAR data.

## 8. Self-scores (1-5)
- **model_uncertainty_alpha: 3.5.** Strong on ranks 3, 6 and 8, weak on rank 2 at depth.
- **rights_alpha: 3.** No filing, second rancher hook, and a water-rights baseline the buyer needs. It does not by itself make land cheaper.
- **buildability: 4.5.** Off-the-shelf sensors, open software, 4-6 weeks to 10 nodes with a small team.
- **cost_scale: 4.** About $30-55k per valley, $3-6M for the West.
- **moat: 3.5.** Methods are public, but two-season private records on optioned land cannot be copied fast.
