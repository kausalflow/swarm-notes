---
created_at: '2026-07-19T07:24:27Z'
source_papers:
- '[[openalex-2607.15157-frequency-selection-in-bayesian-spectral-modeling-of-time-se]]'
title: Scalable Multivariate Spectral Modeling
---

**Background:** Multivariate Bayesian spectral models often employ hierarchical priors to link frequency inclusion patterns across multiple time series. As the number of time series increases, the number of possible joint inclusion patterns grows exponentially, creating computational and storage bottlenecks.

**Question / Future Work:** The scalability of hierarchical frequency inclusion models must be improved for higher-dimensional multivariate data, potentially through more parsimonious joint priors or structured dependency models that maintain efficiency without sacrificing the ability to capture cross-series spectral relationships.

**Why It Matters:** Improving the scalability of multivariate spectral models is essential for applying these techniques to modern, high-dimensional sensor datasets in clinical research.

**Evidence:** As a result, the number of possible joint patterns grows exponentially with the dimension D... increasing both the number of parameters in the prior specification and the computational cost.