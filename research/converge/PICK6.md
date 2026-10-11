# The sixth pick: Margin, the AI-native engineering firm for the nuclear fleet

Written 11 October 2026, after Dhruv scrapped heat-to-power and asked to go back to nuclear, ML and
software only. Constraints carried forward: no prospecting, exploration or drilling; size is the first
filter (a $100-200M a year tool market is too small); prefer a named, large bottleneck an ML team can
execute on over a novel but small gap (the lesson of `PICK4.md`). Research notes with every source:
`ml_software_notes.md`. Models and prototype: `designs/margin/`.

## The answer

**Build the engineering firm that delivers nuclear plant uprates, licence renewals and modifications
in half the time, because it holds each plant's design basis as a live, machine-readable graph
instead of 40 years of PDFs.** Start with power uprates, the one place in nuclear where hyperscalers
are already paying billions for megawatts and the named bottleneck is engineering.

**The pitch, in one line:** *every nuclear megawatt the AI buildout is buying from existing plants
has to be engineered first; we engineer it in half the time.*

Three facts make it the strongest nuclear software company we have found:

1. **The money is committed and dated.** In the last nine months, Google agreed to fund 890 MW of
   uprates at 11 Constellation units (more than $4.3B of capex, 6 October 2026), Meta 433 MW at Vistra's
   three Ohio and Pennsylvania plants, Amazon about 190 MW at Calvert Cliffs, Google about 96 MW at
   Vogtle and Hatch, Walmart 30 MW at Dresden. NRC expects 31 uprate applications from 2026 to 2032,
   16 of them in 2027 alone. DOE's UPRISE programme wants 5 GW by 2029 and will lend up to 80 % of cost.
2. **The bottleneck is named, and it is engineering.** DOE names engineering schedule and staffing as
   "one of the bottlenecks for accelerating uprates and restarts" (POWER, March 2026). Columbia spent 18
   months on analysis before it could approve its uprate. Every month of delay on a 160 MW uprate
   costs about $9M of output at today's $70-115/MWh nuclear PPA prices.
3. **Nobody is doing the engineering itself with AI.** Atomic Canyon owns search, Nuclearn owns
   corrective-action screening and procedures, Everstar writes new-build licence chapters, Westinghouse
   keeps its tools inside its own work. Alva Energy ($33M, Feb 2026) develops uprates but shows no AI.
   The incumbent engineering firms are being bought by private equity at scarcity prices (Enercon on
   about $1.25B of equity, April 2026; Jensen Hughes to New Mountain, August 2026), not rebuilt by
   software.

**Why it fits Dhruv's team.** The hard technical problem is turning decades of scanned, inconsistent
technical records into a calibrated, queryable model with honest uncertainty, then choosing where to
spend scarce analysis effort. That is the same job as digitising old well logs and building a
prospectivity model, applied to a plant instead of a basin, with no exploration in it.

## What the company is

**Product, inside the firm: the design-basis graph.** Every calculation of record, its inputs (and
where each came from), its results, its acceptance limit and margin, every UFSAR section and tech
spec that cites it. Built by extracting the headers of thousands of legacy calcs, vendor reports and
UFSAR tables (language-model extraction with engineer review), then kept current as calcs are
revised. On top of it:
- **Trace:** change one parameter (licensed power, a cooling-water temperature, a pump curve) and get
  every affected calculation and the chain that reaches it, on day one instead of after months of
  scoping, with nothing missed.
- **Margin map:** for every limit, how much power is left before it binds, what a modern analysis
  method buys back, and which limits need hardware and with what lead time.
- **Drafting:** the calc revisions, UFSAR markups, tech-spec pages and the licence amendment package,
  pre-written for engineers to check and sign.

**Business: sell the engineering, not the software.** Utilities buy uprate engineering, not tools;
their capital budgets (about $5,000/kW for an uprate) dwarf their IT budgets. So the company is an
architect-engineer that delivers stamped work under its own 10 CFR 50 Appendix B quality programme,
at a fixed price below the incumbents, faster, with a schedule bonus where the plant can use the
months. Its moat is the graph of each plant it has worked on: the second job at a plant costs a
fraction of the first, and the incumbents' billing model (hours) punishes them for copying it.

**Expansion path**, all running on the same graph:
1. Uprates (2027-2032 peak): measurement-uncertainty recaptures first (engineering- and review-bound,
   small hardware), then stretch and extended uprates.
2. Subsequent licence renewal to 80 years (Vistra is pursuing it for all three of its Meta plants;
   most of the US fleet follows).
3. Digital I&C modernisation (about 160 planned upgrades across the fleet; Limerick's $167M retrofit
   was approved in January 2026) and restarts.
4. New build: start every new unit with a live design basis instead of reconstructing one later, and
   close ITAAC and quality records from it (links to the manufacturing gap in `PICK3.md`).
5. Non-US fleets: Canada (Bruce A is adding 125 MW), Finland, Czech Republic, Sweden, Korea.

## Why now

- **Buyers with money.** Hyperscalers fund uprates through PPAs and tariffs (Google-Georgia Power NU-1).
  Uprate capex runs at $3,800-4,800/kW in real 2026 deals, so engineering sits inside multi-hundred-
  million-dollar budgets.
- **A dated peak.** NRC's own list puts 875 MWe of uprate applications in 2027 and 635 in 2028, with
  review targets cut to 6, 9 and 12 months. If review gets faster, utility-side engineering becomes
  the critical path.
- **The technology just arrived.** Models can now read scanned engineering documents reliably enough
  to extract structured headers; the NRC itself reports a review type cut from about four years to
  nine months with AI. The applicant side has not caught up.
- **Scarce engineers.** DOE's advisory board says the nuclear workforce must triple or quadruple. The
  only way to deliver the 2027-2030 wave is more output per engineer.

## What the models say (`designs/margin/`)

**1. The prototype engine (`engine.py` on `plantx_calcs.txt`).** A synthetic but realistically formatted
index of 23 calculations of record for a 3,411 MWt four-loop PWR. The engine parses it, builds the
parameter-to-calculation graph and produces the two artefacts an uprate team spends its first months
on. Examples (full reports in `report_mur.md`, `report_stretch7.md`):
- A change to decay heat reaches 9 of 23 calcs, including the equipment-qualification profile four
  links away (decay heat, to LOCA mass and energy, to containment temperature, to EQ). This is the
  kind of indirect impact hand scoping misses.
- Cutting calorimetric uncertainty from 2 % to 0.4 % (an ultrasonic flow meter) returns 1.6 % of power
  to the 14 safety analyses that carry it and nothing to balance-of-plant equipment, so a 1.6 %
  recapture passes every limit with no hardware.
- On Plant X the generator binds first at 3.8 %, then the HP turbine (4.5 %), main transformer (5.6 %)
  and condensate pumps (6.0 %); the safety-analysis ceiling is about 9-10 %, and modern LOCA and DNB
  methods push the LOCA limit from 12 % to 23 %. In other words: on this plant the megawatts are
  locked behind long-lead balance-of-plant hardware, which is why the margin map has to come first,
  so the generator and transformer are ordered while the analysis runs.

**2. The schedule model (`impact.py`).** A 31-node graph of the analyses an extended uprate must cover
(heat balance through NSSS, core, transients, LOCA, containment, EQ, dose, BOP, setpoints, PRA, tech
specs, UFSAR, licence package), with owners (vendor, architect-engineer, utility), Monte Carlo
durations, and the failure mode that drives overruns: an affected analysis that is not scoped up
front is found late (at licence-package assembly or as an NRC question) and forces rework downstream.
Today's scoping is assumed to miss 12 % of analyses; the engine 2 % (an engine that only half works:
6 %). Calibrated so a clean EPU analysis takes about 19-21 months, near Columbia's 18. Output is only
counted when it can actually reach the grid: at the first refuelling outage after both NRC approval
and hardware arrival.

| Uprate (MW, hardware lead) | Analysis P50 / P90 today | With engine | Output earlier | Value at $85/MWh | Weak engine |
|---|---|---|---|---|---|
| MUR (17 MW, 12 mo) | 7.5 / 11.9 mo | 4.7 / 5.4 mo | 6.4 mo | $6M | $4M |
| Stretch (40 MW, 18 mo) | 12.9 / 20.5 mo | 8.0 / 9.4 mo | 9.0 mo | $21M | $12M |
| EPU (160 MW, 24 mo) | 21.4 / 33.8 mo | 13.4 / 15.6 mo | 13.7 mo | $126M | $70M |
| EPU (160 MW, 42 mo turbine) | 21.5 / 34.2 mo | 13.5 / 15.7 mo | 2.9 mo | $27M | $25M |

Two findings matter for the pitch:
- **The tail is the product.** The engine cuts the median analysis time by about a third but the P90
  by more than half, because it removes late-found scope. Utilities plan to P90.
- **Engineering only pays when it is on the critical path.** Where a new turbine with a 42-month lead
  binds, faster engineering is worth a tenth as much. So the sales motion starts with the margin map
  (which tells the owner what to order first) and with MURs and pump-and-heat-exchanger EPUs.
- Engineering effort falls 22-44 % on uprate scope alone, before reuse of the plant's graph on the
  next job.

**3. The firm model (`firm.py`).** Addressable engineering for operating fleets is about $1.1-1.9B a year
in the US (12-20 % of $7.59B fleet capex plus outsourced design-basis work; the shares are
assumptions) and about $2.3-3.8B including accessible non-US fleets, plus new-build engineering from
2030. Taking 4 % of that by 2031 and 7 % by 2033 (base case) gives **about $180M of revenue in 2032 and
$255M in 2033 with about 800 engineers**; the bull case (11 %, higher pool) reaches **$440M in 2032 and
$575M in 2033**; the bear case $130M in 2033. A schedule bonus at 5 % of value adds only $1-7M a year,
so this is a fee business: the case for scale is share of a $3-5B engineering market, which is how
Enercon became a $1B-plus company with no software at all.

## Competition

| Who | What they do | Why it is not this |
|---|---|---|
| Sargent & Lundy, Enercon (+Pond, ~2,700 staff), Jensen Hughes, Zachry | The architect-engineers that do uprate, renewal and modification engineering today | Bill by the hour; no AI engineering announced; being consolidated by PE |
| Westinghouse, Framatome, GE Vernova/GNF | NSSS and fuel safety analyses on their approved codes; bertha embedded in Westinghouse's CMIS | Own the vendor critical path; we partner on LOCA/transients and take everything else |
| Nuclearn ($10.5M A) | CAP, procedures, work packages, 50.59 screening feature, design-mod review "in development" | Software sold to sites; closest to moving into engineering, watch closely |
| Atomic Canyon (NVIDIA-backed) | Search and operating-experience assistant, fleetwide via INPO/EPRI/NEI | Search, not engineering |
| Everstar, Inductive | Licence application drafting, mostly new reactors | Documents for new designs, not a plant's calculations of record |
| Alva Energy ($33M A) | Turnkey uprate developer: steam generators and a second turbine, 10 GWe goal | A customer or partner: it needs exactly this engineering |

## Weak points

- **It is a services company first.** It needs licensed engineers, an Appendix B / NQA-1 quality
  programme and a NUPIC-audited place on utility supplier lists before it can sign safety-related
  work. That is 6-12 months and the reason to start with non-safety scoping and margin maps.
- **The vendors own part of the critical path.** LOCA and transient analyses run on vendor codes. The
  firm starts as the integrator and architect-engineer and earns the right to run safety analyses
  later (or licenses codes such as RELAP5-3D or TRACE-based methods).
- **Data access.** Calculations are utility property, held on site, some export-controlled. The graph
  must run on premises and the utility keeps it; the moat is the team's speed and method, not
  possession of the data.
- **The key model inputs are assumptions.** The 12 % miss rate and the speed factors drive the value.
  They are testable from public NRC records before anyone builds anything (plan below).
- **Engineering shares of capex are not published.** The market size rests on assumed 12-20 %; the
  calls in the plan check it.
- **Incumbents can adopt AI.** Enercon's new owners have the money to try. The bet is that an hours-based
  firm will not cannibalise its billing, as in every other AI-native services category.

## Considered and ranked lower

- **Decommissioning characterisation and waste classification** (geostatistics on sparse samples to
  put waste in the cheapest legal class). Best fit with the team and nobody venture-backed doing it,
  but the buyers are DOE EM ($8.2-8.6B a year) and the UK NDA through big contractors, and software
  gets small contracts. Kept as a second product on the same graph and spatial-inference stack.
- **Remote operations for microreactors** (the Control Room idea from `PICK5.md`, re-aimed). NRC's
  proposed Part 57 would allow remote and autonomous operation, but the rule is not final, fleets are
  unlikely before about 2030, and vendors treat autonomy as core intellectual property.
- **Online monitoring to extend calibration intervals**: AMS and EPRI own the approved path; about 90
  US units cap it.
- **ML fuel qualification**: Oklo, NVIDIA and LANL; X-energy, INL and AWS; about 10 buyers building in house.
- Search, CAP screening, procedures, outage schedule risk and new-build licence drafting: occupied.

## Eight-week plan

| Week | Do | Evidence it produces |
|---|---|---|
| 1-3 | Pull every uprate licence amendment since 2000 from NRC ADAMS (about 100 EPUs and MURs) with their requests for additional information and supplements; classify which questions came from missed or inconsistent impacts and how much time they added | The real miss rate and delay that `impact.py` assumes (12 %); the first dataset no competitor has |
| 1-4 | Extract parameters, results and limits from public UFSAR chapters 6 and 15 of three plants into the engine format; score against hand labels | Extraction precision and recall on real documents; a real margin map for a real plant |
| 2-6 | 15 calls: uprate managers at Constellation, Vistra, Duke, Southern, Energy Northwest, Entergy; Sargent & Lundy and Enercon project leads; Alva | Where uprate schedules actually slip, what scoping costs, the engineering share of capex, willingness to buy fixed-price packages |
| 4-8 | Offer a paid scoping pilot on one MUR: affected-calculation list and margin map in four weeks, against the utility's own scope | A first contract, and a head-to-head count of impacts found |
| 4-8 | Draft the Appendix B quality programme; hire one senior licensed nuclear engineer with uprate experience | The path to safety-related work |

## Kill criteria

- The ADAMS history shows that missed or inconsistent impacts explain under about 5 % of uprate
  review delay, and the speed gain alone does not move projects into an earlier outage.
- Most utilities say hardware lead time, not engineering, sets their uprate date.
- Extraction recall on real UFSAR tables stays under about 90 % after four weeks.
- No utility or uprate developer will pay for a pilot within six months.

## Sources

Full list with URLs in `ml_software_notes.md`. Key ones:
- Google-Constellation 890 MW uprates: https://www.powermag.com/google-deal-backs-890-mw-of-constellation-nuclear-uprates-at-11-pjm-reactors/
- Meta-Vistra uprates and renewal: https://www.ans.org/news/2026-01-12/article-7668/the-metavistra-deal-a-closer-look/
- NRC expected uprate applications: https://www.nrc.gov/reactors/operating/licensing/power-uprates/status-power-apps/expected-applications
- DOE UPRISE and engineering bottleneck: https://www.powermag.com/doe-unveils-initiative-to-add-5-gw-of-nuclear-capacity-through-uprates-and-restarts/
- Columbia EPU, 18 months of analysis: https://www.power-eng.com/nuclear/washington-state-nuclear-plant-approved-for-700m-upgrade-to-boost-output/
- INL uprate costs: https://lwrs.inl.gov/content/uploads/11/2025/04/26_Larger-Power-Uprates_rev1.pdf
- Enercon sale: https://www.energyconnects.com/news/utilities/2026/april/arlington-capital-acquires-nuclear-engineering-firm-enercon/
- Alva Energy: https://www.powermag.com/nuclear-power-group-alva-energy-launches-with-33-million-in-funding/
- Nuclearn 50.59 feature: https://nuclearn.ai/2025/08/04/confident-engineering-starts-here-inside-nuclearns-50-59-feature/
- Atomic Canyon NIVA: https://atomic-canyon.com/news/2026-08-18-niva-fleetwide-launch/
- NEI Costs in Context 2026: https://www.nei.org/getContentAsset/47fa8caa-9b0d-4029-932c-07f902e82f4f/8d8ff8d6-b2ae-401b-a63c-f6b108e809d2/2024-Costs-in-Context-final.pdf
