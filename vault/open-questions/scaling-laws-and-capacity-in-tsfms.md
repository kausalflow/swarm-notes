---
created_at: '2026-10-25T09:29:17Z'
source_papers:
- '[[openalex-2610.30950-random-initialization-as-a-baseline-for-time-series-foundati]]'
title: Scaling Laws and Capacity in Time Series Foundation Models
---

**Background:** Time series foundation models leverage large-scale pretraining objectives such as masked reconstruction or contrastive learning to build representations for downstream classification tasks like multivariate time series classification (MTSC).

**Question / Future Work:** Investigate whether scaling laws and performance gains observed in time series foundation models consistently hold across diverse model architectures, scales, downstream classifier capacities, and broader multivariate time series classification benchmarks beyond current empirical observations.

**Why It Matters:** Determining whether pretraining benefits scale predictably with model size and architecture is critical for resource allocation and architectural design in time series representation learning.

**Evidence:** However, it remains unclear whether this pattern extends across multiple TSFM families and model scales, different downstream classifier capacities, and the broader range of general-purpose MTSC datasets considered here.