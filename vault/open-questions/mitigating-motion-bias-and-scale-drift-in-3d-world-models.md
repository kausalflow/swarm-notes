---
created_at: '2026-06-19T09:25:39Z'
source_papers:
- '[[openalex-2606.18250-future-dynamic-3d-reconstruction-a-3d-world-model-with-disen]]'
title: Mitigating Motion Bias and Scale Drift
---

**Background:** Dynamic 3D world models often exhibit performance degradation and geometric inconsistencies when forecasting over long time horizons due to compounded estimation errors.

**Question / Future Work:** Investigation is needed into how geometric constraints and uncertainty quantification can be integrated to mitigate scale drift and motion bias in long-horizon rollouts of latent-space world models.

**Why It Matters:** Scale drift and motion bias are fundamental barriers to the reliability and physical consistency of autonomous world models.

**Evidence:** we observe scale drift in FR3D’s predictions, which worsens with each rollout. We believe that additional geometric constraints could improve the predictions.