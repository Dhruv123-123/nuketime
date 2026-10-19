# Drill hole cost hunt: verdict

Written 19 October 2026. 14 research agents (8 lanes, 6 follow-ups). Every number below is cited in the
lane file named next to it; "(est.)" marks our own arithmetic. Currency is CAD unless marked.

## Verdict

**There is no separate venture-scale company in making exploratory drill holes cheaper.** The money in a
hole is people, days on site and logistics, not rock physics, and contractors, Imdex and the targeting
companies already own every part that can be squeezed. The one lever that is large (drill fewer holes)
is targeting plus owning the ground, which is what Terranox, KoBold, VerAI and Earth AI already do.
Every shape that tries to stand apart from owning the ground comes out tool-sized (under ~USD 0.5B/yr)
or already funded. The useful output is four Terranox features, listed at the end.

## What a hole costs and why (lane A, r2_verification)

| Program | All-in | Per hole |
|---|---|---|
| IsoEnergy Larocque East 2025 (actual, 39 holes, ~400 m) | C$549/m | C$220k |
| IsoEnergy Hawk 2025 (actual, 4 holes, ~900 m) | C$1,140/m | C$1.02M |
| NexGen Patterson Corridor East 2024 (46 holes) | C$736/m before camp and labour | ~C$540k |
| Denison Wheeler River 2025 | C$472/m | ~C$370k |
| Paladin PLS H1 2026 (road access, existing camp) | ~C$365/m | |
| Refined Energy 2026 budget (3 holes, heli-supported) | ~C$1,400-1,650/m | ~C$570k |

- Median of 14 programs: about **C$550/m, C$200k-550k per hole**, over C$1M for deep remote holes.
- IsoEnergy's line items (the only full breakdown found): contractor 55%, camp 14%, labour 12%,
  community and safety 6.5%, **assays 3%**.
- Model that reproduces both IsoEnergy programs: **cost = C$1.0-1.5M fixed per project-season + C$300-500/m**.
  For a 5-hole junior season the fixed share is 45-50%.
- Contractor rate is C$250-400/m; the true all-in cost is 1.5-5x that.
- Cost per metre does not fall with technology. Quebec's census: C$110/m (2006) to C$170/m (2018)
  for drilling outside producing mines; Australia A$89/m (1997) to A$207/m (2017). It tracks the
  drilling cycle (lane C).
- Hit rates: basin-wide, C$2.87B (1967-2017) found 75 deposits, 25 mined: C$38M per deposit,
  C$114M per mine (Wallis, CIM 2018). Roughly 70-130 holes per deposit (est.). Greenfield holes
  mostly miss; step-outs from a known structure hit 60-90%.
- Global: about 700,000 m and USD 200M+ per discovery (MinEx/Schodde 2019), up from 200,000 m in 1985.

So the waste is in **how many holes** it takes, and in the fixed season cost, not in dollars per metre.

## The ceiling (lane B)

- Nonferrous exploration budgets: USD 12.4B (2025, S&P); grassroots a record-low 21%.
- Contracted exploration plus resource-definition drilling: about **USD 7.5B/yr** (est., 6-9B); true
  grassroots discovery holes about USD 1.5-2B; uranium about USD 0.35-0.6B; Athabasca C$250-480M.
- Australia drilled 11.8M m in the year to June 2026 (ABS); Canada 4.6M m of surface core in 2024.
- Contractors are low-margin and small: Major Drilling CAD 889M revenue, 11.6% EBITDA, 688 rigs at ~50%
  use; Boart Longyear taken private for ~USD 371M (2024); Energold went into CCAA (2019).
- Tool benchmark: Imdex A$520M revenue (FY26), 31% EBITDA, about A$2.40 of every A$100 of exploration
  spend. Seequent sold for ~USD 1.05B. That is the size a drilling tool or software company reaches.
- MinEx: 2012-21 the world spent USD 196B and found USD 135B of discovery value (0.69x). Halving the
  cost per metre only gets to break-even; better targeting matters more.

## Every shape tested, scored on the gold rubric

Rubric items (1 point each, 6 max): (1) discovery is 80%+ of a sellable rung and the physical step is
trivial; (2) ML on public, illegible data is what makes it solvable; (3) the unproven right is cheap;
(4) a capitalised buyer pays a step-up at once; (5) a ladder to climb; (6) a very large ceiling.
Scores are our synthesis of the lane files.

| Shape | Score | Why it dies | Who owns it | vs 3 Oct rule | File |
|---|---|---|---|---|---|
| Geothermal prove-and-sell (outside Zanskar) | 3.5 | Buyers pay little for proven-unbuilt resource (~USD 0.25M/MW vs 4.4M/MW operating); step-up is at PPA/plant | Zanskar (USD 180M, 250k+ acres, US); Invenergy, Ormat hold leases | Inside | r2_geothermal |
| Drill-for-royalty underwriter | 3 | 1% NSR costs ~C$1M cash; breaks even only at 5-11% program hit rate vs 1.5-9% with ML lift; few hundred wins to learn from | VerAI (1.5% + 1.5% NSR, USD 24M B), Earth AI, Lithosquare | Never drills, but lives on drilling | r2_drill_royalty_fund |
| Stake covered ground, then strat-drill | 3 | Neighbours stake next door (East Tennant: 10 gov holes, 30+ companies took 140k km²); buyers pay by earn-in | Nobody private found | Inside | r2_wildcards |
| Re-enter old holes that stopped short | 2.5 | One-time pool (493 holes, ~C$20-60M); blank field may be missing data | Nobody | Inside | r2_wildcards |
| Neighbour drill-data market | 2 | ~C$3-25M/yr traded in the Athabasca; data goes public in 3 years anyway | Nobody (oil has done it for a century) | Never drills | r2_wildcards |
| Sequential drill planner sold to juniors | 2 | ~60 Athabasca juniors; only big if it takes royalties, which is VerAI/Terranox | KoBold in-house; Stanford paper | Software | lane D, lane F |
| Drilling-difficulty predictor | 1.5 | Real labels in SMAD free text, no incumbent, but buyer pool is tiny | Nobody | Software | lane F |
| Crew-light automated operator | 1.5 | Physical step is the product; Athabasca all-in only 12-20% cheaper; ~USD 2-5B ceiling at best | Durin (USD 3.4M), XtremeX (USD 11M A, Ivanhoe), Boart, Epiroc, Sandvik | Inside | r2_automated_operator |
| Groundwater rights proven by test wells | 1.5 | Permits, not wells, are the hard step; Vidler sold for USD 291M after 25 years | Vidler/D.R. Horton, Cadiz, Pure Cycle | Outside | r2_groundwater |
| Shared logistics / basin operator | 1 | Coordination waste is 5-12% of program cost; crews and secrecy block pooling | CorePlan, Seequent MX Deposit | Inside | lane H |
| At-rig sensing / core scanning | 1 | Owned and tool-sized | Imdex, Epiroc/Corescan, Boart/Minalyze, GeologicAI | Inside | lane D |
| Cheaper rig hardware (RC, coiled tubing, portable, plasma) | 0.5 | Chips don't serve Athabasca core needs at 400-800 m; RoXplorer still pre-commercial after 16 years | Contractors, Imdex, MinEx CRC | Inside | lane C |
| Hydrogen, CCS, lithium brine, helium, O&G wildcats, offshore wind, geotech | 1-2 | No step-up buyer, crowded, or a service market | Koloma, TGS, Fugro and others | Mostly inside | lane G |

Highest score 3.5/6. None passes items 1 and 6 together. **Law of this hunt:** wherever the hole is
the expensive step, the hole is physical work with thin margins, and the value of the hole lands on
whoever owns the ground. A company that does not own the ground captures a fee, and fees here are
tool-sized.

## What to take into Terranox instead

1. **Sequential drill planner.** Choose the next hole along a conductor from what earlier holes found,
   and decide when to wedge or walk away. The Stanford/KoBold paper (arXiv 2410.10610) reached a 6x6
   grid's go/no-go accuracy with under half the holes in simulation. At C$200k-550k a hole, two holes
   saved per property pays for the whole season's software. Lane D, lane F (W4).
2. **Stopped-short hole list.** 493 historic Athabasca holes of 100 m or more have no recorded
   unconformity while holes within 2 km reach it deeper (median length 192 m, median shortfall 84 m,
   ~120k m already drilled). Rank by why they stopped (SMAD text) and whether the ground is open.
   `sask_drillholes_pull.py` rebuilds the pull. r2_wildcards section 3.
3. **Buy neighbours' misses.** Pay juniors for unreleased logs on adjacent claims, partly in royalty
   (oil's bottom-hole contribution). r2_wildcards.
4. **Sell targets on ground Terranox doesn't want for 1-2% NSRs**, the VerAI structure, and build the
   program-outcome base-rate dataset for its own stop/continue calls first. r2_drill_royalty_fund.

Also: drilling-difficulty labels (lost holes, altered sandstone) exist only in SMAD free text; CanAlaska's
2012 Cree East program got only 10 of 15 holes to target depth. A Terranox cost model that budgets
contingency per collar is cheap to build from the same text (lane F, W2).

## Watch

The 15% METC and 30% CMETC flow-through credits both lapse on **31 March 2027** unless extended
(uranium is on the CMETC list). That hits every junior's 2027 financing, Terranox's included (r2_wildcards,
r2_verification).

## Gaps

Shared web-search budgets ran out in most lanes; figures marked "(memory)" or "(estimate)" in the lane
files are unverified. Still open: Athabasca-only metres per year (no one publishes it), helicopter
line items, whether SMAD logs are image-only scans, any documented re-entry of an old Athabasca hole,
and independent checks of Earth AI's and KoBold's hit-rate claims.

## Files

BRIEF.md; lane_A_athabasca_costs, lane_B_market, lane_C_hardware, lane_D_fewer_holes,
lane_E_business_models, lane_F_public_data_ml, lane_G_adjacent_holes, lane_H_ops_logistics;
r2_automated_operator, r2_drill_royalty_fund, r2_geothermal, r2_groundwater, r2_verification,
r2_wildcards; automated_operator_model.py; sask_drillholes_pull.py; page drill_holes.html.
