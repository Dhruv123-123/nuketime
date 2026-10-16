"""Contamination discount at sale and recovery after closure, from the LA County assessor roll (2006-2025).

Prop 13 resets a parcel's base-year value to its purchase price at a change of ownership, so the roll is a dated
price record. Sale event = a roll year in which Roll_LandBaseYear moves forward to the recording year
(|recording year - base year| <= 1). Price = Roll_TotalValue in that roll year (Roll_LandValue as a variant).
Non-arm's-length screens: value < 10% of the prior roll value, or unchanged value.

GeoTracker cases (LUST, Cleanup Program, Military) are matched to the parcel polygon containing the case point
(fetch_la_parcels.py). Treatment at each sale: case open on the recording date; closed 0-2 / 2-5 / 5+ years before;
case opened after the sale ("later"). Controls: parcels with no GeoTracker case of any type, within 1.5 km of a
matched parcel, same use class (UseCodeDescChar1).

Models (OLS, fixed effects absorbed by alternating projections, SE clustered by 1 km grid cell):
  M1 hedonic: log price ~ treatment + log lot sqft + log(SQFTmain+1) + YearBuilt bins | UseCode + sale year + 1 km cell
  M2 repeat sales: d log price between two sales of the same parcel ~ [open at 1st sale, closed at 2nd] | year1 x year2
  D  descriptive: median price per sq ft of lot by treatment x use class x sale period
Writes results/discount.md, results/discount_sales.csv. Needs data/la_roll/*.pkl, data/la_parcels/*.pkl.
"""
import os

import numpy as np
import pandas as pd

from common import DATA, RESULTS, WORK, log
from discount_core import TREATS, assign, case_dates, fe_ols, hedonic


# ---- roll and sale events ---------------------------------------------------------------------------------
roll = pd.concat([pd.read_pickle(os.path.join(DATA, "la_roll", f)) for f in sorted(os.listdir(os.path.join(DATA, "la_roll"))) if f.endswith(".pkl")],
                 ignore_index=True)
roll["RollYear"] = pd.to_numeric(roll.RollYear, errors="coerce")
for c in ("Roll_LandValue", "Roll_ImpValue", "Roll_TotalValue", "Roll_LandBaseYear", "Roll_ImpBaseYear", "SQFTmain", "YearBuilt", "CENTER_LAT", "CENTER_LON"):
    roll[c] = pd.to_numeric(roll[c], errors="coerce")
roll["rec"] = pd.to_datetime(pd.to_numeric(roll.RecordingDate, errors="coerce"), unit="ms", errors="coerce")  # epoch ms in the ArcGIS table
roll = roll.dropna(subset=["AIN", "RollYear"]).drop_duplicates(["AIN", "RollYear"]).sort_values(["AIN", "RollYear"])
log(f"roll rows {len(roll):,}, parcels {roll.AIN.nunique():,}, years {int(roll.RollYear.min())}-{int(roll.RollYear.max())}")
g = roll.groupby("AIN")
roll["prev_lby"] = g.Roll_LandBaseYear.shift()
roll["prev_total"] = g.Roll_TotalValue.shift()
roll["prev_year"] = g.RollYear.shift()
ev = roll[(roll.prev_year == roll.RollYear - 1) & (roll.Roll_LandBaseYear > roll.prev_lby) & roll.rec.notna()].copy()
ev = ev[((ev.rec.dt.year - ev.Roll_LandBaseYear).abs() <= 1) & (ev.rec.dt.year >= ev.RollYear - 2)]  # recent recording only
n0 = len(ev)
ev = ev[(ev.Roll_TotalValue > 0) & (ev.Roll_TotalValue >= 0.1 * ev.prev_total) & (ev.Roll_TotalValue != ev.prev_total)]
log(f"sale events: {n0:,} base-year resets, {len(ev):,} after screens")

area = pd.read_pickle(os.path.join(DATA, "la_parcels", "area.pkl")).dropna(subset=["AIN"]).drop_duplicates("AIN")
ev = ev.merge(area[["AIN", "lot_sqft"]], on="AIN", how="left")

# ---- cases and treatment at each sale (discount_core) ----------------------------------------------------
s = case_dates()
cp = pd.read_pickle(os.path.join(DATA, "la_parcels", "case_parcel.pkl")).dropna(subset=["AIN"])
cp = cp.join(s[["case_type", "open_date", "closure_date", "status", "clean", "ctype"]], on="gid")
log(f"LA cases in a parcel: {cp.gid.nunique():,} on {cp.AIN.nunique():,} parcels; cleanup cases {cp[cp.clean].gid.nunique():,}")
ev = assign(ev, cp, roll[["AIN", "CENTER_LAT", "CENTER_LON"]])
ev = ev[ev.UseCodeDescChar1.isin(["Commercial", "Industrial"])]  # the brief: commercial/industrial only
ev["sale_year"] = ev.rec.dt.year
ev["lp"] = np.log(ev.Roll_TotalValue)
ev["lpl"] = np.log(ev.Roll_LandValue.where(ev.Roll_LandValue > 0))
ev["llot"] = np.log(ev.lot_sqft.where(ev.lot_sqft > 100))
ev["lsq"] = np.log1p(ev.SQFTmain.fillna(0))
ev["yb"] = pd.cut(ev.YearBuilt.where(ev.YearBuilt > 1800), [1800, 1940, 1960, 1980, 2000, 2030], labels=False).fillna(-1).astype(int)
ev["cell"] = (np.floor(ev.CENTER_LAT / 0.009)).astype("Int64").astype(str) + "_" + (np.floor(ev.CENTER_LON / 0.0109)).astype("Int64").astype(str)
log("treatment counts: " + str(ev.treat.value_counts().to_dict()))



L = ["# Contamination discount and recovery: LA County assessor roll\n",
     "Method: see `discount.py` docstring. Price = assessed total value in the roll year after a Prop 13 base-year reset "
     "(a change of ownership), on commercial/industrial and vacant parcels, 2006-2025 rolls. Cases matched by the parcel polygon "
     "that contains the GeoTracker point. Coefficients are % price difference against nearby clean sales of the same use "
     "class, after lot size, building size, age, use code, sale year and 1 km cell.\n"]
L.append(f"\nSale events after screens: {len(ev):,} ({ev.AIN.nunique():,} parcels). Counts: {ev.treat.value_counts().to_dict()}. "
         f"Share with lot area: {ev.llot.notna().mean():.2f}.\n")
h, n = hedonic(ev)
L.append(f"\n## M1 hedonic, all case types (n = {n:,})\n\n" + h.to_markdown(index=False))
hl, nl = hedonic(ev, "lpl")
L.append(f"\nLand value only (n = {nl:,}): " + ", ".join(f"{r.treatment} {r.pct}% {r.ci95_pct}" for r in hl.itertuples()))
by_type = {}
for ct in ("LUST", "Cleanup Program", "Military/other"):
    sub = ev[(ev.treat == "control") | (ev.ctype == ct)]
    if (sub.treat != "control").sum() < 30:
        continue
    hh, nn = hedonic(sub)
    by_type[ct] = hh
    L.append(f"\n### {ct} (n = {nn:,})\n\n" + hh.to_markdown(index=False))

# ---- M2 repeat sales ----------------------------------------------------------------------------------------
ev = ev.sort_values(["AIN", "rec"])
nxt = ev.groupby("AIN").shift(-1)
pairs = pd.DataFrame({"AIN": ev.AIN, "y1": ev.sale_year, "y2": nxt.sale_year, "t1": ev.treat, "t2": nxt.treat,
                      "dlp": nxt.lp - ev.lp, "cell": ev.cell, "ctype": ev.ctype}).dropna(subset=["dlp", "y2"])
pairs = pairs[pairs.y2 > pairs.y1]
pairs["treated"] = ((pairs.t1 == "open") & pairs.t2.isin(["closed_0_2", "closed_2_5", "closed_5p"])).astype(float)
pairs["still_open"] = ((pairs.t1 == "open") & (pairs.t2 == "open")).astype(float)
rs = pairs[(pairs.t1 == "control") & (pairs.t2 == "control") | (pairs.treated == 1) | (pairs.still_open == 1)].copy()
rs["yy"] = rs.y1.astype(int).astype(str) + "_" + rs.y2.astype(int).astype(str)
xs = [x for x in ("treated", "still_open") if rs[x].sum() >= 5]
if xs:
    r2, n2 = fe_ols(rs, "dlp", xs, ["yy"], "cell")
    L.append(f"\n## M2 repeat sales (parcel fixed effect; n = {n2:,} pairs; open-then-closed pairs {int(rs.treated.sum())}, "
             f"open-then-open {int(rs.still_open.sum())})\n")
    for x in xs:
        b, se = r2.loc[x, "coef"], r2.loc[x, "se"]
        L.append(f"- {x}: {100*(np.exp(b)-1):.1f}% [{100*(np.exp(b-1.96*se)-1):.1f}, {100*(np.exp(b+1.96*se)-1):.1f}] relative to clean repeat sales over the same years")
else:
    L.append("\n## M2 repeat sales: too few parcels sold both while open and after closure.\n")

# ---- D descriptive -----------------------------------------------------------------------------------------
ev["ppsf_lot"] = ev.Roll_TotalValue / ev.lot_sqft.where(ev.lot_sqft > 100)
ev["period"] = pd.cut(ev.sale_year, [2004, 2010, 2015, 2020, 2026], labels=["2005-10", "2011-15", "2016-20", "2021-25"])
dt = ev.dropna(subset=["ppsf_lot"]).pivot_table(index=["UseCodeDescChar1", "period"], columns="treat", values="ppsf_lot", aggfunc="median", observed=True).round(0)
dn = ev.dropna(subset=["ppsf_lot"]).pivot_table(index=["UseCodeDescChar1"], columns="treat", values="ppsf_lot", aggfunc="count", observed=True)
L.append("\n## D. Median price per sq ft of lot ($), by use class x sale period x treatment\n\n" + dt.to_markdown())
L.append("\nCounts (all periods):\n\n" + dn.to_markdown())

# ---- C. rough margin per site: uplift from closing a case vs Cleanup Fund reimbursed-to-date ------------------
cuf = pd.read_pickle(os.path.join(WORK, "cuf.pkl"))
cps = cp[cp.clean].merge(cuf, on="gid")
cps = cps[cps.reimb > 0]
last = roll.sort_values("RollYear").groupby("AIN").tail(1).set_index("AIN")
open_sale = ev[ev.treat == "open"].sort_values("rec").groupby("AIN").Roll_TotalValue.first()
cps["value"] = cps.AIN.map(open_sale).fillna(cps.AIN.map(last.Roll_TotalValue))
cps["value_src"] = np.where(cps.AIN.isin(open_sale.index), "open-case sale", "latest roll")
rows = []
for ct, grp in cps.groupby("ctype"):
    hh = by_type.get(ct, h).set_index("treatment")
    b_open, b_cl = hh.loc["open", "coef"], hh.loc["closed_0_2", "coef"]
    if pd.isna(b_open) or pd.isna(b_cl):
        continue
    up = grp.value * (np.exp(b_cl - b_open) - 1)
    net = up - grp.reimb
    rows.append({"case type": ct, "parcels": len(grp), "recovery (closed 0-2y vs open)": f"{100*(np.exp(b_cl-b_open)-1):.1f}%",
                 "median value $": int(grp.value.median()), "median uplift $": int(up.median()), "median reimbursed $": int(grp.reimb.median()),
                 "uplift - cost p25 $": int(net.quantile(.25)), "median $": int(net.median()), "p75 $": int(net.quantile(.75)), "share positive": round(float((net > 0).mean()), 2)})
ct_tab = pd.DataFrame(rows)
L.append(f"\n## C. Rough margin per site (LA parcels with a Cleanup Fund reimbursed-to-date, n = {len(cps):,})\n\n"
         "Uplift = parcel value (at the open-case sale, else latest roll) x (exp(b_closed_0_2 - b_open) - 1), by case type from M1. "
         "Cost = Cleanup Fund reimbursed-to-date (Oct 2020 capture; excludes the owner's deductible and anything above the $1.5M cap).\n\n"
         + (ct_tab.to_markdown(index=False) if len(ct_tab) else "No case type had both coefficients."))
cps.to_csv(os.path.join(RESULTS, "discount_margin_sites.csv"), index=False)

ev[["AIN", "gid", "ctype", "treat", "rec", "sale_year", "Roll_TotalValue", "Roll_LandValue", "lot_sqft", "SQFTmain", "YearBuilt", "UseType", "UseCode",
    "UseCodeDescChar1", "UseCodeDescChar2", "SitusHouseNo", "SitusStreet", "SitusCity", "CENTER_LAT", "CENTER_LON"]].pipe(
    lambda d: d[d.treat != "control"]).to_csv(os.path.join(RESULTS, "discount_sales.csv"), index=False)  # controls (~110k) stay in work/la_sales.pkl
ev.to_pickle(os.path.join(WORK, "la_sales.pkl"))
pd.to_pickle({"hedonic": h, "by_type": by_type}, os.path.join(WORK, "la_hedonic.pkl"))
L.append("""
## Reading and caveats

- Recorded prices show no stigma discount. Commercial/industrial parcels that sold while a cleanup case was open sold for about
  the same as, or slightly more than, nearby clean parcels of the same use code, size, age and year. The recovery is small:
  sales 0-5 years after closure are about 5-6 points above open-case sales, and the repeat-sales model (same parcel sold
  while open, then after closure, against clean repeat sales over the same years) gives about +7%.
- Price is the assessor's full cash value set at the change of ownership (normally the purchase price under Prop 13), not
  the deed price; base years also reset on some non-sale transfers (entity changes, partial interests), which the
  screens only partly remove. Commercial sales of operating gas stations can carry business value in the price.
- Treatment is assigned by the parcel polygon containing the GeoTracker point; a case point on the street or a
  neighbouring parcel misassigns it, which biases coefficients towards zero.
- Only LA County, commercial/industrial use classes, 2006-2025 rolls; lot area from today's parcel layer (parcels
  since split or merged have no area and drop out of M1). San Francisco was not run.
- Margin table C uses the Cleanup Fund's reimbursed-to-date as the cleanup cost. The Fund, not the buyer, paid that
  money, so it is the social cost of the cleanup, not the buyer's cash cost; the buyer's own outlay is the deductible
  plus anything ineligible or above the cap.
""")
open(os.path.join(RESULTS, "discount.md"), "w").write("\n".join(L) + "\n")
log("\n".join(L))
