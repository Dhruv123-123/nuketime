# L23: Geothermal for data centres and large offtakers. Who buys, at what price, and how much firm clean power the West needs

**Method note.** The shared WebSearch budget for this run was used up before this agent's first query, so no searches ran. All sources below were fetched directly by URL or through the OSTI.gov and OpenAlex bibliographic APIs, and the full-text PDFs were read with pdftotext.

The anchor document is the **NLR (ex-NREL) 2025 U.S. Geothermal Market Report**. Its Table 3 is the best public compilation of geothermal PPAs from 2021 to July 2025, and it is cross-checked here against company releases, the Fervo S-1 and two LBNL tariff reviews.

Some figures come from sibling evidence files in this repo (L06, L07, 02-data-center-power.md). They are labelled with that file name. Anything recalled from memory is marked (unverified).

---

## 1. Primary sources reviewed

### 1.1 Akindipe, Martinez Smith, Witter, Pauling, Oh, … Levine, Schmidt, Pedersen (NLR / Geothermal Rising), 2026. *NLR 2025 U.S. Geothermal Market Report*, NLR/TP-5700-91898, OSTI 3014949

**Offtake volume**
- 26 geothermal PPAs were signed between the 2021 report and June 2025, totalling **1,642 MWe** of new capacity commitments.
- **Next-generation (EGS or closed-loop) geothermal accounts for 60% of PPAs.** Utilities have procured or agreed to procure **984 MWe** of next-generation capacity through 11 PPAs:
  - CA 439 MWe
  - NV 135 MWe
  - NM 150 MWe
  - TX 110 MWe
  - "east of the Rockies" 150 MWe (the Meta-Sage deal)

**Data-centre deals in Table 3** (all marked "energy supply or project development agreement, not within the classic definition of a PPA", with prices undisclosed)

| Buyer | Developer | Size | State | Year | Term |
|---|---|---|---|---|---|
| Google | Fervo, Blue Mountain | 3.5 MW | NV | 2022 | 12 yr |
| Google, via NV Energy | Fervo | 115 MW | NV | 2024 | listed as "6 yr" |
| Meta | Sage | 150 MW | TBD | 2024 | — |
| Meta | XGS | 150 MW | NM | 2025 | — |

**Disclosed prices** (most PPAs are "Undisclosed")
- SMUD–Calpine Geysers: **$99/MWh**, 100 MW, 10 years (2022).
- Port of Oakland–Calpine: **$70/MWh**, 2 MW (2023).
- The report gives the Table 3 PPA range as **$70–99/MWh**.
- Ormat was "negotiating **$100/MWh** (200 MWe) portfolio PPAs" in 2024 and expected prices to rise further.

**LCOE**
- Conventional hydrothermal LCOE has been flat: **$63–74/MWh flash** and **$90–110/MWh binary** (ATB 2024).
- The report calls these "investable" against PPA prices.
- EGS LCOE is falling toward flash levels within about 10 years (ATB Moderate). The Enhanced Geothermal Shot target is $45/MWh by 2035.

**California procurement**
- The CPUC's 2021 mid-term reliability order requires **≥1 GWe of firm, high-capacity-factor resources by 2026**. It credits imports from NV and UT, and has produced **≥616 MWe** of geothermal PPAs.
- The CPUC's August 2024 decision has DWR centrally procure an **additional ~1 GWe of long-lead geothermal for delivery 2031–2037**.

**Other findings**
- Next-generation developers have raised **>$1.5B** of private capital since 2021.
- The report cites LBNL: data centres rise from **4.4% of US electricity in 2023 to 6.7–12% in 2028**.

URL: https://www.osti.gov/biblio/3014949 (full text: https://www.osti.gov/servlets/purl/3014949)

### 1.2 Fervo Energy Co., 2026. *Form S-1* (SEC EDGAR)

**Contracted offtake**
- **658 MW of binding PPAs** with investment-grade buyers (SCE, Shell, Clean Power Alliance, Desert Community Energy), with about 15 years of remaining term.
- Potential revenue backlog of about **$7.2B**. Prices are described only as "attractive".

**Google**
- Google appears as a "tier-one partner" (with NV Energy).
- A **3 GW Google Geothermal Framework Agreement** was signed on 19 March 2026. The S-1 is internally inconsistent on whether it is binding; treat it as non-binding.

**Pricing benchmark**
- The S-1 cites Rystad for clean-firm market pricing of **$100–130/MWh**.

**Cape Station**
- 500 MW under construction in two phases: first power in late 2026 and about 100 MW by early 2027.
- A further 1.5 GW is permitted, giving about 4.3 GW of total potential.

**Market need**
- The S-1 cites Rystad for a projected **~98 GW US accredited-capacity shortfall by 2035**.

Sibling file L07 reports Fervo PPAs above 1 GW by October 2026.

URL: https://www.sec.gov/Archives/edgar/data/1853868/000162828026025821/fervoenergy-sx1.htm

### 1.3 Kahrl, Frick et al. (LBNL), 2026. *Speed to Power: Solutions for Accelerating Large Load Connections*, OSTI 3367528

This report gives the cleanest primary description of the **NV Energy Clean Transition Tariff (CTT)**:
- It is open to customers with **≥5 MW average hourly load**.
- The supply contract runs for the **lifetime of the generating facility**.
- **The customer pays any premium** above NVE's average expected supply cost and **owns the clean-energy credits**.
- Native customers are held harmless; the report calls it "effectively a wholesale contract with a retail provider".
- The first CTT project is "NVE's **115 MW advanced geothermal contract with Fervo on behalf of Google**."

URL: https://www.osti.gov/biblio/3367528

### 1.4 Frick, Cappers, Kalvak, Lam, Hledik (LBNL / Brattle), 2026. *Electricity Rate Designs for Large Loads: 2026 Update*, OSTI 3409217

How the CTT is built:
- **NV Energy holds the PPA with the developer**, and the customer pays the full resource cost through an Energy Supply Agreement (ESA).
- A hold-harmless "**Annual Capacity Protection Cost**" stops the customer's all-in rate falling below the standard bundled rate.
- The **exit fee** equals the remaining contracted kWh × (contract rate − the levelized cost of NVE's latest approved renewables).

The report lists the CTT among *approved* large-load tariffs alongside a dozen utility analogues (Dominion Schedule CFG, Duke GSA, Evergy CER, Ameren). This matters because **the template is spreading: a hyperscaler can pay a green premium for a specific new geothermal asset inside a vertically integrated utility.**

URL: https://www.osti.gov/biblio/3409217 ; https://escholarship.org/uc/item/9n09r4d6

Latitude Media (15 May 2025) reports that **PUCN approved the CTT the week of 15 May 2025**. At that date the ESA and the Fervo–NVE PPA still needed approval, interconnection was the bottleneck, and Corsac Station could be "doubled or tripled". https://www.latitudemedia.com/news/the-clean-transition-tariff-won-approval-in-nevada-whats-next-for-fervo/

### 1.5 King, Ricks, Pastorek, Larsen (Rhodium Group), 11 March 2025. *The Potential for Geothermal Energy to Meet Growing Data Center Electricity Demand*

**Demand**
- Data centres used about 2% of US electricity in 2020 and about 4.5% in 2024.
- In Rhodium's high case, data-centre peak demand reaches **~80 GW by 2030**, of which ~27 GW of growth is hyperscale.

**Geothermal's share**
- Under clustered siting, behind-the-meter next-generation geothermal could serve **55–64% of hyperscale growth (15–17 GW)**.
- If data centres site *to* the geothermal resource instead, it could meet **all** projected growth in the early 2030s, at costs **31–45% lower**.

**Cost**
- National weighted LCOE is **$78–85/MWh** in the baseline with a 20% green premium.
- Regional averages range from **$49 to $111/MWh**.
- With a 0% premium, deployment falls 38–55%.

**Where**
- Top states: CA, CO, NM, NV and OR.
- Of 28 markets with ≥100 MW of growth, geothermal can meet ≥15% of need in 20.

URL: https://rhg.com/research/geothermal-data-center-electricity-demand/

### 1.6 Ricks, Voller, Galban, Norbeck, Jenkins, 2024/2025. "The role of flexible geothermal power in decarbonized electricity systems", *Nature Energy* 10(1):28–40, doi:10.1038/s41560-023-01437-y

Bibliographic details were verified via OpenAlex. The numbers come from sibling file L06, which read the paper:
- Flexible EGS with in-reservoir storage reaches **59–93% round-trip efficiency**.
- Combined with lower drilling costs, it supports **>100 GW of EGS in the western US**.
- This is the academic basis for Liftoff's "300 GW if flexibility is valued" case.
- Both a Fervo co-author (Norbeck) and a Rhodium co-author (Ricks) worked on it. It is the intellectual bridge to the hyperscaler 24/7 carbon-free-energy (CFE) thesis.

URL: https://api.openalex.org/works/doi:10.1038/s41560-023-01437-y

### 1.7 Sepulveda, Jenkins, de Sisternes, Lester, 2018. "The Role of Firm Low-Carbon Electricity Resources in Deep Decarbonization of Power Generation", *Joule* 2(11):2403–2420, doi:10.1016/j.joule.2018.08.006

Metadata was verified via OpenAlex. The key result is from memory (unverified):
- Having firm low-carbon resources (geothermal, nuclear, CCS) available cuts the cost of a deeply decarbonised power system by roughly **10–62%** versus portfolios without them.
- This is the foundational paper behind "clean firm" premiums and hyperscaler 24/7 CFE procurement.

URL: https://api.openalex.org/works/doi:10.1016/j.joule.2018.08.006

### 1.8 Smith, Hubbard, Newkirk, Ganeshalingam, Holecek, Sartor et al. (LBNL), June 2026. *United States Data Center Energy Usage Report: 2025 Update*, LBNL-2001758, OSTI 3374245

- Data centres reach **11.8% of US electricity by 2030 (range 9.5–15.3%)**. The 2024 report range was 6.7–12% by 2028.
- Sibling file 02-data-center-power.md gives the volumes: **192 TWh (2024) → 464 TWh (2028) → 649 TWh (2030)**.

URL: https://www.osti.gov/biblio/3374245

### 1.9 Company primary releases (hyperscaler deals)

**Google–Fervo (Google blog, 28 Nov 2023)**
- The first corporate EGS agreement (begun in 2021) became operational at Project Red, Nevada.
- The S-1 says Red runs at about 3 MW.
- https://blog.google/outreach-initiatives/sustainability/google-fervo-geothermal-energy-partnership/

**Meta–Sage (Meta, 26 Aug 2024)**
- Up to **150 MW**, using Sage's geopressured geothermal system.
- Phase 1 is targeted online in **2027**. Location and price were undisclosed (NLR places it "east of the Rockies").
- https://about.fb.com/news/2024/08/new-geothermal-energy-project-to-support-our-data-centers/

**Meta–XGS (Business Wire, 12 June 2025, via NLR report)**
- Up to **150 MW** in New Mexico, in two phases, delivering to the **New Mexico grid by 2030**.
- The utility counterparty is not stated in the sources read. PNM is the presumptive one (unverified).

**Microsoft–G42 (Microsoft, 22 May 2024)**
- A data-centre campus at **Olkaria, Kenya**, "run entirely on renewable geothermal energy", with an Azure East Africa region within 24 months of definitive agreements. MW were not stated (1 GW is widely reported; unverified).
- In the sources read here, Microsoft has no disclosed US geothermal PPA.
- https://news.microsoft.com/2024/05/22/microsoft-and-g42-announce-1-billion-comprehensive-digital-ecosystem-initiative-for-kenya/

**Zanskar (company news page)**
- **100 MW PPA with NV Energy (8 May 2026)**, price undisclosed.
- A GEODE prospecting agreement with CC Power (California), April 2026.
- $40M of development capital scaling to $100M (April 2026), and a $115M Series C (January 2026).
- No data-centre offtaker is named.
- https://www.zanskar.com/news

### 1.10 Supporting NLR/LLNL work (2026)

**Halloran, Simpson, Ho (NLR), *Value of Geothermal Energy Storage*, NLR/TP-6A40-95722**
- ReEDS valuation of flexible EGS with in-reservoir storage.
- It also cites underground thermal energy storage (UTES) for data-centre cooling (Oh et al. 2025; Zhang et al. 2024).
- https://www.osti.gov/biblio/3377911

**Grappone et al. (LLNL), GRC Trans. 50, 2026**
- Frames geothermal as a strategic firm resource for AI load and notes it is about 0.5% of US generation today.
- https://www.osti.gov/biblio/3904544

---

## 2. Price synthesis ($/MWh)

| Reference | $/MWh | Source |
|---|---|---|
| Hydrothermal flash LCOE (ATB 2024) | 63–74 | NLR 2025 |
| Hydrothermal binary LCOE | 90–110 | NLR 2025 |
| Disclosed geothermal PPAs 2021–25 | 70–99 | NLR Table 3 |
| Ormat portfolio negotiation (2024) | ~100 | Ormat Investor Day via NLR |
| Hell's Kitchen / Puna | ~75 / ~70 | L06 |
| Clean-firm / EGS PPAs (Rystad) | 100–130 | Fervo S-1 |
| Clean-firm PPAs, DOE Liftoff | 70–100 ($20–50 over solar) | L06 |
| Rhodium BTM geothermal for data centres | 78–85 national; 49–111 regional | Rhodium 2025 |
| Nuclear comparables: Meta–Clinton / Microsoft–Crane | ~70 / ~98–115 (estimates) | 02-data-center-power, 05-policy |
| Federal credit | 45Y/48E available to geothermal for construction starting through 2033 (phase-down 2034, repealed 2036) | NLR 2025 |

**Read.** New geothermal PPAs clear at **$75–130/MWh**, and hyperscaler-specific deals sit at the top of that range. They are almost never disclosed, but the CTT structure exists precisely so that the hyperscaler can pay a premium.

**Value of 1 MW** (my arithmetic): at 90% capacity factor, $100/MWh gives about **$0.79M/yr**. A 20-year contract is roughly $10M PV per MW at 6%.

---

## 3. Demand for firm clean power in the West

**National data-centre load**
- LBNL: 4.4% of US electricity (2023) → 11.8% (2030).
- Rhodium high case: ~80 GW by 2030.
- BNEF: 106 GW by 2035 (02-data-center-power).
- Realistic incremental US data-centre load by 2030 is **50–70 GW** after discounting queues (02-data-center-power).

**Western demand pull**
- CPUC: 1 GW firm by 2026, plus 1 GW long-lead geothermal for 2031–37.
- NV Energy: the CTT, 115 MW Fervo/Google and 100 MW Zanskar.
- New Mexico: 150 MW Meta/XGS.
- Phoenix and Las Vegas are among Rhodium's top five growth markets.

**Supply side**
- About 4 GW of US geothermal is installed and only ~1.7 GW sits in interconnection queues (Rhodium).
- Committed next-generation volume is <1 GW (NLR) plus Fervo's >1 GW and the 3 GW Google framework.
- This is against a 15–17 GW data-centre-addressable opportunity (Rhodium) and 90 GW by 2050 (DOE).
- **Demand exceeds identified, permitted, drill-ready resource by an order of magnitude.**

---

## 4. Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **The exit buyer exists, pays a premium and is growing.**
   - Hyperscalers (Google 3 GW framework; Meta 2 × 150 MW) and the utilities that front for them (NV Energy CTT, CPUC/DWR) are short of *sites*, not money.
   - The CTT makes "customer pays the premium for a specific new geothermal asset" an approved regulatory product. LBNL lists similar riders at Dominion, Duke, Evergy and Ameren.
   - So a proven resource with a lease, temperature data and an interconnection path is directly monetisable at $75–130/MWh, or about $10M PV per MW of contracted firm output.
   - The step-up from an unproven lease (about $4/acre historically; $344–1,207/acre in 2025–26 BLM sales per L21/L07) to a contracted resource is large.

2. **Site scarcity is the binding constraint, and data is the lever.**
   - Rhodium shows that siting *to* the resource (choosing the data-centre location by geothermal quality) cuts cost 31–45%. Regional LCOE spreads from $49 to $111/MWh, more than 2x.
   - **Knowing which parcel is in the $49 tier is worth tens of $/MWh across a 20-year contract.** That is exactly the information an ML-over-public-records company produces.
   - The shape is Terranox's uranium arbitrage: own the parcel before the market knows it is low-LCOE.

3. **Zanskar's shape and its gap.**
   - Zanskar is a vertically integrated *hydrothermal* developer. It finds blind systems (Big Blind), drills them, operates plants (Lightning Dock) and sells power. Its first large contract is a **100 MW utility PPA with NV Energy**, and it has no named hyperscaler offtaker.
   - Its capital goes into drilling and plants. That means a limited number of prospects carried to proof at any time, and a focus on Great Basin conventional hydrothermal.
   - **Gap 1, land bank and data room for the hyperscaler-facing next-generation developers.** Fervo, Sage, XGS, Eavor and Quaise hold >60% of new PPAs and almost all data-centre deals. Each needs specific hot, shallow, interconnectable parcels near load (NM, CO, NV, UT, OR, TX). A rights owner that sells or leases pre-qualified parcels to them is not something Zanskar is built to do, since it would be supplying competitors.
   - **Gap 2, siting for the buyer.** Packaging "geothermal-ready" land, combining temperature-at-depth, lease, water, transmission and data-centre-ready acreage, for a hyperscaler or utility before a developer is picked. This is the Rhodium "geothermal-driven siting" case.
   - **Gap 3, outside the Great Basin.** Meta-Sage (east of the Rockies), Meta-XGS (NM), Exceed (TX, 110 MW) and Rhodium's CO/NM/OR/TX states are where hyperscaler demand meets under-explored sedimentary heat mapped by oil and gas BHTs. That is Terranox's public-but-illegible data analogue, and largely outside Zanskar's hydrothermal focus.

4. **Not "too small".**
   - 15–17 GW of data-centre-addressable geothermal × about $10M PV/MW of contracted value is about $150B of offtake value.
   - Even 1–3% captured as land, royalty or development-right value (overrides, option fees, step-up sales) is $1.5–5B.

5. **Risks.**
   - Prices are almost never disclosed, so the $100–130 hyperscaler premium is inferred, not observed (Rystad via the S-1).
   - Interconnection, not resource, was the Corsac bottleneck (Latitude). Parcels must be screened for transmission.
   - Credits phase down from 2034.
   - Next-generation developers may self-source land (Fervo already holds large acreage, per L21), which pushes the company toward partnership, royalty or option structures rather than outright sales.

---

## Sources
- NLR 2025 U.S. Geothermal Market Report (Akindipe et al.): https://www.osti.gov/biblio/3014949 ; https://www.osti.gov/servlets/purl/3014949
- Fervo S-1 (2026): https://www.sec.gov/Archives/edgar/data/1853868/000162828026025821/fervoenergy-sx1.htm
- LBNL, Speed to Power (2026): https://www.osti.gov/biblio/3367528
- LBNL, Rate Designs for Large Loads 2026 Update: https://www.osti.gov/biblio/3409217 ; https://escholarship.org/uc/item/9n09r4d6
- Latitude Media on CTT approval (15 May 2025): https://www.latitudemedia.com/news/the-clean-transition-tariff-won-approval-in-nevada-whats-next-for-fervo/
- Rhodium Group (King, Ricks, Pastorek, Larsen 2025): https://rhg.com/research/geothermal-data-center-electricity-demand/
- Ricks et al., Nature Energy (metadata): https://api.openalex.org/works/doi:10.1038/s41560-023-01437-y
- Sepulveda et al., Joule 2018 (metadata): https://api.openalex.org/works/doi:10.1016/j.joule.2018.08.006
- LBNL Data Center Energy Usage Report 2025 Update: https://www.osti.gov/biblio/3374245
- Google–Fervo blog (2023): https://blog.google/outreach-initiatives/sustainability/google-fervo-geothermal-energy-partnership/
- Meta–Sage (2024): https://about.fb.com/news/2024/08/new-geothermal-energy-project-to-support-our-data-centers/
- XGS–Meta Business Wire (cited in NLR; fetch blocked): https://www.businesswire.com/news/home/20250612778008/en/XGS-Energy-and-Meta-to-Partner-on-150-MW-Advanced-Geothermal-Project
- Microsoft–G42 Kenya (2024): https://news.microsoft.com/2024/05/22/microsoft-and-g42-announce-1-billion-comprehensive-digital-ecosystem-initiative-for-kenya/
- Zanskar news: https://www.zanskar.com/news
- NLR, Value of Geothermal Energy Storage (2026): https://www.osti.gov/biblio/3377911
- LLNL, Grappone et al. GRC 2026: https://www.osti.gov/biblio/3904544
