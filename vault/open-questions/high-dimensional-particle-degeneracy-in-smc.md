---
created_at: '2026-09-26T09:37:48Z'
source_papers:
- '[[openalex-2609.27431-bayesian-inference-on-line-forecasting-and-model-choice-for]]'
title: High-Dimensional Particle Degeneracy in SMC
---

**Background:** Bayesian vector autoregressions with stochastic volatility suffer from severe particle degeneracy and high computational burdens when scaled to high-dimensional systems.

**Question / Future Work:** High-dimensional vector autoregressions with stochastic volatility remain constrained by particle degeneracy in sequential Monte Carlo algorithms, limiting their scalability to larger cross-sections of variables.

**Why It Matters:** Overcoming particle degeneracy in high-dimensional sequential Monte Carlo is critical for enabling real-time forecasting and model choice in large-scale macroeconomic systems.

**Evidence:** The number of parameters in the VAR model grows O(K^2p) with the number of time series K, but SMC algorithms in high dimensions suffer from particle degeneracy. We therefore restrict our empirical evaluation to smaller values of K.