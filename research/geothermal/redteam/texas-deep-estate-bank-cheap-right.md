# Red team: "Texas Deep-Estate Bank (TPL for the subsurface below 2 km)", seen through cheap rights and repricing

*2026-10-21. Method: the workflow's shared WebSearch budget (200 calls per turn) was already spent when this agent started. Every search returned "budget used up", so no new open-web searches ran. Fresh evidence comes from direct WebFetch of primary pages: the TPL Q2-2026 SEC exhibit, the Standard Lithium Franklin PEA release and the ThinkGeoEnergy T5/Glencore article. Everything else rests on the sibling evidence files in /home/user/nuketime/research/geothermal/evidence/, cited by file ID with their URLs. Chevron, Exxon and DOE/TerraVolta pages returned 403/404. Anything not fetched is marked (unverified).*

## Verdict

**Refuted as specified. A narrower version survives at a lower score.** The question here is whether the right stays cheap once you move on it, or once ML spreads. The answer differs by layer, and it runs against the play's own step-up maths:

| Layer | Is it cheap today? | Does it stay cheap after you nominate or ML spreads? | Is there a buyer who pays a step-up now? |
|---|---|---|---|
| Brine lithium (East Texas Smackover) | **No.** It already repriced over 2022-26 | Already repriced | Yes (Exxon, Chevron, Equinor, Glencore via T5) |
| Surface geothermal estate (SB 785) | Yes | Mostly yes: no auction, no public nomination | **Weak.** No buyer has paid for Texas sedimentary heat yet |
| Powered land / data-centre surface (Delaware Basin) | **No.** TPL and University Lands hold it and already sell it | n/a | Yes, but it goes to **TPL**, the incumbent |

The play's headline step-up of "roughly 100-1000x on the lithium layer" has the wrong denominator. It compares a $3-10/acre *geothermal* rent with a *lithium* exit price. The lithium right is a separate estate (SB 785 § 141.004(c)) and was never priced at $3-10. The layer that is still cheap, surface heat, is cheap mainly because nobody pays for it yet. And the most valuable "TPL-like" layer, powered land in Reeves County, already belongs to TPL.

**Revised total: 17/25**, down from 21. Changes: c3 cheap_right 4 → 2, c4 step_up_buyer 4 → 3, c1 3, c2 5, c5 4.

## Rung 1: The lithium layer is not cheap. It has already been repriced.

**Fresh and sibling evidence that the East Texas Smackover is in a land rush, not a quiet window:**

- **Standard Lithium / Equinor Franklin (East Texas).**
  - Leasing began in 2022. The book had grown to 617 private leases on 46,287 gross acres by Sept 2025 (A02).
  - By the 20 Oct 2026 PEA, the project area had grown **37% to 110,064 acres**. Pre-tax NPV8 is $5.9B (fetched: https://www.standardlithium.com/news/press-releases/standard-lithium-files-positive-preliminary-economic-assessment-for-the-high-grade-70000-tonnes-per-year-franklin-project-in-east-texas).
  - A well-funded major-backed lessee is therefore still adding acreage across the exact cell the play names. The release gives no lease or bonus terms.
- **T5 Smackover Partners.**
  - Holds Franklin, Titus and Hopkins counties, with "about 800 ppm" Li zones.
  - Signed a binding **Glencore** offtake for 100% of Phase 1 (about 5,000 t/yr for 5 years). Planned scale is 35-50 ktpa LCE (fetched, 3 Jun 2026: https://www.thinkgeoenergy.com/t5-smackover-partners-signs-offtake-agreement-for-geothermal-lithium-in-texas/).
  - T5 already runs the play's own "heat plus brine on the same ground" concept. It permitted its first well as a *geothermal* well on reclaimed Luminant mine land (L12).
- **Other buyers.**
  - Exxon: about 120k gross acres from Galvanic for more than $100M, about $800+/acre (unverified, A02).
  - Chevron: about 125k net acres in NE Texas and SW Arkansas in 2025 (unverified; chevron.com returned 403).
  - Typical 2023-25 brine-lease bonuses are "low hundreds to about $1,000+/acre" (unverified, A02). L12 already flags that "the cheap-entry window is closing in AR and East TX".
- **The public model already exists.**
  - USGS ran a random forest over the Produced Waters DB (Knierim et al. 2024, *Sci. Adv.* 10:eadp8149; https://pubs.usgs.gov/publication/fs20243052/full).
  - BEG published Texas-wide controls on oilfield-water Li (Darvari et al. 2024, *J. Geochem. Explor.* 257:107363; https://www.osti.gov/biblio/2576668).
  - The coarse-model gap (USGS maximum 399 mg/L against measured 549-806 mg/L) is real. But it has already been closed *in the field* by operators who drilled and sampled. A finer ML model now reproduces what Standard, T5 and Exxon already know from their own wells.

**Repricing arithmetic, corrected:**
- Say an entrant leases brine rights now at about $300-1,000/acre (unverified), then exits at an Equinor-style farm-in of about $2-4k/acre (A02, derived). That is **about 2-10x, not 100-1000x**, and A02's own verdict is "roughly 3-10x".
- The exit needs a grade sample. A02 says "one brine sample (at $ thousands)", but that needs access to an existing wellbore, which an operator usually controls.
- The exit also depends on the lithium price cycle: spot fell from about $70-80k/t to about $10k/t (unverified, A02).
- On top of that, the **mineral estate** owns brine. Mineral owners in East Texas are the oil-patch counterparties that landmen and Enverus's 350M+ courthouse records already map (D08). These are the most legible rights in America, the opposite of "illegible".

**Royalty-capture risk.** Arkansas let the state set landowner compensation at about 2.5-3% (AOGC, 29 May 2025: https://www.standardlithium.com/news/press-releases/smackover-lithiums-south-west-arkansas-project-receives-royalty-rate-approval-from-the-arkansas-oil-and-gas-commission). If Texas adopts a similar unitisation and royalty regime, a holder of a royalty or override is capped there. Whether Texas has its own lithium brine statute is unverified; no search budget was left to check 89th Legislature bills. Only a working interest keeps the step-up, and that means capex and a developer posture. The play wants TPL-style passive overrides, which this undercuts.

**Rung 1 kills the lithium layer as a source of cheap rights.**

## Rung 2: The hottest Texas cell is already held by TPL itself.

The play names the Delaware/Val Verde as a first-test cell. Its deep BHTs run 120-180 °C, and a Pecos County model gives about 195 °C at 3.5 km (R07). But:

- **TPL owns about 880k surface acres in West Texas**, "concentrated in the Permian Basin" (B07; https://www.sec.gov/Archives/edgar/data/1811074/000181107426000056/exhibit991q22026earningsre.htm).
- **Under SB 785, the surface owner owns the geothermal estate** (§ 141.004; https://tcss.legis.texas.gov/resources/NR/htm/NR.141.htm). TPL therefore already *owns the heat under its 880k acres by statute*, without paying for it.
- **In Q2-2026 TPL** (fetched):
  - signed to supply "land and brackish water resources" for **Chevron's Project Kilby**, "a multi-gigawatt power generation and data center hub located in Reeves County";
  - spent **$110.2M on land in Shackelford and Jones counties** "in connection with our data center and power generation initiatives";
  - bought land in Winkler County;
  - booked $23.7M/quarter of easements and surface income;
  - advertises "access to subsurface pore space".
- **University Lands** manages about 2.1M acres in 19 West Texas counties and is "actively seeking to lease PUF lands for renewable energy" (R07; https://universitylands.utsystem.edu/). The GLO leases by **sealed bid** (§ 141.073/.076). That is an auction with price discovery, not a stealth lease.

So in the Permian, **"TPL for the subsurface" is TPL.** The counterparty holding the powered-land and data-centre layer is a $23.75B company at 31.8x EBITDA that is already selling that layer to Chevron. It also legally owns the heat layer underneath. That counterparty will not hand an entrant a 10-year option at $3/acre. The heat right is cheap only where surface is fragmented among unsophisticated owners: East Texas, South Texas and Gulf Coast farm tracts. Heat there is lower: about 31-33 °C/km on the Gulf Coast, and Pleasant Bayou reached 153 °C at 4.47 km (R07, BEG CR1990).

## Rung 3: Surface heat stays cheap, but partly because nobody is buying it.

**Why the heat right does stay cheap after you move on it:**
- No BLM-style nomination, no public all-bids report, no auction. Compare the Pumpernickel step-out, which repriced from $2 to $232/acre within weeks of Zanskar's disclosure (R03; BLM NV-2025-10-2143).
- Private leases are recorded in county records, often as memoranda without prices (R07, unverified). Price signals leak slowly.
- ML spreading does not reprice it quickly. Project InnerSpace's free GeoMap and Enverus's A2D "basin temperature models" (bought 8 Jul 2026, more than 8M raster logs; https://www.prnewswire.com/news-releases/enverus-acquires-a2d-well-log-library-from-tgs-connecting-subsurface-data-to-energy-decision-workflows-302820900.html) commoditise *regional* temperature. Because they sell to many, they raise everyone's prior. The likely response is a broad, mild markup, not a parcel-level bidding war.

**But nothing shows a step-up buyer for Texas sedimentary heat:**
- Sage, the Texas-native champion ($97M Series B, Ormat-led, Meta up to 150 MW), picked **Ormat's Blue Mountain, Nevada** for its next commercial EGS site on 22 Sep 2026 (R07; https://www.sagegeosystems.com/). In Texas it does storage and demos.
- Fervo's step-ups ($4 → $344-410/acre) are Utah/Nevada BLM ground (R04).
- Alberta's Virginia Hills delivers about 7x less than heat-in-place suggests (L10). Sedimentary permeability is the binding constraint, and better ML on log headers does not fix it.

So the heat layer passes the "stays cheap" test and fails the "someone pays the step-up" test today. Under the standing "assume the tech works" rule this does not kill the layer. But it moves the step-up 5-10+ years out and makes it depend on EGS cost curves, not on the company's data edge.

**Aggregation also reprices the right: the holdout problem.**
- An EGS block needs about 5-20 km² (R07), which means dozens of surface owners.
- Texas has no practical compulsory pooling for this estate (the Mineral Interest Pooling Act is narrow and oil/gas-specific; its application to geothermal is unverified).
- The last 10-20% of tracts in a block can therefore hold out. Once the first memoranda are recorded and neighbours talk (ranch communities are small), the marginal acre reprices even with no auction.
- The mineral estate also stays dominant (§ 141.004(c)). Any oil and gas lessee can drill through the block.

## Rung 4: ML spread and incumbents

- **Enverus** now holds A2D's temperature models, more than 1.9M LAS files and 350M+ courthouse records (D08). It is the one party that can join temperature to Texas ownership at scale. It does not take land, but it sells to everyone who does: Exxon, Chevron, TPL and Standard's landmen are all likely customers (unverified).
- **The data edge (c2 = 5) is real but has a short half-life.** Reading 10M headers costs $1.4-6k (D07), so any competitor can copy it within months. The moat has to be the lease book, and on the lithium layer the lease book is already held by others.

## Best AI-leveraged answer to the killer, and whether it rescues the play

**The answer: drop lithium-first and Permian powered land. Become an AI title-and-option machine for fragmented surface-heat estates near ERCOT load, outside TPL and University Lands ground.**

1. **LLM title abstraction over county deed images.**
   - Classify every tract by whether pre-2023 deeds expressly reserved "all minerals and other substances". That clause clouds SB 785 title.
   - Find clean-title, fragmented surface tracts in the hottest non-Permian cells: South Texas Starr/Hidalgo near Sage's JFB Heard well, the East Texas Smackover margins, and the DFW-adjacent Fort Worth Basin.
   - This is the illegible layer Enverus does not package: *who can grant SB 785 heat* is a new question. Note that D08 says Enverus has courthouse records but no geothermal-title product (unverified as of Oct 2026).
2. **Automated outreach and e-sign options:** 10-year options at $1-5/acre plus a 3-5% gross override, with a right of first refusal on the brine lease where the surface owner also holds minerals (common in fee-simple East Texas farms; unverified share).
3. **Exploit the Arkansas-style cap by holding the working interest.** Farm out at FID to Fervo, Sage or XGS-type developers, or to ERCOT large-load campuses. The ERCOT queue is 438 GW, and Rhodium sizes DFW at 2.9 GW of geothermal-servable demand (B06). Keep a carried interest, not only an override.
4. **Partner with TPL instead of competing.** Offer TPL the corrected-temperature model over its 880k acres for a share of the heat-layer upside. This is a service-shaped fallback and scores low on our rules.

**Does it rescue the play?** *Partly.* Points 1-2 give a right that truly stays cheap (no auction, a new estate, an AI moat on title) and a $5-10B size ladder in principle. Under the standing "assume the tech works" rule, the size ladder survives. But:
- the fast, priced step-up (lithium) is gone;
- the TPL-style multi-layer bundle is held by TPL;
- what remains is a long-dated EGS option book whose step-up is unpriced and whose closest buyer just went to Nevada.

That is a credible 17, not a 21. It is better framed as the **Texas leg of a multi-basin sedimentary heat bank** (R07's own recommendation) than as a standalone Texas multi-commodity TPL.

## Sources

- https://www.sec.gov/Archives/edgar/data/1811074/000181107426000056/exhibit991q22026earningsre.htm (TPL Q2-2026: Project Kilby, $110.2M land buys, surface income)
- https://www.standardlithium.com/news/press-releases/standard-lithium-files-positive-preliminary-economic-assessment-for-the-high-grade-70000-tonnes-per-year-franklin-project-in-east-texas
- https://www.standardlithium.com/news/press-releases/smackover-lithium-releases-maiden-inferred-resource-for-its-franklin-project-comprising-a-portion-of-significant-brine-position-in-east-texas
- https://www.standardlithium.com/news/press-releases/standard-lithium-and-equinor-form-partnership-to-develop-south-west-arkansas-and-east-texas-lithium-projects
- https://www.standardlithium.com/news/press-releases/smackover-lithiums-south-west-arkansas-project-receives-royalty-rate-approval-from-the-arkansas-oil-and-gas-commission
- https://www.thinkgeoenergy.com/t5-smackover-partners-signs-offtake-agreement-for-geothermal-lithium-in-texas/
- https://tcss.legis.texas.gov/resources/NR/htm/NR.141.htm (SB 785 / NRC ch. 141)
- https://capitol.texas.gov/tlodocs/88R/billtext/html/SB00785F.htm
- https://universitylands.utsystem.edu/
- https://www.thinkgeoenergy.com/texas-oil-gas-and-geothermal-lease-sale-nov-2-2022/
- https://www.sagegeosystems.com/
- https://www.prnewswire.com/news-releases/enverus-acquires-a2d-well-log-library-from-tgs-connecting-subsurface-data-to-energy-decision-workflows-302820900.html
- https://pubs.usgs.gov/publication/fs20243052/full
- https://www.osti.gov/biblio/2576668 (Darvari et al. 2024, Texas oilfield-water Li)
- https://www.beg.utexas.edu/files/publications/contract-reports/CR1990-Kreitler-1.pdf
- Sibling evidence: A02, B07, D07, D08, L10, L12, R03, R04, R07 in /home/user/nuketime/research/geothermal/evidence/
