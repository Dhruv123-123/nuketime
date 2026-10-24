# D03 STRATA-West: red team, business edge and buildability lens

Date: 24 Oct 2026. Lens: does STRATA beat Zanskar by enough to buy rights first? Can 2-4 people plus agents ship v1 in 6 months? Does it drive land and sensor decisions? No new web searches. Facts come from D03, MODEL.md and the L-digests (L04, L05, L20, L33). My own estimates are marked (unverified).

## Verdict

Not refuted. Score 16/25. The sensor-decoder idea is the best thing in it. Every sensor is a forward operator on one latent, so EIG per dollar falls out for MT, 2 m, TG and chemistry in every cell. Nothing in Zanskar's public stack does this (L05). But D03 as written is a 2-year, 7-person, $2-4M programme dressed as a 6-month plan. Its lift over LightGBM is a bet, and the bet is tested late. Cut v1 to Mini-STRATA plus decoders inside SENTINEL-COX and it is buildable and useful.

| Axis | Score | Why |
|---|---|---|
| Calibrated certainty | 4 | Censored aleatoric decoders, block-bootstrap ensembles, diffusion states, distance-aware head, conformal FDR, freeze-year hindcasts. Risk: stacked layers double-count or are tuned on very few positives. |
| Data realism | 3 | "3-8 billion tokens" is mostly surface rasters and AEF pixels. Deep thermal truth is still ~400k BHTs, mostly shallow and clustered. Westlet realism for Basin-and-Range is unproven. |
| Buildable in 6 months | 2 | Team of 7, not 2-4. A 1B 3D backbone, physics core, diffusion prior, 10^6 Westlets, three freeze backbones and a global stage in 6 months is not credible as stated. |
| Edge vs Zanskar | 3 | Real edges: depth reasoning, effort term, any-sensor EIG, private/state land. But Zanskar also trains on simulations, is hiring for emulator assimilation and VOI, and holds ~27k private samples and 300k+ ft of its own drilling. |
| Drives rights and sensors | 4 | Edge = our RNPV minus crowd RNPV, conformal buy list, EVSI/$ per hurdle, submodular truck routing. Missing a lead-time metric and a model of Zanskar's own footprint. |

## Flaws and AI-leveraged fixes

**1. Scope (serious).** Section 11 asks for seven people. Section 12 asks for a 300M backbone in month 3, freeze-year backbones in month 4 and a West-wide v1 in month 5. The diffusion prior, the West-scale physics core and the 10^6-world bank are each about a quarter of work (unverified). The plan also spends $2-4M of compute before the cheap gate has even proved that pretraining pays.
*Fix:* v1 = Great Basin only; Mini-STRATA at 50-100M params; 10^5 Tier-1 Westlets plus ~1,500 TOUGH3 runs; one freeze year (2015); decoders for wells, 2 m, TG, MT and gravity; ensembles in place of the diffusion prior. Push diffusion, the 1B model and STRATA-Earth to months 7-18, behind the Section 13 gate. Coding agents write encoders, ETL and tests, so three people can run it (ML, geoscience, data/agents). Compute falls to roughly $100-300k (unverified).

**2. The lift is unproven, and the field says algorithms add little (serious).** USGS found a new algorithm on the same layers adds almost nothing (L04). PANGAEA found supervised UNets often match geospatial foundation models (L20). D03 knows this and gates on it. But its edge story assumes the gate passes.
*Fix:* make the edge story survive a failed gate. If the backbone is demoted, its decoders still give imputation and EIG, and Stage 0 extraction still gives private-grade data from public scans. Say up front that edge order is: (1) extracted data, (2) effort-aware Cox, (3) depth-aware decoders, (4) the backbone. Buy land on (1)-(3) from month 1.

**3. The discovery pass bar has no statistical power (serious).** Post-2015 Great Basin blind finds number about 4-8 (Big Blind, Pumpernickel, Granite Springs, Gabbs, a few more). "At least as many in the top 5% as LightGBM" with n of about 5 cannot tell two models apart. A pass or a fail is mostly luck.
*Fix:* make the main gate temperature CRPS under kNNDM blocks and coverage, which have thousands of points. Add the pre-drill-vs-outcome table (dry holes and hits, 100+ rows, unverified) as a second scored set. Use 1,000 synthetic Westlets with planted blind systems for power. Report discovery capture as a Bayesian comparison with intervals, not a pass/fail count.

**4. "Billions of unlabelled tokens" overstates depth signal (moderate).** Most tokens are surface rasters that Zanskar already has as INGENIOUS grids. Of the 150k Nevada driller reports and 1.1M California well reports, most are shallow water wells, and many have no temperature (unverified share). So the joint structure learned is mostly surface-to-surface.
*Fix:* weight the masked loss toward depth tasks (hide wells, predict T(z) from geophysics). Agents mine deep sources first: NDOM and DOGM oil and gas logs, mining holes, MT transfer functions.

**5. Zanskar has a private label moat STRATA lacks (serious for edge).** Zanskar holds ~27,000 samples and 300k+ ft of its own holes, plus 250k+ acres (L05). Its gaps are real (no effort term, no calibrated P, federal-only), but its data grows with every hole it drills. D03's "crowd posterior" fine-tunes on public layers only, so it models the public, not Zanskar.
*Fix:* build a Zanskar-specific rival model. Use BLM MLRS leases and nominations, state permits and press releases as revealed preference. Shade our bids where they are active and steer to private ranch and state land they ignore. Build our own label moat: cheap TG and 2 m campaigns chosen by EIG, and data-sharing deals with ranch owners and mining firms.

**6. Speed to rights is the real race (moderate).** The model wins only if it locks land before Zanskar's next nomination round. D03 has no lead-time KPI.
*Fix:* add one: median days from first signal (our ledger timestamp) to rights locked, against the date the parcel shows up in a rival nomination. Watcher agents already track MLRS. Score it each quarter.

**7. "Re-conditions in milliseconds" is wrong for diffusion posterior sampling (minor).** DPS needs hundreds of denoising steps per sample.
*Fix:* amortise with a learned update network or a latent ensemble Kalman step; run full DPS only on the shortlist.

## Bottom line

STRATA is the right long-run moat: a learned subsurface reanalysis whose decoders price every sensor. It is the wrong first build. Ship SENTINEL-COX plus Mini-STRATA decoders in 6 months. Buy land on extraction and the effort-aware Cox from month 1. Fund the 1B backbone only when the CRPS and label-efficiency gates pass.
