"""P27 toy calculations: what a calibrated, stacked thermal + snow detector can see.
All numbers are judgement priors (unverified) unless marked. Run: python3 -I P27_calc.py
"""
import numpy as np
rng = np.random.default_rng(27)

# ---------- 1. Skin-temperature stack: GLS on a per-pixel energy-balance residual ----------
# Residual r_s (pixel minus local ring background, so scene-wide atmosphere cancels) =
#   a_s*dq + b_s*de + c_s*dI + w*u_pix + e_s
# dq  geothermal excess flux (W/m2), the target
# de  emissivity error (units of 0.01), b ~ 0.7 K night, 0.8 K day per 0.01
# dI  thermal-inertia/moisture-texture anomaly (unit = 1 K night warm), c = +1 night, -2 day
# u_pix persistent per-pixel offset not explained by the fit (shading, shrub, soil) sd w
# e_s scene noise after ring differencing, partly autocorrelated (moisture memory)
def stack_sigma(n_night, n_day, sd_e_prior, sd_I_prior, w, sd_scene=0.6, rho=0.3):
    h_n, h_d = 10.0, 25.0
    a = np.r_[np.full(n_night, 1/h_n), np.full(n_day, 1/h_d)]
    b = np.r_[np.full(n_night, 0.7), np.full(n_day, 0.8)]
    c = np.r_[np.full(n_night, 1.0), np.full(n_day, -2.0)]
    n = n_night + n_day
    # noise covariance: AR(1)-ish exchangeable component + white, plus persistent offset w
    C = sd_scene**2 * ((1-rho)*np.eye(n) + rho*np.ones((n, n)) * 0.25) + w**2*np.ones((n, n))
    X = np.c_[a, b, c]
    prior_prec = np.diag([0.0, 1/sd_e_prior**2, 1/sd_I_prior**2])
    Ci = np.linalg.inv(C)
    post = np.linalg.inv(X.T @ Ci @ X + prior_prec)
    return np.sqrt(post[0, 0])

print("1. Per-pixel 1-sigma on geothermal excess flux dq (W/m2) from a skin-T stack")
cases = {
 "single night scene, no calibration":        (1, 0, 1.5, 0.8, 0.6),
 "300 scenes (150 night), no calibration":    (150, 150, 1.5, 0.8, 0.6),
 "300 scenes, post-calibrated priors":        (150, 150, 0.5, 0.3, 0.35),
 "300 scenes, posts + drone ATI map":         (150, 150, 0.5, 0.12, 0.25),
 "tower 120 pre-dawn stares + drone ATI":     (120, 0, 0.3, 0.12, 0.15),
}
for k, v in cases.items():
    print(f"   {k:45s} sigma_dq = {stack_sigma(*v):5.2f} W/m2")

# footprint averaging: N pixels, persistent offsets correlated over L pixels -> N_eff
def footprint_sigma(sig_pix, area_km2, pix_m, corr_m, floor=0.0):
    # floor = landform-scale systematic error (footprint vs its reference ring) that no
    # amount of pixel averaging removes; added in quadrature (judgement, unverified)
    n_pix = area_km2*1e6/pix_m**2
    n_eff = max(1.0, area_km2*1e6/max(pix_m, corr_m)**2)
    return np.hypot(sig_pix/np.sqrt(min(n_pix, n_eff)), floor)
SAT_FLOOR_RAW, SAT_FLOOR_CAL = 2.0, 0.6     # W/m2 (= 0.2 K and 0.06 K night-equivalent)
SNOW_FLOOR_RAW, SNOW_FLOOR_CAL = 0.4, 0.2   # W/m2 (= 0.8 d and 0.4 d melt-out bias)
s_cal = stack_sigma(150, 150, 0.5, 0.12, 0.25)
s_raw = stack_sigma(150, 150, 1.5, 0.8, 0.6)
print("   footprint 2 km2, 70 m pixels, nuisance correlation 300 m:")
print(f"     uncalibrated  {footprint_sigma(s_raw,2,70,300,SAT_FLOOR_RAW):.2f} W/m2 ; calibrated {footprint_sigma(s_cal,2,70,300,SAT_FLOOR_CAL):.2f} W/m2 (1 sigma)")

# ---------- 2. Snow calorimeter ----------
L_f = 334e3  # J/kg
mm_per_day_per_Wm2 = 86400/L_f  # kg/m2/day = mm SWE/day
print(f"\n2. Snow: 1 W/m2 melts {mm_per_day_per_Wm2:.2f} mm SWE/day; 3 W/m2 -> {3*mm_per_day_per_Wm2:.2f} mm/day (calc)")
def snow_sigma(n_events, D_on=15, melt_bg=2.0, sd_t_event=2.5, sd_persist=1.0):
    shift_per_Wm2 = mm_per_day_per_Wm2*D_on/melt_bg   # days earlier melt-out per W/m2
    sd_t = np.sqrt(sd_t_event**2/n_events + sd_persist**2)
    return sd_t/shift_per_Wm2, shift_per_Wm2
for n_ev, persist in [(4, 2.0), (40, 2.0), (40, 1.0), (40, 0.5)]:
    s, sh = snow_sigma(n_ev, sd_persist=persist)
    print(f"   events={n_ev:3d} persistent-bias sd={persist} d -> shift {sh:.1f} d per W/m2, pixel sigma_dq={s:.2f} W/m2")
s_snow_pix, _ = snow_sigma(40, sd_persist=1.0)
print(f"   footprint 2 km2, 20 m pixels, drift correlation 150 m: {footprint_sigma(s_snow_pix,2,20,150,SNOW_FLOOR_RAW):.2f} W/m2 (1 sigma)")
s_snow_pix_c, _ = snow_sigma(40, sd_persist=0.5)
print(f"   same with stake/camera-calibrated drift model (0.5 d):  {footprint_sigma(s_snow_pix_c,2,20,150,SNOW_FLOOR_CAL):.2f} W/m2")

# ---------- 3. Detection probability of a blind footprint by mask class ----------
# surface-reaching excess flux distribution per mask class (lognormal, W/m2) - judgement
classes = {"leaky (fault-segment)": (3.0, 0.8), "thin dry lid": (0.6, 0.7),
           "thick lid >200 m": (0.15, 0.7), "swept (cold aquifer)": (0.03, 0.8)}
s_snow_raw = footprint_sigma(s_snow_pix,2,20,150,SNOW_FLOOR_RAW)
dets = {"raw satellite stack": footprint_sigma(s_raw,2,70,300,SAT_FLOOR_RAW),
        "calibrated sat stack": footprint_sigma(s_cal,2,70,300,SAT_FLOOR_CAL),
        "uncal. snow": s_snow_raw, "cal. sat + snow": None}
s_combo = 1/np.sqrt(1/footprint_sigma(s_cal,2,70,300,SAT_FLOOR_CAL)**2 + 1/footprint_sigma(s_snow_pix_c,2,20,150,SNOW_FLOOR_CAL)**2)
dets["cal. sat + snow"] = s_combo
print("   sigmas:", {k: round(float(v),2) for k,v in dets.items()})
print("\n3. P(detect at 3 sigma) for a 2 km2 footprint, by mask class")
print("   " + " "*24 + "".join(f"{d:>22s}" for d in dets))
for cname, (med, sl) in classes.items():
    q = rng.lognormal(np.log(med), sl, 200000)
    row = [np.mean(q > 3*s) for s in dets.values()]
    # note: snow columns apply only to snow-regime cells
    print(f"   {cname:24s}" + "".join(f"{p:22.2f}" for p in row))

# ---------- 4. Aircraft pod coverage arithmetic ----------
ifov = 0.65e-3; px = 640; gsd = 1.5
H = gsd/ifov; swath = px*gsd; spacing = swath*0.8
line_km = 1000e6/spacing/1e3*1.0
hours = line_km/200 + 2.0
print(f"\n4. Pod: GSD {gsd} m -> AGL {H:.0f} m, swath {swath:.0f} m, {line_km:.0f} line-km per 1,000 km2, ~{hours:.1f} h with ferry")
print(f"   at $350-450/h aircraft+pilot -> ${hours*350:,.0f}-{hours*450:,.0f} flight cost per 1,000 km2 (unverified rates)")
