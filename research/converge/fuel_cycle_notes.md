# R4 fuel cycle research notes (2026-10-03)
## A. TRISO
- TRISO-X TX-1: NRC SNM-7007 Cat II license 2026-02-13, 40yr; 5 MTU/yr (~700k pebbles, 11 Xe-100s); TX-2 planned 20 MTU/yr; $768M construction; 214,812 sq ft. https://www.powermag.com/triso-x-secures-first-ever-nrc-category-ii-license-for-commercial-advanced-nuclear-fuel-fabrication/
- TX-1 vertical construction complete 2026-09-25 https://nuclear-news.net/2026/10/01/2-b-triso-x-reaches-milestone-in-advanced-nuclear-fuel-facility-construction/
- ORNL ML QA/QC research: https://impact.ornl.gov/en/publications/a-machine-learning-approach-toward-improving-qaqc-of-coated-parti/ ; XCT layer volume method https://www.ornl.gov/publication/method-measurement-triso-kernel-and-layer-volumes-x-ray-computed-tomography ; RU-Net cross sections arXiv 2509.12244 (Sep 2025)
## B. Criticality
- Neutron Bytes 2026-07-31: >5% enrichment loses moderation exclusion 10 CFR 71.55(g); NRC proposed Part 71 rule NRC-2025-1667 comments close 2026-08-26, doesn't touch 71.55/71.59; DNCSH funds 16 projects; DOE $11M to 5 cos for HALEU packages (2-3 yr); Versa-Pac USA/9342/AF-96; Centrus 12 t/yr HALEU by 2029. https://neutronbytes.com/2026/07/31/the-haleu-transport-problem-isnt-radiation-its-criticality/
- Standard Nuclear (NYSE: STDN, IPO Jul 15-17 2026): Q2'26 rev $4.7M; backlog $576.9M total, $119.3M funded (2026-08-26); SN-0 0.5 MTU/yr operating, SN-TN & SN-ID 2.5 MTU each (target 5 MTU), authorization Q4 2026; Framatome JV ~1 MTU/yr from 2027; customers Radiant, Antares. https://www.sec.gov/Archives/edgar/data/2086716/000162828026059143/q2_2026xearningsxpr.htm ; ANS 2026-07-24 https://www.ans.org/news/2026-07-24/article-8241/standard-nuclear-plans-triso-production-at-two-new-facilities-in-2026/
- BWXT: made TRISO for Antares first criticality (announced 2026-06-04), Lynchburg Specialty Fuels; Pele spec. https://www.businesswire.com/news/home/20260604742514/en/BWXT-Manufactures-TRISO-Fuel-Enabling-First-New-Reactor-Criticality-Under-DOE-Program
- TRISO price ~$30,000/kg vs ~$3,300/kg conventional; BWXT $500M Wyoming plant could halve price if operating by 2031 (Canary Media 2026-06-02) https://www.canarymedia.com/articles/nuclear/safer-nuclear-fuel-gaining-steam
- INL cost basis (Sep 2021): TRISO fab $1,000-9,000/kgU, mode $4,000; no QA share given. https://sai.inl.gov/content/uploads/29/2024/11/2021_module_d1-3.pdf
- AGR spec examples: SiC burn-leach defects <=1 in 50,000 (or <=6/120,000); gold spot <=4/31,000; missing OPyC <=1/500; sample sizes 10 to >120,000 particles; QC "generates waste, adds cost". NRC slide deck ML24340A220 (Dec 2024) https://www.nrc.gov/docs/ML2434/ML24340A220.pdf
- ORNL 2009 NRC guidance (Hunn et al.) inspection framework; sample sizes to 100,000 particles; no ML. https://info.ornl.gov/sites/publications/Files/Pub139736.pdf
- ORNL Conry/Helmreich/Gerczak: ML SiC microstructure QC, TopFuel 2025 & JNM vol 626 May 2026 https://impact.ornl.gov/en/publications/methods-development-towards-automated-physics-informed-quantitati/
- INL AUDIT software (2022) kernel defect image processing, licensable; targets BWXT https://inlsoftware.inl.gov/product/audit
- DOE Fuel Line Pilot: Standard Nuclear (Sep 2025), Oklo, Terrestrial, TRISO-X, Valar (2025-09-30) https://www.ans.org/news/2025-10-01/article-7421/four-companies-picked-for-fasttracked-fuel-fabrication/
- Kairos: Pebble Development Lab >50,000 non-nuclear pebbles; LANL LEFFF to start HALEU fuel production 2026; BWXT partner. https://www.kairospower.com/vertical-integration
- No commercial vendor found selling 100% inline TRISO ML inspection (searches 2026-10-03). INL/ORNL research only.
- DOE $11M HALEU package awards 2025-12-08: NAC (both topics), Westinghouse, Container Technologies Industries, American Centrifuge Operating, Paragon D&E; new designs up to 3 yrs. https://www.energy.gov/articles/energy-department-announces-11-million-awards-develop-haleu-transportation-packages
- NCSP FY26-30 plan (2026-03-27): FY26 budget $34.789M, ~$167.4M 5yr; Integral Experiments $20.6M; Training $1.7M; AI/ML only for TSL evals; Whisper/SCALE dev. https://ncsp.llnl.gov/sites/ncsp/files/2026-03/ncsp_five-year_execution_plan_fy2026-2030_-_r5.pdf
- NCS engineer pay avg $154,474 (range $106.5k-186k) ZipRecruiter 2026-10-02 https://www.ziprecruiter.com/Jobs/Locum-Nuclear-Criticality-Safety-Engineer
- ANS NCSD 2005 white paper: min 2 qualified CSEs per facility incl 1 senior; few university sources. https://ncsd.ans.org/file/2159/ncsd_csetng_wp_rev0.pdf
- MIT (Savage, Burnett, Price) arXiv 2606.04033: NN surrogate for sensitivity profiles, inverse critical-experiment design; TN-LC HALEU cask c_k 0.93 for flooded high-poison case that had no benchmark >=0.8. https://arxiv.org/html/2606.04033
- NRC Q3 FY2026 report ML26198A284: Orano Project IKE accepted 2026-05-21 decision Apr 2027; GLE Paducah accepted 2025-08-04 (up to 8%); Radiant R-50 SNM license decision 2026-12-18; Westinghouse CFFF LEU+ pre-app; General Matter LOIs LEU+HALEU; Framatome approved 6.5->10% 2026-06-26. https://www.nrc.gov/docs/ML2619/ML26198A284.pdf
- Everstar $4M pre-seed (Feb 2025) AI nuclear compliance https://www.alleywatch.com/2025/02/everstar-nuclear-compliance-ai-acceleration-automation-platform-kevin-kong/
- DNCSH (NRC slides ML24260A114, 2024-07-31): up to $60M of IRA $700M; Call 1 30 proposals/$28M; 39% on 10-20% enrichment gap; goal fewer RAIs on code validation. https://www.nrc.gov/docs/ML2426/ML24260A114.pdf
- AI licensing startups (Neutron Bytes 2026-03-28): Everstar (Gordian, 208-pg safety doc in 1 day vs 4-6 wks), Atomic Canyon, Nuclearn, Blue Wave AI Labs (Eigenvalue.ai for BWR reload; Constellation), Inductive. None do criticality. https://neutronbytes.com/2026/03/28/using-ai-to-reduce-reactor-licensing-timelines/
- DOE $2.7B enrichment awards 2026-01-06: ACO $900M HALEU, General Matter $900M HALEU (ops by 2034), Orano $900M LEU (prod 2031), GLE $28.5M. https://www.ans.org/news/article-7652/doe-awards-27b-for-haleu-and-leu-enrichment/
- General Matter NCS engineer posting $80k-170k + options, SCALE/MCNP, ANSI/ANS-8.24 preferred https://job-boards.greenhouse.io/generalmatter/jobs/4487697008
- Oklo Aurora Fuel Fab Facility PDSA approved by DOE (2025-12-16) https://www.businesswire.com/news/home/20251216070998/en/
## C. Fuel qualification
- AFQ white paper (Framatome, GA, INL, LANL, ORNL, Westinghouse; 2021-10-01): traditional qual >20 yrs; AFQ target ~5 yrs; FAST 12 yrs -> 1-3 yrs; MiniFuel <4 mm3 in HFIR; ROMs/UQ central. https://www.nrc.gov/docs/ML2128/ML21287A646.pdf
- AGR TRISO program started 2002; ~1,000,000 particles irradiated in ATR; failure <=1/50,000 (INL May 2024) https://nrds.inl.gov/dataset/nsuf_user_development_workshop_on_irradiation_testing/resource/4a0c8add-1736-4111-8abf-fbf58e72bb15/download/doe-triso-fuel-qualification.pdf
- ATR: 250 MWt max, typically ~110 MWt; 77 positions (70 available) + 34 low-flux; 60 EFPD cycles + 28-35 day outages; min 6 months design->insertion for simple capsule. https://inl.gov/content/uploads/2023/07/20-50097_ATR_UserGuide_R24.pdf ; 6th CIC Apr 2021-Mar 2022 (~every 10 yrs) https://www.energy.gov/ne/articles/idaho-national-laboratory-completes-sixth-core-overhaul-advanced-test-reactor
- MITR: 6 MWt, 3 in-core positions (Nov 2023) https://asi.inl.gov/content/uploads/47/2025/05/Irradiation-Capabilities-at-the-MIT-Nuclear-Reactor-1.pdf
- HFIR paper (Aug 2026) addresses "growing fuel-testing backlog" https://interestingengineering.com/energy/us-nuclear-push-hfir-reactor-fuels
- ALEO NEUP (UTSA + ORNL, 2023-): active learning DOE for HFIR MiniFuel https://impact.ornl.gov/en/projects/active-learning-estimation-and-optimization-aleo-of-irradiation-e-3/
- LANL Bayesian + ML UO2 creep (2025-11-18), NEAMS + Westinghouse https://www.lanl.gov/media/newsletters/ste-highlights/11-2025-nuclear-reactor-fuel
- ORNL agentic AI for AFQ, JNM 631, Sep 2026 https://impact.ornl.gov/en/publications/agentic-ai-for-accelerated-fuel-qualification-framework-demonstra/
- DOE Genesis Mission Project Prometheus 2026-07-24: $60M/3 yrs fed, $200M+ industry cost share; 32 partners incl X-energy, TerraPower, Oklo, NVIDIA; targets 3x faster fuel fabrication, 10x licensing. https://neutronbytes.com/2026/07/24/doe-launches-60m-ai-initiative-to-speed-up-deployment-of-nuclear-energy-in-the-u-s/
- Oklo fuel qualification topical pre-sub meeting 2025-09-17 https://www.nrc.gov/public-involve/public-meetings/pmns/20251095
- NUREG-2246 final March 2022 https://www.nrc.gov/docs/ML2206/ML22063A131.pdf
- Nuclearn $10.5M Series A (Sep 2025) https://www.ans.org/news/2025-09-10/article-7356/ai-startup-nuclearn-nets-105m-in-series-a-funding/
- Prior art A: Du et al. 2014 NED 280:144-149 automatic X-ray inspection of HTR-PM spherical fuel elements (China INET) https://www.sciencedirect.com/science/article/abs/pii/S0029549314005275
- X-energy confirmatory ATR irradiation of TRISO-X pebbles began 2025-11-06, 13-month program https://x-energy.com/media/news-releases/x-energy-begins-commercial-qualification-testing-for-triso-x-fuel-at-idaho-national-laboratory
## STATUS: research complete, final report being written (2026-10-03)
