---
created_at: '2026-04-13T07:07:59Z'
source_papers:
- '[[openalex-2503.23960-testing-for-integer-integration-in-functional-time-series]]'
title: Robust fractional integration testing
---

**Background:** The testing of whether functional time series are integrated of order zero or fractionally integrated of order d involves asymptotic properties that depend on the unknown memory parameter d and potential other nuisance parameters. It is currently unclear how to construct a feasible test that maintains discriminating power against fractional alternatives without requiring restrictive assumptions on the underlying memory parameters.

**Question / Future Work:** There is a need to develop a testing procedure for fractional integration in functional time series that remains robust even when the memory parameter is unknown and close to zero or one. The current feasibility of such tests relies on high-level assumptions about the dominant subspace and memory parameters, and there is no consensus on an estimator for the dominant subspace that is entirely independent of the memory properties. Further research is required to relax these conditions, potentially using self-normalization or power enhancement techniques adapted from univariate time series literature to mitigate the bandwidth-power trade-off.

**Why It Matters:** The sensitivity of testing procedures to the underlying memory parameters is a fundamental bottleneck in functional data analysis, limiting the applicability of these tests in real-world scenarios where the memory order is the primary unknown.

**Evidence:** However, it should be noted that the asymptotic properties of the estimator of \bar{h} will inevitably and crucially depend on the value of d1 and possibly on the other memory parameters... As a consequence, it is also not straightforward at all to replace cD with its feasible counterpart while preserving discriminating power against FI alternatives for any nonzero values of d1.