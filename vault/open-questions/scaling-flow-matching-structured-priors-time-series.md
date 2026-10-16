---
created_at: '2026-10-16T09:23:15Z'
source_papers:
- '[[openalex-2610.17715-misspath-fm-flow-matching-with-structured-priors-for-partial]]'
title: Scaling Flow Matching with Structured Priors
---

**Background:** Flow matching models for incomplete time series face performance bottlenecks at scale and under extremely sparse data conditions or high observation noise.

**Question / Future Work:** Scaling flow-matching models with structured priors to handle very high-dimensional variables and longer sequence lengths remains challenging, as exact Gaussian process posteriors scale cubically with dimension and sequence length, and performance degrades under extremely sparse data or high observation noise.

**Why It Matters:** This is technically important because exact inference for structured time-series priors scales poorly with high dimensionality and sequence length, limiting applicability to large-scale multivariate clinical or financial time series.

**Evidence:** Our largest tested setting is D = 36 and T = 192; behaviour at larger scale is not established. The advantage shrinks when observations are very sparse or unreliable... The GP prior is per-variable and ignores cross-variable dependencies; a multi-output GP could exploit them, but its cost grows cubically in D, already the bottleneck at D = 36.