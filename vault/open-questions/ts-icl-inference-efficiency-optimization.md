---
created_at: '2026-06-07T08:18:21Z'
source_papers:
- '[[openalex-2606.05878-ts-icl-a-flexible-time-indexed-foundation-model-for-time-ser]]'
title: Pointwise Forecasting Efficiency Bottlenecks
---

**Background:** Time series foundation models often face trade-offs between expressive power and computational efficiency, particularly when employing pointwise regression or complex transformer architectures.

**Question / Future Work:** Addressing the inference cost bottleneck of pointwise regression-based time series models is essential for practical, real-world deployment of flexible foundation models.

**Why It Matters:** As foundation models move toward broader deployment, reconciling flexibility with computational efficiency remains a critical engineering bottleneck.

**Evidence:** TS-ICL exhibits higher inference cost than highly optimized models such as Chronos-2... due to its pointwise regression formulation.