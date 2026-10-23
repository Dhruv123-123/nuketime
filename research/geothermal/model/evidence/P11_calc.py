# P11 back-of-envelope: slim-hole flow detection limits, AHFO-DTS power, transmissivity to PI, kit cost.
import math
rho_c_w = 4.18e6     # J/m3/K water
print("== Heat-pulse flowmeter: velocity for a given flow in slim holes ==")
for d_mm in (48, 60, 76, 96, 152):
    A = math.pi*(d_mm/2000)**2
    for q_lpm in (0.03, 0.1, 1, 4):
        v = q_lpm/1000/60/A
        print(f"hole {d_mm:3d} mm Q={q_lpm:5.2f} L/min -> v={v*60:7.3f} m/min")
print()
print("== Ambient borehole flow implied by a head difference across one fracture (Thiem) ==")
# Q = 2 pi T dh / ln(R/r)
for T in (1e-7, 1e-6, 1e-5, 1e-4):
    for dh in (0.05, 0.5):
        Q = 2*math.pi*T*dh/math.log(100/0.03)
        print(f"T={T:.0e} m2/s dh={dh:4.2f} m -> Q={Q*6e4:8.4f} L/min")
print()
print("== Active-heated fibre: power and signal ==")
for L in (150, 300, 500):
    for qw in (10, 20):
        print(f"L={L} m at {qw} W/m -> {L*qw/1000:4.1f} kW")
lam = 2.5; r = 0.03
print("conductive rise after 24 h, 15 W/m, lam 2.5:",
      round(15/(4*math.pi*lam)*math.log(4*1e-6*86400/(r**2*1.78)),2), "K")
# Peclet-type threshold: advection removes ~10% of heat when rho_c_w*q*r/lam ~ 0.1
for frac in (0.03, 0.1):
    q = frac*lam/(rho_c_w*r)
    print(f"flux where advection ~{frac*100:.0f}% of conduction (r=3 cm): {q:.1e} m/s = {q*86400*100:.1f} cm/day")
print()
print("== Interval T to a productivity-index proxy ==")
# PI (kg/s/bar) ~ 2 pi k h rho / (mu ln(re/rw)) ; T = k h rho g / mu  -> PI = 2 pi T rho/(g ln) per Pa ->*1e5
rho=950; g=9.81
for T in (1e-6, 1e-5, 1e-4, 1e-3):
    dh_per_bar = 1e5/(rho*g)                     # m of head per bar
    PI = 2*math.pi*T*dh_per_bar/math.log(500/0.1)*rho  # kg/s per bar (Thiem, re=500 m, rw=0.1 m)
    print(f"T={T:.0e} m2/s (cold water) -> PI ~ {PI:7.2f} kg/s/bar (x ~5 for 150C viscosity)")
print()
print("== Kit BOM (unverified estimates, USD) ==")
bom = {
 "500 m 4-conductor electric logging winch + depth encoder": (25e3, 40e3),
 "40 mm acoustic televiewer (ABI40-class), 70 C": (45e3, 65e3),
 "heat-pulse flowmeter, 42 mm, + diverters (buy) or own build": (8e3, 20e3),
 "NQ/HQ double straddle packer, 3 transducers, N2 inflation": (15e3, 30e3),
 "6-8 in packer pair for ranch wells": (8e3, 15e3),
 "1.75 in sub pump, injection pump, flowmeters, 2 m3 tank": (6e3, 10e3),
 "hybrid armoured fibre+copper heater cable 500 m": (8e3, 15e3),
 "DTS interrogator (buy; rental $1-2k/day alternative)": (40e3, 90e3),
 "heater supply 10 kW genset + controller": (6e3, 10e3),
 "blank flexible liners x10 (FLUTe-type)": (20e3, 50e3),
 "push-pull skid: dosing pump, Br ISE, autosampler, UV fluorometer": (8e3, 20e3),
 "trailer, tripod, sheave, safety": (10e3, 20e3),
}
lo=sum(v[0] for v in bom.values()); hi=sum(v[1] for v in bom.values())
for k,v in bom.items(): print(f"{v[0]/1e3:5.0f}-{v[1]/1e3:4.0f}k  {k}")
print(f"TOTAL {lo/1e3:.0f}-{hi/1e3:.0f}k; lean (rent DTS+televiewer, own flowmeter, 4 liners) ~", round((lo-40e3-45e3-30e3)/1e3), "-", round((hi-90e3-65e3-30e3)/1e3), "k")
