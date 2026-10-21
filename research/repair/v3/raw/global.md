# Global (ex-US) CGD / safety-related replacement parts market — raw notes

Prepared 2026-10-21. Tags: **[src]** = from fetched or searched source (URL given). **(recalled)** = from memory, not verified this session. **[est]** = my estimate or assumption.
Search budget: 6 WebSearch calls used. IAEA PDFs returned HTTP 402 and CSA returned 403 to WebFetch, so the IAEA and CSA details are partly recalled.

---

## 1. Fleet baseline

From WNA "Nuclear power in the world today" (page updated 20 Oct 2026) [src]: https://world-nuclear.org/information-library/current-and-future-generation/nuclear-power-in-the-world-today

- **443 operable reactors** worldwide, 405.7 GWe net. **79 under construction**, 86.6 GWe gross.
- Operable units by country: US 94, China 65, France 57, Russia 34, Japan 33, Korea 26, India 24, Canada 17, Ukraine 15, UK 9, Spain 7, Sweden 6, Czech 6, Slovakia 6, Finland 5, Hungary 4, Switzerland 4, UAE 4, Argentina 3, Belgium 2, Brazil 2, South Africa 2, Mexico 2, Romania 2, Bulgaria 2, Slovenia 1.
- Taiwan has had 0 operable units since May 2025.

## 2. IAEA guidance

- **IAEA-TECDOC-2034 (2023), *Suitability Evaluation of Commercial Grade Products for Use in Nuclear Power Plant Safety Systems*** [src, title and abstract via search]: https://www-pub.iaea.org/MTCD/Publications/PDF/TE-2034web.pdf
  - The IAEA uses "suitability evaluation" as the neutral international term. The abstract says SMRs and advanced reactors are "expected to leverage such products to a large extent."
- **IAEA Technical Meeting on commercial grade products and services (April 2022)** [src, info sheet via search]: https://iaea.org/sites/default/files/22/02/evt2103900_info_sheet.pdf
  - The info sheet says some Member States follow established CGD guidelines. Others "rely on methodologies individual to the owner operator organizations and their regulatory body."
  - In practice there is **no harmonised international CGD regime**. The US EPRI NP-5652 / 3002002982 lineage is the de facto reference wherever one exists.
- Related IAEA work (recalled): IAEA NP-T-3.21 on procurement engineering and supply chain, and IAEA SSG-?? / GSR Part 2 on graded approach.
- Related international work (recalled): the CORDEL/WNA Cooperation in Reactor Design Evaluation and Licensing working group, and the NEA MDEP. Both discuss code harmonisation and counterfeit/fraudulent items (CFSI).
- **EPRI 3002029261** (given in brief): about 40% of the world's reactors use CGD regularly. My cross-check (sec. 5) gets about 39%, which is consistent.

## 3. Country-by-country

### Canada (17 units, CANDU). Best ex-US market.
- **Regime:** CNSC licence conditions call up **CSA N286** (management system), **CSA N285.0** (pressure-retaining components, uses ASME III plus Canadian add-ons, registered with TSSA) and **CSA N299.1–.4** (graded supplier QA) (recalled).
  - N299 came from an OPG/Bruce CANDU Owners Group (COG) seed document in 2014, built to replace Z299 [src]: https://www.csagroup.org/wp-content/uploads/CSA-N299-CaseStudy-EN_Accessible_rev.pdf (search snippet; PDF itself returned 403).
  - N299 and N285 contain explicit commercial-grade item dedication provisions, modelled on the EPRI approach (recalled). OPG and Bruce routinely dedicate commercial items and also buy from NQA-1 / 10 CFR 50 App B US vendors (recalled).
- **Refurbishment wave** [src WNA Canada profile]: https://world-nuclear.org/information-library/country-profiles/countries-a-f/canada-nuclear-power
  - **Darlington refurbishment:** C$12.8B, completed early 2026, C$150M under budget and 4 months early. 96% of the investment benefited the Ontario supply chain [src]: https://www.neimagazine.com/news/darlington-refurbishment-complete/
  - **Bruce MCR, Units 3–8:** C$13B (2014$) over 2020–2033, plus a further **C$5B** for asset management and life extension over 2016–2053.
    - Unit 6 returned Sep 2023 and Unit 3 in Jun 2026. Unit 4 is due back in 2027. Unit 5 was approved Apr 2025. Units 7 and 8 start in 2028 and 2030.
  - **Pickering 5–8 refurbishment:** **C$26.8B**, approved Nov 2025, with execution starting early 2027 and finishing in the mid-2030s.
  - **Darlington BWRX-300, 4 units:** C$20.9B, first unit targeted for 2030. This is a US-origin design (GE Vernova Hitachi), so US-style CGD documentation is directly reusable.
  - **Pipeline:** Bruce C (up to 6 × 800 MWe, C$300M pre-development to about 2030) and Wesleyville (up to 10 GWe, first unit about 2040).
  - **Point Lepreau** was refurbished in 2012 [src WNA].
- **Bruce MCR major supply contracts (2018):** C$914M across BWXT (C$642M), Laker, Cameco Fuel Manufacturing and Nu-Tech [src]: https://www.nucnet.org/news/canada-s-bruce-power-signs-cad-914-million-in-refurbishment-contracts
- **Combined pipeline [est]:** Ontario refurbishment plus life-extension capex runs at roughly **C$4–6B/yr** through the mid-2030s.
  - Only a small share of that is CGD-addressable replacement parts: valves, pumps, I&C, electrical and motors. 3–5% is about **C$150–300M/yr** of dedicated-item value.
  - About 2,000 supply chain companies are tied to the "CANDU supply chain" (recalled, Canadian Nuclear Association / OCNI figure, unverified).
- **Access for a US dedicator: HIGH.**
  - English-speaking, with US-derived standards. A cross-border vendor base already exists (BWXT, Westinghouse, Curtiss-Wright, Framatome Canada).
  - The main friction is the "Made in Ontario" content preference, so a Canadian entity or partner is probably needed. A TSSA/N285 registration is needed for pressure-boundary scope.

### UK (9 units: 8 AGR plus Sizewell B PWR). ONR regime.
- ONR does not prescribe CGD. Licensees justify items under their own arrangements (Licence Condition 17), using "special case procedure" and "Production Excellence" style approaches (recalled).
- **AGRs:** EDF plans to run all four AGR stations (Heysham 1/2, Hartlepool, Torness) until **March 2030**. This is a short tail of obsolescence-driven, one-off parts demand [src]: https://world-nuclear.org/information-library/country-profiles/countries-t-z/united-kingdom
- **Sizewell B:** extension to 2055 needs about £800M of investment. A CfD for 2035–2055 was agreed Jul 2026 [src WNA UK].
  - Sizewell B is a Westinghouse-lineage SNUPPS PWR, so it is the one UK plant where US CGD packages map well.
- **New build:**
  - Hinkley Point C: about £35B (2015£).
  - Sizewell C: £38.2B, FID Jul 2025, full operation 2039.
  - Rolls-Royce SMR at Wylfa: 3 units, mid-2030s [src WNA UK].
  - New build follows RCC-M and Framatome supply chains, so it is less addressable.
- **Access: MEDIUM-LOW.** Sizewell B life extension is the realistic entry point.

### France (57 units). EDF Grand Carénage.
- **Cost** [src WNA France and connaissancedesenergies / Cour des comptes via search]:
  - 2014 estimate: €55B. 2020 estimate: €49.4B. Late-2021 estimate for 2014–2025: €50.2B.
  - 2022–2028 phase: **€33B, about €4.7B/yr**.
  - Cour des comptes total for 2014–2035: **€100.8B**, or **€131.9B** including routine maintenance. Annual cost **> €6B/yr**.
  - Sources: https://world-nuclear.org/information-library/country-profiles/countries-a-f/france and https://www.connaissancedesenergies.org/afp/494-milliards-deuros-edf-revoit-la-hausse-le-cout-du-grand-carenage-de-son-parc-nucleaire-201029
- **Inspections and lifetime:** the 900 MWe VD4 programme for 32 units runs to 2031. ASN finished a generic 1300 MWe review beyond 40 years in Jul 2025. Operation past 60 years is being studied.
- **EPR2:** six units at €72.8B (Dec 2025 estimate).
- **Regime** (recalled):
  - Design and manufacturing follow RCC-M, in-service follows RSE-M, and pressure equipment follows the ESPN order.
  - EDF qualifies items itself (in-house "qualification" and "COMSYS"/"QCE" processes) with heavy Framatome / EDF DIPDE involvement.
  - There is no US-style third-party dedicating-entity market. EDF has a "conventional item" (matériel non-classé / EIP) graded approach.
- **Access: LOW.** The market is very large but culturally closed and French-language, and EDF is vertically integrated.
  - Possible wedges: obsolescence on the Westinghouse-licensed 900 MWe CP0/CP1 I&C and electrical items; software or tooling sold to EDF; partnering with Framatome or Assystem.

### South Korea (26 units). KHNP, KEPIC.
- **KEPIC** (Korea Electric Power Industry Code) is an ASME / IEEE-derived code with supplier certification run by KEA [src via search]: https://www.munhwa.com/article/11338016
- Korean CGID follows **EPRI NP-5652** (Ajou University thesis) [src]: https://dspace.ajou.ac.kr/handle/2018.oak/11116
- **2012–13 falsified-certificate scandal** [src WNA Korea]: https://world-nuclear.org/information-library/country-profiles/countries-o-s/south-korea
  - About 60 forged QC certificates covered 7,682 components from 8 suppliers delivered 2003–2012.
  - In 2013, falsified safety-related cable documentation was found. Shin Kori 2 and Shin Wolsong 1 were halted, and about 100 people were indicted.
  - Afterwards KHNP hired Lloyd's Register / Lightbridge to re-verify procurement, with a focus on EQ, seismic and CGD [src]: https://www.nsenergybusiness.com/?p=170506
  - Result: a very strong appetite for documented, audit-trail-heavy dedication. That is a good fit for an AI-native "evidence-first" dedicator.
- **Exports:** Barakah (4 APR1400, US$20.4B, all operating since Sep 2024). Dukovany 5/6 in Czechia (2 × APR1000, about US$18.6B, contract Jun 2025, first unit 2036) [src WNA Korea].
- **Access: MEDIUM.**
  - Strong domestic supply chain and a preference for KEPIC-certified Korean suppliers, with Korean language required.
  - But KHNP imports many US-origin items (Westinghouse / CE lineage, I&C, pumps), and settled the Westinghouse IP dispute in Jan 2025 (recalled).
  - Best route: a partnership with a KEPIC-certified Korean firm (e.g. KEPCO E&C, KEPCO KPS, Doosan) or selling software.

### UAE (4 APR1400). ENEC / Nawah, FANR regulator.
- FANR rules are US NRC-modelled, and FANR-REG-?? accepts CGD (recalled).
- Barakah relies on KHNP and Korean / US OEMs for spares, and Nawah has been localising its supply chain (recalled).
- **Access: MEDIUM-HIGH.** English-speaking and US-friendly (123 Agreement). The fleet is small: 4 units at about 5.3 GWe [src WNA].

### Japan (33 operable, about 14–15 restarted as of 2026, recalled).
- **Regime** (recalled):
  - NRA rules sit under the Reactor Regulation Act, with the JEAC 4111 QA code and JSME codes.
  - Japanese utilities rely on their OEM keiretsu (MHI, Toshiba ESS, Hitachi-GE) to supply and qualify spares. There is little formal third-party CGD.
  - Restarts have needed large safety backfits, more than ¥5 trillion industry-wide (recalled).
- **Access: LOW.** Language, keiretsu and a low share of commercial-grade sourcing all work against entry.
  - A possible niche: obsolescence of US-origin BWR/PWR parts where the OEM licensors were GE or Westinghouse.

### Finland (5 units: Loviisa 1/2 VVER, Olkiluoto 1/2 BWR, OL3 EPR). STUK YVL guides.
- **KELPO** was launched in 2018 by Fortum, TVO and Fennovoima, coordinated by Finnish Energy, with STUK cooperating [src]: https://energia.fi/julkaisut/the-finnish-nuclear-industry-is-on-the-way-to-use-more-high-quality-industrial-grade-items-in-nuclear-installations/ and https://fortum.com/media/2020/05/towards-new-more-streamlined-practices-through-nuclear-sector-collaboration
  - Phase 1 (2018) proposed new procedures for procuring lower-safety-class mechanical equipment.
  - Phase 2 (2019) ran pilots.
  - **Phase 3 (2020) built a shared digital platform for the licensees**: databases, harmonised procedures, templates and materials to support procurement.
  - Key finding: quality is best assured by letting manufacturers follow their "own well-proven procedures", meaning standard industrial products under a graded approach.
  - KELPO2 report (2023, Finnish): https://energia.fi/wp-content/uploads/2023/08/KELPO2_Ydinlaitosten_luvituksen_ja_kelpoistuksen_kehitta-minen_vaihe_2_-raportti.pdf
  - Energiforsk (Sweden) seminar deck on KELPO: https://energiforsk.se/media/27060/palo_kelpo.pdf (the PDF text was not extractable).
- **Relevance:** KELPO is the closest international analogue to a **shared, digital dedication / qualification platform** owned by utilities. That is both evidence the idea is valued and a potential competitor or partner.
- **Lifetimes** (recalled): Loviisa licence was extended to 2050. TVO is studying OL1/2 extension to 2058 plus an uprate.
- **Access: MEDIUM.** The fleet is small, the market is English-friendly, and it is open to platforms.

### Sweden (6 units: Forsmark 1–3, Oskarshamn 3, Ringhals 3/4). SSM regulator.
- ABB-Atom BWRs and Westinghouse PWRs, with Westinghouse Electric Sweden at Västerås as the main OEM (recalled).
- SSMFS 2008:1 requires utilities to justify components themselves. Energiforsk runs joint utility R&D, including the KELPO seminars [src link above].
- Utilities plan operation to 80 years, and new build is planned at Ringhals (Vattenfall SMR choice, recalled).
- **Access: MEDIUM.**

### Spain (7 units).
- 6 Westinghouse PWRs and 1 GE BWR (Cofrentes) (recalled).
- The CSN regulator applies US NRC rules by reference, and the utilities (via UNESA / Foro Nuclear guides) use EPRI-based CGD (recalled).
- **Phase-out plan:** Almaraz 1 in 2027, then all units closed by 2035 (recalled). Almaraz extension requests were pending in 2025–26 (recalled).
- **Access: HIGH technically, but the market is shrinking.** Tecnatom and Enusa / Equipos Nucleares are incumbent local dedicators (recalled).

### Eastern Europe
- **Czech Republic** (6 VVER: Dukovany 1–4, Temelín 1/2)
  - Dukovany 5/6 is a KHNP APR1000 new build [src WNA Korea]. Temelín switched to Westinghouse and Framatome fuel (recalled).
- **Slovakia** (6 VVER including Mochovce 3)
  - Mochovce 4 is pending (recalled). A US–Slovakia intergovernmental agreement for a Westinghouse AP1000 at Bohunice was signed in 2025 (recalled).
- **Hungary** (Paks 1–4 VVER-440)
  - Life extension to 70 years. Paks II (Rosatom VVER-1200) is under construction (1 unit listed) [src WNA table].
- **Poland:** first plant is 3 × AP1000 at Lubiatów-Kopalino (Westinghouse / Bechtel). First concrete is planned around 2028 and operation in the mid-2030s (recalled).
- **Romania** (Cernavodă 1/2 CANDU)
  - The Unit 1 refurbishment (about €1.9B, 2027–2029, recalled) uses a Canadian supply chain (Candu Energy / AtkinsRéalis, KHNP, Ansaldo).
  - The Doicești NuScale SMR is planned (recalled).
- **Bulgaria** (Kozloduy 5/6 VVER-1000)
  - Kozloduy 7/8 is planned as AP1000 (recalled).
- **Slovenia** (Krško, Westinghouse 2-loop): life to 2043, and JEK2 is planned (recalled).
- **Ukraine** (15 VVER, Energoatom)
  - Westinghouse fuel and AP1000 plans (recalled). War-driven demand to replace Russian-origin spares (recalled).
- **Opportunity: VVER de-Russification [est].**
  - About 38 VVER units in the EU, Ukraine and Finland are sanction-exposed. Spares, I&C and valves that used to come from Russian OEMs now need Western replacements.
  - Those replacements need equivalency evaluation, which is CGD-like work. Westinghouse, Framatome, ÚJV Řež, Škoda JS and VUJE already do this (recalled).
  - **Access: MEDIUM**, via partners. The governing codes are national (Czech SÚJB decree 358/2016, Slovak ÚJD decrees, Hungarian NSC) and EU-procured (recalled).

### Other
- **Switzerland** (4): Beznau is Westinghouse, Gösgen is KWU, Leibstadt is GE BWR. ENSI regulates. Beznau closes 2032–33 (recalled). **Access: MEDIUM.**
- **Belgium** (2 remaining): Doel 4 and Tihange 3 extended to 2035 (recalled). **Access: MEDIUM.**
- **Brazil** Angra 1 (Westinghouse) and Angra 2 (KWU). **Mexico** Laguna Verde 1/2 (GE BWR), which uses US NRC rules by reference (recalled). **South Africa** Koeberg (Framatome, licence extended to 2044/45, recalled). **Argentina** Atucha 1/2 and Embalse CANDU (refurbished 2019).
- **Not addressable:** China (65), Russia (34), India (24; domestic, NPCIL), Iran, Pakistan, Belarus, plus Rosatom export units such as Akkuyu, Rooppur and El Dabaa.

## 4. Where can a US dedicator sell? (Ranked)

| Tier | Markets | Units | Why |
|---|---|---|---|
| 1. Direct, compatible | Canada (17), UAE (4), Slovenia (1), Mexico (2), Brazil Angra 1 (1), Spain (7) | 32 | US-derived rules or NQA-1 accepted, US-origin designs, English widely used |
| 2. Partner-led | Korea (26), Sweden (6), Switzerland (4), Belgium (2), Finland (5), Romania (2), Argentina (3), S. Africa (2), UK Sizewell B (1) | 51 | EPRI-style practice exists, but a local code, language or incumbent dedicator (KEPCO KPS, Tecnatom, Westinghouse Sweden, Candu Energy) is needed |
| 3. Opportunistic | VVER fleet: Czech (6), Slovakia (6), Hungary (4), Bulgaria (2), Ukraine (15), Loviisa | about 33 | De-Russification equivalency work. National codes. Partner with ÚJV / VUJE / Westinghouse |
| 4. Hard | France (57), Japan (33), UK AGRs (8, closing 2030) | 98 | Vertically integrated utilities or OEM keiretsu, little third-party CGD |
| 5. Closed | China, Russia, India, etc. | about 125 | Not accessible |
| New-build pull | BWRX-300 (Darlington, Poland?, TVA), AP1000 (Poland, Bulgaria, Slovakia?), APR1000 (Dukovany), NuScale (Romania), RR SMR (Wylfa) | — | TECDOC-2034: SMRs will lean on commercial-grade products. US-origin designs carry US CGD practice abroad |

## 5. What fraction of the world's reactors uses CGD regularly?

Count of reactors in regimes that regularly practise EPRI / NP-5652-style CGD [est from the WNA table]:

- US 94
- Korea 26
- Canada 17
- Spain 7
- Sweden 6
- UAE 4
- Switzerland 4
- Argentina 3
- Belgium 2
- Brazil 2
- Mexico 2
- South Africa 2
- Romania 2
- Slovenia 1
- Sizewell B 1

**Total ≈ 173 of 443 = 39%.** This matches the ~40% EPRI 3002029261 figure given in the brief.

- **Ex-US CGD-regular units: about 79**, roughly 46% of the CGD-using fleet. The US is about 54% of it.
- Adding Finland (KELPO graded approach) and the VVER fleet where equivalency work is CGD-like gives about 210 units, or **about 48%**.

## 6. Global addressable spend (estimates, assumptions explicit)

**Anchor [est, assumption to reconcile with US sibling notes]:** a US reactor spends about **US$10–15M/yr** on dedicated (CGD-routed) safety-related items, inclusive of item cost. Dedication services (engineering, testing, documentation) are about **20–30%** of that value. For 94 units this gives:

- About US$1.0–1.4B/yr of dedicated-item value.
- About US$0.2–0.4B/yr of dedication service revenue.

(Calibrate against the US agent's numbers.)

Ex-US scaling (per-unit factors reflect smaller units, lower labour cost and less CGD reliance):

| Segment | Units | Per-unit dedicated-item value $/yr [est] | Item value pool | Dedication service pool (~25%) |
|---|---|---|---|---|
| Tier 1 + 2 steady state | 83 | $6–10M | $0.50–0.83B | $125–210M |
| Canada refurbishment surge (on top of steady state) | — | C$150–300M/yr total (3–5% of C$4–6B/yr capex) | $0.11–0.22B | $30–55M |
| Tier 3 VVER de-Russification | about 33 | $2–4M | $0.07–0.13B | $15–35M |
| Tier 4 France / Japan / UK AGR (very low third-party share) | 98 | $0.5–1M addressable | $0.05–0.10B | $10–25M |
| **Total ex-US** | **about 214** | | **≈ US$0.7–1.3B/yr** | **≈ US$180–325M/yr** |

**Context ceilings [src]:**
- EDF France maintenance and Grand Carénage spend is over €6B/yr.
- Ontario refurbishment pipeline: C$13B + C$5B (Bruce) and C$26.8B (Pickering), mostly spent 2026–2035.
- Sizewell B extension: about £800M.

These show the gross "safety-related replacement and life-extension" spend outside the US is **US$15–25B/yr**. Only a few percent of it flows through commercial-grade dedication.

**Bottom line [est]:**
- **Global (US + ex-US) dedicated-item value: about US$1.7–2.7B/yr.**
- **Global dedication-service revenue pool: about US$0.4–0.7B/yr.**
- Ex-US is about 40–45% of it.
- **Realistic serviceable market for a US-based AI-native dedicator in years 1–5:** Canada, UAE, Spain / Slovenia / Mexico and partner-led Korea / Sweden. That is about **US$60–120M/yr of service revenue**.
- Canada alone is about $30–60M/yr through the mid-2030s, so it is the obvious first export.

## 7. Key uncertainties / to verify
- The EPRI 3002029261 country list behind the 40% figure was not retrieved.
- The IAEA TECDOC-2034 text was not retrievable (HTTP 402). I could not confirm whether it quantifies CG share or third-party dedicators.
- The commercial-grade dedication clauses in CSA N299 / N285 are recalled, not verified (the CSA PDF returned 403).
- Per-unit dedicated-item spend is an assumption and needs a bottom-up check (e.g. utility procurement data, or revenue of known dedicators such as Curtiss-Wright, Paragon (ex-NuTech), Westinghouse, Framatome, Tecnatom).
- Japan restart count and Spanish phase-out dates are recalled.
