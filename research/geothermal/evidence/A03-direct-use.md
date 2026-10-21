# A03: Geothermal direct use, district heating, industrial heat, data-centre cooling and thermal storage

**Question.** Is there a large lower-temperature geothermal market (heat rather than power) where a Terranox-shape land and data company could acquire and own resources cheaply before they are proven?

**Method note.** The shared WebSearch budget for this run (200 calls per turn) was used up before this agent's first query, so no searches ran. Everything below comes from direct WebFetch of primary or trade pages I could name in advance: DOE, the OSTI API, EGEC, ThinkGeoEnergy articles (which quote BRGM, SWM and Innargi) and Cornell. Where a number is from memory and could not be fetched, it is marked **(unverified)**. Several primary PDFs failed to load: the GeoVision full report and the NLR 2025 Market Report were over 10 MB, IEA returned 403, and Lund and Tóth 2021 is paywalled.

---

## 1. How big is direct use?

### 1.1 Global
- **Lund and Tóth (2021), "Direct utilization of geothermal energy 2020 worldwide review", *Geothermics* 90:101915** (DOI 10.1016/j.geothermics.2020.101915; bibliographic details checked on OpenAlex). It is the canonical WGC census. From memory **(unverified; abstract not retrievable)**:
  - about **107.7 GWth** installed and about **1,020,887 TJ/yr (about 283 TWh-th/yr)** in 88 countries;
  - geothermal heat pumps (GHPs) make up about 58% of capacity and about 59% of energy;
  - the remainder is bathing and swimming, space and district heating, greenhouses, aquaculture, industrial use and agricultural drying.
- Older series, as summarised by Wikipedia from Lund (2007): **28 GW and 273 PJ/yr in 2005**. That implies roughly 4x growth in 15 years, driven mostly by GHPs and China. (https://en.wikipedia.org/wiki/Geothermal_heating)
- **Industrial heat demand** (IEA 2017, via ThinkGeoEnergy): "three-quarters of the energy used in industry is process heat." About **30% of that is below 150 °C** and **22% is 150–400 °C** (https://www.thinkgeoenergy.com/geothermal-and-industrial-heat-demand-new-iea-report-on-the-role-of-heat/). The sub-150 °C band is in principle addressable by sedimentary geothermal.

### 1.2 Europe: the real direct-use market
- **EGEC Market Report 2025** (published July 2026; https://www.egec.org/media-publications/egec-market-report-2025/):
  - **434 geothermal district heating and cooling (GeoDHC) systems** operate, with **more than 6 GWth** installed;
  - **10 new systems (70 MWth) were added in 2025**: France 3, Germany 2, Netherlands 2, Denmark 1, Serbia 1, Spain 1;
  - **more than 500 projects are under development, which could add about 6 GWth**, roughly doubling the fleet;
  - for comparison, Europe has 150 geothermal power plants totalling more than 3.5 GWe.
- **EGEC heat-pump report** (October 2026): about **123k ground-source units were sold in the EU in 2025 (+10%)**. The fleet is more than **2.5M units, 39.2 GWth and about 88 TWh/yr** (https://www.egec.org/resource-type/geothermal-market-report/).
- **EU policy pull** (EGEC, citing the Commission's Electrification Action Plan):
  - district heating and cooling networks should grow **6–7% per year to 2030** and supply **15% of EU heating and cooling**;
  - geothermal could supply "up to 25%" of heating and cooling demand (https://www.egec.org/).

### 1.3 Anchor European projects (asset-scale numbers)

| Project | Size | Capex / notes | Source |
|---|---|---|---|
| **Munich (SWM)** | Expanding to **400–450 MWth by the early 2030s**, about one quarter of Munich district heat. It goes from 1 to 3 doublets at each of Kirchstockach, Dürrnhaar and Sauerlach, plus Grünwald and Pullach | **About €1bn** | https://www.thinkgeoenergy.com/swm-to-invest-eur-1-billion-for-munich-geothermal-expansion/ |
| Munich 2040 plan | CO₂-neutral heat by 2040 "primarily with geothermal": **10 projects and more than 50 new deep wells**. The network grows from about 1,000 km to about 1,600 km. The total heat-transition plan is **about €9.5bn** | Gas heating ban expected from 2045 | https://www.thinkgeoenergy.com/munich-germany-aims-for-co2-neutral-heating-by-2040-primarily-with-geothermal/ |
| **Aarhus (Innargi, A.P. Møller-backed, with the utility Kredsløb)** | **110 MWth**, about **20% of Aarhus heat demand**, full operation by 2029. The reservoir is at about 2.5 km. Three test wells led to **3 plant sites instead of 7**. The first plant (Skejby) started in October 2025 | Innargi takes subsurface risk and sells heat at a "stable price for 30 years" | https://www.thinkgeoenergy.com/innargi-to-deliver-target-geothermal-heating-capacity-in-aarhus-denmark-with-fewer-plants/ ; https://www.thinkgeoenergy.com/geothermal-district-heating-in-aarhus-denmark-officially-starts-operations/ ; https://innargi.com/ |
| **Paris Basin (Île-de-France)** | **54 active deep installations**, the largest cluster in Europe, producing **about 1.97 TWh-th from the Dogger in 2025** at 50–80 °C | Dogger wells cost about **€5M each** and Triassic wells about **€9M**. The Genyo network (20k homes) cost **€78M**, of which about €17M came from ADEME | https://www.thinkgeoenergy.com/geoscan-project-expands-extent-of-known-geothermal-potential-in-ile-de-france-region-france/ ; https://www.thinkgeoenergy.com/geothermal-greater-paris-area-making-better-and-better-use-of-enormous-potential/ |
| **Maasdijk (Westland, Netherlands)** | **50 MWth** in 3 doublets, serving 24 horticulture firms (the equivalent of 54k households) | A heat cooperative plus HVC | https://www.thinkgeoenergy.com/maasdijk-netherlands-geothermal-greenhouse-project-celebrates-start-of-operations/ |
| Unterhaching (Germany) | 38 MWth, Kalina cycle, district heat | | https://en.wikipedia.org/wiki/Geothermal_energy_in_Germany |
| Reykjavík | 830 MWth peak, 230k residents | | https://en.wikipedia.org/wiki/District_heating |

**Data-led exploration is already state-run in Europe.** France's BRGM **GEOSCAN** programme (November 2023 to 2025) acquired 280 km of new geophysics. It reinterpreted **1,660 km of legacy 2D seismic and about 80 oil and geothermal wells** over about 2,000 km² and about 300 municipalities, and found three previously unexplored **Triassic** reservoirs (Donnemarie, Chaunoy, Boissy) and the Oxfordian aquifer (40–65 °C). In other words, **the "reprocess old oil-and-gas data to find hidden heat" step is a public good in France**, not a private edge. The Netherlands does the same through TNO's ThermoGIS/SCAN (see D09). Munich is running a large 3D seismic campaign itself ("Seismik GIGA-M", €44M in federal funding).

### 1.4 United States: small direct use, large ambient and heat-pump market
- **GeoVision (DOE 2019)** (https://www.energy.gov/eere/geothermal/geovision):
  - economic potential of **17,500 geothermal district heating systems**;
  - GHP market potential equivalent to **28 million households**.
  - The underlying dGeo model is McCabe, Beckers, Young and Blair (2019), OSTI 1570964.
- **Simpson et al. (NLR, 2026, *iScience*), OSTI 17116347**: with high incentives, the dGeo update projects **GHP adoption of 251 GWth by 2050** and **thermal energy networks (TENs) of 31 GWth by 2050**, concentrated in dense areas. Uncertainty in cost structure produces "large variations" in adoption.
- **Deep direct use in the US is small and sub-economic at the margin.**
  - The NREL Tuttle, OK school district study (Akar et al. 2023, OSTI 2221828) found a 90.5 °C reservoir at 3.3 km serving 2 schools and 250 houses.
  - That system needs only about 2.6 GWh-th/yr of heating, and its **LCOH is $95–210/MWh-th**, which is well above US natural-gas heat at roughly $15–40/MWh-th **(unverified)**.
  - Beckers et al. 2021 (*Energy Conversion and Management* 243:114335) evaluated US deep direct-use feasibility. I could not retrieve its abstract.
- **Legacy US systems.** Boise (since 1892) is "one of the oldest and largest" in the world and serves downtown and Boise State University (https://www.cityofboise.org/departments/public-works/geothermal/). Klamath Falls dates from 1900. The NREL 2021 market report counted about **23 operating US geothermal district heating systems totalling roughly 75–100 MWth** **(unverified)**.
- **Campuses.** Cornell's **Earth Source Heat** drilled the **CUBO well to about 3 km (almost 10,000 ft)** in 2022. It found temperatures that "strongly match" the district system but **low permeability**, so an EGS-style stimulated system is needed. Cornell is now **seeking cost-sharing partners** before a go/no-go on Phase II (https://sustainable.cornell.edu/buildings-energy/earth-source-heat ; Tester et al. 2025, OSTI 3021474). Most US campus "geothermal" (Colorado Mesa, Ball State, Weber and others) is **shallow GHP borefields**, which involve no scarce subsurface right **(unverified per campus)**.
- **DOE Community Geothermal Heating and Cooling** narrowed 11 projects to 3: Ann Arbor MI, Framingham MA (HEET) and Shawnee OK (University of Oklahoma). All are thermal-network or GHP projects (https://www.energy.gov/eere/geothermal/community-geothermal-heating-and-cooling-design-and-deployment).

## 2. Data-centre cooling and thermal storage
- **Cooling.** Geothermal "cooling" for data centres is almost entirely **ground or aquifer heat rejection** (GHP, ATES or closed loops), not hot-resource extraction.
  - **Strataphy** (Saudi Arabia) raised a **$6M seed** and sells **cooling-as-a-service**, claiming up to 50% savings on cooling electricity; Baker Hughes is its preferred supplier (https://www.thinkgeoenergy.com/strataphy-and-baker-hughes-partner-for-geothermal-cooling-deployment-in-saudi-arabia/).
  - Others include PrimeLoop (2026 webinar), Dig Energy (Boston) and Earths Energy (Australia).
  - Hot-resource absorption chilling exists but is niche.
  - The scarce input here is the **power site plus water**, not a geothermal right. NLR/TP-6A40-95722 cites underground thermal storage for data-centre cooling (OSTI 3377911; see L23).
- **Thermal storage (HT-ATES).** Dobson et al. 2025, *Energies* 18:6292 (OSTI 3017397):
  - **more than 2,800 ATES systems** exist worldwide, mostly **below 25 °C**, and few exceed 40 °C;
  - the review covers 10 HT-ATES projects (4 in Germany, 6 in the Netherlands) and documents poor thermal recovery, scaling, heterogeneity, unclear regulation and financing problems.
  - HT-ATES does reward subsurface characterisation, which is a data edge. But the aquifer is not a scarce, auctioned right in most jurisdictions.
  - Fairbanks, AK district heating with underground thermal storage was modelled by Wagner et al. 2026 (OSTI 17116336).
- **Industrial heat.** The players are an early pilot JV between **GA Drilling and Heatlinq** (Netherlands, 2026), Kawerau NZ (process steam for pulp and paper) and Rittershoffen in France (industrial steam for Roquette). The model is bespoke and tied to one offtaker.

## 3. Economics of heat assets versus power assets
- **Heat cannot travel.**
  - Every heat asset is tied to one network or plant within roughly 10–30 km **(unverified rule of thumb)**, so it has one buyer, a local monopsony (D09).
  - A power right in Nevada can sell into the CAISO/NV Energy grid, a data centre or a utility, so it has a competitive buyer pool.
- **Value density.** The value of a heat asset is real but modest.
  - Munich spends about **€1bn for about 400 MWth**, roughly €2.2–2.5M per MWth of capex, against about 25% of a city's heat.
  - Aarhus's 110 MWth serves about 20% of a city of 330k homes.
  - At about €50/MWh-th and a 50% capacity factor **(unverified)**, a 100 MWth asset grosses about €22M/yr. That is comparable to a **~20–25 MWe** power plant at $90/MWh.
- **Where the value goes.** Capex runs to hundreds of millions of euros, but most of it is wells and network. The **resource right itself is cheap and given out by permit**, so there is little step-up in owning the ground.
- **Subsidy and tender dependence.** Paris projects take about 20% of capex from ADEME, and the Netherlands relies on SDE++. Awards are discretionary, operator-tested and competitive (D09, R12), which is the opposite of first-come cheap staking.
- **The resource is often already mapped.** The Dogger, the Molasse and Dutch Rotliegend aquifers are public knowledge. The incremental discoveries (GEOSCAN's Triassic, the North German Basin) come from state seismic and well reprocessing.
- **Closed-loop pressure on heat-only rights.** L18 finds closed-loop heat at 30 °C/km can reach LCOH of $4–30/MWh almost anywhere. That erodes the scarcity of heat-only parcels.

## 4. Where a land and data company could still own something
1. **Germany, North German Basin and other areas outside the Upper Rhine Graben (URG) and Molasse.**
   - Exploration permits (Erlaubnis) are first-come and cheap. The production right (Bergwerkseigentum) is transferable and can be mortgaged (D09).
   - The heat-planning law (Wärmeplanungsgesetz) forces every municipality to produce a heat plan, which creates many Stadtwerk buyers.
   - The Geothermie-Beschleunigungsgesetz (2025) declares geothermal an overriding public interest **(unverified detail)**.
   - Lithium is a co-product. Vulcan's Lionheart project shows claim-first behaviour (560 GWh/yr of heat plus LiOH).
   - This is the one place where "stake the field, prove it with old O&G well data, sell to the Stadtwerk or an Innargi-type operator" fits the Terranox mechanic.
2. **Heat optionality on US power parcels.** Any 90–150 °C sedimentary or hydrothermal parcel near a town, greenhouse cluster, food processor or data-centre campus carries a second exit. That raises the floor value of rights that fail as power.
3. **Not ownable.** These have no scarce right: US campus GHP borefields, data-centre cooling loops and TENs. They are service or tool businesses, which the scoring rules rate low.

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar
- **Direct use is large in aggregate but weak as a land-banking market.** Europe has 434 systems, more than 6 GWth installed and about 6 GWth more in 500+ projects. Munich (€1bn for 400–450 MWth) and Aarhus (110 MWth) show bankable city-scale demand.
- **Each heat asset has one local buyer, the resource is often state-mapped, and rights are awarded by discretionary permit.** So the "buy the right cheap before proof, own the step-up" mechanic is diluted. Most of the value goes to whoever owns the wells and the 30-year heat contract (the Innargi model), which is developer capital, not land.
- **As a primary wedge, US direct use fails "too small".** It has about 20-odd legacy systems, and deep direct-use LCOH of $95–210/MWh-th is uncompetitive with gas. The large US numbers (17,500 GDH systems of potential, 251 GWth of GHP by 2050) are mostly **shallow heat pumps and networks with no scarce right to own**. That is a services shape, and it scores low.
- **Data-centre cooling and HT-ATES are tool or service plays** (Strataphy is cooling-as-a-service on a $6M seed). The data edge is real, but there is no ownable scarce asset.
- **Best use for a Terranox-shape company: an add-on, not the thesis.**
  - (a) Price heat optionality into every sedimentary or mid-temperature right it acquires, as a second buyer class (Stadtwerke, greenhouses, food processors, data-centre campuses) that raises the floor value of rights that fail as power.
  - (b) Treat **Germany** (first-come Erlaubnis, transferable Bergwerkseigentum, mandated municipal heat plans, lithium co-product, legacy O&G BHT data entering public registers) as the second market after US BLM, state and private power rights.
  - (c) Reuse the same BHT-correction and temperature-at-depth models that the power thesis needs. The Dutch NLOG data is a free training set.
- **Gap vs Zanskar.**
  - Zanskar is a US Great Basin, hydrothermal-power, develop-and-operate company: Lightning Dock (NM) purchased from Cyrq in May 2024, the Big Blind discovery, a 100 MW NV Energy PPA and about $180M of equity.
  - It does nothing visible in heat, Europe or sedimentary direct use.
  - That is an open gap, but a **lower-value** one. The more important gap is still the business model: a **portfolio rights-holder that sells or JVs proven rights** across power *and* heat buyers, rather than a capital-hungry developer that must build every MW it finds.
- **Scoring.** As a standalone "Terranox for geothermal heat", it scores low to medium (local monopsony, permit-based rights, state-mapped resources). As an option layer and a Germany expansion on a power-rights portfolio, it scores positive.

## Sources
- https://www.energy.gov/eere/geothermal/geovision
- https://www.egec.org/media-publications/egec-market-report-2025/
- https://www.egec.org/resource-type/geothermal-market-report/
- https://www.egec.org/
- https://api.openalex.org/works/doi:10.1016/j.geothermics.2020.101915 (Lund and Tóth 2021, bibliographic details only)
- https://www.thinkgeoenergy.com/swm-to-invest-eur-1-billion-for-munich-geothermal-expansion/
- https://www.thinkgeoenergy.com/munich-germany-aims-for-co2-neutral-heating-by-2040-primarily-with-geothermal/
- https://www.thinkgeoenergy.com/innargi-to-deliver-target-geothermal-heating-capacity-in-aarhus-denmark-with-fewer-plants/
- https://www.thinkgeoenergy.com/geothermal-district-heating-in-aarhus-denmark-officially-starts-operations/
- https://innargi.com/
- https://www.thinkgeoenergy.com/geoscan-project-expands-extent-of-known-geothermal-potential-in-ile-de-france-region-france/
- https://www.thinkgeoenergy.com/geothermal-greater-paris-area-making-better-and-better-use-of-enormous-potential/
- https://www.thinkgeoenergy.com/maasdijk-netherlands-geothermal-greenhouse-project-celebrates-start-of-operations/
- https://www.thinkgeoenergy.com/ga-drilling-heatlinq-form-joint-venture-for-industrial-heat/
- https://www.thinkgeoenergy.com/geothermal-and-industrial-heat-demand-new-iea-report-on-the-role-of-heat/
- https://www.thinkgeoenergy.com/strataphy-and-baker-hughes-partner-for-geothermal-cooling-deployment-in-saudi-arabia/
- https://www.thinkgeoenergy.com/zanskar-acquires-lightning-dock-geothermal-power-plant-new-mexico/
- https://www.osti.gov/api/v1/records/17116347 (Simpson et al. 2026, GHP/TEN dGeo)
- https://www.osti.gov/api/v1/records/3017397 (Dobson et al. 2025, HT-ATES review)
- https://www.osti.gov/biblio/2221828 (Akar et al. 2023, Tuttle OK LCOH)
- https://www.osti.gov/biblio/1813622 (Beckers et al. 2021, deep direct use)
- https://www.osti.gov/biblio/1570964 (McCabe et al. 2019, GDH potential)
- https://www.osti.gov/biblio/3014949 (NLR 2025 US Geothermal Market Report)
- https://sustainable.cornell.edu/buildings-energy/earth-source-heat
- https://www.cityofboise.org/departments/public-works/geothermal/
- https://www.energy.gov/eere/geothermal/community-geothermal-heating-and-cooling-design-and-deployment
- https://en.wikipedia.org/wiki/Geothermal_heating (secondary)
- https://en.wikipedia.org/wiki/District_heating (secondary)
- https://en.wikipedia.org/wiki/Geothermal_energy_in_Germany (secondary)
