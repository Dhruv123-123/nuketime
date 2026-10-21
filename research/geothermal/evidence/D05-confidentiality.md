# D05: How long well data stays confidential, by jurisdiction (the analogue of Saskatchewan's 3-year assessment-file release)

**Method note.** The shared WebSearch budget for this run (200 calls per turn) ran out before this agent's first query. Everything below comes from direct fetches of primary legal texts:
- Cornell LII for 43 CFR, 5 USC and 16 TAC;
- the Nevada and Oregon legislatures;
- BC Laws;
- the Alberta King's Printer PDF of the Oil and Gas Conservation Rules, text extracted locally;
- sibling evidence files D01, D03, R11 and L20 in this folder, which hold their own primary URLs.

California (leginfo and Justia both returned 403), Idaho (503), New Mexico (DNS failure) and Saskatchewan (CanLII 403, publications portal 404) could not be fetched. Their figures are marked (unverified).

## 1. Summary table

| Jurisdiction / data class | Confidential period | Trigger and notes | Source |
|---|---|---|---|
| **Texas** oil and gas logs (RRC Rule 16) | **Public on filing.** Filing is due within 90 days. Operator can delay filing by **3 years** (5 years on state submerged land). | The 3-year roll-off runs continuously, so it is the closest US match to SMAD. | 16 TAC 3.16 |
| **Alberta** oil and gas well data (OGCR 12.150(4)) | **1 year** from finished drilling date | Covers logs, DST, wireline, **pressure, temperature and flow test data**, completions, core analysis. Test holes: 5 years for log, location and elevation (12.150(7)). Experimental-scheme data: 5 years after scheme approval, extendable (12.150(8)). Reserves info: 15 years (12.152). | AR 151/71 |
| **BC** oil and gas well data (ERA General Reg s.17) | **2 months** (development), **6 months** (exploratory outpost), **1 year** (wildcat or discovery), **18 months** (special data well), **3+ years** (special project) after rig release | Geological and geophysical reports: 10 years (work-program credit) or **21 years** otherwise (s.16) | BC Reg 274/2010 |
| **BC geothermal** (Geothermal Resources General Reg s.11) | Well reports, data and cores: **2 years after rig release**. Geothermal (exploration) reports: **2 years after permit terminates**, or 5 years after conversion to a lease. | Early release if rights revert to the Crown. Cabinet may release in the public interest. | BC Reg 39/2017 |
| **Nevada geothermal** (NRS 534A.031) | **5 years after filing** | Must be filed within 30 days of being accumulated. Covers "exploration and subsurface information" (whether this covers gradient holes is inferred, not verified). Releasing it earlier needs the operator's written consent. | NRS 534A |
| **Nevada oil and gas** (NAC 522.540) | **1 year** after drilling, and only if the operator asks | Bottom-hole temperatures (BHTs) in log headers of Nevada wildcats are effectively public | D03 / NAC 522 |
| **Utah geothermal** (Utah Code 73-22-6(4), amended 2026) | **Public when filed** unless protection is requested. Protection is capped at the earliest of 5 years from production or injection, or **2 years** from completion of an exploration or test-well project. | DOGM oil and gas data carries explicit `ConfRelDate` release dates | D03 (Utah fetch for this file failed) |
| **Oregon geothermal** (ORS 522.365(2)) | **4 years** after DOGAMI receives the log, history or core record | Treated as a trade secret under ORS 192.345 unless the operator consents to release | ORS 522 |
| **Federal / BLM geothermal** (43 CFR 3255.12, 3266.12, 3278.12) | **No fixed end date.** "The FOIA does not provide a finite period of time during which information may be exempt from public disclosure"; BLM decides case by case under 43 CFR part 2. | FOIA exemption (b)(9) covers "geological and geophysical information and data, including maps, concerning wells." Only surface location, elevation and well status are never confidential (3266.10). Exploration on unleased land, or land you do not lease, **need not be reported at all** (3253.10(b)). | 43 CFR 3200; 5 USC 552 |
| **California geothermal** (PRC 3752) | (unverified) Believed to be confidential for a limited period, commonly cited as up to 5 years, or while the operator keeps the well in confidential status | Fetch blocked (403) | n/a |
| **California oil and gas** (PRC 3234) | (unverified) Commonly cited as 2 years for exploratory wells | Fetch blocked | n/a |
| **Saskatchewan oil and gas** (OGCR 2012) | (unverified) Believed to be about 1 year for most well data, with longer terms for experimental schemes | CanLII 403. Saskatchewan has no stakeable geothermal tenure (R11). | n/a |
| **Saskatchewan mineral assessment (SMAD)** | 3 years (task premise) | This is the benchmark | n/a |
| **Alberta geothermal** (GRDA, AR 250/2021, Directive 089) | (unverified) The King's Printer PDF has no extractable text. Directive 089 says oil and gas requirements apply broadly, so the OGCR 1-year rule probably extends to geothermal wells (inference). Alberta Energy treats Geothermal Assessment Reports as confidential (R11). | Alberta has only 31 geothermal leases, held by 6 holders (R11) | n/a |

## 2. Key primary-text extracts

**Alberta OGCR s.12.150(4)** (fetched PDF, AR 151/71 as amended to 2025):
> "the Regulator, after one year from the finished drilling date or the start of substantially uninterrupted suspension of drilling operations at a well or an oil sands evaluation well, shall make available to the public ... any log, drill stem test data, wire line formation test data, pressure, temperature and flow test data, completion details..."

The rule explicitly names **temperature** data. About 450k+ Alberta wells (unverified count) therefore have public BHT, DST and log temperatures one year after drilling. The AER's ST37 well list is a public download (1.23 GB geodatabase; L20). One caveat is s.12.150(11): the AER does not have to publish the data, only to make it available on request, for viewing, for a fee. The data is legally public but practically illegible, which is the Terranox wedge.

**BC ERA General Regulation s.17(1)**, release after rig release:
- development well: 2 months;
- exploratory outpost: 6 months;
- exploratory wildcat: 1 year;
- discovery re-entry: 1 year;
- special data well: 18 months;
- special project: the later of 3 years and the applicable period above.

Once released, data cannot be made confidential again (s.17(5)). G&G reports take 10 or 21 years (s.16), so seismic interpretations stay closed much longer than well data.

**BC Geothermal Resources General Regulation s.11**: data must be held confidential, then released:
- reports: 2 years after the permit terminates, or 5 years after conversion to a lease;
- well data and cores: 2 years after rig release.

This is structurally the same as SMAD: **failed or lapsed permits feed a public archive.**

**Nevada NRS 534A.031(1)**: "The information is confidential for 5 years after the date of filing" and "may not be disclosed during that time without the express written consent of the operator." Two consequences follow:
- every Nevada geothermal exploration and gradient-hole dataset filed before about Oct 2021 is legally public now;
- every dataset filed from the 2021–2026 Great Basin rush (Zanskar, Fervo, Ormat, Cyrq) **rolls into the public domain on a rolling 5-year schedule through about 2031**.

NDOM's table lists 938 permitted geothermal wells (D03). Nevada also holds operators' records 5 years after operations end (NAC 534A.560).

**Texas 16 TAC 3.16(d)**: each log filed "shall be considered public information." Logs are filed within 90 days, and delayed filing is allowed for "three years beginning from the date the drilling operation was completed" (5 years on state submerged land). D01 reports about 1.5M logs.

**Oregon ORS 522.365(2)**: "For a period of four years after the receipt of any log, history, core record ... such record shall be exempt from disclosure as a trade secret ... unless the operator gives approval."

**BLM (43 CFR 3266.12)**: "The FOIA does not provide a finite period of time during which information may be exempt from public disclosure." Combined with FOIA Exemption 9 (5 USC 552(b)(9): "geological and geophysical information and data, including maps, concerning wells"), federal well data can in principle be withheld **indefinitely**. 43 CFR 3253.10(b) adds that exploration on unleased federal land generates **no filing duty at all**.

## 3. What this means structurally

1. **Release clocks for oil and gas well data are very short: 2 months to 1 year in AB, BC and NV, and 0–3 years in TX.** The global inventory of oil and gas BHTs, DSTs and temperature logs is therefore essentially all public. The binding constraint is legibility (scanned TIFF headers, uncorrected BHTs), not law.
2. **Geothermal-specific data is held longer: 2 years (BC, Utah exploration), 4 years (OR), 5 years (NV, likely CA), indefinitely (BLM).** These are the closest analogues to SMAD's 3 years. They have the same feature that makes SMAD valuable: other people's failed and lapsed exploration becomes public on a predictable schedule.
3. **A federal blind spot.** Because of the BLM FOIA treatment and the absence of any reporting duty on unleased land, the best Great Basin exploration data is often filed only under **state** law (NV 534A; that it applies to NDOM-permitted wells on federal land is an inference, unverified). The state file is the one that eventually opens. The federal file may never open.
4. **Predictable release calendars are a lead-time asset.** A model that ingests each month's newly released NV, BC, UT and OR geothermal files, plus newly public oil and gas logs, sees prospects the day they become public. Other players see them whenever someone gets around to reading the PDFs. This is the Terranox SMAD play almost one-for-one.

## 4. Implications for a Terranox-shape geothermal company and the gap vs Zanskar

- **The analogue is real and in places better than SMAD.** Release windows are:
  - Nevada geothermal: 5 years (5 years after filing);
  - BC geothermal: 2 years;
  - Utah geothermal: 2 years after an exploration project;
  - Oregon: 4 years;
  - Texas oil and gas: 3 years at most;
  - Alberta and BC oil and gas: 1 year or less, temperature data named explicitly.

  Every one of these is a statutory "other people's exploration spend becomes public" pipe, like Saskatchewan's assessment files.
- **The highest-value calendar is Nevada 2026–2031.** The gradient-hole and slim-hole data from the 2021–2026 Great Basin leasing and drilling boom (938 permitted geothermal wells statewide) is filed with NDOM under a 5-year clock. Datasets from projects that were dropped, or from leases that lapsed, will become public while the adjacent BLM ground may be relinquished or never leased. A company that systematically FOIA-requests, ingests and models these releases can nominate and lease that ground through BLM noncompetitive or competitive sales before anyone else reprocesses it. This works because nominations are anonymous until the sale (R03).
- **Zanskar's gap.** Zanskar's public model (Z01–Z05) runs its own physics-plus-ML over regional public data and then **drills its own gradient holes and develops plants itself** (Big Blind, the Lightning Dock acquisition). It is a vertically integrated developer optimising for its own pipeline. No fetched source shows Zanskar running a release-calendar arbitrage: systematically harvesting competitors' newly declassified NV, UT, OR and BC geothermal files and oil and gas BHTs in AB, TX and BC, then buying rights to resell (absence unverified). Its own data is also partly **subject to the same clocks**: its NV gradient-hole filings become public about 5 years after filing. A Terranox-shape player is the natural second reader of Zanskar's own exploration.
- **Sedimentary basins are where legal openness is highest and competition lowest.** Alberta (1-year oil and gas release; first-come geothermal leases; only 31 leases, held by 6 holders) and Texas (3-year roll-off; about 1.5M logs; private geothermal rights) have the most public temperature data and the fewest geothermal land buyers. Zanskar is a Great Basin hydrothermal company. The open lane is "own the sedimentary-basin heat rights that public oil and gas data already proves."
- **Risks to underwrite.**
  - BLM data never has to open, so federal-only targets lean on state filings.
  - California and Saskatchewan rules are unverified.
  - In Alberta and BC, geothermal tenure sits next to oil and gas and lithium tenure, so the economics can stack (heat plus brine).
  - Practical access is often on-request and for a fee (AB s.12.150(11)), not bulk. That is friction for the company but also part of the moat.

## Sources
- Texas 16 TAC §3.16 (Rule 16; logs public, 3-year/5-year delay): https://www.law.cornell.edu/regulations/texas/16-Tex-Admin-Code-SS-3-16
- Alberta Oil and Gas Conservation Rules, AR 151/71, s.12.150 and 12.152: https://kings-printer.alberta.ca/documents/Regs/1971_151.pdf
- Alberta Geothermal Resource Development Regulation AR 250/2021 (fetched; text not extractable): https://kings-printer.alberta.ca/documents/Regs/2021_250.pdf
- AER Directive 089: https://www.aer.ca/regulating-development/rules-and-directives/directives/directive-089
- BC Energy Resource Activities General Regulation, BC Reg 274/2010, ss.14–17: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/274_2010
- BC Drilling and Production Regulation, BC Reg 282/2010 (s.73(5) cross-reference): https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/282_2010
- BC Geothermal Resources General Regulation, BC Reg 39/2017, s.11: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/39_2017
- Nevada NRS 534A.031: https://www.leg.state.nv.us/nrs/nrs-534a.html
- Nevada NAC 534A (.550 logs, .560 records): https://www.leg.state.nv.us/nac/nac-534a.html
- Nevada NAC 522 (oil and gas, .540): https://www.leg.state.nv.us/NAC/NAC-522.html (via D03)
- Oregon ORS 522.365: https://www.oregonlegislature.gov/bills_laws/ors/ors522.html
- 43 CFR 3266.12: https://www.law.cornell.edu/cfr/text/43/3266.12
- 43 CFR 3255.12: https://www.law.cornell.edu/cfr/text/43/3255.12
- 43 CFR 3266.10: https://www.law.cornell.edu/cfr/text/43/3266.10
- 43 CFR 3253.10: https://www.law.cornell.edu/cfr/text/43/3253.10
- 43 CFR 3264.10: https://www.law.cornell.edu/cfr/text/43/3264.10
- 43 CFR Part 3200 table of subparts: https://www.law.cornell.edu/cfr/text/43/part-3200
- 5 USC 552(b)(9): https://www.law.cornell.edu/uscode/text/5/552
- Sibling evidence: D01-texas-rrc.md, D03-great-basin-wells.md (Utah Code 73-22-6, NDOM 938 wells), R03-blm-nomination-dynamics.md, R11-canada-tenure.md, L20-canada-alberta.md in /home/user/nuketime/research/geothermal/evidence/
