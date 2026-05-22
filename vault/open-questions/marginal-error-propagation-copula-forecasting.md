---
created_at: '2026-05-22T08:16:44Z'
source_papers:
- '[[openalex-2605.19685-probabilistic-multivariate-time-series-forecasting-with-diff]]'
title: Mitigating marginal error propagation
---

**Background:** Multivariate probabilistic time series forecasting often relies on two-stage procedures where marginal distributions are modeled independently before being linked by a copula to account for dependence. In these frameworks, errors or model misspecifications in the marginal estimation propagate to the subsequent dependence structure, complicating the accurate modeling of joint tail events.

**Question / Future Work:** Investigate methods to mitigate the propagation of marginal model errors into the dependence structure when using modular two-stage copula-based forecasting frameworks, potentially by integrating more flexible, non-parametric marginal estimators.

**Why It Matters:** This represents a fundamental trade-off between modular flexibility and error accumulation, which is critical for the reliability of risk management tools in high-dimensional multivariate systems.