# D05 HELM: red team, data-reality lens

Date: 24 Oct 2026. Reviewer: data-reality red team. The shared web-search budget was used up before this agent ran, so no new searches were made. Facts come from L14, L17, L19, L32, L37 and v1 evidence (M18, M19, M29). My own estimates are marked (unverified).

## Verdict in one paragraph

HELM is not refuted. Its planner gets most of its skill from synthetic worlds, so it does not need many confirmed systems to learn. That is also its weak point. The parts that tie it to reality are thin: rung transitions, exit prices, rival beliefs and leak cost rest on tens of cases, often on one. Its main real-data test, the 2005 Nevada replay, has too few events to show a 1.2x lift. Every flaw has an AI-leveraged fix. Most fixes swap rare binary outcomes for plentiful graded ones. Score: 17/25.

## Flaws and fixes

**F1. The reward function rests on a handful of deals (serious).** HELM's value is driven by exit price per rung, farm-out terms and leak cost. Public evidence is one third-party farm-in (Crump Geyser 2010, originator floored at 20%), one clear repricing event (Pumpernickel step-out land, $2 to $232/acre) and one US project-level success figure (Wall and Dobson 2016: under one-third, table not released; L32). A planner tuned on this will choose exit rungs from guesses. Getting the structure right does not fix guessed inputs.
*Fix:* an extraction agent builds a project-outcome table from BLM MLRS case histories (assignments, relinquishments, unit agreements), NDOM and Utah DOGM permits, SEC filings (Ormat 10-Ks, Fervo S-1) and GRC/SGW papers. Borrow exit-price structure from mining prospect generators (EMX Royalty option terms, SEDAR NI 43-101 filings). These give hundreds of option deals by stage (unverified count). Run exit prices as a scenario axis and make the planner's policy robust across it, not tuned to one value.

**F2. The 2005 replay has no statistical power (serious).** Post-2005 blind finds in Nevada number about 8-15 (Gabbs Valley, Granite Springs, Big Blind, Pumpernickel, Tungsten Mountain, Don A. Campbell, San Emidio SW, plus McGinness Hills leasing in 2007; M18). Each policy locks a few per cent of the acreage, so it captures maybe 0-5 of them. A 1.2x ratio with a CI above 1 on counts that small cannot be shown. A pass bar that cannot be met is a pass bar that will quietly be dropped. Worse, these finds depended on who chose to look (Ormat, Zanskar, DOE fairway work). A policy that copies past effort gets rewarded.
*Fix:* score the replay on graded outcomes, not on finds. Since 2005, thousands of holes were drilled and logged: TG holes, mining holes, NDOM geothermal permits and water wells with dated temperatures. Score each policy by the log score of the later-measured T(z) inside its locked acres, plus the realised value per acre. That moves n from about 10 to thousands. Add the 1990 freeze, which brings in McGinness, Don A. Campbell and Tungsten. Pool Nevada, Utah, Oregon and Idaho. Keep effort layers out of the intensity (L19).

**F3. Bitemporal "known_time" is mostly unknown (serious).** The design depends on rebuilding what was public on any past day. Most compiled sets (SMU node, AASG/NGDS, GDR uploads) carry an upload date from the 2010s, not the date the number first became public. If known_time is set to the measurement date, post-2005 data that was really proprietary leaks into the past. If it is set to upload date, the 2005 world looks emptier than it was. USGS 2025 favourability and INGENIOUS layers used in the crowd model were fit on labels that include later finds.
*Fix:* a dating agent traces each record to its first public citation (OSTI report, GRC paper, open-file) and stores both dates with a confidence. Run replays under both choices and report the spread. Ban post-freeze model products from frozen worlds, including in the crowd model.

**F4. The crowd model sees only BLM, and BLM bids carry little signal (serious).** BLM all-bids PDFs exist (about 2007 onward) and are fully public (L37). But 37% of Nevada 2025 wins were at the $2 floor, and many parcels draw one bidder. Floor bids say almost nothing about beliefs. Nominator identity is often not shown. State leases and private ranch deals are largely unseen, and that is exactly the channel HELM says is its edge. So rival-belief inversion is weakest where HELM claims to win.
*Fix:* AI OCR of county recorder indexes for memoranda of geothermal lease and water rights filings (Nevada Division of Water Resources; Utah water rights), plus state land office lease lists. Validate the bid-shading code first on BOEM offshore bids since 1954 (L37). Treat rival belief as a prior with wide spread where data are thin.

**F5. BEL falsification has no power where it matters (moderate).** Prior falsification compares real data summaries with the prior predictive per basin and archetype. Most basins have zero to three deep wells, and the Great Basin has about 379 clean conductive wells total (M05). A Mahalanobis test on two points almost never rejects. So "off-simulator" flags fire near known fields and stay silent in the blind basins HELM targets. Silence will be read as a pass.
*Fix:* report test power per cell and add a third flag, "unfalsifiable", which gets the same sensing bonus as "off-simulator". Use the dense shallow data (2 m surveys, water-well temperatures, spring chemistry) as falsification summaries, since they exist in hundreds per basin.

**F6. The archetype library is short in the class that matters (moderate).** Nearly all historic finds had 100 C above about 300 m. The deep-only class (Big Blind, Pumpernickel) has one or two public examples (M18). GHOST worlds will plant blind systems with weights fit to a biased label set, and the planner will learn to value cheap shallow sensors more than it should.
*Fix:* treat archetype weights as uncertain hyperparameters drawn wide in training. Have the hypothesis-tournament agents mine Zanskar talks, DOE GTO project reports and Australian/Turkish analogues for deep-only cases. Test planner regret under a "deep-heavy" world as a stress case.

**F7. Sensor reliability is unknown until money is spent (moderate).** Every EVSI depends on reliability matrices. These come from the calibration campaign (about 20 blind systems, 40 cold controls), which starts in month 4. Before then, EVSI is simulator-only. The month-6 EVSI calibration slope from about 100 actions will have a wide CI.
*Fix:* back-cast reliability from historical paired data first: 2 m surveys later drilled (Faulds play fairway, Coolbaugh's Nevada 2 m sets), MT surveys with later wells. Use historical holes as quasi-actions for the EVSI slope.

**F8. Ownership data for private heat is patchy (minor).** County parcel layers differ by county. Regrid is paid. Split estates make "who owns the heat" unclear in some states.
*Fix:* license Regrid; have an agent read state geothermal statutes (heat as mineral vs water) per state and flag ownership risk per parcel.

## Does it survive 100-200 confirmed systems?

Yes, better than mapping designs do, because the planner trains on synthetic worlds and the belief uses graded negatives. But the reality checks are underpowered. HELM must move its gates from binary finds to graded temperature and value outcomes, or its pass bar will be noise.

## Score (out of 25)

| Axis | Score |
|---|---|
| Calibrated certainty | 3 |
| Data realism | 3 |
| Buildable in 6 months | 2 |
| Edge vs Zanskar | 4 |
| Drives rights and sensors | 5 |
| **Total** | **17** |
