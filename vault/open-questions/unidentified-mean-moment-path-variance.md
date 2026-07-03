---
created_at: '2026-07-03T07:54:41Z'
source_papers:
- '[[openalex-2606.31685-design-based-inference-for-time-series-gmm]]'
title: Unidentified Mean-Moment Path Variance
---

**Background:** The gap between design-based and conventional long-run variance limits in time-series GMM is driven by the long-run variance of the centered mean-moment path. This mean-moment drift arises when dynamic causal effects or shock variances vary predictably over a fixed historical episode.

**Question / Future Work:** The long-run variance of the centered mean-moment path (Ωμ) is generally unidentified from a single realized history, and it is unknown how to provide a general, feasible estimator for this term that does not rely on restrictive assumptions about the form of the heterogeneity. Determining the extent to which Ωμ can be bounded using exogenous time-varying state information remains a critical open problem in time-series GMM inference.

**Why It Matters:** This component represents the fundamental difference between design-based and conventional time-series standard errors; without identification, the degree of conservativeness in GMM inference remains fundamentally opaque.

**Evidence:** This is the dependent-data analogue of the finite-population heterogeneity correction and characterizes when ΩR+ and ΩR are not equal.