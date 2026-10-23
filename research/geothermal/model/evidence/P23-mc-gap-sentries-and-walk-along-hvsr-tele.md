# P23: Mc-Gap Sentries and Walk-Along HVSR. Telemetered microseismic clusters in network gaps, plus a backpack basin-depth kit

Date: 23 Oct 2026. Build candidate P23, model track. This builds on `M12-seismology.md` (no blind seismic discovery on record, catalogs, the 30-80 km network gap, the "long-dwell micro-network" idea), `P03-e-mt-node-2-0-...md` (E-MT node with a 3C geophone, and its point that a 4.5 Hz element cannot do deep-basin HVSR), `P21-tidal-permeability-seismics-...md` (dv/v on the same node fleet), `M09-gravity-magnetics.md` (gravity basin depth about +/-200-300 m), `M30-permeability.md`, `M11-structural-settings.md` (Faulds settings), `../../../hardware/evidence/H03-mt-seismic-nodes.md` (SmartSolo specs and prices), `../../../hardware/evidence/H13-permits-and-secrecy.md` (BLM IM 2026-024 casual use) and `../MODEL.md`. It does not repeat them.

**Method note.** The shared web-search budget for this workflow turn was used up before this agent started. All three searches I tried were refused, so **no new web pages were read.** Facts from repo files are cited by file (those files carry URLs). Papers I know are cited by author, year and journal and marked (from memory, unverified). All prices are my estimates (unverified). Numbers marked (calc) come from `P23_calc.py` in this folder.

## Bottom line

Build it, as two products with one shared electronics board. But change the brief in four places.

1. **"About 100 stations in the gaps" must become about 20 clusters of 5, not 100 stations spread one per gap.** One station in a 30-80 km gap does not lower Mc. It only adds one more pick. A location needs at least 4 stations, and Mc near 0 needs the 4th-nearest station within about 6-10 km of the event. So the unit of design is the **Sentry Cluster**: 5 solar stations on an 8-12 km ring-plus-centre over one Faulds-type setting (step-over, termination, accommodation zone), sharing one hub with a satellite uplink. 20 clusters cover about 20 settings x 150-300 km² each, about 3,000-6,000 km² (calc). That is about 1-2% of the Great Basin, chosen where the model's EVSI per dollar is highest. Clusters move every 9-15 months, so 100 stations see about 40-60 settings in 3 years.
2. **SHmax to +/-10-15 degrees is too optimistic as a default.** With 5 surface stations, focal mechanisms of M0-1 events are poorly constrained. A formal stress inversion needs about 30-50 decent mechanisms. My honest numbers: **+/-10-15 degrees only where a swarm gives 50+ located events (relocated fault-plane geometry plus composite mechanisms)**; +/-20-30 degrees where we get 15-40 events; otherwise use the World Stress Map regional value. The more robust product is not SHmax but the **active-plane geometry**: double-difference relocation of a swarm gives strike and dip of the slipping plane to a few degrees (Coso and Mogul show this; see below). That plugs straight into slip and dilation tendency.
3. **The walk-along kit needs 2 Hz (or lower) geophones, not 4.5 Hz.** P03 already found that a 4.5 Hz element cannot read the 0.1-0.25 Hz peak of a 1-2 km basin. The fix is cheap: 2 Hz 3C elements, plus a low-noise preamp, plus 45-80 minutes per point for deep fill (calc: f0 about 0.2 Hz at 1 km of fill, needs about 50 min of clean record). The microseism peak (0.1-0.3 Hz) is strong everywhere in the West, so this works with ambient noise alone.
4. **Long dwell on BLM land is not casual use.** A station left for a year is "occupancy" in plain terms and needs a land-use authorization (43 CFR 2920, from memory, unverified). So sentries go on **private ranch land first** (the same ranches the Ranch Well Sentinel visits), state trust land under a right-of-entry, and BLM only by permit. The walk-along HVSR kit (under an hour per point, no ground disturbance beyond a spike) fits casual use. This is a feature, not a bug: **hosting a sentry is a reason to sign the heat option on the same ranch.**

With those fixes: Sentry station BOM about **$700-850**, cluster hub about **$1,200-1,600**, so one 5-station cluster is about **$5-6k of hardware** and 20 clusters (100 stations plus spares) about **$120-140k**. The walk-along kit (8 nodes, 2 Hz) is about **$4-6k**. Run cost is about **$4-6k per cluster per year** (two service visits, data plan, cloud picking).

What it buys the model, in order of size:
- **Rank 7 (basin depth / conductive background):** every 2 m probe and every Sentinel well gets a local depth-to-bedrock number. With SPAC-calibrated HVSR the depth error drops from about +/-300 m (gravity) to about +/-100-150 m. At 800 m of fill this cuts T(1.5 km) error from about +/-11 C to about +/-4-6 C (calc). This is the most certain gain, and it comes almost free with the probe crew.
- **Rank 6 (upflow location):** the buried range-front fault is found as a step in HVSR depth, to about the point spacing (+/-150-250 m). The dart and E-MT carpet then go on the right strand.
- **Rank 2 (permeability class):** a swarm on a segment is a likelihood ratio of about 2-4 for "open, critically stressed now" (unverified guess). Quiet at Mc 0 for a year is weak evidence against (LR about 0.7-0.9). I estimate it narrows the permeability-class posterior by about 10-20% in cluster cells. It does not fix the 10x MWe band by itself.
- **Rank 1 (detection gap):** the big structural point. **Seismicity does not care about a cold-water lid.** A hydrologic mask hides heat at 2 m and in ranch wells, but it does not stop deep faults from slipping. So the sentry is a detector whose blind spot is close to independent of the Sentinel's blind spot. That is what a two-detector (capture-recapture) design needs. Its sensitivity is low (many blind systems are seismically quiet), so alone it shrinks the 2-5x band on N by maybe 10-15%. Paired with Sentinel and P03 on the same cells, it is the cleanest test of "is the lidded catch rate really low?".
- **Rank 4 (s/q per observable):** the 20 blind / 40 cold protocol gives s to about +/-0.10-0.11 and q to about +/-0.05-0.06 per seismic observable (calc, binomial). That is enough to tell a useful seismic observable (s 0.5, q 0.1) from a useless one (s 0.3, q 0.25).
- **Rights:** a new swarm on an unleased, un-nominated segment is a trigger to first-file on state land or to approach the ranch owner. Our cluster data are private (our network, our servers). A 12-month **induced-seismicity baseline** is also a data-room item that a buyer must otherwise spend a year collecting (DOE protocol, Majer et al. 2012, DOE/EE-0662, from memory, unverified).

Self-score: model_uncertainty_alpha 3, rights_alpha 3, buildability 4, cost_scale 3, moat 2.

---

## 1. Physics

### 1a. Why microseismicity says something about blind upflow
- **Mechanism.** Great Basin hydrothermal systems are fault-hosted. Upflow lives where faults are critically stressed and stay open: step-overs, terminations, intersections and accommodation zones (Faulds and Hinz, via `M11-structural-settings.md`). A fault that is slipping now at M -1 to 1 is, by definition, close to failure under today's stress. That is the same condition that keeps fractures open for flow (Barton, Zoback and Moos 1995, Geology, "fluid flow along potentially active faults", from memory, unverified). So seismicity is a **permeability likelihood**, not a heat detector (`M12` bottom line).
- **Fluid-driven swarms.** Swarms with slow hypocentre migration (about tens of metres to a km per day, the sqrt(t) diffusion front) point to pore-pressure pulses in a connected fracture network. The 2008 Mogul swarm at Reno was read this way: a fluid front plus aseismic slip (Ruhl, Abercrombie, Smith and Zaliapin 2016, JGR, from memory, unverified). Fitting the front gives a hydraulic diffusivity of about 0.1-1 m²/s, which converts to a fracture permeability estimate (Shapiro et al. 1997 method, from memory, unverified). **That is a direct, if rough, permeability number away from any well**, so it hits rank 2.
- **Known fields are often seismic.** Coso: more than 60,000 events relocated, outlining through-going faults and diffuse fracturing tied to permeability (`M12` F1, USGS). Brady, San Emidio and Dixie Valley sit in seismically active Walker Lane or central Nevada settings (`M12`). But **Crescent Valley showed no discrete events in 75 h with 989 stations** (`M12` F1). So "no events" is common even at real systems. Sensitivity is low to moderate. This is why the protocol in section 5 must measure it, not assume it.
- **What "no events" means.** With Mc 2 (typical in a 30-80 km gap, `M12` F3, unverified), an area can be very active at M0 and look silent. Under Gutenberg-Richter with b = 1, dropping Mc from 2.0 to 0.0 gives **about 100x more events**; from 1.5 to 0.0 about 32x (calc). In a 300 km² cluster with a background rate of 0.5 M>=2 events per 1,000 km² per year, we expect about 15 M>=0 events per year (calc; the rate is a guess, unverified). That is enough to map which segments are active, and enough to make a quiet year mean something. The model needs a **detectability layer** (local Mc map) so a silent cell is treated as "observed quiet" only where Mc is low.

### 1b. Detection limits (what Mc we can really get)
- The physical limit from the local magnitude formula (Hutton and Boore 1987 form) is very low: a quiet rock site at 5-8 km could in theory pick M -2 or smaller (calc). In practice, real dense surface networks reach **Mc about -0.5 to 0.5** at 5-10 km spacing, limited by wind, cattle, pumps, traffic and the need for 4+ clean picks (Coso, Geysers and FORGE-type surface networks, from memory, unverified). I design for **Mc 0 +/- 0.3 inside each cluster ring** and Mc 0.5-1.0 out to 10 km beyond it.
- **ML picking adds about 0.3-0.7 units on top.** Deep-learning pickers (PhaseNet, Zhu and Beroza 2019, GJI; EQTransformer, Mousavi et al. 2020, Nat. Commun.) and template matching typically find 2-10x more events than analyst catalogs on the same data (from memory, unverified). We also run them on the public network stations next to each cluster, so the cluster plus the regional stations give better locations and depth.
- **Noise rules (siting).** Stations go 300+ m from ranch houses, pumps and roads, buried 0.5 m in a sealed vault (a buried 5-gallon pail or PVC vault on a concrete pad), with the geophone on a levelled base. Wind noise falls fast with burial depth.

### 1c. Stress direction and fault-plane geometry
- **Focal mechanisms.** With 5 stations, single mechanisms of M0-1 events have about +/-20-40 degree nodal-plane errors. Composite mechanisms (stacking first motions and S/P amplitude ratios across many events in a swarm, HASH-style, Hardebeck and Shearer 2002/2003, from memory, unverified) do better.
- **Stress inversion.** SATSI/MSATSI-type inversions need about 30-50 mechanisms for +/-10-15 degree SHmax (from memory, unverified). So +/-10-15 degrees is the swarm case only.
- **Relocated plane geometry (the robust product).** Double-difference relocation with cross-correlation times (Waldhauser and Ellsworth 2000, BSSA) turns a swarm of 50+ events into a plane with strike and dip to a few degrees. That directly gives slip tendency and dilation tendency for that strand in the regional stress field. For the model, the most useful seismic output is: "**this strand, this dip, slipping now**".
- **Shear-wave splitting.** 3C stations also give fast-S polarization from local events. Fast direction tends to follow open crack strike, roughly SHmax (Crampin 1994, from memory, unverified). It is a second, cheap stress-and-crack indicator that needs fewer events than an inversion (about 10-20 good S arrivals).

### 1d. HVSR: depth to bedrock at every probe
- **Physics.** Ambient noise on a soft layer over stiff rock shows a peak in the horizontal-to-vertical spectral ratio at about f0 = Vs_avg / (4 H) (Nakamura 1989; Bard and SESAME 2004 guidelines; Ibs-von Seht and Wohlenberg 1999, BSSA, depth law H = a f0^-b, from memory, unverified). Great Basin fill (Vs about 0.3-1.5 km/s) over bedrock (2.5-3.5 km/s, `M12` F4) gives a strong contrast, so the peak is usually clear.
- **Depth range (calc, with Vs rising with depth).** 50 m of fill gives f0 about 1.9 Hz; 200 m about 0.65 Hz; 400 m about 0.4 Hz; 1,000 m about 0.2 Hz; 2,000 m about 0.13 Hz. Minimum clean record (SESAME rule: window at least 10/f0, at least 200 cycles, plus margin for transients) is about 5 min at 50 m, about 25 min at 400 m, about 50 min at 1 km and about 80 min at 2 km.
- **Accuracy.** A depth law fitted elsewhere gives maybe +/-25-40%. A **local Vs profile from SPAC/ESAC** arrays (Aki 1957; Okada 2003; from memory) calibrates it and brings HVSR depth to about **+/-10-20%** (from memory, typical of published basin studies, unverified). At 800 m that is +/-80-160 m, against +/-200-300 m for gravity (`M09`).
- **What it misses.** A deep, weak contrast (fill over altered volcanics) can give a flat curve. A strong shallow contrast (caliche, basalt flow) can give a false shallow peak. Two peaks are common. The model must take HVSR as a likelihood on depth, joined with gravity (`M09`), E-MT basement depth (`P03`) and well logs. This joint basin-depth product is the main input to the conductive temperature model.
- **Heat effect.** None directly. HVSR is a structure tool. Its value is that basin depth is the biggest error in T(z) between control points (`M12` bottom line, `MODEL.md` rank 7).

### 1e. SPAC triangles: Vs to a few hundred metres
- 6-10 nodes in nested triangles (apertures 30, 100, 300 m, plus a centre) for 1-2 hours record Rayleigh-wave dispersion at about 0.5-10 Hz. That inverts to Vs down to about 1/3 to 1/2 of the longest usable wavelength, about 300-600 m (from memory, unverified). One set every 1-2 km gives a local Vs(z) to convert HVSR f0 to depth.

---

## 2. Prior art (and where we sit)
- **Dense nodes over known fields:** Brady (PoroTomo, 238 nodes), San Emidio PSET (1,302 stations), Coso, Hengill (498), Cornwall (450). All retrospective (`M12` F1, `H03`).
- **Regional networks:** UNR Nevada Seismological Laboratory, University of Utah UUSS, PNSN (Oregon), Idaho/Montana networks (from memory). UNR relocated catalog 2008-2023 (Trugman 2024, https://zenodo.org/records/11167510, via `M12`). Gaps of 30-80 km in central/eastern NV, west UT, SE OR, S ID (`M12` F3, unverified).
- **Low-cost seismometers:** Raspberry Shake 3D and 4D (geophone-based, about $500-1,000, unverified) are used in citizen networks and have been shown to record local M1-2 events well (from memory, unverified). SmartSolo IGU-16HR 3C nodes, about $1.5-2.5k each, 30 days at 250 Hz (`H03`, AuScope page).
- **HVSR for basin depth:** used widely for sediment thickness in the US and Europe, including Nevada basins near Reno and Las Vegas for site response (from memory, unverified). Commercial units (Tromino, about $8-15k, unverified) do one point at a time.
- **Zanskar** hires for passive seismic imaging (basement depth, fault structure, stress) and runs large-N arrays at prospects (`M12` F2). So the seismology itself is not a moat. **What is new here:** (a) clusters in network gaps where nobody has Mc 0, chosen by our EVSI map; (b) HVSR carried by the probe crew so every 2 m probe and every ranch well gets a basin depth; (c) a pre-registered s/q measurement for seismic observables against blind and cold sites, which nobody has published; (d) sentries hosted on ranches we option.

---

## 3. v1 design

### 3a. Sentry station (x100 plus 10 spares)
| Part | Choice | Cost (unverified) |
|---|---|---|
| Sensor | 3 x 4.5 Hz geophone elements in a levelled 3C block (SM-24 class), with digital response extension to about 1 Hz | $120-180 |
| ADC | 24-bit, 4-channel delta-sigma (ADS131M04 class), low-noise preamp, 100 sps (event band to about 40 Hz) | $40-60 |
| Compute | Low-power Linux module (Pi Zero 2 W / CM-class) for edge STA/LTA plus a small ML picker; MCU watchdog | $40-70 |
| Timing | GNSS with PPS (u-blox M10 class), better than 1 ms | $30-40 |
| Storage | 256 GB industrial SD (about 2 years of 100 sps 3C compressed) | $30 |
| Radio | LoRa 915 MHz to the hub (picks, health, 10 s waveform snippets); LTE-M/Cat-1 modem where there is coverage | $50-80 |
| Power | 30 W panel, 12 V 30-40 Ah LiFePO4 (about 400-500 Wh, about 18-20 days with no sun at 1 W), MPPT controller | $230-300 |
| Housing | Buried vault (PVC or pail) for sensor; small pole box for electronics; 2 m pole | $70-100 |
| Total | | **about $700-850** |

- **Power budget:** about 1.0 W average (compute 0.6-0.8 W, ADC/GNSS 0.15 W, radio 0.05-0.1 W), so about 24 Wh/day. A 30 W panel in December at 40 N gives about 60 Wh/day (3 peak sun hours, 0.7 derate) (calc, unverified sun hours).
- **Size:** sensor block about 15 x 15 x 10 cm in the vault; pole box about 30 x 25 x 15 cm; total carried weight about 18-22 kg (battery is most of it).

### 3b. Cluster hub (x20)
- Starlink Mini (or Iridium SBD where Starlink is not possible) behind a LoRa gateway and a small router. Hub power: about 150-200 W panels and 100 Ah LiFePO4, running the satellite link in **bursts** (2-4 h per day) to send picks, snippets and health in near real time and the compressed continuous data in daily chunks (about 2-3 kbps per station compressed at 100 sps 3C, so 5 stations make about 135 MB per day, far below Starlink capacity; calc).
- Where LoRa is too slow for continuous data (it is: about 1-5 kbps shared), stations carry continuous data locally and send **picks plus snippets** by LoRa. Continuous data come up by a point-to-point 5 GHz link (about $80-120 per end, run 1-2 h per day) where line of sight allows, or are harvested at service visits. Cloud ML re-picking runs on whatever continuous data have arrived.
- Hub cost: about $1,200-1,600 plus about $50-65/month data (unverified).

### 3c. Cloud stack
- SeisComP or ObsPy-based ingest; PhaseNet/EQTransformer picking; association (GaMMA or REAL); NonLinLoc on a 3D model; HypoDD/GrowClust relocation; HASH composites; MSATSI stress; a nightly **detectability map** (Mc per cell from noise and station geometry, the "probability-based magnitude of completeness" method of Schorlemmer and Woessner 2008, from memory, unverified). The same pipeline re-picks the public stations in and around each cluster. Compute is small (a few CPU-hours per cluster per day).

### 3d. Walk-along HVSR / SPAC kit (one per probe crew)
- **8 nodes:** each is the sentry board with **2 Hz 3C geophones** (about $250-400 per 3C set, unverified), a 6 Ah battery (2-3 days), GNSS, a bubble level, a spike base and a wind cover. About 2.5 kg each. BOM about $450-600 per node.
- **Plus:** a rugged tablet with field QC software (HVSR curve in the field, so a bad point is re-done before the crew leaves), a 300 m tape, flags.
- **Kit cost:** about **$4-6k**. The two-person crew already on site for 2 m probes and Sentinel wells carries it.

### 3e. Deployment and crew time
- **Sentry install:** 2 people, about 2-3 h per station (dig vault, level, pole, panel, test), so a 5-station cluster takes about 2 days with driving. Pull-out about 1 day. Service visits twice a year, about 1 day per cluster.
- **HVSR at every probe:** drop a node next to each 2 m probe as it goes in. Leave it 30-80 min (more over deep fill) while the crew moves on, then leapfrog. With 8 nodes and probes every 250-500 m, the crew adds about **0-15 min per probe point** to the day. A typical day: 15-30 probe points plus 15-30 HVSR points.
- **SPAC triangle every 1-2 km:** 8 nodes in nested triangles for 1-2 h, about 2-3 h crew time each including set-up, done at lunch or at the day's last point. About 1-2 per day.
- **At ranch wells:** one HVSR point at each Sentinel well. The well log (depth to bedrock from the driller's log, when it reached bedrock) is a free calibration point. Over 300-800 Sentinel visits, that gives hundreds of HVSR-vs-log pairs, which is the best calibration set anyone has had for Great Basin HVSR (untested).

### 3f. Siting the 20 clusters
- Rank cells by EVSI per dollar from SENTINEL-COX, filtered to: (1) a Faulds favourable setting (`M11`); (2) local Mc above 1.5 in the current catalog; (3) a cooperative ranch host or state trust land; (4) no operating plant within 10 km (production changes seismicity, `M12` F3). In practice, eastern and central NV, west UT, SE OR, S ID.
- Half of the first 20 clusters serve the **calibration protocol** (section 5). The other half go on top new targets.

---

## 4. Costs
| Item | Cost (unverified) |
|---|---|
| 110 sentry stations | $77-94k |
| 20 hubs | $24-32k |
| 2 walk-along kits | $8-12k |
| Prototype round (10 stations, 1 hub, 1 kit, test bench, shake table time) | $15-25k |
| **Capex total** | **about $125-165k** |
| Run cost per cluster per year (2 service visits, data plan, cloud, battery wear) | $4-6k |
| 20 clusters per year | $80-120k |
| Per setting (a cluster on one setting for 12 months) | **about $10-12k** all-in including amortized hardware |
| Walk-along HVSR | about **$50-150 per km²** extra on a probe campaign (crew time only); about $0 extra hardware after the kit |

Against $0.3-1.5M for one gradient hole (hardware `MEMO.md`), one cluster year is about 1-3% of a hole.

---

## 5. Pre-registered seismic calibration protocol (the 20 blind / 40 cold run)
- **Sites.** 20 known blind systems that are still undeveloped or were pre-production in the catalog window (candidates from `M18-blind-case-studies.md`; e.g. Gabbs Valley, Granite Springs, Crescent Valley, plus systems that are developed but have a pre-production catalog window; status unverified) and 40 cold controls matched on structural setting and basin type (`M19-labels-and-negatives.md`).
- **Walk-along kit at all 60** (about 1-2 crew days each): HVSR line across the range-front, 2-3 SPAC sets. Observables: buried step present (yes/no), depth to bedrock, step offset.
- **Sentry clusters at 10 blind + 10 cold for 9-12 months** (two waves). Observables: events per km² above local Mc on the target segment; swarm flag (a burst with migration); active-plane strike/dip vs mapped faults; shear-wave splitting fast direction; b-value.
- **Also re-pick the public catalog** at all 60 with ML, as a free observable.
- **Pre-register:** the observable definitions, thresholds and analysis code before data, blind the lab to labels until the scoring step, and score s and q per observable and per mask class. With 20/40, s is known to about +/-0.10-0.11 and q to about +/-0.05-0.06 (calc).
- **Bias to watch:** known systems were found partly *because* they are in active settings, so s may be higher at known blind systems than at undiscovered ones. Match controls on setting to limit this, and carry it as a covariate in CREAM-COX.

---

## 6. How much it shrinks the ranked uncertainties
| Rank | Effect (estimates, untested) |
|---|---|
| 7 Conductive background / basin depth | Biggest and surest. Depth error +/-300 m to +/-100-150 m in walked cells; T(1.5 km) error +/-11 C to about +/-4-6 C at 800 m of fill (calc). Overlaps with P03 MT; HVSR wins where no carpet exists, which is most probe cells. |
| 6 Upflow location | Buried range-front strand located to +/-150-250 m along every walked line, so darts and carpets land on the right strand. Maybe 20-30% narrower footprint position in walked cells. |
| 2 Permeability class | Swarm LR about 2-4 for "open now" on a strand (guess); diffusivity from migrating swarms gives a rough permeability number. About 10-20% narrower class posterior in cluster cells. Small against the 10x MWe band. |
| 1 Detection gap | A detector whose blind spot is nearly independent of the hydrologic mask. Alone, about 10-15% off the 2-5x band on N; with Sentinel + P03 on shared cells it is the cleanest two-detector check of the lidded catch rate. |
| 4 s/q | Seismic s/q known to +/-0.1 / +/-0.06 per observable after the protocol. Decides whether seismic observables earn a place in the VOI ranking at all. |
| 3, 5, 8, 9 | No direct effect. |

---

## 7. Rights edge
- **First-file trigger.** A new swarm on an unleased, un-nominated segment, on state trust land, flags it for first-file. On private land it starts a ranch approach. Our cluster data are private, so the trigger is ours for months to years before anyone sees it in a public catalog. But note that regional networks will record the M1.5+ part of a swarm. So the lead is real for small swarms, not for large ones.
- **Hosting deal.** A sentry on a ranch is a natural reason for the heat option visit: free well check (Sentinel), plus "earthquake monitor" for the rancher's own interest. The option is signed on the install day.
- **Induced-seismicity baseline as a data-room asset.** Buyers need a pre-development seismic baseline (DOE protocol, Majer et al. 2012, from memory, unverified). A 12-month cluster record on a parcel saves the buyer about a year and supports a higher sale price or faster close. This also helps permitting for EGS-style buyers (Fervo).
- **No change to federal leasing.** BLM land still goes to auction; this edge is in private and state land, and in timing.

---

## 8. Risks
- **Low sensitivity.** Many blind systems may be seismically quiet at Mc 0 (Crescent Valley had no discrete events in 75 h with 989 stations). If s is below about 0.3 in the protocol, the sentry part drops to a baseline-only product.
- **False positives.** Swarms also happen on cold faults (tectonic swarms, magmatic intrusion in volcanic areas, mining and pumping). q could be 0.2-0.3.
- **Power, theft, cattle, winter.** Remote solar stations fail. Plan for 10-20% station-months lost per year, and put stations where the rancher can see them.
- **Comms.** No cell in most gaps; Starlink power is high; LoRa is too slow for continuous data. The design uses burst satellite plus local storage, so real-time detection is picks-only.
- **Land use.** A year-long station on BLM is not casual use. Without a permit, sentries are limited to private and state land, which may not be where the best targets are.
- **No moat in method.** Zanskar has a seismology team and LBNL ties. The edge is only in where we put clusters and in the joint data with our probes and wells.
- **HVSR ambiguity.** Double peaks, flat curves over weak contrasts, and wind noise. Needs SPAC calibration and the joint basin-depth model.
- **Hindcast bias.** Production at known fields changes seismicity, so labels need pre-production windows.

---

## 9. First test (8-12 weeks, about $20-30k)
1. **Desk, weeks 0-4 (about $2k compute).** Re-pick public waveforms around 10 known blind systems and 20 cold controls in Nevada with PhaseNet/EQTransformer, build a local Mc map, and score "events on the target segment above local Mc" as a first s/q. This alone tells us whether seismic observables are worth field money. Fit HVSR f0-to-depth laws on public nodal data from PoroTomo/Brady and other IRIS nodal sets where wells give bedrock depth.
2. **Bench, weeks 2-8.** Build 10 sentry stations and 8 walk-along nodes. Huddle test against a borrowed broadband or SmartSolo nodes for self-noise and timing.
3. **Field, weeks 8-12.** One cluster on a cooperating ranch over a known blind system with wells (e.g. a Granite Springs-type setting, pre-registered). Walk-along HVSR across the range-front with SPAC every 1-2 km, and score depth against well logs. **Pass:** HVSR depth within +/-20% of logged bedrock at 70%+ of points; cluster Mc at or below 0.3 in the ring after 6 weeks; station uptime over 90%.

---

## Sources
- Repo: `M12-seismology.md` (Brawley DAS, San Emidio PSET, Coso, Brady, Trugman 2024 catalog, Zanskar roles), `P03` (4.5 Hz HVSR limit), `P21`, `M09`, `M11`, `M18`, `M19`, `../../../hardware/evidence/H03-mt-seismic-nodes.md`, `H13-permits-and-secrecy.md`, `../MODEL.md`.
- https://zenodo.org/records/11167510 (UNR relocated Nevada catalog, via M12)
- https://gdr.openei.org/files/1386/WarrenFinalReport.pdf (San Emidio and Crescent Valley PSET, via M12)
- https://www.usgs.gov/publications/using-micro-seismicity-and-seismic-velocities-map-subsurface-geologic-and-hydrologic (Coso, via M12)
- https://auspass.edu.au/xwiki/bin/view/Instrumentation/SmartSolo%20Nodes (SmartSolo specs, via H03)
- From memory, unverified: Hutton and Boore 1987 (BSSA, ML scale); Gutenberg-Richter; Barton, Zoback and Moos 1995 (Geology); Shapiro et al. 1997 (GJI, diffusivity from seismicity fronts); Ruhl et al. 2016 (JGR, Mogul swarm); Zhu and Beroza 2019 (GJI, PhaseNet); Mousavi et al. 2020 (Nat. Commun., EQTransformer); Waldhauser and Ellsworth 2000 (BSSA, hypoDD); Hardebeck and Shearer 2002 (BSSA, HASH); Schorlemmer and Woessner 2008 (BSSA, PMC); Crampin 1994; Nakamura 1989; SESAME 2004 HVSR guidelines; Ibs-von Seht and Wohlenberg 1999 (BSSA); Aki 1957 and Okada 2003 (SPAC); Majer et al. 2012 DOE/EE-0662 induced-seismicity protocol; 43 CFR 2920 land-use authorizations.
- Calculations: `P23_calc.py` (this folder).
