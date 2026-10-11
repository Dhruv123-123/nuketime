# Nuclear ML/software hunt: research notes (2026-10-11)

Raw findings from three capped research agents (15 searches each) behind `PICK6.md`. Items marked
[unverified] were not confirmed by a fetched source.

## A. Competitors in nuclear engineering AI (as of Oct 2026)

| Name | Funding | Lane | Traction | Source |
|---|---|---|---|---|
| Nuclearn | $10.5M Series A, Sep 2025 (Blue Bear) | CAP AI, AtomAssist, 50.59 screening feature (Aug 2025), design-mod review "in development", Parts AI (Feb 2026), certified service providers | 65+ reactors claimed; no uprate product | techcrunch.com/2025/09/09/nuclearn-gets-10-5m-to-help-the-nuclear-industry-embrace-ai ; nuclearn.ai/2025/08/04/confident-engineering-starts-here-inside-nuclearns-50-59-feature/ |
| Atomic Canyon | $7M seed May 2025; NVIDIA, Plug and Play, Tim Buckley Aug 2026 (undisclosed) | Search/knowledge (Neutron, FERMI, NIVA) | NIVA fleetwide via INPO/EPRI/NEI Aug 2026; no calc/50.59/uprate | atomic-canyon.com/news/2026-08-18-niva-fleetwide-launch/ |
| Everstar (Gordian) | $4M pre-seed 2025; no later round found | New-build licensing documents; Genesis Mission with INL/ANL/Microsoft (Mar 2026): 208-page NRC-style section in ~1 day vs 4-6 weeks | Unnamed developers and utilities | prnewswire.com/news-releases/everstar-announces-collaboration-with-doe-national-laboratories-and-microsoft--marking-its-first-major-milestone-in-the-genesis-mission-302726497.html |
| Westinghouse bertha / HiVE | internal, Google Cloud | Licensing LLM; bertha embedded in CMIS (configuration management in OptiLife); planned first NRC submittal of an AI/ML DNB/CHF model | CMIS widely used | westinghousenuclear.com/innovation/westinghouse-ai/ |
| Alva Energy | $33M Series A, Feb 2026 (Playground Global, 8VC, NGP...) | Turnkey uprate developer: SG replacement + second turbine, 200-300 MWe/reactor, 10 GWe target; no AI angle | No named utility deals; first projects ~5 yrs out | powermag.com/nuclear-power-group-alva-energy-launches-with-33-million-in-funding/ |
| Inductive [unverified] | unknown | "TurboTax for nuclear licensing" | unknown | neutronbytes.com/2026/03/28/using-ai-to-reduce-reactor-licensing-timelines/ |
| Blue Wave AI Labs | ~$6.9M incl. DOE $6M | Core/thermal-limits ML | Constellation BWRs | same |

Incumbent A/Es (Sargent & Lundy, Enercon, Jensen Hughes): no AI automation for uprate or design-basis work announced.

Open (no AI-native player found): uprate engineering itself (heat balance, NSSS/BOP calcs, EPU LAR
analysis package, the calc revisions an uprate triggers); design-basis reconstitution and
calculation-of-record management; SLR aging-management review drafting; restart engineering packages;
AI-native engineering services delivering stamped work product.

## B. Market signals

- Enercon: Arlington Capital majority stake on about $1.25B of equity, 29 Apr 2026, merging with Pond & Co. into 2,700+ staff. energyconnects.com/news/utilities/2026/april/arlington-capital-acquires-nuclear-engineering-firm-enercon/
- Jensen Hughes: New Mountain buying from Gryphon (Aug 2026), ~2,000 staff. app.dealroom.co/news/note/new-mountain-to-buy-fire-and-nuclear-engineering-firm-jensen-hughes-from-gryphon
- NEI Costs in Context (Aug 2026): US fleet capex $7.59B in 2025 ($6.10B in 2024), $9.69/MWh; opex $20.82/MWh.
- NRC expected uprates (page fetched 2026-10-11): 30 listed applications Q4 2026 to Q3 2032; McGuire 1-2, Hatch 1-2 EPUs and Salem SPU Q2 2027; Columbia, Catawba 1 2028; Vogtle 1-2 EPU Q4 2028; Perry 2029; Beaver Valley 2030-31; Davis-Besse 2032; 7,336 MWt total.
- About 160 planned digital I&C upgrades across the US fleet (Baird, NECX 2026) [figure from agent, page not re-checked].
- DOE UPRISE (12 Mar 2026): 2.5 GW by 2027, 5 GW by 2029; DOE's Rian Bahran named engineering schedule and staffing among "the bottlenecks for accelerating uprates and restarts"; up to 80% financing. powermag.com/doe-unveils-initiative-to-add-5-gw-of-nuclear-capacity-through-uprates-and-restarts/
- Baird NECX 2026: "Maintenance, engineering and other nuclear services companies ... arguably the clearest near-term commercial beneficiaries of the buildout."
- Not found: sourced engineering cost of an EPU or SLR application (rules of thumb $20-30M+ per renewal application are [unverified]).

## C. Alternatives checked and ranked below the uprate/design-basis engine

1. Decommissioning characterisation and waste classification (geostatistics). DOE EM FY2026 ~$8.6B, FY2027 request $8.2B (exchangemonitor.com/white-house-requests-8-2b-for-em-slightly-less-than-fiscal-2026/). UK class costs: hundreds of GBP/m3 VLLW, thousands LLW, tens of thousands ILW (NEI Magazine 2010). Characterisation bought as small services contracts (Cavendish GBP 2.4M Sellafield). PNNL Visual Sample Plan is free. No venture-backed startup found. Best ML fit and least crowded, weak path to $300M/yr unless priced on avoided disposal cost. Kept as second product.
2. Remote ops for microreactors. NRC proposed Part 57 (comments closed 15 Jun 2026) allows remote and autonomous operation (bdlaw.com/publications/nrc-proposes-new-licensing-framework-for-microreactors/); NuCube+Argonne GAIN voucher; INL MARVEL remote-ops tests; vendors treat autonomy as core IP; fleets unlikely before 2029-31 [unverified]. Late.
3. Online monitoring for calibration/surveillance intervals: AMS and EPRI own the path; ~90 US units; no $300M path.
4. ML fuel qualification: Oklo+NVIDIA+LANL (Apr 2026), X-energy Project Prometheus; ~10 buyers building in-house with labs. Crowded, grant-heavy.
5. Supply-chain qualification: NSI report Mar 2026; poor ML fit (already PICK3).

## D. Uprate economics (agent report, 2026-10-11)

1. NRC expected applications (updated 8 Sep 2026): 31 submittals 2026-2032 (10 MUR, 2 SPU, 19 EPU), 7,336 MWt = ~2,421 MWe; by year 2026 335 MWe, 2027 875, 2028 635, 2029 197, 2030 249, 2031 66, 2032 65. NRC has approved 172 uprates since 1977 (~8 GWe).
2. Google-Constellation (6 Oct 2026): 20-yr PPA for 890 MW of uprates at 11 units on 6 sites, >$4.3B capex, first MW 2028, all by end 2032; Constellation expects 12 filings (5 EPU, 7 MUR) Q4 2026-2030. powermag.com/google-deal-backs-890-mw-of-constellation-nuclear-uprates-at-11-pjm-reactors/
3. Amazon-Constellation Calvert Cliffs: 690 MW PPA incl. ~190 MW uprates, >$3B incl. life extension, 2030-32. Walmart-Constellation Dresden: 30 MW uprate 2029-30.
4. Meta-Vistra (Jan 2026): >2,600 MW PPAs incl. 433 MW uprates through 2034 at Beaver Valley, Davis-Besse, Perry, plus SLR at all three; DOE conditional loan up to $4.2B (Oct 2026). ans.org/news/2026-01-12/article-7668/the-metavistra-deal-a-closer-look/
5. Meta-Constellation Clinton (Jun 2025): 30 MW uprate. Google-Georgia Power NU-1 (22 Sep 2026): ~96 MW at Vogtle 1-2, Hatch 1-2.
6. Columbia EPU (BPA, May 2025): 162 MW + 24 MW efficiency = 186 MW, ~$700M, done 2031, 18 months of analysis before approval, ~30 modifications. power-eng.com/nuclear/washington-state-nuclear-plant-approved-for-700m-upgrade-to-boost-output/
7. INL LWRS (Apr 2025) $/kW: MUR 500-800, SPU 800-1,500, EPU 1,500-2,500, up to 5,000 with major mods. Real deals: Constellation-Google ~$4,800/kW, Columbia ~$3,800/kW. lwrs.inl.gov/content/uploads/11/2025/04/26_Larger-Power-Uprates_rev1.pdf
8. NRC review targets MUR 6, SPU 9, EPU 12 months (May 2024 letter to NEI); achieved 2025-26 times not verified.
9. Engineering share of uprate capex: no public source; agent estimate 10-20% EPU, 30-50% MUR [unverified].
10. PPA prices: Meta-Clinton ~$70/MWh; Microsoft-Crane $98-115; Constellation guidance $80-88. 1 MW-month ~680 MWh at 93% CF -> ~$58k/MW-month at $85/MWh.
11. Outside US: Bruce A +125 MW (Siemens HP turbines, 2028-31); Olkiluoto 1-2 +80 MWe each under study; no verified EDF/KHNP figures; no credible global potential estimate.
12. Agent estimate [unverified]: global uprates to 2035 ~6-9 GWe; engineering spend ~$2-6B total ($200-600M/yr).
