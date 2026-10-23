# P30: Muon Well-Puck (wildcard). A borehole cosmic-muon density meter for sealed caps

Date: 23 Oct 2026. Build candidate P30, model track. It builds on `../../../hardware/evidence/H05-quantum-novel-sensors.md` (muons: TRL about 4, "density, shallow only"), `../../../hardware/evidence/H10-own-hardware-comps.md` (Ideon, KoBold muon patents), `../../../converge/gap_hunt_r3.md` (muon imaging killed as a standalone business), `M23-hydrology-masking.md`, `M30-permeability.md`, `P03` (E-MT node), `P11` (slim-hole wireline kit), `P16` (slim-hole confirmation package) and `../MODEL.md` (ranks 3 and 6). It does not repeat them.

**Method note.** The shared web-search budget for this workflow turn was used up before this agent ran. Both searches were refused. No new pages were read. Prior-art URLs below come from repo files already checked by earlier agents (marked "repo"). Physics comes from standard muon literature I know (marked "from memory, unverified"). All prices are my estimates (unverified). Numbers marked (calc) come from `P30_muon_calc.py` in this folder.

---

## Bottom line

**Build it later, as a small proving add-on, not now and not as a fleet.** It is a real, buildable instrument. It answers one question well that no other sensor in our stack answers: *is there a dense, self-sealed cap above this hole, how thick is it, and where does it end within about 150-350 m?* That is the geometry of the lid that makes a system blind, and where the lid breaks is often where the upflow leaks.

But four facts keep it small:

1. **It only works in holes we already control.** So it adds nothing to the land grab. Rights alpha is about zero. It is a tool for the 1-3 prospects we carry to confirmation.
2. **The sign of the density signal is ambiguous.** Silica or calcite sealing makes rock denser (+0.1 to +0.3 g/cc). Argillic (smectite) clay caps usually make it *lighter* (higher porosity, lower grain density) (from memory, unverified). So density alone does not say "cap". Paired with E-MT conductance (P03) it does: dense + resistive = silica/carbonate seal; light + conductive = clay cap; dense + conductive = rare, check brine. That pairing is the real product.
3. **Hot holes break plastic scintillator.** Standard polystyrene/PVT scintillator is rated to about 60-70 C, and SiPM dark noise doubles about every 8-10 C (from memory, unverified). A puck parked at 200 m in a real blind-system hole may sit at 60-120 C. v1 must be limited to holes below about 55 C at the parking depth (cold side of the lid, or outflow-side holes), or carry a dewar plus heat sink that buys days, not weeks. This is the biggest engineering risk and it was not in the brief.
4. **Count rates are fine at 100-300 m, poor below 400 m.** My estimate for a 1.2 m long, 11 cm wide puck is about 1,400 muons/day at 200 m and about 440/day at 300 m (calc). That is about 3x the brief's 300-500/day at 200 m; the difference is acceptance assumptions, so treat the truth as somewhere between. Four weeks at 200 m gives about 39,000 muons (calc), enough to see an 80 m cap with +0.2 g/cc at 3 sigma in about 36 direction bins.

**Self-scores (1-5):** model_uncertainty_alpha 2, rights_alpha 1, buildability 3, cost_scale 2, moat 2.

---

## 1. Physics: why it sees a sealed cap

### 1.1 What a muon meter measures
Cosmic muons lose energy at about 2 MeV per g/cm2 of rock. The number that reach a detector at depth falls steeply with the column of mass (the "opacity", in metres water equivalent, m.w.e.) along each direction. Count the muons arriving from each direction, compare with the flux expected for a flat model of known overburden, and you get the **average density along each ray**. This is the same principle as Alvarez's 1970 pyramid survey and Tanaka's volcano muography (from memory, unverified). In a borehole, the rays fan upward from the puck in a cone, so the puck "looks up" through the cap.

### 1.2 Flux versus depth (calc)
I used a Miyake-type depth-intensity relation, checked against the WIPP underground flux (about 1,600 m.w.e., about 4.8e-7 /cm2/s) to about 30% (from memory, unverified). Rock density 2.3 g/cc, zenith cut 70 degrees, puck 11 cm x 1.2 m:

| Puck depth (m) | Muons/day | Sensitivity d ln(N) / d ln(opacity) |
|---|---|---|
| 50 | about 32,000 | -1.8 |
| 100 | about 7,500 | -2.1 |
| 150 | about 2,900 | -2.3 |
| 200 | about 1,400 | -2.4 |
| 300 | about 440 | -2.7 |
| 500 | about 80 | -3.2 |

The sweet spot is 100-300 m. Deeper holes see more contrast per count but get too few counts.

### 1.3 Can it see the cap? (calc)
A cap of thickness t and contrast d-rho, inside overburden H of mean density 2.3, changes the counts along a ray by about 2.4 x (t x d-rho) / (H x 2.3).

| Case | Fractional count change | Muons per bin for 3 sigma |
|---|---|---|
| H=200 m, cap 80 m, +0.2 g/cc | 8.5% | about 1,260 |
| H=200 m, cap 40 m, +0.2 g/cc | 4.2% | about 5,000 |
| H=200 m, cap 80 m, +0.1 g/cc | 4.2% | about 5,000 |
| H=300 m, cap 100 m, +0.2 g/cc | 7.9% | about 1,450 |
| H=100 m, cap 40 m, +0.2 g/cc | 7.2% | about 1,700 |

So: a thick (more than about 60 m), strongly sealed cap is seen in each of about 30-36 direction bins in 4 weeks at 200 m. A thin or weak cap is seen only as a single whole-sky average, or needs 3-4 months or two pucks.

### 1.4 What it adds that the hole itself does not give
If we already drilled through the cap, we have cuttings, a gamma-gamma density log and T(z). Those see centimetres around the hole. The puck sees **sideways**: at 60 degrees zenith it reaches about 170 m out at a cap 100 m above the puck and about 350 m out at the surface (calc). So it maps cap **lateral extent and thinning** in a 300-700 m wide cone. A thinning or broken cap on one side points to the leak and the upflow (rank 6 bearing). A cap that is continuous in every direction says the lid is regional, and the system can be bigger than the shallow footprint suggests (rank 3).

### 1.5 Noise and systematics
- **Statistics** dominate for thin caps (above).
- **Overburden model.** Topography must be known to about 1 m (lidar or drone DEM, cheap). Unknown alluvium-over-bedrock depth is the largest systematic, because fill (about 1.9-2.2 g/cc) versus bedrock (about 2.5-2.7) is a bigger contrast than the cap. We must tie basin depth from gravity/HVSR (rank 7 work) or from the hole's own lithology log. Joint inversion with the gamma-gamma log and surface gravity is the honest fix.
- **Water table** barely matters: water in pores is already in the bulk density, and water in the hole is a pressure-housing issue only.
- **Temperature.** Covered in the bottom line. Dark noise is killed by requiring a coincidence across 3-4 layers, but light yield and scintillator softening are not.
- **Energy threshold.** Low-energy muons and soft electrons scatter; a thin lead or steel absorber between layers and a minimum track length cut handle this (from memory, unverified).

---

## 2. Prior art

- **PNNL borehole muon detector** for 4-D overburden density monitoring at CO2 storage sites (repo: https://www.pnnl.gov/publications/muon-borehole-detector-design-use-4-d-density-overburden-monitoring ; https://www.pnnl.gov/publications/muon-tomography-deep-reservoirs). Bonneville and co-authors described scintillator-bar, SiPM-read detectors sized for standard boreholes (about 10-15 cm), tested in a tunnel/mine setting (from memory, unverified details).
- **University of Utah** borehole detector work (repo: https://collections.lib.utah.edu/details?id=197735).
- **Ideon Technologies** (former CRM Geotomography, TRIUMF spin-out): commercial borehole muon detectors and inversion for mining to about 1 km; $16M Series A (repo: https://pulse2.com/mining-imaging-company-ideon-technologies-raises-16-million ; https://ideon.ai/ideon-technologies-launches/). Aug 2026 ARPA-E ROCKS project with Berkeley Lab on laser-plasma muon beams (repo: https://thequantuminsider.com/2026/08/21/berkeley-lab-led-project-secures-funding-to-develop-a-transportable-muon-imager/).
- **Geoptic and CGG**, borehole muon sensors for CCS since 2021, no commercial product yet (repo: https://offshore-mag.com/geosciences/article/14204226/cgg-geoptic-to-collaborate-on-carbon-capture-and-storage-monitoring).
- **Decision Sciences** MOU with KoBold Metals for mineral exploration (repo: https://www.businesswire.com/news/home/20241216673316/en/). KoBold holds compact muon detector patents (repo, H10).
- **Volcano and hydrothermal muography** (Tanaka at Asama, Showa-Shinzan, Satsuma-Iwojima; Lesparre, Jourde and others at La Soufriere de Guadeloupe showing low-density altered, water-rich zones) (from memory, unverified). This is the closest work to "hydrothermal alteration as density", but it is surface-based and looks sideways through mountains, not up from a hole.
- **I know of no published use of a borehole muon detector to map a geothermal cap in a blind Basin and Range system** (unverified). That is the gap. It is a small gap.
- **Competing density tools.** Borehole gravity meters (Micro-g LaCoste / Scintrex class) give a similar "apparent density" at radius of investigation of tens to hundreds of metres, but no direction (from memory, unverified). Surface gravity gives density with poor depth control. The puck's only edge is **direction**.

---

## 3. v1 design

### 3.1 Concept
A sealed stainless tube, 114 mm OD (fits 4.5-inch-plus casing and HQ/NQ-reamed holes larger than about 120 mm ID; does not fit 3/4-1 inch TG pipe, see P09), about 1.6 m long, lowered on a wireline to 50-300 m and left 2-8 weeks. Inside: a stack of scintillator layers that records each muon's direction. A surface box at the collar gives power, a clock and satellite comms.

### 3.2 Parts list (v1, per puck, unverified prices)

| Item | Spec | Est. cost |
|---|---|---|
| Plastic scintillator | 4 tracking planes, each two crossed layers of 10 mm x 10 mm bars, about 95 mm wide, plus a long axial bar bundle for side-entering tracks; total about 8-10 kg of PVT with WLS fibre readout (Eljen/Saint-Gobain/Chinese equivalent) | $3-6k |
| SiPMs | About 64-96 channels, 3 x 3 or 6 x 6 mm (onsemi/Hamamatsu class), plus temperature-compensated bias | $2-4k |
| Readout | CITIROC/PETsys-style ASIC or MAROC board, or 2-4 CAEN/open-source boards; FPGA coincidence logic; 10 ns timestamps; event rate is trivial (about 1 per minute) | $3-6k |
| Absorber | 2 x 10 mm steel or lead plates between planes, to drop soft particles | $0.3k |
| Pressure housing | 316 stainless, 114 mm OD, 6 mm wall, rated about 50 bar (500 m water), O-ring end caps, wireline bail | $2-4k |
| Internal sensors | Tilt and azimuth (MEMS 3-axis accel plus magnetometer; steel casing ruins the compass, so use a gyro-free method: orient by known-azimuth key on the rod, or a cheap north-finding fibre gyro rental) | $0.5-1.5k (key) or rental |
| Thermal | Thermistor, heater for cold holes; for warm holes an optional dewar flask plus about 3 kg phase-change sink (v2) | $0.5k (v1) |
| Cable | 4-conductor armoured wireline, 300 m, power plus RS-485 | $2-4k |
| Surface box | 100 W solar panel, 100 Ah LiFePO4, GNSS clock, Iridium/Starlink-mini or LoRa to a gateway, data logger (Raspberry Pi class) | $2-3k |
| Reference puck | A second identical puck read at the surface (open sky) at each site for flux normalisation, or one shared reference at base | shared |
| Assembly, test, calibration | Bench cosmic run, tunnel or mine-adit check against a known overburden | $3-8k |
| **Total per puck** | | **about $19-40k**, consistent with the brief's $15-40k. First unit about $40-60k with design time |

### 3.3 Power and comms
- Puck: about 2-4 W (SiPM bias, ASIC, FPGA, small computer in the surface box). Run on the cable from the surface box: about 70 Wh/day. A 100 W panel plus 100 Ah battery covers it in Nevada winter (unverified margin).
- Data: about 1,500 events/day x about 100 bytes = about 150 kB/day. A daily Iridium SBD summary (rates per bin, temperature, tilt) and a full download at retrieval. Raw events stay on an SD card in the puck as backup.

### 3.4 Deployment method and crew time
1. Pick a hole we control: our own 150-500 m slim hole (P16), a leased idle well, or a ranch well with no pump (pull the pump with P12 if the owner agrees). Check ID, temperature at the parking depth (first log with the P01/P11 kit), and no live flow.
2. Two people, one pickup with a small tripod and a hand or electric winch. Lower the puck to depth with a depth counter. Key its azimuth with a rod or record orientation.
3. Set the surface box, solar, and a fence panel. Log the collar with GNSS and fly a drone DEM of about 1 x 1 km if no lidar exists.
4. Leave 2-8 weeks. Remote check daily.
5. Retrieve: two people, half a day.

**Crew time per site:** about 1 day to set up (including DEM flight), about 0.5 day to retrieve, near zero in between. About 3 person-days per site, plus about 2-3 days of analyst time for the joint inversion.

### 3.5 Analysis
- Bin tracks by zenith and azimuth. Compare to the forward model: DEM + layered density (fill, cap, host) + the hole's own density log.
- Bayesian inversion for cap top, base, contrast and lateral edge, jointly with E-MT conductance (P03) and surface gravity. Report a posterior, not an image.
- Feed THERMOS-B as one more per-source likelihood on lid thickness and lid continuity, under the shared mask latent.

### 3.6 Build time
About 10-16 weeks for a 2-3 person team (one physicist/electronics, one mechanical, part-time analyst). Most parts are off the shelf; the readout and housing are the work. Licensing an Ideon or PNNL design, or buying a detector, could cut this to 4-8 weeks if they sell (unverified).

---

## 4. How much it shrinks the model's ranked uncertainties

| Rank | Effect | Rough size |
|---|---|---|
| 3 Hydrologic masking / lid thickness | Measures cap thickness and lateral continuity directly at one carried prospect, independent of water flow. Paired with E-MT it also gives the cap type (silica/carbonate vs clay). | At a carried prospect, maybe 20-40% narrower posterior on lid thickness and on "is the lid continuous over the target" (unverified). Regionally, near zero: it is one hole at a time, so only 1-3 prospects a year. A few such sites do help calibrate what E-MT conductance means for cap density, which spreads a little. |
| 6 Upflow location / footprint | Shows which side the cap thins or breaks, within about 150-350 m. That gives a bearing, not a location. | Small: maybe 10-20% on step-out direction at that prospect (unverified). |
| 4 Sensor reliability per mask class | If we park pucks in 2-4 of the 20 known blind calibration systems, it tells us which "lidded" systems have dense seals. That helps label the mask class. | Small, but it is a label nobody else has. |
| 5 Temperature at depth | None directly. A dense seal does imply a conductive lid, which makes T(z) extrapolation below it more trustworthy. | Very small. |
| 1, 2, 7, 8, 9 | None. | 0 |

**Net:** It improves *proving* confidence at a few carried prospects. It does not move the regional count N, the rights map, or the buyer metric (F5/F95 per 100 visits). The model's VOI-Bank should rank it below every Sentinel, dart and E-MT action per dollar, and above it only for the narrow question "do we spend $1-3M on the next confirmation hole here, or step out?".

**Value in money (rough).** If one puck deployment (about $10-15k all-in field cost) changes the step-out direction of one $1-3M confirmation hole with, say, a 10-20% chance of turning a dry hole into a hit, the EVSI is about $100-600k per carried prospect (unverified). That is a good ratio, but it only applies 1-3 times a year.

---

## 5. Rights edge

Weak, close to zero. It needs a hole, so we must already hold the land or the owner's permission. It finds nothing new to lock. Its only rights effect is indirect: a stronger proving package may raise the price or carry we get from Ormat or Fervo at farm-out. It also gives a story ("we know where the seal breaks") that helps sell a prospect, but buyers will re-drill anyway.

---

## 6. Cost and scale

- Per puck: about $19-40k (unverified). Two pucks plus spares: about $60-100k.
- Per site: about $10-15k field and analysis cost (3 person-days, travel, DEM, inversion), or about $30-60k if the hole has to be prepared or the pump pulled.
- Scale: 1-3 prospects per year, 1-2 holes each. That is $30-100k a year of use. Too small to be a business (gap_hunt_r3 agrees), fine as an internal proving tool.

---

## 7. Moat

Weak to medium. The hardware is copyable by Ideon (which already sells borehole detectors) or by Zanskar with a contractor. The only durable edge is the **joint E-MT plus muon cap-type library**: a few dozen holes where we know cap density, conductance and temperature together. That library makes our mask-class priors better than anyone else's, but it grows slowly.

---

## 8. Risks

1. **Hot holes.** Plastic scintillator and SiPMs degrade above about 55-60 C. Many interesting parking depths are hotter. Fix: limit to cooler holes, use a dewar for short runs, or test high-temperature scintillators (unverified options).
2. **Sign ambiguity.** Clay caps are light, silica caps are dense. Without E-MT the density alone can mislead.
3. **Overburden model error.** Fill versus bedrock depth can swamp a 0.2 g/cc cap signal. Needs gravity/HVSR and the hole log.
4. **Hole access.** Few idle, wide, uncased-or-steel-cased holes exist on our prospects. TG holes are too narrow (P09). We may need our own P16 hole, which already gives most of the answer.
5. **Slow.** 2-8 weeks per site. Fine for carried prospects, useless for screening.
6. **Redundancy.** A borehole gravity log or a P11 slim-hole kit plus E-MT may answer the same "is there a sealed lid" question at lower cost. The puck must beat them on lateral extent to earn its place.
7. **Count rate uncertainty.** My estimate (about 1,400/day at 200 m) and the brief's (300-500/day) differ by about 3x. If the low end is right, 8 weeks, not 4, is needed for the same result.

---

## 9. First test

**Desk, weeks 0-3, about $0-2k.** Run `P30_muon_calc.py` against GHOST Tier 1 synthetic columns: put a 40-120 m cap of +0.1 to +0.3 g/cc (and a -0.2 clay cap) over 2-3 known blind-system geometries (Blue Mountain, McGinness Hills, a Granite Springs-like outflow case). Compute EIG on lid thickness per dollar versus E-MT alone, borehole gravity alone, and E-MT plus puck. **Kill rule:** if E-MT plus puck does not beat E-MT plus borehole gravity on lid-continuity EIG by at least 1.5x, drop the puck.

**Bench, weeks 4-14, about $40-60k.** Build one puck. Calibrate it at the surface, then in a mine adit or tunnel with known overburden (a Nevada mine via the P07/P08 relationships). Pass if the measured opacity matches the known rock column to within 5% in 2 weeks.

**Field, one carried prospect.** Park it at 150-250 m in our own P16 hole, on the cold side of the lid, alongside an E-MT carpet. Pass if the cap thickness from muons agrees with the drilled thickness to within 25% and gives a lateral edge that the next step-out hole can test.

---

## Sources
- Repo, prior work: `../../../hardware/evidence/H05-quantum-novel-sensors.md`, `../../../hardware/evidence/H10-own-hardware-comps.md`, `../../../converge/gap_hunt_r3.md`, `../MODEL.md`, `P03`, `P09`, `P11`, `P16`.
- https://www.pnnl.gov/publications/muon-borehole-detector-design-use-4-d-density-overburden-monitoring (repo)
- https://www.pnnl.gov/publications/muon-tomography-deep-reservoirs (repo)
- https://collections.lib.utah.edu/details?id=197735 (repo)
- https://ideon.ai/ideon-technologies-launches/ (repo)
- https://pulse2.com/mining-imaging-company-ideon-technologies-raises-16-million (repo)
- https://thequantuminsider.com/2026/08/21/berkeley-lab-led-project-secures-funding-to-develop-a-transportable-muon-imager/ (repo)
- https://offshore-mag.com/geosciences/article/14204226/cgg-geoptic-to-collaborate-on-carbon-capture-and-storage-monitoring (repo)
- https://www.businesswire.com/news/home/20241216673316/en/ (repo)
- Muon depth-intensity relation, scintillator temperature limits, volcano muography (Tanaka; Lesparre/Jourde), Alvarez 1970: from memory, unverified.
