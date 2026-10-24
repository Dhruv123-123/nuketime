# D08 UNDERCAST: red team, business edge and buildability lens

Date: 24 Oct 2026. Lens: does UNDERCAST beat Zanskar by enough to buy rights first? Can 2-4 people plus agents ship v1 in 6 months? Does it drive land and sensor decisions? No new web searches. Facts come from D08, MODEL.md, and digests L05, L11, L12, L33, L37. Unchecked items are marked (unverified). Science and data red teams cover identifiability and DPS maths; I do not repeat them.

## Verdict

Not refuted. Score 16/25. UNDERCAST is the most ambitious design in the program and has the best sensor story: it can value a sensor that has not been built yet by simulating it. But as written it is a weather-lab project: a 3D VAE, a latent diffusion prior, a hybrid physics core, DPS assimilation and a POMDP, West-wide, nightly, with a team of 7. The edge that buys land is mostly 2D and near-term. The 3D world model pays off later, when pricing and selling rights. Re-sequence it and it becomes a strong year-2 engine on top of a lean v1.

| Axis | Score | Why |
|---|---|---|
| Calibrated certainty | 4 | 5-backbone ensembles, SBC/TARP gates, kNNDM, point-in-time vintages, OOD fallback, pre-registration. Strong. |
| Data realism | 3 | Held-out-observation training is right. Below about 1 km the state is mostly the Westlet generator, and the design admits it. |
| Buildable in 6 months | 2 | Seven roles and five research-grade engines. The first test is well scoped; the 6-month plan is not. |
| Edge vs Zanskar | 3 | Depth awareness and raw-reading supervision are real. Zanskar is already hiring for "temperature data assimilation" (L05), so the window is 12-24 months. |
| Drives rights and sensors | 4 | Simulated-measurement EVSI/$, lock rule, leak routing to off-auction land. Crowd model is the weak part. |

## Flaws and AI-leveraged fixes

**1. Team and scope (serious).** Section 11 asks for 7 people. Months 2-6 hold a 3D VAE, 10^4 TOUGH3 runs, MT emulators, masked pre-training, five heads, three hindcast vintages, a crowd posterior, EVSI and a West-wide nightly run. A 2-4 person team cannot ship that and also buy land.
*Fix:* v1 is the cheapest-first test widened slightly: Nevada only, thermal tokens only, a 50M-parameter prior, DPS, and the SENTINEL-COX existence head reading its features. Skip the VAE at first by running the prior directly on 3D column-plus-plume parameters (simulation-based inference on generator parameters, then render fields). Coding agents write the operators and test harness; simulation agents run the TOUGH3 bank. MT, gravity, chemistry operators, the POMDP and other states move to months 7-18. Roles for v1: one generative-ML engineer, one hydrogeologist-modeller, one data and extraction engineer, Dhruv on land.

**2. The land decision does not need most of the state (serious).** Buying a section needs P(upflow within 2 km), T at 0.5-2 km and a flow-risk term. Voxels to 10 km, salinity, Vs and phase West-wide are for pricing, EGS and data rooms, not for filing first. Nightly rebuilds also outrun the data: new MLRS cases and logs arrive weekly at most, and leases clear quarterly.
*Fix:* split the product. "Fast map" (weekly, event-triggered by watch agents) carries only the heads that change land actions. "Deep state" runs per prospect, on demand, at 250 m, when we price, sell or plan a hole. This cuts GPU cost by an order of magnitude (unverified) and matches the decision clock.

**3. Deep edge is really simulator edge.** Below the deepest nearby well the posterior echoes the Westlet prior. So the deep edge over Zanskar equals "our generator is more real than theirs". Zanskar also trains on simulations (MIT Tech Review, L05) and a co-founder co-authored the fault FNO paper (L11).
*Fix:* make the generator the moat and measure it. Agents fit generator hyper-parameters until posterior-predictive checks match the real deep logs held out (Big Blind about 823 m, Pumpernickel about 762 m, DOE exploration wells). Publish the per-voxel "data-driven share" and send VOI to the low-share fairways. Lock the extracted deep-log archive (oil, mining, P&A holes) early: that data, not the network, is what Zanskar cannot copy fast.

**4. The crowd posterior is the wrong rival.** D08 defines the crowd as "our model on public easy layers". The real rival runs GeoCore: LightGBM on INGENIOUS at H3 res-8, and its repo is public (https://github.com/zanskar-geothermal/GeoCore, not re-fetched).
*Fix:* an agent rebuilds GeoCore on the same INGENIOUS stack as a "Zanskar emulator". Then fit it to Zanskar's revealed nominations and BLM bids (MLRS, all-bids reports; L37) as an inverse model of their beliefs. Edge = our RNPV minus emulator RNPV, priced for leak cost. Buy where the emulator is cold and we are hot. That is the only edge that turns into cheap land.

**5. Pass bar is not a business bar.** CRPS 15% better than kriging at 0.5-2 km is a science win. A buyer and a land team care about area capture of later blind finds against GeoCore.
*Fix:* add a fifth bar: in the 2015 freeze, top-5% area capture of post-2015 finds beats a GeoCore replica by at least 1.5x, and the buy list beats it on cells the replica ranks below its median. If UNDERCAST wins CRPS but not this, it is a pricing tool, not a finding tool, and should run per prospect only.

**6. EVSI by full re-assimilation is too slow at scale.** Simulating each sensor, re-running DPS and recomputing RNPV for every cell, action and member is thousands of GPU jobs per night.
*Fix:* screen with ensemble-covariance (Kalman-gain) EIG, which is near free, then re-assimilate only the top 1%. Later, train an amortised design network on synthetic campaigns (deep adaptive design, Foster et al. 2021) so the policy is one forward pass.

**7. Missed upside: EGS isotherm rights.** The EGS head (depth to 200-250 C) opens a less contested land market: conductive hot ground with no hydrothermal story, which Zanskar's hydrothermal labels ignore. Fervo-style buyers want exactly this. 
*Fix:* rank an EGS book separately and route it to state and private leases, where the 51,200-acre federal cap (L37) does not bind.

## Bottom line

Keep UNDERCAST, but as phase 2. Run the 4-6 week first test now with the GeoCore-replica bar added. Ship SENTINEL-COX as the land engine meanwhile. Promote the world model to the column layer only when it beats the replica on blind capture. Its lasting value is depth, sensor pricing and EGS: three things a 2D LightGBM map cannot do.
