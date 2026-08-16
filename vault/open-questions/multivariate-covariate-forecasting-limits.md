---
created_at: '2026-08-16T05:17:32Z'
source_papers:
- '[[openalex-2608.13262-into-the-orbit-for-time-series-training-regimes-for-foundati]]'
title: Multivariate and Covariate-Rich Forecasting Limits
---

**Background:** Time series foundation models (TSFMs) are typically evaluated using existing zero-shot benchmarks like GIFT-Eval and fev-bench, but performance gaps persist in complex multivariate and covariate-rich domains.

**Question / Future Work:** Develop more comprehensive, domain-specific evaluation benchmarks and architectural extensions that can effectively handle future-known covariates and complex multivariate dependencies across diverse time series domains.

**Why It Matters:** Crucial for bridging the performance gap between univariate and multivariate/covariate-aware forecasting tasks in time series foundation models.

**Evidence:** These findings suggest that the residual performance gap on fev-bench stems primarily from covariate conditioning limitations rather than sensitivity to the forecast window... These findings pinpoint covariate-rich domains and specialized Retail regimes as key frontiers for future refinement of Falcon-2.0’s probabilistic consistency.