# Z05: Zanskar's business model (develop, operate, sell power, sell projects, offtakes)

*Research note, 2026-10-21. Method: the shared WebSearch budget for this turn was already used up when this agent started, so no web searches were run. Every fact below comes from WebFetch of Zanskar primary sources (its website and the official Substack it uses for press releases), from Latitude Media, and from facts already sourced in sibling evidence files Z01, Z02 and L-series, which are cited by URL. Anything without a URL is marked (unverified). These sources do not cover Zanskar PPA pricing, the Lightning Dock purchase price, or any Ormat or data-centre deal, because none of those were found.*

## 1. One-line answer

Zanskar is a **vertically integrated geothermal IPP (independent power producer) that also does its own exploration**:

- It finds resources with its AI prospecting toolkit and field crews.
- It buys the rights: BLM leases at auction, or distressed assets.
- It drills, then builds and operates **20 MW binary-style plants**.
- It sells firm power under long-term utility PPAs.
- In at least one case it builds and operates the plants and then **sells the finished portfolio to the utility**.

It is **not** a software or exploration-services vendor. It does not publicly license its models, and no farm-out or prospect sale to Ormat, Fervo or any other developer has been disclosed.

## 2. What Zanskar says about itself (primary language)

- About page: "We discover these resources, then **develop and operate the power plants** that turn earth's natural heat into electricity." The page also refers to "our operating Lightning Dock Geothermal Power Plant in New Mexico." (https://www.zanskar.com/about/)
- Series C release (21 Jan 2026): the mission is to "**develop, build, own, and operate** high-grade geothermal assets" as "a foundational component of the modern grid." Use of funds is to "expand its AI discovery platform and to **begin building geothermal power plants**," and to advance a "gigawatt-scale pipeline." Power is "slated to begin delivering before 2030" in the Western US. The release names hyperscalers seeking firm clean power as a target market but names none as a customer. (https://zanskargeothermal.substack.com/p/zanskar-raises-115m-series-c-following)
- CEO Carl Hoiland on why they operate: "The only way to test and prove out those ideas is to be an operator of those assets." (https://magazine.asme.org/issues/may-2026/news-hidden-geothermal-goldmines, via Z01)
- Its "Who we work with" page lists:
  - **Customers:** PNM (Public Service Company of New Mexico) and NV Energy.
  - **Partners:** U.S. Department of Energy, "U.S. Department of War," and **Freeport-McMoRan**. The page gives no detail on any of these relationships.
  - **Not listed:** any data centre, hyperscaler, Ormat or Fervo.
  - (https://www.zanskar.com/who-we-work-with/)

## 3. Revenue lines today and planned

| Revenue line | Status | Evidence |
|---|---|---|
| Merchant/contract power sales from an owned operating plant | **Live since mid-2024.** Lightning Dock (NM) is ~15 MW gross and sells to PNM. It delivered ~75,000 MWh in its first year under Zanskar, >140% above the legacy-well counterfactual. | https://zanskargeothermal.substack.com/p/one-year-at-lightning-dock ; customer list above |
| Long-term utility PPA from new greenfield plants | **Signed and conditional.** 100 MW, 20-year PPA with NV Energy (8 May 2026), delivery by 2030 and running to 2050. It takes effect only on PUCN approval of NV Energy's 2026 IRP. Price is undisclosed. | https://zanskargeothermal.substack.com/p/zanskar-inks-100-mw-power-purchase |
| Sale of built projects to the utility | **Contracted inside the NV Energy deal.** The PPA covers "multiple projects that Zanskar will **build and operate, then sell as a portfolio to NV Energy**." Named sites are Pumpernickel and Big Blind, "and others." The structure is effectively build-operate-transfer, and timing of the transfer is undisclosed. | same |
| Prospect-for-offtaker origination | **Framework only.** The GEODE (Geothermal Exploration, Offtake and Development Engagement) agreement with California Community Power, a JPA of 9 CCAs, was signed Apr 2026. Zanskar prospects inside CAISO, and CC Power and its members get "the opportunity" to support development and buy power. There is no MW, price, term or purchase commitment. | https://zanskargeothermal.substack.com/p/zanskar-and-cc-power-sign-geode-agreement |
| Government R&D cost share | **Selected, in negotiation.** Two DOE projects (Sep 2026): a stimulated horizontal injection well at Lightning Dock and deep directional exploration wells at an undrilled Nevada site. Amounts are undisclosed. | https://zanskargeothermal.substack.com/p/zanskar-selected-for-two-us-department |
| Hyperscaler / data-centre PPAs | **Stated target, none signed or disclosed.** | Series C release; Latitude Media |
| Licensing, software or exploration services | **None disclosed.** | (absence across all pages fetched) |

## 4. Capital stack and the "developer, then IPP" shift

- Zanskar has raised **$180M of equity in total**. That includes a **$115M Series C** (Jan 2026, led by Spring Lane Capital), which was oversubscribed and capped to limit dilution. The **Series B was $30M**, led by Obvious. The Series A was co-led by USV and Lowercarbon. (Series C release; https://www.latitudemedia.com/news/armed-with-115-million-geothermal-startup-zanskar-gets-ready-to-build/)
- CFO Diego D'Sola: "We've been 100% venture capital-backed since inception." He calls infrastructure capital "the hundreds of billions of dollars market that you need to tap into." (Latitude)
- **$40M Development Capital Facility** (23 Apr 2026), co-led by Just Climate and Spring Lane.
  - It is revolving and **non-recourse**, and it is designed to upsize to **$100M**.
  - It funds "key pre-construction activities" and bridges projects to conventional bank project finance.
  - Spring Lane's Jason Scott says the key is financing project capex "**off balance sheet**." Hoiland frames it as "pioneering the financial infrastructure the entire industry needs to scale."
  - Collateral, pricing and draw terms are not disclosed.
  - (https://zanskargeothermal.substack.com/p/zanskar-closes-40m-in-novel-development)
- Interpretation: there are three stacked capital layers.
  - VC equity pays for discovery.
  - Development debt pays for permitting, interconnection and confirmation drilling.
  - Project finance pays for construction.
  - This is the classic renewable IPP stack. Zanskar's stated goal is to bring geothermal's cost of capital "in line with mature energy asset classes" (D'Sola, via Z01).

## 5. Project design choices that reveal the model

- **20 MW building blocks.** Plants are sized at 20 MW so they qualify for the Western small-generator interconnection process. CTO Joel Edwards: "**Interconnection is our bottleneck.**" (Latitude)
- **No technology risk on purpose.** Edwards: "We're avoiding the first-of-a-kind risk label, so that we can access cheaper capital sooner." Zanskar uses conventional hydrothermal plus binary plants and oil-and-gas drilling practice. Its stated innovation is *where* to drill, not *how* to produce. (Latitude)
- **Pipeline:**
  - Six 20 MW plants are targeted to reach COD (commercial operation) in 3–4 years from Jan 2026.
  - Zanskar has "full or partial control" of sites with more than 700 MW of potential (D'Sola).
  - It describes a "multi-gigawatt pipeline."
  - It wants at least 10 confirmed sites to attract project finance (via Z01).
  - Pumpernickel Phase 1 is 20 MWe targeting ~2028. (https://www.thinkgeoenergy.com/zanskar-validates-ai-based-discovery-method-with-drilling-at-pumpernickel-geothermal-site-nevada/)
- **Rights acquisition:**
  - At Big Blind, Zanskar flagged the anomaly in late 2023, then **bought BLM leases at competitive auction before any drilling**, then drilled two holes in July–August 2025. It reported ~250 °F at ~2,700 ft and an estimated discovery cost of **<$15k/MW**, against more than $100k/MW historically. (https://zanskargeothermal.substack.com/p/zanskar-reveals-big-blind-the-discovery ; Z02)
  - At Lightning Dock, it bought a distressed operating plant in June 2024 (price undisclosed). One ~8,000 ft well (44-7) raised inlet temperature by ~60 °F and tripled production. (https://zanskargeothermal.substack.com/p/one-year-at-lightning-dock)

## 6. Partnerships: Ormat and others

- **Ormat:** no partnership, equipment supply deal, joint venture or asset sale with Ormat was found on any Zanskar page fetched. Equipment vendors for Lightning Dock or the planned plants are not disclosed (unverified). Ormat dominates Nevada as an owner-operator and lease bidder (see L-series files), so it is Zanskar's **competitor**, not its channel.
- **Freeport-McMoRan** is listed as a partner with no details. A plausible reading is access to mining land, data or power demand, but this is **(unverified)**.
- **"Department of War"** is listed as a partner with no details. A plausible reading is military-base firm-power interest, which is a known DoD geothermal theme, but this is **(unverified)**.
- **Utilities:** PNM is the existing plant offtaker. NV Energy holds the PPA and is the eventual buyer of the portfolio. CC Power is a framework partner.

## 7. Comparator context: how others monetise

- **Fervo** is a fully integrated EGS IPP. It has about 658 MW of binding PPAs (more than 1 GW by Oct 2026) and about $7.2B of backlog. EGS PPA prices run about $100–130/MWh (Rystad), and Google has a non-binding 3 GW framework. Fervo listed via an IPO in 2026. (Fervo S-1: https://www.sec.gov/Archives/edgar/data/1853868/000162828026025821/fervoenergy-sx1.htm ; L-series file)
- **Ormat** is an integrated owner-operator and equipment maker. Example: Tungsten Mountain, 24 MW, a 26-year PPA with SCPPA/LADWP, found through mineral-exploration holes. (https://investor.ormat.com/news-events/news/news-details/2017/24-MW-Tungsten-Mountain-Geothermal-Power-Plant-in-Nevada-Begins-Commercial-Operation/default.aspx)
- **Sage and XGS** have each signed Meta PPAs of up to 150 MWe (L-series file).
- So the hyperscaler offtake market exists. Zanskar simply has not disclosed one yet. Its offtakers so far are regulated utilities and CCAs.

## 8. Assessment of the model

Strengths:
- It owns the full value chain: the discovery arbitrage (<$15k/MW finding cost) plus the operating-asset value.
- It keeps technology risk low, which lowers its cost of capital.
- It has already built a debt layer for pre-construction work.
- The utility build-then-sell structure gives it an exit for built assets.

Weaknesses and constraints:
- **Capital intensity.** A 20 MW plant is roughly $100–150M (unverified rule of thumb, see Z02), and Zanskar can fund only a handful at a time.
- **Interconnection gating.** It is self-declared as the main bottleneck.
- **Utility-regulatory dependence.** The NV Energy PPA depends on IRP approval.
- **Slow cash conversion.** The first greenfield COD is ~2028–2030.
- **Opportunity cost.** Every discovery competes for a slot in a capex-bound build queue, so many good prospects may sit idle in the land book.

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **Zanskar monetises at the end of the chain, not the middle.** It captures value only once a plant is built, either as PPA revenue or through the build-then-sell portfolio to NV Energy. It has no disclosed product for selling *proven-but-unbuilt* resources. This is the clearest gap. A Terranox-shape company would be a **resource originator / rights bank**. It would acquire rights cheaply before proof, de-risk them to a "temperature-confirmed, drill-ready" or "discovery well" stage, then sell, farm out or keep a royalty or carry. Buyers would be Ormat, Fervo, IPPs, utilities, CCAs and data-centre developers. This mirrors mining prospect-generator economics, which Terranox already runs for uranium.
2. **Zanskar's own numbers show how big the step-up is.** Discovery cost is <$15k/MW (Big Blind). Built geothermal sells into PPAs at roughly $60–130/MWh over 20 years and costs roughly $5–7.5M/MW to build (unverified). The difference between the cost of a confirmed resource and its value is what a rights bank captures, without the $100M+ capex for each plant.
3. **Zanskar is structurally unlikely to compete for sales to rivals.** It describes itself as a developer-owner with a capex-bound queue, so selling proven parcels to Fervo or Ormat would cannibalise its own pipeline. Its GEODE deal with CC Power is the closest thing to "prospect for a customer," and it still routes through Zanskar as the developer.
4. **Offtake channel gap.** Zanskar has no disclosed hyperscaler PPA, even though it names hyperscalers as a target. Data-centre developers need **sites with firm-power potential near load and interconnection**, not just electrons. A rights bank could sell them sites or stakes directly. Meta has signed 150 MWe deals with Sage and XGS, and Google has a 3 GW framework with Fervo, so that demand is real.
5. **Rights-type and geography gap.** Zanskar's disclosed rights are BLM leases (Big Blind) and acquired brownfields (Lightning Dock) in NV and NM, plus CA prospecting. Areas with no disclosed Zanskar activity:
   - Private and state geothermal estates.
   - Oil-and-gas basins, where BHT and well-log archives are the data.
   - Mining assessment files (Freeport is a partner, which is a watch item).
   - Canada.
   - These are where a Terranox-style engine for public-but-illegible archives plus title diligence fits best.
6. **Brownfield roll-up is validated and not yet saturated.** Lightning Dock shows that buying a "tapped-out" plant and drilling one deep well can triple output. A rights bank could buy dormant leases or tired small plants and either flip them or redevelop them.
7. **Risks:**
   - Zanskar could add a "sell prospects" arm at any time.
   - Its DOE wins and $100M development facility give it more drilling capacity, and most of the value is confirmed by drilling, which a pure land bank must buy or partner for.
   - The buyer market for un-flow-tested resources is thin (unverified), so a rights bank needs one or two anchor offtake or buyer relationships from day one.
8. **Scoring view:** Zanskar's business is "own the asset, end to end." A Terranox geothermal company that owns the **rights and the de-risked resource** is still an asset-owning shape, not a tool or service. It differentiates on *where in the chain it sells* and *which rights it buys*, not on "AI finds blind hydrothermal." This passes the "not too small" bar: Zanskar alone controls more than 700 MW of potential and has signed a 100 MW PPA.

## Sources

- https://www.zanskar.com/about/
- https://www.zanskar.com/who-we-work-with/
- https://www.zanskar.com/news
- https://zanskargeothermal.substack.com/p/zanskar-raises-115m-series-c-following
- https://zanskargeothermal.substack.com/p/zanskar-closes-40m-in-novel-development
- https://zanskargeothermal.substack.com/p/zanskar-inks-100-mw-power-purchase
- https://zanskargeothermal.substack.com/p/zanskar-and-cc-power-sign-geode-agreement
- https://zanskargeothermal.substack.com/p/zanskar-selected-for-two-us-department
- https://zanskargeothermal.substack.com/p/one-year-at-lightning-dock
- https://zanskargeothermal.substack.com/p/zanskar-reveals-big-blind-the-discovery
- https://www.latitudemedia.com/news/armed-with-115-million-geothermal-startup-zanskar-gets-ready-to-build/
- https://magazine.asme.org/issues/may-2026/news-hidden-geothermal-goldmines
- https://www.thinkgeoenergy.com/zanskar-validates-ai-based-discovery-method-with-drilling-at-pumpernickel-geothermal-site-nevada/
- https://www.sec.gov/Archives/edgar/data/1853868/000162828026025821/fervoenergy-sx1.htm
- https://investor.ormat.com/news-events/news/news-details/2017/24-MW-Tungsten-Mountain-Geothermal-Power-Plant-in-Nevada-Begins-Commercial-Operation/default.aspx
