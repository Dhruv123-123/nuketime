"""ZR91: is stripping Zr-91 from LWR cladding worth a company at 2026 fuel prices?

Textbook one-group estimate on a standard 17x17 PWR pin cell (public geometry), using
2200 m/s absorption cross-sections. Not a core design: it only asks what share of
neutrons the cladding absorbs, how much of that is Zr-91, and what that is worth in fuel.
"""
import math

NA = 0.6022  # 1e24 atoms/mol, so N is in atoms/(barn*cm)
# 17x17 PWR pin cell (cm)
PITCH, R_FUEL, R_CI, R_CO = 1.26, 0.4096, 0.418, 0.475
A_CELL = PITCH**2
A_FUEL = math.pi * R_FUEL**2
A_CLAD = math.pi * (R_CO**2 - R_CI**2)
A_WATER = A_CELL - math.pi * R_CO**2

# thermal absorption cross-sections at 2200 m/s (barns)
SIG = {"U235": 681 * 0.976, "U238": 2.68, "O": 0.00019, "Zr": 0.185, "H": 0.332, "B10": 3840}
ZR91_SHARE_THERMAL = 0.131 / 0.185  # Zr-91: 11.2% abundance x 1.17 b = 0.131 of 0.185 b


def n(rho, molar):
    return rho * NA / molar


def clad_share(enrich=0.045, boron_ppm=600, fuel_flux_depression=0.85):
    m_u = enrich * 235 + (1 - enrich) * 238
    nu = n(10.4, m_u + 32)
    fuel = A_FUEL * fuel_flux_depression * nu * (enrich * SIG["U235"] + (1 - enrich) * SIG["U238"] + 2 * SIG["O"])
    clad = A_CLAD * 0.95 * n(6.55, 91.22) * SIG["Zr"]
    nw = n(0.72, 18.0)
    nb10 = 0.72 * boron_ppm * 1e-6 * NA / 10.81 * 0.199
    water = A_WATER * (2 * nw * SIG["H"] + nw * SIG["O"] + nb10 * SIG["B10"])
    return clad / (fuel + clad + water)


def eup_cost(e, u3o8=86.0, conv=60.0, swu=150.0, fab=350.0, tails=0.0025, feed=0.00711):
    """$ per kgU of enriched product (standard feed and SWU formulas)."""
    V = lambda x: (2 * x - 1) * math.log(x / (1 - x))
    F = (e - tails) / (feed - tails)
    S = V(e) + (F - 1) * V(tails) - F * V(feed)
    return F * (u3o8 * 2.6 + conv) + S * swu + fab


if __name__ == "__main__":
    out = []
    for boron in (0, 600, 1200):
        out.append((boron, clad_share(boron_ppm=boron)))
    thermal_clad = sum(s for _, s in out) / len(out)
    # Guide/instrument tubes and Zircaloy grids add ~20-30% more Zr; thermal absorptions are
    # ~75-85% of all absorptions in a PWR; Zr resonance capture adds a little back.
    lo = thermal_clad * 1.15 * 0.75 * ZR91_SHARE_THERMAL
    hi = thermal_clad * 1.35 * 0.90 * ZR91_SHARE_THERMAL * 1.2
    print("cladding share of thermal absorptions by boron ppm:", [(b, round(s, 4)) for b, s in out])
    print(f"reactivity freed by removing Zr-91: {lo*1e5:.0f}-{hi*1e5:.0f} pcm")
    # Linear reactivity model: ~1,000 pcm ~ 1 GWd/t single-batch; x1.5 for 3-batch loading.
    for pcm in (lo * 1e5, hi * 1e5):
        dB = pcm / 1000 * 1.5          # GWd/t
        frac = dB / 50.0                # at 50 GWd/t discharge
        for swu in (110, 190):
            c = eup_cost(0.045, swu=swu)
            saving_per_kgU = c * frac
            per_kg_zr = saving_per_kgU / 0.28  # ~0.28 kg Zr alloy per kgU in a 17x17 assembly
            pool = per_kg_zr * 2000 * 1000      # ~2,000 t/yr of LWR reload zirconium worldwide
            print(f"  {pcm:4.0f} pcm, SWU ${swu}: fuel {c:,.0f} $/kgU, saving {frac*100:.1f}% "
                  f"= ${saving_per_kgU:,.0f}/kgU = ${per_kg_zr:,.0f}/kg Zr; world value pool ${pool/1e6:,.0f}M/yr")
