# L06: GeoVision, Liftoff, Enhanced Geothermal Shot, and the US geothermal resource and cost literature

Scope: what DOE, NREL and USGS say about how much geothermal resource the US has (hydrothermal, EGS, superhot), what it costs, and how much capacity they forecast by 2050. Read for a Terranox-shape company: find hidden resources in public data, buy the rights cheaply before they are proven, and own the step-up.

## 1. Primary sources reviewed

### 1.1 Williams, Reed, Mariner, DeAngelo, Galanis (USGS, 2008). Fact Sheet 2008-3082, "Assessment of Moderate- and High-Temperature Geothermal Resources of the United States"
- Identified hydrothermal systems: **9,057 MWe** (mean), in 13 states.
- **Undiscovered hydrothermal: 30,033 MWe** (mean), more than 3x the identified total.
- EGS (provisional): **517,800 MWe**.
- This is still the base layer for every DOE/NREL model below. "About 75% of conventional resource is undiscovered" comes from it.
- https://pubs.usgs.gov/fs/2008/3082/

### 1.2 DOE GTO (2019). *GeoVision: Harnessing the Heat Beneath Our Feet*, Chapter 3 (analysis by Augustine et al. 2019, Young et al. 2019, McCabe et al. 2019, using the ReEDS and GETEM models)
- 2050 scenarios: **Business-as-Usual ~6 GWe; Improved Regulatory Timeline 13 GWe; Technology Improvement (TI) 60 GWe**. The TI case is about 26x 2019 capacity, 8.5% of US generation, and mostly deep EGS after 2030.
- Resource available in ReEDS (Table 3-2, TI case): identified hydrothermal **5,128 MWe**, undiscovered hydrothermal **23,038 MWe**, near-field EGS **1,443 MWe**, deep EGS **4,248,879 MWe**. The BAU/IRT case has 5,078 / 18,830 / 1,382 / 3,375,275 MWe.
- **Key assumption for us:** undiscovered hydrothermal becomes available at only **1% per year (~200 MWe/yr) in BAU** and **3% per year in IRT and TI**. The TI rate "was conservatively held constant at 3% ... because it was not possible to quantify an improvement based on yet-unforeseen technology improvements". So the flagship DOE model gives **no credit for better exploration finding more hidden hydrothermal systems**. Exploration gains are modelled only as lower cost and risk.
- Cost and risk inputs (Table 3-3, hydrothermal BAU vs TI):
  - Pre-drilling exploration: **$0.6-1.2M per project**.
  - Exploration drilling: **$3.3-5.4M per project**, cut to two-thirds in TI.
  - Full-size confirmation wells: 3 wells, **50% success** in BAU, **75%** in TI.
  - Drilling success rate: **75% → 90%**.
  - Construction timeline: **8 years** for hydrothermal and **10 years** for EGS in BAU, cut to 4 and 5 years in IRT.
  - Financing: in BAU, geothermal WACC is about **6 percentage points above** wind and solar because of early-stage equity risk. TI assumes de-risking brings it down to the standard 8%.
- Overnight capital cost charts: hydrothermal flash about $4,000+/kW in BAU, reduced by about $1,000/kW in TI. EGS binary falls from about **$31,000/kW to under $5,000/kW** in TI, mostly from flow-rate gains (40 → 110 kg/s per well).
- https://www.energy.gov/eere/geothermal/geovision ; Ch.3: https://www.energy.gov/eere/geothermal/articles/geovision-chapter-3 ; exec summary: https://apps.openei.org/geovision/executive-summary

### 1.3 Augustine, Fisher, Ho, Warren, Witter (NREL, Jan 2023). NREL/TP-5700-84822, *Enhanced Geothermal Shot Analysis for the Geothermal Technologies Office*. Stanford Workshop preprint NREL/CP-5700-85033
- Re-runs GeoVision with updated EGS cost and resource inputs, using ReEDS with Solar Futures decarbonization as the baseline. EGS is assumed commercial from 2030.
- Result: if the Shot cost target is met, US geothermal reaches **90 GWe by 2050**, about 25x current capacity. This is total geothermal, not EGS alone; most of the increase is EGS.
- https://www.nrel.gov/docs/fy23osti/84822.pdf ; https://research-hub.nrel.gov/en/publications/enhanced-geothermal-shot-analysis-for-the-geothermal-technologies/

### 1.4 DOE (Sept 2022). Enhanced Geothermal Shot (Energy Earthshot)
- Target: cut EGS cost **90%, to $45/MWh by 2035**.
- DOE cites more than **5 TW** of US heat resource. Supporting programs include **$44M** for FORGE and **$84M** (Bipartisan Infrastructure Law) for four EGS pilot demonstrations.
- US geothermal capacity at launch: about **3.7 GW**.
- https://www.energy.gov/node/4822595 ; https://www.thinkgeoenergy.com/new-us-doe-earthshot-initiative-aims-to-reduce-egs-cost-by-90/

### 1.5 DOE Office of Technology Transitions / LPO (March 2024). *Pathways to Commercial Liftoff: Next-Generation Geothermal Power* (read in full text)
- Resource: "about **40 GW** of estimated conventional geothermal resource in the U.S., but only **25%** of that estimated resource has been located". Only **9 GW is identified** and **3.7 GW is producing** (93 plants), and 40% of that comes from The Geysers. Next-generation (EGS and closed-loop) resource is **5,500 GW** ("40 GW to over 5,000 GW").
- 2050 deployment: next-generation geothermal reaches **90 GW** (Earthshot scenario; 88-125 GW in the cases modelled). It reaches **130+ GW** if land for other renewables is restricted, **300+ GW** if storage and flexible operation are valued, and 171+ GW in some flexible cases. This is set against a need for **700-900 GW** of new clean firm capacity by 2050.
- Phase 1 "liftoff": **2-5 GW by 2030**, about 100+ developments in 4-6 states, **$20-25B** of capital. Phase 2: **$225-250B** to 2050. To reach 90 GW, the industry needs **10+ GW per year** by the 2040s.
- Costs:
  - Conventional hydrothermal LCOE today: **$61-102/MWh**.
  - EGS overnight capital cost estimate fell from **$27,800/kW (2021) to about $14,700/kW (2023)**, roughly 47%. The path is to **$4,700-5,000/kW by 2030** and EGS national average LCOE of **$60-70/MWh by 2030** ($40-50/MWh in the best regions), then $45/MWh by 2035.
  - Clean firm PPAs are signing at **$70-100/MWh**, $20-50 above solar.
  - Fervo has reported **60-63 L/s per well** and 40-80 ft/hr drilling rates, against ATB 2035 assumptions of 80 L/s and 110 ft/hr.
- Risk: "roughly **20% of projects do not find the intended resource**". Drilling is **40%+ of project cost** and is fully at risk until confirmation. The DOE GRED cost-shared drilling program (1982-2012) "identified much of the geothermal capacity that is currently online in the U.S."
- Permitting: BLM leasing and permitting run through 43 CFR 3250/3260/3270, and the report describes the "chicken-and-egg" problem between exploration funding and permitting.
- The report treats conventional hydrothermal as a niche and puts all of its scale-up on EGS.
- Full text: https://cdn.catf.us/wp-content/uploads/2025/06/09154348/doe-liftoff-nextgen-geothermal.pdf ; summary: https://www.thinkgeoenergy.com/us-doe-publishes-report-on-commercial-liftoff-of-next-generation-geothermal/

### 1.6 Burns, Williams, DeAngelo (USGS, May 2025). Fact Sheet 2025-3027, *Enhanced Geothermal Systems Electric-Resource Assessment for the Great Basin*
- Provisional best estimate: **135 GWe of EGS above 6 km** across 633,072 km², about 10% of current US generating capacity.
- This is only **0.5%** of the accessible electric-grade heat. With continued technology gains (viable geology 25→50%, heat extraction 25→65%), the estimate rises to **more than 10x** (more than 1,350 GWe).
- Uses new heat-flow maps and a 3D temperature model, and counts all electric-grade rock above 90 °C. Rock near active hydrothermal systems (under 1% of volume) is excluded.
- The 2008 Western US EGS estimate was 518 GWe, with 150 GWe in Nevada and Utah.
- The Energy Act of 2020 directs USGS to update assessments, including hydrothermal, for the whole US.
- https://pubs.usgs.gov/publication/fs20253027 ; https://pubs.usgs.gov/fs/2025/3027/fs20253027.pdf

### 1.7 Aljubran and Horne (Stanford, 2024). *Geothermal Energy* (InterPIGNN thermal earth model) and *Scientific Reports* (EGS supply curves)
- A physics-informed graph neural network trained on **more than 400,000 bottom-hole temperatures**, mostly from oil and gas wells, plus gravity, magnetics, heat flow, seismicity, magnetotellurics and fault/volcano distance.
- Output: temperature, heat flow and thermal conductivity for the conterminous US at **0-7 km**, on cells of about 18 km². Mean absolute error is **4.8 °C**, against the coarse 5-arc-minute SMU maps used before.
- Companion EGS supply-curve paper: **82,945 GW** of EGS supply capacity at 1-7 km in the contiguous US under business-as-usual assumptions.
- This shows that public oil and gas well temperatures plus ML give a nationwide, open thermal map. That is the Terranox "illegible public data" analogue, already done at screening level and released openly.
- https://arxiv.org/pdf/2403.09961 ; https://gdr.openei.org/submissions/1592 ; https://doaj.org/article/1a381c8dbfd54ca2931d58ef0120d708

### 1.8 Ricks, Voller, Galban, Norbeck, Jenkins (Princeton/Fervo). *Nature Energy* (online Jan 2024; vol. 10, 2025), "The role of flexible geothermal power in decarbonized electricity systems"
- Flexible EGS operation gives load-following plus in-reservoir storage with **59-93% round-trip efficiency**. Combined with lower drilling costs, it supports **more than 100 GW of EGS in the western US**.
- This is the academic basis for Liftoff's "300 GW" upside case.
- https://ideas.repec.org/a/nat/natene/v10y2025i1d10.1038_s41560-023-01437-y.html ; https://engineering.princeton.edu/news/2024/02/16/flexible-geothermal-power-approach-combines-clean-energy-built-battery

### 1.9 Clean Air Task Force (2022). *Heat Beneath Our Feet* (superhot rock), with HERO and LucidCatalyst
- Superhot rock is above 400 °C (supercritical water). Modelled nth-of-a-kind LCOE is **$20-35/MWh**.
- A single IDDP Krafla well has an estimated **36 MWe** potential, about 10x a typical hydrothermal well.
- A later CATF model claims **4.3 TW** in the US if 1% of the superhot resource is used (63 TW globally). This is advocacy modelling, not a peer-reviewed or USGS figure.
- https://www.thinkgeoenergy.com/catf-publishes-comprehensive-study-on-superhot-rock-energy/ ; https://www.catf.us/2025/01/introduction-next-clean-energy-frontier-superhot-rock-geothermal/

### 1.10 NREL Annual Technology Baseline, geothermal (2022/2024)
- Hydrothermal base-year costs are calibrated to real plants. EGS costs are not calibrated, because no commercial EGS plant exists.
- ATB 2022 hydrothermal OCC is about **$4,156/kW** for ≥200 °C resource, rising to about **$17,060/kW** for <135 °C. This is a garbled extract, so treat the bin mapping as (unverified).
- Recent public PPAs: Hell's Kitchen (CA) about **$75/MWh**; Puna (HI) about **$70/MWh**.
- https://atb.nrel.gov/electricity/2024/geothermal

### 1.11 Faulds et al. (UNR/Nevada Bureau of Mines; DOE Play Fairway, 2015-2021)
- Mapped **96,000 km²** of Nevada and found 24 highly favourable sites. Discovered a blind system at southern Gabbs Valley: about **120 °C at about 150 m**, with no surface expression.
- McGinness Hills (Ormat, about 80 MW net) is the reference blind field.
- Supports the USGS view that most Great Basin systems are blind.
- https://gdr.openei.org/files/756/Faulds-DE-EE0006731-Report-v2.pdf ; https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2017/Faulds.pdf

## 2. Synthesis: resource, cost and forecast numbers

| Layer | US resource | Source |
|---|---|---|
| Producing | 3.7 GW (93 plants) | Liftoff 2024 |
| Identified hydrothermal | 9 GW (5.1 GW usable in ReEDS) | USGS 2008; GeoVision |
| Undiscovered hydrothermal | 30 GW mean (23 GW usable in ReEDS) | USGS 2008; GeoVision |
| EGS, Great Basin only | 135 GWe best estimate, more than 1,350 GWe with tech gains | USGS 2025 |
| EGS, US | 518 GWe (2008), about 5,500 GW (Liftoff), 4.25 TW deep EGS (GeoVision ReEDS), 82,945 GW (Aljubran) | various |
| Superhot | 4.3 TW at 1% use (advocacy) | CATF |

**2050 forecasts:**
- GeoVision 2019: 6 GW (BAU), 13 GW (IRT), 60 GW (TI).
- Enhanced Geothermal Shot / NREL 2023: 90 GW.
- Liftoff 2024: 90 GW base, 88-125 GW range, 130 GW (land-limited), 300 GW (flexible).
- Princeton: more than 100 GW in the western US.

**Costs:**
- Hydrothermal today: $61-102/MWh LCOE; PPAs $70-100/MWh.
- EGS: OCC $27.8k/kW (2021) → $14.7k/kW (2023) → target $4.7-5.0k/kW (2030). LCOE $60-70/MWh by 2030 and $45/MWh by 2035 (Shot target).
- Superhot: $20-35/MWh nth-of-a-kind (modelled).

**Risk economics of exploration (GeoVision/Liftoff):**
- About $4-6.6M per project to reach exploration-drilling results.
- 50% confirmation-well success.
- About 20% of projects miss the resource.
- 8-year hydrothermal timeline.
- About 6 percentage points of WACC penalty until confirmation.
- All of these are exactly the risk premium that a pre-proof rights buyer captures when it resolves the uncertainty.

## 3. Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **The value step-up is large, and DOE has measured it.** The government's own models charge geothermal about 6 percentage points of extra WACC, a 50% confirmation-well success rate and an 8-year timeline, all before resource confirmation. A right that moves from "prospect" to "confirmed resource" removes most of that. This is the same arbitrage Terranox runs in uranium: own the right while the market still prices the risk, then sell or develop once confirmation removes it. Today buyers pay $70-100/MWh for clean firm power, and Liftoff needs 2-5 GW of sites by 2030 and 10+ GW/yr later. Developers will need far more de-risked acreage than exists.

2. **Hidden hydrothermal is about 23-30 GW, and DOE's models give no credit for finding it faster.** GeoVision fixes the discovery rate at 1-3% of the undiscovered resource per year (about 200-600 MWe/yr) and explicitly refuses to credit exploration-technology gains. Any ML lift in discovery rate is therefore upside missing from the official forecasts. At roughly $4,000/kW installed, 25 GW of hidden hydrothermal is more than $100B of plant. This alone is not "too small".

3. **Zanskar's shape: a vertically integrated hydrothermal developer focused on blind systems.** Zanskar uses AI and physics to find blind hydrothermal systems (Big Blind, NV), then drills them, builds or buys plants (Lightning Dock, NM) and operates them. It competes for the same ~30 GW of undiscovered hydrothermal that Liftoff calls niche. Its capital goes into drilling and plants, so it can only hold a limited number of lease positions. (Details of Zanskar's portfolio are covered in other evidence files and are unverified here.)

4. **The gap: owning rights to "EGS-ready" and superhot land at national scale.** Liftoff, the Shot, USGS 2025 and the Princeton paper all put more than 90% of future GW in EGS: 135 GWe in the Great Basin alone, and about 5,500 GW nationally. EGS developers (Fervo, Mazama, Quaise, Sage and others) still need specific parcels. The parcel needs:
   - hot rock at reachable depth (200 °C+ at under 4-5 km);
   - favourable stress and lithology;
   - water;
   - transmission or a data-centre load nearby;
   - leasable rights: BLM competitive geothermal leases, state trust land, or private geothermal estates.

   The literature shows the screening data is public and illegible:
   - more than 400,000 oil and gas bottom-hole temperatures, already used by Aljubran and Horne;
   - USGS 3D temperature models;
   - state well archives.

   No source in this review describes a company systematically buying geothermal rights at scale on EGS-grade thermal anomalies ahead of EGS developers. That is a land-banking and royalty model, closer to Texas Pacific Land or a mineral-rights aggregator than to Zanskar's developer model. It is also hedged: if EGS costs fall as Liftoff projects (to $45/MWh), the rights rise in value without the company drilling a single EGS well. Sedimentary-basin EGS in oil and gas states (TX, ND, OK and others) falls outside Zanskar's Great Basin focus.

5. **A hybrid wedge.** Start with high-confidence hidden-hydrothermal targets. These give near-term cash, either from flips to Ormat, Fervo or utilities, or from small binary plants. At the same time, accumulate EGS-grade acreage cheaply while BLM lease sales still price it as "no known resource". Take overriding royalties when developers build on it. Policy tailwinds include the IRT-style permitting reforms and the categorical exclusions Liftoff calls for. These shorten the time from right to confirmed asset and raise the multiple on owned acreage.

6. **Risks the literature flags.** Liftoff warns that the 90+ GW build is "difficult" without a 10+ GW/yr ramp. If EGS stalls, EGS-land value depends on a technology bet; the hydrothermal sleeve offsets this. USGS stresses that its EGS numbers are provisional and highly uncertain: viable-geology uncertainty "could easily exceed 1,000 percent".

## Sources
- https://pubs.usgs.gov/fs/2008/3082/
- https://www.energy.gov/eere/geothermal/geovision
- https://www.energy.gov/eere/geothermal/articles/geovision-chapter-3
- https://apps.openei.org/geovision/executive-summary
- https://www.nrel.gov/docs/fy23osti/84822.pdf
- https://research-hub.nrel.gov/en/publications/enhanced-geothermal-shot-analysis-for-the-geothermal-technologies/
- https://www.energy.gov/node/4822595
- https://www.thinkgeoenergy.com/new-us-doe-earthshot-initiative-aims-to-reduce-egs-cost-by-90/
- https://cdn.catf.us/wp-content/uploads/2025/06/09154348/doe-liftoff-nextgen-geothermal.pdf
- https://www.thinkgeoenergy.com/us-doe-publishes-report-on-commercial-liftoff-of-next-generation-geothermal/
- https://www.rigzone.com/news/us_needs_as_much_as_250b_to_reach_2050_geothermal_potential_doe-25-mar-2024-176191-article/
- https://pubs.usgs.gov/publication/fs20253027
- https://pubs.usgs.gov/fs/2025/3027/fs20253027.pdf
- https://arxiv.org/pdf/2403.09961
- https://gdr.openei.org/submissions/1592
- https://doaj.org/article/1a381c8dbfd54ca2931d58ef0120d708
- https://ideas.repec.org/a/nat/natene/v10y2025i1d10.1038_s41560-023-01437-y.html
- https://engineering.princeton.edu/news/2024/02/16/flexible-geothermal-power-approach-combines-clean-energy-built-battery
- https://www.thinkgeoenergy.com/catf-publishes-comprehensive-study-on-superhot-rock-energy/
- https://www.catf.us/2025/01/introduction-next-clean-energy-frontier-superhot-rock-geothermal/
- https://atb.nrel.gov/electricity/2024/geothermal
- https://gdr.openei.org/files/756/Faulds-DE-EE0006731-Report-v2.pdf
- https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2017/Faulds.pdf
