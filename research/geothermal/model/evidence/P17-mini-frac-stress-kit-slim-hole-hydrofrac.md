# P17: Mini-Frac Stress Kit. Slim-hole hydraulic fracturing and HTPF, with televiewer before and after, to measure stress before EGS auctions and before confirmation wells

Date: 23 Oct 2026. Build candidate P17, model track.

Builds on: `../../../hardware/evidence/H12-egs-sensors.md` (EGS lease price ladder, FORGE stress gradients, "nobody measures stress cheaply before leasing"), `M30-permeability.md` (Barton-Zoback-Moos critically stressed fractures, Dixie Valley productive vs tight segments, slip and dilation tendency formulas, "a 20-30 degree SHmax error can flip a fault"), `P11-slim-hole-permeability-wireline-kit-pack.md` (straddle packer, 40 mm televiewer, hole population problem, casual-use limits on injection), `P16-slim-hole-confirmation-package-trailer-i.md` (our own slim holes), `M12-seismology.md` and `P03` (nodes, focal mechanisms).

**Method note.** The shared web-search budget for this run was already used up when this slice started (the tool refused every query), and the one fetch tried (the FORGE ARMA 2019 paper, https://gdr.openei.org/files/1209/ARMA2019_JMoore-FORGE.pdf) was blocked by a permission timeout. So all facts below that are not carried from earlier repo files with a URL are from memory and are marked (unverified). The numbers in Section 4 come from my own script, `P17_stress_calc.py`, in this folder (calc).

---

## 0. Summary

- **What it is.** A trailer-mounted straddle-packer stress kit for open HQ/NQ holes (about 76-96 mm) to about 800 m. It runs classic hydraulic fracturing (HF) in unfractured intervals and hydraulic tests on pre-existing fractures (HTPF) on natural fractures. A rented acoustic televiewer logs the hole before (to pick intervals and fractures) and after (to see the new fracture traces). Our P03 nodes listen at the surface.
- **What it gives.** At 3-6 depths per hole: Shmin magnitude (from the shut-in pressure, about +/-0.3-0.5 MPa), SHmax direction (from the fracture trace on the after-log, about +/-10 degrees), a rough SHmax magnitude (from the reopening pressure, about +/-20-30%), and, with HTPF, the normal stress on each natural fracture set. With 6 or more HTPF tests on fractures of different orientation, it inverts the full stress tensor without needing the shaky SHmax breakdown formula (Cornet and Valette 1984, unverified).
- **Why it matters to the model.** Slip and dilation tendency (M30) is the best pre-drill physics handle on rank 2 (permeability class). Today its stress input is the World Stress Map or the Lund Snee-Zoback interpolation. My calc says a measured stress state cuts the spread of slip tendency on a range-front fault set from sd 0.19 to sd 0.08 and gives about 0.14-0.25 bits per fault set on "critically stressed or not" (calc). That is a real gain, but only near tested holes.
- **Why it matters to rights.** EGS land now clears at about $111/ac on average and up to $1,207/ac in Utah BLM sales, against about $1-4/ac unranked (H12, URLs there). A measured stress regime and Shmin gradient on adjacent private or state land, before a BLM sale, lets us pick the 10-20% of parcels worth bidding up and skip the rest. In new EGS provinces (Nevada, Idaho, Oregon, New Mexico) there is no deep stress data at all, so this is a direct pricing edge.
- **Cost.** Lean v1 about **$90-160k**; full kit with its own hose reel and two packer sizes about **$190-300k** (calc, unverified parts prices). Per hole, 4-6 tests plus two televiewer runs: **2-3 crew-days, about $12-35k** in an existing hole (calc). That matches the brief.
- **Main risk.** Not physics but hole supply and permits. It needs open, competent, uncased hole below 300 m. That means mining core holes before plugging, our own P16 holes, and geotech holes. Injection is not casual use on BLM land. And shallow stress (300-800 m) must extrapolate to 2-4 km; that is the one desk check that can kill it, and FORGE/Dixie Valley/Yucca Mountain data let us run it for free.

**Verdict.** Build it as a module of the P11/P16 trailer, not as a stand-alone company bet. It shares the packer, the televiewer rental, the crew and the holes. Its unique job is pricing EGS blocks and the critically-stressed prior. Self-scores: model_uncertainty_alpha 3, rights_alpha 3.5, buildability 3, cost_scale 2.5, moat 3.5.

---

## 1. Physics

### 1.1 Classic hydraulic fracturing (HF)

- Seal a 0.7-1.0 m interval of intact rock with two inflatable packers. Pump water at a small, steady rate (about 2-20 L/min). Pressure rises until the wall breaks (breakdown pressure Pb). A vertical fracture opens perpendicular to Shmin, because that is the easiest direction (Hubbert and Willis 1957, unverified).
- Stop pumping and shut in. The fracture closes when pressure falls to the stress that pushes on it. The **shut-in pressure Ps equals Shmin** (in a normal or strike-slip regime). This is the robust number. Errors are about +/-0.3-0.5 MPa if the shut-in curve is read with several methods (tangent, dP/dt vs P, Muskat) (Haimson and Cornet 2003, ISRM suggested methods, IJRMMS 40:1011, unverified).
- Re-pressurize 3-5 cycles. The reopening pressure Pr gives an SHmax estimate: SHmax = 3 Shmin - Pr - Pp. This formula is known to be weak (Rutqvist et al. 2000; Ito et al. 1999 on reopening, unverified). Treat SHmax magnitude as +/-20-30%.
- Log the hole again with the televiewer. The new fracture shows as two vertical traces 180 degrees apart. Their azimuth is the **SHmax direction**, about +/-10 degrees (unverified).

### 1.2 HTPF (hydraulic tests on pre-existing fractures)

- Pick natural fractures of different strike and dip on the before-log. Isolate each one and pump gently. Each fracture opens when pressure equals the normal stress across it. The shut-in pressure is that normal stress.
- With at least 6 fractures of well-spread orientation, a least-squares inversion gives the full stress tensor (all 3 magnitudes and the directions), assuming stress varies linearly over the tested depth range (Cornet and Valette 1984, JGR; Cornet 1993 in Comprehensive Rock Engineering, unverified).
- **Why this is the better fit for us.** Geothermal prospect rock is fractured. Clean 1 m intervals for classic HF are rare in fault-zone holes. HTPF uses the fractures we care about. It gives the normal stress on each fracture set directly, which is exactly the denominator in slip tendency (Ts = tau/sigma_n) and the numerator in dilation tendency.

### 1.3 Pressures the kit must reach (calc)

At 800 m in granite or welded tuff, normal faulting, hydrostatic pore pressure:
- Sv about 20-21 MPa (2.6 g/cc), Pp about 7.8 MPa, Shmin about 0.55-0.65 Sv = 11-13.5 MPa, SHmax 14-18 MPa, tensile strength 5-12 MPa.
- Breakdown Pb = 3 Shmin - SHmax - Pp + T about 15-30 MPa at depth. The water column already supplies 7.8 MPa, so surface pump pressure is about 8-23 MPa plus hose friction (1-3 MPa at 10 L/min in an 800 m, 8 mm ID hose, unverified).
- Strike-slip regimes or very strong rock can push Pb toward 35-40 MPa downhole. A **35 MPa surface pump** covers almost all cases to 800 m. A 50 MPa rating is margin for 1 km and for hot, strong rock. HTPF reopening pressures are lower than Pb, often by 30-50%.
- Packers must be inflated 2-5 MPa above the test pressure, so the packer elements need a **25-35 MPa differential in a 76 mm hole**. That is the hardest part spec, and it is why off-the-shelf hydrogeology packers (P11, usually rated 3-10 MPa) do not work here (unverified ratings).

### 1.4 What the measurement means for depth

- In the Basin and Range the upper crust is near frictional failure. The frictional limit for Shmin/Sv with hydrostatic pore pressure is 0.59, 0.56 and 0.52 for friction 0.6, 0.7 and 0.85 (calc, Jaeger-Cook form). FORGE's measured 0.62/1.13 psi/ft = 0.55 (H12) sits right at that limit. So **a measured Shmin/Sv near 0.52-0.59 is itself the "critically stressed" signal**, and a value of 0.65-0.75 says faults are clamped.
- Dixie Valley is the template: productive segments had low Shmin/Sv and faults close to failure; the non-productive segment about 8 km away, at similar temperature, had higher Shmin and was not critically stressed (Hickman, Zoback and Benoit 1998; Hickman et al. 2000, via M30, unverified detail).
- Shallow stress is noisy in the top 100-300 m (topography, weathering, unloading, thermal stress). Tests at 300-800 m in competent rock are usually on the deep trend, because the Shmin/Sv ratio tends to settle once you are below the near-surface zone (unverified). The kill check in Section 7 tests this.
- Stress varies smoothly over 5-50 km except near major faults and province edges, where SHmax can rotate up to 90 degrees (Lund Snee and Zoback 2020, via M30). So one well-placed test informs a neighbourhood, not only its own cell. That is the scale argument for P17 over P11.

### 1.5 Noise and failure modes

- Packer-induced fractures (the packer itself cracks the wall) confuse SHmax direction. The after-log separates them because they start at the packer ends (unverified).
- Leaky, permeable intervals never pressurize. Choose tight intervals from the televiewer and P11 flow logs.
- Hot holes: elastomers and gauges must be rated to the hole temperature. v1 targets holes to about 90 C; 150 C elements cost more (unverified).
- Inclined fractures in HF mean the formula assumptions break. HTPF handles it by design.

---

## 2. Prior art

| Who | What | What we add |
|---|---|---|
| Haimson, Zoback, Hickman (USGS, Univ. Wisconsin), 1970s-2000s | Wireline hydrofrac systems used at Cajon Pass, Long Valley, Nevada Test Site, Dixie Valley (unverified details) | Same physics, run in many cheap prospect holes, before leasing |
| Stock, Healy, Hickman, Zoback 1985, JGR | Hydrofrac stress profiles in Yucca Mountain holes USW G-1/G-2 to about 1.3 km. Low Shmin/Sv, normal faulting (unverified numbers) | Free Basin and Range shallow-to-deep calibration set for the desk test |
| Cornet (IPG Strasbourg), Soultz EGS | HTPF method and full-tensor inversions in fractured granite; Soultz stress profile to 5 km (unverified) | HTPF in slim holes as a land-pricing tool |
| ISRM, Haimson and Cornet 2003 | Suggested methods for HF and HTPF | Our QA standard |
| MeSy (Germany), Solexperts (Switzerland), Golder/WSP, Sigra (Australia), Geosystems | Commercial wireline or rod-conveyed hydrofrac in mining, tunnelling, nuclear-waste and coal holes (unverified vendor list) | Rent first; buy or build the parts that matter |
| Utah FORGE 58-32 and 16A/16B(78)-32 | Minifrac and DFIT at 2-2.5 km: Shmin 0.62, SHmax 0.77, Sv 1.13 psi/ft (H12; data at https://gdr.openei.org/submissions/1570) | Deep "truth" against which our shallow method is scored |
| Oil and gas DFITs | Shmin at reservoir depth, $100-300k per test on top of a $5-10M well (H12, unverified) | Our test is 10x cheaper because the hole is cheap |
| Zanskar | Public data, LBNL large-N seismology, own wells (Z files). No known shallow stress programme (unverified) | Measured stress is a layer they do not have |

---

## 3. v1 design

### 3.1 Concept

A 7 m tandem trailer (shared with the P11/P16 package) carrying a hose reel, pump skid, nitrogen and control cab. In a hole where a core rig is still on site, the kit can instead use the rig's NQ rods as the injection string (rod-conveyed mode), which removes the hose reel cost and is the lean v1.

### 3.2 Parts list

| # | Part | Spec | Price (unverified) |
|---|---|---|---|
| 1 | High-pressure straddle packer, NQ size | Seals 72-80 mm, 0.8 m test interval, steel-reinforced elements, 35 MPa differential, 90 C | $25-45k |
| 2 | Same, HQ size | Seals 92-100 mm | $20-35k |
| 3 | HTPF short interval / single-fracture spacer set | 0.5-1.0 m spacers, downhole shut-in valve to cut wellbore storage | $8-15k |
| 4 | Downhole memory gauges, 2 | Quartz, 0-70 MPa, 0.01% FS, 1 Hz, 150 C; one in interval, one below | $12-25k |
| 5 | Surface pump | Electric triplex or air-driven intensifier, 50 MPa, 1-20 L/min, variable speed | $15-35k |
| 6 | Flow and pressure DAQ | Coriolis or high-pressure turbine flowmeter, 2 surface transducers, 10 Hz logger, laptop | $8-15k |
| 7 | Packer inflation | N2 bottles plus booster to 40 MPa, or a separate small water line | $5-10k |
| 8 | Hose reel (full kit only) | 1,000 m dual line: 8 mm ID injection hose rated 50 MPa plus inflation line, on a hydraulic reel with depth counter | $60-110k |
| 9 | Wireline winch (full kit only, shared with P11) | 1,000 m, 4.8 mm 4-conductor, for televiewer and gauge carrier | $25-45k (shared) |
| 10 | Impression packer (fallback for SHmax direction when no televiewer) | NQ size | $5-10k |
| 11 | Acoustic televiewer | ALT ABI40 or QL40-ABI class, 40 mm OD, 1 cm sampling (P11) | Rent $0.5-1k/day, or $45-65k buy |
| 12 | Surface nodes | 6-10 P03 nodes with 3C geophones around the collar, 500 Hz | Reuse P03 |
| 13 | Generator, water tank, filter | 10 kW, 2 m3 tank, 10 micron filter | $5-8k |
| 14 | Software | Shut-in picking (tangent, dP/dt, G-function), HTPF tensor inversion, Bayesian stress update to the regional field | In-house, 3-5 weeks |

**Totals (calc):** lean v1, rod-conveyed, one packer size, rented televiewer: **$90-160k**. Full kit with hose reel, two sizes, own winch share: **$190-300k**.

### 3.3 Dimensions, power, comms

- Downhole string: packer assembly about 4.5 m long, 70 mm OD (NQ) or 89 mm OD (HQ), about 60-90 kg.
- Power: 10 kW generator; pump draws 5-7 kW at 20 MPa and 10 L/min.
- Water: 200-500 L per test, 1-2 m3 per hole. Clean, filtered, temperature-logged (so the thermal effect on the gauges can be removed).
- Comms: gauges are memory-mode in v1 (read after pull). Surface data logs to laptop and syncs by Starlink or cellular. Real-time downhole readout is a v2 upgrade with a conductor-armoured hose.

### 3.4 Deployment and crew time per hole

Crew of 3 (lead rock-mechanics engineer, pump operator, helper/logger).

| Step | Time |
|---|---|
| Mob, set up on collar, check hole with a dummy run | 3-4 h |
| Televiewer log before (300-800 m at 1 cm) | 3-4 h |
| Pick 3 HF intervals and 3-6 HTPF fractures | 1 h (on site, from image) |
| Run packer, 4-6 tests of 4-5 cycles each, 1-1.5 h per test | 6-9 h |
| Televiewer log after over tested zones | 2-3 h |
| Pull, clean, demob | 2-3 h |

So **2-3 days per hole** (calc). Cost per hole in an existing open hole: crew $4-6k/day, televiewer rent $1.5-3k, consumables and water $1-2k, travel $1-3k, lost-in-hole insurance reserve $2-5k, so about **$12-35k per hole** (calc). In rod-conveyed mode with the rig on hand, add rig standby at about $3-6k/day (unverified).

### 3.5 Which holes

1. **Our own P16 confirmation slim holes** (the main source; the kit runs before casing or plugging).
2. **Mining core holes before plugging.** More than 2,000 mining holes a year are drilled in Nevada (M20). We offer the operator a free stress and hydrogeology report (the same door as P11/P07/P08).
3. **Geotech and water-supply exploration holes** on private and state land.
4. Not ranch wells (cased, screened) and not old TG holes (grouted pipe, P11).

---

## 4. How much it shrinks the model's uncertainties

### 4.1 Calc

`P17_stress_calc.py` models a range-front fault set (strike N20E, dip 55-70) at 2 km in a normal-faulting column. Prior: SHmax azimuth +/-25 degrees, Shmin/Sv 0.62 +/- 0.07, SHmax/Sv 0.80 +/- 0.12, friction 0.6-0.85 (stands in for a World Stress Map / Lund Snee-Zoback draw). Posterior: azimuth +/-8 degrees, Shmin/Sv +/-0.03, SHmax/Sv +/-0.07. Results (calc):

- Prior P(critically stressed) = 0.12, entropy 0.52 bits.
- Slip tendency spread: sd 0.19 before, 0.08 after.
- Expected information gain on "critically stressed or not": **0.25 bits** per fault set; 82% of sites end with P below 0.2 or above 0.8.
- Shmin plus direction only, without a good SHmax magnitude: **0.24 bits**. So almost all the value is in Shmin magnitude and direction, which are the robust outputs. Good: we do not need the weak SHmax formula.
- If the shallow ratio extrapolates to 2 km with an extra +/-0.05 error: gain falls to **0.14 bits**. Extrapolation quality is the lever.
- Friction is still unmeasured and is now the main residual. Core friction tests or the P11 flowing-fracture test (Barton-Zoback-Moos) pin it down.

### 4.2 Mapping to ranked uncertainties

| Rank | Uncertainty | Effect of P17 |
|---|---|---|
| 2 | Permeability class / flow per well (about 10x MWe) | The critically-stressed prior per fault set, which M30 identified as the noisiest layer. At a tested prospect I estimate it removes about 20-35% of the log-variance of the permeability class prior that comes from structure (calc from the 0.14-0.25 bit gain; unverified mapping to class). It does not measure transmissivity; P11 does. Together they test Barton-Zoback-Moos in each hole. Regionally, maybe 5-10% of the rank-2 band in year one, rising as a stress GP fills in (unverified). |
| 1 | Detection gap, deep or lidded catch rate | Small. It does not find systems. It sharpens the "is this structure open" covariate in CREAM-COX, which helps separate "cold structure" from "hot but missed" (indirect). |
| 6 | Upflow location | Small to moderate. Dilation tendency on fault intersections points to where upflow focuses (M11 step-overs). Measured stress narrows which intersection. |
| 9 | Recovery factor | Small. Shmin and fracture normal stress feed stimulation and injection pressure limits for EGS-style recovery. |
| EGS block grade (not in the hydrothermal list, but it is the rights product) | Large. Stress regime, Shmin gradient, SHmax direction are 2 of the 5 EGS block inputs in H12. Today they come only from deep wells. |

In VOI-Bank terms, the EVSI per dollar is highest (a) at the confirmation stage of the top 5-10% of hydrothermal prospects, run in the same hole as P11, and (b) on one or two "anchor" holes per EGS province before a BLM sale, where one measurement informs many parcels.

### 4.3 Model integration

- Represent stress as a spatial field: SHmax azimuth (circular GP) and Shmin/Sv and SHmax/Sv ratios (GP with a depth trend), fitted to World Stress Map, focal mechanisms (M12, P03 nodes), breakouts from extracted logs, and P17 points as high-precision observations with a depth-extrapolation error term.
- Draw stress per HMC sample, compute slip and dilation tendency per fault segment, and feed P(critically stressed) and its recency interaction (M30) into the permeability class prior in THERMOS-B.
- GHOST Tier 1 ranks P17 against P11, P03 and P01 in-silico by EIG per dollar before buying anything.

---

## 5. Rights edge

- **EGS auctions.** The Utah step-up from $1-4/ac to $111/ac average and $1,207/ac top (H12; https://www.sltrib.com/news/environment/2025/04/11/utah-renewable-energy-blm-sale; https://www.thinkgeoenergy.com/blm-receives-record-breaking-24m-in-winning-bids-in-utah-geothermal-lease-sale/) means bidders are pricing blind on stress. One anchor hole on private or SITLA land next to a nominated block gives regime, Shmin gradient and SHmax direction for the surrounding 10-30 km (calc, valid away from province edges). We bid only where stress favours stimulation (low Shmin/Sv, SHmax direction that lets laterals cross many fractures) and skip blocks that will be expensive to stimulate. Example arithmetic: avoiding overpaying by $100/ac on one 2,560 ac parcel is $256k, more than the whole kit (calc).
- **Private and state first.** The kit cannot run on BLM land as casual use (injection changes the hole; P11 note on IM 2026-024). On federal land it needs a geothermal exploration notice under 43 CFR 3250 or a mining Plan/Notice under 3809 via the operator (unverified). So we run it on private ranch land (where we sign the heat option on the same visit, the P01 logic) or state trust land, then use the result to price nearby BLM parcels.
- **Farm-out and nomination.** A measured stress report is a standard input to EGS well design. Fervo, Sage, Quaise and Ormat would otherwise wait for their first deep well. Packaging it with temperature (P01/P16) and permeability (P11) supports a higher carry or override on rights we already hold (unverified premium).
- **Leak risk.** Nominating parcels and filing exploration notices reveals interest. Stress tests on private land do not.

---

## 6. Risks

1. **Hole supply ("too small").** Open, competent, uncased hole at 300-800 m is scarce. If we drill fewer than about 10-15 holes a year and mines do not cooperate, the kit is idle. Mitigation: it rides on the P11/P16 trailer, so idle cost is low.
2. **Shallow-to-deep extrapolation.** If Shmin/Sv at 500 m does not predict 2-4 km within about +/-0.05, the gain halves (calc). Desk test first.
3. **High-pressure slim packers.** 35 MPa differential in a 76 mm hole is a specialist part. Element failures and stuck packers happen. Budget $15-30k per lost-in-hole event (unverified).
4. **Permits and water.** Injection tests may need state UIC or water-use clearance in some states (unverified). Tiny volumes (1-2 m3) should be minor.
5. **Fractured rock.** In fault-zone holes, classic HF intervals are rare; HTPF needs well-spread fracture orientations. Steep-only fracture sets make the tensor poorly constrained.
6. **Buyer pull.** EGS developers may value temperature and rock far above stress. If buyers do not pay for stress, the rights edge reduces to our own bid discipline.
7. **Skill.** Shut-in picking and HTPF inversion need an experienced rock-mechanics engineer. Hire a contractor (MeSy/Solexperts-type) for the first 5 holes.

---

## 7. First test

**Desk, weeks 0-4, under $3k:**
1. Compile public stress profiles with both shallow (<1 km) and deep (>2 km) points in the Basin and Range and similar crust: Utah FORGE (GDR submission 1570 and the 58-32 minifrac), Yucca Mountain/NTS hydrofracs (Stock et al. 1985), Dixie Valley (Hickman et al.), Coso and Long Valley if available (unverified availability). Fit Shmin/Sv against depth with site random effects.
2. Score: does the 300-800 m value predict the 2-3 km value? **Pass if residual sd <= 0.05 in Shmin/Sv and SHmax direction within 15 degrees. Kill or downgrade to EGS-only if sd > 0.08.**
3. Run `P17_stress_calc.py` style VOI inside GHOST Tier 1 on 20 synthetic prospects to compare EIG/$ against P11 and P03 focal mechanisms.

**Field, months 2-4, about $40-70k (unverified):**
4. Rent a contractor hydrofrac crew plus a televiewer. Test one open core hole near FORGE/Milford (stress already known at depth) and one at a known blind Nevada system with mapped productive and tight fault segments. Pass if the shallow measurement reproduces the FORGE gradient within 0.05 and correctly ranks the productive segment's fault as more critically stressed.
5. Only then build the lean v1 and fold it into the P16 trailer.

---

## 8. Self-scores (1-5)

- **model_uncertainty_alpha: 3.** Real but local gain on rank 2's structural prior (0.14-0.25 bits per fault set, slip-tendency sd 0.19 -> 0.08, calc). Does not touch rank 1. Spatial correlation of stress spreads its value wider than P11.
- **rights_alpha: 3.5.** Direct pricing edge on EGS auctions in provinces with no deep stress data. Not casual use on BLM, so it works through adjacent private and state land.
- **buildability: 3.** Mostly off-the-shelf or rentable, but the 35 MPa slim packer and HTPF interpretation are specialist. 8-12 weeks for a lean v1 with a contractor partner.
- **cost_scale: 2.5.** $90-160k lean, $12-35k per hole, bound to open-hole supply. One anchor hole informs many parcels, which helps.
- **moat: 3.5.** Methods are public and 40 years old, but nobody runs them pre-lease across many prospects. The growing set of shallow-stress points paired with buyers' later deep wells is ours.

---

## Sources

With URLs (carried from earlier repo files):
- H12 lease prices: https://www.sltrib.com/news/environment/2025/04/11/utah-renewable-energy-blm-sale ; https://www.thinkgeoenergy.com/blm-receives-record-breaking-24m-in-winning-bids-in-utah-geothermal-lease-sale/
- FORGE stress and 58-32: https://gdr.openei.org/files/1209/ARMA2019_JMoore-FORGE.pdf (fetch blocked this turn) ; minifrac data https://gdr.openei.org/submissions/1570
- Stress characterization practice: https://www.weatherford.com/documents/papers/2019/increasing-reliability-of-stress-characterization-through-optimum-design-and-sensitivity-analysis-of/
- Faulds 2013 slip/dilation tendency: https://www.osti.gov/biblio/1136720

From memory, unverified, check before use: Hubbert and Willis 1957; Haimson and Fairhurst 1967; Cornet and Valette 1984 (JGR); Haimson and Cornet 2003 (IJRMMS 40:1011, ISRM suggested methods); Ito et al. 1999 and Rutqvist et al. 2000 on reopening pressure; Stock, Healy, Hickman and Zoback 1985 (JGR, Yucca Mountain); Hickman, Zoback and Benoit 1998 and Hickman et al. 2000 (Dixie Valley); Lund Snee and Zoback 2020; vendor names and all part prices.

Calc: `P17_stress_calc.py` (this folder).
