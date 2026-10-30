---
created_at: '2026-10-30T11:05:28Z'
source_papers:
- '[[openalex-2610.36536-atempo-amortized-transfer-entropy-model-per-lag-over-time]]'
title: Joint Variable and Lag Selection
---

**Background:** Amortized transfer entropy models identify time-varying delays and conditioning depths in multivariate time series, but their performance and scalability in high-dimensional settings remain constrained by data requirements and model capacity.

**Question / Future Work:** Extending the amortization framework from pairwise transfer entropy to condition jointly on multiple sources, enabling simultaneous joint variable-and-lag selection for high-dimensional time series forecasting.

**Why It Matters:** Extending amortized score-based transfer entropy estimators from pairwise interactions to joint multivariate conditioning represents a crucial step toward scalable, end-to-end causal discovery and variable selection in high-dimensional dynamical systems.

**Evidence:** The central idea of ATEMPO, turning quantities normally fixed during estimation into conditioning variables of a shared model, could be extended beyond pairwise transfer entropy to condition jointly on multiple sources.