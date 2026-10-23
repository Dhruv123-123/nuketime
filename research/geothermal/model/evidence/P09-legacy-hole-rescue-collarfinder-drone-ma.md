# P09: Legacy Hole Rescue. CollarFinder (find the old steel collar) plus Needle Logger (re-log the open pipe)

Date: 23 Oct 2026. Build candidate P09, model track. This builds on `M20-tg-and-mining-holes.md` (442 NBMG TG boreholes with scanned logs, 0 LAS; OFR 99-425's 786 holes; the "re-entry logger" idea in its sensor section), `M19-labels-and-negatives.md` (CalGEM 2,008 TG holes with 1,586 plugged, 92 active, 30 idle, 138 unknown; NDOM TG 122 expired, 70 P&A, 55 in use; "share of negatives that are masked positives" as a top unknown), `../../evidence/L16-gtc-holes.md`, `../../../hardware/evidence/H02-existing-well-logging.md` (plugged wells need a rig, only open holes count), `../../../hardware/evidence/H05-quantum-novel-sensors.md` (MagArrow about 1 kg, price quote-only), `../../../hardware/evidence/H13-permits-and-secrecy.md` (BLM IM 2026-024 casual use includes "sampling existing wells without changing them" and drone surveys), `P01` (the 11-12 mm string that fits a 3/4" tube), `P02` (darts), `P03` (E-MT node) and `../MODEL.md`. It does not repeat them.

**Method note.** The shared web-search budget for this workflow turn was used up before this agent started. All 3 searches I tried were refused. So no new web pages were read. Sources are repo files (which carry URLs) or standard literature I know, marked (from memory, unverified). All prices are my estimates (unverified). Numbers marked (calc) come from my own script, `P09_calc.py`, in this folder.

## Bottom line

Build it, with three changes to the brief.

1. **Do not fly blind grids. Cue the drone with old air photos.** A drone magnetometer needs to fly about 3-5 m above the ground to see a 3/4-1 inch pipe (calc: 3-50 nT at 5 m, below 1 nT at 20 m for induced-only magnetization). At 5 m line spacing, one full TRS section (1.6 x 1.6 km) is about 31 flight hours (calc). That is not a product. But desert drill pads and two-track roads from 1975-85 stay visible for decades. So step 1 is a desk step: AI finds the pad on 1980s USGS single-frame air photos and on modern NAIP, inside the TRS box that GeoFM extracted. Then the drone flies a 60 x 60 m box around each pad (about 3-5 minutes of flight, calc), and a handheld magnetic locator finishes the job to about 1 m. This turns a ±400-800 m location into ±1-5 m for about 1 crew-hour per hole.
2. **The small pipe is a physics gift, not a limit.** Free convection in a water-filled pipe starts only when the gradient beats a critical value that scales as 1/r^4. For a 3/4" pipe (20.9 mm ID) at 20 C that is about 1,230 C/km. For 1" pipe it is about 470 C/km. For a normal 4" well it is about 2 C/km (calc). Basin and Range gradients are 30-300 C/km. So the old TG pipes are free of the convection noise that ruins most water-well logs. A 0.005 C probe in them can read real profile curvature. That is why these holes are worth the trouble.
3. **"Plugged" does not mean useless, and "open" is the only thing we log.** A plugged hole cannot be re-entered without a permit and a small rig (H02). But a found collar still (a) fixes the archive location for the model (rank 7) and (b) lets a 2 m probe or a P02 dart sit right beside the old hole as an absolute-temperature tie for the scanned log. So every located collar pays, and every open pipe pays more.

v1 total kit: **about $38-55k** (DIY magnetometer path) or **$60-85k** (commercial drone mag path), plus a rented UTV. Crew of 2. About **1.5-4 crew-hours per hole** and **$400-900 per hole in clustered prospects**, **$1.5-3k for isolated holes**. Build time about **8-12 weeks**.

The prize is not the hole count. It is a **designed truth set**: a few hundred equilibrated, 40-year-later profiles on holes whose 1980 log the GeoFM pipeline also reads. Each one scores the extraction (rank 4), says whether an old "negative" was masked (ranks 1 and 3), gives an accurate deep gradient (rank 5) and fixes position (rank 7). The 40-year gap also gives a unique time-lapse: if pumping or climate has changed the shallow flow, the profile shape changed, and that change measures advection directly.

## 1. Physics case

### 1a. Why an old TG pipe can reveal a blind upflow

- **Fully equilibrated.** Most 1970s-80s TG logs were taken days to weeks after drilling. Drilling disturbance decays roughly as ln(1 + s/t), where s is circulation time and t is time since. At t = 40 years and s = 1-3 days the residue is far below 0.001 C (standard Bullard/Lachenbruch-Brewer result, from memory). So the new log is the true rock profile. The old log was often 0.1-1 C off near the bottom (M20 F7 estimate).
- **Profile shape is the blind-system signal.** A cold isothermal top over a steep bottom (lid), a reversal (lateral outflow nearby), a convex-up shape (upflow in the hole) all show in curvature, not in the one straight-line gradient that OFR 99-425 and the NBMG tables report. Bredehoeft and Papadopulos (1965) type curves give vertical Darcy flux from curvature. With 0.005 C resolution, 0.25-0.5 m steps and 100-300 m of hole, a Peclet number of about 0.05-0.1 is readable. That is a vertical Darcy flux of about **0.3-1.5 cm/yr** (calc, rock conductivity 2 W/m/K). Masking recharge in Basin and Range valleys is often larger than that, so it shows up if it is there.
- **Masked positives among old negatives.** A hole called "cold" in 1980 because its bottom 50 m gradient was near background can, at 0.005 C, show (i) a concave-up bottom (downflow lid with heat below), (ii) a small reversal at a contact (lateral warm outflow at range of 0.1-2 km), or (iii) a bottom gradient 20-40% above what the old straight-line fit said once the drilling transient is gone. Any of these moves the hole from M19 grade G3 (hard negative) to G4/G2 (masked or warm, open-ended).
- **40-year time-lapse (new).** Ground-surface warming since 1980 reaches about 35-75 m down (calc: sqrt(kappa t) = 36 m, 2 sqrt(kappa t) = 71 m). That part is a known, modelled signal. Below about 80 m, any change between the 1980 log (after correcting it) and the 2026 log is from changed groundwater flow, usually valley pumping. A change in reversal depth or curvature is a direct, natural experiment on Peclet and lid thickness (rank 3). No other data source gives this. Climate researchers already use repeat logs decades apart (for example Harris and Chapman and co-workers in Utah, from memory, unverified), so the method is accepted.
- **Pipe convection is negligible (calc).** Critical gradient for onset of convection (Rayleigh 216 for a long vertical tube): 3/4" pipe 560-2,900 C/km and 1" pipe 210-1,090 C/km over 10-50 C water. Only a very hot hole (above about 200 C/km in 1" pipe at 50 C) will convect. So noise is set by the probe (0.002-0.005 C) and depth control, not by the hole.

### 1b. Why a drone magnetometer can find the collar

- A long vertical steel pipe acts like a magnetic pole at its top. For a 3/4-1.25" schedule 40 pipe the steel area is 2.2-4.3 cm2. Induced magnetization alone gives about **3.4-6.9 nT at 5 m and 0.9-1.7 nT at 10 m** (calc). Pipe usually also carries remanence from manufacture and handling, often several times the induced part, giving roughly **34-69 nT at 5 m** with a 10x remanence factor (calc, the factor is unverified). Surface conductor casing (if any), caps, wire and drill junk add more.
- Drone noise for a good fluxgate on a 1-1.5 m boom, after heading compensation, is about 0.5-2 nT; an optically pumped sensor (MagArrow class) is lower (from memory, unverified). So the rule is **fly 3-5 m above the ground, 3-5 m lines**. At 20-30 m altitude (normal drone mag), a TG pipe is lost in geology.
- Detection limit: a pipe is found with high confidence inside about 3-5 m of a line at 3-5 m height. Basalt and magnetite-rich alluvium give short-wavelength clutter of tens of nT, which is the main false-alarm source. A two-sensor vertical gradiometer cuts that.
- **Non-steel holes are missed.** PVC-cased holes (some 1980s TG and most piezometers) are invisible to the magnetometer. For these, the caps, cut-off stub, survey stakes, cement pad and pad scar are the targets: camera plus a pulse-induction metal detector (finds a steel cap or rebar stake to about 0.5-1 m, from memory). Share of PVC in the industry TG pool is unknown (unverified). The extracted completion record often states it, so the desk step sorts holes into "steel" (fly) and "PVC" (walk).

### 1c. Why the location fix matters by itself

- A hole known only to a quarter-quarter (±200 m) or a section (±800 m) can sit in the wrong 500 m model parcel about half the time or more (calc estimate for the section case). The model then smears a temperature over the wrong cell. Most archive holes carry only TRS (M20; MODEL "TRS location error ±400-800 m").
- Locating even 100-200 collars gives an **empirical TRS error model** by company and era (for example, Phillips holes may have used a local prospect grid). That error model then applies to the other 2,500-3,000 holes we never visit. This is the cheapest rank-7 win in the whole plan.

## 2. Prior art

| Who / what | What it does | Gap we fill |
|---|---|---|
| NETL/DOE and USGS drone magnetometer surveys for orphan oil and gas wells (from memory, unverified details) | Find 5-1/2" to 8-5/8" steel casing from 15-30 m altitude | Targets are 5-20x larger in steel area. Nobody has published a 3/4-1" TG-pipe finder. We fly lower and cue from air photos. |
| LBNL AI on old topo maps for lost wells (H14, https://newscenter.lbl.gov/2024/12/04/ai-helps-researchers-dig-through-old-maps-to-find-lost-oil-and-gas-wells/) | Map symbols to candidate well spots | Same idea for TG prospect sketch maps, plus pad detection in air photos |
| Schonstedt-type handheld magnetic locators (surveyors find buried monuments and pipe) | Ground search to about 1-2 m depth (from memory) | We use it as the last step only |
| USGS heat-flow program (Sass, Lachenbruch, Munroe, 1970s-90s) | Logged pipe-cased holes with thermistor probes on 4-conductor or single-conductor cable, often relogged weeks to years later (from memory) | Their probe design is the template. They never relogged the industry archive decades later. |
| Repeat borehole climate logs (Utah, Czech, Canada) | Decade-apart logs to see surface warming (from memory, unverified) | We use the same repeat idea below the climate depth to read flow change |
| ND Geological Survey static temperature logging of TA oil wells (H02) | Third-party logging of idle wells with permission | Proves the access model; they log big casing, not 3/4" TG pipe |
| H02 "Thermal Census" and P01 Sentinel (our own) | Log idle oil wells and ranch wells | P09 is the same winch with a needle probe, aimed at the best-documented exploration holes |
| Zanskar | Public data ML, LBNL seismology, own wells (M13) | No public sign they relog legacy TG pipe (unverified). They have the money but not this habit. |

## 3. v1 design

### 3a. Desk step: "Where is it?" (no field time)

1. **GeoFM Stage 0** pulls each hole's ID, TRS, depth, completion (pipe size, steel or PVC, capped or plugged), log date and any prospect sketch map from NBMG, OFR 99-425, NDOM, CalGEM, UGS/EGI scans.
2. **Map georeferencing.** Sketch maps with roads and section corners are georeferenced to ±30-100 m (estimate).
3. **Pad detection.** A vision model scans 1980s USGS single-frame air photos (EarthExplorer) and NAIP 0.6 m imagery inside the box for pad scars, mud-pit shadows and dead-end two-tracks. Output: 1-5 ranked candidate points per hole with a probability.
4. **Access and status filter.** Join land status (BLM, private checkerboard, state), road access, wilderness/WSA and sage-grouse layers. Drop holes where casual use is unlikely. Rank the rest by EVSI per dollar in the VOI-Bank (see section 6), with a cluster bonus because prospects were drilled as grids of 5-20 holes (L16).

### 3b. CollarFinder field kit

| Part | Choice | Cost (unverified) |
|---|---|---|
| Drone | DJI Matrice 350 RTK class, 2 battery sets, terrain-follow at 3-5 m | $12-16k |
| Magnetometer, DIY path | 2 three-axis fluxgates (Stefan Mayer FLC3-70 class, about 0.1-0.2 nT/rtHz) as a 0.5 m vertical gradiometer, 24-bit logger at 100-200 Hz, on a 1.5 m carbon boom or a 3 m tow line | $2.5-4k |
| Magnetometer, COTS path | SENSYS MagDrone or Geometrics MagArrow class | $20-40k |
| RTK GNSS | Base + rover pair (Emlid Reach RS3 class) for 2 cm collar coordinates | $4-6k |
| Handheld | Magnetic locator (Schonstedt class) + pulse-induction metal detector + probe rod + hand tools (shovel under 10 ft) | $2.5-3.5k |
| Camera | Drone camera for oblique photos; phone for collar photo and cap state | included |
| Software | Heading compensation, gradient filter, monopole fit (x, y, depth to top) | own code |

- Flight plan: 60 x 60 m box around each candidate pad, 3 m lines, 4 m height: about 1.2 line-km, 3-5 minutes (calc). Then fit a monopole: top-of-pipe x, y to about 1 m and burial depth to about ±0.5 m.
- Ground finish: walk to the fit point with the locator, flag, RTK shot, photo, open or dig to the collar (hand tools only, keeps it casual use).
- Power: drone batteries plus a 1 kWh LiFePO4 pack and inverter on the UTV for charging.

### 3c. Needle Logger

| Part | Spec | Cost (unverified) |
|---|---|---|
| Probe | 8 mm OD x 250 mm 316 stainless tube; glass-bead NTC thermistor (time constant about 0.5-1 s in water); MCU with 24-bit ADC (ADS1220 class) and a ratiometric bridge to a reference resistor; small pressure die (MS5837 class) for water level and depth check; 30 MPa rating; build 4 probes | $250-500 each in parts |
| Telemetry | Digital FSK over the cable conductor, armor as return. This is the classic USGS single-conductor approach | in probe |
| Cable | 600 m of 2.4 mm (3/32") single-conductor armored logging cable, or 1.2 mm Kevlar-jacketed coax for a lighter v0 | $1.5-4k |
| Winch | Motor drum with slip ring, 12 V, 0.5-10 m/min speed control, level wind; mounts in a UTV bed or truck hitch | $3-6k DIY, $10-20k COTS small logging winch |
| Depth | Measuring wheel with encoder (0.01 m), plus pressure cross-check | $0.5-1k |
| Tripod | Small sheave tripod over the collar, pipe adapter for 3/4", 1", 1-1/4" | $0.4-0.8k |
| Calibration | Stirred water bath and a reference thermometer traceable to ITS-90 (0.005 C), calibrated before and after each trip | $3-5k |
| Clean-out | 6 mm weighted "sinker bar" dummy run first; fishing magnet; cap tools (pipe wrenches, penetrating oil, bolt cutters) | $0.5k |
| Readout | Rugged tablet, logs T, depth, speed, pressure | $1-2k |

- **Run order:** dummy run to find total depth and blockages; then a slow **down-log at 3-5 m/min** (the undisturbed pass, 0.25 m samples); then an up-log as a repeat check; then 3-5 stationary dips for 5 minutes each to check drift. Pass if the down and up logs agree to 0.02 C below 20 m.
- **Water level.** If the pipe is dry or partly dry, log the air section with stops (slower, convection worse) and flag it. Water level itself is a free head reading for rank 3.
- **Optional add-ons:** a 1-litre bailer sample for EC and a quick Na-K-Ca check if the pipe is open-ended at the bottom (most TG pipes were capped at the bottom, so usually not); a cuttings-library pull from NBMG or EGI for needle-probe conductivity on the same hole (lab, about $50-100 per sample, unverified), which hits rank 7 directly.

### 3d. Crew time per site

| Step | Clustered prospect | Isolated hole |
|---|---|---|
| Drive between holes | 0.2-0.5 h | 1-3 h |
| Drone box + monopole fit | 0.3-0.5 h | 0.3-0.5 h (plus a second pad if the first is wrong) |
| Ground finish, dig, open cap | 0.3-1 h | 0.3-1 h |
| Dummy run + log + repeat | 0.7-2 h (100-300 m hole) | 0.7-2 h |
| Close cap, photo, notes | 0.2 h | 0.2 h |
| **Total** | **about 1.5-4 h, 3-5 holes/day** | **about 3-7 h, 1-2 holes/day** |

At about $1.5-2k per crew-day (2 people, truck, UTV rental, per diem; unverified), that is **$400-900 per hole in clusters** and **$1.5-3k when isolated**. Holes that turn out plugged or blocked cost about a third of that and still give a location fix and a dart or 2 m tie point.

## 4. How big is the pool

| Pool | Count | Note |
|---|---|---|
| NBMG industry TG holes with scanned logs | 442 | M20 F1, Washoe 155, Pershing 150, Elko 146, Churchill 143 |
| USGS OFR 99-425 holes | 786 | mostly Phillips; overlap with NBMG unknown |
| NDOM TG holes | about 124-260 | M19: 122 expired, 70 P&A, 55 in use, 9 pending (NDOM table) |
| CalGEM TG holes | 2,008 | 1,586 plugged; 92 active + 30 idle + 138 unknown are the open candidates |
| Utah UGS/EGI gradient holes | 180+ holes with reports (L16) | count unverified |
| **Total legacy TG** | **about 3,000-3,500** | before de-duplication |

Yield funnel (unverified, to be measured by the first test): collar found 50-80% in desert valleys; pipe still open and loggable 10-30% of all holes (brief); so **about 300-1,000 relogs** across NV, CA, UT. CalGEM "active" and "idle" (122) and NDOM "in use" (55) plus "expired" (122) are the best first targets, because they have no plug record. That is up to about 300 holes where the regulator's own table says "not plugged".

Beyond TG: the same kit locates oil-well and mining collars (H02 Thermal Census) and old water wells, so the CollarFinder is not stranded if the TG pool is smaller than hoped.

## 5. What it shrinks in the model

| Rank | Uncertainty | How P09 helps | Rough size (unverified) |
|---|---|---|---|
| 4 | Sensor reliability s/q per mask class, and GeoFM extraction error | Every relog is a matched pair: the extracted 1980 curve vs the 2026 truth. 100 pairs measure extraction gradient error to about ±2-3% (SE of a 15% scatter). It directly tests the MODEL kill gate (extraction error >20%). It also gives the "archive TG hole" detector its own s/q by mask class from real data, not priors. | Narrows the archive-detector s/q prior by about 50-70%; overall rank-4 VOI swing down about 15-25% |
| 1 | Detection gap / occupancy | Measures the masked share among old negatives (M19's 5-10% guess). At a true 7% and 150 relogs, the 95% CI is about ±4 points. That share sets P_det for the densest effort channel in the archive, across all 3,000+ holes. | About 10-20% of the log-variance of Nevada N; more where TG grids are dense |
| 3 | Masking / lid thickness | Curvature gives Peclet down to about 0.3-1.5 cm/yr; the 40-year time-lapse shows flow change below 80 m; water level is a head point | Strong at visited holes; the masking sensitivity term (0.8 to 0) gets a site-level likelihood at 300-1,000 points |
| 5 | Temperature at 0.5-2 km | Equilibrated bottom gradient error drops from about ±20-30% (single early log) to about ±3-5%; with conductivity from cuttings, T at 1 km error from about ±15-20 C to about ±5-8 C at visited holes | Big locally, about 10% of rank-5 variance regionally |
| 7 | Position error | ±400-800 m to ±1-5 m at visited holes, and an empirical TRS error model for the 2,500+ unvisited | Most of the archive's position term |
| 6 | Upflow location | Reversals give a direction to outflow sources at 0.1-2 km | Moderate, site-level |

Expected direct discoveries (unverified): if 5-10% of 300-1,000 relogged negatives are masked, that is **15-100 masked targets**. If 10-20% of those become bankable at 10-50 MWe, that is about **2-20 resources, roughly 20-1,000 MWe**. That alone is not the case for the build. The case is that the truth set re-weights the whole 3,000-hole negative archive and the GeoFM extraction, which touch most Nevada cells.

## 6. Rights edge

- **Access is cheap.** On unleased BLM land, IM 2026-024 lists "sampling existing wells without changing them" and drone surveys as casual use (H13). No notice, no filing duty for data from unleased land (hardware MEMO, 43 CFR 3253.10(b) as cited there). Opening a cap and closing it again is arguably not a change (unverified; keep a methods memo). Hand digging under 10 ft is listed as casual use.
- **Many old leases lapsed.** The 1970s-80s prospects were on BLM leases or private leases that ended decades ago (L16, L24). A masked positive found under a lapsed lease is open for nomination (BLM competitive, then leftover noncompetitive) or a ranch heat option at $1-2/ac.
- **Railroad checkerboard.** Many Humboldt, Pershing and Elko TG holes sit in the I-80 checkerboard (share unverified). There, half the sections are private, so the same visit can sign the heat option (the P01 "logger as landman" play).
- **Information edge.** Nobody else knows which "dry" holes were masked. The scanned 1980 log is public, but the 2026 relog is ours and need not be filed. The edge is time-limited: if Zanskar or USGS starts relogging, it erodes. Speed matters.
- **Limit.** On BLM land the edge is information, not access: we still face an auction. Nominating a masked hole's cell leaks it. So the best rights alpha is on private and checkerboard land; on BLM, bundle the target cell with decoy cells.

## 7. Risks

1. **Open-pipe rate may be low.** Regulators required TG plugging; many pipes were cut and cemented at the top. If loggable share is under 10%, the Needle Logger is a side tool and the CollarFinder carries the value (location + tie points).
2. **PVC casing is invisible to the magnetometer.** Need the completion record or a walk-and-detect fallback.
3. **Blocked pipes.** Rocks thrown in, collapsed or corroded pipe, mud. Dummy runs catch it; a fishing magnet clears some.
4. **Re-entry legal grey zone.** Drilling out a top plug is a re-entry and needs a permit (NDOM, CalGEM). We do not do it in v1. Even opening a cap on federal land could be argued to be a change; a decoy NOI can get a written ruling within 15 days (H13).
5. **Disturbance claims.** UTV off existing roads can pull the activity out of casual use. Stay on two-tracks; carry the winch on a hand cart for the last 50-100 m if needed.
6. **Old-log linkage errors.** If the 1980 hole ID cannot be matched to the found collar (several holes on one pad, re-drills), the matched-pair value drops. RTK location vs depth and pipe size usually resolves it.
7. **Geology clutter.** Basalt and magnetic alluvium give false targets. Gradiometer plus pad cueing reduces it.
8. **Climate and pumping signal mixed with heat signal.** The 40-year change above 80 m is mostly climate; below that, it must be modelled with pumping history (NDWR records).
9. **Copyable once known.** The method is simple. Moat is the head start, the matched-pair dataset and the private relogs.
10. **Hot holes convect.** Above about 200 C/km in 1" pipe at 50 C, convection adds noise; but those holes were already positives.

## 8. First test

**Weeks 0-4, desk, about $2-5k.** Take the 442 NBMG and 786 OFR 99-425 holes. Run GeoFM location and completion extraction. Run pad detection on 1980s air photos and NAIP. Pre-register 30-40 holes in 3-4 clustered prospects on BLM and checkerboard land, chosen by VOI-Bank EVSI per dollar and access. Also pick 10 CalGEM "active/idle" TG holes in Lassen/Modoc as a second state. Write the casual-use methods memo.

**Weeks 4-10, build, about $35-50k.** DIY fluxgate gradiometer on an M350; Needle Logger v1 (2 probes, 400 m cable, DIY winch); bath calibration. Bench test: find a buried 3 m stub of 3/4" steel pipe at 0.5 m depth from 4 m height in a test field; log a 30 m PVC test tube against a reference string.

**Week 10-12, field, 1 trip of 5 days, about $8-12k.** Targets: 30-40 holes.

Pass/fail gates, all pre-registered:
- Collar located within 5 m for at least 40% of holes (stretch 70%).
- Median crew time to locate under 1.5 h per hole.
- At least 15% of visited holes open and loggable to at least 50 m (stretch 30%).
- Down vs up log agreement under 0.02 C below 20 m.
- Old-vs-new gradient comparison on every logged hole that has an extracted 1980 curve; report the extraction error and the share of old negatives that change grade.
- All-in cost under $3k per logged hole.

If collars are found but few pipes are open, keep CollarFinder and switch the Needle Logger budget to P02 darts beside the collars. If both pass, scale to 300-500 holes in season 1 (about 2 crews, 12-16 weeks).

## 9. Self-scores (1-5)

- Model uncertainty alpha: **4**. A designed truth set for the archive channel and for GeoFM extraction, plus position fixes. It touches ranks 1, 3, 4, 5 and 7.
- Rights alpha: **3**. Strong on private and checkerboard land and for lapsed leases, but BLM targets still go to auction.
- Buildability: **4**. 8-12 weeks, two people, mostly off-the-shelf parts and known physics.
- Cost and scale: **3**. $400-3k per hole is cheap, but the pool is about 3,000-3,500 holes and the open share is unknown; the kit extends to oil, mining and water wells.
- Moat: **3.5**. The relog data and matched pairs are private and slow to copy, but the method itself is easy to copy once known.

## Sources

- Repo: `M20-tg-and-mining-holes.md` (NBMG WellLog service https://web2.nbmg.unr.edu/arcgis/rest/services/NV_Data/NVWellLogs/MapServer/0 ; OFR 99-425 https://pubs.usgs.gov/of/1999/of99-425/webmaps/home.html)
- Repo: `M19-labels-and-negatives.md` (CalGEM and NDOM status counts)
- Repo: `../../../hardware/evidence/H13-permits-and-secrecy.md` (BLM IM 2026-024, https://www.blm.gov/policy/im-2026-024)
- Repo: `../../../hardware/evidence/H05-quantum-novel-sensors.md` (MagArrow, https://maverickdrone.com/products/geometrics-magarrow-mk2-magnetometer)
- Repo: `../../../hardware/evidence/H02-existing-well-logging.md` (plugged wells need rig re-entry; ND TA logging)
- LBNL lost-well AI: https://newscenter.lbl.gov/2024/12/04/ai-helps-researchers-dig-through-old-maps-to-find-lost-oil-and-gas-wells/
- Bredehoeft, J.D. and Papadopulos, I.S. (1965), Rates of vertical groundwater movement estimated from the Earth's thermal profile, Water Resources Research 1(2) (from memory)
- Lachenbruch, A.H. and Brewer, M.C. (1959), Dissipation of the temperature effect of drilling a well in Arctic Alaska, USGS Bulletin 1083-C (from memory)
- Physics arithmetic: `P09_calc.py` in this folder
