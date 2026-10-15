# Lane: the built world, permits and government licences as claimable assets

Eighth hunt, written 15 October 2026. Web searches used: 15 of 20. Several government hosts (TCEQ, ADWR,
PUCT) were not fetched; access to datasets is checked against their documentation only.

## Bottom line

No candidate in this lane is as strong as Terranox. Most scarce licences in the built world fail one of
the brief's tests in a predictable way:

- **They are not first-come.** Many are allocated by comparative review, lottery or auction: CON
  licences, LIHTC, casinos, airport slots, port concessions, NEVI and AFIR grants, Florida quota liquor
  licences.
- **Ownership is restricted.** Pharmacies in the EU and Australia, and broadcast licences, can only be
  owned by qualified operators.
- **The ceiling is small.** Liquor licences, billboards, taxi medallions and short-term-rental permits
  are each sub-$1B in total.
- **Someone large already owns the position.** Towers and ground leases, waste, aggregates, and powered
  data-centre land all have dominant players.

Two candidates are worth a second look:

- **C1, "offset mining"** (score 5). Generate and bank nonattainment-area emission reduction credits ahead
  of the on-site gas wave at data centres and LNG plants. The credits are government-registered,
  rivalrous and finite, but the ceiling is about $0.3-1.5B.
- **C3, rule-change land promotion** (score 5). Use ML on planning-appeal decisions to option land made
  newly permissible by the UK grey belt policy and US state by-right laws. The ceiling is very large
  (£13bn/yr of planning uplift in England alone), but the business is crowded and the claim is only a
  private option, not a government first-come right.

---

## C1. Offset mining: creating and banking nonattainment emission reduction credits (ERCs)

**Thesis.** Under the Clean Air Act's nonattainment New Source Review, a new major source in an ozone or
PM nonattainment area must buy emission offsets (ERCs) before it can be permitted. The ratio is 1.1-1.5
tons of offsets for every ton of new emissions; DFW and Houston-Galveston-Brazoria (HGB) are severe ozone
areas. ERCs are created only by real, surplus, permanent, quantifiable and enforceable reductions (for
example shutting down or electrifying existing sources), and they are registered by the state. Several
kinds of new demand are hitting nonattainment areas at the same time:

- behind-the-meter gas turbines and reciprocating engines at data centres (DFW, Houston, Phoenix, Chicago,
  Northern Virginia);
- LNG and petrochemical expansions on the Gulf Coast;
- fabs (TSMC in Phoenix).

The company finds and acquires the cheapest reductions first, then holds the registered credits.

**Public datasets, and why they are public.**
- EPA National Emissions Inventory (point sources) and the state annual emissions inventories. These are
  mandatory reporting under the CAA.
- EPA CAMD/CEMS hourly unit-level NOx data for power plants, which is public under Acid Rain/CSAPR
  reporting.
- EIA-860 and EIA-923 data on unit age, heat rate and capacity factor, which is a statutory survey.
- The ERC registries: TCEQ (Texas), the Arizona Emissions Bank (ADEQ), NY DEC, PA DEP, SJVAPCD and San
  Diego APCD. Registries are public so that offsets can be verified ([TCEQ ERC program](https://www.tceq.texas.gov/airquality/banking/erc_program.html), [Maricopa ERC](https://www.maricopa.gov/4562/Emission-Reduction-Credit-Program), [NY registry](https://dec.ny.gov/sites/default/files/2024-01/ercregistry.pdf)).
- State air permit applications and public notices, which open-records and permit-notice rules make
  public. These are the demand signal: generator and turbine permits are filed months before data-centre
  announcements.
- TERP grant project lists (Texas).
- Non-road and fleet registrations, for mobile-source ERCs (MERCs) in Maricopa.

**The ML problem.** There are three parts:
1. **Supply.** Rank every emitting unit in each nonattainment area by its expected creditable tons per
   dollar. This means predicting which units are close to retirement or are cheap to electrify (from age,
   dispatch, heat rate and ownership distress), then working out the creditable baseline. The baseline
   follows each state's look-back and surplus rules, so it is not simply reported emissions. This is messy,
   rules-heavy inference across sources that are not joined up.
2. **Demand.** Forecast offset demand by area and pollutant 2-5 years ahead. The inputs are air-permit
   filings, utility large-load filings, data-centre and LNG pipelines, and nonattainment reclassification
   risk (a "bump-up" lowers the major-source threshold and raises the offset ratio, creating demand
   overnight).
3. **Acquisition.** Price each acquisition against the forecast clearing price.

**What the company owns.** Registered ERC certificates: state-issued, transferable, exclusive property
interests in a finite regional pool. It may also own the retired sources themselves, such as old
peakers, industrial boilers and engines, bought for their emission rights.

**Why it is rivalrous and defensible.** Each ton of reduction can be certified only once, and only within
that nonattainment area (or one of equal or higher classification). Shutdown-generated ERCs must be
applied for within a short window after shutdown. The supply of cheap reductions in a given airshed is
finite and gets used up as the airshed cleans up. Whoever locks up the cheap reductions first owns the
supply curve.

**Ceiling, with numbers.**
- **Texas prices.** NOx ERCs traded at $120-150k per ton and VOC at about $150k per ton (Texas, January
  2020, [EDGE ES](https://edge-es.com/?p=228)).
- **Contrast.** The San Joaquin Valley averaged only about $12.8k per ton in 2026 ([SJVAPCD ERC cost
  2026](https://apps.valleyair.org/busind/pto/erc/ERCCost2026.pdf)), so prices vary hugely by area.
- **Rough demand.** One GW of controlled gas generation emits about 150-300 tpy of NOx. At a 1.3-1.5x
  ratio, 10 GW of new gas in nonattainment areas needs about 2,000-4,500 tpy of ERCs, worth about
  $0.3-0.7B at $150k per ton.
- **Total.** Adding VOC for LNG and petrochemicals and other airsheds gives a stock value of perhaps
  $0.5-1.5B.
- **Downside.** Real but probably below "credibly multi-billion". The ceiling is also capped by siting
  behaviour: data centres can move to attainment counties (Abilene is one).

**Who already does it.**
- Brokers: Element Markets (Houston; Energy Risk "Emissions House of the Year"), Evolution/Xpansiv,
  Karbone.
- Environmental consultancies (ALL4, EDGE ES) that help generators certify credits.
- Large emitters that bank their own credits.

I found no company that systematically originates ERCs at scale by buying sources to shut down, but I did
not check exhaustively. The space is not crowded with ML-driven players.

**Concrete first proof.**
1. Use the TCEQ ERC registry and DFW/HGB point-source inventories to build a list of the 50 units with the
   most creditable NOx tons per dollar.
2. Use permit filings since 2024 to estimate DFW/HGB offset demand to 2030.
3. Get three broker quotes for current clearing prices.
4. Option one retiring source.

Kill if current HGB/DFW NOx prices are below $50k per ton, or if most new data-centre gas is permitted as
synthetic-minor sources that need no offsets.

**Score: 5/10.** The claim is the best fit to the Terranox shape in this lane, but the ceiling is small.

---

## C2. Moratorium and vesting arbitrage for data-centre entitlements, with pre-announcement project detection

**Thesis.** Local governments are closing off by-right data-centre use quickly:
- GatherGov counts 1,030 jurisdictions that discussed data-centre moratoria in 2026 and 632 that took
  formal action ([CRE Daily, 16 Sep 2026](https://www.credaily.com/?p=222881)).
- Prince William County largely eliminated by-right data centres on 22 Sep 2026, with a **90-day grace
  window** to file.
- Loudoun is pausing applications and **may strip the grandfathering it granted in 2025** ([McGuireWoods,
  Sep 2026](https://www.mcguirewoods.com/client-resources/alerts/2026/9/virginia-data-centers-fast-changing-landscape-what-developers-need-to-know/)).

Land that holds a vested by-right entitlement just before a door shuts is worth far more:
- Northern Virginia entitled land sells for about $4M per acre and powered land for at least $6M.
- Sites on 230/500 kV lines trade at 2.4x those on 138 kV or less.
- Land worth $10k per acre without a power path can reach six figures with one.
- US data-centre land buying was about $6B in H1 2026 ([TechTarget/Avison Young/Altus](https://www.techtarget.com/it-infrastructure/news/366651918/AI-data-center-land-buying-hits-6B-as-power-premiums-rise)).

The play is to predict which jurisdictions will tighten next and which parcels are feasible there, then
option those parcels and file to vest before the change. Texas Local Government Code Ch. 245, which
freezes rules at the first permit application, is the strongest vesting regime of this kind.

**Public datasets.**
- Municipal agendas, minutes and video (public under open-meetings laws; Legistar and Granicus).
- Zoning codes (Municode).
- Permit and site-plan filings.
- Utility large-load and IRP filings.
- State DEQ generator air permits.
- USACE Section 404 public notices.
- FAA OE/AAA filings.
- Deed transfers to new LLCs.
- State economic-development board agendas, which list codename projects.

**The ML problem.**
- Predict, per jurisdiction, the probability and timing of a moratorium or loss of by-right use, from
  meeting text, petitions, election cycles and nearby-project shocks.
- Predict parcel-level feasibility from voltage proximity, water, flood, fibre and parcel geometry.
- Detect codename megaprojects before announcement by fusing weak signals across filings.

**What the company owns.** Options on land plus vested entitlements (approved site plans, or filed
applications in Texas).

**Why it might be defensible, and why it largely is not.**
- A vested right attaches to the parcel and cannot be re-created after the rule changes, which is a real
  first-come claim.
- But the edge is thin. GatherGov already sells moratorium tracking from meeting text. BuildCentral, Epoch
  AI and SemiAnalysis track data-centre permits.
- **Tract** controls more than 25,000 acres of pre-entitled sites ([DCF, Aug 2025](https://www.datacenterfrontier.com/site-selection/article/55308975/scaling-up-tracts-master-planned-land-and-infrastructure-approach-to-data-center-development)).
  **Cloverleaf** raised $300M for powered sites. Hyperscalers buy directly.
- Legal risk: Loudoun shows that grandfathering can be revoked.
- Political risk: the company would be seen as gaming democratic pauses, which invites retroactive rules.

**Ceiling.** In principle multi-billion: 2,000 vested acres at $1-2M per acre of uplift is $2-4B. In
practice it is competed down by well-funded incumbents.

**Who already does it.** Tract, Cloverleaf, Prometheus Hyperscale, EdgeCore, many land brokers and local
speculators, and the hyperscalers' own land teams.

**First proof.** Backtest: would meeting-text signals have flagged Prince William, Loudoun and the 34 North
Carolina jurisdictions 3-6 months ahead? Then measure the land-price gap between vested and unvested
parcels before and after each change.

**Score: 4/10.** Crowded, and the legal and political ground is moving.

---

## C3. Rule-change land promotion: UK grey belt and US state by-right upzoning, using ML on appeal decisions

**Thesis.** Planning or zoning permission is the largest value-creating licence in the built world:
- English landowners captured about **£13bn a year** of pre-tax uplift from planning permission (2016/17,
  [Planning Resource](https://www.planningresource.co.uk/article/1493303/landowners-made-13bn-pre-tax-profits-2016-17-planning-permission-value-rises-report-claims)).
- Agricultural land at about £20-25k per hectare becomes residential land worth several £M per hectare in
  the South East.

New rules have opened a time-limited land rush:
- **UK:** the 2024 NPPF "grey belt" policy, and the London Plan grey-belt opening for data centres
  ([Computing, 2026](https://www.computing.co.uk/news/2026/datacentre/london-plan-backs-greener-datacentres)).
- **US:** state preemption laws such as CA SB 79 (transit upzoning, 2025), TX SB 840 (by-right housing on
  commercial land, 2025), and the WA and MT middle-housing laws.

The company options land at existing-use value, wins permission, and sells to housebuilders or
data-centre developers.

**Public datasets.**
- Planning Inspectorate appeal decisions (full text, published by law). Tens of thousands of these
  include the new grey-belt reasoning.
- Local planning application registers.
- Green Belt GIS boundaries; HM Land Registry INSPIRE polygons and price-paid data.
- OS open data; Environment Agency flood maps.
- Housing delivery test and 5-year land supply statements (public; a council failing them triggers the
  "tilted balance").
- In the US: zoning GIS, transit stop data (GTFS) and assessor rolls.

**The ML problem.** Predict, per parcel, the probability of permission (including on appeal) and the time
it takes. Inputs are the free text of appeal decisions, how inspectors interpret "grey belt", the
council's land-supply position, and parcel features. For the US laws, model which parcels newly qualify
and which pencil out financially. This is genuine text and geospatial inference.

**What the company owns.** Exclusive option or promotion agreements, then the permissioned land (or a
share of the sale).

**Rivalrous?** Partly. The option is exclusive per parcel, and the grey-belt window is a first-mover
rush. Permission itself is not first-come.

**Who already does it.**
- A mature promoter industry: Gladman, Catesby, Richborough, Hallam, Barwood, Wavensmere, and the
  housebuilders' strategic land arms.
- Data tools (LandTech/LandInsight, Searchland, Nimbus) sell grey-belt site-finding to all of them
  ([LandTech](https://land.tech/blog/identify-grey-belt-with-confidence)).
- US developers and Cover, Deepblocks and Zoneomics on the US side.

ML on appeal text is a modest but real edge over consultants.

**Ceiling.** Set by the asset. Even 1% of England's planning uplift is about £130M a year. A promoter
with 5,000 consented plots at £30-60k uplift per plot holds roughly £150-300M. Getting to "multi-billion"
needs national scale, which Gladman-type players already have.

**First proof.** Train on PINS appeal decisions since December 2024 that mention grey belt. Show
out-of-sample AUC well above a planning consultant's base rate, then secure 3 options in councils without
a 5-year land supply.

**Score: 5/10.** The ceiling and data are real, the right is not first-come, and the field is crowded.

---

## C4. Northeast waste disposal capacity: rail-served transfer permits and landfill expansion airspace

**Thesis.** The Northeast disposed of about 33.6M tons of waste in 2024:
- 23% of it went to landfills that may close within five years;
- about 12M tons (26%) were already exported;
- a new landfill takes 5-7 years to permit and an incinerator about 10.

([Waste Dive on NEWMOA, May 2026](https://wastedive.com/news/newmoa-significant-waste-disposal-capacity-loss-northeast/820326/))

Even if Juniper Ridge and Seneca Meadows expand, about 5.2M tons would still lack a home. Permitted
airspace, and rail-served transfer stations in the sending states, are exclusive and in practice
impossible to re-create.

**Public datasets.**
- EPA LMOP landfill database (design capacity, waste in place, closure year).
- GHGRP Subpart HH (annual landfill reporting, mandatory).
- State solid-waste annual capacity reports (PA DEP, NY DEC, MassDEP, NJ DEP).
- USGS 3DEP LiDAR, to measure actual remaining airspace against the permitted footprint.
- STB rail data.
- Municipal budgets (to spot distressed municipal landfills).

**The ML problem.**
- Estimate true remaining airspace and expansion potential for each of about 2,600 landfills by fusing
  LiDAR with permit footprints and GHGRP inflows.
- Predict regional capacity gaps and tipping-fee trajectories.
- Score which municipal or small private landfills, or rail-adjacent industrial parcels, could be
  permitted for expansion or transfer.

**What the company owns.** Permitted landfill airspace, transfer and rail-load permits, and the land.

**Why it is defensible.** Siting a new landfill is close to impossible because of NIMBY opposition, so
permitted airspace is a local natural monopoly. That is why WM, Republic and Waste Connections trade at
premium multiples.

**Ceiling.** One permitted regional landfill is worth $100M to $1B or more. The exported 12M tons a year,
at a $40-80 per ton disposal margin, is $0.5-1B a year of margin.

**Who already does it.** Heavily crowded: WM, Republic, Waste Connections (Arrowhead, rail volumes up
300%), GFL, Casella (McKean), WIN Waste (5Mt a year by rail), IWS (Apex), Big Sky, and the PE firm
Terramont ([Waste Dive, Sep 2026](https://www.wastedive.com/news/northeast-disposal-capacity-waste-rail-investments/829739/)).
The majors already know every landfill in their territory, so an information edge is unlikely to beat
their capital and relationships.

**First proof.** Use LiDAR and GHGRP to estimate airspace at 20 Northeast or Ohio/PA municipal
landfills, then compare with each one's stated remaining life. If the model finds at least 3 landfills
whose stated life is understated by 30% or more, and that can be bought, there is an edge.

**Score: 4/10.** The asset is real; the edge and freedom to operate are weak.

---

## Killed in this lane (do not re-pitch)

| Idea | Why it is dead |
|---|---|
| Cell-tower ground leases / build-to-suit | Landmark Dividend (DigitalBridge), Radius Global (taken private by EQT in 2023 for about $3B), Vertical Bridge, TowerPoint, Unison, plus AMT/CCI/SBAC. Fully arbitraged. |
| Billboard permits (state DOT spacing rules make them rivalrous) | Total ceiling is small, and Lamar, Outfront and Clear Channel already file on new corridors. |
| Liquor licences (NJ/PA/MA quotas, FL quota lottery) | The licence pool is worth sub-$1B per state. FL allocates new licences by lottery, not first-come. |
| Cannabis licences | Values collapsed. |
| Taxi medallions | Collapsed. |
| Pharmacy licences (distance and population rules in ES/FR/DE/AT/AU) | Rivalrous, but only pharmacists may own them. |
| Broadcast licences (LPFM/LPTV) | Low value; filing windows only. |
| Airport slots, port berths | Grandfathered to airlines and handed out by tender; a startup cannot hold them. |
| Telecom pole attachments | Regulated, non-exclusive access rights. |
| NEVI/AFIR EV charging sites | Competitive grants and tenders, crowded (Tesla, Electrify America, IONNA, bp pulse, Ionity). |
| Hospital/nursing CON | Comparative review against need formulas the state publishes; the holder must operate the facility. |
| LIHTC 9% credits | Allocated by competitive QAP points; thousands of developers. |
| Casino licences | Statutory competitive awards. |
| Texas water/sewer CCN territory | Landowners with 25+ acres can opt out by streamlined decertification ([Lloyd Gosselink](https://www.lglawfirm.com/reflections-and-considerations-regarding-the-streamlined-expedited-decertification-process)); consolidators are active. |
| Powered land and large-load queue positions | Tract, Cloverleaf, Prometheus, EdgeCore, hyperscalers. Also overlaps the energy lane. |
| Aggregate and quarry permits | Vulcan, Martin Marietta, CRH and Heidelberg hold decades of permitted reserves near metros, and the work borders on banned prospecting. |
| Arizona assured-water certificates and long-term storage credits | Real scarcity, but this belongs to the water lane; developers and Howard Hughes/Teravalis are active. Not investigated here. |
