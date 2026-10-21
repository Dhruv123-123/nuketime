# B04: Market size. Geothermal capacity, forecasts, capex, investment flows, and what the land/resource layer is worth

**Method note.** The shared WebSearch budget for this run (200 calls) was used up before this file started, so I ran no new searches. I fetched primary pages directly where they loaded: ThinkGeoEnergy's country ranking, NREL (now NLR) ATB 2024, IRENA, EIA, DOE GeoVision, BLM, Rhodium, and ThinkGeoEnergy's IEA write-up. iea.org returned 403, so I could not open the IEA report itself. DOE Liftoff numbers come from sibling file L06, which read the full text via the CATF mirror. M&A $/MW figures come from sibling B01/B02, which fetched SEC filings. Every figure carries its source. Anything from memory is marked (unverified).

---

## 1. Installed capacity today

| Metric | Value | Source |
|---|---|---|
| Global installed, end-2024 | **16,873 MW** in 35 countries | ThinkGeoEnergy Top-10 2024 |
| Global installed, end-2024 (IRENA, net basis) | **15.4 GW**; only **0.4 GW added in 2024**; 13.0 GW at end-2020 | IRENA |
| US installed, end-2024 | **3,937 MW** (#1 globally, ~23%) | ThinkGeoEnergy |
| Next largest | Indonesia 2,653; Philippines 1,984; Türkiye 1,734; NZ 1,207; Kenya 985; Mexico 976; Italy 916; Iceland 786; Japan 601 MW | ThinkGeoEnergy |
| Top-10 share | ~93% of world capacity | ThinkGeoEnergy |
| US generation | ~**16 TWh**, ~**0.4%** of US utility-scale electricity (2025 prelim.) | EIA |
| US by state (generation share) | CA 68.6%, NV 24.7%, UT 3.0%, HI 1.6%, OR 1.2%, ID 0.5%, NM 0.4% | EIA |
| On BLM lands | **>2.65 GW**, **51 plants**; BLM manages leasing on ~**245M acres** (incl. 104M USFS) | BLM |
| US interconnection queue | ~**1.7 GW** geothermal | Rhodium |
| Global LCOE (weighted avg.) | $0.055/kWh (2010) rising to **$0.060/kWh (2024)** | IRENA |

**Read.** Geothermal is a small, slow incumbent. Global growth is about 0.4 GW a year, roughly 2.5%. Over ~65% of US federal-land geothermal sits on BLM ground (2.65 of 3.94 GW, calc). That makes the BLM lease the main "right" to acquire in the US, as the uranium mineral claim is in Saskatchewan.

## 2. Forecasts: 2030 / 2035 / 2050

### United States
| Source | 2030 | 2050 | Notes |
|---|---|---|---|
| DOE GeoVision (2019) | n/a | BAU ~6 GW; improved permitting 13 GW; **Technology Improvement 60 GW** (8.5% of US generation) | DOE GeoVision page; L06 |
| Enhanced Geothermal Shot update (NREL 2023) | n/a | **90 GW** | DOE GeoVision page |
| DOE Pathways to Commercial Liftoff: Next-Gen Geothermal (Mar 2024) | **2-5 GW next-gen by 2030**, ~100+ developments in 4-6 states, **$20-25B** capital | **90 GW base** (88-125 GW range); **130+ GW** if land for other renewables is restricted; **300+ GW** if flexibility/storage is valued. Needs **10+ GW/yr** by the 2040s and **$225-250B** of Phase-2 capital | L06 (CATF mirror of the DOE PDF) |
| Rhodium (data centres) | Geothermal could meet **up to 64%** of data-centre demand growth by the early 2030s, i.e. **15-17 GW** clustered, or all of it with best-resource siting; LCOE **$78-85/MWh** national (regional $49-111) | n/a | Rhodium |
| Heat pumps (GeoVision) | n/a | heating/cooling for 28M households | DOE |

The US technical resource is very large: ~7 TW accessible at <5 km and >70 TW at all depths (Rhodium, citing DOE). USGS (2008) puts **~30 GWe of undiscovered conventional hydrothermal** in the US. The 2025 NREL/UNR Great Basin estimate is **23 GW (P50) to 79.5 GW (P90)** of hidden hydrothermal (sibling L05). That hidden-hydrothermal pool is what Zanskar targets directly.

### Global
| Source | Figure |
|---|---|
| IEA, *The Future of Geothermal Energy* (Dec 2024) | Next-gen geothermal could reach **up to 800 GW** worldwide by 2050 and meet **~15% of global electricity demand growth to 2050**. Geothermal is ~**1%** of electricity today. Fewer than 30 countries have geothermal-specific policy, against 100+ with solar/wind policy (ThinkGeoEnergy summary of IEA) |
| IEA, same report (unverified, iea.org blocked) | Cumulative investment of about **$1 trillion by 2035** and **~$2.5 trillion by 2050** in the high case. Next-gen costs fall ~80% to ~**$50/MWh by 2035**. Up to ~80% of required skills and investment overlap with oil and gas |

**Read.** The base case is roughly 4x US growth by 2030 (16 GW to ~20+ GW globally). The upside case is ~23x US (90 GW) and ~50x global (800 GW) by 2050. The upside is driven mostly by EGS and next-gen. Hydrothermal is the near-term, cash-generating slice.

## 3. Capex per MW

### NREL (NLR) ATB 2024 overnight capital cost, base year
| Resource type | Average $/kW | Range |
|---|---|---|
| Hydrothermal flash (>=200 °C), identified | **4,350** | 3,091-5,922 |
| Hydrothermal flash, undiscovered | 3,738 | 3,307-4,412 |
| Hydrothermal binary (150-200 °C), identified | **9,483** | 4,882-38,108 |
| Hydrothermal binary, undiscovered | 7,425 | 6,759-8,298 |
| Hydrothermal 135-150 °C | 10,196 | 8,185-12,209 |
| Hydrothermal <135 °C | 18,956 | 12,685-26,440 |
| Near-field EGS flash | 5,469 | 4,542-7,161 |
| Near-field EGS binary | 10,395 | 7,877-13,456 |
| Deep EGS (two columns, presumably flash then binary) | 12,396 / 22,133 | 9,228-33,512 |

Source: https://atb.nlr.gov/electricity/2024/geothermal

Other reference points:
- Wikipedia/Bertani (2007): conventional plants cost about **€2-5M/MW**. A Nevada doublet supporting 4.5 MW cost ~$10M to drill, with a 20% failure rate.
- Liftoff Phase 1 is $20-25B for 2-5 GW, about **$5-10M/MW** (calc).
- Liftoff Phase 2 is $225-250B for ~85 GW, about **$2.6-2.9M/MW** (calc), which assumes learning-curve declines.

**Read.** A 50 MW flash plant is ~$220M of capex and a 20 MW binary plant ~$150-190M. The ATB lists undiscovered flash/binary as cheaper per kW than identified sites. ATB uses a separate exploration-risk model, but the size of the target hints at ML value: the best undiscovered sites are as good as or better than what the industry has already found.

## 4. Total investment flows

| Flow | Figure | Source |
|---|---|---|
| US to 2030 (Liftoff Phase 1) | **$20-25B** | L06 / DOE Liftoff |
| US to 2050 (Phase 2) | **$225-250B**, ~$245-275B total (calc) | L06 / DOE Liftoff |
| Global to 2035 / 2050 (IEA high case) | ~$1T / ~$2.5T | IEA (unverified) |
| Fervo | >$1.5B equity+debt+grants pre-IPO; $462M Series E (Google participated); IPO ~$1.9B raised at a ~**$7.7B** valuation | Wikipedia; B01/B02 (424B4, ESG Today) |
| Ormat | $750M base (up to $862.5M) 2031 converts, Mar 2026; $25M into Sage's $97M Series B | B02 (SEC 8-K, ThinkGeoEnergy) |
| Zanskar | $115M Series C, **~$180M total equity**; owns Lightning Dock (NM, ~15 MW); NV Energy 100 MW PPA | B01/B02 |
| Ormat M&A (operating plants) | Terra-Gen 2021 ~$377-429M EV for ~67.5-76 MW (**~$5.6M/MW**); U.S. Geothermal 2018 $193.6M for ~45 MW (**$4.3M/MW**); Blue Mountain 2025 $88.7M for 20 MW (**$4.4M/MW**); Enel NA 2023 $271M for ~150 MW blended (**~$1.8M/MW**) | B01/B02 (SEC filings) |

## 5. What the land/resource layer is worth

This is the layer a Terranox-shape company owns. It has to be valued at three marks.

**(a) Bare right, cost basis.**
- Fervo assembled ~**595,900 acres at ~$4/acre**, about $2.4M in total (Fervo 424B4, via B01).
- 2025 BLM competitive max bids reached **$344 and $410/acre**. Fervo also cites reports that developers "paid hundreds of dollars per acre in 2025" for positions that failed its screens (B01).
- At ~150 acres/MW (~3,000 acres per 20 MW, unverified), land costs **$600/MW at $4/acre** and **~$60k/MW at $400/acre** (calc).
- Against $4.35M/MW of capex, that is **0.01%-1.4%** of project cost. Land is almost free relative to capex. The price swings 100x between disciplined screening and auction-chasing.

**(b) Confirmed resource (the step-up Terranox would sell).**
- Implied resource-sale value is ~**$0.1-0.5M/MW** (B02, unverified).
- A $5/MWh royalty precedent (Centaurus) has a PV of about **$0.4M/MW** (B01/B02).
- On these figures, the confirmed-resource layer is **~2-10% of capex**: $0.1-0.5M against a $4-6M/MW operating-plant mark.
- USG's undrilled development portfolio (~100 MW) was valued at only ~$10M in liquidation (~$0.1M/MW). Greenfields bundled into the Terra-Gen and Enel deals were priced at zero.
- Value only shows up once a resource is **drilled to temperature, interconnection-positioned and buyer-trusted**.

**(c) Public-market mark on rights + PPAs.**
- Fervo's ~$7.7B valuation on ~658 MW of PPAs and ~596k acres implies **~$11.7M per contracted MW** or **~$13k per leased acre** (calc).
- That is ~3,000x its $4/acre cost basis (calc). Fervo is the clearest evidence that the market capitalises the resource+PPA layer far above capex.

**Sizing the layer (calc, on plausibility):**
- US hidden hydrothermal of 23-30 GW × $0.1-0.5M/MW gives **$2.3-15B** of resource-layer value.
- US 90 GW by 2050 × $0.1-0.5M/MW gives **$9-45B**. At 10 GW/yr in the 2040s, that is **$1-5B per year** of resource value changing hands.
- Global 800 GW × the same range gives **$80-400B**.
- Separately, a $5/MWh royalty on 90 GW at a 90% capacity factor (~710 TWh/yr) is **~$3.5B/yr** of royalty cash flow (calc).

Not "too small": even the hydrothermal-only US slice is multi-billion, and the EGS-driven upside is tens of billions.

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **The market is large, but most dollars sit in capex, not land.** US capital need through 2050 is ~$245-275B, and IEA's global high case is ~$2.5T (unverified). A rights/resource owner captures the ~2-10% de-risking slice, about $9-45B in the US. That is enough for a venture-scale outcome, provided the company takes positions at scale.
2. **The arbitrage is real and wide.** Land costs $4-410/acre. Confirmed resource is worth ~$0.1-0.5M/MW. Fervo's public mark implies ~$13k/acre on contracted ground. The spread between a screened bare right and a confirmed, interconnect-positioned resource is 25-100x+ (B01). This is the Terranox pattern: buy before proof, own the step-up.
3. **Zanskar's gap.**
   - Zanskar is a vertically integrated explorer-developer-operator: ~$180M of equity, Lightning Dock, a 100 MW NV Energy PPA and roughly six planned 20 MW plants. Each MW it finds, it must also build, at ~$4-10M/MW.
   - Its capital caps how many prospects it can carry. With ~$180M, it can carry only a few plants' worth of resource.
   - The space it leaves open is a **capital-light resource bank**. That company would screen basin-wide, lock up tens or hundreds of thousands of acres at $2-10/acre, drill cheap temperature-gradient holes to confirm, and **sell or farm out confirmed blocks**, keeping a $/MWh override, to Fervo, Ormat, utilities and hyperscalers. Each of those buyers needs many GW, on the 10 GW/yr scale, and none screens every basin.
   - This also works in places Zanskar is not focused on: sedimentary basins with dense oil and gas well data (Texas, Oklahoma), and state and private rights.
4. **Timing tailwinds.**
   - Data-centre demand gives a credible 15-17 GW by the early 2030s (Rhodium).
   - PPAs are now >$100/MWh against $60-80 previously (B02).
   - Interconnection is scarce, with only ~1.7 GW in the queue (Rhodium), so a resource with an interconnection position is the premium asset.
   - The 2025 bidding spike shows the bare-right window is closing, which favours moving fast.
5. **Risks to the market thesis.**
   - Growth is slow, ~0.4 GW/yr globally (IRENA).
   - Undrilled greenfields have historically sold for near zero (USG, Terra-Gen, Enel).
   - Raser held 250k+ acres and still went bankrupt, with equity cancelled. A land bank with no confirmation step and no pre-agreed exit buyers goes to zero.
   - The model works only if drilling-to-temperature confirmation is cheap and buyers trust the data package.

## Sources
- ThinkGeoEnergy, Top 10 geothermal countries 2024: https://www.thinkgeoenergy.com/thinkgeoenergys-top-10-geothermal-countries-2024-power/
- IRENA geothermal: https://www.irena.org/Energy-Transition/Technology/Geothermal-energy
- EIA, use of geothermal energy: https://www.eia.gov/energyexplained/geothermal/use-of-geothermal-energy.php
- BLM geothermal program: https://www.blm.gov/programs/energy-and-minerals/renewable-energy/geothermal-energy
- DOE GeoVision: https://www.energy.gov/eere/geothermal/geovision
- DOE Pathways to Commercial Liftoff: Next-Gen Geothermal (CATF mirror): https://cdn.catf.us/wp-content/uploads/2025/06/09154348/doe-liftoff-nextgen-geothermal.pdf
- ThinkGeoEnergy summary of Liftoff: https://www.thinkgeoenergy.com/us-doe-publishes-report-on-commercial-liftoff-of-next-generation-geothermal/
- NREL/NLR ATB 2024 geothermal: https://atb.nlr.gov/electricity/2024/geothermal
- IEA report landing page (403 on fetch): https://www.iea.org/reports/the-future-of-geothermal-energy
- ThinkGeoEnergy on the IEA report: https://www.thinkgeoenergy.com/iea-publishes-special-report-on-the-future-of-geothermal-energy/
- Rhodium Group, geothermal and data centres: https://rhg.com/research/geothermal-data-center-electricity-demand/
- USGS 2008 assessment: https://pubs.usgs.gov/fs/2008/3082/
- USGS 2025 Great Basin EGS assessment: https://pubs.usgs.gov/fs/2025/3027/fs20253027.pdf
- Ormat Q2-2021 release (Terra-Gen): https://www.sec.gov/Archives/edgar/data/1296445/000143774921018710/ex_272176.htm
- Ormat FY2021 10-K: https://www.sec.gov/Archives/edgar/data/1296445/000143774922004440/ora20211231_10k.htm
- Ormat-Enel 8-K: https://www.sec.gov/Archives/edgar/data/1296445/000143774923028865/ex_585361.htm
- Ormat 2031 converts 8-K: https://www.sec.gov/Archives/edgar/data/1296445/000121390026032467/ea028270301ex99-1.htm
- Fervo IPO (ESG Today): https://www.esgtoday.com/geothermal-developer-fervo-energy-raises-1-9-billion-in-upsized-ipo/
- Fervo Series E: https://www.thinkgeoenergy.com/google-joins-usd-462m-funding-round-for-fervo-energy/
- Fervo (Wikipedia): https://en.wikipedia.org/wiki/Fervo_Energy
- Zanskar Series C: https://zanskargeothermal.substack.com/p/zanskar-raises-115m-series-c-following
- Zanskar acquires Lightning Dock: https://www.thinkgeoenergy.com/zanskar-acquires-lightning-dock-geothermal-power-plant-new-mexico/
- Sage Series B: https://www.thinkgeoenergy.com/sage-geosystems-closes-97-million-series-b-funding-round-to-support-pressure-geothermal-deployment/
- Geothermal power (Wikipedia; Bertani 2007 capex): https://en.wikipedia.org/wiki/Geothermal_power
