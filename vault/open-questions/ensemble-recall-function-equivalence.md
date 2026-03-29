---
created_at: '2026-03-29T06:07:56Z'
source_papers:
- '[[openalex-2603.25469-not-a-fragment-but-the-whole-map-based-evaluation-of-data-dr]]'
title: Ensemble recall function equivalence
---

**Background:** The true Fire Danger Index (FDI) is a latent variable that machine learning models attempt to estimate as a noisy prediction. Model ensembles are used to create a more robust estimate by averaging predictions.

**Question / Future Work:** It is an open question whether the mathematical relationship between the nonlinear function used to calculate recall (the percentage of fires correctly identified) and the ensemble-averaged FDI map is trivial, specifically whether the average recall across ensemble members is mathematically equivalent to the recall calculated from the ensemble-averaged FDI map.

**Why It Matters:** Understanding this relationship is key to rigorously validating the performance gains of ensemble averaging over individual model predictions when evaluation relies on a non-linear metric like recall.

**Evidence:** The recall is a nonlinear function of the ground truth and the FDI; therefore, Equation 1 is not trivial. This implies that most members are equally confident in labeling fire and no-fire events.