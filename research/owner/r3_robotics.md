# Round 3 lane: robotics and machines that own the value they harvest

Written 15 Oct 2026. Search budget: 18 of 20 WebSearch calls, all spent on prior art and crowding checks,
plus a few page fetches. No government datasets were downloaded. GitHub's REST search is blocked from
this sandbox, but the GitHub MCP search works, and I used it to find the dataset mirrors named below.
Scores are out of 10 against the four-part law in ROUND2.md.

## Bottom line

Nothing in this lane reaches Terranox grade. The best three score 4/10. The reason is structural and
is worth stating once:

- **Valuable stranded material always has a legal owner.** Telcos own their copper. Cable consortia
  own their dead subsea cable. Landfill owners own the airspace. Insurers own wreck cargo. So the
  "claim" is a negotiated purchase or a service contract, not a first-come filing. The owner can run a
  tender, and does: BT's copper went to EMR for £105m.
- **Truly ownerless material is ownerless for a reason.** Getting it out costs more than it is worth.
  Robots would have to cut extraction cost several-fold. Public data can locate the material, but it
  confers no right to it, and anyone with the same robot can follow.
- **Wherever buying the asset and automating it does work, a well-funded owner already holds the
  position.** FTAI in engine part-out, AMP in owned sorting facilities, Isembard and Re:Build in
  factories, Holtec, NorthStar and EnergySolutions in shut-down nuclear plants.

The pattern from round 3 holds here too. Where the claim is exclusive, it is already priced. Where the
data is illegible, the claim is not exclusive.

| # | Candidate | Score |
|---|-----------|-------|
| 1 | Landfill airspace reclamation by robotic landfill mining | 4 |
| 2 | Buying US telco copper in place, prioritised from FCC retirement notices | 4 |
| 3 | Buying underperforming solar and wind plants and fixing them with robotic O&M | 4 |
| 4 | Recovering out-of-service subsea cable | 3 |
| 5 | Salvaging modern abandoned wrecks (salvor-in-possession, a first-come regime) | 2.5 |
| 6 | Engine and aircraft part-out, timed from ADS-B and FAA registry data | 2 |
| 7 | Robotic e-waste and data-centre hardware recovery | 2 |
| 8 | Robotic shipbreaking, buying ships flagged by AIS and Equasis | 2 |
| 9 | Buying idle factories (ECHO, TRI, WARN data) and automating them | 2 |
| 10 | Owned MRF or C&D sorting plants, sited from demolition-permit data | 1.5 |
| 11 | Robotic deconstruction for reclaimed lumber | 2 |
| 12 | Owning shut-down nuclear plants and their decommissioning trusts | killed (owned) |

---

## 1. Landfill airspace reclamation by robotic landfill mining. 4/10

**Idea.** Dig up old, unlined cells or closed municipal dumps. Run the excavated material through
robotic sorting to recover ferrous metal, aluminium, copper and soil. Re-landfill the residue into a
lined cell. The product that pays is **reclaimed permitted airspace**, sold at tip fees. Metals are a
by-product.

**Datasets, and why they are public**
- EPA LMOP landfill database: about 2,600 landfills, with design capacity, waste in place, and
  opening and closure years. EPA publishes it under its voluntary methane programme.
- GHGRP Subpart HH: mandatory annual reporting of landfill methane, which also gives waste-in-place
  history.
- State solid-waste permit files and closed-landfill inventories.
- Historical aerial imagery (USGS EarthExplorer, NAIP). Waste era tells you composition. Aluminium
  cans start appearing in volume after about 1970.
- EPA "Facts and Figures" MSW composition series, 1960 to 2018.
- Mirrors: `silkieMoth/american_landfills` (LMOP, updated 2026) and `wiljnich/lmop-data` (LMOP plus
  GHGRP, 2019).

**ML problem.** For each site, estimate:
- the volume that can be mined and the density gain;
- the share of recoverable metal, inferred from era, source communities and whether incinerator ash
  was co-disposed;
- whether a permit to re-landfill is possible;
- the local tip-fee trajectory.

The inputs are sparse and multimodal (permits, imagery and methane series) and there are no labels.
Only about a dozen US projects have been dug, which gives a training set of almost nothing.

**What is owned.** Only the airspace, and only if you own the landfill or the permit. You do not get
it by digging someone else's site.

**Rivalry.** None from a public claim. Rights come from buying the landfill or signing an operating
contract. The sellers are counties, which use public procurement.

**Ceiling.**
- Perdido, Escambia County FL: mining and processing cost $2.7M, plus $3M to build new space, and the
  resulting 2.8M cubic yards of airspace is expected to earn $60M in hauler fees. That is at least a
  fivefold return.
- The metals alone do not pay. "Resource recovery alone can't justify these projects financially"
  (Joakim Krook). Denton TX cancelled its 30-acre project.
- About 16.7Mt of aluminium went to US landfills between 1960 and 2018 (EPA, via AIChE 2025). Phinix
  claims 90Mt, which I treat as unverified.
- Per site, the value is $50-500M of airspace in tight markets such as the Northeast. Nationally it is
  several billion, but only by rolling up landfills, which is what Waste Management, Republic and
  Waste Connections already do.

**Who already does it.**
- Covanta (now Reworld) and TARTECH have run a JV mining metals out of monofilled incinerator ash in
  Massachusetts since 2013. The richest stream, ash, is taken.
- Ecomaine dug an ash pile for about $216 per tonne of recovered value against $158 per tonne cost.
- The majors know their own airspace. lane_built C4 already found that an information edge does not
  beat them.
- Group Machiels' Remo project in Belgium (EU ELFM) has stalled. This is from my own knowledge and is
  unverified for 2026.

**Why 4.** It is a real "harvest the unreachable" story and robots plus ML would cut sorting cost. But
the value is airspace, which only landfill owners can capture. There is no first-come claim.

**First proof.** Join LMOP, GHGRP HH and state closure dates. Rank closed, unlined municipal sites
that sit within 30 miles of a landfill closing within 5 years (lane_built C4). Price the airspace at
state tip fees. Check whether 3 or more counties have sites where the Perdido-style ROI is above 3x
and the county is seeking closure relief.

---

## 2. Buying US telco copper in place. 4/10

**Idea.** Buy title to retired copper plant from second-tier ILECs (Lumen, Frontier, Brightspeed,
Windstream, Consolidated and about 1,000 rural LECs) before the big recyclers sign them. Pull it out
with mechanised and robotic crews. Sell the copper (and lead sheath) at roughly 30% margins.

**Datasets, and why they are public**
- FCC Part 51.325-335 network-change notices, which carriers must post publicly.
  - AT&T copper notices rose from 16 in 2019 to 494 in 2025 and 824 in 2026 (MetTel tally via the
    DataRemote Copper Retirement Bulletin, Aug 2026).
  - Lumen posts rolling 51.333 notices by wire center.
  - FCC Order 26-19 (March 2026) set a 31-day auto-approval window for discontinuance applications.
- FCC Form 477 and Broadband Data Collection: fiber overbuild by location, which shows where copper
  is stranded.
- Historical ARMIS reports (loop counts by study area).
- WSJ's 2023 lead-cable dataset.
- No GitHub mirror found. The notices are PDFs on carrier sites, which is the "illegible" part.

**ML problem.**
- Parse the notices.
- Estimate copper tonnes per wire center from historical pair counts, route miles, and whether the
  plant is aerial, in duct or buried.
- Predict recovery cost and lead liability.
- Rank carriers by tonnes per dollar.

That is a real, messy inference problem.

**What is owned.** The copper itself, once bought. Title is rivalrous, but only by contract.

**Rivalry.** Weak. The carrier chooses its buyer and runs a tender. BT's copper went to EMR for £105m.

**Ceiling.**
- TXO estimates up to 800kt of telco copper recoverable worldwide over a decade, worth more than $7B,
  at about 30% profit after costs.
- AT&T recycled more than 14,000 tons from 2021 to 2023 and runs 4 US reclamation centers.
- US share is perhaps $2-4B gross. Profit pool is under $1B. That fails the multi-billion test.

**Who already does it.** TXO (BT, with more than a dozen telcos in talks), EMR, and AT&T in-house.

**Why 4.** The data edge is real, but the asset is sold by tender, the ceiling is too small, the
supply ends once retirement is done, and the lead-sheath liability is a tail risk.

**First proof.** Scrape 2025-26 Lumen and Frontier 51.333 notices. Estimate tonnes per wire center.
Ask two rural LECs what they would sell retired cable for.

---

## 3. Buying underperforming solar and wind plants and fixing them with robotic O&M. 4/10

**Idea.** Find plants whose output is well below what their resource should give, and where the
shortfall is fixable: string outages, inverter faults, broken trackers, soiling, vegetation. Buy them
at a price set by their trailing output. Fix them with robotic O&M:
- cleaning and vegetation robots;
- blade-repair crawlers such as Aerones and Rope Robotics;
- module-swap robots such as AES Maximo and Nextracker's 2025 robotics unit.

Keep the uplift.

**Datasets, and why they are public**
- EIA-923 monthly generation and EIA-860 plant specs, both mandatory.
- NREL NSRDB irradiance and wind reanalysis data.
- Sentinel-2 and NAIP imagery, which shows soiling, vegetation and dead rows.
- Mirrors: PUDL (catalyst-cooperative), `isciences/eia923`.

**ML problem.** Model expected generation for each plant from its resource and specs. Then split the
gap into causes that are fixable and causes that are structural (degradation, curtailment, clipping).
This is noisy and hard because curtailment is not reported.

**What is owned.** The plant. Ownership is fully exclusive.

**Rivalry.** Low. These are negotiated M&A deals, and any bidder sees SCADA data in the data room. The
public-data edge only helps you find sellers.

**Ceiling.**
- Raycatch found 5.27% recoverable energy across 1.2 GW (75 plants). That is about $160k a year per
  16 MW plant, and it extrapolated to about $14.5B a year of lost output globally by 2024.
- On a cheap buy that is a fine return. As an edge it is a few percent of value, and asset prices are
  set by funds.

**Who already does it.**
- PivotGen and ACEN buy and repower older Texas wind plants.
- Clearway, Hull Street and Onward buy legacy assets.
- Raycatch, Raptor Maps, Zeitview and Nextracker sell the diagnosis.

**Why 4.** It owns the asset and the ceiling is asset-sized, but the information edge is thin and
disappears in due diligence.

**First proof.** Use PUDL with NSRDB to rank the bottom decile of US plants from 5 to 100 MW by
generation versus expected. Look at imagery to judge which ones are fixable. Check sale prices of any
that traded in 2023-25.

---

## 4. Recovering out-of-service subsea cable. 3/10

**Data and ML.** Cable route data (TeleGeography, ICPC, NOAA ENC cable areas) plus the age and type of
each cable, used to predict its copper and steel content and the cost to recover it.

**What is owned.** The cable, bought from the consortium. Cables are not abandoned in law: title
persists.

**Who already does it.**
- Oceanic Environmental Cables (OEC) signed with Sparkle in 2025 to acquire and recover more than
  22,000 km of its unused cable.
- Mertech Marine is PE-backed by Metier and has recovered cables such as Bermuda-US-1 and TAT-8.

**Ceiling.** Per-km value is low (some copper, mostly steel and polyethylene). The global pool is
around $1-3B gross; that figure is my estimate and unverified. The niche is held and the ceiling is
small.

---

## 5. Salvaging modern abandoned wrecks. 2.5/10

**Why look at it.** Admiralty "salvor in possession" and the law of finds are a genuinely first-come
regime outside geology, which is what ROUND2 asked for.

**Data and ML.** NOAA AWOIS and ENC wreck records (mirror: `jalbertbowden/AWOIS-data`), plus Lloyd's
casualty lists, plus AIS last-known positions. ML would rank wrecks by cargo value against the cost
of autonomous recovery.

**Why it fails.**
- Historic and war wrecks are excluded (the brief, the Sunken Military Craft Act and the Abandoned
  Shipwreck Act).
- Insurers keep title to most modern cargo through subrogation.
- Bunker oil is a liability, not a prize.
- The deep-water robot fleet already exists: Ocean Infinity's Armada. Odyssey Marine moved into
  seabed minerals.

**Ceiling.** Small and lumpy.

---

## 6-12. Crowded or owned (2/10 or lower)

- **Engine and aircraft part-out.** Track retirement from ADS-B (OpenSky) and the FAA registry, buy
  CFM56 and V2500 engines, and sell modules and used parts. This is exactly "buy retiring assets that
  public data reveals and harvest them". FTAI does it at a market cap of roughly $24B (BTIG $340
  target). AerSale, GA Telesis and AAR also compete. Owned.
- **E-waste and data-centre hardware.**
  - Molg runs robotic microfactories for data-centre e-waste with ABB (2026).
  - Hiro Robotics works on robotic disassembly.
  - ITRenew (Iron Mountain) and Sims Lifecycle own the reuse outcome.
  - Cyclic Materials and HyProMag own magnet recovery.
- **Robotic shipbreaking.** Leviathan has teamed with German Naval Yards to build EU green ship
  recycling. Cash buyers such as GMS already predict which ships go for demolition from AIS and
  freight data. Steel scrap margins are thin.
- **Idle factories bought and automated.**
  - Isembard raised a $50M Series A in March 2026 to open 25 AI-run aerospace and defence factories.
  - Re:Build Manufacturing acquires and automates plants. Hadrian builds new ones.
  - Idle-plant power capacity is the powered-land play already killed in round 3.
- **Owned sorting facilities.** AMP acquired RDS of Virginia's Portsmouth operations (2025, Series D
  $91M) and operates a Waste Connections MRF. The "robot company that owns the facility" model is
  already AMP's strategy.
- **Robotic deconstruction for reclaimed lumber.** Urban Machine ($14M) de-nails and reclaims lumber.
  The material is cheap, so the ceiling is small.
- **Shut-down nuclear plants.** Buy a plant together with its NRC-reported decommissioning trust,
  automate dismantling, keep any surplus, or restart the plant (as Holtec is doing with Palisades).
  This is the purest "own the asset" model in the lane. The few US units are already held by Holtec,
  NorthStar and EnergySolutions, and NRC Decommissioning Funding Status reports need no ML. Killed.

---

## What would change the verdict

A robot that cuts the cost of excavating and sorting landfills or ash by 5 to 10 times would make
unlined municipal dumps a metal resource, not just an airspace one. Even then, rights come from county
procurement, not a claim, so the defence would be cost leadership (robotics IP), not data plus
claim-staking. That is a Gecko or AMP-style robotics company, not Terranox.

## Sources
- [Mining.com/Bloomberg: buried copper worth billions to telcos](https://www.mining.com/web/buried-fortune-of-old-copper-wire-is-worth-billions-to-telcos/)
- [Total Telecom: BT £105m copper recycling deal](https://totaltele.com/bt-bags-105m-from-old-copper-cables-in-new-recycling-deal/)
- [DataRemote Copper Retirement Bulletin, Q3 2026](https://dataremote.com/resources/research/copper-retirement-bulletin.md)
- [Total Telecom: Sparkle and OEC, 22,000 km](https://totaltele.com/sparkle-signs-deal-to-recycle-22000km-of-submarine-cable/)
- [AVCA: Metier invests in Mertech Marine](https://www.avca.africa/news-insights/member-news/metier-invests-in-global-leader-in-telecommunications-cable-recovery-and-recycling-mertech-marine/)
- [NERC: why aren't we mining landfills](https://www.nerc.org/why-aren’t-we-mining-landfills)
- [AIChE 2025: landfill mining for aluminium](https://proceedings.aiche.org/conferences/aiche-annual-meeting/2025/proceeding/paper/landfill-mining-aluminum-and)
- [Phinix: landfill mining in the US](https://www.phinix.net/s/Landfill-mining-in-the-US_untappped-resources.pdf)
- [Waste Management World: Covanta JV mining ash monofill](https://waste-management-world.com/a/covanta-jv-recycling-metals-from-bottom-ash-landfill-in-massachusetts)
- [pv magazine: Raycatch $14bn solar underperformance](http://www.pv-magazine-india.com/2021/03/11/ai-identifies-a-14bn-solar-problem/)
- [NA Windpower: PivotGen and ACEN buy and repower Texas wind](https://nawindpower.com/pivotgen-acen-to-acquire-and-repower-texas-wind-farms)
- [Business Wire: Nextracker AI and robotics unit](https://www.businesswire.com/news/home/20250729097483/en/Nextracker-Launches-New-AI-and-Robotics-Business-with-Technology-Acquisitions-and-New-Executive-Appointment)
- [AMP acquires RDS Portsmouth](https://ampsortation.com/articles/amp-acquires-rds-portsmouth)
- [Offshore Energy: Leviathan and German Naval Yards](https://offshore-energy.biz/?p=600344)
- [tech.eu: Isembard $50M](https://tech.eu/2026/03/09/uk-manufacturing-startup-isembard-secures-50m/)
- [ABB and Molg robotic microfactories](https://new.abb.com/news/detail/120071/prsrl-abb-robotics-and-us-start-up-molg-tackle-data-center-e-waste-with-robotic-microfactories)
- [Yahoo Finance: FTAI BTIG $340 target](https://finance.yahoo.com/markets/stocks/articles/ftai-aviation-could-surge-43-185716052.html)
- [Urban Machine $14M](https://www.trysignalbase.com/news/funding/urban-machine-powers-a-new-era-14m-investment-fuels-robotics-startup-transforming-wood-waste-into-premium-lumber)
- GitHub mirrors: silkieMoth/american_landfills, wiljnich/lmop-data, jalbertbowden/AWOIS-data, isciences/eia923, catalyst-cooperative/pudl
