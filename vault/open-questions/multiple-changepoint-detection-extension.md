---
created_at: '2026-05-23T07:25:17Z'
source_papers:
- '[[openalex-2605.20621-changepoint-detection-in-categorical-time-series-with-applic]]'
title: Multiple Changepoint Detection Extension
---

**Background:** Changepoint detection methods for correlated categorical data often rely on the 'at most one changepoint' (AMOC) assumption to simplify the statistical framework.

**Question / Future Work:** Extending the marginalized transition model to support multiple structural shifts requires developing penalized likelihood approaches, such as modified information criteria, to handle long-term non-stationary series effectively.

**Why It Matters:** Most climate and physical observational time series exhibit multiple discontinuities, making the AMOC assumption a primary bottleneck for real-world homogenization tasks.

**Evidence:** While the assumption of at most one changepoint (AMOC) simplifies the statistical framework, it may be unrealistic for longer time series... A natural extension of the current framework is to allow for the detection of multiple changepoints.