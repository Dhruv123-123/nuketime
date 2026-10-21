# A05: Hidden heat in mines: flooded mines, hot mines, dewatering, and claim holders who don't know they sit on heat

*Research note, 2026-10-21.*

**Method caveat.** The shared WebSearch budget for this run (200 calls) was already used up when this agent started, so I could not run a single search. Everything below comes from three kinds of source:

- direct fetches of primary or near-primary pages: the NREL/NLR *Mining G.O.L.D.* report PDF, which I downloaded and text-extracted, LII copies of 30 USC 1003 and 43 CFR 3204, OSTI and Crossref metadata, and Wikipedia pages for context;
- sourced material in sibling files D06, R02, R13, Z01 and Z04;
- my own background knowledge, which is **marked (unverified)** every time.

Several fetches failed: Mijnwater (503), the UK Coal Authority page (404), GeoScienceWorld (403), and my guessed USGS Carlin dewatering report URLs. A follow-up pass with search enabled should fill the Carlin pumping-rate and UK/NL mine-water numbers.

## 1. Bottom line

There are two very different "heat in mines" plays. Only one of them fits a Terranox-shape company.

1. **Flooded cold-district mines** (coal fields in the UK, Netherlands and Nova Scotia; Appalachian and Midwest coal; Shield metal mines).
   - The water is **12-30 °C**. It is a heat-pump source for district heating, not a power resource.
   - Springhill, NS runs at about 18 °C. Heerlen began in 2008 serving about 200 homes plus commercial buildings.
   - The asset is a local utility with a small ticket, and it belongs to whoever owns the closed mine (often the state). Against the "too small" kill rule this **fails as a core** business. At most it is a side line.
2. **Hot mines in the Great Basin and in active-margin epithermal districts** (Carlin trend, Getchell, Comstock, Florida Canyon, Lihir).
   - Here mining has *already drilled, pumped and measured* hot water at power-grade temperatures:
     - **330 °F (~166 °C) at Barrick's Meikle mine** on the Carlin trend;
     - **223 °F at 160 gpm** from Florida Canyon water-supply wells;
     - **190 °F with geysering** at the McGinness Hills mineral holes.
   - Mining dewatering wells are "constructed similarly to typical full-sized geothermal wells" (NREL 2022). Lihir in PNG turned pit-depressurisation steam into a **50-56 MW** plant.
   - This is the real fit: legible-by-ML records of heat that someone else paid to find, on land where the geothermal right is often unleased.

The decisive legal fact is that **a mining claim does not include the geothermal estate.** Geothermal on federal land is leased separately under the Geothermal Steam Act. The Act also gives a **noncompetitive side door to mining-claim holders who have an approved plan of operations** (30 USC 1003(b)(3); 43 CFR 3204.12), at **$1/acre/yr** advance rent plus a processing fee of about $505-520 (R02). The claim holder therefore holds a latent, cheap, auction-free option on the heat under its claim, and most claim holders neither know about it nor price it.

That is a Terranox-style information and tenure arbitrage. It is also a door that Zanskar's auction-driven land strategy (Z04) does not use, as far as public records show.

## 2. Hot mines: the evidence base

### 2.1 Carlin trend (Barrick/Newmont Nevada Gold Mines)

- **Meikle (Goldstrike complex):** ground and water temperatures of **330 °F** were encountered. NREL used this as the reference resource for its mining-geothermal techno-economic scenario: 330 °F at about 2,000 ft, pumped wells averaging about 1,750 gpm, feeding a 20 MW air-cooled binary plant. The source behind it is Proulx and Scovira (2001), *Drilling and blasting in hot and reactive ground conditions at Barrick Goldstrike's Meikle mine*, CIM Bulletin 94:71-74, as cited in NREL/TP-6A20-81946 pp. 24-25.
- **Dewatering wells as geothermal wells.** NREL: "dewatering wells at the Meikle mine are constructed similarly to typical full-sized geothermal wells". The low end of its cost range assumes "repurposing full-sized wells drilled as part of mine development (e.g., dewatering or water supply wells)". It cites Zahn (2012), *Mine Dewatering and Water Management at Barrick Goldstrike Mine in the Carlin Trend* (US EPA Hardrock Mining Conference).
- **Scale of dewatering.** Carlin trend dewatering at Betze-Post/Goldstrike and Gold Quarry ran at **tens of thousands of gpm** in the 1990s and 2000s. Goldstrike's peak is commonly cited at about 70,000 gpm (**unverified**). Most of that water was discharged or infiltrated, and some went to irrigation and the Humboldt system. Most of it is warm rather than hot, roughly 20-60 °C (**unverified**). The power-grade fraction comes from specific fault-fed zones like Meikle.
- **Genetic link.** Person et al. 2008 (*Geosphere* 4(5):888-917, doi:10.1130/GES00150.1) model "modern and fossil geothermal systems in the Great Basin" as the hydrologic engines of epithermal Au-Ag and Carlin-type gold deposits. NREL adds that epithermal deposits younger than about 7-10 Ma are spatially associated with *active* geothermal systems (Coolbaugh et al. 2005). Gold districts are therefore a prior on heat, not a coincidence.

### 2.2 Florida Canyon (Pershing County, NV)

- Mine water-supply wells flowed **160 gpm at 223 °F**, giving more than 500 kW of available heat.
- Two 50 kW ORC units ran in 2013-14.
- The pilot was decommissioned "likely due to a change in mine ownership and mineral scaling of fluid piping caused by intermittent operation" (NREL 2022, p. 20).
- **Lesson:** the heat was proven by the mine. The project died on operator incentives and O&M, not on the resource. Florida Canyon also appears in the Nevada Division of Minerals geothermal table (D03).

### 2.3 Mineral-exploration holes that became plants (from D06)

| Plant | Mining-data signal | Tenure route | Size |
|---|---|---|---|
| McGinness Hills | Anaconda (1982) and FMC (1984) holes hit hot water. Newcrest found **190 °F at 980-1,200 ft** in 2004, with geysering and a 346 °F geothermometer | Ormat, competitive BLM sale, 2007 | ~160 MW |
| Blue Mountain | Epithermal-gold holes hit hot water in the early 1990s | **Mining company took the geothermal leases noncompetitively**, then sold the leases plus data | 49.5 MW nameplate; Ormat bought the plant for **$88.7M** in 2025 |
| Don A. Campbell | Mining holes showed **140-190 °F fluids and 203 °F vapour over about 46 km²**, with no surface features | Ormat reviewed the data "at no cost", nominated in 2001, won the auction in 2007 | 42 MW |

The Blue Mountain row is the clearest precedent for the claim-holder side door: the miner itself converted its heat knowledge into a geothermal lease and flipped it with the data.

### 2.4 Comstock Lode (Virginia City, NV)

- The 19th-century workings below about 1,500 ft were famously hot. Wikipedia describes water "hot enough to cook an egg or scald a man to death almost instantly", which needed forced ventilation.
- Workings reached **3,250-3,360 ft** (Combination Shaft; Ophir-Mexican winze, 1884).
- The Sutro Tunnel drained up to **4 million gal/day**. Pumps were shut off in **1918**, and the mines have been flooded up to the Sutro level, about **1,640 ft below Virginia City**, ever since.
- Historical accounts put the deep-water temperatures at about 150-170 °F (**unverified**).
- Steamboat Springs, about 20 km northwest, is an operating geothermal field of roughly 100+ MW (**unverified**). This supports a regional heat source.
- **Reading:** a large, flooded, pre-drilled, warm-to-hot reservoir with a century of mine maps (the National Mine Map Repository is listed by NREL as a data source) sits under fragmented patented and unpatented claims. It is a direct-use or low-temperature binary target, not a 50 MW site (**unverified**: there is no published resource assessment that I could reach).

### 2.5 International: Lihir (PNG)

- Newcrest (now Newmont) drilled steam-relief and depressurisation wells to mine the Ladolam pit inside an active geothermal system, then used the steam for power.
- NREL cites a **56 MW** plant supplying about **75%** of mine power for more than 15 years, and notes the plant was registered under the UN CDM. Wikipedia says **50 MW** and about 25%. The discrepancy is unresolved, and the 75% share is the company-sourced figure (Newcrest 2018 Sustainability Report, via NREL).
- Veladero (Argentina, Barrick) studied an 8-20 MW geothermal plant 12 km from the mine. It was apparently never built (NREL, citing Boynton et al. 2019, GRC Bulletin).

### 2.6 NREL economics for mine-co-located geothermal

NREL's GETEM scenarios assume the lease is obtained through the mining claimant's noncompetitive right (43 CFR 3204.12) and that power serves on-site load.

- LCOE falls from **$87/MWh (BAU) to $62-67/MWh**.
- Remote-mine diesel costs **$109-185/MWh**.
- NREL explicitly did *not* model the delay of competitive nomination and auction. That delay is the cost the side door avoids.

## 3. Flooded cold-district mines (scope check)

- **Springhill, Nova Scotia:**
  - coal mines closed in the early 1970s and flooded;
  - the water averages **18 °C**;
  - heat-pump use for the industrial park began in the **late 1980s**;
  - the town approved a broader programme in 2014 (Wikipedia, citing CTV).
- **Heerlen (NL) Mijnwater:** the "minewater power station" opened on **1 Oct 2008** using the Oranje Nassau I and III mines. It was planned for about 200 homes plus retail, office and public buildings (Wikipedia). It later grew into a 5th-generation smart thermal grid with water at about 28 °C from about 700 m (**unverified**).
- **UK:** the Coal Authority has promoted mine-water heat schemes, such as the Gateshead heat network (about 6 MW heat pump, **unverified**) and Seaham Garden Village. About a quarter of UK homes sit above former coalfields, and the water is about 12-20 °C (**unverified**).
- **ORNL/LBNL/NREL 2023 (OSTI 1996689):** more than **17,000 US mine-land sites** with more than **85 GW** of clean-energy potential across all technologies. Geothermal is discussed only qualitatively ("often spatially and genetically associated with ore deposits"), and there is no mine-water geothermal count.
- **Verdict.** These are municipal or utility heat projects worth single-digit MWth each. The mine-water owner is frequently a public body, such as the UK Coal Authority, which owns the coal mine workings (**unverified** as to its heat-rights position). There is no cheap private right to buy before proof, and no step-up sale to Fervo or a hyperscaler. On the standing rules this **fails "too small" and "own the asset"**. Treat it as out of scope except as a direct-use add-on.

## 4. The data: where the heat in mining records actually lives

| Source | What it holds | Public? | ML legibility |
|---|---|---|---|
| **Nevada Division of Water Resources (NDWR) water-rights permits** | Mine dewatering permits ("mining and milling / dewatering" manner of use), pumped volumes, well locations, and well logs for permitted wells | Public, searchable online (**unverified** schema) | Structured locations and volumes; temperature is rarely recorded (**unverified**) |
| **NDEP mining and discharge permits (BMRR / Bureau of Water Pollution Control)** | Water management plans, discharge and infiltration monitoring (some include temperature) | Public on request, partly online (**unverified**) | PDFs; good LLM target |
| **BLM NEPA documents** (EIS/EA for Goldstrike, Gold Quarry, Leeville, Cortez and others) | Groundwater models, dewatering rates, drawdown cones, spring and well temperatures | Public via ePlanning | Long PDFs with hydrogeology chapters; very LLM-friendly |
| **SEC S-K 1300 / NI 43-101 technical reports** | Hydrogeology sections, dewatering design, hot-ground notes (the Meikle type) | Public | LLM-friendly |
| **NBMG archives, county mineral reports, Anaconda collection, National Mine Map Repository** | Historic hole logs and mine maps with "hot water / steam / geysering" text cues | Public (NREL 2022) | Scans; OCR plus LLM |
| **Directional-survey contractors' tool temperatures** | Unequilibrated temperature-depth data from most angled mineral holes | **Proprietary**, a "vast database" (NREL 2022) | Needs data deals |

NREL's recommendations to the mining industry ("collect temperature with depth surveys in dewatering wells prior to beginning operation", "report fluid level and temperature … to NDWR", "consider joint development opportunities") confirm that **none of this is done systematically today**. Miners "are not required to notify the state of Nevada if they encounter hot fluid".

## 5. Hard numbers (sourced unless marked)

- Meikle mine temperature: **330 °F**. NREL reference case: 330 °F at about 2,000 ft, 1,750 gpm per well, 20 MW binary.
- Florida Canyon: **223 °F, 160 gpm, more than 500 kWth**; 2 × 50 kW ORC; 2013-14.
- McGinness Hills mining hole: **190 °F at 980-1,200 ft**; now about 160 MW.
- Blue Mountain: noncompetitive lease taken by the miner, then flipped; plant resold for **$88.7M** (2025).
- Lihir: **50-56 MW**, steam from mine depressurisation wells.
- Mining-co-located LCOE: **$62-67 vs $87/MWh**; remote-mine diesel **$109-185/MWh**.
- Nevada mining drills **more than 2,000 holes/yr**, against 31 geothermal wells in 2017.
- Noncompetitive geothermal lease: **$1/acre/yr** for years 1-10, plus about $505-520 per application (R02). An unpatented claim costs **$200 per 20 ac/yr** in maintenance fees (R13).
- Comstock: flooded to about **1,640 ft** since **1918**; workings to **3,360 ft**; Sutro drained up to **4M gal/day**.
- Springhill: **18 °C** mine water. Heerlen: opened **2008**.
- US mine-land sites: **more than 17,000**.

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **Drop flooded coal-mine heat as a core thesis.** It is low-temperature, the asset is municipal, there is no tradable right, and the exit is small. It fails "too small" and "own the asset". Keep it only as a direct-use upsell if a district-heat partner appears.

2. **Hot Great Basin mines are a genuine Terranox analogue, and arguably a cleaner one than oil wells.**
   - **Someone else has paid** to drill, pump and sometimes measure hot water.
   - **The records are public but illegible:** NDWR dewatering permits, NDEP discharge monitoring, BLM mine EIS groundwater chapters, S-K 1300 hydrogeology sections, NBMG and historic mine files. This is exactly the "public-but-illegible archive plus ML" pattern of SMAD.
   - **The geothermal right is a separate estate** that the mine typically does not hold and does not value.

   An LLM pass over Nevada mine EIS and permit files for temperatures, gpm, "hot", "steam" and "scaling" is cheap, fast and novel. I found no published work doing it (see also D06).

3. **The tenure edge is the mining-claim side door.** Under 30 USC 1003(b)(3) and 43 CFR 3204.12, a claim holder with an approved plan of operations can take a **noncompetitive geothermal lease at $1/acre/yr**, bypassing the nomination-to-auction path that took Don A. Campbell six years and that Zanskar and others now bid against.

   A Terranox-shape company could do the following:
   - partner with or option from junior and mid-tier claim holders whose plans are approved, file the noncompetitive lease through them, and give the miner an ORRI or carry;
   - for large operators (NGM, Kinross, i-80, Hycroft), offer to monetise dewatering heat as on-site power at below-diesel cost, with the developer owning the geothermal lease;
   - acquire claims directly over hot ground and advance a plan of operations. This is slower and needs NEPA, and whether a plan can be geothermal-motivated is a legal-risk question (**unverified**).

   Precedent: Blue Mountain's miner did exactly this, then sold leases plus data, and the plant was later resold for $88.7M.

4. **Optionality and risk.**
   - NREL's scenarios assume on-site use. Whether a 3204.12 lease can support grid export and resale to Fervo, Ormat or a utility without re-competition needs legal confirmation (**unverified**; the statute text I fetched does not restrict use).
   - Operator misalignment killed Florida Canyon. Miners change hands and their mine lives are finite, so contracts must survive a change of control and mine closure. Closure is actually an *opportunity*: dewatering wells could be handed over as geothermal wells instead of being plugged.

5. **The gap vs Zanskar.**
   - Zanskar's public land record is about 50k acres won at **competitive BLM auctions** for under $1M in bonus bids, plus the acquired Lightning Dock plant (Z04).
   - Its data story is digitised legacy geothermal datasets plus its own field team and TG drilling (Z01, Z03).
   - Nothing public shows it ingesting **mine dewatering permits, mine EIS hydrology, or claim-holder data**, or using the **mining-claimant or oil-and-gas noncompetitive doors** (**unverified** as to its internal practice).

   This is a distinct, defensible wedge built on three things:
   - (a) exclusive data and tenure partnerships with claim holders;
   - (b) a "heat-under-claims" map built from permits and EIS files;
   - (c) noncompetitive leases that never hit the auction where Zanskar bids.

   It is complementary to, not competitive with, Zanskar's blind-system ML, and it also yields flip candidates for Zanskar, Ormat or Fervo.

6. **Scoring.**
   - **Scope:** the Nevada hot-mine and epithermal-district subset plausibly holds hundreds of MW to low GW. It overlaps NREL's more than 3 GW of undiscovered Nevada resource, and active epithermal districts track geothermal (calculated or inferred, **unverified** sizing). That is not too small *as a wedge* inside the broader Great Basin play.
   - **Asset ownership:** strong, via the noncompetitive lease.
   - **ML lift:** plausible and untested; text extraction from permits and EIS files is low-risk.
   - **Main unknowns:** how many approved plans of operation sit over hot ground, and the legal durability and exportability of 3204.12 leases.

## Sources

- NREL (NLR), Levine, Rhodes and Kvien 2022, *Mining G.O.L.D. (Geothermal Opportunities Leveraged through Data)*, NREL/TP-6A20-81946 (Meikle 330 °F; Florida Canyon; Lihir; dewatering wells; GETEM LCOE; recommendations): https://docs.nlr.gov/docs/fy22osti/81946.pdf ; https://www.osti.gov/biblio/1855781
- 30 USC 1003 (noncompetitive leasing: mining claimants (b)(3), O&G co-production (b)(4), direct use (f)): https://www.law.cornell.edu/uscode/text/30/1003
- 43 CFR 3204.12 (mining-claim holder noncompetitive application): https://www.law.cornell.edu/cfr/text/43/3204.12
- 43 CFR 3204.10 ($1/acre advance rent): https://www.law.cornell.edu/cfr/text/43/3204.10
- ORNL/LBNL/NREL 2023, *Clean Energy Technology Applications on US Mine Land* (17,000+ sites, 85 GW): https://www.osti.gov/biblio/1996689
- Person et al. 2008, *Hydrologic models of modern and fossil geothermal systems in the Great Basin: genetic implications for epithermal Au-Ag and Carlin-type gold deposits*, Geosphere 4(5): https://doi.org/10.1130/GES00150.1
- Comstock Lode (hot water, depths, Sutro, 1918 flooding): https://en.wikipedia.org/wiki/Comstock_Lode
- Sutro Tunnel: https://en.wikipedia.org/wiki/Sutro_Tunnel
- Springhill, NS mine-water geothermal: https://en.wikipedia.org/wiki/Springhill,_Nova_Scotia
- Heerlen Mijnwater (opened 2008): https://en.wikipedia.org/wiki/Heerlen
- Lihir Island geothermal (50 MW): https://en.wikipedia.org/wiki/Lihir_Island
- Geothermal power in the US (Nevada more than 486 MW, 19 plants): https://en.wikipedia.org/wiki/Geothermal_power_in_the_United_States
- Zanskar: https://www.zanskar.com ; Series C: https://zanskargeothermal.substack.com/p/zanskar-raises-115m-series-c-following
- Sibling evidence files (sourced): D06-mining-assessment.md, D03-great-basin-wells.md, R02-blm-noncompetitive.md, R13-mineral-claims-overlap.md, Z01-overview.md, Z04-land.md
- Cited via NREL, not fetched: Proulx and Scovira 2001, CIM Bulletin 94:71-74 (Meikle hot ground); Zahn 2012, EPA Hardrock Mining Conference (Goldstrike dewatering); Newcrest 2018 Sustainability Report (Lihir); Boynton et al. 2019, GRC Bulletin (Veladero)
