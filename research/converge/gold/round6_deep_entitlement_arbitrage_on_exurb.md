## Entitlement arbitrage on exurban residential land: feasibility deep-dive

*Search note: the shared WebSearch budget (200 per turn) was already used up, so no new searches ran. Figures come from direct fetches of the finalist's sources, Forestar's investor page and Shovels' blog. A number with no source is marked as an estimate.*

### Frame of reference
The rung is: option a farm parcel on the Sun Belt fringe, take it through annexation, rezoning or a preliminary plat with utility will-serve letters, then sell the entitled acreage to a builder or land banker. The rung is discrete and sellable. But picking the parcel is only about 25-40% of the work (estimate). The rest is a 1-4 year campaign of engineering, traffic, drainage and environmental studies, staff negotiation, neighbour management and offsite utility commitments. acres.com says entitlement "is not passive" and needs coordination with several agencies (https://www.acres.com/blog/what-is-land-investing). That is the same shape as the geothermal-in-coal-mines counter-example: doing the proving step is harder than finding the site.

### Step-up ratio
- **Unproven price:** $10-30k/acre for raw fringe land (the candidate's estimate; no hard source).
- **Proven price:** entitled land sells for 2-4x equivalent raw land (https://www.acres.com/blog/what-is-land-investing). The candidate's 3-10x is optimistic.
- **The spread is narrowing.** Since 2019, raw land per acre is up 86.5% against 53.3% for build-ready lots. Year over year, raw land fell 2.4% and build-ready fell 1.1% (Realtor.com via https://themortgagepoint.com/?p=22526). Sellers are already pricing in hope value.
- **Transactions/yr:**
  - 426,986 land listings in Q1 2026, median $62,365/acre across all categories (same source).
  - Forestar sold 14,240 lots in FY2025 and controls 91,700 (https://investor.forestar.com/).
  - Millrose manages about 143k homesites with $8.7B invested capital (https://finance.yahoo.com/markets/stocks/articles/millrose-mrp-q1-2026-earnings-210651199.html).
  - "$50B+ of US builder land spend a year" is unverified (estimate).
- **Return on total capital:** about 3-5x on cash at risk for winners. After failed entitlements and carry, about 2-3x blended (estimate).

### Hit rate and proving capex, today and with ML
- **Cost per attempt:** about $150k-$2M and 1-4 years (candidate estimate, consistent with acres.com's "years of regulatory risk"). The expensive-proving leg is met.
- **Base hit rate:** 40-65% from parcel pick to approval (estimate, no hard source). Cases that reach a hearing are mostly approved, because staff negotiate them first.
- **Existing ML evidence:** a Frederick County MD logit study found rezonings largely follow the ordinance and the staff recommendation (https://ageconsearch.umn.edu/record/159252, returned 403 on fetch, so this is the finalist's summary).
- **With ML:** about 1.2-1.5x better cost per entitled parcel, mostly from dropping doomed options before deposits go hard. 2x would need a signal beyond the future land-use map and sewer service area, which is not shown (estimate).

### Data source
- **Datasets:** Legistar/Granicus agendas, minutes and staff reports; YouTube meeting video; CIP, sewer and water master-plan PDFs; annexation agreements; comp-plan future land-use maps; county GIS parcel, assessor and deed records. All are public and free.
- **Legibility:** partly illegible (scanned PDFs, video). But staff reports carry a legible approve/deny recommendation, and future land-use maps and sewer boundaries are often already GIS layers.
- **Extraction is already commercial.** Shovels bought ReZone in January 2026. Its Decisions API covers 600+ cities and about 200,000 final decisions, and names "home builders and real estate investors tracking rezonings" as a use case. It plans proposed/discussed/approved/postponed status fields (https://www.shovels.ai/blog/decisions-api-launch/; https://www.shovels.ai/blog/shovels-acquires-rezone/). The outcome is fast becoming a legible field.

### How the right is bought
- **From whom:** farm families, estates and local brokers.
- **Mechanics:** a purchase option or contingent contract. Typically 1-5% of price as a deposit, going hard at milestones, with closing at entitlement or simultaneous with resale (estimate).
- **Uplift kept:** the company keeps the spread minus study spend, carry and option fees. That is perhaps 40-60% of gross uplift on winners (estimate).
- **The problem:** fringe sellers are courted by builder land teams and land bankers, so they ask hope-value prices. Sun Belt vacant land per acre more than doubled in the two years to Q2 2022 (WSJ/Land.com, https://www.business.rutgers.edu/sites/default/files/documents/running-short-land-housing-wsj-morris-davis-9-26-2022.pdf, per the verifier; the PDF was unreadable on my fetch). Truly uninformed sellers exist only at the margin.

### Capitalised buyer
The buyer is strong and active:
- **Builders:** D.R. Horton (through Forestar), Lennar, Pulte, NVR and Toll.
- **Land bankers:** Millrose earned about $185M of option fees in Q1 2026, has 17 counterparties and a 10.7% yield on non-Lennar agreements (Yahoo source above).
- **Caveats:** builders report 200-500 bps of margin compression and Texas has excess inventory (same source). Demand for entitled land is cyclical right now.

### Integration ladder above
Entitlement leads to horizontal development and finished lots (Forestar's model), then build-for-rent or vertical homebuilding, then master-planned community operator. The chain is very large, but every rung is crowded with capitalised incumbents.

### Who else does this
- Local entitlement developers and land brokers.
- Forestar (D.R. Horton), Millrose and Varde.
- Builder in-house land teams.
- Data vendors: Shovels/ReZone, Zoneomics and Bassett.ai (https://www.zoneomics.com/, per the verifier).

### Smallest feasibility test (2 weeks)
**Is the ML signal already priced into land?**
1. Pick one fast-growth Sun Belt county with Legistar coverage, such as one exurban Texas or Carolina county.
2. Pull 5 years of rezoning decisions (the Shovels Decisions API free tier, plus scraped staff reports and CIP/sewer PDFs).
3. Train an approval model on features available at the time of application.
4. Benchmark it against a two-feature baseline: staff recommendation plus consistency with the future land-use map.
5. Join model scores to assessor and deed sale prices per acre for parcels sold before their rezoning.

**Kill criteria:**
- the model's AUC beats the baseline by less than 0.05; or
- high-score parcels did not sell at least 30% below comparable hope-value prices.

### Verdict
The buyer, ladder and prize are real. But the rung is an execution-heavy entitlement campaign in an informed land market. The step-up is about 2-4x, and the rezoning outcome is being commoditised into a legible field by Shovels. ML-led discovery is not 80% of the rung, and the land cannot be bought at a deep discount to its proven value.

| Criterion | Score | Reason |
|---|---|---|
| C1 Frame | 2 | Sellable rung, but the campaign dominates the work |
| C2 Value capture | 2.5 | About 2-3x blended on total capital, multi-$B prize, thin spread |
| C3 Hit-rate lever | 3 | Proving is expensive; ML lever about 1.2-1.5x |
| C4 Data + right | 1.5 | Outcome increasingly legible; sellers informed |
| C5 Ladder | 4 | Long, real ladder, but crowded |

**Total: 13/25. Not a Terranox-shaped frame. Do not pursue unless the 2-week pricing test shows a structural discount.**