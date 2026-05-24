---
created_at: '2026-05-24T07:45:52Z'
source_papers:
- '[[openalex-2605.21884-trend-and-seasonality-estimation-for-point-process-time-seri]]'
title: Asymptotic variance for point-process models
---

**Background:** Estimation of autocorrelation functions in point-process time series often relies on computationally intensive methods or strong parametric assumptions, particularly when dealing with latent Gaussian intensity processes. M-estimators for these models require asymptotic variance estimation that depends on unknown latent autocovariance terms.

**Question / Future Work:** The development of a robust and consistent estimator for the asymptotic variance of trend and seasonality estimators in point-process time series remains a challenge, as current methods depend on the latent autocovariance function of the underlying Cox process for which no consistent estimator exists. Future research must devise methods for consistently estimating these covariance terms or develop inference procedures that remain robust without explicit dependency on them.

**Why It Matters:** This bottleneck prevents the reliable construction of confidence intervals and hypothesis testing for trend and seasonality estimates in point-process time series models.

**Evidence:** But the quantities 𝚺jj, σjj and ejj that define V in V in (16) involve γ0(u, u′), for which we do not have a consistent estimator.