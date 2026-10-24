# D05 HELM: red team, business edge and buildability lens

Date: 24 Oct 2026. Lens: does HELM beat Zanskar by enough to buy rights first? Can 2-4 people plus agents ship v1 in 6 months? Does it drive land and sensor decisions? No new web searches. Facts come from D05, MODEL.md and digests L05, L15, L37. My own estimates are marked (unverified).

## Verdict

Not refuted. Score 17/25. HELM is the most business-shaped design so far. It asks the right question: "what is the next dollar of land, sensing or drilling worth?" Its lock rule, channel choice, leak cost and lease clocks map straight onto how cheap rights are won. But its edge claim rests on the wrong part. Planning depth adds about 6-15% in the best published case. Zanskar's lead is data and drilling. HELM is model-agnostic, so it wins only if the belief plug-in, the private-land channel and the crowd model win. And the build is a 6-7 person, 12-month plan sold as 6 months.

| Axis | Score | Why |
|---|---|---|
| Calibrated certainty | 4 | Prior and posterior falsification, SBC, TARP, stacking, max-entropy "unknown play", EVSI calibration slope, Brown-Smith gap. Risk: planner lift is tested on worlds drawn from its own prior. |
| Data realism | 3 | Rung transitions, exit prices per rung and post-2005 blind finds are tens of cases. The planner's reward is mostly guessed. |
| Buildable in 6 months | 2 | Team of 6-7 in Section 11. Months 2-5 stack GHOST, flows per sensor, POMCPOW, Brown-Smith, crowd inversion and BetaZero. First buy list in month 5. |
| Edge vs Zanskar | 3 | Real edge in leak-aware channel choice, private and state land, cheap sensors and the hashed ledger. The planner itself is a small, copyable lift. Zanskar is hiring for VOI and well placement (L05 job post). |
| Drives rights and sensors | 5 | Best of the set. Lock rule, bid at E[value given win], leak cost, clock-aware spend, sensor per hurdle, sell rung. |

## Flaws and AI-leveraged fixes

**1. The pass bar expects more planning lift than the literature gives (serious).** Section 13 wants HELM to beat one-step EVSI by 1.3x. The best evidence is Martinelli, Eidsvik and Hauge on 25 dependent North Sea prospects (L15): 1-step look-ahead 21,841 MUSD, 3-step 23,197. That is about 6% over one-step, and 14.8% over naive. Intelligent Prospector's gains are on synthetic ore bodies. So the desk test will likely "fail" on a fair setup, or "pass" on a rigged one.
*Fix:* split the claim. Score planning against one-step at a realistic 5-15% bar. Put the 1.3-1.5x bar on the parts that can move it: channel choice (private and state versus nomination), leak cost and timing against the sale calendar. Run an agent ablation grid on GHOST worlds that switches each term on and off, so the report says where the dollars come from.

**2. Synthetic lift is circular (serious).** The planner is trained and scored on GHOST worlds drawn from the same prior the belief uses. Lift on matched worlds is partly built in.
*Fix:* train on Tier 1 worlds, score on worlds from a different generator: the FNO/TOUGH3 subset, and archetypes proposed by the hypothesis-tournament agents that the belief has never seen. Report lift on mismatched worlds as the headline. Keep the 2005 real replay as the gate.

**3. Land is too cheap for the "measure or lock" index to matter much (moderate).** Nevada 2025 median winning bid was $3.50/acre, 37% at the $2 floor (L37). With costs that low, the Pandora reservation value says "lock" for almost any plausible cell. The binding limits are elsewhere: leak cost, nomination volume (GAO-26-108040: over 1M acres nominated in 2025, 27% duplicates), rental over the primary term, and deal-team hours for ranch options.
*Fix:* make the planner's budget constraint "people and leak", not dollars. Model annual rental and diligence obligations as holding cost (BLM rental per acre and work rules, unverified). Let the index rank by value per deal-team hour for private ground, and by leak cost for federal ground. Agents draft ranch letters and option papers so the human hour per deal falls.

**4. Too few real outcomes to learn rung prices (serious, fixable).** Exit price per rung and P(next rung) rest on a handful of deals (Crump Geyser carry about 20%, Pumpernickel step-out repricing about 116x; L37). Post-2005 Nevada blind finds that sit inside a replay are single digits (unverified). A 1.2x lift with a CI above 1 on that sample is unlikely.
*Fix:* an extraction agent builds a project-outcome table from MLRS cases, NDOM and Utah DOGM permits, GRC and SGW papers and SEC filings: every lease, TG hole, slim hole and relinquishment since 1975. Score replays on rung events (hot TG holes, permits filed, leases relinquished), which number in the hundreds, not on finished plants. Pool Nevada, Utah, Oregon and California. Price rungs by scenario axes until our own sales exist.

**5. Scope is far beyond 2-4 people (serious, fixable).** BetaZero on 10^7 campaigns, a Brown-Smith bound, per-sensor normalising flows, DGSA and rival-belief inversion each need a specialist.
*Fix:* v1 = "HELM-lite". Index policy plus one-step EVSI, with depth-2 search only inside shared-play groups, using existing POMDPs.jl and POMCPOW.jl. Flows for three sensors only (2 m probe, TG hole, E-MT). Crowd model v1 = a rebuilt GeoCore LightGBM on INGENIOUS (github.com/zanskar-geothermal/GeoCore, not re-fetched) plus Zanskar's nominations as revealed belief. Push BetaZero and Brown-Smith to month 9-12. Team of three: a decision scientist, a Bayesian or geothermal modeller, a data-and-agents engineer, with a part-time land lead. Coding agents write the simulators, tests and solver glue.

**6. The land calendar is missed (serious, fixable).** The first pre-registered buy list arrives in month 5. BLM sales, state first-file and ranch talks do not wait.
*Fix:* run SENTINEL-COX or the LightGBM-PU plug-in with the static lock rule as the live engine from week 2. HELM wraps it month by month. Watcher agents file nominations the week a parcel crosses the rule. Measure lead time: years between our top-5% call and the first public signal.

**7. Model-agnostic cuts both ways (moderate).** If any belief plugs in, the moat is not the science. A decision engine is copyable, and Zanskar already advertises VOI work (L05).
*Fix:* name the moat as the things HELM accrues: the bitemporal ledger of hashed forecasts, our own sensor rows from private and state land Zanskar's BLM-heavy footprint does not see, and the rival-belief history. Keep the GeoCore replica as a standing plug-in, so every claim of edge is "our value minus replica value" on parcels Zanskar has not touched.

**8. Leak padding and decoys carry legal risk (moderate).** Section 14 flags it. A nomination strategy that looks like bundling could draw BLM scrutiny.
*Fix:* a compliance agent checks each nomination plan against 43 CFR 3200 rules before filing (unverified rule cite), with lawyer review. Prefer off-auction channels where leak cost is high, which avoids the issue.

## What would change the score

A desk test that shows lift on mismatched worlds, with ablations that place the dollars in channel and timing, would lift edge to 4. A HELM-lite running live on a real Nevada sale by month 3 would lift buildability to 4. A 500-row rung-outcome table would lift data realism to 4.
