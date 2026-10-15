# WELLFIELD: where software pays in an ISR uranium wellfield, and where it does not

A reduced-order model of in-situ recovery (ISR) uranium production, built to test one claim before
it goes into a pitch: that model-based closed-loop operation of ISR wellfields is worth a
venture-scale product. The answer from the model is no, not as an operating optimiser. The levers
it can pull are worth single-digit percent, and one of them a spreadsheet rule captures.

## The model

- `field.py`: one header house of sixteen 30 m five-spot patterns (25 injectors, 16 producers) on a
  3 m depth-averaged finite-volume grid with a 45 m buffer to a constant-head boundary. Each month
  it solves steady Darcy flow, then advances lixiviant and dissolved uranium by explicit upwind
  transport. Solid uranium dissolves at a rate proportional to lixiviant strength and to remaining
  ore (with a shrinking-surface factor); gangue consumes lixiviant. Permeability is a channelised
  lognormal field (sigma lnK 0.6 to 1.2), ore lies in a patchy roll-front arc, gangue is patchy.
  Injection is production less a 1 % bleed.
- Calibration: at 40 gpm per producer a typical header house peaks near 88 mg/L in month three,
  falls to about 20 mg/L by month eighteen and reaches about 72 to 80 % recovery in 24 months, in
  the range of Wyoming practice (Lance header house 14 at 50 to 60 mg/L; Wyoming decline curves of
  12 to 15 months to 80 % capture, versus about four months at Alta Mesa).
- `operate.py`: a plant of 1,200 gpm fed by six header houses that come online every five months,
  run for 36 months at $90/lb with $0.60/m3 variable cost and an 8 % discount rate. Each header
  house draws its leach kinetics, gangue, permeability and grade from wide priors. The operator
  sees only monthly flow and head grade per producer, plus a delineation estimate of each
  pattern's pounds with 35 % lognormal error.

## Policies compared (same data, same plant, 24 random plants)

| Policy | What it does | NPV vs baseline | Pounds vs baseline |
|---|---|---|---|
| Conventional | Plant at nameplate, flow split equally, shut in at the direct-cost cut-off (~3 mg/L) | 0 | 0 |
| Cut-off 10 mg/L | Same, higher shut-in grade | +2.8 % | +2.7 % |
| Cut-off 20 mg/L | Same, shut-in grade set by the opportunity cost of plant flow | **+5.3 %** (p10 +3.9, p90 +7.4) | +5.1 % |
| Cut-off 30 mg/L | Same | +5.1 % (p10 +2.2, p90 +8.6) | +4.7 % |
| Closed loop | Monthly Bayesian re-fit of a tank model per pattern, flow allocated to equalise marginal value | +2.8 % (p10 -1.0, p90 +7.7) | +2.5 % |
| Grade rank | Max rate to the richest patterns first | -15 to -20 % (4 plants) | |

Mean baseline NPV is $76.9M and 1.01 Mlb over 36 months. Results are in `runs/runs_sweep.json`.

Two further tests:

- **Pattern selection.** Over 2,400 simulated patterns at $90/lb, a $15.20/lb wellfield capex
  (Lost Creek's life-of-mine figure) and $21.27/lb opex, 19 % of patterns lose money. Perfect
  knowledge of every pattern's pounds raises wellfield value only 2.9 % over building them all;
  cutting grade error from 60 % to 25 % is worth about 1.5 %. At today's price the margin covers
  most mistakes.
- **Producibility.** Across 60 header houses run alone, 24-month recovery ranges from 55 % (p10)
  to 78 % (p90), and in this model it is explained by leach kinetics and gangue, not grade
  (`runs/runs_producibility.json`). The spread is an input assumption, so this test shows only
  that grade alone cannot rank producibility if real leachability varies this much.

## What it means

1. Flow allocation is nearly worthless. Equal splitting is close to optimal because recovery per
   cubic metre falls as a pattern is pushed harder; concentrating flow loses 15 to 20 %.
2. The one lever with money in it is when to retire a pattern, and it is a single number: the
   cut-off should be the grade a fresh pattern would deliver with the same plant flow, not the
   direct-cost break-even. Worth about 5 %, and an operator can apply it without software.
3. A model-based controller recovers about half of that, with a downside tail, because a pattern
   model fitted to monthly head grades is noisy early in a pattern's life.
4. So the 2025 to 2026 ISR shortfalls (Lance's flow rates and gassing, Lost Creek's flow, Kazakh
   acid and well-construction pace) are throughput and development-pace problems: wells drilled,
   completed and delivering flow. They are physical and operational, not optimisation problems.
   An ISR software company would be selling single-digit gains to about seven Western buyers.

The useful output for the company pick is negative: do not lead with wellfield operations
software. See `research/converge/PICK.md`.

## Limits

Two-dimensional, single-layer and steady flow each month; no gas lock, plugging or injectivity
decline; no excursion control or restoration; kinetics and gangue are generic. These omissions are
where operating problems actually live, so a product aimed at them would need a different model.
Gains of a few percent are within what better physics could move either way.
