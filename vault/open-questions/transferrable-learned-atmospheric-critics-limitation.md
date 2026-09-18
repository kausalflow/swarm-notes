---
created_at: '2026-09-18T09:17:29Z'
source_papers:
- '[[openalex-2609.18381-every-fixed-metric-has-a-blind-spot-a-learned-atmospheric-cr]]'
title: Transferrable Learned Atmospheric Critics
---

**Background:** Machine learning weather prediction models evaluate forecast realism using fixed distributional metrics that often exhibit blind spots to specific spatial artifacts or structural flaws.

**Question / Future Work:** Investigate whether learned discriminative critics can transfer across different weather models and spatial resolutions without requiring retraining for every specific architecture.

**Why It Matters:** Crucial for establishing a universal, computationally efficient realism evaluation standard in weather forecasting.

**Evidence:** Future work could develop critics that transfer across forecast models, for which preliminary experiments are encouraging, and extend the comparison from marginal distributions to distributions conditioned on the initial state.