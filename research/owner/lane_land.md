# Lane: land, property, water and other claimable physical rights

Sweep agent, 15 Oct 2026. Brief: `research/owner/BRIEF.md`. 16 WebSearch calls used.
Not covered: minerals, drilling, groundwater prospecting as geology (banned).

## Bottom line

Most of this lane is crowded or already priced. "Buy before upzoning" and land promotion have
well-funded incumbents with decades of planning skill and tools that read the same data. Tax liens and deeds
are bid away at auction. Akiya plays are small. Farmland and "climate-advantaged" land are held by large
institutions. Powered land is in a land rush. Western water has funds in it and strong political pushback.

One idea in this lane fits the Terranox shape: **regulatory ecological credits (wetland, stream and
species mitigation banks, plus UK Biodiversity Net Gain habitat banks), sited by forecasting where
impacts will happen before the market sees them.**
- Approving a bank gives its operator an exclusive, regulator-issued inventory of credits within a
  service area.
- The first bank in a service area that runs short takes the scarcity price.
- Demand can be forecast from public permit and infrastructure pipelines. Supply can be found from public
  soils, wetland and LiDAR data.
- It is still only a 6/10. Incumbents are real and well capitalised, and US wetland demand faces a
  legal headwind (Sackett v. EPA, 2023).

| # | Candidate | Score |
|---|---|---|
| 1 | Forecast-led ecological credit banking (US 404 wetland/stream, ESA conservation banks, UK BNG) | **6/10** |
| 2 | Brownfield closure arbitrage (ML cost-to-closure from state cleanup case files) | 5/10 |
| 3 | Western ag-to-urban water conversion, underwritten by ML historic-consumptive-use (OpenET + diversion records) | 4/10 |
| 4 | Linear corridor assembly for HVDC/fiber from STB abandonment and parcel data | 3/10 |
| 5 | UK grey-belt strategic land promotion via ML on planning records | 3/10 (crowded) |

---

## 1. Forecast-led ecological credit banking — 6/10

**The asset.** A Clean Water Act s404 developer, a road or a data center that fills wetland or stream must
buy compensatory mitigation credits. It buys them from an approved **mitigation bank** with a service area
covering the impact site. In-lieu-fee programmes and permittee-responsible mitigation are the
fallbacks. ESA conservation banks work the same way for listed species. England's mandatory Biodiversity
Net Gain (BNG, in force since Feb 2024) requires 10% net gain, met through registered habitat banks.
A bank is a regulator-approved instrument with a fixed credit ledger. Once one or two banks cover a
service area, a newcomer must go through the same 1-3 year approval process. The first mover therefore
holds a de facto local position on a non-substitutable compliance good. This is the claim-staking
analogue.

**Public datasets, and why they are public**
- **RIBITS (USACE/EPA/FWS).** Every federal mitigation bank, its service area, credits released and
  every credit withdrawal by date and permit. It is public because the 2008 Mitigation Rule
  (33 CFR 332) requires public transparency of bank ledgers.
- **USACE Regulatory public notices and permit decisions (ORM2 extracts, district public notice
  pages).** They are public under Administrative Procedure Act / s404 public-notice requirements.
- **Demand leading indicators:**
  - state DOT STIPs (federally required)
  - ISO/RTO interconnection queues
  - FERC and state PUC siting dockets
  - county data-center rezonings and building permits
  - FWS National Listing Workplan and 12-month findings (ESA listing pipeline, published by statute)
- **Supply side:**
  - USDA SSURGO hydric soils
  - National Wetlands Inventory
  - USGS 3DEP LiDAR
  - historic aerial imagery (USGS EarthExplorer)
  - county parcel/assessor rolls
  - NHD stream network
- **UK:**
  - Natural England Biodiversity Gain Site Register
  - planning.data.gov.uk
  - Planning Inspectorate NSIP register (BNG for NSIPs phases in from 2026)
  - HM Land Registry INSPIRE polygons and CCOD/OCOD ownership data

**The ML problem.** There are two hard inferences.
- **Demand (spatio-temporal forecasting):** the credit type and volume each service area will need
  over 2-6 years. Inputs are noisy, multi-source leading indicators: data-center campus filings, transmission
  routes, highway lettings, housing permits, species listings. This has to be joined to historic
  impact-to-credit ratios learned from RIBITS withdrawals matched to permits.
- **Supply (restorability scoring):** which parcels can be restored cheaply into high-ratio credit
  types such as forested wetland, stream restoration and priority river units. Inputs are drained
  hydric soils, ditched farmland, LiDAR micro-topography and land price.

The output ranks (service area, parcel) pairs by expected credit price × credits generated ÷ land and
restoration cost. Incumbents site banks from broker intuition and relationships, and no one has published
a cross-service-area forecast. The only ML found is academic or agency-side, for example a TxDOT
deep-learning model that predicts the mitigation each project needs.

**What the company owns.** The land (fee or long option), the bank instrument (MBI), and the credit
inventory. It sells credits as the regulator releases them. Credits are exclusive, regulator-recorded
property.

**Why rivalrous and defensible**
- Service areas are bounded, and the Interagency Review Team (IRT) approves only so many banks per
  watershed.
- Credits cannot be substituted across service areas without penalty ratios. Out-of-area credits
  carry multipliers, and UK BNG applies spatial-risk multipliers.
- Lead time is 1-3 years to approval and 3-7 years to full credit release. A correct forecast made
  early is decisive, and a fast follower arrives after the scarcity rent is gone.
- The data moat compounds. Every withdrawal in RIBITS sharpens the demand model.

**Ceiling, with numbers**
- EASI (June 2026 review of May 2026 RIBITS data) estimates more than $415B of credits released since
  the 1990s, more than $285B of transactions and about $130B of remaining inventory, or roughly $8B/yr.
  Its Virginia figure (~$304B) looks inflated and may reflect a ledger-unit artefact, so treat the
  totals as directional. Source:
  https://www.easillc.com/2026/06/22/2026-review-u-s-mitigation-credit-marketplace-nears-500-billion/
- Wetland credit prices range from about $8.6k/acre (Mississippi) to about $675k (New Jersey).
  Virginia wetland credits average about $263k and North Carolina about $134k (same source).
- Data centers cause a demand shock. Google's ~800-acre Project Dazzler in Scioto County, Ohio, paid
  $1.94M for 25.3 credits (about $77k/credit) to one bank and about $4M on wetland credits in total.
  A bank owner says data centers need "scores, dozens of credits" and are "sucking up all the supply":
  https://ericsandy.substack.com/p/the-wetlands-behind-the-cloud
- UK BNG unit prices (RICS Land Journal, Apr 2026) run from about £24-25k/unit for neutral grassland
  to £140-160k for rivers and about £200k for priority river units. About 200 banks are on the register.
  Many areas are dominated by one or two suppliers. NSIP BNG adds lumpy demand:
  https://ww3.rics.org/uk/en/journals/land-journal/bng-units-prices.html
- An operator that takes 5% of a roughly $8B/yr US flow, plus UK BNG and ESA banks, would earn about
  $400M/yr of credit sales at 40-60% gross margins. Bank portfolios trade as real assets: EIP's
  Appalachia sale drew 6-12 bids, and a strategic-asset multiple puts that at $2-5B of enterprise value.
  This is credible multi-billion, but not unbounded. The pool is set by regulation.

**Who already does it (adversarial check)**
- **RES (Resource Environmental Solutions):** largest US operator, backed by KKR and Onex, and
  acquisitive (Blueway, Environmental Banc & Exchange, Redwing).
- **Ecosystem Investment Partners:** $1.2B AUM, fifth fund closed at $400M in Oct 2025, sold its
  Appalachia portfolio in 2026:
  https://ecosystempartners.com/eip-sale-points-to-deeper-institutional-market-for-mitigation-bank/
- **Others:** Westervelt Ecological Services, Wildlands, Common Ground Capital (lesser prairie-chicken),
  TNC's Bat Conservation Bank of Indiana, and many small single-bank landowners (about 2,200 US banks
  in 2023).
- **UK:** Environment Bank, Gaia, Natural Capital Solutions, Land App, and councils running their own
  banks.
- **Verdict:** this is not an empty field. It is a capital-intensive real-asset business run by
  incumbents who use relationships rather than forecasting. No ML-native operator was found. The edge
  is a better siting forecast, not a monopoly on data, so it is weaker than Terranox, where reading the
  data was the whole game.

**Main risks**
- **Sackett v. EPA (2023)** cut federal wetland jurisdiction, and the 2025 WOTUS rule proposal narrows
  it further. Some US wetland demand is gone. This makes stream credits, state-regulated wetlands
  (e.g. NJ, VA, CA, OH isolated wetlands), ESA species banks and UK BNG more important.
- Credit release is slow and depends on the regulator.
- Political rollback of UK BNG for small sites is under discussion.

**First proof (8-10 weeks, under $150k)**
1. Scrape RIBITS ledgers for 5 eastern states with data-center build-out (VA, OH, IN, GA, NC).
2. Build a model that predicts, 24 months ahead, which service areas fall below 12 months of credit
   inventory. Backtest on 2016-2023.
3. Success means it beats a naive "last-year withdrawals" baseline at ranking the service areas that
   ran short.
4. Then pick the top 3 forecast-tight service areas and score restorable parcels.
5. Secure 2 land options and get a pre-application meeting with the IRT.

**Score: 6/10.** Real exclusive asset, public data on both sides, a data-center tailwind and no ML
operator. It loses points for incumbents, regulatory (WOTUS) risk and a bounded, slow-cycle ceiling.

---

## 2. Brownfield closure arbitrage — 5/10

**Idea.** Buy contaminated sites where the market's stigma discount exceeds the ML-predicted cost and
time to regulatory closure (NFA/"case closed"), then take them to closure and sell or develop.
Priority goes to sites with industrial power service, rail and zoning that suit data centers and
manufacturing.

**Datasets**
- California GeoTracker (UST/SLIC/DoD cases with full document history and lab results) and
  DTSC EnviroStor.
- EPA ACRES (25+ years of brownfield grant cleanups with costs), Superfund/RCRA (Envirofacts),
  state LUST registries.
- NJDEP Known Contaminated Sites, TCEQ, Michigan Part 201.
- They are public under state right-to-know laws and CERCLA/RCRA public-participation requirements.

**ML problem.** Predict cost-to-closure and time-to-closure from messy case files: PDFs of Phase II
reports, contaminant plumes, regulator correspondence and hydrogeology. This is genuinely
multi-modal, and LLM extraction plus survival models fit it. A DataKind/Community Lattice ACRES study
reported no performance figures, a sign it has not been done well:
https://cdmcd.co/bYGbB8

**What the company owns.** Fee title to the site. It captures the remediated value step-up, plus state
brownfield tax credits (e.g. NY BCP credits, among the most generous).

**Rivalry and defensibility.** Each site is unique and owning it is exclusive. Little competes for the
worst-stigma sites because most buyers' lenders refuse them. The defensibility is only an
underwriting edge, though. Nothing stops copying once the edge is visible.

**Ceiling.** The US has roughly 450k brownfields (the commonly cited EPA figure). The value step-up per
site is often 2-5x the land value after closure. A fund-scale operator is plausible at $1-3B of
deployed capital. Returns are real-estate-like, not venture-like, unless the sites are rezoned and
powered, where land-value uplift for data-center use can be 5-20x.

**Who does it.**
- Cherokee Investment Partners pioneered the model (several funds, about $2B+ raised; from memory,
  not verified this run) and struggled after 2008.
- Others: Brownfield Partners, EnviroFinance Group, Greenfield Acquisition Partners, Cleanfield
  Capital, environmental-insurance-backed buyers, and coal-plant redevelopers (Hilco Redevelopment
  Partners, Commercial Development Co.).
- The model is known. The ML underwriting is not.

**First proof.** Use 10 years of closed GeoTracker UST/SLIC cases (tens of thousands of cases with
full timelines). Train a cost/time-to-closure model on documents available at the date of a site's
first Phase II, and test it on later-closed cases. Then match against Costar/county sale records of
contaminated parcels to measure the actual stigma discount. The thesis holds only if
discount minus predicted cost is systematically positive in some segment.

**Score: 5/10.** The ML problem is real and the asset is owned. It is crowded by brownfield funds,
the edge is an underwriting edge and not claimable, and returns are real-estate-like.

---

## 3. Western water: historic-consumptive-use underwriting for ag-to-urban conversion — 4/10

**Idea.** Prior appropriation really is first-in-time claim-staking, but new appropriations are closed
in nearly every valuable basin. The open seam is underwriting. In a change case (e.g. Colorado water
court), only historic consumptive use (HCU) transfers, not the decreed amount. HCU is highly
uncertain at purchase, so buyers misprice rights.

**Datasets**
- Colorado DWR HydroBase/CDSS (decrees, diversion records, the decennial abandonment lists).
- Utah Division of Water Rights; Idaho, Montana and New Mexico registries; Arizona ADWR.
- OpenET: public satellite evapotranspiration (ET) by field since 2016, built by NASA, USGS, EDF and
  others. It is public because these are agency records and publicly funded science.

**ML problem.** Infer field-level historic consumptive use and the transferable yield from diversion
records, OpenET, crop history (USDA CDL) and return-flow patterns. Predict the probable
water-court outcome. Underpriced rights are the targets.

**Owned asset.** Senior water rights and the farms that hold them. Conversion and lease to
municipalities, homebuilders and data centers.

**Ceiling.**
- Colorado-Big Thompson units and Front Range municipal water trade at tens of thousands of dollars
  per acre-foot.
- Comp: D.R. Horton bought Vidler Water (PICO), the largest listed portfolio, for about $291M in 2022:
  https://www.recordcourier.com/news/2022/apr/23/builder-water-broker-merging-291-million-deal/
- That price is a ceiling signal. A dedicated public water-rights company was worth hundreds of
  millions, not billions.

**Who does it.**
- Water Asset Management (NY; 2,500+ acres in western Colorado), branded "drought profiteers"
  locally: https://www.cbsnews.com/news/new-york-investors-snapping-up-colorado-river-water-rights-betting-big-on-an-increasingly-scarce-resource/
- Kyle Bass's Conservation Equity Management (East Texas Carrizo-Wilcox export permits, now in
  litigation) and Upwell Water: https://grist.org/regulation/how-a-billionaires-plan-to-export-east-texas-groundwater-sparked-a-rural-uprising
- Others: Greenstone, Cadiz, Vidler/D.R. Horton, WestWater Research (broker data), AQUAOSO (water
  data for lenders), Nasdaq Veles water index.

**Kill factors.** Anti-speculation doctrine, buy-and-dry backlash and pending bills (a Texas
export-ban bill is expected in 2027), and slow water-court timelines. The gating risk is political,
not informational.

**First proof.** In one Colorado water division, compare HCU decreed in the last 50 change cases
against an ML estimate built only from pre-filing diversions and OpenET. If the error is much smaller
than the per-case spread, buyers are mispricing.

**Score: 4/10.**

---

## 4. Linear corridor assembly (STB abandonments, rail and utility ROW) for HVDC/fiber — 3/10

**Idea.** Read STB abandonment and discontinuance filings (public dockets under 49 USC 10903). Combine
them with parcel and reversionary-interest data to assemble continuous corridors ahead of transmission
and long-haul fiber demand.

**Why it scores low**
- Abandoned corridors are railbanked and held by trail entities, or revert in fragments to adjacent
  owners, with Fifth Amendment takings litigation attached (Rails-to-Trails Conservancy fact sheet:
  https://www.railstotrails.org/wp-content/uploads/2024/02/Railbanking-Fact-Sheet-.pdf).
- Active rail ROW, the useful asset, is owned by railroads, which already lease it for fiber and
  HVDC. SOO Green uses CPKC ROW.
- ML adds little. The hard part is title and assembly, not inference.

**Score: 3/10.**

---

## 5. UK grey-belt strategic land promotion — 3/10 (crowded; kill)

The structure is attractive. Option agricultural land at about £25k/ha, promote it through the local
plan or appeal to residential at roughly £1-3M/ha, and take a share of the uplift. Options are
exclusive. The 2024 NPPF "grey belt" policy reopened green belt.

The field is saturated:
- Promoters: Gladman, Catesby, Hallam Land (Henry Boot), Richborough, Barwood and Wates
  Developments, plus housebuilders' strategic land arms.
- Tools: LandTech/LandInsight and Searchland already ship grey-belt finders:
  https://land.tech/blog/find-grey-belt-sites-fast-with-landinsight and
  https://searchland.co.uk/guides/grey-belt-green-belt-guide
- Urban Intelligence does ML site-finding for councils.

The data (planning.data.gov.uk, PINS appeals, HELAA call-for-sites) is fully read already. **Kill.**

---

## Killed quickly (no candidate write-up)

- **US "buy before upzoning" entitlement prediction.**
  - Tools that read the same records already exist: Deepblocks, Zoneomics, Gridics, Cherre, Reonomy,
    and Regrid/LandVision.
  - Upzoning is mostly city-wide policy (state YIMBY laws), so it is not parcel-specific alpha.
    Parcel rezonings need the owner's application, so the owner captures the gain.
- **Tax-delinquent liens and deeds, and surplus-fund recovery.** Bid-down auctions with institutional
  lien funds (MTAG, Tower), retail crowds and ethical exposure. Not rivalrous at scale.
- **Escheated and heirs' property, fractional-interest partition plays.** Ethically toxic, with
  documented dispossession of Black landowners.
- **Japan akiya.** Tiny per-unit value; Akiya & Inaka, Akiya Mart and others are already there.
- **UK Land Registry and Australian title arbitrage.** No exclusive claim; prices are efficient.
- **Farmland, timber and climate-advantaged land.** Big institutional holders (Nuveen/TIAA, Manulife,
  Farmland Partners, Gladstone, AcreTrader) and timber REITs. No ML inference gives an exclusive
  edge, and the climate thesis is consensus.
- **Powered land, solar and wind site control, and queue positions.**
  - Land rush: Cloverleaf Infrastructure ($300M raised, Nvidia talks), Tract, hyperscaler land teams.
  - Renewables site tools: LandGate, Paces, Transect, Pearl Street.
  - Covered by the energy lanes anyway.
- **Government land disposals (BLM sales, GSA).** Episodic and political; open auctions are bid to
  fair value.
- **Conservation easements.** IRS syndication crackdown; tax product, not asset.

## Search log
Searches (16):
- UK AI land promoters; Vidler/D.R. Horton; Water Asset Management
- Mitigation market size; ML mitigation siting; BNG prices; RES/KKR
- Rail corridor railbanking; UK promoter economics; water-rights ML startups; Texas groundwater
  investors
- Brownfield ML; Cherokee; powered land; AI mitigation startups; conservation bank pricing
- Grey belt tools

Not fetched: RIBITS itself (not attempted; the cloud network blocks many government hosts), Cherokee
fund details (redirect), and Life on Marsh, an apparent AI-remote-sensing marsh/mitigation startup whose
job post did not load. Check that one before pursuing #1.
