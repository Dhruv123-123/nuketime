# Round 2: groundwater rights in the arid western US, tested properly

Written 19 Oct 2026, as a follow-up to lane G's second-ranked idea (see BRIEF.md and
lane_G_adjacent_holes.md).

The idea under test: buy or claim unproven groundwater (land or applications) cheaply, choose test
wells with ML trained on public driller logs, prove the yield, then sell the proven right or the
water-secured land at a step-up to data centres, industry, farms or cities.

Labels: "(memory)" means from memory and unsourced; "(estimate)" means my own reasoning; "(my
arithmetic)" means derived from the cited figures.

## Summary (the 10 lines that matter)
1. **Verdict: KILL.** In western water, discovery is not the hard step. The legal permit is. The
   state decides how much water a right can carry from a basin-wide water budget (Nevada, New
   Mexico, Utah) or from how much land sits over the aquifer (Colorado's Denver Basin; acreage-based
   permits in many Texas districts, which is from memory). A well that proves yield does not
   create a bigger right. Rubric 1 fails.
2. **This exact business has already been run, for 25 years. Vidler Water (formerly PICO)** filed
   applications for more than 100,000 acre-feet (AF) in rural Nevada and drilled deep test wells that
   yield 600-2,000 gpm. It expected only up to 40,000 AF to be permitted
   ([Vidler 10-K FY2021](https://www.sec.gov/Archives/edgar/data/830122/000083012222000009/vwtr-20211231.htm),
   [NGWA](https://ngwa.confex.com/ngwa/cdg2014/webprogram/Paper9891.html)).
3. **What the regulator did to Vidler's applications:**
   - Tule Desert: applied for 14,000 AF and got 2,100 AF, then a further 396 AF instead of the
     7,240 AF it asked for. That brought a USD 12.4M impairment
     ([SEC](https://www.sec.gov/Archives/edgar/data/830122/000083012212000008/R11.htm)).
   - Kane Springs: Order 1309 subordinated the rights.
   - New Mexico: the Campbell Ranch application was denied (10-K above).
4. **Vidler's exit was modest.** D.R. Horton paid USD 291M, which was **only a 39% premium to book**
   and a 19% premium to the 90-day share price
   ([SEC 8-K](https://www.sec.gov/Archives/edgar/data/830122/000119312522105010/d315776dex991.htm)).
   Vidler carried USD 139.7M of federal tax losses (10-K above). Over decades, the result was about
   USD 0.3B.
5. **Cadiz shows the downside.** It has been working for about 30 years on one large proven aquifer
   (memory). It is still "pre-revenue" on its water bank, has a market cap of about USD 350-580M,
   and posted a FY2025 net loss of USD 34M
   ([roic.ai](https://www.roic.ai/quote/CDZIP), [americancompanies](https://americancompanies.com/company/cadiz-inc/)).
   Proving the water was never the bottleneck. Permits, politics and conveyance were.
6. **New appropriation is closed or closing almost everywhere it is valuable:**
   - Arizona: no new groundwater certificates in the Phoenix AMA since 2023, against 4.86M AF of
     modelled unmet demand ([ADWR](https://azwater.gov/phoenix-ama-groundwater-supply-updates)).
     Moving groundwater between basins is banned except from 4 basins.
   - Nevada: basins are frozen one by one, for example Red Rock Valley in 2025.
   - New Mexico and Utah: basins are being closed one at a time.
7. **The step-ups are real, but they pay for legal paper, location and pipe, not for proven yield:**
   - Colorado-Big Thompson units: USD 58-85k/AF.
   - Fish Springs credits: about USD 41k/AF.
   - Dodge Flat, Nevada: about USD 7k/AF.
   - Pure Cycle's recent purchases: above USD 20k/AF.
   - Texas leases to cities: USD 460-2,300/AF.
   - Nevada state buyback of over-pumped rights: about USD 900-1,000/AF.
   - Arizona long-term storage credits: USD 350-450/AF.
   - Greenstone doubled its money on Cibola land by selling the water to Queen Creek. That was
     surface water, with no hole involved.
8. **Data centres are a small buyer.** Project Blue (Tucson) rests on 96.5 AF a year of existing
   rights ([AZPM](https://azpm.org/s/103423-arizona-water-officials-approve-wells-tied-to-project-blue-data-center/)).
   Meta Mesa plans 550-1,100 AF a year. Data centres mostly buy from utilities, not by acquiring
   aquifers.
9. **Test wells cost USD 20k-360k** (shallow wells up to a 900 ft test well), plus USD 150-300k for
   a pump test. Deep carbonate wells are probably USD 1-5M (estimate). I found no sourced base rate
   for western alluvial wells; in basin-fill aquifers water is usually found (estimate). The hole is
   "usually confirming", not "usually failing".
10. **ML on driller logs already exists in public science.** USGS built a 3D texture model from about
    8,500 driller logs, using kriging rather than ML
    ([USGS](https://www.usgs.gov/publications/development-a-three-dimensional-model-sedimentary-texture-valley-fill-deposits-central)).
    I found no funded ML groundwater-siting startup in the US. The likely reason is that siting
    better wells is worth about a test well per project, which makes it a tool market. The only
    sliver still open is Texas brackish groundwater (see section 9), and it scores low.

**Position relative to the 2026-10-03 ban:** the idea is drilling-based (proving holes), but water is
not on the banned list.

---

## 1. Rubric score

| Rubric item | Score | Why |
|---|---|---|
| R1. Discovery is 80%+ of a rung's work | **fail** | The permit volume comes from the basin budget or the overlying acreage, not from the well. Vidler, SNWA, Cadiz and Pure Cycle were all limited by the regulator or the courts, not by dry holes (sections 4 and 6). |
| R2. Public, hard-to-read data where ML is needed | M | Driller logs are public and messy. But USGS and state agencies already compile them (CVHM2), and better siting does not unlock more legal water. |
| R3. The unproven right can be bought cheaply | M | Texas groundwater in place costs roughly USD 350-490 per acre of rights (section 5). Nevada applications are cheap to file but get cut back or denied, and the valuable basins are closed. |
| R4. A capitalised buyer pays a step-up at once | M | The step-up exists (USD 7-85k/AF), but it takes 5-25 years of permitting and conveyance, so it is not "at once". |
| R5. A ladder to climb | L | The next rung up is utility, pipeline or homebuilder. Those rungs are political and capital-heavy, as Cadiz's 30 years and SNWA's rejected pipeline show. |
| R6. Ceiling | **fail** | The best outcome in the category (Vidler) was about USD 0.3B over about 25 years. California's whole traded water market was USD 2.6B over 2012-2019, about USD 0.3B a year ([CME](https://www.cmegroup.com/education/courses/introduction-to-the-nasdaq-veles-water-index-futures/understanding-the-nasdaq-veles-california-water-index.html)). |
| Already owned by | | Vidler (now part of D.R. Horton), Water Asset Management, Greenstone (MassMutual), Cadiz, Pure Cycle, Texas marketers (Blue Water, Mesa), WestWater Research (broker and data) |

**Kill.** Failing R1 and R6 both rest on sourced evidence, not on inference.

---

## 2. Cost of a proving hole

| Item | Cost (USD) | Source |
|---|---|---|
| Shallow municipal test well (Commerce, GA, 2024, up to 6 wells) | 20,240 per well | [Commerce RFP](https://commercega.gov/business/bid-opportunities/Open%20Bids/24-010%20Test%20Well%20Drilling/24-010%20RFP%20Test%20Wells%20Ad.pdf) (award reported in search snippet) |
| 900 ft test well (Clallam County, WA, 2019) | 356,864 bid | [Sequim Gazette](https://www.sequimgazette.com/news/x-6) |
| Municipal test hole (Orangevale, CA, 2025) | 186,870 | [ConstructConnect](https://projects.constructconnect.com/details/7213171-municipal-well-test-hole-drilling%26find_loc=california-95662) |
| Pump test, Madison aquifer (Rapid City, SD, 2024) | about 150,000 (estimate by city staff) | [Rapid City](https://www.rcgov.org/agenda-items/public-works-committee-agenda-items/2024-pw-agenda-items/pw043024-03-12990.html) |
| Well rehabilitation plus pump test (Rapid City, 2024) | 305,096 | [Rapid City](https://www.rcgov.org/agenda-items/city-council-agenda-items/2024-cc-agenda-items/cc011624-02-3-well-6-redevelopment-and-pump-testing-12669.html) |
| Full municipal well including test borehole (Lakeville, MN, 2024) | 675,280 | [ConstructConnect](https://projects.constructconnect.com/details/6452970-construction-of-well-23%26find_loc=minnesota-55044) |
| Irrigation and high-capacity drilling rate | 25-60 per ft | [Waterfilterguru](https://waterfilterguru.com/?p=39761), [ThePricer](https://www.thepricer.org/cost-to-dig-a-well/) (low-quality sources) |
| Deep Nevada carbonate test and production wells (815-3,800 ft deep, bowls set at 1,200-1,800 ft) | no cost disclosed; probably 1-5M (estimate) | [NGWA](https://ngwa.confex.com/ngwa/cdg2014/webprogram/Paper9891.html) |

**Comparison with uranium.**
- A western water test well plus pump test usually costs USD 0.1-0.5M; deep carbonate wells cost more.
- The hole is about 1-10% of the value of a modest permitted right. For example, 2,000 AF at
  USD 7k/AF is worth USD 14M (my arithmetic).
- The hole is therefore not the expensive step. The legal process is: protests, hearings, a flow
  model, and environmental review. That is consistent with Vidler's multi-decade timelines.

## 3. Base success rate of test wells for a target yield
- **No sourced western-US statistic was found.** I searched USGS, NGWA and state sources and nothing
  turned up.
- The evidence that does exist:
  - Lincoln/Vidler's deep carbonate production wells sustain 600-2,000 gpm (NGWA, above). The
    abstract does not say how many attempts that took.
  - In a 1979 basalt-aquifer report of unclear location, 27% of bores were dry and 13% succeeded in
    one area ([report](https://mrt.stgro-2780.saas.squiz.cloud/mrtdoc/dominfo/download/UR1979_16/UR1979_16.pdf)).
  - Alberta's prairie aquifers have "remarkably low" dry rates
    ([PFRA](https://bac-lac.wayback.archive-it.org/web/20061210122835/http:/agr.gc.ca/pfra/water/reports/ponoka-03.pdf)).
- **My estimate:**
  - In the alluvial basin-fill aquifers that host most western water development, a properly sited
    well almost always finds water. Yield varies by a factor of a few.
  - Fractured rock and carbonate aquifers are more hit-or-miss, perhaps 30-60% (memory, from lane G).
  - Overall, the hole is "usually confirming". The real failure mode is that the regulator
    awards less than the well can pump (section 4).

## 4. Can new rights still be appropriated? (legal regime by state)

| State | Regime | New appropriation available? | Evidence |
|---|---|---|---|
| Nevada | Prior appropriation. The State Engineer sets each basin's perennial yield and designates basins. | Mostly no where it matters. Red Rock Valley was frozen in June 2025 (Order 1339). Coyote Springs and the Lower White River Flow System were merged into a "superbasin" (Order 1303), upheld by the Nevada Supreme Court in 2024; hundreds of permits were denied. SNWA's 250-mile pipeline lost its rights in 2020 over depletion. There are 256 basins and sub-areas. | [Western Water](https://www.western-water.com/2025/06/13/nevada-freezes-new-groundwater-rights-in-red-rock-valley/), [Nat Ag Law](https://nationalaglawcenter.org/supreme-court-of-nevada-issues-important-decision-impacting-groundwater-rights/), [Las Vegas Sun](https://m.lasvegassun.com/news/2020/mar/10/court-strikes-down-southern-nevada-water-authority/), [CWSD](https://www.cwsd.org/wp-content/uploads/2018/05/2018-11-Water-Summit-KING.pdf) |
| Arizona | Inside AMAs: grandfathered rights plus Assured Water Supply rules. Outside AMAs: "reasonable use" with almost no permit. | Inside AMAs: no. Phoenix AMA groundwater certificates paused since 2023, and the 2024 model update still does not support them. Outside AMAs: you can pump, but it is illegal to move the water to an AMA except from McMullen, Butler, Harquahala and Big Chino (1991 Act). | [ADWR](https://azwater.gov/phoenix-ama-groundwater-supply-updates), [ASU](https://azwaterinnovation.asu.edu/understanding-arizonas-groundwater-transportation-basins), [AZ Leg](https://www.azleg.gov/legtext/57leg/2R/summary/H.HB2934_020426_NREW.DOCX.htm) |
| New Mexico | Prior appropriation. The State Engineer administers all 39 declared basins. | Basins are closed one at a time: Hot Springs (2023), part of Gallup (2023), Curry/Portales, Estancia, Lea County and Sandia. Vidler's Campbell Ranch application was denied in 2014 and lost on appeal in 2019. | [OSE](https://www.ose.state.nm.us/hottopics.php), [Sierra County Citizen](https://sierracountycitizen.org/state-engineer-closes-hot-springs-underground-water-basin/), [Vidler 10-K](https://www.sec.gov/Archives/edgar/data/830122/000083012222000009/vwtr-20211231.htm) |
| Utah | Prior appropriation. The State Engineer uses basin policies and proclamations. | Large areas are closed: Sevier groundwater (1997), Tooele (1996), Snyderville (2019), and the Great Salt Lake basin (temporary closure in 2022). | [Utah DWRi Sevier](https://waterrights.utah.gov/wrinfo/policy/sevier.htm), [Snyderville](https://waterrights.utah.gov/wrinfo/mmplan/ugw/snydvll.htm) |
| Colorado | Tributary groundwater is under prior appropriation, and its rivers are over-appropriated. Denver Basin nontributary groundwater is **allocated by overlying land ownership** at about 1% a year over a 100-year aquifer life. | Tributary: new junior rights are near worthless, so new uses buy senior rights. Nontributary: the volume is set by acreage and aquifer thickness, not by a test well. Pure Cycle's application for a new 1,635 AF right was denied. | [CSU Water Knowledge](https://waterknowledge.colostate.edu/water-management-administration/water-rights/groundwater-rights/), [Stock Titan / PCYO 10-K](https://www.stocktitan.net/sec-filings/PCYO/10-k-pure-cycle-corp-files-annual-report-d0d84ccf578e.html) |
| Texas | Rule of capture. Since *Edwards Aquifer Authority v. Day* (2012), groundwater in place is real property, like oil and gas. Production is regulated by groundwater conservation districts (GCDs) under Chapter 36. | Yes, through district permits. This is the one state where you can buy or lease water in place from ranchers without the state's consent. But GCDs cap production (often per acre, from memory), and permits are contested (Corpus Christi vs Sinton in 2026). | [Dykema](https://www.dykema.com/news-insights/changes-to-texas-groundwater-rights-edwards-aquifer-authority-v-day.html), [Yale LJ](https://yalelawjournal.org/forum/liquid-assets-groundwater-in-texas), [Inside Climate News](https://insideclimatenews.org/news/19052026/corpus-christi-emergency-water-supply-delays/) |

**What this means.** In 5 of 6 states, a test well does not decide how much water you own:
- In prior-appropriation states, the cap is the regulator's basin budget, and it is shrinking.
- In Colorado's Denver Basin, the cap is your acreage.
- Texas is the exception in law, but districts still cap production, often by acreage.

## 5. Prices of water rights ($/AF)

| Place and type | USD per AF | Source |
|---|---|---|
| Colorado-Big Thompson units (Northern Colorado) | 58,772 (2024) and 57,487 (2025), per Northern Water's table; auction average about 52-75k (Feb 2024); WestWater puts it at 85k (2025), down from 101k (2022) | [Northern Water](https://www.northernwater.org/getmedia/45190426-0f57-4325-8320-82199f21b984/Colorado-Big-Thompson-Units-Market-Price-Historical-Data), [Colorado Sun](https://coloradosun.com/2026/04/24/colorado-water-prices/), [Coyote Gulch](https://coyotegulch.blog/2024/02/24/colorado-farmers-find-plenty-of-sweet-deals-at-4-7-million-front-range-water-auction-fresh-water-news-coloradoriver-southplatteriver-coriver-aridification/) |
| Pure Cycle's recent purchases (Denver area) | above 20,000, up from 9,700 four to five years earlier | [PCYO 10-K summary](https://www.stocktitan.net/sec-filings/PCYO/10-k-pure-cycle-corp-files-annual-report-d0d84ccf578e.html) (transcript quoted in search snippet) |
| Fish Springs water credits (Reno North Valleys, Nevada) | about 41,000; list price 43,575 residential and 37,800 commercial (2021) | [Vidler 10-K / BusinessWire](https://www.businesswire.com/news/home/20210810005406/en) |
| Dodge Flat (Nevada) | about 6,700-7,100 (my arithmetic: 612 AF for USD 4.1M in 2020; 296 AF for USD 2.1M in 2021) | [Vidler 10-K](https://www.sec.gov/Archives/edgar/data/830122/000083012222000009/vwtr-20211231.htm) |
| Nevada state buyback (rural, over-pumped basins) | 350-900 base; pilot average just over 1,000 | [Nevada Current](https://nevadacurrent.com/2024/03/26/more-willing-water-rights-sellers-in-nv-than-money-say-water-regulators/), [Western Water](https://www.western-water.com/2024/04/02/nevada-groundwater-rights-buyouts-face-challenges/) |
| Arizona long-term storage credits (Harquahala, Phoenix AMA) | 347.50 (2019), 400 (2021), 450 list | [Vidler 10-K](https://www.sec.gov/Archives/edgar/data/830122/000083012222000009/vwtr-20211231.htm) |
| Cibola Colorado River entitlement to Queen Creek, AZ (sold by Greenstone) | about 10,000 (2,083 AF for about USD 20.8M); land cost USD 9.8M | [KJZZ via Cronkite](https://cronkitenews.azpbs.org/?p=88668), [Mother Jones](https://www.motherjones.com/?p=1051824) |
| Texas Carrizo-Wilcox (2014) | 460 paid to Blue Water; 1,900 to SAWS | [TAMU TRERC](https://trerc.tamu.edu/wp-content/uploads/files/PDFs/Articles/1691.pdf) |
| Vista Ridge, delivered to SAWS (Texas) | about 1,600-2,300 | [Texas Tribune](https://www.texastribune.org/2014/11/12/thirsty-san-antonio-embraces-private-sector-risks), [Houston Chronicle](https://preview-prod.w.houstonchronicle.com/news/local/article/Like-it-or-not-Vista-Ridge-pipeline-now-15260352.php) |
| Edwards Aquifer (Texas) | 1,750-2,500 for unrestricted rights (undated) | [TAMU TRERC](https://trerc.tamu.edu/wp-content/uploads/files/PDFs/Articles/1357.pdf) |
| Roberts County groundwater in place (Texas, Pickens/Mesa to CRMWA, 2011) | USD 103M for 211,217 acres of rights, about USD 488 per acre (my arithmetic); CRMWA paid USD 349 per acre in 1997 | [HPPR](https://www.hppr.org/hppr-environment/2013-07-12/negotiations-begin-to-sell-texas-water-rights-to-oklahoma-buyers), [AAPG Explorer](https://explorer.aapg.org/story/articleid/45805/deg-cool-clear-water) |

**The spread is about 100x** (USD 350 to 85,000 per AF). It is explained by:
- seniority and legal reliability;
- how close the water is to a growing city;
- whether there is conveyance;
- whether the water is "wet" or only on paper.

None of these is the hydrogeologic yield a test well proves. The water that sells at USD 40-85k/AF
is already proven and senior. The water you can still claim cheaply is remote and junior, and
regulators cut it.

## 6. Real deals and what they show

**Vidler Water Resources (formerly PICO), 1990s to 2022.**
- This is the closest real-world copy of the proposed company.
- What it did:
  - Filed large applications in rural Nevada basins (Tule Desert, Kane Springs, Clover and Dry Lake
    valleys).
  - Drilled test wells 815 to more than 3,800 ft deep and production wells 1,810-2,732 ft deep, with
    geophysics and isotopes.
  - Built flow models, and in Reno built a 35-mile pipeline
    ([NGWA](https://ngwa.confex.com/ngwa/cdg2014/webprogram/Paper9891.html),
    [10-K](https://www.sec.gov/Archives/edgar/data/830122/000083012222000009/vwtr-20211231.htm)).
- What it got:
  - Tule Desert: applied for 14,000 AF and was awarded 2,100 AF plus 396 AF, then 7,240 AF after a
    2010 settlement, with a USD 12.4M impairment
    ([SEC](https://www.sec.gov/Archives/edgar/data/830122/000083012212000008/R11.htm)).
  - Kane Springs: subordinated by Order 1309 in 2020. Order 1309 was vacated in April 2022, but the
    final outcome is unknown
    ([Barchart](https://www.barchart.com/story/news/8038861/vidler-water-resources-inc-announces-vacation-by-nevada-district-court-of-nevada-state-engineers-order-1309)).
  - Campbell Ranch, New Mexico: denied.
  - Fish Springs: 12,628 AF permitted, but only 5,000 AF approved for transfer, and that still
    needed BLM rights-of-way. Its preferred capital balance had reached USD 201.5M, including
    USD 107M of accrued interest.
- The exit: D.R. Horton bought it for USD 291M in 2022, a 39% premium to book
  ([SEC 8-K](https://www.sec.gov/Archives/edgar/data/830122/000119312522105010/d315776dex991.htm)).
  PICO's long-run shareholder returns were poor (memory).
- **Lesson:** the hydrogeology worked, and the 600-2,000 gpm wells succeeded. The business was still
  mediocre, because the regulator, the pipe and the timeline set the value.

**Cadiz (CDZI).**
- It holds a large proven Mojave aquifer.
- After decades it is still pre-revenue on the water project. It has agreements with EPCOR
  (25,000 AF/yr), Lytton Rancheria financing, a market cap of about USD 350-580M, and a FY2025 loss of
  USD 34M ([roic.ai](https://www.roic.ai/quote/CDZIP),
  [americancompanies](https://americancompanies.com/company/cadiz-inc/),
  [VIC 2012](https://valueinvestorsclub.com/idea/CADIZ_INC/3360682474)).
- Proven water with no permitted path to a buyer is worth little.

**Pure Cycle (PCYO).**
- It holds 30,602 AF in the Denver area and makes money from tap fees: about 179 Sky Ranch taps for
  USD 7.1M in FY2025, roughly USD 40k per tap
  ([Stock Titan](https://www.stocktitan.net/sec-filings/PCYO/10-k-pure-cycle-corp-files-annual-report-d0d84ccf578e.html)).
- It is a small utility and land developer, not a discovery business.

**Water Asset Management (Disque Deane).**
- It buys land that carries water rights: about USD 100M for 12,793 acres in McMullen Valley,
  Arizona (one of the 4 basins whose groundwater can legally be moved), and Grand Valley farms in
  Colorado ([KD Miner](https://www.kdminer.com/news/hedge-fund-s-100m-arizona-farmland-buy-stirs-fears-of-water-grab/article_0598ffeb-81d0-5277-ac6a-56830cf1ec3d.html),
  [Inside Climate News](https://insideclimatenews.org/news/05062020/western-colorado-water-purchases-farming-agriculture)).
- The play is legal arbitrage (moving water from farm to city), not discovery.

**Greenstone (MassMutual) at Cibola.**
- It bought 485 acres for USD 9.8M and sold the Colorado River entitlement to Queen Creek for about
  USD 21-24M, a gross profit of about USD 14M
  ([Mother Jones](https://www.motherjones.com/?p=1051824)).
- A federal judge later found the environmental review inadequate.
- The step-up of about 2x came from surface water, with no hole involved.

**Mesa Water (T. Boone Pickens), Texas.**
- It assembled about 200,000 acres of Ogallala rights in Roberts County and sold them to CRMWA for
  USD 103M in 2011 after its pipeline plan failed
  ([HPPR](https://www.hppr.org/hppr-environment/2013-07-12/negotiations-begin-to-sell-texas-water-rights-to-oklahoma-buyers),
  [Texas Observer](https://www.texasobserver.org/2950-political-intelligence-department-of-dry-holes/)).
- The Ogallala in Roberts County was never in doubt, so this was not a discovery play either.

**Blue Water / Vista Ridge (Texas).**
- It signed thousands of landowner leases in Burleson and Milam counties, obtained about 36-51k AF/yr
  of district permits, and sells to SAWS at about USD 1,600-2,300/AF delivered
  ([San Antonio Report](https://sanantonioreport.org/request-to-pump-more-water-sparks-renewed-vista-ridge-opposition/)).
- This is the nearest Texas version of "lease cheap, permit, sell at a step-up". The value came from
  aggregating land, getting the permit and building the pipe, not from finding water in the
  Carrizo-Wilcox.

**Data centres.**
- Project Blue (Tucson area) relies on 96.5 AF/yr of existing rights
  ([AZPM](https://azpm.org/s/103423-arizona-water-officials-approve-wells-tied-to-project-blue-data-center/)).
- Meta Mesa plans 550-1,100 AF/yr ([DCD](https://datacenterdynamics.com/en/news/huge-data-center-moves-forward-in-mesa-despite-arizona-water-concerns)).
- The Imperial Valley project needs about 880 AF/yr through "buy and dry"
  ([GadgetReview](https://www.gadgetreview.com/californias-biggest-ai-data-center-is-suing-for-colorado-river-water)).
- Texas data centres mostly enter the Edwards market through a utility
  ([Spectrum](https://spectrumlocalnews.com/tx/south-texas-el-paso/news/2026/05/19/experts-praise-edwards-aquifer-water-market)).
- Even at USD 20k/AF, 1,000 AF is USD 20M, which is small next to a multi-billion-dollar campus
  (estimate). Data centres can also switch to dry or closed-loop cooling (memory).
- So data centres are a real buyer, but their volumes are small and they will pay for certainty of
  the permit, not for proven yield.

## 7. Who uses ML for groundwater well siting
- **No funded US startup found.** Two searches turned up nothing:
  - The nearest hits were mineral-exploration companies (Earth AI, Terra AI, GeologicAI) and a
    hydrogen explorer (Mantle8), none of them in water
    ([Mining Technology](https://www.mining-technology.com/news/earth-ai-20m-ai-driven-mineral-exploration-drilling/),
    [Newswire](https://www.newswire.ca/news-releases/terra-ai-raises-20m-to-accelerate-mineral-and-reservoir-exploration-to-meet-global-critical-mineral-and-energy-demands-866020821.html)).
  - Watertech Worldwide claims a "95% success rate", self-reported, using micro-seismic and
    radiometric methods rather than ML ([Watertech](https://watertechworldwide.com/applications/well-siting/)).
  - There is an open-source ML toolkit (WATex) and academic work, mostly in Africa and India
    ([WATex](https://watex.readthedocs.io/en/latest/history/five_min_understanding.html)).
  - A May 2026 review covers more than 200 ML groundwater-mapping studies
    ([Springer](https://link.springer.com/article/10.1007/s13201-026-02964-1)).
- **Public agencies already extract the driller logs.** USGS CVHM2 turned about 8,500 Central Valley
  logs into a public texture model and data release
  ([USGS](https://www.usgs.gov/publications/development-a-three-dimensional-model-sedimentary-texture-valley-fill-deposits-central),
  [data.gov](https://catalog-beta.data.gov/dataset/central-valley-hydrologic-model-version-2-cvhm2-well-log-lithology-database-and-texture-mo)).
  TWDB runs BRACS for Texas brackish aquifers (memory).
  - So the data is legible to agencies, unlike SMAD, where the Terranox edge comes from incumbents
    not extracting the data.
- **Adjacent software has stayed small.**
  - AQUAOSO began as a water-rights marketplace, raised USD 2M in 2021, and pivoted to water-risk
    analytics for lenders ([Food Industry Exec](https://foodindustryexecutive.com/2021/02/2m-seed-funding-round-empowers-aquaoso-to-further-its-water-risk-mitigation-tool-set-for-agricultural-lenders-and-landholders/)).
  - WestWater Research (broker, Waterlitix data) has advised on more than USD 800M of transactions
    in total ([SARE](https://www.sare.org/wp-content/uploads/L2ClayLandry.pdf)).
- **Why there is no ML startup (estimate):** at about USD 0.1-0.5M per test well, a better siting
  model saves perhaps one or two holes per project. That is consulting-sized value, and it does not
  touch the binding constraint, which is the permit.

## 8. Answers to the three questions
- **Is the pool big?**
  - **No.** Traded western water runs to a few hundred million dollars a year. California alone was
    USD 2.6B over 2012-2019 (CME, above).
  - The best exit in the category was USD 291M after about 25 years.
  - The high-value water (USD 20-85k/AF) is senior surface or proven municipal supply. It is not
    unclaimed groundwater waiting to be found.
- **Is discovery the 80% step inside some rung?**
  - **No.** At every rung the binding steps are:
    - the regulator's water budget and protests;
    - conveyance (pipelines, BLM rights-of-way, the ban on moving water between basins);
    - finding a buyer with an assured-supply need.
  - The hole usually confirms water that was expected, and it costs 1-10% of the right's value.
- **Does ML make it solvable?**
  - ML can improve well placement and yield prediction a little.
  - It cannot make the State Engineer award more acre-feet, open the Phoenix AMA, or let water move
    out of non-exempt Arizona basins. The pain point is legal, not informational.

## 9. The one surviving sliver: Texas brackish groundwater for industry and data centres
- **Why it differs:**
  - Brackish aquifers (for example, the Dockum in West Texas and New Mexico) are largely
    uncommitted.
  - Texas designates brackish production zones with a lighter permit route, and SB 2658 (2025)
    proposed exempting some wells from permits
    ([LBB fiscal note](https://capitol.texas.gov/tlodocs/89R/fiscalnotes/html/SB02658E.htm); I could
    not confirm it passed).
  - Water quality and yield vary a lot from place to place, so discovery matters more here
    ([UT Energy Institute](https://energy.utexas.edu/water-resources-ai-data-centers)).
- **Why it still scores low:**
  - The buyer must pay for desalination, so the water is worth less, roughly hundreds of USD per AF
    (estimate), not thousands.
  - The volumes data centres need are small.
  - UT's Bureau of Economic Geology and TWDB already map these aquifers.
- **Overall:** at best a niche water-supply developer for Permian, oil-and-gas or data-centre users.
  It fails R6 (ceiling). I would not pursue it unless a specific buyer has already been found.

## 10. Bottom line for the drill-hole hunt
- Kill groundwater rights as a "Terranox for water". In water, the regulator decides the value of
  a right; in uranium, the hole does.
- Lane G's second-place ranking was too generous. Hydrothermal geothermal stays the only adjacent
  industry with Terranox's shape, and Zanskar already owns it in the US.
- Remove groundwater from the shortlist. Note that Vidler is a 25-year natural experiment: it ran
  this exact model, hydrogeology included, and exited for about USD 0.3B.
