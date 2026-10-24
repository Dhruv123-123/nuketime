# D10 CONCLAVE: red team, scientific validity lens

Date: 24 Oct 2026. Reviewer: science red-team agent. Scope: identifiability, calibration, leakage, physics consistency, and whether the certainty claims can be checked honestly. No web searches. Facts come from D10 and the L-digests it cites. My own judgements are marked (unverified) where they need a check.

## Verdict in one line

Not refuted. Stacking many honest experts is a sound idea, and the bitemporal ledger plus hashed forecasts is the right spine for honest validation. But as written, the stacking layer is not identifiable for the target that pays (Y1 existence), the hindcast freezes are mostly illegal for modern covariates, and the agent tournament is a forking-paths machine. All three have credible fixes. **Score: 16/25.**

## Flaw 1 (serious). Stacking weights for Y1 cannot be learned

Section 4.3 fits weights on thousands of well temperatures (Y2, Y4) and on "tens" of dated discoveries (Y1). Each expert's weight is a softmax of a linear function of about five descriptors, several of them categorical (province, archetype). With ten experts that is roughly 50-150 free parameters (unverified count). Tens of positives cannot pin that down. The Dirichlet prior then pulls everything back to E1. So the Y1 output is, in practice, SENTINEL-COX with extra steps. The "stacked beats single" claim would be true for temperature and silent for existence.

Worse, the experts that matter most for blind finds are the ones that abstain on Y2: E8 (surface), E9 (analogue) and part of E6. Their weights can only be learned from Y1. Weights learned on temperature do not transfer to existence, because a model can be great at T(z) near wells and useless at ranking blank basins.

**Fix.** Stack per target, not globally. For Y1, add a middle-tier target with hundreds of labels: the Y3 failure ladder from AI-extracted completion reports (every dry hole, TG hole and slim hole tagged). Cut the Y1 weight model to two descriptors (label distance, data modality count) and report its effective number of parameters. Use synthetic planted-system worlds from E4 to check that weights are recoverable before trusting them on real data. D10 lists this in risks; it should be a release gate.

## Flaw 2 (serious). Abstention is not "handled natively"

Hierarchical stacking (Yao, Vehtari and Gelman, Bayesian Analysis 2022) assumes every model scores every held-out point. When experts abstain, the weights must be renormalised over whoever is present. Experts abstain where data are thin, which is where blind systems live. That makes the weight fit biased toward easy cells.

**Fix.** Make the abstention pattern an explicit z descriptor. Or fill abstentions with E1's prediction so each expert is scored as "E1 plus my increment". An agent can run both and report the difference.

## Flaw 3 (serious). The hindcast freezes leak

Freezes at 1980, 1990, 2005 and 2015 cannot be honest for many inputs. EMIT is 2022 onward. AlphaEarth embeddings are 2017 onward. GeoDAWN is recent. The USGS 2025 favourability map and INGENIOUS layers were built knowing today's systems, and D10 feeds them into E2 and E10. E3 starts from LANL In-Context Earth, which was trained on the full modern well set (unverified, but likely), so a 2005 hindcast scores wells it has already seen. The Faulds 1,430 FSS polygons used by E6 were partly mapped because systems were known there. And the four named post-2005 test systems are famous to every LLM in the agent layer.

**Fix.** An agent writes a freeze-legality card for every layer: acquisition date, publication date, and whether known systems shaped it. Retrain E3 from scratch on pre-freeze wells only. Rebuild FSS polygons from pre-freeze papers. Run each hindcast twice, legal-only and with leaky layers on. The gap is a measured leak. For satellite layers, accept a stationarity assumption but test it on truly prospective labels: Zanskar's 2025-26 announcements, new NDOM permits and GDR logs that post-date every model artefact.

## Flaw 4 (serious). The agent tournament overfits the hindcast

Agents test "hundreds of hypotheses a month" against one frozen hindcast with tens of blind positives. Any held-out set reused that often stops being held out. The gate is "raises held-out log score", with no multiplicity correction. After a year the hindcast is fitted, not tested.

**Fix.** Keep a sealed vault: one whole province (say Oregon or Idaho) and all labels after a fixed date, opened once per quarter by a human. Gate tournament ideas with a reusable holdout (Dwork et al., Science 2015, "thresholdout") or e-values with alpha spending. Log every test in the ledger so the true number of tries is public in the data room.

## Flaw 5 (moderate). Calibration and FDR guarantees assume exchangeability

Per-province isotonic calibration of Y1 on a handful of events will overfit. Conformal selection (Jin and Candes 2023) gives FDR control only if calibration and test units are exchangeable. New blank-basin prospects are not exchangeable with past drilled sites. Wells were placed where people already suspected heat. So well-based coverage measures skill at chosen sites, not at random cells.

**Fix.** Use weighted conformal under covariate shift (Tibshirani et al. 2019), with weights from E1's drilling-effort model as an inverse-propensity term. Pool isotonic across provinces with a hierarchical prior. Most important, make the month-6 field campaign partly design-based: add 20-40 randomly sampled cells, not only known systems and chosen controls. That gives the only unbiased check on calibration in the blind zone.

## Flaw 6 (moderate). Pooled outputs can break physics

A linear mixture of T(z) bins from different experts, done depth by depth, can produce profiles no rock can host. Y1 and Y2 stacked with different weights can also disagree: P(Y1) high while stacked T at 2 km stays cool.

**Fix.** Stack at the level of joint samples. Each draw picks one expert by weight and takes that expert's whole T(z) curve. Derive Y1 and Y6 from those curves, not from separate heads. Run the physics skeptic on the stacked output, not only on expert inputs.

## Flaw 7 (moderate). The first test has little power

The pass bar compares top-5% capture of perhaps 4-10 blind systems. A tie is the likely result. The temperature log score has power; the discovery count does not.

**Fix.** Pre-register a power analysis. Make the log score of post-2005 wells (inverse-propensity weighted) the primary endpoint. Treat discovery rank as secondary, and add planted systems in synthetic worlds as a third.

## Smaller points

E10 crowd posterior has no direct label. Validate it as revealed preference on BLM parcels that were nominated or bid versus not (thousands of rows). CSEP tests on a 2010 freeze will have tens of events, so report them, but do not gate on them. Y1 needs a depth cap for "120 C within 2 km".

## Scores

| Axis | Score | Why |
|---|---|---|
| Calibrated certainty | 3 | Right tools, but Y1 weights unidentifiable and conformal assumptions broken until fixed |
| Data realism | 3 | Freeze legality ignored for half the layers |
| Buildable in 6 months | 2 | Ten experts plus FNO, NPE and POMDP is too much; months 1-3 alone are realistic |
| Edge vs Zanskar | 4 | Censored negatives, effort and crowd model are real edges |
| Drives rights and sensors | 4 | Disagreement-to-sensor loop and leak-cost routing are strong |
| **Total** | **16/25** | |
