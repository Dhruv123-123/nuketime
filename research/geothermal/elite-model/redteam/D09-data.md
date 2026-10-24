# D09 KEYSTONE: red team, data-reality lens

Date: 24 Oct 2026. Reviewer: data-reality red team. No new web searches. Facts come from D09 and the evidence files L05, L09, L16, L18, L19, L31, L40, M18 and M19. My own estimates are marked (unverified).

## Verdict

KEYSTONE is not refuted. Its data stance is mostly right. It learns from readings and cold holes, not only from about 100-200 system labels. It keeps effort in the thinning term and bans label proxies from the existence term. But it adds a new label layer that the public data cannot fill: an 11-class play archetype, a failure-mode tag per dry hole, and "decisive signal" matches for explanations. Most of these labels do not exist. Where they exist, they come from the same found, leaky systems the model is meant to see past. Every flaw below has an AI-leveraged fix. Score: 16/25.

## Flaws and fixes

**F1. Archetype labels are nearly empty (serious).** The B1-B7 table is this project's own synthesis (L09, "our synthesis"). No expert has tagged Western systems with it. B3 has one public example (Big Blind). B6 has one (Eureka Low). B4 rests on Kimama, a drill hole, not a system. Historic labels are mostly B1 and B2, because about 60% of Great Basin systems were found where water reached the surface (M19). With about 150 systems split 11 ways, five or six classes have three examples or fewer. Pass bar 3 asks the archetype to match "the expert type" for 50 held-out systems. That expert type does not exist yet, so the test would grade the model against its own taxonomy.
*Fix:* treat archetype as a latent, not a label. Run LLM plus vision extraction of the 300-600 conceptual-model figures (L09) into cards. Then have two or three outside experts tag 50-80 systems blind, and report their agreement (Cohen's kappa). Score the model against the expert consensus only where kappa is above about 0.6. For v1, fit four templates plus "unknown" (as month 1 plans). Add a class only when the data supports it.

**F2. Masks can explain away every negative (serious).** The headline edge is "a cold 150 m hole barely lowers psi under B4 but lowers it a lot under B2". That is only safe if the mask is pinned by its own evidence. Most cold holes are shallow. Water wells and TG holes stop at 50-300 m. GeoCore found only 148 cold wells deeper than 400 m in the Great Basin (L05). If the archetype posterior can move freely, the model will "explain" a cold hole by moving mass to a lid or sweep class. Negatives then stop biting. This failure is silent, and SBC on worlds drawn from the templates will not catch it.
*Fix:* make the mask need positive support. Tie lid and sweep priors to mapped aquifer type, NWIS heads, carbonate maps and recharge. Report per cell how much of a negative's log-BF the mask absorbed. Add a portfolio prior predictive check: the share of the West assigned to masked states must match the 4-8 known masked or blind cases, after effort thinning. Treat cells where the mask "rescues" the posterior as VOI targets for a deep log or E-MT. Do not treat them as buys.

**F3. Deep negatives with failure modes are few and not tagged (serious).** Completion reports rarely say "tight" or "outflow". The real hard-negative pool is about 3,000-5,000 depth-censored holes across CA, NV, UT and OR (M19). That includes CalGEM's 1,586 plugged TG holes, NDOM's 159 out-of-field wells and 786 Phillips/Chevron holes (USGS OFR 99-425). Deep dry holes with usable logs number in the low hundreds (unverified). They cluster at known fields, where the failure mode is often "outflow, not upflow".
*Fix:* infer failure mode as a latent from what the reports do hold: lost circulation, flow-test rate, temperature-log shape (an inversion means outflow) and alteration logs. Use LLM extraction with N=5 self-ensembles and keep the spread as noise. Never use a typed failure label as truth.

**F4. Literature priors reuse the evaluation labels (moderate).** DTZ enrichment of about 4.8x and pull-apart 2.2x come from the Faulds share table, which was computed on today's known systems (L09). The FSS inventory itself was mapped hardest around known fields. If these numbers seed templates and the same systems are then scored in hindcast, the test leaks.
*Fix:* refit enrichments inside each CV fold and each hindcast freeze. Widen literature values into weak hyperpriors. Add a "mapping effort" layer (date and scale of fault mapping) to the thinning term, as with springs.

**F5. Known-time is hard to rebuild (moderate).** The 2005 hindcast needs every fact's first public date. Scans carry the scan date, not the date the data existed. INGENIOUS layers, Quaternary fault versions and FSS polygons were made after 2015 with today's systems in mind. Only about 6-10 post-2005 Nevada blind finds exist (L31), so the test has weak power.
*Fix:* agents date each fact from the source document (report date, permit date, NDOM release after the 5-year confidential window). Freeze layers by version (USGS Qfaults releases, NBMG map dates). Where a layer cannot be dated, drop it from the hindcast. Add power by running the same freeze in Utah, Oregon and abroad (Kenya, Turkey, NZ), and by reporting a bootstrap interval on capture, not a point.

**F6. Sparse geophysics for the neural operators (moderate).** The MT operator needs station ensembles. Public MT is mostly EarthScope USArray at about 70 km spacing. Dense local MT is held by operators. The FNO needs natural-state models to calibrate against, and only about 20-40 public Western models exist (unverified). Water chemistry exists mostly where springs exist, so chemistry carries spring-effort leakage into F.
*Fix:* digitise published MT sections and resistivity models with VLM agents. Model "a sample exists here" as effort in the thinning term, separate from what the sample says. Budget E-MT nodes (P03) where MT VOI is highest.

**F7. Location error vs cell size (minor).** Old mining and TG holes are often located to a PLSS section (about 1.6 km). Refinement to 125 m cells and page-level case-file citations can give false precision.
*Fix:* keep loc_err in every likelihood. Block case-file claims finer than the location box. Drone collar search (P09) fixes high-value holes.

## Does it survive 100-200 confirmed systems?

Yes, better than most designs. Readings, cold holes and physics priors do most of the work. The 100-200 labels only fit the existence intensity and the size marks. What does not survive is the 11-class archetype layer as written. Collapse it to four classes plus "unknown" until labels exist.

## Score (out of 25)

| Axis | Score | Why |
|---|---|---|
| Calibrated certainty | 3 | SBC is self-referential; masks can absorb negatives |
| Data realism | 3 | Archetype and failure labels mostly missing |
| Buildable in 6 months | 2 | KG, 11 templates, FNO, amortised inference and agents in 6 months is too much |
| Edge vs Zanskar | 4 | Play-aware negatives and case files are real gaps in GeoCore |
| Drives rights and sensors | 4 | Weakest-link sensing and case files fit the bank well |
| **Total** | **16** | |
