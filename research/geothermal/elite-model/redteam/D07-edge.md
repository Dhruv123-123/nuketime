# D07 PLAYBOOK: red team, business edge and buildability lens

Date: 24 Oct 2026. Lens: does PLAYBOOK beat Zanskar by enough to buy rights first? Can 2-4 people plus agents ship v1 in 6 months? Does it drive land and sensor decisions? No new web searches. Facts come from D07, M33, L05, L17, L31 and L37. Unchecked items are marked (unverified).

## Verdict

Not refuted. Score 15/25. PLAYBOOK has the best business framing in the program so far. It speaks the buyer's language (Pc, risked MW, EMV), it routes land by leak cost, and it picks sensors by the weakest element. That is how a rights bank sells. But its headline science, a per-play count of what is left, cannot be identified at the play level with Nevada's sample. Its prospect ranker is the same model class Zanskar runs. And it needs 5-6 people, not 2-4. All three are fixable.

| Axis | Score | Why |
|---|---|---|
| Calibrated certainty | 3 | Lookback, SBC, Brier gates and hashing are strong. But Pg is a product of five elements, and four have almost no labels. |
| Data realism | 3 | Discovery ledger is doable (L31 already did 11 cases). Per-channel dated effort and failure causes are thin. |
| Buildable in 6 months | 2 | Nine components, U-Net, NPE, dependency network, crowd model. Section 11 asks for 5-6 people. |
| Edge vs Zanskar | 3 | "High geology, blind to every past channel" is a real lead-time signal. Most other parts are copyable within a quarter. |
| Drives rights and sensors | 4 | Best in class. Leak-cost routing, Pandora stop rule, weakest-element sensor choice, play cap. |

## Flaws and AI-leveraged fixes

**1. The play-level count is not identifiable (serious).** D07 wants N_remaining by size class for 150-300 plays. Nevada has about 106 known systems (28 plants plus 78 known) and maybe 20-30 with dated finds and size marks (M33). That is well under one dated find per play. Each play also needs its own channel biases beta_c and gamma_c. The posterior will be the prior. Worse, play archetype (B1-B7) is a latent for unfound systems, so the pool partition itself is uncertain.
*Fix:* fit [F] at province level with three or four channels only (springs, non-geothermal holes, geothermal surveys, our sensors). Treat play shares as a Dirichlet split of the province pool, with weights from the Pg map. Borrow strength from global field histories (NZ, Iceland, Turkey, Kenya) as a hierarchical prior. Run the simulation-based calibration first, on synthetic Westerns with 100 systems, to learn what can be recovered before claiming per-play counts. Use the count to pick provinces and channels, not to rank prospects.

**2. The pass bar has too few events (serious).** Post-2008 Nevada MW (about 425 MW, M33) comes from about 8-10 fields, mostly found by mining holes. Bar 2 (60% of MW in the top third of plays) can pass or fail on one field like McGinness (about 160 MW). Bar 3 compares against a frozen-label GBM with perhaps 6-8 blind finds. The bootstrap interval will rarely exclude 1x.
*Fix:* add count-based scores and the 99 USGS probable systems as a soft label set. Add Utah, Oregon and Idaho finds. Add synthetic hindcasts from the simulator as a power check. Pre-register the bar with expected power, so a "fail" means something.

**3. The prospect ranker is Zanskar's model class (serious for edge).** [E] is monotone LightGBM plus isotonic calibration. Zanskar already runs LightGBM on INGENIOUS (L05) and has hired for fault mapping and data assimilation. Element decomposition and monotone constraints are a quarter of work for them. Zanskar also owns a larger private negative set: it reports a 1 in 550 historical hole rate and has drilled many TG holes of its own. Our public failure ledger (about 300 holes) is smaller than theirs.
*Fix:* put the edge where Zanskar is structurally weak, not in model class. (a) The channel-blindness term: prospects with high Pg but near-zero past effort from every channel, especially B3 buried and B4 lidded plays and private ranch land. That is a lead-time signal, and Zanskar, as a developer, does not chase private split-estate heat at scale. (b) An agent-built failure ledger from BLM geothermal drilling permits, sundry notices and well completion reports by FOIA, plus NDOM and Utah DOGM files. (c) Our own designed TG cells, which enter [F] as a clean new channel.

**4. Pg is a product of five weakly labelled elements (moderate).** Heat failures are the only class with real labels. Pathway, cap, fluid and freshness failures are rarely written down. Multiplying five separately calibrated chances also assumes independence that is false: hot but tight and masked often co-occur.
*Fix:* fit a joint competing-risks model over the L40 outcome classes. Calibrate only total Pg against outcomes. Use LLM-elicited Milkov-style tables as priors for the uncalibrated elements, and say so on the risk card. Let our own post-drill tagging train the elements over time.

**5. Scope versus team (serious, fixable).** Months 1-6 hold a ledger, nine components, a U-Net benchmark on GEMS, NPE on 10^6 simulations, a dependency network, a crowd model, five states and a field season. Section 11 names 5-6 roles plus an adviser.
*Fix:* v1 is four parts: ledgers [A] and [D] (agents), a province-level [F] in NumPyro, a heat-plus-pathway risk card [E], and a greedy EMV-per-dollar book [H] with leak cost. Use Faulds polygons as given. Defer the U-Net, NPE, dependency network beyond simple play shrinkage, and the crowd refit to months 7-12. Coding agents write the bitemporal store and test harness. Team: one Bayesian modeller, one geologist, one data and agent engineer, Dhruv on land. That is buildable.

**6. Land layer misses some real constraints (moderate).** The book does not model the federal acreage cap per lessee per state (51,200 acres, unverified), Nevada split estate and who holds heat under private ranches, or outreach capacity for private options. A nightly book is also faster than the market: BLM Nevada holds about two sales a year.
*Fix:* add an agent that resolves surface and mineral owner from county assessor and BLM MLRS records per parcel, and a capacity constraint on owner outreach. Run the book weekly, with a trigger on new nominations and disclosures, since land beside Pumpernickel repriced 116x within about a month of disclosure (L37).

**7. The crowd posterior is the wrong rival (minor).** A refit on public layers models the median bidder, not Zanskar. The rival that matters has private holes.
*Fix:* add a Zanskar belief layer from its nominations, lease wins and disclosures (L05 suggests this). Treat its nominations as a noisy positive and a leak signal.

## What is genuinely strong

The book format sells. Ormat and utility buyers already read Pc and EMV from oil. Hashed forecasts and a public calibration report give a track record that cannot be copied. The "our sensors are a new channel, and if the curve does not step up, kill" rule is a clean business test. And the counterfactual creaming curve, at province level, answers the real capital question: which province and channel to put the next $1M into.

## Bottom line

Keep PLAYBOOK as the decision and disclosure layer of the elite model. Cut the per-play count to a province-level count. Do not sell the risk tables as the edge. Sell lead time on channel-blind ground and an auditable track record.
