# D10 CONCLAVE: red team, business edge and buildability lens

Date: 24 Oct 2026. Lens: does CONCLAVE beat Zanskar by enough to buy rights first? Can 2-4 people plus agents ship v1 in 6 months? Does it drive land and sensor decisions? The shared web-search budget was used up before this review, so no new searches ran. Facts come from D10, MEMO.md, MODEL.md and the L-digests (L04, L05, L31, L37). Unchecked items are marked (unverified).

## Verdict

Not refuted. Score 16/25. CONCLAVE is the best "company OS" design in the program. Its ledger, hashed forecasts, crowd posterior and leak-cost routing tie the model straight to land. But its headline idea, stacking ten experts, is the part least likely to create edge. L04 says the algorithm barely matters. Stacking is a better algorithm. The real edge sits in the parts around the stack: dated archive extraction, effort and censored negatives, the rival model and the land routes. Six months is enough for those, not for ten experts plus a POMDP.

| Axis | Score | Why |
|---|---|---|
| Calibrated certainty | 4 | Stacking on held-out predictive densities, sampled weights, conformal FDR buy list, SBC/TARP, CSEP tests. Hard to beat. |
| Data realism | 3 | Weights for Y1 rest on tens of dated blind finds. The E2 feature stack is not point-in-time. |
| Buildable in 6 months | 2 | Ten experts, an FNO bank, an NPE, MT ensembles and a POMDP. The plan names 5.5 roles; the brief is 2-4. |
| Edge vs Zanskar | 3 | Edge over public-data LightGBM is real but copyable. E10 models the wrong rival: Zanskar holds private wells. |
| Drives rights and sensors | 4 | Route-typed land tickets, leak cost, Pandora stops, batched sensor queue. Land throughput is not modelled. |

## Flaws and AI-leveraged fixes

**1. Stacking is not the moat (serious).** Zanskar's LightGBM is already an ensemble of trees. Its team can add stacking in a sprint. In published comparisons, stacking usually beats the best single model by a few percent of log score (Yao et al. 2018, *Bayesian Analysis* 13:917) (unverified size for this domain). A few percent will not decide who nominates a parcel first. The experts also share most inputs (INGENIOUS layers, the same wells), so their errors are correlated and the gain shrinks further.
*Fix:* sell disagreement, not the average. Use the stack's spread as the sensor-targeting signal (D10 already hints at this in 4.3). Put the build effort into what Zanskar cannot copy fast: the bitemporal ledger of extracted archives (NDWR's ~132k driller reports, NBMG, CalGEM, mining-company holes). L31 shows most Great Basin blind finds began with an accidental farm or mineral hole. Agents that read every such hole are the moat. Stacking is an add-on.

**2. Stacking weights are fit on the wrong target (serious).** Weights learn mainly from thousands of well temperatures (Y2, Y4), because blind discoveries number in the tens. But wells cluster near known systems and towns. So the weights learn which expert works where wells exist. The money is in cells far from wells, where z(x) extrapolates and the Dirichlet prior simply returns E1.
*Fix:* weight the held-out log score by inverse well density, or score only wells more than 10 km from any known system. Generate synthetic worlds with planted blind systems from the E4 simulator. Agents can build 1,000 such worlds and check that the weights pick the right expert in empty cells. Report stacked-vs-E1 only on the far-from-label stratum.

**3. The crowd posterior models a naive crowd (serious).** E10 trains on public layers only. Zanskar is the rival who matters, and it holds private data: Big Blind and Pumpernickel logs, Lightning Dock, its digitised archive and 6,009 warm-well labels (L05). In Zanskar's own neighbourhoods E10 will under-price the rival, which is the worst error for a bidder. L37's Hendricks-Porter result says the informed neighbour takes the rent.
*Fix:* add an E10-Z "revealed rival" model. Agents watch Zanskar nominations, BLM bid history, NDOM permits (Granite Springs 68-02 style), water-right filings and job posts. Fit an inverse model: what posterior would make Zanskar act this way? Treat each Zanskar nomination as a noisy positive label for geology and as a "do not bid here" flag for land. Our edge zone is then cells far from all rival footprints, plus private and state land.

**4. Hypothesis tournament overfits the hindcast (serious).** Hundreds of agent hypotheses a month scored against one frozen hindcast with ~10-30 blind positives is a forking-paths machine. The 1-in-20 survival bar in Section 13 will pass by chance.
*Fix:* use a reusable holdout (Dwork et al. 2015, *Science* 349:636, Thresholdout). Keep a sequestered final hindcast that agents never see. Correct for the number of tests (Benjamini-Hochberg on log-score gains). Then promote survivors only after a prospective, hashed test against the next BLM sale or drilling result.

**5. Six-month scope (serious, fixable).** Months 4-5 alone hold E4 FNO plus NPE, E5, E6, E7, E8 and a depth-2 POMDP. That is a year for this team.
*Fix:* v1 is E1, E2 rebuilt point-in-time, E3-lite, E9, a distance smoother, E10 and E10-Z, plus stacking, depth-1 EVSI and the conformal buy list. Use published products instead of building: ICE grids, USGS 2025 P05-P95, public MT models. Coding agents write the expert interface, golden-trap suites and backtest harness. E4, E5, E7 and the POMDP move to months 7-18. Team: one Bayesian modeller, one data and document-AI engineer, one geoscientist-dealmaker, Dhruv on land.

**6. E2 leaks the future (moderate).** The USGS 53-feature release (doi 10.5066/P14QM39R) was built in 2025. Several layers (heat flow, strain, fault maps) embed post-2005 wells. A 2005 freeze using them overstates E2 and the stack.
*Fix:* agents rebuild each layer from ledger rows with `known_time` before the freeze. Where that is not possible, flag the layer and run with and without it.

**7. Land throughput is missing (moderate).** Nightly lock tickets for thousands of cells, but one land lead. Private ranch heat needs title work, split-estate checks and owner outreach. State rules on who owns geothermal heat differ (unverified per state).
*Fix:* a title agent on county recorder and BLM MLRS data, an owner-outreach agent drafting letters, and a capacity term in the decision layer: at most N deals per month, so the policy ranks by value per land-hour.

## What survives

The bitemporal ledger, the hashed track record, conformal FDR buy lists, leak cost and route choice are all real business edge. They drive both rights and sensors. Make v1 "ledger plus three experts plus rival model", and CONCLAVE is a strong, buildable company OS. The stack becomes an option to grow into, not the bet.
