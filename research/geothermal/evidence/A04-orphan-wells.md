# A04: Orphaned and idle oil and gas wells as geothermal assets

**Method note.** The shared WebSearch budget (200 calls per turn, shared across agents) was already used up before this agent started, so no open web searches ran. This file uses direct WebFetch of primary pages: the US Code, the Texas Administrative Code (Cornell LII copies), DOI, DOE, EDF, RFF, PMC/ES&T, PA DEP and E&E News. It also uses numbers that sibling evidence files computed from primary data (D01 Texas RRC, D02 Oklahoma OCC, L11 co-produced, L18 closed-loop, R07 Texas law), and each such number is attributed to its file. Several primary pages returned 404 or 403: the RRC orphan-well report page, the IOGCC idle/orphan report PDF, the NREL Blackburn PDF and the USGS undocumented-wells story. Facts that would have come from those pages are marked (unverified). There is no national count of wells plugged under the IIJA in this file, because none of the fetched pages reported one.

---

## 1. How many wells: the headline vs the usable subset

**Documented orphaned wells (US).** Source: Boutot, Peltz, McVay & Kang (2022), *Environ. Sci. Technol.* 56(20):14228–14236 (https://pmc.ncbi.nlm.nih.gov/articles/PMC9583604).
- The count rose from **81,857 (Sept 2021)** to **123,318 (Apr 2022)**, up 51% in seven months. Most of the rise came from states finding wells in their own files (Ohio +19,649, Pennsylvania +9,673, Missouri +4,812, California +2,579, New Mexico +1,771, West Virginia +1,723).
- As of April 2022, **56% sit in OH, PA, OK and KY** (17/15/13/12%). Texas was 9% of the 2021 count, about 7,400 wells (derived).
- Only **49% (40,108)** of the 2021 records have a depth at all.
- **Depth:** mean **2,474 ft (754 m)**, median **1,606 ft (490 m)**, range 6 m to 7.1 km.
- **Only 5% are deeper than one mile.** Texas holds **55%** of those deep wells and Oklahoma **25%**.
- **Undocumented wells:** the paper cites the IOGCC estimate of **310,000–800,000**, and says other studies suggest higher numbers, possibly up to a million.

**EDF Orphan Well Map** (https://www.edf.org/orphanwellmap):
- About **120,000 documented orphans in 30 states** (spring 2022).
- EPA counts **more than 2 million inactive, unplugged wells**, emitting 7–20 MtCO2e/yr of methane.
- Plugging "currently averaging **$75,000 per well**", and sometimes more than $1M.

**Texas, which has the largest inactive stock** (D01, parsed from the RRC "Wells Monitored, Aug 31 2026" PDF: https://www.rrc.texas.gov/media/pp4jbxif/august-2026.pdf):
- **431,492 monitored wells**: 273,371 active and **158,121 inactive**.
- Among inactive wells, **7,639 + 4,678 (about 12.3k)** belong to operators whose P-5 has been delinquent for more than 12 months. Under RRC practice that is the orphan pipeline.
- The BEG Geophysical Log Facility holds about **1.5M logs** (https://www.beg.utexas.edu/about/facilities/geophysical-log-facility).

**Oklahoma** (D02, computed from the OCC RBDMS CSV: https://oklahoma.gov/occ/divisions/oil-gas/oil-gas-data.html):
- **457,186 wells**: **247,647 plugged and abandoned (P&A)**, **18,060 orphan** and 1,319 temporarily abandoned.
- Since 2010 there are 1,192 straight holes ≥10,000 ft, and every well record links to scanned images.

**Alberta comparison** (CanGEA 2017, via L11: https://www.thinkgeoenergy.com/repurposing-oil-gas-wells-for-geothermal-development-a-new-database-for-alberta-canada/):
- Of about **600,000 AER wells**, **60,935 have a bottom-hole temperature (BHT) above 60 °C**, **7,702 above 90 °C**, and only **about 500 above 120 °C**.

**Read-through.** The "120k documented / 300k–800k undocumented" headline is mostly shallow, cool Appalachian and Mid-Continent wells, and is useless for power. The usable stock is the deep tail: about 5% of documented orphans, concentrated in TX and OK, plus a much larger pool of **deep inactive (idle) wells that still have a solvent operator**, such as the 158k Texas inactives. Alberta's ratio suggests that **power-grade wells (>120 °C) are well under 1% of all wells**. Finding them means pulling BHTs out of scanned logs, since neither the TX Full Wellbore file nor the OK RBDMS file has a temperature field (D01, D02). That is the same "public but illegible" problem Terranox solves in Saskatchewan.

## 2. The federal $4.7B plugging program (IIJA §40601, 42 U.S.C. §15907)

Appropriations (FY2022, available to **30 Sept 2030**) (https://www.law.cornell.edu/uscode/text/42/15907):

| Component | Amount |
|---|---|
| Federal lands program | $250M |
| State initial grants | $775M |
| State formula grants | $2,000M |
| State performance grants (matching + regulatory improvement) | $1,500M |
| Tribal program | $150M |
| DOE research | $30M |
| IOGCC | $2M |
| **Total** | **≈ $4.7B** |

**Key statutory language for a geothermal play:**
- An **"idled well"** has been nonoperational for **at least 4 years** with **"no anticipated beneficial future use."** An **"orphaned well"** is not used for an "authorized purpose, such as production, injection, or monitoring."
- The definitions therefore depend on use: **a well with a documented beneficial (geothermal) use is not, by definition, an idled/orphan target.** This is the legal hook for pulling deep candidates out of the plugging queue.
- Regulatory-improvement grants reward state reforms to "**well transfer or temporary abandonment**" programs.
- Formula applications net out "estimated salvage of well site equipment," so the statute already treats well assets as having residual value.
- The statute does **not** mention geothermal or repurposing.

**Status:**
- DOI revised the **$780M State Matching** and **$1.93B State Formula** guidance on **17 July 2025** (https://www.doi.gov/pressreleases/orphaned-wells-program-news).
- **Phase 3 State Formula guidance** was issued in **May 2026**, and an FY2026–2030 Program Office Strategic Plan in April 2026 (https://www.doi.gov/orphanedwells).
- Federal lands: **$109.6M to five agencies for 484 high-priority sites** (16 Dec 2024).
- The program was **paused in early 2025** under the IRA/IIJA funding-freeze directive. IOGCC's 12 Feb 2025 letter says states had to stop plugging jobs already underway. Funds were partly flowing again by April 2025.
- Throughput examples (https://www.eenews.net/articles/interior-slow-walks-4-7b-biden-era-effort-to-plug-old-oil-wells):
  - Kansas plugged **2,405 wells with its $25M initial grant**, roughly $10k per well (derived), because its wells are shallow.
  - New Mexico plugged **130** in the initial round, against about 50 per year before.
  - Texas plugged 45% fewer wells with formula funds than with initial funds.
- Every state got a **$25M initial grant**.

**Plugging costs.** Raimi et al. (RFF, 2021, up to 19,500 wells) (https://www.rff.org/publications/journal-articles/decommissioning-orphaned-and-abandoned-oil-and-gas-wells-new-estimates-and-cost-drivers/):
- Median **about $20k plugging only** and **about $76k with surface reclamation**.
- **Each additional 1,000 ft adds about 20%** to cost. Gas wells cost 9% more than oil wells, and rare wells cost more than $1M.
- Pennsylvania's orphan-plugging grant caps are **$40k for wells ≤3,000 ft and $70k for deeper wells** (https://www.pa.gov/en/agencies/dep/programs-and-services/oil-and-gas/legacy-wells.html). PA expects about $400M of IIJA money through 2030.
- On the 20%-per-1,000 ft rule, a 12,000–15,000 ft Gulf Coast or Anadarko well would cost several times the median. My extrapolation of **$100k–$400k+** is (unverified).

**Implication.** The state is now a motivated, funded payer to get rid of these wells, with a 2030 sunset. A deep orphan well that a private party adopts for geothermal use saves the state its plugging cost. That is a negotiating chip, the reverse of a purchase price.

## 3. Regimes for acquiring idle or orphan wells cheaply

### Texas (largest stock; the most legible rules)

**Statewide Rule 15 (16 TAC §3.15), inactive wells** (https://www.law.cornell.edu/regulations/texas/16-Tex-Admin-Code-SS-3-15):
- A well becomes "inactive" after **>12 months** with no production, injection or other permitted activity.
- Once the RRC approves an operator designation form, the new operator has **6 months** to restore, plug or get an extension.
- A plugging extension requires:
  - an approved **W-3X**;
  - a current P-5;
  - a **"good-faith claim to a continuing right to operate"**;
  - a passing fluid-level or pressure test for wells older than 25 years;
  - one of eight financial options, such as plugging or restoring 10% of inactive wells, a blanket bond, an escrow deposit of 10% of plugging cost, or an abeyance report at **$100/well/yr**.
- Wells inactive for **more than 10 years** must have their surface equipment removed.
- Abeyance and supplemental-assurance documents **do not transfer** to a new operator, who has to re-file within 6 months.

**Transfer mechanics.**
- Operator change is filed on Form **P-4**, which appears in the RRC nightly completion packets (D01).
- The buyer takes on plugging liability and has to post **Rule 78 financial assurance** (https://www.law.cornell.edu/regulations/texas/16-Tex-Admin-Code-SS-3-78):
  - blanket bond of **$25k for ≤10 wells, $50k for 11–99, $250k for ≥100**;
  - or **$2 per foot** per well;
  - bay and offshore inactive wells need +$60k or +$100k per well.
- So a single-well holder can keep a 15,000-ft well alive for a **$25k blanket bond**, or about **$30k individually**. That is tiny next to the $5–15M cost of drilling a new deep well (my generic range, unverified).

**Precedent for non-hydrocarbon handover (Rule 14(a)(4), Form P-13)** (https://www.law.cornell.edu/regulations/texas/16-Tex-Admin-Code-SS-3-14):
- A **surface owner can take over an abandoned well** to convert it to a water well. The surface owner must **assume plugging responsibility**, binding heirs and assigns.
- The operator's liability ends once the RRC approves the application.
- No equivalent geothermal-conversion form was found. A geothermal transfer would probably go through a P-4 plus an RRC geothermal permit under Natural Resources Code ch. 141 (unverified procedure). P-13 shows that the RRC already lets someone other than the operator take a wellbore and its liability for a new use.

**Who owns the heat: SB 785 (2023), Nat. Res. Code §141.004** (R07: https://tcss.legis.texas.gov/resources/NR/htm/NR.141.htm):
- Geothermal energy belongs to the **surface owner** when the estates are severed.
- Brine minerals are excluded, and the mineral estate stays dominant.
- So a Texas idle-well deal has three parties: the **operator** (wellbore and liability), the **surface owner** (heat right) and the **mineral owner** (dominant estate).

### Other states and the federal side
- **Oklahoma:** the DOE Wells of Opportunity Tuttle project "secured the **first permit in Oklahoma to convert oil and gas wells for geothermal use**" (https://www.energy.gov/eere/geothermal/wells-opportunity). There are 18,060 OK orphans (D02).
- **BLM:** Gradient Geothermal (formerly Transitional Energy) at Blackburn, NV "secured a Bureau of Land Management lease and approvals, creating a **pathway for future BLM well conversions**" (same DOE page).
- **Pennsylvania:** no operator "adoption" programme appears on the DEP page that was fetched. It pays Qualified Well Pluggers instead. Other state adoption schemes, such as Ohio and Alberta's Orphan Well Association, were not verified in this run.

## 4. Pilot conversions so far: small, few, mostly unreported

**DOE Wells of Opportunity, ReAmplify:** up to **$8.4M for 4 projects** (https://jpt.spe.org/doe-program-seeks-to-reuse-abandoned-oil-wells-for-geothermal-production ; https://www.energy.gov/eere/geothermal/wells-opportunity). Per L11, the success bar is about 1 MW for one year.

| Project | Wells | Award | Status |
|---|---|---|---|
| Gradient/Transitional, Blackburn NV | Not stated | **$2.5M** (L11) | Phase 1 feasibility done, BLM approvals in hand. A 2022 self-funded pilot at a Grant Canyon well powered field operations, MW undisclosed (https://www.thinkgeoenergy.com/transitional-energy-generates-geothermal-energy-from-oil-and-gas-well/) |
| ICE Thermal Harvesting, CA | **11 existing wells** in the San Joaquin Valley | **$1.7M** (L11) | No public results |
| Geothermix, TX | Not stated | Not stated | Thermoelectric cells built and only lab-tested |
| University of Oklahoma, Tuttle | **4 wells** within a mile | Not stated | First OK conversion permit; repair work begun. Use is direct heat for schools |

**Other re-entries:**
- **Sage Geosystems** re-entered the **P&A JFB Heard 1** gas well in Starr County, TX (about 19,000 ft TVD) for fracture energy storage. It reported about **1 MW peak** over a 44-minute flowback (GRC Trans. 47, via L18).
- Co-production pilots (RMOTC, UND, Swan Hills, Pleasant Bayou) are **0.1–1 MW**. Razor Energy's Swan Hills hybrid ended in insolvency (L11).
- Single-well closed-loop retrofits give **tens to a few hundred kWth** (L11, review literature).

**Read-through.** No orphan-well-to-power conversion is yet running commercially in the US at MW scale (inference from the sources above). Single wellbores are kW to about 1 MW assets. Value at scale needs **field-level** reuse (many wells, water-only production, re-injection) or deep re-entries used as **cheap exploration and test holes** for EGS or sedimentary geothermal.

## 5. Can you buy wellbores cheap? Yes, often for less than zero

- **Price.** A deep idle wellbore on a marginal lease costs the operator its plugging liability (about $20k–$76k median, much more for deep wells) plus bond and Rule 15 compliance costs. Distressed and delinquent-P-5 operators (about 12.3k Texas inactive wells) and states paying out IIJA money both have reasons to hand wells over. A buyer can plausibly get the wellbore for **$0, or be paid** with some or all of the avoided plugging cost (inference, unverified by any closed deal found).
- **What you actually get.**
  - A drilled hole to 3–6 km in sedimentary basins.
  - Casing records, logs, BHTs and DSTs in the RRC/OCC files.
  - Often injection or disposal infrastructure nearby.
  - Drilling is commonly cited as 30–60% of geothermal capex (unverified, L11).
- **What you do not get.**
  - Guaranteed integrity: wells >25 yrs old need tests, and cement or casing in old wells is often poor.
  - Large-diameter completions: typical 5.5-in production casing limits flow (unverified).
  - The heat right itself, which in Texas belongs to the surface owner under SB 785 and needs a separate lease.
  - Freedom from the dominant mineral estate.
- **Main risk.** The buyer inherits the full plugging liability. The deep wells that matter most are the most expensive to plug, so a failed test flips the asset into a negative-value liability. That risk can be bounded with Rule 78 bonding ($25k blanket for ≤10 wells) and well-specific plugging insurance (allowed under Rule 78).

---

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **Orphan wells as the primary asset fail the "too small" test.**
   - About 95% of the 120k documented orphans are shallower than one mile, and single-well conversions top out at kW to about 1 MW.
   - An "orphan-well geothermal" company that sells conversions or plugging-avoidance services is a service shape, which scores low.
2. **As a cheap acquisition-and-proof layer inside a sedimentary or hot-basin land play, they are strong.** The Terranox loop maps cleanly:
   - **Illegible public data.** Millions of TX and OK well files and about 1.5M BEG logs exist, but there are no temperature fields; BHTs sit in scanned images.
   - **ML.** Correct BHTs, rank the under-1% of wells above 120 °C, and flag deep idle wells near favourable structure.
   - **Acquire before proof.** In one move, take the **SB 785 surface geothermal lease** (cheap, no auction, no comparables: R07) plus a **P-4 transfer of the idle wellbore** (about $0 plus a $25k bond).
   - **Prove cheaply.** Run a re-entry, temperature log and flow test for hundreds of thousands of dollars instead of a $5–15M new well (unverified generic figure).
   - **Sell the proven block** to Fervo-style EGS developers, Sage/XGS-style closed-loop and storage players, or data-centre offtakers in ERCOT, at a step-up.
3. **Policy tailwind with a deadline.**
   - The IIJA's "no anticipated beneficial future use" test, plus $4.7B of plugging money available to 2030, makes states motivated counterparties.
   - The "well transfer" regulatory-improvement grants give states a reason to create transfer-for-reuse paths.
   - Tuttle (OK) and Blackburn (BLM) already set conversion-permit precedents.
   - Risk: deep candidates get plugged and lost if nobody claims them first. That makes speed of identification itself part of the moat.
4. **Gap vs Zanskar.**
   - Zanskar works Great Basin blind hydrothermal systems: physics plus ML on geophysics and gradient holes, BLM leases, drilling new wells, and buying plants (Lightning Dock).
   - No public evidence was found that Zanskar works on petroleum well archives, Texas or Mid-Continent sedimentary basins, private surface geothermal estates, or idle-wellbore acquisition (unverified absence; see Z01–Z05).
   - The open niche is **"own the deep idle wellbores plus the surface heat rights in oil country, found by ML on petroleum archives"**. It does not compete with Zanskar on geography, data or land regime.
   - Its weaknesses are lower grades (sedimentary heat at 120–180 °C needs EGS or large-flow production to reach utility MW), integrity and liability risk, and the three-party rights stack in Texas.
5. **Score (standing rules: assume the tech works, own the asset).**
   - Orphan wells as a standalone thesis: **low**.
   - Idle deep wellbores as the cheap "assessment hole" plus a lever for owning Texas and Oklahoma geothermal blocks: **medium-high**, and the most Terranox-like asset mechanism in oil country.

---

## Sources
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9583604 (Boutot et al. 2022, ES&T)
- https://www.edf.org/orphanwellmap
- https://www.law.cornell.edu/uscode/text/42/15907
- https://www.doi.gov/orphanedwells
- https://www.doi.gov/pressreleases/orphaned-wells-program-news
- https://www.eenews.net/articles/interior-slow-walks-4-7b-biden-era-effort-to-plug-old-oil-wells
- https://www.rff.org/publications/journal-articles/decommissioning-orphaned-and-abandoned-oil-and-gas-wells-new-estimates-and-cost-drivers/
- https://www.law.cornell.edu/regulations/texas/16-Tex-Admin-Code-SS-3-15
- https://www.law.cornell.edu/regulations/texas/16-Tex-Admin-Code-SS-3-14
- https://www.law.cornell.edu/regulations/texas/16-Tex-Admin-Code-SS-3-78
- https://tcss.legis.texas.gov/resources/NR/htm/NR.141.htm
- https://www.rrc.texas.gov/media/pp4jbxif/august-2026.pdf (via D01)
- https://www.beg.utexas.edu/about/facilities/geophysical-log-facility (via D01)
- https://oklahoma.gov/occ/divisions/oil-gas/oil-gas-data.html (via D02)
- https://www.energy.gov/eere/geothermal/wells-opportunity
- https://jpt.spe.org/doe-program-seeks-to-reuse-abandoned-oil-wells-for-geothermal-production
- https://www.thinkgeoenergy.com/transitional-energy-generates-geothermal-energy-from-oil-and-gas-well/
- https://www.thinkgeoenergy.com/repurposing-oil-gas-wells-for-geothermal-development-a-new-database-for-alberta-canada/ (via L11)
- https://www.pa.gov/en/agencies/dep/programs-and-services/oil-and-gas/legacy-wells.html
