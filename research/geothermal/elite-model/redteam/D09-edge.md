# D09 KEYSTONE: red team, business edge and buildability lens

Date: 24 Oct 2026. Lens: does KEYSTONE beat Zanskar by enough to buy rights first? Can 2-4 people plus agents ship v1 in 6 months? Does it drive land and sensor decisions? No new web searches. Facts come from D09, MEMO.md and the L-digests (L05 for Zanskar). Unchecked items are marked (unverified).

## Verdict

Not refuted. Score 16/25. KEYSTONE has the best sensor logic in the program. "Which leg is weakest" maps straight to "which cheap test next". Its case files are also a real selling asset. But it is a 7-person research program presented as a 6-month v1. Its own pass bar only asks it to tie LightGBM on ranking. So its edge over Zanskar rests on negatives, transfer and auditability, not on finding more systems. Every flaw below has an agent-based fix.

| Axis | Score | Why |
|---|---|---|
| Calibrated certainty | 4 | SBC on synthetic worlds, "unknown play" mass, MMD misfit flags, conformal buy list. The risk is sharp posteriors from wrong templates. |
| Data realism | 3 | The graph is credible. Archetype tags for 11 classes are thin and partly written after discovery. |
| Buildable in 6 months | 2 | 11 templates, FNO, chemistry SBI, MT operator, ICE prior, amortised NPE+SMC, POMDP. Section 11 asks for 7 people. |
| Edge vs Zanskar | 3 | Play-conditioned cold holes and transfer to thin-label provinces are real. Both are copyable in a few quarters. No metric for lead time. |
| Drives rights and sensors | 4 | Hurdle-to-sensor routing is excellent. Land layer ignores split estate, the federal acreage cap and outreach bandwidth. |

## Flaws and AI-leveraged fixes

**1. Scope is far past 2-4 people (serious).** Month 4 alone adds an FNO trained on about 20k TOUGH3 runs, a chemistry SBI net, five new templates and three new states. Each is a quarter of work for one specialist. Writing a good play template is closer to writing a reservoir conceptual model than to writing code.
*Fix:* v1 is the GeoKG, four templates (B1, B2, B3, B4) plus "unknown", all on the analytic 1D censored column, the v1 effort-thinned Cox layer, and a greedy EVSI-per-dollar ranker. Inference runs per FSS polygon (a few thousand in Nevada, unverified), not per 2 km cell, so plain NUTS or SMC suffices and amortised NPE can wait. Coding agents draft templates from the 300-600 conceptual-model cards. The one geologist reviews; agents write SBC and prior-falsification tests for each. Use published ICE and INGENIOUS grids instead of training new emulators. Defer FNO, MT operator, chemistry net and POMDP to months 7-18. Roles: Bayesian modeller, data/agent engineer, structural geologist, land lead.

**2. The ranking edge is not claimed (serious).** Pass item 1 only needs blind capture equal to flat LightGBM. Zanskar already runs LightGBM on these layers, plus about 27,000 private samples, its own TG holes and over 250,000 acres (L05). On ranking alone, KEYSTONE may be a better-explained copy of what Zanskar already sees. Section 9's "play-aware negatives" is a strong idea, but Zanskar can add censored cold wells in a quarter. Its 2026 job post already asks for temperature data assimilation (L05).
*Fix:* move the edge test to where KEYSTONE should win and Zanskar cannot follow fast. (a) Transfer: freeze Nevada-only fits and score Oregon, Idaho, Utah and New Mexico hindcasts against a Nevada-trained LightGBM. Templates should carry over; GBM correlations should not. (b) Lead time: report "median months ahead of first public signal" (first nomination, permit, lease or press release, from graph known_time). (c) Model Zanskar's revealed beliefs: agents scrape its affiliate nominations, NDOM/DOGM TG permits and water filings as dated votes. Our edge is high posterior where their revealed effort is low.

**3. Archetype labels leak and are few (serious for the hindcast).** Archetype tags come from conceptual-model cards. Most cards were written after the system was drilled. A 2005 freeze that uses them learns post-discovery knowledge. B3 and B6 may have a handful of examples each. The 70% archetype-match bar then measures how well we read papers, not prediction.
*Fix:* treat archetype as latent during the fit. Use tags only for scoring. In hindcasts, admit only cards with known_time before the freeze; a skeptic agent audits each card's date. Pool B3/B4 and B5/B6 into "capped" and "swept" for v1, and split later when labels grow.

**4. "Exact" per-fact explanations are not exact (moderate).** Once mask, archetype and upflow are marginalised, facts interact. Per-fact log Bayes factors then depend on order and do not sum cleanly. A buyer's geologist will find this.
*Fix:* report leave-one-out and flip counterfactuals, which D09 already computes, plus Shapley values over facts for the top 20. Agents batch the reruns overnight; compute is cheap at polygon scale.

**5. Land layer is a cost field, not a title model (serious for land).** Much ranch land came through the Stock-Raising Homestead Act, which reserved minerals, and courts treated geothermal as a reserved mineral (US v. Union Oil, 9th Cir. 1977; unverified here). So "option ranch heat" may need a BLM lease instead. The per-state federal acreage cap and ranch outreach capacity bind before rights prices do, since rights cost about $1-10 per acre.
*Fix:* add a parcel title node to the GeoKG: surface owner, mineral estate, state heat regime, existing leases. Agents join BLM surface/subsurface layers, assessor rolls and recorded deeds. Replace the v1 POMDP with a knapsack under acreage cap, outreach slots and lease clocks. Keep the POMDP for $1-5M drilling decisions.

**6. Land action starts at month 6 (moderate).** Nominations are surging, and six months of silence costs ground.
*Fix:* issue a v0 buy list at week 4 from the Cox layer plus the four-template column fit on keyed data. Start state and ranch outreach in month 2 on the top 50 polygons. Use later releases to add and drop.

**7. Case files may not raise sale prices much (moderate).** Ormat, Fervo and utilities pay for drilled temperature and flow, not narratives. L37 supports verifiable disclosure, but the premium is untested here.
*Fix:* make the case file a pre-registered, hashed forecast that a buyer can check against our own TG hole. The proof is the verified hit, and the case file shows why it was not luck. Track sale price versus case-file depth in the ledger.

## What survives

The weakest-link sensor routing is the best idea here. A cold 150 m hole means little under a lid and a lot under a range-hosted play. That asymmetry turns tens of thousands of silent holes into evidence, and it tells the field crew which $20k test to run. Built lean (Fix 1) and scored on transfer and lead time (Fix 2), KEYSTONE is a strong v1 spine. If it only ties GBM on Nevada ranking, it still ships as the negative-evidence, sensor and data-room layer, as D09 says.
