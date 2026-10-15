# Round 2 deep-dive: D2D satellite spectrum rights via ITU priority filings

Written 15 Oct 2026. Adversarial review of lane_claims.md candidate 1 (scored 6/10 there).
I used 19 of 20 WebSearch calls plus WebFetch. I did not open SNL, SRS or BR IFIC from this
network. Facts I recalled but did not re-verify in this run are marked (unverified).

## Verdict: 3/10. Kill it as a Terranox analogue. Keep it only as a scavenger side bet.

An ITU filing looks like a mineral claim: it is cheap, first-come and public. In practice it is a
claim with three properties that break the Terranox template.

1. **It expires unless you launch.** Under RR 11.44 the filing lapses if a satellite does not operate
   in one of its planes for 90 days within 7 years of filing. Resolution 35 then reduces the filing
   to whatever share of the constellation is actually deployed. You can scavenge a filing, but you
   cannot hold one passively.
2. **In the D2D bands that matter, the senior slots are already held by strategic buyers.** A new
   filing today joins the back of the queue. It has no hold-up value, because coordination
   obligations run from junior filers to senior ones, not the other way round.
3. **ITU priority gives no right to serve users in any country.** That right comes from national
   licences (FCC, the EU selection, ACMA, and so on) and, in IMT bands, from the mobile operator's
   licence.

The one version that has worked is buying distressed but still-alive senior filings and selling
them to D2D operators: Sirion/Helios Wire to EchoStar, and Sky and Space Global to CCUR to AST.
That trade is real, but there are only about 5-15 such assets worldwide, it has been done already,
and finding them needs a spectrum consultant (Tim Farrar named the AST seller from a press release
within hours), not ML.

## 1. How ITU priority actually works

- **The steps.** For coordinated systems the sequence is API, then a coordination request
  (Appendix 4 data) under Art. 9, then notification and recording in the MIFR (Art. 11). Most
  non-GSO MSS systems in the L/S/2 GHz bands fall under RR 9.11A. The date the BR receives a
  *complete* coordination request sets priority. Later filers must coordinate with every earlier
  one, and the earlier filer only has to accept interference it agrees to.
- **Publication.** Each filing is published in the weekly BR IFIC (Space Services) and shows in the
  SNL (free) and SRS (subscription/DVD). Bilateral coordination agreements are *not* public, so the
  data shows a filing's status but not who has settled with whom.
- **Bringing into use (BIU).** One space station must operate on the notified frequencies in one of
  the notified planes for 90 continuous days within 7 years of the filing's receipt. After a
  suspension (RR 11.49), "bringing back into use" (BBIU) uses the same 90-day test. EchoStar did
  exactly this. Its SIRION-1 2 GHz NGSO filing (administered by Australia) was preserved by flying
  the Lyra-4 cubesat at 650 km from 3 Jul to 1 Oct 2025. EchoStar then claimed "highest-priority
  spectrum rights in the 2 GHz band" for NGSO worldwide. So keeping a filing alive costs a cubesat,
  roughly $1-5M (my estimate), not a constellation.
- **Resolution 35 (WRC-19).** Non-GSO filings must deploy 10% of the filed satellites within 2
  years after the BIU deadline (year 9), 50% within 5 years (year 12) and 100% within 7 years
  (year 14). A missed milestone shrinks the recorded system to the number actually deployed. A
  1,000-satellite paper filing kept alive by one cubesat therefore keeps its priority date but
  shrinks unless a buyer deploys under it. That is why AST's payment to CCUR is partly conditional
  on AST launching an L/S satellite under the rights.
- **Cost to file.** Under Council Decision 482 (2013 schedule, since modified in C2025), the API
  for non-GSO costs CHF 570. A coordination request costs CHF 20,560 flat (category C1, at least
  100 units) or a CHF 5,560 start plus CHF 150 per unit, rising to about CHF 33,000 for C3.
  Notification costs about CHF 31-58k. Each administration also gets one free filing a year.
  Non-GSO filings with several mutually exclusive configurations are charged per subset. So the
  ITU fee is tens of thousands of CHF, and the real costs are elsewhere: the engineering for the
  Appendix 4 data, counsel, and above all **persuading an administration to sponsor and stand
  behind the filing** (it takes on Art. 22 and coordination liability). Since Res 35 there is
  also the BIU spacecraft.
- **Can a new small-administration filing gain priority today that big operators must pay for?**
  In L-band (1.5/1.6 GHz), 2 GHz (1980-2010/2170-2200 MHz) and 2.4/2.5 GHz MSS: **no.** A filing
  received in Oct 2026 sits behind decades of Inmarsat, Iridium, Globalstar, Thuraya, EchoStar
  (SIRION), Omnispace, EllioSat (Sky and Space Global), SpaceX and Chinese filings. Senior filers
  owe nothing to a junior one. The only open race would be **new allocations from WRC-27 agenda
  item 1.13** (MSS in IMT bands, 694 MHz-2.7 GHz). Even there:
  - The method options are A (no change), B (secondary MSS for D2D only) and X1 (primary, with
    footnotes stating that MSS cannot claim protection from IMT). Under either B or X1, an MSS
    filing cannot block or extract rent from the terrestrial MNO, and the MNO's national licence
    is the senior right in practice. SpaceX/T-Mobile and AST/AT&T/Verizon already work this way.
  - The race starts when the Final Acts enter into force (about 2028-29), and SpaceX, AST,
    Lynk/Omnispace, Amazon and the Chinese operators will file on day one with large teams.
  - So a filing is a first-come claim, but in the bands that matter the land has already been
    staked.

## 2. Evidence on the economics of paper satellites

| Case | What changed hands | Price | Lesson |
|---|---|---|---|
| Tongasat (1990-) | Tonga filed for 16 GEO slots, cut to 6 by the ITU and later 9, and leased them | Asked $2M/yr per slot; ~$45M market cap (1994) | Worked once, caused outrage, led to ITU tightening; ended in fraud conviction (2018) |
| Sirion Global / Helios Wire to EchoStar (Oct 2019) | Australian-administered global 2 GHz MSS NGSO filing (SIRION) | Not disclosed | The template exit. A small startup's ACMA filing became, after a 2025 BBIU, part of what SpaceX bought |
| Sky and Space Global, then CCUR, then AST (Aug 2025) | EllioSat Ltd (owns Sky and Space Sp. z o.o., Poland; CCUR also bought SSG UK Ltd), holding 1980-2010/2170-2200 MHz LEO MSS ITU priority | $64.5M: $26M at close (paid in shares), $10M at year 2, $10M at year 3, $16.65M when an L/S satellite enters service, $1.85M after 90 days of operation | Shows the scavenger trade working: SSG went into administration in 2020 and a micro-cap holding company (CCUR, Austin) picked up the remains. About 29% of the price depends on the buyer actually using the rights |
| Omnispace + Lynk merger (Oct 2025) | 60 MHz S-band, "high-priority" ITU filings (Omnispace's rights trace to ICO Global's 2 GHz system, unverified), with SES as strategic holder | Not disclosed | ITU priority is an asset that operators combine, not one they sell |
| SpaceX-EchoStar (Sep 2025; FCC approved May 2026; transfers ~Nov 2027) | US AWS-4/H-block/AWS-3 *licences* plus global 2 GHz ITU priority (SIRION) | ~$17B plus ~$2.6B (≈$19.6B) | Most of the value is in US terrestrial/MSS licences. ITU priority was a component |
| Amazon-Globalstar (Apr 2026, closing 2027) | L/S-band MSS licences in 120+ countries, 24 gateways, Apple relationship | $11.6B ($90/share) | A licensed, operating system, not paper |
| Ligado / AST (2025-26) | AST rights to Ligado's US L-band, through Ligado's bankruptcy; Inmarsat disputes; Iridium opposed | n/a | The asset is the national licence and a co-ordination agreement, and it is being fought in court |
| Rwanda "Cinnamon-217/937" (2021) | 327,320 satellites in 27 shells, filed for Greg Wyler (E-Space) | n/a | The African Union and SANSA said they were blindsided. E-Space later also filed in France. Paper of this kind is cheap and draws political backlash |

The prices that matter for this idea are **$64.5M for a distressed senior 2 GHz filing**, partly
paid in stock and partly contingent, and an undisclosed, probably small, price for Sirion. The
$40B headline deals are for *national licences plus operating systems* and are not an
aggregator's exit.

## 3. Who already does filing arbitrage

- **Strategic operators that buy filings:** EchoStar (Helios/Sirion, 2019), AST (EllioSat, 2025),
  SpaceX (EchoStar, 2025-27), Lynk/Omnispace/SES, Amazon (Globalstar), Fleet Space (European
  frequency assets, 2023, from lane_claims), and Rivada (Ka-band filings from Kleo Connect's
  Liechtenstein filings, then a court and ITU dispute; unverified).
- **Distressed scavengers:** CCUR Holdings bought SSG's UK and Polish entities out of the 2020
  administration and sold them to AST in 2025. SSG itself was put into liquidation in Oct-Nov 2025.
  This is the exact "find the weak holder of a live senior filing" play, done by a Texas holding
  company with no ML.
- **Flag administrations and filing agents:** Tonga/Tongasat, Papua New Guinea, Liechtenstein, the
  Isle of Man (Manx Telecom/ManSat, through the UK), Rwanda (for E-Space), and Australia/ACMA (the
  route for Sirion and EchoStar). Filings are prepared by consultancies and law firms: Transfinite,
  Hogan Lovells, Wiley, Milbank, Herbert Smith Freehills and others. The ITU Academy teaches the
  process.
- **Analysts:** Tim Farrar (TMF Associates) and Octus (credit research on EchoStar's spectrum
  collateral) track who holds what.

## 4. Is there an ML edge?

It is weak.
- SRS and SNL are already *structured databases*, with Appendix 4 fields, dates of receipt,
  suspensions, BIU and Res 35 submissions. The BR's SpaceCap/SpaceQry and Transfinite tools query
  them directly. Nothing here is like decades of scanned assessment reports.
- The relevant set is small. Global MSS filings in L/S/2 GHz/2.4 GHz that are both senior and
  alive number in the dozens, and a two-person consultancy can track them by hand.
- The parts that are truly hidden (bilateral coordination agreements, administration willingness,
  the holder's cap table) are not in any public dataset, so ML cannot read them.
- "Predicting which bands D2D will need" is set openly through the WRC-27 agenda item 1.13 studies
  (CPM text, regional briefs from CEPT, APT, ATU and Uganda's UCC). Everyone reads them.
- What remains is an LLM-assisted diligence tool. That is a service, and the brief excludes
  services.

## 5. Ceiling, defensibility, legal and political risk

- **Ceiling for an aggregator.** Supply is perhaps 5-15 distressed but still-alive senior filings
  worldwide, with exits at $10-100M each, so $0.1-0.5B over a decade. The buyers are a monopsony of
  about six (SpaceX, AST, Amazon, Lynk/Omnispace/SES, Viasat/Space42/Equatys, and Chinese
  state-backed operators). Billions require actually operating a constellation, at which point
  you are a satellite operator.
- **Defensibility.** The priority date itself cannot be copied, but:
  - the filing lapses under the BIU and Res 35 rules unless someone spends on hardware;
  - the sponsoring administration can suspend it, cancel it or refuse to cooperate, and the
    administration is the legal holder;
  - national regulators can ignore it. The EU's May 2026 proposal re-awards the 2 GHz band from
    May 2027 on security, "Union added value" and EU-control criteria, reserving 2 of 6 blocks for
    EU governmental use. Starlink is arguing in public that the EU should respect ITU priority,
    which shows the point is contested.
- **Regulatory direction.** Every WRC has tightened rules against paper satellites (Res 35 at
  WRC-19, further WRC-23 work, and WRC-27 agenda item 7 including topic E on RR 4.4 filings). The
  FCC is opening D2D access through its own rulemakings (SCS framework 2024; unlicensed part 15 D2D
  proposal for Aug 2026; the EchoStar 2 GHz use inquiry), not through ITU priority. Speculative
  filings by small administrations draw objections from the AU, regional bodies and operators.
- **Political risk is high.** A Western startup buying a small state's filing to extract rent from
  SpaceX or Amazon looks like Tongasat. It would be the first target of the next tightening, and
  US and EU regulators would side with the operators.

## Scorecard against the four Terranox conditions

| Condition | Result |
|---|---|
| Cheap, first-come claim | The fee is cheap (≈CHF 20-35k) and priority is first-come, **but** the claim lapses without a launch, needs a sponsoring state, and the D2D bands' senior slots are already taken |
| Public but illegible data | Fails. The data is public *and* structured. The hidden parts are not in any dataset |
| Asset worth orders of magnitude more than the claim | Only for the handful of old, senior, alive filings ($64.5M against a few $M), which are already known |
| Value without an incumbent's channel | Fails. The only exit is about six strategic buyers, plus national licences you do not control |

**Score: 3/10.** It is a credible niche trade (distressed senior filings, sold to AST, SpaceX or
Amazon), but it is small, already done by CCUR, Helios and Sirion, and limited by supply, not by
ML. It is not a Terranox analogue.

## Cheapest test if anyone still wants to pursue it (2 weeks, no data purchase)

From the SNL (free), list every non-GSO MSS filing in 1518-1675, 1980-2025, 2160-2200 and
2483.5-2500 MHz with its date of receipt, BIU/suspension/BBIU status and Res 35 submissions. Mark
holders that show distress (insolvent, delisted, no launches). If fewer than 5 senior, alive
filings have weak holders, the scavenger trade has no room left either.

## Sources
- [AST 8-K summary (StockTitan)](https://www.stocktitan.net/sec-filings/ASTS/8-k-ast-space-mobile-inc-reports-material-event-a45cca0f343f.html); [Fierce: seller speculation](https://www.fierce-network.com/wireless/d2d-darling-ast-spacemobile-sparks-intrigue-new-spectrum-pact); [TechLeap: EllioSat/CCUR](https://finder.techleap.nl/news/feed/ast-spacemobile-acquires-elliosat-for-26m); [K&L Gates deal note](https://www.klgates.com/lawyers/Robert-S-Matlin/experience); [Comm Daily](https://communicationsdaily.com/news/2025/08/07/AST-SpaceMobile-Says-Its-Buying-SBand-Rights-Globally-2508060005)
- [Sky and Space Global (Wikipedia)](https://en.wikipedia.org/wiki/Sky_and_Space_Global)
- [EchoStar SIRION-1 BBIU](https://ir.echostar.com/news-releases/news-release-details/echostar-perfects-highest-itu-priority-worldwide-2-ghz-ngso); [Via Satellite](https://www.satellitetoday.com/connectivity/2025/10/03/echostar-secures-milestone-with-2-ghz-band-priority/); [EchoStar acquires Helios Wire](https://ir.echostar.com/node/15751)
- [ITU Decision 482 (C2013)](https://itu.int/en/ITU-R/space/Documents/Decision%20482(C2013)-E.pdf); [ITU cost recovery](https://itu.int/ITU-R/go/space-cost-recovery/en)
- [UCC brief on WRC-27 AI 1.13](https://www.ucc.co.ug/wp-content/uploads/2026/07/Brief-of-AI-1.13.pdf); [UCC brief on AI 7](https://www.ucc.co.ug/wp-content/uploads/2026/06/Brief-on-AI-7.pdf); [SatNews on WRC-27 D2D](https://satnews.com/2026/09/24/the-itus-outgoing-spectrum-chief-expects-wrc-27-to-find-room-for-direct-to-device-151-mobile-operators-are-already-building-toward-it/)
- [Noerr on EU 2 GHz proposal](https://www.noerr.com/en/insights/more-eu-level-steering-new-selection-criteria-new-obligations-the-euproposal-on-the-2-ghz-mss-band-and-its-implications-from-2027-onwards-); [Space Intel Report: Starlink to EU](https://www.spaceintelreport.com/starlink-to-eu-commission-the-us-respects-itu-priority-filings-on-mobile-satellite-spectrum-you-should-too/)
- [Amazon-Globalstar (TNW)](https://thenextweb.com/news/amazon-agrees-to-acquire-globalstar-in-an-11-6b-deal); [SpaceX-EchoStar FCC approval (scan)](https://decision-intel.shapingtomorrow.com/scans/regulation-standards-policy-change/2026-05-15-d2d-spectrum-unbundling/scan.html); [Lynk-Omnispace (Fierce)](https://www.fierce-network.com/wireless/lynk-omnispace-merge-drive-grow-d2d)
- [FCC D2D part 15 vote](https://broadbandbreakfast.com/fcc-to-vote-on-proposal-for-more-direct-to-device-spectrum-in-august/); [Docket Rocket on EchoStar 2 GHz inquiry](https://docketrocket.substack.com/p/docket-rocket-vol-4-inquiry-into)
- [Rwanda Cinnamon / Wyler](https://advanced-television.com/2023/06/30/wyler-now-involved-with-400000-satellites/); [Tongasat (Wikipedia)](https://en.wikipedia.org/wiki/Tongasat)
