# D07 PLAYBOOK: red team, data-reality lens

Date: 24 Oct 2026. Reviewer: data-reality red team. The shared web-search budget was used up when this review started, so no new searches ran. Facts come from D07, M06, M19, M20, M33, L17-L19, L31 and L40. My own estimates are marked (unverified).

## Verdict in one paragraph

PLAYBOOK is not refuted. Its frame (play risk, lookback, portfolio) is the right shape for a land business, and two of its parts sit on real data: the heat element (thousands of censored temperature readings) and the portfolio engine (BLM bid sheets, MLRS, M34 costs). The part that makes it new, the multi-channel discovery-process model [F], does not have the data it needs. It wants dated finds, by channel, with a size mark, plus dated effort per channel. Public data gives about 20 size marks, no dated effort for the channel that found the big blind fields, and no first-signal dates for spring-marked systems. Pg element tables for pathway, fluid and cap have almost no public failure labels. The pass bars rest on about 8-10 post-2008 blind finds. Every flaw has an AI-leveraged fix, but [F] should be demoted from "spine" to "prior generator" until our own sensor effort feeds it. Score: 15/25.

## Flaws and fixes

**F1. The discovery ledger is much thinner than "about 400 dated systems" (serious).** The USGS Great Basin inventory has 205 systems, but 99 are "probable". A probable system has no discovery date by definition. It is inferred, often by the USGS's own model, so using it even as a soft hold-out is circular. Of about 106 known systems, only about 18-28 have a size mark (EIA-860 nameplate). Nameplate is plant, not resource. It is phased (McGinness 72 to 160 MW) and censored below about 10 MW (M33). So beta_c (size bias) per channel is fitted to roughly 20 points split over 3-4 channels. M33's 0.03 rank correlation used first-power year on 18 fields, not discovery date.
*Fix:* do not fit beta_c per channel. Fit one beta with channel offsets, under a strong prior from global field histories (NZ, Iceland, Kenya, Turkey, about 200 fields in WGC country updates). Use USGS 2008 per-system MWe triangles as noisy size marks with a wide error model, not as truth. Run SBC on synthetic Westerns at n = 20 marks first. If beta is not recovered there, publish that and drop it.

**F2. The springs channel has no timing (serious).** Leaky systems were known from settlement, often before 1900. Their "first-signal date" is a left-censored blur. The Plackett-Luce order term needs dated finds under measured effort. For springs, effort is "someone rode by". So about 60% of known systems (M19) carry almost no order information.
*Fix:* treat spring-marked systems as a pre-period stock, observed at t0, with detection tied only to leakiness L_i. Fit the order likelihood only on post-1960 finds, where effort is recorded. Let an LLM agent pull first-mention dates from 19th-century GLO survey notes and USGS Water-Supply Papers (Waring 1965 spring list) only as a check.

**F3. Mining-hole effort is not public, and it is the channel that matters (serious).** L31 shows 8 of 11 US blind finds came from holes drilled for something else, and the big ones (McGinness, Blue Mountain, Tungsten Mountain, Don A. Campbell) came from mining holes. Nevada has no filing duty for mineral holes (M20, D06). MRDS is a deposit list, not drilling effort. So E_c for the key channel is a guess. NDWR driller reports give water-well effort, but temperature was recorded on only 4-6% of reports before 2015 (M06). That is fine for effort, weak for detection.
*Fix:* build a mining-effort proxy with AI extraction. Sources: MLRS mining-claim filings by year and section; BLM Notices and Plans of Operations (drill-pad counts); NBMG annual "Major Mines of Nevada" reports; NI 43-101 and SEDAR technical reports, which list metres drilled per project per year. Calibrate the proxy where both claims and real drill metres exist. Keep its error as a latent in the effort field (Fithian-style shared bias, L18).

**F4. Play cells are nearly empty (serious).** 150-300 plays against 100-200 confirmed systems means under one system per play. Hierarchical Beta over play x province then returns the prior in almost every cell. Archetype labels (B1-B7) for known systems are themselves interpretations, and B3/B4 have perhaps 0-5 confirmed members each.
*Fix:* collapse to about 10-15 archetype-province groups for fitting. Keep the fine play map only for reporting. Have an agent tag each known system's archetype with a probability vector from its literature, so labels are soft. Flag blind-archetype play chances as prior-dominated.

**F5. Public failure labels cover one element (serious).** The failure ledger seed is real: 124 NDOM EXP TG holes, 786 OFR 99-425 holes over 82 prospects, about 1,600 plugged CalGEM TG holes, 442 NBMG scanned TG boreholes (M19, M20). But nearly all say only "cool to depth d". That labels the heat element. "Hot but tight" needs flow tests, which are mostly Ormat and other private data. "Masked" needs a full T-z curve with reversal, which most single-gradient tables lack. So the pathway, fluid and cap tables would be isotonic-calibrated on tens of labels. The Pg = product of five elements also assumes independence that the data cannot test.
*Fix:* (a) vision-model digitisation of the 2,002 NBMG scanned logs for full T-z curves, which separates "no heat" from "masked". (b) OSTI and GDR full reports from DOE-funded wells (Play Fairway Phase 2-3, FORGE, EGS demos at Desert Peak 27-15, Patua, Newberry), which include flow and injectivity tests. (c) Ormat 10-K and S-1 impairment notes and BLM sundry notices for project-level causes. (d) IFC 2,500-well data as a prior. Fit a joint element model with a shared latent, not a product. Report pathway risk as a prior until our own holes add labels.

**F6. The prospect inventory leaks into the 2008 hindcast (serious).** The 1,430 Faulds polygons were mapped mostly after 2010, partly by studying known systems. Using them as the 2008 prospect set gives the hindcast post-2008 knowledge. They also cover only the Great Basin. The Cascades, Snake River Plain and Rio Grande rift have no equal. GeoDAWN magnetics cover only part of NW Nevada and NE California.
*Fix:* rebuild a 2008-vintage inventory with the U-Net run on pre-2009 inputs only (NED, Qfaults, PACES gravity, NURE). Score how many post-2008 finds sit inside it. Outside the Great Basin, run the same mapper and mark it as out-of-domain.

**F7. The pass bars have no power (moderate).** Post-2008 Nevada has about 8-10 blind finds and about 425 MW, of which McGinness is 160 MW. Bar 2 (60% of MW in the top third of plays) is decided by one field. Bar 3 (2x the GBM, with a bootstrap CI excluding 1) cannot be met at n = 8-10 unless the lift is huge. Bar 1 (a count inside a 90% interval) is easy to pass with a wide posterior. McGinness and Blue Mountain also had hot holes on record before 2008 (L31), so they are not blind at the freeze. Pumpernickel had old holes too.
*Fix:* make the gating test a likelihood score on thousands of post-2008 temperature readings and TG outcomes, which has power. Report blind-find capture as a number, not a gate. Add synthetic-world bars with known truth.

**F8. Crowd model sees only public layers (minor).** Zanskar holds a private 27,000-sample compilation (L05). Fix: infer rival belief from actions (nominations, bids, permits by date), which D07 already partly does.

## Does it survive 100-200 confirmed systems?

Partly. The heat element, lookback and portfolio engine survive. The count forecast N_remaining does not, as a stand-alone number. It becomes a prior-driven creaming curve whose best use is the one D07 names last: a live test of whether our own sensor channel steps the curve up. Our own designed survey cells give the dated, measured effort that public data lacks. So [F] becomes strong only after a year of our own search.

## Scores

| Axis | Score |
|---|---|
| Calibrated certainty | 3 |
| Data realism | 2 |
| Buildable in 6 months | 2 |
| Edge vs Zanskar | 4 |
| Drives rights and sensors | 4 |
| **Total** | **15/25** |
