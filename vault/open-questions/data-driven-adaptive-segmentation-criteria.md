---
created_at: '2026-04-11T05:56:28Z'
source_papers:
- '[[openalex-2503.13093-localized-dynamic-mode-decomposition-with-temporally-adaptiv]]'
title: Data-Driven Adaptive Segmentation Criteria
---

**Background:** Reduced-order modeling techniques like Dynamic Mode Decomposition often rely on error estimators to drive adaptive partitioning of temporal or spatial domains.

**Question / Future Work:** Developing adaptive segmentation criteria for dynamical system forecasting that function strictly in a data-driven manner, without requiring access to known governing equations, remains a significant challenge. Current approaches often depend on residual evaluation of physical operators, limiting their utility for black-box or partially observed dynamical systems.

**Why It Matters:** This is a fundamental bottleneck for deploying localized model reduction methods in real-world settings where governing physical equations are unknown or computationally prohibitive.

**Evidence:** The residual-based error estimator requires explicit access to the governing equations, limiting the fully data-driven applicability of the adaptive method.