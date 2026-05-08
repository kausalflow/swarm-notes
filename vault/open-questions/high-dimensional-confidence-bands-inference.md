---
created_at: '2026-05-08T06:27:14Z'
source_papers:
- '[[openalex-2605.03997-uncertainty-quantification-in-forecast-comparisons]]'
title: High-dimensional simultaneous confidence bands
---

**Background:** The number of locations in modern meteorological applications, such as large-scale spatial grid forecasting, often exceeds the number of observations available for statistical evaluation. Standard asymptotic theory for confidence bands typically assumes the dimension of the evaluation vector remains fixed while the sample size approaches infinity.

**Question / Future Work:** There is a need to develop asymptotic theory for simultaneous confidence bands where the dimension of the evaluation vector grows with the sample size. Establishing these properties would provide theoretical validity for large-scale spatial grid evaluations where the number of grid points is large relative to the length of the time series.

**Why It Matters:** High-dimensional forecast evaluation, such as in spatial weather modeling, requires theoretical justification for inference when the number of evaluation points is large, as current frameworks rely on fixed-dimension asymptotics.

**Evidence:** Extending the asymptotic theory to allow J -> infinity with N -> infinity would be of interest for applications involving large spatial grids, such as the weather forecasting case study, where the number of locations exceeds the sample size.