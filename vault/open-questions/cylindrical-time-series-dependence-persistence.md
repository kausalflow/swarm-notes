---
created_at: '2026-07-11T07:05:46Z'
source_papers:
- '[[openalex-2607.07464-infinite-hidden-markov-models-for-cylindrical-data]]'
title: Cylindrical data modeling enhancements
---

**Background:** Infinite hidden Markov models (iHMMs) are applied to time series with mixed data types such as circular-linear (cylindrical) components. Current models often assume simplified independence between these components and limited state-duration flexibility.

**Question / Future Work:** There is a need to explore copula-based dependence structures between circular and linear components and to extend this framework to infinite hidden semi-Markov models (iHSMMs) to better account for state persistence and duration modeling in non-stationary time series.

**Why It Matters:** Improving the handling of component correlation and state duration dynamics is critical for extending HMM-based approaches to more realistic, complex environmental and biological signals.

**Evidence:** Future work may consider copula-based dependence between the linear and circular components (Lagona, 2019), as well as state persistence through infinite hidden semi-Markov models to improve posterior inference.