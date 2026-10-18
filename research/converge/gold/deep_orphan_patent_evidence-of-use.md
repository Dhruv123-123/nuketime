## Orphan Patent Evidence-of-Use: feasibility memo

**Search limit:** the shared WebSearch budget for this turn was already used up, so nothing here comes from a fresh search. Figures come from three things: the 2025 Richardson Oliver (RO) Patent Market Report PDF, which I downloaded and read in full; the USPTO PTAB FY26 Q3 PDF, which I parsed; and first-party pages fetched directly. Anything else is marked as an estimate.

### Frame of reference
The rung is: own an orphan US patent that nobody has read, prove it reads on a product that is shipping now, and sell it as an asset with evidence-of-use (EoU) attached. Inside that rung, discovery is about 85% of the work (estimate): picking the right patent out of thousands and mapping its claims onto FCC internal photos, teardowns or driver code. The physical step is desk work, plus the occasional teardown at roughly $5-20k (estimate). This frame does exist. Its weakness is that the output is an opinion, not a proof. The uncertain, costly step of licensing or litigation still sits with the buyer. This is the geothermal problem moved up one rung.

### Step-up ratio
- **Unproven price:** about $0 for lapse-bound patents. The owner simply pays nothing and lets the patent die. The only cost is the maintenance fee: $8,280 large entity or $3,312 small entity at 11.5 years, plus a $540 grace-period surcharge ([USPTO fees](https://www.uspto.gov/learning-and-resources/fees-and-payment/uspto-fee-schedule)). Estate and assignment-for-benefit-of-creditors (ABC) lots go for about $2-30k per asset (estimate, not verified).
- **Proven price:** the median asking price of *sold* assets was $63k in 2022, $33k in 2023 and $95k in 2024. Per US-issued patent it was $83k, $75k and $141k. Closing discounts run from 0% to 75% or more ([RO 2025](https://www.richardsonoliver.com/publications/the-2025-richardson-oliver-patent-market-report), PDF Table 3).
- **Premium from EoU:** +32% to +108% across five years, which is a 1.3-2.1x step-up from the proving step alone (same source).
- **Overall step-up:** about 3-30x from a paid estate lot. It only reaches about 10-100x when you start from a near-free lapse-bound patent, and those are adversely selected (see below). Terranox's step-up is 10^4.
- **Transactions per year:** the whole brokered market was **$158M** in 2024, flat with 2022 and 2023. 1,611 packages were listed, the median package held 2 assets, brokers handled 87% of sales, and about 30% of packages eventually sell (RO 2025).

### Hit rate and proving capex, today and with ML
- **Hit rate today:** about 1-5% of random orphan patents read on a live product with enough term left and damages worth chasing (estimate).
- **Cost per hit today:** a manual chart costs about $3-15k (estimate), so each hit costs roughly $100k-$1M.
- **With ML:** ML triage could cut that cost 5-20x. That would be a real lever, but it is not proprietary:
  - Patlytics advertises "Crawl for evidence of use across public sources" and "Citation-backed claim charts". It reports savings of "$1,000–$5,000 minimum" per detection report, has a $40M Series B, and lists Quinn Emanuel and Panasonic IP among its customers ([patlytics.ai](https://www.patlytics.ai/)).
  - RO says sellers can now produce "high-grade EOUs at relatively low costs" (RO 2025).
- **PTAB risk is lower than the finalist assumed:**
  - Across 1,096 petitions, 50% were denied institution and only 18% ended with all claims unpatentable.
  - 47% of *instituted* claims were found unpatentable ([USPTO FY26Q3](https://www.uspto.gov/sites/default/files/documents/TrialsOutcomeRoundupFY26Q3.pdf)).

### Data source
- **Datasets:** USPTO full text, assignments, maintenance-fee events and PTAB data (public bulk data). FCC Equipment Authorization internal photos ([fcc.gov/oet/ea/fccid](https://www.fcc.gov/oet/ea/fccid)). PACER section 363 sale schedules. Linux driver source, IEDM papers and die-shot archives.
- **Why it is illegible:** the evidence is spread across images, code and scanned schedules.
- **Is the outcome summarised anywhere?** Whether a patent reads on a product is not written in any legible field, so this part passes. The proxies are, though: citations, family size, maintenance payments and litigation history. Commercial patent-value scores (PatentSight, Ocean Tomo, RPX) already rank on them (from memory). TechInsights already covers the products of large companies (from memory).

### How the right is bought
- **Legal mechanics:** patents can be assigned outright (35 USC 261), and a section 363 sale passes clean title. The sources are trustees, ABC assignees and owners about to let a patent lapse.
- **Competition for estates:** any estate with visible value is brokered competitively. Nortel went from a $900M stalking-horse bid to $4.5B (from memory). That leaves only the long tail cheap, and in the long tail the discount and the hit rate move in opposite directions.
- **Limits on lapse-bound patents:** you must buy before the 6-month grace period ends. Revival under 37 CFR 1.378 requires an "unintentional" delay, and intervening rights under 35 USC 41(c) protect anyone who started using the invention during the lapse.
- **Limits on damages:** marking (35 USC 287) and the six-year look-back (35 USC 286) cut what an orphan patent can recover.

### Capitalised buyer
- **Who buys:** operating companies bought 37-90% of sold assets in 2020-24, and NPEs bought 13-50%. NPEs show only 2% so far in 2024, likely understated because of recording lag. Defensive aggregators are "increasingly selective" (RO 2025).
- **How buyers behave:** RO calls the market "advantageous to buyers", with "rarely competing buyers".
- **Why this is not a mine developer:** buyers cannot develop the asset at a known cost and payoff, so they discount the price.

### Integration ladder above
1. Buy and chart patents.
2. Sell them to aggregators.
3. License them directly.
4. Run your own assertion campaigns.
5. Fund litigation, yours and others'.
6. Become an IP fund or defensive pool.

The ceiling is a $1-5B outcome of the Acacia, Intellectual Ventures or RPX kind (from memory). Patent monetisation tops out at a few billion dollars a year, and anti-NPE policy creates friction. There is no trillion-dollar path.

### Who else does this
- **Funded tooling for the proving step:** Patlytics, plus IPRally and Amplified (from memory).
- **People who market estates:** Hilco Streambank, Tangible IP and ICAP Ocean Tomo (from memory).
- **Buyers of exactly this inventory:** Dominion Harbor, IP Edge, Atlantic IP, Acacia, Sisvel, Burford and Fortress.

### Smallest feasibility test (2 weeks)
1. Pull every US patent from the USPTO maintenance-fee events data that has entered the grace period of its 11.5-year fee and belongs to a dissolved or bankrupt assignee. That should be several hundred patents (estimate).
2. Triage them with an off-the-shelf EoU tool and keep the top 10.
3. Have an attorney spot-check those 10.
4. Shop them blind to 5 brokers or buyers for indicative bids.

**Pass:** at least 2 of the 10 draw bids of $75k or more each, and the owners agree to assign for under $5k. **Fail:** bids fall in the 1.3-2.1x EoU band, or nobody bids at all. That would show the asset gets its price from the buyer's litigation budget, not from discovery.

### Verdict
**Does not pass the rubric. Revised total: about 10-11 out of 25.** The 80%+ discovery frame is real and the right can be bought. But the proving step adds only a 1.3-2.1x premium according to RO's measured data, the market totals $158M a year with rarely competing buyers, and the ML lever is already sold off the shelf. The ladder also caps at a few billion dollars. At best this is a cash-flow side business that buys lapse-bound patents for the cost of the maintenance fee; it is not a Terranox analogue. The test above settles that within 2 weeks.

Working files: /tmp/claude-0/-home-user-nuketime/2305f78e-f084-5801-ab25-e340938a9d29/scratchpad/ro/r.txt (the RO 2025 report as text) and /tmp/claude-0/-home-user-nuketime/2305f78e-f084-5801-ab25-e340938a9d29/scratchpad/ptab/p.pdf (the USPTO PTAB FY26 Q3 report).