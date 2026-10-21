# Red team: "Texas Deep-Estate Bank" (TPL for the subsurface below 2 km), seen through Zanskar and the incumbents

*2026-10-21. Method: the workflow's shared WebSearch budget (200 calls per turn) was used up before this agent ran, so no new open-web searches were possible. Three primary pages were fetched directly: TPL's Q2-2026 earnings exhibit (SEC), TPL's homepage, and Standard Lithium's Franklin PEA release. Everything else rests on the primary-source evidence files in /home/user/nuketime/research/geothermal/evidence/, cited by file ID together with their URLs. A follow-up turn with fresh search budget should check four things: the Texas lithium-brine statute and royalty status (2025 session), whether Chevron, Exxon or Standard Lithium have taken surface geothermal top-leases, any Enverus geothermal product, and TPL's current surface acreage. These are marked (unverified).*

## Verdict

**Partly refuted in its stated form; rescued only as a narrower play.**

The pitch stacks four layers on Texas acreage: heat, lithium brine, storage/pore space, and powered land. Each of the three valuable layers already has an incumbent that owns the right or can take it trivially:

1. **Lithium brine**, the only layer with real step-up evidence, is the most contested ground in the state. Exxon, Chevron, Standard Lithium/Equinor and others have been leasing the Smackover since 2022. They lease it from the mineral owner, with full commercial well data, and the "cheap right" there is no longer cheap.
2. **Hot West Texas heat plus powered land.** Under SB 785 the heat belongs to the surface owner, and the biggest surface owner in the hottest Texas fairway (the Delaware Basin) is **TPL itself** (~880k surface acres). TPL is already running data-centre and power deals with Chevron on that land. "TPL for the subsurface" is TPL. University Lands (~2.1M acres) is the next-largest block.
3. **Data.** Enverus now owns the A2D library: >8M raster logs, >5M proprietary logs, "basin temperature models", and 350M+ courthouse ownership records. Meanwhile the LLM extraction step costs about $1.4-6k per 10M headers (D07). The data edge is therefore real but cheap to copy, and the incumbent with the most complete copy is a vendor that will sell it to anyone.

**Zanskar is not the threat.** It has no Texas, sedimentary, private-fee or minerals position (Z04, Z06). The threat comes from TPL, the lithium majors and Enverus.

**Revised total: 16/25** (from 21). The narrower rescue described below is worth pursuing as an option within a multi-basin sedimentary land bank, not as the flagship.

## Rung-by-rung attack

### 1. Zanskar: doing it, or able to copy it?

- **Doing it: no.**
  - Zanskar's auction-won land is about 50k acres of BLM leases, all in northern and western Nevada, bought for under $1M (Z04, BLM all-bids PDFs).
  - It also owns the Lightning Dock plant in NM.
  - None of its news items from Sep 2025 to Sep 2026 mention lithium, brine or DLE, despite the entity name "Zanskar Geothermal & Minerals Inc." (Z06; https://www.zanskar.com/news).
  - It has no sedimentary, oil-patch, state or private-fee position (Z06).
- **Could it copy: technically yes, strategically unlikely.** Zanskar's stack is tuned to blind convective systems in the Great Basin, and its capital is committed to building and operating plants (a 100 MW NV Energy PPA, $115M Series C; https://www.zanskar.com/about).
- **Conclusion: Zanskar does not kill this rung.** The "Zanskar gap" claim holds. It is also the least important claim in the pitch, because Zanskar is not the competitor in Texas.

### 2. Lithium layer: the step-up is real, but it already belongs to the incumbents

The pitch's 100-1000x step-up compares a ~$3-10/acre *geothermal* lease price against *lithium* exit values. That mixes two different estates. SB 785 §141.004(c) excludes "minerals dissolved or otherwise contained in groundwater, including in hot brines" from the surface owner's geothermal estate (https://tcss.legis.texas.gov/resources/NR/htm/NR.141.htm). Lithium therefore has to be leased from the **mineral** owner, a separate counterparty in a separate market. That market has been competitive since 2022.

**Who already holds East Texas and Arkansas Smackover acreage:**

| Player | Position | Source |
|---|---|---|
| Standard Lithium (with Equinor), East Texas Franklin project | 617 brine leases on 46,287 gross acres at the maiden resource (Sep 2025). Grew to **110,064 acres (+37%)** by the 20 Oct 2026 PEA. Pre-tax NPV8 $5.9B | https://www.standardlithium.com/news/press-releases/standard-lithium-files-positive-preliminary-economic-assessment-for-the-high-grade-70000-tonnes-per-year-franklin-project-in-east-texas |
| Equinor | Paid $30M cash plus a $60M work programme for 45% of SWA and ETX (May 2024) | https://www.standardlithium.com/news/press-releases/standard-lithium-and-equinor-form-partnership-to-develop-south-west-arkansas-and-east-texas-lithium-projects |
| ExxonMobil | About 120k gross acres in SW Arkansas from Galvanic, reportedly >$100M (about $800+/acre) | A02 (unverified) |
| Chevron | About 125k net acres in NE Texas and SW Arkansas, 2025 | A02 (unverified) |

**What this means for the play:**

- **The information gap is already closed.** The pitch says the miss between USGS's random-forest model (max 399 mg/L) and operator measurements (549-806 mg/L) is the gap a finer model fills (A02). But the operators who measured 806 mg/L are the ones holding the leases. The gap has already been arbitraged, by Standard Lithium, which ran almost exactly this play (lease from 2022, prove grade, farm out to Equinor about 2 years later).
- **The right is no longer cheap.** Brine bonuses in TX/AR are said to run from the low hundreds to $1,000+/acre (A02, unverified), not $3-10.
- **Royalty-holder economics are capped.** Arkansas set the Reynolds Unit royalty at **2.5% gross plus $65.05/acre/yr**, about 3% in total (https://www.standardlithium.com/news/press-releases/smackover-lithiums-south-west-arkansas-project-receives-royalty-rate-approval-from-the-arkansas-oil-and-gas-commission). If Texas follows a similar unitisation model (status unverified), a brine royalty strip is thin. Owning the step-up means holding working interest, which makes the company a lithium developer competing with Exxon and Chevron at about $3.5B capex per Franklin-scale project (A02, derived).
- **Copy risk is maximal.** Every lithium incumbent licenses IHS/Enverus data and runs its own land team.

**This rung kills the lithium layer as a source of cheap rights.**

### 3. Heat and powered land: TPL is the incumbent the play is named after

The fetched TPL Q2-2026 earnings exhibit (https://www.sec.gov/Archives/edgar/data/1811074/000181107426000056/exhibit991q22026earningsre.htm) shows:

- TPL agreed "to provide land and brackish water resources for Chevron's recently announced development known as **Project Kilby**". That is Chevron's "large-scale power generation facility ... to support a customer data center in **Reeves County, Texas**".
- TPL is expanding "our data center and power generation efforts to areas beyond the immediate Permian Basin".
- It spent **$110.2M on land acquisitions** in Shackelford and Jones Counties in the quarter, plus Winkler County.
- It commissioned a 10,000 bbl/d produced-water desalination test facility in Orla, TX.
- B07 (same exhibit, plus StockAnalysis): **~880k surface acres**, a **$23.75B market cap**, and **41% of revenue from non-royalty sources**.

**Why that matters:**

- **TPL already owns the heat right on its best ground.** Reeves, Pecos and Winkler are the deep Delaware: BHTs of 120-180 °C, and a modelled ~195 °C at 3.5 km in Pecos (L10; https://repositories.lib.utexas.edu/items/01be6734-86ac-4892-a3f2-1c5e362b3409). Under SB 785, TPL as surface owner holds the geothermal estate on about 880k acres there by default, with no lease needed.
- **TPL already has the powered-land relationship.** It has a hyperscale-adjacent customer (Chevron's data-centre power plant) and an acquisition budget.
- **Copying is trivial.** Adding "geothermal estate" to its surface-monetisation menu costs TPL a data licence and a press release. Geothermal is not mentioned in the exhibit, so TPL has not done this yet.
- **The other big blocks are institutional too.** University Lands manages ~2.1M acres in 19 West Texas counties and is "actively seeking to lease PUF lands for renewable energy" (https://universitylands.utsystem.edu/). The GLO leases by sealed bid (R07).
- **Where the cheap, fragmented rancher estate sits.** It is mostly East Texas and the Gulf Coast, where the heat is lower grade: a gradient of about 31-33 °C/km, and Pleasant Bayou at 153 °C at 4.47 km (https://www.beg.utexas.edu/files/publications/contract-reports/CR1990-Kreitler-1.pdf).

**The cheap-right rung inverts.** The hot, consolidated ground is not cheap or available. The cheap ground is fragmented and cooler.

### 4. Heat buyers: none have shown up in Texas

- **Fervo** holds ~595,900 acres in CA, CO, ID, NV, NM, UT and WA, **none in Texas**. It bought them at ~$4/acre and has 256k idle "Prospects" acres (Fervo 424B4, https://www.sec.gov/Archives/edgar/data/1853868/000162828026034849/fervoenergy-424b4.htm; Z08). It is land-long, not land-short, outside its core.
- **Ormat** holds ~434k acres in CA, HI, NV, NM, UT, ID and OR (10-K; Z08), no Texas.
- **SLB-Ormat** chose Desert Peak, NV for its EGS pilot (https://www.slb.com/newsroom/updates/2026/2026-0609-slb-ormat-update).
- **Sage**, the Texas-native champion with a Meta deal for up to 150 MW, took its next commercial EGS project to **Ormat's Blue Mountain, Nevada** on 22 Sep 2026 (https://www.sagegeosystems.com/). Its Texas activity is storage (3 MW at San Miguel) and demos (R07).
- **Devon** has funded Fervo since 2023 and holds Delaware logs, but has no disclosed geothermal-rights activity (A01).

**Reading:** the Texas heat layer has plausible buyers but no observed demand at any price. The pitch's step-up comparables for heat come from elsewhere:

- BLM Utah/Nevada land at $344-1,207/acre.
- The Stream/Plug powered-land deal in Graham, TX at ~$0.47M/MW (B06; https://thetexaslandagent.com/texas-data-center-land-young-county). That premium was paid for the **grid interconnection**, not for heat.

**The heat layer's step-up is unpriced, as the pitch itself admits.**

### 5. Data edge: real, but cheap to copy and consolidated at Enverus

- **What Enverus bought.** It closed the A2D purchase from TGS on 8 Jul 2026 for $100M plus a $15M earn-out (https://www.tgs.com/press-releases/tgs-sells-north-american-well-data-products-business-to-enverus). The library holds:
  - >8M depth-calibrated raster logs and >1.9M LAS files;
  - >5M proprietary logs "not available from any public or regulatory source";
  - >2M tops and interpretations, plus "basin temperature models".
  - Source: https://www.prnewswire.com/news-releases/enverus-acquires-a2d-well-log-library-from-tgs-connecting-subsurface-data-to-energy-decision-workflows-302820900.html
- **Enverus also holds the title layer:** 350M+ courthouse records (D08).
- **Enverus lacks** only a geothermal package and land positions.
- **The pitch's own numbers make the edge cheap.** At about $1.4-6k to LLM-read 10M headers and about $1M for a 100k deep-well BEG subset (D07), extraction is a weekend's work for Enverus, TPL's technical team, Chevron or Standard Lithium.
- **Free screening exists at the regional scale.** Project InnerSpace's free GeoMap already offers isotherm-depth layers (https://www.thinkgeoenergy.com/project-innerspace-launches-geomap-geothermal-prospecting-tool-for-north-america/).
- **Temperature is not the binding variable.** Permeability is: heat-in-place overstates deliverable power by about 7x at Virginia Hills (L10). The LLM header play extracts mostly temperature.

**The data rung survives only as a speed edge, not a moat.**

### 6. Title and estate structure

- **The mineral estate stays dominant** (§141.004(c)(2)(B)). In the active Permian, oil-and-gas lessees, including Chevron and Exxon, keep reasonable surface use over any geothermal lessee.
- **Pre-2023 deeds** reserving "all minerals and other substances" invite disputes (R07).
- **Thousands of counterparties** per fairway in East Texas.
- **Two counterparties for the multi-commodity stack:** a surface owner for heat and a mineral owner for brine. Bundling them works only where the estates are unsevered, which is rare in East Texas oil country (unverified share).

## Best AI-leveraged answers to the killers, and whether they rescue the play

**A. "Surface-heat blocking estate over the brine units"** (best answer; partial rescue).

- **The wedge:** lithium majors lease the *mineral* brine estate, but under SB 785 the **heat** in hot brines ("hot water and hot brines ... and associated heat", §141.003) sits with the *surface* owner wherever the estates are severed.
- **The tension:** DLE operators producing about 100 °C+ brine (Franklin) want that heat for process energy and power. They also need surface sites and reinjection. The carve-out says dissolved minerals and groundwater law are unaffected, so who owns the heat in produced brine is legally ambiguous (unverified; needs Texas counsel).
- **The AI angle:** join Enverus/courthouse ownership with LLM-read BHTs to map every severed-estate surface parcel over Standard/Chevron/Exxon brine units, then option the surface geothermal estate at $3-10/acre.
- **The exit:** sell or license to the unit operator as a heat right, reinjection or pore-space easement, or site lease. The buyer is a known, funded major that has already committed billions.
- **Why it only partly rescues:**
  - The value is a hold-up or easement value (tens to hundreds of $/acre, or a heat royalty), not a resource step-up.
  - It depends on an untested legal reading.
  - It probably caps out at hundreds of millions, not TPL scale.
  - Cheap to test, though.

**B. "Be the geothermal arm for TPL and University Lands"** (no rescue). An ML map of the heat on 880k TPL acres sold for a share of revenue is a service or tool shape, which scores low under the standing rules. TPL captures the asset value.

**C. "Fragmented mid-Texas EGS fairways TPL doesn't own"** (weak rescue). SMU found 150 °C at 2.6-5.1 km in Webb County and 2.7-8.0 km in Crockett, "hotter than previously calculated" (https://gdr.openei.org/submissions/1291). The ML edge is real here: 532 to 5,410 sites from just 3 counties. Two problems remain:

- No Texas heat buyer has bought anything yet.
- Fervo and Sage are long on cheap western land.

This works as a low-cost option bank (5-10k acres at <$10/acre) that pays out only if EGS costs fall and ERCOT large-load buyers want behind-the-meter supply. Under the "assume the tech works" rule this is plausible, but the step-up is unpriced, and TPL can enter the same counties (as its Shackelford and Jones purchases show).

**D. "Multi-basin sedimentary rights bank"** (structural rescue, already proposed in R07/L10). Texas becomes one jurisdiction alongside Saskatchewan/Williston (Terranox-native tenure and data) and Alberta (FIFO at C$3.50/ha). That removes the single-state dependence on TPL's footprint.

**Net:** the TPL-of-the-subsurface framing does not survive, because TPL is the TPL of the subsurface. What survives is (A) as a cheap legal and data test, plus (C)/(D) as optionality.

## Revised scoring

| Criterion | Was | Now | Why |
|---|---|---|---|
| c1 proving step | 3 | 3 | Lithium proof is fast, but it is someone else's. Heat proof needs EGS flow tests |
| c2 illegible data | 5 | 3 | TIFF-only is real, but Enverus/A2D already holds digitised and proprietary logs, temperature models and title. LLM extraction is cheap for any incumbent |
| c3 cheap right | 4 | 3 | The surface heat estate is cheap only where it is fragmented and cooler. Hot Delaware ground is held by TPL and University Lands. Lithium rights are no longer cheap |
| c4 step-up buyer | 4 | 3 | Lithium buyers are real but buy from mineral owners or lease themselves. No heat buyer has transacted in Texas. Sage, Fervo and SLB-Ormat all went to Nevada |
| c5 size ladder | 5 | 4 | A TPL-scale outcome requires owning TPL's geography. The fragmented remainder plus a heat hold-up value is $100Ms to low $Bs |
| **Total** | **21** | **16** | |

## Cheapest kill test (instead of the pitch's $300k test)

Before buying scans, spend about $20-40k over 3 weeks on two checks:

1. A Texas oil-and-gas/water title opinion on who owns the **heat** in brine produced by a DLE unit on severed land under §141.003/.004.
2. A courthouse pull, through Enverus, of 2023-26 recorded instruments that mention "geothermal" in Reeves, Pecos, Lamar, Franklin and Webb counties.

Interpreting the results:

- If TPL, Chevron, Exxon or Standard Lithium are already taking surface geothermal leases or top-leases, the play is dead.
- If not, and counsel says the heat sits with the surface owner, rescue (A) is live.

## Sources

- TPL Q2-2026 earnings exhibit (Project Kilby, Reeves County data-centre power, $110.2M land buys): https://www.sec.gov/Archives/edgar/data/1811074/000181107426000056/exhibit991q22026earningsre.htm
- TPL homepage ("Pure Play in the Permian Basin", one of the largest Texas landowners): https://www.texaspacific.com/
- Texas Natural Resources Code ch. 141 (SB 785): https://tcss.legis.texas.gov/resources/NR/htm/NR.141.htm
- SB 785 enrolled: https://capitol.texas.gov/tlodocs/88R/billtext/html/SB00785F.htm
- Standard Lithium Franklin PEA (110,064 acres): https://www.standardlithium.com/news/press-releases/standard-lithium-files-positive-preliminary-economic-assessment-for-the-high-grade-70000-tonnes-per-year-franklin-project-in-east-texas
- Franklin maiden resource (617 leases, 46,287 acres, 806 mg/L peak): https://www.standardlithium.com/news/press-releases/smackover-lithium-releases-maiden-inferred-resource-for-its-franklin-project-comprising-a-portion-of-significant-brine-position-in-east-texas
- Equinor farm-in: https://www.standardlithium.com/news/press-releases/standard-lithium-and-equinor-form-partnership-to-develop-south-west-arkansas-and-east-texas-lithium-projects
- Arkansas 2.5% brine royalty: https://www.standardlithium.com/news/press-releases/smackover-lithiums-south-west-arkansas-project-receives-royalty-rate-approval-from-the-arkansas-oil-and-gas-commission
- TGS sale of A2D to Enverus: https://www.tgs.com/press-releases/tgs-sells-north-american-well-data-products-business-to-enverus
- Enverus A2D release: https://www.prnewswire.com/news-releases/enverus-acquires-a2d-well-log-library-from-tgs-connecting-subsurface-data-to-energy-decision-workflows-302820900.html
- Fervo 424B4 (acreage by state, ~$4/acre): https://www.sec.gov/Archives/edgar/data/1853868/000162828026034849/fervoenergy-424b4.htm
- Sage Geosystems (Blue Mountain NV selection): https://www.sagegeosystems.com/
- SLB-Ormat Desert Peak: https://www.slb.com/newsroom/updates/2026/2026-0609-slb-ormat-update
- University Lands: https://universitylands.utsystem.edu/
- SMU three-county Texas study: https://gdr.openei.org/submissions/1291
- BEG/DOE Pleasant Bayou report: https://www.beg.utexas.edu/files/publications/contract-reports/CR1990-Kreitler-1.pdf
- Pecos County temperature model: https://repositories.lib.utexas.edu/items/01be6734-86ac-4892-a3f2-1c5e362b3409
- Texas powered-land deal (Graham, TX): https://thetexaslandagent.com/texas-data-center-land-young-county
- Project InnerSpace GeoMap: https://www.thinkgeoenergy.com/project-innerspace-launches-geomap-geothermal-prospecting-tool-for-north-america/
- Zanskar: https://www.zanskar.com/about ; https://www.zanskar.com/news
- Sibling evidence files: A01, A02, B06, B07, D01, D07, D08, L10, R07, Z04, Z06, Z07, Z08 in /home/user/nuketime/research/geothermal/evidence/
