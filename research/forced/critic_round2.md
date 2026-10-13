# Final judge: both rounds combined

None of the 19 deep-dived candidates clears the bar as pure software. Every analytics-only version tops out at roughly $10-150M in revenue. A $1B outcome needs the data edge used to take risk (underwrite, transfer or lend), so the ranking below favours ideas where the forced public data creates an underwriting edge that incumbents lack.

## 1) Combined top 10

| # | Idea | Verdict (one line) | $1B path |
|---|---|---|---|
| 1 | **End-of-life liability underwriter** (Alberta AER + Petrinex, then Saskatchewan, BC and US states) | Best mix of a law-created dataset, outcome labels, timing, uncrowded space and founder fit. Main risk is that the catalysts are policy-dependent. | Start by selling the liability score. Then sell closure surety and security bonds as an MGA on Canadian surety capacity. Then price and take over end-of-life liabilities from producers. Official Alberta liability is C$36.6B; a leaked AER estimate put it at C$260B. |
| 2 | **CA GeoTracker pollution-liability pricing** | The data is real (230M lab results) and contamination is an uninsured or badly priced peril. But the data has selection bias and LightBox/EDR own the diligence channel. | A pollution-legal-liability MGA plus pricing environmental exposure in property deals. US environmental insurance is a multi-billion premium line (from memory). |
| 3 | **Patent-validity underwriter (PTAB)** | About 15k decided PTAB outcomes and a clear risk product. But USPTO's 2025 changes to institution rules make old labels unreliable for pricing. | Patent-invalidity insurance and pricing for litigation finance and IP-backed lending. |
| 4 | **FOAK technology-performance underwriter** (OSTI/ARPA-E final reports) | The most original idea in round 2 (revolutionary score 6). But the forcing rule lets awardees strip out the numbers an underwriter needs, and today's market is about $100-300M of premium. | An MGA, then a "Moody's for FOAK" rating standard. This only works if the market for wrapping first-of-a-kind projects grows about 5x. |
| 5 | **Florida condo SIRS distress** | Law-forced building-condition disclosures arrive while condo associations face a funding crunch. Florida-only, with exposure to repeal or amendment by the legislature. | Lending to condo associations (special-assessment loans) plus pricing insurance and mortgages on condo units. |
| 6 | **Korea jeonse deposit-default underwriter** | Strongest labels since lease reporting was enforced in June 2025, and the state guarantor HUG is retreating. Korean licensing blocks a foreign founder. | A private deposit-guarantee insurer stepping into the space HUG is leaving. |
| 7 | **Mass-tort forecaster** (PACER + FAERS) | A genuine prediction problem. Praedicat proves buyers exist and also how small the software market is. | Casualty-reinsurance pricing and trading tort-exposed credit. Needs a capital partner. |
| 8 | **HCRIS SNF/hospital distress lender** | Good closure labels and a why-now from Medicaid cuts. Cost reports lag 1-2 years, and Kaufman Hall and the rating agencies cover the space. | Rescue and bridge lending to distressed facilities. Capital-heavy. |
| 9 | **PAGA wage-and-hour liability** | The data is real (about 80-90k notices), but wages owed are uninsurable and buyers who know they are violating select into cover. California-only. | Only as a feature inside a national employment-practices MGA. |
| 10 | **Contract surety priced on DOT bid tabs** | The surety market is real (about $11-12B a year), but bid tabs are a weak signal next to the WIP schedules sureties already receive. | An MGA would need 20-40% of the addressable public low-bid slice. Implausible. |

**Dropped as crowded or capped:** SBA (Lumos), Schedule P (WTW ResQ, rating agencies), Brazil precatórios (EC 136 changed the regime), India IBC (RBI only lets licensed ARCs buy bad loans), MOT-based vehicle service contracts (MOT records the wrong failures; AutoTrust already prices warranties on claims), No Surprises Act IDR (HaloMD and Daffodil already hold the position), Dutch BRO, SEP essentiality, FCC, OSHA, NHTSA, EMMA, EMA dossiers.

## 2) Single best pick: end-of-life (closure) liability underwriter

Start with Alberta and Saskatchewan oil and gas wells and facilities, then extend to mine reclamation and solar/wind decommissioning.

**Quirk-created data edge**
- Alberta's licensing regime forces every licensee to file well licences and status changes, per-well production volumes, inspections and compliance records, and closure work.
- These are published as the AER ST37 well list and Petrinex public volumetrics.
- The Orphan Well Association (OWA) publishes the orphan inventory, which gives dated default labels with the former licensee named.
- Directive 088 forces mandatory closure spend, and Directive 011 sets the regulator's formula cost per well.
- So there are three things in public: a monthly panel of who holds which liability, outcome labels (which wells were orphaned), and the regulator's own deemed-cost formula to beat.
- This is the same pattern as SMAD: tenure law forces filings, and the public panel has never been modelled at well level for underwriting.
- Saskatchewan has its own licensee liability rating program and well data, a direct overlap with Dhruv's current work.

**Revolutionary ML**
- The official liability estimate is C$36.6B (C$23.4B inactive, C$13.2B active). The Auditor General said up to C$60B, and a leaked 2018 AER presentation said C$260B.
- That gap between C$36.6B and C$260B is the mispricing. Nobody has a per-well model of the true cost to close each well or the probability that it ends up orphaned.
- The AER itself still has no fixed approach to collecting security; decisions remain discretionary.
- Its June 2024 consultation proposes "performance and risk-informed security determination" and "alternative forms of security (bonds, trusts, etc)". The regulator is asking for exactly the model that does not exist yet.

**$1B path, in three layers**
- **(a) Liability score.** Sell it to sureties (for example Trisura and Intact, the natural first partners in Canadian surety), lenders and acquirers. Every licence transfer already triggers an AER security decision. Revenue is about $10-30M; this layer exists to win distribution and collect cost labels.
- **(b) Closure surety and security bonds as an MGA.** This opens once Alberta accepts bonds as security, and also covers Saskatchewan, BC, US state bonding and mine reclamation bonds.
  - Sizing: securing 10-20% of Alberta's C$36.6B at 1-3% rate on line is C$70-220M of premium a year in Alberta alone. This sizing is my estimate.
- **(c) Liability transfer, the largest pool.** Take inactive liabilities off producers for a cash fee priced by the model, then close them in batches below the fee.
  - Market size: C$23.4B of inactive liability in Alberta. US documented unplugged wells add plugging liability that independent estimates (RFF/EDF) put in the hundreds of billions (from memory).
  - Pace: industry already spends about C$900M a year on closure against a C$700M quota.
  - This is a balance-sheet business. The model is what keeps it from being the next R&Q-style mispricing failure.

**Uncrowded**
- My searches found no startup underwriting closure liability with ML; results were only academic, such as Insley (UWaterloo, 2024) on environmental bonds.
- Data vendors (XI Technologies' ARO tools, Enverus, geoLOGIC, from memory) sell estimates for acquisition analysis but take no risk and do not model probability of orphaning.

**Founder fit**
- Turning messy filings into predictions on geoscience records is exactly what Dhruv's team does: well files, casing and vent-flow reports, production histories.
- The opportunity is Canadian-first, with a Saskatchewan overlap to his current work. It is not a Terranox clone and finds no resources.

**Why it beats #2-#10**
- GeoTracker has a similar data edge, but LightBox owns its channel and its labels are biased.
- The PTAB and Korea ideas have stronger labels but an unstable regime or a licensing block.
- FOAK is more revolutionary but rests on a missing market.
- None of the others has a regulator actively designing a risk-based security regime that needs this model.

**Honest risks**
- **Brief-boundary risk.** It is resource-adjacent, but it is end-of-life liability, not prospecting or drilling.
- **The US catalyst is being reversed.** BLM's 2024 bonding rule (higher minimum bonds per lease and statewide) is being repealed by the current administration.
- **The Alberta catalyst is not yet in force.** AER's security framework is still undecided, and critics call the April 2025 Mature Asset Strategy reforms "smoke and mirrors".
- **Layer (c) needs a lot of capital.**
- **Capacity.** Sureties write against a model only once a carrier partner backs it.

## 3) One-day proof on real data

The question it answers: does a well-level model built from public filings predict orphaning materially better than the regulator's own Liability Management Rating (LMR)?

**Hour 0-1: stage the data outside the container.** The AER, Petrinex and OWA hosts are not github/pypi/s3/googleapis, and I found no mirror, so push the raw files to a GitHub release or GCS bucket.
- **AER ST37:** list of wells, current plus Wayback/archived monthly snapshots for 2015-2024. Gives licensee, status, fluid, depth, spud date and location.
- **Petrinex public conventional volumetric data:** monthly oil, gas and water volumes and days on, with operator ID, 2015-2025.
- **OWA orphan inventory:** wells and facilities with former licensee and designation date. Back it up with AER receivership and closure-order bulletins for dates.
- **Historical AER monthly LMR licensee ratings:** this is the baseline. Use archived copies.
- **Directive 011 cost tables:** the regulator's deemed cost per well.
- **AER surface casing vent flow / gas migration lists:** optional, if published.

**Hours 1-3: build the panel.**
- Build a well x month panel: holding licensee, status transitions, months since last production, decline, water cut, age, depth, H2S and region.
- Add licensee aggregates: the share of the licensee's liability that is inactive, the trend in its production revenue proxy, recent licence transfers, and its count of compliance hits.

**Hours 3-6: model.**
- Label: the well is in the OWA inventory, or its licensee was in receivership or under a closure order, within 48 months.
- Out-of-time design:
  - Train on 2015-2016 snapshots with outcomes through 2019.
  - Test on a December 2019 snapshot with outcomes 2020-2024. This window covers the 2020 receivership wave, so there are hundreds of licensees and thousands of wells in the labels.
- Model: LightBGM at well level, with licensee-level roll-up.
- Baselines:
  - the licensee's LMR ratio;
  - inactive share plus well age.

**Hours 6-8: metrics and cost check.**
- Metrics:
  - well-level and licensee-level AUC;
  - share of later-orphaned Directive 011 liability (dollars) captured in the top risk decile;
  - median lead time ahead of receivership.
- Cost side check: compare Directive 011 deemed cost with the OWA's reported actual closure costs, using annual-report averages by well type. Note that per-well actual costs are the gap a surety or area-based-closure partner would fill.

**Kill criteria.** Kill the idea if any of these hold:
- AUC lift over the LMR baseline is under 0.05;
- the top decile captures less than 50% of orphaned liability dollars;
- median lead time is under 6 months.

**Deliverable:** a ranked league table of current licensees by orphan risk. That is the artifact to put in front of Trisura or Intact surety underwriters and the AER's security-framework team.

Sources:
- [AER LMR Session 3: Security Framework (June 2024)](https://static.aer.ca/prd/documents/liability/LMR-Session3-Security-Framework.pdf)
- [ABlawg: Grading the 2024 AER Liability Management Performance Report](https://ablawg.ca/2026/02/05/grading-the-2024-aer-liability-management-performance-report/)
- [AER Liability Management Performance Report 2024](https://static.aer.ca/prd/documents/reports/liability-management/LMPerformance-Report-2024.pdf)
- [Osler: Directive 088 mandatory closure spending](https://www.osler.com/en/insights/updates/alberta-well-cleanup-directive-088-comes-into-effect-with-new-mandatory-closure-spending-targets-fo/?pdf=1)
- [Taxpayers for Common Sense: administration to repeal BLM bonding requirements](https://www.taxpayer.net/energy-natural-resources/administration-to-repeal-recently-updated-oil-and-gas-bonding-requirements/)
- [E&E News: Trump targets oil well cleanup requirements](https://www.eenews.net/articles/trump-targets-bidens-oil-well-cleanup-requirements/)
- [Insley 2024, environmental bonds (UWaterloo)](https://uwaterloo.ca/economics/sites/default/files/uploads/documents/2024_insley_environmental_bonds.pdf)
- [C.D. Howe: Alberta's orphan well challenge](https://cdhowe.org/intelligence-memos/dachis-shaffer-and-thivierge-alberta%E2%80%99s-orphan-well-challenge)