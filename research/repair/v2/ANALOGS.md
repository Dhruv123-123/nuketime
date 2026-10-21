# Analog lessons: how verification was automated or privatised elsewhere, and what that means for a hardware verification company

Method note: sources are the research items cited in brackets. Figures marked (recalled) were not freshly verified by the agent that reported them. Several analog agents (a03-a10) had no web search quota, so their figures need checking before they go into a YC application.

---

## 1. Vanta and Drata: SOC 2 compliance automation [a01, c31, a07]

**What was automated.** The applicant's preparation. API connectors pull evidence from cloud, HR and identity systems. Controls are monitored continuously, and a trust center shows the result. The audit itself was not automated: a licensed CPA still signs. AI-native entrants such as Delve now draft the evidence and the narrative. Fieldguide does the same work on the auditor side and claims about 55% fewer engagement hours [a07].

**How acceptance was won.** No regulator had to agree, because SOC 2 is an AICPA attestation. Vanta gave auditors a read-only portal and sent them deal flow. More than 100 audit firms joined, and about 26,000 audits have run through the platform [c31]. The auditor's hours fell and their volume rose, so the auditor became Vanta's sales channel.

**How long.** About 6-7 years from founding to roughly $300M ARR (founding date recalled).

**Who captured the value.**
- Vanta: about $300M ARR, $4.15B valuation, $500M+ raised, about 16,000 customers [a01].
- Drata: about $98M ARR at a $2B valuation (recalled) [c31].
- Auditors kept the signature and their fees. Audit fees did not collapse even where AI cut hours; the firms kept the savings as margin [a07].
- Price pressure produced cheap "SOC 2 report mills", and the credential's reputation suffered [a07].

**Business model and margins.** SaaS at about $19k per customer [a01]. Margins are software-like. A bundled variant (Thoropass) includes the audit itself.

**What carries over to hardware.**
- The FAA DER system is structurally close to the CPA model: a private, delegated signer paid by the applicant. DLA's government engineering support activity (ESA) is not [a01].
- Hardware has no network of verifiers like Vanta's auditor network [c31].
- Physical evidence cannot be pulled through an API. It has to be signed at the instrument.
- A hardware approval is worth $100k or more, but there are far fewer of them than SOC 2 audits. That favours owning approvals over selling seats [a01].

## 2. UL: a private lab becomes the electrical-safety gate [a02, d08]

**What was automated.** Nothing in the AI sense. UL industrialised testing against standards it wrote itself, and it repeatedly checked factories that make certified products.

**How acceptance was won.**
1. In 1894 the party carrying the risk paid for it: fire insurers.
2. UL wrote the standards. They went into model codes such as the National Electrical Code, states adopted those codes into law, and local inspectors enforced them.
3. The UL Mark saved inspectors work.

UL lost its named OSHA status in 1988, after which 21 labs became Nationally Recognized Testing Laboratories. Its dominance did not suffer, because its brand, installed base and ownership of the standards were what mattered [a02].

**How long.** Several decades to become the de facto gate, and 130 years to reach today's scale. UL ran as a nonprofit for 118 years, and the nonprofit still holds 94.1% of the votes after the IPO [a02].

**Who captured the value.** UL Solutions: $3.05B revenue and 25.9% adjusted EBITDA in FY2025, IPO in 2024 at about $7B [d08].
- About a third of revenue comes from keeping products certified, not from first certification [d08].
- The Industrial segment, where the mark is code-mandated, earns 34.9% against 18.9% for Consumer [d08]. (a02 recalled 29% against 9%. The d08 filing figures should take precedence.)
- UL's 10-K names AI that replicates its services, and any rule forcing it to accept third-party test data, as threats [a02].

**Business model.** Fees for testing and certification, plus a recurring annuity from follow-up factory inspections. Mark labels are themselves "material" to the business [a02].

## 3. EDA sign-off in chip design: Synopsys, Cadence, Mentor/Siemens [a04]

**What was automated.** Nearly all verification: design-rule checking, equivalence checking, timing and power sign-off, and formal verification. This was possible because the specification is digital and executable.

**How acceptance was won.**
- Escaped errors are very expensive: a mask set costs $10M or more, plus respins, and the FDIV recall cost about $475M (recalled).
- The gatekeeper is the foundry. It certifies specific tools as "golden sign-off" and ships a process design kit (PDK) for them. Permission flows through the tool rather than through a person's signature [a04].

**How long.** Roughly 15-20 years from academic formal methods to tool sign-off as the standard (recalled).

**Who captured the value.** A software oligopoly: Synopsys at about $6B+ revenue (recalled), Cadence and Siemens.
- These vendors are now buying physical simulation: Synopsys bought Ansys for about $35B, Siemens bought Altair for about $10.6B, and Cadence bought BETA CAE (all recalled) [a04, c14].
- None of them sells regulator-accepted sign-off for physical parts [a04].

**Business model.** High-margin term licences, priced per seat and per run (margin recalled).

**What carries over to hardware.**
- Physical parts have no executable specification. The certification basis is written in prose [g01, c06].
- No regulator certifies a tool. The FAA and DLA delegate to people (DERs, ODA unit members, ESA engineers) [a04].
- The nearest equivalents of a PDK are shared materials databases: MMPDS, CMH-17 and NCAMP.

## 4. Euro NCAP and UNECE virtual crash testing [a03]

**What was automated.** Crash simulation, in stages:
- 1986: first full-car simulation.
- 2010: EU Regulation 371/2010 allows virtual testing, but only for simple geometric acts.
- About 2013: Euro NCAP accepts OEM predictions for pedestrian tests.
- 2023-2026: human-body-model and occupant-diversity virtual assessments.
- 2026: the regulatory full-scale crash test is still physical.

Simulation got in by covering cases nobody tests physically (more occupant sizes, grid points and load cases), with one physical test kept as the anchor.

**How acceptance was won.** Not by proving the models correct. The applicant predicts every result, the assessor physically tests a sample it chooses, and wrong predictions are penalised with a correction factor. Euro NCAP made dishonest predictions costly rather than trusting OEM models.
- The EU expands virtual testing one act at a time from a positive list, starting with low-consequence acts.
- The voluntary rating body, Euro NCAP, moved about 10 years before the law did.
- Free, shared reference models made it scale (Toyota's THUMS human body model became free in 2021) [a03].

**How long.** 24 to 40 years.

**Who captured the value.**
- OEMs, through avoided prototype cost.
- Solver vendors, who were absorbed into larger groups: ESI went to Keysight for about EUR 900M, Altair to Siemens, and LS-DYNA (via Ansys) to Synopsys (recalled).
- Technical services firms (IDIADA, TUV, DEKRA), which kept the witness role [a03].

**Business model.** Tool licences plus services from accredited technical-service firms. No dedicated "credibility vendor" exists even in automotive [a03].

## 5. FDA in-silico evidence: ASME V&V 40, credibility guidance, MDDT, PBPK [a05, c34, c13, c14]

**What was automated.** Credibility of simulation evidence, scaled by risk.
- ASME V&V 40 (2018) sets how much credibility a model needs by weighing how much the decision relies on it against the harm of a wrong decision. FDA's 2023 credibility guidance builds on it.
- FDA's Medical Device Development Tools (MDDT) programme lets a model be qualified once and cited by any sponsor.
- Simcyp physiology-based drug modelling (PBPK) supported about 120 FDA-approved drugs in place of clinical studies and is licensed by 11 regulators [c34].
- Unlearn's PROCOVA was EMA-qualified in September 2022. Its statistical validity holds even if the AI is wrong [c34].

**How acceptance was won.**
- Every outright case of simulation replacing a test involved the regulator co-developing or qualifying the model: the UVA/Padova diabetes simulator, VICTRE, the Virtual Population models [a05].
- Wins came first on ancillary studies, not pivotal trials [c34].
- FDA's 2023 guidance excludes ML and AI models, so there is a regulatory vacuum for AI surrogates [c14].

**How long.** PBPK took about 15-20 years from the early 2000s to routine waivers. V&V 40 took 5 years from standard (2018) to guidance (2023).

**Who captured the value.**
- Sponsors, through avoided trials.
- The tool monopolist earns modestly: Certara has about $419M revenue and a ~$1.49B market cap [c34].
- Exponent-style consultancies assemble credibility dossiers by hand, at about $500M revenue (recalled) [a05].
- Very few computational MDDTs exist, so the qualify-once model is barely used [a05].

**Related evidence: medtech submission-drafting AI [c13].**
- Drafting is commoditised: 510(k) builds start at about $11k.
- A former FDA reviewer calls the output a "C-minus 510(k)".
- The 2025 median clearance time is still about 142 days, so drafting AI shows no review-time compression.
- What did move FDA's clock was procedure: structured submissions (eSTAR), delegated third-party review (3P510k) and pre-approved change protocols (PCCP).

## 6. Hatch-Waxman, bioequivalence (BE) CROs and first filers [a09, f08]

**What was automated or standardised.** Proof of sameness became one cheap number: the 90% confidence interval of AUC and Cmax must fall within 80-125% of the reference drug. Generics no longer had to show efficacy again. Model-based ("virtual") bioequivalence later replaced some studies.

**How acceptance was won.** By statute in 1984. The deal had three parts: a fixed evidence standard, 180-day exclusivity for the first filer, and patent-term restoration plus a 30-month stay as a concession to incumbents [a09, f08].

**How long.** The law passed in one negotiation. The industry took about 10-15 years to form (recalled).

**Who captured the value** (all recalled):
- Payers and patients captured most of it: prices fall more than 95% once six or more entrants arrive.
- First filers captured the scarce 180-day exclusivity slot. Most of a generic's lifetime profit can come from those 180 days.
- BE CROs captured the least: about $50-150M revenue each, commoditised and prone to fraud (Cetero, Semler, Synchron, Ranbaxy). Regulators mostly caught the fraud after approval [a09].
- The fixed test can still miss real differences: FDA reversed its own equivalence finding for Budeprion XL 300 in 2012 [a09].

**What carries over.** 10 USC 3243 already has much of the ANDA skeleton: stated reasons for rejection, reimbursed test costs and revalidation. It lacks an evidence standard, a review deadline and a safe harbor [f08]. The 2017 Competitive Generic Therapy designation is a direct template for exclusivity on orphaned products [a09].

## 7. Carfax and the credit bureaus [a08, s10, c09]

**What was automated.** Assembling fragmented records into a history for each identifier (VIN or person), then scoring it.

**How acceptance was won.**
- Seeding from public records.
- Give-to-get: contributors handed over data for free in exchange for marketing value or relief from a chore. The Work Number is the model.
- Charging the party that verifies, per report, at the moment of a decision.
- Law came after adoption and then locked in the incumbents (FCRA, and NMVTIS for vehicles) [a08].

**How long.** Decades. The bureaus took shape in the mid-20th century and Carfax in the 1980s (recalled).

**Who captured the value.** The score more than the data. FICO runs about 46% operating margin (recalled), above the bureaus that hold the data [a08].

**Aviation contrast.**
- Blockchain provenance pilots (SkyThread, Aerotrax, GoDirect, Moog) stalled. Contributors had no reason to join, and a ledger does not show that the first entry was true [c09, f09].
- In the AOG Technics fraud (60,000+ parts on altered certificates), the OEM's serial registry already held the authoritative data. Nobody queried it at purchase. The fraud was caught by one technician's eye, not by any system [a08, s10].
- Disclosed venture funding across aviation records and provenance adds up to under $10M [c09].

## 8. Financial audit and rating agencies [a07]

**What was automated.** Labour, not the signature. Firms moved from sample testing to testing 100% of the population with AI, and evidence matching was automated (DataSnipper, Fieldguide).

**How acceptance was won.**
- The signature is legally designated: PCAOB-registered audit firms, and rating agencies recognised by the SEC as NRSROs.
- The PCAOB came to accept technology-assisted analysis through use alongside human work over time.
- The designated verifiers have defeated regulators. Rating agencies blocked Dodd-Frank's liability provision by refusing to consent to being named, which froze the asset-backed securities market [a07].

**How long.** Audit has existed for about a century. The AI layer arrived from about 2015.

**Who captured the value.**
- The Big Four: $219B revenue in FY2025, of which $66.5B is assurance. They hold about 99% of large-cap audits, even though about 31% of inspected audits are deficient and only about 6.6% are punished.
- Moody's: $5.9B revenue in 2023, with margins around 60% (recalled).
- Rating moved to issuer-pays after the photocopier made copying cheap, which created the independence conflict.
- Kroll became a new NRSRO after 2010 by entering a slow niche.
- Fieldguide and DataSnipper are real businesses but thin slices next to the signer [a07].

## 9. Building-permit AI and performance-based fire engineering [c32, a06, f12]

**What was automated.** Checks against prescriptive code: Archistar in 25+ governments, CodeComply, CivCheck, UpCodes, and Singapore's CORENET X model checker. All are advisory. No regulator accepts AI as the legal approver [c32].

**How acceptance was won.** The real speed-ups came from law, not AI:
- Private-provider statutes such as Florida 553.791 let a licensed private reviewer replace the backlogged agency queue. Review fell from 6+ months to about 10 days, and from 90-120 days to 21-45 days.
- GreenLite holds the licensed stamp and runs AI internally. It averages 0.5 resubmission cycles [c32, f12].
- CivCheck pioneered "free to the city, applicant pays a prescreen fee" and was acquired by Clariti [c31].

**How long.**
- Singapore has worked on automated code checking since the early 2000s, and its checker is still pre-check only. The win there came from redesigning the process.
- LA's rollout ran under emergency orders with philanthropic funding [c32].

**Who captured the value.** The firms that hold a permission or the applicant relationship: GreenLite ($49.5M Series B) and PermitFlow ($54M). Pure code-checkers did not [c32].

**Performance-based fire engineering [a06].**
- Codes already allow alternatives to their prescriptive rules (IBC 104.11, NFPA 101 Ch. 5).
- The money goes to fire engineers on both the design and peer-review side, scarce furnace labs, and ICC-ES, which writes acceptance criteria.
- There is no precedent system: an identical alternative is reviewed again from scratch in each of about 20,000 US jurisdictions.
- The peer review is paid by the applicant.

## 10. Other short analogs from the research

**NCAMP and AGATE (composites).** Pooled, FAA- and EASA-accepted material databases plus small equivalency subsets. Claimed 10x lower cost and 4x faster certification. This 10x came from statistics and data sharing, not robots, and nobody has applied it to reverse-engineered metal parts [a10, f03, s06, f11].

**Class societies (DNV, ABS, LR).** Remote surveys became permanent where the verifier is a private competitor that saves money by doing them. At the FAA and NRC remote review survived only as a contingency mode. Class-society AI is still only rule search [f14, c20].

**Nuclear NDE.**
- Qualified software already acts as one of two steam-generator eddy-current analysts, accepted through performance demonstration.
- ENIQ RP13 (2021) explicitly allows simulated and augmented data for ML qualification.
- Aviation has nothing equivalent [c10, f02].

**Insurer-built verifiers.**
- HSB (1866) inspected and then insured [d06, g10].
- CAPA, founded by insurers in 1987, certifies aftermarket auto parts. NSF quit auto-part certification in 2019 because the margins were thin [c25].

**Margin ladder.** Where a firm sits relative to the signature sets its margin:

| Position | Example | Margin | Valuation |
|---|---|---|---|
| Certified labour | Mistras | 12.6% adj. EBITDA | sold at about 9.5x ($866M EV) |
| Owns the approvals | HEICO Flight Support Group | 24.1% operating | — |
| Owns a code-mandated mark | UL Industrial | 34.9% adj. EBITDA | — |
| Scarce qualification capacity | Element | — | about $7B, roughly 25-30x EBITDA (rough) |

Sources [d08, d07].

**Norm Ai.** The best-funded AI compliance company ($1.2B) chose to become a law firm so it would own the sign-off [c31].

---

## Summary table

| Analog | What got automated | How acceptance was won | Time | Who captured value |
|---|---|---|---|---|
| Vanta | Applicant evidence | Signer on the platform; no rule change | ~6-7 yrs | Platform; signer keeps fees |
| UL | Testing against own standards; surveillance | Risk-bearer paid; standards into codes, then law | Decades | Mark owner, ~26-35% EBITDA, 33% annuity |
| EDA sign-off | Nearly all verification | Gatekeeper certifies the tool | ~15-20 yrs | Tool oligopoly |
| Euro NCAP | Prediction plus spot checks | Correction-factor penalty; positive list; voluntary body first | 24-40 yrs | OEMs, solver vendors, technical services |
| FDA in-silico | Ancillary studies; qualify once | Regulator co-builds or qualifies the model; risk-tiered | 5-20 yrs | Sponsors; tool vendor modest (~$1.5B cap) |
| Hatch-Waxman | Equivalence as one number | Statute plus incumbent bargain | 1 law, ~10-15 yr industry | Payers, first filers; CROs least |
| Carfax / bureaus | Record assembly plus score | Public records, give-to-get, law later | Decades | The score (FICO) |
| Audit / ratings | Labour, not signature | Designated signer | — | Signer (99% share; ~60% margins) |
| Permit AI | Prescriptive pre-check | Private-provider law | 20+ yrs (Singapore) | Permission holders (GreenLite) |

---

## Rules for building a verification company in hardware

1. **Own the signature, or sell to the person who holds it, and never be the testing lab.** Across every analog the margin sits with the regulator-recognised signer: the Big Four, rating agencies, UL's mark, GreenLite's stamp, Norm Law, and HEICO's delegated authority. Bioequivalence CROs, certified-labour firms like Mistras and tool vendors next to the signer earn thin, commoditised margins [a07, a09, d08, c32, c31]. In hardware that means DERs, an ODA, a NUPIC-audited dedicating entity, or an accredited ISO 17025/17065 or ISO 17020 body [g01, g05, c29]. Where the law forbids delegation, as with ESA approval of DoD critical safety items [g04], work as the reviewer's contracted evaluator and keep a firewall from the applicant business [s08].

2. **Never ask the regulator to trust the AI; make the result valid whether or not the AI is right.**
   - Euro NCAP penalises wrong predictions found in random spot checks [a03].
   - PROCOVA keeps its statistical guarantee even when the model is wrong [c34].
   - Chip sign-off relies on a deterministic checker [a04].
   - Nuclear NDE uses frozen-model performance demonstration [f02].

   For hardware: the AI generates, a deterministic qualified checker recomputes every claim, and only the checker needs DO-330-style qualification [c06, c21]. F4 Industries markets "no AI" to its buyers for a reason [c01].

3. **Get a method accepted once per part class, start with the lowest-consequence class, and expand class by class.** The EU's list of acts eligible for virtual testing, MDDT, NCAMP equivalency and Simcyp all followed this pattern. Simcyp won ancillary studies, not pivotal trials [a03, a05, c34, a10]. The hardware path:
   - Start with parts that are not critical safety items, on a legacy platform, with one ESA that has discretion.
   - Go after "ancillary" evidence first: equivalency coupons, fungus and salt-fog waivers, similarity extensions [s06, f16].
   - Expect 5-10 years per class if no rule change is needed, and 15-40 years where one is [a03, a05].

4. **Reviewer hours are the currency. Put the reviewer on your platform and pay for it on the applicant side.**
   - Vanta's auditor portal [a01].
   - CivCheck: free to the city, applicant pays [c31].
   - Simcyp licensed by 11 regulators [c34].
   - The UL Mark saving inspectors work [a02].

   DLA, the FAA and ESAs publish no queue data, about half of decided Land and Maritime SARs were rejected, and the stated rejection reason "can't validate part (no government data to compare)" is an information gap [g03, s08]. Supply the government's reference data and the reviewer-format evidence, and measure reviewer hours per approval and review cycles per approval [f12]. Drafting-only AI commoditises: 510(k) builds sell for about $11k at "C-minus" quality with no review-time gain [c13].

5. **Find the party that bears the risk and make it the payer, or the co-signer.**
   - UL was born from fire insurers, HSB from boiler insurers, CAPA from auto insurers [a02, d06, c25].
   - In aviation the hidden co-signers are lessors and underwriters. An FAA approval gives no tort immunity, and 2025-26 leases still ban PMA and DER content [s12, d02].
   - On the DLA side there is no insurer. The payer is readiness: DLA guarantees a new source 40% of the award for a year, and sole-source lead times run up to 1,261 days [g03].

   An evidence-priced warranty or MGA turns "no" into a priced "yes" [d06, s12].

6. **The data moat comes from running the work, not from collecting data in a database.**
   - Carfax used give-to-get, NCAMP pooled databases, Simcyp built population libraries [a08, a10, c34].
   - Every package an Approval Factory files produces the corpus nobody else has: reviewer questions and rejection reasons [f12], a record of predictions made before each physical test and the results [f01, f06], paired non-destructive and destructive material results [s04, f05], and field reliability per approval holder [s11].
   - CM4QC, the FAA/NASA computational-materials roadmap, names this side-by-side corpus as the missing input for granting test credit [f01].
   - The calibrated score earns more than the database (FICO ~46%, recalled) [a08].

7. **Use voluntary or private gates first; law follows adoption.**
   - Euro NCAP accepted simulation about 10 years before EU law [a03].
   - SOC 2 needed no rule change [a01].
   - Class societies made remote surveys permanent [f14].
   - FCRA and NMVTIS came after adoption [a08].
   - Private-provider permit statutes already existed [c32].

   In hardware the existing levers are 14 CFR 21.303 "computations" and 25.613(f) [s05, c07], MIL-PRF-38535's test-deletion rights [g09], the DLAD 9.3 first-article-test waiver [s07], Appendix B Criterion III design verification by analysis [d04], and space programmes where the customer, not a regulator, decides acceptance [c28]. Lobby for the "ANDA for parts" amendment to 10 USC 3243 only once there is a track record [f08].

8. **Sell staying valid, not only getting approved, and make evidence reproducible to protect independence and catch fraud.**
   - About a third of UL's revenue is surveillance [d08].
   - Cheap verification without reproducibility invites backlash and fraud: SOC 2 report mills, the bioequivalence CRO frauds, AOG Technics [a07, a09, s10].
   - Practical steps: sign evidence at the instrument, link every claim to raw data that can be re-run [f09, f14], and monitor approved parts continuously after approval [s11].
   - Keep verifier governance separate from part manufacture, as UL did by splitting into three entities in 2022, or make the evidence checkable by any third party [a02].

**Implication for the YC pitch.** In every analog the winner either became the signer or put the signer on its platform. An Approval Factory that holds its own approvals and submits machine-checkable packages ESAs can review quickly has the UL/HEICO economics. A standalone "AI DER copilot" has Fieldguide or bioequivalence-CRO economics unless it captures the signature or the risk-bearer.