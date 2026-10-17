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

**Reframed as a proof of concept (Dhruv, 23:58Z: "don't check your ideas on the basis of the model's
efficiency; treat this as a PoC and idea project").** The kill bar above was our own criterion for
"unattackable". Dropping it, what the run proves for the idea: (1) the public record is enough to rank
California's 10,053 open contaminated sites by how fast they will close, three times better than random and
clearly better than how buyers rank them today (0.846 vs 0.768; 75% vs 60% of a 300-site book near 230 kV
substations closed within five years); (2) the same model ranks total cleanup spend (Spearman 0.60 vs 0.26
for the lookup); (3) the whole pipeline runs end to end in under two hours on one machine, so the
"ML-armed vulture" is buildable now, and the moat is speed plus doing the remediation and redevelopment
yourself, which is the Terranox pivot (sell predictions, then do the drilling) mapped one to one. What the
PoC does not yet show, in the order the cofounder asked: (a) that the discount exists (no price data here);
(b) that enough built-out industrial sites exist (the top of the list is gas stations; the industrial class
is a third of cases and needs a plant list joined in); (c) that cleanup can be done very profitably (the cost
label is cumulative, not forward); (d) one use case, where the data points at powered load on the
industrial and plant class.

**Built-out test (16 Oct, 00:05Z; `research/owner/ca/builtout.py`, results in `results/builtout.md`).**
Industrial-class cases only (Cleanup Program and military; no gas stations): 7,403 open today. Within 300 m of
a 115 kV+ substation, the proxy for "the substation is on or beside the parcel": **135** (24 at 230 kV+);
within 1.5 km: **1,443** (292); within 3 km: **2,928** (863). Alameda, Santa Clara, San Francisco and San
Mateo hold most of the 300 m set; Los Angeles and Sacramento most of the 3 km set. Power plants are the
cleaner test of infrastructure on the parcel: of 473 California thermal plants in EIA-860, **188** have an
open Cleanup Program or military case within 1 km (546 cases), and **44 of the 121** retired or partly
retired thermal plants do, several of them the plant's own case (Moss Landing, 1.7 GW retired, open
verification monitoring at 120 m; Humboldt Bay; Burbank's Magnolia steam plant; Alamitos). Plants with any
open case within 1 km carry 41 GW of thermal nameplate. On the industrial class alone (835 sites open at 2016
within 3 km of 230 kV+, base five-year closure 16%), the model's top 100 closed at **68%** against 45% for
the buyer's heuristic, median 1.5 years to close; the list with names and addresses is
`results/top_industrial_2016.csv`. So the built-out set in California is in the low hundreds on the parcel
and about 1,400 within 1.5 km of power: enough for one fund's book, not a national roll-up from one state.
Caveats: GeoTracker is one point per case, so refineries, bases and plants are undercounted at 300 m; the
substation layer misses plant switchyards; EIA-860 misses plants demolished before about 2001; nothing here
checks parcel size, zoning or interconnection capacity. Remaining validations after this: the discount
(next), a forward cleanup margin, and the one use case.

**Discount test (16 Oct, 00:42Z; `fetch_la_roll.py`, `fetch_la_parcels.py`, `discount.py`; results in
`results/discount.md`). Recorded prices show no stigma discount.** Under Prop 13 the assessor resets a
parcel's value to its purchase price at every change of ownership, so LA County's public roll (2006-2025,
from the county's ArcGIS services: 401k commercial, industrial and vacant parcels, 6.2M parcel-years) is a
dated sale-price record. 13,834 of LA's 15,288 GeoTracker cases fall inside a parcel polygon. After screens,
118,513 sale events on commercial and industrial parcels, 1,484 of them while a cleanup case was open.
Hedonic model against nearby clean sales (lot, building, age, use code, sale year, 1 km cell; standard
errors clustered by cell): open-case sales **+5.4%** [0.8, 10.3], 0-2 years after closure +11.3%, 2-5
years +11.9%, 5+ years +7.4%. Repeat sales on the same parcel (sold while open, then after closure, 224
pairs) **+6.9%** [0.2, 14.2] against clean repeat sales over the same years. By case type: LUST open +6.0%,
closed +11%; Cleanup Program open +4.8%, closed 2-5 years +23% (n=50, wide). Rough margin on the 312 LA
parcels with a Cleanup Fund reimbursed figure (309 gas stations): median parcel $1.3M, median uplift from
closure $60k, median cleanup reimbursed $643k; uplift minus cost positive for 13%. So the "buy at a steal"
leg fails in the record: an open case does not depress the price of a commercial or industrial parcel in
LA, closure adds mid-single digits, and on gas stations the cleanup costs ten times the uplift. Caveats:
assessor value at transfer, not the deed price; some resets are non-sale transfers; operating gas stations
carry business value; a case point on the street or a neighbouring parcel biases the estimates toward
zero; LA County only, San Francisco not run; the industrial class is thin (n=58 recently closed) and has the
largest point estimates. Other counties (`fetch_sf_roll.py`, `discount_other.py`): San Francisco has too
few treated sales to say anything (13 open); Alameda's parcel layer gives one rough cross-section (current
value deflated to the latest document year): open +14.6% [-0.3, 31.7], Cleanup Program open +28% (n=160).
Pooled industrial class, LA plus Alameda, inverse-variance: open **+7.0%** [0.5, 13.9] (n=712), closed 0-2
years **+20.0%** [1.5, 41.9] (n=75), closed 2-5 years +25.2% [4.7, 49.8] (n=64), closed 5+ years +2.1%;
pooled all types: open +6.4%, closed 0-2 years +14.4%. So the recovery right after closure is larger on
industrial sites (+13 to +18 points over open) than on gas stations (+8), on thin samples. What survives
for the thesis: any discount would have to be won off-market, and the value of a closed, powered industrial
parcel to a load customer is not in any public price record.

## Feasibility verdict (17 Oct, after Dhruv's "do it for feasibility, not implementation")

The question: is an ML-armed brownfield developer feasible, one that finds failing contaminated industrial
sites in public records faster than incumbents, buys them cheap, remediates, and sells or leases them as
powered land? Five premises, each tested on real California data, plus the one that could not be tested.

| Premise | Test | Result | Verdict |
|---|---|---|---|
| 1. Public records can rank which open sites will close, better than buyers do today | 27,956 cases at six snapshots, no future data; buying simulation at 2016 | AUC 0.846 vs 0.768 for the buyer heuristic; top 300 near 230 kV close at 75% vs 60% vs 29% random; industrial top 100 at 68% vs 45% | **Feasible**, buildable in weeks from a 40 MB table; copyable for the same reason |
| 2. ML is what makes it solvable (the Terranox test) | Full model vs structured fields only; cost model with and without the lab record | +0.004 AUC; +0.05 Spearman on cost | **Not supported**: the regulator already writes the signal into the legible fields |
| 3. Enough built-out sites exist | Industrial-class open cases near substations; EIA-860 plants joined to GeoTracker | 135 within 300 m of a 115 kV+ substation, 1,443 within 1.5 km; 188 of 473 thermal plants with an open case within 1 km, 44 of 121 retired | **Feasible for one fund's book** in California (low hundreds); a national count is unverified |
| 4. They can be bought at a steal | 118,513 LA commercial and industrial sales from the assessor roll (Prop 13 resets), plus Alameda and SF | Open-case parcels sell at +5% to +7% against clean ones, not a discount; closure adds +11-12% (industrial +20-25%, n=75 and 64) | **Not supported** in recorded prices; any discount is off-market and unproven |
| 5. Cleanup is very profitable | Cleanup Fund claims (2020: 3,779 claims; FY2024-25 payments: $123M over 866 claims) against the closure uplift | Gas-station cleanup: median $617k-808k reimbursed over a median 29 years since discovery, $25k-57k a year; closure uplift median $60k on a $1.3M parcel; 13% positive | **Not for gas stations.** On industrial sites the uplift is about $260k on a median parcel and the cost is in no public record |
| 6. A closed industrial parcel with a live substation is worth a multiple of its dirt to a load customer | None possible: no public record prices powered land | Untested | **The whole thesis now rests here** |

Reading. Feasible: a data-enabled brownfield developer that uses public records to pick the sites that
will close soonest, buys them at market, and makes its money on execution and capital, like any developer.
Not feasible on this evidence: a company whose edge is mispriced contaminated land, or ML reading data
nobody else can read. What would make it YC-sized is premise 6, which the public record cannot test: that
data centres and electrified industry waiting years for interconnection will pay a multiple for a closed
industrial parcel with a live 115 kV+ substation. That is a ten-phone-call test (powered-land brokers,
data-centre site selectors, a utility's interconnection queue), not a dataset test, and it is the one to
run next. The forward cleanup-cost model was dropped under the feasibility steer; the Fund's dated payment
ledger (121,252 payments, FY1992-93 to date) sits in Dhruv's data folder (`~/data/geotracker/cuf/`) if it
is ever wanted.

## Feasibility across the hunt (17 Oct): which public-dataset play has a real gap

Dhruv's question: of everything seen in eight hunts, which public-dataset play has a gap, and can ML be
the radically more efficient way to rebuild old factories, or only a nice-to-have?

**The law, restated with the evidence.** Public data plus ML is a company-making edge only where four
things hold at once: the record is illegible to incumbents at scale; the outcome that matters is not
summarised in any legible field; the right can be bought from people who cannot read the record; and the
buyer realises the value itself. Regulatory and administrative records fail the second condition, every
time we tested it: the regulator writes the answer into the status fields, so a lookup table gets within
0.03 to 0.08 AUC of the best model (grid queue 0.727 vs 0.721; Pennsylvania tanks 0.695 vs 0.727;
California 0.768 vs 0.846, with the 230M-row lab record worth +0.004). Geology passes because nobody
summarises where the ore is. That is the whole finding of the hunt, and it is why the shortlist below is
short.

| Play | Record | Is there a gap? | What ML is | Verdict |
|---|---|---|---|---|
| Geology (Terranox: SMAD and the other forced-public assessment files; US scanned well and gamma logs) | Scanned logs, decades deep, no outcome column | **Yes, verified by Terranox's own existence** and by eight hunts failing to find a second | The only way to read the record at scale | **The one proven play.** It is Dhruv's own company |
| Powered brownfields (GeoTracker, assessor rolls, substations, EIA-860) | Legible case tables; lab record adds nothing | **Partial**: sourcing edge real (+0.08 AUC, 75% vs 60% closure); no discount; cleanup cost dwarfs uplift on gas stations | A 5-10% sourcing edge, copyable in weeks | **Feasible as a developer, not as an ML company**; the open question is the powered-land premium (ten calls) |
| Rail corridor rights (scanned ICC valuation maps, 1910s deeds, STB abandonment dockets) for transmission and fibre routes | Truly illegible, truly unsummarised: who holds the reversion or easement on an abandoned corridor is in nobody's table | **Untested, and the only candidate with all four conditions** | Reading 100-year-old maps and deed books at scale | **The one to test next** if a second company idea is wanted: one state, two weeks, label = corridors later sold or built on. Doubts: big railroads hold the best corridors; siting approval |
| Interconnection system-impact studies (ISO and utility PDFs) | Illegible part untested; structured queue has no edge | Probably occupied (GridCARE, Cloverleaf, Tract read grid data) | Reading study PDFs for cheap-upgrade positions | **Not a gap** on the evidence; expect incumbents |
| Alberta closure-liability underwriter (AER ST37, Petrinex, Orphan Well labels) | Semi-legible; regulator's own rating is crude (C$36.6B official vs about C$260B leaked) | **Yes, but capped** by Alberta's producer base and politics; rejected by Dhruv as too small; drilling-adjacent | Scoring wells the regulator mis-rates | **Feasible, small**; proof never run (data hosts blocked) |
| Lineage (SBIR Phase III rights, FPDS) | Legible; matching is a join | Weak: Phase III is a preference, old data rights lapse, primes already price lineage | A join, not a necessity | **Feasible as an M&A roll-up**, 5/10; no data gap |
| Orphaned ICS/OT software lines (CISA advisories, vendor EOL notices) | Legible | No: value is M&A skill and capital | Target finding | **Feasible business, not a data play** |
| Underperforming solar and wind fixed with robotic O&M (EIA-860M and 923) | Legible; the gap is visible in any diligence pack | No information gap | A screen | **An operations business**, not a data play |
| Foreign-approved drugs missing in the US (DrugCentral, EMA, FDA letters) | Legible; IQVIA and Citeline list them | No; pool about 7 a year | Diligence | **Not a gap**; off-sector anyway |
| Grid-queue attrition and powered-land options (LBNL Queued Up) | Legible | No: AUC 0.721 vs 0.727 lookup; position held by Cloverleaf (7 GW sold), Tract, GridCARE | None over a lookup | **Killed** |
| Assets with an owner who sells by tender (idle turbines, telco copper, nuclear sites, IPv4, transformers) | Legible | No: the owner runs the auction | Nothing | **Killed** |
| Rights that are auctioned or cost a dossier (spectrum, drug exclusivities, grid connections, aquaculture) | Varies | No: the price is set by the auction | Nothing | **Killed** |
| Illegible records with non-exclusive rights (FAA PMA parts, DLA alternate sourcing, mitigation credits) | Illegible | No: reading it first wins nothing exclusive | Reading | **Killed** |
| Nuclear picks from hunts 1-6 (TRISO sorter, nuclear-qualified manufacturer, Margin, hafnium) | Not public-data plays | Gaps are named and occupied, or under $300M a year | Engineering productivity | Recorded for completeness; Dhruv rejected or scrapped each |

**The straight answer on rebuilding old factories.** Many firms do it, and the job's cost and time sit
in acquisition, due diligence, remediation, permits, interconnection, construction and leasing.
Identification is one or two percent of it. Our model does that one or two percent well: it scores all
10,053 open California sites in two hours and beats the buyer's heuristic by +0.08 AUC. That is a real
edge and it is copyable in weeks, because the signal sits in a 40 MB table the state publishes. For ML to
be the radically more efficient way to do the whole job it would have to shorten the part that takes
decades, and the data says that part is not a knowledge problem. The lab record and boring logs, read
in full, improve the cost prediction by +0.05 Spearman and the closure prediction by +0.004 AUC. Closure
drags because of regulatory process and monitoring, and the one thing that did compress it was policy:
California's 2012 Low-Threat Closure Policy, after which open cases fell from 22,226 (2004) to 10,053
(2019). An AI that drafts closure reports is a consultant productivity tool (Liora sells that as a
service) and the cofounder's "hardly tech" objection applies to it. Remediation itself is excavation,
pump-and-treat and vapour extraction; robots are marginal. So in brownfields ML is a sourcing edge, not
the engine; the engine is capital, powered-land scarcity and execution speed. The one corner of the
record that is illegible, pre-database industrial parcels readable only from Sanborn fire-insurance maps
and old aerials, does not help either: knowing a parcel is dirty is a reason to pay less, not a way to buy
it cheaper, and the infrastructure that makes it valuable is visible in any GIS layer.

**What I would back.** For the application: Terranox's own thesis, because it is the only public-dataset
play that passed every test, and eight hunts of looking for a second one are themselves evidence for how
rare the property is. If a second company idea is wanted: a two-week test of rail corridor title, the
only untested candidate with all four conditions, before any more brownfield work. Brownfields only as
a developer with an execution moat, and only after the ten-call test on the powered-land premium says
there is a multiple to earn.

## The decision for Dhruv (updated 17 Oct after the cross-hunt verdict)

1. **Build the application around Terranox and what it already proves.** Eight hunts, three real-data
   backtests and the California feasibility study all say the "public data only ML can read, outcome
   summarised nowhere" moat lives in geology. (Recommended.)
2. **If a second company idea is wanted: a two-week test of rail corridor title** from scanned ICC
   valuation maps, deed books and STB abandonment dockets, the only untested candidate with the full
   property. Expect a data-access fight first.
3. **Brownfields as a developer, not an ML company**, and only after the ten-call test on the
   powered-land premium (powered-land brokers, data-centre site selectors, a utility's interconnection
   queue) says a closed industrial parcel with a live substation earns a multiple. The California
   evidence: sourcing edge real, built-out set low hundreds, no discount, closure adds 5-7%, cleanup
   cost dwarfs the uplift on gas stations, industrial cost in no public record.

Earlier decision list (written before round 4): take Lineage to its kill test; accept the moat is
geological; or drop the claim requirement and rank on execution moats.

Search budget used: about 360 web searches across three rounds. Government data hosts (fda.gov, sbir.gov,
eia.gov, NRC, EMA) were blocked from this environment; datasets were checked against documentation, and
both proofs ran on GitHub mirrors.
