"""P30 Muon Well-Puck: rate and density-resolution arithmetic (calc, approximate).
Vertical intensity: Miyake-type depth-intensity relation (from memory, unverified constants):
  I_v(h) = 174/(h+400) * h**-1.53 * exp(-8e-4*h)   [cm^-2 s^-1 sr^-1], h in m.w.e. (hg/cm2)
Checked against WIPP (~1600 mwe, ~4.8e-7 /cm2/s total, from memory) within ~30%.
Flat overburden; slant depth h/cos(theta). Detector = cylinder D x L, hit if muon crosses both
end-planes of the tracking stack is NOT required; we use projected area of the cylinder with a
minimum track length cut (L_trk >= 0.3 m) and zenith cut theta<=70 deg.
"""
import numpy as np
def Iv(h): return 174.0/(h+400.0)*h**-1.53*np.exp(-8e-4*h)
def rate(depth_m, rho=2.3, D=0.11, L=1.2, thmax=70):
    th=np.radians(np.linspace(0.5,thmax,300)); dth=th[1]-th[0]
    h=depth_m*rho/np.cos(th)  # mwe (rho in g/cc, depth in m -> hg/cm2 = m*g/cc)
    I=Iv(h)
    # projected area of cylinder (axis vertical) seen at zenith th, cm2
    A=(np.pi*(D*100/2)**2*np.cos(th) + D*100*L*100*np.sin(th))
    # require chord through scintillator stack >= 0.3 m equivalent: crude efficiency
    eff=np.clip((L*np.cos(th)+D*np.sin(th))/0.3,0,1)
    dOm=2*np.pi*np.sin(th)*dth
    return np.sum(I*A*eff*dOm)*86400  # per day
def dlnI(h,eps=1e-3): return (np.log(Iv(h*(1+eps)))-np.log(Iv(h)))/eps
print("depth_m  muons/day(1.2m puck)  dlnI/dlnX(vertical)")
for d in [50,100,150,200,300,500]:
    print(d, round(rate(d)), round(dlnI(d*2.3),2))
# Cap detection: cap contrast drho over thickness t in overburden H of mean rho0
def counts_needed(H=200,t=80,drho=0.2,rho0=2.3,sigma=3,cosfac=1.0):
    frac=t*drho/(H*rho0)            # fractional change in opacity along path
    s=abs(dlnI(H*rho0))*frac         # fractional change in counts
    return (sigma/s)**2, s
for (H,t,dr) in [(200,80,0.2),(200,40,0.2),(200,80,0.1),(300,100,0.2),(100,40,0.2)]:
    N,s=counts_needed(H,t,dr)
    print(f"H={H} cap t={t} drho={dr}: dN/N={s:.3f}, N for 3sigma per bin={N:.0f}")
# Lateral edge: compare sector bins. 12 azimuth x 3 zenith = 36 bins at 200 m, 4 weeks
R=rate(200)*28
print("200 m, 28 d total muons:",round(R)," per bin (36):",round(R/36))
# footprint radius at cap top (100 m above puck) for theta 60 deg
print("lateral reach at 100 m above puck, 60 deg:",round(100*np.tan(np.radians(60))),"m; at surface 200 m:",round(200*np.tan(np.radians(60))))
