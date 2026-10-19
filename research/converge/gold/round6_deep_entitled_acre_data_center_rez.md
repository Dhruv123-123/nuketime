## Entitled Acre (data center rezoning arbitrage): feasibility deep-dive

*Method note: the shared web-search budget for this turn ran out before my first query, so I could not run any new searches. The evidence below comes from 7 page fetches (the finalist's and verifiers' sources plus the Data Center Watch homepage). Figures marked "est." are my estimates.*

### Frame of reference
The rung is "entitled land": take an option on agricultural parcels, win a rezoning or special exception, then sell to a data center developer. Picking the parcel and predicting the vote from minutes is about 40-50% of the work (est.). The rest is political and legal work, plus proving power through a utility load study, a will-serve letter and a substation. Power is the bespoke physical step, the same pattern as the geothermal counter-example. Even the best case shows this: Kuhn's Twin Creeks site needed a 13.3-acre substation parcel sold to Dominion for $45M ([NoVA Mag](https://northernvirginiamag.com/news/2025/11/06/chuck-kuhn-sells-leesburg-land-to-data-center-developer-for-615-million/)).

### Step-up ratio
- **Unproven:** farmland at about $6k/acre in Kentucky and $10.5-23k/acre in Wisconsin ([Fortune](https://fortune.com/2026/02/21/farmer-15-million-dollar-data-center-developers-farmland-prices-preservation-backlash-agriculture-economy), [Dairy News](https://dairynews.today/news/ai_data_centers_drive_up_wisconsin_dairy_land_prices_8754400.html)). Speculative entitlers already pay about $26k/acre for land with no rezoning and no utility commitment: Arizona Land Consulting paid $25M for 956 acres in Tonopah ([Hoodline](https://hoodline.com/2026/05/tonopah-desert-mega-deal-supercharges-data-center-land-grab/)).
- **Proven:** Google paid $42.5M for 948 acres, about $45k/acre, after a C-1 rezoning in Nov 2024 ([Baxtel](https://baxtel.com/data-center/google-monroe-county)). Developers offered $60k/acre in Lancaster PA ([Fortune](https://fortune.com/2026/02/21/farmer-15-million-dollar-data-center-developers-farmland-prices-preservation-backlash-agriculture-economy)). In Loudoun, JK Land paid $57M (mostly 2021) and sold 97 acres for $615M, about $6M/acre ([NoVA Mag](https://northernvirginiamag.com/news/2025/11/06/chuck-kuhn-sells-leesburg-land-to-data-center-developer-for-615-million/)).
- **Ratio:** about 5-10x in greenfield counties and about 11x in the best powered Northern Virginia case, i.e. 10^0.7 to 10^1.
- **Transactions per year:** dozens of large US deals (est.; no source found).

### Hit rate and proving capex, today and with ML
- **Cost:** about $100-500k per attempt (est.). Rezoning takes 6-12+ months, and 24-36 months or denial under opposition ([Acres](https://www.acres.com/blog/zoning-trajectory-data-center-land-costs)).
- **Base approval rate:** unsourced. My estimate is 50-80% and falling. At least $152-156B of projects were blocked or delayed in 2025, with hundreds of opposition groups active in 42 states ([DCW](https://www.datacenterwatch.org/q3-q4-2025)). Archbald PA denied one project 5-0 in March 2026 ([DCW](https://www.datacenterwatch.org/)).
- **With ML:** about 1.2-1.5x on cost per entitled parcel (est.). The cap comes from two things:
  - The staff recommendation and the opposition data are already legible.
  - Power, which planning records do not show, is a second gate that passes maybe 30-50% of the time (est.).

### Data source
- **What exists:** planning commission agendas, packets, minutes, hearing videos, comprehensive plans and overlay maps for about 3,000 counties. All public, scattered and unstructured.
- **Is the outcome already written down?** Partly. The staff recommendation in the agenda packet is a legible field that likely predicts most votes (untested; this is the C4 kill risk). Opposition is already compiled and sold: Data Center Watch sells project-level data, Paces sells AI power and permitting screens, and Zoneomics sells zoning data for 23,500+ cities via API ([verifier sources](https://www.paces.com/)). Power signals (IRPs, queues) are semi-legible.

### How the right is bought
- **From whom:** private farmland owners, through purchase options.
- **Price:** option fees of about 1-3% of the strike per year (est.), with a strike near farm value plus a premium.
- **Mechanics:** a recorded option with a rezoning-contingent close, plus owner consent to the land-use application.
- **Problem:** sellers can read the opportunity. Press coverage of $35-60k/acre offers is widespread, a land trust outbid a developer in Lancaster, and hyperscalers such as QTS/Compass contract directly with owners on rezoning-contingent terms, so the owner keeps the premium (Pageland, per verifier).
- **Share kept:** an intermediary keeps maybe 20-50% of the uplift, and only in unwatched counties, which are also where power is usually missing (est.).

### Capitalised buyer
Real and very large: Google, AWS, Microsoft, Meta, QTS/Blackstone, Vantage, SDC and Compass. They pay most for land that has both power and entitlement.

### Integration ladder above
Option, then entitled land, then powered land (substation and interconnection), then a powered shell, then a leased campus, then operator or REIT, possibly with on-site generation. This runs to a very large company. Each rung above entitlement needs $100M+ of capital and utility access, where ML gives no edge.

### Who else does this
- **Asset owners:** Tract, Arizona Land Consulting, JK Land Holdings, brokers and land trusts.
- **Data/analytics sellers:** Paces, Zoneomics and Data Center Watch (10a Labs).

### Smallest feasibility test (2 weeks)
Backtest about 100 data center rezoning or special-use votes from 2024-26 in Virginia, Georgia, Indiana and Pennsylvania:
1. Scrape the pre-vote agenda packets and minutes.
2. Fit two predictors: (a) the staff recommendation plus zoning class only, and (b) an LLM reading the full record plus opposition signals.
3. **Kill test:** if (b) beats (a) by less than about 0.05 AUC, or the staff recommendation alone is at least 85% accurate, the illegibility edge is dead.

In parallel, call 15 owners or brokers in "unwatched" counties that have a substation within 5 miles, to learn the option strikes actually on offer.

### Verdict (relaxed rubric)
| | Score | Reason |
|---|---|---|
| C1 | 2 | Discovery is not 80%+ of the work; proving power is physical and bespoke. |
| C2 | 3 | Options give leverage: a Kuhn-style ~11x is possible, but only where power and competition already exist. Risk-adjusted, it is about 2-4x on capital in a multi-$B market. |
| C3 | 3 | Proving is expensive, but ML gives at best about 1.2-1.5x. |
| C4 | 2 | The data is illegible, but the staff recommendation and opposition data are legible or already sold. |
| C5 | 4 | A real ladder to a very large company. |

**Total: 14/25. Not excluded.** This is not a Terranox analogue. The ML proves the wrong thing (zoning), while power sets the premium and sellers already know it. Run the 2-week backtest only if the staff-recommendation baseline turns out weak.