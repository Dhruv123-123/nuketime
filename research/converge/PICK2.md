# The second pick: no prospecting, no drilling

Written 3 October 2026, after the first pick (`PICK.md`, producible uranium for ISR plants) was
ruled out along with anything else touching prospecting, exploration or drilling. Everything here
was scored again from scratch. Evidence is in three models built for this decision:
`designs/release/` (the pick), `designs/megawatts/` (a strong runner-up that failed its test) and
`designs/wellfield/` (the first round), plus sourced research notes in this folder (`fuel_cycle_notes.md`, `fleet_ops_notes.md`,
`overlooked_notes.md`, `lost_mw_notes.md`).

## The answer

**A 100 % X-ray inspection and sorting station for TRISO fuel particles, sold to the new US
coated-particle fuel lines as they ramp, that pays for itself by stopping whole batches from
failing release.**

Every TRISO batch today is released by destroying a sample of tens to hundreds of thousands of
particles in a burn-leach test. If too many in the sample are defective, the whole batch (about
13 million particles, roughly $150,000 of fuel) fails, because there is no way to find the bad
particles in the rest. The NRC's own slides say this QC "generates waste, adds cost". A station
that images every particle and removes the visibly defective ones turns a pass-or-scrap decision
into a sort. The first product sits in front of the unchanged release test, so it needs no new
regulatory approval; replacing the destructive test comes later.

## Why this one

1. **It is open.** No company sells 100 % inline TRISO inspection (searches on 3 October 2026).
   The work that exists is research: ORNL's machine-learning QC of coated particles and
   X-ray CT layer measurement, INL's AUDIT image software, and China INET's X-ray inspection of
   whole pebbles (2014). CT makers (Zeiss, Nikon, Comet Yxlon) sell instruments, not release
   decisions.
2. **The buyers are being created right now.**
   - TRISO-X received the first NRC Category II fuel licence (SNM-7007) in February 2026, and TX-1
     (5 MTU a year, about 700,000 pebbles) finished vertical construction on 25 September 2026.
   - Standard Nuclear listed in July 2026 with a $576.9M backlog and is bringing up two 2.5 MTU
     lines from Q4 2026.
   - BWXT made the TRISO for Antares' first criticality and plans a $500M Wyoming plant. Kairos is
     making its own fuel with LANL.
   - DOE's $60M Project Prometheus aims for three times faster fuel fabrication with AI.
3. **The money is in the fuel maker's own P&L.** The model below puts a sorter at roughly $1M to
   $30M a year per 5 MTU line, largest while a line ramps and its defect rate is still high, which
   is 2027 to 2030 for every line above.
4. **It is a tangible performance gain, not a safety-only argument**: higher yield, smaller
   destructive samples, faster release, and about 10 times fewer defective particles shipped.
5. **It can be shown by November** with simulation, a benchtop CT on non-nuclear surrogate
   particles, and calls to the eight or so organisations that make TRISO.

## How the candidates scored

Scores are 1 (weak) to 5 (strong). *Open* is the absence of funded competitors. *Proof by Nov* is
how much of the case could be shown in eight weeks. *Ceiling* is the size of the business if it
works.

| Candidate | Pain evidence | Open | Tangible merit | Proof by Nov | Ceiling | Verdict |
|---|---|---|---|---|---|---|
| **TRISO 100 % inspection and sorting (the pick)** | 4 | 5 | 5 | 4 | 3 | Pick |
| Lost-megawatt recovery for operating reactors | 4 | 2 | 3 | 4 | 2 | No: model says about 1 MWe per unit over conventional KPIs; GSE/Belsim, BTB Jansky, Curtiss-Wright, EtaPRO installed; MUR largely done (57) |
| Uprate engineering engine | 4 | 3 | 4 | 2 | 3 | No: 31 applications expected 2026 to 2032, but the work is services run on OEM codes |
| Criticality-safety copilot (fuel cycle, HALEU) | 4 | 4 | 2 | 3 | 2 | Close second; capped because a qualified engineer signs every evaluation and buyers number in the dozens |
| Bayesian fuel qualification | 4 | 3 | 4 | 1 | 3 | Labs and Prometheus already on it; needs irradiation data you do not have |
| Quality copilot for shops entering nuclear | 3 | 3 | 2 | 3 | 3 | Software must itself be NQA-1 qualified; small contracts per shop |
| Radioligand dose orchestration | 4 | 2 | 3 | 2 | 4 | GE, Siemens and DOSIsoft moved in during 2026; nuclear angle thin |
| Nuclear document search and ops AI | 4 | 1 | 2 | 3 | 3 | Atomic Canyon, Nuclearn ($10.5M A), Everstar already there |
| Co-location, rad-hard electronics, decommissioning | 2 to 3 | 2 to 3 | 2 | 1 | 2 to 4 | Few buyers, hardware qualification, or government sales cycles |
| ISR wellfield operations (first round) | 4 | 5 | 2 | 2 | 2 | Excluded now; model said 3 % NPV |

The two software ideas that looked strongest on paper both failed the same way when modelled.
Optimising a competent operation is worth single-digit percent (3 % NPV for ISR wellfields, about
1 MWe per reactor for lost-megawatt monitoring). The pick is different in kind: it changes what is
physically possible (sorting a batch that today can only be passed or scrapped), so its value is
not a percentage of an already-good process.

## The prototype test

Full method and tables are in `designs/release/DESIGN.md`.

**Part A, release economics.** With batch defect rates lognormal around 5e-6 to 3e-5 against the
1e-4 limit, the cheapest sampling plan costs $3M to $39M a year per 5 MTU line (failed batches plus
destroyed samples). Perfect 100 % inspection would cost about $0.3M.

**Part B, can X-ray see the defects?** A voxel model of the particle, projected in three views
with realistic noise, scored by an untrained self-referencing detector at 0.1 % false flags:

| 20 um pixels, 10,000 photons per pixel | Caught, 3 views | Caught, 1 view |
|---|---|---|
| Missing SiC patch, radius 80 um | 92 % | 52 % |
| Missing SiC patch, radius 50 um | 44 % | 23 % |
| SiC thinned by half over 200 um | 80 % | 50 % |
| Tight crack through the SiC | about 1 % | under 1 % |

So radiography finds missing and thin SiC but not tight cracks. That rules out replacing burn-leach
on day one and shapes the product.

**Part C, a sorter in front of today's test.** If the station sees a share g of real defects, the
saving per 5 MTU line is $0.9M to $1.9M a year for a mature process (median 5e-6) and $4M to $11M
for a ramping one (1e-5 to 2e-5, g = 0.5), up to $31M for a rough start-up.

## Company brief

**Problem.** New TRISO lines must release fuel by destructive sampling, and a batch that fails
cannot be sorted. The AGR programme's specs call for samples from 10 to more than 120,000
particles per test. A ramping line with a median defect rate of 2e-5 fails about one batch in ten
at the cheapest plan.

**Product.**
1. A station that images every coated particle (trays or a falling stream) from at least three
   angles, flags missing and thin SiC and geometry defects, and diverts them.
2. A release ledger that records every particle's images and result, gives the batch's estimated
   defect fraction with uncertainty, and hands QA a release package.
3. Process feedback: defect rate by coater run, position and time, so the line fixes the cause.

**Business model.** Sell or lease the station ($2M to $4M is an assumption to test) with a
per-batch software fee, priced against the batches it saves. Start with the line that hurts most
during ramp.

**Size, honestly.** Eight to twelve Western TRISO lines by about 2030 makes the station business
worth tens of millions a year, not billions. The larger company is the second step: an inspection
signal good enough to become the release method (cutting destructive testing), then the same
particle-level QA for other advanced fuels and components, as the US scales fuel fabrication.

**Competition and the answer to "why won't they build it themselves?"** Fuel makers have strong QC
teams but are spending 2026 to 2028 on licensing and first production, not on building an
inspection product; X-energy, Standard Nuclear and BWXT each need the same thing. CT vendors sell
machines and leave the algorithms, sorting and release statistics to the buyer. National labs
publish methods and license software (INL AUDIT) but do not build production stations.

**Risks.**
1. Real defect populations may be mostly cracks, which radiography misses. Test: ask fuel makers
   what share of burn-leach failures are missing or thin SiC.
2. Defect rates on real lines may already be low enough that few batches fail. Test: ask for
   failure rates in pilot production.
3. Throughput: about 3e10 photons a second at the detector for 400 particles a second in three
   views (inferred). Test: a source vendor quote and a benchtop run.
4. Fuel makers may insist on building in-house. Test: whether any will run a pilot on surrogates.
5. Particles handled outside the coater can be damaged. Test: drop and tray handling on
   surrogates.

## Eight-week validation plan

| Week | Do | Evidence it produces |
|---|---|---|
| 1 | Extend the simulation: a trained detector, five to seven views, phase contrast for cracks | The detection floor and what cracks need |
| 1 to 2 | Book time on a university micro-CT; get non-nuclear surrogate particles (ZrO2 kernels) from ORNL, Kairos or BWXT | Real radiographs of real coatings |
| 2 to 4 | Seed defects on surrogates (ground-through SiC, induced cracks), image blind with three views | Measured catch rate and false flags on real particles, the Knapp-Kushner-style seeded-set test QA teams trust |
| 2 to 6 | Ten conversations (below) | Real batch failure rates, defect mix, and one pilot or letter of intent |
| 5 to 6 | Re-cost Part C with the numbers from the calls | A savings figure in a buyer's own units |
| 7 to 8 | Station design and source quote at TX-1 throughput | A bill of materials and a price |

**Who to call, and what each call must answer.**

| Who | Why them | The call must answer |
|---|---|---|
| TRISO-X (X-energy) | TX-1 starts operations around 2028; Xe-100 spec owner | Batch failure rates in pilot lines, and what share are missing or thin SiC |
| Standard Nuclear | Two lines starting Q4 2026, public company with a backlog to deliver | Would a sorter speed their ramp? Who signs off? |
| BWXT Specialty Fuels | Longest commercial TRISO record, Wyoming plant planned | How release works today; would they pilot? |
| Kairos Power | Makes its own pebbles, has thousands of surrogates | Surrogate particles; in-house versus buy |
| Framatome (Standard JV) | Brings LWR fuel QA culture | What evidence QA would need to rely on an inspection signal |
| ORNL coated-particle group (Hunn, Helmreich, Gerczak) | Wrote the inspection methods and ML QC papers | Defect mix data; surrogate supply; collaboration |
| INL (AUDIT, AGR programme) | Licensable image software and AGR data | Licensing terms; AGR defect statistics |
| A CT source vendor (Excillum, Comet Yxlon) | Throughput and price | Photons per second at 20 um and the cost |
| NRC fuel-facility staff (pre-application meeting) | Path from sorter to release method | What a topical report would need |

**Kill criteria.**
- Fuel makers report that fewer than about 2 % of batches fail release, or that most failures are
  cracks.
- The seeded-set test on surrogates catches under 70 % of missing-SiC defects of 80 um radius at
  0.1 % false flags.
- No fuel maker will run a pilot on surrogates.

If the second holds but not the first, the fall-back is the criticality-safety copilot, the
runner-up that does not depend on imaging physics.
