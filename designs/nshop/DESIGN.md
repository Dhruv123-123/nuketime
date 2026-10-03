# NSHOP: when do nuclear-qualified parts become the bottleneck?

A small model built to test the third pick (`research/converge/PICK3.md`): a contract manufacturer
that holds the nuclear quality certifications and turns ordinary precision shops into qualified
capacity. It asks how lead times for safety-related machined, welded and inspected parts behave as
reactor builds ramp, and what adding qualified capacity faster is worth to the projects waiting on
it. It is an illustration of the mechanism with labelled assumptions, not a forecast.

## Sourced inputs

- US holders of ASME nuclear ("N") stamps fell from about 500 in the 1970s and 80s to about 100
  ([Power Engineering, 2009](https://www.power-eng.com/nuclear/stamp-of-approval/)). Fluor took
  about 20 months and an experienced firm about $1M to get one.
- Machining, welding, finishing, inspection and NDE "frequently sit on the critical path"; heavy
  manufacturing often has "two to five" qualified firms; suppliers will not add capacity without
  firm multi-unit orders ([Nuclear Scaling Initiative, March 2026](https://www.nuclearscaling.org/wp-content/uploads/2026/03/2026-Landscape-of-U.S.-Domestic-Advanced-Nuclear-Energy-Supply-Chain.pdf)).
- Vogtle 3 and 4 slipped 3 to 6 months at a cost of $920M because "tens of thousands" of quality
  documents were missing ([E&E News, February 2022](https://www.eenews.net/articles/plant-vogtle-hits-new-delays-costs-surge-near-30b/)),
  about $75M to $155M per unit-month.

## The model (`queue.py`, `runs/queue.json`)

- Qualified capacity is c "cells" (one qualified machine-and-crew line for a year), 100 in 2026,
  growing 3 % a year, plus new stamp holders who enter two years after demand shows up and close
  half the gap to 80 % utilisation.
- Demand is 60 cell-years a year for the operating fleet, plus 40 cell-years per large unit over four
  years and 10 per SMR over three. Three build scenarios run to 2036: low (one large unit a year from
  2029, up to 4 SMRs a year), base (two large a year, up to 10 SMRs) and high (four large a year, up to
  15 SMRs, near DOE's goal of 10 large units under construction by 2030).
- Lead time each month is a 3-month job, plus the Erlang C queue wait at that utilisation, plus any
  backlog worked off at the capacity rate.
- A project is delayed by a quarter of the worst excess lead time it meets during its build, at
  $100M per large-unit month and $15M per SMR-month.

## Results

| Scenario | Peak lead time | With +10 qualified cells a year from 2028 | Delay cost avoided, 2027 to 2036 |
|---|---|---|---|
| Low | 4.5 months | 3.0 | $0.3B |
| Base | 16.6 months (2034) | 4.9 | $7.3B |
| High | 28.6 months (2032) | 17.5 | $14.2B |

Sensitivity in the base scenario:

| Assumption moved | Peak lead time | With +10 cells a year | Avoided |
|---|---|---|---|
| As set | 16.6 | 4.9 | $7.3B |
| Existing capacity x1.5 | 7.2 | 3.0 | $2.2B |
| Existing capacity x2 | 3.1 | 3.0 | $0.0B |
| Work per unit x0.5 | 5.6 | 3.0 | $1.2B |
| Work per unit x2 | 29.8 | 17.8 | $7.8B |
| New entrants take 1 year | 6.2 | 3.0 | $1.4B |
| New entrants take 3 years | 27.4 | 8.3 | $11.6B |

## What it says

- Lead times stay flat until qualified shops are about 90 % busy, then build a backlog that takes
  years to clear, because new stamp holders arrive two years late. That is the "market paralysis"
  the NSI report describes, as a queue.
- Whenever the crunch happens, qualifying capacity in months instead of two years is worth billions
  to the projects, far more than the parts themselves cost.
- Everything hinges on one ratio: real build demand against today's idle qualified capacity. If US
  shops have twice the spare capacity assumed here, there is no crunch. That ratio is the first thing
  the validation plan measures (ASME's public certificate-holder directory, and lead-time quotes from
  reactor vendors).
