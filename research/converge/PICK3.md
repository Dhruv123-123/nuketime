# The third pick: size first

Written 3 October 2026. The TRISO sorter (`PICK2.md`) was rejected as too niche: even after
expanding to every advanced fuel, it tops out around $100M to $200M a year because there are only
twenty or so fuel lines to sell to. So this round used size as the first filter, discarding
anything whose buyer pool caps it under about $300M a year, and still excluded prospecting,
exploration and drilling. Sourced notes: `big_nuclear_notes.md` and `big_energy_notes.md` in this
folder. Model: `designs/nshop/`.

## The answer

**Become the nuclear-qualified manufacturer the buildout is short of: a contract manufacturer that
holds the nuclear quality certifications (ASME Section III, NQA-1) centrally, qualifies ordinary
precision shops into its network in months rather than years, and sells finished, fully documented
safety-related parts to reactor builders and the operating fleet.**

The short version is Hadrian for nuclear, with the quality-records engine as the moat. Software
enforces the travelers, material certificates, inspection data and data reports for every part, so
the records are complete by construction. This is the step the earlier niche ideas (the shop
quality copilot, the TRISO sorter) were small pieces of: instead of selling quality tools to the
people who make nuclear parts, make the parts.

## Why this one

1. **The bottleneck is named and sourced.** The Nuclear Scaling Initiative's March 2026
   supply-chain report says machining, welding, finishing, inspection and NDE "frequently sit on the
   critical path", that heavy manufacturing often has "two to five" qualified firms, and that
   suppliers will not add capacity without firm multi-unit orders.
2. **The supplier base shrank five-fold.** About 500 US companies held nuclear stamps in the 1970s and
   80s; about 100 did by 2009. Getting one took Fluor about 20 months (Power Engineering, 2009).
3. **Quality records are what actually delays plants.** Vogtle 3 and 4 slipped 3 to 6 months at a
   cost of $920M because "tens of thousands" of quality documents were missing (E&E News, 2022).
   That is $75M to $155M per unit-month.
4. **The ceiling is large.** Equipment and engineering ran about $2,971/kW at Vogtle (MIT, 2022),
   roughly $3.3B per AP1000. The October 2026 US–Korea framework targets $120B for eight large units,
   on top of SMR programmes and spares for 94 operating reactors. A 10 % share of the component work
   is a $1B-a-year business.
5. **It is open.** Hadrian (aerospace, defence and shipbuilding; reported $1.37B raised at about $8B
   in August 2026) does not do nuclear. Path Robotics works in shipyards. The nuclear incumbents
   (Curtiss-Wright, BWXT, Flowserve, Framatome) are capacity-constrained themselves.
6. **It earns money now, not in 2030.** The operating fleet already buys obsolete spares through
   commercial-grade dedication, so the first revenue does not wait for new reactors.

## How the candidates scored

Scores are 1 (weak) to 5 (strong).

| Candidate | Ceiling | Open | Proof by Nov | Nuclear | Verdict |
|---|---|---|---|---|---|
| **Nuclear-qualified contract manufacturer (the pick)** | 5 | 4 | 3 | 5 | Pick |
| Self-performing nuclear construction subcontractor (automated welding crews) | 5 | 3 | 2 | 5 | Strong, but contractors won't hand safety work to a newcomer first; a later product line |
| Recertified high-voltage equipment bank (transformers, breakers) for data centres | 4 | 2 | 4 | 2 | Sunbelt Solomon already remanufactures substation units up to 85 MVA and 230 kV |
| Licensed operator for non-utility reactor owners | 5 | 3 | 1 | 5 | No revenue before about 2030; Constellation and Vistra will compete |
| Modular uranium conversion | 4 | 2 | 1 | 5 | Commodity chemistry, $0.5B to $1B plant; UEC and FluxPoint already in |
| Heavy components without giant forgings (powder metal and EB welding) | 4 | 4 | 1 | 5 | Code approval unfinished; capital-heavy |
| Collateral desk for large-load tariffs | 4 | 4 | 3 | 1 | Correlated defaults; barely nuclear |
| TRISO sorter (second pick) | 2 | 5 | 4 | 5 | Too niche |

## The prototype test (`designs/nshop/`)

A queueing model of US qualified capacity against three build scenarios to 2036, with labelled
assumptions for capacity and work per unit. In the base case (two large units and up to ten SMRs a
year), qualified shops pass 90 % utilisation around 2029 and peak lead times reach about 17 months
by 2034, because new stamp holders arrive two years after the demand. Adding ten qualified cells a
year from 2028 holds the peak to about 5 months and avoids about $7B of project delay over the
decade (about $14B in the high case).

The model's honest lesson is that everything hinges on one ratio: real build demand against today's
idle qualified capacity. If US shops have twice the spare capacity assumed, there is no crunch.
Measuring that ratio is the first job of the validation plan.

## Company brief

**Product.** Finished, documented nuclear parts with a guaranteed lead time, in three steps:
1. *Now:* commercial-grade dedication and reverse-engineered obsolete spares for operating plants,
   plus non-safety and "augmented quality" parts for SMR vendors. This needs an NQA-1 programme
   (Appendix B) and buyer audits, not an N-stamp, so it starts this year.
2. *From about 2028:* ASME Section III parts (supports, piping spools, valve bodies, internals,
   skids) once the company's own certificate is in place, routed to network shops it has qualified
   under its programme.
3. *Then:* its own automated cells for the part families with steady volume, Hadrian-style.

**The moat.** A quality system that is software, not binders: every part's travel record, material
certificates, inspection results and code data report are generated and checked as it is made. That
is what lets the company bring a shop in fast, and what Vogtle was missing.

**Business model.** Margin on parts, priced on lead time. Nuclear parts carry a premium over the
same part sold commercially, mostly for the paperwork and audits; the company's cost advantage is
doing that paperwork in software across many shops.

**Competition.** Incumbent nuclear manufacturers are full. Hadrian is the most likely entrant, and
Oklo sits with Hadrian in an industrial alliance, so speed to the first nuclear programme and the
first buyer audits matters. Reactor vendors such as Valar may make some parts themselves.

**Risks.**
1. There may be no crunch if build demand stalls or idle capacity is larger than assumed. Test: a
   capacity census and vendor lead-time quotes.
2. The certificate holder is liable for its network shops, and buyers audit the actual shop. The
   "virtual" model may need owned factories sooner. Mitigation: own the highest-risk steps (final
   inspection, NDE, records) from day one.
3. Qualification takes about 20 months for an N-stamp. Mitigation: start with dedication and
   augmented-quality work that does not need one.
4. Hadrian enters nuclear. Mitigation: be first to the audits and programmes.
5. Services-style margins. Mitigation: price on lead time; automate the records.

## Eight-week validation plan

| Week | Do | Evidence it produces |
|---|---|---|
| 1 to 2 | Census of ASME nuclear certificate holders by scope (ASME's public directory), plus NUPIC and utility approved-supplier lists | Today's qualified base by part family, against the model's assumption |
| 1 to 4 | Lead-time and backlog calls with reactor vendors and utility supply chains (below) | Real lead times and which part families are already late |
| 2 to 5 | Sign three non-nuclear precision shops (aerospace AS9100 shops near the SMR sites) as network members | A network ready to audit |
| 3 to 6 | Write the NQA-1 programme with records software; book a consultant gap assessment | A programme a buyer can audit |
| 4 to 8 | Win one dedicated obsolete spare or augmented-quality part order and deliver it | First revenue and a delivered lead time against the incumbent's quote |
| 6 to 8 | Re-run the queue model with census and call data | Whether, when and for which parts the crunch comes |

**Who to call, and what each call must answer.**

| Who | The call must answer |
|---|---|
| GE Vernova Hitachi (BWRX-300, Darlington and TVA) | Which part families have the longest lead times, and would they audit a new supplier? |
| X-energy (Long Mott) and Kairos (Hermes) | Same, plus what they make in-house |
| TerraPower (Kemmerer) | Same, for sodium-reactor parts |
| Westinghouse (AP1000 programme) | Supplier qualification timeline for the new AP1000 fleet |
| Valar, Aalo, Radiant | Will fast-moving vendors buy from a network instead of building their own shop? |
| Two utility supply-chain heads (Constellation, Duke or Southern) | Obsolete-spares backlog, dedication cost and lead time today |
| Two AS9100 aerospace shops | Would they join a nuclear network, and on what terms? |
| An NQA-1 or Section III consultant | Realistic time and cost to a programme and a stamp |

**Kill criteria.**
- The census and calls show qualified capacity is not the binding constraint for any common part
  family (lead times under about 6 months across the board).
- No reactor vendor or utility will audit a new supplier within a year.
- No first order can be won in eight weeks even for dedicated spares.

If the first holds but buyers report record and inspection delays rather than capacity, fall back to
the records engine sold to the existing incumbents.
