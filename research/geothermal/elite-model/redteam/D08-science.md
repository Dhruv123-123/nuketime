# D08 UNDERCAST: red team, scientific validity

Reviewer lens: identifiability, calibration, leakage, physics consistency, and whether the certainty claims can be checked honestly. No web searches ran: the shared search budget was used up. Facts below come from D08 and the L/M evidence files. Anything I did not check is marked (unverified).

## Verdict in one line

Not refuted. The idea is sound and the pass bar is unusually honest. But as written, the posterior is not a true posterior, the hindcasts leak through the simulator, and the "certainty" mostly measures how well the model knows its own prior. All five problems have AI-leveraged fixes. Score 16/25.

## 1. Identifiability: the state is far bigger than the data

The latent state has about 3 x 10^8 voxels, each holding T, a three-part permeability tensor, flux, phase, salinity and seven rock properties. Below about 1 km, almost no cell has a direct reading. Permeability and Darcy flux are only seen through weak proxies (lost circulation, helium, seismicity). So most of the state is the prior with no data behind it. D08 admits this as risk 2. But the headline product, P(T >= 150 C AND permeable), multiplies two quantities, and one of them is nearly all prior.

**Fix.** Make "how much the data moved this" a first-class output, not a footnote. For each voxel and head, compute posterior contraction (1 minus posterior variance over prior variance) and the KL from prior to posterior. Do this per vintage. Any buy decision whose RNPV depends mostly on low-contraction voxels gets a forced wide flow-risk term. Also run a **prior-swap test**: re-assimilate with two structurally different generators (for example Noddy-style and GemPy-style Westlets). Where the posteriors disagree, the answer is prior-driven by definition.

## 2. Calibration: DPS is not an exact sampler

Diffusion posterior sampling (Chung et al. 2023) uses a point estimate of the clean state to approximate the likelihood gradient. It is known to give biased, often overconfident posteriors with nonlinear operators (my recollection of the literature, unverified here). D08 stacks many nonlinear operators: MT, mixing geothermometers, Cox seismicity. Then the hybrid physics core (H) sits after the prior. It is unclear whether H shapes the samples or corrects them afterwards. If it corrects them afterwards, the output is no longer a posterior at all, and SBC on the raw sampler says nothing about it.

**Fix.** Use asymptotically exact samplers: sequential Monte Carlo guidance (twisted diffusion sampler, Wu et al. 2023; MCGdiff, Cardoso et al. 2023) with particle weights. Put the physics constraints inside the likelihood or the prior training, never as a post-hoc projection. Run SBC on the whole pipeline end to end (prior, DPS, physics core, heads), not on the sampler alone. Agents can run the 1,000-world SBC on every release.

## 3. Synthetic SBC only proves self-consistency

SBC and TARP on Westlets show the sampler inverts its own simulator. They cannot show that the simulator looks like Nevada. The 5-backbone ensemble shares one generator family, so its spread misses the biggest error: structural prior mismatch. Ranking SBC first "in order of honesty" overstates it.

**Fix.** Treat SBC as a unit test, not evidence. The real calibration gate is coverage on real held-out readings. Add posterior-predictive checks on real data summaries (gradient histograms, reversal rates, the share of hot 2 m cells). Agents tune the generator until these pass. The test held out must stay untouched by that tuning.

## 4. Real held-out CRPS is biased by where people drilled

Wells sit where someone expected heat or water. Held-out readings are therefore clustered near known systems and shallow aquifers. This is preferential sampling (Diggle et al. 2010). Good CRPS and good coverage there do not carry over to the blank cells where Terranox wants to buy. kNNDM fixes spatial distance, not selection.

**Fix.** Weight each held-out reading by inverse probability of drilling. The Cox effort model already estimates that. Report CRPS and coverage separately for "high-effort" and "low-effort" strata. The pass bar should require coverage in the low-effort stratum, not just overall.

## 5. Leakage: the hindcasts are not point-in-time

D08 dates the data by known-time. It does not date the **model**. Four leaks:
- The Westlet generator is seeded with Faulds' FSS templates and conceptual-model figures pulled from the literature. Those were refined by play-fairway work that drilled Gabbs Valley and Granite Springs (Faulds et al. 2021, OSTI 1724080). A 2015 freeze that uses today's generator already "knows" those plays.
- Masked-modality pre-training (MultiMAE) on real data and the learned operators (BHT bias, Archie-plus-clay) are fitted once on all data, including post-freeze data.
- Extraction agents use LLMs that may remember answers.
- Pass-bar item 4 tests two sites that were picked *because* fairway maps scored them high. Hitting them in the top 5% partly reproduces the fairway map.

**Fix.** Freeze the model as well as the data. Keep a model "vintage manifest": generator templates, papers and operator training data, each with a known-time. Rebuild the generator and operators per vintage. The tier-(a) runs are cheap, so this costs little. Give the extraction agents redacted inputs: strip site names and post-freeze citations. Score Gabbs and Granite Springs against a "fairway map alone" baseline, and require UNDERCAST to beat it. Add Big Blind (about 820 m), which the fairway maps did not flag (unverified).

## 6. Physics consistency

Steady conduction-advection is right for many systems but wrong for young, sealing or fossil systems. Those are exactly the decoys the M/L files warn about: fossil caps and outflow tongues (McGinness Campbell). A steady core will force a live upflow to explain a fossil anomaly. The rule "no inversion without lateral flux" also bans transient cooling, which is real.

**Fix.** Add age and sealing as latent variables. Add a transient tier to the TOUGH3 runs (10^4 runs, agent-built). Then a "fossil" archetype can explain a hot cap with a cold core.

## 7. The Cox head can leak effort back in

D08 says effort never enters the intensity. But the world-model features fed to the intensity are sharper where data is dense. So feature quality tracks effort. **Fix:** compute intensity features from blind-only, effort-invariant inputs, or randomly mask dense cells during training until feature statistics match across effort strata. Test that by regressing features on effort.

## Scores (out of 5 each)

- Calibrated certainty: 3. Good gates, but DPS bias and model leakage undercut them.
- Data realism: 3. The token design is right. Deep and permeability data are thin.
- Buildable in 6 months: 2. A West-wide 3D diffusion reanalysis, a hybrid core and a POMDP is too much. The Nevada thermal-only first test is doable.
- Edge vs Zanskar: 4. 3D, depth-aware, sensor simulation and pre-registration are real edges.
- Drives rights and sensors: 4. EVSI from one generative model is the right design.

**Total: 16/25. Refuted: no.**
