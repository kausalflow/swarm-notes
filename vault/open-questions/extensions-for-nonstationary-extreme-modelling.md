---
created_at: '2026-05-08T06:28:28Z'
source_papers:
- '[[openalex-2605.03331-bayesian-modelling-of-nonstationary-extreme-values-using-a-n]]'
title: Extensions for Nonstationary Extreme Modelling
---

**Background:** Extreme value analysis often involves modelling the occurrence of events via point processes and the magnitudes via the Generalised Pareto Distribution (GPD). Many applications require models that handle nonstationarity in both the temporal occurrence of events and the evolution of their magnitudes.

**Question / Future Work:** Future research could extend the proposed framework by incorporating time-varying background intensity or covariates into the Hawkes process background rate, enabling the separation of long-term trends from short-term self-excitation. Additionally, integrating covariates into the hierarchical mark model or the global shape parameter, as well as developing multivariate extensions for interacting extreme processes, remain significant avenues for future work.

**Why It Matters:** These extensions address the limitations of the current model in handling exogenous non-stationarity and multivariate dependencies, which are critical for real-world risk management scenarios such as financial contagion or multi-hazard natural disasters.

**Evidence:** The background intensity \\mu(t) could be made time-varying or allowed to depend on covariates, allowing long-run changes in the rate of exceedances to be separated from short-run self-excitation. Similarly, covariates could be introduced into the mark distribution, either through the cluster-scale hierarchy or through the global shape parameter. A multivariate extension would also be valuable in applications such as financial risk or natural hazards...