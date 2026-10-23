"""P25 soil-gas integrator noise calc (toy model, all inputs assumed).
Compares one-shot grab vs 28-day integrating cup for radon-like soil gas,
and Rn/Tn normalisation against spatial soil-source noise.
Run: python3 -I P25_calc.py
"""
import numpy as np
rng = np.random.default_rng(1)
NS = 4000             # synthetic sites
days = 28
# temporal noise: log-normal, AR(1) daily, sigma_ln 0.6 (moisture+barometric), memory 3 d
sig_t, phi = 0.6, np.exp(-1/3)
# spatial noise: soil U/permeability, sigma_ln 0.5, shared by Rn and Tn at rho 0.7
sig_s, rho_s = 0.5, 0.7
def series(n):
    x = np.zeros((n, days*24))
    e = rng.normal(0, sig_t*np.sqrt(1-phi**(2/24)), x.shape)
    ph = phi**(1/24)
    x[:, 0] = rng.normal(0, sig_t, n)
    for t in range(1, x.shape[1]):
        x[:, t] = ph*x[:, t-1] + e[:, t]
    return x
def detect(ratio_true, use_tn):
    out = {}
    for lab, anom in [("bg", 1.0), ("anom", ratio_true)]:
        s = rng.normal(0, sig_s, NS)
        s_tn = rho_s*s + np.sqrt(1-rho_s**2)*rng.normal(0, sig_s, NS)
        ts = series(NS)
        grab = np.log(anom) + s + ts[:, rng.integers(0, ts.shape[1])]
        cup = np.log(anom) + s + np.log(np.exp(ts).mean(1))
        if use_tn:  # thoron sees local source only, integrated, small temporal noise
            grab = grab - s_tn; cup = cup - s_tn
        out[lab] = (grab, cup)
    res = {}
    for k, i in [("grab", 0), ("cup", 1)]:
        b, a = out["bg"][i], out["anom"][i]
        thr = np.quantile(b, 0.9)          # 10% false alarm
        res[k] = (a > thr).mean()
    return res
for use_tn in (False, True):
    for r in (1.5, 2.0, 3.0):
        d = detect(r, use_tn)
        print(f"Tn-normalised={use_tn!s:5} anomaly x{r}: P_det@10%FA grab={d['grab']:.2f} cup={d['cup']:.2f}")
