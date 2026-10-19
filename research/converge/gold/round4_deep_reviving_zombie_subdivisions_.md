# Zombie subdivisions (lapsed or antiquated plats): feasibility deep-dive

*Note: the shared WebSearch budget ran out before this agent made its first search. Everything below comes from direct WebFetch reads of primary sources (SEC 10-Ks, the Florida Senate report) plus the finalist's cited pages. Unsourced figures are marked as estimates.*

## Frame of reference
The rung is a stalled or antiquated plat turned into entitled, serviceable land. Proving it is mostly legal and records work: a vested-rights determination or replat, a development agreement, and will-serve letters. The trouble is that the buyers who pay real money buy *finished* lots. Forestar, D.R. Horton's lot arm, spent **$595.3M on land acquisition and about $1.1B on land development** in FY2025 ([Forestar 10-K](https://www.sec.gov/Archives/edgar/data/1406587/000162828025053125/for-20250930.htm)). So physical horizontal work (roads, sewer, grading) is about two thirds of the capital in the rung builders pay for. That is the geothermal counter-example's failure mode. A rung where discovery is 80%+ of the work does exist (sell entitled, unimproved land), but its buyers pay cost plus carry.

## Step-up ratio
- **Unproven:** a stalled-plat lot-equivalent at about $5-15k (estimate, from the pitch). Raw land is not priced near zero: the national median is $62,365/acre, and raw land is up 86.5% since 2019 against 53.3% for build-ready land ([MortgagePoint/Realtor.com](https://themortgagepoint.com/2026/04/23/prices-for-raw-land-has-surged-a-whopping-87-since-2019/)).
- **Entitled, mostly unimproved:** about $34k per homesite. Millrose bought Rausch's roughly 25,000 homesites for about $859M ([Millrose 10-K](https://www.sec.gov/Archives/edgar/data/2017206/000201720626000002/ck0002017206-20251231.htm)).
- **Finished:** $108,400 average Forestar lot price ([Forestar 10-K](https://www.sec.gov/Archives/edgar/data/1406587/000162828025053125/for-20250930.htm)). Millrose implies about $113k per homesite ($16.1B over 142,139 homesites).
- A same-county raw-versus-developed example gives 6x ($3k vs $18k/acre), and utility extension alone costs "tens of thousands to over $100,000" ([Acres.com](https://www.acres.com/blog/raw-land-vs-developed-land)).
- **Net for the proving rung: about 2-5x.** Raw to finished is about 10x, but only after you pay for the development.
- **Transactions per year:** Forestar sold 14,240 lots in FY2025. Total US builder lot takedown is about 1M a year (estimate). The zombie or uncertain-vesting slice is a small fraction of that (estimate).

## Hit rate and proving capex today and with ML
- **Capex:** about $100k-1M and 12-36 months per vested-rights determination or replat (estimate, from the pitch). Forestar says municipalities "were frequently delayed in granting the proper approvals" and have broad discretion over conditions.
- **Base hit rate:** 50-70% (estimate, unverified). Weakened by *Dawe v. Scottsdale*, which holds that a recorded plat alone vests no rights ([case brief](https://www.lexplug.com/casebrief/dawe_v_city_of_scottsdale_67cb06bf99e747a38d58393b)).
- **With ML:** screening plats for partly built infrastructure, released bonds, live development agreements and utility capacity could avoid dead options. Plausible gain is about 1.2-1.5x on cost per proven asset (estimate). It is capped because council votes and holdout owners cannot be predicted from documents.

## Data source
- **Datasets:** county recorder plat books, recorded development agreements, planning and council minutes, improvement-bond release records, tax-delinquency rolls and aerial imagery, in AZ (Maricopa, Pinal), FL (Lee, Charlotte, Marion), NV, ID and TX.
- **Why it is illegible:** the records are scanned and spread across agencies.
- **Is the outcome already summarised?** Partly. Zonda and John Burns sell subdivision lot-pipeline status to builders (domain knowledge, not fetched). Plat dates and zoning sit in county GIS fields. The Florida Senate report says the 2.1M lots in about 2,600 antiquated subdivisions are undeveloped because of "lack of infrastructure" and fragmented absentee ownership, which is a known assembly problem rather than an information gap ([FL Senate report](https://spikowski.com/documents-LehighAcres/FloridaSenateReportOnAntiquatedSubdivisions.pdf)).

## How the right is bought
- **Single-owner stalled tracts:** a non-recourse purchase option with earnest money, the same structure Forestar uses ([10-K](https://www.sec.gov/Archives/edgar/data/1406587/000162828025053125/for-20250930.htm)).
- **Antiquated subdivisions:** buy hundreds of tiny lots from absentee owners. Florida proposals required 60% fee-title ownership before a replat, and owners have "little incentive to sell" ([FL Senate](https://spikowski.com/documents-LehighAcres/FloridaSenateReportOnAntiquatedSubdivisions.pdf)).
- **Uplift kept:** if the company sells entitled land at the about-$34k/homesite level, it keeps the entitlement gain, perhaps $15-25k per lot (estimate). Forestar's whole buy-entitle-develop-sell chain earns about a 21.9% gross margin ($1,662.4M revenue against $1,298.9M cost of sales).

## Capitalised buyer
Lennar, D.R. Horton and Pulte buy through option and takedown programs, and land bankers such as Millrose and Varde fund the land. Millrose's takedown price is its own acquisition cost plus the development budget, at an 8.5-11% yield, with no independent appraisals ([Millrose 10-K](https://www.sec.gov/Archives/edgar/data/2017206/000201720626000002/ck0002017206-20251231.htm)). The buyers are real, but neither pays a jackpot.

## Integration ladder above
Entitlement, then horizontal development (Forestar-style), then land banking (Millrose), then vertical homebuilding and master-planned communities, then mortgage and title. These are very large markets, but capital-heavy and cyclical.

## Who else does this
- Forestar, majority-owned by D.R. Horton
- Builder land teams and Land Advisors Organization
- Land bankers: Millrose, Varde, JEN Partners
- Florida paper-lot mass-mail "land flippers"
- Post-2008 distressed funds, which absorbed the REO-desk zombie inventory from 2010 to 2015 (domain knowledge)

## Smallest feasibility test (2 weeks)
1. In Pinal County, AZ, pull 200 plats recorded 2004-2009 that have fewer than 20% of lots improved. Use the assessor parcel roll to find vacant lots.
2. Hand-label each plat's current status from the planning portal and bond-release records.
3. Compare recent recorded sale prices of vacant lots in plats labelled "revivable" with plats labelled "dead", and with entitled-land comps.
4. Call five land brokers to ask whether they already track these plats.

**Kill if:** the revivable-versus-dead price gap is under 2x, or if more than 80% of the status is already in GIS or broker knowledge.

## Verdict (relaxed C3)
- **C1 = 1.** The buyers pay cost plus carry, and the high-value rung is mostly physical construction.
- **C2 = 2.** About 2-5x for entitlement alone.
- **C3 = 3.** Proving is expensive, but ML gains are about 1.2-1.5x because local politics and holdouts cap them.
- **C4 = 2.** The data is illegible but partly summarised and sold. Rights are buyable, but antiquated lots need slow, holdout-prone assembly.
- **C5 = 4.** A real, very large homebuilding ladder.

**Total: 12/25. Not excluded, but weak.** The step-up that matters comes from horizontal development (about $65k+ of the $108k Forestar lot, estimate based on its 2:1 development-to-acquisition spend), not from discovery.