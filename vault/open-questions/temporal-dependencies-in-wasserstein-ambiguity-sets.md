---
created_at: '2026-05-17T07:31:05Z'
source_papers:
- '[[openalex-2605.14642-distributionally-robust-model-predictive-control-for-virtual]]'
title: Capturing temporal dependencies in ambiguity sets
---

**Background:** Distributionally robust control frameworks for power systems often rely on stage-wise construction of ambiguity sets, which process forecasts of uncertain variables independently at each step.

**Question / Future Work:** Stage-wise ambiguity sets fail to explicitly capture temporal dependencies in stochastic price or generation processes, which are vital for multi-step control and storage management. Developing and integrating joint Wasserstein ambiguity sets that account for temporal correlations over the entire prediction horizon remains an open challenge.

**Why It Matters:** Addressing temporal dependencies is critical for improving the performance of VPPs, as storage-related arbitrage decisions inherently depend on the joint distribution of market signals over time.

**Evidence:** the resulting ambiguity sets B_k(ε) are constructed independently at each prediction step from marginal quantile forecasts, and temporal dependencies in the price process are therefore not explicitly captured.