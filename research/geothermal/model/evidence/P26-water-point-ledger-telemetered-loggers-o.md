# P26: Water-Point Ledger (telemetered loggers on streams, springs and stock tanks for chloride-flux and diluted-leakage detection)

Date: 23 Oct 2026. Build candidate P26, model track. This builds on `M23` (four hydrologic masks; Cascades 1,050 MW advective heat, only ~240 MW via thermal springs, Ingebritsen and Mariner 2010; plume decay length L = rho·c·v·b·d/lambda, 3-30 km; "watershed tree" idea), `M07` (diluted leak tracers B, Li, Cl, SiO2, He), `M22` (He back-projection along heads), `P05` (pump-cycle mixing lines, irrigation water-quality report as a gift), `P01` (Ranch Well Sentinel), `../../../hardware/evidence/H06` (landman water-well visit) and `H13` (casual use under BLM IM 2026-024), and `MODEL.md` (SENTINEL-COX ranks). It does not repeat them. New here: (1) a three-tier design with a parts list, power, comms and crew time; (2) a detection-limit calculation for a nested stream-node pair (`P26_calc.py`, this folder); (3) how a catchment heat budget enters CREAM-COX as an *areal-integral* likelihood, which no other detector in the stack provides; (4) the rights path for each tier.

**Method note.** The shared web-search budget was used up before this slice ran. No searches or fetches worked. Sources below are ones already read in M23/M07/M22 (URLs checked there) plus papers and part prices I know from memory, marked (from memory, unverified). Calculation outputs are marked (calc).

---

## Bottom line

- **The idea is sound and is the only "integrating" detector in the stack.** Every other sensor (Sentinel, darts, E-MT, soil gas) asks "is there heat under this spot?". A stream node asks "how much deep fluid leaves this whole catchment?". Chloride is not lost to conduction, so it carries the signal past rain curtains and lateral outflow that blind every thermal sensor. USGS already uses this exact budget to weigh hidden heat (Cascades, Yellowstone, Long Valley). We would industrialise it, nest it, and make it continuous.
- **Detection limit (calc, `P26_calc.py`).** A nested node pair around a 100 km2 sub-catchment with 1.5 m3/s baseflow, 1.5 mg/L background Cl, 12 monthly grabs, and a deep end-member of 800 mg/L Cl at 180 C sees a hidden leak of about **0.4 MWth** (99% one-sided). A 50 km2 headwater sees ~0.2 MWth. A 1,000 km2 trunk node sees ~5 MWth. Low-Cl deep water (200 mg/L, typical of some Cascade and SRP-margin waters, unverified) raises the limit about 3-4x. For comparison, a commercial-size upflow usually loses several to tens of MWth naturally (unverified range). So at 50-150 km2 nesting, any system whose liquid outflow reaches the stream is detectable. The real limit is **capture**: does the outflow drain to this stream, or to a deep regional aquifer?
- **Cost (calc, unverified prices).** Tier 1 stream node: about **$19/km2/yr** at 100 km2 nesting, **$2/km2/yr** as a 1,000 km2 trunk screen. Tier 2 ranch spring: about **$40/km2/yr**. Tier 3 stock-tank inlet logger: about **$11/km2/yr**. This is the cheapest per-area detector in the stack and matches the brief's $1-150/km2/yr.
- **Model effect (estimate).** Strongest on **rank 1 (detection gap)** in rain-curtain and stream-drained provinces (Cascades, Idaho batholith, western Oregon, SRP margins with gaining streams): the catchment budget is a near-independent second detector with a high and *checkable* P_det, so it can narrow the N band there from 2-5x to about **1.5-2.5x**. Moderate on **rank 6 (upflow location)** via nesting plus DTS walk, down to a 0.2-1 km stream reach. Moderate on **rank 5 (T at depth)** via year-long mixing-line extrapolation at springs. Small on rank 3 (mask class) and rank 2. Weak in closed Great Basin basins, where there are few perennial streams; Tier 3 tanks are the only piece that works there.
- **Rights edge.** It names a drainage, then a spring, then parcels before anything is filed. In the Cascades and Idaho, much of the ground is private timberland or state endowment land, where heat rights are signed off-market (inference). The Tier 2 water-use record is a real gift to ranchers and gets us onto the land with the heat option in hand.
- **Self-score:** model uncertainty alpha 4, rights alpha 4, buildability 5, cost/scale 5, moat 3. **Total 21/25.**

---

## 1. Physics case

### 1.1 The chloride-inventory heat budget
Deep geothermal liquid is a Na-Cl water. Cold recharge in young volcanics has very little Cl (a few mg/L at most, mostly from rain and dust). When deep water leaks into a catchment, the extra Cl stays in solution all the way to the gauge. So:

- Hidden deep water flux (kg/s) = excess Cl flux (g/s) / deep Cl (g/kg).
- Hidden advective heat (W) = that flux x c_p x (T_reservoir - T_ambient).

T_reservoir comes from geothermometers on the most concentrated spring or well in the catchment, or from a mixing-line extrapolation (1.4). This is the method Ingebritsen, Sherrod and Mariner used in the Oregon Cascades, and Ingebritsen and Mariner 2010 used for the whole US arc (M23 F1). Fournier and others used river Cl flux for Yellowstone's total heat (from memory, unverified). The Long Valley USGS monitoring of Hot Creek Cl flux follows the same logic (from memory, unverified).

Key point: **heat diffuses away in 3-30 km (M23 F3), chloride does not.** Boron and lithium are also conservative in most streams. SiO2 is not (it is taken up by diatoms) but it helps at springs.

### 1.2 Detection limit (calc, `P26_calc.py`)
The noise has two parts.

1. **Measurement.** Baseflow discharge error ~7% (rated gauge or salt dilution), Cl error ~3% (ion chromatography), 12 grabs per year with seasonal autocorrelation (treated as ~4 independent samples).
2. **Background.** Rain and dust Cl. I assume 1.5 kg/ha/yr deposition known to +/-30% (unverified for each region; NADP wet deposition maps give it per site).

| Sub-catchment | Baseflow | Deep Cl | T_res | Cl limit | Deep water | Heat limit (99%) |
|---|---|---|---|---|---|---|
| 50 km2 | 0.5 m3/s | 800 mg/L | 180 C | 0.19 g/s | 0.24 kg/s | 0.17 MWth |
| 100 km2 | 1.5 m3/s | 800 mg/L | 180 C | 0.44 g/s | 0.54 kg/s | 0.39 MWth |
| 300 km2 | 5 m3/s | 800 mg/L | 180 C | 1.6 g/s | 2.0 kg/s | 1.4 MWth |
| 100 km2, dilute deep end | 1.5 m3/s | 200 mg/L | 150 C | 0.44 g/s | 2.2 kg/s | 1.3 MWth |
| 1,000 km2 trunk | 20 m3/s | 800 mg/L | 180 C | 6.0 g/s | 7.5 kg/s | 5.4 MWth |

With a lognormal natural-discharge prior for commercial systems (median 10 MWth, unverified) and 70% of the upflow heat leaving as liquid into the gauged stream, P_det is about 0.99 at a 100 km2 node and about 0.6 at a 1,000 km2 trunk node (calc). Read this as P_det *given capture*. The capture share is the main unknown, and it is a parameter the model learns from known systems (section 4).

### 1.3 Separating geothermal Cl from other Cl
False positives: road salt, evaporites, septic and feedlots, sea spray near the coast. Tracer ratios fix most of this:
- **B/Cl and Li/Cl** are high in geothermal water and low in road salt and evaporite brine (standard geochemistry, from memory).
- **Cl/Br** is ~250-300 in rain, higher (often >1,000) in halite-derived salt, and different again in geothermal fluids (from memory, unverified ranges).
- **Continuous EC + T** show whether the Cl excess is steady at baseflow (deep source) or tied to storms and snowmelt (surface source).
- **He at springs** (Tier 2): mantle He (R/Ra > ~1) is close to proof of a deep source (M22).

### 1.4 Year-long mixing lines at springs (Tier 2)
A warm spring is a mix of deep water and seasonally varying cold recharge. Over a year the cold share swings with snowmelt. Each sample is one point on a line in T-Cl, SiO2-Cl and enthalpy-Cl space. Twelve points spread by the season give a much better extrapolation to the deep end than one grab (same idea as P05 pump cycles, but nature does the pumping). Flow x (T - T_amb) from a flume gives the spring's advected heat directly. A diffusion sampler for He/Ne adds R/Ra and a He-excess that fixes the deep-water fraction independently of Cl.

### 1.5 Walking the anomaly upstream (Tier 1, follow-up)
Once a node pair shows excess, the source sits in a 50-150 km2 sub-catchment. Then:
- **EC/T synoptic walk**: a hand probe every 200-500 m along the stream on one baseflow day. Cl jumps at the inflow reach.
- **Fibre DTS**: 1-2 km of cable on the streambed for 2-7 days finds warm inflow points at about 1 m resolution, a well-known stream-groundwater method (Selker et al. 2006, from memory).
- **Streambed temperature rods** (Hatch/Constantz-type, 0.1-1 m): give vertical flux at the inflow, i.e. how much water comes up.
This narrows location to a 0.2-1 km reach. Then structural mapping, darts (P02), E-MT (P03) and soil gas (P25) take over.

### 1.6 Stock-tank inlet loggers (Tier 3)
Many BLM allotment tanks are fed by wells (solar or windmill pumps) or piped springs. The water at the inlet during pumping is aquifer water at well temperature. A T logger in the inlet stream, plus a cheap EC channel, gives a year of pumped-water temperature and salinity at a point no database has. A tank fed by a 100-200 m well that runs 3-6 C warmer than its neighbours is a warm well (M06-type signal) we would never otherwise find. Signal is coarse (no profile) but the density is high and the cost is near zero.

### 1.7 Where it works and where it does not
- **Works best:** rain-curtain provinces with gaining perennial streams (Oregon and Washington Cascades, Idaho batholith, Lassen-Shasta, the northern and southern SRP margins where canyons cut aquifers).
- **Medium:** Great Basin range-front springs (Tier 2) and allotment tanks (Tier 3).
- **Poor:** closed basins with no baseflow, and deep regional aquifers that drain to very large springs (e.g. Thousand Springs on the SRP, or Ash Meadows in the carbonate province), where dilution is huge. There, a regional budget gives only an upper bound.

---

## 2. Prior art

- **Ingebritsen and Mariner 2010**, Cascade arc hydrothermal heat discharge by Cl flux x geothermometer T: https://pubs.usgs.gov/publication/70037638 (read in M23).
- **Ingebritsen, Sherrod and Mariner 1989**, Science 243:1458, Oregon Cascades heat budget: https://pubs.usgs.gov/publication/70015370 ; and **USGS PP 1044-L**: https://pubs.usgs.gov/publication/pp1044L (read in M23).
- **Sorey and Ingebritsen 1984**, Lassen hydrothermal outflow, WRI 84-4278: https://pubs.usgs.gov/publication/wri844278 (read in M23).
- **Sorey et al. 1991**, Long Valley outflow model: https://openei.org/wiki/Conceptual_Model_At_Long_Valley_Caldera_Geothermal_Area_(Sorey,_Et_Al.,_1991) (read in M23).
- **USGS Yellowstone river chemistry and Cl flux monitoring**, using continuous specific conductance as a Cl proxy (Hurwitz, McCleskey and others, from memory, unverified).
- **Fournier 1989**, Annual Review of Earth and Planetary Sciences, Yellowstone heat from Cl flux (from memory, unverified).
- **Manga 1998 and Saar/Manga Cascades spring studies**, heat carried by cold springs in the Oregon Cascades (from memory, unverified).
- **Gardner and Solomon 2009**, WRR, passive diffusion sampler for dissolved noble gases (from memory, unverified).
- **Selker et al. 2006**, WRR, fibre DTS in streams (from memory, unverified).
- **USGS NWIS** continuous specific conductance (00095) and temperature (00010) at gauges: https://waterdata.usgs.gov ; **Water Quality Portal** Cl, B, Li: https://www.waterqualitydata.us (both listed in M23 datasets).
- **New Zealand Taupo Volcanic Zone** Cl-flux heat budgets of the Waikato River (from memory, unverified).

What is not done anywhere I know of: a nested, continuous, commercial network across many provinces, with the budget fed into a count model, and with the follow-up tied to rights.

---

## 3. Concrete v1 design

All three tiers write to one data system ("the Ledger"): site, time, T, EC, stage, grab chemistry, photos, landowner and tenure tag.

### 3.1 Tier 1: stream node (about $1,000-1,500 hardware, unverified)
| Part | Spec | Price (unverified) |
|---|---|---|
| T/EC/stage logger | Onset HOBO U24-001 class (EC 0-10,000 uS/cm) or an in-house board with a 4-electrode EC cell, a 0.05 C thermistor and a vented or absolute pressure sensor for stage | $300-600 |
| Barometric reference | one per 5-10 nodes, for stage | $250 |
| Housing | 50 mm PVC or steel stilling pipe, 1-1.5 m, perforated, bolted to a bridge pier or a T-post driven in the bed; anti-foul copper mesh on the EC cell | $40 |
| Telemetry hub | Iridium SBD modem (RockBLOCK 9603 class) or LoRa to a cellular gateway where coverage exists; daily 340-byte summary (mean, min, max EC/T/stage) | $250-350 + ~$15-25/mo (unverified) |
| Power | 5-10 W solar panel, 7 Ah LiFePO4, MPPT; the logger itself runs on its own lithium cell for years | $80 |
| Grab kit | 60 mL HDPE (anions), 60 mL acid-washed HDPE with HNO3 (cations, B, Li, SiO2), 0.45 um syringe filter, field EC/T pen | $10 per visit |
- **Siting.** At USGS gauges (discharge already published), at confluences, and at road crossings so that nodes nest: trunk at 500-2,000 km2, then sub-catchments of 50-150 km2.
- **Discharge at ungauged nodes.** Salt-dilution gauging on each visit (the EC logger records the salt slug; the same hardware does it) to build a stage-discharge rating.
- **Lab.** Cl, Br, SO4 by IC; B, Li, Na, K, Ca, Mg, SiO2 by ICP-OES; about $40-70 per sample at a commercial lab (unverified). Later an in-house IC.
- **Crew time.** Install 1.5-2 h per node (2 people). Monthly service 20-30 min per node (grab, salt-dilution, clean the cell); a route of 8-12 nodes per day.

### 3.2 Tier 2: ranch spring station (about $1,000-1,600, unverified)
| Part | Spec | Price (unverified) |
|---|---|---|
| Flume | Prefabricated 3-6 in Parshall or cutthroat flume, or a V-notch weir plate for small springs | $200-600 |
| T/EC/stage logger | same as Tier 1, in the flume stilling well | $300-600 |
| He/Ne diffusion sampler | copper tube with a gas-permeable membrane, left 1-2 weeks in the spring pool (Gardner-Solomon type), crimped and sent to a noble-gas lab | $50 hardware + $200-400 lab per sample (unverified) |
| Grab kit | as Tier 1, quarterly, plus one full geothermometer suite (Na, K, Ca, Mg, SiO2, B, Li, Cl, HCO3, d18O/dD) | $150-250 per full suite |
- **Data product for the rancher.** A year-long certified flow record (cfs and acre-feet), temperature and water quality. This is the evidence a rancher needs for a stockwater or irrigation beneficial-use claim, an adjudication or a change application (in OR, ID and NV the state engineer weighs measured use, from memory, unverified). Delivered free with the heat option.
- **Crew time.** Install 2-3 h (flume set in the channel, sandbagged or grouted). Quarterly service 30 min; the rancher can download with a phone app.

### 3.3 Tier 3: stock-tank inlet logger ($40-90, unverified)
| Part | Spec | Price (unverified) |
|---|---|---|
| T logger | waterproof 0.1-0.2 C logger (iButton DS1922L class or HOBO Pendant class), or an in-house board | $25-60 |
| EC add-on (optional) | two stainless electrodes + a small AC excitation board (in-house) | $15-25 |
| Mount | stainless hose clamp to the inlet pipe inside the float valve box, in the flow | $5 |
- Records every 15 min for 1-2 years. Pumping periods show as flat steps at well temperature.
- **Serviced by grazing permittees**, who already visit tanks weekly in the season. They swap or tap the logger once a year; we pay a stipend ($30-60 per tank per year, unverified) or give them a tank-level and pump alarm as a gift (the same board with a float switch and LoRa).
- **Crew time.** 10 minutes per tank to fit if we go; zero if the permittee fits it.

### 3.4 Data system
- Ledger database: each reading tagged with site, catchment polygon (NHDPlus HR), tenure (BLM, USFS, state, private parcel ID), and landowner contact.
- Nightly job: compute Cl flux per node from the EC-Cl regression (calibrated per node from grabs), the excess over upstream nodes and deposition, and the implied MWth with an error band. Push flags to CREAM-COX.

---

## 4. How it enters the model and what it shrinks

### 4.1 A new kind of likelihood: the catchment integral
CREAM-COX now has point likelihoods (each Sentinel or dart sees a cell). P26 adds an **areal-integral** term: for each sub-catchment k,

excess Cl flux_k ~ Normal( sum over sources i inside k of [ capture_i x m_i x Cl_deep_i ], sigma_k ).

- m_i is the source's natural liquid outflow, tied to its MWe through a size-to-discharge relation fit on known systems.
- capture_i (0-1) is the share of outflow that reaches this stream. It has a prior by mask class and aquifer type and is learned from known systems in gauged catchments (Breitenbush, Austin, Belknap and other Cascade springs in the Ingebritsen and Mariner data).
- sigma_k comes from section 1.2.

This term constrains the *count and size* of all sources in the catchment at once, no matter where they are inside it, and no matter how thick the cold lid is above them. Its misses (low capture) come from deep export to regional aquifers, which is a different failure from the thermal detectors' misses (local lids, sweep). That partial independence is what the "designed two-detector survey" in rank 1 needs.

### 4.2 Estimated shrink by rank (estimates, untested)
- **Rank 1, detection gap (2-5x on N).** In stream-drained rain-curtain provinces: about **40-60% narrower**, from 2-5x to roughly 1.5-2.5x, because the budget directly bounds total hidden outflow per catchment, and Ingebritsen and Mariner's ~810 MW of non-spring advective heat becomes allocatable to named sub-catchments. In Great Basin closed basins: about **5-15%** (Tier 2/3 only). West-wide weighted: roughly **20-30%** on the N band.
- **Rank 6, upflow location.** Nesting gives a 50-150 km2 box; the DTS and rod walk gives a 0.2-1 km reach; about a **30-50% cut** in footprint-location spread in drained provinces.
- **Rank 5, T at 0.5-2 km.** Year-long mixing-line geothermometry at Tier 2 springs: about **20-35% cut** in deep-end T spread at sampled springs versus one grab (by analogy with P05; unverified).
- **Rank 3, mask class.** Excess Cl with no surface heat flags "rain curtain or lateral outflow, not empty". About **10-20%** entropy cut at catchment level.
- **Rank 4, sensor reliability.** Gives an independent truth channel for calibrating Sentinel and dart s/q in drained provinces; small but useful.
- **Rank 2, permeability.** Small. Steady baseflow Cl flux implies a steady open path, a weak proxy (5-10%).
- **Regional total.** This is the cheapest way to move the Cascades, Idaho and SRP-margin share of the undiscovered MWe from "prior only" to "bounded by data". It also gives a hard check against USGS 2008 in those provinces without fitting to it (rule B).

---

## 5. Rights edge

- **Tier 1 is public-access work.** Loggers at bridges and public crossings; grabs are casual use (H13, IM 2026-024). On USFS land a stream logger may need a special-use permit or a researcher letter (unverified per forest); at USGS gauges, ask the local Water Science Center. Nothing is filed.
- **It names drainages first.** The excess shows up in our private data months before any public signal. Competitors who use NWIS see only the ~10% of nodes at USGS gauges, and mostly not their Cl.
- **Lockable land in the target provinces.** Western Oregon and Washington have large private timberlands; Idaho has state endowment land; SRP margins and eastern Oregon are mostly ranches. Private heat at ~$1-2/ac and state first-file both fit (inference, R05/R06).
- **Tier 2 opens ranch gates.** The free water-use record is a concrete gift tied to the visit where we sign the heat option (same play as H06/P01).
- **Tier 3 runs through permittees**, who often hold the private base property next to the allotment and know every well. It leads to private-parcel options and to leftover BLM noncompetitive parcels.
- Risk: once a catchment is flagged and we start a DTS walk on public land, people may see it. Keep the walk short and lock first.

---

## 6. Risks

1. **Capture is low in some places.** Deep outflow may go to regional aquifers or big springs, not the local stream (SRP, carbonate province). Then P_det falls a lot. Mitigation: learn capture from known systems before scaling.
2. **Dilute deep end-members.** Some Cascade and SRP deep waters are low-Cl (100-300 mg/L, unverified), which raises the heat limit 3-4x.
3. **Cl background is uncertain.** Deposition, dust and human Cl (roads, septic, irrigation return flow) can swamp small signals in farmed valleys. B/Cl, Li/Cl and Cl/Br help but do not always separate.
4. **EC fouling and ice.** Cells foul in summer and freeze in winter. Monthly cleaning and winter pull-outs at high sites.
5. **Vandalism and floods.** Bridge sites are visible; spring flood can take a node. Budget 10-20% loss per year (unverified).
6. **Telemetry.** Iridium costs add up; cell coverage is poor in the Cascades backcountry. Most nodes can log locally and send only a daily summary.
7. **Permits.** USFS special-use rules and state water-right rules on flumes in a channel vary (unverified).
8. **Low moat on method.** The Cl budget is USGS public method. The moat is the nested data, the capture priors learned from known systems, and the rights pipeline.
9. **Slow.** A full year is needed for mixing lines and seasonal baseline; the first catchment flags appear after 3-6 months of baseflow data.

---

## 7. First test (6 months, about $25-40k, unverified)

1. **Desk, weeks 0-4 (free).** Pull all NWIS and WQP Cl, B, Li, SC, discharge for Oregon/Washington Cascades and the SRP margins. Rebuild Ingebritsen and Mariner 2010 per catchment. Rank sub-catchments by "excess Cl not explained by known springs". This alone may name targets.
2. **Field calibration, months 1-6.** 20 Tier 1 nodes in two Oregon Cascade basins: one with a known thermal system (for example around Breitenbush or Austin Hot Springs) and one cold control. 5 Tier 2 stations on known warm springs. 50 Tier 3 loggers through 5-10 permittees in one Nevada or Idaho allotment area with known warm wells.
3. **Pass if:** (a) the known system's sub-catchment shows excess heat within a factor of 2 of the published spring-plus-diffuse discharge; (b) the cold control shows no excess above the 99% limit; (c) Tier 3 loggers flag the known warm wells with >= 80% hit rate and < 10% false alarms; (d) at least one unexplained excess shows up somewhere in the network.
4. **Kill or shrink if:** recovered heat is off by more than 3x on the known system, or the background noise limit is above 3 MWth at 100 km2. Then keep only Tier 2 springs as a Sentinel add-on.

---

## Sources

Read in earlier slices (URLs checked there): Ingebritsen and Mariner 2010 https://pubs.usgs.gov/publication/70037638 ; Ingebritsen, Sherrod and Mariner 1989 https://pubs.usgs.gov/publication/70015370 ; USGS PP 1044-L https://pubs.usgs.gov/publication/pp1044L ; Sorey and Ingebritsen 1984 https://pubs.usgs.gov/publication/wri844278 ; Sorey et al. 1991 https://openei.org/wiki/Conceptual_Model_At_Long_Valley_Caldera_Geothermal_Area_(Sorey,_Et_Al.,_1991) ; Lachmar et al. 2017 https://link.springer.com/10.1186/s40517-017-0086-8 ; NWIS https://waterdata.usgs.gov ; WQP https://www.waterqualitydata.us .

From memory, not checked in this slice (unverified): Fournier 1989 Yellowstone Cl-flux heat; USGS Yellowstone river SC-Cl monitoring (Hurwitz, McCleskey); Long Valley Hot Creek Cl-flux monitoring; Manga 1998 and Saar/Manga Oregon Cascades springs; Gardner and Solomon 2009 noble-gas diffusion sampler; Selker et al. 2006 stream DTS; Hatch et al. 2006 and Constantz streambed temperature methods; NADP Cl deposition; Taupo Volcanic Zone Waikato Cl budgets; all part and lab prices; state beneficial-use rules.

Toy calculation: `P26_calc.py` (this folder).
