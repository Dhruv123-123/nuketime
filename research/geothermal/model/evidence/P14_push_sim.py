# P14: DART-60 push-hole physics check (calc, simple analytic models).
# Usage: python3 P14_push_sim.py
# (1) Noise budget for heat flux from a 15-60 m logged tube: sensor noise, k error,
#     residual ground-surface warming (GST) after subtracting a valley reference hole.
# (2) Minimum detectable vertical Darcy flux (Bredehoeft-Papadopulos 1965) over a 20-60 m interval.
# (3) Three mask scenarios: clay lid over heat, cold aquifer sweep, no anomaly; show the 60 m
#     profile separates them while 2 m does not.
import numpy as np
from math import erfc, sqrt, pi, exp
r=np.random.default_rng(3)
kap=0.6e-6; rc_w=4.18e6
def gst(z,dT,t_yr):  # temperature perturbation from a step surface warming dT, t years ago
    t=t_yr*3.156e7; return dT*erfc(z/(2*sqrt(kap*t)))
z=np.arange(15,60.01,0.5)
# (1) flux error, Monte Carlo
errs={}
for zbot in (30,45,60):
    zz=z[z<=zbot]; e=[]
    for i in range(4000):
        k=1.5; q=0.08; G=q/k
        Tn=G*zz + r.normal(0,0.01,zz.size)           # 0.01 C noise per 0.5 m reading
        dTres=r.normal(0,0.5)                          # site-specific GST residual after valley reference (unverified prior)
        Tn+= np.array([gst(x,dTres,40) for x in zz])
        g=np.polyfit(zz,Tn,1)[0]
        kh=k*(1+r.normal(0,0.12))                      # k from T-CPT/needle + SBT at ~12%
        e.append(kh*g-q)
    errs[zbot]=np.std(e)
    print(f"(1) flux error, 15-{zbot} m interval: sd {np.std(e)*1000:.0f} mW/m2")
# (2) Bredehoeft-Papadopulos: T(z)=T0+dT*(exp(B z/L)-1)/(exp(B)-1), B=rho c v L / k
L=40.0; k=1.5
for v_myr in (0.005,0.01,0.02,0.05,0.1):
    v=v_myr/3.156e7; B=rc_w*v*L/k
    zz=np.linspace(0,L,81); lin=zz/L
    prof=(np.exp(B*lin)-1)/(np.exp(B)-1) if B>1e-9 else lin
    dT=2.0  # 2 C across 40 m (about 50 C/km)
    dev=np.max(np.abs(prof-lin))*dT
    print(f"(2) upward Darcy {v_myr*100:.1f} cm/yr over 40 m: Pe={B:.3f}, max curvature signal {dev*1000:.1f} mC (noise 10 mC, GST residual ~20-60 mC)")
# (3) scenarios: background q=0.08 W/m2, upflow-heated basin q=0.4 W/m2
def profile(zs,kind):
    T=np.zeros_like(zs); Ts=15.0
    if kind=="none": return Ts+0.08/1.5*zs
    if kind=="lid":  # 80 m dry clay/silt lid k=1.2 over warm zone, conductive excess flux 0.35 W/m2
        return Ts+0.35/1.2*zs
    if kind=="sweep": # cold aquifer 8-35 m, lateral flow keeps it isothermal near 15.6 C, steep gradient below in aquitard
        out=[]
        for x in zs:
            if x<8: out.append(Ts+0.08/1.5*x)
            elif x<35: out.append(Ts+0.08/1.5*8+0.002*(x-8))
            else: out.append(Ts+0.08/1.5*8+0.002*27+0.40/1.3*(x-35))
        return np.array(out)
zs=np.array([2,10,20,30,40,50,60.])
for kind in ("none","lid","sweep"):
    p=profile(zs,kind)
    print(f"(3) {kind:5s}: "+" ".join(f"{a:.0f}m={b:.2f}" for a,b in zip(zs,p)))
