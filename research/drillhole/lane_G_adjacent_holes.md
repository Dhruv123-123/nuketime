# Lane G: the same expensive, usually-failing proving hole in other industries

Written 19 Oct 2026. Lane G of the drill-hole hunt (see BRIEF.md).
Evidence caveat: the shared WebSearch budget ran out partway through this lane, so the costs for
CCS stratigraphic wells, helium, salt caverns, geotechnical holes, groundwater and repository holes
are partly from memory and are marked "(memory)" or "(estimate)". Everything else has a URL.

## Summary (the 10 lines that matter)
1. Only one adjacent industry matches Terranox's shape closely: **hydrothermal geothermal**. A cheap
   federal lease ($32/acre average in Nevada in 2025, $107/acre in New Mexico in 2026), a first-well
   success rate of about 50%, a $0.1-5M proving hole, and a large step-up (an operating plant traded at
   about $4.4M per MW; Fervo IPO'd at about $10B).
2. **Zanskar already does exactly this** in the US: ML on public data, then drill, then develop. It has
   $180M of equity (Series C of $115M in Jan 2026), three discoveries in about a year, and Big Blind, the
   first blind system proved commercial in 30 years. So the US geothermal version is taken.
3. What may still be open in geothermal: geographies Zanskar does not cover (Canada's BC/Alberta/
   Saskatchewan, Latin America, East Africa, Indonesia) and **selling proven leases** rather than
   building plants. That second option is a rung Zanskar skips on purpose.
4. **Groundwater rights for data centres and farms in the western US** ranks second. The rights are
   tradable and buyers have money, and driller-log PDFs are public but hard to read. Base hit rates and
   costs here are mostly unsourced, so verify them first.
5. **CCS pore space:** the land is cheap ($34-110/acre bonus) and strat wells are expensive. But the
   geology is already known from oil and gas logs, so the hole is "usually confirming", not "usually
   failing". Buyers are shaky, and TGS, S&P and the operators' in-house teams are already in it.
6. **Natural hydrogen:** there is a lot of capital (Koloma $245M Series B, HyTerra backed by Fortescue,
   Mantle8 and Getech using ML), but no capitalised buyer pays a step-up for a proven hydrogen lease
   yet. Rubric 4 fails today.
7. **Lithium brine (Smackover):** the step-up is real (Equinor committed up to $160M for 45%). But
   grades are already known from legacy oil wells, and the hard part is direct lithium extraction (DLE)
   processing, not discovery. Rubric 1 fails.
8. **Oil and gas wildcats** fit the "usually fails" test (25% commercial success for high-impact wells
   in 2024; about $42M per well on the Norwegian shelf). But the field is saturated with incumbents and
   much of the data is proprietary. Kill.
9. **Offshore wind site investigation, geotechnical boreholes and nuclear repository boreholes** are
   characterisation services on land someone already controls. Nobody can buy an unproven right
   cheaply. Kill on rubrics 3, 4 and 6.
10. All the oil, gas, geothermal, hydrogen, brine and pore-space ideas fall inside Dhruv's 2026-10-03
    ban. Groundwater, geotechnical, offshore wind site investigation and repository holes fall outside
    it, but they are also the weakest on the rubric apart from groundwater.

---

## Ranking on the gold rubric
Scores: H = high, M = medium, L = low, and "fail" means the idea fails that rubric item.

| Rank | Domain | R1 discovery is the hard step | R2 public, hard-to-read data where ML is needed | R3 cheap right | R4 capitalised buyer pays step-up | R5 ladder | R6 ceiling | Already owned by | vs 10-03 ban |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Hydrothermal geothermal (blind systems) | H | H | H | H | H | H | Zanskar (US), Ormat in-house | Inside ban |
| 2 | Groundwater rights (data centres, farms; arid western US) | M | H | M | M-H | M | M | Water-rights investors, hydro consultancies | Outside ban |
| 3 | CCS pore space and Class VI sites | M (confirming hole) | H (state well-log archives) | H | M (depends on 45Q) | M | M | TGS, S&P, operators, Carbon TerraVault | Inside ban |
| 4 | Natural hydrogen | H | M | H | fail (no buyer yet) | M | H if it works | Koloma, HyTerra, Mantle8, Getech | Inside ban |
| 5 | Lithium brine | L | M | M | H | M | M | Standard Lithium/Equinor, Exxon, Smackover players | Inside ban |
| 6 | Helium | H | M | H | M (gas majors buy offtake, not land) | L | fail (small market) | Pulsar, Desert Mountain, many juniors | Inside ban (gas) |
| 7 | Salt-cavern storage | L (salt domes are mapped) | L | M | M | L | L | Operators, engineering firms | Inside ban (in spirit) |
| 8 | Oil and gas wildcats | H | L (proprietary seismic) | M | H | H | H | Majors, NOCs, TGS, dozens of AI vendors | Inside ban |
| 9 | Offshore wind site investigation | fail | L | fail (seabed lease auctioned) | fail | L | fail (service) | Fugro, Gardline, G-tec | Outside ban |
| 10 | Geotechnical boreholes | fail | M | fail | fail | L | fail | Geotech consultancies | Outside ban |
| 11 | Nuclear repository boreholes | fail | L | fail (state-run, single buyer) | fail | fail | fail | NWMO, Posiva, Deep Isolation | Outside ban |

---

## 1. Hydrothermal geothermal: temperature-gradient holes and slim holes, then full-size wells

**Cost of one proving hole**
- Temperature-gradient wells are shallow (150-1,000 m) and typically cost **USD 100k-1M per well**
  ([SLB](https://www.slb.com/products-and-services/scaling-new-energy-systems/geothermal/geothermal-exploration-drilling)).
- Slim holes cost about $100-200/ft
  ([OpenEI](https://openei.org/wiki/Slim_Holes)). One project's 3.9-inch slim hole cost about $150/ft, against
  $377/ft for a nearby production well
  ([The Driller](https://thedriller.com/articles/85554-slimhole-drilling-in-geothermal-exploration)).
- Ormat says exploration before the first full-size well costs **USD 1-5M per site**, excluding land
  ([Ormat FY2024 10-K](https://www.sec.gov/Archives/edgar/data/1296445/000162828025008531/ora-20241231.htm)).
- A full-size well costs about **USD 5M** with more than 50% failure, according to an investor;
  Zanskar claims it halves the failure rate and cuts the cost to about $2M per well
  ([Lowercarbon, via search snippet](https://lowercarboncapital.com/company/zanskar/)). These are
  secondary claims, not audited.

**Base success rate**
- The IFC study covered 2,613 wells. Success was about 60% in the exploration phase, about 75% in
  development and more than 80% in operation. The **first well is roughly 50:50**
  ([ESMAP/IFC](https://www.esmap.org/sites/esmap.org/files/1-Patrick%20Avato.pdf),
  [ThinkGeoEnergy](https://www.thinkgeoenergy.com/global-study-on-success-of-drilling-geothermal-wells-by-ifc/?amp=1)).
- In Iceland the first well succeeds 43% of the time, the first five 60%, and the rate plateaus at 74%
  ([ThinkGeoEnergy](https://www.thinkgeoenergy.com/report-success-of-high-temperature-geothermal-wells-in-iceland/)).
- Older sources put exploration-well success as low as 20%
  ([Bloomquist](https://www.bgr.de/GEOTHERM/ArGeoC1/pdf/02%20R.%20Gordon%20Bloomquist%20Determining%20the%20Feasibility%20of%20Electrical%20Generation%20Projects.pdf)).
- That base rate falls inside Dhruv's accepted 30-70% band, so a 1.5-3x lever counts.

**Who owns the unproven right, and what it costs**
- In the western US the rights are BLM competitive geothermal leases.
- Nevada, October 2025: 86 parcels and 280,559 acres received bids, with high bids totalling $8.87M. That
  is about **$32/acre on average (my arithmetic)**, with a top bid of $410/acre
  ([BLM results](https://www.blm.gov/sites/default/files/docs/2025-10/NV_Geot_20251021_Comp_Sale_Results.pdf),
  [ThinkGeoEnergy](https://www.thinkgeoenergy.com/blm-nevada-geothermal-lease-sale-nets-over-usd-9-million-in-bids-on-86-parcels/)).
- New Mexico, June 2026: **$107/acre on average**, a top tract at $701/acre, and a record $16.3M in total
  ([World Oil](https://worldoil.com/news/2026/7/28/new-mexico-geothermal-lease-sale-signals-higher-federal-acreage-values/)).
- Nevada in 2019: the top bid was only $20/acre
  ([ThinkGeoEnergy](https://www.thinkgeoenergy.com/details-on-results-and-key-bidders-of-recent-geothermal-lease-sale-in-nevada/)).
  Lease prices are rising fast, which shows competition is arriving.

**Step-up on success**
- In June 2025 Ormat bought Blue Mountain (20 MW) for $88.7M, about **$4.4M per MW**
  ([Nasdaq](https://www.nasdaq.com/articles/ormat-technologies-expands-electricity-generation-portfolio-acquisition-blue-mountain)).
- Zanskar says systems like Big Blind can each produce more than 100 MWe
  ([ThinkGeoEnergy](https://www.thinkgeoenergy.com/zanskar-announces-discovery-of-big-blind-geothermal-site-in-western-nevada-usa/)).
- Rough arithmetic (estimate): a confirmed but undeveloped resource might sell at 10-25% of
  operating-plant value, which would be $0.4-1M per MW. On a 4,000-acre lease bought for $130k-430k,
  a 50 MW confirmed resource would be worth tens of millions. That is a step-up of 50-100x or more.

**Capitalised buyers**
- Ormat (a serial acquirer), Fervo (IPO in May 2026 at about a $10B valuation, raising $1.89B; check
  against the S-1) ([BNN Bloomberg](https://www.bnnbloomberg.ca/business/2026/05/04/fervo-energy-eyes-us65-billion-valuation-in-us-ipo/),
  [SentiSense](https://app.sentisense.ai/stories/fervo-energy-completes-successful-ipo-raises-1.89b-reaches-10.21b-valuation-05132026)),
  Terra-Gen, utilities, and hyperscalers looking for firm clean power (memory: Google with Fervo,
  Meta with Sage).

**Would public data plus ML raise the hit rate?**
- Yes, and it has been shown. Zanskar's Big Blind had no surface features and no prior well data. It
  found the target with its prospecting toolkit and AI target selection: two intermediate wells hit a
  250°F reservoir at 2,700 ft
  ([Zanskar](https://zanskargeothermal.substack.com/p/zanskar-reveals-big-blind-the-discovery)).
- It also found Pumpernickel (137°C at 762 m) ([ASME](https://magazine.asme.org/issues/may-2026/news-hidden-geothermal-goldmines)).
- Public data exists in volume: the DOE Geothermal Data Repository, the Nevada Bureau of Mines and
  Geology grey-literature archive with thousands of old gradient holes and mining or oil-and-gas holes,
  and USGS heat-flow data (memory).

**Who already does it**
- **Zanskar.** $180M equity; plans to "develop, build, own, and operate"; Spring Lane, Obvious, USV and
  Lowercarbon invested; it calls itself the largest geothermal exploration company in the US
  ([VCA](https://www.vcaonline.com/news/2026012101/zanskar-raises-115m-series-c-following-record-setting-year-of-geothermal-discoveries/)).
  It bought the struggling Lightning Dock plant (BLM lease) in May 2024 and turned it around
  ([NM legislature handout](https://www.nmlegis.gov/handouts/WNR%20083126%20Item%208%20Zanskar%201-pager.pdf)).
- DOE Play Fairway and INGENIOUS academic programs (memory).
- Ormat's in-house exploration team.

**Verdict**
- This is the best rubric fit in the lane, and Terranox's playbook carries over directly.
- In the US it is **owned**: Zanskar has a two-to-three-year lead, the capital and the proof.
- What remains:
  - (a) A **lease-flipper**: prove and sell to Ormat, Fervo or utilities instead of building. This is
    capital-light and Zanskar will not do it, but Zanskar would compete for the same leases.
  - (b) **Outside the US**: Canada (BC, Alberta's Leduc/Swan Hills, Saskatchewan's Williston, where
    DEEP Earth Energy is the incumbent (memory)), Mexico, Chile, Kenya, Indonesia. Each has its own
    tenure rules and public-data quality, which needs checking.
- Inside the 10-03 ban (geothermal is named).

## 2. Groundwater: aquifer test wells for data centres and agriculture

**Cost of one proving hole**
- A production-scale test well plus a 72-hour pump test is **USD 0.1-1M** (estimate, memory). Deep
  municipal or industrial wells cost more.
- Analogues found: nine 2-inch monitor wells for about $80k
  ([LA DNR](https://www.dnr.louisiana.gov/assets/OC/env_div/Guidry/BP/AppendixQ/04HETActiveRemediation.pdf)).
- No sourced data-centre figure exists. Data-centre campuses do commission groundwater-sufficiency
  studies, for example the Pairmont study in Virginia
  ([Spotsylvania County](https://www.spotsylvania.va.us/DocumentCenter/View/41106/Pairmont-Hydrogeological-Assessment)).

**Base success rate**
- Unsourced. In hard-rock or fractured aquifers, success for high-yield wells is commonly cited at
  30-60% (memory).

**Who owns the unproven right**
- In the western US (prior appropriation) the rights are tradable water rights. Appropriating a new
  right needs a permit plus proof of beneficial use.
- Proven, adjudicated rights in Arizona, Nevada and Colorado sell for thousands to tens of thousands of
  USD per acre-foot (memory). Unproven applications or land over an aquifer cost far less.

**Step-up and buyers**
- Data centres (Arizona, Nevada, Texas), homebuilders and farms.
- Memory: D.R. Horton bought Vidler Water Resources for about USD 290M in 2022. Water Asset Management
  and Cadiz are other players.

**Would public data plus ML raise the hit rate?**
- Plausibly. State driller-log archives are vast and hard to read: scanned PDFs, lithology written
  free-text. USGS NWIS and InSAR subsidence data are also public. The analogue is SMAD.

**Who does it**
- Hydrogeology consultancies (a services market) and water-rights investors.
- No well-known ML discover-and-flip company came up in searching (thin evidence).

**Verdict**
- Second-best fit. But water is politically capped: new appropriations are closed in many basins, so
  the cheap right may not exist. The hit rate is not clearly "usually failing", and the ceiling is
  uncertain.
- Outside the 10-03 ban (groundwater is not on the banned list). **Worth a focused follow-up lane.**

## 3. CCS pore space and Class VI stratigraphic test wells

**Cost of one proving hole**
- No per-well figure turned up in searching.
- The Wyoming CarbonSAFE Phase III program as a whole costs $19.5M including 2-3 strat test wells
  ([carbonstorage.io](https://www.carbonstorage.io/storage/wyoming-carbonsafe-project-phase-iii)).
- Carbon GeoCapture's $7.2M field subcontract covered 3 strat wells
  ([NETL](https://netl.doe.gov/sites/default/files/netl-file/21CMOG_CCUS_McLaughlin.pdf)).
- That implies roughly **USD 2-5M per onshore strat well in Wyoming** (estimate). Gulf Coast deep wells
  with whole core are commonly cited at USD 10-30M (memory).
- Site characterisation is a sunk cost whether or not the project goes ahead
  ([Hovorka/GWPC](https://www.gwpc.org/wp-content/uploads/2024/04/Hovorka_CCSEconomics.pdf)).

**Base success rate**
- High. Most Gulf Coast and Permian saline formations are known from thousands of oil and gas logs.
  The well confirms injectivity and seal; it rarely discovers anything (memory, estimate).
- The real failure modes are permit delay and offtake, not dry holes. So rubric 1 is weak.

**Who owns the unproven right, and what it costs**
- Initial bonuses: Talos Bayou Bend about $110/acre (40,200 acres for $4.5M); Air Products $50/acre;
  Capio $34/acre ([LSU, Keith Hall](https://collegium.lsu.edu/energy-innovation/news/files/keith_hall_ccus_iei_may.pdf)).
- Royalties run 3-6%.
- Frontier Carbon Solutions has more than 100,000 acres of leased pore space and the first three
  Wyoming Class VI permits
  ([OilandGas360](https://www.oilandgas360.com/frontier-carbon-solutions-secures-first-permits-for-sweetwater-carbon-storage-hub-in-wyoming)).

**Step-up and buyers**
- Buyers are emitters and oil majors. Memory: Exxon bought Denbury for $4.9B in 2023, largely for the
  CO2 pipelines; Oxy, CRC/Carbon TerraVault, Chevron and Talos are the others.
- A permitted Class VI site is the proven state, and the step-up is real but undisclosed.
- Demand depends on 45Q. Memory: 45Q survived the 2025 budget law, but many hubs have stalled.

**Public data plus ML**
- Yes. State well-log libraries (Texas RRC, Louisiana SONRIS, KGS) are classic hard-to-read public
  data. Stanford's Earthflow AI/CCSNet does ML subsurface modelling
  ([Stanford OTL](https://otl.stanford.edu/researchers/high-impact-technology-hit-fund/hit-portfolio%23sustainability/earthflow-ai-subsurface)).
  LSU is building a statewide site heat map
  ([LSU](https://lsu.edu/cce/mediacenter/news/2023/10/mukhopadhyay_ccus_ai.php)).
- TGS sells Gulf Coast CO2 storage assessments
  ([Ocean News](https://oceannews.com/?p=100714)).

**Verdict**
- A middling fit: the right is cheap, but the hole usually confirms rather than fails, buyers depend on
  policy, and data incumbents (TGS, S&P) are present. Inside the 10-03 ban.

## 4. Natural (geologic) hydrogen
- **Cost of a hole:** HyTerra's Sue Duroche 3 in Kansas went to 1,052 m and was "on time and on
  budget", with no figure disclosed. Fortescue's $21.9M investment funds the 12-month program
  ([Stockhead](https://stockhead.com.au/energy/hyterra-off-to-rousing-start-as-first-well-returns-up-to-96-1pc-hydrogen),
  [HyTerra ASX Mar 2026](https://announcements.asx.com.au/asxpdf/20260331/pdf/06y0mfgqhpq8x5.pdf)).
  A Kansas well of that depth is likely USD 1-3M (estimate).
- **Results:** mud gas readings showed up to 96% hydrogen and 5% helium, but these are preliminary.
  The well was converted to a monitoring well.
- **Base rate:** unknown. Memory: Mali's Bourakebougou is the only producing hydrogen field.
- **Players:**
  - Koloma: $245M Series B led by Khosla, plus Amazon and United; uses AI-assisted tools
    ([Canary Media](https://canarymedia.com/articles/hydrogen/the-245m-bid-to-pull-clean-hydrogen-straight-from-the-earth)).
    S&P reported in January 2025 that it was quiet on next steps after test drilling
    ([S&P Global](https://spglobal.com/commodity-insights/en/news-research/latest-news/energy-transition/012425-geologic-hydrogen-explorer-koloma-with-400-mil-in-funding-quiet-on-next-step)).
  - Mantle8: €3.4M seed from BEV and Kiko, uses AI ([Sifted](https://sifted.eu/articles/natural-hydrogen-mantle8-bill-gates)).
  - Getech: ML hydrogen locator ([Hydrogen Central](https://hydrogen-central.com/getech-unlock-natural-hydrogen-exploration-sites/)).
  - Snowfox, backed by Rio Tinto and BP.
- **Verdict:** rubric 4 fails, because no one yet pays a step-up for a proven hydrogen lease; offtake
  and economics are unproven. The space is crowded with well-funded explorers already using ML. Inside
  the ban.

## 5. Lithium brine (Smackover)
- **Step-up:** Equinor committed up to USD 160M for 45% of Standard Lithium's SW Arkansas and East Texas
  projects ($30M cash, a $60M work program, and $70M due at FID)
  ([Standard Lithium](https://www.standardlithium.com/_resources/news/nr-20240508.pdf)).
- **Hole:** new wells confirm grades of 663-806 mg/L Li
  ([JPT](https://jpt.spe.org/firm-claims-texas-well-holds-highest-lithium-concentrations-in-north-america),
  [Arkansas Business](https://www.arkansasbusiness.com/article/new-standard-well-yields-high-concentrations-of-lithium-potash-and-bromine/)).
  Grades are largely predictable from legacy oil-field brine sampling. No sourced well cost; likely
  USD 2-5M (estimate).
- **Verdict:** discovery is not the hard step (DLE processing and royalty rulings are), and Exxon,
  Chevron, Equinor and others are already leasing. Rubric 1 fails. Inside the ban.

## 6. Helium
- Pulsar's Topaz project in Minnesota hit gas in all 7 of 7 wells, but drilling fines restricted flow in
  testing ([Mesabi Tribune](https://www.mesabitribune.com/news/local/pulsar-helium-goes-seven-for-seven/article_9d4d47f1-7529-4d7e-b24c-32cc17f88f96.html),
  [Crux](https://www.cruxinvestor.com/posts/pulsar-helium-extends-topaz-project-footprint-with-sixth-consecutive-gas-discovery)).
- Saskatchewan helium wells cost about CAD 2-5M (memory). They use the same Saskatchewan public
  databases as Terranox, which is an adjacency worth noting.
- **Verdict:** the ceiling fails. The global helium market is roughly USD 3-6B a year (memory), and the
  buyers (Linde, Air Products) sign offtake rather than paying a step-up for land. Many juniors are
  already in it. Inside the ban.

## 7. Salt-cavern storage characterisation (hydrogen, gas, CAES)
- Memory: one characterisation well costs a few USD million. US Gulf salt domes are mapped by decades
  of oil and gas drilling, so the hole confirms thickness and purity rather than discovering anything.
  Examples include the ACES Delta hydrogen hub in Utah and NYSERDA and European studies.
- **Verdict:** a low fit. The hole rarely fails, and buyers and operators control their own sites.

## 8. Oil and gas wildcats
- In 2024, 75 high-impact wells produced 19 commercial discoveries, a 25% success rate. The supermajors
  managed 5% net ([Westwood](https://www.westwoodenergy.com/news/westwood-insight-the-state-of-exploration-2025)).
- Norway 2014-2023: 289 wells for USD 12.1B, which is about $42M per well (my arithmetic), with 28%
  commercial success ([energy-pedia / Westwood](https://www.energy-pedia.com/news/norway/westwood-insight-%E2%80%93-norway-state-of-exploration-2014-2023-197013)).
- **Verdict:** this is the biggest "expensive hole" market. But it is saturated: the majors' in-house
  ML, TGS/CGG/SLB, and many AI startups (memory: Earth Science Analytics, Bluware). The signal is in
  proprietary seismic, and licences go through competitive government rounds. Kill. Inside the ban.

## 9. Offshore wind site investigation boreholes
- The geotechnical survey for a 1 GW floating farm is about GBP 5M
  ([Guide to Floating Offshore Wind](https://guidetofloatingoffshorewind.com/?p=544)).
- A Baltic campaign covered 64 boreholes at 49 locations ([ENS](https://ens.dk/media/6069/download)).
- Triton Knoll ran a 3-week Fugro programme over 92 locations
  ([Triton Knoll](https://www.tritonknoll.co.uk/?p=1634)).
- **Verdict:** these holes characterise an already-leased seabed and do not discover anything. Fugro
  and others sell them as a service. Fails rubrics 1, 3, 4 and 6. Outside the ban.

## 10. Geotechnical boreholes for infrastructure
- No sourced cost. Onshore holes cost thousands to tens of thousands of USD each (memory). Unforeseen
  ground conditions are a known cause of overruns (memory).
- **Verdict:** the project owner already holds the land, so there is no unproven right to buy. The
  market is a consulting service: Fugro, Arup, Golder/WSP. Kill. Outside the ban.

## 11. Nuclear repository site-characterisation boreholes
- NWMO drilled 6 boreholes about 1,000 m deep at Ignace and 2 at South Bruce, about 90 days each. The
  whole program is estimated at about CAD 24B
  ([World Nuclear News](https://www.world-nuclear-news.org/Articles/First-borehole-drilled-in-Canadian-repository-site),
  [NWMO](https://annualreport.nwmo.ca/2020_22/site-assessment/)).
- **Verdict:** there is one state buyer, sites are chosen by consent rather than discovery, and no
  right is tradable. Deep Isolation (memory) does borehole disposal technology, not discovery. Kill.
  Outside the ban.

---

## Implications for the drill-hole hunt
- The pattern Dhruv likes (cheap right, hole that usually fails, public hard-to-read data, step-up
  buyer) fits **hydrothermal geothermal** best outside uranium and minerals, and Zanskar proves the
  thesis works and gets funded. That is evidence for the rubric, and it is also the strongest
  competitor to any geothermal copy.
- The "make the hole cheaper, fewer, or more informative" angle across industries points to a
  horizontal tool, such as cheaper slim-hole or gradient drilling or downhole sensing. That is a
  service or tool market and would probably fail rubric 6 unless paired with owning the rights.
- **Follow-ups needed (search budget ran out):**
  - Zanskar's lease count and whether it ever sells leases.
  - Canadian geothermal tenure costs (BC, Alberta, Saskatchewan).
  - Western US water-right prices and new-appropriation availability for data centres.
  - Sourced Gulf Coast strat-well costs from Class VI permit applications.
