---
created_at: '2026-07-11T07:05:03Z'
source_papers:
- '[[openalex-2607.07500-timee-end-to-end-time-series-classification-via-in-context-l]]'
title: Multivariate Synthetic Prior Design
---

**Background:** Time series classification models often struggle with high-dimensional cross-variate dependencies, particularly when meta-trained on synthetic priors that primarily assume simple temporal structures.

**Question / Future Work:** Developing synthetic priors and generation mechanisms that effectively capture and exploit complex inter-variate dependency structures remains a critical bottleneck for scaling foundation models to multivariate time series.

**Why It Matters:** This is a fundamental barrier to scaling TSC foundation models beyond simple univariate or small-scale multivariate datasets.

**Evidence:** Extending TimEE to multivariate inputs via variate pooling yields only marginal gains... Designing priors that better leverage inter-variate structure remains an open problem.