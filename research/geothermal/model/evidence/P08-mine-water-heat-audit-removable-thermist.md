# P08: Mine-Water Heat Audit. Removable thermistor chains in mine piezometers, plus T/EC/flow loggers on dewatering lines

Date: 23 Oct 2026. Build candidate P08, model track. This builds on `../../evidence/A05-hidden-heat-in-mines.md` (NREL Mining G.O.L.D.: Meikle 330 F, 1,750 gpm per well, Florida Canyon 223 F at 160 gpm, Lihir, the 43 CFR 3204.12 claimant side door), `M20-tg-and-mining-holes.md` (NBMG borehole-temperature layer: 226 "mining" and 82 "dewater" wells, 41 of them at or above 50 C; Meikle rock 140-160 C; Eureka County dewatering wells at 50-60 C), `P07-drill-rig-ride-along-free-core-barrel-me.md` (grouted VW piezometers already carry thermistors; NAC 534 plugging; claimant carry), `P01` (the Sentinel drop probe), `P04` (the wellhead clamp error budget), `M23-hydrology-masking.md` and `../MODEL.md`. It does not repeat them.

**Method note.** The shared web-search budget for this workflow turn was used up before this agent's first query (all three searches were refused). So no new web sources were read this turn. Facts below come from sibling files that cite primary sources, plus what I know. Every number not traced to a sibling file or a named source is marked (unverified). Part prices are my own estimates from catalogue memory and are (unverified).

---

## Bottom line

- **What it is.** A partnership kit for operating mines that already pump hot water. Two parts. (1) A **removable thermistor chain** (and a one-pass drop-probe sweep) that goes down the open standpipe piezometers and monitoring wells a mine already owns. (2) **Clamp-on T, EC and pump-state loggers** on the dewatering wells and their discharge lines, joined to the mine's own flow-meter records. We add a cheap geochemistry bottle on the deepest dewatering wells. The mine gets a free 3D heat model it can use for ventilation, refrigeration, hot-inflow forecasting and dewatering design. We get a dense 3D temperature field with heads and known pumping, which no other site in the West gives us.
- **Why it matters to the model.** A mine dewatering field is a **giant, documented pumping test run inside a hot system**. Known pumping (Q at each well), dense heads, and dense temperatures let us solve the coupled flow-and-heat problem with far fewer unknowns than anywhere else. This is the best real-data setting for calibrating **plume back-projection (rank 6)**, the **mask-class reliability of every other sensor (rank 4)**, and the **permeability class (rank 2)**, because the flow per well is measured, not guessed. Deep dewatering wells (300-1,000 m) plus cation geothermometers attack **rank 5**.
- **Heat output as a lower bound.** The excess heat leaving in dewatering water, H = sum of m_i c (T_i - T_bg), is a hard lower bound on what the hidden system delivers to the mine's capture zone, once we split out the share that comes from draining stored warm water (section 1c). At Meikle-type numbers, one well at 1,750 gpm (about 110 kg/s) and 166 C carries about 70 MWth above a 15 C base. That is bankable flow data, not a proxy.
- **Rights edge: real but tricky.** Mines sit on claims, patented ground and railroad checkerboard. The upflow often sits off the claim block, on unleased BLM ground we can nominate. But the mine also holds the 3204.12 noncompetitive door, and our model would teach the mine where the heat is. So the contract must be a joint venture: we file through the mine's side door or nominate the off-claim ground, and the mine gets a carry and first offtake. A mine that buys the power raises the package price to Ormat or Fervo.
- **Scale check (not "too small").** There are about 20-40 large Nevada mines with dewatering or piezometer networks (unverified), each with 50-500 piezometers (unverified). That is 2,000-10,000 monitoring points, clustered in the gold belts. As a lease engine it is a wedge of hundreds of MWe (A05's estimate, unverified). As a calibration engine its value spills statewide, because each mine is a 3D "answer key" for one mask class.
- **Cost.** About $20-60k for the first mine, mostly reusable kit; about $10-25k per later mine (unverified). The hard part is the 2-4 month partnership and MSHA site training, not the hardware.
- **Self-scores:** model_uncertainty_alpha 4, rights_alpha 3, buildability 4, cost_scale 3, moat 3.

---

## 1. Physics

### 1a. What a piezometer temperature means

- **Open standpipe piezometers** (25-50 mm PVC or steel, screened over a short interval, open above) hold a water column that is mostly at rest. Away from the screen, the column water equilibrates with the rock through the casing in days to weeks. A thermistor chain in that column reads the formation temperature profile above the screen, with a small error from in-hole free convection.
- **Free convection noise.** In a 50 mm pipe with a gradient of 50-200 C/km, the Rayleigh number exceeds the onset value, and small convection cells add noise of about 0.01-0.1 C (standard result for small-bore wells, Gretener-type analysis; magnitude unverified for this exact geometry). That is tiny next to the signal: a blind upflow changes T by 5-60 C across a mine site.
- **Grouted vibrating-wire (VW) piezometers** already carry a thermistor at the tip (P07, Mikkelsen and Green 2003). Many mines have dozens to hundreds of them, read for years, with the temperature channel stored but unused (unverified). Typical VW thermistors are rated about +/-0.5 C absolute (unverified). So these are a free point-temperature dataset, and our chain gives the calibration to tie them in.
- **Dewatering wells.** Pumped water is a flow-weighted mix of the screened intervals (P04). The wellhead temperature is a lower bound on the hottest inflow zone, minus up-hole cooling. At 50-110 kg/s the up-hole cooling is under 1-2 C (calc: high flow, short transit). EC rises with deep, hot, older water and drops with recharge, so T and EC together split the mix into end-members.

### 1b. The coupled inversion (why a mine is special)

- Heat moves by conduction and by groundwater flow. Bredehoeft and Papadopulos (1965) showed that the curvature of a T(z) profile gives the vertical Peclet number, so the vertical flow rate. Anderson (2005) reviews heat as a groundwater tracer.
- In normal country, we see T but must guess the flow field. At a mine, the flow field is pinned by three things the mine already measures: pumping rates per well (reported to NDWR), heads in hundreds of piezometers, and a calibrated groundwater model (MODFLOW or FEFLOW) built for the permit.
- So the only big unknowns left are (i) the deep heat source geometry (where the upflow conduit enters), (ii) the conduit permeability, and (iii) the upflow rate and its temperature. With dense T and known flow, these are well posed. The forward model is MODFLOW 6 with heat transport (the USGS added a groundwater energy transport model, GWE, in recent MODFLOW 6 releases; release version unverified), or FEFLOW.
- **The dewatering transient is a free experiment.** As the cone of depression grows over years, warm water is pulled in from new directions. The way each piezometer's T changes over time, against the known Q history, tells which direction the hot water comes from. This is exactly the plume back-projection problem in rank 6, run with the answer partly known.

### 1c. Advected heat flux as a lower bound on output

- Excess heat in discharge: H_adv = sum over wells of m_i c_w (T_i - T_bg). Example (calc): 1,750 gpm = 110 kg/s; c_w = 4.2 kJ/kg/K; T = 166 C; T_bg = 15 C. H = 110 x 4.2 x 151 = about 70 MWth for one Meikle-type well. A Carlin-type field of 20 wells at 50-60 C and 1,000-3,000 gpm each (M20 temperatures; flows unverified) would carry about 100-400 MWth of excess heat.
- **The storage trap.** Much of that heat is not steady upflow. It is warm water and warm rock that were stored over thousands of years and are now being drained. Read naively, H_adv overstates the natural system.
- **How to split it.** Stored heat decays as the cone grows and the drained volume cools. Steady upflow heat stays flat or rises as the cone captures more of the conduit. So we fit H_adv(t) = H_up + H_store(t), with H_store following the drained-volume history from the mine's own model. Rock heat capacity sets the decay rate. A record of 5-20 years of pump logs (which mines must keep for NDWR) makes this fit tight (unverified on record quality).
- **Lower bound statement.** Even after removing storage, H_up is only the part of the upflow the mine captures. The true natural output is at least H_up. That is a clean, one-sided censored likelihood, which is exactly the form THERMOS-B already uses.
- **Link to MWe.** Natural-state heat output and power capacity are linked through recovery factor and conversion efficiency. For binary plants near 150 C, net conversion efficiency is about 10-12% (NREL GETEM range, unverified). A captured H_up of 50 MWth at 150 C is consistent with roughly 5-6 MWe from that flow alone, and the full system is larger. Meikle's NREL reference case is a 20 MW binary plant (A05).

### 1d. Detection limits (summary)

| Reading | Precision | What it detects |
|---|---|---|
| Removable chain in standpipe (our v1) | +/-0.02 C relative, +/-0.05 C absolute after bath calibration | Profile curvature (Peclet down to about 0.1-0.3), lid base, inflow zones |
| Drop-probe sweep (P01 Sentinel) | +/-0.01 C at 0.5 m steps | Same, one pass per hole, faster for 100+ holes |
| VW piezometer thermistor (mine-owned) | +/-0.5 C absolute (unverified), drifts | Point T in 3D, long time series |
| Wellhead clamp RTD on dewatering well | +/-0.2-0.5 C (P04 budget) | Mixed inflow T, transients |
| EC at sample tap | +/-1-2% | Mixing end-members, deep-water share |
| Cation and silica geothermometers | +/-10-25 C | Source temperature below the deepest well (rank 5) |
| H_adv after storage split | about +/-20-40% (unverified) | Lower bound on upflow heat output |

---

## 2. Prior art

- **NREL Mining G.O.L.D. (Levine, Rhodes and Kvien 2022).** Says miners should "collect temperature with depth surveys in dewatering wells prior to beginning operation" and "report fluid level and temperature" to NDWR. It notes miners are not required to report hot fluid. That is the gap this kit fills (A05).
- **Meikle hot ground.** Proulx and Scovira (2001) on drilling and blasting in hot ground; E&MJ reports 140-160 C rock and heavy refrigeration (M20). Mines already measure rock heat for safety, but the data stay in ventilation files.
- **Florida Canyon ORC (2013-14).** Two 50 kW units on 223 F water-supply wells. It proved the heat and died on operator change and scaling (A05). It also shows mines will host a geothermal pilot.
- **Lihir (PNG).** Pit depressurisation wells became a 50-56 MW plant. This is the strongest case for "mine dewatering field = geothermal well field" (A05).
- **Mine-water heat in cold districts** (Heerlen, Springhill, UK Coal Authority) use similar loggers but at 12-30 C, and are a different business (A05, rejected as "too small").
- **Heat as a tracer in hydrogeology.** Bredehoeft and Papadopulos 1965; Anderson 2005. Standard method, rarely applied to a dewatering field with known Q.
- **DTS fibre in boreholes** is common in hydrogeology and at Fervo (M32). It would work in piezometers too, but the readout costs tens of thousands of dollars (unverified), so it is a v2 option.
- **Person et al. 2008** model Great Basin geothermal systems as the hydrologic engines of Carlin and epithermal gold. So a gold mine is a natural place to find a live or fossil upflow.
- **What I did not find:** any published work that uses a mine's full piezometer and dewatering network to invert for a geothermal upflow, or any company offering a mine heat audit as a front end for geothermal leasing (as far as sibling files show; no new search possible this turn).

---

## 3. v1 design

### 3a. Sweep first, then leave chains

The fastest path is a two-step audit at each mine:

1. **Sweep (weeks 1-2).** Run the P01 Sentinel drop probe (0.01 C, 0.5 m steps, P and EC) down every accessible open standpipe and monitoring well. One profile takes 20-60 minutes, depending on depth. That gives a full T(z) in 50-150 holes per mine.
2. **Resident chains (months 1-6).** Leave removable chains in the 8-15 holes that carry the most information: the hottest, the ones on the edge of the thermal anomaly, and the ones whose T is changing with pumping. These capture the dewatering transient.
3. **Line loggers (months 1-6).** Put a clamp RTD and a pump-state sensor on every dewatering well, plus an EC/T sonde at 3-5 manifold sample taps.
4. **Geochem (week 2).** Take 10-20 samples from the deepest and hottest dewatering wells for cations, silica and He/Ne.

### 3b. Chain-R (the removable thermistor chain)

| Item | Spec | Cost (unverified) |
|---|---|---|
| Sensor nodes | 16-32 nodes. Each is a glass-bead NTC thermistor (calibrated to +/-0.02 C in a stirred bath against an SPRT) with a 24-bit ADC and a tiny MCU, potted in a 10 mm OD x 60 mm 316 stainless tube | $25-40 per node in parts |
| Node spacing | 5-20 m, set per hole. Tighter (2-5 m) near the screen and the expected lid base | n/a |
| Cable | 4-conductor, FEP or polyurethane jacket, Kevlar strength member, about 6 mm OD; digital RS-485 bus | $3-5 per m |
| Length | 100-600 m (v1 standard 300 m on a hand reel; long reels for deep holes) | n/a |
| Bottom weight | 1-2 kg stainless sinker bar, 20 mm OD (fits 25 mm pipes) | $50 |
| Temperature rating | v1 standard to 85 C; v1-HT to 150 C (high-temp thermistors, FEP, HT potting) for Meikle-type and Turquoise Ridge-type holes | +30-50% |
| Surface logger | Well-cap mount: MCU, SD card, 2 x D-cell lithium (12-18 months at 15-min sampling), barometer | $150-250 |
| Comms | LoRaWAN to one solar gateway per mine (or into the mine's own SCADA if allowed); cellular as fallback | $80 per node; gateway $500-1,000 |
| Total per chain | 300 m, 24 nodes | **about $1.5-3k parts; $2.5-4k built** |

- **Removable** means it hangs from a cap clamp, does not touch the screen, and comes out in 10-20 minutes on a hand reel. It moves to the next mine.
- **Clearance check.** Many piezometers have a pressure transducer or a VW sensor hanging inside. The chain is 10 mm OD and goes beside it in a 50 mm pipe, but not in a 25 mm pipe that already has a transducer (then we use the sweep only).

### 3c. Line-Q (dewatering line kit)

| Item | Spec | Cost (unverified) |
|---|---|---|
| Clamp RTD | Pt1000 class A, strapped to bare pipe under 25 mm closed-cell insulation, +/-0.2-0.5 C (P04 budget) | $60-100 |
| Pump-state | Split-core current clamp on the pump power lead (or the mine's VFD signal) | $40-80 |
| Logger + radio | Same board as Chain-R surface logger, LoRa | $200-300 |
| Flow | **Use the mine's own flow meters** (reported to NDWR). Add a clamp-on transit-time ultrasonic meter only on wells with no meter | $0 or rental $500/month |
| EC/T sonde | At 3-5 sample taps on the manifold: a commercial EC/T logger (In-Situ or Solinst class) | $1-2k each |
| Total per mine | 30 wells + 4 sondes | **about $15-20k** |

### 3d. Geochem bottle

- 250 ml HDPE (filtered, acidified) for cations and silica; a sealed copper tube or diffusion sampler for He/Ne (as in the Sentinel, MODEL.md rank 2).
- Lab cost about $150-300 per sample for cations and silica; He isotopes about $300-600 (unverified).

### 3e. Power, data and software

- Everything runs on lithium primary cells. No mains power, nothing to approve on the mine's power grid.
- Data go to a private cloud. The mine gets a dashboard and a monthly heat-model report.
- **Heat model build:** import the mine's groundwater model and pumping history; add heat transport (MODFLOW 6 GWE or FEFLOW); invert for source geometry and upflow with our Tier 1 GHOST simulator and an MCMC or ensemble Kalman step. About 3-6 weeks of one modeller for the first mine, about 1-2 weeks after.

### 3f. Crew time per site

| Step | Crew | Time |
|---|---|---|
| MSHA training (Part 46 surface or Part 48 underground; mine-specific hazard training) | 2 techs | 1-3 days once per mine (24 h new-miner training is a one-time cost per person; unverified hours) |
| Sweep of 100 piezometers | 2 techs, 1 truck, escort | 8-12 field days |
| Install 10 chains + 30 line loggers + gateway | 2 techs | 3-4 days |
| Geochem sampling | 1 tech | 1-2 days |
| Monthly check and download | 1 tech | 1 day per month |
| Pull-out at end | 2 techs | 1-2 days |
| **Total field time, first 6 months** | | **about 20-30 crew-days per mine** |

### 3g. Cost per mine (unverified)

| Line | First mine | Later mines |
|---|---|---|
| Chains (10, reusable) | $25-40k | $3-6k (wear, cable) |
| Line-Q kit | $15-20k | $5-10k (sondes reused) |
| Geochem | $4-8k | $4-8k |
| Field labour, travel, training | $15-25k | $10-15k |
| Modelling | $10-20k | $4-8k |
| **Total** | **about $70-110k with kit; $20-60k excluding reusable kit** | **about $25-45k** |

The brief's $20-60k per mine holds for later mines and excludes kit on the first.

---

## 4. Target mines (first list)

| Mine / area | Why | Status of heat (from sibling files) |
|---|---|---|
| Goldstrike / Meikle / Leeville (Carlin trend, NGM) | Hottest known Nevada mine; huge dewatering field; carbonate aquifer (mask class) | 140-160 C rock; 330 F water (A05, M20) |
| Gold Quarry, Carlin complex (NGM) | Dewatering field at 50-60 C (M20, Eureka County cluster) | Warm |
| Turquoise Ridge / Getchell (NGM) | Known hot underground mine (M20, Cassinerio and Muntean 2011) | Hot (degree unverified) |
| Florida Canyon (Pershing Co.) | 223 F water-supply wells; past ORC pilot; mid-tier owner, easier partner | 132 C by air lift (M20) |
| Round Mountain (Kinross) | Big pit, cold-control candidate or warm (unverified); Kinross is a mid-size partner | Unknown |
| Marigold, Phoenix, Cortez, Rochester, Hycroft | Large dewatering or monitoring networks; mix of warm and cold controls | Mostly unknown |
| Lithium: Thacker Pass (McDermitt caldera), Clayton Valley brine field (Silver Peak), Rhyolite Ridge | New mines with fresh baseline monitoring networks. Clayton Valley brine wells sit in a high-heat-flow basin (unverified temperatures). Brine operators also need T for brine chemistry | Unknown; worth a desk check |

- **Cold controls matter.** Rank 4 needs truth on cold sites as much as hot ones. Mines with big dewatering and no heat are perfect cold controls with dense data.

---

## 5. How it enters the model (SENTINEL-COX)

- **New THERMOS-B source class "mine 3D field".** A local 3D heat-and-flow inversion, not a 1D column. Its output, per mine, is a posterior over: upflow location (x, y), conduit width, upflow T, upflow rate, conduit permeability, and lid thickness. These collapse into the same latent variables the 1D column uses, so they plug into CREAM-COX as a "hard" local observation.
- **Calibration of the plume kernel (rank 6).** The model's outflow kernel uses L = rho c v b d / lambda along NDWR heads. At a mine we know v (from pumping and heads), b and d. So we can test the kernel shape directly, then fit its error model by mask class. The method: hold out 50% of the piezometers, back-project the upflow from the rest, and score the prediction against the held-out holes and the deep dewatering wells.
- **Reliability of other sensors (rank 4).** Each mine with a resolved 3D field is an answer key. We then run the cheap sensors (2 m probes, darts, ranch-well Sentinels, the clamp, E-MT) on the land around the mine and measure their hit rates against truth. This is the calibration campaign the model asks for, with 3D truth instead of a single TG hole.
- **Permeability class (rank 2).** Dewatering wells give measured flow per well and specific capacity at reservoir scale. A Meikle well at about 110 kg/s is well above the 40 kg/s "Limited Distributed" line. These are the only measured high-T flow rates outside geothermal fields. They feed the permeability prior for carbonate-hosted and fault-hosted systems.
- **Detection and masking (ranks 1 and 3).** Mines were placed for gold, not heat, and they cut through the lid. So "was this system visible from the surface before the mine?" is a clean test of P_det for that mask class. Few mines means a small sample, so the effect on rank 1 is modest.
- **Regional total.** The H_up lower bound per mine enters as a censored observation on the size of that system. It also tests the size-tail model (rank 8) a little.
- **GHOST Tier 1 job.** Before field spend, simulate a synthetic mine (pumping, cone growth, hidden upflow) and measure how far the dense data shrink each parameter. This confirms the EIG per dollar against the Sentinel.

---

## 6. How much it shrinks the ranked uncertainties (my estimates, untested)

Base case: 5 mines in year 1, 12-15 by year 2. Of these, about 3-6 are hot (blind or semi-blind upflow) and the rest are warm or cold controls.

| Rank | Uncertainty | Mechanism | Rough shrink |
|---|---|---|---|
| 6 | Upflow location and footprint | Dense 3D T + known flow lets us test back-projection on real data; kernel error model fitted by mask class | **40-60% of the kernel-parameter uncertainty in the carbonate and basin-fill mask classes**; upflow position error statewide from about +/-5-10 km toward +/-2-4 km where heads exist (on top of P04) |
| 2 | Permeability class / flow per well | Measured kg/s and specific capacity in hot rock; transient response in heads | **25-40%** on the permeability-class prior for fault- and carbonate-hosted systems; little for other classes |
| 4 | Sensor reliability s/q by mask class | 3D answer keys, with hot and cold controls, around which cheap sensors are scored | **20-30%**, mostly for the "carbonate lid" and "deep outflow" mask classes. Complements the 20/40 campaign rather than replacing it |
| 5 | T at 0.5-2 km | Deep dewatering wells (300-1,000 m), rock T in underground mines, geothermometers | **40-60% locally** at each mine; about 3-5% statewide |
| 3 | Masking / lid thickness | Lid base seen directly in 3D; carbonate cold-flow masking measured under pumping | **20-30%** for the carbonate mask class (the eastern carbonate province that MODEL.md expects to move up) |
| 1 | Detection gap | Few sites, but each is a clean "was it visible?" test | **5-10%** |
| 8 | Size tail | H_up lower bounds on a few blind systems | 5% |

- **Why rank 6 is the big win.** Today the back-projection rests on a kernel with no real-data test. One good mine is worth more than hundreds of scattered ranch wells for testing the kernel, because the flow field is known. The Tier 1 EIG pass should check this before the second mine.
- **Buyer metric.** The kit does little for the F5/F95 of the regional total by itself (few sites). Its value is in making every other sensor's reading trustworthy, so it raises the bits per visit of the whole Sentinel program.

---

## 7. Legal access

- **Access is by contract, not permit.** We work on the mine's private and claim ground as the mine's contractor or invitee. No BLM casual-use or NOI is needed for logging the mine's own wells, because the mine's plan of operations covers its monitoring network (inference).
- **MSHA.** Anyone on a mine site needs MSHA training (30 CFR Part 46 for surface, Part 48 for underground) and the mine's hazard training. The mine usually provides the site part. Plan on one-time training per person.
- **NDWR / NAC 534.** We place nothing permanent and drill nothing. A removable chain in an existing monitoring well is not a new well (inference; check with the State Engineer). The mine's pumping and water-level data are already reported to NDWR, and some are public.
- **Data ownership.** The mine owns its wells and data. The contract gives us a perpetual licence to use the data for geothermal, and the mine a licence to use our heat model for mining. Confidentiality both ways. Mines listed in the US or Canada may need to disclose material heat findings under S-K 1300 or NI 43-101 only if they bear on the mineral project (unverified), which they mostly do not.
- **Getting a yes.** Large operators (NGM) have strong hydro teams and slow legal; mid-tiers (Florida Canyon's operator, Kinross, SSR, i-80 Gold, lithium juniors) are faster. Start with a mid-tier. Expect 2-4 months per partnership and 40-70% refusal (unverified).

---

## 8. Rights edge

- **On federal land off the claims.** A mining claim conveys no heat right (30 USC 1022; R13). If the back-projected upflow sits on open BLM ground beyond the claim block, we nominate a padded block. If it goes unsold, we take it at $1/ac/yr (R02). Our 3D model is private, so nobody else knows where the conduit is.
- **On the claims.** The mine can take a noncompetitive lease through 43 CFR 3204.12 at $1/ac/yr. That is both the opportunity and the risk. The opportunity: we file it together, through their door, with no auction (the Blue Mountain precedent, A05). The risk: our audit tells the mine where the heat is, and it files alone.
- **The deal that solves it.** Before any data are collected, sign a geothermal JV letter: we hold operatorship and the right to flip the geothermal interest; the mine gets a 10-30% carry, a first right to buy power below its current cost, and the heat model for free. NREL shows mine-sited geothermal at $62-67/MWh against $109-185/MWh for remote diesel (A05), so the mine gains as an offtaker.
- **On private and patented ground.** Heat goes with the surface (NRS 534A.050). Sign a heat option or ROFR on the mine's private and checkerboard ground on day one, at $1-2/ac.
- **Package price.** A Carlin-trend resource with measured kg/s, a known lid, and a ready offtaker is worth more to Ormat or Fervo than a model-only prospect. A mine offtake contract can be the anchor of a PPA stack.
- **Weakness.** The number of mines is small, NGM is sophisticated and may already know its own heat, and Zanskar could pitch the same deal. So the rights edge is real but narrower than in the ranch and ride-along programs.

---

## 9. Risks

1. **Partnership friction.** Majors move slowly. Mines worry about third parties on site, safety, and their water-permit politics (the Humboldt River and Carlin dewatering are public issues). Mid-tiers first.
2. **Teaching the mine.** Without the JV letter signed first, the mine can use 3204.12 alone. Do not collect a single reading before the letter.
3. **Storage heat confusion.** Misreading drained stored heat as upflow would overstate the system. The time-split fit (1c) needs years of pump logs. If they are poor, report only a wide lower bound.
4. **Pumping disturbs the natural state.** Decades of dewatering have changed the thermal field. The inversion must model the history, which needs the mine's groundwater model. If the mine will not share it, the inversion is much weaker.
5. **Few sites, clustered.** The calibration covers the carbonate and gold-belt mask classes well and others badly. Results must carry a mask-class label and a covariate-shift penalty.
6. **Mine life and closure.** When a mine closes, pumping stops and recovery begins. That is actually a second free experiment (a recovery test), and dewatering wells could be handed over as geothermal wells instead of plugged (A05).
7. **Access to piezometers.** Some are in active pits, on benches, or blocked by transducers. Expect 50-70% to be usable (unverified).
8. **High temperatures.** Meikle-type holes need the 150 C variant. Scaling in discharge lines (the Florida Canyon lesson) can foul clamp readings only slightly, since the clamp is outside the pipe.

---

## 10. Cheapest first test

**Weeks 0-10, about $15-30k.**

1. **Desk (weeks 0-4, about $2-5k).** Pull public data first: NBMG borehole-temperature layer (226 mining + 82 dewater wells, M20), NDWR pumpage and water-level reports, NDEP and BLM monitoring reports (field T and EC are often recorded on every quarterly sample; unverified how often), and the hydrology chapters of BLM mine EIS documents. Build a "desk heat audit" for 5 mines with an LLM extraction pass. Rank mines by EVSI per dollar.
2. **GHOST in-silico (weeks 2-6, compute only).** Simulate one synthetic Carlin-type mine and estimate how far a 100-piezometer sweep shrinks the kernel parameters, versus 10 ranch-well Sentinels at the same cost.
3. **Pitch one mid-tier (weeks 2-10).** Florida Canyon's operator is the first target (proven 223 F water, past ORC pilot, smaller company). Ask first for the VW-piezometer thermistor records and pump logs: if they give them, the first 3D field is free.
4. **Pilot (once signed, 6 weeks, about $15-25k).** Sweep 30 piezometers, place 5 chains and 10 line loggers, take 10 geochem samples.

**Pre-registered pass rules:** (a) the back-projected upflow, fitted on 50% of holes, predicts held-out piezometer T within 2 C RMS; (b) the storage-split H_up has a 90% interval narrower than a factor of 3; (c) the mine signs the JV letter and heat ROFR. **Fail if** fewer than 30% of piezometers are usable, or the held-out RMS exceeds 5 C after the transient model.

---

## 11. Self-scores (1-5)

| Axis | Score | Why |
|---|---|---|
| model_uncertainty_alpha | 4 | Best real-data test of plume back-projection (rank 6); measured flow per well (rank 2); 3D answer keys for sensor reliability (rank 4). Few, clustered sites cap the statewide effect |
| rights_alpha | 3 | Off-claim upflow on open BLM land is nominable; claimant side door can be used jointly; mine offtake raises package price. But the mine holds its own door and can learn from us |
| buildability | 4 | Chains and loggers are simple, mostly off-the-shelf; 6-10 weeks to build v1. The gate is the 2-4 month partnership and MSHA training |
| cost_scale | 3 | $25-45k per later mine is cheap per bit, but only 20-40 candidate mines exist in Nevada |
| moat | 3 | Exclusive mine data deals and the calibrated kernel are hard to copy, but NGM could also deal with Zanskar, and the hardware is generic |

---

## Sources

- NREL (NLR), Levine, Rhodes and Kvien 2022, *Mining G.O.L.D.*, NREL/TP-6A20-81946 (Meikle, Florida Canyon, Lihir, recommendations, LCOE): https://docs.nlr.gov/docs/fy22osti/81946.pdf ; https://www.osti.gov/biblio/1855781 (via A05)
- E&MJ on Meikle hot rock and refrigeration: https://www.e-mj.com/?p=5358 (via M20)
- Cassinerio and Muntean 2011, Turquoise Ridge, GSN: https://nbmg.unr.edu/staff/pdfs/CassinerioMuntean_TurqRidge_GSN2011.pdf (via M20)
- NBMG borehole-temperature service (NV_Data/NVBoreholeTemperatures), queried in M20
- Person et al. 2008, Geosphere 4(5):888-917: https://doi.org/10.1130/GES00150.1 (via A05)
- Bredehoeft, J.D. and Papadopulos, I.S. 1965, Rates of vertical groundwater movement estimated from the Earth's thermal profile, Water Resources Research 1(2):325-328: https://doi.org/10.1029/WR001i002p00325 (from memory; DOI unverified)
- Anderson, M.P. 2005, Heat as a ground water tracer, Ground Water 43(6):951-968: https://doi.org/10.1111/j.1745-6584.2005.00052.x (from memory; DOI unverified)
- Mikkelsen, P.E. and Green, G.E. 2003, Piezometers in fully grouted boreholes, FMGM Oslo (via P07)
- USGS MODFLOW 6: https://www.usgs.gov/software/modflow-6-usgs-modular-hydrologic-model (GWE release details unverified)
- 30 USC 1003: https://www.law.cornell.edu/uscode/text/30/1003 ; 43 CFR 3204.12: https://www.law.cornell.edu/cfr/text/43/3204.12 ; 30 USC 1022 (via R13)
- MSHA training rules, 30 CFR Parts 46 and 48: https://www.ecfr.gov/current/title-30/chapter-I/subchapter-H (from memory; URL unverified)
- Sibling files: ../../evidence/A05-hidden-heat-in-mines.md, M20-tg-and-mining-holes.md, P01, P04, P07, M23-hydrology-masking.md, ../MODEL.md
