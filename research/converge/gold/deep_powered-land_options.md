## Powered-Land Options: feasibility memo

**Search note:** the shared WebSearch budget (200 calls per turn) was used up before this run, so no searches ran. I fetched the primary pages listed below directly. Any figure without a URL is marked as an estimate or as recalled from memory. A follow-up message can resume searching.

### Frame of reference
The proposed rung: option farmland near a substation, prove headroom with a utility large-load study or will-serve letter, then sell "powered land." Discovery (finding headroom) is about 30-40% of this rung (estimate). The rest is not discovery:
- **Site control.** Texas SB6 requires an ownership interest or lease. [SB6 text, s.37.0561(g)](https://capitol.texas.gov/tlodocs/89R/billtext/html/SB00006F.htm)
- **$/MW financial security or CIAC** for transmission ([SB6 s.37.0561(h)](https://capitol.texas.gov/tlodocs/89R/billtext/html/SB00006F.htm)), plus multi-year minimum bills.
- **Rezoning, water and fiber.**

CBRE reports that utilities are asking developers to "contribute toward capital costs for generation and transmission" ([CBRE H1 2025](https://www.cbre.com/insights/reports/north-america-data-center-trends-h1-2025)). The physical and capital step dominates. This matches the geothermal-in-coal-mines counter-example.

### Step-up ratio
- **Unproven:** US cropland averages $5,830/acre ([USDA NASS 2025](https://www.nass.usda.gov/Publications/Todays_Reports/reports/land0825.pdf)). Options run $50-300/acre/yr (candidate's figure, unverified).
- **Proven:**
  - NoVA data-center land at about $1-3M/acre (recalled, unverified).
  - Secondary-market hyperscaler farmland buys at about $30-300k/acre (recalled, unverified).
  - Prince William Digital Gateway contracts at about $0.5-1M/acre against roughly $20-50k/acre before. That jump came from county rezoning, not a load study (recalled; the Wikipedia page 404'd).
- **What a study alone earns:** about 2-5x (estimate), because buyers price firm, contracted MW. CBRE says buyers want power "within 18 to 36 months" and increasingly need 200 MW or more ([CBRE](https://www.cbre.com/insights/reports/north-america-data-center-trends-h1-2025)).
- **The headline 10^3x is not an asset step-up.** It compares an annual option fee with a fee-simple price.
- **Transactions/yr:** a few hundred large US data-center land deals a year (estimate).

### Hit rate and proving capex today and with ML
- **Cost per attempt:** at least $100k study fee per site for loads of 75 MW and up in Texas ([SB6 s.37.0561(f)](https://capitol.texas.gov/tlodocs/89R/billtext/html/SB00006F.htm)). Candidate's range is $50-250k.
- **Base hit rate:** 15-30% (estimate), so ML's lever is capped at about 3-6x.
- **Speculation is high.** Near Homer City, 181 of 233 interconnection requests (78%) were withdrawn ([LandGate](https://www.landgate.com/news/ferc-rejected-pjm-s-large-load-plan)). AEP Ohio's queue reportedly fell from about 30 GW to about 13 GW after its tariff (recalled, unverified).
- **Capex does not bind.** About $100k per attempt is small against a $10-100M exit. ML would not change the economics by 10x.

### Data source
- **Datasets:** FERC Form 715 (CEII-gated), RTO expansion plans, EIA-860, IRPs, PUC large-load dockets, HIFLD substations, queue withdrawals.
- **The signal is already legible.** LandGate sells offtake capacity for "98%" of US substations (">84K mapped"), with parcel search by distance and capacity, and a PowerLeads landowner marketplace ([LandGate](https://www.landgate.com/energy-markets/data-centers)).
- **The true outcome is not in any dataset.** Firm capacity is created by the utility study plus ESA collateral.
- **Prior hunt:** ML added only about +0.004 AUC over simple screening.
- **C4 fails.**

### How the right is bought
Options or fee purchases come from farmers through standard option-to-purchase agreements, with recording of a memorandum of option. The purchase discount is real, unlike brownfields.

The discount is eroding:
- LandGate's marketplace lists ">100MM acres" ([LandGate](https://www.landgate.com/energy-markets/data-centers)), which narrows the owner's information gap.
- Farmers near substations increasingly ask for data-center-contingent strike prices (estimate).

Capacity does not run with the land. It attaches to whoever signs the service agreement and posts security:
- AEP Ohio: 85% minimum bill for up to 12 years.
- Ameren Missouri: two years of minimum bills posted upfront.
- Evergy Kansas: 80% minimum bill for 12 years.

Source for all three: [LandGate tariff survey](https://www.landgate.com/news/large-load-tariffs-are-redrawing-the-site-selection-map). Texas SB6 also forces disclosure of duplicate requests elsewhere in the state ([s.37.0561(d)](https://capitol.texas.gov/tlodocs/89R/billtext/html/SB00006F.htm)).

### Capitalised buyer
Hyperscalers (Microsoft, Meta, Google, AWS), colos (QTS, Vantage, Stack, Aligned) and powered-land funds. Primary-market vacancy is a record-low 1.6% ([CBRE](https://www.cbre.com/insights/reports/north-america-data-center-trends-h1-2025)). The buyer is real and deep-pocketed, but it buys contracted, energizable MW, not studies.

### Integration ladder above
1. Options
2. Study
3. ESA/collateral
4. Entitlements
5. Powered shell
6. Own substation or behind-the-meter generation
7. Campus developer or operator

Cloverleaf is already at rungs 5-6: Project Red Granite covers up to 1,900 acres next to 345 kV lines, targets 3.5 GW by 2030, and expected zoning by May 2025 ([Cloverleaf](https://www.cloverleafinfra.com/)). The trillion-dollar path exists (site, then power, then compute), but every rung is capital-heavy, not discovery-heavy.

### Who else does this
- **Tract:** powered-land developer (its site returned empty; recalled).
- **Cloverleaf Infrastructure** ([site](https://www.cloverleafinfra.com/)).
- **EdgeCore and Hunt** (recalled).
- **LandGate:** data plus landowner marketplace ([site](https://www.landgate.com/energy-markets/data-centers)).
- **Others:** land brokers and powerflow consultancies.
- **Regulators are tightening:** 29 large-load tariffs approved in 2025, against 14 in the prior seven years combined ([LandGate](https://www.landgate.com/news/large-load-tariffs-are-redrawing-the-site-selection-map)). FERC kept PJM's 50 MW large-load registry on Oct 9, 2026 ([LandGate](https://www.landgate.com/news/ferc-rejected-pjm-s-large-load-plan)).

### Smallest feasibility test (2 weeks)
Pull 20-30 recent hyperscaler or colo farmland purchases in Ohio, Indiana, Georgia and Texas from county deed records. For each, record:
- price per acre against the prior ag sale;
- whether a utility study or will-serve letter existed before the sale, or a rezoning or ESA came first (PUC dockets, county minutes);
- LandGate's capacity score for the parcel before the sale.

Then ask 5 powered-land brokers or funds to quote the same site three ways: study-only, ESA-backed, and energized.

**Decision rule:**
- **Kill** if the price jump tracks rezoning or ESA timing rather than study timing, or if study-only sites quote under 5x ag value, or if LandGate already flagged the winning parcels.
- **Survive** only if study-only sites sell at 30x or more and the winning parcels were not visible in LandGate.

### Verdict
**Kill.** The farmland purchase discount is real and the ladder is large, but the rung fails the 80%-discovery frame:
- Capacity belongs to whoever posts collateral and signs the ESA, not to the parcel or to whoever reads grid data first ([SB6](https://capitol.texas.gov/tlodocs/89R/billtext/html/SB00006F.htm), [tariff survey](https://www.landgate.com/news/large-load-tariffs-are-redrawing-the-site-selection-map)).
- Headroom data is already sold as a legible field ([LandGate](https://www.landgate.com/energy-markets/data-centers)).
- A study-only step-up is about 2-5x (estimate).
- The ML lever is at most 3-6x, on capex that is not the binding constraint.

Revised scores: C1 1, C2 2, C3 2, C4 1, C5 4. Total about 10-11 of 25. This is not worth a YC slot as a Terranox analogue. The 2-week deed-record test above would settle it cheaply if anyone wants a confirmatory kill.