"""P16 calc: slim-hole injection/fall-off sizing. All inputs are assumptions (unverified)."""
import math
# 1. Radius scaling of PI (Garg-Combs style, steady radial, skin s)
re=500.0
for rws,rwl,ss,sl in [(0.048,0.108,0,0),(0.038,0.108,0,0),(0.048,0.108,0,-2),(0.048,0.108,3,0)]:
    r=(math.log(re/rws)+ss)/(math.log(re/rwl)+sl)
    print(f"PI_large/PI_slim rw_s={rws} rw_L={rwl} s_s={ss} s_L={sl}: {r:.2f}")
# 2. Viscosity correction cold injection (15 C) vs 150 C production
mu15,mu150,mu200=1.14e-3,1.83e-4,1.35e-4
print("mu ratio 15C/150C",round(mu15/mu150,1)," 15C/200C",round(mu15/mu200,1))
# 3. Pressure response at 3 kg/s for big-well-equivalent PI values
for PI in [0.1,0.5,1,5,20,60,100]:
    print(f"PI {PI} kg/s/bar -> dP at 3 kg/s = {3/PI:.3f} bar")
# 4. Friction in 60 mm ID string over 300 m at 4 kg/s
q=4e-3; D=0.06; L=300; v=q/(math.pi*(D/2)**2); Re=1000*v*D/1.0e-3
f=0.316*Re**-0.25; dP=f*L/D*1000*v*v/2
print(f"v={v:.2f} m/s Re={Re:.0f} f={f:.4f} friction dP={dP/1e5:.2f} bar")
# 5. Radius of investigation r=sqrt(4 D t), D=k/(phi mu ct)
for k in [1e-15,1e-14,1e-13,1e-12]:
    for t in [12*3600,48*3600]:
        Dd=k/(0.05*mu150*1e-9); print(f"k={k:.0e} t={t/3600:.0f}h r_inv={math.sqrt(4*Dd*t):.0f} m")
# 6. Water budget
step=sum([1,2,3,4])*1.5*3600/1000; cr=3*12*3600/1000
print(f"step-rate {step:.0f} m3, 12h constant 3 kg/s {cr:.0f} m3, total {step+cr:.0f} m3")
# 7. Seismogenic index N(M>=m)=V*10^(Sigma-b*m), b=1
for S in [-5,-3,-1]:
    for m in [-2,-1,0]:
        print(f"Sigma={S} V=150 m3 N(M>={m}) = {150*10**(S-m):.2f}")
# 8. Streaming potential: dV=C*dP, C in mV/bar
for C in [1,5,20]:
    for dPb in [0.5,2,10]:
        print(f"C={C} mV/bar dP={dPb} bar -> source dV {C*dPb:.1f} mV")
# 9. MWe per well at 20 bar drawdown, 25 kg/s per MWe, pump cap 100 kg/s (M30 arithmetic)
for PI in [1,5,10,60]:
    m=min(PI*20,100); print(f"PI {PI}: {m:.0f} kg/s -> {m/25:.1f} MWe/well")
