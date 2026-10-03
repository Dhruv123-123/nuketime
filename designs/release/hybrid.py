"""Release when the X-ray screen can only see part of the defect population.

The imaging sweep (runs/imaging.json) shows projection radiography finds missing or
thinned SiC patches but not tight cracks. So the realistic product is a sorter that
removes the visible share g of defective particles (at sensitivity s) ahead of the same
burn-leach release test operators use today. Release rules do not change; the batch
that reaches burn-leach is simply cleaner, so fewer batches fail and a smaller-c plan
becomes cheapest. Writes runs/hybrid.json.
"""
import json
import numpy as np
from lots import best_sampling, BATCHES_PER_YEAR, BATCH_VALUE

F = 1e-3          # good particles discarded by the screen
S = 0.95          # sensitivity on the visible share (imaging sweep, 3 views, holes >= 80 um)

rows = []
for p50, sig in ((5e-6, 1.0), (1e-5, 1.0), (2e-5, 1.0), (3e-5, 1.2)):
    base = best_sampling(np.random.default_rng(0), p50, sig)
    for g in (0.0, 0.3, 0.5, 0.8):
        p_out = p50 * (1 - g * S)
        cost, c, n, rej, bad = best_sampling(np.random.default_rng(0), p_out, sig)
        screen = F * BATCHES_PER_YEAR * BATCH_VALUE if g > 0 else 0.0
        rows.append(dict(p50=p50, sigma=sig, visible_share=g, c=c, n=n, reject=round(rej, 3),
                         cost_M=round((cost + screen) / 1e6, 2),
                         saving_M=round((base[0] - cost - screen) / 1e6, 2)))
        print(rows[-1])
json.dump(rows, open("runs/hybrid.json", "w"), indent=1)
