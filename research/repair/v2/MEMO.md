# The verification side of the approval pathway

*2026-10-21. 119 agents ran on Dhruv's follow-up: is anyone already doing the Approval Factory, what does the full verification pathway look like, what in it is left undone, and what AI play sits on the verification side. Treat hard technical problems as solvable.*

*The agents were 93 research agents (35 competitor sweeps, 12 regulatory-regime maps, 12 step deep-dives, 16 frontier questions, 8 demand checks, 10 analogs), 3 syntheses, 4 play lenses, 1 ranker, and 18 attackers (a competitor checker, a killer and a rescuer for each of 6 finalists). Raw notes with about 900 cited URLs are in `raw/`. The synthesis files are `LANDSCAPE.md`, `GAP_MAP.md` and `ANALOGS.md`, and everything structured is in `results.json`.*

*Evidence caveat: the shared search quota ran short again. 73 of 93 notes mention it. Those agents fetched primary sources directly and flagged anything recalled from memory.*

---

## Verdict

1. **Nobody is running the Approval Factory, and nobody sits in the reviewer's seat for parts approvals.** The closest are:
   - **ELEVAN**, a 10-person firm with a $110k Phase I award in 2024 for AI-assisted source-approval review and no Phase II.
   - **20-30 DLA SAR shops** that do the work by hand on about $100M of SBIR money.
   - **HEICO, AAR and TransDigm.** They own the approvals but disclose no AI in approval engineering. HEICO's R&D rose 66% while its PMA output stayed flat.
   - **Everstar** in nuclear, which claims parts qualification "at scale" but has published nothing.
   - **SRI's GEM programme** for chips, which works but takes 48 weeks to 18 months per part.

   The money in this space has gone to the steps either side of approval: Nominal ($1B, test data), Flow Engineering ($750M, requirements), Istari (model-based certification for whole new airframes), GroundControl and F4 (first-article paperwork), and Novineer (scan-to-CAD, 0.7 mm error).
2. **Physics is not the clock.** In every regulated regime the engineering hours go to material identification, the substantiation argument and package compilation. The calendar time goes to reviewer queues, RFI loops, test pre-agreement and production approval. Physical testing is usually **5-25% of elapsed time**. Examples:
   - A DLA SAR takes about 2.5 years, of which about 14 weeks is physics.
   - An NRTL listing takes about 32 hours of bench time and 9-12 weeks of queue plus 18 weeks of admin.
   - A fatigue-critical metal part needs about 4-8 weeks of physics when fully parallelised, inside a 6-18 month programme.
   - Physics paces the work only for gas-turbine fleet hours, rail service trials, nuclear EQ ageing and electronics life tests.
3. **So the open AI play on the verification side is to turn approval into code.** Encode each rulebook as checkable predicates. Link every claim in a package to its evidence. Use a deterministic checker to recompute every number, so nobody has to trust the model. Then attach that engine to whoever holds the signature. The attackers ran this logic against all six finalists, and each one survived only once it was attached to a signature: the dedicator's, the approval holder's or a depot's. A verification tool sold on its own gets copied or bundled.
4. **My pick: Dedicate**, an AI-native nuclear commercial-grade dedicator, scoring **17.3/25**. Its engine is the same one FirstPass would use in defence (17/25).
   - Nuclear is the one regime where **the permission already sits with a private company and no rule has to change**. The NRC approves no dedication plans; the dedicator's own Appendix B programme is the permission. Hours saved by AI therefore turn straight into speed and margin.
   - Buyers pay for speed, because outage days cost about $1-2M each.
   - Demand is rising, from restarts, 80-year licences, data-centre power contracts and SMR builds.
   - The incumbents (Mirion/Paragon at about $585M, Curtiss-Wright, Westinghouse) bill engineering hours, so cutting those hours cuts their own revenue.
   - It fits the energy brief.
   - Defence SARs (FirstPass) are the second market for the same engine.

---

## 1. Who is already in the pathway

See `LANDSCAPE.md` for the full table.

| Step | Crowded or empty | Who is there |
|---|---|---|
| Target selection and demand data | Thin | Govini, Palantir and PTC Servigistics provide sustainment analytics. None ranks parts by how easy they are to approve |
| Data rights and IP clearance | **Empty** | Done by hand by lawyers. No clean-room AI reverse engineering with an audit trail exists |
| Geometry capture and scan-to-CAD | **Crowded** | Backflip, Physna, Novineer, Hexagon, Creaform. Tops out around 0.7 mm and covers only 5-15% of package hours |
| Material and process identification | **Nearly empty** | One-off metallurgy labs (Element, IMR); Fraunhofer 3MA prior art; NIAR teardowns. Nobody keeps a population baseline |
| Substantiation and equivalence argument | Empty for replacement parts | Istari works on whole new airframes; Xcert on compliance documents (about 50% usable) |
| Physical testing | Crowded but queue-bound | Element, Westmoreland, SwRI, NIAR/NCAMP. All billed per test and run by people |
| Package compilation | Manual | SAR shops and DERs |
| **Reviewer intake, review and RFI loops** | **Empty** | ELEVAN ($110k) and Calibre (generic TIC auditor AI, $3.3M). Regulators are building their own tools (NRC SimplifAI, FDA Elsa) |
| Production conformity and first article | Crowded | GroundControl, F4, Rapta |
| NDT method qualification | Government and non-profit only | Sandia AANC, EPRI PDI, ENIQ, Trueflaw, UDRI. Nobody sells it commercially |
| Release certificate and provenance | Crowded | ProvenAir, FLYdocs, Bluetail |
| Nuclear dedication | Incumbents are manual; startups sell tools | Paragon/Mirion, Curtiss-Wright, UCI. Nuclearn and Atomic Canyon sell to utilities and sign nothing |
| Obsolete chip equivalence | One proven but slow programme | SRI GEM/AME, Rochester, Tekmos, KaiSemi, DMEA |

---

## 2. The pathway and what nobody does

See `GAP_MAP.md` for all 16 steps and regime tables.

The dominant clock in each regime:

| Regime | Dominant clock | Who holds the permission | Physics share |
|---|---|---|---|
| FAA PMA / DER repair | Comment cycles of 4-8 weeks each, plus ACO and ODA capacity | ACO, ODAs (75), DERs | Small |
| DLA SAR (non-CSI) | ESA review and the pending backlog | The service's ESA | About 14 weeks of about 2.5 years |
| Military critical safety items | Statutory review by government only | Design control activity | Moderate |
| Nuclear commercial-grade dedication | Technical evaluation labour; NUPIC audits on a 33-month cycle | **The dedicator itself** | EQ ageing only |
| Gas turbines | Fleet hours on a lead unit, 2-4 years | Owners and insurers; no neutral verifier exists | High |
| Electronics obsolescence | Per-platform requalification, about 1,000 h of life tests | Programme office, DLA | Moderate |

Data on SAR outcomes conflict. In FY17, DLA Land and Maritime approved 111 of 225 decided SARs, with 144 still pending. RPPOB data show about 91% approved. Both data sets put the loss in the pending queue and in packages never filed. INL found about 95% of exchanges between applicants and regulators are non-blocking.

**Things nobody does today, ranked by impact:**
1. A machine reviewer in the reviewer's own seat, plus a package standard that links each claim to its evidence (an "eCTD for parts").
2. Delegated signing capacity inside an AI-native house, by buying an existing ODA, DER group or dedicator. On the defence side, add a deemed-approval clock through an amendment to 10 USC 3243.
3. A government baseline plus a precedent and similarity graph, so one approval covers sibling parts.
4. An equivalence engine: a multimodal "spec passport" that identifies material and process, plus statistical equivalence.
5. A credibility standard for simulation evidence on replacement parts, with a public blind predict-then-test ledger.
6. A lights-out test foundry with a bank of pre-characterised material.
7. A ranked list of approvable parts, plus a graph of who holds the data rights.
8. Attested evidence and per-serial "proof-carrying" parts.

---

## 3. Six verification plays, each attacked three times

Four lenses each proposed 5 plays. The ranker merged them into 6. Each was then scored out of 25 by a competitor checker, a killer and a rescuer.

| Play | Competitor / Killer / Rescuer | Average | What it is | What lets it live |
|---|---|---|---|---|
| **Dedicate** | 18 / 16 / 18 | **17.3** | AI-native nuclear commercial-grade dedicating entity, later with owned EQ and seismic rigs | Buy a small NUPIC-accepted dedicator. Start with mild-environment, non-EQ commodity items for restart and life-extension plants. Sell dedicated parts and a 72-hour emergent-part guarantee rather than evaluations. The product is a traceability chain from design basis to safety function, failure mode, critical characteristic, acceptance method and signed evidence |
| **FirstPass** | 18 / 15 / 18 | 17 | Machine reviewer and approval-as-code for DLA ESAs, FAA ACOs, ODAs and NUPIC | Applicants pay first: a $5-10k SAR-readiness prescreen built from the shops' own past packages, which needs no ATO or FOIA. Then a conflict-free SAR evaluation contractor paid by DLA. Then a statutory third-party reviewer. Kept separate from any party holding approvals, on the UL model |
| **Method House** | 17 / 15 / 19 | 17 | Accredited body that qualifies AI inspection methods (simulation-assisted POD) and issues "born-certified" passports | An "NCAMP for inspection". It sells submission-ready POD dossiers that a DER, ESA or NAVSEA engineer can cite, with space and defence AM (NASA-STD-6030) first, because that acceptance is customer-controlled. There is no FAA "method approval" object |
| **Twin Silicon** | 17 / 16 / 18 | 17 | Behavioural-equivalence certificates for obsolete defence chips | Start on verification: active-learning ATE plus a formal check from measured silicon to new RTL, sold to SRI, DMEA and Rochester. Grow into substrates that are qualified once and reused |
| **Reference Atlas** | 16.5 / 15 / 18 | 16.5 | Paired NDE-and-destructive atlas of legacy parts, giving material "spec passports" and an equivalence mark | Under a CRADA with one Air Logistics Complex, the government co-owns the fingerprints, so they count as government data. Start with aluminium 7075/2024 and 4340 families rejected for "no government data". Acts as the verification engine of the Approval Factory |
| **Blind Ledger Foundry** | 14 / 13 / 18 | 15 | Lights-out predict-then-test lab selling test credit | Weakest standalone, because testing is not the binding queue. Survives only as the Approval Factory's in-house evidence arm |

**Rejected or merged:**
- *Second Source*, the earlier Approval Factory. It is an approval holder, not a verifier; it becomes the captive first customer for the engine.
- *Stamp* and *Signet*, buying an ODA. These are a holder's play in commercial aviation, a later vertical move.
- *Truth Ledger*, *Baseline* and *Heatline*.

### What converged
All three attackers on every finalist reached the same rule: **the verification engine is worth most when it is attached to a signature.** Selling the engine as a tool invites copying: by AAR, which already ships agentic AI and owns an ODA, by generic LLM platforms already inside the Air Logistics Complexes, or by the regulators' own tools. Holding the signature turns saved hours into price and speed.

That is why Dedicate leads. In nuclear the signature can be bought with a small dedicator, and no regulator has to accept anything new. FirstPass, the Atlas and the Ledger are the same engine aimed at defence, where the signature belongs to the government. There the business has to begin applicant-paid and earn its way into the reviewer's seat.

---

## 4. Cheapest tests (run in parallel)

**Dedicate, about 6 weeks**
1. Get 25-50 already-closed dedication packages for mild-environment Class 1E commodity items. Source them from one restart or life-extension plant (Palisades/Holtec, Crane, or a Constellation or TVA site) or from a small dedicator.
2. Regenerate each technical evaluation and acceptance plan blind, using only the FSAR, design basis and procurement specs.
3. Have the plant's own dedication engineers and a retired NUPIC lead auditor score the results against the signed originals.
4. Kill it if engineer hours per accepted package do not fall at least 3x, or if utility QA would not accept the result with a human signing.

**FirstPass, about 4 weeks**
1. Get 30-50 past non-CSI C-130/KC-135 SAR packages, with their RFI and disapproval letters, from 3-5 SAR shops. The shops own these, so no government data is needed.
2. Encode the WR-ALC/OC-ALC SAR checklists as predicates and predict each package's RFIs blind.
3. Split each package's elapsed time into queue, RFI rounds, testing and review.
4. Kill it if the predictor catches fewer than half of the real RFIs, or if review and RFI loops are under half of elapsed time.

---

## Files
- Page: https://claude.ai/artifact/QhVbxyEGMpRXNhhZAQD5Kh
- `MEMO.md`: this memo
- `LANDSCAPE.md`: every player, by pathway step
- `GAP_MAP.md`: the 16-step pathway, regime clocks, and the ranked list of what nobody does
- `ANALOGS.md`: lessons from Vanta, UL, EDA sign-off, Euro NCAP, FDA in-silico, Hatch-Waxman CROs, Carfax and others
- `results.json`: all structured outputs
- `raw/*.md`: 93 research notes with sources
