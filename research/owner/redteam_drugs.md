# Red team: the "stranded drugs" holding company (CRL rescue + approved-abroad, US-naive drugs)

Written 15 Oct 2026. I used 15 of 15 WebSearch calls, plus fetches. Anything marked (memory) is my own
knowledge and was not re-checked in this run.

## Verdict: SURVIVES WITH CHANGES as a business, but DEAD against the brief's criterion 2 (ML is the edge)

The asset logic holds up. Exclusive licences and statutory NCE/orphan exclusivity are rivalrous, and
Harmony, Catalyst and Zevra are real billion-dollar precedents. Three of the pitch's load-bearing claims
do not survive:

1. **Feed (a), the published CRLs, is fragile and adds little information.**
   - FDA paused publication in April 2026 after a citizen petition.
   - Release resumed haphazardly in July. The legal basis is contested, and FDA has asked Congress for
     explicit authority.
   - Material CRLs were already disclosed in sponsors' 8-Ks.
   - The CMC/facility-only CRLs the pitch wants are exactly the ones owners fix themselves.
2. **Feed (b) is small and enumerable.**
   - The high-quality pool (modern EU/Japan approvals with no US approval) adds only about 5-8 new
     molecular entities a year.
   - An analyst with IQVIA or Citeline can list the whole set in a week, so it is a lookup, not an
     inference problem.
   - The long tail (old national registers, China, India, Russia) is large, but mostly low-evidence or
     commercially thin.
3. **The binding constraint is not data.** It is owner willingness and price, the US evidence and
   trial cost, capital, and commercial execution. ML is a cheap diligence tool here, not a moat.

## 1. Are the inputs real?

### FDA CRL publication: real, but paused and legally contested in 2026
- **Timeline of releases:**
  - July 2025: more than 200 CRLs released, for applications from 2020-2024 that were later approved.
  - September 2025: 89 CRLs for pending or withdrawn applications, plus a promise of real-time release.
  - openFDA held 458 records as of 13 Aug 2026.
  - Sources: [IntuitionLabs](https://intuitionlabs.ai/articles/fda-complete-response-letters-dataset),
    [Debevoise, Apr 2026](https://www.debevoise.com/insights/publications/2026/04/fdas-real-time-release-of-complete-response-letter).
- **The April 2026 rollback:**
  - On 20 Apr 2026 a pharma company filed a citizen petition through Covington. It calls publication
    "unlawful" and asks FDA to "immediately cease".
  - FDA "temporarily paused" publication from April onwards. The last CRL posted was AbbVie's, dated
    22 Apr. Sobi's late-June CRL was never posted.
  - FDA has proposed a rule to formalise disclosure.
  - Makary, the commissioner who drove the policy, is gone; Kyle Diamantas is acting commissioner.
  - FDA's FY2027 budget asks Congress for "explicit authority".
  - Sources: [Applied Clinical Trials, 10 Jul 2026](https://www.appliedclinicaltrialsonline.com/view/fda-pauses-real-time-release-drug-rejection-letters-formalize-policy),
    [PharmExec](https://www.pharmexec.com/view/fda-pauses-release-new-crl-following-citizen-petition).
- **After the pause:**
  - On about 11 Jul, 14 new CRLs appeared, including letters dated 9 Jul to Hengrui and Elevar
    ([BioSpace](https://www.biospace.com/fda/fda-posts-new-rejection-letters-days-after-confirming-pause),
    [BioCentury "FDA resumes"](https://biocentury.com/article/660099/fda-resumes-crl-releases-citing-commitment-to-transparency)).
  - Status today: intermittent, with no statutory basis, and one adverse ruling or administration
    change away from ending.
- **What the corpus actually adds:**
  - The [FDA Law Blog](https://www.thefdalawblog.com/2025/07/radical-transparency-or-radical-redundancy-fda-publishes-200-complete-response-letters-most-of-which-are-already-public/)
    called the first batch "radical redundancy": most of those letters were already public.
  - For listed sponsors, the fact and gist of a CRL is already disclosed as a material event.
  - The real new information is the exact deficiency wording on unapproved applications, and that is the
    part under legal attack.
- **Volume:** CDER issued only about 19 CRLs on 18 novel drugs in 2025 (IntuitionLabs). The
  deal-relevant flow is tens per year, not hundreds.

### Biossil: real
- **The round:** US$153M led by the OpenAI Startup Fund at a US$1B valuation, reported 28 Sep 2026.
  Founders Fund, Quiet, ADIC, Duke and others joined. CEO is Anthony Mouchantaf. Sources:
  [LetsDataScience](https://letsdatascience.com/news/biossil-raises-153m-in-openai-led-round-7c603c9c),
  [BetaKit](https://betakit.com/?p=410364),
  [Dealroom](https://dealroom.co/news/157312-openai-leads-150m-round-for-drug-reviving-startup-biossil/).
- **What it does:**
  - It acquires shelved or failed clinical candidates and uses AI to re-target them to patient subgroups
    or new indications.
  - It holds 12 molecules, including ridinilazole from Summit at $0.5M upfront plus $104.5M in
    milestones (per lane_bio).
  - Coverage says nothing about CRLs or foreign-approved drugs. It is efficacy-failure resurrection,
    not paperwork rescue.
  - Its capital base and investor pull, however, make it the obvious fast follower into either feed.

### Other AI-native or systematic buyers
- **Formation Bio** (formerly TrialSpark) is the most direct threat.
  - It is AI-native and in-licenses clinical-stage assets, including a TYK2 inhibitor from China's
    Lynk Pharmaceuticals.
  - It has raised about $622M in total, including a $372M Series D backed by Sanofi, and has an
    OpenAI collaboration.
  - Sources: [Patsnap](https://synapse.patsnap.com/article/formation-raises-372m-series-d-for-ai-driven-drug-licensing-backed-by-sanofi),
    [IntuitionLabs profile](https://intuitionlabs.ai/companies/biotech/formation-bio).
  - Its thesis is "AI makes the US development step cheaper". That is a better use of AI in this
    business than "AI finds the asset".
- **Ignota Labs** bought Kronos Bio's whole clinical portfolio in October 2025 (per lane_bio).
- **Non-AI specialty pharma** already runs exactly this playbook by hand:
  - Harmony (pitolisant from Bioprojet)
  - Catalyst (amifampridine; then vamorolone, see §3)
  - Zevra (arimoclomol out of the Orphazyme estate)
  - Medexus (treosulfan from medac)
  - Eton (approved-abroad paediatric and rare-disease products, memory)
  - Marathon (deflazacort, memory)
  - Mitsubishi Tanabe (Radicava, filed itself)
- **Chinese out-licensing** is the most crowded feed of all: 157 deals worth $135.7B in 2025,
  including Pfizer–3SBio at $1.25B upfront and GSK–Hengrui at $500M upfront
  ([Caixin](https://www.caixinglobal.com/2026-01-14/chinese-drugmakers-strike-record-136-billion-in-cross-border-licensing-deals-102403540.html)).
- **What I did not find:** a company that explicitly runs ML over foreign registers to source approved,
  US-naive molecules. My searches turned up nothing, which is weak evidence of absence. It is equally
  consistent with "this is not where the value is".

## 2. Pool size

### Approved abroad, never in the US
- **IQVIA Institute, Dec 2024** ([report](https://www.iqvia.com/insights/the-iqvia-institute/reports-and-publications/reports/assessing-availability-of-new-drugs-in-europe-japan-and-the-us)):
  - 545 novel active substances were approved in 2014-2022 by the US, EU and/or Japan.
  - Only about **61 were never approved in the US**: 12 EU-only, 43 Japan-only and 6 EU-plus-Japan.
  - That is roughly **7 a year**.
- **Kasahara, JAMA Network Open** ([RAPS summary](https://www.raps.org/resource/study-notes-disparities-in-new-drugs-approved-in-t.html)):
  - 431 NMEs were approved in Japan in 2005-2022. Of these, **78 (18%) were never approved in the US**.
  - The reverse gap is much bigger: 280 US approvals never reached Japan.
  - The drug-lag problem runs mainly *into* Japan and the EU, not into the US.
- **How many could sell over $100M a year in the US** (my estimate, not published):
  - Many Japan-only NMEs are Japan-specific: local epidemiology, Japanese-only trials, or me-too drugs
    in classes the US already serves. Several have been withdrawn.
  - Plausibly only **10-25% clear $100M/yr** in the US. That gives about **10-20 candidates across two
    decades**, most of them already known to their owners and to US business-development (BD) teams.
  - The older long tail of pre-2000 EU national registrations and China/India/Russia approvals runs to
    hundreds or low thousands of moieties. Most are off-patent with old evidence. They stay unapproved
    in the US for reasons: safety (metamizole, nimesulide), evidence standards, or no commercial case.
- **Bottom line:** the high-quality pool is roughly the size of one specialty-pharma BD team's
  watch-list. It is a lookup.

### CRLs: CMC/facility-only and never resubmitted
- **Facility involvement:** 56% of the 89 unapproved CRLs from 2024-25 cite facility inspection
  problems, 47% cite product quality and more than 30% cite clinical issues; the categories overlap
  ([FDA Group](https://insider.thefdagroup.com/p/an-analysis-of-89-fda-crls)).
- **CMC-only share:** historically only **15%** of first-cycle NME failures were CMC- or labelling-only
  (JAMA 2014, via IntuitionLabs).
- **CMC-only and abandoned:** no published count exists. At about 15% of tens of CRLs a year, that is
  **a handful a year**.
- **Adverse selection:** those are the cheapest CRLs to fix, so owners fix them themselves. Recent
  examples:
  - Grace Therapeutics' GTx-104 got a CRL on 23 Apr 2026 for CMO cGMP, leachables and toxicology risk
    assessment, with no clinical deficiencies. Grace kept the asset and requested a Type A meeting
    ([PharmaNow](https://www.pharmanow.live/latest-news/grace-therapeutics-fda-crl-gtx-104-nda-cmc-cgmp-deficiencies-cmo)).
  - Fortress/Cyprium's CUTX-101 was resubmitted by its owner.
- **What reaches distress:** disproportionately clinical CRLs, sponsors with no cash, or assets with
  tiny markets.
- **The anchor precedent is not a CMC case.** Orphazyme's 2021 arimoclomol CRL raised
  evidence and efficacy questions, and Zevra fixed it with further analysis and data (memory). Its
  value came mainly from the PRV.

## 3. Unit economics

| Path | When it applies | Cost to US approval | Time | Examples |
|---|---|---|---|---|
| Foreign pivotal data accepted (505(b)(1) with right of reference, ICH E5 bridging) | Good GCP trials, a population relevant to the US, an orphan setting | ~$10-40M: US-compliant CMC/site, PK bridging, NDA (fee waived for orphan) | 1.5-3 yrs | Pitolisant: licensed about 2017, approved Aug 2019 on EU trials (memory) |
| 505(b)(2) on literature, no right of reference | Off-patent old molecule, owner not needed | ~$15-60M, usually plus one new adequate and well-controlled trial | 2-4 yrs | Deflazacort/Marathon, approved 2017 on old trials; sold to PTC for about $140M upfront (memory) |
| New US Phase 3 required | Foreign data inadequate | $30-150M | 4-7 yrs | Amifampridine: Catalyst licensed 2012, refuse-to-file 2016, approved Nov 2018 (memory) |
| CRL rescue, CMC/facility | Facility swap or tech transfer | ~$5-30M, plus re-inspection | 1-3 yrs | Treosulfan: EU 2019, CRL Aug 2021, resubmitted Jul 2022, approved **Jan 2025** ([Drugs.com](https://www.drugs.com/history/grafapex.html)) |

Notes on the table:
- NCE exclusivity attaches to the first approval of an active moiety, whether through 505(b)(1) or
  (b)(2).
- Orphan exclusivity is specific to the indication.

**Licence terms.** Owners who know what they have price it in:
- **Vamorolone (Santhera to Catalyst, June 2023):** **$75M upfront plus a $15M equity investment**,
  plus milestones and royalties. That was while the NDA *was already under FDA review*: the originator
  had done the US work and captured most of the arbitrage
  ([Muscular Dystrophy News](https://musculardystrophynews.com/news/north-american-rights-dmd-therapy-vamorolone-acquired-catalyst/)).
- **Typical approved or near-approved specialty licence (memory, unverified):** low-to-mid-teens up to
  20%+ tiered royalties plus sales milestones.
- **Where the cheap deals are:** the $1-15M "cheap" deals (arimoclomol at $12.8M, ridinilazole at
  $0.5M) exist only for distressed or failed assets, which carry the clinical risk.

## 4. Why hasn't it been arbitraged away?

1. **The opportunity is visible, not hidden.**
   - Modern foreign approvals are listed in IQVIA, Citeline and Cortellis, which every BD team
     subscribes to.
   - Foreign originators (Japanese majors, Santhera, medac, Mitsubishi Tanabe, Chinese biotechs) now
     file in the US themselves or license early at full price.
2. **The real constraints are:**
   - **(a) Owner willingness and price.** Relationship-driven, slow, often tied up with existing
     partners or territories.
   - **(b) Evidence gap.** FDA acceptance of foreign data, sometimes requiring a US trial.
   - **(c) Capital.** $20-150M and 2-5 years per asset.
   - **(d) Commercial build-out** and pricing scrutiny (the Firdapse and Emflaza backlash).
   - **(e) Small markets.** Many stranded drugs are stranded because they are commercially marginal.
3. **Where ML helps:**
   - Multilingual entity resolution (salts, INN variants against "active moiety") on the long tail.
   - Triaging CRL text.
   - Predicting whether FDA will accept foreign data.
   - These are real but modest. They shave diligence weeks off; they do not create the asset. The brief
     requires an inference problem "humans and incumbents are not doing well". Incumbents enumerate the
     good part of this pool well enough by hand, because it is small.
4. **Honest call:** ML is not the edge. The edges are capital cost, regulatory execution speed, and
   reaching foreign owners before the next buyer does. If AI matters, it is Formation Bio's version: a
   cheaper and faster US development and trial step.

## 5. Defensibility

- **Exclusive per asset? Yes, with caveats.**
  - A signed exclusive licence plus first-approval NCE exclusivity (5 years) and orphan exclusivity
    (7 years) is a genuine regulatory monopoly.
  - NCE exclusivity is short; generics can file a Paragraph IV challenge at NCE minus one year.
  - Orphan exclusivity covers only the indication.
  - For an off-patent molecule with no licence, a rival 505(b)(2) filer racing you is possible until
    your approval, and only the first approval wins.
- **Defensible as a company? No.**
  - The sourcing method (scan registers, read CRLs) is trivially copyable by any BD team or by
    Biossil or Formation, which have $150-600M each.
  - The data is public and, for the CRL half, possibly temporary.
  - Each win is publicised in the 8-K that announces the deal, so competitors learn the playbook at
    once.
  - The only lasting moats are a portfolio of signed exclusive licences and a regulatory and commercial
    execution record. Those are a specialty pharma's moats, not a data moat.

## Strongest reframing if pursued

**A "first-US-approval" specialty pharma roll-up: an exclusivity-and-voucher harvester, with ML as the
diligence engine rather than the pitch.**
- **Focus** on off-patent or abandoned foreign-approved moieties in rare paediatric or tropical
  indications.
- **Why that focus:**
  - No licence is needed, or the owner is indifferent, so owner willingness drops out as a constraint.
  - First US approval earns NCE and orphan exclusivity outright.
  - A transferable PRV ($150-200M, rare paediatric program through Sep 2029; the tropical program is
    permanent) pays for the development step by itself.
- **CRLs:** use them as an opportunistic side-feed, not the thesis. Watch 8-Ks and bankruptcy dockets
  as well as openFDA, since the openFDA feed may disappear.
- **Where to spend effort on AI:** predicting whether FDA will accept foreign data, and a cheaper US
  bridging trial (the Formation Bio lesson), not discovery.
- **What it is:** a capital-heavy pharma company (about $50-150M per shot, 2-4 years). It fits Dhruv's
  "own the asset, ceiling set by asset value" test, but fails "ML is the hard edge" and "unattackable".
- **Recommendation for this hunt:** do not advance as the Terranox-analogue winner. Keep it as the
  fallback "real business" option.

## Sources
- https://intuitionlabs.ai/articles/fda-complete-response-letters-dataset
- https://www.debevoise.com/insights/publications/2026/04/fdas-real-time-release-of-complete-response-letter
- https://www.appliedclinicaltrialsonline.com/view/fda-pauses-real-time-release-drug-rejection-letters-formalize-policy
- https://www.pharmexec.com/view/fda-pauses-release-new-crl-following-citizen-petition
- https://www.biospace.com/fda/fda-posts-new-rejection-letters-days-after-confirming-pause
- https://biocentury.com/article/660099/fda-resumes-crl-releases-citing-commitment-to-transparency
- https://www.thefdalawblog.com/2025/07/radical-transparency-or-radical-redundancy-fda-publishes-200-complete-response-letters-most-of-which-are-already-public/
- https://insider.thefdagroup.com/p/an-analysis-of-89-fda-crls
- https://letsdatascience.com/news/biossil-raises-153m-in-openai-led-round-7c603c9c
- https://betakit.com/?p=410364
- https://dealroom.co/news/157312-openai-leads-150m-round-for-drug-reviving-startup-biossil/
- https://synapse.patsnap.com/article/formation-raises-372m-series-d-for-ai-driven-drug-licensing-backed-by-sanofi
- https://intuitionlabs.ai/companies/biotech/formation-bio
- https://www.iqvia.com/insights/the-iqvia-institute/reports-and-publications/reports/assessing-availability-of-new-drugs-in-europe-japan-and-the-us
- https://www.raps.org/resource/study-notes-disparities-in-new-drugs-approved-in-t.html
- https://www.caixinglobal.com/2026-01-14/chinese-drugmakers-strike-record-136-billion-in-cross-border-licensing-deals-102403540.html
- https://musculardystrophynews.com/news/north-american-rights-dmd-therapy-vamorolone-acquired-catalyst/
- https://www.drugs.com/history/grafapex.html
- https://www.pharmanow.live/latest-news/grace-therapeutics-fda-crl-gtx-104-nda-cmc-cgmp-deficiencies-cmo
