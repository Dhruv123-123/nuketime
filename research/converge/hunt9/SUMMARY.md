# Hunt 9 sweeps: cross-sweep read (17 Oct 2026, 22:05Z)

Eight sweeps (A energy sites, B title and rights, C government rights, D hidden physical condition, E claims and credits,
F life sciences and agriculture, G non-US regimes and wildcards, H first principles) scored about 115 candidates against
the four-part drill test in `BRIEF.md` and the rubric in `RUBRIC.md`. Each sweep's full report, with sources, kill tests
and per-candidate doubts, is in `sweep_*.md`. Caveat: the shared web-search budget ran out part-way through the sweeps
(sweep H had none at all), so figures tagged "(memory)" or "(my estimate)" in the reports are unverified and the gold-rubric
thread should firm them up before relying on them.

## Ranking (sweep scores, 0-10; two scores where two sweeps met the same candidate)

| # | Candidate | Scores | Proving step, cost, base hit rate p | Step-up R1 | Pool | Incumbents | Biggest doubt |
|---|---|---|---|---|---|---|---|
| 1 | Land-promotion junior: option farmland, win planning consent, sell consented land to housebuilders (UK first; US entitlement, Australia later) | B 6, H 7 | Outline permission plus appeal; £25-40k per gross acre or £250k-1M per site; 2-5 years; p 0.3-0.67 (Gladman about 2/3; appeals 60% won where the council lacks a 5-year land supply vs 30% where it has one); lever 1.5-3x | Farmland £21k/ha to consented £1-6M/ha (50-300x); promoter keeps 20-25% under an exclusive option | £10-20B/yr of consented-land value (estimate); Gladman sold 2,796 plots/yr; Barratt bought Gladman for £250M | Gladman, Catesby, Richborough, Rosconn, Hallam; LandTech and Searchland already legibilise part of the data | p is high and the 5-year land supply and Housing Delivery Test are legible fields. Kill test: 200 PINS appeal letters, see whether those two fields predict within 0.05 AUC |
| 2 | Mitigation-bank junior: buy drained or hydric farmland bilaterally, win Interagency Review Team approval, sell wetland and species credits or the approved bank | F 7, H 6.5, E 5 | IRT instrument approval, average 1,100-1,200 days (496 banks), $1-5M per bank; p(sells out in 5 years) 0.3-0.5 (estimate), lever 2-3x; about 70% of released credits ever sold | Farmland $3-10k/acre to credits $8.6k (MS) to $134k (NC) to $675k (NJ) per acre; 10-100x on credit-bearing acres, 3-10x per parcel | About $3-8B/yr credit demand; 1,200+ banks, 750,000 credits; EIP funds $181M, $303M, $454.5M; banks trade before sell-out (EIP, RES/KKR, Westervelt) | EIP, RES, Westervelt, Wildlands; GIS and spreadsheets, no ML seen | Sackett 2023 shrank jurisdiction; the hidden state is demand, not approval; RIBITS supply side is legible. Kill test: RIBITS credits sold vs available in five districts |
| 3 | Orphaned-source NSNs: buy drawings, tooling and approved-source status of defunct sole-source part makers, re-approve through DLA | C 6 | Source Approval Request plus first article, $25-250k per NSN, about 1 year; p 10% (2009-11 L&M sample) to 49% of decided (FY17) | Comparable: $925k for a whole light-aircraft type-certificate line plus tooling; proven state is a sole-source supplier with DLA demand | $7.9B sole-source spares on 136 large contracts FY15-19; 4M consumable NSNs | TransDigm, HEICO, Ontic, PE roll-ups, DLA's own reverse-engineering programme | The proven state is an operating business with small dollars per NSN; AMSC codes are a legible field. Kill: FLIS NSNs with AMSC B/C/P/R, >= $40k demand and a SAM-expired sole CAGE; kill if < 2,000 NSNs or < $200M/yr |
| 4 | Unenforced commercial civil judgments: buy judgments at pennies, find assets, enforce | E 6, H 5 | Enforcement and asset discovery, $1-10k and 6-24 months per judgment; p 0.15-0.25 (80% of US judgments never enforced), lever 4-7x | Bought at 2c (small) to 73c (large collectible); proven at 100c plus 6-10% interest; per-hit 10-50x, blended 2-10x | $97B unpaid federal judgments; state commercial pool > $100B (estimate) | Encore, PRA (consumer, bureau data), small recovery shops, JudgmentMarketplace; no ML buyer found | Private bureau data may already make the join legible; collections reputation |
| 5 | Shelved clinical-stage compounds (Roivant model) | F 5, H 6 | Phase 2, $6-20M, 2-3 years; p 0.29 Phase II to III (0.45 rare disease), lever 3.5x | Licences at $5-45M; Telavant sold for $7.1B upfront 11 months after a $45M purchase | Large | Roivant, BridgeBio, XOMA/Ligand; Every Cure, Healx, BenevolentAI, Formation Bio read the same archives | Sellers are the best-informed party; occupied |
| 6 | Art "sleepers": vision ML over regional auction lot images, then authentication | G 5, H 6 | Buy, clean, technical analysis, expert dossier; $5-100k, 6 months to 5 years; p 2-10% on a filtered shortlist, lever 10-50x | 63x (Artemisia), 1,000x (Constable), Salvator Mundi $1,175 to $450M | Sleeper value creation $100-300M/yr: too niche | Philip Mould, Turquin, Colnaghi, Art Recognition | The best structural fit in the hunt on the smallest pool |
| 7 | Powered land for data centres via large-load interconnection | A 5, E 5 | Utility large-load study and energy services agreement, deposits $40-90k/MW, 1-3 years; about 28% of 1,066 GW requested likely committed | $10k/acre rural to six figures once powered; NoVA $4M unpowered vs $6M+ powered per acre; Stream paid $305-466k/MW for a site | $6B of data-centre land bought H1 2026 | Tract, Cloverleaf, GridCARE, Crusoe, Verrus, hyperscaler site teams | Occupied, as the seen list said |
| 8 | Closed-loop pumped-storage licence flipping | A 5 | FERC licence, millions to tens of millions, 5+ years; permit-to-licence about 5% | Licensed projects trade pre-build (CIP bought Swan Lake and Goldendale; Statkraft bought Red John); licence worth 1-5% of capex | 59-91 GW pipeline, about 5 licences since 2014 | Rye, CIP, Absaroka | Topography is legible (ANU atlas); the failure mode is financing, not hidden state |
| 9 | Western US agriculture-to-urban water rights | B 5, F 5, H 4 | Water-court change case, > $100k legal, 3-10 years; p 0.5-0.9 in basin, lever 1.2-2x | Vidler 3-5x per deal; C-BT units $7k (2010) to $57-85k/AF (2025) | About $1B/yr of transactions | Water Asset Management, Greenstone, Vidler, RWR | OpenET is erasing the illegibility; the risk is political |
| 10 | Mexico ejido to full title on nearshoring corridors | B 5 | Qualified assembly plus registration, 1-3 years; 3.4% of social property converted since 1991 | Ejidal farmland $1-5/m2 to serviced industrial $60-150/m2 | 99.5M ha ejidal | Local developers and nominees | Outsiders cannot legally hold the right before conversion: fatal |

Scored 4 or below by their sweeps (details in the reports): non-powered dam licences (A 3, D 4: permits are free and first-come,
licences do not get built), Florida ageing-condo assembly (D 4), retired CF6 engine cores to 48 MW turbines (D 4, no public
signal), German onshore wind permits (A 4.5, p near 1), Norwegian fall rights (A 4, pool $100-150M), Chilean water rights (G 4),
Nazi-era looted-art claims (G 4), catastrophe subrogation (E 4), veterinary reuse of human molecules (F 4), legacy IPv4 (B 4),
pesticide registrations (C 4), approved-but-unlaunched ANDAs (C 5), SBIR lineage (C 5, no evidence anyone buys dormant firms for
Phase III), reverter archaeology in scanned deed books (H 5), post-Sackett jurisdictional determinations (H 5), coal-to-nuclear
Early Site Permits (A 2: p about 0.85, DOE published the list, no ESP site has ever traded), CMMC arbitrage (C 2), remanufactured
transformers and aircraft part-outs (D 3), carbon credits (E: 3.8% of Verra projects rejected, no class imbalance).

## What the eight sweeps found, as laws

1. **Adjudications and permits mostly succeed once filed.** Title cases settle, permits are granted, licences issue: p is 0.5-0.9
   across sweeps A, B and E, so the lever cap is 1.1-3x, not 10x. The low-p steps in the economy (judgment enforcement 0.15-0.25,
   art authentication 0.02-0.1, pumped-storage licences 0.05, DLA source approval 0.1-0.5, Phase 2 trials 0.29) sit on small
   pools, political holders, or occupied ground.
2. **Where the pool is big, a regulator has already published the ranking.** DOE's 54,000-dam list, INL's 315 coal sites, the ANU
   pumped-storage atlas, utility hosting-capacity maps, RIBITS, AMSC codes, the Orange Book, the Housing Delivery Test and 5-year
   land supply statements. The signal is legible exactly where the money is.
3. **Machines keep their hidden state in private records.** Aircraft, engines, ships, turbines, transformers and fab tools: the
   owner holds the maintenance file, so the owner is the informed party and sells by tender. Buildings: the regulator publishes
   the hazard list and the market prices it on day one (sweep D, nothing above 4).
4. **Where the 10^4 structure does exist**, the pool is small (art sleepers), the right cannot be held before proving (ejido land,
   qui tam), or the holder is a state (restitution, sovereign awards).
5. **The two nearest Terranox analogues in the whole economy are land promotion and mitigation banking.** Both have a junior/major
   split with capitalised buyers (housebuilders; EIP and RES), bilateral options or purchases from farmers who price corn, a
   50-300x or 10-100x step-up on the proven acre, a proven state that sells before the build, and a PDF-bound signal (planning
   appeal letters; 404 permits and jurisdictional determinations). Both fail the lever test (p 0.3-0.67) and both carry a
   legibility doubt. They are the ones that "got close on the full frame", which Dhruv's refinement says to treat as very
   promising, and both have a ladder (promoter to developer; bank sponsor to restoration contractor to credit buyer).

The gold-rubric thread owns the next step. The kill tests above are each a few days of public-data work and no building.
