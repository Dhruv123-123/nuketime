"""Can X-ray radiography see a defective SiC layer in a TRISO particle at line rate?

Each particle is a voxel phantom (6 um voxels) of kernel, buffer, IPyC, SiC and
OPyC with natural size scatter, carrying at most one defect at a random orientation.
It is projected along three orthogonal axes (as a falling particle could be imaged
by three cameras), sampled on a detector of a given pixel size with blur and photon
noise, and scored by a self-referencing ring detector: unwrap the image around the
particle centre, take the median radial profile over all angles as that particle's
own reference, and score the largest local departure inside the SiC band. Thresholds
are set on defect-free particles.

Linear attenuation at ~25 keV (cm^-1), from NIST mass coefficients: UCO kernel
opaque (~650), buffer 0.31, PyC 0.57, SiC 6.1.
"""
import numpy as np
from scipy.ndimage import gaussian_filter, map_coordinates

VOX = 6.0                       # um
R_NOM = dict(kernel=212.5, buffer=312.5, IPyC=352.5, SiC=387.5, OPyC=427.5)
MU = dict(kernel=650.0, buffer=0.31, IPyC=0.57, SiC=6.1, OPyC=0.57)   # 1/cm
HALF = int(450 / VOX)
g = (np.arange(-HALF, HALF + 1) + 0.5) * VOX
X, Y, Z = np.meshgrid(g, g, g, indexing="ij")
RR = np.sqrt(X * X + Y * Y + Z * Z)
UNIT = np.stack([X, Y, Z]) / np.maximum(RR, 1e-9)

DEFECTS = ("none", "sic_hole", "sic_thin", "sic_crack", "no_opyc")


def random_dir(rng):
    v = rng.normal(size=3)
    return v / np.linalg.norm(v)


def phantom(rng, defect, size=None):
    """Return 3D attenuation volume (1/cm). size: defect extent in um."""
    s = rng.normal(1, 0.03)                      # overall scale scatter
    radii = {k: v * s * rng.normal(1, 0.02) for k, v in R_NOM.items()}
    # keep layers ordered
    order = list(R_NOM)
    for a, b in zip(order, order[1:]):
        radii[b] = max(radii[b], radii[a] + 15)
    off = rng.normal(0, 8, 3)                    # kernel off-centre, um
    vol = np.zeros(RR.shape, np.float32)
    rk = np.sqrt((X - off[0]) ** 2 + (Y - off[1]) ** 2 + (Z - off[2]) ** 2)
    prev = 0.0
    for k in order:
        r_in, r_out = (0.0, radii[k]) if k == "kernel" else (radii[order[order.index(k) - 1]], radii[k])
        if k == "kernel":
            m = rk <= r_out
        else:
            m = (RR > r_in) & (RR <= r_out) & ~(rk <= radii["kernel"])
        if k == "OPyC" and defect == "no_opyc":
            continue
        vol[m] = MU[k]
    if defect in ("sic_hole", "sic_thin", "sic_crack"):
        d = random_dir(rng)
        cosang = np.tensordot(d, UNIT, axes=1)
        r_sic_in, r_sic = radii["IPyC"], radii["SiC"]
        theta = size / r_sic                      # cap half-angle
        cap = cosang >= np.cos(theta)
        shell = (RR > r_sic_in) & (RR <= r_sic)
        if defect == "sic_hole":
            vol[shell & cap] = MU["OPyC"]         # SiC missing, filled by pyrocarbon
        elif defect == "sic_thin":
            mid = (r_sic_in + r_sic) / 2
            vol[shell & cap & (RR > mid)] = MU["OPyC"]
        else:                                     # crack: planar slit through the cap
            n = np.cross(d, random_dir(rng)); n /= np.linalg.norm(n)
            dist = np.abs(np.tensordot(n, np.stack([X, Y, Z]), axes=1))
            vol[shell & cap & (dist <= 6.0)] = MU["IPyC"] * 0   # open gap
    return vol


def projections(vol):
    """Transmission images along x, y and z at voxel resolution."""
    return [np.exp(-vol.sum(axis=a) * VOX * 1e-4) for a in range(3)]


def detector(img, pixel, photons, blur_um, rng):
    k = int(round(pixel / VOX))
    if k > 1:
        n = (img.shape[0] // k) * k
        img = img[:n, :n].reshape(n // k, k, n // k, k).mean(axis=(1, 3))
    img = gaussian_filter(img, blur_um / max(pixel, VOX))
    return rng.poisson(img * photons) / photons


def score(img, pixel):
    """Self-referencing ring anomaly score in the SiC band."""
    n = img.shape[0]
    # centre from the opaque kernel's centroid
    w = (img < 0.2).astype(float)
    cy, cx = (np.array(np.nonzero(w)).mean(axis=1) if w.sum() > 0 else (n / 2, n / 2))
    rs = np.arange(330, 450, max(pixel / 2, 3.0)) / pixel
    ts = np.linspace(0, 2 * np.pi, 360, endpoint=False)
    rr, tt = np.meshgrid(rs, ts)
    pol = map_coordinates(img, [cy + rr * np.sin(tt), cx + rr * np.cos(tt)], order=1, mode="nearest")
    ref = np.median(pol, axis=0)
    mad = np.median(np.abs(pol - ref), axis=0) * 1.4826 + 1e-6
    z = (pol - ref) / mad
    z = gaussian_filter(np.abs(z), (3, 1), mode="wrap")
    return float(z.max())
