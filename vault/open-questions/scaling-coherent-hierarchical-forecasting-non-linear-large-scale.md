---
created_at: '2026-09-18T09:16:39Z'
source_papers:
- '[[openalex-2609.17918-coherent-hierarchical-forecasting-for-proportion-and-discret]]'
title: Scaling Coherent Forecasting to Non-Linear and Large Hierarchies
---

**Background:** Hierarchical time series reconciliation methods often rely on linear constraints and Gaussian assumptions, which fail when applied to bounded or discrete domains such as proportions and counts.

**Question / Future Work:** Extend the proposed framework of forecast convolutions and exponential tilting to handle non-linear and sequential hierarchical relationships, as well as evaluate its computational efficiency and performance on larger hierarchical series.

**Why It Matters:** Real-world hierarchical systems frequently involve complex non-linear aggregation constraints and massive scale, presenting significant scalability and methodological hurdles for current probabilistic reconciliation algorithms.

**Evidence:** For future research, we aim to extend this framework to non-linear and sequential hierarchical relationships. Additionally, while this study considers relatively small hierarchies (fewer than 100 nodes in the complete series), evaluating the efficiency and performance of our method on larger hierarchical series is a natural next step.