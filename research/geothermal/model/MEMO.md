# Hidden Hydrothermal: Model and Sensor Memo

Date: 23 Oct 2026. This memo answers Dhruv's request: "read about the data, decide how to make a better model to figure out how much hidden hydrothermal there is with greater certainty, and tell me what sensor to make". It is built from `MODEL.md` (6 model designs, 3 judges), 30 physical-build deep-dives (P01-P30 in `evidence/`), a first-pass scoring of all 30, and 3-vote red teams on the top 6. It builds on `../MEMO.md` and `../../hardware/MEMO.md` and does not repeat them. The scores are in `SCORES.json`.

**Sourcing note.** No new web searches were run for this synthesis. The shared search budget ran out during the red-team turn. Primary sources below come from the evidence files. Prices, sensitivities and VOI figures are estimates and are marked (unverified) where they matter.

---

## 1. Verdict

**The sensor to build: the Logging Heat-Flux Dart v1.1.** It is a 3 m casual-use probe with a 6-depth temperature string (TMP117, 0.01 C relative), a heater that measures rock conductivity in place, a moisture ring and a gas port. It is installed in **clusters of 3**, with a ring of cheap surface-temperature buttons, and read as a line average. On BLM land it runs in **30-60 day campaigns** that fit casual use under IM 2026-024. On private land under our option, and on our own leases, it runs for 12 months. It won on red-team revised totals: 15/25, tied with the Wellhead Clamp and ahead of it on rights alpha (3 vs 2.5). It was also the only top-6 build that two of three red-teamers did **not** refute. The honest claim, after the red team, is about 2-3x the flux sensitivity of the logged 2 m probe we already picked (not 8-15x), and a reach to 100 C fluid of about 260-570 m under a dry lid (not 400-1,000 m). That is still the cheapest way to turn "2 m blank" cells into calibrated negatives or real hits in the masked ground where rights are mispriced. The ranch-well drop-probe visit stays, but as the rights door-opener with a helium sampler and a simple temperature port added, not as the main detector.

**The model: SENTINEL-COX.** The spine is VOI-Bank: the target is risked NPV per acre on 500 m parcels, and every next action (buy a right, place darts, visit a well, drill) is picked by expected value of sample information per dollar. The count of hidden systems comes from CREAM-COX: a log-Gaussian Cox process whose detection is "thinned" by the dated history of who found what, through which search channel, after how much effort. Each raw reading enters through its own censored likelihood on a 1D temperature column (THERMOS-B). The main new data is Stage 0: AI extraction of scanned temperature logs and well files (NBMG, NDWR, CalGEM, NDOM). One shared latent "mask class" (open, cold lid, swept, outflow tongue) sits under every detector, so two detectors in the same cell identify the miss rate without assuming they fail independently. Certainty is quantified by about 4,000 joint posterior draws, summed draw by draw into regional MWe bands, and checked by simulation-based calibration on synthetic Nevadas and by frozen-date hindcasts. USGS and NREL totals are hold-out checks only and are never fitted.

---

## 2. What the data says

### Best datasets

| Dataset | Why it matters | Source |
|---|---|---|
| USGS Great Basin 205-system inventory (28 plant, 78 known, 99 probable) | Dated, channel-tagged finds; the 99 probable are the main hold-out | doi 10.5066/P13AXSYL |
| NDWR Well Driller Reports, 146,235 reports; about 90% of temperatures never keyed | Biggest dated search-effort layer, and a large unkeyed temperature pool for Stage 0 | https://arcgis.water.nv.gov/arcgis/rest/services/NDWR/Well_Driller_Reports/FeatureServer/0 |
| NBMG WellLog scans (2,002 PDFs, 500+ T-logs on 442 TG holes); CalGEM 4,346 wells (2,008 TG holes); NDOM 938 well files | Full T(z) curves nobody has keyed | M-files; CalGEM, NBMG portals |
| OFR 99-425 TG archive (786 holes) | Benchmark for extraction error, and hard negatives | https://pubs.usgs.gov/of/1999/of99-425/webmaps/home.html |
| Burns et al. 2024 wells (22,535; 4,672 deeper than 50 m; 92% of those flow-disturbed) | Shows that most water-well temperatures are disturbed by flow | M05 |
| INGENIOUS 2 m stations (about 3,800, dated) | Shallow effort layer; 64% blank rate is a predictive check | https://gdr.openei.org/submissions/1391 |
| NDWR static water levels (146k heads), carbonate-aquifer extent, basin-fill gravity | Mask-class prior and plume direction | M23 |
| Faulds favorable structural settings (>1,430, typed) | Intensity and permeability prior | M-files |
| USGS 2025 favorability rasters | Benchmark only, because it was trained on later finds | https://www.sciencebase.gov/catalog/item/66e88690d34e0606a9db9b43 |

### What dominates uncertainty about blind resources

From `MODEL.md` Section 10, in order:

1. **Detection gap and occupancy**, especially for deep or lidded systems. This moves the hidden count N by 2-5x. 97% of the Great Basin has no 2 m reading.
2. **Permeability and flow per well.** About 10x on MWe at a fixed temperature.
3. **Hydrologic masking and lid thickness.** Shallow-sensor sensitivity runs from about 0.8 to about 0 (Argenta, Granite Springs, Kimama).
4. **Reliability of each cheap sensor per mask class.** Nothing is published. A sensitivity of 0.3 vs 0.7 swings VOI more than 2x.
5. **Temperature at 0.5-2 km.** Almost no public data between 300 and 1,500 m.
6. Upflow location and footprint; 7. conductive background and position error; 8. the size tail; 9. recovery factor (a scenario axis only).

The red team added one lesson that cuts across all of this. **Ranch wells sample outflow on valley floors.** They see little under real lids (Kimama is near-isothermal to about 950 m), and long well screens dilute thin warm layers. So well-based tools mostly re-find the kind of system that is already in the labels. The masked ground needs a detector that reads heat flux, not water temperature.

### How much hidden hydrothermal there plausibly is

| Estimate | Value | Status |
|---|---|---|
| USGS 2008, West, undiscovered | 30,033 MWe mean; F95 7,917; F50 23,739; F5 73,286 (11.6x F5/F95 in each Basin and Range state) | Published: https://pubs.usgs.gov/fs/2008/3082/pdf/fs2008-3082.pdf |
| USGS 2008, Nevada | 4,364 MWe undiscovered vs 1,391 MWe identified | Published, same |
| NREL/UNR Great Basin hidden | 23 GW P50, 28.45 GW mean | Published: https://www.osti.gov/pages/servlets/purl/3018341 |
| Coolbaugh 2006, Nevada count | 157 undiscovered vs 69 known | M33 |
| **Our prior, Great Basin, USGS-comparable** | (1.5-3) x 205 systems x 0.87 P(>=10 MW) x about 45 MW mean = **about 12-24 GWe** | calc, (unverified); not yet fitted |
| **Our prior, bankable on lockable land** | 12-24 GWe x 0.3-0.5 share that crosses the sloped Tmin line with flow >= 40 kg/s x 0.3-0.5 share on private, state or leftover-BLM tenure = **about 1-6 GWe** | calc, (unverified) |

What this means in plain words:
- Our Great Basin prior sits below NREL/UNR's 23 GW P50 and well above USGS's 4.4 GWe for Nevada alone. The USGS West total of about 30 GWe is a fair centre for now.
- We expect the fitted model to move **up** in masked and data-poor provinces (Snake River Plain, Cascades, AZ/NM rift, eastern carbonate Great Basin) and **down**, with tight bands, in heavily drilled empty Nevada valleys.
- The bankable, lockable slice (1-6 GWe) straddles the main kill line of 2 GWe P50. That is the single most important number the first desk fit must pin down.
- The target is to turn the uniform 11.6x F5/F95 band into local bands, under 4x in the first three states (untested).

---

## 3. The model (summary of `MODEL.md`)

**Inputs.** Dated finds (USGS 205 systems, M18 blind-case table with first-signal years); dated effort layers for 3 collapsed channels (surface leakage; shallow wells and mining; TG holes, 2 m and our sensors), with effort treated as a latent; Stage 0 extracted T(z) curves carrying a +/-400-800 m township-range location error; raw temperatures (Burns wells, USGS heat flow, NBMG, NDWR, oil BHTs, IDWR, 2 m, OFR 99-425); conductive background models; heads and aquifer extent; structure; chemistry; patchy geophysics; our own frozen-label LightGBM (1990/2005/2008) residualized against effort; and our pre-registered sensor rows.

**Architecture.**
- L1: per-source censored likelihoods (equilibrium logs, censored cold holes, skewed BHT, mixed-interval driller readings, 2 m flux, mixing-model chemistry). No 3D surrogate in v1.
- L2: a 500 m latent column per cell: conductive T(z), an upflow term, an outflow plume kernel along heads, a mask class and a permeability class.
- L3: CREAM-COX on a 2 km mesh, fitted first in inlabru and then in NumPyro HMC. Detection is 1 - exp(-sum of catch rate x effort) per channel and mask class. Size marks are lognormal-Pareto.
- L4: VOI-Bank. RNPV per acre from the fixed M34 economics, with price, Rg and capture stage as scenario axes. Actions are ranked by EVSI per dollar. The lock rule is to buy wherever RNPV/ac exceeds 3x the 10-year holding cost.
- GHOST Tier 1 (an analytic column-plus-plume simulator, about 1 ms per run) is used for calibration checks and to rank sensors before we build them.

**Two rules.** (A) Do not use the USGS 2025 favorability as a raw offset: it encodes detection and leaks later finds into hindcasts. (B) USGS 2008, Coolbaugh and NREL/UNR totals are hold-out checks only.

**How certainty is quantified.** About 4,000 joint posterior draws. Regional totals are summed draw by draw, clustered at 10 km and reported per Rg scenario (0.08/0.16/0.25). The band is split four ways: count and detection, masking and depth, size and permeability (these three can be shrunk by sensors), and Rg and economics (handed to the buyer). Cells far from training data get inflated variance and a VOI bonus.

**Cheapest first validation (desk, weeks 0-10, about $5k or less, unverified).**
1. Rank the 697 isolated warm NDWR wells by EVSI per dollar. Pre-register Granite Springs 68-02.
2. Stage 0 extraction benchmark against OFR 99-425: pass at median gradient error 10% or less and at least 80% usable curves.
3. Nevada LGCP plus column fit, with SBC on 20 synthetic Nevadas and predictive checks (64% 2 m blank rate, 92% flow-disturbed share).
4. Replay backtest frozen at 2005, with all policies drawing from one shared bank, and bootstrap CIs. Hindcasts freeze at each system's real first-signal date (Blue Mountain, McGinness and DAC are pre-1990 signals).

**Judge scoreboard (sum of 3 judges, out of 75):** VOI-Bank 60, CREAM-COX 57.5, THERMOS-B 50.5, GHOST-SBI 49.5, GeoFM-West 47.5, HEATFIELD-PU 44.5.

**One change this memo makes to `MODEL.md`.** The model named the one-visit Ranch Well Sentinel as the main sensor and darts as the second build. The red team reversed that order (Section 6). In THERMOS-B the dart enters as reading type D, and the well visit becomes the paired second detector for the swept mask.

---

## 4. Ranked list of all physical builds

Ranking rule: red-team revised total (median of 3 votes). Ties are broken by median rights alpha, then buildability. Only the first-pass top 6 were red-teamed. Their totals fell by 3.5-5.5 points, a mean of 5.0. The other 24 builds get a provisional total of first pass minus 5.0, so they are compared on the same footing. Even if each unvetted build lost only the smallest drop (3.5), the best of them (17) would score 13.5, below the pick's 15.

Sub-scores: M = model-uncertainty alpha, R = rights alpha, B = buildability, C = cost and scale, Mo = moat. Each is out of 5. Red-teamed rows show median revised sub-scores. The other rows show first-pass sub-scores.

| Rank | ID | Build | M | R | B | C | Mo | First pass | Ranking total | Red-team result |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | P02 | Logging Heat-Flux Dart (3 m) | 3 | 3 | 3 | 3.5 | 2 | 18.5 | **15** | Refuted 1/3. Gain is about 2-3x over logged 2 m, not 8-15x; reach 260-570 m; the sim shared forcing between darts; surface patchiness and the install disturb the gradient; 12-month unattended may not be casual use |
| 2 | P04 | Wellhead Clamp fleet | 2.5 | 2.5 | 4 | 4 | 1.5 | 20.5 | **15** | Refuted 3/3. Blind to lids; back-projection is not identifiable from down-gradient wells; wells are not owners; same-day e-sign fails in community-property states; it finds farm outflow, not upflow |
| 3 | P26 | Water-Point Ledger (Cl-flux) | 3 | 2 | 4 | 4 | 1.5 | 19.5 | **14.5** | Refuted 3/3. Measures Cl, not heat (about 23x band); Idaho waters are too dilute; SRP is swamped by farm Cl; Cascades budget is already public and has no buyers |
| 4 | P12 | Pump-Puller Open-Hole Sonde | 3 | 3 | 3.5 | 2.5 | 2 | 19.5 | **14** | Refuted 2/3. Long-pumped wells are not near equilibrium; it re-measures the same well population; same-day swaps leave no time; stuck-tool risk |
| 5 | P07 | Drill-Rig Ride-Along pucks + strings | 3 | 3 | 3 | 2.5 | 2 | 19.5 | **14** | Refuted 3/3. Rigs run 24/7 so stands are rare; Horner rule does not apply; dry rod columns; lost circulation chills hot zones; Carlin belt sits in the Eureka Low lid; miners already spot hot water |
| 6 | P24 | Field Gas Lab (He/Ne + valley lab) | 3 | 2 | 2 | 3 | 3 | 19 | **14** | Refuted 3/3. Helium does not cross sealed lids better than heat; false positives left out of the MC; same-night R/Ra buys a speed nobody races; lab costs more per point than outside labs at 400 points a year. Cartridge-only P24a judged about 16 by two voters |
| 7 | P01 | Ranch Well Sentinel 2.0 (resident) | 3 | 4 | 4 | 3 | 3 | 17 | 12 (prov.) | Not red-teamed |
| 8 | P19 | Kite semi-airborne EM | 3.5 | 4 | 2.5 | 4 | 3 | 17 | 12 (prov.) | Not red-teamed; hover noise test first |
| 9 | P09 | Legacy Hole Rescue | 3.5 | 3 | 4 | 3 | 3.5 | 17 | 12 (prov.) | Not red-teamed |
| 10 | P29 | Archive Truth Lab | 3.5 | 3 | 4 | 3.5 | 3 | 17 | 12 (prov.) | Not red-teamed |
| 11 | P20 | Plume Rover (towed tTEM) | 3 | 3.5 | 3.5 | 4 | 2.5 | 16.5 | 11.5 (prov.) | Not red-teamed; rent first |
| 12 | P27 | Thermal Calibration Chain | 2.5 | 3.5 | 3.5 | 4.5 | 2.5 | 16.5 | 11.5 (prov.) | Not red-teamed |
| 13 | P25 | Soil-Gas Integrator cups | 2.5 | 3 | 5 | 4 | 2 | 16.5 | 11.5 (prov.) | Not red-teamed; dart add-on only |
| 14 | P06 | Valley Pressure-and-InSAR Array | 3 | 3 | 4 | 3 | 3 | 16 | 11 (prov.) | Not red-teamed |
| 15 | P14 | DART-60 Thermal Push Rig | 4 | 2.5 | 4 | 2.5 | 3 | 16 | 11 (prov.) | Not red-teamed; hire, do not buy |
| 16 | P10 | Slickline Trailer + Deep Grab | 3.5 | 3 | 3.5 | 2.5 | 3 | 15.5 | 10.5 (prov.) | Not red-teamed |
| 17 | P03 | E-MT Node 2.0 (drone carpet) | 4 | 3 | 2.5 | 3 | 3 | 15.5 | 10.5 (prov.) | Not red-teamed; keep hand-placed nodes |
| 18 | P28 | Parcel Structure Payloads | 3 | 3.5 | 3.5 | 3 | 2 | 15 | 10 (prov.) | Not red-teamed; rent |
| 19 | P13 | Drone Dart Carpet (1 m) | 2.5 | 3.5 | 3 | 4 | 2 | 15 | 10 (prov.) | Not red-teamed; superseded by P02 |
| 20 | P23 | Mc-Gap Sentries + HVSR | 3 | 2.5 | 4 | 3.5 | 2 | 15 | 10 (prov.) | Not red-teamed; keep HVSR only |
| 21 | P16 | Slim-Hole Confirmation Package | 3 | 3.5 | 3 | 2 | 3 | 14.5 | 9.5 (prov.) | Not red-teamed |
| 22 | P05 | Pump-Cycle Mixing Sampler | 2.5 | 3 | 4 | 2 | 3 | 14.5 | 9.5 (prov.) | Not red-teamed; fold into visit |
| 23 | P08 | Mine-Water Heat Audit | 3.5 | 3 | 3 | 2 | 3 | 14.5 | 9.5 (prov.) | Not red-teamed |
| 24 | P15 | PACKSACK-CORE corer | 3.5 | 2.5 | 3 | 2 | 3.5 | 14.5 | 9.5 (prov.) | Not red-teamed |
| 25 | P22 | Corridor Fibre and Rail Lines | 3 | 2.5 | 2 | 3.5 | 3.5 | 14.5 | 9.5 (prov.) | Not red-teamed |
| 26 | P11 | Slim-Hole Permeability Kit | 3 | 2.5 | 3.5 | 2 | 3 | 14 | 9 (prov.) | Not red-teamed; rent |
| 27 | P18 | Coded-Source Transmitter | 2.5 | 2.5 | 3.5 | 3 | 2.5 | 14 | 9 (prov.) | Not red-teamed; P03 accessory |
| 28 | P21 | Tidal Permeability Seismics | 2.5 | 2.5 | 3 | 3 | 3 | 14 | 9 (prov.) | Not red-teamed; desk test on PoroTomo first |
| 29 | P17 | Mini-Frac Stress Kit | 2.5 | 3 | 2.5 | 2 | 3 | 13 | 8 (prov.) | Not red-teamed |
| 30 | P30 | Muon Well-Puck | 2 | 1 | 2.5 | 1.5 | 2 | 9 | 4 (prov.) | Not red-teamed; kill |

Two things stand out. First, no build survived the red team above 15/25, so no single sensor is a company by itself. That matches the prior hardware memo: the bank is the company and the sensor is its moat. Second, the five well and rig builds (P04, P12, P07, P24, P26) all failed for the same root reason: they see water that has already left the upflow, under land that buyers do not need. The dart failed only on size of claim, not on direction.

---

## 5. The sensor in depth: Logging Heat-Flux Dart v1.1

### Why this one
- It reads **heat flux** (gradient times in-place conductivity), which survives a dry lid that hides the heat from a 2 m temperature reading. Granite Springs is the clean example: TG holes above 220 C/km (GDR 969), but a 2 m maximum of only 3.4 C, so the 2 m survey missed it.
- Its blanks become **calibrated negatives**, which is what rank 1 (detection gap) and rank 3 (masking) need.
- It works on **unleased, unfiled BLM land** under casual use, where data need not be filed (43 CFR 3253.10(b), per the prior memo), and on optioned private land.
- Cost per site is about $300, against about $1,000 per Zanskar shallow sample (Edwards SGW 2025, https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Edwards.pdf) and $150-500k per TG hole.

### Design v1.1 (red-team fixes built in)
1. **Smaller hole.** A 1.25 in casing, or a sacrificial 1/2 in stainless rod with the string bonded inside, in place of the 1.75 in casing. This cuts refusal on stony fans and removes the need to pull casing against bentonite.
2. **Removable string in a permanent thin tube**, so the electronics come back even when the tube stays.
3. **Six TMP117 sensors from 0.5 to 2.95 m**, with a redundant pair at 2.9 m. Burn-in and bath calibration to 0.01 C relative before deployment, because 0.02 C a year of drift roughly doubles the error.
4. **Line-source heater** for horizontal k (target within 15% of a needle probe). Spend one dart pair per valley on core measured both ways to check kh against kv.
5. **Moisture ring** at 1 and 2.5 m, and a **gas port** that takes a P25 Rn/He cup.
6. **Clusters of 3 darts at 10-30 m spacing**, plus a ring of 4-8 surface or 10 cm temperature buttons within about 5 m. Report flux per cluster, not per dart. This averages out surface patchiness at 5-50 m.
7. **Small install footprint.** Disturbed patch under 0.5 m radius; restore surface material and keep shrubs (the Apollo heat-flow lesson). Drop or model the first 60-90 days.
8. **Fine-sand slurry backfill** in place of native fill, so the annulus has no voids.
9. **No fixed gateway on BLM land.** Data come back by truck or drone data mule, or through a gateway on private ranch land.
10. **Two modes.** Campaign mode: 30-60 days, read by a Kalman inversion forced with ERA5-Land and PRISM, wider sigma. Record mode: 12 months, only on private land under option or on our own leases.

### BOM (per dart, unverified)

| Item | Cost |
|---|---|
| TMP117 string, 7 sensors, cable, potting | $45-60 |
| MCU, logger, LoRa radio, battery | $40-55 |
| Heater element and driver | $10-15 |
| Moisture ring | $25-35 |
| Tube or sacrificial rod, cap, slurry | $30-45 |
| Gas-port cup (optional P25) | $10-20 |
| **Per dart** | **about $160-230** |
| Surface-button ring per cluster (6 buttons) | $30-50 |
| **Per cluster of 3** | **about $510-740 hardware** |
| Shared: hand breaker, drive kit, calibration bath, data-mule kit | $6-10k per crew |

### Cost per site and per km2 (unverified)
- Installed cost: about $300 per dart, so about $900-1,200 per cluster with crew time.
- Prospect line (12 clusters across a target, 12 in a control valley): about $25-35k all-in for a 6-12 month read.
- Carpet at one cluster per 500 m cell (4 per km2): about $4-5k per km2 for the first deployment and about $2.5-3k per km2 with hardware reused. This is about the same as the prior pick's E-MT carpet ($3-8k per km2), so the dart is used on lines and high-EVSI cells, not wall to wall.

### Build weeks
- Weeks 0-2: desk sim rerun and legal ruling request.
- Weeks 2-8: 30 darts (10 clusters), bath calibration and the heater k sand-box test, with a team of 2-3.
- Weeks 4-6, in parallel: a 50-hole install-rate pilot on a stony range-front fan.
- Kalman inversion software: 4-6 weeks in parallel.
- The OHV pusher is deferred. It needs a field-office ruling, and roads-only travel limits it to transects.

### How it plugs into the model
- In THERMOS-B it is reading type D: q_obs ~ N(q_3m(column, mask) - q_ref, sigma^2), with sigma_model at 0.1-0.3 W/m2 per dart until the calibration campaign measures it, and lower per cluster.
- Its sensitivity q_c depends on the mask class: high under a dry lid, about 0 under a swept mask. It replaces the weak G5 "shallow blank" rule in cells it covers.
- It is paired with the ranch-well visit and its helium sample, which covers the swept mask. The two detectors share one latent mask class, so their agreement identifies the catch rate.
- VOI-Bank places darts where EVSI per dollar is highest: 2 m-blank, high-lambda, deep-water-table cells with no wells.
- GHOST Tier 1 must confirm that a dart cluster beats a well visit per dollar in those cells before we scale past 100 units.

### How it plugs into rights buying
- On **BLM land** it screens parcels before we nominate, bid or file on leftover noncompetitive parcels at $1/ac/yr. The data stay private while the land is unleased. Leftover-parcel supply is limited, so we count how many parcels a year the flux maps actually change (Section 8).
- On **private ranch land** it runs only after the heat option is signed. A 12-month record there sets the option step-up.
- It does **not** raise the price a buyer pays. Ormat and Fervo still re-drill. Its value is in buying the right acres and dropping the wrong ones sooner.

---

## 6. Where this agrees with or overturns the prior hardware pick

The prior pick (`../../hardware/MEMO.md`, 18/25) was a ranch water-well drop probe that signs the heat option on the same visit, plus logging 2 m probes and E-field-only MT nodes under casual use.

**Agrees:**
- Casual-use sensing on open land is the right spine, and IM 2026-024 is the window.
- The drop-probe visit stays as the rights engine. Every red team on the well builds (P04, P12, P24) said to fold them into it, not run them as separate fleets.
- Hand-placed E-field MT nodes stay as the tool for lids thicker than about 200 m. The drone carpet (P03) is not needed yet.
- "The bank is the company; the sensor is its moat" still holds. No build cleared 15/25.

**Overturns or changes:**
- **The 2 m probe becomes the 3 m dart cluster.** It gives about 2-3x the flux sensitivity and calibrated negatives. The logged 2 m probe is kept only as the co-located baseline on test lines.
- **The well visit is no longer the main detector.** `MODEL.md` named the one-visit Sentinel as the primary sensor. The red team showed wells sample valley-floor outflow, see little under lids, and mostly re-find known types. The visit is now (a) the door-opener for options and (b) the second detector for the swept mask.
- **The visit kit gets slimmer.** T/EC/P drop probe, a sealed geothermometer bottle, a passive He/Ne diffusion sampler or cartridge (P24a) with lab R/Ra under NDA, and a hose-bib temperature port. No ultrasonic flowmeter, no current clamp on 480 V leads, no in-house noble-gas lab.
- **No same-day e-sign.** In community-property states, with LLC or trust owners, and with notarised recording, the realistic same-day result is a letter of intent, then a remote-online-notarised option within 7 days. Title is screened for SRHA, Pittman Act and Desert Land Entry reservations before the visit.
- **Rights go up-gradient.** A warm valley-floor well points at the range-front upflow. We lock that ground (fee, state first-file, quiet BLM nominations), not just the farm that showed the warm water.
- **The time window is shorter on BLM.** 12-month unattended installs may not be casual use, so BLM work runs in 30-60 day campaigns.

---

## 7. Field kit roadmap, months 0-12

| Month | Build or action | Cost (unverified) |
|---|---|---|
| 0-2 | Model desk validation (Section 3). Dart sim rerun with independent forcing per dart. Decoy NOI asking in writing about 12-month, 2.95 m unattended installs; check 43 CFR 8365.1-2 and the ROW question. Free desk layers: NWIS/WQP Cl/B/Li budget (P26 desk), PoroTomo dv/v (P21 desk), NBMG core catalogue join (P29 desk), background-sigma check for well temperatures (P04 fix) | $5-15k |
| 0-2 | Slim drop-probe visit kit, 2-4 units (prior pick plus He diffusion sampler and temperature port). "Mining Heat Desk": data deals for survey-tool and VW-piezometer temperatures, and a driller hot-water bounty (P07, no hardware). Pump-contractor referral deals (P12-lite) | $15-30k |
| 1-2 | Build 30 darts; 50-hole install-rate pilot on a stony fan | $10-15k |
| 2-3 (Nov) | Install dart lines: Granite Springs (12 clusters), cold control valley (12), SE Gabbs or Tungsten Mountain (6), each with co-located logged 2 m probes. Check Granite Springs lease status first | $15-25k |
| 3-5 | 20 blind / 40 cold calibration campaign with two detectors per cell: dart cluster plus well visit with helium. Kite (P19) hover noise test. P09 CollarFinder pilot on 30-40 legacy holes | $60-120k |
| 4-6 | Buy or rent a miniRUEDI-class He cartridge (P24a) if diffusion samplers prove the signal. Rent tTEM (P20) at Gabbs Valley. Hire a push contractor (P14) for a head-to-head against darts on one line | $60-100k |
| 6 | Interim dart read (Kalman, 6 months). Go/no-go on the fleet (Section 8) | — |
| 6-9 | If go: scale to 100-150 darts in campaign mode on high-EVSI BLM cells and record mode on optioned private land. Pre-plug log service on 1-3 junior mining programs (P07 fix). Hand-placed E-MT nodes on lidded cells | $100-200k |
| 9-12 | 12-month read at Granite Springs. Fleet to 300-500 darts if the cluster floor holds. Rent the confirmation trailer (P11/P16) only for the top 1-3% of held prospects | $150-300k |

Not built in year 1: the valley noble-gas lab and trailer, the drone dart carpet, the drone E-MT carpet, corridor fibre, seismic sentries (keep the HVSR walk-along only), the muon puck.

---

## 8. Cheapest first tests, with pass/fail numbers

| Test | Cost, time | Pass | Fail or kill |
|---|---|---|---|
| Dart sim rerun with independent surface forcing per dart (offset sd 0.5-2 C), patchy snow, 0.02 C/yr drift | $0, 2 weeks | Cluster floor at or below 0.15 W/m2 at 1 sigma | Cluster floor above 0.3 W/m2: stop the build and keep logged 2 m |
| Install-rate pilot, 50 holes on a stony fan | about $3-5k, 1 week | At least 70% reach 2.9 m; tube or rod set in 15 min or less | Under 50% reach: switch to 2 m plus hired push (P14) |
| Legal ruling (decoy NOI) | $5-10k with attorney memo, 30 days | Written OK for 30-60 day campaigns at least | Field office treats darts as non-casual: private land and own leases only |
| Granite Springs line vs control, cluster averages | about $15-25k, 6-12 months | Mean excess at least 3 sigma above control (sigma from control scatter); flux within 30% of TG-hole k x G; heater k within 15% of needle; at least 90% of units reporting at 6 months | Not separable from control at 12 months, or field floor above 0.4 W/m2 per dart |
| Head-to-head: dart vs co-located logged 2 m probe | in the line above | Dart gives at least 1.5x lower flux error | Under 1.5x: kill the dart, keep the logged 2 m probe |
| Head-to-head: dart vs 10-30 m push | about $15-25k | Dart within 2x of push at about 1/5 the cost per site | Push gives 5x better flux at similar cost: use push except where secrecy matters |
| Rights supply check | desk, $0 | At least 20 BLM parcels a year in NV+UT+OR where the flux map would change a nominate, bid or file decision | Under 20: rights alpha for the BLM side drops to 2 |
| Drop-probe visit funnel | in the calibration campaign | At least 3 distinct owners per crew-day; at least 1 recorded option per 2 crew-days; at least 15% of owners sign within 14 days | Under 10% recorded within 30 days, or warm-well owners sign at under half the cold-well rate |
| He sampler or cartridge | about $35-50k | Cartridge within +/-5% He of lab; at least 50% of plume wells above 3 sigma of control | Under 30% of plume wells above 2 sigma, or controls fire at q above 0.4 |
| Model desk gates (`MODEL.md`) | about $5k, weeks 0-10 | Extraction median error 10% or less; SBC variance ratio on N below 0.8; replay lift at least 1.5x with CI above 1 | See Section 9 |

---

## 9. Kill conditions

**Company-level (from `MODEL.md`):**
1. **Too small (main kill).** Bankable hidden resource on lockable land in NV+UT+OR+ID+NM is below about 2 GWe P50, or fewer than about 30 undiscovered systems have P(MWe >= 20) of 0.5 or more. Our prior (1-6 GWe) straddles this line, so the first fit decides it.
2. **No decision lift.** Replay lift below 1.2x over "lock the USGS top 10%" at every budget. Switch to a pure land-first strategy.
3. **Not identifiable.** SBC variance ratio on N above 0.8. Do not kill; make the designed two-detector survey mandatory.
4. **Calibration fails.** Held-out 90% T(z) coverage below 80%, or reliability slope below 0.5 on the first 200 visits.
5. **Extraction fails.** Median gradient error above 20%, or fewer than 1,000 new readings more than 3 km from known systems.
6. **Sensors cannot move the answer.** Sensor-shrinkable share of the regional band below 30%. Then the company is a plain land bank.
7. **Rights cost breaks.** Options above $20/ac, or more than 70% refusal.

**Sensor-level (this memo):**
8. Dart field floor above 0.4 W/m2 per dart, or Granite Springs not separable from control at 12 months.
9. Dart gain over the logged 2 m probe below 1.5x.
10. BLM rules dart campaigns are not casual use and fewer than 20 private or own-lease target sites a year are available.
11. Combined dart plus well-visit sensitivity below 0.3 under lidded or swept masks in more than half of target provinces (from `MODEL.md` kill 6). Then shift budget to hand-placed E-MT and hired push holes.

Untested ML lift is never by itself a kill.

---

## 10. One-line answer

Build the SENTINEL-COX model (a discovery-thinned Cox count inside a value-of-information land engine, fed by AI-extracted old logs), and build one new sensor, a clustered 3 m logging heat-flux dart that runs in casual-use campaigns on BLM land and as a 12-month record on optioned ranches, while the ranch-well drop-probe visit with a helium sampler stays as the way we sign the rights.
