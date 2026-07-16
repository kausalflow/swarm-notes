---
created_at: '2026-07-16T07:13:57Z'
source_papers:
- '[[openalex-1904.05209-local-polynomial-estimation-of-time-varying-parameters-in-no]]'
title: Identification with general kernels
---

**Background:** Local polynomial estimation of time-varying parameters in nonlinear time series models, such as those relying on quasi-likelihood, currently faces challenges when the underlying objective functions are non-concave and when dealing with discrete-valued time series. A robust asymptotic theory for non-concave objective functions in this context is complex and remains a topic of active investigation.

**Question / Future Work:** A key unresolved research direction is establishing primitive, broadly applicable conditions for identifying time-varying parameters when kernel functions are allowed to take negative values (general kernels), as current proof techniques in non-concave settings often rely on positive kernel functions to ensure identification. Removing the positivity constraint is essential for enabling higher-order kernels that allow for improved bias reduction in nonparametric smoothing.

**Why It Matters:** Removing the positivity constraint on the kernel function is critical for allowing more flexible kernel choices (such as higher-order kernels) which are essential for further bias reduction in nonparametric smoothing.