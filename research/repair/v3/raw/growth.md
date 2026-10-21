# Growth 2026-2040: US safety-related (NQA-1 / 10 CFR 50 App. B) procurement and CGD demand

As of 2026-10-21. Figures from a fetched or searched source carry the URL. Figures from memory are marked **(recalled)**. Figures I derived or assumed are marked **(est.)** or **(assumption)**. Method: 6 WebSearch calls plus WebFetch of NRC, World Nuclear Association (WNA), World Nuclear News (WNN), ANS and Power Engineering pages. liftoff.energy.gov did not resolve, so Liftoff figures here are recalled.

---

## 1. Baseline fleet

- 94 operable reactors, 96,952 MWe; 41 shut down; WNA lists none as "under construction" (the Kemmerer and Clinch River permits are not yet counted as construction starts). Source: WNA US country profile, https://world-nuclear.org/information-library/country-profiles/countries-t-z/usa-nuclear-power
- The operating fleet is the main buyer today. Assumed baseline: safety-related (SR) parts and materials procurement of about $2.0-3.0B/yr, of which about 30-40% by value goes through commercial-grade dedication (CGD), i.e. about $0.6-1.0B/yr of dedicated items. **(assumption, to be reconciled with the sibling baseline notes.)** EPRI and industry commentary say that for the operating fleet, most SR replacement items by line count (not value) are now dedicated commercial items, because Appendix B OEM suppliers have left the market **(recalled)**.

## 2. Demand drivers and current status

### 2.1 Restarts (about 2.2 GWe in total)
| Plant | MWe | Status (Oct 2026) | Source |
|---|---|---|---|
| Palisades (Holtec, MI) | 805 | Fuel load began late Aug/Sep 2026; it was paused in Sept after an assembly tilted. Restart targeted for 2026. | WNA profile (above); https://oenergetice.cz/en/nuclear-power/palisades-comes-back-to-life-us-nuclear-plant-heads-for-restart-after-four-years |
| Crane CEC / TMI-1 (Constellation, PA) | 819 | NRC final EA issued Sept 2026; $1B DOE loan (Nov 2025). Constellation targets 2027; a PJM analysis suggests grid connection could slip to 2031. Microsoft 20-yr PPA **(recalled)**. | WNA; https://www.ans.org/news/tag-three+mile+island |
| Duane Arnold (NextEra, IA) | 601 | Iowa approval June 2026; DOE loan up to $1.9B closed Sept 2026. Restart early 2029. Google PPA (Oct 2025) **(recalled)**. | WNA; https://www.ans.org/news/tag-fonsi |

What this means for CGD: each restart is a burst of one-time refurbishment spend. It covers steam generator and condenser work, replacement of obsolete I&C, and the backlog of items whose original suppliers are gone, which is where CGD is used heavily. Estimated SR spend per restart: $100-300M **(est.)**. Palisades alone is about a $2B program on DOE/state support **(recalled)**.

### 2.2 Uprates
- NRC: uprates have added about 6 GW over 20 years, and the fleet has signalled about 2 GW more (page updated 2026-09-15). https://www.nrc.gov/reactors/operating/licensing/power-uprates.html
- The May 2025 executive orders call for 5 GW of uprates (WNA). DOE launched the UPRISE uprate program in March 2026 (WNA).
- Committed uprate projects:
  - Southern Co.: 345 MWe across six units at Hatch, Vogtle and Farley, inside a $26.5B DOE loan package (Feb 2026).
  - Vistra: 433 MWe at Beaver Valley, Davis-Besse and Perry, with a conditional $4.2B DOE loan (Oct 2026). Perry is expected online 2031 and all four by 2034.
  - Constellation: up to about 1 GW through the end of the decade.
  - Google/Georgia Power: 96 MW at Vogtle and Hatch.
  - Sources: WNA; https://world-nuclear-news.org/articles/ppas-support-extended-operations-at-vistra-plants ; https://www.power-eng.com/nuclear/google-constellation-doe-nuclear-plant-investment/
- What this means for CGD: an extended power uprate (EPU) replaces large turbine-side equipment, which is mostly non-safety. The SR content is in pumps, motors, valves, heat exchangers, Class 1E electrical and I&C setpoint changes. Assumed SR share of EPU capex is about 20-30%. EPU capex is assumed at about $2,000-4,000/kW. On those assumptions, 3 GW of uprates by 2035 means about $6-12B of capex and $1.5-3B of SR spend over about 8 years, or about $0.2-0.35B/yr **(est.)**.

### 2.3 Subsequent license renewal (SLR, 60 to 80 years)
NRC SLR page: https://www.nrc.gov/reactors/operating/licensing/renewal/subsequent-license-renewal.html
- **Issued: 13 plants / 25 units.** The plants are Turkey Point 3-4, Peach Bottom 2-3, Surry 1-2, North Anna 1-2, Monticello, Oconee 1-3, V.C. Summer 1, Point Beach 1-2, Browns Ferry 1-3, Dresden 2-3, Robinson 2, St. Lucie 1-2 and Hatch 1-2.
- **Under review: 3** (Nine Mile Point 1, Cooper, Ginna).
- **Expected: 23 applications** covering about 29 named units plus 4 unnamed Constellation applications. Submittals run FY2025-FY2034, mostly FY2027-FY2030.
- Total covered by SLR (issued, in review or planned): **about 60-65 of 94 units, roughly two-thirds of the fleet (est.)**.
- A July 2026 NRC proposed rule would lengthen renewal terms from 20 to 40 years (WNA).
- What this means for CGD: SLR aging-management programs plus 80-year operation lead to obsolescence-driven replacement of analog I&C, electrical (cables, breakers, relays), valves and snubbers. The original Appendix B OEM sources for these mostly no longer exist, so this is the most CGD-intensive demand stream. Estimated uplift to fleet SR spend: +10-20% through the 2030s **(est.)**.

### 2.4 Hyperscaler PPAs (they keep the existing fleet running and fund uprates)
- Meta-Vistra (Jan 2026): 20-yr PPAs for more than 2.6 GW (2,176 MW operating plus 433 MW uprates) at Perry, Davis-Besse and Beaver Valley.
- Meta-Constellation Clinton: 1,092 MW, 20 yr from 2027, plus a 30 MW uprate.
- Amazon-Talen Susquehanna: 1,920 MW through 2042, reaching full volume by 2032.
- Amazon-Vistra Comanche Peak: up to 1,200 MW, 20 yr.
- Sources: https://world-nuclear-news.org/articles/ppas-support-extended-operations-at-vistra-plants ; https://www.utilitydive.com/news/meta-constellation-ppa-could-be-first-of-many-deals-for-existing-reactors/750567/
- Sum of these four: about **6.8 GW (est.)**. Microsoft-Crane is 835 MW **(recalled)**.
- Hyperscaler deals for new build **(recalled)**: Amazon-X-energy (5 GW by 2039), Google-Kairos (500 MW), Meta with Oklo and TerraPower (Jan 2026, multi-GW), and Google-NextEra for Duane Arnold.
- Vistra sees up to 3.2 GW more it could contract at Beaver Valley and Comanche Peak.
- What this means for CGD: 20-year offtake makes SLR and uprate capex bankable, which raises fleet SR spend.

### 2.5 US policy
- The May 2025 executive orders set four targets (WNA):
  - 400 GWe by 2050, up from about 100.
  - 10 large reactors under construction by 2030.
  - 5 GW of uprates.
  - At least 3 test reactors critical by 4 July 2026.
- Reactor Pilot Program: 10 companies selected (Aalo, Antares, Atomic Alchemy/Oklo, Deep Fission, Last Energy, Natura, Oklo, Radiant, Terrestrial, Valar). https://www.ans.org/news/article-7543/the-progress-so-far-an-update-on-the-reactor-pilot-program/
  - Criticality results: Antares Mark-0 (June), Valar Ward 250 (June 18), Deployable Energy Unity (June 30), Aalo-X (July 4); Oklo Groves reached criticality in August 2026, making 5 critical by August. https://www.energy.gov/articles/department-energy-celebrates-fourth-criticality-ahead-july-4th-goal ; WNA.
  - These reactors are authorized by DOE, not licensed by NRC. Their QA falls under DOE O 414.1D, which invokes NQA-1 **(recalled)**, and they work through DOE Nuclear Safety Design Agreements (NSDAs). The ANS article does not mention NQA-1.
  - Why this matters: these are startups with small QA staffs that buy mostly commercial parts. They are a natural early wedge for an outsourced, AI-assisted dedicating entity.
- Westinghouse / US government (27 Oct 2025): $80B partnership with Commerce, Brookfield and Cameco for an AP1000 fleet. https://www.ans.org/news/article-7499/westinghouse-signs-80b-contract-to-meet-ai-demand/ ; https://neutronbytes.com/2025/10/28/feds-in-80-billion-partnership-with-westinghouse-to-build-ap1000s/
  - June 2026: DOE conditionally committed up to **$17.5B in loans for long-lead procurement for up to five 2-unit AP1000 projects (10 units)** (WNA).
  - Sept 2026 "Project Power": a US-Korea $120B framework for 6 AP1000 plus 2 APR1400, sites not yet named (WNA).

### 2.6 Large new builds (AP1000)
| Project | Units | Status |
|---|---|---|
| Fermi America (TX) | 4 x AP1000 (about 1,250 MWe each) | COL applications docketed Sept 2025; first unit targeted for 2032 (WNA) |
| V.C. Summer 2-3 (SC) | 2 | Brookfield/Santee Cooper; feasibility done mid-2026; FID Q1 2028 (WNA) |
| DOE-loan AP1000 tranche | up to 10 | Long-lead orders now; sites mostly not yet public |
| Project Power (US-Korea) | 6 AP1000 + 2 APR1400 | Framework only |
| Vogtle 3-4 | 2 (done) | Online 2023-24, about $35B total **(recalled)** |

### 2.7 SMRs and advanced reactors
| Project | Design | Status (Oct 2026) | Source |
|---|---|---|---|
| TVA Clinch River (TN) | GE-H BWRX-300, 300 MWe | NRC construction permit (CP) issued 2026-09-29 after a 14-month review. Construction start not announced; COD about 2033. | https://world-nuclear-news.org/articles/first-construction-permit-issued-for-bwrx300-smr-in-us ; https://www.gevernova.com/news/press-releases/nrc-issues-first-us-construction-permit-bwrx-300-small-modular-reactor-tva-clinch-river |
| OPG Darlington (Canada) | 4 x BWRX-300 | Unit 1 under construction. 4-unit cost C$20.9B **(recalled)**. CNSC rather than NRC, but uses the same US-heavy supply chain. | WNN |
| TerraPower Kemmerer 1 (WY) | Natrium, 345 MWe | CP Mar 2026; non-nuclear construction since Apr 2026; first SR concrete 2027 | WNA |
| X-energy/Dow Long Mott (TX) | 4 x Xe-100 (80 MWe) | CP application Mar 2025; FONSI May 2026; CP decision expected 1H 2027 | WNA |
| Kairos Hermes 1 and 2 (TN) | FHR test / demo | Hermes 1 CP Dec 2023, completion by Apr 2029; Hermes 2 CP Nov 2024 | WNA |
| Oklo Aurora-INL (ID) | 75 MWe fast reactor | DOE pilot path; COD late 2027 to early 2028 | WNA |
| Holtec Palisades SMR-300 (MI) | 2 x 300 MWe | Partial CP application accepted Feb 2026; preliminary safety analysis report (PSAR) Sept 2026 | WNA |
| NuScale / ENTRA1 - TVA | up to 6 GW of NuScale 77 MWe modules | Framework (Sept 2025) **(recalled)**; NuScale 77 MWe design approved May 2025 | WNA (design approval) |
| Blue Energy (TX) | BWRX-300 | Part 1 of CP application submitted | WNN |
| Others in NRC applicant list | Pioneer 1-2 (LWA), UIUC KRONOS, Duke Belews Creek ESP, Eden isotope | | https://www.nrc.gov/reactors/new-reactors/advanced/who-were-working-with/applicant-projects.html |

### 2.8 Naval and DOE complex
- DOE/NNSA nuclear facilities need NQA-1 through DOE O 414.1D and 10 CFR 830 Subpart A **(recalled)**. Examples include Hanford WTP, SRS, the Y-12 UPF, LANL/SRS pit production and INL test reactors.
- NNSA's budget is about $25B/yr, and DOE-EM's is about $8-9B/yr **(recalled)**. NQA-1-graded procurement in the DOE complex is assumed at about $1-2B/yr, and the CGD portion at about $0.1-0.2B/yr **(assumption)**. DOE sites dedicate commercial items routinely under NQA-1 Part II Subpart 2.14 **(recalled)**.
- Naval nuclear propulsion is a large nuclear-quality market: Columbia-class submarines plus about 2 Virginia-class boats a year, around $30B+/yr in shipbuilding **(recalled)**. However, Naval Reactors uses its own NAVSEA/NR QA specs rather than NQA-1 or Appendix B CGD **(recalled)**, so it is only adjacent to this market. It competes for the same forgings, valve and N-stamp capacity, which makes the supplier shortage worse.

## 3. Safety-related procurement per new reactor (est.)

These figures are built from overnight cost and assumed shares, not taken from a single source. Treat them as order-of-magnitude.

| | AP1000 (about 1,117-1,250 MWe) | BWRX-300 / SMR-300 (300 MWe) | Advanced non-LWR (Natrium 345 / Xe-100 4x80) |
|---|---|---|---|
| Overnight cost (NOAK-ish) | $8-11B per unit **(est.; Liftoff NOAK target about $6-10k/kW, recalled)** | $2-4B per unit (FOAK higher; Darlington about C$5B+/unit, recalled) | $2-4B per plant (FOAK, DOE ARDP cost share, recalled) |
| Equipment and materials share | about 35-40% | about 40% | about 40% |
| SR / Q-class share of equipment value | about 35-45% (nuclear steam supply system (NSSS), Class 1E, safety I&C, ASME III piping, valves, supports) | about 30-40% (passive design, fewer SR SSCs) | about 20-30% (Natrium and Xe-100 put more SSCs out of SR scope, e.g. Natrium's energy island) |
| **SR procurement per unit** | **$1.2-2.0B** | **$0.3-0.5B** | **$0.2-0.4B** |
| SR line items per unit | tens of thousands of tagged SR components, plus hundreds of thousands of piece parts and bulk items **(recalled order of magnitude)** | about 5,000-15,000 SR tags **(est.)** | fewer still |
| Share that could go through CGD (by value) | 10-15%. Heavy NSSS components (reactor pressure vessel (RPV), steam generators, reactor coolant pumps (RCPs), pressurizer) and ASME III fabrications need N-stamps and cannot be dedicated. CGD is possible for Class 1E electrical, safety I&C hardware, instruments, small valves and actuators, fasteners, bulk commodities, HVAC, and seismically qualified commercial gear. | 15-20% | 20-30%. Commercial-off-the-shelf (COTS) heavy designs, and DOE-authorized projects lean on CGD. |
| CGD by line count | about 40-60% **(est.)** | 50-70% **(est.)** | 60%+ **(est.)** |
| SR spend timing | spread over about 5-7 yrs, peaking in years 2-4 (long-lead forgings 3-5 yrs ahead of first concrete) | about 4-5 yrs | about 4-5 yrs |

Rule of thumb **(est.)**: about $1.2-1.8M of SR procurement per MWe for large LWRs, about $1.0-1.7M/MWe for LWR SMRs, and about $0.6-1.2M/MWe for advanced non-LWRs. CGD-addressable value is about $0.15-0.3M per MWe.

## 4. N-stamp supplier shortage (ASME data)

- Worldwide holders of an ASME N-type or Quality System Certificate fell from 395 in 2013 to 270 in 2019, a 32% drop. This comes from WNA's *World Nuclear Supply Chain: Outlook 2040*, as reported by WNN, which quotes the EC JRC calling it "the greatest challenge facing the supply chain". https://world-nuclear-news.org/articles/panellists-address-smr-supply-chain-challenges
- About 500 US firms held nuclear stamps in the 1970s-80s, down to about 100 by 2009. The cost of certification is about $1M for firms that held a stamp before, and many times that for first-time applicants. https://www.power-eng.com/nuclear/stamp-of-approval/
- A Sandia study (2021) of N-stamp holders from 1989 to 2020 found that US vendors still hold the most N-stamps worldwide despite consolidation. https://www.sandia.gov/research/publications/details/global-trends-of-asme-n-stamp-certifications-for-nuclear-component-vendors-2021-08-17/
- Other figures **(recalled)**:
  - ASME's certificate directory shows on the order of 500-600 active N-type certificates worldwide, a count of certificates rather than companies.
  - The Liftoff report (2024) flags long-lead large forgings (no US source for RPV-scale forgings, which come from Japan Steel Works, Doosan, Framatome/Creusot), nuclear-grade valves, pumps and qualified I&C as constraints.
  - The number of 10 CFR 50 Appendix B suppliers serving the fleet has fallen sharply since the 1980s.
- Policy response: the draft Atomic Supply Chain Solutions Act would direct DOE to study streamlining N-stamp requirements. https://donalds.house.gov/UploadedFiles/Atomic_Supply_Chain_Solutions_Act.pdf
- **Implication:** demand under the EO pathway, assumed at roughly 10-20 GW under construction by the mid-2030s **(est.)**, would far exceed what about 270 QA-certified companies worldwide can supply. That pushes buyers toward dedicating commercial items wherever the code allows: Class 1E electrical, I&C, bulk items, sub-tier parts. It also pushes up the cost of dedication engineering, testing labs and source verification. Both effects grow the CGD market faster than SR spend overall.

## 5. Growth curve (2026 dollars, $B/yr) (est.)

### 5.1 Safety-related procurement, US (operating fleet plus new build plus DOE-authorized)
| Segment | 2026 | 2030 | 2035 | 2040 |
|---|---|---|---|---|
| Operating fleet baseline (94 to about 97 units) | 2.5 | 2.6 | 2.7 | 2.7 |
| SLR / obsolescence uplift | 0.1 | 0.3 | 0.4 | 0.4 |
| Restarts (one-time) | 0.3 | 0.1 | 0 | 0 |
| Uprates | 0.05 | 0.25 | 0.3 | 0.15 |
| New build, large LWR (base) | 0.1 | 1.0 | 3.0 | 5.0 |
| New build, SMR plus advanced (base) | 0.2 | 0.5 | 1.3 | 2.0 |
| DOE-authorized pilot plus DOE complex NQA-1 | 1.1 | 1.4 | 1.5 | 1.6 |
| **Total, base case** | **about 4.4** | **about 6.2** | **about 9.2** | **about 11.9** |
| Total, low case (AP1000 delays, few SMRs) | 4.3 | 5.2 | 6.0 | 6.8 |
| Total, high case (EO-aligned: 10 large units under construction by 2030, about 5-8 GW/yr starts late 2030s) | 4.5 | 9.0 | 16 | 22 |

Assumptions behind the base case **(est.)**:
- Large LWR units under construction: about 4 in 2030, about 12 in 2035, about 20 in 2040.
- SR spend per large unit: about $0.25B/yr while under construction.
- SMR and advanced units under construction: about 6 in 2030 (about 0.5 including Darlington-linked US supply and pilot follow-ons), about 15 in 2035, about 25 in 2040.
- SR spend per SMR or advanced unit: about $0.08B/yr.

### 5.2 CGD demand: value of items dedicated (and service fee pool)
| Segment | CGD share | 2026 | 2030 | 2035 | 2040 |
|---|---|---|---|---|---|
| Operating fleet, SLR, restarts, uprates | 30-40% | 0.95 | 1.1 | 1.2 | 1.15 |
| New build, large LWR | 12% | 0.01 | 0.12 | 0.36 | 0.6 |
| New build, SMR plus advanced | 20% | 0.04 | 0.10 | 0.26 | 0.4 |
| DOE pilot plus DOE complex | 10-15% | 0.13 | 0.18 | 0.2 | 0.22 |
| **CGD item value, base** | | **about 1.1** | **about 1.5** | **about 2.0** | **about 2.4** |
| CGD item value, low | | 1.1 | 1.35 | 1.5 | 1.6 |
| CGD item value, high | | 1.15 | 2.1 | 3.3 | 4.5 |
| **Dedication services fee pool (about 25-35% of item value, assumption)** | | **about $0.3-0.4B** | **about $0.4-0.5B** | **about $0.5-0.7B** | **about $0.6-0.85B** |

Implied growth in the base case:
- SR procurement: about 2.7x from 2026 to 2040, a CAGR of about 7%.
- CGD item value: about 2.1x, a CAGR of about 5.5%.
- High case: CGD grows about 4x, a CAGR of about 10%.

The new-build share of CGD rises from about 5% today to about 40% by 2040 in the base case. Until about 2032, the operating fleet (SLR, obsolescence, uprates) remains the dominant and most CGD-intensive buyer.

## 6. Key takeaways for the startup
1. Near-term demand for 2026-2030 comes mainly from the existing fleet: SLR for about two-thirds of units, PPA-funded uprates and restarts. Large new build does not produce meaningful SR purchase-order volume until about 2029-2031, when long-lead forgings are released before first concrete.
2. The fastest-growing and least served segment is the set of DOE-authorized pilot reactors and advanced non-LWRs: 5 critical by August 2026, with Kemmerer, Hermes, Aurora and Long Mott to follow. They have heavy COTS content, small QA teams and NQA-1 obligations.
3. The N-stamp and Appendix B supplier base shrank by about 30% from 2013 to 2019 and by about 80% in the US since the 1980s. That structural scarcity is why CGD's share of SR procurement should rise.
4. The largest uncertainty is whether the 10-units-by-2030 AP1000 tranche actually reaches FID. The DOE loan commitment is $17.5B for up to five two-unit projects. The gap between the low and high cases by 2040 is about 3x.
