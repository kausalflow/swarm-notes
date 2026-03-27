---
created_at: '2026-03-27T15:43:26Z'
source_papers:
- '[[openalex-2603.22719-a-frequency-domain-approach-for-integrating-multiple-functio]]'
title: Extend Framework with Exogenous Covariates
---

**Background:** Analyzing Multivariate Functional Time Series (MFTS) requires a unified framework that can effectively capture dependencies across multiple levels: within-curve structures, temporal correlations, and cross-subject interactions. Current methods often specialize in one or two of these dependencies.

**Question / Future Work:** The proposed Spectral MPCA framework successfully integrates within-curve, temporal, and cross-individual dependencies using a frequency-domain marginalization approach. Future work should generalize this framework to incorporate additional predictors, such as exogenous covariates or subject-specific spatial features, to further enhance predictive accuracy in practical forecasting scenarios.

**Why It Matters:** Incorporating exogenous information is a standard and highly valuable extension for improving the predictive power of time series models in real-world applications.

**Evidence:** In this article, forecasting with Spectral MPCA is performed using only historical trajectories. In many scenarios, it would be valuable to extend our method to incorporate additional information, such as exogenous covariates or subject-specific spatial features, to further improve predictive accuracy.