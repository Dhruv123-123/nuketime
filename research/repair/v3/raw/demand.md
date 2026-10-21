# Demand evidence: buyer pain and willingness to adopt (AI-native CGD entity)

Research date: 2026-10-21. Search budget used: 6 WebSearch calls plus WebFetch. Figures marked (recalled) come from memory and were not checked against a source this session.

## 1. Buyer pain: supply chain, dedication, obsolescence

### Supplier base and lead times
- **Paragon Energy Solutions, CEO Doug VanTassell, "Nuclear Supply Chain Innovation and Collaboration" (Nuclear News, Aug 2024)**: says the industry is at an "all-time low number of qualified parts and component suppliers," after a slow-moving crisis of about 20 years. Suppliers left because the QA burden was too costly for the volume of demand. Because of this, the industry relies on "third parties or limited internal resources" for CGD, qualification of alternatives, utility-to-utility transfers, repair and reverse engineering.
  - Lewis Dawson (Dominion Energy) says lead times for engineered or highly manufactured items are "significantly understated," and that "in a matter of weeks, lead time can increase by months or even years."
  - Parts arrive after their scheduled work windows. Some parts fail receipt inspection or bench testing, which adds more delay.
  - Plants usually learn a part is obsolete only when they try to buy it.
  - URL: https://paragones.com/nuclear-supply-chain-innovation-and-collaboration-keeping-the-nuclear-supply-chain-viable-through-change/
- **"Over 60% of nuclear-qualified manufacturers have left the market or dropped nuclear programmes."** Source: NEI Magazine, Azeez/Mizuno/Tume, 30 Nov 2001 (Candu context). The figure is unsourced ("it has been estimated") and 25 years old. It is widely repeated but weak, so it should not be the headline stat. https://neimagazine.com/?p=52674
- (recalled) The number of N-stamp holders in the US fell from about 600 in 1980 to about 200 in the 2000s. Check against ASME before citing.

### EPRI view (procurement engineering)
- **Marc Tannenbaum (EPRI Technical Executive, procurement engineering and supply chain), "Nuclear supply chain challenges and opportunities," Nuclear News, April 2019.** https://wx1.ans.org/pubs/magazines/download/a_1157
  - EPRI runs a twice-yearly **Joint Utility Task Group (JUTG) on procurement engineering**. This is a ready-made buyer community and a channel to reach buyers.
  - Suppliers report a "noticeable decrease in orders for safety-related items." Several suppliers have announced they will discontinue product lines or their entire nuclear QA programs. Utilities missed "last-time-buy" notices because the notices did not reach the right people. JUTG created a **Pending Obsolescence Response Protocol** in response.
  - Even with a good program, "the first notification that an item is obsolete will occur after a licensee contacts the supplier to order the item." In other words, obsolescence often turns up during an emergent need.
  - CGD and equivalency evaluations are "**labor intensive**." Technical evaluations "involve engineering judgment and can therefore be subjective." Practice differs between OEMs, **third-party dedicators** and licensees.
  - EPRI was building **pre-built technical-evaluation data for frequently dedicated items**: functions, then failure modes, then critical characteristics, held in a web form to "quickly complete" evaluations. This is a direct precedent for templated or AI-assisted dedication, and EPRI is both a potential partner and a potential competitor.
  - One third-party dedicator was trying to cut cost by dedicating to the end-use application instead of a standard specification.
- **Tannenbaum, OECD-NEA workshop, Paris, 7 Nov 2018**: names the areas of CGD difficulty as bounding functions when the end use is unknown, FMEA, and identifying critical characteristics. Reverse engineering is an "important tool for addressing obsolescence," with "inherent risk," and "design control cannot be assumed." Licensees were increasingly asking how to avoid dedication altogether. https://www.oecd-nea.org/nsd/workshops/nscm2018/presentations/
- EPRI guidance: 3002002982 (CGD guideline, Rev 1 to NP-5652/TR-102260, 2014), endorsed with conditions by **NRC RG 1.164 (2017)**. 3002010685 covers critical spares. TR-107372 covers reverse engineering.
- **Old utility survey (NUOG era, about 2000s)**: about 25% of components likely to need replacement are obsolete (12% mechanical, 33% electrical, 27% I&C). Direct obsolescence cost is estimated at **over $1M per plant per year**. This came from a search snippet. The source PDF (UNT digital library 840372.pdf) returned 503 and could not be verified. https://digital.library.unt.edu/ark:/67531/metadc780247/m2/1/high_res_d/840372.pdf
- 2026 Korean Nuclear Society paper (26S-560): attributes the sharp rise in obsolescence to small, varied purchase quantities and the cost of keeping a nuclear QA program. Proposes reverse engineering plus CGD. https://www.kns.org/files/pre_paper/55/26S-560-손권우.pdf
- Industry players already selling obsolescence and CGD services: Curtiss-Wright (seismic, environmental and LOCA testing) https://cwnuclear.com/products-and-services/obsolescencesolutions ; Paragon https://paragones.com/markets/commercial-nuclear/ . (recalled) Also Framatome, Westinghouse, Ultra/NSS, Nuclear Logistics (AZZ), Sargent & Lundy, ENERCON, Kinectrics, Global Nuclear Associates and others.

### NRC enforcement pressure on procurement and CGD
- An NRC 2018 vendor workshop reported a "recent increase of inspection findings in the areas of procurement and oversight of suppliers," and a revised RIS was in progress. https://www.nrc.gov/docs/ML1815/ML18150A373.pdf
- NRC presentations cite inadequate dedication as a typical vendor finding. https://www.nrc.gov/docs/ML1206/ML12060A291.pdf
- Part 21 history: commercial-grade items are outside Part 21 until dedication is complete. The dedicating entity then takes on Part 21 reporting responsibility. https://www.nrc.gov/docs/ML0834/ML083400299.pdf (2008 NRC history deck)
- NUPIC letter to NRC, 12 Jun 2026, on retention requirements for commercial-grade survey reports. CGD paperwork rules are still an active topic. https://www.nrc.gov/reactors/new-reactors/how-we-regulate/oversight/quality-assurance/nupic-industry.html

### Outages and derates caused by parts
- I found **no clean 2025-26 US public case** of an outage extended specifically because a CGD-dedicated part was late. Utilities do not disclose outage durations in this detail.
- Nearest cases:
  - **Cernavoda Unit 2 (Romania)**: tripped 4 May 2026 on a transformer insulator fault. The shutdown was extended while a backup transformer was swapped in. https://m.bvb.ro/infocont/infocont26/SNN_20260507111742_CR-Cernavoda-NPP-U1-U2.pdf
  - **PSEG Salem**: refueling outage extended for bolt degradation repairs (older). https://www.power-eng.com/nuclear/pseg-temporarily-without-more-than-2-200-mw-of-nuclear-generation/
- Economics (recalled): one day of outage or lost generation on a 1 GW unit costs about $0.5-1.5M+ in replacement power and lost revenue, depending on the market. Since 2024, PJM/ERCOT prices and data-center PPAs have raised the value of each MWh. A single avoided outage day can justify an expedited-dedication premium.
- Recommended follow-up: search NRC LERs and Part 21 reports in ADAMS for cases where a part was unavailable during an outage. Also check Constellation and Vistra earnings calls for "supply chain" mentions; these were not covered this session.

## 2. How utilities buy

- **Buyer roles**: procurement engineering (writes the technical evaluation and CGD plan, or reviews a third-party dedicator's), supply chain/purchasing (POs, expediting), QA/supplier quality (approved supplier list, audits), plus the system engineer or maintenance planner who raises the need. Outage managers feel the urgency. EPRI JUTG is the peer forum for procurement engineering (EPRI NN 2019).
- **Approved supplier list (ASL/QSL)**: a utility can issue a safety-related PO only to a supplier on its approved list. That requires a supplier audit, normally the NUPIC joint audit, plus a commercial-grade survey of any sub-suppliers whose processes are credited.
- **NUPIC** (https://www.nupic.com/; NRC page above):
  - Formed in 1989. Members are "all domestic and several international" nuclear utilities.
  - Audits run on a standard **33-month cycle**.
  - **To get a NUPIC audit, a supplier needs at least five NRC-licensee or international-operator customers, and sponsorship by five NUPIC members automatically enrolls it.** This is a cold-start barrier for a new dedicator: it needs about five utility customers before it can join the shared audit. Until then, each utility must audit it separately (single-utility audits) or buy through an already-approved distributor or dedicator.
  - Audit assignments are made 6-8 months before each audit (NPPD presentation, NRC 2022 workshop). https://ww2.nrc.gov/docs/ML2213/ML22137A167.pdf
  - The NRC observes selected NUPIC audits and treats the joint audit as an acceptable alternative to its own vendor inspections.
- **Sole-source and emergent procurement**: in an emergent need, utilities use sole-source justifications, utility-to-utility transfers (RAPID/PeAks inventory sharing, (recalled)), or in-house dedication. A fast third-party dedicator would compete mainly with **in-house dedication** and with **incumbent third-party dedicators**, whose typical turnaround is weeks to months (recalled; no hard source found).
- **Procurement cycle** (recalled): PO to delivery for a dedicated safety-related item is often 8-20+ weeks. A new-supplier qualification (audit, ASL entry) takes 6-12+ months.

## 3. Who and how many buyers (concentration)

NRC operating reactor list (fetched 2026-10): **95 units at 55 sites**, including Vogtle 3/4 and Holtec Palisades. https://www.nrc.gov/reactors/operating/list-power-reactor-units.html

| Parent / operator (consolidated) | Units (approx.) |
|---|---|
| Constellation (incl. Calvert Cliffs, STP stake not operated) | 21 (12 plants, per WashEx 2026) |
| Duke Energy (Carolinas + Progress) | 11 |
| Southern Nuclear (incl. Vogtle 3/4) | 8 |
| TVA | 7 |
| Dominion (incl. V.C. Summer, ex-SCE&G) | 7 |
| NextEra / FPL (Turkey Point, St. Lucie, Point Beach, Seabrook) | 7 |
| Vistra (Comanche Peak + ex-Energy Harbor: Beaver Valley 2, Davis-Besse, Perry) | 6 |
| Entergy | 5 |
| PSEG (Salem 1-2, Hope Creek) | 3 |
| Xcel / NSP-Minnesota | 3 |
| APS (Palo Verde) | 3 |
| PG&E (Diablo Canyon), AEP/I&M (Cook), STPNOC, Talen (Susquehanna) | 2 each |
| Ameren (Callaway), DTE (Fermi 2), NPPD (Cooper), Energy Northwest (Columbia), Evergy/Wolf Creek, Holtec (Palisades) | 1 each |

- Some NRC row names are out of date: Energy Harbor and FirstEnergy are now Vistra, and SCE&G is now Dominion. The table above is my consolidation.
- That leaves about **21 buying entities**. The **top 6 (Constellation, Duke, Southern, TVA, Dominion, NextEra) run about 61 of 95 units, roughly 64%**. Constellation alone has about 22%. Adding Vistra and Entergy, the top 8 hold about 75%.
- Implication: this is a concentrated enterprise sale, with a few fleet-level supply-chain organizations and multi-year MSAs. One or two fleet wins would give the five-customer NUPIC threshold or come close to it. Fleets also centralize procurement engineering, which helps a vendor scale.
- Adjacent buyers: DOE labs and research reactors, the Canadian fleet (OPG, Bruce: CSA N299 rather than App B, (recalled)), new builds and restarts (Palisades, Crane/TMI-1 restart (recalled, Constellation, target ~2027), Duane Arnold (NextEra, recalled)), SMR and advanced developers (Kairos, X-energy, TerraPower), and the NSSS vendors themselves.

## 4. Appetite for AI

- **Nuclearn**: $10.5M Series A (Sep 2025, Blue Bear Capital lead). Its AI tools are used at "**more than 65 nuclear reactors worldwide**." It started at Palo Verde (APS) and automates documentation and paperwork, with operator-set automation thresholds and human sign-off. CEO Bradley Fox: "Liability always falls with a person"; the NRC treats most AI as a tool; "Think of this as the junior employee." https://techcrunch.com/2025/09/09/nuclearn-gets-10-5m-to-help-the-nuclear-industry-embrace-ai . The ABC15 2026 report repeats the 65+ plant figure. https://www.abc15.com/news/business/arizona-utilities-plan-ahead-for-nuclear-future . The "70+ facilities" figure in the brief is not confirmed; use 65+ reactors.
- **Atomic Canyon**: Diablo Canyon (PG&E) became the first US plant to adopt AI in Nov 2024 (Nvidia-supported). In Aug 2026 Atomic Canyon launched **NIVA**, developed **with INPO, EPRI and NEI**. NIVA runs on the FERMI retrieval engine, trained on tens of millions of NRC pages, and offers a regulatory knowledge assistant plus an operating-experience assistant. It targets about **15,000 workers** and will be released to all INPO members. **Constellation is an early adopter.** The founder expects a majority of INPO members to adopt it by the end of 2026. AI "not anywhere near ready" to make plant decisions. Washington Examiner, 7 Oct 2026. https://www.washingtonexaminer.com/daily-on-energy/4757946/daily-on-energy-nuclear-plants-embrace-artificial-intelligence/
- **NRC**: AI Strategic Plan published 29 Sep 2025 (ML25269A196). AI and Data Steering Committee formed "for the future use of responsible AI in NRC-regulated activities." Public AI workshop held 15 Sep 2026. No specific rules yet on licensee AI use in engineering or procurement. https://www.nrc.gov/ai.html
- Reading: the industry's own bodies (INPO, EPRI, NEI) are now co-developing AI tools, and the largest fleet has adopted them. Accepted uses so far are **assistive work with a human signing**: document drafting and retrieval. AI that *produces* a dedication package, signed by a qualified engineer under an App B program, fits this pattern. AI that *decides* acceptance does not.

## 5. Risks to adoption

1. **Conservative QA culture**: a new dedicator's technical evaluations are reviewed line by line by the utility's procurement engineering. "AI-generated" may draw more scrutiny, not less, until a track record exists. EPRI itself calls CGD subjective and engineering-judgment heavy.
2. **NUPIC cold start**: the joint audit needs five licensee customers. Before that, each utility runs its own audit, which costs it time and money, or the startup sells through an approved incumbent. It takes about 12-24 months (recalled) to get onto ASLs at scale.
3. **Part 21 liability**: the dedicating entity becomes responsible for Part 21 evaluation and reporting of defects. Errors expose the company to NRC vendor inspection findings, notices of nonconformance and civil penalties under 10 CFR 21.61 (recalled), plus utility claims. Insurance and indemnity terms will be stiff.
4. **NRC vendor inspection scrutiny**: procurement and CGD were already a rising inspection-finding area in 2018. A novel AI-heavy process will likely be inspected early.
5. **The bottleneck may be physical, not paperwork**: lead time is often set by testing (seismic, EQ, LOCA), sub-supplier surveys, or manufacturing for reverse-engineered parts, not by writing the technical evaluation. "Days not months" holds only for items where the critical characteristics can be verified by fast inspection or testing.
6. **Incumbents and EPRI templating**: EPRI's shared technical-evaluation data and Nuclearn/Atomic Canyon document tools could cut in-house CGD time and erode the outsourcing case.
7. **Demand volume**: safety-related order volumes have been falling (EPRI 2019). Restarts, uprates, 80-year license extensions and new builds partly reverse this.

## 6. Gaps (not verified this session)
- NEI supply-chain survey numbers, INPO statements, and current NRC public meetings on CGD (e.g., Part 21 rulemaking status).
- Utility earnings-call quotes on parts-driven outage delays.
- Count of NUPIC audits per year, and typical third-party dedication turnaround and price per item.
