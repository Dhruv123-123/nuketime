# Lane: Earth observation, agriculture, oceans, forests and wild biology

Eighth hunt, 15 Oct 2026. I used 18 of my 20 web searches, almost all on prior art and pricing. Where a figure comes from memory and not from a page I fetched, it is marked *(unverified)*.

## Bottom line

This lane has no clean Terranox. The test is "public data, plus ML, then claim first and own it". Under that test most natural resources outside geology fail in one of three ways:

- **The state allocates them by auction or merit, not first-come.** Examples: Norwegian salmon capacity, offshore wind and aquaculture lease rounds. Here ML helps you bid, but you still pay full price.
- **A fund or incumbent already owns the position.** Examples: farmland, timber, water, carbon developers, microbial-strain discovery.
- **The asset cannot be fenced off.** Examples: genebank material under the ITPGRFA SMTA, and wild genetic resources under Nagoya.

The best fit is **compensatory mitigation and conservation banking (candidate 1)**:

- The scarce asset is regulator-issued credits, and they are tied to a geographic service area.
- The first approved bank in an undersupplied service area earns near-monopoly prices.
- Credits sell for $50k to $500k+ each.
- Siting and demand forecasting are messy, multi-modal inference problems that the industry still does by hand.

Western water rights (candidate 2) are second. Fishing quota and genebank trait-mining are weaker. Five more ideas are killed in the last section.

---

## Candidate 1: ML-sited mitigation and conservation banks (own the credits). Score 6/10

**Datasets, and why they are public**
- **USACE RIBITS.** Every approved bank, its service area, credits released, debited and remaining. It is public because the 2008 Mitigation Rule (33 CFR 332.8) requires the ledger to be transparent.
- **USACE ORM2 permit decisions and public notices.** Section 404 public notices are mandatory.
- **National Wetlands Inventory, SSURGO hydric soils, 3DEP LiDAR, NHD, Sentinel-2 and Landsat.** These are federal open data.
- **State DOT STIPs, FERC pipeline dockets, utility IRPs and data-center announcements.** These are legally required planning disclosures, and they show future demand for wetland and stream impacts.
- **USFWS species ranges, critical habitat and GBIF/eBird occurrence data.** These cover species conservation banks, for example gopher tortoise, scrub jay and American burying beetle.

I verified RIBITS only by documentation and citation (EASI uses it). I did not fetch it from the sandbox.

**The ML problem**
There are two coupled models.

1. **Credit-scarcity forecast per service area and credit type**, 3 to 7 years ahead. Bank approval takes about that long, so this is the horizon that matters.
   - Inputs: the infrastructure pipeline (STIPs, FERC, data centers, housing permits), mapped onto HUC-8 watersheds and estimated wetland and stream acreage in each project corridor; historic debit rates from RIBITS; and the regulatory regime (state rules after Sackett).
   - Output: when each service area sells out, and the clearing price.
2. **Restoration-lift parcel scoring.** This finds cheap parcels, typically drained or tiled farmland on hydric soils, where re-wetting or stream restoration produces the most credits per dollar and gets approved by the Interagency Review Team.
   - Inputs: LiDAR micro-topography, ditch detection, hydric soils, flow accumulation, historical imagery of wetness, and parcel prices.

This is sparse, spatial and multi-source inference that bankers now do by consultant intuition.

**What the company owns**
The land, or a conservation easement on it, and the credits the Corps or state releases under the Mitigation Banking Instrument. Credits are property that can be sold to any permittee in the service area.

**Why it is defensible (partly rivalrous)**
- Getting an MBI takes 2 to 4 years.
- The first bank in a service area sets the market and often fills most of the demand there.
- IRTs are reluctant to approve too many overlapping banks.
- Later entrants lose the window, the same dynamic as a mineral claim.

It is not as exclusive as a mineral claim, because a competitor can still site a bank in the same HUC.

**Ceiling, with numbers**
- Industry revenue was about $3.5B in 2019 (2023 study cited by The Lens / Tennessee Lookout).
- EASI estimates about $8B/yr average demand over roughly 35 years, $415B+ of credits released and about $285B transacted (EASI 2026 review). Treat the cumulative figures as advocacy numbers.
- **Credit prices:**
  - Florida bank sheet (Mitigation Banking Group): $50k to $550k per credit. Alafia River sells at $500k and saltwater Gulf Coast at $450k to $550k.
  - Virginia: about $263k per wetland credit.
  - North Carolina: about $134k.
  - Tennessee: about $50k.
  - Georgia isolated-wetland credits: quoted at $750k to $1.1M.
- **One bank.** A bank of 200 to 400 acres can yield 100 to 300 credits. At $100k to $250k each that is $10M to $75M of revenue against about $3M to $10M of land and restoration cost *(unverified per-bank economics; typical industry figures)*.
- **The company.** 30 to 50 banks in forecast-short service areas gives a $1B to $3B asset base. RES, the largest player, attracted KKR and Onex capital.

This is multi-billion but not tens of billions.

**Who already does it (crowding check)**
The field has many players but is fragmented:
- RES (KKR and Onex backed, and it rolls up others such as Environmental Banc & Exchange)
- Ecosystem Investment Partners (EIP, with a joint venture with RES in Georgia)
- Westervelt Ecological Services
- Wildlands
- Earth Partners
- Hundreds of local bankers. There are more than 2,500 banks; Virginia alone has 164.

Data vendors (EASI, MitigationDesk) report prices but do not forecast or own. I found no ML-first bank developer.

In the UK, Biodiversity Net Gain habitat banks are crowded with startups, so I am excluding the UK.

**Key risks**
- **Sackett v. EPA (2023)** removed federal jurisdiction over isolated wetlands.
- **State rollbacks.** Tennessee's bill would deregulate about 80% of isolated wetlands, and one banker projected an 80% drop in demand there.

Regulatory demand risk is therefore the core risk. The model has to treat the legal regime as an input, and the strategy should favour stream credits, species credits and states with their own wetland programmes (NJ, VA, NC, FL).

**Concrete first proof (4 to 6 weeks, under $100k)**
1. Scrape RIBITS for VA, NC, GA, TN and FL into a service-area time series of releases, debits and sold-out dates.
2. Backtest: train on data up to 2018 and predict which service areas sold out, or had the steepest price rises, in 2019 to 2024, using only the infrastructure-pipeline features available at the time. The kill criterion is no lift over a naive "recent debit rate" baseline.
3. For the top three forecast-short service areas, rank parcels by restoration lift and price.
4. Take one land option for $25k to $75k. Hold a pre-application meeting with the district IRT to test whether approval is realistic.

---

## Candidate 2: Buy western water rights whose true transferable yield is mispriced. Score 5/10

**Datasets, and why they are public**
- **State water-rights registries**: Colorado CDSS/HydroBase, Idaho, Utah, Washington and others. They exist because prior-appropriation law requires public registries of priority, decreed amount and point of use.
- **Diversion records**, published by state engineers.
- **Water-court decrees and change cases.** These are court records, mostly scanned PDFs.
- **HarDWR**, which harmonises rights across 11 states and is on figshare.
- **OpenET**, Landsat-based field-scale evapotranspiration from 1985 to now. It is publicly funded (NASA, USGS, EDF, DRI).
- **Kansas WIMAS** per-well pumping reports, required under K.S.A. 82a-732.

A prior round of this project, `forced/round1.json`, pitched this data as an analytics service. Here it is re-pitched as owning the rights.

**The ML problem**
In change-of-use cases, only **historic consumptive use (HCU)** is transferable, not the paper decree.

1. Reconstruct field-level consumptive use for each right over 30+ years, using Landsat ET, diversion records and crop classification.
2. Use LLMs to extract decree terms, past change-case outcomes and engineer-applied return-flow factors.
3. Predict what a water court would let you transfer and the expected curtailment by priority under drought scenarios.
4. Rank rights by transferable acre-feet per dollar of acquisition price.

Rights with high HCU and senior priority are often sold at farmland prices that do not reflect their municipal or industrial value.

**What the company owns**
The water right. It is real property, exclusive and senior by priority date. The company buys it with the farm or alone, then changes it to municipal, industrial or data-center use, or leases it.

**Why it is defensible**
Priority dates are fixed and cannot be re-created; whoever owns the senior right owns it permanently. But the asset is not newly claimable. New appropriations are effectively closed in over-appropriated basins, so this is buying mispriced assets, not claiming first.

**Ceiling**
- WestWater tracked about 2.5M acre-feet in leases and sales worth about $1B in its latest annual report.
- Colorado-Big Thompson sold at about $85k per acre-foot in 2025, against a peak of about $101k in 2022 (Colorado Sun, April 2026).
- Arizona prices rose 75%.
- The C-BT project alone (about 310k units) is worth about $20B+ at market *(unverified unit count)*.
- Converting agricultural rights to municipal or industrial use commonly gives a 3 to 10x uplift *(unverified, typical)*.
- A $1B to $3B portfolio is plausible over time.

**Who already does it (crowded)**
- Water Asset Management (Disque Deane)
- Greenstone / Cadiz
- Vidler Water (acquired by D.R. Horton in 2022)
- Pure Cycle
- Gladstone Land (reports water assets)
- Renewable Resources Group
- Municipal buyers
- WestWater Research (broker)

None appears to use parcel-level ML on OpenET *(unverified absence)*.

**Risks**
- There is political "buy-and-dry" backlash, including the Western Slope fights reported by Denver7 and KUER, and anti-speculation laws.
- Change cases take 2 to 5 years and are contested by every downstream user.
- It is slow and capital-heavy, and the incumbents already know where the value is.

**Concrete first proof**
1. Pick about 50 Colorado change-of-water-right decrees from 2010 to 2024.
2. Predict the court-decreed HCU from OpenET and CDSS alone, then compare with the decrees. Success is a median error under 15% against the engineers' figures.
3. Screen currently listed farms with water in the South Platte and Arkansas basins for transferable acre-feet per dollar in the top decile.

---

## Candidate 3: Climate-forecast fishing quota acquisition. Score 4/10

**Datasets, and why they are public**
- Copernicus Marine (CMEMS) ocean reanalysis and forecasts (EU open data).
- NOAA OISST and NOAA trawl surveys.
- OBIS/GBIF occurrences.
- Global Fishing Watch AIS fishing effort (open for research).
- Stock assessments and total allowable catch (TAC) histories. These are public because managers must publish them, for example AFMA, NZ MPI, NOAA SAFE reports and ICES.
- Quota trade prices in some jurisdictions, such as NZ quota trading data and NOAA IFQ reports.

**The ML problem**
Species-distribution and recruitment models driven by ocean state forecast which stocks will see their TACs rise or fall over 3 to 10 years as stocks shift poleward. The company buys quota in stocks forecast to rise before managers raise the TAC. Quota prices tend to follow realised TACs (see the UMD "Fishy Business" paper on groundfish quota and climate).

**What the company owns**
Individual transferable quota (ITQ) or statutory fishing rights. These are perpetual, exclusive and transferable in Australia and New Zealand, and limited in Iceland and Alaska.

**Why it is defensible**
Quota is fixed-supply and exclusive. But the edge is informational: the company buys an existing traded asset early, so this is closer to a long-horizon trade than a claim.

**Ceiling**
National quota stocks are worth several billion each, for example NZ QMS and Iceland *(unverified)*. Ownership rules cap outsiders:
- Iceland and NZ restrict foreign ownership.
- Alaska halibut and sablefish IFQ require owners on board.

A realistic portfolio is $0.3B to $1B.

**Who already does it**
The Longreach Maris Sustainable Seafood Fund (Andrew Rado) already invests in Australian quota, plus vertically integrated fishers. The MSC and academics model stock shifts.

**First proof**
Hindcast 2005 to 2024 for about 30 Australian and NZ quota stocks. Test whether ocean-state features available at the time predicted TAC changes 3 or more years ahead, and whether quota prices lagged those changes.

---

## Candidate 4: Genebank and landrace trait mining into owned varieties. Score 3/10

**Datasets, and why they are public**
- Genesys (about 4M accession records).
- USDA GRIN-Global.
- CGIAR genebanks with passport and collection-site coordinates.
- DivSeek and CIMMYT Seeds of Discovery genotypes.
- WorldClim/CHELSA and SoilGrids, for the climate and soil at each collection site.
- Public multi-environment trials, such as Genomes to Fields.

These are public because of the ITPGRFA Multilateral System and taxpayer-funded genebanks.

**The ML problem**
Environment-to-trait association (FIGS plus genomic prediction). It predicts which of millions of uncharacterised accessions carry heat, drought or salinity tolerance, then introgresses that into elite lines.

**What the company would own**
Plant variety protection or utility patents on the improved varieties, not on the accessions.

**Why it is weak**
- **No exclusivity on the input.** Under SMTA Article 6.2 you cannot claim IP over material "in the form received", so anyone can request the same accessions.
- **FIGS is already done.** ICARDA publishes FIGS work with ML on barley.
- **Well-funded competitors.** Inari has raised $575M+ *(sum of announced rounds, approximate)*, plus Ohalo, Avalo, Benson Hill (struggling) and Corteva/Bayer internal pipelines.
- **Slow and benefit-sharing.** It takes 5 to 10 years to a commercial variety, and benefit-sharing payments are owed.

**First proof**
Replicate a FIGS-style prediction on GRIN wheat or sorghum accessions that already have published heat-tolerance phenotypes. Measure whether the ML beats random or core-collection selection.

**Verdict:** essentially killed. It stays only as a reference point.

---

## Killed in this lane (do not pitch)

**Aquaculture licences and sites**
- Norway sells capacity by auction. In June 2024 all 17,330 t sold for NOK 5.29B, about NOK 305k per tonne, against a NOK 170k floor. Mowi and Cermaq were the biggest buyers.
- Iceland halted new permits in September 2023.
- US offshore aquaculture siting is done by NOAA itself (Aquaculture Opportunity Areas).

No first-come window exists, so ML only helps you bid.

**FERC preliminary permits for hydropower on non-powered dams and pumped storage**
These are first-to-file priority claims, but speculators have filed on this land for 15 years (Rye Development, Free Flow Power, and the Wise County, VA duplicate filings in 2026). The ORNL and ANU site atlases are already public, and the permit is worth little against $2B to $4B per GW of build cost.

**Climate-frontier farmland and timberland**
Bonnefield (Canada), Nuveen/TIAA, Manulife, farmland REITs and Ontario investor buying are all reported. It is not claimable, the market prices it, and the edge is thin.

**Kelp, seaweed and sargassum biomass rights**
There is no exclusive rights regime for open-ocean sargassum. Players include Running Tide (failed), Seaweed Generation, Carbonwave and Kelp Blue. Ceiling is small.

**Carbon and nature credit developers**
These include ARR, IFM, blue carbon and peat concessions. Pachama, Chestnut, Living Carbon, Renoster, Finite Carbon and many others are already here, along with credibility and price collapse.

**Microbial strains and metagenome mining**
Pivot Bio, Indigo, Basecamp Research (with proprietary data), Profluent, Hexagon Bio and Ginkgo are all here. After the Myriad ruling, natural sequences are not patentable.

**Solar and wind land options ahead of interconnection**
Every developer does this, plus tools such as Paces, Transect and LandGate.

**UK Biodiversity Net Gain habitat banks**
These are mandatory since February 2024 but already crowded: Environment Bank, Nattergal and many land-agent spinouts.

---

## Scores

| # | Candidate | Claimable? | Ceiling | Crowding | Score |
|---|---|---|---|---|---|
| 1 | ML-sited mitigation and conservation banks | Partly: MBI plus a first-mover service area | $1B to $3B asset base | Fragmented, no ML-first player found | **6** |
| 2 | Water rights bought on mispriced HCU | Exclusive senior rights, but bought, not claimed | $1B to $3B | Funds present | **5** |
| 3 | Climate-forecast fishing quota | Exclusive ITQ, but bought | $0.3B to $1B | Longreach Maris | **4** |
| 4 | Genebank trait mining into PVP | No (SMTA) | Large but slow | Inari, Ohalo, Avalo, FIGS | **3** |

## Sources

**Mitigation and conservation banking**
- [EASI 2026 review of the US mitigation credit marketplace](https://www.easillc.com/2026/06/22/2026-review-u-s-mitigation-credit-marketplace-nears-500-billion/)
- [Mitigation Banking Group: Florida credit prices](https://mitigationbankinginc.com/mitigation-credit-prices/)
- [The Lens: wetlands rollbacks and mitigation banking (Sackett, Tennessee)](https://thelensnola.org/2025/04/14/wetlands-protections-built-an-industry-for-mitigation-banking-rollbacks-could-erode-it/)
- [RES and EIP joint venture](https://res.us/?p=3237)
- [Onex Partners and KKR invest in RES](https://www.privsource.com/acquisitions/deal/y3SeGR)
- [Forest Trends: nine steps towards doubling US mitigation markets](https://www.forest-trends.org/articles/opinion-nine-steps-towards-doubling-the-value-of-us-mitigation-markets/)

**Water rights**
- [Colorado Sun: Colorado water prices](https://coloradosun.com/2026/04/24/colorado-water-prices/)
- [Northern Water: C-BT historical market prices](https://www.northernwater.org/getmedia/45190426-0f57-4325-8320-82199f21b984/Colorado-Big-Thompson-Units-Market-Price-Historical-Data)
- [Denver7: farming, water and Wall Street on the Western Slope](https://www.denver7.com/news/local-news/farming-water-and-wall-street-on-colorados-western-slope)
- [Agri Investor: Water Asset Management](https://www.agriinvestor.com/liquid-portfolio/)
- [USGS: OpenET](https://pubs.usgs.gov/publication/70226741)

**Fishing quota**
- [Livewire: Longreach Maris fishing quota fund](https://livewiremarkets.com/wires/andrew-rado-casting-a-wide-net-investing-in-australia-s-fishing-quotas)
- [UMD: climate change and groundfish quota prices](https://mdsoar.org/items/9a78a0cf-c5f2-41d4-8872-24eea123c059)

**Aquaculture**
- [We Are Aquaculture: Norway 2024 auction sold out](https://weareaquaculture.com/news/aquaculture/norwegian-farming-permits-sold-out)
- [Salmon Business: Iceland halts new permits](https://www.salmonbusiness.com/icelandic-government-issues-a-halt-on-further-licences-for-salmon-farming/?amp=1)

**Genebank and breeding**
- [ICARDA: FIGS and machine learning on barley accessions](https://dspacetest.mel.cgiar.org/items/8d8789ed-0ff1-45c4-b0e0-51299df3f916/full)
- [Global AgInvesting: Inari Series C](https://globalaginvesting.com/inari-announces-89m-series-c-advance-next-generation-seed-breeding/)

**Hydropower and farmland**
- [Cardinal News: Wise County pumped storage filings](https://cardinalnews.org/2026/07/07/2-pumped-storage-hydroelectric-stations-could-be-located-just-miles-apart-in-wise-county/)
- [CBC: investors and Ontario farmland](https://amp.cbc.ca/news/canada/london/ontario-farmland-real-estate-investment-1.7218435)
