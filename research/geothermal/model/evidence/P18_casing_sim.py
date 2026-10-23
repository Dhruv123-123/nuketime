"""P18 casing-source DC sim (3D finite-volume, nodal potentials).
Compares a steel ranch-well casing used as a buried current electrode with a
plain surface electrode at the same wellhead, over a cold-lid + warm saline
outflow tongue. Reports the plume's surface E-field anomaly vs azimuth at a
ring of E-nodes. Simple, coarse, for order-of-magnitude only.
Run: python3 -I P18_casing_sim.py
"""
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spl

def axis(core_half, dcore, nexp, f=1.35):
    core = np.arange(-core_half, core_half + 1e-6, dcore)
    pad = [core[-1]]
    d = dcore
    for _ in range(nexp):
        d *= f; pad.append(pad[-1] + d)
    pad = np.array(pad[1:])
    return np.concatenate([-pad[::-1], core, pad])

x = axis(2500, 100, 12)
y = axis(2500, 100, 12)
z = np.concatenate([np.arange(0, 400, 25), np.arange(400, 1000, 75)])
z = np.concatenate([z, z[-1] + np.cumsum(75 * 1.35 ** np.arange(1, 12))])
nx, ny, nz = len(x), len(y), len(z)
xc, yc, zc = (x[:-1]+x[1:])/2, (y[:-1]+y[1:])/2, (z[:-1]+z[1:])/2
dx, dy, dz = np.diff(x), np.diff(y), np.diff(z)

LID, PT, PB, RLID = 150, 150, 250, 60.0
SCALE = 1.0  # 1 = real steel conductance smeared on a 100 m cell; 100 = near-equipotential limit
def model(plume, casing_L):
    rho = np.full((nx-1, ny-1, nz-1), 30.0)
    X, Y, Z = np.meshgrid(xc, yc, zc, indexing='ij')
    rho[Z < LID] = RLID                      # cold fresh lid
    if plume:                                # warm saline outflow tongue, toward +x
        m = (Z > PT) & (Z < PB) & (X > -200) & (X < 6000) & (np.abs(Y) < 600)
        rho[m] = 3.0
    sig = 1.0 / rho
    if casing_L > 0:                          # casing: smear steel conductance over the central cell column
        i = np.argmin(np.abs(xc)); j = np.argmin(np.abs(yc))
        A = dx[i] * dy[j]
        sig_c = SCALE * 2.0e4 / A                     # sigma_steel*area ~ 5.5e6*3.7e-3 S.m
        for k in range(nz-1):
            if zc[k] < casing_L: sig[i, j, k] += sig_c
    return sig

def solve(sig, src_node_xy=(0.0, 0.0), ret_xy=(0.0, -9000.0)):
    N = nx*ny*nz
    idx = np.arange(N).reshape(nx, ny, nz)
    rows, cols, vals = [], [], []
    def cellsig(i, j, k):
        return sig[i, j, k]
    # face conductances between nodes: average of the 4 adjacent cells weighted by area
    S = np.pad(sig, 1, mode='edge')
    DX = np.pad(dx, 1, mode='edge'); DY = np.pad(dy, 1, mode='edge'); DZ = np.pad(dz, 1, mode='edge')
    # surface: no cells above z=0 -> zero conductance there
    S[:, :, 0] = 0.0
    diag = np.zeros(N)
    def add(axis_):
        if axis_ == 0:
            for i in range(nx-1):
                # cells adjacent to edge (i..i+1) in x: cells (i, j-1..j, k-1..k) in padded index offset +1
                c = S[i+1]  # shape (ny+1, nz+1)
                a = (c[:-1, :-1]*DY[:-1, None]*DZ[None, :-1] + c[1:, :-1]*DY[1:, None]*DZ[None, :-1]
                     + c[:-1, 1:]*DY[:-1, None]*DZ[None, 1:] + c[1:, 1:]*DY[1:, None]*DZ[None, 1:]) / 4.0
                g = a / dx[i]
                p, q = idx[i].ravel(), idx[i+1].ravel(); g = g.ravel()
                rows.extend([p, q]); cols.extend([q, p]); vals.extend([-g, -g])
                np.add.at(diag, p, g); np.add.at(diag, q, g)
        elif axis_ == 1:
            for j in range(ny-1):
                c = S[:, j+1, :]
                a = (c[:-1, :-1]*DX[:-1, None]*DZ[None, :-1] + c[1:, :-1]*DX[1:, None]*DZ[None, :-1]
                     + c[:-1, 1:]*DX[:-1, None]*DZ[None, 1:] + c[1:, 1:]*DX[1:, None]*DZ[None, 1:]) / 4.0
                g = a / dy[j]
                p, q = idx[:, j].ravel(), idx[:, j+1].ravel(); g = g.ravel()
                rows.extend([p, q]); cols.extend([q, p]); vals.extend([-g, -g])
                np.add.at(diag, p, g); np.add.at(diag, q, g)
        else:
            for k in range(nz-1):
                c = S[:, :, k+1]
                a = (c[:-1, :-1]*DX[:-1, None]*DY[None, :-1] + c[1:, :-1]*DX[1:, None]*DY[None, :-1]
                     + c[:-1, 1:]*DX[:-1, None]*DY[None, 1:] + c[1:, 1:]*DX[1:, None]*DY[None, 1:]) / 4.0
                g = a / dz[k]
                p, q = idx[:, :, k].ravel(), idx[:, :, k+1].ravel(); g = g.ravel()
                rows.extend([p, q]); cols.extend([q, p]); vals.extend([-g, -g])
                np.add.at(diag, p, g); np.add.at(diag, q, g)
    for a_ in range(3): add(a_)
    # Dirichlet-ish: tie outer boundary nodes to ground with a big conductance
    bnd = np.zeros((nx, ny, nz), bool)
    bnd[0] = bnd[-1] = True; bnd[:, 0] = bnd[:, -1] = True; bnd[:, :, -1] = True
    diag[idx[bnd]] += 1e3
    rows.append(np.arange(N)); cols.append(np.arange(N)); vals.append(diag)
    Amat = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(N, N))
    b = np.zeros(N)
    i0 = np.argmin(np.abs(x - src_node_xy[0])); j0 = np.argmin(np.abs(y - src_node_xy[1]))
    b[idx[i0, j0, 0]] = 1.0                    # 1 A in at wellhead (casing top)
    ir = np.argmin(np.abs(x - ret_xy[0])); jr = np.argmin(np.abs(y - ret_xy[1]))
    b[idx[ir, jr, 0]] = -1.0
    M = sp.diags(1.0 / Amat.diagonal())
    v, info = spl.cg(Amat, b, M=M, rtol=1e-9, maxiter=20000)
    return v.reshape(nx, ny, nz), info

def ring_E(v, r=1000.0, naz=12):
    from scipy.interpolate import RegularGridInterpolator
    f = RegularGridInterpolator((x, y), v[:, :, 0])
    out = []
    for az in np.arange(naz) * 360.0 / naz:
        t = np.radians(az); px, py = r*np.cos(t), r*np.sin(t)
        h = 50.0
        ex = -(f([px+h, py]) - f([px-h, py]))[0] / (2*h)
        ey = -(f([px, py+h]) - f([px, py-h]))[0] / (2*h)
        out.append((az, np.hypot(ex, ey)))
    return np.array(out)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        LID, PT, PB, RLID, CL = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
        if len(sys.argv) > 6: SCALE = float(sys.argv[6])
    else:
        CL = 250
    print('lid', LID, 'plume', PT, PB, 'rho_lid', RLID, 'casing', CL)
    res = {}
    for name, plume, L in [('casing_plume', True, CL), ('casing_none', False, CL),
                           ('surf_plume', True, 0), ('surf_none', False, 0)]:
        v, info = solve(model(plume, L))
        res[name] = {r: ring_E(v, r) for r in (600.0, 1000.0, 2000.0)}
        print(name, 'cg info', info)
    for r in (600.0, 1000.0, 2000.0):
        print(f'\nring r={r:.0f} m  |E| per A (uV/m), plume/no-plume ratio, az 0 = plume direction (+x)')
        print(' az   casing_plume  ratio_casing   surf_plume  ratio_surf')
        for k in range(len(res['casing_plume'][r])):
            az = res['casing_plume'][r][k, 0]
            cp, cn = res['casing_plume'][r][k, 1], res['casing_none'][r][k, 1]
            spm, sn = res['surf_plume'][r][k, 1], res['surf_none'][r][k, 1]
            print(f'{az:4.0f}  {cp*1e6:10.2f}  {cp/cn:10.2f}  {spm*1e6:10.2f}  {spm/sn:10.2f}')
        rc = res['casing_plume'][r][:, 1] / res['casing_none'][r][:, 1]
        rs = res['surf_plume'][r][:, 1] / res['surf_none'][r][:, 1]
        print(f'azimuthal contrast (max/min of ratio): casing {rc.max()/rc.min():.2f}, surface {rs.max()/rs.min():.2f}')
