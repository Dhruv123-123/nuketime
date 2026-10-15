# Lane: energy, grid and infrastructure claims (not drilling)

Written 15 Oct 2026. I used 20 web searches plus fetches of the pages they returned. Government hosts and paywalled sources (Bloomberg, Axios Pro, The Information) were only partly readable. Anything marked [unverified] comes from my background knowledge, not from a page I fetched this run.

## Bottom line first

- **The "geostatistics over the grid" company already exists, and it is winning.** Cloverleaf Infrastructure has sold **more than 7 GW of powered land** to data-centre developers, including Wisconsin sites for Oracle and OpenAI. It claims a pipeline of more than 10 GW and took an Nvidia minority stake in Aug 2026 ([Baxtel, 21 Aug 2026](https://baxtel.com/news/nvidia-backs-data-center-powered-land-company-cloverleaf)). It was founded by Pattern, ConnectGen and Clean Line people and raised $300M of equity from NGP and Sandbrook ([Latitude, 2024](https://latitudemedia.com/news/investors-embrace-cloverleafs-energy-first-approach-to-data-centers)). Tract does the same thing at multi-GW scale (2,200-acre Reno park, a 2.4 GW Richmond park). GridCARE raised a $64M Series A in May 2026 ($77.5M total, led by Sutter Hill, with John Doerr). It "uses AI to analyze the power grid across millions of scenarios" and claims 120 GW of hidden capacity worth $350B, with a 2 GW pipeline across more than a dozen markets ([Bloomberg](https://www.bloomberg.com/news/articles/2026-05-14/early-nvidia-investor-backs-startup-to-tap-idle-grid-power), [Latitude](https://www.latitudemedia.com/news/gridcare-raises-oversubscribed-64-million-series-a/)). The capacity-map software layer is saturated:
  - Enverus bought Pearl Street (SUGAR power-flow software).
  - Wood Mackenzie bought LandGate in June 2026.
  - Paces, Nira, Orennia, interconnection.fyi, GridStatus and GridVision AI round out the field.
- **Grid capacity is no longer first-to-file.** Order 2023 cluster studies, Texas SB6 and the June 2026 FERC show-cause orders all require site control, deposits, financial security and readiness screens before a position counts. A position is won by capital plus land plus a utility relationship, not by reading data first. That breaks the Terranox "stake it, it's yours" defence.
- **"Geostatistics" is the wrong frame for deliverability.** Headroom at a bus is a deterministic power-flow result from the planning base case. You don't interpolate it from neighbouring study results. Pearl Street, Nira and GridCARE run the physics directly. The base cases are FERC Form 715 / CEII material, available under a non-disclosure agreement (NDA) and not public. ML has a real edge only on the *soft* variables:
  - which queued projects will withdraw;
  - which plants will retire;
  - which utilities move fast;
  - where local opposition will appear.
- **Best score in this lane: 6/10** (candidate 1, queue-attrition arbitrage). Nothing here meets the brief's "unattackable" test.

## Price anchors for powered land (2025-26)

| Anchor | Number | Source |
|---|---|---|
| Plug Power sold its Graham, TX site to Stream, 164 MW reference capacity | $50M base + up to $26.5M contingent, about **$0.47M/MW** (later restructured: $40M for the HV infrastructure, Aug 2026) | [TechTarget, 9 Oct 2026](https://www.techtarget.com/it-infrastructure/news/366651918/AI-data-center-land-buying-hits-6B-as-power-premiums-rise) |
| Northern Virginia: unpowered entitled land vs powered land | about $4M/acre vs at least $6M/acre (about 50% premium); campuses use 0.5-1 acre/MW, so powered land is roughly **$3-12M/MW of land** in NoVA | Avison Young, via TechTarget |
| Secondary markets | land at about $10k/acre with no power path reaches six figures per acre once power is established (about 10-50x) | Avison Young, via TechTarget |
| Altus Group, 80 transactions | sites tied to 230/500 kV infrastructure trade at **2.4x** sites at 138 kV or lower | TechTarget |
| US data-centre land purchases | $6B in H1 2026, up 79% year on year | Avison Young Q2 2026 |
| Amazon, Ashburn (122 acres) | $427M, about $3.5M/acre | [Metro Colo Advisory, Oct 2026](https://metrocoloadvisory.com/powered-land/) |
| CBRE, pending NoVA and Northeast deals | above $8M/acre | CBRE H2 2025 |
| Value per MW of operating platforms | Aligned at about **$8M/MW** (BlackRock/Nvidia $40B deal) vs listed bitcoin miners at about $3M/MW | [The Block, Oct 2025](https://www.theblock.co/post/374754/blackrock-nvidias-40-billion-data-center-deal-values-power-sites-160-above-public-bitcoin-miners) |

Working figure: a site with a credible path to power within 18-36 months is worth about **$0.3-1.5M/MW more than raw land** outside the tier-1 hubs, and several $M/MW in NoVA.

What that implies for Cloverleaf: 7 GW at about $0.3-1M/MW is roughly **$2-7B of value created**. The ceiling clears the brief's multi-billion bar. The issue is who captures it.

## Regulatory state as of Oct 2026 (what is claimable, and how)

**FERC large-load action.** DOE sent FERC a Section 403 directive on 23 Oct 2025 covering loads above 20 MW connected to transmission: standardized deposits, readiness screens, expedited studies for curtailable load, a right to build, and 100% of upgrade costs assigned to the load. FERC did **not** issue a generic rule. On **18 Jun 2026** it sent show-cause orders to all six RTOs. Each had 30 days to report on resource adequacy and 60 days to justify its tariff or file reforms in five areas:
1. study process;
2. cost allocation and transparency;
3. co-location and behind-the-meter generation;
4. new transmission services for flexible load;
5. a study process for generators serving nearby or co-located load.

The rulemaking stays open and non-RTO utilities could be reached later ([Duane Morris](https://www.duanemorris.com/alerts/ferc_acts_advance_data_center_large_load_integration_six_rto_regions_0626.html)). Precedents already in place: FERC's December 2025 PJM co-location order and its January 2026 approval of SPP's High Impact Large Load (HILL) framework. Utility Dive also reports that FERC rejected most of PJM's own large-load interconnection plan.

**ERCOT / SB6.** About 438 GW of large-load requests (about 90% data centres) against an 85.5 GW all-time peak. S&P puts the queue at nearly 500 GW (Oct 2026). Batch Zero timeline:
- docs were due 10 Jul 2026;
- classifications were sent 7 Aug 2026;
- **capacity allocations arrive spring 2027**;
- proof of commitment (financial security plus site control) is due Q2 2027;
- Batch 1 opens summer 2027.

Two optional pathways exist: on-site generation can offset required transmission capacity (WLPUN), and partial curtailment buys early access (PCLR). Governor Abbott then ordered an audit of every Batch Zero project, and TCEQ paused data-centre permits ([ERCOT](https://www.ercot.com/files/docs/2026/06/18/Trending-Topics-ERCOT-s-New-Batch-Connection-Process-for-Large-Electricity-Users-v2.pdf), [S&P](https://www.spglobal.com/energy/en/technology-ai-research-insights/blogs/the-texas-data-center-boom)). ERCOT's documents do not say whether an allocation can be transferred.

**PJM replacement generation.** FERC accepted this on 29 Jan 2026 (ER26-403-001). The replacement must:
- assume the retiring unit's capacity interconnection rights (CIRs);
- be requested within 1 year of deactivation;
- be at the same substation and voltage;
- be no larger than the retiring unit's maximum output;
- be in service within about 3-4 years.

Where third parties stand is unclear from the summary ([Troutman](https://www.troutmanenergyreport.com/2026/02/ferc-accepts-pjms-replacement-generation-interconnection-process/)). Surplus interconnection service (Order 845) lets an existing interconnection customer add resources behind its own point of interconnection. Virginia and Indiana passed surplus-interconnection bills in 2026 ([Utility Dive](https://www.utilitydive.com/news/virginia-indiana-surplus-interconnection-pjm-miso-spp/813442/)).

**Hydro preliminary permits (RM26-5).** This is the one truly first-to-file energy right. DOE's 23 Oct 2025 directive asks FERC to stop denying permits solely because a tribe or federal land manager objects (the policy FERC adopted in Feb 2024). As of Oct 2025 FERC had **109 active permits totalling 55.4 GW**, mostly pumped storage, plus 21 pending applications totalling 12 GW ([Utility Dive](https://www.utilitydive.com/news/tribes-ferc-doe-preliminary-permit-hydroelectric/805387/), [FERC RM26-5](https://ferc.gov/rm26-5)). I could not confirm a final rule.

**Interconnection cost data.** LBNL study costs by status:

| Market | Completed | Active | Withdrawn |
|---|---|---|---|
| PJM | $84/kW | $240/kW | $599/kW |
| MISO | $102/kW | $156/kW | $452/kW |
| SPP | $57/kW | $106/kW | $304/kW |

Withdrawal tracks high assigned cost ([GridVision AI, quoting LBNL](https://gridvisionai.com/interconnection-queue/costs); [LBNL Queued Up 2026](https://eta-publications.lbl.gov/sites/default/files/2026-06/queued_up_2026_edition.pdf)).

---

## Candidate 1: Queue-attrition arbitrage, "where headroom will be freed next" (score 6/10)

**Datasets, and why they are public**
- ISO/RTO interconnection queues (PJM, MISO, SPP, CAISO, NYISO, ISO-NE, ERCOT GINR and the large-load list). The OATT and Order 2023 force their publication.
- Cluster study, restudy and facilities study reports, with network upgrades and $ assigned per project. Order 2023 requires posting; the one-line diagrams are CEII but the cost tables are generally public.
- The LBNL "Queued Up" project-level dataset (DOE-funded, public).
- Withdrawal notices and penalty postings.
- EIA-860/860M for existing plants, and Form 715 base cases (CEII, available under NDA).

**ML problem**
- Predict, per project, the probability of withdrawal at each Order 2023 decision point. Features include the developer's track record, assigned $/kW, readiness deposit posted, PPA and tax-credit exposure (2025 OBBBA phase-outs), parcel site control, and county moratoria.
- Then push the expected withdrawals through the cost-reallocation and restudy logic to forecast, per point of interconnection (POI), the **freed deliverable MW and the expected upgrade cost in the next cluster**. This is hard: sparse, staged, censored, with interdependent outcomes. Incumbents publish backward-looking queue statistics, not forward forecasts of where headroom will be released.

**What the company owns**
- Options on land at the 20-50 POIs where headroom is predicted to free up.
- Its own generation-plus-load hybrid positions, filed into the next cluster. This uses the co-location and generator-serving-load study paths the June 2026 orders require.
- Distressed late-stage generator projects with signed generator interconnection agreements (GIAs), bought before the market prices the data-centre conversion. A GIA travels with the project on assignment.
- The exit: sell energized or "agreement-signed" sites to hyperscalers and developers. The power ladder (load request, will-serve letter, study done, agreement signed, energized) puts most of the premium at the signed-agreement rung.

**Rivalrous / defensible?**
- Partly. A POI's headroom goes to whoever is next in the cluster with site control. The land option near that substation is exclusive.
- But the advantage is a forecasting lead of one or two cluster cycles, not a perpetual claim. Developers with deep pockets (NextEra, Invenergy, Cloverleaf, Tract) watch the same queues.
- Withdrawal penalties and readiness deposits make the bets cost real capital: roughly $5-10M at risk per position in PJM and MISO [unverified magnitude].

**Ceiling**
- Each GW of signed-agreement powered land sells for about $0.3-1.5M/MW over raw land outside tier-1 hubs, so **$0.3-1.5B per GW**.
- Cloverleaf's 7 GW shows the market will absorb several GW per firm, so a credible ceiling is **$2-5B** of site value over 5 years.

**Who already does it**
- Cloverleaf, Tract, GridCARE, Lancium/Crusoe, Prometheus Hyperscale, EdgeCore, LandBridge (in the Permian, with NRG and PowerBridge).
- Bitcoin miners such as Cipher, Hut 8 and IREN, who converted their sites.
- The big IPPs (Talen, Constellation, Vistra).
- None publicly markets forward withdrawal forecasting as the core edge, but Enverus/Pearl Street and Paces are a feature release away.

**First proof (8 weeks, under $100k)**
1. Backtest on MISO DPP cycles 2019-2022 and PJM transition cycles. Using only the data posted before decision point 2, predict which projects withdrew and how the restudy changed the remaining projects' $/kW at each POI.
2. Kill it if the model can't beat a naive "withdraw if $/kW > X" rule by a clear margin on area under the curve (AUC) and on predicted freed MW.
3. If it does, name 10 live POIs in MISO and SPP with more than 300 MW of predicted freed headroom.
4. Pull parcels at each (Regrid or county records), and get two hyperscaler or developer LOIs at a stated $/MW for agreement-signed sites before buying a single option.

---

## Candidate 2: ERCOT Batch Zero fallout map, Texas-specific and time-boxed (score 5/10)

**Datasets**
- ERCOT large-load interconnection status reports and the Regional Planning Group (RPG) project list. ERCOT posts these; SB6 added transparency requirements.
- ERCOT GINR queue, the CDR, and TCEQ permit filings (public under Texas law).
- County appraisal-district parcels.
- Batch Zero classifications (sent Aug 2026) and allocations (spring 2027). Per-project detail may be partly confidential [unverified].

**ML problem**
- Nearly 500 GW of requests compete for perhaps 20-30 GW of realistic headroom by 2030.
- The task: predict which Batch Zero "studied load" projects will fail to post financial security and site control by the Q2 2027 commitment deadline, and where that frees allocated capacity.
- Second task: score substations for the PCLR (curtailable) and WLPUN (on-site generation offset) pathways. That means joining gas-pipeline proximity, firm capacity and the constraint profile.

**What the company owns**
- Land options plus a Batch 1 application (summer 2027) at substations where Batch Zero capacity is likely to be freed.
- A self-supplied behind-the-meter gas or battery design that qualifies under WLPUN or PCLR.
- The exit: sell sites to developers at the allocated-capacity rung.

**Rivalrous / defensible?** Batch allocations are exclusive per site, but transferability is not documented. Politics are risky: the Abbott audit, the TCEQ permit pause, and senators pushing to repeal tax breaks. The window is about 12 months.

**Ceiling** About 1-3 GW captured at about $0.3-0.5M/MW (the Plug/Stream Texas comp is $0.47M/MW), so **$0.3-1.5B**. Below the brief's bar on its own; better as the first market for Candidate 1.

**Who already does it** Lancium, Crusoe, Cipher, LandBridge, Fermi America, Prometheus, and every Texas powered-land broker. It is crowded.

**First proof** Take the ERCOT large-load list as posted and score each project's survival odds from developer funding, site-control evidence, TCEQ filings and press. Publish a private prediction before the spring 2027 allocations and check it against the outcome. Cost: about $30k.

---

## Candidate 3: Retiring-plant interconnection rights ("brownfield headroom") (score 4/10)

**Datasets**
- EIA-860 / 860M, which lists planned retirements by unit (federal statistical law).
- EIA-923 generation, which gives capacity factor and surplus headroom at the POI.
- PJM, MISO and SPP deactivation request lists (tariff-mandated posting).
- EPA eGRID/CAMPD hourly emissions and load.
- FERC Form 1 for utility-owned plants.

**ML problem**
- Predict retirement 2-5 years before announcement from heat rate, age, capacity-market clears, environmental-rule exposure and owner balance sheet.
- Estimate usable surplus interconnection (nameplate minus actual output profile).
- Rank sites by land, water, fibre and gas access.

**What the company owns**
- **Nothing it can claim unilaterally.** The CIRs and surplus interconnection belong to the plant owner. In PJM the replacement window closes 1 year after deactivation, at the same substation.
- The company would have to buy or joint-venture (JV) the plant or site before the owner reprices it.

**Defensibility** Low. Owners now know these rights are the most valuable thing they hold. Coal-to-data-centre conversion is public strategy: PNNL's coal-to-data-centre study, GridLab, Homer City, Talen, Vistra, Constellation, plus federal and state surplus-interconnection bills.

**Ceiling** US coal retirements are large, tens of GW over a decade [EIA, unverified exact figure], at $1-3M/MW for an energized brownfield. Still multi-billion, but the value accrues to plant owners and the large IPPs.

**Who already does it** IPPs, utilities, Energy Capital Partners, Homer City Redevelopment, Fermi, and many PE funds.

**First proof** Build a model of retirement announcements before they happen from 2015-2022 EIA data and backtest it on 2023-2026 announcements. It is only worth anything if it surfaces small, municipal or co-op units (50-300 MW) that the big funds ignore and that will sell cheaply.

---

## Candidate 4: Hydro preliminary permits at non-powered dams and pumped-storage sites (score 3/10)

**Datasets**
- The National Inventory of Dams (USACE, public by statute).
- ORNL's Non-Powered Dam assessment (DOE public research): about 12 GW of potential, heavily concentrated at USACE locks and dams [from my knowledge of the 2012 study].
- USGS streamflow and the ANU global pumped-hydro atlas.
- The FERC eLibrary of active permits.

**ML problem** Head, flow and economic scoring at every NID dam, with a market-access layer for nearby large-load substations. This is modest ML. The site-finding is largely solved already (ORNL, the ANU atlas).

**What the company owns** A true **first-to-file** FERC preliminary permit: up to 4 years, extendable, giving priority for the licence. It is cheap and exclusive. This is the cleanest "claim" in energy.

**Why it still fails**
1. The priority is real, but non-powered-dam projects are small (mostly under 50 MW) and take 5-10 years to license. Data centres need GWs within 18-36 months.
2. The good sites are already claimed: Rye Development and Free Flow Power filed hundreds of permits in the 2010s [background knowledge], and 55.4 GW of active permits exist, mostly pumped storage.
3. A permit gives priority, not a right to build. Pumped storage costs over $2,000/kW and is hard to finance.
4. RM26-5 could reopen tribal and federal-land sites, but that is contested.

**Ceiling** Speculative permit flipping is worth tens of $M, not billions.

**First proof** Join NID with FERC active permits and filter non-powered dams with more than 10 MW of potential within 10 miles of a 230 kV+ substation. If fewer than about 30 unclaimed sites remain, kill it.

---

## Candidate 5 (killed in triage): other claimable energy rights

- **Offshore and onshore wind or solar lease rounds.** BOEM offshore wind lease activity was halted and lease areas were rescinded in 2025. BLM renewable rights-of-way are deprioritized. The leases are claimable, but the policy direction is against them.
- **Transmission rights-of-way.** Held by utilities, with eminent domain. A private company can't claim them first.
- **Utility hosting-capacity maps.** Distribution-level, mostly under 20 MW. Low value per site, and LandGate/WoodMac and Paces already ingest them.
- **Firm gas-pipeline capacity.** FERC Index of Customers and the capacity-release postings are public. Firm capacity is valuable for behind-the-meter data-centre generation, but it is released and recalled under a tariff, pre-arranged deals dominate, and it is close to the banned gas lane.

---

## Verdict for the owner hunt

The energy lane has the right *shape*: a public dataset, a scarce right, and an asset worth $0.3-8M/MW. Cloverleaf proves the model works at 7 GW and Nvidia-backed scale. But it fails the brief on two counts:

1. **Not first-to-file.** Grid rights now go to whoever posts capital, site control and readiness. Reading data first is not enough.
2. **Crowded.** At least six well-funded firms already own the powered-land position, and the analytics layer has been consolidated by Enverus and Wood Mackenzie.

The only defensible ML wedge is **forward prediction of queue attrition and freed headroom** (Candidate 1). A clever newcomer could win a few GW with it, but it is not unattackable. I recommend it only as a fallback, or as a feature of a broader land-option strategy, not as the hunt's answer.
