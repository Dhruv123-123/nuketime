# Red team: ML-sited ecological mitigation bank developer

Written 15 October 2026. Budget: 15 WebSearch calls (all 15 used), plus WebFetch on the pages they returned.
Target: the candidate that lane_land (#1) and lane_earth (#1) both reached independently, each scoring it 6/10.
The thesis is that RIBITS ledgers, permit notices and project pipelines can forecast which service areas will
run short. The company would then option land, get a bank approved, and own the credit ledger.

## Verdict: DEAD as a Terranox-class idea. A narrowed, capped variant survives, but it fails the brief.

The thesis fails three of the brief's tests:
- It is not "unattackable".
- The ML edge is thin, because forecasting is not the binding constraint.
- The demand base is being legislated away during the very 4-6 year window the forecast is supposed to exploit.

What remains is a good regional real-asset business: a roll-up worth about $1-3B, with a ceiling set by a
regulated market that is shrinking. That is the "capped like a regional developer" outcome.

---

## 1. Market size: the $8B/yr headline is inflated

- **EASI (June 2026)** is the source both lanes cited.
  - Its "$500B" is the *authorized* value of credits. It counts released, unreleased and already-sold credits:
    about $415B released, $285B transacted and $130B still held by bankers.
  - EASI built that figure by multiplying RIBITS credit counts by its own average state prices.
  - The "$8B/yr" is that $285B divided by 35 years. It is not a measured annual flow.
  - EASI is a broker and consultant with a reason to talk the market up. Its units are inconsistent ("per acre"
    vs "per credit"), and in the same piece it cites "$12B annual transactions" (2018) without reconciling the two.
  - Source: https://www.easillc.com/2026/06/22/2026-review-u-s-mitigation-credit-marketplace-nears-500-billion/
- **ERBA-funded 2023 study:** more than 2,500 banks earned about **$3.5B in 2019**
  (https://thelensnola.org/2025/04/14/wetlands-protections-built-an-industry-for-mitigation-banking-rollbacks-could-erode-it/).
  - Older Forest Trends/ELI estimates of all US compensatory mitigation (banks plus ILF plus PRM) are in the same
    $3-4B/yr range. I recall this from memory and could not re-verify it within budget.
  - **Working number: about $2.5-4B/yr of bank credit sales**, which is roughly half the EASI headline.
- **Prices are real and highly local.**
  - Wetland credits run from about $14k (SC) and $50k (TN) to $134k (NC), $263k (VA), $450-550k (FL Gulf),
    $675k (NJ) and $0.75-1.1M (GA).
  - VA stream credits are about $550 each.
  - That dispersion is the opportunity, and it is also proof that the market is a collection of hundreds of
    small local markets.
- **Sector mix:** no source gives a national split.
  - DOTs are the largest single buyers. EASI notes about $248M of SC DOT contract commitments.
  - Data centres are named as *the* current driver in the May 2026 State-of-Market webinar (wetlands.com).
    It says data centres have strained wetland supply in VA's Middle James and Roanoke, and that Potomac stream
    supply is low. Michigan and Ohio Google sites add more anecdotes.
  - Data-centre demand is locally decisive but national volume is unverified. My estimate is that it is a
    single-digit percentage of national credit dollars, concentrated in about 10-20 service areas.

## 2. Regulation: the demand base is being cut, and the cut lands during the forecast window

- **Sackett (2023)** removed isolated and non-abutting wetlands from federal jurisdiction.
- **Nov 2025 proposed WOTUS rule:** the agencies' own estimate is that jurisdictional adjacent wetlands would be
  only **about 19% of NWI-mapped wetlands**. It would also drop many intermittent streams.
  - The cut relative to current practice is smaller than that figure suggests, because many of those wetlands
    were already non-jurisdictional after Sackett.
  - Source: https://esassoc.com/news-and-ideas/2025/12/proposed-update-to-definition-of-wotus-will-federally-regulated-wetlands-continue-to-shrink/
- **Sept 9, 2026 Supplemental Proposed Rule** is narrower still:
  - "Relatively permanent" would mean **perennial**: water present every day, with no non-anomalous interruption
    over 30 days.
  - A wetland would need a perennial surface connection, and only the part "indistinguishable" from the water
    would be jurisdictional.
  - The agencies are asking whether to drop "adjacent" and "abutting" altogether.
  - Comments closed on Oct 9, 2026. **It is not final as of mid-Oct 2026**, and litigation is expected.
  - Source: https://www.bracewell.com/resources/federal-agencies-propose-additional-revisions-to-the-definition-of-waters-of-the-united-states/
  - **Stream credits are hit too.** Intermittent headwater streams lose jurisdiction, and they generate much
    of the stream-credit demand in Appalachia and the Southeast. That undercuts lane_earth's "favour streams"
    hedge.
- **States are rolling back.**
  - Tennessee's bill would deregulate about 80% of isolated wetlands. A bank manager testified it would cut
    demand by about 80%.
  - NC, IN and KY have also loosened their rules since Sackett.
  - The offset: GA, where isolated wetlands are unregulated, sees $0.75-1.1M credits on the remaining
    jurisdictional supply. Scarcity raises prices on a shrinking base.
- **Proposed changes to how mitigation is done (House Crawford amendment, 2025):**
  - It would direct the Army to "promote equivalency" among banks, in-lieu-fee programmes and
    permittee-responsible mitigation, which removes the 2008 rule's de facto preference for banks.
  - It would let credits be generated and sold **across multiple HUCs**, and encourage off-site and out-of-kind
    mitigation.
  - The State-of-Market deck also lists proposed revisions to the 2008 Mitigation Rule.
  - These changes attack the moat directly. Service-area exclusivity is the whole "claim" analogue, and
    multi-HUC service areas dilute it.
  - Source: https://amendments-rules.house.gov/amendments/Crawford%20-%20Compensatory%20Mitigation%20Amendment%20Language250717185437526.pdf
- **How much demand vanishes:** this cannot be pinned down until the rule is final, and any final rule will be
  litigated.
  - My estimate is a 30-60% cut in *federal* wetland/stream credit demand in states without their own
    programmes (TN-style), and little change in states with their own programmes (NJ, NY, PA, MD, VA state
    waters, FL, CA, MI, WI, MN).
  - The bigger problem is the *variance*. The 3-7 year forecast the model is meant to win on is dominated by a
    legal variable (rule text, court outcomes, state legislatures) that ML on RIBITS and permit pipelines
    cannot predict.

## 3. Prior art and crowding

- **Life on Marsh** is an early, pre-funding startup recruiting a "Data Scientist, AI & Remote Sensing" and a
  hydrology advisor (Notion job posts).
  - I could not render the pages, so I do not know its business model.
  - It is evidence that someone is already starting an ML mitigation/marsh company. Check it before going
    further.
- **Incumbents already do the "forecast", just without ML branding:**
  - RES (KKR, then Onex in 2022; the largest player) sells a "regional mitigation inventory analysis" to data-centre
    developers. It writes that "the regional mitigation bank is depleted" as a known pattern.
  - EASI runs a proprietary price database with more than 4,100 referents across states.
  - The wetlands.com State-of-Market webinars chart "Outstanding Proposed Projects by State" against supply by
    service area. That is the demand-versus-supply shortage map, published for free.
  - EIP (whose sale drew 6-12 bids), Westervelt, Wildlands and Restoration Systems are capitalised, multi-state
    developers with decades of IRT relationships.
- **Academic work already does it:** Theis and Poesch (2022, J. Nature Conservation) used 26 years of RIBITS
  data to project capacity bottlenecks by bank type.
  - Wetland banks are bottlenecked, and reserves are concentrated in few service areas.
  - Stream and species banks are projected to meet demand.
  - Source: https://poeschlab.ualberta.ca/2022/02/28/theis-s-and-m-s-poesch-2022-current-capacity-bottlenecks-and-future-projections-for-offsetting-habitat-loss-using-mitigation-and-conservation-banking-in-the-united-states-journal-for-nature-co/
- **The data is the same for everyone.** RIBITS is public by rule, so there is no Terranox-style asymmetry where
  one player reads opaque filings better than others. In hot markets (VA, GA, OH, TX), every banker already
  knows which service areas are short.
- **UK BNG:** both lanes conceded it is crowded (Environment Bank, Nattergal, Gaia, land-agent spinouts,
  about 200 registered sites). Small-site BNG rollback is also under discussion.

## 4. The binding constraint is approval, capital and land, not siting knowledge

- **The Corps' approval process is slow, and getting slower.**
  - Bank approvals take an average of **about 1,150-1,195 days in total**, and the total is rising by 18-27 days
    a year.
  - Federal processing alone averages 336 days, against a 225-day requirement.
  - The slowest quartile of districts takes more than 1,500 days. These include Norfolk, Savannah, Charleston,
    Jacksonville, Galveston and LA, which are many of the high-price markets.
  - Credit-release reviews average 92 days, against a 45-day target.
  - Source: https://policyinnovation.org/blog/mbi-timelines-2024-update
- **Land and cash flow are the next constraints.**
  - Add land control, construction and performance monitoring, and the first meaningful credit release comes
    4-6 years after the land option.
  - Each bank needs about $3-10M of land plus restoration capital before revenue.
  - Willing sellers of the right hydric parcels are limited.
- **An ML forecast does not compress any of that.** The returns go to whoever has IRT relationships, a template
  instrument, patient capital and the ability to carry inventory.
  - Those are incumbent strengths. RES and EIP are capitalised precisely for this.
  - A forecast that tells you where shortages will be in 5 years is useful but not exclusive. A rival can site a
    bank in the same HUC, and IRTs do approve multiple banks per service area.
- **Where ML helps:** parcel-level restoration-lift scoring (hydric soils, tile drainage, LiDAR, NWI) to cut
  cost per credit by perhaps 20-40%. That is an operating-margin edge, not a moat. Large incumbents can buy the
  same capability from GIS consultancies.

## 5. Ceiling

- **Market and revenue:** the market is about $2.5-4B/yr of bank credit sales, fragmented across about 2,500 banks
  and hundreds of service areas, and federally shrinking.
  - A 5-10% national share would be about $150-400M/yr of credit revenue. It is lumpy and depends on the
    release schedule.
- **Valuation:** real-asset and infrastructure multiples put that at about $1-3B of enterprise value after a
  decade or more of capital deployment. RES is the comparable (valuation undisclosed).
- **Path:** there is no credible route to much higher than that. Unlike a uranium discovery, a credit's value is
  capped by the cost of the permittee's alternatives (ILF, PRM, redesigning the project, or a state with no
  programme), and those alternatives are being made easier.
- **Conclusion:** this is capped like a regional developer or roll-up, and it fails brief criterion 4 in spirit,
  as well as the "unattackable" requirement.

## What would have to be true to revive it (the narrow variant)

1. Restrict it to **ESA conservation banks** (species credits are not affected by WOTUS) and to **states with
   their own wetland programmes**, plus data-centre corridors (VA Middle James/Roanoke, central OH, GA, IN).
2. Treat the ML forecast as input to a deal-sourcing machine that front-runs IRT approvals using templates. Sell
   forward credits to hyperscalers under offtake agreements (as Google's Ohio Dazzler purchase shows they will
   pay about $77k/credit). This turns the business into "mitigation-as-a-service for data centres", with
   offtake-backed financing.
3. Even so, the ceiling is about $1-2B, and RES is already marketing exactly this to data-centre developers.
   It does not clear the bar for this hunt.

## Searches used (15)

1. EASI 2026 review
2. WOTUS 2026 final
3. Life on Marsh
4. WOTUS finalized 2026
5. Forest Trends/ELI size
6. Sackett banker demand
7. 2025 WOTUS jurisdiction share
8. Demand-forecasting startups
9. RES data/GIS
10. AI bank startup 2026
11. MBI timelines
12. Data-centre credit shortage
13. Incumbent proprietary forecasting
14. RES valuation
15. 2008 Mitigation Rule changes

**Not fetched or not verified:**
- Life on Marsh pages (Notion needs JavaScript).
- The full Theis and Poesch paper.
- The original Forest Trends/ELI figures.
- RES and EIP financials.
- RIBITS itself.
