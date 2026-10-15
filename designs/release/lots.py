"""Lot release for TRISO particles: destructive acceptance sampling versus 100 %
inspection with sorting.

A coating batch of N particles has a true defective-SiC fraction p that varies batch
to batch. The specification limit is P_LIM (Xe-100 preliminary spec for defective
SiC, 1e-4). Release must show, at 95 % confidence, that the batch shipped meets it.

Sampling (today): burn-leach n particles, accept if at most c defects. A rejected
batch cannot be sorted, so it is scrapped or reworked.

100 % inspection: every particle is imaged; flagged ones are removed. The machine
detects a defective particle with probability s (demonstrated on a seeded set, so
known only to a lower confidence bound s_lo) and flags a good one with probability f.
The batch is released when the upper 95 % bound on the outgoing defective fraction,
computed from the count of flagged defectives and s_lo, is under the limit; a
confirmatory burn-leach of n_conf particles is kept.
"""
import numpy as np
from scipy import stats

P_LIM = 1e-4
N_BATCH = 13_000_000        # ~5 kgU of 425 um UCO kernels, ~2.6 M particles per kgU
BATCH_VALUE = 150_000.0     # $; ~5 kg at ~$30,000/kg TRISO fuel
BATCHES_PER_YEAR = 1000     # 5 MTU/yr line (TX-1 scale)


def sampling_plan(p_lim=P_LIM, conf=0.95, c=4):
    """Smallest n such that a batch at the limit passes with probability <= 1-conf."""
    lo, hi = 1, 10_000_000
    while lo < hi:
        n = (lo + hi) // 2
        if stats.binom.cdf(c, n, p_lim) <= 1 - conf:
            hi = n
        else:
            lo = n + 1
    return lo, c


def simulate(rng, n_batches, median_p, sigma, s=0.95, f=1e-3, s_lo=None,
             c=4, n_conf=0):
    n, c = sampling_plan(c=c)
    p = np.exp(rng.normal(np.log(median_p), sigma, n_batches))
    # --- sampling
    k = rng.binomial(n, p)
    acc_s = k <= c
    # --- 100 % inspection
    s_lo = s if s_lo is None else s_lo
    D = rng.binomial(N_BATCH, p)                 # defectives in the batch
    det = rng.binomial(D, s)                     # removed
    fp = rng.binomial(N_BATCH - D, f)            # good particles removed
    flagged = det + fp
    # estimate of defectives present: flagged minus expected false calls, over s_lo
    est_D = np.maximum(flagged - f * N_BATCH, 0) / s_lo
    # 95 % upper bound on outgoing defectives: Poisson bound on missed ones
    miss_mean = est_D * (1 - s_lo)
    up = stats.poisson.ppf(0.95, np.maximum(miss_mean, 1e-9) + 3 * np.sqrt(f * N_BATCH) * (1 - s_lo) / s_lo)
    out_frac_bound = up / (N_BATCH - flagged)
    acc_i = out_frac_bound <= P_LIM
    true_out = (D - det) / (N_BATCH - flagged)
    yield_i = (N_BATCH - flagged) / N_BATCH
    return dict(p=p, acc_s=acc_s, acc_i=acc_i, true_out_i=true_out,
                true_out_s=np.where(acc_s, p, np.nan), yield_i=yield_i, n=n, c=c)


def summary(r):
    hi = r["p"] > P_LIM
    return dict(
        sampling_reject_rate=float(1 - r["acc_s"].mean()),
        sampling_good_batches_rejected=float((~r["acc_s"] & ~hi).sum() / max((~hi).sum(), 1)),
        sampling_bad_batches_shipped=float((r["acc_s"] & hi).sum() / max(hi.sum(), 1)),
        inspect_reject_rate=float(1 - r["acc_i"].mean()),
        inspect_yield=float(r["yield_i"].mean()),
        inspect_shipped_over_limit=float((r["acc_i"] & (r["true_out_i"] > P_LIM)).mean()),
        mean_outgoing_sampling=float(np.nanmean(r["true_out_s"])),
        mean_outgoing_inspect=float(r["true_out_i"][r["acc_i"]].mean()),
    )


# particle geometry (AGR-2 UCO-like): radii in um, densities g/cc
LAYERS = [("kernel", 212.5, 11.0), ("buffer", 312.5, 1.05), ("IPyC", 352.5, 1.90),
          ("SiC", 387.5, 3.20), ("OPyC", 427.5, 1.90)]


def particle_mass_g():
    m, r0 = 0.0, 0.0
    for _, r, rho in LAYERS:
        m += rho * 4 / 3 * np.pi * ((r * 1e-4) ** 3 - (r0 * 1e-4) ** 3)
        r0 = r
    return m


def costs(r, n_sample, n_conf=10_000):
    """$ per year for each method: batches lost plus particles destroyed or discarded."""
    frac_s = n_sample / N_BATCH
    frac_c = n_conf / N_BATCH
    samp = (1 - r["acc_s"].mean() + frac_s) * BATCHES_PER_YEAR * BATCH_VALUE
    insp = (1 - r["acc_i"].mean() + (1 - r["yield_i"].mean()) + frac_c) * BATCHES_PER_YEAR * BATCH_VALUE
    return samp, insp


def best_sampling(rng, median_p, sigma, cs=range(0, 41, 2)):
    """Cheapest attribute plan for this process: trade sample size against false rejects."""
    best = None
    p = np.exp(rng.normal(np.log(median_p), sigma, 20000))
    for c in cs:
        n, _ = sampling_plan(c=c)
        acc = rng.binomial(n, p) <= c
        cost = (1 - acc.mean() + n / N_BATCH) * BATCHES_PER_YEAR * BATCH_VALUE
        bad = (acc & (p > P_LIM)).sum() / max((p > P_LIM).sum(), 1)
        if best is None or cost < best[0]:
            best = (cost, c, n, 1 - acc.mean(), bad)
    return best
