# Geothermal dataset catalogue: shared schema (v1)

Owner: lead thread "Design the elite geothermal prospecting model" (branch `claude/project-thread-wxx4ln`).
Used by the four survey threads (subsurface; remote sensing and surface; business and land; global and labelled outcomes). The lead thread merges every catalogue into `research/geothermal/datasets/INDEX.md`, so **keep to this schema exactly**.

## Where to write

- One catalogue per thread: `research/geothermal/datasets/<THREAD_KEY>/CATALOGUE.md` plus a machine-readable `CATALOGUE.jsonl` (one JSON object per line, same fields).
- Thread keys: `subsurface`, `surface`, `business`, `global`.
- ID prefix per thread so IDs never collide: `SUB-001`, `SRF-001`, `BIZ-001`, `GLB-001`.
- If two threads find the same dataset, both may list it; the merge keeps one and records both IDs in `aliases`.

## Fields (every entry)

| # | Field | Type | What to write |
|---|---|---|---|
| 1 | `id` | string | `SUB-001` etc. |
| 2 | `name` | string | Official dataset name. |
| 3 | `owner` | string | Agency, company or project that publishes it. |
| 4 | `url` | string | Landing page or direct download/API. Add more in `urls_extra`. |
| 5 | `class` | enum | One of the **dataset classes** below. One primary class; extra in `tags`. |
| 6 | `coverage` | string | Geography (e.g. "Great Basin", "CONUS", "Nevada", "global") and time span. |
| 7 | `resolution` | string | Spatial (grid cell, station spacing, point count) and vertical or temporal resolution. |
| 8 | `format` | string | e.g. GeoTIFF, shapefile, CSV, LAS, SEG-Y, PDF scans, REST API, netCDF, HDF5, Zarr. |
| 9 | `access` | enum + note | `open` / `open-registration` / `request` / `paid` / `confidential-timed` (state when it opens) / `foia`. Add licence (CC-BY, public domain, terms) in a note. |
| 10 | `size` | string | Approximate volume (MB/GB/TB, or record count). "unknown" allowed. |
| 11 | `update_cadence` | string | static / annual / monthly / live / one-off campaign; last update date if known. |
| 12 | `signal` | string | What it tells us about geothermal (heat, permeability/structure, fluid, cap/seal, masking, cost, rights, market, outcome label). One or two sentences, concrete. |
| 13 | `signal_tags` | list | Any of: `heat`, `heat_flow`, `temperature_at_depth`, `permeability`, `structure`, `stress`, `fluid_chemistry`, `alteration`, `surface_manifestation`, `seismicity`, `deformation`, `geophysics_mt`, `geophysics_gravity`, `geophysics_magnetic`, `geophysics_seismic`, `lithology`, `masking_cover`, `hydrology`, `label_positive`, `label_negative`, `search_effort`, `land_rights`, `land_status`, `grid`, `market_price`, `cost`, `permitting`, `environmental_constraint`, `ownership`, `transaction`, `well_record`, `text_corpus`, `foundation_model_input`. |
| 14 | `literature_uses` | list | Papers/reports that used it (short cite + link). Note which PFA/ML studies (Nevada PFA, INGENIOUS, GeoDAWN, Faulds et al., Zanskar, Fervo, etc.). |
| 15 | `model_entry` | string | How it enters the model: `feature-raster`, `point-observation` (with likelihood), `label`, `effort/thinning layer`, `prior`, `constraint/mask`, `economic layer`, `text-to-extract`, `validation-holdout`, `foundation-model pretraining`. Say which latent variable it informs. |
| 16 | `quality_caveats` | string | Biases, gaps, datum issues, sparse sampling, survivorship (sites only measured where already promising), unit/depth inconsistencies. |
| 17 | `acquisition_effort` | enum + note | `S` = download now (< 1 day); `M` = scraping/parsing/registration (days); `L` = OCR/digitising/FOIA/negotiation (weeks); `XL` = commissioned or bought. Note the blocker. |
| 18 | `priority` | enum | `P0` must-have for the PoC; `P1` strong add; `P2` nice to have; `P3` reference only. |
| 19 | `cost_usd` | string | 0 if free; otherwise price or "unknown". |
| 20 | `verified` | bool + date | true only if an agent actually opened the URL / downloaded a sample this run. Record `verified_on`. |
| 21 | `notes` | string | Anything else: who else uses it (competitive), legal nuance, mirrors. |
| 22 | `aliases` | list | Other catalogue IDs for the same dataset (filled at merge). |

## Dataset classes (`class`)

| Class | Examples |
|---|---|
| `thermal` | heat-flow databases (SMU, USGS, IHFC), BHT/temperature logs, gradient holes, temperature-at-depth models, Curie depth |
| `wells` | geothermal/oil-gas/water/mining well records, logs, driller reports, core |
| `geophysics` | MT/EM, gravity, aeromagnetic, seismic reflection/refraction, airborne EM, GeoDAWN |
| `structure_stress` | Quaternary faults, fault slip/dilation tendency, stress maps (WSM), strain (GNSS), InSAR deformation |
| `seismicity` | earthquake catalogues, focal mechanisms, microseismic |
| `geology_geochem` | geologic maps, lithology, volcanic vents, geochemistry (springs, wells, geothermometers), isotopes (He, C), soil gas |
| `remote_sensing` | thermal IR (ASTER, Landsat, ECOSTRESS), hyperspectral alteration (EMIT, AVIRIS), SAR, DEM, vegetation/snow anomalies |
| `hydrology` | groundwater levels, springs, water rights, aquifers, recharge |
| `labels` | known resources, power plants, discoveries, dry holes, failed projects, assessments (USGS 2008 favourability) used as positive/negative labels |
| `land_rights` | BLM leases/nominations/auctions (MLRS, LR2000), state leases, private surface/mineral ownership, parcels, withdrawals |
| `constraints` | protected areas, sage grouse, tribal lands, military, cultural, wilderness, setbacks |
| `infrastructure_market` | transmission, substations, interconnection queues, LMP prices, PPAs, data-centre demand, roads |
| `cost_economics` | drilling cost, plant cost, NREL ATB, GETEM, project finance data |
| `corporate_transactions` | operator filings, M&A, lease sale results, company disclosures |
| `literature_text` | reports, theses, GRC/Stanford papers, OSTI, state survey scans (text to mine) |
| `global` | non-US national datasets (NZ, Iceland, Kenya, Indonesia, Philippines, Turkey, Mexico, Chile, Japan, Europe) |
| `models_products` | derived products: PFA maps, INGENIOUS favourability, temperature-at-depth grids, foundation-model embeddings |

## Markdown layout per entry (CATALOGUE.md)

```
### SUB-001 · SMU Geothermal Laboratory heat-flow database
- **Owner:** SMU Geothermal Lab · **URL:** ...
- **Class:** thermal · **Tags:** heat_flow, temperature_at_depth, well_record
- **Coverage / resolution:** CONUS, ~20k sites, 1960s-2010s / point data
- **Format / size / cadence:** CSV via GDR, ~50 MB, static (last 2013)
- **Access:** open (CC-BY 4.0) · **Effort:** S · **Priority:** P0 · **Cost:** 0 · **Verified:** yes 2026-10-24
- **Signal:** ...
- **Literature:** ...
- **Model entry:** point-observation (censored Gaussian on heat-flow latent), effort layer from site density
- **Caveats:** ...
- **Notes:** ...
```

## Catalogue header (top of each CATALOGUE.md)

1. Count of entries by class and by priority.
2. The 10 datasets this thread thinks matter most and why.
3. Gaps: data that should exist but does not (or is closed), and how AI could fill it (OCR, inference, sensing).
4. Sources searched (so the merge can see coverage).

## Hand-off

When committed and pushed, message the lead thread with the branch, the path and the entry count. The lead thread will fetch your branch and merge.
