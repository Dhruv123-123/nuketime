"""How big can an AI-native nuclear engineering firm get, and what does it need to win?

Top-down pool from sourced fleet spend, a share ramp, and two pricing levers: fixed-price work
delivered with fewer engineer-hours, and a schedule bonus on uprates paid from megawatts brought
online earlier (impact.py). Every non-sourced number is an assumption and labelled.

Sourced:
- US fleet capex $7.59B in 2025, opex $20.82/MWh on ~780 TWh (NEI Costs in Context, Aug 2026).
- US uprate pipeline 2026-2032: 19 EPU, 2 SPU, 10 MUR, ~2,421 MWe (NRC, Sep 2026); Google-
  Constellation 890 MW and Meta-Vistra 433 MW sit partly outside that list.
- Enercon sold a majority stake on ~$1.25B of equity (Apr 2026), merging into a 2,700+ person firm.
"""
import json

US_CAPEX = 7.59e9
US_OPEX = 20.82 * 780e6                      # $/MWh x MWh
ENG_SHARE_CAPEX = (0.12, 0.20)               # engineering+licensing share of capital projects (assumption)
ENG_SHARE_OPEX = (0.04, 0.07)                # design-basis upkeep, calcs, 50.59, operability (assumption)
OUTSOURCED_OPEX = 0.35                       # share of opex engineering that utilities buy outside (assumption)
INTL_MULT = 1.0                              # accessible non-US fleets (Canada, Europe, Korea, Japan) vs US,
                                             # ~2x the GW, halved for access and language (assumption)
NEW_BUILD_2032 = 1.0e9                       # owner's and A/E engineering for new units by 2032 (assumption)

REV_PER_ENGINEER_INCUMBENT = 200e3           # $/engineer-year at an incumbent A/E (assumption)
PRODUCTIVITY = (1.8, 2.5)                    # AI-native output per engineer vs incumbent; impact.py gives
                                             # 0.22-0.44 fewer hours on uprate scope (1.3-1.8x) before the
                                             # cross-project reuse of a plant's graph (assumption above that)
PRICE_DISCOUNT = 0.15                        # undercut incumbents on fixed price (assumption)

# Uprate schedule bonus: impact.py says $70-126M of earlier output per 160 MW EPU when hardware does
# not bind, ~$25M when it does. Firm takes a 5% bonus of that value (assumption).
EPU_VALUE = {"low": 0.5 * (69.5 + 24.5), "high": 0.5 * (126.4 + 27.1)}   # $M per 160 MW EPU, half hw-bound
BONUS_SHARE = 0.05
EPU_PER_YEAR = 5                             # US+Canada EPU-equivalents reaching analysis each year (assumption)

YEARS = list(range(2027, 2034))
SHARE = {"bear": [0.000, 0.002, 0.006, 0.012, 0.020, 0.028, 0.035],
         "base": [0.000, 0.004, 0.012, 0.025, 0.040, 0.055, 0.070],
         "bull": [0.001, 0.008, 0.020, 0.040, 0.065, 0.090, 0.110]}
EPU_SHARE = {"bear": 0.10, "base": 0.20, "bull": 0.35}  # share of EPUs the firm engineers by 2030+


def pool(lo_hi):
    i = 0 if lo_hi == "low" else 1
    us = US_CAPEX * ENG_SHARE_CAPEX[i] + US_OPEX * ENG_SHARE_OPEX[i] * OUTSOURCED_OPEX
    return us, us * (1 + INTL_MULT)


def run():
    out = {}
    for case, lohi in (("bear", "low"), ("base", "low"), ("bull", "high")):
        us, fleet = pool(lohi)
        rows = []
        for k, y in enumerate(YEARS):
            addressable = fleet + (NEW_BUILD_2032 * max(0, (y - 2029)) / 3 if y >= 2030 else 0)
            fee = addressable * SHARE[case][k]
            bonus = EPU_PER_YEAR * EPU_SHARE[case] * min(1, (k + 1) / 4) * EPU_VALUE[lohi] * 1e6 * BONUS_SHARE
            rev = fee + bonus
            prod = PRODUCTIVITY[0] if case != "bull" else PRODUCTIVITY[1]
            heads = fee / (REV_PER_ENGINEER_INCUMBENT * (1 - PRICE_DISCOUNT) * prod)
            rows.append(dict(year=y, addressable_B=round(addressable / 1e9, 2),
                             fee_M=round(fee / 1e6), bonus_M=round(bonus / 1e6),
                             revenue_M=round(rev / 1e6), engineers=round(heads)))
        out[case] = dict(us_pool_B=round(us / 1e9, 2), fleet_pool_B=round(fleet / 1e9, 2), years=rows)
    return out


if __name__ == "__main__":
    print(json.dumps(run(), indent=1))
