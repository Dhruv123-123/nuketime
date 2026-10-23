# P16: Slim-Hole Confirmation Package. Trailer injection and fall-off kit, plus a streaming-potential and microseismic carpet

Date: 23 Oct 2026. Build candidate P16, model track. This builds on `M30-permeability.md` (Libbey and Murphy 2026 classes and MPWPI bands; PI-to-MWe arithmetic), `M29-drilling-success-data.md` (Garg and Combs slim-hole scaling, Sandia slim-hole program), `M12-seismology.md`, `M08-magnetotellurics.md`, `P01` (Ranch Well Sentinel and tide logger), `P03` (DC-coupled E-MT node with SP channel), `P06` (tidal pressure array), `P07` (rig ride-along in mining core holes), `P10` (slickline trailer and memory gauges), `P11` (slim-hole wireline kit: straddle packer, heat-pulse flowmeter, A-DTS, televiewer), `../../evidence/B01-step-up.md` (Crump Geyser farm-in, Centaurus $5/MWh royalty), `../../../hardware/evidence/H13-permits-and-secrecy.md` (BLM IM 2026-024) and `../MODEL.md`. It does not repeat them.

**How P16 differs from P11.** P11 tests 1-3 m intervals and maps which fractures flow. It sees metres of rock around the hole. P16 runs one long, hole-scale test (hours of injection, then 12-48 h of fall-off) and reads the reservoir out to hundreds of metres or kilometres. Its product is not a fracture log. It is a **scaled full-size-well productivity index plus a footprint**, packaged for a buyer's data room. The two kits share a winch, gauges and packers, and should be built as one fleet.

**Method note.** The shared web-search budget for this workflow turn (200 calls) was used up before this agent's first query. All three searches were refused. No new web pages were read. Physics and prior art come from repo files (cited by file, with their URLs) and from standard literature I know; those items are marked (from memory, unverified). All prices are my own estimates (unverified). Numbers marked (calc) come from `P16_calc.py` in this folder.

---

## Bottom line

**Build it. It is the bank's "value step-up" tool, the one step that turns a hot slim hole into something a buyer will pay a carry for. Keep it lean and pair it with P11.** Four points:

1. **Injection, not discharge, is the right test in a slim hole.** A slim hole cannot flow at commercial rates. Wellbore friction and flashing choke it. Injection, followed by a pressure fall-off, gives the reservoir's injectivity and kh without those limits. Garg and Combs showed in the 1990s that slim-hole injectivity, corrected for hole radius, fluid viscosity and skin, predicts full-size well productivity at fields with liquid feed zones (Steamboat Hills NV; Oguni, Sumikawa and Kirishima in Japan; from memory, unverified; see M29). The radius correction itself is small: about 1.1x for an HQ hole against an 8.5 inch well (calc). The big corrections are viscosity (cold injected water is about 6x more viscous than 150 C water, calc) and skin. A well-designed fall-off handles both.
2. **It hits rank 2 directly.** The full-size PI of fields spans 0.5 to over 100 kg/s/bar. The top five Libbey fields sit above 60; the bottom five sit at 1 or less (M30, https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Libbey.pdf). At a 20 bar pump drawdown, PI 1 gives about 0.8 MWe per well, and PI 5 or more gives a pump-limited 4 MWe (calc). So the test answers the one question that decides whether a hot target is a project: is PI below about 2, or above about 5? A scaled PI with a factor-of-2 error answers that cleanly.
3. **The carpet turns one hole into a footprint, but only part of the time.** An SP electrode grid and 3C seismic nodes, laid out for the 2-4 days of the test, can show which way the injected pressure travels (SP) and, where the fault is critically stressed, where the pressure triggers tiny earthquakes (microseismic). The fall-off derivative gives distances to boundaries. Together these give a structure length and area. Honest catch (calc, section 1.6): SP and microseismic signals are strongest in the low-to-middle PI range. In a very permeable reservoir (PI 60) the injected pressure rise is only about 0.05 bar, so SP is small and few events trigger. There, the fall-off itself reaches 1-3 km (calc) and carries the footprint. The two halves cover each other.
4. **The kit itself is cheap. The cost is the hole and the permit.** Lean v1: about **$95-140k** (section 2, unverified prices). Per test: about **$10-22k** including node rental, water and a 3-person crew for 3-4 days (unverified). It works only where there is a hole that reaches warm, permeable rock: our own 300-1,500 m HQ/NQ core holes, partner and mining holes, and idle geothermal slim holes. On BLM land it is **not casual use** (section 5).

**Self-score:** model_uncertainty_alpha 4, rights_alpha 4, buildability 4, cost_scale 3, moat 3.

---

## 1. Physics

### 1.1 What the test measures

- **Step-rate injection (4-6 h).** We inject at 3-5 rising rates (for example 1, 2, 3, 4 kg/s for 1-1.5 h each) and log downhole pressure at the feed zone. The slope of rate against stabilised pressure is the **injectivity index (II, kg/s/bar)**. A break in slope marks fracture opening (the fracture-parting pressure, a direct stress reading: the minimum horizontal stress at that depth if the hole is in tight rock). That stress reading feeds the slip-tendency model in M30.
- **Constant-rate injection (6-12 h), then shut-in fall-off (12-48 h).** The fall-off is the clean part. No pump noise, no rate changes. Standard pressure-transient analysis (Bourdet derivative, type curves) gives:
  - **kh** (permeability times thickness) from the radial flow plateau.
  - **Skin**, which separates near-hole damage (drilling mud, cold) from the reservoir.
  - **Flow regime.** A half-slope derivative means flow into one dominant fracture. A quarter slope means a finite-conductivity fracture. A flat plateau means radial flow in distributed fractures. A late rise means a sealing boundary. A late fall means a constant-pressure boundary (a large, leaky reservoir or a recharge zone). These map onto Libbey's Discrete versus Distributed classes at reservoir scale, not at hole scale.
  - **Boundary distances** from the time each boundary shows up.
- **Composite (two-zone) model.** The injected cold water forms a cold bank around the hole. Early fall-off sees the cold bank; late fall-off sees the hot reservoir. A two-zone radial composite model, standard in geothermal well testing (from memory, unverified; Grant and Bixley, *Geothermal Reservoir Engineering*, 2011), gives the hot kh/mu directly. That is what the full-size producer will see.

### 1.2 Scaling slim-hole II to a full-size well PI (the Garg-Combs step)

- **Radius term.** Steady radial flow gives PI proportional to 1/(ln(re/rw) + s). For an HQ hole (rw about 48 mm) and an 8.5 inch production hole (rw about 108 mm) with re = 500 m and no skin, the ratio is **1.10** (calc). For NQ (rw about 38 mm), 1.12 (calc). If the big well is stimulated to skin -2, the ratio rises to 1.44 (calc). So hole size is a small correction.
- **Viscosity term.** Water at 15 C has about 6.2x the viscosity of water at 150 C, and 8.4x at 200 C (calc). If the cold bank dominates the measured II, raw II understates hot PI by up to that factor. The composite fall-off model removes most of this; a direct correction by the ratio of hot to cold mobility is the bound.
- **Flashing and two-phase.** Garg and Combs found the scaling holds for liquid feed zones and breaks where the feed zone flashes (from memory, unverified). Below about 180-200 C at the feed, with liquid static levels, as in nearly all Basin and Range blind targets, the liquid case applies.
- **Result.** A scaled PI with roughly a factor-of-2 (1 sigma, log10 SD about 0.2-0.3) error for the tested interval (estimate, unverified). The prior across fields spans more than two orders of magnitude (log10 SD about 0.6-0.7, estimate from Libbey's 0.5 to over 100 range).

### 1.3 How far the test sees

Radius of investigation, r = sqrt(4 D t), with D = k/(phi mu ct), using 150 C water, porosity 0.05 and total compressibility 1e-9 per Pa (calc):

| k (m2) | ~mD | 12 h | 48 h |
|---|---|---|---|
| 1e-15 | 1 | 137 m | 275 m |
| 1e-14 | 10 | 435 m | 869 m |
| 1e-13 | 100 | 1.4 km | 2.7 km |
| 1e-12 | 1,000 | 4.3 km | 8.7 km |

So in a commercial-grade reservoir (100 mD or more) a 48 h fall-off reads the rock 1-3 km out. That is the size of a whole Libbey "Discrete" system (0.5-2.5 km2). This is why the test is a footprint tool and not only a well tool: it sees boundaries at reservoir scale.

### 1.4 What the downhole gauge must resolve

At 3 kg/s, the pressure rise is 30 bar at PI 0.1, 3 bar at PI 1, 0.15 bar at PI 20, and only 0.05 bar at PI 60 (calc). A quartz gauge resolves about 0.0001 bar (from memory, unverified), so even PI 100 is measurable. But earth tides move confined-aquifer pressure by roughly 0.01-0.05 bar (unverified; see P06 and P01). In high-PI reservoirs the tide is as large as the test signal. **Fix:** log a barometer and a reference gauge for 2-4 days before the test (the P01 tide logger), fit the tidal response, and subtract it. That pre-test record also gives an independent tidal-transmissivity estimate (Hsieh et al. 1987, via M30).

Friction is not negligible. At 4 kg/s in a 60 mm string over 300 m, friction is about 0.9 bar (calc). So surface pressure is useless for high-PI holes. The gauge must sit at the feed zone below the packer.

### 1.5 Streaming potential (SP) carpet

- **Physics.** Water flowing through charged pore walls drags ions and makes a voltage. The voltage change is about C times the pressure change, where C is the electrokinetic coupling coefficient. C is roughly 1-20 mV per bar in fresh to brackish water and falls with salinity (Ishido and Mizutani 1981, JGR; Revil et al. 1999; from memory, unverified). Prior art: SP has been tracked during injection and stimulation at Soultz-sous-Forets (Marquis et al. 2002; Darnet et al. 2006, GRL) and during discharge tests in Japanese fields (Ishido and Pritchett; from memory, unverified).
- **Signal size.** At the source the voltage change is about 0.5-10 mV for a 0.5-10 bar change with C = 1 mV/bar, and 10-200 mV with C = 20 mV/bar (calc). At the surface the signal falls with depth. For feed zones above about 300-500 m it should read as a few mV over the structure. For deeper feeds the steel casing acts as a long electrode and carries the signal up to the wellhead. This "casing effect" is a known amplifier (Ishido and Pritchett 1999, JGR; from memory, unverified).
- **Noise.** Good lead/lead-chloride electrodes drift about 0.1-1 mV per day (Petiau 2000, from memory, unverified). Telluric noise is removed with a remote reference electrode pair and the P03 node's E-field record. The step-rate schedule helps: the on-off pattern repeats 4-6 times, so the signal can be stacked.
- **What it gives.** The direction and elongation of the SP change outline which way the pressure moves: along the fault (length), or into a broad aquifer (area). Stated as a probability, not a map.

### 1.6 Microseismic carpet

- **Physics.** Raising pore pressure on a critically stressed fault triggers small slips. Shapiro's seismogenic index gives the expected count: N(M >= m) = V x 10^(Sigma - b m), with V the injected volume and Sigma a site value, about -5 to 0 in published sites (Shapiro et al. 2010, The Leading Edge; from memory, unverified).
- **Expected counts for our test (V = 150 m3, b = 1, calc).** Sigma = -5: about 0.15 events above M -2 (so usually none). Sigma = -3: about 15 events above M -2 and 1.5 above M -1. Sigma = -1: about 1,500 above M -2 and 15 above M 0.
- **Detection.** 24-48 surface 3C 5 Hz nodes at 100-300 m spacing in a quiet desert should catch about M -1.5 to -1 within about 1 km (estimate, unverified). So in a moderately to highly critically stressed system we get 1-100 locatable events. Their spread traces the flowing structure, and focal mechanisms give the slip direction.
- **A blank is informative.** Zero events puts an upper bound on Sigma. Low Sigma means the fault is not critically stressed or is not hydraulically connected. In the Barton-Zoback-Moos picture (M30), that lowers the chance of a high-PI reservoir. So the carpet gives a label either way.
- **Bonus.** The same nodes run 2-4 days of ambient noise. That gives HVSR basin depth (rank 7) and natural microseismicity for the M12 large-N prior. The nodes earn their rental even with zero induced events.

### 1.7 Where the physics is weak

- **The hole must reach the reservoir.** In a 150-300 m gradient hole above a lid, the test measures the lid or outflow, not the upflow. The scaled PI then applies to the wrong layer. The best targets are 600-1,500 m HQ core holes that cut the fault at depth.
- **SP and microseismic are weak in very permeable rock** (small pressure change). The fall-off covers that case.
- **Cold-water thermal stress** can open fractures near the hole and inflate II (thermal stimulation). This is known from geothermal injection wells (unverified). The step-rate design and composite model flag it, but it biases II up by an uncertain amount.

---

## 2. Design: concrete v1

### 2.1 Deployment concept

One 20 ft tandem-axle trailer, towed by a 3/4-ton pickup, plus a 10-day node kit in the truck bed. Three people: a field engineer (test design and analysis), a technician (wireline, gauges, pump), and a local hand or the rancher (water supply, nodes). The hole is already drilled and cased to the top of the test interval.

### 2.2 Parts list (lean v1, all prices unverified estimates)

| Item | Spec | Est. cost |
|---|---|---|
| Trailer | 20 ft tandem flatbed, 7,000 kg GVWR, with toolbox and cover | $10-15k |
| Water storage | Two 20 m3 collapsible pillow tanks (bladders), plus transfer hoses | $5-8k |
| Feed | 3 inch trash pump (to fill from ranch well, stock tank or water truck) | $1.5k |
| Injection pump | Portable multistage centrifugal on VFD, about 0.5-5 kg/s at up to 20 bar | $10-16k |
| Gravity mode | Control valve only. Many Basin and Range holes have static water 50-200 m down, so gravity alone gives 5-20 bar of drive | (in plumbing) |
| Flow metering | Two battery-logging electromagnetic flow meters, 2 inch, 0.5% accuracy | $6-10k |
| Flow control | Motorised ball valve, PID controller, pressure relief, check valve, filter (to 25 micron) | $3-5k |
| Packer | Wireline-set or rod-set inflatable packer for HQ/NQ, rated about 200 C; shared with P11 | $10-20k |
| Wireline | Small electric winch, 1,500 m of 0.092 inch slickline, depth counter, mast; shared with P10/P11 | $15-25k (or $0 if shared) |
| Downhole gauges | Two quartz memory P-T gauges. One 177 C long-duration gauge (no dewar) for most holes; one 250 C gauge in a dewar for hot holes | $30-50k |
| Surface gauges | Two wellhead pressure transducers, barometer, water level logger, tide reference (from P01) | $2-3k |
| SP carpet | 48 lead/lead-chloride non-polarizing electrodes (built in-house) on 24 P03 E-field nodes (DC coupled), plus a remote reference pair 3-5 km out | $8-14k (electrodes $3-5k; nodes from P03) |
| Seismic carpet | 36 3C 5 Hz autonomous nodes, rented for the first 10 tests; buy at about 20 tests a year | rent about $3-6k per test; buy about $60-90k (later) |
| Power | 7 kW inverter generator plus a 5 kWh battery bank for quiet night operation (low seismic noise) | $6-9k |
| Comms | Starlink Mini for live upload of gauge-at-surface and flow data; LoRa heartbeat on nodes | $1-2k |
| Software | Own Python stack: Bourdet derivative, composite radial model, Bayesian inversion (PyMC or NumPyro), SP forward model, event picking (PhaseNet-type picker, open source). KAPPA Saphir licence later if buyers want it | $0-25k |
| **Total lean v1** | Sharing the winch and packer with P10/P11 | **about $95-140k** |
| Full v1 | Own winch, own seismic nodes | about $170-250k |

This matches the brief's $60-120k for the core kit only if the winch, packer and nodes are shared or rented.

### 2.3 Dimensions and weight

- Trailer bed 6.1 x 2.4 m. Dry weight loaded with pump, generator, winch, tanks empty: about 2,500-3,000 kg (estimate). Tanks are laid out on the ground, full weight about 20 t each, not carried.
- Downhole string below the packer: gauges about 1.5-2 m long, 32-45 mm OD, fit inside NQ (about 60 mm) and HQ (about 77 mm) holes.

### 2.4 Power

- Pump at 3 kg/s and 10 bar: about 3 kW hydraulic, about 4-5 kW electric. Generator covers it. In gravity mode, under 0.5 kW.
- Nodes run on their own batteries (10-30 days).

### 2.5 Test protocol and crew time per site

| Day | Work | Crew-hours |
|---|---|---|
| -3 to 0 | Barometer and tide reference gauge in the hole (P01 logger); lay SP electrodes and seismic nodes (24 SP + 36 seismic, about 1-1.5 km2 grid around the hole). Fill tanks | 2 people x 1 day = 16 |
| 1 morning | Set packer, run gauges to feed zone, wellhead plumbing, pressure test | 3 x 4 = 12 |
| 1 day | Step-rate injection, 4-5 steps x 1-1.5 h (about 54 m3 water, calc) | 3 x 7 = 21 |
| 1 night to 2 | Constant-rate injection 6-12 h (about 65-130 m3, calc) | 1-2 on watch = 12 |
| 2 to 4 | Shut-in fall-off 12-48 h. Nodes and SP keep running | Remote watch only = 4 |
| 4 | Pull gauges and packer; pick up carpet | 3 x 6 = 18 |
| **Total** | About 3.5-4.5 days on site; about **80-90 crew-hours**; 120-190 m3 of water | |

Analysis: about 2-3 analyst-days per test, producing a standard data-room package (section 4).

### 2.6 Water

The test needs about 120-190 m3 (32-50k gallons) (calc). Options, in order: a ranch irrigation well (30-60 L/s fills a tank in minutes); a stock well at about 1-2 L/s running for a day before the test; or 5-8 loads from a 4,000 gallon water truck (about $1-3k, unverified). Water must be clean (filtered) and similar in chemistry to formation water where possible, to avoid scaling or clay swelling that would raise skin.

### 2.7 Per-test cost (unverified)

| Item | Cost |
|---|---|
| Crew 3 people x 4.5 days, loaded | $5-8k |
| Seismic node rental | $3-6k |
| Water and trucking | $0.5-3k |
| Travel, fuel, consumables | $1-2k |
| Analysis (2-3 days) | $1.5-3k |
| **Total** | **about $11-22k** |

Excluded: the hole itself. Our own 600-1,500 m HQ core hole is about $0.3-1.2M (H11 and L16, unverified). The test adds 2-5% to that.

---

## 3. Prior art

- **Garg and Combs (1990s), slim-hole to full-size scaling** at Steamboat Hills and Japanese fields; Sandia's slim-hole program (Finger, Jacobson and others; Sandia Handbook of Best Practices for Geothermal Drilling, 2010) (via M29, from memory, unverified). This is the scientific base for the scaling claim.
- **Combs, Garg and Pritchett**, use of slim holes for small geothermal projects (from memory, unverified).
- **Standard geothermal well testing**: Grant and Bixley 2011; injection, completion and fall-off testing at every New Zealand, Icelandic and Kenyan field (from memory, unverified). Big operators run these tests on every new well; nobody runs them as a packaged, cheap product on slim holes for a lease bank.
- **Mining geotech Lugeon and packer tests** in core holes (P11). These are short and interval-scale, not reservoir-scale.
- **SP during injection**: Soultz (Marquis 2002; Darnet 2006), Japanese discharge tests (Ishido), Kakkonda (from memory, unverified).
- **Microseismic monitoring of injection**: Soultz, Basel, FORGE (L07), Desert Peak EGS. All are big, rig-scale programs, not a trailer kit.
- **Zanskar and Fervo** test their own wells, but use full-scale contractors. No public evidence of a dedicated slim-hole kit (unverified).

The novelty is not any single method. It is the package (cheap, repeatable, buyer-format output, carpet included) and the decision to run it on slim holes before any full-size well.

---

## 4. How much it shrinks the model's uncertainties

All numbers are rough estimates (unverified), to be checked with GHOST Tier 1 EIG.

| Rank | Today | With P16 at a tested prospect | Across untested cells |
|---|---|---|---|
| **2 Permeability class / flow per well (about 10x on MWe)** | PI prior spans 0.5 to over 100 kg/s/bar (log10 SD about 0.65); MWe spread about 10x at fixed heat | Hole reaches reservoir: scaled PI log10 SD about 0.2-0.3, MWe spread about **2-3x**. Shallow hole (lid/outflow only): about 4-5x. Class (Discrete / Distributed / Limited) from the derivative shape, entropy from about 1.9 to about 0.8-1.0 bits | Each test is a high-grade label tying surface proxies (structure, He R/Ra, specific capacity, tides, P11 fracture logs) to reservoir PI. 10-20 tests a year might cut the proxy-to-PI model error by 10-20% |
| **6 Upflow location and footprint area** | Area prior about 0.5 to over 20 km2 (factor 5-10) | Boundary distances from fall-off, plus SP elongation, plus event cloud: factor about **2-3** | Small directly; teaches the plume back-projection model how long structures run |
| **9 Recovery factor (scenario axis)** | Rg 0.08/0.16/0.25 spread, about 3x | Libbey RF tracks MPWPI, so a scaled PI moves RF prior to about 1.6-2x | Converts rank 9 to a data-driven prior at confirmed prospects |
| 5 Temperature at 0.5-2 km | | Feed-zone temperature from the gauge after recovery; minor | P10/P11 cover this |
| 7 Background and position | | HVSR from nodes | Minor |
| 4 Sensor reliability s/q | | Ground-truth flow class for the 20/40 calibration campaign, where holes exist | Moderate |

**Overall.** At a confirmed-hot prospect, P16 is the single strongest data step for rank 2 short of a full-size well. Compared with P11, it reads 100-1,000x more rock volume, so the representativeness problem in P11 section 4.1 is much smaller. Regionally its effect is small because it needs a hole. I estimate it narrows the regional F5/F95 band by about 5-10% in year one through labels (unverified), much more at the 10-20 prospects it tests. In VOI-Bank terms its EVSI per dollar is low at screening and highest at the top 1-3% of prospects, right before farm-out.

---

## 5. Rights edge and legal access

- **Not casual use on BLM land.** IM 2026-024 lists logging and "sampling existing wells without changing them" as casual use (H13, https://www.blm.gov/policy/im-2026-024). Injecting 100-200 m3 of water is a change to the hole and the aquifer. On federal land it needs a lease and a Sundry Notice or a Geothermal Drilling Permit amendment under the lease (43 CFR 3260 series, unverified detail). So P16 runs only on land we already hold.
- **Nevada.** Thermal gradient holes are permitted by NDOM under NAC 534A. Flow or injection testing likely needs the hole reclassified, or an observation or production well permit, and possibly NDEP UIC review (unverified). Water for the test may need a temporary waiver from NDWR (NRS 534, unverified). Plan: permit the test with the hole, not after.
- **Private (fee) land.** Easiest. Ranch consent plus state well rules. On fee land our heat option already covers testing (P01 option form should name injection testing explicitly).
- **Data confidentiality.** On a federal lease, test data is filed but held confidential while the lease is held (unverified). On fee land it is ours. The data room is a private asset.
- **The value step-up.** This is the core case. B01 shows confirmed resource without a PPA trades near zero (about $0.1M/MW), and the Crump Geyser farm-in happened only after slim holes plus a 5,000 ft well (B01, via R04). A buyer's main fear is a hot but tight resource (M30 item 6). A data room with a scaled PI, kh, skin, boundary distances, a class label and a footprint addresses that fear directly. Plausible terms (estimates, unverified): a **10-25% carried interest** or a **$2-5/MWh override** (Centaurus $5/MWh precedent, about $0.4M/MW PV, B01) instead of 2-5% for a heat-only prospect. The brief's 20-50% carry is plausible only when the slim hole hits reservoir temperature and a scaled PI above about 10; a buyer will still drill one full-size well before a PPA. Even so, a carry of 15% on a 30 MWe project at $0.4M/MW is about $1.8M per prospect, against about $1M of hole plus test. That is the step-up the bank was missing.
- **Speed.** P16 does not lock rights. It raises the value of rights already locked. It also kills bad prospects early, so we can drop BLM leases before rentals rise and stop carrying dead acres.

---

## 6. Risks

1. **Hole access.** The test needs a hole that reaches warm, permeable rock. Most legacy TG holes are 3/4-1 inch grouted pipe (P09) and cannot be tested. Most of our own 150-300 m holes sit in the lid. Real candidates are 600-1,500 m core holes, which cost $0.3-1.2M each.
2. **Permits.** Injection is outside casual use; NDOM, UIC and water permits add weeks to months (unverified).
3. **Scaling error.** Garg-Combs worked in liquid feed zones. Skin, thermal stimulation by cold water, and partial penetration can bias the scaled PI by 2-3x either way.
4. **Weak carpet signals.** SP needs a coupling coefficient that is not too low (saline fluids reduce it) and a feed zone that is not too deep. Microseismic needs a critically stressed, connected fault. Either may come back blank.
5. **High-PI test signal is tiny** (0.05 bar at PI 60). Earth tides and barometric noise must be removed with a pre-test record.
6. **Water.** 120-190 m3 in dry country. Ranch wells may be seasonal.
7. **Induced seismicity perception.** Even M -1 events need a plain-language plan for ranchers and BLM. The injected volume is tiny, so the felt-event risk is negligible (calc: N(M>=0) about 0-15 even at a high Sigma), but the plan matters.
8. **Buyers may not pay for it.** Some buyers will insist on their own full-size well. The data room then mainly saves our own capital by killing tight prospects. That still has value but a smaller one.
9. **Gauge temperature.** A 250 C memory gauge in a dewar holds temperature for hours, not days (estimate, unverified). For 48 h fall-offs in holes above about 180 C, use a surface-readout capillary tube or a fibre gauge instead, or shorten the test.

---

## 7. First test

**Desk, weeks 0-4, about $0-3k.**
1. Pull public slim-hole and full-size well test pairs: Sandia slim-hole reports, Steamboat Hills, NDOM well files and UIC injection permits (M30 item 25), and any fall-off data in the GDR (https://gdr.openei.org). Rebuild the Garg-Combs scaling with our own code and check that our composite-model inversion recovers full-size PI within a factor of 2 on at least 5 pairs.
2. Run GHOST Tier 1 for a synthetic blind system with three permeability classes. Simulate the step-rate plus fall-off, the SP response (coupling coefficients 1-20 mV/bar) and the seismogenic index range. Confirm the class is recoverable and compute EIG per dollar against P11 alone and P01 alone.

**Field, months 2-4, about $40-60k.**
3. Build the lean kit with shared winch and packer. Run it first on a cold, well-understood water well or a mining dewatering hole where the operator has its own pumping test data. Pass if our fall-off kh agrees with their pumping kh within a factor of 2, and the SP carpet shows a repeatable step signal above 1 mV.
4. Then run 2-3 tests in holes inside or next to a known producing field (a partner hole near Steamboat, Desert Peak, or a Japanese or Kenyan partner hole), where full-size PI is known. Pass if the scaled PI lands within a factor of 2-3 of the field's known well PI.

**Kill or rescope.** If scaled PI misses known well PI by more than 3x in 3 of 4 pairs, drop the PI claim and keep only the class label and footprint. If the carpet shows nothing in all 4 tests, drop the carpet and keep the fall-off.

---

## Sources

- Libbey and Murphy, SGW 2026, 40 analog fields, MPWPI and recovery factor: https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Libbey.pdf (via M30)
- NREL productivity benchmarks (via M30): https://docs.nlr.gov/docs/fy19osti/71833.pdf
- BLM IM 2026-024, casual use: https://www.blm.gov/policy/im-2026-024 (via H13)
- DOE Geothermal Data Repository: https://gdr.openei.org
- Garg and Combs slim-hole scaling; Sandia slim-hole program and handbook; Grant and Bixley 2011; Ishido and Mizutani 1981; Ishido and Pritchett 1999; Revil 1999; Marquis 2002; Darnet 2006; Petiau 2000; Shapiro 2010; Hsieh 1987. All from memory, not fetched this session (unverified).
- Calculations: `P16_calc.py` in this folder.
