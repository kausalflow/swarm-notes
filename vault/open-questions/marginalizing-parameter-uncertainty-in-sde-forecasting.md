---
created_at: '2026-06-13T08:16:18Z'
source_papers:
- '[[openalex-2606.12097-weibull-stationary-stochastic-differential-equations-for-con]]'
title: Full Parameter Marginalization in SDEs
---

**Background:** Stochastic differential equations (SDEs) are often used to model wind speed trajectories by constraining the process to a stationary distribution such as the Weibull law. Currently, these models typically rely on plug-in parameter estimates, which fails to account for parameter uncertainty and its propagation through the forecasting chain.

**Question / Future Work:** Future research should develop a fully marginalized forecasting framework that integrates the predictive distribution of parametric model priors into the SDE simulation pipeline. This would improve the characterization of probabilistic uncertainty in long-horizon forecasting tasks.

**Why It Matters:** Propagating parameter uncertainty is critical for reliable decision-making in power system operations like reserve scheduling and energy storage sizing.

**Evidence:** Full marginalisation over the Kalman predictive law of the Weibull parameters is left as a natural extension.