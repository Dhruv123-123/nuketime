# Deep check: AI-native reverse-engineering parts house (19 Oct 2026)

Frame: `V5_OPTIMIST.md`. Tech is assumed to work. The idea must close on numbers and on the clock. Inputs: `v5_resurrect.md` (scored it 21), `v5_machines.md` (hot-section PMA house, 21) and `v5_security.md` (Breakout second source, 21). This file is the adversarial-but-fair check of all three and the single best version of the company.

## Verdict

**16/25 (N3 T3 C4 A3 D3). FAIL as a venture pass at the V5 bar. It is a real, fundable business, and a conditional 19 if the 8-week test below clears every threshold.** No leg is below 3.

The three sweeps converged for a good reason: approvals portfolios are among the best businesses in industry. HEICO is worth ~$36B and TransDigm ~$60B ([247wallst, 5 Oct 2026](https://247wallst.com/investing/2026/10/05/heico-has-the-better-business-the-better-balance-sheet-and-a-price-that-makes-it-impossible-to-buy/)), and TransDigm paid ~7.9x revenue for a PMA house in Jan 2026. But the 21s rested on three numbers that the evidence does not support:

1. **The engineering cost the AI attacks is already ~$100k a part, not $250-600k.** TransDigm's own view is "~1.5 years and ~$100k per part to approve a PMA" ([In Practise](https://inpractise.com/articles/transdigm-and-pmas-ccc-vs-mitchell-casualty-toast-gross-churn)). HEICO's Flight Support Group spent $43.7M of R&D in FY2025 and adds ~400-550 PMAs a year including acquisitions (HEICO FY2025 10-K, via search summary), which is ~$80-110k per part. AI can plausibly cut this to $40-60k. That is 2x, not the 4x the sweeps used, and it is ~1.5-2x against the best incumbent, not against a job shop.
2. **The clock is set by the gate, not the engineering.** DLA says SAR review takes "a minimum of 90 days, and possibly up to 180 days or longer" ([DLA SAR Guide](https://www.dla.mil/Portals/104/Documents/SmallBusiness/DLA%20SAR%20Guide.pdf)). Packages that go to a service Engineering Support Activity (ESA) need at least 180 more days. GAO found that **fewer than 10% (141 of 1,650) of DLA reverse-engineering projects started in FY2015-18 were completed by Dec 2018. 909 were still in process and 600 were cancelled**, and ESAs "sometimes take a long time to respond" ([GAO-19-586](https://www.gao.gov/assets/gao-19-586.pdf), pp. 12-13). AI does not shorten an ESA queue.
3. **Revenue per approved part is ~$100-150k a year, not $300k-1.7M.** HEICO FSG's $3.1B of sales over ~19,500 PMA parts ([HEICO](https://heico.com/?p=8203)) is ~$160k per part, and FSG revenue also includes repair and distribution. All 141 completed DLA reverse-engineering projects together saved only $22M ([GAO-19-586](https://www.gao.gov/assets/gao-19-586.pdf), p. 12). And an approved source only "grants the opportunity to compete", not orders ([DLA/NDIA 2024 SAR brief](https://ndia.dtic.mil/wp-content/uploads/2024/dla/Tue_Breakout_SAR_RPPOB.pdf)).

Rebuilt with these numbers, the best version (below) reaches ~$100M of revenue around year 7 on ~$250-280M of capital. That is fundable but slow, and the moat is ordinary. The A leg is 3 because AI answers the engineering-cost killer but not the gate-time killer, and gate time dominates.

## 1. Cost and time to get a part approved today

### DLA Source Approval Request (defence)
- **Process.** SARs can be submitted at any time, with no open solicitation needed. They apply only to items coded other than full-and-open (AMSC B/C/D, not G or T). Category IV covers reverse-engineered parts, done "at the expense and risk of the supplier", and needs a full TDP: signed drawings, materials, inspection and test criteria, and a manufacturing plan. The SAR Monitor logs the package and Value Engineering checks completeness. **Critical or weapon-system items go to the service ESA**, which may ask for parts to test and may inspect the site ([DLA/NDIA brief, Apr 2024](https://ndia.dtic.mil/wp-content/uploads/2024/dla/Tue_Breakout_SAR_RPPOB.pdf)).
- **Time.** Published ranges:
  - DLA Land & Maritime: 30-120 days ([vendor info](https://www.dla.mil/portals/104/documents/landandmaritime/v/ve/vendorinfo.pdf)).
  - DLA guide: 90-180+ days, longer for incomplete packages ([DLA SAR Guide](https://www.dla.mil/Portals/104/Documents/SmallBusiness/DLA%20SAR%20Guide.pdf)).
  - DLA Aviation: "can take over 180 days".
  - A secondary source says Navy and Army ESA reviews add at least 180 days ([govpathstrategies summary](https://govpathstrategies.com/source-approval-request-sar-guide)).
  
  So a realistic gate is **3-4 months for non-critical DLA-reviewed items and 9-15 months for CSI or ESA items**, plus rework loops.
- **Sample parts (RPPOB).** A vendor can buy or borrow a government part to reverse engineer. It takes 10 + 10 days of screening, plus **at least 30 days if ESA concurrence is sought**. NSNs below $10k of annual buy value are excluded ([same brief](https://ndia.dtic.mil/wp-content/uploads/2024/dla/Tue_Breakout_SAR_RPPOB.pdf)).
- **Approval does not mean orders.** When DLA splits an award, the best-value offer gets at least 60% of the requirement (same brief). DLA may also decline to process a SAR if the item's demand is too low (SAR guide).
- **Completion rate.** Fewer than 10% of projects completed (above). Contractor-funded projects completed at 55 of 617, which is 9% ([GAO-19-586](https://www.gao.gov/assets/gao-19-586.pdf)). Reasons given: the effort turned out more labour-intensive than expected, and ESA/DLA responses were slow. **This is the single most important number in this file.** The AI lever addresses the first reason, not the second.
- **First article.** It is required at the ESA's discretion and is typically a contract FAT after award. That is cheap for machined parts (~$5-25k, est.) and expensive for engine CSIs (rig or engine test).

### FAA PMA (commercial aviation)
- **Cost and time.** About $100k and about 1.5 years per part on average (TransDigm, via [In Practise](https://inpractise.com/articles/transdigm-and-pmas-ccc-vs-mitchell-casualty-toast-gross-churn)). HEICO's implied R&D is ~$80-110k per new PMA. Consultants quote 6-12 months for test-and-computation packages and 9-18 months for engine-critical parts ([Prime Propulsion](https://www.primepropulsion.com/post/faa-pma-certification-timeline-delays)). Identicality (licence) PMAs are faster but require OEM data.
- **Hot-section exception.** Chromalloy reports more than $100M invested across its V2500 HPT PMA programme, including casting and coating capability ([Chromalloy](https://www.chromalloy.com/chromalloy-secures-faa-approval-of-commercial-aviation-pma-for-the-v2500-turbine-engine/)). The CFM56 HPT blade PMA took roughly a decade (informal source, [In Practise FTAI/Chromalloy](https://inpractise.com/articles/ftai-chromalloy-and-cfm56-hpt-blade-pma)).
- **Second gate: the customer.** Each airline runs its own engineering approval. Lessors contractually bar return of engines with PMA parts ([In Practise](https://inpractise.com/articles/transdigm-and-pmas-ccc-vs-mitchell-casualty-toast-gross-churn)).
- **Volume.** About 130 test-and-computation PMAs are filed each year against TransDigm's 300,000+ part numbers (same source).

### Industrial gas-turbine (IGT) parts
- **No regulator.** The approver is the plant owner (IPP or utility), usually backed by the insurer and the O&M contractor. Typical requirements: references, a site and quality-system audit, material traceability, a warranty written in equivalent operating hours (EOH), and OEM parts for designs under ~10 years old ([Turbomachinery Mag, Chromalloy](https://www.turbomachinerymag.com/view/aftermarket-parts-is-there-life-after-the-oem)).
- **The real gate is the long-term service agreement plus fleet proof.** GE Vernova's heavy-duty GT service-agreement backlog was **$43B, with more than 70% of it running 10+ more years** ([GEV 2024 investor day](https://www.GEvernova.com/sites/default/files/2024-03/ge-vernova-2024-investor-day_power-segment-mavi-zingoni.pdf)). Parts under a CSA are not contestable. Combustion parts prove out over one combustion-inspection interval and hot-gas-path parts over one HGP interval (~24-32k EOH, so ~3-4 years at baseload; PSM claims 32k+ for its parts, [PSM 7F](https://www.psm.com/products/f-class-frames/7f)).
- **Proof that second sources move prices.** DOJ found that GE plus PSM held ~92% of 7FA aftermarket parts and service, and that **7FA replacement-part prices fell 60-70%** after PSM entered in 1998 ([DOJ complaint, 2015](https://www.justice.gov/atr/case-document/file/768396/dl)). OEMs hold ~60% of GT services and independents ~40% ([Grand View](https://www.grandviewresearch.com/industry-analysis/gas-turbine-services-market); [Dataintelo](https://dataintelo.com/report/industrial-gas-turbine-service-market)).

## 2. What AI, CT and automated TDPs can remove, and what still gates

| Step (simple machined DLA part / IGT combustion part) | Today (est., anchored to ~$100k total) | AI pipeline (est.) | Who gates it |
|---|---|---|---|
| Opportunity selection (FPDS, DIBBS, SRVA 24-month forecast, IGT fleet data) | Analyst weeks | Hours; a prioritizer ranks NSNs by sole-source $ × win odds × ESA path | Nobody |
| Sample acquisition (RPPOB or scrap part) | 1-3 months | Same, 1-3 months | DLA/ESA concurrence ≥30 days; IPP scrap access |
| CT/3D scan, metrology, alloy ID | $3-10k, 2-4 weeks | $1-3k, days (CT service $600-900/part, [cadcam.org](https://www.cadcam.org/faq-type/3d-scanning-faqs)) | Nobody |
| CAD, GD&T, drawings, material/process specs | $30-50k, 2-3 months | $8-15k, 2-3 weeks (Novineer claims >80% cut in assessment time; vendor claim, [Defense Post](https://thedefensepost.com/2026/06/30/novineer-ai-reverse-engineering-sustainment/)) | Nobody |
| Substantiation analysis (stress, thermal, T&C report) | $20-40k | $8-15k | DER (FAA) / ESA engineer |
| Package authoring (SAR Cat IV / PMA data package) | $10-20k | $2-5k | Nobody |
| Prototype + first-article test | $10-30k (machined); $0.3-1M+ (hot-section rig/engine test) | Unchanged | Test lab, physics |
| **Agency/customer review** | **3-15 months (DLA/ESA); ~6-18 months (FAA); 1 inspection interval (IGT)** | **Unchanged; rework loops fall** | **DLA VE, ESA, FAA ACO, airline, IPP** |

- **What AI removes.** About 50-60% of the *engineering* dollars (~$100k down to ~$40-60k per simple part) and ~2-3 months of the *engineering* calendar. A first-pass-complete package plausibly removes 1-2 rework loops: DLA says review time depends on package quality (SAR guide).
- **What it cannot remove.** ESA and FAA queue time, physical first-article and rig tests, and EOH field proof. For a simple non-critical DLA part, total elapsed time goes from ~12-18 months to ~6-9 months. For a CSI or engine part it goes from ~18-30 months to ~14-24 months. **The gate is 60-80% of elapsed time once the AI is in place.** That confirms the risk named in the brief.

**Who already does AI or digital reverse engineering, and what they achieved:**
- **Army (Secretary Driscoll).** Scanned, reverse engineered, printed and structurally validated a Black Hawk fuel-tank fin in **43 days for ~$3k against a $14k vendor price** ([CSIS](https://www.csis.org/analysis/who-controls-wrench-debate-over-right-repair); [Mobility Eng.](https://www.mobilityengineeringtech.com/component/content/article/54057-ausa-2025-secretary-driscoll-wants-army-to-save-time-and-money-by-3d-printing-replacement-parts)). This is organic, government-owned work, and it competes with the second-source thesis for the Army's own parts.
- **DLA.** 1,642 RE projects in FY2015-18 with 124 contractors, 103 of them small businesses; <10% completed; $22M saved ([GAO-19-586](https://www.gao.gov/assets/gao-19-586.pdf)).
- **Air Force Rapid Sustainment Office.** Reverse-engineering and scanning programmes; a KC-135 trim wheel example ([Air & Space Forces](https://www.airandspaceforces.com/USAF-to-Stand-Up-New-Rapid-Sustainment-Office)). No portfolio results published.
- **Novineer (NoviVision).** Photos to CAD in ~2 minutes, 0.72 mm mean error. Has a US Army agreement and a Stratasys partnership; no private funding disclosed ([Defense Post, sponsored](https://thedefensepost.com/2026/06/30/novineer-ai-reverse-engineering-sustainment/)). It sells a tool and does not own approvals.
- **AMCA (Advanced Manufacturing Co. of America).** Raised a **$300M Series B at a $1B valuation (2026)**. Its "Rapid" AI platform covers engineering, **qualification testing and TDP development** plus six AS9100-type factories, with customers including GE Aerospace, Honeywell and BAE ([Manufacturing Dive](https://www.manufacturingdive.com/news/boeing-lockheed-supplier-amca-jai-malik-series-b-300m-factories-ai-deploy/820650/)). **This is the closest well-funded threat.** It is one product decision away from owning second-source approvals.
- **Others.** Phillips Corp and 3YOURMIND reverse engineered tank parts for an Army digital inventory ([3DPrint](https://3dprint.com/327729/3yourmind-partners-with-phillips-corp-in-us-navys-rimpac-distributed-manufacturing-experiment/amp/)). Parts Life (R.O.P.E.) and NCMS DMSMS projects ([NCMS](https://ncms.org/news/project-announcement/project-announcement-resolving-part-obsolescence-diminishing-manufacturing-sources-and-material-shortages-dmsms-for-improved-maintenance-and-sustainment/)). Divergent ($2.3B) and Hadrian build new parts, not approvals. No ARL or JPEO AI-to-TDP programme with published results was found.

## 3. Demand

**DLA sole-source pool (pulled from USAspending, FY2025, DLA awarding sub-agency).**
- DLA FY2025 contract obligations by extent competed:
  - Not competed (C): $8.16B
  - Not available for competition (B): $0.98B
  - Not competed under simplified acquisition (G): $1.24B
  - **Non-competitive total: ~$10.4B of ~$56B.** That includes fuel, food and missiles.
- **Restricted to 25 mechanical spares product codes** (1560 airframe structure, 2840 aero gas turbines, 1680, 1650, 1630, 2915, 1615, bearings, valves, power transmission and so on): **$2.96B not-competed + $0.64B simplified not-competed = ~$3.6B a year.**
- **Concentration kills much of it.** The top recipients of that $2.96B:
  - Boeing $931M
  - GE $255M + $154M
  - CFM $190M
  - RTX $172M
  - Bell-Boeing $136M
  - Parker $131M
  - Goodrich $105M
  
  **The top 25 recipients take $2.45B (83%).** Most of that is long-term contracts, performance-based logistics or CSI engine parts where the OEM holds design control. TransDigm units (e.g. Arkwin $8M) are small in DLA's book.
- **Reachable long tail: ~$0.6-1.2B a year at DLA**, plus service-direct buys (NAVSUP WSS, AF and Army depots, not pulled), so **~$1.5-2.5B a year total, derived**. Capturing 10-15% means **~$150-350M of defence revenue at maturity**. That is a good business, not $10B on its own.
- **Number of NSNs above ~$150-250k a year: not established.** No source gives it. This is test item #1.

**Political tailwind is real but not decisive.**
- FY2026 NDAA: right-to-repair mandates were **stripped in conference**. Only a technical-data tracking system and contract review survived (Sec. 804/805) ([Defense Daily](https://www.defensedaily.com/right-to-repair-reforms-mostly-stripped-from-final-fy-26-ndaa/congress/); [Federal News Network](https://federalnewsnetwork.com/congress/2025/12/congress-quietly-strips-right-to-repair-provisions-from-2026-ndaa-despite-wide-support/)).
- FY2027: SASC included right to repair ([Warren](https://www.warren.senate.gov/newsroom/press-releases/warren-sheehy-statement-on-right-to-repair-win-in-senate-fy-27-ndaa/)) and the House text includes the Harrigan-Goodlander amendment ([Harrigan, 4 Jun 2026](https://harrigan.house.gov/media/press-releases/congressman-pat-harrigan-secures-military-right-repair-final-fy27-ndaa)). Conference is pending. The Army Secretary is an advocate.
- The DoD IG found TransDigm made $16.1M of excess profit on 46 parts sold for $26.2M, with margins of 17-4,451% ([DODIG-2019-060](https://media.defense.gov/2019/Feb/27/2002093709/-1/-1/1/DODIG-2019-060.PDF)), and $20.8M more in 2017-19 ([DODIG-2022-043](https://media.defense.gov/2021/Dec/13/2002908344/-1/-1/1/DODIG-2022-043.PDF)). Buyer pain is documented, but per-part dollars are small.

**Commercial PMA and IGT.**
- **PMA market:** $3.9-12.1B depending on publisher ([search summary](https://www.reanin.com/reports/commercial-aircraft-parts-manufacturer-approval-market)); low confidence.
- **Price:** PMAs sell at a 30-40% discount (some at 50-65% of OEM price) and earn 60%+ gross margin. Once an airline adopts a PMA, "you keep it" ([In Practise](https://inpractise.com/articles/transdigm-and-pmas-ccc-vs-mitchell-casualty-toast-gross-churn)).
- **FTAI and Chromalloy PMA:** an HPT vane at ~$5k against ~$20k OEM, and up to $2M saved per CFM56 shop visit ([In Practise](https://inpractise.com/articles/ftai-chromalloy-and-cfm56-hpt-blade-pma)).
- **IGT services:** $16-20B (2012 Chromalloy estimate); parts are 68% of the F-class aftermarket ([Turbomachinery](https://www.turbomachinerymag.com/view/aftermarket-parts-is-there-life-after-the-oem)).
- **Fleet:** 670+ 7FA and 1,100+ 9FA units in service ([Zurn](https://www.zurnpower.com/spares/ge-7fa-9fa-gas-turbine-spare-parts)).
- **Why now:** GE Vernova's gas backlog plus slot reservations reached 116 GW in Q2 2026 ([Utility Dive](https://www.utilitydive.com/news/ge-vernova-gas-turbine-backlog-climbs-to-116-gw/826039/)). Old units run harder and are reactivated, and data-centre behind-the-meter fleets are new buyers outside OEM service agreements.

**OEM countermeasures.**
- **Price cuts on attacked parts:** 7FA prices fell 60-70% once PSM entered, which shrinks the prize. An OEM that matches a PMA price cuts its own margin 40-50% ([In Practise HEICO](https://inpractise.com/articles/heico-pma-history-and-pricing)), so most do not match.
- **Long-term service agreements:** GE's $43B, 10+ year book locks the newest fleet.
- **Lessor PMA bans** on aircraft and engines.
- **Lawsuits.** GE sued Siemens Energy for trade secrets in 2021 (settled) ([CNBC](https://www.cnbc.com/2021/01/14/ge-accuses-siemens-energy-of-usi-stolen-trade-secrets-to-rig-contract-bids.html)). However, reverse engineering a lawfully bought part is expressly *not* "improper means" under the Defend Trade Secrets Act ([18 U.S.C. §1839(6)(B)](https://www.law.cornell.edu/uscode/text/18/1839)), so the residual legal risk is patents and ex-employee data, not reverse engineering itself.
- **OEMs buying the attackers:** TransDigm bought Jet Parts Engineering and Victor Sierra (PMA) for $2.2B on ~$280M revenue ([TDG, Jan 2026](https://transdigmgroupinc.gcs-web.com/news-releases/news-release-details/transdigm-announces-acquisition-jet-parts-engineering-and-victor)). That is both a countermeasure and the exit.

## 4. Unit economics and the portfolio curve

**Per part (derived; the inputs are what the test must confirm).**

| | DLA long-tail NSN | IGT combustion/HGP part | FAA PMA (non-hot-section) |
|---|---|---|---|
| Cost to submit (AI) incl. sample and FAT | $60k | $600k (tooling, coating, test, field trial) | $150k |
| Approval / acceptance probability | 55% | 80% | 85% |
| Win rate once approved | 65% | 80% | 70% |
| Steady revenue per earning part | $120k/yr | $1.2M/yr (8-10% of a part family's fleet demand) | $300k/yr |
| Gross margin (contract-made) | 40-50% | 45-55% | 55-60% |
| **Effective cost per earning part** | **~$170k** | **~$0.95M** | **~$250k** |
| **Payback after approval** | **~3 yrs** | **~1.7 yrs** | **~1.5 yrs** |
| Gate lag | 6-15 mo | 12-24 mo (+ EOH proof for HGP) | ~18 mo |

The IGT part is the best engine per dollar. Defence gives breadth and early, small revenue. The resurrect model's "$300k/part, 3-7 month payback" does not survive the approval-probability and win-rate haircuts.

**Portfolio curve (derived; model in session scratchpad).** Inputs:
- Defence: 60, 200, 350, 450, 500, then 550-600 packages a year.
- IGT: 4, 8, 12, 15, 15, 18, then 20 parts a year.
- PMA: from year 4, 15 rising to 100 a year.

| Year | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| Revenue $M | 0 | 1.3 | 8 | 24 | 49 | 80 | **118** | 160 | 262 |
| Earning parts (def/IGT/PMA) | 0 | 21/0/0 | 93/3/0 | 218/8/0 | 379/15/0 | 558/25/9 | 754/35/24 | 969/46/48 | 1398/72/131 |
| Cumulative development spend $M | 6 | 23 | 51 | 89 | 132 | 182 | 239 | 299 | 425 |

- **$100M of revenue in ~year 6.5-7.**
- **Capital to $100M revenue:**
  - development spend ~$210M
  - minus cumulative gross profit ~$75M
  - plus G&A ~$80M
  - plus working capital ~25% of revenue ($30M)
  - **= ~$250-280M** of equity plus an inventory/receivables credit line.
  
  That is raisable in 2026 (AMCA's $300M Series B; Hadrian). It is not cheap.
- **Capital to $1B of revenue:** organically ~year 13-15 on ~$0.6-0.8B. Realistically it needs a roll-up. PMA and repair houses trade at ~8x revenue (Jet Parts) or ~13x EBITDA (HEICO paid $2.05B for Wencor on $153M EBITDA, [Benzinga](https://www.benzinga.com/markets/equities/23/08/33578896/heico-closes-its-largest-ever-acquisition-buys-wencor-for-2-05b)). So the last $700M of revenue costs ~$3-5B of acquisition capital.

**Who makes the parts.**
- **Machined, sheet-metal and fabricated combustion parts:** contract job shops and the new AI-native shops (Hadrian, AMCA, Isembard) make them. These are not scarce.
- **Superalloy castings are the bottleneck** for hot-gas-path parts: 18+ month lead times and US foundry count down 67% since 2000 (DDM/AFS via `v5_machines.md` [S5]); GE paid $11.75B for CPP. Start with fabricated combustion hardware, use printed-core foundries (DDM, Rangeview) for development castings, and own casting later. That is phase 2, and it adds capital.

## 5. Ceiling and ladder

- **Comparables.**
  - HEICO: ~$36B market cap (51x trailing P/E). It took ~35 years and ~100 acquisitions to reach FSG's $3.1B.
  - TransDigm: ~$60B ([247wallst](https://247wallst.com/investing/2026/10/05/heico-has-the-better-business-the-better-balance-sheet-and-a-price-that-makes-it-impossible-to-buy/)).
  - FTAI Aviation: ~$20B, secondary source. It owns 1,000+ engines, uses PMA hot-section parts via Chromalloy, runs the Module Factory, and launched FTAI Power (CFM56 to 25 MW data-centre turbines, 100+ a year) ([Distribution Strategy, Jan 2026](https://distributionstrategy.com/2026/01/ftai-aviation-moves-into-data-center-power-leveraging-engine-distribution-and-mro-platform/)).
- **The ladder that reaches $10B is FTAI's, not HEICO's:**
  1. Approvals.
  2. Own manufacturing and coatings.
  3. Exchange and rotable pool plus repair (MRO).
  4. Own aeroderivative and IGT units, leased or sold as power.
  
  Owning the parts library cuts the cost of running a turbine fleet by an estimated ~20-30% (FTAI's ~$2M saving per shop visit), which is the edge for a power-fleet business. **But FTAI already holds the CFM56/power rung**, and rung 4 is capital-heavy.
- **Credible outcome.**
  - $150M revenue × 30% EBITDA × 20x ≈ $0.9B; at Jet Parts' 7.9x revenue ≈ $1.2B, by year ~8.
  - $10B+ needs ~$1.5B of revenue at HEICO multiples, or a power-fleet balance sheet. That is possible but not shown. **C = 4.**

## 6. Kill risks, AI answers (with stated effect), and what is left

| Killer | AI counter-move | Quantified effect | Residual |
|---|---|---|---|
| ESA/FAA review time dominates | (a) Route the portfolio toward **non-CSI, DLA-VE-reviewed** NSNs (30-120 days), using an ESA-path classifier. (b) First-pass-complete packages generated with a rules/LLM checker against the SAR guide and the DLAD L04 note. (c) Run 100+ in parallel | Elapsed time ~12-18 to ~6-9 months for simple parts; rework loops ~2 to ~0.5 (est.) | CSI/engine parts are still 14-24 months. **Unanswered for the high-value parts** |
| Thin demand per part; approval does not mean an award | Prioritizer on FPDS, DIBBS and SRVA 24-month forecasts, scoring $ × P(approval) × P(win) × ESA path | Breakeven demand falls from ~$220k/yr to ~$90-120k/yr, roughly doubling the list of NSNs worth a SAR | Long-tail depth unknown (test #1) |
| Incumbent price cuts (7FA fell 60-70%) | Pick orphan and obsolescent items and lead-time-driven buys (DLA scores lead time); win on delivery with digital machining | Keeps ≥60% of each split award at a 25-35% discount (est.) | Portfolio margin compresses on the best parts |
| Long-term service agreements and lessor bans | Target units leaving OEM agreements, older E/F frames, behind-the-meter data-centre fleets and owner-operators (the FTAI model) | Contestable IGT pool ~40% ISP share | GE's 10+ yr agreements lock the newest fleet |
| OEM IP lawsuits | Clean-room reverse engineering from purchased parts (DTSA §1839(6)(B)); AI patent screen per part | Per-part legal screen ~$2k against ~$15k by counsel (est.) | Patent hits on newer frames |
| Castings bottleneck | Fabricated combustion parts first; printed-core foundries for development castings | Removes ~6-12 months of tooling per cast part (DDM claim) | Production castings are still 18+ months out |
| HEICO, AMCA or OEMs adopt the same AI | Speed of portfolio build plus a data flywheel (scan, material and test outcomes) | ~1.5-2x cost advantage over HEICO for 2-4 years (est.) | **The tools commoditize; only the approvals compound. D = 3** |

## Rescore

| Leg | Sweeps | This check | Why |
|---|---|---|---|
| N | 4 | **3** | Closes at ~20% part-level IRR. Needs ~$250-280M to $100M revenue; per-part revenue is 2-3x lower than modelled |
| T | 4 | **3** | First revenue in year 2 (DLA non-CSI awards, IGT spot parts). $100M around year 7 on optimistic ramps |
| C | 5 | **4** | $1B+ credible. $10B needs a HEICO-style roll-up or the FTAI power-fleet ladder |
| A | 4 | **3** | AI halves engineering cost, but gates are 60-80% of elapsed time and AI does not touch them |
| D | 4 | **3** | Approvals are sticky, but the AI tools are copyable by HEICO, AMCA and the OEMs |
| **Total** | 21 | **16** | **Fail (needs 19)** |

**Path to 19 (conditional).** If the test shows ≥1,500 reachable non-CSI NSNs, a ≤120-day DLA VE path and ≤$40k per complete package, then N goes to 4 and T to 4 (18). IPP pull at 65-70% of OEM price with EOH warranties accepted on fabricated parts within one combustion-inspection interval takes A to 4 (19).

## Cheapest feasibility test (8 weeks, ~$90-110k)

1. **Depth (weeks 1-3, ~$5k).**
   - Method: pull 3 years of FPDS/USAspending and DIBBS/SRVA data for DLA Weapons Support in the 25 mechanical product codes. Map NSNs to AMSC code (B/C/D, excluding G and T) and to CSI/ESA path. Count NSNs with ≥$150k a year of sole-source buys that are *not* held by the top-25 OEMs.
   - **Kill if fewer than 1,000.**
2. **Pipeline cost (weeks 2-7, ~$60-80k).**
   - Method: buy samples of 10 non-CSI NSNs via RPPOB or the surplus market, and get 2 7FA/7EA combustion parts from an IPP's scrap. Run CT at ~$600-900 a part, alloy ID, AI CAD and drawings, and AI-written Category IV SAR packages. Log engineer-hours and compare with a quote from an independent RE/DER shop. Submit 3-5 SARs; DLA VE's completeness response or rework request arrives within the window.
   - **Kill if the median complete package costs more than $50k or takes more than 6 engineer-weeks, or if VE flags 2 or more of 5 as incomplete.**
3. **Gate and price (weeks 1-8, ~$25k travel and time).**
   - Method: interview the DLA SAR monitor or VE analyst on current non-CSI review times. Seek 2-3 IPP or O&M LOIs for named parts at 65-70% of OEM price with an EOH warranty. Pull post-approval price drops for 20 historical SAR-broken NSNs from FPDS.
   - **Kill if the non-CSI review is over 180 days, or there are fewer than 2 IPP LOIs, or the median post-breakout price drop is under 20%.**

## Caveats
- One scorer.
- Per-part revenue, approval probability, win rate and IGT part economics are derived estimates, flagged above. The HEICO R&D-per-part figure divides R&D by new PMAs, and the new-PMA count includes acquired parts.
- USAspending pulls are FY2025 DLA only and do not include service-direct buys. Extent-competed codes are from FPDS. Top-40-PSC aggregation came from quarterly queries.
- PMA market size, IGT services size and ISP share come from paid-report summaries. Market caps come from secondary articles (Oct 2026).
- The FY2027 NDAA conference outcome is not yet known.
