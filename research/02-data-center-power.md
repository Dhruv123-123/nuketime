# Data Center Power Crunch: Sourced Briefing (as of 2026-09-25)

## 1. Demand: how much is real?

**Forecast range (US data center load, 2030):**
- LBNL 2025 Update (June 2026): data centers = 11.8% of US electricity by 2030 (range 9.5–15.3%); 192 TWh (2024) → 464 TWh (2028) → 649 TWh (2030). https://datacenters.lbl.gov/modeling-forecasting
- EPRI "Powering Intelligence 2026" (Feb 2026): 384 / 596 / 793 TWh (low/med/high) in 2030 = 9–17% of US electricity. https://powering-intelligence.epri.com/executive-summary.html
- BloombergNEF (Dec 2025): 106 GW US DC demand by 2035 (from 78 GW est. Apr 2025); ~25 GW operating 2024. https://www.utilitydive.com/news/us-data-center-power-demand-could-reach-106-gw-by-2035-bloombergnef/806972/
- Grid Strategies (Nov 2025): utility 5-yr peak growth forecast 166 GW by 2030; DCs ~90 GW. https://gridstrategiesllc.com/wp-content/uploads/Grid-Strategies-National-Load-Growth-Report-2025.pdf
- Goldman: US DCs add 36.3 GW in 2027 alone.

CONFLICT: 2030 estimates span ~2x. Spread is a realization-rate assumption.

**Hyperscaler capex:** 2026 guidance ~$725–732B combined (Amazon ~$200B, Google $175–185B, Meta $125–145B, Microsoft $110–190B depending on FY definition). H1 2026 actual $301B. 2027 consensus ~$935B. Capex now outruns operating cash flow. https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html ; https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow

**Phantom load:**
- Grid Strategies (Nov 2025): utility DC forecasts of 90 GW by 2030 overstated by ~25 GW. https://www.utilitydive.com/news/some-load-forecasts-using-unrealistically-high-load-factors-grid-strateg/805927/
- Camus CEO: 5–10x more interconnection requests than DCs built. https://www.utilitydive.com/news/a-fraction-of-proposed-data-centers-will-get-built-utilities-are-wising-up/748214/
- ~30% of one utility's 2024 load applications cancelled; same project bid multiple times. https://www.latitudemedia.com/news/phantom-data-centers-are-flooding-the-load-queue/
- PJM 2026 forecast cut 2028 peak by 4.4 GW after stricter vetting; still 30 GW DC growth 2024–2030. https://www.utilitydive.com/news/pjm-interconnection-load-forecast-data-centers/809717/
- ERCOT: 233 GW large-load requests end-2025; 438 GW by June 2026 (~89% DC). https://www.ercot.com/news/release/06182026-puct-approves-ercots
- Southern Co: 10 GW contracted vs 75 GW pipeline (Feb 2026); 17 GW contracted by Q2 2026. https://www.utilitydive.com/news/southern-co-load-data-center-earnings/812681/
- AEP Ohio 85% take-or-pay tariff "weeding out uncommitted load."

Bottom line: discount queue numbers 5–10x. Realistic incremental US DC load by 2030: 50–70 GW.

## 2. Interconnection and time-to-power

**PJM capacity auctions (three consecutive caps):** 2026/27 $329.17; 2027/28 $333.44 (uncapped ~$530); 2028/29 (July 14, 2026) $325 cap, 138,318 MW, 6,831 MW short of reliability requirement, uncapped would have been $554.72 RTO / $776.69 ComEd. https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2028-2029/2028-2029-bra-results-report.pdf
- Market monitor: DCs = $6.5B (40%) of 2027/28 cost; 45% ($21.3B of $47.2B) over three auctions. https://www.utilitydive.com/news/data-centers-pjm-capacity-auction/808951/

**PJM co-location:** FERC Dec 18, 2025 found PJM tariff unjust for co-located load; ordered provisional interconnection, below-nameplate service, interim non-firm NITS. https://www.ferc.gov/news-events/news/ferc-directs-nations-largest-grid-operator-create-new-rules-embrace-innovation-and

**Federal:** DOE Sec. 403 directive Oct 23, 2025 → FERC issued six §206 show-cause orders June 18, 2026 to all RTOs on large-load rules. https://www.ferc.gov/rm26-4

**ERCOT / SB6:** ≥75 MW loads: financial security, site control, mandatory emergency curtailment, batch studies. PUCT approved Batch Zero June 18, 2026; most projects operational "by 2030"; Batch 1 opens Summer 2027. https://www.ercot.com/news/release/06182026-puct-approves-ercots

**MISO ERAS:** GIA in ~3 months, capped at 68 projects through Aug 2027. **SPP HILL:** conditional curtailable service, agreements ~90 days.

**State large-load tariffs:** AEP Ohio >25 MW, 85% minimum bill up to 12 yrs; Dominion GS-5 (eff. Jan 2027) 85% T&D / 60% generation take-or-pay; Georgia Power ~10 GW / $16B new gen, 15-yr bilateral minimums. EEI list: https://www.eei.org/-/media/Project/EEI/Documents/Issues%20and%20Policy/List%20of%20Large%20Customer%20Projects%20and%20Tariffs

**Time-to-power, 300 MW+ site:** 4–7 years for firm grid service in PJM/ERCOT/Southeast vs ~12–24 months for curtailable/conditional service. ProEnergy sizes bridging at 5–7 years.

## 3. Behind-the-meter and bridging power

- GE Vernova: 116 GW gas backlog + slots (Q2 2026), ≥125 GW by YE2026; ~10 GW of 2029–30 slots left; lead times ~3 yrs, 5–7 for non-prioritized. https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000147/gev2q2026form8-k.pdf
- Siemens Energy (Aug 2026): 69 GW backlog, booked out to FY2028; 65% of gas orders for DCs. https://www.utilitydive.com/news/siemens-gas-turbine-backlog-nears-70-gw-as-company-expands-manufacturing/827390/
- Mitsubishi (Aug 2026): 35 GW backlog, deliveries 2028–2030.
- Recips: Wärtsilä 8–10 months; Cat up to ~46 months observed. Deals: Nscale 2 GW Cat (WV); INNIO 1.5 GW to VoltaGrid. https://naturalgasintel.com/news/no-turbine-data-centers-find-faster-path-with-natural-gas-reciprocating-engines/
- Bloom: Brookfield $5B framework; AEP $2.65B / 1 GW; Oracle 2.8 GW (via aggregator, verify). https://www.sec.gov/Archives/edgar/data/1664703/000162828026006516/be-20251231.htm
- Capex/lead (SemiAnalysis Dec 2025): aeros $1,700–2,000/kW 18–36 mo; industrial GTs $1,500–1,800/kW; recips $1,700–2,000/kW 15–24 mo; Bloom $3,000–4,000/kW weeks. https://newsletter.semianalysis.com/p/how-ai-labs-are-solving-the-power
- $/MWh bridging (Rabobank 2026): BTM gas $100–165/MWh vs $90–95 grid. No public mobile-turbine rental prices. Solaris $1.25B 7% bond. https://www.rabobank.com/knowledge/d011532274-the-marathon-can-behind-the-meter-data-center-power-solutions-endure-the-decade-in-the-us
- xAI Colossus: 27 unpermitted turbines; MS approved 41 permanent (1.2 GW) Mar 2026; NAACP CAA suit. https://www.eenews.net/articles/xai-gets-air-permit-for-unauthorized-gas-turbines/
- Meta Hyperion: expanded to 10 plants / 7.5 GW / ~$11B (Mar 2026). https://fortune.com/2026/03/27/meta-hyperion-10-gas-power-plants-louisiana-entergy/
- Stargate Abilene: 1.2 GW; ~360 MW onsite; ~$15B financing. Vantage Shackelford: 2.3 GW VoltaGrid for 1.4 GW DC (64% overbuild).
- Latitude: 25–33% of incremental DC demand through 2030 will be BTM. https://www.latitudemedia.com/news/behind-the-meter-generation-is-picking-up-traction/

## 4. Batteries and flexibility

- Duke (Feb 2025): 76/98/126 GW at 0.25/0.5/1% curtailment. https://www.utilitydive.com/news/us-grid-headroom-flexible-load-data-center-ai-ev-duke-report/739767/
- Google: 1 GW of DR embedded in contracts (Mar 2026). https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/demand-response-data-center-milestone/
- Emerald AI: $150M Series A at $1.05B (Aug 25, 2026); AI Energy Management Alliance with Google, Nvidia (Sept 16, 2026). https://www.axios.com/2026/09/16/tech-giants-launch-flexible-power-coalition-data-centers
- Camus FlexConnect, GridCARE ($13.5M), GridUnity ($50M DOE).
- Tesla Megablock (20 MWh) late 2026; Verrus battery-microgrid DCs.
- SB6 mandatory curtailment and PJM non-firm NITS: flexibility is a condition of faster service.

## 5. Nuclear deals: construction vs paper

| Deal | Status | Pricing |
|---|---|---|
| Microsoft–Constellation Crane (835 MW) | Restart target 2027; ~$16B/20yr | est. $70–95/MWh |
| Amazon–Talen Susquehanna (1.92 GW) | Restructured front-of-meter June 2025; transition complete Apr 2026; $18B/17yr | ~$60–70/MWh implied |
| Meta–Constellation Clinton (1.1 GW) | Binding 20-yr PPA from mid-2027 | undisclosed |
| Meta–Vistra (2.176 GW + 433 MW uprates) | Binding 20-yr PPAs from late 2026 | undisclosed |
| Meta–TerraPower | Development funding, ≥2032 | n/a |
| Meta–Oklo (1.2 GW OH) | Framework; first phase ≥2030 | n/a |
| Google–Kairos (500 MW) | Hermes under construction; first commercial 2030 | n/a |
| Amazon–X-energy (320 MW) | Pre-construction | n/a |
| Oklo–Switch (12 GW) | Non-binding; Aurora-INL slipped to 2028 | n/a |

Only existing-plant deals deliver electrons before 2030. No SMR deal is under commercial construction. FERC pushes co-located BTM nuclear to front-of-meter.

## 6. Grid equipment shortages

- Transformers: power ~128 wks, GSU ~144 wks (WoodMac); LPTs 30–36 mo, EHV up to 60 mo; prices +77% power since 2019. 30% power / 10% distribution deficit 2026. https://www.powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/
- New capacity: Hitachi $457M VA (2028), Siemens Charlotte (2027), Eaton $340M SC (2027).
- Startups: Heron Power $140M (Feb 2026); DG Matrix $60M; Amperesand $80M; Hyperscale Power (Mar 2026).
- MV switchgear 15 kV 52–80 wks; 38 kV 78–104 wks; HV breakers ~125 wks. https://www.industrialsage.com/switchgear-lead-times-2026/

## 7. Cooling, site, opposition

- Rack density 27 kW avg (+69%); GB200 liquid-only; cooling fluids constraining. https://adi-analytics.com/2026/05/07/cooling-fluids-are-constraining-ai-data-centers/
- Powered land: Graham TX $76.5M / 66 acres / 164 MW ≈ $470k/MW premium. Greenfield $11.3–17.6M/MW. https://thetexaslandagent.com/texas-data-center-land-young-county
- NextEra 15 GW at 20–40 hubs by 2035; PPL–Blackstone JV merchant CCGTs; Blackstone $5.34B into Williams BTM gas.
- Opposition: Data Center Watch Q1 2026: 75 projects / $130B blocked or delayed; 843 groups in 49 states; 300+ state bills; >100 local moratoria by mid-2026. https://www.datacenterwatch.org/q1-2026

## 8. Capital

- Nvidia + Apollo/BlackRock/Blackstone/Brookfield/Goldman/KKR (Aug 2026): >$500B platforms. https://nvidianews.nvidia.com/news/nvidia-partners-with-apollo-blackrock-blackstone-brookfield-goldman-sachs-and-kkr-to-establish-ai-compute-infrastructure-financing-platforms-to-mobilize-over-500-billion-of-third-party-capital
- Blackstone $1B into VoltaGrid (May 2026). Crusoe Abilene ~$15B. Solaris $1.25B 7% notes.
- Where returns are made: existing dispatchable capacity in PJM; turbine slot ownership and mobile fleets ($15–75/MWh premium); powered land arbitrage; OEM pricing power. DCs took 78% of built-environment VC in 2025.

## Observed gaps a new company could fill

1. Load-queue de-duplication and realization scoring for utilities/RTOs (KYC for load).
2. Bridging-power-as-a-service in the 20–150 MW gap with published pricing.
3. Secondary/refurbished turbine and engine marketplace with hours-based warranties.
4. Curtailment-monetization and compliance software for SB6 / PJM NITS / SPP HILL (utility-facing telemetry, settlement, audit for colos/neoclouds).
5. Onsite-gas air permitting + emissions-control + community-benefit productized service.
6. Powered-land origination in secondary markets with interconnection-position underwriting.
7. MV switchgear and transformer "kit" manufacturing at 15–38 kV with 20-week delivery.
8. Take-or-pay tariff risk transfer / load-commitment insurance.
9. BTM battery for GPU load-swing smoothing and ride-through compliance (ERCOT flagged 3,200 MW at risk of tripping).
10. Cooling-fluid supply and CDU service.
11. Front-of-meter co-location wrapper for existing PJM IPP plants.
12. Large-load forecast validation for regulators.

Unresolved data gaps: mobile-turbine rental rates; secondary turbine prices; nuclear PPA strike prices; ERCOT Batch Zero results; DR compensation levels.
