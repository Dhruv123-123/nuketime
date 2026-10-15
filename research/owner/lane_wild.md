# Lane: WILDCARDS. Public data plus ML used to find and own a claimable asset

Written 15 Oct 2026. I used 18 of my 20 WebSearch calls, almost all on checking who already does each idea.
Figures marked (memory) come from what I already knew and were not re-checked in this run.

## Bottom line

The best wildcard is **cross-border regulatory arbitrage in medicines**. Many drugs are approved abroad
(EU national registers, Japan PMDA, China NMPA, India CDSCO, Brazil ANVISA) but have never been approved
by the FDA. A company that finds the right ones, takes an exclusive US licence and wins FDA approval
gets statutory exclusivity: 5 years for a new chemical entity (NCE) and 7 years for an orphan drug. The
first company to be approved gets it, so the claim is rivalrous in the Terranox sense. Harmony
Biosciences and Catalyst Pharmaceuticals are each worth billions and each was built on a single drug of
this kind. Both got their drug through relationships. Nobody I could find does this systematically with
ML across non-English registries. A narrower version of the same play hunts FDA tropical-disease
priority review vouchers (PRVs), which now sell for $160-200M each.

Western US water rights are a real asset pool worth over $10B, and satellite data makes ML there
genuinely useful, but the political and legal risk is heavy. Rail-corridor assembly and art "sleepers"
are weaker. Shipwrecks, hydro permits at existing dams, abandoned brands, university patents,
orbital/ITU slots and zombie biotechs are killed below.

| # | Candidate | Score |
|---|---|---|
| A | Drugs approved abroad but never in the US, licensed in for US NCE and orphan exclusivity | **7** |
| B | Tropical-disease PRV hunting (exclusive US rights to neglected-disease drugs from endemic countries) | **6** |
| C | Western US water rights: find under-used senior rights with satellite data, then buy, lease or transfer | **5** |
| D | Assembling rail and linear rights of way for underground HVDC and fibre to data centres | **4** |
| E | Art "sleepers": misattributed old masters found in auction archives | **3** |

---

## A. Drugs approved abroad but never in the US, licensed in for US exclusivity (7/10)

**Datasets and why they are public**
- **FDA:** Drugs@FDA and the Orange Book (exclusivity and patent listings are public by statute under
  the Hatch-Waxman Act), the Purple Book, and the FDA orphan designation database.
- **EU:** EMA EPARs and the Article 57 product data, plus the national registers that list decades of
  pre-EMA approvals (ANSM BDPM, BfArM/AMIce, AIFA, AEMPS CIMA, MHRA). EU transparency law requires
  these to be published.
- **Asia and Latin America:** Japan PMDA package inserts and review reports, China NMPA approvals,
  India CDSCO, Brazil ANVISA and Korea MFDS. All are public regulator databases.
- **Trials and literature:** ClinicalTrials.gov, EU CTR, jRCT and ChiCTR (trial registration is
  mandatory), and PubMed and J-STAGE, including non-English papers.
- **Market sizing:** Orphanet prevalence and CMS public-use claims.

**The ML problem.** Most of it is hard entity resolution:
- Match active ingredients across languages, salts, esters, brand names and fixed combinations, and
  decide whether the active moiety has ever been approved under FDA §505(b)(1), which sets NCE
  eligibility.
- Read foreign dossiers and the literature and predict how far the evidence is from US approval
  (bridging trial versus full Phase 3).
- Estimate US demand from claims and ICD prevalence.
- Score how likely each foreign owner is to licence. These are small Japanese and European firms
  with no US presence, so ownership structure and BD history are the signals.

The data is messy, multilingual and multimodal. Today big-pharma and specialty BD teams do this by
hand and through conference networking.

**What the company owns.**
- An exclusive US (or North American) licence from the foreign owner.
- Its own NDA, 5-year NCE exclusivity (no generic application can be filed for 4-5 years) and, where it
  applies, 7-year orphan exclusivity. Both go to the first approval, so they are rivalrous.
- Sometimes a transferable PRV as well.
- If the molecule is off patent everywhere, no licence is needed: the first US approval takes the
  exclusivity outright.

**Why it is defensible.** Exclusivity is set by statute and is winner-take-all, and the licence is
exclusive. The ML edge is coverage: thousands of approved actives in Japanese, Chinese, Korean and older
EU national registers are invisible to US BD teams, who mostly watch EMA centralised approvals.

**Ceiling, with sources**
- **Harmony Biosciences** licensed pitolisant from Bioprojet in France (EU approval 2016, US approval as
  Wakix in 2019). It guided 2025 revenue to **$845-865M** and Wakix revenue to **over $1B in 2026**
  ([Harmony 2025 guidance](https://www.barchart.com/story/news/35886513/harmony-biosciences-reports-strong-q3-2025-financial-results-recently-raised-2025-revenue-guidance-to-845-865m),
  [over $1B in 2026](https://www.businesswire.com/news/home/20260112364024/en/Harmony-Biosciences-Guides-to-Over-1-Billion-in-WAKIX%C2%AE-Revenue-in-2026-Advancing-Robust-Late-Stage-Pipeline-With-Potential-for-Long-term-Value-Creation)).
  The company is worth billions.
- **Catalyst Pharmaceuticals** sells Firdapse (amifampridine, EU-approved first through BioMarin). It
  guided 2025 total revenue to **$565-585M**, with Firdapse at **$355-360M**
  ([Catalyst Q3 2025 results](https://www.biospace.com/press-releases/catalyst-pharmaceuticals-reports-third-quarter-2025-financial-results-and-provides-business-update)).
- **Marathon Pharmaceuticals** got US approval for deflazacort (Emflaza), long sold in Europe, in 2017
  and sold it to PTC for about $140M upfront plus contingent payments (memory).
- The gap runs the other way too. Of 814 FDA orphan approvals in 2011-2023, **271 were never
  authorised by the EMA** for that indication, mostly because the sponsor never filed
  ([PMC study](https://pmc.ncbi.nlm.nih.gov/articles/PMC13375132/)).
- **Sizing:** one hit can be worth $0.5-1B a year. A portfolio of 5-10 hits supports a $5-10B outcome.

**Who already does it**
- Specialty pharma takes these drugs one deal at a time: Harmony, Catalyst, Eton, Zevra and Jazz in the
  US direction.
- For the reverse direction (US drugs into the EU and Japan), Immedica, Medison, Swixx and Pint Pharma
  are established and that side is crowded.
- Plenty of AI drug-discovery firms exist (e.g. the [GreyB list](https://greyb.com/blog/ai-drug-discovery-startups/)),
  but my searches found **no company sourcing approved ex-US assets systematically with ML.** The
  position looks open, though the BD habit is old.

**Risks**
- The foreign owner may file in the US itself.
- Pricing backlash is real: Firdapse's list price, the Emflaza price outcry, and Jacobus's Ruzurgi
  litigation.
- The FDA may demand a new trial, which costs $20-80M.
- Execution is that of a pharma company, not a software company.

**Concrete first proof (8 weeks, under $100k)**
1. Build a cross-walk of active ingredients across PMDA, NMPA, CDSCO, ANVISA, the EU national registers
   and Drugs@FDA/Orange Book.
2. Filter for molecules that are 505(b)(1)-naive, have at least one RCT, and treat a US condition with
   prevalence under 200k, or a large condition with an unmet need.
3. **Back-test:** the pipeline must flag pitolisant, amifampridine, deflazacort and vamorolone before
   their US filings.
4. Rank the top 25 and send 5 term-sheet approaches to owners.

**Score: 7.** The asset is rivalrous with large proven exits, the ML is truly hard and multilingual,
and there is no ML incumbent. It loses points for drug-development execution risk, capital needs and
political pricing risk.

---

## B. Tropical-disease PRV hunting (6/10)

**Datasets and why they are public**
- FDA's tropical-disease PRV eligibility list: 18 statutory diseases plus 9 added by order, including
  Chagas, rabies, chikungunya, cryptococcal meningitis, brucellosis and Lassa fever
  ([FDA program page](https://www.fda.gov/about-fda/center-drug-evaluation-and-research-cder/tropical-disease-priority-review-voucher-program)).
- The WHO Prequalification and Essential Medicines Lists.
- The CDSCO, ANVISA and NMPA registers.
- The DNDi and MMV pipelines, which are published by nonprofits.
- ClinicalTrials.gov and Drugs@FDA, used to check that no US approval exists for the active
  ingredient.

**The ML problem.** Find active ingredients that:
1. treat an eligible disease;
2. have never been approved under §505(b)(1) or §351;
3. already have efficacy data from endemic settings; and
4. need the smallest new clinical study to satisfy the post-2017 rule.

Since 30 Sep 2017 the sponsor must run its own new clinical investigation that is essential to
approval. The clinical reports cannot have been submitted for approval in India, Brazil, Thailand or a
PIC/S country before Sep 2007 ([FDA](https://www.fda.gov/about-fda/center-drug-evaluation-and-research-cder/tropical-disease-priority-review-voucher-program),
[RAPS on the 2017 fix](https://www.raps.org/resource/tropical-disease-prv-fix-didnt-stop-novartis-from.html)).
The ML is mostly NLP across registries and literature plus estimating trial size, so it is lighter
than in A.

**What the company owns.** An exclusive US licence from the endemic-country originator, for example an
Indian rabies monoclonal such as Serum Institute's Rabishield or Zydus's Twinrab (memory: neither has
FDA approval, and the US uses plasma-derived HRIG). It also owns the NDA or BLA and a **transferable
PRV**.

**Ceiling, with sources**
- Recent PRV sales: Bavarian Nordic **$160M** for its chikungunya vaccine voucher
  ([Fierce](https://www.fiercepharma.com/pharma/bavarian-nordic-sells-priority-review-voucher-chikungunya-vaccine-approval-160m))
  and Jazz **$200M** in Jan 2026
  ([Lachman](https://www.lachmanconsultants.com/2026/01/bazinga-another-priority-review-voucher-sold-for-200-million/)).
- Only **14 tropical PRVs were issued in 2009-2023**
  ([FDA Law Blog](https://www.thefdalawblog.com/2025/02/can-the-tropical-prv-have-its-moment-again-not-all-priority-review-vouchers-are-created-alike-what-the-potential-loss-of-the-rare-pediatric-prv-could-mean-for-the-tropical-disease-prv-pr/)).
- **Sizing:** capturing about 1 voucher a year at about $175M gives roughly $1.5-2B over a decade, plus
  modest US product revenue. That is multi-billion only at the margin, which is why it scores below A.
  It works best as a module inside A.

**Who already does it**
- Big pharma neglected-disease units: Novartis, Sanofi, GSK and Bayer.
- Vaccine firms: Bavarian Nordic and Valneva.
- Nonprofits: MDGH, which won the moxidectin voucher.
- Chemo Research won the benznidazole voucher after the KaloBios/Shkreli episode, and that episode is
  why the loophole was tightened.
- No one runs a systematic licence-in factory for this.

**Risks**
- Congress can change the voucher rules.
- MSF and other NGOs will push back on any appearance of profiteering.
- Each voucher needs a real new trial.

**First proof (4 weeks)**
1. List every active ingredient for the 27 eligible diseases that is approved anywhere but has never
   had a 505(b)(1) or 351 approval.
2. Score each by trial burden.
3. Open talks with 3 originators (rabies mAbs, dengue vaccines, leishmaniasis or Chagas drugs).

**Score: 6.**

---

## C. Western US water rights: under-used senior rights found by satellite (5/10)

**Datasets and why they are public**
- State water-rights registries, public under the prior-appropriation statutes of each state: Colorado
  CDSS/HydroBase, California eWRIMS, Arizona ADWR, Utah, Idaho IDWR, Nevada NDWR and Washington.
- **OpenET**: field-level evapotranspiration from Landsat for 2016 onwards, built by NASA, DRI, EDF
  and Google, and openly published
  ([NASA](https://www.nasa.gov/missions/landsat/transforming-water-management-in-the-u-s-west-with-nasa-data/),
  [JAWRA paper](https://onlinelibrary.wiley.com/doi/full/10.1111/1752-1688.12956)).
- USDA's Cropland Data Layer, county parcel records and Bureau of Reclamation contract data.

**The ML problem.** For every right, infer the historic consumptive use that a water court will
recognise in a transfer, using satellite evapotranspiration joined to fields. Then infer:
- yield under drought calls, adjusted for seniority;
- the risk that unused rights are forfeited or abandoned;
- the holder's propensity to sell (age, estate status, crop economics).

Last, match supply to growing demand from municipalities and data centres. This is a real sparse,
multimodal inference problem: messy paper rights joined to pixels.

**What the company owns.** Fee title to water rights or land with rights attached, or long-term leases
and fallowing agreements. Senior priority dates are fixed and finite, so the asset is rivalrous.

**Ceiling, with sources**
- Greenstone sold the 2,033 AF/yr entitlement from about 500 acres in Cibola, AZ to Queen Creek for
  **$24M**, about **$11.8k per acre-foot of annual entitlement**
  ([Guardian, via Coyote Gulch](https://coyotegulch.blog/2024/04/17/water-is-more-valuable-than-oil-the-corporation-cashing-in-on-americas-drought-the-guardian/)).
- About 1 MAF/yr of transferable rights at $5-15k/AF is **$5-15B**. The Colorado River alone carries
  about 15 MAF of apportionments.

**Who already does it**
- **Principals:** Water Asset Management, Vidler Water (bought by D.R. Horton in 2022, memory),
  Greenstone, Renewable Resources Group and Cadiz. Together, Vidler and WAM own about 8.6k acres in
  Arizona and Greenstone about 8.9k acres
  ([Arizona State Law Journal](https://arizonastatelawjournal.org/2024/11/07/the-central-arizona-oasis/)).
- **Tools:** WestWater Research (brokerage), SWIIM and Mammoth (marketplaces). These are not owners.
- The ML angle is open, but the asset class is known and well funded.

**Risks**
- Heavy political and legal risk. A federal court found Reclamation's approval of the Greenstone to
  Queen Creek transfer deficient.
- Colorado's anti-speculation doctrine and "buy-and-dry" backlash.
- Possible state legislation.

**First proof.** Join OpenET to CDSS for one Colorado basin (for example the Lower Arkansas). Rank
rights by gap between paper and actual use and by seniority. Back-test against recorded transfers in
2016-2024.

**Score: 5.** The pool is large and the asset is rivalrous, but the backlash and slow water-court
process are serious, and incumbents are well capitalised.

---

## D. Rail and linear right-of-way assembly for underground HVDC and fibre (4/10)

**Datasets.**
- STB abandonment dockets (public under 49 USC 10903).
- The USDOT/BTS North American Rail Network, including abandoned lines.
- ICC valuation maps from 1915 onwards.
- County deed and parcel records.
- Rails-to-Trails corridor inventories.

**The ML problem.** Rebuild corridor continuity and title type (fee versus easement) from scanned
deeds and maps. Then route HVDC between generation and data-centre load, and rank railroads and
short lines by willingness to grant longitudinal easements.

**What the company owns.** Long-distance easements or options and the development rights to an
underground HVDC line.

**Ceiling.** SOO Green: 350 miles, 2.1 GW, **$2.5B**, built mainly in Canadian Pacific right of way,
with PPL taking a stake and a $900M Prysmian cable award
([Canary Media](https://www.canarymedia.com/articles/transmission/how-transmission-along-railroads-and-highways-could-break-open-clean-energy-growth),
[NS Energy](https://www.nsenergybusiness.com/news/ppl-acquires-ownership-interest-in-soo-green-hvdc-link-transmission-project/)).

**Who already does it.** Direct Connect Development (SOO Green), Grid United, the railroads themselves,
and the NextGen Highways advocates.

**Why it scores low**
- Active corridors are negotiated privately with Class I railroads. That takes no ML and favours
  incumbents.
- Abandoned corridors held as easements revert to the adjacent landowners, as the Supreme Court held
  in Marvin M. Brandt (2014) (memory). That destroys most of the "hidden value".

**Score: 4.**

---

## E. Art "sleepers" from auction archives (3/10)

**Datasets.** Open-access museum collections (Met, Rijksmuseum, NGA), the Getty Provenance Index, and
public online auction catalogues. The catalogues are public listings, but not public by statute.

**The ML problem.** Attribution from images and provenance.

**What the company owns.** The painting, bought cheap and re-attributed. Salvator Mundi is the famous
example, bought for about $1k and sold for $450M (memory).

**Who already does it.** Art Recognition, academic deep-learning work such as the
[Rubens attribution paper](https://arxiv.org/pdf/2511.22667), and trade dealers who hunt sleepers.
Apollo magazine reports that the field is sceptical of AI attribution
([Apollo](https://apollo-magazine.com/artificial-intelligence-authentication-artworks/)).

**Why it scores low.** Old-master turnover is only about $0.5-1B a year (memory). Attributions get
contested, there are few hits, and nothing is rivalrous beyond winning the lot.

**Score: 3.**

---

## Killed (do not re-pitch)

| Idea | Why it is killed |
|---|---|
| **Shipwreck cargo from historical archives** | AE Studio (Skunkworks) has run AI over about 80M pages of Spanish colonial archives and was hiring salvors in Aug 2026 ([ua.news](https://ua.news/en/world/u-ssha-shukaiut-pirata-dlia-poshuku-zatonulikh-skarbiv-za-dopomogoiu-shi)). Odyssey Marine is the incumbent. Sovereign immunity cases go against salvors: Spain won the Mercedes treasure (about $500M) back from Odyssey (memory). Crowded and legally hostile. |
| **Hydro at non-powered dams and pumped-storage preliminary permits** | FERC preliminary permits are first-to-file, but Rye Development and others already hold large non-powered-dam and pumped-storage portfolios ([Rye in West Virginia](https://www.nacleanenergy.com/energy-storage/rye-development-grows-non-powered-dam-portfolio-filing-preliminary-permits-for-three-new-projects-in-west-virginia)). Permit squatting is already the norm. |
| **Abandoned brand and trademark revival** | River West Brands, Retrobrands and Hilco do this already ([propertyintangible](https://propertyintangible.com/tag/river-west-brands)). Exits are $10-100M, the "residual goodwill" doctrine is weak, and the pool is not multi-billion. |
| **Dormant university and national-lab patents** | Hit rates are low, patents are often half expired by the time they are found, and Allied Minds, IP Group and PureTech have mixed or poor records. |
| **Zombie biotechs and shelved clinical assets** | Concentra Biosciences (Tang Capital), Roivant, BridgeBio and XOMA already own this. |
| **Paragraph IV first-filer and CGT generic exclusivity** | The generic industry (Teva, Viatris, Indian majors) is saturated. |
| **ITU orbital filings and spectrum** | Priority comes from paperwork, not inference. Paper-satellite filing through small states is already gamed. |
| **Power sites at retired plants and interconnection queue positions** | Crowded (Crusoe, Tract, Prometheus, utilities) and likely covered by other lanes. |
| **Unmatched music royalties (MLC black box)** | The pool is about $0.4B and Songtrust, Kobalt and royalty funds already work it. |

## Searches used: 18 of 20

I could not fetch the Tom's Hardware article on AE Studio (the URL was too long for the proxy), so I
read a syndicated copy instead. I did not try to download any large dataset.
