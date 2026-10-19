# v4: plausible ML lift counts (19 Oct 2026)

Dhruv: "obviously untested is real? where has uranium ML been tested before? just use your synthesis and guess whether it's plausible (like mineral prospectivity)... ease that rule and go over all hundreds again."

Rule change: the ML leg is scored on PLAUSIBILITY, the way mineral prospectivity mapping was judged before anyone drilled on it. Untested is NOT a kill.
ML plausibility (0-5) asks:
- Is there a large, messy, multi-source record where the outcome depends on many weak signals humans can't combine? (prospectivity-like)
- Is there an analogous domain where ML has worked (mineral prospectivity, credit, ads, protein structure, defect detection)?
- Are there enough historical outcomes to learn from, or a good physical prior?
- Would a smart domain expert, shown the model's ranking, plausibly say "I wouldn't have picked that, but it makes sense"?
Only a REAL negative test lowers it (e.g. powered-land queue AUC 0.721 vs 0.727 lookup; trial subgroups at chance in Chekroud 2024). "A vendor sells similar ML" lowers ownability (S5), not plausibility.

Use the v3 legs (V3_SHAPE.md) with S3 replaced by ML plausibility. Numbers stay relaxed (3x+ step-up fine, years fine). Standing rules kept: no prospecting/drilling, not Terranox, own the asset, path to a large company.
Pass = 17+/25 with no leg at 0-1. Web checks still apply to everything EXCEPT the ML leg, which is judgement.
