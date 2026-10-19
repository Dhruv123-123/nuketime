## Frame of reference
The company would buy an option over broadacre rural land on a growth front, get it rezoned, and sell it as englobo land to a master-planned community developer. Under the rubric this is a sellable rung and the buyer is real. The problem is the work mix. Choosing the parcel is about 20-30% of the effort (estimate). The rest is a planning proposal or scheme amendment: specialist studies, council and state advocacy, exhibition, panel hearings and negotiating contributions. That proving step is not cheap, short or hidden. It is political and procedural, which makes this look like the geothermal counter-example: carrying out the bespoke step is harder than finding the site.

## Step-up ratio
**Hard limit on this run:** the shared WebSearch budget was used up before this deep-dive started. All three searches I tried were rejected. The figures below come from direct fetches of known URLs and the finalist's own sources. Several fetches failed (NSW DPHI pages 404, Planning Panels Victoria and Stockland 403). Prices are mostly from 2018 and need a refresh.

| Item | Value | Source |
|---|---|---|
| Land likely to be added in the next Melbourne growth-boundary expansion (hope value) | AUD $125-250k/ha | Cushman & Wakefield, quoted in https://www.beefcentral.com/?p=151472 |
| Unplanned land inside the growth boundary (Beveridge, 600 ha, $220M, 2018) | ~$367k/ha | same |
| Zoned residential parcel (Gisborne, 75 ha, $61.1M) | ~$815k/ha | same |
| Development-land benchmark (Biggin & Scott, H1 2018) | $2M/ha | same |
| Austral, Western Sydney (41 ha, $100M guide, 2023, flexible commercial zoning, not residential) | ~$2.4M/ha | https://www.realcommercial.com.au/news/western-sydneys-largest-ever-land-parcel-includes-100m-guide |
| True farm value | ~$10-100k/ha | estimate |

- **Gross step-up for parcels a model would actually pick** (hope value to zoned): about 6-16x.
- **In Victoria:** Windfall Gains Tax applies at rezoning. It is 62.5% of uplift between $100k and $500k, and 50% of the whole uplift above $500k. The owner at rezoning pays, and it can be deferred to the next dutiable transaction (https://www.sro.vic.gov.au/understanding-windfall-gains-tax). That roughly halves the net gain.
- **In NSW:** the Housing and Productivity Contribution plus s7.11 local charges cost tens of thousands of dollars per lot (estimate; the DPHI page returned 404).
- **Net step-up:** about 2-6x after proving cost and carry (estimate). The 10³-10⁴ needed is not reached.
- **Transactions per year:** dozens of englobo deals across Melbourne, Sydney and SEQ (estimate, unverified).

## Hit rate and proving capex, today and with ML
- **Capex:** about AUD $0.5-3M and 2-6 years per proposal (estimate from the finalist's sources). NSW gateway deadlines are routinely extended (https://engagement.yourvoiceourcoast.com/sites/default/files/2021-09/background_information_-_gateway_determination_extensions.pdf).
- **Hit rate:** no published success rate found. 30-60% inside investigation areas is plausible (estimate). The register does publish "Made" and "Withdrawn" stages, so a base rate could be computed (https://www.planningportal.nsw.gov.au/ppr).
- **ML lift:** about 1.1-1.3x on cost per proven parcel (estimate). Which parcels get zoned first is set mostly by published servicing and sequencing plans and by lobbying, not by hidden signals in documents. The VPA publishes an interactive precinct status map and a 10-year greenfields plan (https://www.vpa.vic.gov.au/).

## Data source
- **Datasets:**
  - NSW Planning Proposal register (stages from Under Assessment through Made or Withdrawn)
  - Planning Panels Victoria reports
  - council business papers
  - VPA status map
  - ShapingSEQ investigation areas
  - water-authority growth servicing plans
  - flood studies
  - the Government Gazette
- **Access:** all public.
- **What is illegible:** gateway conditions, panel reasoning and refusal grounds, which sit in PDFs.
- **What is not:** the outcome is summarised in a structured register stage, and the leading indicators (growth boundaries, investigation areas, PSP sequencing) are published maps. Developers' acquisition teams already read them, and Landchecker sells the zoning layers (https://landchecker.com.au/). This fails the rubric's "outcome not already summarised" test.

## How the right is bought
- **From whom:** pastoral or family owners.
- **Mechanism:** a call option or put-and-call option, with a fee of about 1-5% (estimate). The owner consents to the proponent lodging the proposal.
- **Price:** owners near growth fronts already charge hope value. Cushman & Wakefield's $125-250k/ha and CBRE's "notable premium" for farms just outside the boundary both say so (Beef Central). Cheap farm-value options exist only well outside published growth areas, where hit rates and timelines collapse.
- **Share of uplift kept:** after the option strike, Victoria's Windfall Gains Tax (which owners will push into the strike price) and contributions, the company keeps perhaps 30-50% of the gross uplift (estimate).

## Capitalised buyer
Stockland, Mirvac, Lendlease Communities, Frasers, Peet, AVJennings, Satterley, ID Land and land funds. They pay immediately for zoned englobo land (Beef Central). But they also option land and run rezonings in-house, so the buyer is also the main competitor for the rung.

## Integration ladder above
Above zoned englobo land sit civil works and subdivision, then lot sales, then built-form housing, then master-planned communities and retail or community assets. A Stockland-scale ASX outcome is possible. The market is domestic, cyclical and capital-intensive, so this is not a trillion-dollar path.

## Who else does this
Every major master-planned community developer's acquisition team, specialist rezoning syndicates and land-bank marketers, and agents openly selling "rezoning upside" parcels. Data and AI tools such as Landchecker and Archistar (https://www.archistar.ai/) sell the legible layers. None of them appears to predict rezoning outcomes.

## Smallest feasibility test (2 weeks)
1. Scrape the NSW planning proposal register for Greater Sydney and the Hunter, 2019-2025, covering Made and Withdrawn proposals.
2. Pull each proposal's gateway determination PDF.
3. Train two models to predict Made versus Withdrawn and time-to-made:
   - a baseline that uses only published layers (growth area, servicing plan, LGA);
   - a model that adds features extracted from the PDFs.
4. Kill criterion: if the PDF features add less than 0.05 AUC, or under 1.2x on implied cost per made proposal, stop.
5. In the same two weeks, interview 3 land agents for current hope-value prices in investigation areas.

## Verdict (relaxed rubric)
| Criterion | Score | Reason |
|---|---|---|
| C1 Frame | 1 | Buyer exists, but discovery is under 30% of the work and the proving step is advocacy |
| C2 Step-up | 2 | About 6-16x gross, 2-6x net |
| C3 Hit-rate lever | 2 | Proving is expensive, but the likely ML lift is about 1.1-1.3x |
| C4 Data + right | 1 | Outcome sits in a structured register stage, indicators are published maps, owners price in hope value |
| C5 Ladder | 4 | Real ladder, but domestic and cyclical |

**Total: 10/25. Not excluded, but killed.** The step-up is already priced in, and Victoria's Windfall Gains Tax takes about half of whatever is left. The proving step is the hard part, not discovery. The signal is already published, and the buyers compete for the same rung.