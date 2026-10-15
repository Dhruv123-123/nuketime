# The eighth hunt: public data used to find and own the thing itself

Written 15 October 2026, after Dhruv rejected the Alberta closure-liability underwriter as capped by
the size of one service industry. His ask: "datasets in anything can be used for anything... the thing
which terranox does is uses this data to find uranium. find something like this using public datasets
that is unattackable." Mid-hunt he narrowed it: "look largely in the energy/ machine/robotics/deeptech/
security tech spaces". Raw output for every lane is in `research/owner/`. Page: https://claude.ai/artifact/NBpxdkX8tDvvPPFfr7gGVN

## The answer in one paragraph

Three rounds, 21 research agents, about 95 candidate companies and about 50 legal claim regimes, plus
two backtests on real data. **No idea outside geology passed the Terranox test, and the reason is
structural.** What makes Terranox hard to copy is not SMAD alone. It is that mineral tenure law hands
out exclusive rights first-come for a few dollars a hectare, and forces the old exploration record public
so the next explorer can use it. Almost no other law does both. The closest thing in Dhruv's sectors is
**Lineage: buy dormant defence R&D firms for the sole-source production rights their old SBIR
contracts carry**, which survives red-team only barely (5/10). It is the pick because it is the only
idea that cleared every filter, not because it clears the bar the way Terranox does.

## The Terranox test (what the hunt learned)

Terranox works because four things hold at once:

1. **The claim is cheap and first-come.** Stake ground for a few dollars; no auction, no incumbent's
   permission.
2. **The data is public but illegible.** Decades of scanned assessment filings that need ML to read.
3. **The asset is worth orders of magnitude more than the claim.**
4. **Realising the value needs nobody's permission.** A discovery can be sold or developed.

Every other domain failed at least one:

- **Exclusive rights that are first-come are worthless options until you spend heavily** (new ITU
  filings, FERC hydro permits, Chinese utility models, patents on predictions).
- **Exclusive rights worth a lot are $3-150M dossiers or are auctioned** (drug exclusivities, spectrum,
  aquaculture licences, grid connections).
- **Valuable stranded assets always have an owner** who sells by tender (retired telco copper, idle
  turbines, transformers, nuclear sites, dormant IPv4 blocks).
- **Where the data is truly illegible, the right is usually non-exclusive** (FAA replacement parts,
  DLA alternate sourcing, mitigation credits in a shared service area).
- **In nuclear, the regulator is the incumbent's channel.** Every asset moves by NRC licence transfer
  and state approval, which reward track record and balance sheet, not reading the data first.

## The pick: Lineage

**One line.** Federal agencies, mostly the Pentagon, have made about 219,500 small-business research (SBIR/STTR) awards since 1983. US
law says the firm that did that research, or whoever buys its assets, can be handed the follow-on
production contract sole-source, with no dollar cap and no time limit. Many of those firms are now dormant (our inference; the count is part of the kill test). Lineage reads the whole public record, finds the dormant lineages that match a live programme
need, buys them cheaply, and builds the hardware.

**The dataset and why it is public.** The SBIR/STTR award file (about 219,500 awards, abstracts,
agencies, topics; published by SBA at sbir.gov), Phase II final reports filed with DTIC (many
are public), FPDS contract actions (now linked to prior SBIR award IDs under the April 2026 reauthorization),
SAM.gov notices and sole-source justifications, and service budget exhibits.

**The law that makes it claimable.**
- 15 USC 638(r)(4) tells agencies to award Phase III work to the SBIR developer "to the greatest extent
  practicable". Phase III can be sole-source, uncapped and unlimited in time.
- The October 2020 SBA policy directive lets a **successor in interest** (a buyer of the firm or the
  relevant assets) keep that status. GAO upheld it in *Clear Align* (B-423319, 19 May 2025), where an
  asset buyer won a whole system sole-source on the strength of one SBIR-derived component, and *Bode*
  (B-423754, Nov 2025) let off-the-shelf parts ride along.
- Pub. L. 119-83 (signed 13 April 2026) reauthorised SBIR to 2031 and dropped the proposed Phase III caps.
- Only one holder can own a lineage: a licensee does not inherit it. That is the exclusive claim.

**What ML does.** Matches 220k abstracts and final reports against live requirements (budget lines,
notices, programme documents), scores which lineages a programme office would accept as "derived from"
the original work, and detects dormancy (no new awards, lapsed registrations, owners near retirement).
It is a messy text-and-graph inference problem across five public sources.

**Why the company owns the upside.** It holds the right and builds the product. The ceiling is the value
of a defence hardware company with a portfolio of sole-source positions, not a software market. Phase
III obligations run about $2.5-3.7B a year across agencies. Arlington Capital's roll-up of SBIR firms,
BlueHalo, sold to AeroVironment for about $4.1B in April 2025.

**Why it is only a 5, stated plainly.**
- **Phase III is a preference, not a right.** GAO's *G2 Ops* decision (Feb 2026) says an agency need not
  use it. A contracting officer and a programme office must want the product.
- **Dormant lineages mostly lost their data rights.** The 20-year SBIR data-rights period applies to
  awards after the 2019 directive (DFARS caught up in Jan 2025). Older dormant firms keep the Phase III
  preference but not the data protection.
- **Lineage is already priced by buyers** (primes, Arlington-style roll-ups, corporate venture arms;
  SBIR Advisors sells a sole-source catalogue on AWS Marketplace), and the 2026 law makes lineage links
  public in FPDS, which erodes a pure data edge.
- **A shell with no team wins nothing.** The company has to be a real builder, so the edge is in deal
  sourcing for a hardware company, not a standalone moat.
- No commercial actor was found running a data-driven hunt for dormant lineages; an open-source research
  repo (`hollomancer/sbir-analytics`) already does much of the matching.

**First proof (not run here).** Take Phase II awards from 2012-2018. Predict which received more than $10M
of Phase III within five years from text similarity to later requirements plus dormancy signals, against
an agency x topic lookup. Kill it if the model adds less than 0.05 AUC, or if fewer than about 20
post-2019 lineages sit in inactive firms with a live programme match. The award file is blocked from
this cloud environment (sbir.gov returns 403) and too large to mirror; it runs from any laptop, starting
from `hollomancer/sbir-analytics` v0.18.0.

## Runners-up and what killed them

| Idea | Score | Sector | Why it is not the pick |
|---|---|---|---|
| Grid-capacity attrition: predict which queued projects drop out, option land where capacity frees, sell powered sites | 6 then killed by our backtest | Energy | Our backtest on Berkeley Lab data (below) found no edge over a lookup table; Cloverleaf (7 GW sold), Tract, GridCARE hold the position |
| Never-fired gas turbines stranded at dead projects worldwide | 5 | Energy | Hallador bought 460 MW for $350M in June 2026; OEMs track every serial number; one-off window until 2029-31 |
| Buying orphaned industrial-control software lines | 5 | Security | Won by capital and M&A, not by claiming first |
| "First US approval" drug company (foreign-approved and rejected-but-fixable drugs) | 5.5 | Off-sector | Pool about 7 drugs a year; IQVIA and Citeline already list them; ML is diligence, not discovery. Proof built (below) |
| Hazardous-waste reclaimer reading EPA manifests | 5 | Materials | Half the revenue is a disposal service; incumbents copy the targeting |
| Ecological mitigation banks | 6 then dead | Land | RIBITS is read by everyone; WOTUS rules cut demand; ceiling $1-3B |
| Dormant ITU satellite priority | 3-6 | Space | Dozens of filings, 4-6 buyers, no ML edge |
| Dormant legacy IPv4 blocks | 4 | Security | Pool $0.6-1.8B and shrinking; Hilco and Brander already hunt them |
| Nuclear site banking / decommissioning trusts | 2-4 | Nuclear | Trusts roughly fully funded ($94.7B vs over $90B costs); sites held by Holtec, EnergySolutions, Elementl |
| Robotic landfill mining, telco copper, plant part-out | 4 | Robotics | Value has a legal owner who sells by tender |

Killed outright with evidence in the lane files: AI materials discovery, FAA PMA parts, DLA sourcing,
QPL slots, space salvage, AI vulnerability bounties, EOL open-source maintenance, law-forced equipment
replacement (FCC Covered List actions apply only to new approvals), transformers, PJM plant arbitrage,
backup-generator aggregation, unapproved-drug NDAs, PRV farming, water rights, farmland, quota, akiya,
tax liens, class-action claims, music royalties, carbon credits.

## Proofs run on real data

**1. Grid-queue attrition (energy).** `research/owner/proof/attrition_backtest.py` on Berkeley Lab
"Queued Up" snapshots for end-2024 (36,441 projects) and end-2025 (38,201), from GitHub mirrors.
Features come only from the earlier snapshot; labels from the later one.

| Test | Model AUC | Lookup baseline AUC | Top-100 POIs capture of freed MW (model / naive) |
|---|---|---|---|
| Leave-one-region-out, 9,940 active projects, 30% withdrew in 2025 | 0.721 | 0.727 (type x study phase) | 17.9% / 14.5% |
| Train end-2023, test end-2024 (ERCOT, PJM, ISO-NE) | 0.629 | 0.648 (region x type) | 22.5% / 27.1% |

Public queue lists alone do not beat a lookup table. That is why the energy runner-up was killed.

**2. Drugs approved abroad but not in the US (off-sector).** `research/owner/proof/build_gap.py` joins
DrugCentral (Nov 2023), the EMA EPAR list (Feb 2023), WHO ATC and a 401-row FDA rejection-letter table.
296 of 1,143 ex-US ingredients have no US approval; 112 are usable small molecules. Backtest: 12 of 20
known Europe-first drugs would have been flagged 0.2-11.6 years early (pitolisant 3.4 years,
amifampridine 8.9). Limit: US data ends in 2023, so this is not a point-in-time test.

## Round 4: Dhruv's correction (15 Oct, 04:56Z)

Dhruv corrected test part 1: Terranox does not get claims first-come, it **buys** mineral rights. The real
bar is that **ML/AI is what makes the pain point solvable**. Corrected test: buy the right at a price set by
people who cannot see its value; the value hides in illegible public data that only ML can read at scale;
the asset is worth far more than its price; the company realises the value itself. Every candidate was
rescored (`research/owner/r4_rescore.md`) and a fresh sweep run (`r4_sweep.md`).

**New lead: powered brownfields (8/8 on the corrected test).** Buy contaminated former industrial and
power sites, which already carry substations, rail and water, at the stigma discount. Price the real
cleanup cost and time from state case files (California GeoTracker alone has 230M+ lab rows, boring logs
and reports, forced public by its electronic-submittal rules). Then clean them up and sell or develop them
as powered industrial and data-centre land. Sellers and lenders cannot price the cleanup; a model trained
on decades of case files can. No ML-led principal buyer was found (Liora sells AI remediation as a
service; Cherokee-style brownfield funds underwrite by hand). It is energy-adjacent, not core energy.

**Proof run (`research/owner/proof/cleanup_backtest.py`).** On 20,390 Pennsylvania storage-tank cleanup
incidents (structured fields and short descriptions only, GitHub mirror of PA DEP data): train on
1995-2007, test on 2008-2012, predicting closure within 3 years. Model AUC **0.727** vs **0.695** for an
impact x substance lookup (+0.03; top-decile lift 1.79 vs 1.68). That is a real but small edge, under our
0.05 bar. The structured record alone is not enough; the thesis rests on reading the illegible part (lab
time series, boring logs, consultant reports), which is blocked from this environment. **Kill test:** on
GeoTracker, a model using lab and boring-log data must beat the lookup by 0.05 AUC on time-to-closure,
and listed sale discounts must exceed predicted cost on at least 20 powered sites.

**Rescored shortlist on the corrected test.**

| Idea | Score | Sector | Main doubt |
|---|---|---|---|
| Powered brownfields | 8/8 | Energy-adjacent | Proof above shows structured data alone gives +0.03 AUC |
| Orphaned OT/ICS software lines | 7/8 | Security | ML finds targets; value is M&A skill |
| Corridor rights from scanned railroad deeds and valuation maps | 6/10 | Energy (transmission, fibre) | Big railroads hold the best corridors; siting approval |
| Underperforming solar/wind bought on a public screen, fixed with robotic O&M | 6/8 | Energy, robotics | Gap is visible in diligence data |
| Lineage (SBIR) | 5/8 | Deeptech | Agency can decline Phase III; FPDS linkage makes matching a join |

## Round 5: the California kill test (15 Oct, 23:12Z)

Dhruv, 21:32Z: "use a lot of compute and actually run a really deep experiment of doing this in cali."
Run on the full GeoTracker record in a cloud environment with network access (pipeline `research/owner/ca/`,
results `research/owner/ca/results/`): the statewide case table, 232 county well and boring files and 58
county lab files, 4.4 GB zipped, 230M+ lab rows. Panel: every cleanup case (LUST, Cleanup Program,
Military) open on 1 January of 2004, 2007, 2010, 2013, 2016 and 2019, with features built only from records
dated before that day, and the label "closed within five years". 96,761 site-snapshots over 27,956 cases.
Two leaks were found and removed before any number was read (present-day site-history text; all-time well
counts), and dropping the present-day lead-agency field moves the result by under 0.005.

Four scorers on the temporal test (train through 2013, test on 2016 and 2019, n = 21,502):

| scorer | AUC | top-decile lift |
|---|---|---|
| lookup: case type x county | 0.763 | 2.1 |
| lookup: case type x status x years open (the buyer's heuristic) | 0.768 | 2.9 |
| LightGBM on the structured fields only | 0.842 | 3.3 |
| LightGBM on everything (lab series per analyte, wells, activity text, neighbours) | **0.846** | 3.2 |

Held-out counties: 0.694 / 0.768 / 0.794 for the heuristic, structured and full models. On the sites that
have lab data: structured 0.815, full 0.844. Time to closure among sites that did close: MAE 1.13 vs 1.26
years, Spearman 0.34 vs 0.01 for the lookup.

Buying simulation at 2016: among 1,277 open sites within 3 km of a 230 kV or larger substation, the full
model's top 300 closed within five years at 75%, the buyer's heuristic's top 300 at 60%, a random 300 at 29%.
Within 3 km of 115 kV or larger (4,216 sites): 88% vs 80% vs 28%.

**Verdict: fails the kill bar.** ML beats what buyers use by +0.08 AUC (bar 0.05: passed). The illegible
record adds **+0.004** over ML on the structured fields alone (bar 0.02: failed); it is worth about +0.03
only where lab data exists and in counties the model has never seen. The edge is real and it is ML, but it
comes from a 40 MB case table anyone can model in a week, not from the 230M-row record. That fails the second
leg of the corrected test: ML is not what makes the problem solvable here, it makes a solvable problem a
little better solved. A brownfield buyer with this model would beat the field, and nothing would stop the
next buyer from building the same model.

**Cost (run after the closure numbers).** The 3,779 archived Cleanup Fund claims (2020 capture, in
`research/owner/ca/data/cuf/`) gave 1,530 sites with a reimbursed-to-date figure, 1,185 of them open at the
2010 snapshot; median $808k, 11% at the $1.5M cap. Leave-counties-out, predicting log10 reimbursed-to-date:
Spearman **0.60** for the full model, 0.55 for structured fields plus sampling volume, 0.37 structured only,
0.26 for the lookup (MAE in log10: 0.21 / 0.22 / 0.27 / 0.26; 2007 snapshot similar). That looks like the lab
record finally earning its keep, but it is weaker than it looks: reimbursed-to-date includes money spent
before the snapshot, and the count of lab samples before the snapshot is a direct record of that spend. Volume
alone takes the structured model from 0.37 to 0.55; concentrations, trends and text add about +0.05. So the
lab record mostly tells you what has already been spent, not what cleanup will cost from here. A forward cost
test needs dated reimbursements per site, which the archive does not hold (the FY2024-25 payments file has no
site id). The verdict stands. Also untested: mispricing. The simulation shows which
sites close, not which are cheap; the sites the model likes may already be priced near clean. The listed
discount versus predicted cost test on 20 powered sites needs listing data this environment does not have.

**What it does to the shortlist.** Powered brownfields drops from 8/8 to about 5/8: still a business (an
ML-underwritten brownfield developer near substations), not an unattackable one; its moat would be capital
and execution, like any developer's. The pattern across the three backtests (grid queue: no edge; PA tanks:
+0.03 from structured fields; California: +0.08 from structured fields and +0.004 from the illegible part) is
that in regulatory case records the legible fields carry the signal, because the regulator already writes the
outcome-relevant facts into them. Terranox's edge survives because geology logs are illegible **and** the
outcome (ore) is not summarised anywhere in the record. That is the property to look for next, and it is
rare: scanned deeds and valuation maps (corridor title), scanned interconnection and system-impact studies,
and old well logs have it; status tables, permits and advisories do not.

## The decision for Dhruv (updated after round 5)

1. **Build the application around Terranox and what it already proves.** Eight hunts and three real-data
   backtests say the "public data only ML can read, outcome not summarised anywhere" moat lives in geology.
   Terranox has it. (Recommended.)
2. **Keep brownfields as a developer play** with ML underwriting and an execution moat. It is a real edge
   over today's buyers (+15 points of closure in a 300-site portfolio near 230 kV) but it is copyable, and
   the cost and mispricing legs are unproven.
3. **One more kill test on a record with the Terranox property**: corridor title from scanned railroad
   deeds and ICC valuation maps (6/10 in round 4; transmission and fibre siting), or scanned interconnection
   studies. Expect a data-access fight before any modelling.

Earlier decision list (written before round 4): take Lineage to its kill test; accept the moat is
geological; or drop the claim requirement and rank on execution moats.

Search budget used: about 360 web searches across three rounds. Government data hosts (fda.gov, sbir.gov,
eia.gov, NRC, EMA) were blocked from this environment; datasets were checked against documentation, and
both proofs ran on GitHub mirrors.
