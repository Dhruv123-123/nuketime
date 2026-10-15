"""HAFNIUM: how much revenue can a new Western hafnium producer earn before it crashes the price?

Constant-elasticity demand calibrated on sourced points (see research/converge/PICK4.md): Western
market ~110 t/yr at ~$13k/kg (Apr 2026, under China's export controls); ~130 t/yr at ~$5k/kg without
them. Long-run floor where dehafniating non-nuclear zirconium pays: ~$2.75k/kg (CPM/MMTA $2.5-3k).
Below the floor nobody adds supply, so an entrant can sell at most what demand absorbs at the floor.
'rivals' is other new supply reaching the same market (Framatome +15 t, Daiichi Kigenso from 2028,
ATI/Westinghouse expansions, any leak of China's ~110 t Liaoning Huaxiang/Sanxiang output).
"""
FLOOR = 2750.0


def demand_q(p, q0, p0, eps):
    return q0 * (p / p0) ** eps


def price(total_new, q0, p0, eps):
    return p0 * ((q0 + total_new) / q0) ** (1.0 / eps)


def entrant_revenue(q, rivals, q0, p0, eps):
    p = price(q + rivals, q0, p0, eps)
    if p < FLOOR:
        p = FLOOR
        q = max(0.0, demand_q(FLOOR, q0, p0, eps) - q0 - rivals)
    return q, p, q * 1000 * p


if __name__ == "__main__":
    for label, q0, p0 in (("export controls hold", 110, 13000), ("controls relaxed", 130, 5000)):
        for rivals in (0, 40):
            for eps in (-0.3, -0.5):  # small cost share in chips and turbines: inelastic
                best = max((entrant_revenue(q, rivals, q0, p0, eps) for q in range(5, 301, 5)), key=lambda t: t[2])
                print(f"{label:21s} rivals +{rivals:2d} t  elasticity {eps}: best {best[0]:.0f} t at "
                      f"${best[1]/1e3:.1f}k/kg = ${best[2]/1e6:.0f}M/yr")
