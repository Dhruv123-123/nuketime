# D04 TWIN-WEST: red team, business edge and buildability lens

Date: 24 Oct 2026. Lens: does TWIN-WEST beat Zanskar by enough to buy rights first? Can 2-4 people plus agents ship v1 in 6 months? Does it drive land and sensor decisions? The shared web-search budget was used up when this agent ran (one search attempted, refused). Facts come from D04, MODEL.md and the digests L05, L37. My own estimates are marked (unverified).

## Verdict

Not refuted. Score 17/25. TWIN-WEST has the best decision machinery of the designs so far. The OSSE sensor engine, the upflow-offset vector and the "dated discovery record as an observation" are real, sellable edges. Its weak point is not science. It is the calendar. As written it is a 7-person, 12-18 month build that produces its first RNPV map in month 4. Land is bought in months 1-3. Cut v1 to a Nevada 1D/2.5D twin that plugs into SENTINEL-COX, and it is buildable and useful.

| Axis | Score | Why |
|---|---|---|
| Calibrated certainty | 4 | Every reading is a censored likelihood on one state. Surrogate error, discrepancy GP and OOD flags are in the posterior. Risk: the twin tests mostly check the model against itself (see D04-science). |
| Data realism | 3 | Most voxels below 300 m see no data. The "reanalysis" is mostly prior there. Honest, but it shrinks the area where edge can exist. |
| Buildable in 6 months | 2 | Section 11 asks for 7 people. Month 3 asks for 5,000 two-phase 3D Waiwera tiles, a multi-fidelity FNO, a corrector, an OSSE harness and the discovery layer at once. Not credible for 2-4 people. |
| Edge vs Zanskar | 4 | Regional physics inversion, effort-aware discovery likelihood, depth extrapolation with error bars, private and state land. Zanskar also uses physics, but only at site scale (L05). |
| Drives rights and sensors | 4 | Buy rule, crowd gap, up-gradient parcel, OSSE per sensor with travel batching. Missing: a Zanskar replica as the crowd, and a lead-time metric. |

## Flaws and AI-leveraged fixes

**1. Physics is not, by itself, an edge over Zanskar (serious).** Zanskar used a physics simulator at Lightning Dock, trains FNOs on 1,200 fault simulations (Liang et al., SGW 2026), and is hiring for emulator assimilation and VOI (L05). Section 10 pitches "physics vs LightGBM". That framing will age badly within a year. Zanskar also holds about 27,000 private samples and its own drilling, which no public-data twin can see.
*Fix:* restate the edge as three things Zanskar does not publish: (a) a regional, not prospect-scale, inversion that uses every cold well as a censored observation, against GeoCore's 148 negatives; (b) the effort-thinned discovery likelihood, so "searched and not found" lowers a cell's score; (c) the upflow-offset vector, which says buy up-gradient. Then measure it. GeoCore is open source (github.com/zanskar-geothermal/GeoCore, not re-fetched). An agent rebuilds the GeoCore LightGBM on INGENIOUS layers as a "Zanskar replica". That replica, plus Zanskar's public lease nominations and wins as revealed belief, replaces D04's generic crowd posterior. Edge = our RNPV minus replica RNPV, on parcels Zanskar has not touched.

**2. The plan misses the land calendar (serious).** BLM Nevada sells leases on a fixed cycle, and Zanskar won 16,720 acres at $2/acre with single bids in 2023 (L37). Land is cheap. Being first is what pays. D04 gives no RNPV until month 4 and no buy list for California, Utah, Oregon or Idaho until month 5.
*Fix:* run SENTINEL-COX v1 as the live decision engine from week 1. The twin enters as an upgrade to v1's 1D censored column likelihood, tile by tile, as each tile passes its gate. Add a lead-time metric to the hindcasts: years between our top-5% call and the first public signal (nomination, permit, press). A watcher agent files nominations the week a parcel crosses the buy rule.

**3. Scope exceeds 2-4 people (serious, fixable).** Two-phase 3D TOUGH3 runs on random generator draws fail to converge often. Ten observation operators, a diffusion prior, ES-MDA stitching and EKI each need a specialist.
*Fix:* v1 = "TWIN-NV". Great Basin only. Analytic plus 2.5D generator (10^5 sections). Tile NPE. Discovery layer. Operators for logs, BHT, TG, 2 m, chemistry and gravity only. Skip the latent diffusion prior; use NPE ensembles. 3D TOUGH3 only inside EKI on optioned parcels (about 700 runs each). Coding agents write operators and tests against PyTOUGH examples; a simulation agent repairs non-converged runs and logs failures. Team of three: a reservoir modeller, an SBI/ML engineer, a data-and-agents engineer. The Section 13 hindcast ($8k, 4-6 weeks) is the right first gate, and it fits this team (unverified cost).

**4. Selling the reanalysis gives away the edge (moderate).** Section 1 calls the twin "a sellable data product". If rivals buy the upflow layer, the crowd gap closes.
*Fix:* sell only layers that do not compete with our land plays: conduction-only and EGS isotherm depths to Fervo-type and closed-loop buyers, and a 3-year-lagged hydrothermal layer. Keep P(upflow) and offset vectors private until we hold the rights. Hashed forecasts still prove skill without revealing locations.

**5. OSSE can over-value sensors in prior-only cells (moderate).** Where the posterior is the max-entropy prior, every sensor looks valuable. The engine could send trucks to empty desert.
*Fix:* weight EVSI by land cost and access. Rank only cells where a sensor can flip a buy decision within the next lease cycle. Require the crowd gap to be positive before spending field money. Cap the share of the sensor budget spent on cells with less than a set information gain.

**6. Edge is concentrated in few places (moderate).** Prospect-scale MT covers under 2% of the ~1,430 FSS (D04-data). Our edge exists only where extracted archives and effort data add signal Zanskar lacks.
*Fix:* point AI extraction first at NBMG, NDWR and OSWCR scans in private and state land inside unsampled FSS. That is where Zanskar's BLM-heavy footprint is thin and where the twin's cold-well likelihood beats 148 negatives most.

## What would change the score

A passed Section 13 hindcast scored against the GeoCore replica, not kriging, would lift edge to 5. A shipped TWIN-NV in month 4 with a live nomination would lift buildability to 4.
