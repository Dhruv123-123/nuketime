# The seventh hunt: datasets that exist only because a law forces disclosure

Written 13 October 2026, after Dhruv rejected Margin as "not plausible" and asked for "shit like this":
public datasets created by a law or quirk that forces private work into the open (his example is SMAD,
which Terranox uses to find uranium), on which ML could do something revolutionary. Constraints carried
forward: size is the first filter (a $100-200M a year market is too small); no Terranox clone; no
prospecting or drilling for resources. Raw output and every candidate: `research/forced/`. Claude Doc: https://claude.ai/code/artifact/a6157d9d-02d3-463c-93b4-234e30430d11

## How the hunt ran

Two rounds, 56 research agents, about 190 candidate regimes, 20 deep dives with adversarial checks.

- **Round 1**, 16 lanes: subsurface energy, mining beyond exploration, health and pharma, securities,
  grid and utilities, environment, property and land, transport, courts and patents, agriculture and
  water, insurance and labour, telecom and space, Asia and Latin America, European quirks, science
  archives, wildcards. 107 candidates, 12 deep dives.
- **Round 2**, 16 new lanes aimed at what round 1 missed: US healthcare arbitration, court-judgment
  publication abroad (China, India, Brazil, France), periodic inspection mandates (UK MOT, Dutch APK,
  Japanese bridges), loan-level securitisation disclosure, power markets that publish every bid (AEMO,
  ERCOT), patents as forced disclosure, public R&D final reports, infrastructure condition, data-sharing
  mandates (EU Data Act, AFIR, open banking), pay and tax disclosure, carbon and land registries, Korea
  and Japan transaction registers, bid-level procurement (ProZorro, state DOT bid tabs), trade-level
  finance, Africa, Middle East and Eastern Europe, and lateral oddities (EFSA studies, TTB labels).
  85 candidates, 8 deep dives.

Caveat: the shared web-search budget ran out partway through round 1, so some round-1 crowding checks
are from agent memory. Round 2 searched more sparingly and finished its checks.

## The finding that matters more than any single idea

**A forced-disclosure dataset almost never supports a large software company by itself.** All 20 deep
dives put the pure analytics market between about $10M and $400M a year. The reason is the same
everywhere. Because the data is public, incumbents in the buyer's workflow (LightBox for contamination,
S&P and Clearwater for insurer filings, Praedicat and Verisk for casualty, Fugro for ground models,
PatSnap for patents, HaloMD for surprise-billing arbitration) can see it too, and the buyers who care
most usually have better private data.

SMAD works for Terranox for a reason the other datasets mostly lack: the prediction is used to **take a
position** (stake ground, then own the discovery). The datasets that pass the size bar are the ones
where the model's edge can be used the same way: to underwrite, lend, buy claims or take on a
liability. So the hunt ranks ideas on three things: whether the law creates a real data edge with
outcome labels, whether a risk-taking business can sit on top, and whether nobody is already doing it.

## Ranked shortlist (both rounds)

| # | Idea | Forced-disclosure quirk | Verdict | $1B path |
|---|---|---|---|---|
| 1 | **End-of-life liability underwriter** (Alberta, then Saskatchewan, BC, US states) | AER licensing forces every well's status, production (Petrinex) and closure work into public; the Orphan Well Association publishes dated orphan labels; Directive 011 publishes the regulator's own deemed cost per well | Best mix of data edge, labels, timing and fit. Policy-dependent | Score, then closure-security bonds as an MGA, then taking inactive liabilities off producers for a fee |
| 2 | **Pollution-liability pricing** on California GeoTracker | ESI regulations force every responsible party to upload lab results (230M+ rows), boring logs and reports | Huge, rich data, but it only covers sites already suspected dirty (no clean negatives), and LightBox/EDR owns the lender channel | Pollution-legal-liability MGA; best as #1's second product |
| 3 | **Patent-validity underwriter** | Every PTAB challenge and decision is public (about 15k outcomes) | Clear risk product; USPTO's 2025 institution changes make old labels less reliable | Invalidity insurance and pricing for litigation funders and IP-backed lenders |
| 4 | **First-of-a-kind technology underwriter** | DOE, ARPA-E, EU CORDIS and SBIR rules force funded projects to publish final technical reports | Most original idea of the hunt, but awardees can strip out the numbers an underwriter needs, and the FOAK insurance market is about $100-300M of premium today | MGA, then a "Moody's for FOAK" rating |
| 5 | Florida condo structural and financial distress | Post-Surfside laws force milestone inspections and reserve studies, published as filed | Real money in special-assessment lending; Florida-only, under two years of outcomes | Association lending plus insurance and mortgage pricing |
| 6 | Korea jeonse deposit-default underwriter | Rent reporting enforced since June 2025 plus every sale price within 30 days | Strongest labels found; Korean licensing blocks a foreign founder | Private deposit guarantee as the state guarantor retreats |
| 7 | Mass-tort forecaster (PACER plus FAERS) | Public dockets plus mandatory adverse-event reporting | Real prediction problem; Praedicat proves buyers exist and that the market is small | Casualty reinsurance pricing with a capital partner |
| 8 | Hospital and nursing-home distress lender | Medicare cost reports (HCRIS) are a condition of payment and public | Good closure labels, Medicaid cuts as why-now; reports lag 1-2 years | Rescue and bridge lending |
| 9 | California wage-and-hour (PAGA) liability | Every PAGA notice and settlement filed with the state | Real data, but wages owed are uninsurable and the risk is adversely selected | Only as a feature of a national employment-practices MGA |
| 10 | Contract surety priced on DOT bid tabs | Every bidder's unit prices on public highway work are public | Bid tabs are a weak signal next to the work-in-progress schedules sureties already get | Implausible share needed |

**Killed after deep checks, and why** (so nobody re-pitches them): SBA loan-level lending (Lumos and
others), insurer Schedule P reserves (WTW, rating agencies), NAIC private-credit marks (paid data, S&P
and Clearwater already show it), surprise-billing arbitration (HaloMD and Daffodil hold the position;
politically volatile), Brazil court-ordered debt (2025 constitutional change), India bad-loan recovery
(only licensed ARCs may buy), UK MOT warranty pricing (MOT records the wrong failures), Dutch borehole
ground models (Fugro GroundIQ), standard-essential patents (PatSnap ships AI claim charts), FCC
teardown photos (shield cans hide the chips), OSHA injury logs (wrong accounts), vehicle recalls (the
predictive warranty counts stay confidential), municipal bond filings (crowded, small), EMA and Health
Canada dossiers (Health Canada's terms ban commercial use), power-market bid disclosure (Tesla
Autobidder, Habitat, Fluence already learn from it). Full table: `research/forced/candidates.md`.

## The pick: an end-of-life liability underwriter, starting with Alberta wells

**One line:** Alberta's official estimate of what it costs to close every oil and gas well is C$36.6B;
a leaked 2018 AER estimate said C$260B. Nobody can say, well by well, what closure will really cost or
who will be left holding it. The regulator's own data can.

**Why it is "SMAD-shaped" without being a Terranox clone.** The same law-created pattern: decades of
mandatory operator filings (licence holder, status changes, monthly production, inspections, closure
work), a public outcome label (the Orphan Well Association inventory names every orphaned well and its
former licensee), and a crude official benchmark to beat (the regulator's licensee rating and Directive
011 cost tables). The job is the one Dhruv's team already does: turning messy geoscience filings into a
calibrated prediction. But it finds nothing in the ground. It prices a liability.

**Why now.**
- Directive 088 forces industry to spend on closure every year (C$750M quota for 2026; about C$900M
  spent in 2024 against C$700M).
- The AER's 2024 consultation on its security framework proposes "risk-informed security determination"
  and "alternative forms of security (bonds, trusts)". The regulator is asking for the model that does
  not exist yet.
- No startup was found underwriting closure liability with ML. Data vendors (XI Technologies, Enverus,
  geoLOGIC) sell cost estimates for acquisitions but take no risk and do not model who ends up orphaned.

**How it becomes large.**
1. **Score** (about $10-30M revenue): per-well true closure cost and per-licensee orphan probability,
   sold to sureties, lenders and acquirers. Every licence transfer already triggers a regulator security
   decision. This layer exists to win distribution and collect real cost labels.
2. **Closure-security bonds as an MGA**, once Alberta accepts bonds as security, plus Saskatchewan, BC,
   US state bonding, mine reclamation and solar and wind decommissioning bonds. Securing 10-20 % of
   Alberta's C$36.6B at 1-3 % a year is C$70-220M of premium in Alberta alone (our estimate).
3. **Liability transfer**, the largest pool: take inactive wells off producers for a fee priced by the
   model and close them in batches below that fee. Alberta's inactive liability alone is C$23.4B.

**What could kill it** (stated plainly, because these are serious):
- **Boundary with your rule.** It is about oil and gas wells. It is end-of-life liability, not
  exploration or drilling, but if anything near oil wells is out, this pick is out and #2 to #4 move up.
- **Price is often set by statute, not risk.** Texas and most states use fixed blanket bonds, and
  Alberta mostly takes security deposits rather than market bonds. The MGA layer only opens where
  regulators move to risk-based security, which is proposed in Alberta but not decided.
- **The US catalyst is going backwards.** BLM's 2024 bonding rule is being repealed.
- **Capital.** An MGA needs a fronting carrier and reinsurance; layer 3 is a balance-sheet business.
- **Software alone tops out around $200-400M a year**, the size already rejected. The venture case
  depends on taking risk.

## The proof to run (one day, real data)

Question: does a model built only from public filings predict orphaning materially better than the
regulator's own licensee rating?

- **Data, all free:** AER ST37 well list (current plus archived monthly snapshots 2015-2024), Petrinex
  public monthly volumes, the Orphan Well Association inventory with designation dates, AER receivership
  and closure-order bulletins, historical licensee ratings (LMR, then LCA), Directive 011 cost tables.
- **Label:** the well is orphaned, or its licensee enters receivership or gets a closure order, within
  48 months.
- **Split by time:** train on 2015-2016 snapshots with outcomes to 2019; test on a December 2019
  snapshot with outcomes 2020-2024, which covers the 2020 receivership wave.
- **Features:** inactive share and its trend, months since last production, decline and water cut,
  age, depth, sour gas, region, licence transfers (asset dumping), compliance history.
- **Baselines:** the regulator's licensee rating; inactive share plus age.
- **Pass bar:** AUC at least 0.05 above the regulator's rating, the top decile capturing at least half
  of later-orphaned liability dollars, and a median lead time over 6 months. Fail any of these and the
  underwriting edge is not there.
- **Deliverable if it passes:** a league table of current licensees by orphan risk, to put in front of
  Canadian surety underwriters (Trisura, Intact) and the AER security-framework team.

**Status: not run.** This cloud environment's network policy blocks the AER, Petrinex and Orphan Well
Association hosts (and most government data hosts). No mirror was found on GitHub or other reachable
hosts. The proof runs once those hosts are allowed, or on any normal machine.

## If you want a different direction from this list

- **No oil and gas at all:** #2 (pollution liability on GeoTracker) has the same shape, with a harder
  labels problem; #3 (patent validity) is the cleanest risk product outside energy.
- **Most "revolutionary":** #4 (first-of-a-kind technology underwriter) would make bankable new
  energy and industrial technology faster, but its market is still forming.
