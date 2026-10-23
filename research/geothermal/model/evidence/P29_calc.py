"""P29 Archive Truth Lab: throughput, cost per metre, and a toy lid-depth / live-test value calc.
All inputs are estimates (unverified). Run: python3 -I P29_calc.py"""
import random, statistics as st
random.seed(29)

# ---- 1. CoreSweep throughput (tray-limited, not sensor-limited)
def throughput(m_per_tray, min_handle, min_scan, hours=8.0, eff=0.75):
    trays = hours*60*eff/(min_handle+min_scan)
    return trays*m_per_tray
cases = {"old US 10-ft box, 3 rows (~9 m)": (9.0, 2.5, 1.0),
         "NQ 5-row 1.5 m tray (7.5 m)": (7.5, 2.0, 0.8),
         "RC chip tray (20 x 1.5 m = 30 m)": (30.0, 3.0, 1.5)}
print("1. CoreSweep metres/day (8 h, 75% uptime)")
for k,(m,h,s) in cases.items():
    print(f"   {k:38s} {throughput(m,h,s):7.0f} m/day")

# ---- 2. Cost per metre
crew_day = 2*650 + 450          # two techs + per diem/travel (unverified)
capex = 200_000; life_days = 3*150
amort = capex/life_days
lib_fee = 150                   # library handling / forklift time per day (unverified)
for mpd in (500, 750, 1000, 1500, 3000):
    print(f"2. {mpd:5d} m/day -> ${ (crew_day+amort+lib_fee)/mpd:5.2f} /m  (day cost ${crew_day+amort+lib_fee:,.0f})")

# ---- 3. Toy: lid thickness from smectite-out depth vs prior
# Prior on lid thickness b (m) for a lidded cell: lognormal median 300, sigma 0.8
# Observation: smectite->illite transition depth in a hole that reaches it, error +/-40 m;
# hole only sees it if b < hole depth (~300-900 m).
N=20000; prior=[]; post=[]
for _ in range(N):
    b = random.lognormvariate(5.7, 0.8)
    hole = random.uniform(300, 900)
    prior.append(b)
    if b < hole:
        post.append(abs(random.gauss(0,40)))
    else:
        post.append(abs(b-hole)*0.5)  # censored: know only b>hole
pr_sd = st.pstdev(prior)
print(f"3. lid prior SD {pr_sd:.0f} m; mean abs residual after core {st.mean(post):.0f} m; "
      f"share of cored lids resolved {sum(1 for p in post if p<100)/N:.2f}")

# ---- 4. Live vs dead: likelihood ratio from 3 semi-independent tests
# clay isograd alone (fossil Miocene caps everywhere): s=0.85 q=0.45
# + present-T from archive log consistent with mineral T (+/-25C): s=0.75 q=0.15
# + youngest FI Th on boiling curve matching present depth: s=0.6 q=0.15
tests=[(0.85,0.45),(0.75,0.15),(0.6,0.15)]
lr=1
for s,q in tests:
    lr*= s/q
    print(f"4. cumulative positive LR {lr:5.1f}")
prior_live=0.10
po=prior_live/(1-prior_live)*lr
print(f"   P(live | all three positive) from 10% prior = {po/(1+po):.2f}")

# ---- 5. Archive scale (unverified holdings)
holes_per_yr = 2000; yrs = 40; core_share=0.3; m_per_hole=300
print(f"5. NV mining holes since ~1985 ~{holes_per_yr*yrs:,}; cored+chips retained (30%) ~{holes_per_yr*yrs*core_share*m_per_hole/1e6:.1f} M m")
print(f"   one crew at 750 m/d x 150 d = {750*150/1e3:.0f} km/yr")
