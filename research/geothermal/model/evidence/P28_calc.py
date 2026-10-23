"""P28 arithmetic: gravity step, magnetic low, gamma counting, survey rates, block-hit odds."""
import math
G=6.674e-11
# 1. Gravity step over a buried normal fault: infinite-slab approximation, mGal
def slab(drho_gcc,h_m): return 2*math.pi*G*drho_gcc*1000*h_m*1e5
for th in (10,25,50,100,300):
    print(f"gravity step, throw {th} m, drho -0.45: {slab(0.45,th):.2f} mGal")
# height error -> gravity error (free-air minus Bouguer at 2.0 g/cc)
fa,bg=0.3086,slab(2.0,1)
print(f"net height coefficient {fa-bg:.3f} mGal/m; 3 cm RTK -> {0.03*(fa-bg)*1000:.1f} uGal")
# 2. Magnetic low from a demagnetized vertical prism (2D thin-dike-like, half-width a, depth-to-top z)
# peak anomaly of vertical 2D prism, vertical inducing field, approx: dT = 2*k*F*(atan((x+a)/z)-atan((x-a)/z)) / (2*pi) * ... use simple form
F=50000.0
def prism_peak(dchi,a,z):  # SI susceptibility; 2D vertical prism infinite depth extent, vertical field at pole
    return 2*dchi*F/(4*math.pi)*2*math.atan(a/z)*2  # 2*chi*F*atan(a/z)/pi *... (order of magnitude)
for dchi,a,z in ((0.02,100,30),(0.02,100,130),(0.005,100,130),(0.02,50,230)):
    print(f"mag low dchi={dchi} halfwidth={a} m depth-to-top+AGL={z} m: ~{prism_peak(dchi,a,z):.0f} nT")
# 3. Gamma K-window counting precision (2 L NaI at 30 m AGL), assume 40-80 cps K window
for cps in (40,80):
    for t in (1,5,10):
        print(f"K window {cps} cps, {t}s: {100/math.sqrt(cps*t):.1f}% 1-sigma")
# 4. Survey rate, drone mag+gamma
v,flight_min,lines_sp,flights_hr,hrs=7.0,22,40,2.5,6
km_line=v*flight_min*60/1000
km2_flight=km_line*lines_sp/1000
print(f"mag+gamma: {km_line:.1f} line-km/flight, {km2_flight:.2f} km2/flight, {km2_flight*flights_hr*hrs:.1f} km2/day")
crew_day=1400+350+250  # 2 crew, amortization, processing
print(f"cost per km2 mag+gamma ~ ${crew_day/(km2_flight*flights_hr*hrs):.0f}")
# LiDAR at 70 m AGL, 60 m swath spacing, 10 m/s, 30 min flights
km2_l=10*30*60/1000*0.06
print(f"lidar: {km2_l:.2f} km2/flight, {km2_l*2*6:.0f} km2/day, ~${crew_day/(km2_l*12):.0f}/km2")
# Gravity rover: station time 3.5 min read+level+RTK, 1.5 min drive at 200 m spacing
st=60*10/(3.5+1.5); print(f"gravity rover stations/day (10 h) ~ {st:.0f}")
# 5. Block-hit odds vs location error (sigma, m), Gaussian, square cells centred on best estimate
def p_in(half,s): return math.erf(half/(s*math.sqrt(2)))**2
for s in (1000,600,400,200,120):
    print(f"sigma {s} m: P(upflow in nominated 640-ac block)={p_in(805,s):.2f}; P(in 500 m parcel)={p_in(250,s):.2f}; blocks to reach 90%: ",end="")
    n=1
    while p_in(805*(2*n-1),s)<0.9 and n<6: n+=1
    print(f"{(2*n-1)**2}")
# 6. T at 1.5 km vs basin depth error (fill k=1.2, basement k=2.8, q=0.1 W/m2)
q,kf,kb=0.1,1.2,2.8
dTdh=q/kf-q/kb
for e in (300,200,100):
    print(f"basin depth error {e} m -> T(1.5km) error ~{e*dTdh*1000/1000:.1f} C")
