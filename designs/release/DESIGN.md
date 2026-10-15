# RELEASE: sorting TRISO particles before the burn-leach test

Two linked models, built to test the second pick (`research/converge/PICK2.md`): that a 100 %
inspection station for TRISO coated particles is worth a company. Part A asks what lot release
costs today and what 100 % inspection would save. Part B asks what X-ray radiography can actually
see at line rate. Part C re-costs Part A with what Part B found. The short answer: X-ray sees
missing and thinned SiC but not tight cracks, so the first product is a sorter in front of today's
release test rather than a replacement for it, and it is still worth millions a year per line.

## Part A: lot release today (`lots.py`, `runs/lots.json`)

- A coating batch is 13 million particles (about 5 kgU), worth about $150,000 at roughly
  $30,000 per kg of TRISO fuel. A 5 MTU-a-year line (TX-1 scale) makes about 1,000 batches a year.
- Its defective-SiC fraction is lognormal from batch to batch (median 5e-6 to 3e-5, sigma 1 to
  1.2). The limit is 1e-4 (X-energy's preliminary Xe-100 spec).
- Today's release is attribute sampling by burn-leach: destroy n particles and accept if at most c
  are defective, with n set so a batch at the limit passes at most 5 % of the time (c = 0 needs
  29,956 particles; c = 4 needs 91,533). A failed batch cannot be sorted, so it is lost. The model
  picks the cheapest c for each process.
- 100 % inspection: every particle is imaged and flagged ones are removed, with sensitivity s and
  false-flag rate f, and release rests on the count of flagged defectives plus a 10,000-particle
  confirmatory burn-leach.

| Process median (sigma) | Cheapest plan | Batches failed | Cost of sampling a year | Cost of 100 % inspection (f = 1e-3) |
|---|---|---|---|---|
| 5e-6 (1.0) | c = 8, n = 144k | 0.9 % | $3.1M | $0.27M |
| 1e-5 (1.0) | c = 14, n = 219k | 3.3 % | $7.5M | $0.27M |
| 2e-5 (1.0) | c = 30, n = 407k | 9.6 % | $19M | $0.28M |
| 3e-5 (1.2) | c = 32, n = 430k | 22 % | $38.6M | $0.27M to $0.65M |

Inspection also ships about 10 times fewer defective particles at s = 0.9 and about 100 times
fewer at s = 0.99, and ships no batch over the limit where sampling lets about 1 % through. At f =
1e-2 its cost rises to $1.6M. The case rests on s: Part B tests it.

## Part B: what X-ray radiography sees (`imaging.py`, `sweep_imaging.py`, `runs/imaging.json`)

- Each particle is a 6 um voxel phantom: UCO kernel 425 um, buffer 100 um, IPyC 40 um, SiC 35 um,
  OPyC 40 um, with 3 % size scatter, 2 % layer scatter and an 8 um kernel offset. Attenuation at
  about 25 keV comes from NIST mass coefficients (SiC 6.1 per cm, pyrocarbon 0.57, buffer 0.31,
  kernel opaque).
- Defects at a random orientation: a missing SiC patch (cap radius 30 to 200 um), a SiC patch
  thinned by half, a 6 um open crack through the SiC (extent 100 or 200 um), and missing OPyC.
- Each particle is projected along three orthogonal axes, binned to 6, 12 or 20 um pixels with
  matching blur and Poisson noise at 300, 2,000 or 10,000 photons per pixel.
- The detector needs no training: unwrap the image around the kernel, take the median radial
  profile as that particle's own reference, and score the largest smoothed local departure in the
  SiC band. The threshold is set for 0.1 % false flags on 3,000 defect-free particles; each defect
  case has 300 particles.

Share of defective particles caught at 0.1 % false flags:

| Pixel, photons per pixel, views | Hole r = 50 um | 80 um | 120 um | 200 um | Thinned, 200 um | Crack | Missing OPyC |
|---|---|---|---|---|---|---|---|
| 20 um, 10,000, 3 views | 44 % | 92 % | 98 % | 100 % | 80 % | 0 to 2 % | 1 % |
| 20 um, 10,000, 1 view | 23 % | 52 % | 65 % | 77 % | 50 % | under 1 % | 1 % |
| 12 um, 10,000, 3 views | 31 % | 76 % | 88 % | 96 % | 61 % | under 1 % | 1 % |
| 20 um, 2,000, 3 views | 2 % | 32 % | 66 % | 90 % | 30 % | 0 % | 0 % |
| 6 um, 10,000, 3 views | 7 % | 38 % | 57 % | 75 % | 27 % | 0 % | 2 % |

What this says:
- One view is not enough. A projection sees a SiC defect well only near the particle's edge, where
  the beam runs along the shell; three views roughly double what is caught.
- Photons matter more than resolution. At a fixed count per pixel, 20 um pixels beat 6 um pixels
  here, partly because coarse pixels average out voxel staircasing in the phantom (so the 6 um rows
  understate what a real 6 um system does) and partly because each pixel carries more signal.
- Tight cracks are invisible to projection radiography at these settings, and missing OPyC is
  invisible to this self-referencing score (it changes the whole outline, which an optical size
  gauge already catches).
- Photon budget, inferred and to be checked with a source vendor: 20 um pixels over a 1 mm field at
  10,000 photons is about 2.5e7 photons per view, so three views at TX-1's roughly 400 particles a
  second need about 3e10 photons a second at the detector. Imaging monolayer trays of particles,
  not falling ones, relaxes the timing.
- The detector is deliberately simple. A trained model, more views or tomosynthesis should do
  better; this is a floor, not a ceiling.

## Part C: a sorter in front of burn-leach (`hybrid.py`, `runs/hybrid.json`)

If the screen can see a share g of the real defect population (at s = 0.95, f = 1e-3), it removes
those particles before the unchanged burn-leach release test, so fewer batches fail and a smaller
sample becomes cheapest. Saving a year for one 5 MTU line, after paying for the discarded good
particles:

| Process median (sigma) | g = 0.3 | g = 0.5 | g = 0.8 |
|---|---|---|---|
| 5e-6 (1.0) | $0.9M | $1.3M | $1.9M |
| 1e-5 (1.0) | $2.5M | $4.0M | $5.8M |
| 2e-5 (1.0) | $6.8M | $11.0M | $15.9M |
| 3e-5 (1.2) | $11.2M | $19.3M | $30.9M |

## Verdict and what would change it

- A sorter is worth roughly $1M to $30M a year per 5 MTU line, mostly while a line is ramping and
  its defect rate is still high, which is exactly 2027 to 2030 for TX-1, Standard Nuclear and BWXT.
  It needs no change to the release method, so it does not wait on the NRC.
- Replacing burn-leach as the release method needs a crack-sensitive signal (phase contrast,
  higher energy resolution, or acoustic or eddy methods on SiC) and a qualification campaign.
- Two numbers decide it, and only fuel makers have them: the real batch-to-batch defect
  distribution, and what share of burn-leach failures are missing or thin SiC rather than cracks.
  They are the first questions in the validation plan.
