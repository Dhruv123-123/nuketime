# D03 STRATA-West: red team, data-reality lens

Date: 24 Oct 2026. Reviewer: data-reality red team. No new web searches. Numbers come from the L-files (L05, L10, L19, L20, L29, L33) and v1 evidence (M05, M06, M08). My own estimates are marked (unverified).

## Verdict in one paragraph

STRATA-West is not refuted. Its core bet is right: with ~106 G1 systems, you must learn from unlabelled readings and from simulated worlds. But the design oversells how much data it has. "3-8 billion tokens" is mostly surface pixels and flight-line samples. The deep, independent heat signal is a few thousand wells. Pretraining solves the label famine for **temperature**. It does not solve it for **existence, permeability or archetype**, which stay near 100-200 real examples. The hindcast that is meant to prove all this has fewer than 15 test finds. Every flaw below has an AI-leveraged fix. Score: 15/25.

## Where the data is thin

**F1. The token count hides how little deep data there is (serious).** Count what reaches depth. About 400k BHT readings exist nationally (L29), but only 379 of 4,672 Great Basin wells deeper than 50 m are clean conductive fits (L03, M05). Zanskar says under 10% of the West has any subsurface temperature, and most sampled cells have only wells shallower than 20 m (M06). CA OSWCR's 1.11M reports are water wells. Few carry a temperature (yield 5-15%, unverified). Public prospect-scale MT covers a few dozen areas. Elsewhere there is only the ~70 km USMTArray grid (M08). So the masked task "hide wells in a 20 km block, predict T(z) from MT" has perhaps tens of training blocks, not millions. The backbone will mostly learn surface-to-surface and potential-field correlations, which are cheap and already in INGENIOUS.
*Fix:* report an "effective deep sample size" per voxel depth band, not raw tokens. Weight the masked loss by depth and by information content. Run Stage 0 first and measure the true temperature yield on 1,000 random NDWR and OSWCR pages before sizing the backbone. Let synthetic Westlets carry the depth physics; let real tokens only tune it.

**F2. Data sits where people already looked (serious).** Water wells cluster in farmed valleys. Geophysics clusters around known fields. B2 range-hosted and B3 basin-buried targets sit where there is least data. Masked reconstruction learns the statistics of data-rich valleys and known fields, then extrapolates to blanks. That is the opposite of where the money is.
*Fix:* keep the design's distance-aware head, but also train with "blank-like" masks. Mask whole blocks to the density seen in unexplored ranges, so the model learns to predict under real sparsity. Score skill only in cells whose data density matches the targets (kNNDM, L19).

**F3. `known_time` mostly does not exist (serious).** SMU heat-flow rows, PACES-style gravity compilations and NBMG tables often carry a publication date or none. GeoDAWN (2022) and AEF (2017 onward, L20) postdate the 2015 freeze. So the 2015 backbone cannot see the inputs the live model leans on. AEF also images post-discovery well pads and plants. The hindcast backbone and the live backbone are then different models, and the hindcast does not validate the live one.
*Fix:* an LLM dating agent assigns acquisition dates from report headers, permit numbers and survey metadata, with a sigma. Run a "same-inputs" hindcast: a 2015 backbone *and* a 2026 backbone both with AEF and GeoDAWN removed. The gap between that and the full live model is then the measured value of the post-2015 inputs. For AEF, use the per-pixel change between years to mask built-up pixels.

**F4. The hindcast has no statistical power (serious).** Post-2015 Great Basin blind finds are Big Blind, Pumpernickel, Granite Springs, Gabbs and a handful more (L05, L31). Call it 5-15. "Ranks at least as many in its top 5% as LightGBM" is a difference of one or two finds. Several were Zanskar finds whose public data trail (permits, GDR uploads) appears only after discovery, so they leak too.
*Fix:* make thermal readings the main test, not finds. Thousands of temperatures entered the public record after 2015 (NDWR keyed reports, the 16 DOE drilling sites, L07). Score CRPS and coverage on them under the freeze. Add 1,000 planted systems in Westlets with SBC/TARP (already in Section 7). Keep finds as a sanity check only, and say so.

**F5. Heads beyond heat still have 100-200 labels (serious).** The Cox head has 28 plant + 78 known systems (L03). Split by 11 archetypes, that is about 10 each. Failure-mode labels from completion reports (L40) may be a few hundred holes (unverified). Public flow tests that set a permeability class are rarer still. He R/Ra samples in the Great Basin are a few hundred (unverified). So existence, open-path and archetype outputs will be set mostly by the synthetic prior.
*Fix:* calibrate the Westlet generator itself to real data by simulation-based inference. Fit its archetype mix, permeability and masking rates so that simulated worlds reproduce real summary statistics: heat-flow histograms, spring chemistry, counts of known systems per basin, and the dated discovery curve. Then the prior is learned from real data, not chosen. Report what fraction of each head's posterior comes from the prior versus real evidence.

**F6. Sensor decoders need paired data that barely exists (moderate).** An MT decoder that predicts resistivity from the latent needs co-located MT and T(z). That is a few dozen sites (M08). EIG for MT in a blank cell will be set by the simulator's rock-physics model.
*Fix:* fine, if stated. Use the sim decoder with a misspecification flag (MMD, L28), and buy paired data on purpose. Every v1 field campaign should log MT, 2 m and a TG hole at the same spots.

**F7. The crowd posterior misses rivals' private data (moderate).** Zanskar holds hundreds of its own TG holes and digitised archives. A "public layers only" model understates what Zanskar knows, so our edge looks larger than it is.
*Fix:* infer rival beliefs from what they do. BLM nominations, bids, drilling permits and NEPA filings reveal where they think heat is. Fit the crowd model to their actions, not to our guess of their inputs.

**F8. STRATA-Earth data is not open (minor for now).** Turkish MTA, Kenyan KenGen and Indonesian data are mostly licensed or paper. The In-Context Earth transfer numbers (L10) are for temperature, in data-rich places. Fix: treat global as a later licensing play; use NZ, Iceland and Alberta, which have open data.

## Does it survive 100-200 systems?

Partly. For heat at depth, yes: it trains on continuous, censored readings and synthetic truth, not on system labels. For "is there an open, fluid-filled system here", no data trick creates labels that do not exist. The answer is the calibrated generator (F5) plus our own field data. Each v1 campaign adds dated, paired, negative-inclusive labels that no rival can download.

## Scores (out of 5)

- Calibrated certainty: 3. Good stack, but the hindcast cannot prove it (F4).
- Data realism: 2. Token counts and `known_time` are overstated (F1, F3).
- Buildable in 6 months: 2. Mini-STRATA is buildable; a calibrated West-wide backbone with freeze years is not.
- Edge vs Zanskar: 4. Raw-curve inputs, depth reasoning and EIG are real edges.
- Drives rights and sensors: 4. The EVSI loop is direct, and the sparse-data problem becomes a sensor plan.

**Total: 15/25. Not refuted.**
