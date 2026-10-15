"""Figures for the CAVERN design report (reference palette from the dataviz skill)."""
import json, math, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from model import Store, Rock, size_plant

C = dict(blue="#2a78d6", orange="#eb6834", aqua="#1baf7a", yellow="#eda100", violet="#4a3aa7", red="#e34948",
         ink="#0b0b0b", ink2="#52514e", muted="#8a8984", grid="#e6e5e1", surface="#fcfcfb", critical="#d03b3b")
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10, "axes.edgecolor": C["muted"], "axes.labelcolor": C["ink2"],
    "xtick.color": C["ink2"], "ytick.color": C["ink2"], "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": C["grid"], "grid.linewidth": 0.8, "axes.titleweight": "bold",
    "axes.titlecolor": C["ink"], "figure.facecolor": C["surface"], "axes.facecolor": C["surface"], "legend.frameon": False,
})
os.makedirs("figures", exist_ok=True)
D = json.load(open("runs/design.json"))
Th, Tw, hd = D["design"]["T_h"], D["design"]["T_w"], D["design"]["h_discharge"]
plant = D["plant"]

# ------------------------------------------------------------- 1. daily dispatch on a duck curve
hours = np.arange(25)
price = np.array([45, 42, 40, 40, 42, 55, 70, 60, 35, 15, 8, 5, 5, 8, 12, 20, 60, 130, 175, 180, 150, 95, 65, 50, 50], float)
P_base = 1156.0
out = np.full(25, P_base)
charge_h = list(range(9, 15))        # 6 h, 09:00-15:00
dis_h = list(range(17, 17 + int(hd)))
out[charge_h] -= plant["P_charge_drop_MW"]
out[dis_h] += plant["P_peak_MW"]
fig, ax1 = plt.subplots(figsize=(9.5, 4.6))
ax1.step(hours, out, where="post", color=C["blue"], lw=2.2, label="Plant output with store")
ax1.step(hours, np.full(25, P_base), where="post", color=C["muted"], lw=1.2, ls="--", label="Plant output without store")
ax1.fill_between([9, 15], [P_base, P_base], [P_base - plant["P_charge_drop_MW"]] * 2, color=C["blue"], alpha=0.15)
ax1.fill_between([17, 17 + hd], [P_base, P_base], [P_base + plant["P_peak_MW"]] * 2, color=C["orange"], alpha=0.25)
ax1.set_ylim(0, 1700); ax1.set_ylabel("MW to grid"); ax1.set_xlim(0, 24); ax1.set_xticks(range(0, 25, 3))
ax1.set_xlabel("Hour of day")
ax1.text(12, 760, f"charge: −{plant['P_charge_drop_MW']:.0f} MW for 6 h\n{plant['E_forgone_MWh']:.0f} MWh forgone at low price", ha="center", va="top", fontsize=9, color=C["ink2"])
ax1.text(19.5, 1540, f"discharge: +{plant['P_peak_MW']:.0f} MW for {hd:.0f} h\n{plant['E_peak_MWh']:.0f} MWh sold at the peak", ha="center", va="bottom", fontsize=9, color=C["ink2"])
ax1.set_title("One day of a 1,100 MWe PWR with the cavern store (reactor at 100 % all day)")
ax1.legend(loc="lower left")
# price as small inset (separate axis, not a dual axis)
ins = ax1.inset_axes([0.0, -0.62, 1.0, 0.32])
ins.step(hours, price, where="post", color=C["ink2"], lw=1.5)
ins.fill_between(hours, 0, price, step="post", color=C["grid"])
ins.set_xlim(0, 24); ins.set_xticks(range(0, 25, 3)); ins.set_ylabel("$/MWh"); ins.set_title("Stylised solar-heavy day-ahead price (illustrative)", fontsize=9, loc="left")
fig.subplots_adjust(bottom=0.42)
fig.savefig("figures/fig1_dispatch.png", dpi=160, bbox_inches="tight"); plt.close(fig)

# ------------------------------------------------------------- 2. round trip map + stage count
Ths = list(range(200, 290, 10)); Tws = [120, 140, 160, 180]
M = np.full((len(Tws), len(Ths)), np.nan)
for i, tw in enumerate(Tws):
    for j, th in enumerate(Ths):
        k = f"{th}_{tw}"
        if k in D["rt_table"]:
            M[i, j] = D["rt_table"][k] * 100
cmap = LinearSegmentedColormap.from_list("blue", ["#cde2fb", "#86b6ef", "#3987e5", "#1c5cab", "#0d366b"])
fig, axs = plt.subplots(1, 2, figsize=(12, 4.4), gridspec_kw=dict(width_ratios=[1.4, 1]))
ax = axs[0]
im = ax.imshow(M, cmap=cmap, vmin=60, vmax=80, aspect="auto", origin="lower")
ax.set_xticks(range(len(Ths))); ax.set_xticklabels(Ths); ax.set_yticks(range(len(Tws))); ax.set_yticklabels(Tws)
ax.set_xlabel("Hot cavern temperature T_h (°C)"); ax.set_ylabel("Warm cavern T_w (°C)"); ax.grid(False)
for i in range(len(Tws)):
    for j in range(len(Ths)):
        if not np.isnan(M[i, j]):
            ax.text(j, i, f"{M[i, j]:.0f}", ha="center", va="center", fontsize=9, color="#ffffff" if M[i, j] > 70 else C["ink"])
ax.add_patch(plt.Rectangle((Ths.index(230) - 0.5, Tws.index(160) - 0.5), 1, 1, fill=False, ec=C["orange"], lw=2.5))
ax.set_title("Electric round trip, % (6 charge stages, 4 flash stages)")
cb = fig.colorbar(im, ax=ax, shrink=0.9); cb.set_label("%")
ax = axs[1]
ncs, nfs = [1, 2, 4, 6, 8], [1, 2, 3, 4, 6]
for nf, col in zip(nfs, ["#cde2fb", "#86b6ef", "#3987e5", "#1c5cab", "#0d366b"]):
    ax.plot(ncs, [D["stage_table"][f"{nc}_{nf}"] * 100 for nc in ncs], marker="o", ms=5, lw=2, color=col, label=f"{nf} flash stage{'s' if nf > 1 else ''}")
ax.set_xlabel("Charge stages (feed heaters used)"); ax.set_ylabel("Round trip, %"); ax.set_ylim(45, 80)
ax.set_title(f"Why staging matters (T_h = {Th:.0f} °C, T_w = {Tw:.0f} °C)"); ax.legend(loc="lower right")
fig.tight_layout(); fig.savefig("figures/fig2_roundtrip.png", dpi=160); plt.close(fig)

# ------------------------------------------------------------- 3. scan: payback vs discharge hours and T_h
fig, axs = plt.subplots(1, 2, figsize=(12, 4.3))
ax = axs[0]
for th, col in zip((220, 235, 250, 265, 280), ["#cde2fb", "#86b6ef", "#3987e5", "#1c5cab", "#0d366b"]):
    st = Store(T_h=th, T_w=160, n_charge=6, n_flash=4)
    hds = [3, 4, 5, 6, 8]
    ax.plot(hds, [size_plant(st, h_discharge=h)["payback_yr"] for h in hds], marker="o", ms=5, lw=2, color=col, label=f"T_h = {th} °C")
ax.set_xlabel("Discharge duration (h)"); ax.set_ylabel("Simple payback (years)"); ax.set_ylim(0, 10)
ax.set_title("Payback vs discharge duration"); ax.text(0.02, 0.03, "T_w = 160 °C; midday 15, peak 160 USD per MWh", transform=ax.transAxes, fontsize=9, color=C["ink2"]); ax.legend()
ax = axs[1]
st = Store(T_h=Th, T_w=Tw, n_charge=6, n_flash=4)
items = [("Retrofit, new peaking turbine (450 per kW)", size_plant(st, h_discharge=hd)),
         ("New build, oversized main turbine (250 per kW)", size_plant(st, h_discharge=hd, capex_inputs=dict(peaker_kw=250.0))),
         ("Retrofit, peak price 100", size_plant(st, h_discharge=hd, price_peak=100)),
         ("Retrofit, peak price 200", size_plant(st, h_discharge=hd, price_peak=200)),
         ("Retrofit, midday price −20", size_plant(st, h_discharge=hd, price_mid=-20))]
y = np.arange(len(items))[::-1]
vals = [p["payback_yr"] for _, p in items]
ax.hlines(y, 0, vals, color=C["grid"], lw=6); ax.scatter(vals, y, s=60, color=C["blue"], zorder=3)
for yy, v, (_, p) in zip(y, vals, items):
    ax.text(v + 0.15, yy, f"{v:.1f} y   (capex {p['capex_total_M']:.0f} M, revenue {p['revenue_M_per_yr']:.0f} M per yr)", va="center", fontsize=8.5, color=C["ink2"])
ax.set_yticks(y); ax.set_yticklabels([n for n, _ in items]); ax.set_xlim(0, 14); ax.grid(axis="y", visible=False)
ax.set_title("Payback under different cases"); ax.set_xlabel("years (prices in USD per MWh, capex in USD)")
fig.tight_layout(); fig.savefig("figures/fig3_economics.png", dpi=160); plt.close(fig)

# ------------------------------------------------------------- 4. rock: wall temperature and profile over decades
rock = Rock(); R = D["rock"]["R_eq_m"]; yr = 365.25 * 86400
fig, axs = plt.subplots(1, 2, figsize=(12, 4.2))
ax = axs[0]
ts = np.logspace(-1, math.log10(40), 60)
for label, R_ins, col in (("no insulation", 0.0, C["muted"]), ("0.5 m foam concrete, k = 0.3", 0.5 / 0.3, "#86b6ef"), ("1.0 m insulating layer, k = 0.15", 1.0 / 0.15, C["blue"])):
    ax.plot(ts, [rock.wall_temperature(R, Th, t * yr, R_ins) for t in ts], lw=2, color=col, label=label)
ax.set_xscale("log"); ax.set_xlabel("Years of operation"); ax.set_ylabel("Rock wall temperature (°C)"); ax.set_ylim(0, 260)
ax.set_title("Hot-cavern rock wall temperature"); ax.legend(loc="lower right")
ax = axs[1]
r = np.linspace(R, R + 120, 300)
for t, col in ((1, "#cde2fb"), (5, "#86b6ef"), (10, "#3987e5"), (30, "#1c5cab")):
    ax.plot(r - R, rock.sphere_profile(R, 119.0, t * yr, r), lw=2, color=col, label=f"{t} y")
ax.set_xlabel("Distance from cavern wall (m)"); ax.set_ylabel("Rock temperature (°C)"); ax.set_ylim(0, 140)
ax.set_title("Rock temperature profile, wall at 119 °C (1 m insulation)"); ax.legend()
fig.tight_layout(); fig.savefig("figures/fig4_rock.png", dpi=160); plt.close(fig)
print("figures:", sorted(os.listdir("figures")))
