"""Run single header houses at design rate for 24 months and record how much of
the uranium in place each one actually gives up, against what is knowable from
drilling (grade) and what is not (permeability, gangue, leach kinetics)."""
import json, sys, numpy as np
from multiprocessing import Pool
from operate import new_header_house, PRICE, VAR_COST, DISC
from field import GPM, LB_PER_KG


def one(seed):
    rng = np.random.default_rng(seed)
    hh = new_header_house(np.random.default_rng(rng.integers(1 << 31)))
    q = np.full(16, 40 * GPM)
    kg = npv = 0.0
    for m in range(24):
        vol, k, _ = hh.step_month(q)
        kg += k.sum()
        npv += (k.sum() * LB_PER_KG * PRICE - vol.sum() * VAR_COST) / (1 + DISC) ** ((m + .5) / 12)
    return dict(seed=seed, inplace_lb=hh.total_kg * LB_PER_KG, rec=kg / hh.total_kg,
                lb=kg * LB_PER_KG, npv=npv, grade=float(hh.S0[hh.S0 > 0].mean() / 20),
                K=float(np.exp(np.log(hh.K).mean())), k_u=hh.k_u, k_g=hh.k_g)


if __name__ == "__main__":
    with Pool(4) as p:
        out = p.map(one, range(int(sys.argv[1])))
    json.dump(out, open(sys.argv[2], "w"))
