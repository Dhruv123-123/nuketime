# End-to-End Verification Pathway Gap Map: alternate-source approval for orphaned and sole-source parts

**How to read this.** "Clock type" is one of four things: **Physics** (a test that must physically run), **Queue** (waiting for scarce capacity, such as reviewers or lab slots), **Legal** (permission, data rights or statute) or **Labour** (engineering hours). Bracketed ids point to the research notes. Figures marked (recalled) were not verified in the source notes.

**Who is already doing this.** Across 87 research threads, no funded company owns the whole loop: AI reverse engineering, then the technical data package (TDP), then winning a DLA Source Approval Request (SAR) or an FAA PMA, then holding the approval [c01, c22, c30, c31]. AI money goes to two places. The first is new-design verification and validation (V&V): Nominal at $1B, Flow at $750M, PhysicsX at $2.4B [c05, c06, c30]. The second is geometry capture: Backflip, Lumafield, Novineer [c03, s03]. The only reviewer-side award for source approval was a $110k Phase I to ELEVAN/UTSA in 2024, with no Phase II [c02, g03]. The incumbents (HEICO, AAR, TransDigm, Chromalloy) disclose no AI in approval engineering. HEICO names FAA review throughput as its bottleneck, and its Flight Support Group R&D rose from $26.4M to $43.7M while PMA output stayed flat [c17]. The verifier's seat is empty in every regime surveyed.

---

## 1. The pathway, step by step

### Step 0: Picking targets and checking demand
- **Time and cost.** Days to weeks per candidate. The real cost is wasted downstream work: fewer than 10% of 1,650 DLA reverse-engineering projects in FY15-18 finished, and some failed because demand disappeared before approval [s01]. Only 7% of RPPOB bailment requests became SARs [g03].
- **Who does it.** Contractors working from DLA candidate lists, DLA competition advocates, and PMA houses working with airline partners [s01, c17].
- **What is manual.** Everything. DLA's screen is only ">$10k bought in each of the last 2 years" [s01].
- **Undone or broken.** Nobody ranks the universe of parts by price, readiness impact, remaining platform life, approval probability, part family and buy timing [s01, c02, g04, d01]. AMSC codes have not been re-screened under the cheaper cost of AI-built packages, even though a code challenge must get a status reply within 60 days [g03]. No public data weights spend by AMSC code; in FY25, about $3.4B of DLA aviation awards (60-68% of dollars) were non-competed [d01].
- **Clock type.** Labour and data. No physics.

### Step 1: Data rights and IP clearance
- **Time and cost.** Weeks to months. Attorney hours are billed hourly [s02].
- **Who does it.** DLA reads legends by hand, plus government-contracts law firms and in-house IP staff at PMA houses [s02, c27].
- **What is manual.** Rights are judged one legend at a time. DLA checks for patent markings on the part, and DLA Troop Support does no patent check at all [s02].
- **Undone or broken.** Nobody rebuilds funding history. Government purpose rights (GPR) on mixed-funding data convert to unlimited rights after 5 years, and data delivered without markings is presumed unlimited, yet no one sweeps for either [s02]. DFARS 252.227-7037 challenges to restrictive markings are almost never filed. DoD built an AI tool to scrape data rights and then cancelled it for lack of funds [d01]. Freedom-to-operate (FTO) checks run on patent text only, never on scanned geometry [c27]. Only about 15% of NSNs are fully open (code 1G) [s01].
- **Clock type.** Legal and labour.

### Step 2: Getting a sample and permission to start
- **Time and cost.** About 30 days just to get specs (Rotair) [g04]. Bailment loans are slow, and only about 200 items are available through RPPOB [c18].
- **Who does it.** DLA RPPOB and the service engineering activity [c02, g04].
- **What is manual.** Requests and loans.
- **Undone or broken.** Many Category IV (reverse-engineered) SARs need the service's concurrence *before* a sample can be bought, a permission gate ahead of any engineering [c02, g04]. Source-controlled items (AMC B) and items under $10k/yr are excluded, and these are often the most locked-in parts [g04]. Golden samples are scarce: 1 to 3 units are typical, and destructive testing uses them up [s04, c23].
- **Clock type.** Legal and queue.

### Step 3: Certification basis, criticality and the requirement set
- **Time and cost.** Weeks of DER or engineer time per package. The FAA cites this as a leading cause of delay [g01].
- **Who does it.** DERs, engineers at PMA houses and DLA engineering support activities (ESAs).
- **What is manual.** Reading TCDS amendment levels, ADs, special conditions, ICA, MIL-HDBK-516 and the SAR guides as PDFs [g01, c06, f07].
- **Undone or broken.** No machine-readable, versioned regulation graph exists. Criticality calls (CSI, failure condition) are judgement calls that set the scope of everything downstream, and disputes cause rework [g01, c06]. FAA failure-condition classifications are not public, which blocks China (CAAC) eligibility [g12]. Navy Level I and SUBSAFE boundaries are not machine-readable and tend to be drawn too wide [g08].
- **Clock type.** Labour.

### Step 4: Geometry capture and drawing reconstruction
- **Time and cost.** Capture takes hours to days. Mesh-to-CAD is becoming minutes (Backflip, about $20/month). The tolerance and GD&T work is still weeks [c03, s03].
- **Who does it.** Metrology bureaus, depot cells (REACT, REARM), NIAR and PMA houses [s03, c18].
- **What is manual.** Inferring tolerances and GD&T from one or two worn samples, and drafting to Y14.5 / MIL-STD-31000 [c03, s03].
- **Undone or broken.** No tool infers tolerances statistically from many samples while separating wear from manufacturing variation. No per-feature uncertainty budget exists. No public benchmark exists for AI mesh-to-CAD on aerospace parts [c03, s03]. Phone-photo-to-CAD reaches about 0.7 mm, more than 5x coarser than aerospace tolerances [c01, c02]. **This step covers only about 5-15% of package hours** [c03].
- **Clock type.** Labour. Physics is not binding.

### Step 5: Material and process identification
- **Time and cost.** About 2-6 weeks and 40-100 hours of a metallurgist's time [s04].
- **Who does it.** Contract labs such as Element, IMR and Lambda.
- **What is manual.** Each instrument (XRF, LIBS, eddy current, hardness, XRD) is read separately and fused by a metallurgist [s04, f05].
- **Undone or broken.** No calibrated multimodal NDE classifier that names the spec, temper and process. No paired NDE-to-destructive ground-truth dataset. No plan that minimises how much of the part gets destroyed [s04, f05]. Some steps leave no detectable signature (hydrogen bake, peen intensity) and need conservative bounding envelopes [s04]. ICME cannot yet infer the original process route (inverse ICME) [f06]. AMS 2658 accepts non-destructive temper verification for aluminium only [f05]. Process recovery is the weakest step and causes failed fatigue tests [g01].
- **Clock type.** Labour, plus the scarcity of samples.

### Step 6: Substantiation and equivalence argument
- **Time and cost.** Takes the largest share of the roughly $100k and 300-1,000 hours per package [c05, c14].
- **Who does it.** DERs and stress engineers using FEA, NASGRO and AFGROW [s05].
- **What is manual.** Engineers analyse a few hand-picked load cases. OEM loads are unknown [s05, g02].
- **Undone or broken.** No tool produces a machine-checkable equivalence case with quantified margins; [c06] calls this the biggest gap. Nobody bounds the full envelope of plausible loads to remove the need for OEM loads [s05]. No accepted Bayesian or model-informed method exists for equivalence or allowables [c07, f03]. The law already permits analysis: 21.303 "computations", AC 25.571 "analysis supported by test", and 25.613(f) alternative design values [s05, c07].
- **Clock type.** Labour, plus regulator acceptance.

### Step 7: Test plan and pre-agreement with the reviewer
- **Time and cost.** Months of agreement loops [s06].
- **Who does it.** DERs and ESAs.
- **What is manual.** Specimen counts are set by handbook, not by how much evidence is needed. Precedent lives in individual DERs' heads [s06].
- **Undone or broken.** No planner computes the minimum test matrix. No structured concurrence step exists on the defence side, comparable to the FDA's Q-Sub or the pharma paired meeting [c13, c34, f12]. Waivers that are argued once, such as fungus test by material inertness, get re-argued every time [s06].
- **Clock type.** Queue and labour.

### Step 8: Physical qualification testing
- **Time and cost.** The irreducible physics for a fatigue-critical metal part is about **4-8 weeks when fully parallelised** (1-2 weeks for non-critical parts), yet programmes take 6-18+ months. **75-95% of that is queue**: material lead times of 40-80 weeks, specimen machining, lab slots, witnessing and re-test loops [s06]. In the one dated SAR case, testing was about 14 weeks of a roughly 2.5-year journey [g03].
- **Who does it.** Element/NTS, LTI, Westmoreland, SwRI and NIAR [s06, f11].
- **What is manual.** Running frames serially, writing reports.
- **Undone or broken.** No lights-out test lab serves many parts and many specs [f11]. No shelf stock of pre-characterised legacy heats exists [s06]. Ultrasonic fatigue is accepted only case by case [f16]. Tests that compare the OEM part and the copy side by side, which cancel errors in the acceleration model, are not standardised [f16]. One failure restarts the whole cycle, and no cheap pre-screen exists [s06].
- **Genuinely incompressible clocks.** Creep beyond 10^5 hours, low-dose-rate radiation, real-time ageing, burn-in of 48-168 hours, and lead-unit field hours for gas turbines (2-4 years). These are mostly avoided by arguing *equivalence* to a part that already has a service history [f16, c08, c24].
- **Clock type.** Mostly queue. Physics is the floor.

### Step 9: Package compilation (SAR/TDP, 8110-3, PMA data)
- **Time and cost.** A large part of the 300-1,000 hours [c05].
- **Who does it.** Applicant engineers, by hand.
- **What is manual.** Prose PDFs in three service-specific formats [g04].
- **Undone or broken.** No machine-readable evidence schema exists (no eCTD equivalent for parts). Packages are rejected on form [g03, g04, s08]. Packages are not batched across NSNs [g03].
- **Clock type.** Labour.

### Step 10: Intake and completeness screen
- **Time and cost.** At DLA, Value Engineering accepts about 90% at this gate. Land and Maritime had 7 analysts in FY18 [g03, s08]. Each loop adds 30 days or a full reset [s08].
- **Who does it.** The DLA Competition Advocate Office and Value Engineering, and FAA project intake.
- **Undone or broken.** No applicant checks a package against the reviewer's own checklist before submitting [s08]. This is the easiest step to automate.
- **Clock type.** Queue.

### Step 11: Engineering review and RFI loops (the binding step)
- **Time and cost.** For DLA, the ESA takes 90 of about 190 nominal days [s08]. The ESA queue is often 180+ days [c22]. Historically it ran 6-12+ months (recalled) [s06]. In the Rotair case (GAO B-409950), about 12 weeks passed before review started, review took 3.5 months, then the package went on hold with RFIs in 6 areas while the incumbent won a 5-year IDIQ [g04]. For FAA PMA test-and-computation, it is 9-18 months, with each comment cycle adding 4-8 weeks, and comment cycles dominate the variance in schedule [g01]. Navy AM throughput is "tens of TDPs per quarter against a goal of hundreds" [g08].
- **Who does it.** Service ESAs, FAA ACOs and ODAs (75 holders) [f07], and NAVSEA technical warrant holders.
- **What is manual.** All of it. Each NSN starts from zero [c02].
- **Undone or broken.** No reviewer tooling. No precedent or similarity search. No government baseline: one of DLA's top rejection reasons is "can't validate part (no government data to compare)" [g03, s08]. Liability pushes reviewers toward "need more data" [g03]. By statute, critical safety items (CSIs) can be approved only by the government design control activity. DoD has no designee path like the FAA DER/ODA [g04]. The 2024 FAA Reauthorization tightened ODA oversight rather than widening delegation [f07]. The FAA publishes no queue metrics and charges no fee [g01, s08].
- **Data conflict to resolve.** RPPOB data show about 91% of decided SARs approved (40 of 44) [g03]. FY17 Land and Maritime approved 111 of 225 decided, with 144 pending [s08]. In both data sets the loss sits in the pending queue and in packages never filed. In FY16 the pending SARs held about 12x the savings of the approved ones [g03, f12].
- **Clock type.** Queue, legal and liability. This is the dominant clock.

### Step 12: Production approval, quality system and first article / conformity
- **Time and cost.** A quality system is cheap: about $10-50k for AS9100 and $50-200k (recalled) for 21.137. The holder's first MIDO production approval takes 6-18 months (recalled) [s07]. An AS9102 report takes about 8 hours by hand or about 1 hour with tools [s07, s09]. DLA first article testing (FAT) takes months [s07].
- **Who does it.** MIDO, DCMA, DARs, and shop quality staff.
- **What is manual.** Witness visits and paper conformity [g01, s09].
- **Undone or broken.** Ballooning the drawing is a commodity. Proving *equivalence to the OEM population* with uncertainty is not done by anyone [s09]. CT data for critical features is not accepted [s09]. No per-serial conformity passport exists. FAT waivers based on past performance (DLAD 9.3: 5 years, or 3 years for CSI) are under-used [s07]. Approval covers one part number, one manufacturer and one site, and does not transfer [g04]. In-situ AM monitoring earns no credit with any regulator [c04, f04].
- **Clock type.** Queue and legal.

### Step 13: Approval, listing and the next competitive buy
- **Time and cost.** Revenue arrives only at the next buy. DLA guarantees a new source 40% of the award for at least 1 year (DAG 17.7501-6) [g03, s08]. Awards do not wait for pending SARs, and a justification and approval (J&A) can lock out new sources for 5 years [g04, f12]. Similar DLA work draws a median of one bidder (52% single-bid) [c16].
- **Undone or broken.** Nobody times approvals to J&A expiry or the solicitation calendar [g04, f12].
- **Clock type.** Legal and queue.

### Step 14: Release certificate, provenance and return to service
- **Time and cost.** Per part at receiving inspection.
- **Who does it.** Receiving inspectors check paper against the box [s10].
- **Undone or broken.** No registry exists to check an 8130-3 or Form 1 against its issuer, and no registry records who is authorised to sign. AOG Technics sold more than 60,000 parts on altered certificates and was caught by one technician's eye [s10, c08, c09]. Electronic 8130-3s have been legal since 2009, but the first digitally signed one shipped in October 2025 [s10]. Non-serialised hardware has no identity at all [d02]. Blockchain efforts stalled because they protect the record after entry, not the truth of the first entry [c09, f09].
- **Clock type.** Labour. A verification gap.

### Step 15: Continued airworthiness and field feedback
- **Who does it.** FAA SDRS, which records failures but not the installed base or hours behind them; part number is optional, after the FAA dropped the rule requiring it in 2005. Military reporting goes through JDRS/PQDR, which is tagged by CAGE code [s11].
- **Undone or broken.** No ledger compares PMA and OEM reliability with denominators. The only hard data point is anti-PMA: ECi cylinders failed at about 32x the OEM rate [s11]. Field data is never fed back into the equivalence case [c06, s11].
- **Clock type.** Data access.

### Cross-cutting gate A: Liability, insurance and lessor acceptance
An FAA approval transfers no liability (Sikkelee). The FAA itself is immune (Varig) [s12]. Engine leases signed in November 2025 and August 2026 still ban PMA and DER content [d02]. Lessors control about 40% of the fleet and act as a second regulator [d06]. Nobody offers evidence-priced cover or a residual-value guarantee [s12, d06]. On the military side the main exposure is the False Claims Act over conformance, which is a verification problem [s12].

### Cross-cutting gate B: Cross-border validation
Only FAA PMA travels abroad. The TIP slot for EASA EPA is "Reserved". Canada rejects identicality. China accepts only parts with minor or no-safety-effect failure conditions, and those classifications are not published. Critical parts need a separate EASA STC [g12].

---

## 2. Where elapsed time and cost concentrate, by regime

| Regime | Dominant clock | Permission holder | Physics share | Notes |
|---|---|---|---|---|
| FAA PMA / DER repair | Comment-cycle queue (4-8 weeks each), ACO/ODA capacity, MIDO | ACO, ODA (75), DERs | Small. Repairs are mostly analysis [g02] | 9-18 months for complex PMA [g01]. Lessor acceptance is the hidden gate [d02] |
| DLA SAR (non-CSI) | ESA review plus pending backlog; losses before filing | Service ESA | ~14 weeks of ~2.5 years [g03] | Nominal ~190 days, ESA 90 days [s08] |
| Military CSI | Statutory government-only review; RFI loops | Design control activity (no delegation) | Moderate (rigs, witnesses) | 12-week queue, 3.5-month review, then hold [g04] |
| Navy Level I / SUBSAFE | TDP adjudication, OQE review | NAVSEA TWH | Moderate | Tens of TDPs per quarter; 7 years for one AM procedure [g08] |
| NRC commercial-grade dedication (CGD) | Technical evaluation labour; NUPIC audit capacity (33-month cycle); EQ/seismic rigs | The dedicator's Appendix B program (NRC approves no plans) | EQ ageing is real | Utilities pay per outage day (~$1-2M/day) [g05, c12, d03] |
| ASME/NBIC/API | Level 3 FFS engineers; Authorized Inspector hours | AIAs (insurers) | Low | R stamp costs $1,150 per 3 years; permission is cheap [g06] |
| Rail (AAR, EU ECM) | Service trials (years); per-agency re-approval | AAR committees, ECM risk appetite | Service-trial clock | Like-for-like replacement is already legal in the EU [g07] |
| Power (gas turbines) | Lead-unit fleet hours (2-4 years); OEM LTSA leverage | Owners and insurers | High (field hours) | No neutral verifier and no loss register (IMIA 2009) [c24, g10] |
| Medical service parts | Hospital trust; firmware pairing | Mostly nobody (servicing is unreviewed) | Low | No PMA-like tier [g11] |
| Electronics DMSMS | Per-platform re-qualification; QML lots | Program office ECP, DLA, DO-254 | Burn-in and life tests (~1,000 h) | GEM takes 48 weeks, Rochester 18 months [c11, c35, g09] |
| NRTL (energy hardware) | Lab queue plus admin | NRTL, local fire marshal | ~32 h of actual bench time against 9-12 weeks plus 18 weeks admin [c33] | |

**Synthesis.** In every regulated regime, the hours sit in steps 5, 6 and 9 (labour), and the calendar sits in steps 7, 10, 11 and 12 (queue and permission). Physics is usually 5-25% of elapsed time [s06, f16]. Only gas turbines, rail service trials, EQ ageing and electronics life tests have physics as the true pacing item. Even there, a comparative argument against fleet evidence can stand in for absolute life proof [f16, s11].

---

## 3. Things nobody does today, ranked by impact (assuming abundant compute and intelligence)

### 1. A machine reviewer in the reviewer's own seat, plus an evidence-linked package standard
- **What it is.** Executable checklists per ESA, ACO and TWH (the SAR guides, 8110.42, AFMC Form 260, the CSI handbook, AC 33-13), pre-adjudication of non-blocking RFIs, and drafted dispositions with every claim cited to evidence. The package schema is something like STEP AP242 + QIF + CT volumes + a claim-to-evidence graph [c02, c06, s08, g04, f07, f12, c31].
- **Why first.** It attacks the dominant clock in every regime. INL finds 95% of applicant-regulator exchanges non-blocking and models up to 65% faster licensing [f07]. The NRC prices reviewer time at $337/hr [d08]. Analogues show both buyer types: CivCheck sells free-to-regulator, applicant-pays; GreenLite reaches 0.5 resubmission cycles [c31, c32, f12].
- **Binding constraint.** Regulator acceptance, IL4/5 and ITAR hosting, and the conflict of interest if the same firm also files packages.
- **To change it.** An SBIR or OTA pilot with one ALC ESA (C-130 at Robins, KC-135 at Tinker) under which AI pre-review is formally the first pass, citing 10 USC 3243's prompt-opportunity and stated-reasons duties [c02]. Use a firewalled entity or give the tool away free.

### 2. Delegated signing capacity inside an AI-native house, plus a statutory deadline on review
- **What it is.** Acquire an existing ODA, DER group, EASA DOA or nuclear dedicating entity rather than spending years applying, and put AI behind the human signers [f07, g01, g02, c12, g05]. On the DoD side, lobby for a 10 USC 3243 subsection adding an evidence standard, a 90-180 day deemed-approval clock, and accredited third-party reviewers [f08, c32].
- **Why second.** It turns cheaper evidence into shorter calendar time. Norm Ai, GreenLite and AAR's ART all show the money goes to whoever holds the stamp [c31, c32, c17].
- **Binding constraint.** Law for CSIs (government-only review) and post-737 MAX oversight politics.
- **To change it.** Buy a holder. For DoD, use NDAA language with a Hatch-Waxman-style concession to OEMs, such as excluding new platforms [f08].

### 3. A government baseline plus a precedent and similarity graph, so one approval covers many parts
- **What it is.** CT, metrology and material fingerprints of serviceable stock obtained through bailment, which removes the "no government data to compare" rejection [g03, s08]. Add a cross-NSN graph so one approved Category III SAR turns sibling parts into Category II-G cases [g03, f13, c18]. In electronics, an "approve once, use everywhere" SMD-level equivalence designation [c11].
- **Precedent.** Similarity is already institutionalised: DLA Category II, QML, MMPDS, and NCAMP's claimed 4x faster and 10x cheaper qualification [f13, a10]. AST Korea received one PMA covering 6,395 items [c22].
- **Binding constraint.** A policy change at ESA level (not statutory), plus access to PQDR and GIDEP failure labels.
- **To change it.** A DLA CRADA, and a published back-test of the similarity graph against field failures.

### 4. An equivalence engine: multimodal material and process "spec passport" plus statistical equivalence
- **What it is.** Fuse XRF, LIBS, eddy current, hardness, XRD, ultrasound and CT into a calibrated posterior over spec, temper and process. Use Bayesian, TOST or SPRT equivalence on a handful of confirmatory specimens instead of 18-55+ [s04, f05, f03, f06, c07]. Build it on a paired NDE-to-destructive atlas of about 3,000-10,000 retired parts from AMARG and DLA scrap, at roughly $10-60M [s04, f05].
- **Why it matters.** Steps 5 and 6 hold most of the engineering hours, and the result is a defensible data moat.
- **Precedent.** AMS 2658 for aluminium temper, and the regulations never fix specimen counts [f03, f05].
- **To change it.** An SAE AMS / ASTM E07 standard with probability-of-correct-identification curves, piloted with one ESA.

### 5. A credibility standard for model and simulation evidence on replacement parts, plus a blind predict-then-test ledger
- **What it is.** The V&V 40 / FDA 2023 template applied to parts. No aviation equivalent exists, and the CM4QC roadmap says the FAA "has no procedures" to use computational results [f01, f06, a05, c14, c34]. The missing input is a side-by-side record of predicted versus tested results, which CM4QC says nobody funds. An approval factory produces it as exhaust [f01].
- **Start where it is easiest.** Ancillary tests first, as Simcyp did in pharma [c34].
- **To change it.** Join CM4QC, then pursue an FAA issue paper on one PMA, then an AC.

### 6. An owned lights-out test foundry, a pre-characterised material bank and adaptive test design
- **What it is.** 100+ frames, robotic specimen loading, in-house CNC, heat treatment and NDT, and in-situ early stopping [s06, f11, f16]. Capex is about $20-40M. It collapses the 75-95% of qualification time that is queue down to the physics floor, and a shelf of legacy heats removes the 40-80 week material wait [s06].
- **Status.** Nobody sells approval-grade robotic testing. The roughly $800M+ in self-driving-lab funding goes to materials discovery [f11].

### 7. A ranked universe of approvable parts plus a rights-provenance graph
- **What it is.** Fuse PUB LOG, FOIA price-paid logs, DIBBS, the FAA PMA list, retirement schedules and modelled approval probability [s01, d01]. Add automated sweeps for lapsed GPR and unmarked deliveries, and batched 7037 challenges; this is the tool DoD cancelled [s02, d01]. It is pure compute with no regulator needed, and the cheapest first wedge.

### 8. Attested evidence and per-serial proof-carrying parts
- **What it is.** Instruments sign data at capture, enabling remote and asynchronous witnessing. Neither FAA nor NRC rules require physical presence [f14]. Add a per-serial conformity passport tied to the release certificate and a surface fingerprint [s07, f09], and an issuer and signer registry for 8130-3 and Form 1, which the industry coalition requested in its Recommendations 8-9 and nobody owns [s10, c09].
- **Why it matters.** It cuts witness queues and closes the AOG-type fraud gap.

### 9. A reliability ledger with denominators, plus evidence-priced cover
- **What it is.** Cross-operator PMA-versus-OEM rates by part number and approval holder [s11]. That ledger feeds an MGA or residual-value guarantee that turns lessors' and insurers' "no" into a priced "yes" [s12, d02, d06]. In power, it is the turbine loss register IMIA asked for in 2009 [g10, c24].
- **Why it matters.** It unlocks demand after approval and over time earns lighter re-approvals.

### 10. Behavioural equivalence certificates for obsolete electronics
- **What it is.** Active-learning conformance testing of golden parts, formal equivalence from the reconstructed model to the new design, and pre-qualified emulation substrates per package family. Qualification is then inherited from the substrate, and Class I changes become Class II [c23, c35, f10, c11, g09].
- **Why it matters.** It attacks the most expensive permission step: system re-qualification repeated for every platform. A $46.7M F-16 sole-source buy drew zero RFI responses [c18].

### 11. A POD and method-qualification engine for AI inspection and in-situ monitoring
- **What it is.** Simulated flaws plus a small robotic anchor set produce a90/95 curves. Add the missing ML-POD and simulation-credibility standards, and a reusable STC-like method approval [f02, c10, c04, f04]. Nuclear already allows this (ENIQ RP13; steam-generator ADA) [f02, c10].
- **Why it matters.** It earns CT and coupon credit, which is 25-50% of AM part cost [f04].

### 12. Executable bilateral rules and a single test campaign that satisfies several authorities
- **What it is.** One evidence set that serves FAA, TCCA, an EASA Non-Basic STC and CAAC [g12]. It is narrower in impact but multiplies markets per approval.

### 13. A clean-room independent-derivation ledger
- **What it is.** Hashed specimens, signed scans, and a link from every feature to the measurement it came from. It is a defence against trade-secret claims and can be underwritten as IP insurance [c27, s02]. It cuts litigation tail rather than calendar time.

**Constraints that remain after all of this.** The incompressible physics clocks are creep, real-time ageing, low-dose-rate radiation, burn-in, and the fatigue floor of about 4-8 weeks parallelised. The government-only CSI review is statutory. Golden samples and OEM data rights stay scarce. Every one of the levers above works by moving those clocks out of the critical path (equivalence, similarity, attested evidence, delegation) rather than by making the physics faster.

The raw notes behind every id are in `/home/user/nuketime/research/repair/v2/raw/*.md`. This map was built from the summaries without re-reading those files, so exact numbers should be checked against them, especially the (recalled) ones.