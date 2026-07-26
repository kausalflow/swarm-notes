---
created_at: '2026-07-26T07:29:42Z'
source_papers:
- '[[openalex-2607.21431-modeling-dependence-structures-in-astronomical-multi-band-ti]]'
title: Uncertainty Quantification in Multi-Output GPs
---

**Background:** Multi-output Gaussian process (GP) models applied to time-domain astronomical surveys often rely on point estimation via maximum likelihood, leaving the propagation of parameter and model uncertainties to derived quantities such as power spectral densities, coherence functions, and transfer functions unaddressed.

**Question / Future Work:** Develop comprehensive uncertainty quantification frameworks—such as multivariate delta methods, parametric bootstrapping, or efficient Bayesian inference coupled with scalable GP approximations—to properly propagate the uncertainty of model parameters to derived frequency-domain quantities, covariance structures, and transfer functions in multi-output Gaussian process models.

**Why It Matters:** Rigorous uncertainty quantification is critical for scientific interpretation and model comparison in modern astronomical surveys, ensuring that derived physical constraints (such as reverberation lags and spectral properties) are statistically robust.

**Evidence:** Although Hessian-based standard errors are reported for the estimated model parameters, the uncertainty associated with derived quantities, including covariance functions, power spectral densities, coherence functions, and transfer functions, has not been propagated throughout the analysis. ... Developing efficient Bayesian inference for multi-output GP models, particularly in conjunction with the computational strategies discussed in Section V.2, represents an important direction for future work.