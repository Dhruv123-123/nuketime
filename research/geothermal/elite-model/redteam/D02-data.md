# D02 TRIBUNAL: red team, data-reality lens

Date: 24 Oct 2026. Reviewer: data-reality red team. Web budget for the run was used up before my searches went out, so the numbers below come from the repo evidence files (M05, M06, M08, M18, M19, M20, M29). Anything I did not check is marked (unverified).

## Verdict in one paragraph

TRIBUNAL is not refuted. Its best idea, a judge with no LLM in it that scores cards by physics likelihood, is the right answer to a world with only ~100-200 confirmed western systems. A simulator does not need labels to say what a B3 capped system looks like. But the design acts as if each prospect has a rich file. Most do not. On most of the 1,430+ FSS polygons, the judge's evidence term will be almost flat, so the card weights will just repeat the prior. The council will cost tokens and add nothing there. Second, calibration "per archetype" and the 40-prospect hindcast are both far too small to mean much. Third, geo-blinding cannot remove LLM memory of the 11 famous cases. All three have AI-leveraged fixes. Score: 15/25.

## Where the data is thin

**F1. Most prospects have no data that can tell cards apart (serious).** Only 379 clean Great Basin heat-flow wells pass USGS tests, about 38 km apart, against a thermal halo a few km wide (M05, Burns et al. 2024). Zanskar's own SGW 2025 paper says under 10% of the West has any subsurface temperature, and in 90% of sampled 1 km cells the only wells are shallower than 20 m (M06). Public MT at prospect scale exists for only a few dozen areas. More than 98% of structural settings have nothing finer than the 70 km USMTArray grid (M08). So for a typical polygon, the judge sees the prior plus a few shallow censored wells. Shallow censored columns can reject a B1 outflow card. They say almost nothing about B2 range-hosted or B3 basin-buried cards, which are the targets that matter (M18: Big Blind had no shallow hit). Result: card weights near prior, posterior near SENTINEL-COX.
*Fix:* make "data sufficiency" a gate. Compute the expected KL between card posteriors and the prior before convening a council. Below a threshold, skip the debate and let one cheap agent write only sensor challenges. That turns the sparse-data problem into the design's real product: a priced sensor plan. Spend tokens only where there is evidence to weigh.

**F2. The learned resistivity-to-temperature likelihood has very few training pairs (serious).** M08 calls "labels pairing resistivity with measured temperature the scarcest input in this whole problem". Public pairs exist at Gabbs Valley (59 stations), East Hawthorne (61), a few BRIDGE and PFA sites. Pre-training on Iceland, NZ and Anatolia brings in smectite-illite caps in different rocks.
*Fix:* train it on simulation (TOUGH3 plus a petrophysical clay model) with a learned bias term. Hold out every public US pair to fit only that term. Report the term's spread as a misspecification width. Every E-node carpet tied to a TG hole then adds a private pair.

**F3. Per-archetype calibration on tiny n (serious).** Split 100-200 systems over B1-B7 plus a failure ladder, and most archetypes get 5-30 cases. Isotonic regression and Venn-Abers on 15 points are noise. The pilot gate "7 of 11 in the top 10 of 40" has a binomial 95% interval of about 0.35-0.88 (calc), so it cannot separate a good council from a lucky one.
*Fix:* calibrate on thousands of temperature observations, not on system existence. Every censored column (NDOM, CalGEM 2,008 TG holes, 442 NBMG scanned TG boreholes, 786 OFR 99-425 holes; M19, M20) is a scored prediction of T(z). Use hierarchical calibration that pools archetypes with partial pooling, plus GHOST synthetic worlds for the existence layer. Report existence calibration only at province level.

**F4. Positive labels are biased toward shallow outflow (moderate, partly handled).** M18: nearly every historic system hit 100 C shallower than about 300 m. About 60% of known Great Basin systems were found by surface discharge (M19). An archetype library of 300-600 cards drawn from GRC/SGW figures will over-represent B1.
*Fix:* weight the card library by the Cox effort term, as SENTINEL-COX already does for counts. Use simulation to fill B2-B3 card priors. Keep the fixed-mass unknown card above 10% for B2/B3 tiles.

**F5. The failure-mode ladder has few labels (moderate).** Tagging dry holes "hot but tight" needs flow tests or lost-circulation notes. Many plugged TG holes have only a gradient. NDOM has 159 out-of-field wells; CalGEM has 1,586 plugged TG holes, mostly scanned files, and 676 still confidential (M19). Permeability outcomes are rarer still (M29: no public table links pre-drill data to well outcome).
*Fix:* AI-extract lost circulation, drilling breaks and isothermal profile segments as weak permeability labels with a noise model. Request NDOM completion reports in bulk (public after 5 years). Treat failure modes as partly observed latents, not hard labels.

## Where the data leaks

**F6. Geo-blinding does not blind (serious).** Rotating coordinates does not hide the facts. "Gold holes hit 88 C water at 300 m in 2004" is McGinness Hills to any frontier model. Geothermometer values, fault geometry and operator history are fingerprints. A probe that asks the model to name the site misses tacit recognition. The model can be steered by memory without being able to say the name.
*Fix:* (a) measure the agents' lift only on post-training-cutoff outcomes: the 16 DOE DE-FOA-0003472 sites, Granite Springs 68-02, new Zanskar or Ormat announcements. (b) Build "synthetic twins": real prospect files with the outcome flipped and the physics edited to match, then check whether agents follow the data or the memory. (c) Ablate: run the judge on fixed template cards with no agents. The council earns its place only by beating that baseline.

**F7. known_time is hard to know (moderate).** NDWR temperature fields jumped from 4-6% to 24-26% after 2015 (M06). That is a digitisation date, not a measurement date. Company reports entered the public record years after drilling. The card library built from post-freeze papers about the test systems also leaks.
*Fix:* known_time = earliest proven public release (OSTI posting date, NBMG scan date, report date), extracted by AI with page citations. Default to the latest date when unsure. Time-slice the card library by publication date too.

**F8. Big Blind and Pumpernickel deciding signals are private.** Zanskar's deciding data was its own drilling and survey. A "deciding-signal freeze" with only public facts may be impossible to build for these two.
*Fix:* use them only as first-signal tests, or replace them with PFA Gabbs and Granite Springs, which have public deciding data.

## Scores (out of 5)

- Calibrated certainty: 3. Physics judge plus unknown card is sound; per-archetype calibration is not, until F3.
- Data realism: 2. Assumes per-prospect evidence that exists for perhaps 5-15% of polygons (unverified).
- Buildable in 6 months: 3. The judge and extraction are buildable. Councils at 3,000 per month with an FNO and a blinded hindcast is a lot.
- Edge vs Zanskar: 4. Upflow placement and a physics judge with less label need are a real edge.
- Drives rights and sensors: 3. Strong once the F1 gate makes sensor challenges the main output in sparse ground.

**Total: 15/25. Not refuted.** The fatal-looking flaw (no data in most prospects) becomes the product: the council writes the sensor plan, and the judge only weighs evidence where evidence exists.
