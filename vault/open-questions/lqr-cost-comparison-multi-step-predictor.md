---
created_at: '2026-03-27T15:43:52Z'
source_papers:
- '[[openalex-2603.23465-statistical-efficiency-of-single-and-multi-step-models-for-f]]'
title: Analyze closed-loop LQR comparison
---

**Background:** The study compares the asymptotic prediction error rates for three classes of learned models: single-step autoregressive rollouts, direct multi-step predictors, and single-step models trained with multi-step losses, under a fully observed linear dynamical system setting.

**Question / Future Work:** The theoretical comparison between the single-step predictor and the direct multi-step predictor for closed-loop control performance (infinite-horizon LQR cost) was explicitly stated as being left for future work.

**Why It Matters:** This comparison is crucial for practitioners to fully understand the trade-offs in control performance across all three model classes, especially since the prediction error ranking (Prop II.4) contradicted the LQR cost ranking observed between the intermediate and multi-step predictors (Section IV-A).

**Evidence:** Comparison with the multi-step predictor is left for future work.