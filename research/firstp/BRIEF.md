# First-principles sweep brief (2026-10-19)

Dhruv (applying to YC end Nov 2026) needs ONE new company idea. His existing company Terranox (YC W26) uses ML on SMAD, Saskatchewan's public mineral assessment archive, to find uranium and BUYS the mineral right cheap before proving it. The new company must NOT be Terranox.

## Standing rules (kept in every sweep unless your sweep's relaxation says otherwise)
- No prospecting- or drilling-related ideas (no mineral/oil/gas/geothermal/hydrogen exploration, no tailings or placer hunting).
- Own the valuable thing you find or make; not a service or consulting firm.
- ML must be what makes the pain solvable, not a nice-to-have.
- "Too small" kills: needs a credible path to a $1B+ company.
- Sectors: largely energy, machines, robotics, deeptech, security tech, but Dhruv said "look broad, go crazy".

## The gold rubric (score each idea 0-5 on each, total /25)
C1 Frame: a discrete sellable rung where discovery is 80%+ of the work, the physical step is trivial or abstracted, a capitalised buyer buys the rung's output.
C2 Step-up: proving takes the asset from near zero to a big step-up at once (5 = 10^3x+, 3 = 10-100x, 1 = <3x).
C3 Lever: the proving step is expensive and usually fails, so ML cuts discovery capex ~10x (lever capped at 1/base hit rate).
C4 Data and right: signal in public-but-illegible data, outcome in no legible field, unproven right buyable cheaply from owners who cannot read the data.
C5 Ladder: rungs above lead to the whole chain.

## The six laws that killed ~570 ideas in nine hunts
L1 Cheap proofs usually succeed: in human-made systems (permits, filings, studies) the proof passes 50-90%, so lever is 1.1-3x; proofs that usually fail are the expensive bespoke build.
L2 Someone always records the outcome: a regulator/market publishes a legible summary field, so a lookup table is within 0.03-0.08 AUC of the best model.
L3 The seller already prices in the hope: unproven rights are not cheap (German edge fields 15-40% of building-land price; data-centre farmers ask 5-10x; Millrose buys at cost plus yield).
L4 Public bodies reprice to market or keep the best: trust lands reprice to fair value; WaterNSW / Newfoundland tender after reading their own files; FERC permits non-transferable.
L5 Where nature hides the thing, nobody owns it to sell: product-of-nature doctrine, first-come filings, and no buyer pays at the proof stage.
L6 Ladder: every first rung of a real industry is already held by a funded startup or a private-equity roll-up.

## Old ideas (already scored and killed) are in this repo
- research/converge/PICK9.md (all 7 rounds summarised, laws, tables)
- research/converge/gold/ALL_SCORES.md and scored_263.csv (every round-1 idea with reason), round4_results.json ... round7_results.json, nature_results.json (round 2), proof_results.json (round 3), nearmiss_verify.json, deep_*.md
- research/converge/PICK.md ... PICK8.md (earlier picks: powered brownfields, TRISO sorting, nuclear contract manufacturer, heat-to-power, Margin, Alberta closure liability, Lineage SBIR)
Use grep/jq; don't read giant JSON files whole.
