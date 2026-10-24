# D09 KEYSTONE: red team, scientific validity lens

Date: 24 Oct 2026. Reviewer lens: identifiability, calibration, leakage, physics consistency, and whether the certainty claims can be checked honestly. No new web searches were run. Paper citations are from memory and marked (unverified) where details matter.

## Verdict in one line

KEYSTONE is the most scientifically honest design shape so far. It has a causal story, negatives as observations, and a pre-registered ledger. But three of its validity claims are overstated as written: the "exact" explanation, the SBC "calibration", and the 2005 hindcast. All three are fixable. None is fatal. Score 16/25. Not refuted.

## Flaw 1 (serious): the 2005 hindcast leaks through the templates, not the facts

The KG freezes facts by known-time. It does not freeze knowledge. The template library, rule weights and priors are written today. The DTZ 4.8x and pull-apart 2.2x enrichments come from the 2015-17 Nevada PFA and the INGENIOUS FSS inventory (Faulds et al. 2026, per L01). The B3 "basin-buried capped" archetype exists as a named class largely because of Big Blind (2023). The "outflow first, upflow later" logic comes from Don A. Campbell and Granite Springs write-ups (L31). So a 2005-frozen KEYSTONE "finds" Big Blind with a template invented to explain Big Blind. That is target leakage at the model-structure level. kNNDM CV cannot catch it, because it lives in the priors, not the features. The LLM agents add a second leak: any rule-proposer or case-file agent has read about Big Blind in pretraining.

**Fix (AI-leveraged).** Make templates and rules bitemporal objects in the KG, like facts. Each prior and rule gets a known-time and a source citation. Agents re-derive every prior from a literature corpus sliced at the freeze date (OSTI, GRC and SGW papers dated before 2005). For 2005, this means FSS enrichments from Faulds and Coolbaugh pre-2005 work only, and no B3 template unless pre-2005 literature describes it. Run the hindcast twice: "time-sliced templates" and "today's templates". The gap between them measures structural leakage and is itself a result. Keep LLMs to extraction in hindcasts. Rule proposal in a hindcast uses only the sliced corpus, and a skeptic agent checks each rule's citations for dates. Accept that only pre-registration is fully clean (see Flaw 5).

## Flaw 2 (serious): SBC on self-generated worlds proves the code, not the calibration

Section 7 lists "simulation-based calibration on synthetic western worlds sampled from the templates" first, "in order of honesty". SBC (Talts et al. 2018, unverified details) checks that the inference engine recovers the program's own posterior. It says nothing about whether the program matches the Earth. Pass bar item 4 ("archetype and psi calibrated on synthetic Nevadas") is therefore a software test. It cannot carry any certainty claim to buyers. Amortised SBI is also known to be overconfident (Hermans et al. 2022, "A trust crisis in simulation-based inference?", unverified details), so SBC is needed, but it is not enough.

**Fix.** Rename it "inference check". Add out-of-family synthetic worlds: TOUGH3 and Waiwera runs with geometries no template generates, built by adversarial agents told to break the templates. Measure how fast the "unknown play" absorbs mass and how badly psi is miscalibrated. Real calibration claims must rest only on held-out real T(z) logs and prospective outcomes.

## Flaw 3 (serious): too many knobs for ~200-400 positives

The existence intensity has: four latent fields per archetype, an 11-class archetype mixture, a mask state, a regional GP, a gated neural residual, per-archetype label frequency (PULSNAR), a shared effort field, Diggle preferential sampling, and per-channel discovery efficiency. Several are not separately identifiable from presence-only data. Effort thinning and the GP both explain spatial clustering of finds. Per-archetype label frequency trades off one-for-one against per-archetype intensity unless something fixes it (PU learning needs SCAR or a known c). The residual's "25% of log-odds" flag depends on the prior scale you choose, so it is a tuning knob, not a diagnostic. Without fixes, B3 and B6 posteriors will mostly echo their priors, while the case file presents them as findings.

**Fix.** (a) Report posterior contraction (prior SD over posterior SD) for every global parameter, and print "prior-dominated" in case files when it is below about 1.5. (b) Pin label frequency with external anchors: the USGS 2008 and 2025 assessments' undiscovered estimates, and the dated discovery curve (Arps-Roberts). (c) Use the Month-5 field campaign as a designed, effort-free sample: add 30-50 randomly chosen FSS cells (stratified, not targeted) with 2 m probes. Random cells break the effort-intensity confound directly. This is cheap, and it is the single best identifiability buy in the design.

## Flaw 4 (moderate): the "exact" per-fact explanation is not exact

Facts are only conditionally independent given shared latents (archetype, mask, GP, play-level parameters). After you marginalise those, the per-fact log Bayes factors depend on the order of conditioning. Leave-one-out counterfactuals do not sum to the total. With NPE proposals and SMC, each number also carries Monte Carlo error. So "the explanation is the model" is true only at fixed latents.

**Fix.** Use a chain-rule decomposition with a stated canonical order (oldest fact first, which also matches discovery narratives), or Shapley values over fact groups computed by re-running amortised inference. Print the Monte Carlo error. Both are cheap on the amortised network.

## Flaw 5 (moderate): validation tests have little power and some circularity

- Eleven ladder cases give a Molchan curve and a bootstrap log-score interval that will be very wide. Item 1 can pass or fail on one case.
- "Explanation validity" (top facts match the published narrative) is circular. Templates and rules are built from those same narratives. Matching them rewards conformity, not truth.
- The 70% archetype match on 50 systems needs a baseline: 11 classes, imbalanced, and expert labels that disagree. Without an inter-expert kappa, 70% means nothing.
- Conformal selection with a stated FDR (Jin and Candes 2023, unverified) assumes exchangeability. Spatial shift and effort-biased labels break it.
- Bayesian model averaging over templates is overconfident when the true play is outside the set (M-open).

**Fixes.** Grow the test set with the agent-built dated discovery database (L31 gap 1, L36 gap 1: about 400 KGS with first-signal dates), giving hundreds of time-split events instead of 11. Pre-register many fast-resolving proxies, not just Granite Springs 68-02: predict 2 m temperatures and TG-hole gradients at every point the team or others measure, with intervals hashed in advance. These resolve in weeks and give real coverage statistics within six months. Use weighted conformal (Tibshirani et al. 2019, unverified) with effort-based weights. Use stacking (Yao, Vehtari, Simpson and Gelman 2018) instead of BMA for template weights. Get two or three expert archetype labels per system and report kappa.

## Flaw 6 (minor): physics consistency gaps

"Weakest link" implies a conjunctive model (no heat means no system). Log-additive Gaussian fields never reach zero, so a cell with zero pathway can still score high on heat. Use a soft-min or a product of probabilities on a bounded scale. The FNO is trained on Basin-and-Range runs, but templates call it for arc and rift plays. Gate it by a domain flag and fall back to the 1D column outside its training range. The boiling-point cap and monotone limits are good.

## Scores (out of 5)

| Axis | Score | Why |
|---|---|---|
| Calibrated certainty | 3 | Right instruments, but SBC is mislabeled and the hindcast leaks via templates |
| Data realism | 3 | KG-of-everything is real work; archetype labels are thin |
| Buildable in 6 months | 2 | 11 templates, FNO, amortised SBI, KG, POMDP: too much; four templates plus the column is realistic |
| Edge vs Zanskar | 4 | Play-conditioned negatives and auditable case files are real gaps |
| Drives rights and sensors | 4 | Hurdle-specific EVSI is the best sensor logic yet |
| **Total** | **16/25** | |
