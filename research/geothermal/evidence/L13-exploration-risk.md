# L13: Geothermal exploration risk, drilling success rates, costs, timelines and risk insurance

**Scope:** a literature review of how often geothermal exploration wells succeed, what exploration costs per well and per campaign, how long it takes to reach first MW, and how the risk is financed or insured. It ends with what this means for a "Terranox for geothermal" company (buy rights cheaply before proof, own the step-up).

**Method note:** the WebSearch budget for this run was used up before this agent began, so I collected sources by direct fetch of known primary URLs. Stanford's geothermal workshop server (pangea.stanford.edu) returned 503 or TLS errors and NREL's site was blocked by the proxy. As a result:
- I could not open IFC (2013), Sanyal & Morrow (2012) or Wall & Dobson (2016) directly.
- Their results below come from the detailed summaries in Lowry et al. (2017, Sandia) and DOE GeoVision (2019). Both are primary government reports that cite these studies.
- They are marked "(via Lowry 2017)" or "(via GeoVision)".

Everything else was read in full-text PDF.

---

## 1. Primary sources reviewed

### 1.1 IFC / World Bank (2013), *Success of Geothermal Wells: A Global Study* (via Lowry et al. 2017)
- **Dataset:** 2,613 wells, 57 fields, 14 countries, about 71% of global installed geothermal capacity.
- **Definition of success:** a production well whose final capacity is ≥3 MWe.
- **Overall success:** 78% of wells whose status could be confirmed.
- **Learning curve:**
  - First well in a field: **50%**.
  - First five wells (the "exploration phase"): **59%**.
  - Development phase: **74%**.
  - Operational phase: **83%**.
- **Geology:** fields in sedimentary basins had higher success rates than other settings.
- Original URL (now redirect-loops): https://www.ifc.org/wps/wcm/connect/7e5eb4804fe24994b118ff23ff966f85/ifc-drilling-success-report-final.pdf?MOD=AJPERES
- Summary source: https://www.osti.gov/servlets/purl/1394062 (pp. 33-34)

### 1.2 Sanyal, S.K. & Morrow, J.W. (2012), "Success and the Learning Curve Effect in Geothermal Well Drilling: A Worldwide Survey", 37th Stanford Geothermal Workshop (via Lowry 2017)
- **Dataset:** 2,528 wells, mostly the same data as IFC.
- **Success rate:** across 52 fields it is roughly normally distributed with a **mean of about 68%**.
- **Volatility:** in the exploration phase (first 5 wells) success "varies wildly". It stabilises only after about **40 wells**.
- **Learning effects:**
  - There is no continuous learning-curve effect on MW per well or on success rate.
  - In 19 liquid-dominated fields, well capacity shows *step changes* that track revisions to the conceptual model.
  - Rate of penetration (ROP) roughly doubles from exploration to operations at Kamojang.
- **Takeaway:** what drives success is *knowing where to drill*, which is the conceptual model, not drilling practice.
- Summary source: https://www.osti.gov/servlets/purl/1394062

### 1.3 Wall, A.M. & Dobson, P.F. (2016), "Refining the Definition of a Geothermal Exploration Success Rate", 41st Stanford Workshop, SGP-TR-209 (via GeoVision and Lowry)
- Wall & Dobson criticise the IFC and Sanyal metric (≥3 MWe production well). It measures well success *inside fields that were already developed*, which is survivorship bias.
- **Key result, as quoted by GeoVision:** exploration drilling results "led to drilling full-sized development wells **less than one-third of the time**."
- **So the project-level exploration success rate is below 33%**, not 50-59%. This is close to the roughly 33% exploration success rate in the oil industry cited by ESMAP (Tordo et al. 2010).
- Record: https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=26553
- Quoted in: https://www.energy.gov/sites/prod/files/2019/06/f63/GeoVision-full-report-opt.pdf (p. 37)

### 1.4 Gehringer, M. & Loksha, V. (2012), *Geothermal Handbook: Planning and Financing Power Generation*, ESMAP/World Bank TR002/12
Indicative costs for a 50 MW project (US$ million, low / medium / high):

| Phase | Low | Medium | High |
|---|---|---|---|
| Preliminary survey and permits | 1 | 2 | 5 |
| Exploration (surface geoscience) | 2 | 3 | 4 |
| **Test drilling (3-5 wells, slimhole to full size)** | **11** | **18** | **30** |
| Feasibility | 5 | 7 | 10 |
| Drilling (20 wells) | 45 | 70 | 100 |
| Plant | 65 | 75 | 95 |
| Gathering and grid | 10 | 16 | 22 |
| Start-up | 3 | 5 | 8 |
| **Total** | **142** | **196** | **274** |
| **Per MW** | **2.8** | **3.9** | **5.5** |

Other points from the handbook:
- Phases 1-2 (everything up to drilling) cost **$3-9M**. That is 2-3% of capex, and it is the "cheap" step.
- Test drilling is "up to 15% of overall capital cost" and comes "at a point when the risk of project failure is still high".
- **Per-well costs:**
  - **Slimhole: US$0.5-1.5M.**
  - **Full-size well: US$2-6M.**
  - Four full-size wells 2.5-3 km deep: $10-25M.
  - Slimholes can reach 1,500 m at about **50% of the cost** of a regular well of the same depth.
- Temperature-gradient holes are "shallow and slim boreholes, usually less than 500 m".
- An extra 0.5 km of depth adds more than $1M per well.
- **Timeline:** "5 to 10 years to complete", typically about **7 years** for a 50 MW first unit.
- **Benchmark:** global oil exploration success is about 33% (Tordo, Johnston & Johnston 2010).
- https://openknowledge.worldbank.org/handle/10986/23712

### 1.5 ESMAP / World Bank Group (2016), *Comparative Analysis of Approaches to Geothermal Resource Risk Mitigation: A Global Survey*
**Stage costs and timing:**

| Stage | Cost | Years |
|---|---|---|
| Surface reconnaissance | $1-2M | 1-2 |
| **Exploration drilling, a typical 3-5-well test campaign** | **$20-30M** | **2-3** |
| Production drilling | $20-120M | 4-6 |
| Plant | $20-200M | 6-8 |
| Operation | | 8+ |

**Insurance:**
- It is "limited" and has had "mixed" results.
- "Less than a handful of insurers worldwide" underwrite resource risk.
- At most "a few tens of megawatts" worldwide were catalysed by insurance.
- In the early 1980s a US insurer offered cover and **no developer applied** because premiums were too high.
- Germany's scheme worked mainly because of a feed-in tariff of about $0.30/kWh.
- **The binding constraint is portfolio scale and actuarial data.**

**Cost-sharing works better:**
- Japan paid up to 40% of exploration wells and 20% of production wells, which helped build most of its 536 MW.
- US cost-shared drilling confirmed about 150 MW, and **public disclosure of results was required**.
- The East Africa GRMF covers 40% of up to 2 exploration wells.
- Latin America's GDF covers 40% of up to 3 wells as a contingency grant. If a well succeeds, 80% of the grant is repaid.

https://openknowledge.worldbank.org/handle/10986/24277

### 1.6 US DOE (2019), *GeoVision: Harnessing the Heat Beneath Our Feet*
**Resource base:**
- 9 GWe of identified hydrothermal resources, of which about 3 GWe is developed.
- **30 GWe is undiscovered** (Williams et al. 2008, USGS) and is "the majority of the remaining conventional hydrothermal resource potential".
- Blind discoveries already developed include McGinness Hills and Don A. Campbell.

**Exploration share of cost:**
- "No existing exploration technologies... on their own" can deliver the needed gains in success rate.
- Exploration, confirmation and development drilling together are **30-50% of development cost** (Bromley et al. 2010).

**Model assumptions:**
- Discovery rate of undiscovered resources: **1%/yr in business-as-usual (BAU)**, 3%/yr with improved permitting.
- **Full-size confirmation-well success rate: 50%.**
- Confirmation wells cost 20-50% more than production wells.
- Drilling success rate: **75%** in BAU, 90% in the technology-improvement case.
- Geothermal WACC is set about **6 points above** wind and solar to reflect "high risks and equity financing requirements at the beginning of geothermal projects".
- Construction timeline: about 8 years for hydrothermal in BAU (from L06), 4 years with streamlined permitting.

https://www.energy.gov/sites/prod/files/2019/06/f63/GeoVision-full-report-opt.pdf

### 1.7 Wall, A.M., Dobson, P.F. & Thomas, H. (2017), "Geothermal Costs of Capital: Relating Market Valuation to Project Risk and Technology", GRC Transactions 41: 45-61
Literature-derived cost of capital by stage:

| Stage | Share of spend | Cost of capital, external financing |
|---|---|---|
| Exploration / feasibility | 12% | **35% cost of equity**, 100% equity |
| Drilling / well-field | 58% | 30% equity, 15% debt, 40:60 |
| Plant | 30% | 8% debt |
| **Project WACC** | | **19.4%** external, 14.0% internal |

- Under a separate valuation-based build (author table), exploration-stage cost of equity is 12.9-18.2% and falls to about 6-10% at plant stage.
- **Hudson Ranch (49 MW, Salton Sea):**
  - The developer first secured the leases.
  - The first two wells were financed by a **$15M** Glitnir loan.
  - Bank debt became available once wells showed about 75% of capacity "behind wellhead".
  - Total cost was $401.3M, with $101.1M of equity.
- **Takeaway:** the jump in valuation happens at confirmation by flow test, when the cost of capital falls from about 30-35% to about 5-8%.

https://publications.mygeoenergynow.org/grc/1033704.pdf

### 1.8 Young, K., Witherbee, K., Levine, A., Keller, A., Balu, J. & Bennett, M. (2014), "Geothermal Permitting and NEPA Timelines", GRC Transactions 38 (NREL)
**Federal land:** 90% of US geothermal resources are on federally managed land (BLM 2005).

**Median NEPA times:**

| Review type | Median time |
|---|---|
| CX / DNA | 1-2 months |
| EA | **10 months** |
| EIS | **25 months** |

**Other timing data:**
- GAO (2013) found Nevada geothermal permits took **1-4 years**.
- New York Canyon combined exploration and development into one EA, and permitting still took about 4 years.

**BLM leasing:**
- Since EPAct 2005, BLM leasing is all-competitive on public nominations.
- BLM must hold a sale at least every 2 years.
- After the programmatic EIS (PGEIS), **376 parcels were offered through November 2013, 267 of them in Nevada**. 295 were cleared via DNA.

**Industry ask:** a "major industry concern" is the time from nomination to sale. Industry wants leases pre-cleared for temperature-gradient hole (TGH) and slimhole drilling.

https://publications.mygeoenergynow.org/grc/1033639.pdf

### 1.9 Lowry, T.S., Finger, J.T. et al. (2017), *GeoVision Analysis Supporting Task Force Report: Reservoir Maintenance and Development*, Sandia SAND2017-9977
**Drilling costs:**
- Drilling is **50% or more of capex** (Tester et al. 2006).
- Geothermal wells cost **2-5 times** more than oil and gas wells of the same depth (Augustine et al. 2006).
- Probabilistic cost studies show variance of more than ±50%.

**Data scarcity:**
- There are **fewer than 1,000 geothermal wells on public land, against more than 100,000 oil and gas wells**.
- Geothermal well cost data are "usually proprietary".
- Rig-rate inflation after 2004 reset the cost baseline upward.

This report is also the source of the IFC and Sanyal summaries above.

https://www.osti.gov/servlets/purl/1394062

### 1.10 Supporting: DOE Play Fairway, Nevada (Faulds et al. 2021, OSTI 1724080), and Zanskar disclosures
**Play Fairway Nevada:**
- Covered about 96,000 km², with 24 areas ranked and 5 studied in detail.
- Phase 3 drilled 6 TG holes at each of 2 sites, about $1.5M in all (L01).
- Gabbs Valley reached **124 °C at 152 m** and Granite Springs about **96 °C at about 250 m**. Both were blind.
- https://www.osti.gov/biblio/1724080

**Zanskar:**
- **Big Blind:** two intermediate-depth wells (Jul-Aug 2025) found about 250 °F (121 °C) at about 2,700 ft. Capacity is unconfirmed. "Analogous systems" produce more than 100 MWe.
- **Model:** "develop, build, own, and operate".
- **Track record:** "three of three" successes on sites funded by its prior round.
- **Funding:** $115M Series C.
- **Pipeline:** at least 1 GW, with a target of at least 10 confirmed sites to attract project finance.
- Sources:
  - https://zanskargeothermal.substack.com/p/zanskar-reveals-big-blind-the-discovery
  - https://techcrunch.com/2026/01/21/zanskar-thinks-1-tw-of-geothermal-power-is-being-overlooked/
  - https://www.latitudemedia.com/news/armed-with-115-million-geothermal-startup-zanskar-gets-ready-to-build/

---

## 2. Synthesis: the numbers that matter

| Metric | Value | Source |
|---|---|---|
| First-well success (≥3 MWe, developed fields) | 50% | IFC 2013 |
| First-5-wells success | 59% | IFC 2013 |
| Development / operational well success | 74% / 83% | IFC 2013 |
| Mean field success rate | about 68%; stabilises after about 40 wells | Sanyal & Morrow 2012 |
| Exploration that leads to full-size development wells | <1/3 | Wall & Dobson 2016 |
| Full-size confirmation-well success, DOE model | 50% | GeoVision 2019 |
| Oil exploration benchmark | about 33% | ESMAP 2012 |
| Surface exploration cost | $1-2M (ESMAP 2016); $3-9M including permits (ESMAP 2012) | |
| Slimhole cost | $0.5-1.5M (2012 $) | ESMAP 2012 |
| Full-size well cost | $2-6M (2012 $), 2-5 times O&G | ESMAP 2012; Lowry 2017 |
| Test-drilling campaign (3-5 wells) | $11-30M / $20-30M | ESMAP 2012 / 2016 |
| Test drilling share of capex | up to 15% | ESMAP 2012 |
| Time to first MW | 5-10 yrs (about 7 typical; about 8 in DOE BAU) | ESMAP 2012; GeoVision |
| NEPA EA / EIS median | 10 / 25 months | Young 2014 |
| Cost of equity at exploration | about 30-35% external | Wall et al. 2017 |
| Project WACC | 19.4% external | Wall et al. 2017 |
| Undiscovered US hydrothermal | 30 GWe; discovered at about 1%/yr | USGS 2008 via GeoVision |
| Resource-risk insurance catalysed globally | a few tens of MW; fewer than 5 insurers | ESMAP 2016 |

Today's well costs are probably higher in nominal terms than the 2012 figures; a 2025 full-size well is plausibly $5-10M (unverified).

### Three takeaways
1. **The risk is concentrated, and it is front-loaded:**
   - Surface work is cheap, at $1-9M.
   - The first 3-5 wells cost $11-30M with roughly 50% per-well odds and below 33% project-level odds.
   - Everything after that, which is 85%+ of capex, is financed at 5-8%.
   - The value step-up therefore sits *exactly* at the confirmation well.
2. **The market will not insure the step.** Insurance has failed for 40 years for lack of portfolio scale and actuarial data. Government cost-share works but usually requires public disclosure. The financing gap at the exploration stage is structural, and equity at 30-35% fills it.
3. **Success depends on targeting, not on drilling learning.** Sanyal & Morrow find step changes driven by revisions to the conceptual model. That is the lever ML and data integration act on. Even a modest gain matters: raising first-well success from 50% to 70% (unverified, plausibility only) cuts the expected cost per discovery by about 30%.

---

## 3. Implications for a Terranox-shape geothermal company and the gap vs Zanskar

**1. The Terranox analogue works because exploration risk is priced at 30-35% equity and the cheap rungs are really cheap.**
- A lease is worth hundreds to about $1,200/acre at competitive sale (state sales, L01). A TG-hole programme costs a few hundred thousand dollars per site (PFA: about $1.5M for 2 sites and 12 holes).
- A confirmed resource, however, carries project-finance WACC, and the downstream value is $140-270M+ of capex per 50 MW.
- A company that owns many rights and climbs only the cheap rungs (data → lease → TG/slimhole) holds options on the most mispriced step in the energy value chain.

**2. Which proven state you sell sets the size of the step-up.**
- Bankers want flow-tested full-size wells ("75% behind wellhead", Hudson Ranch).
- A TG-confirmed blind anomaly is worth much less than a flow-tested reservoir. Still, it is far more than raw acreage, because buyers' alternative is a sub-33% project hit rate.
- The plausible model:
  - Sell or joint-venture at the TG/slimhole stage to Ormat, Fervo or utilities, keeping a carried interest or royalty.
  - Self-fund one confirmation well ($5-10M, unverified) on the best 10-20% of prospects to capture the full step.

**3. A portfolio is the moat and the insurance.**
- ESMAP finds resource insurance failed because no one had a large enough portfolio or actuarial data.
- A landholder with 100+ prospects and its own TG/slimhole dataset becomes the de facto actuary.
- It can:
  - diversify the 50% per-well risk;
  - price prospects for buyers;
  - potentially wrap or warrant prospects (a novel product, unverified demand).
- Sanyal's finding that success stabilises only after about 40 wells argues for scale across many prospects rather than concentration.

**4. Data asymmetry is real.**
- There are fewer than 1,000 geothermal wells on public land against more than 100,000 oil and gas wells, and geothermal cost and well data are proprietary.
- The large public dataset is O&G bottom-hole temperatures (BHTs) plus TG holes and mineral holes.
- That is the Saskatchewan-assessment-file analogue, and it is under-used.
- US cost-share drilling also required public disclosure, so legacy DOE-funded results exist in archives.

**5. Timing and permits are a lever for an owner.**
- BLM sales are held at least every 2 years, on public nominations.
- An EA takes about 10 months and an EIS about 25 months, and lease-to-power takes 5-10 years.
- Every year of permitting compressed is worth money to a buyer. A rights company that pre-permits TGH and slimhole work under combined EAs sells a faster asset.
- **Risk:** competitive nominations reveal interest. Private and state rights (L01) avoid public disclosure.

**6. The gap vs Zanskar:**
- Zanskar is vertically integrated ("develop, build, own, and operate"). It has a $115M Series C, aims for at least 10 confirmed sites and is building plants.
- Its capital therefore goes to the expensive, low-ROIC rungs: $20-30M test campaigns and $140M+ plants per site.
- It cannot economically hold or advance hundreds of marginal or mid-size prospects. It also publicises discoveries (Big Blind), which raises adjacent lease prices.
- The **gap** is a capital-light **prospect-generator and landholder** across the West:
  - acquire hundreds of BLM, state and private rights ahead of the market;
  - TG-test them cheaply;
  - sell or JV the de-risked state to developers, including Zanskar itself, Fervo, Ormat, utilities and data-centre offtakers, while keeping royalties.
- This is the classic mining "prospect generator" model (unverified as a geothermal precedent) applied to the step where IFC, Wall & Dobson and ESMAP agree the risk premium is largest.
- **Main risks:**
  - Buyers may pay little before a full-size flow test.
  - BLM competitive sales cap how cheaply rights can be bought.
  - Zanskar or Fervo could add a lease-flipping arm.

**Score note:** the shape owns the asset, and the market is large (30 GWe undiscovered at 1%/yr discovery, with 10x upside per Zanskar). The ML lift is plausible because targeting, not drilling skill, drives success. The idea passes the standing rules.

---

## Sources
- IFC (2013) Success of Geothermal Wells: A Global Study: https://www.ifc.org/wps/wcm/connect/7e5eb4804fe24994b118ff23ff966f85/ifc-drilling-success-report-final.pdf?MOD=AJPERES (redirect loop; read via Lowry 2017)
- Lowry et al. (2017) SAND2017-9977: https://www.osti.gov/servlets/purl/1394062
- Sanyal & Morrow (2012), Stanford SGW 37 (read via Lowry 2017): https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2012/Sanyal1.pdf (not reachable this run)
- Wall & Dobson (2016), Stanford SGW 41: https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=26553
- DOE GeoVision (2019): https://www.energy.gov/sites/prod/files/2019/06/f63/GeoVision-full-report-opt.pdf
- Gehringer & Loksha (2012) ESMAP Geothermal Handbook: https://openknowledge.worldbank.org/handle/10986/23712
- ESMAP (2016) Comparative Analysis of Approaches to Geothermal Resource Risk Mitigation: https://openknowledge.worldbank.org/handle/10986/24277
- Wall, Dobson & Thomas (2017) GRC Trans 41: https://publications.mygeoenergynow.org/grc/1033704.pdf
- Young et al. (2014) GRC Trans 38: https://publications.mygeoenergynow.org/grc/1033639.pdf
- Faulds et al. (2021) Nevada Play Fairway, OSTI 1724080: https://www.osti.gov/biblio/1724080
- Zanskar Big Blind: https://zanskargeothermal.substack.com/p/zanskar-reveals-big-blind-the-discovery
- TechCrunch (2026) Zanskar: https://techcrunch.com/2026/01/21/zanskar-thinks-1-tw-of-geothermal-power-is-being-overlooked/
- Latitude Media, Zanskar $115M: https://www.latitudemedia.com/news/armed-with-115-million-geothermal-startup-zanskar-gets-ready-to-build/
