---
created_at: '2026-10-10T10:51:45Z'
source_papers:
- '[[openalex-2610.12240-adacast-conditional-parameter-generation-for-adaptive-time-s]]'
title: Cross-Variate Conditional Parameter Generation
---

**Background:** Time-series foundation models (TSFMs) are typically univariate or adapted via shared static updates across all inputs, leaving multi-variate conditioning largely unexplored in instance-specific parameter generation frameworks.

**Question / Future Work:** Investigate and extend conditional parameter generation frameworks (such as AdaCast) to handle cross-variate conditioning, as current implementations rely strictly on univariate series processing strategies.

**Why It Matters:** Crucial for real-world multivariate time series forecasting where cross-variable dependencies and inter-variable correlations are vital for accurate predictions.

**Evidence:** Several questions remain. AdaCast is an univariate model, leaving cross-variate conditioning unexplored.