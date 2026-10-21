# R10: Interconnection queue positions and transmission as the scarce right for Western geothermal

**Method note.** The shared WebSearch budget for this run (200 calls per turn) was used up before this agent ran its first query, so no searches ran. Sources were fetched directly by URL: SEC EDGAR, the OSTI.gov full-text PDFs of LBNL, PNNL and NLR reports, and Latitude Media. Facts from sibling evidence files (R04, Z05, Z06, Z08, L23) are cross-referenced with their original URLs. **No primary source for Greenlink costs or dates could be fetched**: NV Energy's site returned empty pages, and the BLM and Wikipedia pages returned 404. Every Greenlink number below is therefore marked (unverified) and should be confirmed in a follow-up pass.

---

## 1. Headline: geothermal's queue is small, concentrated in Nevada, and growing fast

From LBNL's **Queued Up: 2026 Edition**, with data to the end of 2025 (OSTI 3376147, https://www.osti.gov/servlets/purl/3376147):

**Geothermal**
- **Active geothermal capacity in US queues reached 4.8 GW at the end of 2025, up from 1.8 GW at the end of 2024 (+170%).**
- By region: **West (non-ISO) 4,736 MW; CAISO 53 MW; none anywhere else.**
- LBNL: "Geothermal is only requested in the West (primarily Nevada) and CAISO; the West accounted for all of the year-over-year increase."

**All resources**
- 2,061 GW is active in queues across all types. The non-ISO West has the most of any region, at **567.4 GW across 1,603 requests**.
- Geothermal is therefore **less than 1% of Western queue capacity**. It is competing for the same substations and network upgrades as roughly 560 GW of solar, storage and wind.

**Completion and timing**
- Completion rates are low. Of capacity requested in 2000–2020, **13% reached COD (19% by number of requests)**. The non-ISO West completed **10% of requests** and CAISO **8%**.
- **More than 70% of requests withdraw. 41% of capacity that had signed an interconnection agreement (IA) in 2000–2022 had withdrawn by the end of 2025.**
- The **median project built in 2025 took 61 months** from interconnection request to COD. The figure was 36 months in 2015 and 22 months in 2008.
- Over 750 GW withdrew in 2025 while about 600 GW of new requests came in. LBNL attributes the churn to **Order 2023 reforms: "higher at-risk deposits and withdrawal penalties; stricter readiness criteria to enter and advance in queue"**, and to high upgrade costs.

**Rhodium (March 2025), using the earlier queue snapshot:** about 1.7 GW of geothermal was waiting for IAs, against about 4 GW installed in the US. Rhodium argues that behind-the-meter (BTM) supply to data centres "bypasses this lengthy wait". Source: https://rhg.com/research/geothermal-data-center-electricity-demand/

**Read-across.** The 1.8 → 4.8 GW jump in a single year, almost entirely in Nevada, is the land rush (R01–R03) arriving at the grid. Queue scarcity in Nevada is turning acute right now. The bottleneck is no longer the lease. It is the study slot and the upgrade allocation behind it.

---

## 2. Developers say it outright: "interconnection is the new PPA"

- **Fervo, Sarah Jewett Owens, May 2025:** "The primary bottleneck, though, is interconnection … **Interconnection is the new PPA.**" Fervo is making sure its interconnection details are "really buttoned up" to clear queues faster. Rising interconnection timelines are pushing customers toward BTM geothermal. The Corsac Station (NV) Google/NV Energy deal is 115 MW and could be "doubled or tripled". https://www.latitudemedia.com/news/the-clean-transition-tariff-won-approval-in-nevada-whats-next-for-fervo/
- **Zanskar, CTO Joel Edwards:** "**Interconnection is our bottleneck.**" Zanskar sizes plants in **20 MW increments** to use the Western **small generator interconnection** process, which "significantly speeds up permitting and processing times". It has six 20 MW plants in the pipeline, with COD expected in 3–4 years. https://www.latitudemedia.com/news/armed-with-115-million-geothermal-startup-zanskar-gets-ready-to-build/
- **Fervo 424B4 prospectus (May 2026):**
  - "for **Cape Station Phase II, we currently have approximately 290 megawatts of interconnection and transmission rights**."
  - Its SCE PPAs **require "firm, end-to-end transmission"** from the point of interconnection to designated delivery points.
  - Losing "adequate interconnection or transmission rights" is a **PPA termination trigger**.
  - Lenders may judge projects without interconnection or transmission "not financeable on a non-recourse or limited recourse basis".
  - Its "Ready to Build" milestone is defined as "obtained interconnection or established a clear, achievable path".
  - https://www.sec.gov/Archives/edgar/data/1853868/000162828026034849/fervoenergy-424b4.htm
- **Ormat FY2025 10-K:**
  - Lists competition for "power purchase agreements, development sites, **interconnection capacity**" as a growth risk.
  - Says "We rely on power transmission facilities that we do not own or control."
  - McGinness Hills (NV, about 160 MW) "experienced heavy curtailments during the year as a result of NV Energy T-line maintenance".
  - https://www.sec.gov/Archives/edgar/data/1296445/000129644526000006/ora-20251231.htm
- **Zanskar, Lightning Dock (NM):** output is curtailed in winter by a **transmission cap**. The resource now exceeds what the line can take (Z02, Z10; https://zanskargeothermal.substack.com/p/one-year-at-lightning-dock).

**Industry phase definitions (NLR 2025 US Geothermal Market Report, Appendix):**
- A **Phase II** project needs "Interconnection Application Submitted and Queue Position Established" or transmission feasibility studies under way.
- **Phase III** needs at least two of: feasibility study complete, System Impact Study under way or complete, facility study under way, transmission service request submitted.
- **Phase IV** requires that "the Large Generator Interconnection Agreement must be signed". Where point-to-point delivery is needed, transmission service studies must also be complete.

The queue position is therefore a formal rung on the industry's own de-risking ladder, alongside the temperature-gradient hole and the full-size well. Source: https://www.osti.gov/servlets/purl/3014949

---

## 3. Evidence that interconnection capacity is priced as a separate asset

| Datapoint | Number | Source |
|---|---|---|
| Ormat buys Blue Mountain (NV) from Cyrq, Jun 2025 | **$88.7M for a 20 MW plant that holds 51 MW of interconnection**, about $4.4M/MW. The roughly 31 MW of unused interconnection headroom is surplus-interconnection optionality that Ormat can fill with expansion or storage. | Ormat 10-Q Q2-2025 https://www.sec.gov/Archives/edgar/data/1296445/000129644525000008/ora-20250630.htm (via R04) |
| Open Mountain Energy (Reno) discloses its portfolio | **95.8 MW of contracted interconnection vs 57.5 MW of guaranteed PPA capacity**. Interconnection is marketed as its own line item, ahead of PPA MW. | https://www.openmountainenergy.com/ (via Z07/Z08) |
| Fervo Cape Phase II | **about 290 MW of interconnection and transmission rights**, held as a named asset in the prospectus | Fervo 424B4 |
| U.S. Geothermal sale process (2017) | Development projects were discounted at 14–16% vs 8–10% for operating ones, because there was "no PPA and transmission costs were rising". Undeveloped resources were worth about $0.1M/MW against $4.4M/MW operating. | R04 (DEFM14A) |

R04 concludes that **value jumps at PPA plus interconnection, not at the temperature hole**. That is the key finding for this topic. In the Terranox value chain, the queue position sits between "confirmed resource" and "PPA" and captures a meaningful part of the step-up.

### Surplus interconnection service: a brownfield arbitrage

FERC **Order 845** requires transmission providers to offer **surplus interconnection service**. A new generator can connect at an existing point of interconnection (POI) using studied-but-unused injection capacity, "in exchange for faster interconnection and lower interconnection costs … without the need for more in-depth new study and network upgrades". LBNL also describes **provisional** service (curtailable until upgrades are built) and **ERIS** (energy-only, non-firm, cheaper and faster). Source: LBNL *Speed to Power* (2026), https://www.osti.gov/servlets/purl/3367528

**Implication.** Every existing Nevada geothermal plant, and every retired or under-used fossil, solar or geothermal POI with headroom, is an interconnection right that skips the 61-month queue. Two examples:
- **Blue Mountain** has 31 MW of headroom.
- **Lightning Dock** has the opposite problem: it is capped.

A map of POI headroom near blind resources is itself a "public but illegible" dataset. It can be built from utility OASIS postings, FERC Form 1, EIA-860 nameplate versus interconnection limits, and queue data.

---

## 4. Regional picture: NV Energy, PacifiCorp, CAISO

### NV Energy and Greenlink

**Greenlink West** (all figures unverified)
- About 350 miles of 525 kV line from the Las Vegas area to Fort Churchill/Yerington.
- Cost estimates reportedly rose from about $1.3B (2021 IRP) to about $2.4B in later filings.
- Target in-service about 2027.

**Greenlink North** (all figures unverified)
- About 235 miles from Ely (Robinson Summit) to Fort Churchill.
- Estimated at about $1.9B or more.
- Target about 2028.

**Combined program:** more than $4B (unverified). Both lines are confirmed only as "baseline" Western transmission projects in PNNL's *Western Interconnection Baseline Study* (PNNL-36452, Sep 2024, https://www.osti.gov/servlets/purl/2440740).

**Geography.** Both lines terminate at Fort Churchill, in the Churchill/Lyon/Pershing heart of the Nevada geothermal belt (Dixie Valley, Fallon, Carson Sink). Greenlink North crosses central Nevada along the US-50 corridor, where Ormat's McGinness Hills sits and where Lander-county BLM parcels have been heavily contested, including Invenergy's $112/acre win over Zanskar's $111 (Z08).

**Timing.** Leases within reach of Greenlink substations should see a step-up in value when the lines are energised, about 2027–28 (unverified).

**Process and demand**
- NV Energy has moved to a cluster study process under Order 2023 (LBNL: non-ISO focus on "Order 2023 compliance; moving to cluster study process").
- The **Clean Transition Tariff** (customers of 5 MW or more fund dedicated clean resources at their own premium; the first project is the 115 MW Fervo/Google geothermal contract) creates a direct path from a large-load customer to a specific resource. That makes a "resource + land + queue" package monetisable to a hyperscaler, not just to NV Energy (LBNL *Speed to Power*).

### PacifiCorp (Utah, Oregon, Wyoming, Idaho)

- PacifiCorp was the first large Western utility to move to cluster studies, around 2020 (unverified).
- Fervo's Cape Station (Beaver County, UT) holds about 290 MW of interconnection and transmission rights for Phase II. Its SCE PPAs need firm end-to-end transmission into CAISO, reportedly over the Intermountain/IPP path (unverified).
- **Delivery is part of the right.** For export sales to California, the queue position alone is not enough; firm point-to-point transmission service must also be secured.

### CAISO

- 191.3 GW is active, but only **53 MW of it is geothermal**.
- Cluster 15 was forced to pause and resubmit in 2024, and "many did not". **Cluster 16 was not open until 2026.**
- CAISO's Interconnection Process Enhancements "prioritize requests based on commercial readiness and alignment with state resource" plans. Points of interconnection are effectively zonal and capped by transmission plan deliverability (Queued Up 2026).
- Geothermal's policy alignment (CPUC mid-term reliability "firm clean" procurement) helps it score well. However, an out-of-state Nevada project still needs deliverability into CAISO or a pseudo-tie/dynamic transfer.

---

## 5. Cost and transferability of queue positions

**Under Order 2023** (exact amounts unverified; confirm against FERC Order No. 2023 and each utility's OATT)
- **Study deposits** scale with MW, on the order of $35k plus about $1k/MW for small projects and up to roughly $250k for projects of 200 MW or more.
- **Commercial readiness deposits** escalate, from roughly 2× the study deposit at entry to a percentage of allocated network-upgrade cost at later stages.
- **Withdrawal penalties** can forfeit multiples of the study deposit.
- **Site control** must be demonstrated for the generating facility at application. A geothermal lease or right is therefore a gating input to holding a queue position.

**Order 2023's design and its effect.** The rules were built to squeeze out speculative positions, and LBNL attributes the record 750 GW of withdrawals in 2025 partly to them. Two effects follow:
- **The cost of holding a queue position has risen**, from hundreds of thousands to several million dollars at risk per 100 MW project (unverified magnitude).
- **The value of surviving positions has risen.**

**Transferability** (unverified as a rule; confirm in the NV Energy and PacifiCorp OATTs)
- Pro-forma LGIP/LGIA terms generally allow an interconnection request or LGIA to be **assigned with the project**: same site, same POI, same technology envelope.
- A change of POI or a large technology change is a "material modification" that loses queue priority.
- **Positions are therefore transferable as part of a site package, not as free-floating tickets.** That fits a Terranox-shape "sell the proven package" model. Secondary sales of interconnection-advantaged projects are routine in solar and storage M&A (unverified for geothermal specifically).

**Small generator path (20 MW or less, under the SGIP)**
- This is Zanskar's chosen lane.
- It is faster, but it caps project size and makes portfolios of 100 MW or more slow to fill.
- Several 20 MW positions at different POIs is also a diversification of interconnection risk.

---

## 6. Is land + queue the real moat?

**Arguments for**
1. The scarce input moves along the chain. In 2019–21 the cheap input was BLM acreage: Fervo paid about $4/acre for about 596k acres (R04/Z08). By 2024–25 Nevada parcels cleared at $100–400 or more per acre (R01–R03). Now **the queue is the bottleneck**, by the stated view of both leading developers.
2. Interconnection is formally a de-risking milestone (NLR phase definitions), a PPA covenant, and a financing gate (Fervo 424B4). It is visibly priced: Blue Mountain's 51 MW of interconnection on a 20 MW plant, and Open Mountain's 95.8 MW of interconnection vs 57.5 MW of PPA.
3. Only about 4.8 GW of geothermal is queued nationally. The total opportunity cited is tens of GW (USGS about 30 GW undiscovered hydrothermal; DOE GeoVision 60–90 GW), so the queue, not the resource, is the binding constraint.
4. Queue positions require site control. A party that holds the right **and** files the interconnection request at the same time locks out rivals at that POI.

**Arguments against, or limits**
1. Queue positions cost real money and decay through study milestones and withdrawal penalties. A speculative rights bank can't afford positions on every parcel.
2. Positions aren't detachable from the site and POI, so they can't be traded freely like mineral claims.
3. **BTM and co-location are a bypass.** Fervo's GeoClusters, the CTT and Rhodium's BTM analysis all route around queues by siting load at the resource. That lowers queue scarcity for data-centre-sited projects, but raises the value of **land + resource + data-centre-ready acreage** near substations.
4. Transmission build-outs such as Greenlink, about 2027–28 (unverified), will relieve scarcity in specific corridors over time.

**Verdict.** The moat is a bundle of five items:
- **resource evidence**;
- **lease or right**;
- **a queue position at a POI with headroom**, or a **surplus-interconnection** slot at an existing plant;
- **water** (R09);
- **an offtake path**: utility PPA, CTT large-load contract, or BTM.

Land alone is now competitively bid. Queue alone is not legally possible without site control. The combination, filed early, is the scarce asset.

---

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **The step-up has a new rung.** Terranox's uranium playbook buys a claim and sells the proven claim. In Western geothermal, the evidence (R04, the NLR phase definitions, Fervo, Ormat) says **the biggest discrete value jump comes at "confirmed resource + interconnection position/IA"**, not at the temperature hole. A Terranox-shape company should plan to **file interconnection requests as soon as site control is secured**. It would then sell Phase II/III packages (lease + TG data + queue position + water) to Fervo, Ormat, Invenergy or hyperscaler-backed developers, who value speed to COD above all ("interconnection is the new PPA").
2. **The ML target should include grid geometry, not just heat.** Score every parcel on resource probability **and** distance to a POI with headroom: surplus capacity at existing plants, under-used substations, and future Greenlink substations. Do this with the same "public but illegible" approach, applied to OASIS/queue spreadsheets, EIA-860 and FERC filings. This is a distinctive dataset that geologically focused competitors don't prioritise.
3. **Brownfield POI arbitrage is an asset-owning play.** Buy small, aging or curtailed plants, or retired fossil sites, chiefly for their interconnection agreements. Blue Mountain shows Ormat paid $88.7M for 20 MW of plant plus 51 MW of interconnection. Then attach newly discovered nearby blind resources through surplus interconnection service and skip the 61-month queue.
4. **Gap vs Zanskar.**
   - Zanskar treats interconnection as **its own bottleneck**: it self-limits to 20 MW SGIP plants, builds itself, and is capped by its own capex and queue throughput (Z05/Z06).
   - It is structurally unwilling to sell pre-queued packages to rivals, and it is not optimising for large POIs or for hyperscaler BTM siting.
   - A Terranox-shape company can be the **upstream "land + queue" warehouse** for the whole industry, and in particular for the large-scale developers (Fervo's 290 MW Cape rights, GeoClusters of 1 GW or more) that need many large, interconnectable sites quickly.
   - Zanskar finds and builds. The gap is to find, secure and grid-position, then sell or JV at the step-up, across many more parcels than a builder can carry.
5. **Risks to manage.**
   - Order 2023 deposits and withdrawal penalties make blanket queue filing expensive. File selectively on the highest-confidence parcels, and use SGIP for 20 MW options.
   - Positions transfer only with the site and POI, so structure each project as a separate SPV for clean assignment.
   - Verify Greenlink timing, cost and substation locations before underwriting corridor-adjacent leases.

---

## Sources

- LBNL, *Queued Up: 2026 Edition* (data to end-2025), OSTI 3376147: https://www.osti.gov/servlets/purl/3376147
- LBNL, Kahrl, Frick et al., *Speed to Power: Solutions for Accelerating Large Load Connections* (2026), OSTI 3367528: https://www.osti.gov/servlets/purl/3367528
- NLR (ex-NREL), *2025 U.S. Geothermal Market Report* (phase definitions appendix), OSTI 3014949: https://www.osti.gov/servlets/purl/3014949
- PNNL, *Western Interconnection Baseline Study* (PNNL-36452, 2024), OSTI 2440740: https://www.osti.gov/servlets/purl/2440740
- Fervo Energy 424B4 prospectus (May 2026): https://www.sec.gov/Archives/edgar/data/1853868/000162828026034849/fervoenergy-424b4.htm
- Ormat FY2025 10-K: https://www.sec.gov/Archives/edgar/data/1296445/000129644526000006/ora-20251231.htm
- Ormat 10-Q Q2-2025 (Blue Mountain): https://www.sec.gov/Archives/edgar/data/1296445/000129644525000008/ora-20250630.htm
- Latitude Media, Fervo and the CTT (May 2025): https://www.latitudemedia.com/news/the-clean-transition-tariff-won-approval-in-nevada-whats-next-for-fervo/
- Latitude Media, Zanskar $115M (2025): https://www.latitudemedia.com/news/armed-with-115-million-geothermal-startup-zanskar-gets-ready-to-build/
- Rhodium Group (2025): https://rhg.com/research/geothermal-data-center-electricity-demand/
- Zanskar, One year at Lightning Dock: https://zanskargeothermal.substack.com/p/one-year-at-lightning-dock
- Open Mountain Energy: https://www.openmountainenergy.com/
- Sibling evidence files: R01–R04, R09, Z02, Z05–Z08, Z10 and L23 in /home/user/nuketime/research/geothermal/evidence/
