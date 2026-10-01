"""Reduced-order ISR wellfield: one header house of 5-spot patterns.

Depth-averaged 2D finite volumes. Steady Darcy pressure each control month, explicit
upwind transport of lixiviant (oxidant or acid strength, normalised to 1 at injection)
and dissolved uranium, first-order dissolution of solid uranium and of gangue that
consumes lixiviant. Permeability, ore grade and gangue are heterogeneous and hidden
from the operator, who sees only monthly per-producer flow and head grade.
"""
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.signal import fftconvolve

GPM = 5.451            # m3/day per US gpm
LB_PER_KG = 2.20462


def _grf(rng, n, corr_cells, aniso=1.0):
    r = int(3 * corr_cells * max(1, aniso)) + 1
    g = np.arange(-r, r + 1)
    gx, gy = np.meshgrid(g, g)
    k = np.exp(-0.5 * ((gx / (corr_cells * aniso)) ** 2 + (gy / corr_cells) ** 2))
    f = fftconvolve(rng.normal(0, 1, (n + 2 * r, n + 2 * r)), k, mode="same")[r:-r, r:-r]
    return (f - f.mean()) / f.std()


class Wellfield:
    def __init__(self, rng, n_pat=4, spacing=30.0, dx=3.0, buffer=45.0,
                 thick=5.0, poro=0.30, K_mean=4.0, sig_lnK=0.9,
                 grade_mean=0.08, k_u=0.004, k_g=0.03, gangue_mean=1.0,
                 lix_per_u=1.0, gangue_deplete=0.05):
        self.rng = rng
        self.dx, self.h, self.phi = dx, thick, poro
        ext = n_pat * spacing + 2 * buffer
        self.n = n = int(round(ext / dx))
        xs = (np.arange(n) + 0.5) * dx
        self.X, self.Y = np.meshgrid(xs, xs)
        # permeability: channelised sand, anisotropic correlation along the trend
        lnK = np.log(K_mean) + sig_lnK * _grf(rng, n, 4.0, aniso=3.0)
        self.K = np.exp(lnK)                                # m/day
        # roll front: an arc of ore crossing the wellfield, patchy along it
        cx = ext / 2 + rng.uniform(-30, 30)
        cy = ext * rng.uniform(1.0, 1.6)
        R = np.hypot(self.X - cx, self.Y - cy)
        r0 = cy - ext / 2 + rng.uniform(-25, 25)
        band = np.exp(-((R - r0) / rng.uniform(25, 45)) ** 2)
        patch = np.exp(0.6 * _grf(rng, n, 5.0))
        g = band * patch
        # grade as % U3O8; S0 = kg U3O8 per m3 bulk rock (2,000 kg/m3)
        lo, hi = buffer - 8, buffer + n_pat * spacing + 8
        foot = (1 / (1 + np.exp(-(self.X - lo) / 3)) * 1 / (1 + np.exp((self.X - hi) / 3))
                * 1 / (1 + np.exp(-(self.Y - lo) / 3)) * 1 / (1 + np.exp((self.Y - hi) / 3)))
        g = g * foot
        g = g / g[self._wf_mask(n_pat, spacing, buffer)].mean() * grade_mean
        self.S = 2000 * g / 100
        self.S0 = self.S.copy()
        # gangue (pyrite, organics, carbonate) that eats lixiviant
        self.G = gangue_mean * np.exp(0.8 * _grf(rng, n, 6.0))
        self.k_u, self.k_g, self.lix_per_u, self.gdep = k_u, k_g, lix_per_u, gangue_deplete
        self.C = np.zeros((n, n))       # lixiviant, normalised
        self.U = np.zeros((n, n))       # dissolved U3O8, kg/m3 water
        # wells: injectors at pattern corners, producers at centres
        self.inj, self.prod = [], []
        for i in range(n_pat + 1):
            for j in range(n_pat + 1):
                self.inj.append(self._cell(buffer + j * spacing, buffer + i * spacing))
        for i in range(n_pat):
            for j in range(n_pat):
                self.prod.append(self._cell(buffer + (j + .5) * spacing,
                                            buffer + (i + .5) * spacing))
        self.n_pat = n_pat
        # which injectors feed each pattern (4 corners)
        self.corners = []
        for i in range(n_pat):
            for j in range(n_pat):
                a = i * (n_pat + 1) + j
                self.corners.append([a, a + 1, a + n_pat + 1, a + n_pat + 2])
        # per-pattern truth, for reporting only
        self.pat_masks = []
        for i in range(n_pat):
            for j in range(n_pat):
                m = ((self.X >= buffer + j * spacing) & (self.X < buffer + (j + 1) * spacing)
                     & (self.Y >= buffer + i * spacing) & (self.Y < buffer + (i + 1) * spacing))
                self.pat_masks.append(m)
        self.inplace_kg = np.array([self.S0[m].sum() * dx * dx * thick for m in self.pat_masks])
        self.total_kg = self.S0.sum() * dx * dx * thick
        self._build_T()

    def _wf_mask(self, n_pat, spacing, buffer):
        lo, hi = buffer, buffer + n_pat * spacing
        return (self.X >= lo) & (self.X < hi) & (self.Y >= lo) & (self.Y < hi)

    def _cell(self, x, y):
        return int(y / self.dx), int(x / self.dx)

    def _build_T(self):
        n, K, h = self.n, self.K, self.h
        self.Tx = 2 * K[:, :-1] * K[:, 1:] / (K[:, :-1] + K[:, 1:]) * h   # m2/day per unit head
        self.Ty = 2 * K[:-1, :] * K[1:, :] / (K[:-1, :] + K[1:, :]) * h
        idx = np.arange(n * n).reshape(n, n)
        rows, cols, vals = [], [], []
        diag = np.zeros(n * n)
        for T, a, b in ((self.Tx, idx[:, :-1], idx[:, 1:]), (self.Ty, idx[:-1, :], idx[1:, :])):
            a, b, t = a.ravel(), b.ravel(), T.ravel()
            rows += [a, b]; cols += [b, a]; vals += [-t, -t]
            np.add.at(diag, a, t); np.add.at(diag, b, t)
        # constant-head boundary: leakage to the far field from edge cells
        edge = np.zeros((n, n)); edge[0, :] = edge[-1, :] = edge[:, 0] = edge[:, -1] = 1
        self.leak = (edge * K * h * 2).ravel()
        diag += self.leak
        A = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                          shape=(n * n, n * n)) + sp.diags(diag)
        self.solve = spla.factorized(A.tocsc())

    def step_month(self, q_prod, inj_scale=None, days=30.0, lix=None):
        """Run one month. q_prod: producer rates (m3/day). Injection matches production
        less a 1 % bleed, split over each producer's four corner injectors.
        lix: per-injector lixiviant strength (default 1). Returns per-producer
        (volume m3, U3O8 kg) for the month."""
        n = self.n
        q_inj = np.zeros(len(self.inj))
        for p, cs in enumerate(self.corners):
            for c in cs:
                q_inj[c] += 0.99 * q_prod[p] / 4
        lix = np.ones(len(self.inj)) if lix is None else lix
        src = np.zeros((n, n))
        for (iy, ix), q in zip(self.inj, q_inj):
            src[iy, ix] += q
        for (iy, ix), q in zip(self.prod, q_prod):
            src[iy, ix] -= q
        head = self.solve(src.ravel()).reshape(n, n)
        Fx = -self.Tx * (head[:, 1:] - head[:, :-1])      # m3/day across x faces (+ = rightwards)
        Fy = -self.Ty * (head[1:, :] - head[:-1, :])
        lk = (self.leak.reshape(n, n) * head)              # outflow to far field
        V = self.phi * self.dx * self.dx * self.h          # pore volume per cell
        outflow = (np.pad(np.maximum(Fx, 0), ((0, 0), (0, 1))) + np.pad(np.maximum(-Fx, 0), ((0, 0), (1, 0)))
                   + np.pad(np.maximum(Fy, 0), ((0, 1), (0, 0))) + np.pad(np.maximum(-Fy, 0), ((1, 0), (0, 0)))
                   + np.maximum(lk, 0) + np.maximum(-src, 0))
        dt = min(0.5, 0.45 * V / max(outflow.max(), 1e-9))
        nsub = int(np.ceil(days / dt)); dt = days / nsub
        inj_C = np.zeros((n, n)); inj_q = np.zeros((n, n))
        for (iy, ix), q, s in zip(self.inj, q_inj, lix):
            inj_q[iy, ix] += q; inj_C[iy, ix] += q * s
        prod_cells = tuple(np.array(self.prod).T)
        q_p = np.asarray(q_prod)
        vol = q_p * days
        kg = np.zeros(len(self.prod))
        lix_used = float((q_inj * lix).sum() * days)
        Vb = self.dx * self.dx * self.h                    # bulk volume per cell
        for _ in range(nsub):
            C, U = self.C, self.U
            dC = self._adv(C, Fx, Fy, outflow) + inj_C
            dU = self._adv(U, Fx, Fy, outflow)
            # producers withdraw at the cell concentration (already in outflow)
            kg += U[prod_cells] * q_p * dt
            # reactions (per bulk volume): U dissolution and gangue consumption
            ru = self.k_u * C * self.S * np.sqrt(self.S / (self.S0 + 1e-12))                    # kg/m3 bulk / day
            rg = self.k_g * C * self.G
            self.S = np.maximum(self.S - ru * dt, 0)
            self.G = np.maximum(self.G - self.gdep * rg * dt, 0)
            self.C = np.maximum(C + dt * (dC / V - (self.lix_per_u * ru / 2.0 + rg) * Vb / V), 0)
            self.U = U + dt * (dU / V + ru * Vb / V)
            self.C = np.minimum(self.C, lix.max())
        return vol, kg, lix_used

    @staticmethod
    def _adv(c, Fx, Fy, outflow):
        """Net advective mass rate into each cell (upwind), minus all outflow."""
        inn = np.zeros_like(c)
        # x faces
        fpos, fneg = np.maximum(Fx, 0), np.maximum(-Fx, 0)
        inn[:, 1:] += fpos * c[:, :-1]
        inn[:, :-1] += fneg * c[:, 1:]
        fpos, fneg = np.maximum(Fy, 0), np.maximum(-Fy, 0)
        inn[1:, :] += fpos * c[:-1, :]
        inn[:-1, :] += fneg * c[1:, :]
        return inn - outflow * c
