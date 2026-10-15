# Round 3 lane: deeptech, defence and space

Written 15 Oct 2026. Lane brief: find places where public data plus ML locates something in
deeptech, defence or space that the company then owns. I used 17 of 20 WebSearch calls. Government
hosts (sbir.gov API, api.usaspending.gov, celestrak.org) all returned connection failures from this
container. Dataset access below is confirmed from documentation, not by downloading.

## Bottom line

| # | Candidate | What is owned | Exclusive? | Score |
|---|---|---|---|---|
| A | **SBIR lineage acquisition: buy dormant Phase I/II holders, use the statutory Phase III sole-source path** | Successor-in-interest SBIR status, which gives Phase III sole-source eligibility and SBIR data rights | Yes. One lineage per technology, held by one firm at a time; licensees do not get it | **6** |
| B | First qualified replacement for obsolete defence parts (DMSMS, DLA) | Source approval or qualification | No. DLA re-competes, and breaking out a part destroys its margin | 3 |
| B2 | Authorised aftermarket licences for end-of-life defence microelectronics (the Rochester model) | OEM die, masks and licence for a product line | Partly. Negotiated with the OEM, not first-come | 4 |
| C | Space: salvage or revival of defunct or insurer-owned satellites | Title bought from insurers (HGS-1 precedent) | No salvage law in orbit, and the owner state keeps jurisdiction | 2-3 |
| C2 | Orbital servicing contracts (life extension, reboost, deorbit) | Service contracts | No. Crowded, and a service market | 2 |
| D | Proven-but-abandoned national lab, ARPA-E or DOE technology, exclusively licensed in | Exclusive federal patent licence (35 USC 209) | Yes on paper, but the patents on abandoned tech have often expired | 3 |
| E | Sole qualified source on a QPL/QML specification | Qualification | No; it is a de facto position only | 2 |

**Verdict.** Only A has a legally exclusive, rivalrous position that public data plus ML can find
before others do. It is cheap to acquire: a dormant SBIR shop or its asset line costs $1-10M, while
it can unlock uncapped sole-source awards. It still fails the fourth part of the Terranox law. The
value only arrives when a contracting officer chooses to use the sole-source path, and the
government is the only buyer. Treat it as a TransDigm-style acquire-and-build holding company with a
statutory moat, not as a mineral claim. The other theses fail on exclusivity (B, E), on law (C), or
on asset size (D).

---

## A. SBIR lineage acquisition (6/10)

**The legal position (confirmed).**
- **Phase III has no cap.** An SBIR Phase III award is any work that "derives from, extends or
  completes" an earlier Phase I or II award, paid with non-SBIR money. Agencies may award it
  sole-source with no new competition, no dollar cap and no time limit (15 USC 638(r)(4), per Arnold
  & Porter).
- **Data rights run 20 years.** The 2019 SBA Policy Directive set SBIR data-rights protection at
  20 years.
- **The right can be bought.**
  - In 2020, GAO's ASRC Federal (B-418028) decision sustained a protest: an acquirer that had not
    been novated the earlier awards was not eligible.
  - From 1 Oct 2020, the SBA amended the Directive so that a "successor in interest" keeps Phase III
    sole-source eligibility and the data rights after a merger or acquisition (Ward & Berry).
- **GAO has upheld it.** In *Digital Force Technologies* (B-423319, 19 May 2025), GAO denied a
  protest against an Air Force Phase III sole-source to **Clear Align**:
  - Clear Align had bought **Computer Optics' assets in 2013**, and the Air Force treated it as
    successor in interest.
  - Only a camera derived from Computer Optics' Phase II work, about 32% of unit cost, and that was
    enough to sole-source the whole system.
  - GAO also held that the *requirement* need not derive from SBIR; only the *work* must.
  - This is the exact play: buy an old lineage, then win a sole-source for a larger system wrapped
    around it.
- **Licensing does not transfer it.** Licensees do not get Phase III rights; the rights cannot sit
  in two places at once. So the right follows ownership of the business or product line, and only
  one holder exists at a time. That makes it rivalrous.

**Public datasets, and why they are public.**
- SBIR.gov award database: every Phase I and II award since 1983, with abstracts, topic, agency,
  firm and PI. It is public under the SBIR statute's reporting rules; bulk CSV and an API are
  documented, but the host was blocked here.
- FPDS / USAspending: every obligation, including the SBIR/STTR "research" code that flags Phase
  III awards. Public under the FFATA and DATA Acts.
- SAM.gov: sources-sought notices, J&As and sole-source notices, which show live requirements.
  Public under FAR part 5.
- DoD budget R-2/P-40 exhibits: program-level requirement text.
- DTIC: SBIR final reports, partly public.
- SBA's size and DSBS profiles: whether the firm is still alive.

**ML problem (hard, not a lookup).**
1. Embed about 200,000 Phase I/II abstracts and final reports.
2. Map them against live requirements: SAM notices, budget exhibits, programme-office J&As.
3. Infer which dormant lineages, whose firm is dead, shrunk or founder-retired, could credibly
   support "derives from" for a large current programme.
4. Rank by expected Phase III value times the cost of acquiring the lineage.

The hard parts are entity resolution across SAM UEI and DUNS changes, inferring firm dormancy, and
legal-derivation similarity on technical text. Primes and PE firms do this by relationships, not
systematically. A model must beat an agency x topic-area lookup (see the first proof below).

**What is owned.** The lineage itself: the company, or its asset line, as successor in interest. It
carries Phase III sole-source eligibility, 20-year data rights and the technical data package.

**Rivalry and crowding.**
- **Primes and acquirers already buy SBIR firms.**
  - Large primes buy product lines for exactly this reason, and Arnold & Porter's deck calls it
    "Model 4".
  - AE Industrial runs roll-ups.
  - Anduril has bought many small firms (memory: Area-I, Dive Technologies, Blue Force Technologies,
    Numerica's radar line). Anduril appears beside the Clear Align award.
- **No one appears to run it as a data-driven lineage arbitrage.** Nothing in my searches showed a
  firm whose thesis is "buy dormant SBIR lineages ranked by an ML match to current requirements."
  This is the open gap.
- **The government counter-party problem.** Contracting officers *may* use Phase III. The statute
  says agencies should do so "to the greatest extent practicable", but they often do not. Rivals can
  protest; Digital Force lost its protest, but each protest costs months.

**Ceiling (sourced).**
- Navy Phase III obligations were **$1.20B in FY23**, the second year above $1B: 440 actions and
  158 small businesses (DON FY23 SBIR Year in Review).
- The Air Force's Phase III rose from $309M to $977M by 2021 (Acquisition Talk).
- DoD-wide Phase III is therefore plausibly $2.5-4B a year (my estimate, not sourced).
- A single Phase III can be many times the Phase II it derives from: one example was $42M from a $1M
  Phase II (unverified, anecdotal).
- The asset-sized ceiling is a defence company built on several lineages, valued like TransDigm
  ($8.83B FY25 sales, 53.9% EBITDA margin, built on proprietary sole-source positions). That
  requires execution: you still have to build the system.

**First proof (2-4 weeks, no data purchase).**
1. Pull the SBIR.gov bulk award file and the FPDS Phase III flag. Both hosts are blocked here, so
   run this from a laptop.
2. Backtest: from Phase II awards made in 2012-2018, predict which lineages received at least $10M
   of Phase III within 5 years. Use abstract and requirement-text similarity plus dormancy features.
3. Compare against an agency x topic x firm-size lookup baseline.
4. **Kill if the AUC lift is below 0.05**, the same test that killed grid queues.
5. Separately, count how many top-ranked lineages sit in firms that are inactive in SAM. That
   number is the purchasable inventory.

**GitHub mirror.** None found. GitHub search finds only a 2015 hiatus project
(AnnaVM/SBIR_Project), which notes the dataset alone "was not rich enough" to predict Phase I to
Phase II. That is a warning: the signal must come from joining requirement text, not from the award
file alone.

**Scores:** data 8, ML edge 6, exclusivity 8, cheap claim 7, asset ceiling 6, independence from an
incumbent's permission 3, crowding 5. **Overall 6.**

---

## B. First qualified replacement for obsolete defence parts (3/10); B2 authorised aftermarket (4/10)

**Data.**
- DLA DIBBS solicitations and the 24-month SRVA demand forecasts, public under CICA and the
  small-business mandate.
- FPDS J&As that cite "only one responsible source".
- **GIDEP is not public.** It is restricted to members (government and industry participants), so
  DMSMS notices are not an open dataset. OEM PCN/EOL notices are public but scattered.

**ML problem.** Rank NSNs by spend x price escalation x original-maker disappearance x
reverse-engineering feasibility.

**Owned and exclusivity.** A source-approval request (SAR) or first-article approval makes you an
*approved* source, not the only one. DLA's stated aim is break-out to competition, so being first
erodes once a second source qualifies.
- The TransDigm model works because TransDigm owns the design and the type certificate. A
  replacement supplier holds neither.
- Requalification cost does protect incumbents on low-volume parts, but those parts are small (DLA
  excludes NSNs under $10k/yr from reverse engineering).
- Round 2 already scored this 3.

**Who does it.** Hundreds of reverse-engineering shops and AI-for-legacy-drawings SBIR topics.
**Hadrian raised $1.37B at about $7.9B in Aug 2026** (Manufacturing Dive), but for capacity
(munitions, submarines, PAC-3 and THAAD parts for Lockheed), not exclusivity. Divergent sells
capacity in the same way.

**B2, the authorised aftermarket.**
- **Rochester Electronics** holds die, masks and licences from **70+ semiconductor makers**: 12
  billion die in stock, 70,000 device types it can make, 200,000 part numbers (eeNews Europe).
- This is the real exclusive form of obsolescence value: the OEM licenses the product line to one
  continuation maker.
- An ML edge could predict which chip families will be EOL'd before PCNs land. But the licence is
  negotiated with the OEM, not claimed first-come.
- Rochester, Micross and Flip Electronics already occupy the space. **4.**

## C. Space (2-3/10)

**Data.** The data is public but not the edge:
- Space-Track and CelesTrak SATCAT and TLEs: public by US policy to promote safe operations. A
  GitHub mirror exists, **astrion-tech/celestrak-mirror**, refreshed every 30 minutes and reachable
  from here.
- FCC Part 25 and ITU filings, and UCS's satellite database.
- Insurance loss data comes mostly from Seradata, which is paid.

**What could be owned.**
1. **Salvage of defunct objects.** There is no maritime-style salvage in orbit. Under Outer Space
   Treaty Art. VIII the state of registry keeps jurisdiction and control indefinitely, so derelicts
   are not abandoned property. Debris removal needs the owner's consent. A 2022 JBIS paper argues
   only a "potential" basis for harvesting without consent. Nothing is claimable.
2. **Buying insurer-owned wrecks.** This has a real precedent: AsiaSat 3 (1997).
   - It was stranded by an upper-stage failure. Its 27 insurers declared a total loss and took the
     asset.
   - Hughes Global Services took it on a profit-share. It rescued the satellite with lunar flybys,
     and PanAmSat acquired it in 1999 (as HGS-1, renamed PAS-22) for about half a normal life
     (Wikipedia).
   - It is a real asset purchase, but the spectrum and orbital slot belong to the operator and its
     administration, not to the hardware.
   - Total losses run at a handful a year, and GEO commercial orders are shrinking.
   - Score 3.
3. **Servicing contracts.** These are services, and crowded:
   - Northrop's MEV.
   - Astroscale: FY4/2025 revenue was ¥2.46B, about $17M. Its LEXI-P life-extension deal of up to
     ¥16.9B is still a non-binding term sheet.
   - Starfish Space.
   - Katalyst: a **$30M NASA SBIR Phase III** to reboost Swift.
   - The Katalyst award is itself an instance of thesis A.
   - Score 2.

Spectrum filings were killed in round 2 (3/10) and are not re-pitched.

## D. Proven-but-abandoned national lab and ARPA-E technology (3/10)

**Data.** OSTI.gov final reports for DOE, ARPA-E and the labs, public under DOE's public-access
plan. USPTO assignments to "United States of America as represented by the Secretary of Energy" or
"of the Navy". Federal Register notices of intent to grant exclusive licences (37 CFR 404).

**ML problem.** Find technologies with proven results in a final report, no follow-on funding and no
licensee, and score their market value.

**Owned.** An exclusive federal licence. The 35 USC 209 process requires a Federal Register notice
and a 15-day objection period, prefers small businesses, and is cheap.

**Why it fails.**
1. **The pool is tiny.** Total federal-lab licence income was **about $180M in FY2017 across 6,657
   active licences** (NIST via FLC). Energy and defence deeptech is no better than the university
   picture round 1 found.
2. **Abandoned means old, and old means the patents have expired.** Tech proven and dropped 10-20
   years ago is usually in the public domain, so there is nothing exclusive left. The value then
   moves to new patents on improvements, which is ordinary R&D.
3. **The labs already run matchmaking.**
   - DOE's Emerging Tech Studio with FedTech.
   - FedTech's studios.
   - The new DOE **COMPASS** programme (SLAC, Sandia, LBNL, LANL and others; July 2026), which
     targets six spin-outs.
   - Tekcapital-style IP holding stays small-cap (round 1).

**Counter-examples.** The big energy outcomes from lab IP were mostly non-exclusive licences:
Argonne NMC cathodes went to BASF, GM and Toda (memory). Laser enrichment (SILEX) and AVLIS revival
are isotope plays, already killed.

## E. Sole qualified source on QPL/QML (2/10)

The DLA QPD lists every qualified source by specification. Specs with one or zero sources show
where qualification would be valuable, for example rad-hard QML-V microelectronics. But
qualification is not exclusive, costs $1-10M and years, and the largest specs are held by Microchip,
Renesas/Intersil, BAE and Honeywell. It is a lookup, not ML, and not claimable.

---

## What to do next

Run the A backtest (see A, "First proof"): SBIR.gov plus FPDS Phase III flags, with a 2012-2018
Phase II cohort predicting at least $10M of Phase III within 5 years, against a lookup baseline. If
it lifts AUC by 0.05 or more and finds dormant lineages in more than about 50 firms that are
inactive in SAM, write the acquire-and-build plan. Otherwise kill the lane.

## Sources

- [Ward & Berry: SBA amends Directive, successor-in-interest Phase III eligibility](https://www.wardberry.com/sba-amends-sbir-sttr-policy-directive-clarifying-broad-phase-iii-eligibility-for-the-successors-in-interest-of-phase-ii-recipients/)
- [Wiley: GAO ASRC Federal, B-418028](https://wiley.law/alert-GAO-SBIR-Phase-III-Awardees-Must-Have-Performed-Or-Been-Novated-the-Preceding-SBIR-Phase-I-Or-II-Awards-To-Be-Eligible-for-Award)
- [GAO B-423319 Digital Force Technologies (Clear Align Phase III upheld, May 2025)](https://www.gao.gov/products/b-423319)
- [Arnold & Porter: Commercializing SBIR technologies, six paths](https://www.arnoldporter.com/en/perspectives/publications/2013/03/commercializing-sbir-technologies-six-paths-to-w__)
- [Phase III is a sole source authority (substack)](https://reshmapaul1.substack.com/p/phase-iii-is-a-sole-source-authority-not-a-separate-program)
- [DON FY23 SBIR Year in Review ($1.2B Phase III)](https://navysbir.com/docs/DON-FY-23-SBIR-Year_in_Review.pdf)
- [Acquisition Talk: AFWERX Phase III $309M to $977M](https://acquisitiontalk.com/2022/01/afwerx-companies-starting-to-transition-but-jurys-still-out-scaling-transformation/)
- [National Academies 2026 review of DoD SBIR/STTR (Phase III poorly tracked)](https://www.nationalacademies.org/read/29329/chapter/5)
- [Hoover: The Warfighter's Pipeline](https://www.hoover.org/sites/default/files/research/docs/Berkenstock-Chung_The%20Warfighters%20Pipeline_web-250410_final.pdf)
- [TransDigm FY2025 Q4 release](https://www.sec.gov/Archives/edgar/data/1260221/000126022125000078/exhibit991tdg2025q4earning.htm)
- [Manufacturing Dive: Hadrian $1.37B Series D](https://manufacturingdive.com/news/hadrian-automation-1-4b-funding-manufacturing-workforce-growth/827136)
- [eeNews Europe: Rochester/ST licensed continuation](https://www.eenewseurope.com/news/st-deal-boosts-long-term-device-availability)
- [Wikipedia: HGS-1 (AsiaSat 3 salvage)](https://en.wikipedia.org/wiki/HGS-1)
- [Altagrove: Astroscale FY2025 results, LEXI-P delay](https://www.altagrove.com/grovewire-news/astroscale-fy-2025-rev-down-14-big-satellite-life-extension-mission-again-delayed-turnaround-expected-this-year-cee40)
- [Astronomy: Katalyst $30M SBIR Phase III for Swift](https://www.astronomy.com/science/swift-observatory-rescue-mission)
- [JBIS: potential legal basis for harvesting debris without consent](https://bis-space.com/shop/product/jbis-075-07-0245/); [The Space Review](https://thespacereview.com/article/2130/1)
- [FLC: NIST federal tech transfer report (FY2017 licence income about $180M)](https://federallabs.org/flc-highlights/federal-lab-news/federal-technology-transfer-successes-continue-to-increase,-nist-report-finds)
- [SLAC: DOE COMPASS programme, July 2026](https://www6.slac.stanford.edu/news/2026-07-28-compass-turning-federally-funded-inventions-economic-opportunities)
- [DOE Emerging Tech Studio](https://www.energy.gov/technologytransitions/doe-emerging-tech-studio)
- GitHub: [astrion-tech/celestrak-mirror](https://github.com/astrion-tech/celestrak-mirror); [AnnaVM/SBIR_Project](https://github.com/AnnaVM/SBIR_Project)
