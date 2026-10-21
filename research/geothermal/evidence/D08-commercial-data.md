# D08: Commercial subsurface data incumbents (Enverus, S&P Global/IHS, TGS, Novi, Kinetica) and geothermal

*Method note: the shared WebSearch budget (200 calls per turn, shared across agents) was used up before this agent's first query, so no open searches ran. Everything below comes from direct WebFetch of primary pages: TGS, PR Newswire (the Enverus release), Kinetica, Zanskar, DOE GDR, SMU, Project InnerSpace and ThinkGeoEnergy. It also uses numbers that sibling evidence files (D01, D07, L10, Z07) had already sourced. Enverus.com and spglobal.com returned HTTP 403, and several Novi Labs pages returned empty bodies. Claims about those vendors' product catalogues are therefore marked (unverified). The brief's premise of "TGS geothermal maps 2024" could not be confirmed from any page fetched (unverified). A follow-up turn with a fresh search budget should check it.*

## 1. The headline fact: the biggest legacy log library now belongs to one vendor, Enverus

On **8 July 2026**, TGS closed the sale of its North American well data products business (A2D, acquired by TGS in 2002) to **Enverus, Inc.**:

- **Price:** "in excess of USD 100 million". That is **USD 100M at closing plus a USD 15M earn-out**, conditional on milestones. Source: https://www.tgs.com/press-releases/tgs-sells-north-american-well-data-products-business-to-enverus
- **Revenue:** **USD 27M in 2025**, about **2.9% of TGS multi-client revenue**. This implies roughly **3.7–4.3x revenue**, which is low for data, and TGS called the business "less strategic" next to its offshore seismic focus (after the PGS, Magseis and ION deals). Source: https://www.tgs.com/well-data
- **What Enverus bought:** **>8 million depth-calibrated raster logs**, **>1.9 million digital LAS files**, **>5 million proprietary logs "not available from any public or regulatory source"**, and **>2 million hand-picked formation tops, petrophysical interpretations and basin temperature models**. Coverage spans every major US producing basin (Permian, Eagle Ford, Bakken, Marcellus named), plus 3D log attribute volumes. Source: https://www.prnewswire.com/news-releases/enverus-acquires-a2d-well-log-library-from-tgs-connecting-subsurface-data-to-energy-decision-workflows-302820900.html
- **TGS keeps an internal-use licence** to the library, for seismic enhancement only.
- **Stated use cases are all oil and gas:** well planning, landing zones, reservoir characterisation, asset development. Neither release mentions **geothermal, CCS, lithium or power** as uses of A2D. Enverus promises "energy-specific AI workflows" over time but gives no timeline.
- Enverus had also just bought **PDS Energy Information's exchange assets**. Those carry the data exchange for an estimated **80% of US completions, production and drilling data** (same PR Newswire release).

**Reading:** A2D already contains "basin temperature models", which are a temperature-at-depth product in all but name. That product now sits inside Enverus, the largest US upstream data platform, which also runs land, ownership and courthouse records (Enverus cites 350M+ courthouse records; https://www.tgs.com/well-data). Enverus already holds the ingredients a geothermal data product needs: corrected BHTs, LAS curves, tops, land and ownership. It has not yet packaged them as a geothermal product, and it does not take land positions.

## 2. Vendor-by-vendor

| Vendor | Geothermal product? | Temperature-at-depth? | Pricing | Owns assets / takes land? |
|---|---|---|---|---|
| **Enverus** (private; now owns A2D) | No dedicated geothermal product found in any fetched release. Enverus Intelligence research covers energy transition and power (unverified for geothermal specifically) | Yes, implicitly: A2D "basin temperature models" plus header BHTs | Subscription and enterprise licensing; LAS sold per curve with volume discounts; no public price list (D07) | No. It is a pure data and SaaS vendor |
| **TGS** (Oslo-listed) | None on the current site. The "New Energy" section lists only Carbon Storage, Wind, Solar and Marine Consulting (https://www.tgs.com/new-energy). A claimed 2024 geothermal map product could not be found (unverified) | Its onshore temperature asset left with A2D. TGS keeps an internal licence | Multi-client seismic licences | No |
| **S&P Global Commodity Insights (ex-IHS, Petroleum Information)** | Not verified (site returned 403). Its research and analytics cover geothermal power markets (unverified) | Holds US well headers and LAS with BHT fields (count unverified; D01, D07) | Enterprise licences; widely reported as six to seven figures a year for large users (unverified) | No |
| **Novi Labs** | No geothermal mention in any recent blog excerpt fetched (https://novilabs.com/blog/) | No | SaaS for shale operators (unverified) | No |
| **Kinetica** | No. It sells a GPU-accelerated SQL, vector, spatial and time-series database. "Energy & utilities" is a listed vertical, and **Enverus is shown as a customer** (https://www.kinetica.com/) | No | Cloud, Developer and Enterprise editions | No. It is infrastructure, not a subsurface data owner |

Other data holders in this market (from sibling files): **MJ Logs** (3M wells, 7M logs; D07) and **Neuralog** sell raster and LAS. **BEG (Texas)** charges **$10 per raster scan**, about **$15M at list for its 1.5M-image archive** (D01, D07).

## 3. Free and public substitutes are commoditising regional temperature

- **Project InnerSpace GeoMap.** The Beta launched on 1 Dec 2023 at COP28, built with Google. **GeoMap North America launched 4 June 2024 with more than 150 surface and subsurface layers, free to use**, including US isotherm-depth layers such as depth to 200 °C. The ThinkGeoEnergy article names only Google as a collaborator. https://www.thinkgeoenergy.com/project-innerspace-launches-geomap-geothermal-prospecting-tool-for-north-america/ ; https://geomap.projectinnerspace.org/
- **DOE Geothermal Data Repository:** **1,423 datasets from 146 providers, 764 TB, 73.7M downloads**, free under CC-BY 4.0. It includes Play Fairway, FORGE and Data Lakes. https://gdr.openei.org/
- **SMU Geothermal Lab:** Geothermal Map of North America, temperature-depth maps and NGDS contributions. https://www.smu.edu/dedman/academics/departments/earth-sciences/research/geothermallab
- **USGS, NREL and UNR ML favourability maps** (L03, L10, Z07).

Regional temperature screening is therefore no longer a moat. Free tools give a first pass, and commercial vendors have well-level data but no geothermal packaging. Neither tells you **where permeability and an acquirable right overlap**. Sibling L10 found that permeability and transmissivity, not temperature, are the binding constraint in sedimentary basins.

## 4. Is the incumbent data stack a threat to a data-led entrant?

**As a competitor selling data: low threat to an asset-owner, high threat to a data seller.**
- The economics of selling legacy logs are mediocre. The cleanest comparable is A2D: ~$27M a year in revenue, sold for ~$100–115M after 30 years of building. A Terranox-shape company that tries to *sell* geothermal maps competes with free GeoMap at the low end and with Enverus bundles at the high end. That service shape scores low under the standing rules.
- Enverus is the only vendor that could plausibly ship a "geothermal favourability" layer quickly, because it holds BHTs, temperature models, land, ownership and AI ambitions. That would raise the floor for everyone, including competing lessees. It would **sell to many**, so it would erode an information edge that depends on being first.

**As a supplier: an opportunity.**
- The proprietary part of A2D (>5M logs not in public sources) is exactly the "illegible" data a Terranox-shape entrant wants. Enverus monetises it per curve or by subscription. A field-of-use licence (geothermal only, for internal use) is a plausible negotiation (price unverified). That is cheaper than re-digitising, and it stays non-exclusive.
- Enverus's land and ownership records (350M+ courthouse records) are directly useful for finding **private geothermal and mineral rights holders** in Texas and other split-estate states.

**As acquirers or partners: possible exit.**
- None of these vendors takes land positions or owns resources. Enverus's buying behaviour (PDS exchange, then A2D) shows a consolidator that pays for data with a durable edge. A geothermal entrant whose *proven acreage* is the product is not acquisition-shaped for Enverus, but its *derived dataset* (corrected temperature at depth plus permeability proxies plus drilled outcomes) could be.

**Key risk to watch:** Enverus packaging A2D "basin temperature models" and land data into a geothermal or "subsurface heat" module aimed at Fervo, Ormat, Sage and data-centre developers (unverified as of Oct 2026). Developers already licensing Enverus for oil and gas (Fervo's team is heavily ex-oil-and-gas) would get the same temperature view in their existing platform.

## 5. Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **Don't sell data; own the right.** Selling data tops out at about A2D scale (~$27M a year, ~$100M exit after decades) and competes with free GeoMap. The Terranox step-up comes from buying BLM, state or private geothermal rights before proof. No incumbent data vendor does this, so none of them is a direct competitor for the asset.
2. **Incumbents are oil-and-gas-shaped, and so is the gap.** Enverus, S&P, A2D and MJ cover *sedimentary producing basins* (Permian, Gulf Coast, Williston, DJ, Anadarko). Zanskar's discoveries, land and plant are in the **Great Basin and New Mexico** hydrothermal settings. Its stated model is field geology plus AI, millions of acres across the western US, Big Blind, Lightning Dock, a 100 MW NV Energy PPA, and a $115M Series C (Jan 2026) plus $40M development capital (Apr 2026) (https://www.zanskar.com/about). The open gap is **geothermal in the oil-patch footprint**: deep BHT-rich basins where millions of commercial logs exist but rights are fragmented private or state minerals. Zanskar is not leasing there (Z07), and the data vendors are not acquiring.
3. **The data moat must be combinatorial, not regional.** Regional temperature is commoditised (GeoMap, USGS, NREL, A2D temperature models). The defensible layer is well-level corrected BHT, permeability proxies from LAS (porosity and lithology), and drilled outcomes, joined to **who owns the right and whether it is acquirable**. That last join is exactly what Terranox does with the Saskatchewan assessment files.
4. **Buy data inputs tactically.** Budget for a non-exclusive Enverus/A2D or S&P licence for deep wells only, plus BEG scans at about $10 each (D01). A targeted first pass costs far less than the ~$15M full Texas archive. Treat incumbents as suppliers.
5. **Speed is the moat against Enverus.** If Enverus ships a geothermal layer, the information edge narrows for everyone. The entrant must convert insight into leases or option agreements quickly and build proprietary drilled-truth data, such as temperature-gradient holes, that no vendor holds.
6. **Exit buyers are developers, not data vendors.** Proven acreage sells to Fervo, Ormat, Sage, utilities and data-centre offtakers. A derived subsurface-heat dataset could be a secondary sale to Enverus.

## Sources
- https://www.tgs.com/press-releases/tgs-sells-north-american-well-data-products-business-to-enverus
- https://www.tgs.com/well-data
- https://www.prnewswire.com/news-releases/enverus-acquires-a2d-well-log-library-from-tgs-connecting-subsurface-data-to-energy-decision-workflows-302820900.html
- https://www.prnewswire.com/news/enverus/
- https://www.tgs.com/new-energy
- https://www.tgs.com/digital
- https://www.kinetica.com/
- https://novilabs.com/blog/
- https://www.thinkgeoenergy.com/project-innerspace-launches-geomap-geothermal-prospecting-tool-for-north-america/
- https://geomap.projectinnerspace.org/
- https://gdr.openei.org/
- https://www.smu.edu/dedman/academics/departments/earth-sciences/research/geothermallab
- https://www.zanskar.com/about
- https://www.zanskar.com/who-we-work-with
- Sibling evidence: D01-texas-rrc.md, D07-scanned-logs.md, L10-sedimentary.md, Z07-other-ai.md (same folder)
