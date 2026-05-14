---
created_at: '2026-05-14T07:38:04Z'
source_papers:
- '[[openalex-2605.10298-set-prediction-for-next-day-active-fire-forecasting]]'
title: Stabilizing Set Prediction Assignments
---

**Background:** Sparse set prediction models often employ bipartite matching to assign predictions to ground-truth targets during training, which can lead to unstable supervision as small changes in query outputs switch assignments.

**Question / Future Work:** Investigate methods to stabilize target-to-query assignments in set prediction models to mitigate the instability caused by sensitive bipartite matching, particularly in the context of sparse spatial event forecasting.

**Why It Matters:** This is a fundamental challenge in DETR-style set prediction architectures, directly impacting model convergence and the reliability of learned spatial representations.

**Evidence:** small changes in query scores or locations can switch which query receives localization supervision.