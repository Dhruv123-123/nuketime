## Verdict up front
The best variant I found is a preservation-only species conservation bank on land the company owns outright, in California. It fixes two of the old killers: almost no physical work, and no exposure to Sackett. It does not fix the step-up, and demand stays the hidden variable. Even with the relaxed C3 it remains weak, at about 10/25.

## Frame of reference
The rung is buying grazing or farm land outright (fee simple) where a listed species lives (vernal pool shrimp, California tiger salamander, Swainson's hawk, giant garter snake). The company preserves it, gets a USFWS/CDFW bank enabling instrument, and then sells ESA/CESA credits or the whole entitled bank.

This fixes two old killers:
- **Physical step:** preservation needs no earthwork. At Van Vleck, preservation credits release on how much of the endowment is funded, not on growing-season performance: 15% at establishment, then 25%, 15% and 15% at 15%, 40% and 70% funded, and the rest at full funding. The endowment needed is $765 per credit (https://www.conservationfund.org/wp-content/uploads/2023/08/Van_Vleck_Mitigation_Bank.pdf).
- **Sackett:** species credits are under ESA/CESA, not the Clean Water Act, so the 2023 ruling does not shrink demand.

What it does not fix: the work is not 80% discovery. Most of the value is still in selling credits over a decade into local permit demand, plus the capital tied up in the endowment.

## Step-up ratio
**Unproven land:**
- A San Benito County, CA horse ranch was bought for $1,400/acre in 2014.
- Santa Clara range land had a book ("Yellow Book") value of $4,000/acre.
- Thurston County, WA: The Conservation Fund offered $5,300/acre.

All three are from the EASI landowner deck (https://www.easillc.com/wordpress/wp-content/uploads/2025/02/2024-Real-Estate-Landowner-Deck_short_v-1.3.pdf).

**Realised once proven (same source):**
- San Benito: an energy company paid $4,400/acre for the mitigation land, 3x market. The same credits from a local bank would have cost about $21.7k/acre, about 15x.
- Santa Clara: sold to POST at $11,700/acre, about 2.9x.
- Vancouver, WA: about $97k/acre gross over 15 years.
- Credit prices for species run from $1,505 to $205,055 per credit in 2015 dollars (https://link.springer.com/article/10.1007/s10531-019-01747-2). Sonoma CTS credits run "as high as $200,000" (https://www.biologicaldiversity.org/news/media-archive/a2016/herp_pressdemo_6.21.16.pdf). Most banks issue about 1 credit per acre.

**Net result:**
- About 3x when the land itself is sold.
- About 10-25x gross on credits, before endowment, holding costs and a 17.5-18% discount rate (EASI's own rate).
- Only 15% releases at approval. Nothing reaches 10^3.

**Transactions:**
- USFWS approved 135 banks by Dec 2015 (https://www.doi.gov/sites/default/files/uploads/cb_sponsors_and_managers_survey_report_final_092716.pdf). The Springer study counts 155 by Sep 2018, so roughly 7 new banks a year.
- Whole-bank sales are rare. EIP's Appalachia portfolio drew 6-12 bids and sold for less than its $82.6M projected net revenue (https://ecosystempartners.com/eip-sale-points-to-deeper-institutional-market-for-mitigation-bank/).

## Hit rate and proving capex, today and with ML
**Approval time:** planning averages 13.6 months (median 12) and final approval 18.6 months (median 14.5), so about 2.7 years in total (DOI survey).

**Upfront cost:** about $1M, mostly the endowment (https://bren.ucsb.edu/media/1441).

**Approval rarely fails.** The weak point is sales: sponsors name weak credit demand as a top obstacle, and rate demand "weak" in USFWS Regions 1 and 2 (DOI survey).

**Hit-rate definition:** under the relaxed C3, I define a "hit" as a bank that sells out within 7 years. My estimate of the base rate is 30-50%.

**Where ML could help:** choosing parcels where future impacts on a species are concentrated, read from CEQA project pipelines. That could plausibly lift sell-through 1.3-1.8x (estimate, untested). The proving step is expensive, so C3 is worth about 3.

## Data source
- **CEQAnet** (https://ceqanet.lci.ca.gov): tens of thousands of notices, environmental impact reports and mitigated negative declarations. Their biology appendices are unstructured PDFs that state required mitigation ratios, species and locations. That makes them a forward demand signal that nobody aggregates.
- **Credit prices are not public.** They are negotiated, RIBITS and HabitatCAN ledgers show no prices, and sponsors say "contact the Sponsor" (https://www.habitatcan.org/local-resources/Hazel-Mitigation-Bank/69127/). Scattered staff reports carry the price points.
- **Outcome summary:** whether a bank was approved, and how many credits it has sold, is legible in RIBITS. Future demand by service area is not summarised anywhere.
- **Supply side is legible:** CNDDB occurrences, SSURGO and the CDFW approved-bank list (https://wildlife.ca.gov/conservation/planning/banking/approved-banks).

## How the right is bought
- **Seller and price:** bilateral fee-simple purchase from ranch owners at range or ag value ($1.4-5.3k/acre, EASI deck).
- **What the company keeps:** owning outright means it keeps 100% of the uplift. A promotion agreement would split it.
- **Legal mechanics:** a conservation easement plus the enabling instrument. The prospectus fee is $10k, with a 30-day completeness review (https://californiaglobe.com/articles/conservation-banks/).
- **Owners can increasingly read the data.** EASI sells eco-asset valuations directly to landowners and targets holdings of 500-20,000 acres, so the information discount is closing.

## Capitalised buyer
- Developers, Caltrans, utilities and energy companies buy credits as they need them.
- Funds buy entitled banks: EIP ($1.2B AUM, Fund V $400M), plus a 50/50 mix of financial and strategic bidders on the Appalachia portfolio (EIP article).
- They pay for banks with performance already de-risked, at a discount to projected revenue. They do not pay a premium at the moment of approval.

## Integration ladder above
1. Single bank.
2. Portfolio of banks.
3. Full-delivery and in-lieu-fee programs.
4. Regional habitat conservation plan administrator.
5. Entitlement services for developers.

This tops out around a $1-5B category (estimate). It does not lead to the whole value chain.

## Who else does this
- Sponsors: Westervelt Ecological Services, RES, Wildlands, EIP and The Conservation Fund.
- EASI: GIS-based eco-asset valuation.
- CEC: a GIS tool for choosing bank sites (https://www.cecinc.com/project/gis-based-mitigation-banking-site-selection-tool/).
- Aarden AI: land underwriting, not banks.

None of them, as far as I found, forecasts demand from CEQA filings.

## Smallest feasibility test (2 weeks)
1. Use an LLM to extract species-mitigation requirements (species, acres, ratio, location) from Sacramento, Placer and Sonoma CEQA environmental impact reports and mitigated negative declarations, 2012-2018.
2. Aggregate the results by bank service area.
3. Check against RIBITS ledgers whether this predicts 2018-2025 credit sell-through better than a legible baseline (population growth plus existing credit supply).
4. In parallel, collect 20 credit prices from staff reports.

**Kill conditions:**
- The top quintile of service areas sells through less than 1.5x faster than the baseline.
- Median credit price divided by land price comes out below 10x.

## Scores (relaxed rubric)
| Criterion | Score | Reason |
|---|---|---|
| C1 Frame | 2 | Preservation makes the physical step trivial, but demand and endowment carry the risk, and buyers pay after de-risking. |
| C2 Step-up | 2 | About 3x on land sold, 10-25x gross on credits. |
| C3 Hit-rate lever | 3 | Proving is expensive (about 2.7 years, about $1M); the ML lift on sell-through is plausibly about 1.3-1.8x (estimate). |
| C4 Data + right | 2 | CEQA and price data are illegible, but the supply side is legible and EASI is educating owners. |
| C5 Ladder | 1 | The chain above is small. |
| **Total** | **10/25** | Still refuted. |

The hard killer is C2. No variant of mitigation banking I found produces a step-up of 100x or more.