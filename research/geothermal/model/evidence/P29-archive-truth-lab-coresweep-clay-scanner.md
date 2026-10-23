# P29: Archive Truth Lab. CoreSweep clay scanner, ArchivePack paper scanning, ChipK conductivity bench, VeinTherm fluid inclusions and a Rosetta resistivity-IP bench

Date: 23 Oct 2026. Build candidate P29, model track. This builds on `MODEL.md` (SENTINEL-COX, ranks 1-9, kill gates), `M08-magnetotellurics.md` (smectite below about 180 C gives a 1-10 ohm-m cap; conductors are non-unique: brine, lake clay, graphite, fossil caps; "use an explicit physics likelihood, not a raw resistivity feature"), `M18-blind-case-studies.md` (Blue Mountain, McGinness, Don A. Campbell and Tungsten Mountain were first seen in mineral holes; Don A. Campbell HTEM conductor under 100 m from smectite), `M20-tg-and-mining-holes.md` (2,002 NBMG scanned well-log PDFs, 442 TG holes, zero LAS), `M04`/`M05` (conductivity adds about +/-10-20% to heat flow), `M10` (SWIR sees alteration that outlives heat), `M23` (mask classes, Kimama smectite seal at about 950-1,020 m under the Snake River Plain aquifer), `P07` (memory pucks on active mining rigs), `P15` (our own corer with an alteration scan on new core), `../../evidence/D06-mining-assessment.md` (USGS core libraries in Mercury NV and Denver, UGS core database, more than 2,000 mining holes a year in Nevada, no heat filing duty) and `../../evidence/D07-scanned-logs.md` (raster log economics). It does not repeat them. What is new here: the **already-drilled core and chips sitting on shelves**, read for heat for the first time, and the bench physics that turns our EM and gradient data into calibrated likelihoods.

**Method note.** The shared web-search budget for this workflow turn was used up before this slice ran (3 of 3 searches refused). No new web sources were read. Everything comes from sibling files (which cite primary sources with URLs), from the literature I know (author, year and journal given so it can be found; marked "from memory"), and from a new calc script, `P29_calc.py` (same folder). Instrument models and prices are **(unverified)** and must be quoted before buying. Library holdings (metres of core) are **(unverified)**.

---

## Bottom line

- **What it is.** A van-and-trailer lab that goes to core libraries (NBMG Great Basin Science Sample and Records Library in Reno, USGS Core Research Center in Denver, the UGS Utah Core Research Center, the USGS Mercury NV store per D06) and to mining-company core yards. It reads old mining and oil core and RC chips for **heat** with five benches. The headline bench is CoreSweep, a tray scanner that logs SWIR clay mineralogy, magnetic susceptibility and gamma every few cm.
- **Why it matters.** The case studies (M18) show that the first sign of most blind Nevada systems was a hole drilled for gold. The temperature in those holes was mostly not written down. But the **rock in the core box remembers**: the smectite-to-illite change, zeolites, adularia and bladed calcite (boiling), and fluid inclusions. This is a second detector that does not depend on the thermal channel at all, and it reaches 300-1,000 m, below the 200 m lids that beat 2 m probes, darts and ranch wells.
- **The hard part is live versus dead.** Most of the Great Basin's clay caps are fossil (Miocene epithermal gold systems). Clay alone is a weak clue (toy likelihood ratio about 1.9). Clay plus a present-day temperature tie (from an ArchivePack-extracted log, P07 puck or a Sentinel visit) plus young fluid inclusions on the boiling curve gives a toy LR of about **38**, which lifts a 10% prior to about **0.8** (calc).
- **Throughput and cost.** Tray handling, not the sensor, sets the pace: about **900-960 m/day** of core and about **2,400 m/day** of RC chip trays with two people (calc). Cost is about **$2,300 per day**, so **$1.5-3 per metre of core and about $1 per metre of chips** (calc, unverified). The brief's "under $1/m" holds only for chips, or if the library provides forklift and racking staff. Still trivial against $300-1,500/m for a new gradient hole.
- **Build cost for all five benches: about $210-350k** (BOM below, unverified), a bit above the brief's $135-260k; renting the spectrometer and outsourcing FI and SIP work at first brings it inside. A lean v1 (CoreSweep with a point SWIR spectrometer, ChipK, ArchivePack) is about $110-160k and can be in a library in 8-12 weeks.
- **Model effect (estimates, untested).** Rank 3 lid thickness: about 30-50% cut in cored cells. Rank 5 T at 0.5-2 km: about 20-35% cut in cored cells. Rank 7 conductive background: about 40-60% cut in the k term. Rank 4 s/q per mask: about 30-50% cut in the EM detector spread (Rosetta). Rank 1 detection gap: about 10-25% at the regional level, and it directly feeds the archive coverage kill gate ("T(z) coverage < 80%", "< 1,000 new readings").
- **Rights edge.** Real but leaky. A lid seen in core from lapsed mining ground leads to a $1/ac/yr leftover lease, a nomination, or a private ranch heat option. This repeats the Blue Mountain pattern (the miner took non-competitive leases and sold them with the data) and the DAC pattern (Ormat read mining data "at no cost" and nominated in 2001), both from M18. The leak: public library core can be read by anyone, so the edge is speed, method and the company-yard NDAs.
- **Self-score:** model uncertainty alpha 3.5, rights alpha 3, buildability 4, cost/scale 4, moat 3. **Total 17.5/25.**

---

## 1. Physics case

### 1.1 Clay and alteration minerals are thermometers that stay behind

Hydrothermal clays form in a fixed order with temperature. In active fields (Browne 1978, Ann. Rev. Earth Planet. Sci. 6:229; Harvey and Browne 1991, Clays and Clay Minerals 39:614; from memory):

| Mineral or texture | Typical temperature | What it tells us |
|---|---|---|
| Smectite (Ca/Na montmorillonite) | below about 120-150 C | Low-T cap. The 1-10 ohm-m conductor in MT (M08). |
| Interlayered illite-smectite (I/S) | about 150-220 C | The cap base. Percent illite rises with T. |
| Illite, chlorite | above about 220 C | Reservoir, more resistive (20-100+ ohm-m). |
| Kaolinite, alunite, opal | below about 100-150 C, acid | Steam-heated zone above boiling. A vapour-cap clue. |
| Laumontite, wairakite (zeolites) | about 120-230 C | Fits the 120-180 C binary targets we sell. |
| Epidote | above about 240 C | Hot core, rare in Great Basin binaries. |
| Adularia, bladed calcite, lattice quartz | any T at boiling | Boiling horizon. A depth-pressure-temperature tie. |

**SWIR (1.0-2.5 um) separates these quickly.** Smectite has a deep 1,900 nm water band and a broad 2,200 nm Al-OH band. Illite has a sharp 2,200 nm band plus 2,350 and 2,440 nm features. The ratio of the 2,200 nm depth to the 1,900 nm depth (often called illite crystallinity or "spectral maturity") goes up as smectite turns to illite (Pontual et al., AusSpec G-Mex guides; Simpson and Rae 2018, Geothermics, on New Zealand fields; from memory). Kaolinite has a doublet at about 2,165/2,205 nm. Alunite has a 1,760 nm band. Carbonates have a 2,330-2,350 nm band. A portable spectrometer reads one point in about 1-2 s (from memory).

**Where it can fool us.** (a) Lake and playa clays in basin fill are smectite too. Lithology and depth context separate most of these. (b) Diagenetic illite in old sediments can look like hydrothermal illite. (c) The big one: **fossil systems**. The Great Basin is full of 15-40 Ma alteration. So the clay isograd tells us "this rock was once hot", not "this rock is hot now". Section 1.4 handles this.

### 1.2 Depth of sensitivity

Old mining core runs to 100-1,000 m. Oil and gas core and chips in Denver and the UGS store run deeper. That is the band where the model's lidded class hides: lids thicker than 200 m defeat 2 m probes and darts and are a known gap in the ranch-well sentinel (MODEL rank 3, M23). So core reads exactly where our cheap tools are blind. In the toy calc a hole that reaches the smectite-out depth fixes lid thickness to about +/-40-70 m against a prior SD of about 380 m. About 87% of lids in the toy fall within the reach of a 300-900 m hole (calc, `P29_calc.py`, section 3; the prior is our guess).

### 1.3 Magnetic susceptibility and gamma (cheap channels on the same sweep)

- **Susceptibility.** Hydrothermal fluids destroy magnetite. That is why magnetic lows sat on Don A. Campbell and Gabbs (M18). A KT-10 style meter along the core turns the aeromag low into a depth: where the magnetite went and how thick the bleached zone is.
- **Gamma (K, U, Th).** Adularia and illite add potassium. Heat production in uW/m^3 is A = rho (9.52 U + 2.56 Th + 3.48 K) x 1e-5, with rho in kg/m^3, U and Th in ppm and K in percent (Rybach 1988, in Handbook of Terrestrial Heat-Flow Density Determination; from memory). This feeds the conductive background (rank 7).

### 1.4 Live versus dead (the test that makes clay worth anything)

Three ties, each cheap once the core is on the table:

1. **Present temperature versus mineral temperature.** If an extracted log (ArchivePack plus GeoFM), a P07 puck, or a Sentinel profile shows T today near the I/S temperature at the same depth, the system is live. If T today is 60 C below it, it is fossil. Rule of thumb: within about +/-25 C counts as consistent.
2. **Youngest fluid inclusions.** VeinTherm measures homogenisation temperature (Th) and ice-melting salinity on the youngest vein generation (the cross-cutting calcite or quartz). If Th sits on the boiling-point-for-depth curve at the present water table, the boiling horizon fits today's hydrology. A Miocene system that was eroded by hundreds of metres will plot off that curve. This is the method of "fluid inclusion stratigraphy" and Th-versus-present-T comparisons at Coso and The Geysers (Moore, Norman, Dilley and others, Stanford Geothermal Workshop and GRC papers 2000s; Moore et al. on Coso heating and cooling histories; from memory).
3. **Clay that is still out of balance.** Fresh, poorly ordered I/S next to hot fluid points to a system that is heating now. Well-ordered illite with chlorite overprint points to old, cooled ground (Harvey and Browne 1991; from memory, unverified as a general rule).

Toy numbers (calc, section 4; s = true positive rate on live, q = false positive rate on fossil or cold, all guesses): clay alone s 0.85 / q 0.45 gives LR 1.9. Add the present-T tie (s 0.75 / q 0.15) and LR is 9.4. Add young inclusions (s 0.6 / q 0.15) and LR is about 38. From a 10% prior that is P(live) about 0.8. The tests are not fully independent, so treat 38 as an upper bound. A realistic combined LR of 10-25 is still one of the strongest single-cell signals in the model.

### 1.5 ChipK: conductivity turns gradients into heat flow

Heat flow q = k dT/dz. The model now carries about +/-10-20% from k (M05). Conductivity can be measured on chips, not only on whole core (Sass, Lachenbruch and Munroe 1971, JGR 76:3391, "Thermal conductivity of rocks from measurements on fragments and its application to heat-flow determinations"; from memory). Options: a needle probe (TeKa TK04 type), an optical scanning unit (Popov / Lippmann TCS type) on slabbed core, or a home-built divided bar on chips in a water-saturated cell. Target error +/-5-8% per lithology. With porosity from the same sample, we can correct to in-situ saturated k.

### 1.6 Rosetta bench: resistivity and IP against T, salinity and clay

M08 asked for an explicit physics likelihood for MT conductors with false-positive classes (brine, lake clay, graphite, fossil cap). The Rosetta bench supplies it for Great Basin rocks:
- Measure complex conductivity (SIP, 1 mHz-10 kHz) on core plugs from 20-80 C (and to about 150 C in a sealed cell) at 3-4 fluid salinities.
- Measure cation exchange capacity (methylene blue; Lévy et al. 2018, JGR Solid Earth, on Icelandic smectite and conductivity; from memory) and SWIR clay index on the same plug.
- Fit a Waxman-Smits / Revil type model: sigma = sigma_w phi^m + sigma_surface(CEC, T). Smectite has high CEC (about 80-120 meq/100 g) and a strong IP phase. Illite is about 10-40. Lake clay looks like smectite in DC resistivity but often differs in IP phase and its temperature slope (Revil and others, IP papers 2017-2019; from memory, unverified as a separator).
- The output is a lookup: given an MT or HTEM resistivity at depth, what is P(T > 150 C | lithology class, salinity)? That is the EM detector's s and q in the model.

### 1.7 ArchivePack: the paper that never got scanned

GeoFM Stage 0 assumes scans exist (M20: 2,002 NBMG well-log PDFs). Much does not exist as scans. Company mining files, driller notes, fiche at USGS and state offices, and paper logs in core boxes are still paper. ArchivePack is a portable overhead book scanner, a microfiche/film scanner and a roll scanner for long log strips, plus a barcode and photo workflow that ties every page to a hole ID and box. Pages go straight into the GeoFM extraction queue with provenance.

---

## 2. Prior art

| Who | What | Why we are different |
|---|---|---|
| CSIRO HyLogger and AuScope National Virtual Core Library (Australia) | Automated SWIR/TIR core scanning across state core libraries; hundreds of km scanned (from memory, unverified total) | Built for minerals mapping. It shows the method and throughput are mature. Nobody runs it in the US for heat. |
| Corescan, TerraCore, GeologicAI, Minalyze (commercial) | Hyperspectral imaging and XRF core scanning as a service, mostly at mine sites | Service is per metre to miners. They do not interpret for geothermal or pair with present-day T. Possible subcontractor. |
| USGS Earth MRI and the USGS spectroscopy lab | Hyperspectral of outcrop and some core for critical minerals (from memory) | Minerals focus. A possible data partner. |
| Fluid Inclusion Technologies (Tulsa) / FIS | Mass spec of inclusion volatiles on cuttings; geothermal use at Coso and Geysers (Dilley, Norman, Moore; from memory) | Used inside known fields. We use it as a live/dead screen on archive core in unknown ground. |
| Geothermal clay mapping in NZ, Iceland, Indonesia | XRD and SWIR clay logs, methylene blue in production wells (Harvey and Browne 1991; Mauriohooho et al. 2016 on methylene blue; Simpson and Rae 2018; from memory) | Done on new geothermal wells, not on old mining core. |
| ISOR / Iceland resistivity-clay work | Flóvenz et al. 1985 and 2005; Árnason; Lévy et al. 2018: conductivity tracks smectite, not T directly | Our Rosetta bench repeats this for Great Basin lithologies (carbonate, tuff, basin fill), which no one has published as a full table (my belief, unverified). |
| Ussher et al. 2000 (WGC), Cumming 2009 (Stanford) | Clay-cap conceptual model for MT | We turn it into a calibrated likelihood with Great Basin plugs. |
| Ormat at Don A. Campbell (M18) | Read mining data "at no cost", nominated in 2001 | The same move, done systematically across the whole archive. |
| Zanskar (M13, Z files) | ML on public layers, own wells, LBNL seismology | No sign of a core or archive physical-sample program (unverified). Gap is open now. |

---

## 3. v1 design

### 3.1 Platform
- **Vehicle.** A 20-24 ft enclosed cargo trailer with a 7 kW inverter generator plus a 10 kWh LiFePO4 bank and shore-power inlet (most libraries have outlets), climate control for the spectrometers, two roller-conveyor benches. Towed by a crew-cab pickup. Inside a library we unload benches onto their floor if allowed.
- **Footprint inside a library.** Two 2.4 m benches plus a cart, about 4 x 3 m.
- **Power.** CoreSweep about 400 W with halogen/ LED-SWIR illumination; ChipK about 150 W; Rosetta oven about 1 kW peak; ArchivePack about 200 W. Total under 2 kW running.
- **Comms.** Local NAS (20 TB). Starlink or cellular for nightly upload of compressed spectra and page images to the GeoFM queue. Raw data stays on encrypted drives until NDAs are clear.

### 3.2 CoreSweep (v1: point-SWIR robot, v2: line-scan camera)
- **Motion.** A 2.0 m x 1.0 m XY gantry (belt drive, NEMA 23 steppers, open-source controller) over a standard core box or chip tray. A tray sits on a roller conveyor and is pulled under the gantry, indexed by a barcode or QR label we print and stick on the box end.
- **Sensors on the gantry head.**
  - SWIR point spectrometer, 350-2,500 nm, contact probe (ASD TerraSpec Halo or Spectral Evolution oreXpress class). One reading every 5-10 cm, 1-2 s each. (v2: Specim SWIR line camera at about 1 mm pixels, if budget allows.)
  - Handheld-class magnetic susceptibility sensor (KT-10 type) on a spring arm, one reading per 10 cm.
  - Gamma: a 2 L NaI or BGO detector (RS-230 class) under the tray for 60 s per tray for K/U/Th. A tray-integrated count, not a per-cm log.
  - RGB line camera (industrial, 4k) plus a ring light for a core photo with depth scale.
  - Optional laser profiler for core recovery and fracture count (rank 2 helper).
- **Software.** Spectral feature fitting for 1,900/2,200/2,350/2,440 nm depths and positions; clay index; unmixing to smectite, I/S, illite, kaolinite, alunite, carbonate, zeolite, chlorite classes; a confidence score. Depth registration from box labels and run blocks. All output to a per-hole parquet table in the model's column format.
- **Dimensions and mass.** Gantry frame 2.4 x 1.3 x 0.8 m, about 60 kg, splits into two 30 kg pieces.
- **Throughput.** About 900-960 m/day core, 2,400 m/day chip trays (calc, section 1). The scan per tray is about 1 minute; pulling and re-shelving the tray is the bottleneck.

### 3.3 ArchivePack
- Overhead book scanner (A2/A3, 300-600 dpi) for files and notebooks.
- Microfiche/microfilm digital scanner.
- Roll-feed large-format scanner (about 36-44 in wide) for log strips and maps, if the custodian lets material leave the shelf; otherwise a copy stand with a 60 MP camera.
- Tablet app: hole ID, box, page, photo of the custodian's catalogue card; output to the GeoFM queue with provenance hashes.
- Rate: about 400-800 pages per hour on the book scanner (unverified).

### 3.4 ChipK
- Needle-probe conductivity meter with full-space and half-space probes (TK04 class) for core.
- A home-built divided-bar cell for chips (fused silica references, Peltier ends, 4 thermistors), saturated with water under vacuum. Several hours per sample batch, run unattended overnight.
- Porosity and density: a balance and a vacuum saturation jar (Archimedes method).
- Heat production from the gamma detector on CoreSweep, plus a 10% subsample to a commercial lab for U/Th/K by ICP-MS.

### 3.5 VeinTherm
- Transmitted-light petrographic microscope with long-working-distance objectives and a camera.
- Heating-freezing stage (Linkam THMS600 class, -196 to 600 C).
- Diamond saw and a doubly polished wafer service. In-house polishing for v1 is slow; outsource wafers to a thin-section lab at about $30-60 each (unverified), turnaround 1-2 weeks.
- Throughput: about 3-6 wafers a day, 20-40 inclusions per wafer. Only the 5% of samples where clay says "was hot" and a live test matters.

### 3.6 Rosetta bench
- Four-electrode SIP impedance analyser (Radic SIP-Fuchs or similar class) and plug holders.
- Coring drill press with a 25 mm diamond bit for plugs from archive core (with custodian permission; destructive sampling rules differ).
- Oven to 90 C for plugs at atmospheric pressure (v1), and a 150 C sealed pressure cell (v2).
- Three to four NaCl-NaHCO3 brines matched to Great Basin waters.
- Methylene blue CEC kit.
- Target: 200-400 plugs in year 1 across 8-10 lithology classes, each at 4 temperatures and 3 salinities.

### 3.7 Parts list and cost (all unverified)

| Item | Low $ | High $ |
|---|---|---|
| SWIR point spectrometer (TerraSpec Halo / oreXpress class) | 55,000 | 80,000 |
| SWIR line camera upgrade (v2, optional) | 0 | 120,000 |
| Gantry, conveyor, controller, barcode, RGB camera, lights | 8,000 | 15,000 |
| Magnetic susceptibility meter | 5,000 | 8,000 |
| Gamma spectrometer (BGO/NaI) | 15,000 | 25,000 |
| ArchivePack (book scanner, fiche scanner, copy stand camera, tablets) | 10,000 | 25,000 |
| ChipK (needle probe meter, divided bar build, balance, vacuum) | 25,000 | 45,000 |
| VeinTherm (microscope, Linkam stage, camera, saw) | 35,000 | 55,000 |
| Rosetta (SIP analyser, oven, pressure cell, drill press, CEC kit) | 30,000 | 55,000 |
| Trailer, generator, battery, climate, NAS, Starlink | 25,000 | 40,000 |
| **Total, all five benches without line camera** | **~208,000** | **~348,000** |
| **Lean v1 (CoreSweep point, ArchivePack, ChipK, trailer)** | **~110,000** | **~160,000** |

A cheaper path: rent the SWIR spectrometer for the first month (about $2-4k per week, unverified) and use university FI and SIP labs (UNR, U of Utah EGI) on a per-sample basis until volume justifies owning. That drops month-one capex to about $40-60k.

### 3.8 Crew and time per site
- **Crew.** Two people: a geologist-tech who runs CoreSweep and logs, and a tech who pulls boxes and runs ArchivePack. A third part-time person (petrologist, remote) does VeinTherm and Rosetta in a fixed home lab, not on the road.
- **Per library visit.** Setup half a day. Then a target list of 20-60 holes. At about 900 m/day, a 400 m hole is about half a day. A 10-day visit covers about 15-25 holes or 9 km of core, plus 5,000-10,000 pages of paper.
- **Per company yard.** One to three days, a single deposit, often 10-50 holes. Needs an NDA and a data-sharing deal (they get a free clay map useful for their own exploration).
- **Per year.** About 150 field days: about 110 km of core-equivalent and 50,000-150,000 pages.

### 3.9 Deployment and access
- Core libraries generally allow on-site examination by appointment and sometimes allow sampling with permission (unverified for each library). Many ask that analytical results be returned to the library (unverified). That makes library data semi-public after a lag, which matters for the moat (section 6).
- Company yards: access by NDA. The offer is a free hyperspectral clay map, which miners already pay $5-20/m for (unverified). In return we get the heat read and a first look at lapsed ground.
- No permits are needed. Nothing touches federal land. This is the cheapest legal footprint of any build.

---

## 4. How much it shrinks the model's uncertainties (estimates, untested)

Coverage matters. Only cells that have archive core benefit. I guess 5-15% of high-lambda Nevada cells and less elsewhere (unverified; see section 7 test 1). Numbers below are "in cored cells" unless marked regional.

| Rank | What P29 adds | Shrink |
|---|---|---|
| 1 Detection gap / occupancy (and the archive coverage kill gate) | A new, mostly independent detector (mineralogy) that sees the lidded class at 300-1,000 m. Two detectors on the same cells give the designed two-detector survey the model asks for. ArchivePack lifts the count of usable T(z) readings, which directly tests the "< 1,000 new readings" and "T(z) coverage < 80%" gates. | 10-25% regional on N; much larger in cored cells |
| 3 Hydrologic masking / lid thickness | Smectite-out depth and the bleached-magnetite zone give lid thickness to +/-40-70 m where a hole reaches it (toy calc, prior SD about 380 m). | 30-50% in cored cells |
| 5 Temperature at 0.5-2 km | Clay and zeolite geothermometers, FI Th and boiling horizons, tied to present-day T. Gives a ceiling and, if live, a +/-15-25 C estimate. | 20-35% in cored cells |
| 7 Conductive background and position error | ChipK k per lithology cuts the k term from about +/-15% to +/-5-8%. Gamma gives heat production. Core box labels and collar files tighten hole positions. | 40-60% of the k term; a small cut in position |
| 4 Sensor reliability s/q per mask class | Rosetta turns each MT/HTEM conductor into a physics likelihood with brine, lake clay and fossil-cap classes. Also provides labelled core from the 20/40 calibration systems. | 30-50% of the EM detector's s/q spread |
| 2 Permeability class | Fracture and vein density from the core image and laser profile; open-space textures. | 5-10% |
| 6 Upflow location | Little. Some help from the alteration zoning direction between nearby holes. | under 10% |

In VOI terms, rank 3 and the live/dead test have the largest effect, because they let a cold-at-200 m cell be split into "really cold" versus "lidded and hot below". That is the cell class where our other sensors are weakest and where competitors are most likely to pass.

---

## 5. Rights edge

- **The pattern.** A gold explorer cored a hole on BLM ground in 1985-2015. The claims lapsed. Core sits in Reno. CoreSweep plus a present-T tie shows a live smectite-to-illite cap at 350 m. That parcel is now either: (a) open for nomination at the next BLM competitive sale (leaks at nomination); (b) a parcel that already went through a sale unbid, so a noncompetitive lease at $1/ac/yr is available for a period (R02); or (c) private or patented ground, where a ranch heat option at $1-2/ac is the move (after the Stock-Raising Homestead screen).
- **Why it is better than desk ML.** It produces a physical, quotable proof ("mineral thermometer plus present-T tie at 350 m") that a buyer like Ormat can check against the same core. That raises the step-up at sale.
- **Leak and limits.** Library core is public to anyone who walks in. Results may need to be returned to the library. Company-yard work is private but gives the miner first look. The edge is speed (reading hundreds of holes a year for heat) and the live/dead method, not exclusivity of the rock.
- **Scale.** Toy archive arithmetic: about 80,000 Nevada mining holes since about 1985, about 30% with retained core or chips, about 300 m each, so maybe 7 M m (calc, section 5, unverified). One crew does about 110 km a year. So the archive is far from "too small", and the work can scale to 3-5 crews and then to Utah, Idaho, Oregon and the oil-core stores in Denver and Salt Lake.

---

## 6. Risks

1. **Fossil caps dominate.** Most Great Basin alteration is Miocene. Without a present-T tie, clay is a weak clue (LR about 2). The live/dead tests need a temperature source per hole, which may not exist.
2. **Coverage is patchy.** Libraries keep a small share of drilled core. Cored holes cluster in gold districts, which overlap only partly with high-lambda heat cells. If fewer than about 5% of top cells have core, the regional effect is small.
3. **Access and data return rules.** Custodians may refuse destructive sampling (plugs, wafers) or require public return of results, which weakens the moat.
4. **Core quality.** Old boxes are mixed, mislabelled, partly lost or sampled out. Depth registration may be poor.
5. **Throughput is handling-limited.** Without library staff and forklifts, real rates may be 300-500 m/day, giving $5-8/m.
6. **Lake clay and diagenetic illite** give false positives in basin fill.
7. **Rosetta transfer.** Lab plugs at small scale may not match field MT at 100 m scale (fracture and scale effects).
8. **Company NDAs** may restrict use of the read for land acquisition on adjacent ground.

---

## 7. First test (6-10 weeks, about $15-30k)

1. **Desk (weeks 0-3, about $2k).** Join the NBMG/USGS/UGS core catalogues (hole IDs, depths, coordinates) to the model's lambda map and to the 697 warm NDWR wells. Report the share of top-decile cells with any retained core or chips. Kill gate: under 3% of top-decile Nevada cells with core deeper than 200 m means P29 shrinks to a one-off calibration tool.
2. **Pilot week at the Reno library (weeks 4-8, about $15-25k with a rented spectrometer and borrowed gamma/KT-10).** Pull core from 5-10 holes near known blind systems first seen in mining holes (Blue Mountain, McGinness Hills, Don A. Campbell, Tungsten Mountain; M18), and from 10 holes in fossil epithermal districts and cold controls. Score blind (the analyst does not know which is which).
3. **Pass marks.** (a) The SWIR clay index tracks known present-day T within +/-25 C in at least 70% of live holes. (b) The combined live/dead test separates live from fossil at a likelihood ratio of at least 5. (c) Throughput at least 500 m/day. (d) ArchivePack recovers at least 200 new T-depth readings or temperature notes from paper in that week.
4. **Then.** Buy the spectrometer, build the gantry, and put one Rosetta batch (50 plugs from the calibration systems) through a university SIP lab.

---

## 8. Self-score

| Criterion | Score | Why |
|---|---|---|
| Model uncertainty alpha | 3.5 | Hits ranks 3, 5, 7 and 4 hard, and feeds rank 1 gates. Limited to cells with core. |
| Rights alpha | 3 | Clear Blue Mountain / DAC pattern, but library core is public and results may be returned. |
| Buildability | 4 | All parts are catalogue items. Lean v1 in 8-12 weeks with 2-3 people. |
| Cost / scale | 4 | About $1-3/m read, $110-350k capex, scales by adding crews; millions of metres available (unverified). |
| Moat | 3 | Method plus speed plus company-yard NDAs. Not exclusive rock. |
| **Total** | **17.5** | |

## Sources (from sibling files; no new web reads this slice)
- M18 blind case studies (Blue Mountain, DAC, McGinness, Tungsten Mountain; Faulds et al. 2019; Kraal et al. 2025) and URLs therein.
- M08 MT physics (Ussher et al. WGC 2000; Cumming 2009) and URLs therein.
- M20 NBMG NGDS counts. D06 mining assessment (NREL 2022; USGS core libraries; UGS core database). D07 scanned logs (BEG $10/log, https://www.beg.utexas.edu/).
- M23 Kimama smectite seal: Lachmar et al. 2017, Geothermal Energy 5:28, https://link.springer.com/10.1186/s40517-017-0086-8
- From memory (verify): Browne 1978; Harvey and Browne 1991; Sass, Lachenbruch and Munroe 1971; Rybach 1988; Lévy et al. 2018; Flóvenz et al. 1985/2005; Simpson and Rae 2018; Mauriohooho et al. 2016; Moore, Norman and Dilley fluid-inclusion stratigraphy papers; CSIRO HyLogger / AuScope NVCL.
