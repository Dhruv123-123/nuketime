"""P21 arithmetic: tidal dv/v detectability, source force, depth, power. All inputs are estimates (unverified)."""
import numpy as np
# 1) Tidal regression precision for eta = (dv/v)/strain
eps_tide = 3e-8          # M2+O1 volumetric strain amplitude, mid-latitude (typ 2-5e-8)
for sig_h, npairs, days, label in [(1e-3,100,14,"ambient, 6-node patch-ish"),(1e-3,400,28,"ambient, 30 nodes 4 wk"),
                                    (1e-3,1500,42,"ambient, 60 nodes 6 wk"),(1e-5,30,28,"active source, 30 rx 4 wk")]:
    nh = days*24
    neff = npairs*0.25    # pairs not independent: assume 25% effective
    sig_amp = sig_h/np.sqrt(nh*neff/2)
    sig_eta = sig_amp/eps_tide
    print(f"{label:28s} sigma(dv/v tidal amp)={sig_amp:.1e}  sigma(eta)={sig_eta:,.0f}  3-sigma floor={3*sig_eta:,.0f}")
# Barometric lever: 1 kPa synoptic swing, stress sensitivity s = (dv/v)/dP
dP=1000.0
for s in [1e-9,1e-8,1e-7]:
    print(f"baro: s={s:.0e}/Pa -> dv/v={s*dP:.0e} per 1 kPa")
# 2) Eccentric-mass source force F = m r w^2
for mr,f in [(0.05,20),(0.2,20),(0.2,40),(1.0,15)]:
    F = mr*(2*np.pi*f)**2
    print(f"m*r={mr} kg m, f={f} Hz -> F={F/1e3:.1f} kN")
# 3) Depth of sensitivity ~ wavelength/3 for surface waves
for vs in [400,800,1500]:
    for f in [0.2,1,5,10]:
        print(f"Vs={vs} f={f}Hz depth~{vs/f/3:,.0f} m", end="; ")
    print()
# 4) Tidal line separation (Rayleigh): days needed
fr = {"M2":1.9322736,"S2":2.0,"N2":1.8959820,"O1":0.9295357,"K1":1.0027379,"P1":0.9972621}
for a,b in [("M2","S2"),("O1","K1"),("M2","N2"),("K1","P1")]:
    print(a,b,f"{1/abs(fr[a]-fr[b]):.1f} days")
# 5) Source power budget: 15 min sweep per hour at 400 W
print("energy/day kWh at 400 W, 25% duty:", 0.4*24*0.25)
