# Lane D: fewer, smarter holes (in-hole sensing, core scanning, directional drilling, ML/VOI placement)

Written 19 October 2026. Research cut short by the shared web-search budget (200 calls per turn across all agents ran
out partway through). Gaps are listed at the end. Items marked (memory) or (estimate) are not web-verified.

## Summary (the 10 lines that matter)

1. Baseline: MinEx Consulting (Schodde, March 2019) puts the world average at about 700,000 m of drilling and about
   US$200M per new Moderate-or-larger deposit, up from about 200,000 m in 1985. https://minexconsulting.com/?p=933
2. The best published evidence that sequencing holes well cuts the count is Stanford/KoBold's "Intelligent Prospector v2"
   (Mern, Corso, Burch, Kurt House [KoBold CEO], Caers, arXiv 2410.10610). In simulation it reached the same go/no-go
   accuracy with "less than half as many boreholes" as a 6x6 grid, and the authors say it aided Mingomba appraisal in
   2023. The evidence is simulation only, there is no disclosed field count, and the main author is the company that profits from it.
3. KoBold's field claim: 8 of 10 isolated Quebec holes hit Ni-sulfide, "easily 10 times better than the industry average"
   (self-reported, IEEE Spectrum). Earth AI claims a 75% discovery rate against an industry 0.5% (its own press release, unaudited).
   I found no independent, peer-reviewed study showing that ML targeting raised drill hit rates.
4. At-rig and in-hole sensing is already owned and consolidated. Imdex (A$431M revenue in FY25, 66% from sensors and SaaS) owns
   Reflex, Devico (directional/daughter holes), Datarock (core-image AI) and Lab-at-Rig. Epiroc owns Corescan. Boart
   Longyear/Veracio bought Minalyze for US$29.3M. GeologicAI raised a US$44M Series B with BHP and Rio.
5. Ceiling check: Imdex captures about A$2.40 of every A$100 of drilling spend (its FY26 "share of wallet"). That is a hard read on
   the size of the "make each hole more informative" tool market. It is a large-tool business, not a rubric-#6 company.
6. Exit prices confirm this: Corescan had about MSEK 65 of revenue at exit, Minalyze sold for US$29.3M, Datarock for about A$31M for the last
   49%, and Seequent (Leapfrog) for US$1.05B at about 13x on about US$80M revenue. Seequent is the ceiling for pure software in this lane.
7. Uranium-specific: the Athabasca already has "lab at rig" for free. Calibrated downhole gamma probes give in-situ eU3O8
   during the program (they saturate at high grade and need assay confirmation). So the at-rig sensing pain is smaller in
   uranium than in base metals. The remaining pain is where to put the next hole on a conductor fence, and whether to wedge.
8. Directional/daughter holes are a mature, owned product (Devico under Imdex). The one hard number is SolGold Alpala:
   about 24,000 m and about US$12M saved (client testimonial). Areva/UEX already used daughter holes at Shea Creek.
9. "Fewer, smarter holes" as a decision engine is what targeting companies already do: KoBold (in-house POMDP), Earth AI
   (own drill rigs), VerAI (paid in NSR royalties), VRIFY DORA, and Terranox. It is a Terranox feature, not a new company.
10. Possible unowned slot: a sequential drill-planning engine for third-party juniors, paid by success fee or royalty. VerAI already
    does the royalty version, and that slot only becomes big by owning the asset, which brings it back to the Terranox/KoBold model.
    Verdict: no separate venture-scale company here. Build it inside Terranox.

---

## 1. Baseline: how many metres and holes per discovery

| Metric | Value | Source |
|---|---|---|
| Drilling per new deposit (world, Moderate+), c.2018 | ~700,000 m, 2.8x the previous decade; ~200,000 m in 1985 | MinEx/Schodde, AMIRA, Mar 2019, https://minexconsulting.com/?p=933 |
| Cost per discovery (world) | ~US$200M (3.8x the previous decade); US$60-80M before 2005 | same |
| Global metres drilled | 47M m in 2018, down from a 94M m peak in 2012 | same |
| Australia, significant discovery | 600,000 m (vs 400,000 m in 1980) | MinEx 2015, https://minexconsulting.com/?p=758 |
| Uranium unit discovery cost (Australia) | ~A$4/lb U3O8 | same |
| Saskatchewan average drilling cost 2024 | ~C$383/m (all commodities; ON C$208, QC C$295, BC C$364, YT C$537) | aggregator, https://farmonaut.com/mining/mineral-exploration-spending-canada-nrcan-data (quality low; claims NRCan basis) |
| Athabasca all-in, deep unconformity holes | C$400-700/m (estimate, memory), so a 600-800 m hole costs ~C$0.3-0.5M | (estimate) |
| Athabasca program scale | NexGen 34,000 m Patterson Corridor East 2024 (largest in basin), 43,000 m planned 2025; Denison winter: 30,400 m in 32 holes (~950 m/hole) | https://mugglehead.com/?p=1381196 ; https://canadianminingjournal.com/news/uranium-denison-wraps-up-successful-winter-drilling-program |

Implication: at ~700,000 m and C$400+/m, a "discovery" costs C$280M+ in drilling alone (estimate). A 2x cut in holes per
decision, the size IPv2 shows in simulation, is worth a lot per discovery. But the saving lands with whoever owns the
ground, not with a tool vendor.

---

## 2. In-hole and at-rig sensing

### Imdex (ASX: IMD), the consolidator
- FY25 (to 30 June 2025): revenue A$431M, normalised EBITDA A$126M (29%), sensors and SaaS 66% of revenue.
  https://filingreader.com/news-wire/sydney/2025-10-16/imdex-reports-resilient-fy25-performance-strong-1q26-growth ;
  https://announcements.asx.com.au/asxpdf/20250825/pdf/06n7yv6xhvmxsb.pdf
- FY26: record "share of wallet" of A$2.40 per A$100 of drilling spend (up from A$2.20); Imdex Mining Technologies revenue +32%;
  next-generation tools 12% of the fleet. https://bulletin.webull.com/qbd/announcement/20260817/499501201/e15aba0f48c62ae115eef059c8188c5f.pdf
- Brands: REFLEX (downhole survey and orientation, plus the Lab-at-Rig commercialisation), Devico/DeviDrill (directional core drilling,
  now hosted at imdex.com/directional-drilling/devidrill), Datarock (core-image AI), BLAST DOG (blast-hole sensing for mine
  production, not exploration; first contract about A$13M at Iron Bridge in 2022). https://www.imdex.com/news-knowledge/news/deal-on-blast-dog-caps-off-record-year-for-imdex
- Takeaway: anything sensor-shaped that bolts onto a rig ends up as an Imdex SKU. A share of wallet of 2.4% is the market telling you
  what "more informative holes" is worth to the driller and explorer as a tool.

### DET CRC Lab-at-Rig and RoXplorer
- Lab-at-Rig: XRF/XRD on dried cuttings from the solids-removal unit, with about a 1-hour result cycle. CSIRO/Imdex/Olympus built it, and it was licensed to
  Imdex/REFLEX in 2015. https://www.csiro.au/en/research/production/materials/resource-characterisation-developments/lab-at-rig
- RoXplorer coiled-tubing rig: claimed about 1/6 the cost of diamond drilling, licensed to Imdex in 2018. Its developer said in 2017 that it was
  "years away realistically". DET CRC closed on 30 June 2018. https://www.globalminingreview.com/mining/07082018/revolutionary-new-drill-rig-licensed-to-imdex/ ;
  https://magazine.cim.org/en/technology/reel-disruption
- I found no 2019+ evidence of fleet-scale commercial use of either. The follow-on was an A$11M "Lab-at-Rig Futures" project (CSIRO page).
- Evidence of fewer metres per discovery: none found. Its value case was cutting assay turnaround from weeks to hours, so a program can stop or redirect
  a hole while the rig is still on it.

### Downhole spectral gamma and uranium probes (Athabasca relevance)
- Standard practice already: calibrated downhole gamma probes (for example Mount Sopris QL40 spectral gamma, calibrated at SRC Saskatoon
  test pits) give in-situ eU3O8 during the program. Denison-style disclosures report eU3O8 "estimated in-situ ... using calibrated
  down-hole radiometric gamma probes". https://www.sec.gov/Archives/edgar/data/1334933/000143774924002695/ex_621334.htm ;
  https://myriaduranium.com/myriad-uranium-reports-chemical-assays-on-20-copper-mountain-boreholes-confirmed-u3o8-grades-are-20-higher-on-average-than-previously-reported-gamma-grades-assays-also-reveal-the-presence-of-extensi/
- Limits: probes saturate in high-grade intervals and disequilibrium matters. In one Myriad case gamma gave 343.8 ppm eU3O8 against an
  832.5 ppm chemical assay. Assays are still required.
- Implication: in uranium the "real-time grade at the rig" problem is already mostly solved and cheap (memory: the probes are commodity
  hardware run by small Saskatoon logging contractors). There is no venture-scale gap here.

### Borehole EM / DC resistivity / radar
- Athabasca use is routine. Uravan's Stewardson program ran borehole pulse EM (Geonics BH-43-3D) through Discovery International
  Geophysics (Saskatoon), and Cameco supplied downhole resistivity equipment. https://newswire.ca/news-releases/uravan-completes-stewardson-drill-program-515798381.html
- GSC EXTECH IV showed that inductive conductivity logs in plastic-cased holes at Shea Creek delineate graphitic conductors.
  https://www.download-telecharger.services.geo.ca/pub/nrcan_rncan/vector/gsc_sem/extech-IV/vsp/summary2000_with_figs.doc
- DHEM in general is a service-contractor market (Crone, Discovery, Abitibi, EMIT software; memory). Borehole radar is niche
  (memory). These are mature, fragmented services, and I found no metres-per-discovery evidence for them.

### Muon tomography from boreholes: Ideon Technologies (Vancouver)
- Funding: C$1.3M seed (2020) https://ideon.ai/earth-x-ray-pioneer-ideon-technologies-closes-1-3m-in-seed-funding/ ; US$16M Series A,
  Sept 2022, led by Playground Global https://techcrunch.com/2022/09/19/ideon-technologies-digs-up-16m-series-a-to-use-particle-physics-to-find-critical-minerals ;
  aggregators put the total at US$23-27M (https://bouncewatch.com/company/ideon-technologies). I could not fetch a 2026 Business Wire release (403).
- Traction: a 2026 release lists Rio Tinto, Freeport, BHP, Glencore and Vale Base Metals as partners. BHP is a repeat client (fifth survey after a blind
  nickel trial). Uranium: it has worked with Orano since 2016, and in May 2023 delivered what it calls the world's first borehole muon tomography project for exploration,
  at McClean Lake, Saskatchewan. The idea came from founder Brian Powell while he was at Cameco in the Athabasca.
  https://www.mining.com/ideon-technologies-aims-to-take-some-of-the-guesswork-out-of-mineral-exploration/ ; https://ideon.ai/about/our-story/
- Why it is relevant to fewer holes: one HQ hole becomes a density image of a volume around it, which turns a miss into a vector.
  Athabasca high-grade pods are dense, so the physics fits.
- Evidence of fewer metres per discovery: none published. It is still survey-by-survey.
- Rubric: closest thing in this lane to "ML/physics makes it possible at all". But it sells a service per survey (a tool market).
  It already exists in Saskatchewan with Orano, so the slot is owned.

---

## 3. Core scanning

| Company | What | Funding / exit | Traction | Fewer metres? |
|---|---|---|---|---|
| Minalyze (SE) | Continuous XRF + imagery + structure on core trays (Minalyzer CS, 2014) | ~US$1.5M raised; sold to Veracio (Boart Longyear) for US$29.3M, Sep 2023 https://mynewsdesk.com/se/chalmers-ventures/pressreleases/chalmers-ventures-portfoeljbolag-minalyze-foervaervas-av-veracio-3274205 ; https://www.cbinsights.com/company/minalyze | Used via Intertek labs, among others | No evidence |
| Corescan (AU) | Hyperspectral + photo + 3D laser core scanning; Coreshed | Sold to Epiroc, Oct 2022; ~50 staff, 2021 revenue ~MSEK 65 (~US$7M) https://www.epirocgroup.com/en/media/corporate-press-releases/2022/20221007-epiroc-to-acquire-australian-provider-of-digital-core-imaging-solutions-for-mining-companies | Majors | No evidence |
| GeologicAI (CA) | XRF + hyperspectral + RGB + ML, real-time core analysis, 24-48 h turnaround | US$10M Series A 2023 (BEV, EDC); US$44M Series B Jul 2025 led by Blue Earth, with BHP Ventures and Rio Tinto https://www.businesswire.com/news/home/20250714636265/en/GeologicAI-Raises-%2444-Million-USD-Series-B-to-Accelerate-AI-Driven-Discovery-and-Development-of-Critical-Minerals-Globally | Best-funded independent | No evidence published |
| Datarock (AU) | Deep learning on core imagery (Datarock Core) | Imdex 30% for A$5.5M in 2021 at ~A$2M revenue; 51% by Jul 2024; 100% Feb 2026 for ~A$31M https://www.investmets.com/?p=2585 ; https://www.imdex.com/news-knowledge/news/imdex-completes-datarock-acquisition-accelerating-digital-earth-knowledge-expansion | Imdex channel | No evidence |
| Plotlogic (AU) | Hyperspectral ore characterisation at the mine face (OreSense) | US$28M Series B Jul 2023 (Galvanize, SE Ventures, DCVC) https://dcvc.com/press-releases/top-sustainability-vcs-lead-us28-million-series-b-for-australian-breakthrough-mining-tech-plotlogic | BHP, Vale, South32, Pilbara: production, not exploration | Not applicable |
| TerraCore (US/ZA) | Hyperspectral core imaging services; 2015 merger with GeoSpectral Imaging | No transaction found https://nnbw.com/news/2018/mar/02/reno-based-terracore-aims-to-bring-mining-industry | Services | No evidence |
| Spectra-Map (UK) | Hyperspectral core | Bought by Geotek 2021 https://www.geotek.co.uk/2021/09/24/geotek-limited-acquires-spectra-map-limited-a-specialist-hyperspectral-core-scanning-services-company/ | Niche | No evidence |

Read: core scanning is a consolidated, sub-US$50M-exit tool market. GeologicAI is the only independent with venture
money. None publishes metres saved per discovery. Their pitch is speed and consistency of logging, not fewer holes.
Athabasca note: alteration mineralogy (illite/kaolinite/chlorite/dravite halos) from SWIR on core is a known vector to
unconformity deposits (memory). Hyperspectral scanning does help decide the next hole, but it is a service anyone can buy.

---

## 4. Directional drilling and daughter holes / wedging

- Devico (Norway), DeviDrill directional core drilling, branches from a mother hole. Now an Imdex brand (Imdex hosts the product page,
  https://www.imdex.com/directional-drilling/devidrill ; acquisition in about 2022 is from memory).
- Hard number: SolGold Alpala, "a saving of 23,997.6m of drilling, or approximately $12M USD" (client testimonial, so promotional).
  https://devico.com/drill-less-hit-more . Sakatti (Anglo American): nine targets cut from one pilot hole.
  https://www.imdex.com/getmedia/9c2b8181-e281-45c4-8c9f-3896dd21df42/DeviDrill-DCD-case-study-directional-drilling-program-of-high-technical-quality.pdf
- A Devico patent says each daughter hole typically saves 4-5 weeks against re-drilling from surface. https://patents.google.com/patent/US12084970
- Athabasca precedent: Areva/UEX Shea Creek ran directional holes off pilot holes to test extensions, and the Kianna East discovery came
  from five directional holes. https://www.northernminer.com/news/areva-uex-jv-cuts-more-high-grade-uranium-at-shea-creek/1000205723/
- Reflex (Imdex) supplies the gyro/survey tools that make wedging accurate.
- Verdict: owned (Imdex) and adopted. For deep Athabasca holes (500-1,000 m of sandstone before the unconformity), daughter holes are
  the obvious metre-saver, and operators already use them. The savings are real but go to the explorer. The tool is a contractor product.

---

## 5. Drill-target placement by ML / value-of-information / Bayesian experimental design

### Academic and the one quantitative result
- Intelligent Prospector v1 (Mern & Caers, GMD 2023) frames data acquisition as a POMDP, "playing chess against nature".
  https://gmd.copernicus.org/articles/16/289/2023/
- Intelligent Prospector v2 (Mern, Corso, Burch, House, Caers; arXiv 2410.10610, Oct 2024) https://arxiv.org/abs/2410.10610v1
  - Simulation on 17 ground-truth models against a 6x6 grid (36 holes): "For the same decision accuracy, the POMDP needed less than half
    as many boreholes as grid-based drilling". Convergence in one example came after about 9 holes, against 35 for the grid. It also falsified wrong geological
    hypotheses faster (after 2 and 7 holes in the example).
  - Field claim: it "aided in the characterization of an ultra high-grade deposit in Zambia in 2023" (Mingomba). The authors say that because of
    ongoing appraisal "we cannot disclose" field details. There are no field hole counts.
  - Caveat: the drill cost and economics are toy values (cut-off 6, drill cost 0.1). The comparison is against a naive grid, not against a good
    human geologist. Kurt House, KoBold's CEO, is a co-author.
- Tyler Hall's Stanford thesis covers a sequential-VOI greenfield drilling case in Western Australia. https://purl.stanford.edu/pm892rp3036
- ML prospectivity validated by later drilling is rare in the literature. The clearest example I found: Tongling, China (Ore Geology Reviews 2019),
  where two newly found deposits fell inside the SVM/RF/ANN prospective zones. That is retrospective, with no hit-rate statistic.
  https://www.sciencedirect.com/science/article/pii/S0169136818307406 . A 2025 review says practically validated ML workflows are
  "confined to supporting tasks". https://doi.org/10.3390/min15101042

### Companies

| Company | Model | Funding | Claimed hit rate / evidence | Independent? |
|---|---|---|---|---|
| KoBold Metals | Own the ground; ML + "efficacy of information" drill planning (IPv2 in-house) | US$537M Series C at US$2.96B (Jan 2025) https://www.miningweekly.com/article/gates-backed-kobold-metals-raises-537m-in-funding-round-2025-01-06 ; ~US$280M C-III extension Nov 2025, secondary-implied ~US$4.17B (unverified) https://sacra.com/c/kobold-metals/ | Quebec: 8/10 isolated holes hit Ni-sulfide, "easily 10x" the industry rate https://spectrum.ieee.org/ai-mining ; Mingomba passed 100,000 m drilled; reported 247Mt @ 3.6% Cu (media) https://www.mining.com/gates-bezos-backed-kobold-says-zambia-copper-find-largest-in-a-century/ | No. Self-reported; little technical disclosure |
| Earth AI (YC) | Own the ground and the rigs (mobile low-disturbance drill at about US$100/m) | US$20M Series B, Jan 2025 (Tamarack, Cantos, YC) https://www.globalminingreview.com/mining/31012025/earth-ai-raises-us20-million-for-ai-driven-mineral-exploration/ | "75% discovery success rate" against an "estimated industry average of 0.5%"; Legacy Minerals palladium system (Nov 2024), Willow Glen gold (Dec 2024) https://pulse2.com/earth-ai-clean-energy-metals-company-raises-20-million | No. "Discovery" is undefined; the 0.5% denominator is not comparable |
| VerAI Discoveries | Targets on other people's ground, paid in NSR royalty | US$12M Series A, Mar 2023 (T. Rowe, Orion, Chrysalix) https://www.chrysalix.com/news/ai-powered-mineral-discovery-technology-company-verai-raises-12m-to-radically-improve-the-ability-to-locate-concealed-minerals-critical-for-a-sustainable-future | Conquest Belfast-TeckMag: "at least three of the four AI-derived targets intersected a potential mineralized system"; 1.5% + 1.5% NSR https://www.newsfilecorp.com/release/240334/Conquest-Drill-Testing-of-VerAI-AIgenerated-Targets-Identifies-Potential-VMS-System-at-Its-BelfastTeckMag-Project | Partner press release |
| VRIFY (DORA) | SaaS/service prospectivity scoring (VPS) for juniors | ~US$8.66M (Feb 2025) per CB Insights summary | RUA Gold first two holes hit (vendor case study) https://vrify.com/case-studies/how-ai-optimized-rua-golds-exploration-strategy ; Cartier ~25% of 100,000 m on DORA targets | Vendor |
| GoldSpot Discoveries / ResGold | AI targeting service plus royalty/equity stakes | Not found | Single-hole highlights (New Found Queensway 19 m @ 92.86 g/t was the first of 10 recon holes); Courcy produced 28 targets, with no outcome stats https://www.newsfilecorp.com/release/119237 | No hit-rate disclosure. I did not verify the ResGold rename/status |
| Minerva Intelligence | Knowledge-graph geology AI | C$4.5M equity; geology division sold to Seequent Dec 2022 https://www.cbinsights.com/company/minerva-intelligence-geology-division | No data | Absorbed |
| Mira Geoscience | 3D modelling/inversion consultancy plus software (Geoscience ANALYST, AI agent, bought HiveMap from SRK) https://www.newsfilecorp.com/release/282533 | Private, no data | No data | Consultancy |
| Seequent (Leapfrog) | 3D geological modelling, the standard workspace where holes get planned | Bought by Bentley for ~US$1.05B (2021), ~US$80M revenue implied, ~13x https://schnitgercorp.com/2021/03/11/bentley-acquires-seequent-for-1-05-billion/ | Not applicable | Software ceiling |
| Sumitomo | Not researched (search budget ran out) | | | |

Read: no one has independent, audited evidence that ML raises the hit rate of drill holes. The strongest real-world signal
(Mingomba) belongs to a company that owns the asset and does not publish the counterfactual. Every player that only sells
targets (VerAI, VRIFY, GoldSpot, Minerva) is small or got absorbed. The players that own the ground (KoBold, Earth AI) are the
ones with scale, which is evidence for rubric points 3-4: the value sits in the land step-up, not in the targeting service.

---

## 6. Key question: separate company, or what targeting companies already do?

**It is what targeting companies already do.** "Fewer, smarter holes" splits into three layers, and each one is owned:

1. **Hardware/sensor layer** (probes, at-rig XRF, core scanners, gyros, wedges, muon detectors). Owned by Imdex (Reflex, Devico,
   Datarock, Lab-at-Rig), Epiroc (Corescan), Boart/Veracio (Minalyze), GeologicAI and Ideon. The market ceiling is about 2.4% of drilling
   spend (Imdex's own share-of-wallet figure), and exits run US$7M-revenue to US$30M deals. This fails rubric #6. In uranium, the probe
   layer is already a commodity.
2. **Modelling workspace** (where holes get designed): Seequent/Leapfrog, Mira and Geosoft. This tops out at about US$1B (Seequent). It is owned.
3. **Decision layer** (where to drill the next hole, when to stop, when to wedge, given all prior holes): this is sequential
   Bayesian experimental design. KoBold has it in-house (IPv2), the Stanford Mineral-X group publishes it, and VerAI, VRIFY DORA and Earth AI
   sell or use cruder versions. For Terranox, this is the same model it already runs on SMAD, extended from "where to stake"
   to "where to put hole n+1". It is a feature of a targeting company, not a separate product.

**Is there an unowned position?** Only narrow ones:
- **Athabasca-specific sequential drill planner sold to third-party juniors** (Denison, IsoEnergy, Cosa, Standard Uranium and others
  drilling conductor fences at about C$0.3-0.5M a hole, estimate). Nobody sells a POMDP drill planner for unconformity uranium (none found).
  But the buyer base is a few dozen juniors spending about C$100-300M a year in total on basin drilling (estimate), so a services ceiling.
  The only way to make it large is to take carried interest or royalties (the VerAI model), which turns it into Terranox.
- **Muon or density imaging from existing holes in the basin.** Ideon already does this with Orano at McClean Lake. Owned.
- **Re-logging legacy SMAD holes** (gamma logs, core photos, assessment-file drill logs) to rank old misses as near-misses. This is the
  "public but illegible data" play (rubric #2), but it is literally Terranox's input pipeline. It is a feature.

**Rubric scoring of "fewer, smarter holes" as a standalone company:**
- #1 discovery-is-80%: partly. The decision is the hard step, but the company does not own the asset, so it does not get the step-up.
- #2 illegible public data: weak for sensors; moderate for the decision layer (SMAD drill logs).
- #3/#4 cheap right, step-up buyer: not applicable unless it holds the ground.
- #5 ladder: the ladder up from a drill planner ends at owning the ground, which is Terranox/KoBold.
- #6 ceiling: sensors are about 2.4% of drill spend, and software tops out near Seequent at about US$1B. Fails.
- Base-rate lever: IPv2's "half as many holes" (simulation) is a 2x lever per decision. That passes the new 1.5-3x bar, but it accrues to the
  ground owner.
- Relative to the 3 Oct ban: the sensing and directional parts are drilling-based. The decision layer is software, but its value depends on
  the drilling.

**Recommendation:** Kill as a separate company. Build a sequential drill-planning (VOI/POMDP) module inside Terranox,
seeded with SMAD hole logs and downhole gamma. Cite IPv2 as the method, and use it to claim about 2x fewer holes per go/no-go
when raising money or selling a JV. Buy sensing (gamma, DHEM, hyperspectral, Ideon muon, Devico wedges) as contractor services.

---

## 7. Gaps (the search budget ran out)
- No primary Athabasca cost-per-metre figure from a NI 43-101 or MD&A. The C$383/m Saskatchewan number comes from an aggregator.
- Ideon's 2026 funding and partner release could not be fetched (403). The current round and revenue are unknown.
- I did not independently verify Earth AI's discoveries (Legacy Minerals Fontenoy assays).
- I did not research Sumitomo or ResGold's current status. I found no TerraCore ownership change.
- I found no published study with field (not simulated) metres-per-discovery before and after ML. That absence is itself the finding.
