"""Figures for the LOCKSTEP design report (reference palette from the dataviz skill)."""
import json, os, math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

C = dict(blue="#2a78d6", orange="#eb6834", aqua="#1baf7a", yellow="#eda100", violet="#4a3aa7", red="#e34948",
         ink="#0b0b0b", ink2="#52514e", muted="#8a8984", grid="#e6e5e1", surface="#fcfcfb", critical="#d03b3b")
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10, "axes.edgecolor": C["muted"], "axes.labelcolor": C["ink2"],
    "xtick.color": C["ink2"], "ytick.color": C["ink2"], "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": C["grid"], "grid.linewidth": 0.8, "axes.titleweight": "bold",
    "axes.titlecolor": C["ink"], "figure.facecolor": C["surface"], "axes.facecolor": C["surface"], "legend.frameon": False,
})
os.makedirs("figures", exist_ok=True)
S = json.load(open("runs/island.json"))
def load(name):
    z = np.load(f"runs/island_{name}.npz"); return {k: z[k] for k in z.files}

# ---------------------------------------------------------------- 1. islanding transient
a, b = load("island_520"), load("island_house_only")
def trip_time(d, name):
    # first time any trip condition is met (recompute from arrays)
    tr = S[name]["trips"]
    t = d["t"]
    cond = np.zeros_like(t, dtype=bool)
    cond |= d["P_pz"] > 16.7; cond |= d["p_sg"] > 8.3; cond |= d["freq"] > 66; cond |= d["freq"] < 57
    idx = np.argmax(cond) if cond.any() else None
    return None if idx is None else float(t[idx])
tb = trip_time(b, "island_house_only")
fig, axs = plt.subplots(2, 3, figsize=(13.5, 7.2))
def panel(ax, key, ylabel, title, lines=(), scale=1.0, tmax=600):
    for d, col, lab in ((a, C["blue"], "island on data centre (520 MW) + house load"), (b, C["orange"], "full load rejection to house load only")):
        m = d["t"] <= tmax
        ax.plot(d["t"][m] - 10, d[key][m] * scale, color=col, lw=2, label=lab)
    for yv, txt in lines:
        ax.axhline(yv, color=C["critical"], ls=":", lw=1); ax.text(tmax - 12, yv, txt, color=C["critical"], fontsize=8, ha="right", va="bottom")
    if tb is not None:
        ax.axvline(tb - 10, color=C["orange"], ls="--", lw=1)
    ax.set_xlim(-10, tmax - 10); ax.set_ylabel(ylabel); ax.set_title(title, fontsize=10.5)
panel(axs[0, 0], "freq", "Hz", "Island frequency", [(66, "overspeed trip 66 Hz")])
axs[0, 0].set_ylim(56, 68)
panel(axs[0, 1], "n", "fraction of rated", "Reactor power", [])
axs[0, 1].plot(a["t"][a["t"] <= 600] - 10, a["m_frac"][a["t"] <= 600], color=C["blue"], lw=1.2, ls="--", label="turbine steam (island case)")
axs[0, 1].plot(a["t"][a["t"] <= 600] - 10, a["dump"][a["t"] <= 600], color=C["aqua"], lw=1.5, label="steam dump (island case)")
axs[0, 1].set_ylim(0, 1.3); axs[0, 1].legend(fontsize=8, loc="upper right")
panel(axs[0, 2], "Tavg", "°C", "Average coolant temperature", [])
panel(axs[1, 0], "P_pz", "MPa", "Pressuriser pressure", [(16.2, "PORV 16.2"), (16.7, "reactor trip 16.7")])
axs[1, 0].set_ylim(14, 17.5)
panel(axs[1, 1], "p_sg", "MPa", "Steam generator pressure", [(8.3, "safety valves 8.3")])
axs[1, 1].set_ylim(5, 11.5)
panel(axs[1, 2], "rho_rod", "Δk/k", "Control-rod reactivity inserted", [])
for ax in axs[1]: ax.set_xlabel("seconds after grid breaker opens")
h, l = axs[0, 0].get_legend_handles_labels()
fig.legend(h, l, loc="lower center", ncol=2, bbox_to_anchor=(0.5, -0.01))
fig.suptitle("Loss of grid at full power: islanding on the data centre rides through; the same plant rejecting to house load alone trips within seconds", fontsize=11.5, fontweight="bold")
fig.tight_layout(rect=(0, 0.04, 1, 0.96)); fig.savefig("figures/fig1_island.png", dpi=160); plt.close(fig)

# ---------------------------------------------------------------- 2. threshold vs data-centre load
rows = []
for name, s in S.items():
    if name.startswith("island_") and "step" not in name and "24h" not in name and "slow" not in name and "runback" not in name:
        dc = 0.0 if "house_only" in name else float(name.split("_")[1])
        dump = 0.40
        if "dump_25" in name or "dump25" in name: dump = 0.25
        if "dump50" in name: dump = 0.50
        if "dump60" in name: dump = 0.60
        rows.append((dc, dump, s))
fig, axs = plt.subplots(1, 3, figsize=(13, 4.2))
for dump, col, lab in ((0.25, "#86b6ef", "steam dump 25 %"), (0.40, C["blue"], "steam dump 40 % (typical)"), (0.50, "#1c5cab", "steam dump 50 %"), (0.60, "#0d366b", "steam dump 60 %")):
    pts = sorted([(dc, s) for dc, d, s in rows if abs(d - dump) < 1e-6], key=lambda p: p[0])
    if not pts: continue
    x = [p[0] / 1180 * 100 for p in pts]
    axs[0].plot(x, [p[1]["P_pz_max"] for p in pts], marker="o", ms=6, lw=2, color=col, label=lab)
    axs[1].plot(x, [p[1]["p_sg_max"] for p in pts], marker="o", ms=6, lw=2, color=col, label=lab)
    axs[2].plot(x, [p[1]["Tavg_max"] for p in pts], marker="o", ms=6, lw=2, color=col, label=lab)
axs[0].axhline(16.7, color=C["critical"], ls=":"); axs[0].text(2, 16.72, "reactor trip", color=C["critical"], fontsize=8.5)
axs[0].axhline(16.2, color=C["warn"] if "warn" in C else "#a8600c", ls=":"); axs[0].text(2, 16.22, "PORV lifts", color="#a8600c", fontsize=8.5)
axs[1].axhline(8.3, color=C["critical"], ls=":"); axs[1].text(2, 8.33, "safety valves lift", color=C["critical"], fontsize=8.5)
axs[0].set_ylabel("peak pressuriser pressure (MPa)"); axs[1].set_ylabel("peak SG pressure (MPa)"); axs[2].set_ylabel("peak Tavg (°C)")
for ax in axs: ax.set_xlabel("data-centre load, % of plant rating"); ax.legend(fontsize=8)
axs[0].set_title("Islanding survives above a minimum load"); axs[1].set_title("Secondary side"); axs[2].set_title("Primary temperature")
fig.tight_layout(); fig.savefig("figures/fig2_threshold.png", dpi=160); plt.close(fig)

# ---------------------------------------------------------------- 3. 24 h island
d = load("island_520_24h")
fig, axs = plt.subplots(1, 3, figsize=(13, 3.9))
th = d["t"] / 3600
axs[0].plot(th, d["n"], color=C["blue"], lw=2); axs[0].set_ylabel("reactor power, fraction"); axs[0].set_title("Reactor power over 24 h on the island"); axs[0].set_ylim(0, 1.1)
axs[1].plot(th, d["X"], color=C["orange"], lw=2); axs[1].set_ylabel("Xe-135, relative to full-power equilibrium"); axs[1].set_title("Xenon transient after the power drop")
axs[2].plot(th, d["rho_rod"] * 1e5, color=C["violet"], lw=2); axs[2].set_ylabel("rod reactivity (pcm)"); axs[2].set_title("Rods compensate xenon")
for ax in axs: ax.set_xlabel("hours")
fig.tight_layout(); fig.savefig("figures/fig3_island24h.png", dpi=160); plt.close(fig)

# ---------------------------------------------------------------- 4. tower sharing
T = json.load(open("runs/tower.json"))["cases"]
Twb = np.load("runs/Twb.npy")
fig, axs = plt.subplots(1, 2, figsize=(12.5, 4.3))
ax = axs[0]
for scale, col, lab in ((1.0, C["blue"], "existing tower"), (1.25, "#0d366b", "tower with 25 % more cells")):
    dcs = [0, 250, 500, 750]
    ax.plot(dcs, [T[f"scale{scale}_dc{dc}"]["MW_avg_lost"] for dc in dcs], marker="o", ms=6, lw=2, color=col, label=lab)
ax.plot([0, 250, 500, 750], [0, 10, 20, 30], marker="s", ms=5, lw=1.5, ls="--", color=C["orange"], label="data-centre cooling energy avoided (4 % of IT)")
ax.set_xlabel("data-centre IT load (MW)"); ax.set_ylabel("MW, annual average"); ax.set_title("Plant output lost vs data-centre cooling energy avoided"); ax.legend(fontsize=8.5)
ax = axs[1]
c = T["scale1.0_dc500"]
# recompute the hourly supply temperature distribution from the tower model for the 500 MW case (stored stats only) -> plot wet-bulb histogram + supply lines
ax.hist(Twb, bins=40, color=C["grid"], edgecolor=C["muted"])
ax.axvline(c["dc_supply_p99"], color=C["blue"], lw=2)
ax.text(c["dc_supply_p99"] + 0.3, ax.get_ylim()[1] * 0.85, f"data-centre supply water\n99th percentile {c['dc_supply_p99']:.1f} °C\nmax {c['dc_supply_max']:.1f} °C", color=C["blue"], fontsize=9)
ax.axvline(40, color=C["critical"], ls=":"); ax.text(40.2, ax.get_ylim()[1] * 0.5, "ASHRAE W40 limit", color=C["critical"], fontsize=8.5, rotation=90, va="center")
ax.set_xlabel("°C"); ax.set_ylabel("hours per year"); ax.set_title("Synthetic wet-bulb year and the water the data centre receives")
fig.tight_layout(); fig.savefig("figures/fig4_tower.png", dpi=160); plt.close(fig)

# ---------------------------------------------------------------- 5. risk
R = json.load(open("runs/risk_econ.json"))
cats = ["plant_centered", "switchyard_centered", "grid_related", "weather_related"]
labels = ["baseline", "islanding on data centre", "data-centre backup as diverse AC", "both"]
keys = ["baseline", "islanding", "dc_ac", "both"]
fig, ax = plt.subplots(figsize=(9, 4.4))
bottom = np.zeros(4)
cols = {"plant_centered": "#cde2fb", "switchyard_centered": "#86b6ef", "grid_related": "#3987e5", "weather_related": "#0d366b"}
x = np.arange(4)
for cat in cats:
    vals = np.array([R["detail"][k][cat]["cdf"] for k in keys])
    ax.bar(x, vals, bottom=bottom, color=cols[cat], label=cat.replace("_", " "), width=0.6, edgecolor=C["surface"], linewidth=1)
    bottom += vals
for i, k in enumerate(keys):
    ax.text(i, bottom[i] * 1.15, f"{R['cdf'][k]:.1e}", ha="center", fontsize=9, color=C["ink"])
ax.set_yscale("log"); ax.set_ylim(1e-9, 3e-5); ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=9)
ax.set_ylabel("station-blackout core-damage frequency, per reactor-year"); ax.set_title("Generic-fleet blackout risk with the two Lockstep provisions (order-of-magnitude PRA)")
ax.legend(fontsize=8.5, loc="upper right")
fig.tight_layout(); fig.savefig("figures/fig5_risk.png", dpi=160); plt.close(fig)
print("figures:", sorted(os.listdir("figures")))
