# Lane: legal claims, IP and financial assets (eighth hunt)

Written 15 Oct 2026. Web searches used: 16 of 20. Sources at the bottom. Nothing was downloaded; dataset access
is checked against documentation only.

## Verdict first

The lane is mostly picked over. Almost every "buy a mispriced claim" market already has well-funded specialist
buyers: claims trading (Xclaim, Cherokee, distressed funds), litigation and antitrust opt-outs (Burford,
Legalist), music royalties (Duetti, Concord/Recognition, Primary Wave, Royalty Exchange, Claimy, Salt), carbon
quality (Sylvera, BeZero, Calyx, Renoster, Pachama), zombie biotech IP (XOMA, Concentra/Tang), and tariff refunds
(hedge funds and private credit already pay 50-90 cents). The best candidate in this lane is **direct-to-device
(D2D) satellite spectrum rights**: ITU priority filings plus national MSS licences. It is a real
first-come-first-served claim with asset prices of ~$40B in the last 13 months, but hyperscalers are buying the
same asset and the ML edge there is moderate, not decisive. No candidate here scores above 6.

## Candidate 1: D2D/MSS spectrum-rights aggregation (ITU filings + national MSS licences). Score 6/10

- **Dataset and why it is public.** ITU Radiocommunication Bureau records: the Space Network List (SNL, free
  online), BR IFIC weekly circulars and the SRS database. They are public because the Radio Regulations make
  advance publication, coordination requests and notification public, so other administrations can object.
  National registers are public for the same reason: FCC ULS/IBFS/ICFS, Ofcom WTR, ACMA RRL, ANFR, ISED and
  others. Also the EU 2 GHz MSS selection record, with incumbent licences reported to expire in May 2027 (verify
  the date). I did not fetch SNL or BR IFIC from this network.
- **ML problem.** Most filings are paper. China has filed for ~244k satellites and Rwanda for ~327k. The useful
  inference across roughly 190 administrations is which filings in D2D-usable bands (L, S, 2 GHz, and IMT bands if
  WRC-27 agenda item 1.13 opens them) are (a) still legally alive under bringing-into-use and Resolution 35
  milestones, (b) senior in coordination date to the big constellations, and (c) held by a weak holder (a small
  administration, a dormant satco or a bankrupt estate) who would sell. Then join that to national
  landing-rights and licence-expiry calendars. The inputs are messy multilingual PDFs, partial records and
  regulatory state machines, and the output is a ranked list of buyable, senior, live rights.
- **What the company owns.** The holding entity of the ITU priority, or the national MSS or terrestrial licence,
  bought outright or won at a national selection. AST SpaceMobile did exactly this: it paid $64.5M ($26M up
  front) for an entity holding global S-band ITU priority, in Aug 2025. Fleet Space bought European frequency
  assets in 2023.
- **Why defensible.** ITU coordination priority is first-in-time, and a national licence is exclusive. Whoever
  holds the senior filing or licence holds the asset. This is the closest analogue in my lane to staking a
  mineral claim.
- **Ceiling (numbers).** SpaceX-EchoStar: ~$17B for AWS-4/H-block (Sep 2025), plus ~$2.6B for unpaired AWS-3,
  so close to $20B in total. Amazon-Globalstar: $11.6B for ~25 MHz of L/S-band MSS plus 11.5 MHz at 2.4 GHz
  (Apr 2026). Rocket Lab-Iridium values Iridium at ~$8B for 9 MHz of L-band MSS. Lynk-Omnispace merged around
  60 MHz of international S-band rights. That is about $40B of D2D spectrum changing hands in 13 months.
  Fragments outside the US and EU are worth tens to hundreds of millions each, and an aggregated multi-country
  stack is worth billions.
- **Who already does it.** SpaceX, Amazon, AST, Rocket Lab, Lynk/Omnispace (Elveo), and Viasat/Space42 (the
  Equatys JV). They are strategic buyers with large balance sheets, and they are the exit, not just the
  competition. No pure-play "find and warehouse" ITU and licence aggregator turned up in search.
- **Why only a 6.** (1) Resolution 35 milestones mean an ITU filing cannot be warehoused indefinitely. You have
  to launch, or sell before the milestone. (2) Every filing needs a sponsoring national administration. (3) The
  edge is regulatory diligence that LLMs speed up, not an inference humans cannot do. Strategic buyers can hire
  the same 20 spectrum lawyers.
- **First proof (4-6 weeks).** Build a parser over SNL/BR IFIC for MSS bands 1518-1675 MHz, 1980-2025 MHz and
  2160-2200 MHz. List every non-GSO and GSO network with its date of receipt, BIU/suspension status and
  administration. Cross it with national licence registers, and mark each holder's distress signals (insolvency,
  no launches, lapsed filings). Deliverable: the top 25 senior, live, buyable rights, with the AST S-band
  transaction as the price benchmark ($64.5M), and one letter of intent with a holder.

## Candidate 2: Buying pending patent families with early priority dates whose specs support claims on today's products. Score 4/10

- **Dataset and why it is public.** USPTO Patent Center file wrappers and the Open Data Portal (successor to
  PEDS). Applications publish at 18 months under 35 USC 122(b). The USPTO assignment database and maintenance-fee
  events are public, as are EPO Register and INPADOC families. Office-action dates are public, so
  response/abandonment deadlines can be computed.
- **ML problem.** Find families that are still pending (so continuations can be filed), old in priority date, and
  whose written description (§112) supports claims that read on products shipping now. The model has to reason
  from the spec to product teardowns and docs. Then predict whether the owner will let the family lapse at the
  next deadline: small entity, no recent filings, assignee in distress.
- **What the company owns.** The pending family itself, by assignment. It then files continuations with new
  claims and keeps the original priority date.
- **Why defensible.** Each family's priority date is unique and cannot be copied. Ownership is exclusive.
- **Ceiling.** Single families have produced nine- and ten-figure outcomes. VLSI won $2.18B against Intel in
  2021, though it was later vacated. The asset value is real, but it is realised through licensing or
  litigation, under PTAB and §101 risk.
- **Who already does it.** NPEs and aggregators (Intellectual Ventures, Acacia, Dominion Harbor, IPValue, IP Edge,
  RPX defensively). AI tools for continuation and infringement mapping are sold to owners (Patlytics, XLSCOUT), so
  the ML is turning into a commodity. The brief already killed SEP (PatSnap) and docket-based litigation finance
  (Legalist).
- **Why only a 4.** It is an NPE business with reputational and venue risk, the ML edge is being sold to
  everyone, and the payout runs through courts.
- **First proof.** Backtest: take families abandoned in 2018-2021 and check whether a model, given only their
  specs, flags ones that a human attorney confirms could have supported claims on products launched later.

## Candidate 3: US copyright termination recapture (music and books from 1979-2001 grants). Score 4/10

- **Dataset and why it is public.** U.S. Copyright Office public catalog and recorded documents, plus the
  recorded termination notices themselves: 17 USC 203/304 require notices to be recorded. Other public sources:
  ASCAP/BMI Songview, MLC public works data, streaming play counts, and obituaries and probate records for heirs.
- **ML problem.** Join messy work, author and grant records to current earnings. Find terminable works with
  high streaming value where no notice has been recorded and the window (2 to 10 years before the effective
  date) is open. Then find the living authors or statutory heirs.
- **What the company owns.** Here the legal design is weak. Under §203(b)(4), a further grant, or agreement to
  make one, is valid only after the effective date of termination, unless it goes to the original grantee. So a
  third party cannot lock up the recaptured rights in advance. It can only fund the author or heirs, serve the
  notices, and then compete to buy at the effective date.
- **Ceiling.** Global music copyright value is about $45B a year. Catalog prices: Sony-Queen ~$1.27B (2024);
  Concord-Hipgnosis/Recognition ~$1.6B (2024). Late-1980s to 1990s pop and hip-hop grants become terminable from
  2026 to 2036. Recent litigation (Vetter v. Resnik, holding that recapture reaches worldwide rights, and the
  Waite v. UMG recording-terminations class action) would raise the value if upheld. Treat both as unsettled.
- **Who already does it.** Music lawyers (Songwriters Guild termination service) and Primary Wave, Concord and
  Reservoir buying from estates. No ML-driven player turned up, but the asset is not exclusive before the
  effective date.
- **Why only a 4.** The asset is not claimable first-come. Authors are free agents, and incumbent publishers
  have both the renegotiation right and the relationships.
- **First proof.** Pick 500 top-streaming songs registered 1989-1995, compute their termination windows, and
  check what fraction have no recorded notice. If more than 30% of the high-value ones are unnoticed, the
  sourcing edge is real.

## Candidate 4: Western water rights repriced with satellite consumptive use. Score 4/10 (overlaps a land/water lane)

- **Dataset and why it is public.** State water-rights registers (Colorado CDSS/HydroBase, Utah, Nevada,
  Arizona ADWR, California eWRIMS), which are public because rights are adjudicated, recorded property. Also
  OpenET (Landsat-based field-scale evapotranspiration, free; NASA/EDF/DRI/Google), which several states already
  use.
- **ML problem.** Transferable volume in a change case is historic consumptive use, not the paper decree.
  Field-level ET from 1984 onward, together with decree records, lets you estimate the true transferable
  "wet water" of every senior right. You can then find rights that are undervalued (paper looks small, use is
  high) or that face abandonment or forfeiture.
- **What the company owns.** Senior water rights, usually by buying the land.
- **Why defensible.** Priority dates are exclusive and senior rights are fixed in number.
- **Ceiling.** Western water rights are a multi-billion asset class. Water Asset Management calls it a
  "trillion-dollar" opportunity and has bought ~2,500+ acres in Colorado's Grand Valley.
- **Who already does it.** Water Asset Management, Vidler (now D.R. Horton), Cadiz, ag funds, and WestWater
  Research for valuation. States use OpenET too.
- **Why only a 4.** There is political anti-speculation risk (Colorado's anti-speculation doctrine, plus active
  legislation), slow water-court change cases, and an edge that OpenET hands to everyone for free.
- **First proof.** For one Colorado basin, rank decrees by OpenET-estimated historic consumptive use relative to
  decreed volume, and compare against 20 recent sale prices.

## Candidate 5 (killed but noted): duty refund claims. Score 3/10

The IEEPA tariffs were struck down by the Supreme Court on 20 Feb 2026, 6-3. The CIT ordered refunds of an
estimated ~$166-175B to all importers of record, CBP's CAPE portal opened 20 Apr 2026, and payments began from
12 May 2026. Public CBP manifest data (19 CFR 103.31, the source behind ImportGenius/Panjiva) could identify
importers and estimate what they paid. But funds already pay $0.50-0.90 on the dollar, refunds are flowing, and
the Assignment of Claims Act complicates true sales. The next wave (Section 122 and forced-labor tariff cases) is
"still really early" per Holland & Knight and is a one-off event, not a franchise. Killed.

## Killed quickly (with reason)

- **MLC unmatched / black-box royalties.** Only ~$6M per usage month remains for 2021, plus ~$158.6M of
  historical pre-2021 money, and market-share distribution starts Apr 2027. Too small, and Claimy, Salt and
  Song Sleuth (Epidemic) already do the matching.
- **Unclaimed property and dormant accounts.** States cap finder fees and void claim purchases. It is a service
  business, not an owned asset.
- **Class-action, antitrust opt-out and bankruptcy claims trading.** Burford, Xclaim, Cherokee and distressed
  funds already price it. This is the brief's Legalist kill applied again.
- **Lapsed patents.** Only the owner can revive (37 CFR 1.137, with extra scrutiny for delays over 2 years), and
  35 USC 41(c) intervening rights protect anyone who used the invention during the lapse. Low value.
- **Carbon and biodiversity credits.** The whole VCM was worth $1.04B in 2025 (Sylvera), and rated credits
  already command a premium ($26/t vs $14/t for ARR). The quality arbitrage has been priced in by Sylvera,
  BeZero, Calyx and Renoster.
- **Domains and abandoned trademarks.** The ceiling is small, residual-goodwill law creates risk, and River West
  Brands and domain investors are already in it.
- **Tax liens, trade credit and government receivables.** Competitive bid-down auctions and fintech factoring
  make this a crowded spread business.
- **Distressed or zombie biotech IP.** XOMA and Concentra (Tang) are serial buyers. It also belongs in a pharma
  lane.
- **FCC terrestrial auctions** (AWS-3 re-auction, upper C-band). This is pricing skill against carriers and Grain,
  with no claimable edge.

## Sources

- AST S-band ITU priority acquisition, $64.5M: https://www.telecomtv.com/content/access-evolution/ast-spacemobile-agrees-to-acquire-global-s-band-spectrum-priority-rights-held-under-the-itu-53590/
- Fleet Space European frequency assets: https://fleetspace.com/newsroom/fleet-space-continues-global-expansion-with-first-acquisition-of-european-frequency-assets
- D2D deal roundup (EchoStar, Globalstar, Iridium, Omnispace): https://www.lightreading.com/satellite/satellite-d2d-dealmaking-spacex-amazon-rocket-lab-and-the-spectrum-they-re-after
- SpaceX-EchoStar $17B: https://www.fierce-network.com/wireless/spacex-scoops-echostar-spectrum-17b
- Rwanda 327k-satellite filing: https://advanced-television.com/2021/10/18/rwanda-files-with-itu-for-327000-satellites/
- MLC unmatched balances: https://www.musicbusinessworldwide.com/the-mlc-has-paid-out-more-than-4-2bn-to-songwriters-and-publishers-to-date-and-will-begin-market-share-distributions-of-unmatched-and-unclaimed-royalties-in-april-2027/
- Claimy (AI black-box matching): https://www.frenchtechjournal.com/claimy-wants-to-use-ai-to-end-musics-missing-money-problem/
- Termination rights practice: https://www.agg.com/news-insights/publications/attention-songwriters-and-recordings-artists-of-the-80s-and-90s-time-is-running-out-to-reclaim-your-copyrights/ ; https://songwritersguild.com/copyright-termination
- IEEPA ruling and refunds: https://www.cohnreznick.com/insights/supreme-court-invalidates-2025-ieepa-tariffs/ ; https://www.argusmedia.com/es/news-and-insights/latest-market-news/2796596-us-court-orders-refunds-on-trump-s-ieepa-tariffs
- Refund-rights secondary market: https://www.troutman.com/insights/phase-one-ieepa-tariff-refunds-are-hitting-bank-accounts-what-importers-should-do-now-and-implications-for-the-secondary-market-in-refund-rights/ ; https://www.hklaw.com/en/news/intheheadlines/2026/08/tariff-litigation-boosts-novel-market-for-importers-refund-rights
- Water Asset Management in Colorado: https://www.cbsnews.com/news/new-york-investors-snapping-up-colorado-river-water-rights-betting-big-on-an-increasingly-scarce-resource/
- OpenET: https://www.edf.org/media/edf-nasa-dri-and-google-announce-web-application-transform-water-management-western-united
- Carbon market 2025 value and premiums: https://www.sylvera.com/blog/sylvera-state-of-carbon-credits-2025-market-shifts-from-volume-to-value
- XOMA zombie-biotech strategy: https://www.biopharmadive.com/news/xoma-royalty-zombie-biotechs-liquidate-wind-down/760535/
- AI continuation/infringement tools: https://www.patlytics.ai/blog/best-patent-analysis-software ; https://xlscout.ai/continuation-patent-strategy-in-2026-how-ai-maximises-portfolio-coverage/
- Figures from memory, not re-verified this run: Sony-Queen ~$1.27B; Concord-Hipgnosis ~$1.6B; VLSI v Intel $2.18B (vacated); ~$45B global music copyright value; the EU 2 GHz MSS expiry date.
