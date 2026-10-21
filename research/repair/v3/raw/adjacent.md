# Adjacent markets for the CGD engine (AI technical evaluation + deterministic traceability checker + robotic acceptance testing, human-signed under a QA program)

Date: 2026-10-21. Method: I read prior notes v2/raw/d01.md (DoD sole-source demand), g03.md (DLA SAR pathway) and c12.md (nuclear CGD/AI landscape), ran 6 WebSearches, did several WebFetches, and pulled USAspending API data myself.
Tags: **(recalled)** = from memory, not re-verified. **(est.)** = my own estimate, with the reasoning shown. Market-research-vendor figures are low confidence.

## Summary table

| # | Market | Spend anchor | Growth | Engine fit | Barrier to entry |
|---|---|---|---|---|---|
| 1 | Nuclear EQ / seismic testing services | No public figure. US EQ+seismic services est. $150-300M/yr | 5-10%/yr (SMR/AR first-of-a-kind quals, restarts, life extension to 80 yrs) | Medium. Strong on EQ files and qualification-by-similarity/analysis. Weak on physics: shake tables, LOCA chambers and irradiation are capital-heavy | Large shake tables, LOCA/irradiation facilities, 40-yr reputations |
| 2 | DOE complex NQA-1 procurement and CGD | DOE contract obligations $48.4B FY2025; EM about $8.5B; NNSA $24.1B | Flat to slightly up; NNSA rising, EM flat | High. Same NQA-1 and CGD logic (DOE O 414.1D, EFCOG CGD guidance (recalled)) | M&O approved-supplier lists, NQA-1 audits, site-specific procedures |
| 3 | Naval nuclear / NAVSEA Level I / SUBSAFE | Naval Reactors $1.95B FY25 enacted, $2.35B FY26 request | Up strongly (submarine industrial base) | Low inside naval nuclear propulsion; medium for non-nuclear Level I/SUBSAFE traceability and for harvested-part refurbishment | Clearances, NOFORN/NNPI, ITAR; NR does not use CGD |
| 4 | Nuclear reverse engineering, obsolescence, digital I&C | Digital I&C upgrades $4.2B global 2025 (vendor report, low confidence); about $25-100M per unit | 6-7% CAGR (vendor) | High for RE + CGD packages and digital/software dedication. Medium for full I&C system replacement (an OEM/integrator game) | NRC digital I&C review (BTP 7-19, ISG-06), EPRI digital CGD guidance |
| 5 | DLA SARs / defense alternate sourcing | DLA non-competed $10.38B FY25; aviation about $3.4B; DoD-wide $15-20B non-competed components and repair | Steady; policy tailwind (right-to-repair, data rights) | High on the package side (same structure: design basis to critical characteristics to evidence to signer). ESA review is the bottleneck | ESA queues; CSI rules (DFARS 209.270); first-article testing |
| 6 | Fusion and advanced-reactor supply chains | Fusion supply-chain spend $538M (2025), projected $681M (2026). AR: ARDP about $3.2B federal (recalled) plus private build-outs | Fusion +25-27%/yr; AR spend steps up with the first builds 2026-2030 | AR: high (Appendix B/NQA-1 applies; CGD is how ARs cut cost). Fusion: low-medium (byproduct-material framework, no NQA-1 mandate) | Small near-term volume; customers few and concentrated |
| 7 | Medical device service parts; EU rail ECM; (FAA PMA) | Medical equipment service about $40-50B global (recalled); rail ECM: a few hundred certified ECMs in the EU (recalled) | Mid single digits | Low-medium. Neither regime has a formal "dedication" act to sign. FAA PMA is the strongest non-nuclear analog | Different regulators; low price per determination |

**Ranking for the same engine** (by fit, price per approval and accessibility):
(a) DLA SAR / defense alternate sourcing: largest money pool; the d01/g03 work already maps the pathway.
(b) Nuclear RE/obsolescence plus digital CGD: the same customer as the core business, so a natural upsell.
(c) DOE complex NQA-1 CGD: the same QA regime, a different buyer.
(d) Advanced-reactor supply chains: high fit, but the volume arrives later.
(e) EQ testing: better treated as a partner (Element, Curtiss-Wright) than a target.
(f) Fusion, naval nuclear, medical, rail: low.

---

## 1. Nuclear equipment qualification (IEEE 323 / 344, 10 CFR 50.49) and seismic testing

**What it is.** Harsh-environment EQ under 10 CFR 50.49 and IEEE 323 runs in this order: thermal and radiation aging, then a seismic test (IEEE 344), then a LOCA/HELB simulation. Mild-environment and seismic qualification are often done as part of CGD. The output is a qualification report plus the maintenance of the plant's EQ file.

**Players.**
- **Element** (absorbed NTS, which had absorbed Wyle (recalled)). Its page claims "#1 Nuclear qualification provider in US & UK" and "Over 4,000 previously qualified items from other OEMs", plus 40+ yrs of experience. It runs the Huntsville, AL Nuclear Center of Excellence (ICAP certified, radioactive material licensed), the "largest commercially available electrodynamic shakers", and biaxial/triaxial tables. It also offers CGD and cybersecurity validation. UK work runs via the EQSA alliance (Wood Nuclear, Tecnatom, TÜV Rheinland) and a Bristol University seismic partnership. https://www.element.com/product-qualification-testing-services/nuclear-equipment-qualification ; https://www.element.com/product-qualification-testing-services/seismic-testing
- **Paragon Energy Solutions** (now Mirion; c12): 4 seismic shake tables, 12 aging ovens, 6 environmental chambers, testing to IEEE 323-1974/1983. https://paragones.com/products-services/qualification-dedication
- **Curtiss-Wright** (NLI, Scientech, and the qualification labs formerly Wyle's Nuclear Qualification (recalled)). It sits inside the Naval & Power segment. CW total sales are about $3.1B (2024) and the commercial nuclear aftermarket is roughly $0.3-0.5B (recalled, not verified). Its federal contract obligations in FY25 were small: Navy $71M, DLA $24M, USAF $22M (USAspending, my pull).
- Others: Kinectrics (Canada), Framatome/Westinghouse in-house, and Korean and Japanese labs (recalled).

**Size.** No public market figure was found (search returned none).
- (est.) The ~94 US units each spend low single-digit $M/yr on EQ program maintenance and on qualification of replacement parts (recalled range). Add new qualification for SMR/AR components and vendor-paid qualifications.
- Result: US nuclear EQ+seismic **testing and analysis services about $150-300M/yr**; global perhaps 2x.
- Growth (est.) 5-10%/yr, from 80-year subsequent license renewals (which re-examine EQ aging), restarts (Palisades, Crane; recalled) and first-of-a-kind AR/SMR qualification.

**Fit.**
- *Strong:* AI drafting of qualification plans, similarity analyses ("qualification by similarity", which Element's 4,000-item library exploits), EQ file reconciliation, and aging calculations (Arrhenius). The traceability checker maps cleanly onto EQ file audits, which NRC inspects.
- *Weak:* the physics. Seismic tables, LOCA chambers and Co-60 irradiation are capital-heavy, licensed, and few. Robotic acceptance testing in a CGD sense (dimensional, hardness, PMI, functional) is a different class of test.
- *Play:* partner and subcontract the physics to Element or Curtiss-Wright. Sell them, or utilities, AI-drafted qualification by analysis/similarity and EQ file maintenance. Do not build a seismic lab.

## 2. DOE complex NQA-1 procurement (Hanford, Savannah River, national labs, NNSA)

**Spend anchors.**
- DOE FY2025 contract obligations were **$48.4B** (USAspending awarding-subagency query, contracts A-D, FY2025, my pull). DOE total obligations were $98.5B (USAspending agency budgetary resources).
- Top FY25 prime recipients (all M&O / cleanup contractors):

  | Recipient | FY25 obligations |
  |---|---|
  | Sandia NTESS | $5.67B |
  | Triad (LANL) | $5.20B |
  | LLNS | $3.63B |
  | UT-Battelle (ORNL) | $2.68B |
  | CNS (Y-12) | $2.54B |
  | Honeywell FM&T (KCNSC) | $2.11B |
  | Savannah River Nuclear Solutions | $1.95B |
  | Battelle Energy Alliance (INL) | $1.94B |
  | PanTeXas (Pantex) | $1.92B |
  | Fluor Marine Propulsion (Naval Reactors labs) | $1.72B |
  | Savannah River Mission Completion | $1.06B |

- FY25 subawards reported under DOE contracts: $5.47B. FFATA subaward reporting is incomplete, so this is a floor on M&O downstream purchasing.
- Budget, from CRS R48551 (FY26 request), with FY25 enacted implied from the stated reductions:

  | Program | FY25 enacted (implied) | FY26 request |
  |---|---|---|
  | Environmental Management | $8.48B | $8.09B |
  | NNSA | $24.1B | $24B discretionary + about $6B reconciliation |
  | Office of Science | $8.24B | $7.09B |
  | Nuclear Energy | $1.69B | $1.28B |

  https://www.everycrsreport.com/files/2025-05-30_R48551_b60b12ff9bc7c1fbcc914a1e5801551312aa164c.html
- The DOE FY26 budget-in-brief table gives: Naval Reactors $1.946B FY25 enacted, $2.346B FY26 request; defense EM $7.285B, $6.956B; NNSA total $24.135B, $30.042B including reconciliation. https://www.energy.gov/sites/default/files/2025-06/doe-fy-2026-budget-approps-summary-v3.pdf
- EM's FY2027 request is **$8.176B**, with Savannah River $1.785B and Office of River Protection (Hanford tank waste) $1.945B (EM SSAB chairs deck, Apr 2026). https://www.energy.gov/sites/default/files/2026-05/EM%20SSAB%20Chairs%20Apr%202026%20Budget%20Du%20Bosq%20DOE.pdf

**Regime.**
- DOE O 414.1D and 10 CFR 830 Subpart A require NQA-1 for nuclear facilities.
- CGD is used heavily for safety-class and safety-significant SSCs. EFCOG publishes a CGD guide and DOE has CGD training material (recalled). The M&O usually is the dedicating entity, or it buys from NQA-1 suppliers on its Evaluated Supplier List.
- Recurring DOE IG and DNFSB findings cover suspect/counterfeit items and CGD weaknesses (for example at WTP, Hanford; recalled).

**Size of the CGD-relevant slice (est.).**
- M&O and cleanup contractors buy materials, equipment and subcontracted services worth perhaps 30-40% of their obligations, roughly $15-20B. That covers construction (WTP, Savannah River's SRPPF pit plant, UPF at Y-12) and operations.
- The safety-class/safety-significant, nuclear-QA-graded items share is perhaps 3-8%, about **$0.5-1.5B/yr of NQA-1 graded procurement**.
- The dedication engineering, test and documentation layer on top of that is perhaps **$50-150M/yr**, mostly performed in-house by M&O procurement engineering today.
- Growth: NNSA capital (pits, UPF, lithium, tritium) is rising and EM is roughly flat.

**Fit: high.**
- Same standard (NQA-1), same CGD method (EPRI NP-5652-style critical characteristics), and the same counterfeit/suspect-item pain.
- Differences:
  - The buyer is a contractor with site procedures, not a utility.
  - Classified and export-controlled items exist at NNSA sites.
  - Supplier-list entry requires an NQA-1 audit by each M&O. DOE has no direct NUPIC equivalent, though EFCOG shared audits exist (recalled).
- *Wedge:* EM cleanup sites (Hanford WTP/ORP, SRS) and INL, where items are mostly unclassified commercial industrial goods (pumps, valves, instruments) dedicated for safety-significant service.

## 3. Naval nuclear and NAVSEA Level I / SUBSAFE

**Spend anchors.**
- Naval Reactors: $1.946B FY25 enacted, $2.346B FY26 request (DOE summary above).
- The NR labs (Bettis, KAPL) are run by Fluor Marine Propulsion: $1.72B FY25 obligations (my USAspending pull).
- BWXT makes naval reactor cores and components; its Government Operations revenue is about $2B/yr (recalled).
- The submarine industrial base (SIB) receives multi-$B/yr of supplier-development money (recalled, about $3-4B/yr across FY24-26 in shipbuilding accounts).

**Can a private firm play?**
- **Naval nuclear propulsion plant (NAVSEA 08 / NR):** effectively no, for a dedicating-entity model. NR does not use commercial-grade dedication. Its material comes under NR's own specs from a small, cleared, NR-audited supplier base, and the information is NNPI (recalled).
- **Non-nuclear Level I and SUBSAFE:** yes. Level I material (NAVSEA 0948-LP-045-7010 Material Control Standard (recalled), S9510-AB-PRC-010/SUB) needs objective quality evidence (OQE) and 100% traceability. Many small private suppliers hold Level I programs, for example a 5-yr IDIQ for "All Level 1 and SUBSAFE material" (NAICS 332999, start about May 30, 2026). https://govconinabox.com/explore/federal-contracting-opportunities/5-year-idiq-all-level-1-and-subsafe-material-310cfad8833646118a1355388a43de83
- **Harvesting and refurbishment of parts from inactivated submarines:** NAVSEA sources-sought N00024-25-R-4307 (notice Mar 27, 2026) for a MAC IDIQ. Lot 1 (Critical) falls under NAVSEA Note 5000. The scope includes "obsolescence management, including reverse engineering of obsolete components, where allowable". Government approval is needed before the build phase, and all technical data and analyses go to the government for review. https://samsearch.co/gov-explore/federal/nuclear-powered-submarine-material-harvesting-and-refurbishment/N00024-25-R-4307
- **Other demand signals:** a Puget Sound NSY SUBSAFE proprietary-parts supply notice, a NUWC Newport electrical hull fitting repair notice (Jul 2026), and an IMEC scouting notice for submarine valve bodies (2026-452). https://www.imec.org/wp-content/uploads/2026/08/SSO_2026-452.pdf ; https://www.cleat.ai/government/contracts/specialized-parts-and-components-supply-au2p

**Fit.**
- Medium for the traceability checker plus OQE package generation for Level I/SUBSAFE suppliers, and for RE of harvested and obsolete parts.
- Low for anything inside NR.
- The engine's "dedication" act maps onto "Level I certification of a refurbished or reverse-engineered part", but approval stays with the government (NAVSEA/SUPSHIP), not the firm.
- Size of the accessible slice (est.): Level I/SUBSAFE non-nuclear material spend of perhaps $0.5-1B/yr, with the documentation/OQE/RE services layer in the tens of $M.

## 4. Nuclear reverse engineering, obsolescence replacement, digital I&C

**Spend anchors.**
- Vendor estimate: the global nuclear digital I&C upgrade market is **$4.2B (2025) rising to $7.8B by 2034, a 6.8% CAGR**; Framatome is named as a leader. Low confidence. https://marketintelo.com/report/nuclear-digital-ic-upgrade-market
- SNS Insider puts the broader nuclear plant digitalization market at $3.15B (2025) and $9.27B (2035), with the US at about $1.05B. https://www.snsinsider.com/reports/nuclear-power-plant-digitalization-market-10913
- Per-unit cost: about **$100M per unit** for worldwide digital upgrades (informal industry survey), and as low as $25M for RPS, ESFAS and NIS scope only. https://neimagazine.com/?p=53275
- Hashemian (around 2013) put US digital I&C upgrades at $5.4B over 10 years. https://www.nsenergybusiness.com/?p=171639
- RE/obsolescence services:
  - Paragon was acquired by Mirion (recalled: about $585M, 2025; not verified). It reports 12M+ parts, 22,000+ components dedicated, and 175 facilities served (c12).
  - Park Nuclear presented at NUOG 2026 (c12).
  - POMS is the industry obsolescence database (c12).
- US utility obsolescence plus RE plus CGD services: (est.) $200-400M/yr, overlapping the core CGD market.

**Fit.**
- **High for component-level RE + CGD.** This is the core engine: a CT/metrology "digital twin" produces both the RE TDP and the technical evaluation.
- **High-potential but hard for digital CGD.** This is software dedication of commercial digital devices: EPRI 3002011816 / TR-106439 (recalled), plus NRC BTP 7-19 diversity and defense-in-depth and ISG-06 (recalled). AI static analysis, test generation and failure-mode analysis address the most painful bottleneck (c12).
- **Low for whole-system I&C replacement.** That is a $25-100M/unit integrator game: Westinghouse, Framatome, Curtiss-Wright, Mirion/Paragon HIPS, Lockheed (the Lockheed point is recalled). The engine sells into those projects as a subcontractor for the dedication of commercial digital sub-components (PLCs, smart transmitters, breakers with electronic trip units).
- Growth: tied to 80-year licence renewals and the DOE LWRS program's push for digital main-control-room modernization (recalled).

## 5. DLA Source Approval Requests and defense alternate sourcing

**Spend anchors** (from v2 d01/g03, USAspending pulls):
- DLA FY2025: **$10.38B non-competed** against $45.56B competed.
- Non-competed engineered aviation hardware (FSGs 15/16/28/29): **about $3.4B/yr**.
- DoD-wide non-competed component, accessory and repair spend: **about $15-20B/yr**. This includes J0xx repair at $11.8B non-competed.
- GAO-25-107468: most sole-source justifications trace to inadequate technical data or rights.
- StandardAero bought Aero Turbine Inc. for $120M plus a $21M earnout, explicitly for "military Source Approval Request expertise". https://www.sec.gov/Archives/edgar/data/2025410/000095017024126325/saro-ex99_1.htm

**SARs per year.**
- DLA Land & Maritime alone, FY16: 211 SARs received, 55 approved, 184 pending. The pending pile carried 12x the savings of the approved one.
- The RPPOB program: 742 bailment requests, of which 55 became SARs. https://ndia.dtic.mil/wp-content/uploads/2016/DLA/SourceApprovalRequestsCastingandForging.pdf
- (est.) Across DLA Aviation, L&M and Troop Support plus the service ESAs: roughly **1,000-3,000 SARs/yr**. No published total exists (g03).
- Typical elapsed time is 5-6 months nominal and 12-30 months real. The JMS example took about 2.5 years for one NSN (g03).
- (est.) At $20-80k package cost each, applicant-side SAR preparation spend is **about $50-200M/yr**. The latent pool is far larger: AMSC C/D/P/Q/R items whose breakout becomes economic if package cost falls 10x.

**Fit: high.**
- The structure is identical: design basis, then critical characteristics, then acceptance evidence (first article, dimensional, material, FFF), then a liable signer.
- Differences:
  - The approval authority is the government ESA, not the firm. The firm's "signature" is a package, not a dedication.
  - CSIs need DCA approval under DFARS 209.270.
  - Robotic first-article dimensional and material testing maps directly onto AFMC Form 260-type FAT.
- The wedge options in g03 apply: an ESA reviewer workbench, an AMSC re-screening engine, and portfolio SARs.

## 6. Fusion and advanced-reactor supply chains

**Fusion.**
- FIA's 4th supply-chain report (Jun 2026): fusion-company supply-chain spend was **$538M in 2025, up 25%**; FIA projects **$681M in 2026, up 27%**.
- Survey base: 25 fusion companies and 67 suppliers. 75% of suppliers invested in capacity; 69% lack long-term visibility.
- Bottlenecks: power systems 48%, heat management 44%, vacuum vessels and pumps 32%.
- The report does not mention QA, NQA-1 or ASME. It recommends shared standards, specs and testing protocols.
  - https://www.world-nuclear-news.org/articles/fusion-supply-chain-spend-up-big-challenges-remain
  - https://www.neimagazine.com/news/fusion-supply-chain-spending-surges/
- The 2025 edition reported $434M (2024 spend, +73%). https://world-nuclear-news.org/articles/fusion-supply-chain-sees-growth-in-business
- Regulation: the NRC regulates fusion machines under the byproduct-material framework (Part 30), not as utilization facilities. The rule was finalized around 2025-26 (recalled). No Appendix B/NQA-1 mandate follows, so QA is graded and voluntary (many adopt ISO 9001 or NQA-1-lite).
- Fit: **low-medium.** There is no legal CGD act to sell. The traceability checker and supplier-qualification engine could still serve fusion developers that self-impose NQA-1, such as CFS and Helion, which have signed PPAs (recalled). The pool is small: well under $1B of total supply spend.

**Advanced reactors (fission).**
- Part 50/52 and the new Part 53 all keep Appendix B (recalled), so NQA-1 applies to safety-related SSCs.
- Developers (TerraPower Natrium at Kemmerer, X-energy/Dow, Kairos Hermes 1/2, NuScale/ENTRA1-TVA, GE-Hitachi BWRX-300 at OPG Darlington and TVA Clinch River, Oklo, plus the DOE reactor pilot program; recalled) all lean on CGD of commercial items to escape N-stamp costs.
- DOE ARDP federal share is about $3.2B across Natrium and Xe-100 (recalled). Total announced AR/SMR capex in North America exceeds $20B for the first wave (recalled, est.).
- (est.) Safety-related procurement is perhaps 10-20% of equipment spend, and the CGD and qualification services layer is perhaps 3-5% of that. That gives about **$20-80M/yr in 2026-2028**, rising toward $100-300M/yr by the early 2030s if the first fleets proceed.
- Fit: **high.** These are greenfield, digital-first customers with no legacy CGD departments. Many have no NUPIC-audited dedication capacity in-house. AI-drafted technical evaluations for novel environments (sodium, molten salt, high-temperature helium) need more engineering judgement. Robotic acceptance testing applies as-is.

## 7. Other regulated commercial-grade analogs

**Medical device service parts (FDA).**
- FDA's final remanufacturing guidance (May 10, 2024) separates "servicing" from "remanufacturing". Servicers generally are not subject to device requirements; remanufacturers are. Critics note servicers self-assess the boundary. https://www.morganlewis.com/pubs/2024/05/fda-clarifies-distinction-between-device-remanufacturing-and-servicing-in-final-guidance
- FDA's 2018 report found third-party servicing critical and the evidence too weak to justify burdensome rules. https://www.fda.gov/media/113431/download?attachment
- Market: global medical equipment maintenance is about $40-50B (recalled; no reliable figure found this session).
- Fit: **low-medium.**
  - There is no dedication signature with liability. The analogous artifact is a documented "not remanufacturing" determination, plus parts equivalence for non-OEM parts in imaging (CT/MRI tubes, coils).
  - The price per determination is low.
  - A possible product is an AI-drafted remanufacturing-vs-servicing assessment plus a parts-equivalence file for ISOs (independent service organizations).

**EU rail ECM (Entity in Charge of Maintenance, Reg. (EU) 2019/779).**
- Every vehicle needs a certified ECM. ERADIS lists ECM certificates, but I could not get counts (https://www.era.europa.eu/domains/registers/eradis_en ; database at https://eradis.era.europa.eu/).
- (recalled) There are several hundred ECM certificates EU-wide.
- Spare-part substitution in rail is governed by ECM procedures plus the CSM risk assessment (Reg. 402/2013), not by a dedication act.
- Fit: **low.** The logic is analogous (part equivalence, risk assessment, traceability) but fragmented, priced low, and needs European presence. US FRA has no equivalent regime.

**FAA PMA / 14 CFR 21 (the strongest non-nuclear analog, not in the brief).**
- PMA by test and computation, or by identicality, is the closest analog: design basis, then substantiation, then FAA approval.
- PMA parts are about 3-7% of the commercial aftermarket, roughly $1-2B/yr (recalled). HEICO is the scaled incumbent.
- Fit: high in structure, but the FAA (or an ODA) is the approver.

## Cross-cutting read

1. **The engine has two separable products.** Only nuclear (commercial and DOE) gives the firm the legal *signature* (10 CFR 21 dedicating entity).
   - (a) A *package generator plus traceability checker*, which works in every regime above.
   - (b) A *dedication signature*, which only works where the regime lets a private QA program accept the item.
   - In DLA, NAVSEA, FAA and FDA the signature belongs to the government or the regulator. There the business is "package factory plus applicant", or a reviewer workbench.
2. **Dollar ranking of addressable services layers (est.):**

   | Regime | Addressable services layer (est.) |
   |---|---|
   | DLA/DoD alternate sourcing | $50-200M package prep today; latent pool billions |
   | Nuclear RE/obsolescence | $200-400M |
   | Nuclear EQ testing | $150-300M (mostly physics) |
   | DOE NQA-1 CGD | $50-150M |
   | Advanced reactors | $20-80M now, $100-300M early 2030s |
   | Naval Level I | tens of $M |
   | Fusion | under $10M |

3. **Robotic acceptance testing travels best** to DLA first-article testing, DOE CGD, and AR CGD. **AI technical evaluation travels best** to digital CGD and to SAR packages.

## Gaps
- No published EQ/seismic services market size. Curtiss-Wright segment detail was not verified (its 10-K was not fetched).
- No published DLA-wide SAR count.
- DOE spend on safety-class/NQA-1 graded items is not broken out anywhere public; the estimate above is a top-down guess.
- ECM certificate counts and the medical servicing market figure were not verified.
- The Mirion/Paragon deal value is recalled.
