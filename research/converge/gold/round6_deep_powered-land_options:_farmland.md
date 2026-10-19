## Frame of reference
The rung: buy an option on farmland near a substation, then get a utility large-load study or will-serve letter for it, and sell the result to a data-center developer as "powered land". The frame fails C1. A buyer pays for an executed ESA or final interconnection, not for a study. In the Plug Power to Stream deal (Graham TX), $26.5M of the price depended on the load capacity in the final agreement ([DCK](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)). Altus calls committed load "the strongest variable" in data-center land prices, and says power and utility coordination usually takes 30-40 months before a deal is recorded ([Altus](https://www.altusgroup.com/insights/where-value-is-created-in-data-center-land/)). So picking the site is perhaps 30-40% of the work (estimate). Collateral, rezoning and utility negotiation make up the rest. This is the geothermal failure mode: the capital step dominates the discovery step.

## Step-up ratio
- **Unproven price:** about $10k/acre in low-cost markets with no power path ([DCK](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)). PA farmland averages $9,560/acre ([Fortune](https://fortune.com/2026/02/21/farmer-15-million-dollar-data-center-developers-farmland-prices-preservation-backlash-agriculture-economy)).
- **Proven price:** "six figures" per acre once power is established ([DCK](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)). The median in markets with limited committed load is $28k/acre, and Central OH, Phoenix and Atlanta run $100k-460k/acre ([Altus](https://www.altusgroup.com/insights/where-value-is-created-in-data-center-land/)). Plug/Stream paid a $50M base for about 66 acres, roughly $760k/acre (my calculation from [DCK](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)). In NoVA, entitled land without power is about $4M/acre and powered land at least $6M/acre, so power alone adds only about 1.5x there.
- **Ratio:** about 3-35x, and it arrives only with committed capacity (estimate drawn from the figures above).
- **Volume:** about $6B in H1 2026, up 79% YoY ([DCK/Avison Young](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)). That is a few hundred deals a year at most (estimate; Cushman puts the average deal at 224 acres).

## Hit rate and proving capex today and with ML
- **Cost per attempt:** each study or deposit costs $75k-600k and takes 6-24 months. EKPC charges $75k + $1k/MW ([KY PSC](https://psc.ky.gov/pscecf/2025-00140/jacob.watson@ekpc.coop/07142025083010/2025-00140_Responses_to_Staffs_DR1.pdf)). Xcel CO asks about $600k upfront ([i2i](https://i2i.org/xcel-energy-proposes-large-load-tariff-for-data-centers/)).
- **Texas:** the draft PUCT rule adds $50k/MW of security, with 80% forfeitable, which is about $10M per 200 MW site ([Foley](https://www.foley.com/insights/publications/2026/03/public-utility-commission-of-texas-issues-proposed-rules-for-large-load-interconn/)).
- **Base rate:** about 12% of 1,066 GW of requested load has firm service, and about 28% is expected to be served ([Wood Mackenzie via Capacity](https://capacityglobal.com/news/wood-mackenzie-us-grid-operators-set-to-serve-28pc-of-data/)). Most of the failure comes from commitment and speculation, not from picking the wrong substation.
- **ML lift:** a competitor can simply subscribe to modelled substation offtake data, so ML likely lifts cost per proven site by under 1.2x (estimate). Earlier work found lookup tables match ML on grid siting.

## Data source
Public inputs: FERC Form 715 power-flow cases, ISO queue files, utility hosting-capacity maps, IRP appendices and large-load tariff dockets. Some pieces are scanned or unstructured, such as IRP appendices and substation one-lines. But the outcome is already a legible field you can buy. LandGate sells "offtake capacity data for every substation in the US" with 98% coverage across more than 84k substations, built from DC and AC models ([LandGate](https://www.landgate.com/energy-markets/data-centers)). Enverus sells parcel-level MW feasibility ([Enverus](https://www.enverus.com/solutions/site-and-screen/)). Fails C4.

## How the right is bought
A purchase or lease option comes from the farmer. Texas's draft rule accepts an option as site control ([Foley](https://www.foley.com/insights/publications/2026/03/public-utility-commission-of-texas-issues-proposed-rules-for-large-load-interconn/)). But sellers are informed:
- A PA farmer turned down $15M at $60k/acre ([Fortune](https://fortune.com/2026/02/21/farmer-15-million-dollar-data-center-developers-farmland-prices-preservation-backlash-agriculture-economy)).
- NE Wisconsin dairy land doubled in price ([Dairy News](https://dairynews.today/news/ai_data_centers_drive_up_wisconsin_dairy_land_prices_8754400.html)).
- LandGate's PowerLeads marketplace offers "ready to sign deals with landowners" ([LandGate](https://www.landgate.com/energy-markets/data-centers)).

Share of uplift kept: if the company sells at the study stage, perhaps 10-30% (estimate). If it posts ESA collateral and holds the site, more, but then the return comes from capital, not from information.

## Capitalised buyer
Yes, and well funded: hyperscalers, colocation developers (QTS, Stream, Vantage) and land platforms such as Tract. Plug/Stream shows they will pay about $300k/MW for capacity that is actually established (my calculation from [DCK](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)).

## Integration ladder above
The rungs run: powered land, then entitled and energised campus, then powered shell or build-to-suit, then data-center operation, then on-site generation and PPAs. Tract shows the land-to-campus path can support a multi-$B company. Strong C5.

## Who else does this
- Tract
- Cloverleaf ($300M raised; abandoned Greenleaf WI; [DCD](https://www.datacenterdynamics.com/en/news/cloverleaf-backs-out-of-data-center-project-in-greenleaf-wisconsin/))
- Scale/Reload ([Latitude](https://www.latitudemedia.com/news/scale-buys-reload-as-the-hunt-for-powered-land-heats-up/))
- Silver Lake/Commonwealth ($400M powered-land platform)
- Quinbrook's Rowan
- Exowatt's ExoRise
- Data vendors: LandGate, Enverus, Acres

## Smallest feasibility test (2 weeks)
1. Run a backtest in one ISO, such as PJM's AEP Ohio zone. Label parcels that sold at data-center prices from county records plus the Altus/DCK comps. Score them three ways: (a) a simple rule (within 0.5 mi of a 230kV+ substation); (b) LandGate's offtake field; (c) an ML model over FERC 715, queue and IRP text.
2. Call 20 owners near the top-ranked substations and record their option asks as a multiple of farm value.
3. Kill criteria: kill the idea if ML beats LandGate by less than 0.03 AUC, or if the median ask is above 3x ag value.

## Verdict (relaxed rubric)
| | Score | Why |
|---|---|---|
| C1 Frame | 2 | Buyers pay for committed capacity, which needs collateral, not discovery |
| C2 Value capture | 2 | Holding and developing the site is possible, but sellers already price in the premium; return on capital is likely 1.5-2.5x (estimate) |
| C3 Hit-rate lever | 2 | Proving is expensive, but ML adds under 1.2x over vendor offtake data |
| C4 Data + right | 1 | The outcome is sold as a field; owners are informed |
| C5 Ladder | 4 | Tract-style path to campus and operation |
| **Total** | **11/25** | Not excluded, but weak |

The prior verifiers agreed: all 3 refuted it, and their revised totals averaged 12.7. Recommend dropping it.

My web search budget was used up for this turn, so I could only open existing sources directly, not run new searches. I did not independently re-verify the Cloverleaf sale price, the adopted Texas rule text, or the Fortune, Dairy News, Enverus and Latitude pages.