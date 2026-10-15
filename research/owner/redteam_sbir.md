# Red team: SBIR lineage acquisition (round 3, deeptech thesis A)

Written 15 Oct 2026. I used 17 of 18 WebSearch calls. sbir.gov, data.www.sbir.gov and huggingface.co
are blocked from this container (proxy 403). Sources are listed at the end.

## Verdict: survives with changes, and only barely. Dead as a Terranox-style claim.

The law holds up and has even widened since the r3 note. Three parts of the original thesis fail:

1. **The "20-year data rights" do not come with dormant lineages.** The 20 years run from the award
   date of each SBIR contract. Awards made under the old regime were protected only until five years
   after the final deliverable. A lineage that went dormant between 2012 and 2018 has largely
   unprotected data.
2. **Phase III is a preference, not a claim.** GAO's G2 Ops decision (Feb 2026) held that an agency
   need not make a Phase III award when it is not buying the SBIR technology. Strategi (Court of
   Federal Claims, 2026) is a jurisdictional ruling only. The asset is an option whose strike is a
   contracting officer's discretion.
3. **Lineage value is already priced, and ML gives less edge each year.** Primes, PE roll-ups and
   advisers say openly that they price "SBIR lineage". Section 8 of the 2026 reauthorization orders
   FPDS and the SBIR database to link every Phase III award to its prior SBIR award IDs. That makes
   lineage value easy for anyone to read.

What survives is the wrapper doctrine. Clear Align (2025) and Bode v. SNA (Nov 2025) show that a
small SBIR-derived component can carry a whole system, commercial off-the-shelf parts included,
sole-source and with no price test. That is a real, rivalrous legal vehicle. But it pays only to
someone who can build and deliver the system.

## 1. Law (verified)

- **Statute.** Under 15 USC 638(r)(4), agencies shall award Phase III to the SBIR firm "to the
  greatest extent practicable". Phase III uses non-SBIR money, so there is no size limit, no dollar
  cap and no time cap (Crowell, May 2026; Precision Federal).
- **Successor in interest.** The SBA Policy Directive amendment effective 1 Oct 2020 says a Phase III
  awardee may "be a successor-in-interest entity" (Ward & Bradel).
  - Novation is not needed if the prior award is complete (Mondaq/Pratt's).
  - No source says staff must transfer. The test is acquiring "all the assets involved in
    performance", or the relevant portion. Bass Berry (2026) restates the same rule.
  - The earlier bar, ASRC Federal B-418028 (2020), applies only where the award was neither novated
    nor succeeded to.
- **Data rights.**
  - The 2019 Directive set a fixed 20 years from award of the specific SBIR contract. DoD wrote it
    into DFARS 252.227-7018 in a final rule (MoFo, Jan 2025).
  - The FAR clause (52.227-20) does not yet have it (Crowell).
  - The old rule protected data until five years after the final deliverable, extended by later
    SBIR awards that derive from the same work. A dormant pre-2019 lineage has mostly lapsed
    protection.
- **GAO B-423319, Digital Force Technologies (19 May 2025).** The protest was denied.
  - Clear Align bought Computer Optics' relevant assets, including IP, in 2013. The Air Force
    reasonably relied on the asset purchase agreement to treat it as successor.
  - Only the infrared camera derived from the Phase II work, and the rest was COTS. GAO found "no
    authority" barring Phase III where only a component derives from SBIR work, provided it is
    reasonably related to the system's objective.
  - The test applies to the work acquired, not to the agency's requirement.
  - The r3 note's figure of "32% of unit cost" does not appear in the Covington summary. I could
    not verify it from the decision text.
- **Later cases.**
  - *Bode Technology*, B-423754 (21 Nov 2025): denied. A Phase III award may include commercial
    items, and there is no statutory price test on their share. **This widens Clear Align.**
  - *G2 Ops*, B-423967 (13 Feb 2026): denied. An agency need not award Phase III when it is not
    pursuing the SBIR technology and the protester shows no specific connection. **This narrows
    the claim: it is not an entitlement.**
  - *Strategi Consulting v. US* (Court of Federal Claims, 2026, docket 26-450): survived a motion
    to dismiss. A firm can challenge an agency that brings SBIR work in-house or gives it to
    incumbents. This is jurisdiction only; the court decided nothing on the merits.
- **Reauthorization.**
  - The program lapsed on 30 Sep 2025. S.3971, the Small Business Innovation and Economic Security
    Act (Pub. L. 119-83), was signed on 13 Apr 2026 and runs to 30 Sep 2031.
  - Phase III sole-source authority is unchanged. Proposals for Phase III competition or dollar
    ceilings and a $75M lifetime cap were dropped.
  - New provisions:
    - Per-firm caps on Phase I and direct-to-Phase II proposals from FY2027, aimed at proposal
      mills.
    - Mandatory contracting-officer training on Phase III sole-source awards and data rights.
    - Standard Phase III eligibility clauses.
    - Phase III linkage in FPDS and the SBIR database (section 8).
    - Expanded foreign-ownership and security screening, which keeps the 2022 change-of-ownership
      clawback.
    - Strategic Breakthrough awards of up to $30M.
  - On balance the act is **mildly positive for Phase III use** and **negative for any data edge**.

## 2. Size

- **Phase III obligations, all agencies (FPDS, per GovSpend):**

  | Fiscal year | Phase III obligations |
  |---|---|
  | FY20 | $2.53B |
  | FY21 | $2.47B |
  | FY22 | $3.05B |
  | FY23 | $3.68B |

  DoD is about 91% of SBIR/STTR spend. Earlier sources add the Navy at $1.2B (FY23) and the Air
  Force at $977M (2021). NASA's Phase III averages only about $56M a year across about 75 awards
  (Payload).
- **Large examples.**
  - Anduril: a $363M one-year Phase III task from DHS for autonomous surveillance towers, and a
    $99M AFWERX "Thunderdome" Phase III IDIQ for Lattice.
  - An unnamed firm built a $489M sole-source IDIQ on a single Phase I (Long Capture).
- **Concentration.** I found no published figure for how many lineages exceed $50M. The top SBIR
  recipients are active, staffed firms: Linquest, Technology Service Corp, Anduril, Progeny and
  Cosmic AES.
- **Read-across.** A $3-4B a year pool flows mostly to the original, active performers. The part
  reachable by buying dormant lineages is unmeasured. It is probably small, because dollars follow
  the program-office relationships that dormant firms lack.

## 3. Prior art and crowding

- **Arlington Capital / BlueHalo.**
  - BlueHalo bought Intelligent Automation Inc. in 2021, citing its "substantial IP portfolio",
    more than 75 PhDs and R&D-to-product record. IAI was an SBIR-heavy shop.
  - AeroVironment then bought BlueHalo for about $4.1B, all stock, closing on 1 Apr 2025.
  - This is the proof that SBIR-lineage roll-ups exit big, and that PE runs them.
- **Mondaq/Pratt's (2025), "The Rise of SBIR Acquisitions".** "The value of SBIR lineage is being
  actively priced into acquisition strategies." Buyers are primes, integrators and corporate
  venture arms, and some buy SBIR awards without the company. Sellers are told to price Phase III
  eligibility and to use earnouts.
- **SBIR Advisors.** It launched a catalog of sole-source-eligible companies on AWS Marketplace in
  June 2025. It works with 180+ startups and claims $500M+ of DoD wins.
- **Lookup tools.** Forward Edge-AI, Long Capture, HigherGov, SAMSearch and an SBIR MCP server are
  Phase III advisory and lookup tools. None owns lineages.
- **hollomancer/sbir-analytics (GitHub, active 2026).**
  - A personal research project. It has a "Phase III census" that pairs Phase II awards with
    federal contracts by exact UEI: 72,996 prior awards and 8,938 firms in the February 2026 cut.
  - It also has exploratory "M&A discovery" and "transition scoring". It is non-commercial but
    already does much of the proposed ML step.
- **Gap.** I found nobody running a public data-driven hunt for dormant lineages to buy, so the gap
  remains. The concept is well known, though: dealmakers price lineages through relationships, and
  the data needed to find them is getting easier to read.

## 4. Practical

- **Price of dormant shells.** No source found. The r3 figure of $1-10M is unsourced. A dead firm's
  IP and assets may sit with the founder, a bank (UCC liens) or a bankruptcy estate. Buying assets
  from these holders is cheap but slow, one deal at a time.
- **A successor with no staff.** The legal test is about assets, not people. In practice, though,
  a contracting officer must find the firm responsible and the work credible. A shell with no team
  can win only if a builder or prime stands behind it. Phase III has no limit on subcontracting,
  and the SBIR firm can be a small sub to a prime: Forward Edge-AI says a 5-20% share is accepted.
- **"Derives from, extends or completes".** Agencies are given reasonableness deference.
  - The Air Force in Clear Align and ICE in Bode were upheld on thin component links.
  - Where the agency does not want the technology, the protester loses (G2 Ops).
  - The binding constraint is therefore the will of the program office, not legal strictness.
- **Security screening.** Under the 2026 act, foreign-tied acquirers face new risk. Ownership
  changes can trigger the clawback.

## 5. Data

- **Source file.** The full SBIR award file with abstracts is
  `https://data.www.sbir.gov/mod_awarddatapublic/award_data.csv`. It is about 395 MB (394,636,989
  bytes in the 2026-09-21 version pinned by hollomancer), with 42 columns and about 219,500 rows.
  It is **blocked here (proxy 403)** and larger than the 300 MB cap, so I downloaded nothing.
- **No full mirror on GitHub.** A code search for `award_data.csv` finds only unrelated files.
  Partial or sample files exist:
  - `hollomancer/sbir-analytics`: `tests/fixtures/sbir_sample.csv` and
    `examples/army_science_technology_awards.csv`.
  - `namansingh27/nj-venture-radar`: `data/sbir_nj.csv`.
- **PyPI.** `sbirtools` (GitHub gerwaric/sbirtools) only downloads from sbir.gov and is not on
  PyPI.
- **Reachability.** raw.githubusercontent.com works. huggingface.co and sbir.gov do not.
- **Practical route.** Run `hollomancer/sbir-analytics` at tag v0.18.0 from a laptop. It fetches
  the hashed sources, including USAspending, and already builds the Phase II to contract pairs
  needed for the backtest.

## Strongest reframing

**"Phase III wrapper" acquirer inside an operating defence hardware company. It is not a lineage
claim-stake.**

1. Use ML on the SBIR file and the new FPDS Phase III links to find live programmes where a small,
   cheap, *post-2019* lineage (data rights still running) could serve as the SBIR-derived component
   of a larger system. This is the Clear Align and Bode doctrine.
2. Buy that lineage's assets.
3. Bid the whole system sole-source as prime, or rent the vehicle to a builder for a share of the
   work.

The ceiling is the operating company's value, as with BlueHalo's exit at about $4.1B, not the
value of the lineage. The ML edge is in deal sourcing for M&A only, and it decays as section 8
linkage makes the data legible.

**Kill test.** Use the hollomancer census cut. If a dormancy-and-similarity model does not beat an
agency x topic baseline by at least 0.05 AUC at predicting more than $10M of follow-on work, and
fewer than about 20 post-2019 lineages sit in inactive firms with a programme match, drop it.

## Sources
- Bidwell, S.3971 and Phase III: https://bidwellnow.com/sbir-reauthorization-2026
- SBIR.org, S.3971 changes: https://sbir.org/news/s-3971-sbir-sttr-changes
- Bass Berry: https://www.bassberrygovcontrade.com/sbir-sttr-reauthorization/
- Crowell, SBIR 101 (May 2026): https://www.crowell.com/en/insights/client-alerts/small-business-innovation-research-sbir-101-following-re-authorization-what-contractors-and-their-investors-need-to-know
- Covington, Digital Force: https://www.insidegovernmentcontracts.com/2025/06/digital-force-technologies-inc-a-sbir-derived-component-can-be-sufficient-for-sbir-phase-iii/
- GAO B-423319: https://www.gao.gov/products/b-423319
- GAO B-423754 (Bode): https://www.gao.gov/products/b-423754,b-423754.2
- GAO B-423967 (G2 Ops): https://www.gao.gov/products/b-423967
- Strategi v. US (Court of Federal Claims): https://www.fedcontractpros.com/blog/can-an-agency-take-sbir-technology-in-house-instead-of-awarding-phase-iii-strategi-opens-the-door-to-review
- Ward & Bradel, successor in interest: https://www.wardbradel.com/sba-amends-sbir-sttr-policy-directive-clarifying-broad-phase-iii-eligibility-for-the-successors-in-interest-of-phase-ii-recipients/
- MoFo, DFARS data rights: https://www.mofo.com/resources/insights/250124-dod-updates-data-rights-regulations-for-sbir-sttr-programs
- GovSpend, Phase III FPDS totals: https://govspend.com/blog/understanding-sbirs-sttrs-federal-contract-spend/
- Payload, NASA Phase III: https://payloadspace.com/inside-nasas-sbir-phase-iii-program-by-the-numbers-payload-research/
- Anduril $363M DHS Phase III: https://orangeslices.ai/anduril-scores-1-year-363m-sbir-phase-iii-autonomous-surveillance-towers-idiq-task-with-dhs-border-patrol/
- Long Capture ($489M IDIQ): https://www.longcapture.com/blog/phase-iii-sbir-one-of-the-most-powerful-and-underused-paths-to-scaling-dow-revenue
- Mondaq, Rise of SBIR acquisitions: https://www.mondaq.com/unitedstates/contracts-and-commercial-law/1661956/the-rise-of-sbir-acquisitions-a-strategic-pathway-for-growth-and-exit
- BlueHalo/IAI: https://www.businesswire.com/news/home/20210819005287/en/
- AeroVironment/BlueHalo: https://www.privsource.com/acquisitions/deal/X0SZER
- SBIR Advisors catalog: https://www.afcea.org/signal-media/technology/new-sbir-phase-iii-catalog-advances-procurement-process
- Forward Edge-AI partnering: https://support.forwardedge.ai/en/articles/8895732-sbir-phase-iii-partnering-requirements
- GAO-26-107828 (cites Pub. L. 119-83): https://www.gao.gov/assets/890/885925.pdf
- hollomancer/sbir-analytics: https://github.com/hollomancer/sbir-analytics
