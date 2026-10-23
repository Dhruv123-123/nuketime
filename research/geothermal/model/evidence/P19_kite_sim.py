"""P19 Kite: 1D layered-earth forward model of grounded-wire semi-airborne EM.

Uses empymod (Werthmuller 2017, Geophysics 82(6) WB9-WB19) for a finite grounded
wire (bipole) on the surface and a 3-component magnetic receiver in the air.

Question: how big is the change in B when a conductive clay cap (or brine) sits
under a resistive cold lid, for cap tops 200-1500 m, at 0.5-4 km offset, 1-8000 Hz?
And is that change above a realistic drone noise floor?

1D only: it gives an upper bound for a laterally small (1-3 km2) body. See the
.md file for the 3D discount used.

Run:  python P19_kite_sim.py     (needs: pip install empymod)
"""
import numpy as np
import empymod

MU0 = 4e-7 * np.pi
I = 20.0                     # transmitter current, A
L = 2000.0                   # wire length, m (x from -1000 to +1000)
H = 40.0                     # receiver height above ground, m
freqs = np.array([1, 3, 10, 30, 100, 300, 1000, 3000, 8000], float)
offsets = np.array([500, 1000, 2000, 3000, 4000], float)   # broadside, along +y


def field(depth, res, comp):
    """Return B (T, complex) [freq, offset] for component comp in {'x','y','z'}."""
    az, dip = {'x': (0, 0), 'y': (90, 0), 'z': (0, 90)}[comp]
    rec = [np.zeros_like(offsets) + 300.0, offsets, -H, az, dip]  # x=300 m, off the centre line
    src = [-L / 2, L / 2, 0, 0, 0.01, 0.01]
    h = empymod.bipole(src, rec, depth, res, freqs, msrc=False, mrec=True,
                       srcpts=21, strength=I, verb=1)
    return MU0 * np.asarray(h)          # H (A/m) -> B (T)


def model(cap_top, cap_thick=300.0, lid_rho=80.0, cap_rho=3.0, base_rho=60.0):
    depth = [0, cap_top, cap_top + cap_thick]
    res = [2e14, lid_rho, cap_rho, base_rho]
    return depth, res


def background(lid_rho=80.0, base_rho=60.0, lid_thick=None):
    # same column with the cap replaced by base rock
    return [0, 1e4], [2e14, lid_rho, base_rho]


def main():
    bg_d, bg_r = background()
    out = {}
    print(f"Source: {L/1000:.0f} km wire, {I:.0f} A; receiver {H:.0f} m above ground")
    for comp in ('z', 'x'):
        Bb = field(bg_d, bg_r, comp)
        print(f"\n=== B{comp}: background amplitude |B| (pT), rows=freq, cols=offset km {offsets/1000}")
        for i, f in enumerate(freqs):
            print(f"{f:7.0f} Hz " + " ".join(f"{abs(Bb[i,j])*1e12:9.1f}" for j in range(len(offsets))))
        for top in (200, 400, 700, 1000, 1500):
            d, r = model(top)
            Bm = field(d, r, comp)
            dB = np.abs(Bm - Bb)
            rel = dB / np.abs(Bb)
            out[(comp, top)] = (dB, rel)
            print(f"-- cap 3 ohm-m, 300 m thick, top {top} m under 80 ohm-m lid: |dB| pT (rel %) best freq per offset")
            for j, o in enumerate(offsets):
                k = np.argmax(dB[:, j])
                print(f"   offset {o/1000:.1f} km: max |dB| {dB[k,j]*1e12:8.1f} pT at {freqs[k]:.0f} Hz "
                      f"(rel {rel[k,j]*100:5.1f} %); max rel {rel[:,j].max()*100:5.1f} % at "
                      f"{freqs[np.argmax(rel[:,j])]:.0f} Hz")
    # thin cap / weaker contrast case (10 ohm-m, 150 m thick)
    print("\n=== Weak case: cap 10 ohm-m, 150 m thick, Bz")
    Bb = field(bg_d, bg_r, 'z')
    for top in (400, 700, 1000):
        d, r = model(top, cap_thick=150.0, cap_rho=10.0)
        dB = np.abs(field(d, r, 'z') - Bb)
        for j, o in enumerate(offsets):
            k = np.argmax(dB[:, j])
            print(f"   top {top} m, offset {o/1000:.1f} km: max |dB| {dB[k,j]*1e12:7.1f} pT at {freqs[k]:.0f} Hz "
                  f"(rel {dB[k,j]/abs(Bb[k,j])*100:5.1f} %)")
    # conductive lid case (playa clay 10 ohm-m, 150 m), cap at 700 m
    print("\n=== Conductive-lid case: 10 ohm-m 150 m playa over 80 ohm-m, cap 3 ohm-m top 700 m, Bz")
    d0, r0 = [0, 150, 1e4], [2e14, 10, 80, 60]
    d1, r1 = [0, 150, 700, 1000], [2e14, 10, 80, 3, 60]
    B0 = field(d0, r0, 'z'); B1 = field(d1, r1, 'z')
    dB = np.abs(B1 - B0)
    for j, o in enumerate(offsets):
        k = np.argmax(dB[:, j])
        print(f"   offset {o/1000:.1f} km: max |dB| {dB[k,j]*1e12:7.1f} pT at {freqs[k]:.0f} Hz "
              f"(rel {dB[k,j]/abs(B0[k,j])*100:5.1f} %)")


if __name__ == '__main__':
    main()
