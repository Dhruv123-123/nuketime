"""P26 Water-Point Ledger: toy detection-limit and cost calculation.
All inputs are assumptions (unverified). Run: python3 -I P26_calc.py
Detection limit = smallest hidden advective heat (MWth) a nested pair of
stream nodes can see at baseflow, given chloride (Cl) flux errors and an
atmospheric-Cl background whose deposition rate is only known to +/-30%.
"""
import numpy as np
rng = np.random.default_rng(26)
N = 20000
cp = 4.18e3  # J/kg/K

def det_limit(area_km2, q_m3s, cl_bg_mgL, cl_deep_mgL, t_res, sd_q=0.07, sd_cl=0.03,
              dep_kg_ha_yr=1.5, dep_sd=0.3, n_obs=12, z=2.33):
    # background Cl flux from rain (g/s) vs measured stream Cl flux (g/s)
    flux = q_m3s * cl_bg_mgL  # g/s (m3/s * mg/L = g/s)
    dep = area_km2 * 100 * dep_kg_ha_yr * 1000 / 3.156e7  # g/s
    # error of differential flux (downstream minus upstream) from n_obs monthly baseflow grabs
    meas = flux * np.sqrt(2) * np.hypot(sd_q, sd_cl) / np.sqrt(n_obs / 3)  # ~seasonal autocorrelation
    bg = dep * dep_sd
    sig = np.hypot(meas, bg)
    cl_lim = z * sig  # g/s of Cl at 99% one-sided
    # convert Cl flux to deep-water mass flux then to heat above 10 C ambient
    m_deep = cl_lim / (cl_deep_mgL / 1000.0)  # kg/s  (g/s / (g/kg))
    return cl_lim, m_deep, m_deep * cp * (t_res - 10) / 1e6

print("area_km2 baseflow_m3s bgCl_mgL deepCl_mgL Tres  Cl_lim_g/s  deep_kg/s  MWth_limit")
for area, q, clb, cld, t in [(50, 0.5, 1.5, 800, 180), (100, 1.5, 1.5, 800, 180), (300, 5, 2, 800, 180),
                             (100, 1.5, 1.5, 200, 150), (1000, 20, 2, 800, 180), (100, 0.3, 5, 2000, 200)]:
    c, m, h = det_limit(area, q, clb, cld, t)
    print(f"{area:8d} {q:11.1f} {clb:8.1f} {cld:10.0f} {t:5.0f} {c:10.2f} {m:10.2f} {h:10.2f}")

# Natural advective discharge of commercial-size systems (rough lognormal, unverified):
# median ~10 MWth, 10-90% about 2-50 MWth. P_det at a 100 km2 node pair:
nat = np.exp(rng.normal(np.log(10), 1.25, N))
_, _, lim100 = det_limit(100, 1.5, 1.5, 800, 180)
_, _, lim1000 = det_limit(1000, 20, 2, 800, 180)
frac_liq = 0.7  # share of upflow heat that leaves as liquid into the gauged catchment (not vapour, not deep export)
print(f"P_det(100 km2 node, liquid leak share {frac_liq}) = {np.mean(nat*frac_liq > lim100):.2f}")
print(f"P_det(1000 km2 trunk node)                     = {np.mean(nat*frac_liq > lim1000):.2f}")

# cost per km2 per year by tier (USD, unverified)
tiers = {
 "T1 stream node (100 km2 each)": dict(capex=1500, life=4, opex=12*55 + 300 + 4*150, area=100),
 "T1 trunk node (1000 km2)":      dict(capex=1500, life=4, opex=12*55 + 300 + 4*150, area=1000),
 "T2 ranch spring (25 km2)":      dict(capex=1400, life=5, opex=4*55 + 250 + 2*150, area=25),
 "T3 stock tank (10 km2)":        dict(capex=70, life=4, opex=60 + 1*30, area=10),
}
for k, v in tiers.items():
    c = (v["capex"] / v["life"] + v["opex"]) / v["area"]
    print(f"{k:34s} ${c:7.1f} /km2/yr")
