# Final ranking, best pick and missed regimes

**Headline:** none of the 12 shortlisted ideas clears the size bar as a pure data or SaaS company. Every deep dive puts the analytics market at about $30-400M a year, the same range Dhruv already rejected. The ideas that could become large companies all take on risk using the data edge: an insurance agency that underwrites for a carrier (MGA), a lender or a claims funder. So I ranked on three things: how well the data gives an underwriting edge, whether a risk-transfer market already exists to plug into, and fit with Dhruv's background.

**Search budget:** the shared web-search budget ran out before any of my searches ran. I made one page fetch, the CMS dispute-resolution reports page. Everything in section 3 except that one regime comes from prior knowledge and is not verified.

## 1. Ranking

| # | Idea | Score sum* | Verdict |
|---|---|---|---|
| 1 | **Decommissioning-liability underwriter** (well files, closure and orphan risk, then reclamation bonds through an MGA) | 27 | Closest analog to SMAD: decades of forced filings that read like geology, held in Canadian and Texas archives. Fewest crowding signals of the 12. The rival rating is the regulator's own crude ratio, so beating it is a clean, provable result. Fits Dhruv: subsurface work, Canadian regulators, Saskatchewan. Weaknesses: the software alone tops out at about $200-400M, and bond prices are often set by statute. |
| 2 | **Subsurface contamination / pollution-liability pricing** (California GeoTracker data) | 26 | Huge, rich dataset (230M+ lab results). Fatal selection bias: there are no clean-parcel negatives. LightBox/EDR owns the lender-screening channel and the PFAS piece is weak. Best used as the **expansion** of #1 into one "subsurface liability" pricing engine, not as the starting wedge. |
| 3 | Florida condo structural and financial distress | 23 | Real money flows through it: special-assessment lending and non-warrantable mortgages. But the state's own auditor calls the data incomplete, it is Florida-only, there are under 2 years of outcomes, and the condo-review screens Fannie Mae and Freddie Mac already run gate the lending decision. |
| 4 | Mass-tort forecaster / casualty litigation catastrophe model | 23 | The pain is enormous: tens of billions of reserve strengthening. But there are only about 100-150 product mass-tort consolidations (MDLs) as labels, and most of the biggest torts never showed up in FDA adverse-event data first. Praedicat (backed by Verisk) has sold this for about 10 years and stayed small, which suggests a thin market. |
| 5 | Virtual site investigation from Dutch BRO soil tests | 23.5 | Clean open data. Fugro GroundIQ is already building this, and Fugro holds the biggest private archive. The Netherlands is a small market and the demand (US data centres) sits on geology the Dutch data doesn't cover. |
| 6 | Virtual teardown from FCC equipment filings | 23.5 | Original, but RF shield cans hide the valuable chips, parts lists stay confidential, and the market is about $50-150M. |
| 7 | Standard-essential-patent (SEP) essentiality engine | 21 | AI claim charts already ship (PatSnap). The real barrier is court and licensor trust, not technology. |
| 8 | OSHA workplace-injury risk scoring | 21 | Covers the wrong accounts: large, broker-placed employers, not small businesses. Carriers already see better data (the employer's own loss history). |
| 9 | Vehicle recall forecaster | 21 | The most predictive data (manufacturers' warranty counts filed with NHTSA) stays confidential. Viaduct and We Predict show where this ends: a tuck-in acquisition and a quiet pivot away. |
| 10 | Unrated-municipal-bond shadow rating | 20 | Small buyer pool, crowded, and the founder has no muni network. |
| 11 | Private-credit marks from insurers' statutory filings (NAIC) | 19 | Data is paid and licensed, marks are once a year, stale and correlated across insurers, and S&P and Clearwater already show this view. |
| 12 | AI regulatory reviewer on published regulator dossiers | 18 | Legally dead. Health Canada's terms (checked) ban commercial use and any use supporting a drug application, and EMA's appear to match (from memory). What is left is about 458 FDA rejection letters in a crowded category. |

\*Score sum = moat + revolutionary + market + uncrowded + feasibility, as scored in the deep dives. Below #2, I broke ties on who actually pays and where risk can be transferred.

## 2. Best pick: subsurface liability underwriting, starting with orphan-well and closure liability in Western Canada

**Why:**
- It has the same shape as Terranox. Decades of mandated operator filings exist, nobody reads them at scale, and a model that reads them all sees what the market can't.
- The money is in pricing liability, not finding resources. That makes it clearly not a Terranox clone.
- The incumbent's benchmark is weak. The Alberta Energy Regulator (AER) has rated licensee risk with a simple assets-to-liabilities ratio (the LMR, now replaced by its Licensee Capability Assessment, LCA), and that ratio missed many insolvencies.
- **Path to a large company:**
  1. A licensee-risk and inactive-well liability rating, sold to acquirers, lenders, AER-facing consultants and Class VI carbon-storage developers.
  2. A closure-cost and orphan-probability model for each well.
  3. An MGA writing well-plugging, mine-reclamation and renewables-decommissioning bonds, plus pollution-liability cover by merging in #2's GeoTracker model.
- Decommissioning-bond and pollution-liability premiums together are the multi-billion pool. Software alone is not.

**Risks to underwrite before committing (still open):**
- Whether Alberta and Saskatchewan regulators accept market surety bonds as security, and in what volume (not verified).
- The software ceiling of about $200-400M.
- An MGA needs a fronting carrier.
- Enverus and S&P own the digitized US well data.

**One-day proof on real public data** (run on a laptop; this container's proxy blocks most government hosts):
1. **Data (all free):**
   - AER ST37 well list, monthly snapshots, with licensee and status.
   - Petrinex public monthly volumes for Alberta, and for Saskatchewan as a second test.
   - AER's published LMR/LCA licensee ratings and liability-management reports.
   - The Orphan Well Association inventory and AER orphan, receivership and closure-order notices, as labels.
2. **Label:** a licensee that is designated orphan, enters receivership or insolvency, or receives an AER closure or abandonment order within 24 months.
3. **Training and test windows:** train on snapshots from 2015-2019, test on 2020-2023 events. Hold out by time, never mixing a licensee across splits.
4. **Features, by licensee:**
   - well count, and the inactive share and its trend
   - how long wells have been inactive, and their age
   - production decline and water cut
   - number of sour wells
   - deemed liability per producing barrel of oil equivalent
   - well-transfer activity, to catch assets being dumped
   - how concentrated wells are by area
   - months since any well was abandoned
5. **Baseline:** the regulator's own LMR/LCA rating at the same date.
6. **Model and metrics:** gradient boosting. Report AUC, top-decile precision, and the **share of eventual orphaned dollar liability captured in the top decile** against the regulator's ratio.
7. **Pass bar:**
   - AUC at least 0.05 above the regulator's ratio, and
   - a top decile that captures materially more orphaned liability (for example, 1.5x).

   That is a result you can tweet: "our model beat the regulator's own rating."
8. **Optional second half (same day):** have a vision model read about 300 scanned Texas RRC plugging records and score field accuracy against the RRC's structured data. That proves cheap document reading for the well-level product.

**Kill criterion:** if the model cannot beat the regulator's ratio by a clear margin, the underwriting edge is not there. Drop it and fall back to the GeoTracker cost-to-close test (#2, Task A).

## 3. Forced-disclosure regimes the sweep missed

- **No Surprises Act federal arbitration (IDR) public use files. Verified on cms.gov; the most important miss.**
  - What it is: Congress requires CMS to publish outcomes of the arbitration process that settles out-of-network billing disputes between providers and health plans.
  - Volume (verified): 7.05M disputes from April 2022 to July 2026, now 300-400k a month (394,140 in July 2026). CMS publishes dispute-line-item files each quarter for 2023 through Q4 2025. Starting with the late-2025 files, each line also names the arbitration entity that decided it.
  - Likely fields (from memory, check against the data dictionary): service code, the parties, both offers relative to the plan's benchmark rate, and which side won.
  - Why it matters: this is a fast-growing, multi-billion-dollar arbitration market where ML could predict who wins and price disputes. The payer-side defense (which disputes to fight, settle or contest) may be the bigger buyer set.
  - Risks (unverified): crowded on the provider side (HaloMD and big physician groups' in-house teams) and by Claritev/MultiPlan and Zelis on the payer side. It is politically volatile, and it is litigation-arbitrage rather than "revolutionary". Still, it deserves its own deep dive because it likely clears the size bar.
- **Missed and unverified (from prior knowledge):**
  - SEC asset-level filings for public securitisations (Reg AB II ABS-EE: monthly loan-level auto and lease performance on EDGAR). Already partly mined, for example by dv01.
  - ERCOT's 60-day disclosure of each generator's bids and offers. Crowded with power-analytics firms.
  - The CFTC's real-time public swap trade data. Clarus already uses it.
  - NRC licensee event reports and the ADAMS document archive. These are in Dhruv's own domain, but nuclear-adjacent ideas were already rejected.
  - USGS/BOEM's archive of industry marine seismic, released after confidentiality. A Terranox-clone class.
  - EU EUDAMED device safety and clinical-performance summaries.
  - UK DVSA MOT vehicle-inspection results (per-vehicle bulk open data).
  - City building-energy benchmarking laws. Crowded.

  None looks stronger than the IDR files.

Sources:
- [CMS No Surprises IDR reports and PUFs](https://www.cms.gov/nosurprises/policies-and-resources/reports)
- Plus the deep-dive sources above: AER ST37, Texas RRC data sets, AER 2024 liability-management performance report, ABlawg 2026 review, and the Water Board GeoTracker data-fair deck.