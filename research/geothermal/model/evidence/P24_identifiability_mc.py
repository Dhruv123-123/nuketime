"""P24 Field Gas Lab: Monte Carlo of how adding a helium detector changes
the detection-gap multiplier on N (rank 1) under a shared latent mask class.
Priors are judgement (unverified). Run: python3 -I P24_identifiability_mc.py
"""
import numpy as np
rng = np.random.default_rng(24)
M = 200_000
masks = ["open", "cold lid", "swept", "outflow tongue"]
alpha = np.array([2, 3, 2, 2.0])            # mask prevalence prior in high-lambda low-Pdet cells
sT  = [(8, 2), (1, 6), (1.5, 6), (6, 3)]    # temperature detector (Sentinel profile/discharge)
sHe = [(8, 2), (3, 4), (6, 3), (5, 3)]      # excess-He detector (cartridge, Ne-corrected)
# within-class failure correlation between T and He (shared plumbing), as a phi coefficient
rho = 0.3

def draw(ab, n):  # beta draws per class
    return np.stack([rng.beta(a, b, n) for a, b in ab], axis=1)

def summarise(name, mult):
    p5, p50, p95 = np.percentile(mult, [5, 50, 95])
    print(f"{name:42s} median x{p50:5.2f}  5-95% [{p5:5.2f}, {p95:5.2f}]  ratio {p95/p5:5.2f}")
    return p95 / p5

def run(calib_n=0, label=""):
    pi = rng.dirichlet(alpha, M)
    t = draw(sT, M); h = draw(sHe, M)
    if calib_n:  # calibration campaign: shrink each class's beta to n effective obs around its draw
        t = rng.beta(t * calib_n + 1, (1 - t) * calib_n + 1)
        h = rng.beta(h * calib_n + 1, (1 - h) * calib_n + 1)
        g = rng.gamma(pi * 30 + 1); pi = g / g.sum(1, keepdims=True)  # mask class also read from profile shape on calibration wells
    miss_T = (pi * (1 - t)).sum(1)
    # P(both miss) with within-class correlation rho
    cov = rho * np.sqrt(t * (1 - t) * h * (1 - h))
    both_miss = (pi * ((1 - t) * (1 - h) + cov)).sum(1)
    r1 = summarise(f"T only {label}", 1 / (1 - miss_T))
    r2 = summarise(f"T + He (either fires) {label}", 1 / (1 - both_miss))
    return r1, r2

print("Multiplier on N = 1 / P_det (systems present per system detected), in surveyed cells")
a = run(0, "(priors)")
b = run(5, "(after 20/40 calibration)")
print(f"band shrink from He, priors: {a[0]/a[1]:.2f}x ; after calibration: {b[0]/b[1]:.2f}x")
