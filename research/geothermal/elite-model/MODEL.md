# MODEL.md: the elite geothermal prospecting model (SENTINEL-HELM)

Date: 24 Oct 2026. Chief-architect synthesis of 40 literature reviews (`evidence/L01`-`L40`), 10 designs (`designs/D01`-`D10`), 30 red-team reviews (`redteam/`) and 3 judges. It improves on `../model/MODEL.md` (SENTINEL-COX v1) and serves the business in `../MEMO.md`. The shared web-search budget was used up before this file was written, so no new searches ran. Numbers come from the L-files, the designs and the red teams, which cite primary sources. My own arithmetic and anything not re-checked is marked (unverified).

Working name: **SENTINEL-HELM** (SH). HELM is the decision spine (D05). SENTINEL is the belief it runs on (SENTINEL-COX v2-lite from D01, with the play factor and failure ledger from D07 and play programs from D09).

---

## 1. Verdict in five lines

1. We build a **decision engine first** (HELM-lite): each night it asks which next dollar of land, sensing or drilling adds the most portfolio value, and when to stop measuring and lock the right.
2. It runs on a **pluggable, play-risked belief**: an effort-thinned Cox count, censored temperature columns calibrated on tens of thousands of real T(z) readings, a latent play factor so one cold hole re-prices its neighbours, and four play programs plus an "unknown" play.
3. It is fed by **agent extraction of archives nobody has keyed** (NDWR about 132k reports, CA OSWCR about 1.1M, NBMG 442 TG holes, CalGEM 2,008 TG holes, NDOM and DOGM files) into a bitemporal evidence graph, so every hindcast is point-in-time and leak-measured.
4. It is elite because it is **honest where others are not** (calibrated on censored T(z), not on about 280 existence labels; per-field contraction decides "buy" versus "sense"; a random field audit gives the only unbiased error rate) and **fast where it matters** (a revealed-rival model of Zanskar, leak-cost land routing and a measured lead-time metric).
5. Heavy world models (D04 TWIN, D03 STRATA, D08 UNDERCAST) are **not cut**. They enter in months 7-18 as plug-ins that must beat the spine on held-out T(z) log score, and meanwhile they run OSSE sensor choice on optioned ground.

---

## 2. Scoreboard and the pick

### 2.1 Totals

Judge totals are out of 25 each (75 max). Red-team scores are out of 25 per lens (data, science, edge; 75 max).

| ID | Design | J1 geoscience | J2 ML/calibration | J3 founder/edge | Judges /75 | RT data | RT science | RT edge | Red team /75 | Rank |
|---|---|---|---|---|---|---|---|---|---|---|
| D05 | HELM (decision-first, pluggable belief) | 20 | 20 | 19 | **59** | 17 | 17 | 17 | **51** | 1 |
| D07 | PLAYBOOK (discovery process + play risk) | 21 | 17 | 17 | **55** | 15 | 17 | 15 | 47 | 2 |
| D09 | KEYSTONE (play programs + case files) | 19 | 17 | 18 | **54** | 16 | 16 | 16 | 48 | 3 |
| D04 | TWIN-WEST (physics reanalysis) | 17 | 18 | 18 | **53** | 17 | 16 | 17 | 50 | 4 |
| D01 | SENTINEL-COX v2 (four-field Cox + Simformer + POMDP) | 18 | 18 | 16 | **52** | 15 | 16 | 15 | 46 | 5 |
| D02 | TRIBUNAL (agent council + likelihood judge) | 17 | 17 | 17 | **51** | 15 | 16 | 16 | 47 | 6 |
| D10 | CONCLAVE (expert bench + stacking) | 16 | 17 | 15 | **48** | 14 | 16 | 16 | 46 | 7 |
| D03 | STRATA-West (masked any-to-any foundation model) | 15 | 16 | 14 | **45** | 15 | 16 | 16 | 47 | 8= |
| D06 | HEARTHNET (token fusion + PU) | 15 | 16 | 14 | **45** | 15 | 16 | 16 | 47 | 8= |
| D08 | UNDERCAST (diffusion reanalysis) | 15 | 16 | 14 | **45** | 16 | 16 | 16 | 48 | 8= |

No red team found a fatal flaw in any design. Every design's red teams converged on the same four fixes: calibrate on censored T(z), report per-field contraction, model the real rival (Zanskar) from its revealed actions, and measure lead time.

### 2.2 The pick: spine plus grafts

All three judges, separately, recommended the same shape: **HELM-lite as the spine, SCX2-lite as the belief, PLAYBOOK's play factor and failure ledger, KEYSTONE's play programs and case files, and the heavy world models as months 7-18 plug-ins.** I adopt it, with the grafts below.

| Graft | From | Why it is in v1 | What we cut from the source design |
|---|---|---|---|
| Belief plug-in interface (sample / predict / update / falsify); Pandora reservation values; one-step EVSI; depth-2 POMCPOW only inside shared-play groups; lease clocks; leak-cost channel choice | D05 | The only design whose basic question is the business question. Science can improve monthly without rewiring the business. | BetaZero, Brown-Smith bound (months 9-12, synthetic diagnostic only), full portfolio POMDP |
| BEL direct-forecast flows for 2 m probe, TG hole and E-MT | D05 | Makes EVSI a millisecond call per cell | Flows for other sensors until month 7+ |
| Bitemporal evidence graph with valid_time, known_time, channel, location error, extraction sigma; freeze-legality card per layer | D01, D09 | Without it every hindcast leaks | RDF export, full ontology until needed |
| Effort-thinned Cox with Fithian shared effort from signal-blind channels only, fitted at province level with 3-4 channels | D01, D07 | Turns "unlabelled" into "unsearched"; explains Nevada's flat creaming curve | Per-play channel betas (not identifiable) |
| Analytic Tier-1 censored column likelihoods, warm-started from In-Context Earth (ICE) | v1, D06, D01 | Heat is the one field with thousands of labels | Simformer column engine (months 7-18) |
| Four fields (heat, pathway, fluid, cap), each with its own data; existence labels fit only 4-8 coupling weights | D01 red-team fix | Makes the product identifiable | Fields without data stay prior and are labelled so |
| Latent play factor plus local factor per prospect; play-concentration cap | D07 | One cold hole re-prices its neighbours, as a geologist would | Per-play counts |
| Province-level multi-channel discovery-process model | D07 | Counts what is left; tells us which province and channel to fund | Play-level counts, size-bias per channel |
| AI-extracted failure-mode ledger as a noisy latent; calibrate only total Pg and outcome class | D07, D09 | Uses every dry and cool hole | Element-by-element isotonic calibration |
| Play templates B1-B4 plus max-entropy "unknown" as NumPyro programs; masks need positive evidence | D09 | Explicit, auditable geology; stops "mask rescue" of every negative | B5-B7, EGS, arc, rift templates until month 7+ |
| Per-parcel case file with leave-one-out and Shapley fact attribution, cited to page and bbox | D09 | Buyer data room and internal audit | "Exact" Bayes-factor claims |
| Archivist and Skeptic agents; challenge-as-priced-sensor; upflow-offset density per prospect | D02 | Agents add most as archivists and skeptics, not as probability engines | LLM council BMA; other roles until they beat an auto-enumerator |
| Stacking by held-out T(z) log score with Thresholdout and a sealed vault province; shrink to the Cox model outside the data hull | D10 | Combines plug-ins without double counting | Ten-expert bench |
| Revealed-rival model of Zanskar (nominations, TG permits, water filings, GeoCore replica) | all edge red teams | Edge is "high our-posterior, low their effort" | Public-only "crowd" refit as the only rival |
| Per-parcel title latent (surface, mineral/heat estate, state regime, prior claims) | D01 edge red team | Routes targets to ranch and state land where rivals do not look | none |
| Lead-time metric and design-based random field audit | all red teams | The only honest measures of edge and of the low-score region | none |
| Per-sensor observation operators and OSSE sensor choice; co-located E-MT plus TG pairs | D04 | Best long-run sensor logic; builds our private resistivity-temperature pairs | West-wide twin until months 7-18 |
| HEARTHNET-small T(z) field layer | D06 | A second heat expert for stacking | End-to-end PU existence |

**Why D05 over D07 as spine, though Judge 1 put D07 first.** D07 is the better risk language, and we keep it whole in the book and the case files. But D07's core engine (the per-play discovery model) is not identifiable at play level, and its ranker is the same model class Zanskar runs. D05's interface lets D07's parts plug in without making them load-bearing for the business. D05 was also the only design all three judges scored at 19-20.

**Why not a foundation model first.** L04 shows the algorithm barely matters on gridded layers with about 280 positives. Per-voxel contraction away from wells will be low in the first six months. The 3D designs are a sensor-routing and pricing moat in year 2, not a land machine in month 2.

---

## 3. What changed versus SENTINEL-COX v1, and why

| Area | SENTINEL-COX v1 (23 Oct) | SENTINEL-HELM (this file) | Why |
|---|---|---|---|
| Decision engine | VOI-Bank: one-step, per-cell EVSI/$; fixed "3x holding cost" lock rule | HELM-lite: Pandora reservation value per parcel and play group; one-step EVSI everywhere; depth-2 search inside shared-play groups; lease clocks; leak cost; channel choice | Land is cheap (Nevada 2025 median win $3.50/acre, 37% at the floor; L37). The binding limits are leak, timing and deal-team hours, not dollars per acre. |
| Rival | None (crowd only implied) | Revealed-rival model of Zanskar plus a GeoCore LightGBM replica; edge = our RNPV minus replica RNPV on ground they have not touched | A public-only refit models the median bidder, not the informed one (D07 edge red team). |
| Heat | Hand-set 1D column kernels | Same analytic Tier-1 censored likelihoods, plus an ICE-warm-started conductive prior with typed BHT tokens; HEARTHNET-small as a second expert | ICE: 4.7 C US MAE vs 5.1 kriging; transfers with no retraining (L10). |
| Existence structure | One field plus one 4-state mask class | Four fields (heat, pathway, fluid, cap), each with its own data; archetype latent B1-B4 plus unknown; masks need positive evidence | v1 folded heat and permeability together; masks could explain away any cold hole. |
| Shared risk | None | Latent play factor plus local factor; play-concentration cap | A cold hole should lower its neighbours (L17). |
| Effort | 3 channels, effort as latent | Fithian shared effort from signal-blind proxies only; springs moved to the geology side as a joint species; province-level discovery-process model | D06 and D07 science red teams: effort built from springs leaks geology. |
| Labels | Graded ladder G1-G5 | Same, plus failure-mode ledger (no heat, hot-tight, outflow, masked, fossil, success) and rung ladder (desk anomaly, hot TG, hot intermediate well, flow test, bankable) | Turns hundreds of holes into graded labels. |
| Time | Freezes, purge and embargo | Bitemporal graph; freeze-legality card per layer; legal-only vs leaky hindcast gap reported | Derived products (INGENIOUS, USGS 2025, Faulds FSS) carry post-freeze knowledge (D05 science red team). |
| Main gate | Coverage plus replay of blind finds | Held-out T(z) log score and coverage on thousands of post-freeze readings; finds reported but not gating | About 8-15 post-2005 blind finds give no power (D05 data red team). |
| "Buy" versus "sense" | EVSI only | Per-field contraction: cells whose posterior barely moved from prior are never bought, only sensed | Stops buying on prior. |
| Buy-list error rate | Conformal FDR on existence | Conformal selection on a measurable outcome (T at 1 km above 120 C), with covariate-shift weighting; existence FDR only from a random field audit | Exchangeability fails in unexplored ground (L27). |
| Track record | Hashed forecasts | Same, plus Sodir-style lookback with volume bias tracked separately, EVSI calibration as a predictive check, and lead-time ledger | Buyers pay for verifiable records (linkage principle; L37). |
| Agents | Extraction | Extraction, archivist, skeptic, dating, title, rival-watch, case-file writer, field planner; never edit the scorer | L39: agents fail silently; L22: they are best at reading, not deciding. |

Kept from v1, unchanged: the fixed M34 RNPV/acre economics, USGS and Coolbaugh totals out of the fit, the Ranch Well Sentinel, the two-detector calibration campaign, and every v1 kill condition.

---

## 4. Target variables and decision outputs

### 4.1 Grids and units
- **Cells:** 500 m equal-area (EPSG:5070), refined to 250 m inside the >1,430 Faulds favourable structural settings (FSS) and on optioned parcels. Existence field on a 2 km mesh.
- **Prospects:** FSS polygons (median 13.4 km2), AI-mapped hidden FSS, and basin-hosted polygons for the 17% of known systems with no FSS (L02).
- **Plays (for the shared factor):** archetype x province x depth band, collapsed to about 10-15 archetype-province groups for fitting (D07 data red team).
- **Parcels:** PLSS 40-acre aliquots and assessor parcels via a crosswalk.

### 4.2 Physical targets (posterior draws, not points)
| Target | Form | Main data |
|---|---|---|
| T(z) at 0.5, 1, 1.5, 2, 3 km | 128 ordinal bins | censored T(z) readings, BHT, TG, 2 m |
| psi = P(upflow within 2 km), by archetype | probability | Cox count + all fields |
| Heat, pathway, fluid, cap field values | latent log-fields | each its own data (Section 5) |
| Archetype | B1 shallow outflow, B2 range-hosted, B3 basin-buried capped, B4 cold-aquifer lid, unknown | play programs |
| Upflow offset vector | 2D density | chemistry, heads, T-log shape |
| Failure-mode distribution | {no heat, hot-tight, outflow, masked, fossil, success} | failure ledger |
| Size mark | MWe P10/P50/P90 with 0.5-0.7x haircut until our lookback exists | USGS 2008 triangles, flow tests |
| P_det(t) | probability the system is already known to someone | effort channels |
| Rival effort | intensity of Zanskar and others' activity | revealed-rival model |
| Per-field contraction | prior-to-posterior KL for each field | computed |

### 4.3 Value targets
RNPV/acre with three buyer heads (D05): hydrothermal (Ormat-type), EGS (P(T >= 200 C at <= 4 km), isotherm depths, stress), closed-loop (conductive T at 3-6 km). Commercial chance Pc = Pg x P(MW > minimum economic size). Rung probabilities P(reach rung k). All economics are fixed, versioned code with scenario axes for price, ITC and recovery factor.

### 4.4 Decision outputs (nightly, or on watcher triggers)
1. **The book.** For each parcel: best next action, EVSI/$, reservation value, leak cost, lease or option clock, channel (ranch option, state first-file, leftover BLM, nomination).
2. **Buy list** with a stated error rate on T(1 km) > 120 C.
3. **Sensor list:** cells routed to sensing because contraction is low, with the weakest field named.
4. **Rival map:** where Zanskar is active, predicted next-quarter nominations.
5. **Case files:** per prospect, for the data room.
6. **Regional report:** undiscovered systems per province by size class, F95/F50/F5, with contraction stated.
7. **Ledger entries:** hashed forecasts before every sale, field season and hole.

---

## 5. Architecture

### 5.1 Diagram

```
SOURCES (all 17 SCHEMA classes)          AGENT DATA PLANE (never edits scorer)
keyed layers | scans | permits | filings  fetch | extract x5 | date | title | rival-watch
          |                                         |
          v                                         v
+-----------------------------------------------------------------------------+
| L0  BITEMPORAL EVIDENCE GRAPH  (GeoParquet + Zarr + DuckDB)                 |
|  fact = value, sigma, censor bound, loc_err, channel, valid_time,           |
|         known_time [interval], source hash, page+bbox, public_flag          |
|  negatives first-class | contradictions queue | freeze-legality card/layer  |
+-----------------------------------------------------------------------------+
          | point-in-time join at freeze t*                    |
          v                                                    v
+--------------------------------------------------+  +------------------------+
| L1  BELIEF PLUG-INS  (interface: sample/predict/  |  | L1r RIVAL + TITLE      |
|     update/falsify)                               |  | Zanskar effort process |
|  P1 SCX2-lite (play-risked SENTINEL):             |  | GeoCore replica RNPV   |
|   a. heat: ICE prior + Tier-1 censored columns    |  | nominations forecast   |
|   b. pathway: stress MC, slip age, LC notes, He   |  | title latent / parcel  |
|   c. fluid: mixing chemistry, heads               |  +------------------------+
|   d. cap: MT ensembles, AEM, aquifer evidence     |           |
|   e. archetype programs B1-B4 + unknown (NumPyro) |           |
|   f. Cox count, Fithian shared effort (blind)     |           |
|   g. play factor z_p + local factor u_j           |           |
|   h. failure-mode latent (ledger)                 |           |
|  P2 HEARTHNET-small T(z) field expert             |           |
|  P3 GeoCore-style LightGBM-PU control             |           |
|  [7-18 mo] P4 TWIN tiles, P5 STRATA decoders      |           |
|  STACKING per target by held-out T(z) log score   |           |
|  (Thresholdout, vault province, shrink to P1)     |           |
+--------------------------------------------------+           |
          | joint particles + per-field contraction            |
          v                                                    |
+--------------------------------------------------+           |
| L2  BEL LAYER                                     |           |
|  GHOST Tier-1 synthetic worlds (planted systems,  |           |
|  effort, rivals, sales); held-out falsification;  |           |
|  direct-forecast flows: 2 m, TG, E-MT -> value    |           |
|  off-manifold gate -> explicit likelihood         |           |
+--------------------------------------------------+           |
          v                                                    v
+-----------------------------------------------------------------------------+
| L3  VALUE LAYER: RNPV/ac (hydro/EGS/closed-loop), Pc, rung prices,          |
|     E[value | win], edge = ours - replica, leak cost, contraction gate       |
+-----------------------------------------------------------------------------+
          v
+-----------------------------------------------------------------------------+
| L4  HELM-lite PLANNER: Pandora index (parcel + play group); one-step EVSI;  |
|     depth-2 POMCPOW in shared-play groups; submodular batching + routing;   |
|     budget = people-hours + leak + cash; play-concentration cap             |
+-----------------------------------------------------------------------------+
          v
 BOOK | buy list (conformal, T1km>120C) | sensor routes | case files | ledger
          v
+-----------------------------------------------------------------------------+
| L5  LEDGER + LOOKBACK: hashed forecasts, rung outcomes, failure tags,       |
|     EVSI PIT checks, lead time, field-audit results -> refits of L1, L2     |
+-----------------------------------------------------------------------------+
```

### 5.2 Components and methods

**L0 Bitemporal evidence graph.** GeoParquet tables for nodes and edges, COG for rasters, Zarr for posterior draws, DuckDB as the only query engine (L35). Each fact carries `valid_time` and `known_time`. Known_time is stored as an interval from a dating agent (earliest citing document, permit date plus statutory confidentiality, scan date). Hindcasts use the late end. A leakage agent re-scores with shifted intervals (D10 data red team). Every derived layer (INGENIOUS, USGS 2025 favourability, Faulds FSS, AlphaEarth, GeoDAWN) gets a freeze-legality card: legal for which freeze, and why. Every hindcast is run twice, legal-only and with leaky layers, and the gap is reported as a measured leak. Dry holes, cold wells, "temperature absent" reports and lease status are first-class facts. Contradictions (a warm well beside a cold TG hole) go to the sensor list as cheap targets.

**L1-P1a Heat field.** Conductive prior from an ICE-style in-context transformer (O'Malley et al. 2026, arXiv 2605.16665; 4-layer, about 830k parameters, 128 ordinal bins). We fine-tune it with typed tokens: raw BHT plus shut-in time, era, mud, extraction sigma, location error. Pretraining data: KGS (212k BHTs), Alberta, OZTemp, UKOGL. The convective part comes from the analytic Tier-1 column-plus-plume model (GHOST, about 1 ms per run). Each reading enters through its own censored likelihood: equilibrium logs, censored TG holes, BHT with ANN SFT correction, driller-report temperatures, 2 m with seasonal nuisance. Variance grows below the deepest nearby calibration well. Calibration data: thousands of censored T(z) readings, not existence labels.

**L1-P1b Pathway field.** Monte Carlo slip tendency under a sampled stress tensor (L25), a fault sealing clock (P(open) decays with time since last slip, resets with Quaternary offset, microseismicity and InSAR strain; L40), AI-extracted lost-circulation and flow-test notes, and helium R/Ra as a pathway-only signal (L26). FSS type priors: DTZ about 4.8x, pull-apart about 2.2x, step-over about 0.85x (L01, L09).

**L1-P1c Fluid field.** Mixing-aware geothermometer posteriors per water sample (PHREEQC/GeoT forward runs, lab and era bias terms; L26). NWIS heads and recharge for flow direction and the up-gradient offset.

**L1-P1d Cap field.** Public MT stations inverted as RTO or trans-D ensembles with false-conductor classes (basin clay, brine, fossil cap; L13), AEM where it exists, aquifer and carbonate maps. Masks (B4 lid, outflow sweep) need positive evidence: aquifer maps, NWIS heads, recharge. A mask cannot be invoked just to explain away a cold hole (D09 data red team). The share of each negative's log Bayes factor absorbed by a mask is reported.

**L1-P1e Archetype programs.** B1-B4 plus a max-entropy "unknown" play, each a NumPyro program of a few hundred lines sharing sub-programs (column, stress, chemistry, mask). B3/B4 are pooled in v1 if they have too few members. The unknown play's weight is set from the hindcast "surprise rate": the share of post-freeze finds whose archetype the model could not represent at the freeze (D05 science red team). Templates are bitemporal objects: re-derived from literature sliced at the freeze date; the gap between time-sliced and today's templates is reported as structural leakage.

**L1-P1f Existence count.** Log-Gaussian Cox process: log lambda_a(s) = province offset + w_H H + w_P P + w_F F + w_C C + Z(s). Existence labels fit only the 4-8 coupling weights w, not the fields. Thinning: P_det(s,t) = 1 - exp(-sum_c q_c E_c(s,t)). Effort E_c is a Fithian shared field built only from signal-blind proxies: roads, survey footprints, permit dates, off-target oil and gas holes, mining-claim filings, the AlphaEarth "built infrastructure" direction (L18, L20). Springs are modelled as a joint species sharing the pathway and fluid fields, not as effort. A Diggle preferential-sampling term corrects warm bias in drilled valleys. A province-level multi-channel discovery-process model (D07 [F], 3-4 channels: springs, non-geothermal holes, geothermal surveys, ours) gives undiscovered counts by size class. It uses one size-bias beta with channel offsets, a strong prior from about 200 global field histories (WGC country updates, unverified count), and SBC at n = 20 marks before any count is quoted. Our own designed sensor cells are a new clean channel with exactly known effort.

**L1-P1g Play factor.** Each prospect's element state mixes a play factor z_p and a local factor u_j (Van Wees 2008; Martinelli 2013, from L17). A cold hole at j moves z_p and so every j' in the play. Shared-element weights are learned from the ledger and capped until the lookback calibrates them, so one hole cannot over-swing a play.

**L1-P1h Failure-mode latent.** Each hole's outcome class is a noisy latent inferred from extracted lost circulation, flow tests, T-log shape (conductive, reversal, isothermal) and alteration, by an N=5 self-ensemble classifier. Only total Pg and the coarse outcome class are calibrated. The five-row element card is shown as a posterior decomposition with contraction per element. Element dependence uses a shared latent, not a product of independent chances (D07 science red team).

**L1-P2 HEARTHNET-small.** A small Perceiver over raw-reading tokens within 20 km, ICE-warm-started, trained with density-matched token thinning and a firewalled effort encoder (D06). It is a second heat expert for stacking only, with no existence head.

**L1-P3 Control.** A rebuilt GeoCore LightGBM on INGENIOUS layers (Grujic et al., SGW 2025). It is both the "beat this" baseline and the Zanskar replica.

**Stacking.** Per-target hierarchical stacking (Yao et al. 2018), fit by held-out log score on kNNDM spatial blocks and walk-forward time splits. Weights shrink to P1 outside the area of applicability. Expert likelihoods are never multiplied. Promotions pass a Thresholdout reusable holdout (Dwork 2015) and a sealed vault province (Oregon in v1) that a human opens quarterly.

**L1r Rival and title.** Agents scrape Zanskar-affiliate MLRS nominations and assignments, BLM all-bids, NDOM and Utah DOGM TG permits, county drilling and water-right filings, DOE awards (16 DE-FOA-0003472 sites; L07) and job posts. A dated point process of their effort is fitted. It is scored by forecasting next quarter's nominations. The title latent per parcel holds surface owner, mineral and heat estate owner, state heat regime (heat as mineral vs water), prior leases and claims, from BLM surface/subsurface layers, assessor rolls, county memoranda of geothermal lease and state statutes.

**L2 BEL layer.** 10^5-10^6 synthetic prospect tiles from GHOST Tier 1 with planted blind systems, dated effort, rivals and a sale calendar. Prior falsification uses only held-out basins and dense shallow summaries (2 m, water-well temperatures, spring chemistry), with power reported per cell and an "unfalsifiable" flag that earns a sensing bonus (D05 data red team). Shared latents are never pruned by DGSA. Direct-forecast conditional normalising flows for three sensors (2 m probe, TG hole, E-MT) map "data we could buy" to decision value, making EVSI a millisecond batched call. Deep ensembles of flows plus an off-manifold gate (classifier two-sample test or MMD) fall back to the explicit likelihood when real data look unlike Tier 1.

**L3 Value layer.** GETEM/SAM fork with belief-driven success and Lowry lognormal well costs (±50%). Bid = E[RNPV | we win], with informed-bidder count as a scenario axis (bid prices are floor-censored; D05 science red team). Edge = our RNPV minus GeoCore-replica RNPV. Leak cost = expected rise in rival posterior on our unlocked neighbours if we act publicly (legal descriptions go public 4-16 months before a sale; GAO-26-108040, L37). **Contraction gate:** a cell is buy-eligible only if prior-to-posterior KL on its limiting field passes a threshold; otherwise it is sense-only.

**L4 HELM-lite planner.** Pandora (Weitzman 1979) reservation value per parcel and play group. One-step EVSI/$ for every cell. Depth-2 POMCPOW (POMDPs.jl) only inside shared-play groups, where look-ahead pays (Martinelli-Eidsvik-Hauge: about 6% over one-step, 14.8% over naive; L15). Budget constraint is people-hours plus leak plus cash, because land is cheap (D05 edge red team). Field actions are batched per mobilisation by submodular greedy EVSI/$ with truck-route cost.

**L5 Ledger and lookback.** Every forecast hashed before the outcome. Every hole tagged by failure mode. EVSI calibration as a predictive check (PIT of each realised observation under `predict(action)`), plus a slope target of 0.7-1.3. Volume bias tracked separately from chance (Sodir: volumes 1.4-2.5x high; L17).

---

## 6. Data-class mapping

One row per class in `../datasets/SCHEMA.md`. Priority: P0 = needed for the PoC.

| Class | Entry mode | Latent or decision term informed | Priority | 2-3 key datasets |
|---|---|---|---|---|
| `thermal` | point-observation with censored likelihood; main calibration target | heat field, T(z) bins, EGS head | P0 | SMU/NGDS heat-flow and BHT compilation; OFR 99-425 TG holes (786 holes over 82 prospects); KGS 212k BHT for ICE pretraining |
| `wells` | text-to-extract and point-observation; effort layer for non-geothermal holes; failure ledger | heat, pathway (lost circulation, flow tests), failure latent, effort E_c | P0 | NDWR Well Driller Reports (146,235; about 132k without keyed T); NBMG WellLog scans (2,002 PDFs, 442 TG holes); NDOM well files (938 geothermal) and CalGEM (4,346 wells, 2,008 TG) |
| `geophysics` | posterior ensembles (RTO/trans-D) per MT station; gravity for basin depth; survey footprints as effort | cap field, basin depth, archetype; E-MT sensor action | P1 (P0 for MT in Nevada) | EarthScope/USArray MT EDIs (SPUD); PACES/USGS gravity; GeoDAWN aeromagnetics (legality card: post-2022) |
| `structure_stress` | prior covariates; FSS type priors; stress Monte Carlo; sealing clock | pathway field, play membership, prospect inventory | P0 | Faulds FSS polygons (>1,430; legality card: post-2010); USGS Qfaults; World Stress Map plus re-picked focal mechanisms |
| `seismicity` | Mc-thinned covariate; swarms and b-value | pathway field, local SHmax | P2 | ANSS ComCat; Nevada Seismological Lab catalogue; ML re-picks (months 7+) |
| `geology_geochem` | mixing-model likelihood per sample; He as pathway; lithology priors | fluid field, reservoir T, upflow offset, archetype | P1 | USGS/NBMG spring and well chemistry (NWIS-QW, NURE); DeAngelo 2025 geothermometer circulation depths (doi:10.5066/P14B8XOH); USGS geologic maps (SGMC) |
| `remote_sensing` | detection likelihood per sensor; lidar for FSS mapper; AlphaEarth PCs with infrastructure direction routed to effort | surface leakage, fossil vs live alteration, effort | P2 | 3DEP lidar; EMIT/AVIRIS hyperspectral; AlphaEarth embeddings (legality card: post-2017) |
| `hydrology` | positive evidence for masks; heads for outflow back-projection | cap/mask, upflow offset, fluid | P1 | USGS NWIS groundwater levels; principal aquifer and carbonate maps; NDWR/Utah water-right filings (also rival signal) |
| `labels` | dated, channel-tagged finds for the Cox count; failure ledger; rung ledger; hold-outs | psi, catch rates, Pg, rung probabilities | P0 | USGS Great Basin inventory (205: 28 plants, 78 known, 99 probable); L31 blind-case table (11 US cases); failure seeds (Reese River 10 cold TG, Argenta, Gabbs, NDOM P&A 124) |
| `land_rights` | planner state (holdings, clocks, channels); title latent; never a geology feature | action set, holding cost, leak cost, rival effort | P0 | BLM MLRS cases and nominations; BLM all-bids reports (about 2007+); county assessor rolls and recorder memoranda of geothermal lease |
| `constraints` | hard action mask and RNPV haircut | which parcels can be bought or built | P1 | PAD-US; BLM sage-grouse habitat; tribal and DoD lands |
| `infrastructure_market` | value layer | P(build), price scenario, buyer head | P1 | HIFLD transmission and substations; interconnection queues (LBNL Queued Up); EIA-860/923 |
| `cost_economics` | value layer and action costs | RNPV/acre, action cost, stopping rung | P0 | NREL ATB; GETEM/SAM; Lowry 2017 drilling cost curves |
| `corporate_transactions` | revealed-rival model; exit prices per rung; outcome table | edge, bid shading, rung prices | P0 (rival), P1 (exit) | BLM sale results (Pumpernickel step-out $2 to $232/acre); Ormat 10-K, Fervo S-1; Crump Geyser farm-in (SEC exhibit) |
| `literature_text` | text-to-extract: logs, failure causes, conceptual models, first-signal dates | labels, failure ledger, archetype library, known_time | P0 | OSTI/GDR DOE project reports (PFA Phase 2-3, Granite Springs GDR 969); GRC and Stanford SGW papers; NBMG open-file reports |
| `global` | ICE pretraining; hierarchical priors for size and play chance; out-of-domain tests | heat prior, size prior, resistivity-to-T link | P1 | Alberta AER/AGS temperatures, OZTemp, UKOGL (ICE sets); NZ/Iceland/Kenya field histories (WGC updates); IHFC global heat-flow |
| `models_products` | baselines, crowd and replica inputs, down-weighted priors; never frozen labels | benchmark to beat; rival replica | P0 | INGENIOUS Great Basin layers; USGS 2025 favourability; ICE and Stanford temperature-at-depth grids |

---

## 7. The agent layer

Agents read, date, extract, propose and plan. They never set probabilities and never edit the scorer, the economics or the test sets (L22, L39). Every agent output is a typed proposal that must pass a gate.

| Agent | Job | Guard against hallucination | Guard against leakage |
|---|---|---|---|
| **Extractor** (Stage 0) | VLM header reader plus SAM-style curve tracer on scanned T-logs, driller reports, well files; N=5 two-family self-ensemble; median is the value, spread is sigma | pass^5 >= 95% on a planted-trap golden suite; scored against OFR 99-425 and SMU duplicates; unit and datum contracts | outputs carry source scan date; no model products as inputs |
| **Dating agent** | assigns known_time intervals from first citation, permit confidentiality, scan date | cites the document; confidence stored | hindcasts use the late end; leakage agent shifts intervals |
| **Archivist** (from D02) | reads unstructured reports for conceptual models, first-signal dates, failure causes, upflow anchors | every fact cites page and bbox; Skeptic re-reads | only cards dated before the freeze are admitted |
| **Skeptic** | challenges each top prospect: files a query, a simulation or a priced sensor that would move the posterior | challenges are scored by the non-LLM likelihood, not by debate | sees only legal facts for the freeze |
| **Conceptual modeller** | drafts new play templates and rules from the literature | admitted only on held-out log-score gain, under Thresholdout | literature sliced at freeze date |
| **Title agent** | builds the per-parcel title latent; reads state statutes on heat ownership | cross-checks two sources; flags split estate | n/a |
| **Rival watcher** | scrapes MLRS, all-bids, TG permits, water filings, DOE awards, job posts | structured fields only; nightly diffs | rival data never enters geology fields |
| **Field planner** | turns the sensor list into routes, permits, landowner letters, kit lists | human approves every mobilisation; compliance check against 43 CFR 3200 before any nomination | n/a |
| **Leakage red team** | diffs every feature against its publication date; re-runs hindcasts with illegal layers on | fails the run on mismatch | its job |
| **Case-file writer** | writes per-prospect case files from the model's attributions | text must quote model numbers and cited facts only; automated number check | n/a |
| **Coding agents** | build ETL, tests, simulators, harness | humans own the scorer and test sets | test sets hashed and sealed |

**Contamination.** LLMs may remember famous systems. Inside hindcasts, agents only extract; they never reason about prospects. A contamination probe asks agents to name systems from blinded coordinates; prospects where they succeed are excluded from agent-lift claims (D02 science red team).

**Agent lift is measured, not assumed.** The Archivist and Skeptic roles are kept only if they beat an auto-enumerator that samples cards along the fault graph with the same judge and compute.

---

## 8. Uncertainty and validation ladder

Uncertainty lives in posterior particles from each plug-in, in stacking weights, in the unknown-play mass, and in scenario axes for price, size haircut and informed-bidder count. Every map shows per-field contraction, and prior-dominated cells are greyed out.

Validation runs from cheapest and most honest to most expensive. A release must pass every gate above it.

| Gate | Test | Pass bar | Notes |
|---|---|---|---|
| G0 Extraction | 1,000 random NDWR and OSWCR pages; NBMG scans scored against OFR 99-425 and SMU | median gradient error <= 10%; >= 80% usable curves; pass^5 >= 95%; yield of depth-tagged readings measured and reported | v1 kill 5 still applies |
| G1 Synthetic | SBC and TARP on GHOST worlds; N_hidden recovery in planted worlds | SBC ranks uniform (KS p > 0.05); N in 90% interval >= 85% of the time | Called an "inference check", not proof of realism |
| G2 Mismatched worlds | plan on Tier 1, score on TOUGH3 worlds and on agent-invented archetypes | mismatched lift reported as the headline; well-specified lift as a ceiling | D05 science fix |
| G3 Held-out T(z) (main gate) | log score and 90% coverage on thousands of post-freeze TG, NDOM, NBMG and water-well readings, kNNDM blocks, freezes 2005 and 2015 | coverage 85-95% overall and >= 80% in the lowest-effort stratum; log score beats ICE alone, kriging and the GeoCore replica, block-bootstrap CI above 0 | weighted by inverse drilling propensity |
| G4 Leak gap | legal-only vs leaky-layer hindcast | gap reported; claims made on legal-only numbers | |
| G5 Contraction | per-field prior-to-posterior KL map | no buy on a cell below threshold on its limiting field | threshold set on synthetic worlds |
| G6 Play factor | leave-one-hole-out within play groups | neighbour log score improves when the held-out hole is added; no over-swing (PIT uniform) | |
| G7 Discovery counts | CSEP N-test on post-freeze counts per province; sharpness bar | p > 0.05 and 90% interval width <= about 2x the observed count | counts never quoted per play |
| G8 Buy list | conformal selection on T(1 km) > 120 C with covariate-shift weights (Tibshirani 2019) | realised false-discovery rate on held-out wells <= stated rate (target 20%, unverified level) | existence FDR only from G9 |
| G9 Random field audit | about 30 cells per score decile, one cheap sensor each (2 m line or Sentinel) | reliability slope 0.7-1.3; low deciles truly low | the only unbiased check of the low-score region; about $30-60k (unverified) |
| G10 EVSI calibration | PIT of realised observations under `predict(action)`; slope of predicted vs realised value moved | PIT KS p > 0.05; slope 0.7-1.3 | |
| G11 Rival model | forecast next quarter's Zanskar nominations by section | AUC >= 0.7 (unverified bar) | |
| G12 Lead time | median months between our top-5% call and the first public signal (nomination, permit, press), and acres lockable per $ before signal | median >= 12 months (unverified bar) | dated from the evidence graph |
| G13 Lookback | hashed forecasts vs rung outcomes | Pg reliability slope 0.8-1.2 after 50+ outcomes | volume bias tracked separately |

**Reported but never gating:** blind-find capture in top 1/5/10% of area (about 8-15 post-2005 Nevada blind finds give no power), BLM sale replay, Brown-Smith gap (synthetic diagnostic only).

---

## 9. How it drives rights, sensors and sales

### 9.1 Rights
- **Lock rule.** Lock when the parcel's value exceeds its Pandora reservation value and the contraction gate passes. Land is cheap, so the real question is "lock now" versus "leak now".
- **Channel choice by leak cost and title.** High edge and high leak: private ranch heat option or state first-file. Low leak: leftover BLM parcel or nomination. Split-estate parcels follow the title latent. Nominations are filed by a watcher agent the week a parcel crosses the rule, after a compliance check.
- **Bid.** E[RNPV | we win] minus winner's-curse shading, with informed-bidder count as a scenario axis.
- **Where to point.** Edge = high our-posterior and low rival effort. "High geology, blind to every past channel" (D07) is the lead-time score: buried B3, lidded B4, private ranch land, and provinces outside Nevada.
- **Book limits.** Play-concentration cap, because the size tail is power-law (top 3 Nevada fields hold 44% of MW; M33).

### 9.2 Sensors
- **Weakest field picks the sensor (D09).** Heat-limited: 2 m arrays, darts, TG holes. Pathway-limited: helium samplers, geophone nodes, earth-tide loggers. Cap-limited or lidded: E-MT. Contradictions: re-log or a Sentinel visit.
- **EVSI/$ over the whole play.** Through the play factor, one hole informs its neighbours, so the planner may drill the most informative hole first, not the best.
- **First spend buys sensor truth.** The v1 calibration campaign (about 20 known blind systems, about 40 cold controls, two detectors per cell) plus the G9 random audit. Every later EVSI depends on the reliability matrix.
- **Private resistivity-temperature pairs.** Every E-MT carpet is co-located with a TG hole (D04). These pairs train the cap operator that nobody else has.
- **Our sensors are a new channel.** If the discovery curve does not step up when we deploy, that is a kill signal (D07).

### 9.3 Sales and the data room
- **Case file per prospect (D09):** archetype posterior; weakest field; top facts for and against with leave-one-out and Shapley attributions, cited to page and bbox; contraction per field; failure-mode distribution; upflow-offset density ("buy the up-gradient acre, not the warm well", D02); rung probabilities; hashed forecast history.
- **Buyer language (D07):** Pc, risked MW, EMV, and AGRCC/CanGEA-style categories (L37). Verified disclosure raises sale price (linkage principle).
- **What we sell and keep.** Sell non-competing layers (conduction-only, EGS isotherms, lagged hydrothermal maps). Keep psi and offset vectors private until rights are held (D04 edge red team).
- **Exit rung.** Sell or farm out at the rung where P(next rung) x price uplift no longer pays for the next action. Exit prices run as a scenario axis until our own sales exist.

---

## 10. Edge versus Zanskar and the moat over time

**What Zanskar has (L05).** GeoCore LightGBM on INGENIOUS (679,826 H3 cells; 6,009 positives against 148 negatives; the only skill figure is 94.5% of 309 hot springs in the top half of favourability). A private 27,000-sample compilation. Its own TG and intermediate wells (Big Blind about 823 m, Pumpernickel about 762 m). Job posts for data assimilation and VOI. Owner-operator, mostly on BLM ground.

**Where we win, ranked by durability:**
1. **Archives nobody keyed.** About 132k NDWR reports and 1.1M OSWCR reports without keyed temperature. A VLM pass costs about $300-13,000 for both states (L21, unverified). This turns tens of thousands of wells into censored observations, against GeoCore's 148 negatives.
2. **Ground no channel has looked at.** High geology, near-zero past effort, scored by lead time, not by rank.
3. **Private and state land.** Ranch heat options and state first-file do not leak through BLM nominations. Zanskar's footprint is BLM-heavy.
4. **Knowing the rival.** We model Zanskar's revealed effort and score ourselves on forecasting it. Edge is defined as "our value minus replica value" on ground they have not touched.
5. **Our own sensor rows**, especially co-located E-MT plus TG pairs and random-audit cells. These are calibration data no public model has.
6. **A hashed track record.** Zanskar publishes no hit rate. We publish calibration and lead time.
7. **Model class is not the edge.** Zanskar can copy an effort term or a censored loss within a quarter. That is why the plug-in design matters: we absorb any better science, theirs included.

**Flywheel.**
```
extract archives -> better heat posterior -> sense where contraction is low
      ^                                              |
      |                                              v
 lookback + ledger <- outcomes on locked land <- lock before signal (lead time)
      |                                              |
      +-----> buyer trust -> higher exit prices -> more cash for sensors
```
Each turn adds private, dated, effort-known observations. After about 12-18 months these feed the D04 tile twin and STRATA decoders, which then make sensor choice sharper again.

---

## 11. Build plan

Principle: acres get locked in months 1-3 on SENTINEL-COX v1 with a static lock rule. HELM wraps it month by month.

| Period | Build | Business output |
|---|---|---|
| **Months 0-1** | L0 graph for NV and UT with known_time; dating and leakage agents; Stage 0 extraction on NBMG 442 TG holes, NDOM, and a 1,000-page NDWR/OSWCR yield sample; SENTINEL-COX v1 wrapped as plug-in 1; GeoCore replica as plug-in 3; watcher agents on MLRS, permits, GDR; title agent v0; first hashed forecast (Granite Springs 68-02) | first ranch letters on top-decile private parcels; first state first-file and leftover-BLM picks by static rule |
| **Months 1-3** | ICE fine-tune with typed tokens; four-field SCX2-lite in NumPyro with Fithian blind effort; play factor; B1-B4 + unknown programs; failure ledger v1 (about 300-1,000 holes); revealed-rival model v0; Pandora index + one-step EVSI; G0-G5 run on the 2015 freeze | first options signed; nominations filed by watcher on rule-crossing; rival-forecast scoring starts |
| **Months 3-6** | GHOST Tier-1 world bank; flows for 2 m, TG, E-MT; depth-2 POMCPOW in play groups; province-level discovery model with SBC; HEARTHNET-small; stacking with Thresholdout and Oregon vault; conformal buy list; case-file writer; calibration campaign and G9 random audit | first planner-chosen field season (about 100 actions, all pre-registered); first data-room packs; first lookback |
| **Months 6-12** | Archivist and Skeptic agents vs auto-enumerator; Simformer column engine with Kennedy-O'Hagan discrepancy; D04 TWIN-NV tiles on optioned parcels with OSSE sensor choice; extend to ID, OR, NM, AZ, CA; BetaZero and Brown-Smith as synthetic diagnostics | first rung sales or farm-outs; published calibration report |
| **Months 12-18** | Mini-STRATA decoders (50-100M params) for any-sensor EIG; full West; global transfer tests | sensor products and EGS-buyer layers |

**Team (v1).** Three core plus Dhruv: a Bayesian modeller (owns P1 and gates), a decision scientist (owns L2-L4), a data and agents engineer (owns L0 and agents). Dhruv leads land and rival. A part-time geothermal geologist adviser from month 1 and a part-time field technician from month 3. Coding agents write ETL, simulators, tests and solver glue. Add a simulation engineer and a second geologist at month 6.

**Compute and cost (unverified).**
| Item | Months 0-6 | Months 6-12 |
|---|---|---|
| LLM extraction and agents | $20-60k | $10-30k per year run-rate |
| Cloud compute (one 8-GPU node part-time, CPU burst) | $30-60k | $60-150k |
| Field: calibration campaign + random audit + first season | $150-400k | $0.5-1.5M incl. TG holes |
| Land and options | $50-200k | scales with book |
| Paid data (Regrid parcels etc.) | $10-30k | similar |

GHOST Tier 1: 10^6 tiles x 10 sensors at about 1 ms is about 3 CPU-hours (D05). ICE fine-tune: GPU-hours. NumPyro HMC per province: CPU-hours.

---

## 12. PoC: the cheapest test that shows the model works

**"Freeze-2015 Nevada-Utah duel."** Desk only. About $8-15k of compute and LLM calls, 6-8 weeks, one to two people plus agents (unverified cost). A separate $30-60k random field audit (G9) follows in months 3-4 if the desk test passes.

**Steps.**
1. Build the point-in-time NV + UT graph at known_time 2015, with legality cards. Run legal-only and leaky versions.
2. Extract NBMG 442 TG holes, NDOM files and a 1,000-page NDWR sample. Measure yield and error (G0).
3. Fit four contenders on the same legal inputs: (a) SCX2-lite with play factor and blind effort; (b) ICE alone; (c) universal kriging; (d) GeoCore LightGBM replica.
4. Score on post-2015 held-out temperature readings (TG, NDOM permits, DOE wells, water wells with temperatures), kNNDM blocks.
5. Play-factor test: leave one hole out per play group and check neighbour updates.
6. Lead-time test: for every post-2015 dated event (nominations, TG permits, discoveries such as Big Blind, Pumpernickel, Granite Springs), find when our top 5% first contained it, and the first public signal.
7. Rival test: fit the Zanskar effort model on 2015-2023, forecast 2024-2026 nominations.
8. Planner test on mismatched worlds: HELM-lite vs static top-10% lock vs one-step EVSI; plan on Tier 1, score on a TOUGH3 subset; ablate channel choice, leak cost and timing.

**Pass bars (pre-registered and hashed before step 4).**
| # | Bar | Pass |
|---|---|---|
| 1 | Extraction | median gradient error <= 10%, >= 80% usable curves, >= 1,000 new depth-tagged readings > 3 km from known systems |
| 2 | Calibration | 90% coverage 85-95% on held-out readings; >= 80% in the lowest-effort stratum |
| 3 | Skill | (a) beats (b), (c) and (d) on mean log score per reading, block-bootstrap 90% CI above 0 |
| 4 | Play factor | neighbour log score improves with the held-out hole in >= 60% of play groups; PIT uniform |
| 5 | Lead time | median >= 12 months ahead of first public signal on post-2015 events, with n reported (unverified bar) |
| 6 | Rival | 2024-2026 nomination forecast AUC >= 0.7 |
| 7 | Planner | on mismatched worlds, HELM-lite >= 1.3x systems per $ over static top-10%, and >= 5% over one-step EVSI, CI above 1 |
| 8 | Leak | legal-only skill is within the CI of leaky skill, or the gap is reported and claims use legal-only |

**Reading the result.** Bars 1-3 are the core. If they pass, buy land on the model from month 2. If 3 fails but 1-2 pass, the archive is still the moat; keep SENTINEL-COX v1 as the belief and push extraction. If 5 or 6 fails, edge is not proven; shift land effort to private and state ground where leak does not matter and re-test in a quarter. If 7 fails on the planner term only, keep one-step EVSI (D05 science red team kill rule: under 1.1x real lift, revert). Untested ML lift alone never kills.

---

## 13. Kill conditions and top risks

### 13.1 Kill conditions
v1 kills 1-8 (`../model/MODEL.md` Section 12) stand: too small (< about 2 GWe P50 bankable hidden resource on lockable land), no decision lift, not identifiable, calibration fails, extraction fails, sensor fails, sensors cannot move the answer, rights cost breaks (ranch options > $20/acre or > 70% refusal). New ones:

9. **No lead time.** Median lead time stays under 3 months after two refits. Then we are fast-following Zanskar; become a data and services company.
10. **Contraction is near zero almost everywhere.** If fewer than about 5% of high-prior cells pass the contraction gate even after extraction, the model is a sensor router, not a land picker. Become a sensing-first company that buys after measuring.
11. **Our channel does not step the curve.** After a year of designed sensing, the discovery rate per unit effort in our channel is no better than historical channels.
12. **Random audit contradicts the map.** G9 shows the bottom three deciles as hot as the top three. The belief is mis-specified; stop buying on it until fixed.

### 13.2 Top risks and AI-leveraged answers
| Risk | Why it bites | AI-leveraged answer |
|---|---|---|
| Known_time is fuzzy for 1970s-2000s data | leaks into hindcasts | dating agent with intervals; late-end rule; legal vs leaky gap |
| Archive yield is low (temperatures not in reports) | weak moat | measure on 1,000 random pages first; then aim at richer sources (NDOM, CalGEM, KGS-style log scans, mining NI 43-101 texts) |
| Pathway, fluid, cap have few labels | four-field product stays prior | own data per field; report contraction; our holes add labels; Archivist mines DOE flow tests |
| Deep-only archetype (Big Blind-type) has 1-2 examples | planner undervalues deep targets | wide archetype weights; hypothesis agents mine Zanskar talks and foreign analogues; stress-test regret in deep-heavy worlds |
| Rival copies tactics | edge shrinks | speed of loop; private sensor rows; title-led land; re-fit rival model each sale |
| Simulator bias | planner learns Tier-1 quirks | mismatched-world scoring; off-manifold gate; Kennedy-O'Hagan discrepancy from paired Tier-1/TOUGH3 runs |
| LLM contamination | agents "remember" answers | agents only extract inside hindcasts; contamination probe; auto-enumerator baseline |
| Reward misspecified (exit prices) | wrong sell rung | agent-built 500+ row outcome table from MLRS, permits, SEC filings; mining prospect-generator option terms (EMX, NI 43-101) as priors; scenario axis |
| Nomination strategy draws legal scrutiny | regulatory risk | compliance agent plus lawyer; prefer off-auction channels |
| Team scope | stall | HELM-lite only; everything else is a plug-in with a gate |

---

## 14. Open questions for the dataset catalogues

The four survey threads (subsurface, surface, business, global) must confirm these. Each one changes a pass bar or a priority.

1. **NDWR temperature yield.** What share of the about 132k un-keyed NDWR reports carry any temperature or "warm/hot water" note? Same for a sample of OSWCR. (Sets the archive moat size.)
2. **Post-2015 held-out readings.** How many dated temperature readings with depth exist after 2015 in NV and UT (NDOM permits, DOE wells, GDR uploads, TG holes)? Is it really thousands? (Sets G3 power.)
3. **NBMG scans.** Are all 2,002 WellLog PDFs downloadable in bulk, and how many of the 442 TG holes have full T-z curves rather than single gradients?
4. **CalGEM TG holes.** Are the about 2,008 TG holes and their logs online with dates and depths?
5. **Mining effort.** Can MLRS mining-claim filings by year, BLM Notices and Plans of Operations, and NI 43-101 drill metres be pulled at section level? (Key effort channel.)
6. **BLM data.** Are MLRS nominations attributable to nominator and dated? Are all-bids reports complete since about 2007?
7. **State and private land.** Which states' land offices publish geothermal lease lists? Which counties publish recorder indexes searchable for "memorandum of geothermal lease"? Regrid price and coverage for NV, UT, OR, ID, NM?
8. **Heat ownership by state.** Is geothermal heat a mineral, water or sui generis right in each target state? (Feeds the title latent.)
9. **MT coverage.** How many public MT stations with EDIs are in the Great Basin, and how many sit within 2 km of a well with a temperature log? (Resistivity-temperature pairs.)
10. **Known_time sources.** Which compiled sets (SMU, NGDS, GDR) keep original report dates, not upload dates?
11. **Legality of derived layers.** Exact build dates and label vintages of INGENIOUS layers, USGS 2025 favourability, Faulds FSS polygons, GeoDAWN flights and AlphaEarth versions.
12. **Failure data.** Are BLM geothermal drilling permits, sundry notices and completion reports available without FOIA? How many NDOM P&A and Utah DOGM TG files state a cause?
13. **Global ICE pretraining sets.** Licences and download routes for KGS BHT, Alberta AER/AGS, OZTemp and UKOGL.
14. **Field histories.** Is there a clean table of about 200 global field histories with discovery date and size for the size-bias prior?
15. **Rival filings.** Which Zanskar affiliates file nominations, TG permits and water rights, and under which names?
16. **Outcome and price data.** Any public geothermal option, farm-out or lease-assignment prices beyond Crump Geyser and the Pumpernickel step-out repricing?
17. **AEM and 2 m coverage.** Which INGENIOUS and USGS 2 m and AEM surveys are dated and downloadable (GDR 1391 and others)?

