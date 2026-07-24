---
created_at: '2026-07-24T07:25:34Z'
source_papers:
- '[[openalex-2607.19311-gartfima-models-a-class-of-observation-driven-models-with-te]]'
title: Identifiability and Estimation Challenges
---

**Background:** Tempered fractional time series models introduce a tempering parameter to fractional differencing to model semi-long memory processes, but parameter estimation and identification remain challenging in small-sample settings due to weak identifiability among model coefficients.

**Question / Future Work:** Future investigations are needed to explore alternative estimation strategies, regularization methods, or reparameterizations to mitigate the weak identifiability and finite-sample estimation challenges inherent in GARTFIMA and ARTFIMA models when parameters like the fractional differencing order, tempering parameter, and moving-average coefficients interact.

**Why It Matters:** Weak identifiability and estimation challenges in tempered fractional models affect convergence, standard error estimation, and reliable inference across non-Gaussian time series applications.

**Evidence:** In our numerical experiments, we found that the same difficulties encountered in estimating ARTFIMA(1, d, λ, 1) models also apply to GARTFIMA(1, d, λ, 1) models... empirical identification of the parameters in small samples remains challenging in this setting.