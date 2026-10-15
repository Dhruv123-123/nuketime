"""Figures for the ROCKSINK design report. Palette: validated reference palette (dataviz skill)."""
import json, glob, os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

C = dict(blue="#2a78d6", orange="#eb6834", aqua="#1baf7a", yellow="#eda100", violet="#4a3aa7", red="#e34948",
         ink="#0b0b0b", ink2="#52514e", muted="#8a8984", grid="#e6e5e1", surface="#fcfcfb", critical="#d03b3b")
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10, "axes.edgecolor": C["muted"], "axes.labelcolor": C["ink2"],
    "xtick.color": C["ink2"], "ytick.color": C["ink2"], "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": C["grid"], "grid.linewidth": 0.8, "axes.titleweight": "bold",
    "axes.titlecolor": C["ink"], "figure.facecolor": C["surface"], "axes.facecolor": C["surface"], "legend.frameon": False,
})
os.makedirs("figures", exist_ok=True)
z = np.load("runs/final_series.npz")
t = z["t"]; th = t / 3600.0
ticks = [1, 6, 24, 24 * 7, 24 * 30, 24 * 365, 24 * 365 * 3]
tlab = ["1 h", "6 h", "1 d", "7 d", "30 d", "1 y", "3 y"]

def timeaxis(ax):
    ax.set_xscale("log"); ax.set_xlim(0.1, th[-1]); ax.set_xticks(ticks); ax.set_xticklabels(tlab)
    ax.tick_params(axis="x", which="minor", bottom=False)

# ---------------------------------------------------------------- 1. time series
fig, axs = plt.subplots(3, 1, figsize=(9, 10.5), sharex=True)
ax = axs[0]
ax.plot(th, z["Qin"] / 1e6, color=C["orange"], lw=2, label="Heat into jacket (decay + stored primary heat)")
ax.plot(th, z["Qdec"] / 1e6, color=C["orange"], lw=1.2, ls="--", label="Decay heat alone")
ax.plot(th, z["Qrock"] / 1e6, color=C["blue"], lw=2, label="Heat carried into rock by thermosyphons")
ax.set_yscale("log"); ax.set_ylim(0.03, 40); ax.set_ylabel("MW")
ax.set_title("Heat flow after scram (250 MWth module, loss of all AC and all water)")
ax.legend(loc="upper right")
ax = axs[1]
ax.plot(th, z["Tj"], color=C["orange"], lw=2, label="Containment jacket water")
ax.plot(th, z["Tv"], color=C["blue"], lw=2, label="Thermosyphon vapour")
ax.plot(th, z["Tw"].max(axis=1), color=C["aqua"], lw=2, label="Hottest borehole wall")
ax.plot(th, z["T_cnv"], color=C["violet"], lw=1.2, ls="--", label="Containment inner wall (estimate)")
ax.axhline(150, color=C["critical"], lw=1, ls=":"); ax.text(0.12, 152, "jacket limit 150 °C (0.48 MPa)", color=C["critical"], fontsize=8.5)
ax.axhline(90, color=C["critical"], lw=1, ls=":"); ax.text(0.12, 92, "borehole-wall limit 90 °C", color=C["critical"], fontsize=8.5)
ax.axhline(14, color=C["muted"], lw=1, ls=":"); ax.text(0.12, 16, "undisturbed rock 14 °C", color=C["muted"], fontsize=8.5)
ax.set_ylim(0, 170); ax.set_ylabel("°C"); ax.set_title("Temperatures"); ax.legend(loc="upper right", ncol=2)
ax = axs[2]
Qu = z["Q_unit"].max(axis=1) / 1e3
ax.plot(th, z["q_flood"] / 1e3, color=C["muted"], lw=1.5, label="Flooding limit at vapour temperature")
ax.plot(th, 0.5 * z["q_flood"] / 1e3, color=C["critical"], lw=1, ls=":", label="Design cap: 50 % of flooding limit")
ax.plot(th, Qu, color=C["blue"], lw=2, label="Load on most-loaded thermosyphon")
ax.set_ylim(0, 320); ax.set_ylabel("kW per thermosyphon"); ax.set_title("Thermosyphon capacity margin (125 mm ID, water)")
ax.legend(loc="upper right"); timeaxis(ax); ax.set_xlabel("Time after scram")
fig.tight_layout(); fig.savefig("figures/fig1_timeseries.png", dpi=160); plt.close(fig)

# ---------------------------------------------------------------- 2. sensitivity
rows = []
for f in sorted(glob.glob("runs/F_*.json")):
    s = json.load(open(f)); rows.append((os.path.basename(f)[2:-5], s))
label = {"k3": "Granite, k = 3.0 W/m·K (base)", "k2": "Limestone/sandstone, k = 2.0", "k15": "Shale, k = 1.5",
         "N96": "96 thermosyphons instead of 128", "N160": "160 thermosyphons", "grout1": "Poor grout, k = 1.0",
         "smalljacket": "Half-size jacket (60 t water)", "T0_20": "Warm rock, 20 °C", "L45": "Shorter condensers, 45 m"}
order = ["k3", "k2", "k15", "N96", "N160", "grout1", "smalljacket", "T0_20", "L45"]
rows = sorted(rows, key=lambda r: order.index(r[0]) if r[0] in order else 99)
if rows:
    fig, axs = plt.subplots(1, 3, figsize=(12, 4.2), sharey=True)
    names = [label.get(k, k) for k, _ in rows]; y = np.arange(len(rows))[::-1]
    for ax, key, lim, ttl in zip(axs, ["Tj_peak", "Tw_peak", "flood_ratio_max"], [150, 90, 0.5],
                                 ["Peak jacket temperature (°C)", "Peak borehole-wall temperature (°C)", "Peak load / flooding limit"]):
        vals = [s[key] for _, s in rows]
        ax.hlines(y, 0, vals, color=C["grid"], lw=6)
        ax.scatter(vals, y, s=60, color=[C["critical"] if v > lim * 1.01 else C["blue"] for v in vals], zorder=3)
        for yy, v in zip(y, vals):
            ax.text(v + (0.01 if key == "flood_ratio_max" else 2), yy, f"{v:.2f}" if key == "flood_ratio_max" else f"{v:.0f}", va="center", fontsize=8.5, color=C["ink2"])
        ax.axvline(lim, color=C["critical"], ls=":", lw=1); ax.set_title(ttl, fontsize=10)
        ax.set_xlim(0, lim * 1.25); ax.grid(axis="y", visible=False)
    axs[0].set_yticks(y); axs[0].set_yticklabels(names)
    fig.suptitle("Sensitivity: temperature limits hold in every case; red marks the two cases that exceed the self-imposed flooding cap", fontsize=11, fontweight="bold")
    fig.tight_layout(); fig.savefig("figures/fig3_sensitivity.png", dpi=160); plt.close(fig)

# ---------------------------------------------------------------- 3. rock field
if os.path.exists("runs/field.npz"):
    f = np.load("runs/field.npz")
    cmap = LinearSegmentedColormap.from_list("heat", ["#fcfcfb", "#fbd9c6", "#f2a679", "#eb6834", "#b2431a", "#6b2408"])
    days = [1, 7, 30, 365]
    fig, axs = plt.subplots(2, 4, figsize=(14, 7.4))
    vmax = max(f[f"vert_{d}"].max() for d in days)
    for j, d in enumerate(days):
        ax = axs[0, j]
        im = ax.pcolormesh(f["xs"], -f["zs"], f[f"vert_{d}"], cmap=cmap, vmin=14, vmax=vmax, shading="auto")
        ax.set_aspect("equal"); ax.set_title(f"Day {d}", fontsize=10)
        ax.add_patch(plt.Rectangle((-5, -100), 10, 100, fill=False, ec=C["ink2"], lw=0.8, ls="--"))
        ax.add_patch(plt.Rectangle((-2.6, -98), 5.2, 25, fill=False, ec=C["ink"], lw=1))
        ax.set_xlim(-45, 45); ax.set_ylim(-100, 0); ax.grid(False)
        if j == 0: ax.set_ylabel("Vertical section through axis\ndepth (m)")
        ax = axs[1, j]
        ax.pcolormesh(f["xs"], f["ys"], f[f"horiz_{d}"], cmap=cmap, vmin=14, vmax=vmax, shading="auto")
        ax.set_aspect("equal"); ax.add_patch(plt.Circle((0, 0), 5, fill=False, ec=C["ink2"], lw=0.8, ls="--"))
        ax.set_xlim(-45, 45); ax.set_ylim(-45, 45); ax.grid(False)
        if j == 0: ax.set_ylabel(f"Plan at {f['zmid']:.0f} m depth\n(m)")
    cb = fig.colorbar(im, ax=axs, shrink=0.8, pad=0.02); cb.set_label("Rock temperature (°C)")
    fig.suptitle("Rock temperature around the module (dashed: shaft; solid: containment jacket). Surface held at 14 °C.", fontsize=11, fontweight="bold")
    fig.savefig("figures/fig2_rockfield.png", dpi=150); plt.close(fig)
print("figures written:", sorted(os.listdir("figures")))
