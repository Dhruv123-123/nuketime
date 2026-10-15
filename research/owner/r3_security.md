# Round 3 lane: security technology (cyber, supply chain, physical and critical-infrastructure security)

Written 15 Oct 2026. I used 20 WebSearch calls plus fetches of the pages they returned. Government hosts were not fetched. Anything marked [unverified] comes from my background knowledge, not from a page I read this run.

## Bottom line first

- **Thesis 1, law-forced replacement, mostly fails the Terranox test, because almost every Covered List action is prospective.**
  - Drones (Dec 2025), consumer Wi-Fi routers (23 Mar 2026), and power inverters plus advanced robotics (28 Jul 2026) only block **new equipment authorizations**.
  - Installed devices stay legal. Previously authorized models can still be sold. Inverters even keep firmware updates until at least 1 Jan 2029 ([Troutman](https://www.troutman.com/insights/grid-lockout-fcc-bars-foreign-produced-power-inverters-from-the-us-market/), [DWT](https://www.dwt.com/blogs/broadband-advisor/2026/09/fcc-covered-list-power-inverters-update), [ComSoc on routers](https://techblog.comsoc.org/category/wifi-routers/), [DroneLife](https://dronelife.com/2025/12/29/fcc-foreign-drone-rule-market-impact/)).
  - So there is usually no installed base the law forces out, and therefore nothing that mapping it with ML would let a company claim. The real effect is a shift in new sales, and product companies already capture it: BRINC and Skydio in drones, Netgear and eero in routers, US inverter assemblers.
  - Two regimes do reach installed equipment:
    - **Rip-and-replace.** It is funded and run by Ericsson, Nokia and Mavenir, and 53 of 126 projects were done by June 2026 ([Broadband Breakfast](https://broadbandbreakfast.com/nearly-half-of-rip-and-replace-projects-done-fcc-tells-congress/)).
    - **Executive Order 14420 (26 Aug 2026).** It declares a national emergency over foreign-produced bulk-power equipment and *can* reach equipment already in service, but no replacement mandate has been issued yet ([DWT](https://www.dwt.com/blogs/broadband-advisor/2026/09/fcc-covered-list-power-inverters-update)).
  - None of these regimes gives a first-come exclusive claim. Winning is a matter of selling a product.
- **Thesis 2, end-of-life software, is real but crowded, and it is a services market.**
  - HeroDevs took $125M from PSG in Jul 2025 and has 1,000+ customers, about a third of them in the Fortune 100 ([Utah Business](https://www.utahbusiness.com/entrepreneurship/2025/07/24/herodevs-secures-125-million-from-psg/)).
  - Chainguard is valued at $3.5B after a $356M Series D ([Verdict](https://www.verdict.co.uk/cybersecurity-chainguard-356m-valuation/)).
  - Other players: TuxCare, Canonical ESM, Rimini Street, Spinnaker, and Tidelift (bought by Sonar) [unverified for the last two].
  - The only *exclusive* version is buying the abandoned product's IP. For operational-technology (OT) and industrial-control (ICS) products, that is the Constellation Software / Rochester Electronics model applied to orphaned industrial software. It scores 5/10, the best in this lane.
- **Thesis 3, AI vulnerability discovery where the company owns the outcome, has nothing to own.**
  - XBOW is valued at more than $1B after a $120M Series C in Mar 2026 ([BusinessWire](https://www.businesswire.com/news/home/20260318258057/en/XBOW-Raises-$120M-to-Scale-its-Autonomous-Hacker)).
  - All seven DARPA AIxCC finalist systems were open-sourced, and they found 18 real vulnerabilities at about $152 per task ([DARPA](https://www.darpa.mil/news/2025/aixcc-results)).
  - Bounties are first-come, since the first reporter wins, but the pool is under $0.1B a year. Exclusive remediation rights do not exist as a legal form. 2/10.
- **Thesis 4, being first to claim something public.** One thing is genuinely Terranox-shaped: **dormant legacy IPv4 blocks held by defunct companies**.
  - **Data:** public WHOIS and routing (BGP) data, joined to corporate-registry and bankruptcy records by ML entity resolution.
  - **Claim:** the first buyer to sign the legal successor gets the block.
  - **Asset value:** about $20 per address.
  - **What holds it back:** prices fell from about $60 in 2021 to about $20 in 2026, brokers such as IPv4.Global/Hilco ($500M brokered) already hunt hidden blocks, and the defunct-owner slice is probably $0.5-2B in total and shrinking. 4/10.
- Abandoned S3 buckets and domains are cheap and first-come (watchTowr re-registered about 150 buckets for $400 and received 8M requests from governments, militaries and banks). But the only legitimate value is defensive intel, so AWS sinkholed them ([watchTowr](https://labs.watchtowr.com/8-million-requests-later-we-made-the-solarwinds-supply-chain-attack-look-amateur/)). 1/10 as a business.
- **No candidate in security clears the brief's bar.** The structural reason is that security value is realised by selling to the owner of the vulnerable thing, so it sits in service markets. Ownership only appears where the asset itself is transferable: IP addresses, product IP, or hardware.

---

## 1. Law-forced replacement markets

### Regime-by-regime facts

| Regime | Date | Reaches installed base? | Forced market, rough size | Who already supplies replacements |
|---|---|---|---|---|
| Secure Networks Act rip-and-replace (Huawei/ZTE) | 2020 onward; $4.98B program, shortfall funded by FY25 NDAA via AWS-3 auction [unverified] | **Yes**, the only fully forced one | about $5B, 126 projects, 53 complete by Jun 2026 ([BB](https://broadbandbreakfast.com/nearly-half-of-rip-and-replace-projects-done-fcc-tells-congress/), [Inside Towers](https://insidetowers.com/?p=50848)) | Ericsson, Nokia, Mavenir, Samsung; tower integrators |
| NDAA §889 (Huawei, ZTE, Hikvision, Dahua, Hytera in federal contractors) | 2019-20 | Yes, but only for federal agencies and contractors | several $B in cameras and radios [unverified]; mostly done by 2026 | Axis, Motorola/Avigilon, Verkada, Hanwha |
| Covered List: all foreign drones and components | Dec 2025 | **No**, new models only | DJI held most of the US market [unverified ~70-90%]; public safety is about 18-20k agencies and 80k stations | BRINC ($125M, Jul 2026, led by Motorola; 900+ agencies; [PickDrones](https://pickdrones.com/brinc-125-million-funding-911-drones/)), Skydio, Teal/Red Cat, Parrot, Neros |
| Covered List: foreign consumer Wi-Fi routers | 23 Mar 2026 | **No** | TP-Link about 35% of US consumer routers ([ComSoc](https://techblog.comsoc.org/category/wifi-routers/)) | Netgear, eero, Starlink and ISP-supplied gear, whoever builds in the US |
| Covered List: foreign power inverters with remote comms; advanced robotics | 28 Jul 2026; definitions narrowed 20 Aug 2026 | **No**, and firmware updates allowed to at least 1 Jan 2029 | Inverters are about $0.03-0.06/W, so 50 GW of Chinese-made utility and storage inverters is about $2-3B to fully replace [unverified estimate] | 45X-eligible US assembly: Fluence, Tesla, SMA America, Power Electronics, Ingeteam, Yaskawa-Solectria, EPC Power, Enphase |
| EO 14420, bulk-power-system national emergency | 26 Aug 2026 | **Can**, but no implementing order yet | Same pool as inverters, plus transformers and control systems | Same |
| DoD 1260H list (CATL, BYD, Huawei and others), procurement ban from 2027 | Jan 2026 listing | DoD procurement only | Small | Fluence, LGES Michigan, Tesla |
| Commerce connected-vehicle rule (Jan 2025 final) | Software from model year 2027, hardware from MY2030 | No, new vehicles only | Vehicle connectivity modules and ADAS software, about $1-3B a year [unverified] | Harman, Continental, Aptiv, u-blox, Telit/Sierra |
| Cellular IoT modules (Quectel, Fibocom) | Flagged by FCC in Sep 2023; no Covered List designation confirmed ([Location Business News](https://locationbusinessnews.com/fcc-chair-says-quectel-fibocom-wireless-iot-modules-pose-national-security-risk)) | No | Hundreds of millions of US modules [unverified] | Telit, Sierra (Semtech), u-blox, Nordic |
| Port cranes (ZPMC) | Section 301 tariff (25% to 100%) on new Chinese STS cranes, 2024-26 | No | US fleet of about 200+ ZPMC STS cranes at about $10-15M each [unverified] | PACECO/Mitsui (US assembly), Konecranes, Liebherr |

### Candidate 1a: an inverter installed-base map leading to a "domestic control plane" retrofit
- **Datasets and why they are public:**
  - California DGStats interconnection data, and similar data in New York and Massachusetts, which list inverter make and model by interconnection because of state DER reporting rules [unverified field coverage].
  - The CEC Solar Equipment List and UL 1741 listings (certification).
  - The FCC Equipment Authorization (FCC ID) database, a statutory record that shows which inverter models carry radios.
  - EIA-860 and 860M for plant location and MW, but not inverter make.
  - Interconnection-queue PDFs, county permits, and import bills of lading (Panjiva and ImportGenius resell US Customs manifests, which are public under 19 CFR 103.31).
- **ML problem:** infer inverter vendor and model for every US plant above 1 MW where it is unknown. Inputs are permit text, bills of lading matched to EPC (engineering, procurement and construction contractor) and site, aerial imagery of skid and string-inverter layouts, and the date and developer. This is a real multi-modal inference problem.
- **What is owned:** a retrofit product. Candidates are a 45X-eligible US gateway or controller that cuts the foreign unit's radio path and takes over plant control, plus long-term service contracts. That product could be the main compliance answer when EO 14420 acts or when the 2029 firmware cliff hits.
- **Rivalry:** none is exclusive. Utilities and IPPs (independent power producers) buy from anyone qualified. The map is a sales list. SEL, Fortinet/Nozomi, Dragos and the inverter OEMs are natural competitors.
- **Ceiling:** about $2-3B one-time if a full replacement is mandated; about $0.2-0.5B if a gateway retrofit is accepted [unverified estimates]. It depends on a rule that does not yet exist.
- **Who already does it:** OEM retrofit programs; SEL and Schweitzer power-plant controllers; Dragos and Nozomi for visibility.
- **First proof:** pull DGStats from its GitHub mirrors if any exist (not checked), count MW by Chinese-brand inverter, and test whether bill-of-lading consignee and port-of-entry data predicts vendor for EIA-860 plants.
- **Score: 3/10.** It is a product sale that hangs on a pending rule, with no claim.

### Candidate 1b: the drone fleet transition
- **Data:** FCC ID records; public procurement (state contracts, city council agendas, GovSpend-style data); FAA Part 107 and COA records; police-department public-records responses.
- **ML problem:** build a DJI fleet census per agency.
- **What is owned:** an OEM business.
- **Rivalry and crowding:** BRINC has Motorola backing and a stated goal of 80,000 stations; Skydio is the incumbent of record. **Killed as crowded, 2/10.**

### Candidate 1c: rip-and-replace distressed-asset buy
- **Idea:** buy rural carriers that cannot finish the swap.
- **Why it dies:** the program is funded and in progress, the carriers are small, and spectrum and licences pass through FCC transfer review. **1/10.**

## 2. End-of-life software and firmware in critical infrastructure

### Candidate 2a: maintainer of record for EOL open source (the HeroDevs model)
- **Data:**
  - PyPI, npm and Maven download statistics. PyPI's BigQuery dataset is public, and these are public because registries publish them.
  - deps.dev dependency graphs; endoflife.date, which is on GitHub; CISA KEV (Known Exploited Vulnerabilities), which is on GitHub.
- **ML problem:** rank abandoned packages by transitive criticality-weighted exposure, then predict which will get a CVE.
- **What is owned:**
  - Maintainership itself, partly claimable. PyPI's PEP 541 and npm dispute processes let a requester take over an abandoned name, and this is close to first-come. The registries scrutinise such requests, though, and community trust is not transferable property.
  - Commercial support contracts.
- **Crowding:** HeroDevs ($125M PSG), Chainguard ($3.5B), TuxCare, Canonical ESM, Rimini Street, and OpenSSF/Alpha-Omega for the grants side.
- **Ceiling:** a services market. HeroDevs' revenue is undisclosed; the leaders are probably in the $100-400M ARR range [unverified]. That is exactly what the brief excludes.
- **Score: 3/10.**

### Candidate 2b: buy orphaned OT/ICS software and firmware product lines (best in lane)
- **Data:**
  - CISA ICS advisories, which are public by statute and mirrored on GitHub (cisagov CSAF repo, and the ICS Advisory Project dataset [unverified mirror names]).
  - Vendor EOL and EOS notices.
  - Shodan, Censys and Shadowserver internet-exposure counts by product banner (the exposure data is public).
  - SEC filings and press releases on vendor divestitures; distributor parts listings (Radwell, PLCCenter) that show the installed base through refurb demand.
- **ML problem:**
  - Entity-resolve product names across advisories, banners and EOL notices.
  - Estimate the installed base, including the share not exposed to the internet, from exposure counts plus refurb-parts price and volume.
  - Predict which products have a large captive base and no committed vendor.
- **What is owned:** the IP itself, bought from the vendor, a bankruptcy estate, or a carve-out. With it come exclusive support, patching and successor-hardware rights. This is the software form of Rochester Electronics, which is authorised by 70+ semiconductor OEMs to make their EOL parts [unverified count].
- **Rivalry:** buying IP is exclusive, and the first credible bidder wins a negotiated deal. It is not a public claim, though, and vendors sell to buyers they know.
- **Ceiling:** each product line is worth about $5-100M. A roll-up can compound, since Constellation Software is worth about $60B+ [unverified] from thousands of such buys. That is asset-sized only through repeated acquisitions.
- **Who already does it:**
  - Constellation/Volaris, Valsoft and Rocket Software in software.
  - Rochester Electronics in chips.
  - PLC refurbishers (Radwell) on the hardware side.
  - OEM aftermarket arms (Rockwell, Emerson, Schneider), which rarely abandon products outright.
- **First proof:** from the CISA ICS advisory mirror, list advisories from 2020-2026 where the vendor answered "EOL, no fix" or "product discontinued". Join to Shodan banner counts from public reports and return the top 30 orphaned products by exposure. Then check whether each one's IP owner is a defunct or small vendor that could be bought.
- **Score: 5/10.** It is genuinely owned, ML has a real role in finding targets, and ICS is security-critical. It is not first-come or cheap, though, and it depends on capital and M&A (mergers and acquisitions) skill more than on data.

## 3. AI vulnerability discovery where the company owns the outcome

- **State of the field:**
  - XBOW topped HackerOne in 2025 and raised $120M at more than $1B in Mar 2026. Its customers are enterprises buying continuous pentesting, which is a SaaS service.
  - AIxCC finalist systems (Team Atlanta, Trail of Bits, Theori) were open-sourced, so the capability is commoditising.
  - Google Big Sleep and the frontier labs' own agents compete at zero price for open source [unverified detail].
- **Ownable outcomes, and why each fails:**
  1. **Bounties** are first-reporter-wins, a real claim, but the pool is small (HackerOne about $80M a year [unverified]).
  2. **Selling to ZDI or other brokers** gives the same answer, with ethical limits.
  3. **Patents on fixes** are not valuable.
  4. **Exclusive remediation contracts** do not exist as a legal right.
- **Defensive framing only:** the closest "owned" version is 2a or 2b, where the company owns the maintained fork.
- **Score: 2/10.**

## 4. Other "first to claim something public" plays in security and internet infrastructure

### Candidate 4a: dormant legacy IPv4 blocks of defunct holders
- **Datasets and why they are public:**
  - RIR WHOIS and RDAP for ARIN, RIPE, APNIC, LACNIC and AFRINIC, published by registry policy.
  - BGP tables from RouteViews and RIPE RIS, open research archives. Announced space is 3.11B addresses, 84.1% of allocated, so about 590M allocated addresses are not announced ([RouteViews report, May 2025](https://lists.nsrc.org/pipermail/ren-bgp-stats-all/2025-May/101169.html)).
  - State corporate registries, SEC EDGAR M&A filings, PACER and Canadian insolvency dockets.
- **ML problem:** entity resolution from a 1980s-90s WHOIS organisation name to its current legal successor through mergers, name changes, dissolutions and bankruptcies. Then classify unannounced blocks as defunct, internally used, or reserved, using routing history, reverse-DNS, and abuse and scan data. This is messy, sparse, and multi-jurisdictional.
- **What is owned:** the block itself. The company buys it from the successor, trustee or estate, which often does not know it owns it (for example the KSV/Dylex estate recovery, page now 404), then transfers it through RIR policy and sells or leases it.
- **Rivalry:** rivalrous. The first buyer to sign the legal successor gets it. Registry transfer needs documented chain of title, which is the moat for whoever does the legal work.
- **Ceiling:** 590M unannounced addresses × about $20 is about $12B nominal ([IPregistry mid-2026](https://ipregistry.co/blog/ipv4-market-mid-2026): average $20.04, 29.7M moved in H1 2026, about 59M a year projected). Most of it is DoD, live enterprise internal use, or reserved. If 5-15% is defunct-owner space, the realisable pool is **about $0.6-1.8B one-time** [estimate].
- **Headwinds:** prices fell from about $60 (2021) to $13-24 (2026). AWS's per-IP charge is pushing hoarded space onto the market. IPv6 adoption is a slow decay.
- **Who already does it:** IPv4.Global by Hilco Streambank (48M addresses, nearly $500M brokered, offers "audits to identify unused addresses"; [Hilco](https://hilcoglobal.com/perspective/ipv4-addresses-often-a-hidden-asset-with-significant-monetization-potential/)), Brander Group, IPXO (leasing), Addrex, and insolvency practitioners. Hijackers also target the same orphaned blocks, which the security angle can help with.
- **First proof (can run here):**
  1. Pull a RIPE RIS or RouteViews RIB dump, plus ARIN bulk WHOIS. Bulk WHOIS needs an ARIN agreement, so use RDAP sampling instead.
  2. List legacy /16-/24 blocks that are unannounced and have had no WHOIS update for 10+ years.
  3. Match organisation names against OpenCorporates and EDGAR, and count blocks whose registrant is dissolved.
  4. Multiply by $20 to measure the true pool before going further.
- **Score: 4/10.** It has the right shape (cheap, first-come, public-but-illegible data, an asset worth more than the claim), but the ceiling is about $1B and falling, and brokers are already in it.

### Candidate 4b: abandoned cloud buckets, domains and package names in update paths
- **Shape:** first-come and costs dollars. watchTowr spent $400 on about 150 buckets and drew 8M requests from US, UK and other government, military, bank and Fortune 100 networks.
- **Why it fails as a business:** the only legitimate value is notifying owners and selling exposure-management SaaS. Owning the resource to exploit it is harmful, and the right outcome is a sinkhole. Registries such as PyPI and npm now protect names.
- **Score: 1/10.** It is good research, not a business.

### Candidate 4c: first to file under the CVE or certification regimes
- **Ideas:** become a CNA (CVE Numbering Authority) for an orphaned product family, or be the first lab accredited for the FCC's new Conditional Approval or "trusted" schemes.
- **Why it fails:** these are certification-lab and service-market economics (UL, TÜV, Intertek), and round 2 already covered certify-first. **2/10.**

## Scores

| # | Candidate | Score |
|---|---|---|
| 2b | Buy orphaned OT/ICS product IP, ranked by advisories + exposure + EOL data | **5** |
| 4a | Dormant legacy IPv4 of defunct holders | **4** |
| 1a | Inverter installed-base map + domestic control-plane retrofit (EO 14420 / 2029 firmware cliff) | 3 |
| 2a | EOL open-source maintainer of record | 3 |
| 1b | Drone fleet transition | 2 |
| 3 | AI vulnerability discovery, owned outcome | 2 |
| 4c | First-to-certify / CNA | 2 |
| 1c | Rip-and-replace distressed buy | 1 |
| 4b | Abandoned buckets, domains and names | 1 |

## What I could not verify
- I did not check GitHub mirror names for CISA ICS advisories or California DGStats.
- These figures are background estimates I could not confirm from a page: Chinese-inverter GW in the US, DJI's US share, Quectel's installed base, ZPMC crane counts, HackerOne payouts, and Constellation's market cap.
- The FCC and Commerce primary documents were not fetched; the sources are law-firm summaries.
