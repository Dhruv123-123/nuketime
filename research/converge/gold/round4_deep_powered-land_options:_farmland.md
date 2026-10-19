## Powered-Land Options: round-4 feasibility check

**Search note:** the shared WebSearch budget was used up before this task ran, so I could not run any new searches. The evidence comes from fetching 8 pages directly: the finalist's sources, LandGate, Interconnection.fyi and the Texas SB6 bill text. Figures marked (est.) are my estimates.

### Frame of reference
The rung is: option farmland near a substation, prove "power is coming" with a utility large-load study or will-serve letter, then sell to a data-center developer. The frame breaks because the proof the buyer pays for is **committed load**, not a study. Altus Group (80 deals checked) found "committed utility load was the strongest predictor of land pricing" ([DCK](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)). Committing load means signing an ESA, posting collateral and accepting take-or-pay terms. AEP Ohio requires an 85% minimum demand over 12 years plus a 3-year exit fee ([mgrid](https://mgrid.org/2025/12/03/aep-ohio-data-center-tariff-sets-national-precedent-after-30-gw-interconnection-surge/)). That step is capital-heavy and the utility controls it. Discovery is about 20-35% of the rung (est.). This is the same failure as the geothermal counter-example: the physical/financial step is the hard part.

### Step-up ratio
- **Unproven price:** Licking County, OH farmland sells for $10-15k/acre ([Acres](https://www.acres.com/blog/meta-expands-ohio-footprint-679-million-invested-1345-acre-data-center-campus)). In low-cost markets, unpowered land is about $10k/acre ([DCK](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)). An option costs about $50-300/acre/yr (est.).
- **Proven price, by type of proof:**
  - **Power path established** (infrastructure plus utility relationships): "six figures per acre", about 10-30x ([DCK](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)).
  - **Committed load:** Meta paid more than $1.1M/acre in 2025, after the AEP transmission commitments, about 70-100x farmland ([Acres](https://www.acres.com/blog/meta-expands-ohio-footprint-679-million-invested-1345-acre-data-center-campus)).
  - **Northern Virginia:** entitled unpowered land is about $4M/acre and powered land at least $6M/acre, so power adds about 1.5x ([DCK](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)).
- **Location premium is captured before any proof:** Meta paid about $123k/acre in 2019, before any power proof, so farmers near known demand already capture about 10x ([Acres](https://www.acres.com/blog/meta-expands-ohio-footprint-679-million-invested-1345-acre-data-center-campus)).
- **Buyers pay in tranches against delivered megawatts:** Plug Power sold its Graham, TX site to Stream for $50M plus up to $26.5M contingent on the load finally established ([DCK](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)).
- **Transactions per year:** 80 verified in August alone, and about $6B of land bought in H1 2026, up 79% ([DCK](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)). That suggests about 600-1,000 deals a year (est.).
- **Step-up that can be credited to a study alone:** about 2-10x (est.).

### Hit rate and proving capex, today and with ML
- **Study cost:** Texas SB6 sets a flat screening-study fee of at least $100,000 ([SB6](https://capitol.texas.gov/tlodocs/89R/billtext/html/SB00006F.htm)).
- **Real proving capex:** Plug/Stream put up a $6.5M deposit to Oncor plus a $7.75M letter of credit for 164 MW, about $87k/MW ([DCK](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)). This clears the "expensive" bar easily, but the money is collateral, not discovery spend.
- **Base hit rate:** no source gives a measured study-to-ESA rate. AEP's queue fell from 30 GW to 13 GW once commitments were required ([mgrid](https://mgrid.org/2025/12/03/aep-ohio-data-center-tariff-sets-national-precedent-after-30-gw-interconnection-surge/)), then to 5.6 GW ([E&E](https://www.eenews.net/articles/has-ohio-found-a-way-to-predict-the-power-needs-of-data-centers/)). That is 19-43% survival, but it measures speculators dropping out, not site quality.
- **Lift with ML:** ranking substations by headroom against a naive "230 kV line within X miles" screen gives about 1.2-1.4x on cost per proven site (est.). The voltage tier is already a legible price driver: 230/500 kV sites trade at about 2.4x 138 kV sites ([DCK](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)).

### Data source
- **Named datasets:** utility hosting-capacity maps, IRP load forecasts, ISO/utility generation queues (Interconnection.fyi tracks 44,281 requests from 50+ ISOs and utilities, [link](https://www.interconnection.fyi/)), and FERC Form 715 (CEII-restricted; the FERC page returned 403 to my fetch).
- **Why it is not illegible:** LandGate already sells "Available Power" offtake capacity for "every substation in the US", plus substation-level queues ([LandGate](https://www.landgate.com/energy-markets/data-centers)). So the answer to "where is headroom" is already a packaged field.
- **Where the outcome actually lives:** large-load ESA status is private between the utility and the customer, and capital commitment decides it, not data.

### How the right is bought
- **From whom:** farmers.
- **Legal mechanics:** a purchase option or a ground-lease option, recorded as a memorandum.
- **Price:** near agricultural value, but the gap is closing. LandGate's PowerLeads marketplace sells "ready to sign deals with landowners" ([LandGate](https://www.landgate.com/energy-markets/data-centers)).
- **Site control:** SB6 requires the requester to show site control through ownership, a lease or another legal interest the PUC accepts ([SB6](https://capitol.texas.gov/tlodocs/89R/billtext/html/SB00006F.htm)). An option may not qualify without PUC acceptance (est.).
- **Share of uplift kept:** if the company sells at the study stage, it keeps roughly the 2-10x on option value. To capture the 70-100x it must post per-MW security and sign the ESA itself, which means becoming a capital-heavy developer.

### Capitalised buyer
Real and deep-pocketed:
- Hyperscalers. Meta paid $566M for 514 acres ([Acres](https://www.acres.com/blog/meta-expands-ohio-footprint-679-million-invested-1345-acre-data-center-campus)).
- Developers. SDC paid $615M for 97 acres, and Stream bought Plug Power's Graham site ([DCK](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)).
- Utilities. Dominion paid $45M for about 14 acres ([DCK](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)).

### Integration ladder above
The rungs go: option, then study, then ESA plus collateral, then entitled powered shell, then campus developer, then on-site generation or a utility-like power provider. The ladder is real, and it could lead to a very large company.

### Who else does this
- LandGate (data plus landowner marketplace, [link](https://www.landgate.com/energy-markets/data-centers)).
- GridTracker / Interconnection.fyi ([link](https://www.interconnection.fyi/)).
- Powered-land developers Tract, Cloverleaf and EdgeCore. These are named from background knowledge: tract.com returned empty or 404 to my fetches.
- Brokers such as Avison Young.

### Smallest feasibility test (2 weeks)
Run a backtest in ERCOT/Oncor:
1. Pull 2024-26 county deed records for parcels that sold at 10x or more above farmland value.
2. Score candidate parcels three ways:
   - (a) a naive screen: 230 kV or higher within 2 miles,
   - (b) LandGate's "Available Power" layer (demo account),
   - (c) an ML headroom model built on public queues and IRPs.
3. Kill the idea if (c) does not beat both (a) and (b) by 1.5x in precision at the top 50 parcels.

In parallel, phone 10 farmers near the flagged substations for option quotes, to measure how much of the purchase discount is left.

### Verdict under the relaxed rubric
| | Score | Reason |
|---|---|---|
| C1 Frame | 1.5 | The buyer pays for committed load, and the utility allocates it against collateral; discovery is a minority of the rung. |
| C2 Step-up | 2.5 | About 2-10x for a study, 10-30x for a power path; 70-100x only with an ESA. |
| C3 Hit-rate lever | 2.5 | Proving is expensive, but ML gives about 1.2-1.4x against a kV screen and LandGate (est.). |
| C4 Data + right | 1 | Headroom is already sold as a field; options can be bought, but the discount is closing. |
| C5 Ladder | 4 | Real ladder up to campus developer and power provider. |
| **Total** | **11.5 / 25** | **Not excluded, but it fails the frame test.** |

The relaxed C3 helps a little, but the step-up still comes from committing capital to the utility, not from discovery. Unless the backtest shows ML beating LandGate by 1.5x or more, kill this finalist.