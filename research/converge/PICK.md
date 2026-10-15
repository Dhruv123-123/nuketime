# The pick: one company out of everything in this repo

Written 1 October 2026, to turn the breadth of this repo (11 stress-tested ideas, 23 moonshots,
three designs, a 59-step vertical map and the Analogue Atlas) into one company with a plan to
prove it. Evidence is in `exploration_market.md` and `isr_wedges.md` beside this file (every
number sourced and dated), and in `designs/wellfield/`, a model built to test the leading idea.

## The answer

**Find the uranium that US ISR plants can actually produce, starting with the pounds their own
historic logs missed.**

The company re-reads roll-front drill logs with ML, correcting gamma logs for disequilibrium and
mapping the roll front's geometry and leachability. It hands each in-situ recovery (ISR) operator
pounds inside the boundaries it already holds, paid as a royalty on production. Then it uses the
same engine on district-scale public logs to stake and option out its own ground. The founder's
existing ML prospecting work is the engine; the twist is aiming it at producible pounds next to
plants that are running below nameplate, not at discovery in general.

## How the candidates scored

Scores are 1 (weak) to 5 (strong). *Fit* is fit to a team that already ships ML for uranium
prospecting. *Open* is the absence of funded competitors. *Proof by Nov* is how much of the case
the founder could prove in eight weeks.

| Candidate | Fit | Pain evidence | Open | Proof by Nov | Ceiling | Verdict |
|---|---|---|---|---|---|---|
| **Producible-pounds generator for US ISR (the pick)** | 5 | 5 | 4 | 4 | 4 | Pick |
| AI uranium prospect generator, general | 5 | 4 | 2 | 3 | 5 | Same engine, but Terranox (YC W26) pitches exactly this |
| ISR wellfield operations software | 3 | 4 | 5 | 2 | 2 | No: the model says 3 to 5 % gains, about 7 Western buyers |
| Drill-targeting SaaS for juniors | 4 | 3 | 1 | 4 | 2 | No: Terra AI ($20M, Khosla, BHP), VRIFY, Fleet; software exits are C$30M to A$60M |
| Log-to-grade product alone | 4 | 3 | 4 | 4 | 1 | A feature: the US PFN logging fleet sold for $3.1M |
| Supplier qualification network (`RESEARCH.md` pick) | 1 | 5 | 4 | 3 | 3 | Strong idea for a different team |
| Machine-readable safety case (map #1) | 2 | 4 | 2 | 2 | 5 | Crowded by licensing genAI and the NRC's own tools |
| Outage emergent-work prediction (map #6) | 2 | 4 | 3 | 1 | 3 | Needs utility data you do not have |
| Cavern Store, Lockstep, Rocksink | 1 | 3 | 4 | 1 | 4 | Hardware for a utility; years to first proof |

The ISR-software row is graded on a model built for this decision (`designs/wellfield/`). Over 24
simulated plants, monthly Bayesian re-fitting and marginal flow allocation added 2.8 % NPV (p10 -1
%, p90 +8 %). Simply raising the shut-in grade to 20 mg/L added 5.3 %, and an operator can do that
without software. Perfect knowledge of every pattern's pounds was worth 2.9 % at $90/lb. The
2025 to 2026 shortfalls were about wells drilled and flow delivered, not optimisation. That moved
the pick upstream, to which pounds get developed at all.

## Company brief

**Problem.** US uranium plants are short of feed, not capacity. Peninsula's Lance plant is
licensed for 2 Mlb a year and expects 0.5 to 0.6 Mlb in 2027 after withdrawing 2026 guidance on
wellfield flow. Alta Mesa's plant has a 2 Mlb nameplate configured for 1. enCore's Q1 2026 output
fell 32 % because new wellfields were late. The whole US produced about 1.09 Mlb a quarter in
2026. New pounds outside licensed areas take years: Burke Hollow took 11 years from permits to
first production.

**Insight.** The fastest pounds are the ones already inside licensed boundaries and already
drilled. Roll-front districts were drilled intensively in the 1970s and 80s and mostly logged with
total-count gamma, which misreads grade where uranium and its daughters
are out of equilibrium. enCore said so when it paid $3.1M for the only US PFN fleet: "without
accurate in-situ measurement of uranium, significant high-grade ore has been missed using
traditional downhole techniques." Alta Mesa's historic resource carried a 1.13 disequilibrium
factor. Wyoming's survey publishes scanned uranium logs; the USGS holds scanned AEC logs. We found no one re-reading
them with models at district scale.

**Product.**
1. A log engine: digitise scanned and paper gamma logs, correct them for disequilibrium using
   paired PFN or chemical assays, and output grade-thickness per hole with uncertainty.
2. A roll-front model: trace the front, its sand and its confinement across holes, and rank
   untested segments by producible pounds rather than contained pounds.
3. A pre-registered target list per operator, scored afterwards against their delineation drilling.

**Business model.** Operators pay nothing up front for a re-read of their own data. The company
takes a royalty of a few percent on production from pounds it identified. Revenue arrives when
those pounds are produced. Option payments from staked ground come sooner. Software fees are a
bridge only. Every operator engagement adds paired data (gamma, PFN, assays, production) that a
discovery-only competitor never sees. That data is the moat, and it turns into the
prospect-generator business: stake under-explored roll-front ground ranked by the same engine,
then option it to the producers who need feed for cash, shares, work commitments and a 1 to 2 %
net smelter return royalty. The template is Renaissance Gold's Silicon option: $3M plus 1 %,
later worth about C$421M.

**Why now.**
- Term price at a nominal record of $96.50/lb (Aug 2026).
- The Russian import ban's waivers end on 1 January 2028.
- A January 2026 Section 232 proclamation names uranium.
- Two new US ISR mines started in April 2026.
- UEC is running 38 rigs. Every US producer is buying drilling and needs pounds near its plants.

**Competition and the answer to "why not Terranox?"**
- Terranox (YC W26, two people, $1M) and VerAI pitch AI discovery and own projects.
- Earth AI and KoBold own ground in other metals.
- Terra AI, VRIFY and Fleet sell targeting.
- All of them start at discovery and are judged on hit rates nobody has yet published for
  uranium.
- This company starts inside producers' licences, is paid on production, and gets proprietary
  paired data as a result. Discovery comes second, with a buyer already attached.

**Risks.**
1. Operators may not share logs. Test: three conversations.
2. Missed pounds inside licences may be small. Test: a blind re-read on public logs.
3. Royalties on production pay late. Mitigate with option payments and paid re-reads.
4. Permitting still gates satellite deposits.
5. The uranium price.

## Eight-week validation plan

Each week has a deliverable that is evidence by itself.

| Week | Do | Evidence it produces |
|---|---|---|
| 1 | Pull Wyoming's scanned logs for one district (Powder River or Shirley Basin) and the USGS AEC scans; build the digitiser | A table of digitised holes, with error measured against a hand-picked sample |
| 2 | Disequilibrium correction, trained on any paired data you hold plus published factors | Corrected grade-thickness per hole with uncertainty |
| 3 | Blind backtest: hide every hole drilled after a cut-off year, trace the front from the earlier ones, rank segments | Share of later ore holes inside the top 10 % of ranked ground, against a distance-to-old-hole baseline |
| 4 | Publish a timestamped target list for that district | A pre-registered prediction, which no AI uranium company has shown |
| 2 to 6 | Ten conversations (list below) | One data-sharing pilot or LOI, and the real answer on logs and royalties |
| 5 to 6 | Re-read one operator's or junior's historic data under NDA | Pounds found inside their boundary, in their units |
| 7 to 8 | Stake the best open ground from week 3 if it is open and cheap | Ground, and a first option conversation |

**Who to call, and what each call must answer.**

| Who | Why them | The call must answer |
|---|---|---|
| UEC | Largest US ISR fleet, 38 rigs, holds acquired historic databases | Would they share old logs for a royalty on pounds found? |
| enCore | Owns the PFN fleet and the Alta Mesa disequilibrium data | Partner or competitor? Would they license paired PFN and gamma data? |
| Ur-Energy | Lost Creek and Shirley Basin, $195.6M of wellfield capex ahead | Where are they short of delineated pounds near the plant? |
| Peninsula | Lance has 2 Mlb a year of plant and under 0.6 Mlb of output | Is feed or flow the binding constraint? |
| Energy Fuels | Nichols Ranch on standby, deep historic Wyoming data | Would they vend historic data or ground? |
| Cameco US | Smith Ranch-Highland idle | What would restart require in pounds? |
| Premier American, Global Uranium, Indigo | Wyoming juniors compiling historic data now | Would they pay for a re-read today? |
| Skyharbour or CanAlaska | Prospect generators that know the option mechanics | What would they need to see to partner? |
| Wyoming State Geological Survey | Holds the scanned logs | Coverage, bulk access, gaps |

**Kill criteria.**
- The blind backtest does no better than the distance baseline.
- None of the ten will share logs on any terms.
- The pounds found inside licences are under about 5 % of a project's resource.

If any of these holds, fall back to the general prospect generator and compete with Terranox on
pre-registered results.
