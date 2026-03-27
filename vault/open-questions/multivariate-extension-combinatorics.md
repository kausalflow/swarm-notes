---
created_at: '2026-03-27T14:09:37Z'
source_papers:
- '[[openalex-2603.00636-retrodictive-forecasting-a-proof-of-concept-for-exploiting-t]]'
title: Multivariate Extension Challenge
---

**Background:** The scope of a proof-of-concept study often necessitates simplification of evaluation settings, which may mask issues when scaling to more complex data structures.

**Question / Future Work:** The current implementation is restricted to univariate time series with fixed window sizes (n=32, m=16). Extending the retrodictive framework to multivariate time series will introduce significant complexity, especially regarding the MAP optimization routine over the augmented future variable 𝒚.