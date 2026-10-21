# B06: Hyperscaler demand for firm clean power, geothermal near data centres, and powered land

*Research note, 2026-10-21. Method: this workflow turn had already used up its shared WebSearch budget (200 calls) when this agent started, so no new web searches ran. Facts come from three places: direct WebFetch or download of primary documents (the Rhodium Group report PDF, parsed locally; Meta's newsroom; Latitude Media; a Texas land-deal article); sibling evidence files in this repo that cite SEC filings and primary releases (B02, B03, L23, R07, R10, Z05); and the repo's earlier data-centre power research (`research/02-data-center-power.md`, `research/owner/lane_energy.md`). Where a fact is cited through a sibling file, the file is named. Anything not sourced is marked (unverified).*

## 1. Bottom line

- **The demand is real, contracted and premium-priced.** Hyperscalers have committed about **0.7 GW** of geothermal through named deals, plus a non-binding **3 GW** Google framework.
  - Google: 115 MW from Fervo and up to 150 MW from Ormat, both through NV Energy's Clean Transition Tariff (CTT).
  - Meta: up to 150 MW from Sage and up to 150 MW from XGS.
  - Google also has equity in Fervo.
- **Demand is outrunning confirmed resource.** Ormat has to find up to 150 MW of *new* Nevada geothermal for Google by 2028-30. Under its framework, Fervo has to propose 1 GW to Google within two years. Neither number comes from resource already in hand.
- **Rhodium's modelling puts the addressable volume at 15-17 GW of behind-the-meter (BTM) geothermal for hyperscale data centres by the early 2030s,** at a national LCOE of $78-85/MWh.
  - That assumes data centres keep clustering where they do today.
  - If campuses site to the resource, geothermal can meet *all* projected growth, at costs 31-45% lower.
- **The step-up asset is "resource + land + water + interconnection or BTM path".** Powered land in Texas has sold for about **$470k per MW over raw land** (Plug Power to Stream, Graham, TX). Secondary-market powered land runs at roughly $0.3-1.5M/MW over raw land.
  - A geothermal-backed powered site therefore stacks two step-ups: the resource step-up and the powered-land step-up.
- **Zanskar has no disclosed hyperscaler offtake** and no powered-land or campus product (Z05). It sells to utilities and community choice aggregators (CCAs), such as NV Energy (100 MW build-transfer). That leaves a clear gap.

## 2. Who is buying, and on what terms

| Buyer | Seller / structure | MW | Status | Price | Source |
|---|---|---|---|---|---|
| Google | Fervo Blue Mountain pilot (NV) | 3.5 | operating, 2023 | n/d | https://blog.google/outreach-initiatives/sustainability/google-fervo-geothermal-energy-partnership/ |
| Google via NV Energy CTT | Fervo "Corsac Station" (NV) | 115 | CTT approved by PUCN in the week of 15 May 2025; COD 2-5 yrs | not disclosed | https://www.latitudemedia.com/news/the-clean-transition-tariff-won-approval-in-nevada-whats-next-for-fervo/ |
| Google via NV Energy CTT | Ormat portfolio of *new* geothermal | up to 150 | PPA signed 17 Feb 2026; deliveries 2028-30 | not disclosed | Ormat 8-K Ex. 99.1: https://www.sec.gov/Archives/edgar/data/1296445/000143774926004369/ex_921781.htm |
| Google | Fervo Geothermal Framework Agreement | 3,000 | 19 Mar 2026; "does not obligate Google to purchase power"; ROFR, exclusivity, audit rights over costs and pricing | cost-visibility | Fervo 424B4 (via B02/B03) |
| Google | Fervo equity | n/a | Series E, $462M, Dec 2025 | n/a | https://www.thinkgeoenergy.com/google-joins-usd-462m-funding-round-for-fervo-energy/ |
| Meta | Sage Geosystems (geopressured) | up to 150 | first phase targeted 2027; "east of the Rockies" | not disclosed | https://about.fb.com/news/2024/08/new-geothermal-energy-project-to-support-our-data-centers/ |
| Meta | XGS Energy (New Mexico) | up to 150 | announced Jun 2025 | not disclosed | https://www.businesswire.com/news/home/20250612778008/en/XGS-Energy-and-Meta-to-Partner-on-150-MW-Advanced-Geothermal-Project (fetch blocked; cited via NLR in L23) |
| Switch | Ormat Salt Wells (Fallon, NV) | ~13 | 20-yr PPA, Jan 2026 | n/d | Ormat filings (via B03) |
| Microsoft | G42 Olkaria, Kenya, geothermal-powered campus | n/d | announced May 2024; no US geothermal PPA found | n/a | https://news.microsoft.com/2024/05/22/microsoft-and-g42-announce-1-billion-comprehensive-digital-ecosystem-initiative-for-kenya/ |

**How the CTT works.**
- NV Energy's Clean Transition Tariff lets a customer with 5 MW or more of load fund a dedicated new clean resource at its own premium. The cost stays off other ratepayers.
- In the Fervo deal, Google funds the project through a long-term agreement with NV Energy and receives credits against the value of the power. NV Energy sits in the middle as the regulated counterparty.
- The PUCN approved the tariff the week of 15 May 2025. At that point the energy supply agreement (ESA) and the Fervo-NV Energy PPA still needed approval.
- Fervo called interconnection "the primary bottleneck." It said Corsac could be "doubled or tripled," that it controls more than 16 GW of leases, and that it is in "at least five serious commercial conversations" with major corporations, with interest in BTM geothermal.
- Google said it is "already seeing conversations emerge in several other states" (Latitude Media).
- L23 counts the CTT among a dozen approved large-load clean tariffs, alongside Dominion Schedule CFG, Duke GSA, Evergy CER and Ameren. The template is spreading.

**What buyers pay.**
- No hyperscaler geothermal price has been disclosed.
- Sibling synthesis (L23, B03): new geothermal PPAs clear at **$75-130/MWh**. Hyperscaler-specific deals are inferred to sit at the top of that range.
- Fervo's 658 MW of binding PPAs carry about $7.2B of backlog (424B4, via B02). That works out to roughly $11M of contracted revenue per MW (calc).
- For comparison, BTM gas bridging power costs **$100-165/MWh**, against $90-95/MWh from the grid (Rabobank 2026, via `02-data-center-power.md`). Geothermal at $80-130 is cost-competitive with the firm alternative hyperscalers are actually buying today, before any carbon premium.
- Google's audit rights in the 3 GW framework show that hyperscalers want cost-plus visibility, not a blind premium (B03). Their real willingness to pay is for **certainty of MW and COD**.

## 3. How much demand: Rhodium (March 2025)

Rhodium Group, King, Ricks, Pastorek and Larsen, *The Potential for Geothermal Energy to Meet Growing Data Center Electricity Demand*, 11 Mar 2025. The PDF was parsed locally. https://rhg.com/research/geothermal-data-center-electricity-demand/

**Demand assumptions**
- About 80 GW of US data-centre peak demand by 2030, with about 27 GW of growth from hyperscale. Load is assumed flat.
- Data-centre share of US electricity: about 2% (2020) and about 4.5% (2024).
- LBNL's 2025 update projects **11.8% of US electricity by 2030** (range 9.5-15.3%): 192 TWh (2024) → 649 TWh (2030) (via L23).

**Clustered siting**
- If data centres keep siting near fibre and population, **BTM geothermal can meet 55-64% of hyperscale growth, or 15-17 GW**.
- It can meet 100% of growth in 13 of the 15 largest markets, under the dry-cooling-plus-solar-and-battery option.
- Per-market GW from Rhodium's Figure 3:

| Market | BTM geothermal potential (GW) |
|---|---|
| Phoenix | 3.8 (100% of growth) |
| Dallas-Fort Worth | 2.9 |
| Las Vegas | 1.9 |
| San Jose | 1.1 |
| Salt Lake City | 0.9 |
| Washington, DC | 0.9 (15%) |
| Chicago | 0.8 (46%) |
| Reno | 0.8 |
| Austin | 0.6 |
| San Antonio | 0.6 |

- **Nevada + Utah + Texas together come to about 7.7 GW** of the 15-market total in that table (calc): Las Vegas, Reno, Salt Lake City, Dallas-Fort Worth, Austin and San Antonio.

**Geothermal-driven siting**
- If campuses go to the heat, geothermal meets **all** projected growth at **31-45% lower LCOE**.
- The top states are CO, CA, NV, NM and OR. Utah, Texas, Idaho, Indiana and Ohio follow (Figure 6).
- The fibre-constrained case requires a site within 25 km of a fibre node.

**Cost and willingness to pay**
- Baseline: a **20% green premium** over retail, giving a national LCOE of **$78-85/MWh** (regional $49-111/MWh).
- With **0% premium**, deployment falls 38-55%, mainly in Phoenix and Northern Virginia.
- With **50% premium**, every available site up to expected demand is used.
- Willingness to pay is the swing variable, and the CTT is the regulatory mechanism that turns it into cash.

**Why behind-the-meter**
- About 1.7 GW of geothermal was waiting for interconnection agreements, against about 4 GW installed.
- BTM "bypass[es] this lengthy wait."
- Direct geothermal cooling can also cut data-centre electric load.
- R10 reports that the Nevada geothermal queue jumped from about 1.8 to 4.8 GW in one year, so queue scarcity there is acute.

**Barriers Rhodium names**
- Federal-land projects take 7-10 years and involve 8 or more agencies.
- Some states have unclear ownership of the heat resource. Texas settled it in 2023.
- State rules may treat BTM sales as utility service.
- **Improved data:** "maps with less geographic granularity may miss important hot spots". This is explicitly the Terranox wedge.

## 4. Siting: Nevada, Utah, Texas

**Nevada**
- **Strongest buyer-side state today.** It has the CTT, two Google deals totalling about 265 MW, and Zanskar's 100 MW build-transfer to NV Energy. In total, about 365 MW of new geothermal has been committed through one utility in about 2 years (B02).
- **Market size.** Rhodium gives Las Vegas 1.9 GW and Reno 0.8 GW of BTM potential.
- **Constraints.**
  - Interconnection is the bottleneck (Fervo; R10).
  - NRS 533.372 gives the State Engineer discretion over water used for power exported from Nevada (R09).
- **Lease prices.** Nevada BLM lease prices have repriced from about $2-4/acre to $232-410/acre next to discoveries (R03, R04, L07).
- **Campus geography.** The Reno/Tahoe-Reno Industrial Center cluster hosts Switch, Google and others (unverified detail), close to Great Basin hydrothermal fairways.

**Utah**
- **Market size.** Rhodium gives Salt Lake City 0.9 GW. Utah appears in its geothermal-driven top-10 states.
- **Offtake goes to California.** Fervo's Cape Station (Millard County) sells to California load: SCE 336 + 62 MW, plus CCAs. It does not sell to PacifiCorp or to Utah data centres (B03).
  - That means **no Utah in-state hyperscaler geothermal deal has been disclosed.** This is an open lane.
- **Policy and water.**
  - "Operation Gigawatt" is a state energy-expansion push (via `05-policy-economics.md`).
  - Utah's 2025 SB 132 reportedly lets large loads procure generation outside PacifiCorp's standard path (unverified; the bill page fetched had no text).
  - Utah splits heat ownership (which follows land) from geothermal *fluid* appropriation, and the Milford area is water-constrained (R09).
- **Lease prices.** 2025 Utah BLM sales cleared at up to $344/acre (L07).

**Texas**
- **Market size.** Rhodium gives about 4.1 GW in DFW, Austin and San Antonio. Texas becomes material in the geothermal-driven cases.
- **Resource rights.**
  - Texas clarified heat ownership in 2023: heat belongs to the surface estate, and the RRC regulates it.
  - The RRC permitted its first geothermal well in about six months (Rhodium). Sage says permitting takes "a few weeks" (R07).
  - Resource grade is moderate: 31-33 °C/km on the Gulf Coast, and 120-200 °C or more at 3.5-5 km in the Delaware and Val Verde basins (R07). Power there is an EGS or deep-sedimentary play.
- **Demand and grid rules.**
  - The ERCOT large-load queue stood at about **438 GW** by June 2026, about 89% data centres, against an 85.5 GW all-time peak.
  - SB6 (2025) imposes financial security, site control and mandatory curtailment on loads of 75 MW or more.
  - On-site generation can offset required transmission capacity (WLPUN), and partial curtailment can buy early access (PCLR) (`owner/lane_energy.md`, ERCOT 18 Jun 2026: https://www.ercot.com/news/release/06182026-puct-approves-ercots).
  - The PUCT's first SB6 case (Jul 2026) required a 260 MW co-located data centre to shed its full load within 30 minutes (`05-policy-economics.md`).
  - **Firm on-site generation is therefore a speed-to-power asset in ERCOT.**
- **Headwinds.**
  - Sage, the Texas-native champion, took its next commercial EGS project to Ormat's Blue Mountain in **Nevada** (22 Sep 2026; R07).
  - Meta-Sage's location is only "east of the Rockies."

## 5. "Power-first" campuses and powered land

- **Speed to power decides site value.** Firm grid service for a site of 300 MW or more takes 4-7 years in PJM, ERCOT and the Southeast, against about 12-24 months for curtailable service (`02-data-center-power.md`).
- Latitude estimates that 25-33% of incremental data-centre demand through 2030 will be served BTM (https://www.latitudemedia.com/news/behind-the-meter-generation-is-picking-up-traction/, via `02-data-center-power.md`).

**Powered-land comparables**

| Deal / market | Price | What it shows | Source |
|---|---|---|---|
| Plug Power → Stream Data Centers (Apollo), Graham, Young County, TX | up to **$76.5M** ($50M at close + $26.5M contingent) for 66 acres with 164 MW of grid interconnection; about $1.16M/acre against $1,831/acre regional rural land (**about 630x**); about $0.47M/MW | "The interconnection... is what commands the price" | https://thetexaslandagent.com/texas-data-center-land-young-county |
| Secondary markets | land at about $10k/acre with no power path reaches six figures per acre once power is established (10-50x) | — | Avison Young via TechTarget (`owner/lane_energy.md`) |
| Northern Virginia | about $4M/acre unpowered vs at least $6M/acre powered | — | Avison Young via TechTarget (`owner/lane_energy.md`) |
| Signed-agreement powered land outside tier-1 hubs | **about $0.3-1.5M/MW over raw land** | — | `owner/lane_energy.md` |
| Cloverleaf Infrastructure | has sold more than 7 GW of powered land, including to Oracle and OpenAI; Nvidia minority stake Aug 2026 | Grid-based powered-land origination is proven and crowded | `owner/lane_energy.md` |

**Geothermal powered land.** A geothermal-backed site offers firm, 24/7, carbon-free power on the land itself, with no queue for BTM, plus direct cooling. Rhodium's geothermal-driven case is exactly this product.

Stacked value per MW (calc, indicative):

| Layer | Value per MW |
|---|---|
| Confirmed resource | $0.1-0.5M (B02, unverified) |
| Powered-land premium | $0.3-1.5M |
| Contracted-PPA developer value | about $11.6M per PPA-MW (Fervo IPO-implied, B01); this is development value, not land |

**Caveats**
- BTM geothermal needs the resource to sit within campus distance: about 25 km of fibre in Rhodium's case.
- The hydrothermal fairways of rural Nevada and Utah are remote from fibre and population. Las Vegas has thin hydrothermal resource. Reno is better.
- A BTM plant still needs firming or N+1 redundancy for data-centre uptime (unverified magnitude).
- State law may treat BTM sales as utility service (Rhodium).

## 6. Risks to the demand thesis

- Hyperscaler appetite for PPAs depends on AI monetisation (`05-policy-economics.md`).
- Interconnection requests run at 5-10x the data centres that actually get built (Camus, via `02-data-center-power.md`).
- Many deals are "up to" or non-binding: Meta 2 x 150 MW, and Google's 3 GW framework.
- Prices are confidential, and Google's audit rights cap the premium.
- Federal permitting takes 7-10 years. A data-centre timeline (2-3 years) is shorter than a hydrothermal development timeline, so the asset has to be *pre-positioned* years ahead.

## 7. Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **The end buyer exists and pays for certainty.**
   - Google, Meta and the CTT pathway are paying premiums for named new geothermal MW.
   - Ormat (150 MW for Google by 2028-30) and Fervo (1 GW proposal due to Google) need *more confirmed resource* than their own pipelines produce.
   - A company that finds blind resources in public data and banks the rights cheaply ($2-10/acre non-competitive, against $232-410/acre after a discovery) sells into a buyer pool that is short of resource.
2. **The best asset is geothermal powered land, not a bare lease.**
   - The asset is an SPV holding the lease, a confirmed temperature-gradient or flow result, the water appropriation (in Utah, a separate filing), surface and land option, and a queue position or BTM plan.
   - It can be sold to:
     - a developer (Ormat, Fervo, Sage, XGS);
     - a hyperscaler or campus developer, as a power-first site;
     - a utility via CTT.
   - Value stacks the resource step-up and the powered-land premium of about $0.3-1.5M/MW. A 100 MW site could plausibly be worth tens of millions of dollars before a plant is built (calc, optimistic).
   - This matches "own the asset" and avoids the "service/tool" shape.
3. **Search for heat near load, not just high enthalpy.**
   - Rhodium's results are capped by distance to fibre and population. The ML target should be favourability conditioned on within about 25 km of fibre and substations, near Reno, Salt Lake/Wasatch Front, DFW/Austin/San Antonio, Phoenix and Las Vegas.
   - The public oil and gas BHT and log archives (Texas RRC, Utah, Nevada) are densest in exactly the sedimentary basins near Texas loads. Classic Great Basin hydrothermal targeting ignores them.
4. **The gap vs Zanskar.**
   - Zanskar is a vertically integrated build-own-operate developer: about $180M of equity, Lightning Dock, a 100 MW NV Energy build-transfer, and about six 20 MW plants.
   - Its offtakers are utilities and CCAs. It has **no disclosed hyperscaler PPA** despite naming the target (Z05).
   - It concentrates on remote Great Basin blind hydrothermal systems.
   - It does not sell pre-proven packages to rivals, and it does not optimise for co-location with campuses.
   - The open seam is a **neutral, capital-light origination and site bank**. That company would:
     - bank rights basin-wide;
     - add campus-ready land, water and interconnection or BTM status;
     - sell or JV to whoever holds the hyperscaler contract, whether Ormat, Fervo, Sage, XGS, a utility under a CTT-type tariff, or Zanskar itself;
     - lean into Utah in-state and Texas/ERCOT, where no hyperscaler geothermal deal has been disclosed and SB6 rewards on-site firm power.
5. **Scale check (passes "not too small").**
   - Rhodium's addressable volume is 15-17 GW, rising to all growth under geothermal-driven siting.
   - Even 1-2 GW of banked, campus-proximate sites at $0.3-1.5M/MW of combined resource and powered-land premium is a **$0.3-3B asset value** (calc).
   - The upside is a royalty or $/MWh override (Centaurus precedent, $5/MWh ≈ $0.4M/MW PV; B02) on top.

## Sources

- Rhodium Group (2025), Geothermal and data centres: https://rhg.com/research/geothermal-data-center-electricity-demand/ (PDF parsed locally)
- Latitude Media, CTT approval (15 May 2025): https://www.latitudemedia.com/news/the-clean-transition-tariff-won-approval-in-nevada-whats-next-for-fervo/
- Meta-Sage (26 Aug 2024): https://about.fb.com/news/2024/08/new-geothermal-energy-project-to-support-our-data-centers/
- XGS-Meta (Jun 2025): https://www.businesswire.com/news/home/20250612778008/en/XGS-Energy-and-Meta-to-Partner-on-150-MW-Advanced-Geothermal-Project
- Ormat-NV Energy-Google 8-K (17 Feb 2026): https://www.sec.gov/Archives/edgar/data/1296445/000143774926004369/ex_921781.htm
- Google-Fervo (2023): https://blog.google/outreach-initiatives/sustainability/google-fervo-geothermal-energy-partnership/
- Fervo Series E with Google: https://www.thinkgeoenergy.com/google-joins-usd-462m-funding-round-for-fervo-energy/
- Sage Series B (Ormat $25M): https://www.thinkgeoenergy.com/sage-geosystems-closes-97-million-series-b-funding-round-to-support-pressure-geothermal-deployment/
- Microsoft-G42 Kenya: https://news.microsoft.com/2024/05/22/microsoft-and-g42-announce-1-billion-comprehensive-digital-ecosystem-initiative-for-kenya/
- Texas powered land (Plug/Stream, Graham TX): https://thetexaslandagent.com/texas-data-center-land-young-county
- ERCOT/PUCT Batch Zero (18 Jun 2026): https://www.ercot.com/news/release/06182026-puct-approves-ercots
- Latitude Media, BTM share: https://www.latitudemedia.com/news/behind-the-meter-generation-is-picking-up-traction/
- Zanskar-NV Energy 100 MW: https://zanskargeothermal.substack.com/p/zanskar-inks-100-mw-power-purchase
- Utah SB 132 (2025) bill page (text not retrieved): https://le.utah.gov/~2025/bills/static/SB0132.html
- Sibling files: /home/user/nuketime/research/geothermal/evidence/B02-buyers.md, B03-ppa-prices.md, L23-data-centre-heat.md, R07-texas.md, R09-water-rights.md, R10-transmission-queue.md, Z05-business.md; /home/user/nuketime/research/02-data-center-power.md; /home/user/nuketime/research/owner/lane_energy.md
