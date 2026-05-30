---
created_at: '2026-05-30T07:35:28Z'
source_papers:
- '[[openalex-2605.28520-gs-fuse-granger-supervised-gated-fusion-and-multi-granularit]]'
title: Structural Causal Financial Modeling
---

**Background:** Event-driven financial forecasting frequently relies on a mix of text and historical price time series, yet models often lack causal mechanisms to account for the heterogeneous and non-stationary influence of text on market dynamics. Current approaches typically assume a stable, event-invariant balance between modalities, which fails to isolate the true structural impact of exogenous information.

**Question / Future Work:** There is a need for structural causal modeling in financial forecasting that moves beyond Granger-style predictive utility signals. Future research should address the integration of explicit regime detection, comprehensive confounder control, and modeling of non-stationary market dynamics that transcend the exogenous shock assumption.

**Why It Matters:** Bridging the gap between statistical predictive utility and structural causal discovery is a fundamental bottleneck for deploying event-driven models in complex, non-stationary financial environments.

**Evidence:** Finally, our Granger-style supervision should be viewed as a principled predictive utility signal rather than a full structural causal claim.