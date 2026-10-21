# D02: Oklahoma (OCC/OGS) and Kansas (KGS) well databases, and Mid-Continent geothermal potential

**Method note.** The shared WebSearch budget for this run was already used up (0 searches were available to this agent), so literature search was not possible. Instead I **downloaded the primary bulk files** from KGS and OCC and parsed them myself. All counts below marked "(computed)" are my own tallies from those files on 2026-10-21. Literature context (Harrison 1983, NGDS, Stanford 2024) comes from sibling file L09 and is cited there. Anything else is marked (unverified).

---

## 1. Kansas Geological Survey (KGS): the most machine-legible state archive in the US Mid-Continent

### 1.1 What exists
- **Master well list:** KGS reports a "Total Count of Wells" of **467,933** oil-and-gas-related, non-workover records ([KGS well stats](https://www.kgs.ku.edu/PRS/wellStats.html)). New drilling is now small: **1,515 new wells in 2023, 1,492 in 2024, 933 in 2025, and 454 in 2026 YTD** (to Oct 9). That makes it a legacy archive, not a live data stream.
- **Digital LAS logs:** the KGS log page cites **21,780** LAS wells (12/31/2024) ([KGS LAS](https://www.kgs.ku.edu/Magellan/Logs/index.html)). The per-year LAS archive listing sums to **28,908 files** for 1999–2026 (computed; the archives may overlap) ([KGS LAS archive](https://www.kgs.ku.edu/PRS/Scans/Log_Summary/index.html)).
- **Scanned wireline logs (TIFF):** there is a bulk index, `ks_elog_scans.zip` ([KGS scan page](https://www.kgs.ku.edu/Magellan/Elog/scan.html); file at https://www.kgs.ku.edu/PRS/Ora_Archive/ks_elog_scans.zip, updated 9 Oct 2026). Parsing it gives (computed):
  - **367,768 scanned log records** across **148,969 wells**. Each record has lat/long, TD, formation at TD, logger, tool, log top and bottom, and a TIFF URL.
  - **A `BHT` field, hand-keyed by KGS from log headers.** **74,299 wells have at least one BHT**, for **212,089 BHT readings** in total.
  - **6,950 wells have more than one distinct BHT** (different runs or depths). That is the raw material for Horner-type corrections, if run times can be recovered from the TIFF headers.
- **DST database:** "scans and digital data", with a bulk ZIP of all DST wells (current 1 Sep 2025) ([KGS DST](https://apps.kgs.ku.edu/web/DST/)). DST temperatures are usually closer to equilibrium than log BHTs. The fields in the ZIP were not checked here (unverified).
- **Also available:** tops, core analyses, brine analyses and production ([KGS PetroDB](https://www.kgs.ku.edu/PRS/petroDB.html)).

### 1.2 What the Kansas data says about heat (computed from the KGS scan index)
- Readings with log-bottom >1,500 ft: **n = 205,721**. **Median BHT is 116 °F (47 °C)** at a **median log-bottom depth of 4,375 ft (1.33 km)**.
- Apparent (uncorrected) gradient, assuming a 57 °F surface: **p5 / p25 / p50 / p75 / p95 = 1.08 / 1.29 / 1.40 / 1.51 / 1.71 °F per 100 ft**. The median is **about 25.6 °C/km**. Raw BHTs read cold by about 10–25 °C (L09), so the true median is likely **about 28–33 °C/km** (inference).
- **The hot tail is thin.** Only **215 wells** have a recorded BHT ≥150 °F (66 °C), **28 wells** ≥175 °F, and **10 wells** ≥200 °F. A few of those are probably keying errors: for example, 214 °F at 784 ft log-bottom is implausible.
- **The wells are shallow.** Only **15,129 wells** in the scan index reach ≥5,000 ft, **168** reach ≥8,000 ft, and **1** reaches ≥10,000 ft. The deepest BHT well recorded (260 °F, about 9,800 ft) is in Comanche/Barber County (37.34N, −99.43W), on the north flank of the Anadarko Basin.
- **Basement is reachable and sampled.** **653 wells** reach TD in Precambrian or granite (excluding granite wash), and **472** of them have a BHT. That gives a free regional calibration set for basement heat flow, which is the EGS host rock. Precambrian basement is roughly 1–3 km deep across most of Kansas (unverified).

**Verdict on Kansas:** this is a superb dataset (digitised BHTs at about 74k wells, with TIFFs behind each), but the resource is **low-enthalpy**. Nothing in the existing wells is hot enough for power. Power would need EGS at about 5–7 km at roughly 30 °C/km to reach 150–200 °C, which means new deep drilling into basement. Kansas fits **direct use / district heat / geothermal heat pumps** and Kansas data fits **training and calibrating** a BHT-correction model. It is not a land-bank target for a power resource. Sibling search note: the DOE Geothermal Data Repository returns **0 results for "Kansas"** ([GDR search](https://gdr.openei.org/search?q=Kansas)), so Kansas is essentially untouched by the geothermal community.

---

## 2. Oklahoma: OCC (regulator) and OGS (survey)

### 2.1 What exists
- **OCC RBDMS well file:** a nightly-updated CSV ([OCC data page](https://oklahoma.gov/occ/divisions/oil-gas/oil-gas-data.html); file at https://oklahoma.gov/content/dam/ok/en/occ/documents/og/ogdatafiles/rbdms-wells.csv). Parsed on 2026-10-21 (computed):
  - **457,186 wells**, every one with a `WELL_RECORDS_DOCS` link into the OCC imaged well-records system (public.occ.ok.gov Laserfiche).
  - By status: **247,647 plugged & abandoned**, **129,188 active**, **45,558 never-drilled permits**, **18,060 orphan**, **1,319 temporarily abandoned**.
  - By type: **180,803 oil**, **74,558 gas**, **84,903 dry**.
  - **The RBDMS file has no depth, log or BHT fields.** Everything thermal sits in the scanned PDF/TIFF forms (1002A completion reports, logs). This is the Saskatchewan "public but illegible" condition in its purest form.
- **OCC completions master (2010–present):** 203,381 formation-level rows covering **37,490 unique wells** (computed) ([same OCC page](https://oklahoma.gov/occ/divisions/oil-gas/oil-gas-data.html)).
  - **17,472 straight holes** (median TD 4,028 ft), of which **1,192 are ≥10,000 ft**, **192 are ≥15,000 ft** and **33 are ≥20,000 ft**. **17,271 are horizontals**.
  - An `Open_Hole_Logs` flag is "Yes" for **13,846 wells**. Even in the modern era there is **no temperature field**, so BHTs must come from the log images.
- **OGS / OPIC (Oklahoma Petroleum Information Center):** **>100 miles of core from almost 10,000 wells** and **cuttings from >50,000 wells**, plus a well-log library with no count given ([OPIC](https://www.ou.edu/ogs/opic)). OGS's data page lists oil and gas, brine data, well pressure, fault database and slimhole cores, but **no geothermal or BHT dataset** ([OGS data](https://www.ou.edu/ogs/data)).
- **Oklahoma gave the industry its standard BHT correction.** Harrison, Luza, Prater & Cheung (1983), OGS SP 83-1, calibrated the depth polynomial on Oklahoma DST temperatures to about 3 km. It is still used by SMU and in Stanford's 2024 400k-BHT national model (L09). Oklahoma's own BHT archive is therefore **already partly harvested into national compilations, but only as single, Harrison-corrected, metadata-poor points**.
- The DOE Geothermal Data Repository returns 36 Oklahoma-tagged items, almost all **lab work by OSU/OU** (ionic EGS fluids, FORGE rock mechanics) and **no Oklahoma resource datasets** ([GDR search](https://gdr.openei.org/search?q=Oklahoma)).

### 2.2 Oklahoma's geothermal potential (mostly literature-level, partly unverified)
- **Anadarko Basin.** This is one of the deepest US onshore sedimentary basins. Sediment is >12 km thick in the deep basin and wells reach >30,000 ft; the Bertha Rogers well reached 31,441 ft in 1974 (unverified here). NREL's sedimentary-basin assessment (Porro et al. 2012, in L10) includes the **Anadarko** among 15 basins with volumetric heat in place. Deep-basin temperatures of roughly **150–200+ °C at 5–7 km** are plausible (unverified; Gallardo & Blackwell 1999, AAPG Bull. 83(2), was paywalled/403).
- **The OCC file shows ~1,200 modern straight holes ≥10,000 ft and 33 ≥20,000 ft since 2010 alone** (computed). Pre-2010 deep Anadarko wells behind the scanned records likely number several thousand more (unverified).
- **Co-produced and Arbuckle brine.** Oklahoma has a huge legacy of produced water and Arbuckle saltwater disposal. That is a hot-water-handling infrastructure analogue (L11), but it also brings the **induced-seismicity history** (the 2016 Pawnee M5.8; unverified here). That history raises permitting risk for any EGS stimulation or large reinjection in Oklahoma.
- **University of Oklahoma at Tuttle** is a DOE-backed demo using legacy oil and gas wells for school heating and cooling (L11). It is direct use, not power.
- **Rights:** Oklahoma's geothermal ownership law (surface vs mineral estate) was **not verified in this pass**. It is the critical diligence item, given 247k plugged and 18k orphan wells on split estates (unverified).

---

## 3. Mid-Continent geothermal: overall read
| | Kansas | Oklahoma |
|---|---|---|
| Wells in state DB | 467,933 (KGS) | 457,186 (OCC RBDMS) |
| Digitised BHT | **74,299 wells / 212k readings** (KGS index) | None in OCC tables; some in national compilations via SMU/AASG |
| Log images | 148,969 wells / 367,768 scans (TIFF, bulk index) | Imaged records linked for all 457k wells (Laserfiche, no bulk index) |
| Typical depth | median log-bottom ~4,400 ft; 168 wells ≥8,000 ft | deep Anadarko; ≥1,192 straight holes ≥10k ft since 2010 |
| Resource class | low-enthalpy, direct use; EGS only with new deep wells | Anadarko deep sedimentary/EGS at 4–7 km; co-produced; direct use |
| Geothermal community attention | essentially zero (GDR: 0 hits) | lab-scale only (GDR: OSU/OU lab data) |

---

## 4. Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **The data substrate is real and big, and it is free to bulk-download.** Kansas has already keyed BHTs for 74k wells, linked to 368k TIFFs. Oklahoma has 457k wells, each linked to scanned records with no thermal fields. That is the exact Saskatchewan pattern: legally public, physically illegible. OCR of log headers (BHT, time since circulation, mud type, run number) turns single Harrison points into Horner-correctable multi-point data. The 6,950 Kansas wells with multiple BHTs, plus DSTs, are a ready **training and validation set** for an ML correction that can then be applied to Oklahoma's and Texas's unindexed images.
2. **But Kansas fails the "too small / too cold" test as an asset play.** The median is ~47 °C at 1.3 km, and only 10 wells are ≥200 °F. There is no power resource to buy before proof. Kansas belongs in the **data moat** (calibration), not the **land bank**.
3. **Oklahoma's Anadarko is the Mid-Continent asset candidate.** It has a deep, hot sedimentary section, thousands of deep wells with images, a dense pipeline/transmission and gas-plant footprint, and fragmented private mineral and surface estates where rights can be leased cheaply before proof. The step-up buyers would be EGS developers (Fervo/Sage-style), utilities, and data-centre offtakers in the OK/TX power market. Risks to score on plausibility, not as kills: seismicity-driven permitting, unclear geothermal-estate law, and low gradients relative to the Great Basin.
4. **The gap vs Zanskar is clear.** Zanskar works on **convective hydrothermal discovery in the Great Basin on BLM leases**. Its whole auction position is about 50k acres in Nevada, plus Lightning Dock in NM (Z04). It does not touch **private-mineral, O&G-dense sedimentary basins**, where the edge is reading **millions of legacy well images** rather than running new geophysics. The Mid-Continent (plus Texas, sibling R07) is uncontested white space: zero GDR resource datasets, no Zanskar land, and national temperature maps still built on single uncorrected Oklahoma-calibrated points.
5. **Recommended shape.** Build the BHT-correction model on Kansas (clean labels), deploy it on the Oklahoma and Texas image archives, and rank deep Anadarko/Permian acreage by corrected 4–6 km temperature × permeability (from DST/core) × rights fragmentation. Lease private geothermal and mineral rights before publishing anything. Z04 shows that disclosure reprices adjacent land ~116× within weeks.

---

## Sources
- KGS well statistics (467,933 wells; drilling by year): https://www.kgs.ku.edu/PRS/wellStats.html
- KGS PetroDB index: https://www.kgs.ku.edu/PRS/petroDB.html
- KGS LAS logs (21,780 as of 12/31/2024): https://www.kgs.ku.edu/Magellan/Logs/index.html
- KGS LAS archives by year: https://www.kgs.ku.edu/PRS/Scans/Log_Summary/index.html
- KGS scanned-log index page and bulk file (BHT field): https://www.kgs.ku.edu/Magellan/Elog/scan.html ; https://www.kgs.ku.edu/PRS/Ora_Archive/ks_elog_scans.zip
- KGS DST database: https://apps.kgs.ku.edu/web/DST/
- KGS master well list: https://apps.kgs.ku.edu/web/qualified/index
- OCC oil and gas data files: https://oklahoma.gov/occ/divisions/oil-gas/oil-gas-data.html
- OCC RBDMS wells CSV: https://oklahoma.gov/content/dam/ok/en/occ/documents/og/ogdatafiles/rbdms-wells.csv
- OCC completions master: https://oklahoma.gov/content/dam/ok/en/occ/documents/og/ogdatafiles/completions-wells-formations-base.xlsx
- OGS OPIC holdings: https://www.ou.edu/ogs/opic
- OGS data page: https://www.ou.edu/ogs/data
- DOE GDR searches: https://gdr.openei.org/search?q=Oklahoma ; https://gdr.openei.org/search?q=Kansas
- Sibling files (literature, BHT corrections, Zanskar land): L09-temperature-at-depth.md, L10-sedimentary.md, L11-coproduced.md, Z04-land.md in /home/user/nuketime/research/geothermal/evidence/
