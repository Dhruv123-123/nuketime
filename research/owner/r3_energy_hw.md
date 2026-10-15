# Round 3 lane: energy hardware and plant assets (not drilling, not powered land or queue positions)

Written 15 Oct 2026. I used 20 WebSearch calls, plus fetches of the pages they returned. Figures marked [bg] come from my background knowledge; I did not verify them this run. GitHub search is blocked from this session. The PUDL data bucket on S3 does answer: a range request to `pudl.catalyst.coop/stable/pudl.sqlite.zip` returned HTTP 206, so the EIA and FERC data can be pulled for a proof.

## Bottom line

- **The scarcity is real and severe.**
  - PJM's 2027/28 Base Residual Auction cleared at the **$333.44/MW-day cap** across the whole footprint. It came in 6,623 MW short of the reliability requirement and cost about $16.4B ([Power Engineering, Dec 2025](https://www.power-eng.com/business/pjm-capacity-auction-hits-price-cap-again-as-region-falls-short-of-reliability-target/)).
  - Gas turbines are expected to reach **$600/kW by end-2027**, up 195% since 2019. Lead times are about 6 years, and orders of 110 GW compare with 60-70 GW of factory capacity ([APPA citing Wood Mackenzie](https://www.publicpower.org/periodical/article/gas-turbine-market-will-see-prices-surge-through-2027-report)).
  - GSU transformer lead times are over 160 weeks and HV breaker lead times about 125 weeks ([Reuters via Kitco, Jul 2026](https://www.kitco.com/news/off-the-wire/2026-07-09/us-power-companies-scramble-secure-equipment-surging-data-center)). Transformer prices are up about 80% in five years and lead times reach 4 years ([pv magazine, May 2026](https://pv-magazine-usa.com/2026/05/11/u-s-transformer-market-faces-severe-supply-constraints-as-lead-times-extend-to-four-years/)).
- **The candidates fail on the "unattackable" leg.** An idle turbine, transformer or plant is a physical object. Whoever writes a cheque first takes it. There is no cheap claim, and every unit has a known owner who has an OEM, a broker and the scarcity headlines telling them what it is worth.
- **The data edge is weak where the assets are.**
  - EIA-860 already names every generator, with its prime mover, nameplate, status and planned retirement date.
  - OEMs know where every serial number sits through their service agreements (LTSAs).
  - Equipment dealers already buy whole retired plants.
- **Best idea: B, stranded never-fired turbines found worldwide (5/10).** The Hallador / Energy World deal proves that this class of equipment exists and sells for about $760/kW. The pool is probably tens of units, though, and the arbitrage lasts only until OEM capacity catches up around 2029-30. Nothing in this lane clears 6/10.

## Scores

| # | Candidate | Score |
|---|---|---|
| A | Idle transformers, GSUs and switchgear at retired plants: buy, refurbish, resell or lease | 3 |
| B | Stranded new or never-fired turbines in stalled projects worldwide (Hallador model) | 5 |
| C | Undervalued or restartable PJM generating units bought on capacity-price signals | 2 |
| D | Behind-the-meter backup gensets found through air permits, aggregated as capacity | 3 |
| E | OEM turbine slot reservations as a tradable claim | 3 |
| F | Buy retired plants whole, part them out, keep the site (Phoenix model with an ML retirement predictor) | 4 |

---

## A. Idle grid equipment at retired plants and utility yards (3/10)

- **Data, and why it is public**
  - EIA-860 lists every generator, including retired and standby units, with their plant and status. It is mandatory under the Federal Energy Administration Act.
  - FERC Form 1 gives plant accounts in dollars, not individual equipment.
  - Utility rate cases and IRPs sometimes list spare transformers.
  - The EEI Spare Transformer Equipment Program (STEP) and Grid Assurance hold spare pools. Both are member-only, not public.
  - **No public dataset lists transformers unit by unit.** HIFLD substation layers give locations and voltages, not the units in them.
- **ML problem.** Infer which retiring plants have a reusable GSU or switchgear: voltage class, MVA, age and whether it is still energised. Inputs would be EIA-860 nameplate data plus the retirement date, satellite imagery of yards, and decommissioning RFPs. That is a matching problem, not a deep inference problem.
- **What is owned.** Purchased equipment, held as inventory and then resold or leased.
- **Rivalry.** First to buy wins. The owner sets the price.
- **Ceiling and size.** Remanufacturing costs 10-40% less than new, and remanufactured distribution units ship in 1-4 weeks against 60-80 weeks for new ones. Maddox buys feedstock at "up to five times scrap value" ([Maddox / POWER](https://www.powermag.com/partner-content/beating-the-transformer-bottleneck-remanufacturing-build-to-stock-and-smart-procurement/)). Market reports on transformer rebuilding put it in the low billions worldwide; I treat those reports as unreliable. **Large power transformers (100 MVA and up) are bespoke.** Voltage, impedance and footprint must match, so a used GSU rarely drops into a data-centre substation without redesign. The scarce, high-value class is the least fungible.
- **Who already does it.**
  - **Sunbelt Solomon:** 42 locations in the US, Canada and Chile; sold by Trilantic to TJC (over $31B AUM) in July 2026 ([briefglance](https://briefglance.com/articles/tjcs-power-play-why-this-deal-is-a-bet-on-americas-grid-future)).
  - **Maddox:** five remanufacturing shops and thousands of units in stock.
  - **Others:** ELSCO, Northern Transformer, the OEM service arms (Hitachi Energy, Siemens Energy, GE Vernova) and the utility spare pools.
- **Why GSUs at retired plants are not loose.** Owners keep them because they hold on to the interconnection rights for repowering (killed in Round 3). PJM's Reliability Resource Initiative, for example, favoured uprates and reactivations on existing sites [bg].
- **Verdict.** The market is crowded, the equipment is not fungible, and nothing can be claimed. Score 3.

## B. Stranded new or never-fired turbines worldwide (5/10, best in lane)

- **Proof the class exists.** On 1 June 2026, Hallador bought about **460 MW of never-fired Siemens gas and steam turbines plus balance of plant** from Energy World Corp (ASX: EWC). The kit came from a Philippine LNG-to-power project that had been in development for more than ten years.
  - Price: **$350M, about $760/kW**, plus about $100M for transport and Siemens refurbishment.
  - Without the deal, new units would not arrive before late 2028 at the earliest ([Turbomachinery, Jun 2026](https://www.turbomachinerymag.com/view/hallador-energy-bypasses-oem-backlog-secures-unfired-siemens-turbine-in-350-million-deal)).
  - Engie and Calpine have also bought "lightly used turbines from projects that were canceled or delayed" ([Gainer substack](https://mitchgainer.substack.com/p/green-fundamentals-gas-gridlock)).
  - xAI reportedly shipped an entire overseas power plant to the US [bg].
- **Data, and why it is public**
  - Global Energy Monitor's Global Oil and Gas Plant Tracker lists cancelled, shelved and mothballed projects worldwide, often with the turbine OEM named. It is CC BY 4.0, downloadable through a form, and has a gem.wiki page per plant.
  - Stock-exchange continuous-disclosure filings (ASX, SGX, PSE, BSE, JSE) record impairments of "equipment in storage". EWC's sale was announced on ASX ([ASX PDF, Jul 2026](https://announcements.asx.com.au/asxpdf/20260722/pdf/071ylt57prmb4y.pdf)).
  - Export credit agency and development bank project documents, and court or insolvency dockets for failed IPPs, are also public.
- **ML problem.** Find equipment that was paid for but never commissioned. That means joining:
  - project status (shelved or cancelled);
  - OEM order announcements;
  - financial-statement notes in many languages ("capital work in progress", "plant held for sale");
  - satellite imagery of laydown yards.

  The signal is sparse, multilingual and multi-modal, which is a real inference task.
- **What is owned.** An option or purchase agreement over a specific unit, then resale or lease to a US data-centre or IPP buyer. Alternatively, the units are bundled with a site to build a plant (Hallador did this for itself).
- **Rivalry.** A physical unit is exclusive. Whoever signs the purchase agreement first wins. It is not a cheap claim: an option still costs a deposit, and the full price is $100M+ per block.
- **Ceiling.** Suppose 5-15 GW of stranded frame and aero units exist worldwide [my guess, unverified], bought at $300-500/kW and resold at $700-1,000/kW. The gross spread would be about **$1-5B, one-off**, available only while the new-build gap lasts (to about 2029-31). It is a trading window, not an annuity.
- **Who already does it.**
  - **The OEMs.** They know every serial number and its LTSA, and Siemens refurbished the EWC units.
  - **Used-equipment dealers.** USPE claims 3,000 MW+ under relationship and lists a 1990s 100 MW W501D-5 at $39.4M (about $394/kW) ([USPE](https://uspeglobal.com/inventory/)). Others include Phoenix Equipment, ProEnergy and Wood/EthosEnergy [bg].
  - **Strategic buyers acting for themselves:** Calpine, Engie, Hallador, Crusoe.
- **Why only 5.**
  - The OEMs hold the master list.
  - Refurbishment and the LTSA run through the OEM, which can slow-walk a competitor's resale.
  - The pool is small.
  - Prices are already marked to scarcity.

  The edge is real but narrow, so this works as a fund or trading desk rather than a "Terranox".
- **First proof (cheap).** Pull GEM shelved and cancelled gas projects from 2010 to 2025 that have OEM fields. Filter to projects with financial close or an announced turbine order. Then search exchange filings by hand for 20 of them and count how many still hold unsold turbines. If 5 or more of the 20 do, the pool is worth pursuing.
- **Mirror.** I could not verify a GitHub mirror of GEM (search blocked). GEM's own downloads are free once the form is filled in.

## C. Undervalued or restartable generating units in PJM (2/10)

- **Data.** All of these are public by statute or tariff:
  - EIA-860 and EIA-923 (heat rate, capacity factor, fuel);
  - EPA CEMS hourly;
  - PJM deactivation notices and RMR filings;
  - BRA results.
- **The economics.** At $333/MW-day, capacity alone pays about $122k/MW-year, so a 100 MW peaker earns about $12M a year before energy margins. Prices in the two prior years were $269.92 (2025/26) and $329.17 (2026/27) [bg].
- **The asset is already priced.**
  - Vistra paid **$1.9B for 2,557 MW, about $743/kW**, for Lotus's mixed CCGT and peaker fleet in PJM, New England and New York ([POWER, May 2025](https://www.powermag.com/vistra-to-acquire-2-6-gw-gas-fleet-for-1-9b-citing-surging-u-s-power-demand)).
  - NRG bought LS Power's 13 GW for about $12B, and Constellation bought Calpine [bg].
  - TeraWulf is buying GenOn's retired Morgantown site. PJM's market monitor objected on 4 March 2026 that the deal would pull the resource out of the market ([Global Transmission](https://globaltransmission.info/pjm-market-monitor-opposes-maryland-power-plant-sale-to-data-centre-company/)).
- **Restarts.** Retirement dates on 16.5 GW across 34 units were pushed back by their *owners*, through RMR agreements and DOE 202(c) orders (Brandon Shores, Eddystone, Campbell and others) ([Frontier Group](https://frontiergroup.org/articles/data-center-energy-use-is-giving-old-dirty-power-plants-a-new-lease-on-life/)). Owners and regulators capture this value. An outsider cannot claim it.
- **Who.** Vistra, NRG, Constellation, Talen, LS Power, ArcLight, Carlyle, Earthrise and Hull Street, all of them running Enverus or S&P models on the same EIA data.
- **Verdict.** This is the most heavily covered asset class in US energy. Score 2.

## D. Behind-the-meter backup gensets found through air permits (3/10)

- **Data.** State Title V and minor-source permits, EPA RICE NESHAP and NSPS notifications, EIA-860 for units of 1 MW and up, and county building permits. All are public as part of permitting.
- **ML problem.** Extract the generator inventory from scanned permits across 50 state formats. This is real document ML, similar to Terranox's work on SMAD.
- **What is owned.** Nothing. The generators belong to the hospitals and data centres. The company could own only an aggregation contract, which customers can switch, or the gensets it buys outright.
- **Regulation caps the value.** Emergency RICE are limited to about 50 non-emergency hours a year. Selling into capacity markets usually needs a non-emergency permit and Tier 4 controls. PJM can already push data centres onto backup in emergencies (DOE order, July 2026).
- **Who.** Enchanted Rock owns and operates resiliency microgrids. Voltus, CPower, Enel X and Generac Concerto aggregate. AGent Energy raised an **$11M seed in August 2026** to do exactly this, citing about **200 GW** of BTM generation ([Runtime Wire](https://runtimewire.com/article/stephanie-hendricks-agent-energy-11-million-seed-backup-generators)).
- **Verdict.** The model is an aggregation service: crowded, non-exclusive, with its ceiling set by fees. Score 3.

## E. OEM turbine slot reservations as a tradable claim (3/10)

GE Vernova signed 9 GW of reservations in one month [Power Engineering, via search result]. Slot reservations are the closest thing in this lane to a cheap first-come claim: a deposit holds a future factory slot.

They fail on three counts:
- Assignment usually needs the OEM's consent [bg].
- Deposits are sizeable.
- Holders are NextEra, Chevron, Crusoe and the hyperscalers, which have balance sheets and specific sites.

No public dataset exists, apart from occasional press releases. Data and ML give no edge, so this is plain capital speculation. Score 3.

## F. Buy retired plants whole, part them out, keep the site (4/10)

- **Proof.** Phoenix Equipment bought the whole Pawtucket cogeneration plant at no cost to its owner and sold its GE Frame 6B to a buyer in Rochester ([Phoenix](https://www.phxequip.com/resource-detail/111/pawtucket-cogeneration-plant-full-facility-redeployment-site-clearance)). Its stated lines of business are "Buy Used Plants", "Dismantlement" and "Liquidations".
- **Data and ML.** EIA-860 retired, standby and planned-retirement units; EIA-923 capacity factors; owner financial distress; state decommissioning filings. Train a model on which owners sell rather than repower, and approach them before the auction.
- **Owned.** The equipment, plus the site, which may carry rights.
- **Weaknesses.**
  - Owners now hold sites for data-centre conversion, as with Homer City and Morgantown.
  - Dealers and demolition contractors already work the retirement list.
  - Demolition liabilities fall on the buyer.

Score 4.

## G. Other ideas checked quickly

- **Converting retired aircraft engines to power.** CF6-80C2 cores are being turned into 48 MW PE6000 units (ProEnergy, 21 units sold), and CFM56 engines into 25 MW units (FTAI Power) ([GasTurbineHub](https://antonios-newsletter-aff62c.beehiiv.com/p/from-boneyard-to-baseload-how-retired-flight-engines-just-became-a-serious-competitor-to-oem-gas-tur)). The FAA registry and Cirium-type fleet data show where cores are. It is crowded (FTAI, ProEnergy, Boom building new), and the cores are bought on the open market. Score 3.
- **Strategic transformer reserves.** DOE, Grid Assurance and STEP are utility clubs, so there is no entry point. Score 2.

## What would change the picture

Only B has an inference problem that incumbents do not obviously solve: stranded equipment hidden in many languages and in illegible filings outside the US. If a quick GEM-plus-filings count turns up 5 GW or more of unsold, never-fired units outside OEM-controlled channels, it becomes a credible $1B+ trading business. That would still be a window, not a Terranox-style durable claim.

## Datasets and mirrors

- **PUDL (Catalyst Cooperative)** combines EIA-860, EIA-923, FERC Form 1 and EPA CEMS into a single SQLite file. It is reachable from this cloud: `https://s3.us-west-2.amazonaws.com/pudl.catalyst.coop/stable/pudl.sqlite.zip` returned HTTP 206 on a range request. The repo is `github.com/catalyst-cooperative/pudl` (HTML page gave 403, PyPI page returned 200). This is enough for the proofs in B and F (retired and standby gas turbines by model and age).
- **GEM Global Oil and Gas Plant Tracker:** CC BY 4.0, downloaded through a form, with one gem.wiki page per project. I did not check for a GitHub mirror.
- **PJM BRA results and deactivation lists:** pjm.com (government-style host, may be blocked). Grid Status mirrors some of this.
