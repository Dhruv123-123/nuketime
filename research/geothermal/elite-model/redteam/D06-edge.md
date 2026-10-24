# D06 HEARTHNET: red team, business edge and buildability lens

Date: 24 Oct 2026. Lens: does HEARTHNET beat Zanskar by enough to buy rights first? Can 2-4 people plus agents ship v1 in 6 months? Does it drive land and sensor decisions? No new web searches. Facts come from D06, the L-digests (L05, L29, L37) and MEMO.md. Unchecked items are marked (unverified).

## Verdict

Not refuted. Score 16/25. HEARTHNET has the right core idea: firewalled effort as a PU label frequency, plus censored cold wells as depth-honest negatives. Its token reader is a real gain for temperature, where labels are dense. But it puts a 100-300M parameter network on about 280 positives and 5-10 dated blind finds. That is where its edge claim is weakest. The six-month plan is also two plans packed into one. Every flaw has an agent-heavy fix or a scope cut.

| Axis | Score | Why |
|---|---|---|
| Calibrated certainty | 4 | Ensemble, SNGP, AOA, spatial conformal, ledger. The buy-list FDR claim leans on synthetic worlds. |
| Data realism | 3 | Tokens from scans are feasible with agents. 10^7 worldwide tokens and multilingual reports are a year of work, not a month. |
| Buildable in 6 months | 2 | World pretraining, 10^5 Westlets, crowd model, 16-member ensemble and generative EVSI all land in months 4-6. |
| Edge vs Zanskar | 3 | Effort term and censored negatives are copyable fast. The crowd model mis-models Zanskar. |
| Drives rights and sensors | 4 | Lock-vs-sense per parcel and generated-token EVSI are strong. First buy only in month 6. |

## Flaws and AI-leveraged fixes

**1. The network is sized for temperature but sold for existence (serious).** H1 has millions of readings. Transformer neural processes already win there: In-Context Earth reaches MAE 4.7 C against 5.1 for kriging (L29). H2 has about 280 US positives and roughly 10 dated blind finds. A Perceiver cannot learn existence from that. It will learn the prior and the synthetic worlds. The desk-test bar ("median blind find in top 5% vs top 10%") rests on five cases. One rank swap flips the result.
*Fix:* split the model by data density. Use HEARTHNET-small as a field layer for T(z), started from In-Context Earth weights. Put existence in a small, interpretable PU intensity (a GLM or the SENTINEL-COX Cox) that reads z_cell and the fault-graph embedding. Score existence on censored log-likelihood across tens of thousands of cold wells, not on five ranks. Add lead time as a metric (point 4).

**2. Two plans in one six-month box (serious).** Months 4-6 hold world pretraining across seven countries, a crowd model, a 16-member SNGP ensemble, conformal layers, generated-token EVSI, VOI hookup and a 60-site field campaign. With 2 ML engineers this slips. Ten to the fifth Westlets at 10^5-10^6 CPU-hours is affordable, but someone has to make the masking and BHT-bias simulators credible.
*Fix:* v1 is Nevada plus Utah only. Cut to a 5-member ensemble, Tier-1 analytic Westlets (10^4), and conformal on T only. Move world pretraining and the crowd network to months 7-12. Coding agents write the tokeniser, unit contracts and hindcast harness. Extraction agents run from week 1 in parallel, since the data plane is the long pole, not the model.

**3. The crowd model is not Zanskar (serious).** C9 trains a HEARTHNET on public layers. Zanskar has about 27,000 private samples, its own TG holes and site-scale simulation (L05). Its 2026 job posts already ask for GNN and PINN emulators and temperature assimilation (L05). So the gap "our posterior minus crowd posterior" is wrong exactly where Zanskar has drilled.
*Fix:* model Zanskar from what it does, not what it could see. Agents ingest MLRS cases, BLM all-bids reports, NDOM and DOGM gradient-hole permits and county permits by affiliate name (L37). A point process over these dated votes gives "a rival has looked here". Our edge is high posterior and low revealed rival effort. Score it by forecasting next quarter's nominations.

**4. Model class is not the moat; lead time is (serious).** Everything in Section 9 is copyable in a quarter by a funded team. L29 itself says the algorithm on rasters barely matters. What lasts is data nobody else extracted (NDWR 132k unkeyed reports, CA OSWCR 1.1M logs) and ground locked before any public signal. Pumpernickel's neighbour land went from $2 to $232/acre a month after disclosure (L37). HEARTHNET never measures time ahead of the crowd.
*Fix:* add "median months ahead of first public signal" to every hindcast, from known_time in the store. Add "acres lockable per dollar before signal". Aim extraction agents at the sources Zanskar is least likely to have keyed, such as private and state land outside Nevada, and score their marginal lift.

**5. The conformal FDR is mostly a synthetic promise (moderate).** Conformal selection needs calibration outcomes exchangeable with the buy list. Real outcomes of "parcel has >=120 C at <=1.5 km" exist mainly at known, leaky systems. Blind B3 cases are nearly absent. So the stated FDR holds on Westlets, not on Nevada.
*Fix:* label the FDR "synthetic-calibrated" until about 50 field outcomes exist. Our own TG holes and 2 m arrays become the calibration set, with online conformal. Use the FDR mainly on the sell side, in data rooms for Ormat or Fervo. At $2-4/acre, buy-side precision matters less than the acreage cap and outreach bandwidth.

**6. The effort probe will fail for honest reasons (moderate).** Hot springs attract roads, ranches and wells. So true geology predicts effort. An AUC <=0.6 probe on z_cell can fail on a correct model.
*Fix:* make the probe conditional. Test whether z_cell predicts effort after conditioning on surface manifestations and the archetype posterior. Also run the inverse test on Westlets, where the leak is known.

**7. Land action starts too late, and title is missing (moderate).** First locked parcels come in month 6. Nominations grew from 25.8k acres (2020) to over 1M (2025) (GAO-26-108040, L37). Also, much western ranch land has a federal mineral estate under the Stock-Raising Homestead Act (unverified per parcel). Then "ranch heat" needs a BLM lease, not a landowner option.
*Fix:* the month-1 LightGBM-PU baseline is already a buy list. Ship it as v0 at week 4. Start outreach on the top 50 cells in month 2. Add a title latent per parcel (surface owner, mineral owner, state heat regime) built by agents from BLM surface/subsurface layers and assessor rolls.

**8. Generated sensor readings inherit model error (minor).** EVSI from pseudo-tokens is only as good as the generator.
*Fix:* check PIT of generated readings against held-out real TG holes before EVSI drives spending.

## What to keep

The effort encoder shared across "species" (Fithian 2015), censored cold-well negatives, failure-mode labels from completion reports, the bitemporal store and the pre-registration ledger. These are the parts that move land first. Keep the Perceiver for T(z). Do not let it carry existence alone.
