# L21: Geothermal drilling cost and learning curves, 2015-2026, and what cheaper drilling does to the value of exploration knowledge versus land

**Method note.** The shared WebSearch budget for this run was used up before this agent started. The review therefore relies on primary documents fetched directly and read in full text: Sandia, NREL and DOE reports, the Fervo S-1 on SEC EDGAR, NREL ATB 2024, Stanford Workshop proceedings, and company releases. Numbers come from those texts unless marked (unverified) or (illustrative).

## Bottom line

1. **Drilling is the largest cost line in geothermal, and it is falling fast.**
   - Drilling is 40-50%+ of project capex (Lowry et al. 2017; DOE Liftoff 2024).
   - In 2017 the GeoVision "Baseline" assumed 25 ft/hr ROP, and a 5 km large-diameter vertical well cost **$16.4M over 73.5 days**.
   - By 2024, Fervo's Cape wells reached **70 ft/hr** and **21 days per well**. Cost per horizontal well fell from **$9.4M to $4.8M** over the first four wells.
   - Fervo's 2026 S-1 reports about **75% less drilling time** and about **70% lower cost per foot** from 2022 to 2025.
   - The realized learning rate was **35%**. The plan assumed 18%, and oil and gas averages about 15%.
2. **Cost models have been re-based.**
   - EGS overnight capital cost (OCC): about **$27,800/kW** (ATB 2021 base), then about **$14,700/kW** (2023 FOAK estimate), then about **$7,000/kW** (Fervo's actual Cape figure, S-1 2026).
   - Targets: **$4,700-5,000/kW** by 2030 (Liftoff) and **$3,565-3,700/kW** by 2035 (EGS Shot).
   - ATB 2024 now uses learning rates of 13%/18% (moderate) and 30%/35% (advanced) for hydrothermal and EGS.
3. **Strategic consequence: the scarce input moves from permeability to hot land.**
   - Cheap horizontal drilling plus stimulation makes permeability manufacturable.
   - What cannot be manufactured is **heat at a drillable depth plus legal title to it**.
   - The Fervo S-1 shows the result. Leases cost about **$4/acre** (2019-21). Comparable 2025 BLM bids reached **$344-410/acre**, and a 2026 Utah sale hit **$1,207/acre** (per L07).
   - Cheaper drilling also cuts the cost of *proving* a parcel. That shortens the step-up cycle for a landbank.

## Primary sources reviewed

### 1. Lowry, Finger, Carrigan, Foris, Kennedy, Corbet, Doughty, Pye, Sonnenthal (2017). *GeoVision Analysis Supporting Task Force Report: Reservoir Maintenance and Development.* Sandia SAND2017-9977.
This report builds the well-cost curves that GETEM, GeoVision and the ATB all inherit.
- Drilling "can account for 50% or more of the total capital costs."
- Geothermal wells cost **2-5x** oil and gas wells at the same depth (citing Augustine et al. 2006).
- Cost estimates vary by more than **±50%**.
- Baseline ROP is **25 ft/hr** (88th percentile of Australian EGS bit data) and bit life is 50 hr.
- Baseline 5,000 m large-diameter (12.25") vertical well:
  - **$16.40M total over 73.5 days**;
  - materials 78% of cost; casing alone is 38% and cement 20%;
  - time-dependent costs are 22%, with rotating time only 6.6% of total cost.
- Doubling ROP saves only **14.4%** at 2,500 m and **10.4%** at 5,000 m.
- The "Ideal" curve (mono-bore and similar designs) is **50-75% cheaper than Baseline**. The authors conclude that game-changing cuts "must include a reduction in material costs."
- **Field-scale effect:** with one rig, a 50 MW field of 11 wells takes **1 yr 7 mo** at Baseline and **6.5 months** at Ideal. Faster drilling brings revenue forward. That matters more than the per-well saving.
- Source: https://www.osti.gov/servlets/purl/1394062

### 2. Augustine, Ho, Blair (2019). *GeoVision Analysis Supporting Task Force Report: Electric Sector Potential to Penetration.* NREL/TP-6A20-71833.
GETEM inputs, business-as-usual (BAU) versus Technology Improvement (TI):

| Input | BAU | TI |
|---|---|---|
| Hydrothermal exploration drilling, per project | $3.3-5.4M | 2/3 of BAU |
| Hydrothermal pre-drilling, per project | $0.6-1.2M | about the same |
| Full-size confirmation wells, EGS | 9 at 50% success | 3 |
| Full-size confirmation wells, hydrothermal | 3 at 50% success | 3 at 75% |
| Drilling success | 75% | 90% |
| Cost curve | Baseline | Ideal |

- It cites **Wall & Dobson (2016): 21% exploration project success** (industry feedback 25%). Only 1 in 4-5 explored sites becomes a project.
- Historic growth of about 50 MW/yr implies 200-250 MW/yr of explored sites. Undiscovered-hydrothermal discovery is assumed at **1%/yr (188 MW/yr)**.
- It notes that developers keep exploration data secret "because knowledge of potential sites is a competitive advantage."
- Source: https://docs.nlr.gov/docs/fy19osti/71833.pdf (also https://www.energy.gov/eere/geothermal/geovision)

### 3. Augustine, Fisher, Ho, Warren, Witter (2023). *Enhanced Geothermal Shot Analysis for the Geothermal Technologies Office.* NREL/TP-5700-84822.
- Reference plant: 175 °C, 3 km, binary deep EGS. GETEM gives a BAU OCC of **$32,255/kWe**. Applying the Shot assumptions gives **$3,565/kWe (-89%)**.
- Shot assumptions:
  - exploration drilling at 2/3 of BAU ($1.5-5M per project);
  - **3 rather than 9** full-size confirmation wells, with 75% rather than 50% success;
  - drilling cost at **80% of the GeoVision Ideal curve**, reflecting FORGE ROP gains, cheaper casing and pad drilling;
  - flow of **125 kg/s versus 40 kg/s** per well;
  - plant size of 100 MW rather than 25 MW.
- The Shot target is **$45/MWh by 2035**.
- Order matters: exploration savings come first in the waterfall. Lowering confirmation-well count is an explicit cost lever.
- Source: https://www.nrel.gov/docs/fy23osti/84822.pdf

### 4. US DOE (March 2024). *Pathways to Commercial Liftoff: Next-Generation Geothermal Power.*
- Drilling is **40%+ of project costs**, and about **20% of conventional projects do not find the intended resource**. Conventional LCOE is **$61-102/MWh**.
- **EGS OCC waterfall:**
  - ~$27,800/kW (ATB 2021 base) minus ~$12,000 from recent improvements gives ~$14,700/kW (2023 FOAK, -47%);
  - then -$1,900 exploration, -$4,100 well and reservoir, and -$3,700 power plant;
  - that reaches **$4,700-5,000/kW by 2030 (LCOE $60-70/MWh)** and then $3,700/kW by 2035 ($45/MWh).
- FORGE ROP rose **more than 500% in 3 years**. Fervo showed a 300% ROP gain, with cost falling from **$9.5M to $4.8M over six wells in 6 months**. Per-well development cost fell from **$13M to under $5M** between the first two commercial EGS pilots.
- The oil and gas learning rate is about 15%, and EGS is "doubling" it.
- ATB 2035 advanced assumptions are 80 L/s and 110 ft/hr, against a 2022 base of 40 L/s and 25 ft/hr. Fervo is already at 61-63 L/s and 40-80 ft/hr, more than 50% of the way there.
- A 30 MW EGS facility is about 20 wells, and the 2030 goal implies **1,300-3,300 wells at ~3 MW/well**.
- Only **25 geothermal wells were drilled in the US in 2022**. Oil and gas drilled about 24,000 per year in the 1990s. The learning curve is therefore throughput-limited.
- Source: https://cdn.catf.us/wp-content/uploads/2025/06/09154348/doe-liftoff-nextgen-geothermal.pdf (mirror of liftoff.energy.gov PDF)

### 5. Fervo Energy (El-Sadi et al.), Stanford Geothermal Workshop, 12 Feb 2024: Cape drilling performance. (Release via DCVC; full author list unverified. ATB 2024 cites "El-Sadi et al., 2024".)
- Cape drilling began June 2023, with 6 horizontal and 1 vertical well in about 6 months.
- Fastest well: **21 days, 70% less time** than the first Project Red horizontal (2022).
- Rate of penetration (ROP) reached **70 ft/hr** on the 4th horizontal, which Fervo says exceeds NREL's 2035 moderate projection.
- Cost per horizontal well fell **from $9.4M to $4.8M** (-49%) over the first four wells.
- **Learning rate 35% versus a planned 18%.**
- Cape wells are more than 2,100 ft deeper than Red's.
- Source: https://www.dcvc.com/press-releases/fervo-energy-drilling-results-show-rapid-advancement-of-geothermal-performance/

### 6. NREL (2024). *Annual Technology Baseline 2024, Geothermal.*
- Base-year OCC for identified sites, averages:
  - flash hydrothermal **$4,350/kW** (range $3,091-5,922);
  - binary hydrothermal **$9,483/kW**;
  - NF-EGS **$5,469 / $10,395/kW** (flash / binary columns as inferred);
  - deep EGS **$12,396 / $22,133/kW**.
- Scenarios:
  - Conservative: ROP **25 ft/hr** with the GeoVision Baseline curve, cut 10% using El-Sadi 2024.
  - Moderate: **50 ft/hr** with Intermediate-1, and learning rates of 13% hydrothermal / 18% EGS for 2022-2035.
  - Advanced: **100 ft/hr** with Ideal, and learning rates of 30% / 35%.
- Fervo's realized 35% equals the ATB *advanced* EGS learning rate.
- Source: https://atb.nrel.gov/electricity/2024/geothermal (now served at atb.nlr.gov)

### 7. Fervo Energy Co. (2026). Form S-1 (SEC EDGAR).
- From 2022 to 2025: drilling time down about **75%** and cost per foot down about **70%**.
- Well geometry:
  - Project Red: about 7,500 ft TVD, 11,000 ft MD, 3,000 ft lateral.
  - Cape Phase I: about 9,000 ft TVD, 14,000 ft MD, 5,000 ft lateral.
- More than 25 wells drilled. A 50 MW GeoBlock needs 8-10 wells.
- **Cape capex about $7,000/kW**, with an NOAK target of **$3,000/kW**.
- **Land:** 595,900 acres at a **weighted average of about $4/acre** (2019-2021). The **2025 BLM maximum bids were $344/acre (UT) and $410/acre (NV)**.
- Fervo's screening window is 300-625 °F at ≤13,000 ft TVD.
- Separately (per L07, citing Fervo releases), Sawtooth 7 reached 19,450 ft MD with a 7,500 ft lateral at 460 °F in 21 days.
- Source: https://www.sec.gov/Archives/edgar/data/1853868/000162828026025821/fervoenergy-sx1.htm

### 8. Anderson, Eros, Klarin, Ring, Simpkins (Sage Geosystems), Stanford Workshop 2025. *Hot Dry Rock Geothermal Power Generation Estimates for the USA (L48) Using Reduced Order Physical Models.*
- More than 5 TW of hot-dry-rock potential above 5 km.
- LCOE by depth to 180 °C, relative to a 3-4 km base:

| Depth to 180 °C | LCOE vs base | Capacity |
|---|---|---|
| 2-3 km | -$5/MWh | 53 GW |
| 3-4 km | base | 562 GW |
| 4-5 km | +$5/MWh | 1,044 GW |
| 5-6 km | +$35/MWh | 2,327 GW |

- Below 5 km, **surface high-pressure equipment overtakes drilling** as the capex driver. 6 km is a practical cutoff.
- Implication: cheaper drilling flattens the depth penalty down to about 5 km. Shallow heat still carries a premium, and the 2-3 km bucket is scarce (53 GW).
- Source: https://cdn.prod.website-files.com/67c9634e56bc9ae5113f2fcb/67e6c076244be58baf21aa7f_Stanford%202025.pdf

### 9. LucidCatalyst and Hotrock Research Organization for CATF (Nov 2022). *A Preliminary Techno-Economic Model of Superhot Rock Energy.*
- Each superhot well (≥5 km) costs **$22.0M to drill and complete**, plus **$3.65M stimulation** (the Eagle Ford average), for a total of **$25.7M**.
- Breakdown: drilling 23%, casing 12%, cementing 10%.
- Learning-curve elasticity is -0.125, which is **25% cost reduction from well 1 to well 10**.
- An "advanced drilling without casing" case assumes about $1,000/m.
- This shows that well cost dominates at depth. Each step down in depth multiplies well cost, so the shallow-heat premium persists.
- Source: https://www.catf.us/2025/01/introduction-next-clean-energy-frontier-superhot-rock-geothermal/ (report PDF via CATF)

### 10. Zanskar (Dec 2025). *Zanskar reveals Big Blind* (company Substack).
- Two intermediate-depth wells drilled Jul-Aug 2025 found about **250 °F at about 2,700 ft**. The site had no prior geothermal data, and the discovery was announced 4 Dec 2025.
- Zanskar positions its approach against "expensive stimulations associated with next-gen drilling technologies." Its thesis is that finding natural permeability beats manufacturing it.
- The post gives no exploration-cost figures.
- Source: https://zanskargeothermal.substack.com/p/zanskar-reveals-big-blind-the-discovery

## Synthesis: how cheaper drilling changes knowledge value versus land value

**(a) The cost of proof falls, and so does the information premium for permeability.**
- Under BAU, proving a site takes $1.5-5.4M of exploration drilling plus 3-9 full-size confirmation wells at a 50% hit rate. At 2017-era $5-10M per well, that is $20-50M+ at risk (illustrative, from Sources 2-3).
- That expense is what made pre-drill knowledge of *where the permeable hydrothermal system is* so valuable, and it is Zanskar's product.
- At $4.8M per well and falling, with stimulation able to rescue dry holes (90% success assumed in GeoVision TI), a wrong guess on permeability costs much less.
- Knowledge about **temperature at depth** keeps its value, because heat cannot be engineered. Sage's LCOE-by-depth table and the CATF well cost at depth both show this.

**(b) Land becomes the binding scarce input, and its price is rising.**
- Fervo paid about $4/acre. Two to five years later, comparable bids clear at $344-1,207/acre, a 100-300x step-up.
- The cause was public proof that EGS works and is cheap to drill, not any new data on those parcels.
- Illustrative arithmetic:
  - a 50 MW GeoBlock at $7,000/kW is about $350M of capex;
  - 5,000 acres at $1,207/acre is about $6M, under 2% of capex.
- Developers therefore have large headroom to pay more for qualified hot land (illustrative; acreage per GeoBlock unverified).

**(c) Faster drilling compresses the step-up cycle.**
- Lowry shows field build time falling to about one third, and Fervo drills in 21 days.
- A landbank can move from "ML-ranked" to "drill-confirmed hot" in months, not years. One temperature-gradient or slim hole costs far less than a $4.8M production well (TG-hole costs are in L16; here unverified).

**(d) Throughput limits learning.**
- Only 25 US geothermal wells were drilled in 2022, and Liftoff needs 1,300-3,300 by 2030.
- Learning accrues to whoever drills the most wells, which today is Fervo. A non-drilling rights owner rides that curve for free: every cost-per-foot drop raises the value of hot acreage it already holds.

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **The cost-curve evidence favors owning land over owning drilling know-how.**
   - Drilling cost is being commoditized by the operators: Fervo's 35% learning rate, cost per foot down 70%, and oil and gas rigs and crews.
   - As drilling gets cheaper, value migrates to the input that cannot be replicated: **titled acreage with heat at shallow depth**, meaning ≥300 °F at ≤13,000 ft (Fervo's own screen) and ideally 180 °C at 2-4 km.
   - This is the exact Terranox move: buy the right before the market prices it.
2. **The target should be temperature-at-depth (EGS-grade), not only blind hydrothermal.**
   - Public oil and gas BHTs, gradient holes and mining assessment drill logs are temperature data. They are the right archive for the asset whose value cheaper drilling *raises*.
   - Permeability data, which is Zanskar's moat, is the input whose value cheaper stimulation *erodes*.
3. **Buyers and pricing are already proven.**
   - Fervo's $4 to $344-1,207/acre step-up is the comparable. NOAK capex of $3,000-5,000/kW means land under 2% of capex, so buyers will pay up.
   - Buyers include Fervo (38-50 GW pipeline), Sage, Mazama and Quaise, plus Ormat and utilities for hydrothermal.
4. **The gap vs Zanskar.**
   - Zanskar is vertically integrated. It explores, drills its own wells and operates plants (Lightning Dock), with about $115M raised.
   - Its thesis is to *avoid* stimulation by finding natural permeability, and it optimizes the most drilling-cost-sensitive part of the value chain.
   - It ties up capital per site and is concentrated in Great Basin hydrothermal.
   - The open gap is a **national-scale, capital-light landbank of EGS-grade hot acreage**, ranked by ML on legacy temperature data. It would be de-risked with one cheap gradient or slim hole and sold or farmed out to the EGS developers whose falling drilling costs are lifting land values.
   - Hybrid upside: blind-hydrothermal hits found along the way can be flipped to Ormat-type buyers.
5. **Risks.**
   - (i) BLM competitive sales now price in EGS hype, so the edge must come from cells *not yet nominated*, state and private rights, and non-Great Basin basins.
   - (ii) Fervo already holds about 596k acres and may not need to buy.
   - (iii) The 35% learning rate comes from one operator at one site. Under ATB moderate (18%), the land-value uplift is slower but still positive.

## Sources
- Lowry et al. 2017, SAND2017-9977: https://www.osti.gov/servlets/purl/1394062
- Augustine, Ho, Blair 2019, NREL/TP-6A20-71833: https://docs.nlr.gov/docs/fy19osti/71833.pdf
- GeoVision: https://www.energy.gov/eere/geothermal/geovision
- Augustine et al. 2023, NREL/TP-5700-84822: https://www.nrel.gov/docs/fy23osti/84822.pdf
- DOE Liftoff 2024 (mirror): https://cdn.catf.us/wp-content/uploads/2025/06/09154348/doe-liftoff-nextgen-geothermal.pdf
- Fervo Cape drilling (Feb 2024): https://www.dcvc.com/press-releases/fervo-energy-drilling-results-show-rapid-advancement-of-geothermal-performance/
- NREL ATB 2024 Geothermal: https://atb.nrel.gov/electricity/2024/geothermal
- Fervo S-1 (2026): https://www.sec.gov/Archives/edgar/data/1853868/000162828026025821/fervoenergy-sx1.htm
- Anderson et al. 2025 (Sage), Stanford: https://cdn.prod.website-files.com/67c9634e56bc9ae5113f2fcb/67e6c076244be58baf21aa7f_Stanford%202025.pdf
- LucidCatalyst/HRO for CATF 2022: https://www.catf.us/2025/01/introduction-next-clean-energy-frontier-superhot-rock-geothermal/
- Zanskar Big Blind: https://zanskargeothermal.substack.com/p/zanskar-reveals-big-blind-the-discovery
- BLM lease-price comparables (via L07): https://www.thinkgeoenergy.com/blm-receives-record-breaking-24m-in-winning-bids-in-utah-geothermal-lease-sale/
