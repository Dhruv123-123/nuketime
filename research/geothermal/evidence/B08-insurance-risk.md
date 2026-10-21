# B08: Exploration risk transfer and financing (insurance, cost-share, farm-outs)

**Scope:** who pays for the expensive and risky step between "we hold a cheap right with an anomaly" and "a buyer will pay a step-up". Covers resource-risk insurance (Munich Re, Germany, Turkey), donor risk-mitigation funds (GRMF in East Africa, the GDF in Latin America, Indonesia GREM), DOE cost-share, and farm-out or carried-interest precedents. It ends with what this means for a Terranox-shape company.

**Method note:** this turn's shared web-search budget ran out (200 calls across all agents), so no new searches could be run. Everything below comes from primary documents fetched directly: World Bank project papers (PDFs extracted to text), ESMAP and IFC reports, 43 CFR via Cornell LII, SEC EDGAR filings, Zanskar's own posts, and the DOE GTO history PDF and Liftoff report already in the shared scratchpad. Munich Re product specifics could not be fetched (both munichre.com URLs returned 404) and are marked (unverified).

---

## 1. The base rate the instruments price against

- **IFC/World Bank (2013), "Success of geothermal wells: a global study":** 2,613 wells in 52 fields; **78% of wells overall were successful** (median field 71%).
  - **First well in a field averages 50% success.**
  - The first five wells average **59%**.
  - Development-phase wells average **74%**, operation-phase wells **83%**.
  - Source: http://documents.worldbank.org/curated/en/305681468168834775/pdf/782300WP0Succe00Box0377330B0PUBLIC0.pdf
- **World Bank Indonesia GREM (2019):** a single exploration well has "around 55–60 percent" likelihood of being usable for steam. A normal site success criterion is "two-thirds of the exploration wells being productive". Full development success is assumed at 75% (75–80% range for Indonesia).
  - Source: http://documents.worldbank.org/curated/en/972941569608786496/pdf/Indonesia-Geothermal-Resource-Risk-Mitigation-Project.pdf
- **Takeaway:** the risk that needs transferring is concentrated in the **first 1–3 wells per prospect, at roughly 50/50 odds**. Every instrument below is built around that coin flip.

## 2. Resource-risk insurance: thin, expensive, and historically marginal

**ESMAP (2016), "Comparative analysis of approaches to geothermal resource risk mitigation: a global survey"** is the key primary source. Source: http://documents.worldbank.org/curated/en/621131468180534369/pdf/105172-ESM-P144569-PUBLIC-FINAL-ESMAP-GeoRiskMitigation-KS024-16-web.pdf

**How the product works:**
- The insurer does resource due diligence.
- The insurer and developer jointly set well success criteria (flow rate and temperature).
- The developer pays the premium **up front**.
- A well that misses the criteria triggers a payout.
- Single wells have been insured. The trend is toward portfolio policies, but there is "little experience and success in scaling up" them.

**Track record:**
- "There are **less than a handful of insurers worldwide**" willing to underwrite resource risk.
- "**A few tens of megawatts at most** have been developed and catalyzed" by geothermal risk insurance.
- In the early 1980s a US insurer offered such a scheme and "**no developer applied** ... because of the high premiums".
- **Germany** is the main success case, but ESMAP says the ~**US$0.30/kWh feed-in tariff** "likely played a more significant role ... than the insurance product itself".
- France also tried it, "with modest success".
- Efforts were under way in Turkey, Kenya and the US. The GeoFund for Eastern Europe planned a geological risk insurance component that "did not materialize" (GREM PAD).

**Why it fails:**
- Limited actuarial data on wells.
- A small sector, so no pool for diversification.
- High premiums on top of drilling capex.
- Complex monitoring: the insurer reviews drilling, logging and testing data.

**Munich Re:** it is the insurer most associated with German deep-geothermal (Bavarian Molasse) "Fündigkeitsrisiko" (discovery-risk) policies in the 2000s (unverified; product pages not retrievable). Munich Re's present role in this space is visible in one verified fact: **Munich Re Ventures is an investor in Zanskar's Series C** (https://zanskargeothermal.substack.com/p/zanskar-raises-115m-series-c-following). The reinsurer is backing the data-driven explorer rather than writing stand-alone well cover.

**Implication:** insurance is not a dependable financing source for a single-prospect developer. ESMAP's diagnosis is that the market is missing **portfolio scale plus actuarial data**, which is exactly what a high-throughput, data-heavy prospect bank would create.

## 3. Public and donor risk-sharing facilities (hard terms)

| Facility | Mechanism | Hard numbers | Source |
|---|---|---|---|
| **Turkey Geothermal Development Project, RSM** (World Bank/CTF, via TKYB) | Contingent grant: if exploration wells fail pre-agreed success criteria, the RSM reimburses a fixed share of well cost. If they succeed, the developer pays a **success fee** | **US$39.8M CTF grant**, of which US$37M is for the RSM, inside a US$289.8M project (US$250M IBRD). Payout = **60% of acceptable well costs** on failure. Success fee was cut in Feb 2021 from **10% to 5%** of drilling costs (first 3 wells) and from **25% to 10%** (up to 2 extra wells). Round 1: 7 shortlisted, 2 signed, **both failed (0 MW)**, payout **US$5.1M on US$8.6M of well cost**. Rounds 2–4: 34 + 14 full proposals, but most withdrew over land, licensing, drilling cost or EIA. Targets: 16 drilling projects, US$78M catalysed, 99.5 MW confirmed. US$31.7M of payout capacity remained; closing extended to Dec 2027. Planning assumption: **50% fail / 50% succeed** | Restructuring paper Dec 2024: http://documents1.worldbank.org/curated/en/099121624135086707/pdf/P1517391e523690b3190c1191a3ac08f7df.pdf ; project API: https://search.worldbank.org/api/v2/projects?id=P151739&format=json |
| **GRMF East Africa** (AUC, KfW/BMZ, EU-AITF, DfID) | Grants on actual eligible costs | **80% of surface studies**, **20% of infrastructure**, **40% of exploration and confirmation drilling** for up to 2 wells. On success, a **further 30%** of pre-set well cost is paid as a "premium". Annual calls; first call Dec 2012 funded 4 projects in Kenya and Ethiopia. Covers 15 countries. Programmes: GRMF POWER and GRMF HEAT | ESMAP 2016; GREM PAD; https://grmf-eastafrica.org/ |
| **GDF Latin America** (KfW et al.) | Contingency grant | **40% of up to 3 exploration wells**. Converts to a full grant on failure. On success, **80% is repaid** into the revolving fund. The GREM PAD summary describes it as paying 8% of cost on successful wells and 40% on failed wells | ESMAP 2016; GREM PAD |
| **Indonesia GREM** (World Bank/GCF/CTF via PT SMI) | Blended loan up to **75% of drilling cost**, max **US$30M per developer** for exploration. Of that: 50% is an IBRD sub-loan guaranteed by the sponsor, and 50% is a **"Financial Instrument" whose value is linked to the developer's shares**. Success = full repayment **plus a premium**. Partial success = a share of fair market value. Failure = write-off | GCF Tranche 1 US$100M (of US$185M approved). US$72.5M CTF. Target ≥600 MW enabled | GREM PAD (above) |
| **Japan** (historic) | Government cost-share | Up to **40% of exploration wells** and **20% of production and injection wells**. Credited with most of Japan's 536 MW | ESMAP 2016 |

**Pattern:** the global standard is **public money absorbing about 40–60% of first-well cost on failure**, in exchange for a success fee, upside share, or data. Indonesia's FI is effectively **equity in the step-up**, which is the Terranox thesis expressed as a donor instrument.

## 4. United States: DOE cost-share history and the current state

**Industry-Coupled Drilling Program (from 1977):**
- DOE cost-shared reservoir-confirmation holes. **In exchange, companies released their confidential data packages to open file.**
- **8 of 14** areas explored were later developed: Roosevelt Hot Springs, Cove Fort, Beowawe, San Emidio, Soda Lake, Stillwater, Dixie Valley, Desert Peak. Together they produce **137 MWe**.
- Source: DOE GTO, *A History of Geothermal Energy R&D in the US: Exploration 1976–2006*, https://www.energy.gov/sites/prod/files/2014/02/f7/geothermal_history_1_exploration.pdf (path as archived; document text verified).

**GRED I–III (2000–2007):**
- **GRED I** included **Lightning Dock, NM**, now Zanskar's operating plant.
- **GRED III** included **Noramex at Pumpernickel Valley, NV**, now a Zanskar-named discovery.
- Blue Mountain (49.5 MW) and Raft River came out of GRED (same DOE history).
- Zanskar's two flagship assets therefore sit on **previously DOE-cost-shared, publicly reported** prospects. This is direct evidence that legacy public data marks the hunting ground.

**DOE Liftoff (2024):**
- GRED (1982–2012 in DOE's framing) "identified much of the geothermal capacity that is currently online in the U.S."
- Recommends cost-share and drilling-insurance products.
- Endorses a "**farm-down**" model, which cuts up-front equity to about **US$180M per 30 MW** (EGS).
- Source: https://cdn.catf.us/wp-content/uploads/2025/06/09154348/doe-liftoff-nextgen-geothermal.pdf

**Typical small-company awards:**
- **Nevada Geothermal Power, Crump Geyser (2009):** about **US$1.8M** DOE cost-share. It reimbursed roughly **50% overall**, with **Phase I at 80%** and later phases lower.
- **U.S. Geothermal, San Emidio (2016 SubTER):** **US$1.5M** DOE on a US$1.9M programme (company cost share US$400k).
- **U.S. Geothermal, Raft River (2011):** **US$11.4M** cost-shared EGS stimulation grant.
- Sources: NGP 20-F FY2011, https://www.sec.gov/Archives/edgar/data/1177440/000117625611000946/ngp20f110630.htm ; U.S. Geothermal 10-K (EDGAR CIK 1172136).

**Current state:**
- Zanskar was **selected for two DOE awards (Sep 2026)**: a horizontal stimulated injection well at Lightning Dock, and deep directional confirmation wells at an undrilled Nevada site.
- Amounts are undisclosed and the awards are still in negotiation.
- Source: https://zanskargeothermal.substack.com/p/zanskar-selected-for-two-us-department

**BLM lease carrying cost** (43 CFR):
- Rental is **$2/acre in year 1, $3/acre in years 2–10** (competitive), or $1/acre (noncompetitive).
- The primary term is **10 years**. The only primary-term work obligation is **$40/acre cumulative by the end of year 10**. Payment in lieu is allowed, and temperature-gradient holes and geophysics qualify.
- Extensions require **$15/acre/yr** (years 11–15), then **$25/acre/yr** (years 16–19).
- So a 10,000-acre option costs about **$290k in rent plus $400k of work over 10 years**. It is a long, cheap call option.
- Sources: https://www.law.cornell.edu/cfr/text/43/3211.11 , https://www.law.cornell.edu/cfr/text/43/3207.11 , https://www.law.cornell.edu/cfr/text/43/3207.12

## 5. Farm-out / carried-interest precedents (geothermal)

| Deal | Terms | Source |
|---|---|---|
| **NGP → Ormat, Crump Geyser OR (2010)** | 50:50 LLC. NGP contributed leases, **technical data, permits, and the DOE cost-share grant**. **Ormat funded 100% of initial development (US$15M)** and **paid NGP US$2.5M in instalments over 3 years**. NGP could be diluted if obligations were missed, with a **floor of 20%** and an option to reinstate 50% up to commercial operation. If Ormat stopped before meeting its Development Obligations, **its interest reverted to NGP**. The early wells hit about 130 °C, the low end of commercial | NGP 20-F FY2011 (above); LLC agreement: https://www.sec.gov/Archives/edgar/data/1177440/000117625610001045/exhibit4-158.htm |
| **Eden Energy → Origin Energy, GEL 185, South Australia (2009)** | Origin earns **70%** for **A$1M cash + the first A$0.5M of spend**, then contributes pro rata. Origin operates | https://www.thinkgeoenergy.com/australia-origin-energy-to-farm-in-to-eden-energys-geothermal-license/ |
| **Basic Energy → DESCO, Mariveles PH (2017)** | **25% participating interest** farm-in. Price undisclosed | https://www.thinkgeoenergy.com/basic-energy-finalises-farm-in-agreement-with-desco-on-mariveles-geothermal-project/ |
| **Enel → LaGeo, El Salvador (2002+)** | Bought 9% and earned up to **36%** by funding investment | ESMAP 2016 |
| **Public-explore / private-develop** (Kenya GDC steam sales, Olkaria III, Turkey MTA tenders) | The state drills and confirms, then transfers rights to the private sector at a value. This is the "step-up" captured by a public entity | ESMAP 2016 |

**Read-across:** the market-standard geothermal farm-in is a **50% carry for about 1–3 confirmation wells (US$10–20M) plus a modest cash payment**, or **70% earned for a small cash plus a work commitment** at a less mature stage.
- The originator keeps a 20–50% free-carried or diluted stake.
- This mirrors mining and oil and gas earn-ins.
- Disclosed $/MW values at the confirmation stage are rare (unverified beyond Crump).

## 6. Zanskar's financing stack (comparator)

- **Equity:** US$115M Series C (Jan 2026; lead Spring Lane; with Obvious, USV, Lowercarbon, **Munich Re Ventures**, StepStone). **US$180M total equity.** Stated model: "develop, build, own, and operate." No asset sales are mentioned.
- **Debt:** **US$40M non-recourse revolving Development Capital Facility** (closed Apr 16 2026; Just Climate + Spring Lane). It funds "key pre-construction activities" and bridges to bank project finance, and is **upsizable to US$100M**. Source: https://zanskargeothermal.substack.com/p/zanskar-closes-40m-in-novel-development
- **Offtake:**
  - **100 MW PPA with NV Energy** (May 2026).
  - **CC Power "GEODE" agreement** for exploration, offtake and development in CAISO. CC Power is 9 CCAs and about 12% of CAISO load. No MW or financial terms are disclosed. Source: https://zanskargeothermal.substack.com/p/zanskar-and-cc-power-sign-geode-agreement
- **Grants:** 2 DOE selections (Sep 2026), amounts undisclosed.
- **Insurance, farm-outs, carried interests:** **none disclosed.** Zanskar self-funds exploration drilling from equity and then moves to project-level credit.

---

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **The exploration-drilling gap is structural and priced at about 50% odds per first well.**
   - Insurance has failed for 40 years: fewer than 5 insurers, a few tens of MW catalysed, no 1980s US uptake.
   - Donor funds converge on about 40–60% of failed-well cost.
   - Whoever can de-risk the first well cheaply captures the largest value step in the chain. That is the Terranox step-up.

2. **A land+data company does not need to self-fund drilling. There is a proven farm-out playbook.**
   - Crump Geyser is the template. The originator contributes **leases + data + a DOE grant**. The developer pays **100% of the first US$15M plus US$2.5M cash** for 50%, with reversion if it walks and a 20% dilution floor.
   - Origin/Eden shows **70% earned for under A$2M** at an earlier stage.
   - A Terranox shape can run dozens of prospects to "TG-hole/slimhole-confirmed" for about US$0.5–3M each (cost range unverified) and farm each out for a **carry of 20–50% plus cash**.
   - Alternative: a retained override (see B07).

3. **Stack non-dilutive money on the cheapest step.**
   - DOE has historically paid **50–80%** of early phases (NGP Phase I at 80%).
   - DOE programmes traded cost-share for **data release**. That is a feature for a data company: the released data feeds the model, and the land is already held.
   - Zanskar's two best assets (Lightning Dock = GRED I, Pumpernickel = GRED III) are former DOE cost-share sites. This validates "mine the public archive, then lease".

4. **Portfolio scale makes risk insurable, so the company can become the risk-transfer counterparty.**
   - ESMAP blames insurance failure on missing portfolio scale and actuarial data.
   - A company holding 100+ ranked prospects can (a) negotiate **portfolio well cover** with Munich Re, whose venture arm already backs Zanskar, and (b) sell **portfolio-level, success-fee-style structures** to developers. This mirrors the Turkey RSM (60% refund on failure, 5–10% success fee) and Indonesia's FI (share-linked upside on success).
   - That turns the ML hit-rate lift directly into an insurance spread. The plausibility is high; the actual lift is untested.

5. **The gap vs Zanskar.**
   - Zanskar finances the whole chain itself: US$180M equity plus a US$40M→100M non-recourse facility, then builds, owns and operates.
   - It has **no disclosed farm-outs, carried interests, insurance or prospect sales**. Its PPA/GEODE deals monetise only at the plant stage.
   - That leaves open the **middle of the chain**: originating rights cheaply, confirming with others' money (DOE, farm-in partners, insurers), and exiting or retaining a carry at the confirmed stage to many buyers (Ormat, Fervo, Cyrq, utilities, data-centre offtakers, even Zanskar itself).
   - The capital intensity is about 1–2 orders of magnitude lower (Liftoff: ~US$180M per 30 MW even for a farm-down developer).
   - This is asset ownership, not a tool or service. The carry or override is a durable stake in each step-up.

6. **Risks to note:**
   - Farm-in partners may lowball unconfirmed resources. Crump turned out marginal (about 130 °C).
   - Turkey shows that permitting, land and EIA kill more prospects than drilling does: 12 of 16 Round 2 subprojects withdrew.
   - DOE cost-share is awarded competitively and is slow (Zanskar's awards are still in negotiation).
   - A small company with no balance sheet may face reluctant insurers.

## Sources
- IFC/World Bank 2013, Success of Geothermal Wells: http://documents.worldbank.org/curated/en/305681468168834775/pdf/782300WP0Succe00Box0377330B0PUBLIC0.pdf
- ESMAP 2016, Comparative Analysis of Approaches to Geothermal Resource Risk Mitigation: http://documents.worldbank.org/curated/en/621131468180534369/pdf/105172-ESM-P144569-PUBLIC-FINAL-ESMAP-GeoRiskMitigation-KS024-16-web.pdf
- World Bank Turkey Geothermal Development Project restructuring paper (Dec 2024): http://documents1.worldbank.org/curated/en/099121624135086707/pdf/P1517391e523690b3190c1191a3ac08f7df.pdf
- World Bank project record P151739: https://search.worldbank.org/api/v2/projects?id=P151739&format=json
- World Bank Indonesia GREM PAD (2019): http://documents.worldbank.org/curated/en/972941569608786496/pdf/Indonesia-Geothermal-Resource-Risk-Mitigation-Project.pdf
- GRMF East Africa: https://grmf-eastafrica.org/
- DOE GTO exploration history 1976–2006: https://www.energy.gov/sites/prod/files/2014/02/f7/geothermal_history_1_exploration.pdf
- DOE Pathways to Commercial Liftoff: Next-Generation Geothermal: https://cdn.catf.us/wp-content/uploads/2025/06/09154348/doe-liftoff-nextgen-geothermal.pdf
- 43 CFR 3211.11, 3207.10–12: https://www.law.cornell.edu/cfr/text/43/3211.11 ; https://www.law.cornell.edu/cfr/text/43/3207.11 ; https://www.law.cornell.edu/cfr/text/43/3207.12 ; https://www.law.cornell.edu/cfr/text/43/3207.10
- BLM geothermal program: https://www.blm.gov/programs/energy-and-minerals/renewable-energy/geothermal-energy
- Nevada Geothermal Power 20-F FY2011: https://www.sec.gov/Archives/edgar/data/1177440/000117625611000946/ngp20f110630.htm
- Crump Geothermal Company LLC agreement: https://www.sec.gov/Archives/edgar/data/1177440/000117625610001045/exhibit4-158.htm
- Origin/Eden farm-in: https://www.thinkgeoenergy.com/australia-origin-energy-to-farm-in-to-eden-energys-geothermal-license/
- Basic Energy/DESCO farm-in: https://www.thinkgeoenergy.com/basic-energy-finalises-farm-in-agreement-with-desco-on-mariveles-geothermal-project/
- Zanskar Series C: https://zanskargeothermal.substack.com/p/zanskar-raises-115m-series-c-following
- Zanskar US$40M development capital facility: https://zanskargeothermal.substack.com/p/zanskar-closes-40m-in-novel-development
- Zanskar–CC Power GEODE: https://zanskargeothermal.substack.com/p/zanskar-and-cc-power-sign-geode-agreement
- Zanskar DOE selections: https://zanskargeothermal.substack.com/p/zanskar-selected-for-two-us-department
