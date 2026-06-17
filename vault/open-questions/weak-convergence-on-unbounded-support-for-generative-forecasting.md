---
created_at: '2026-06-17T09:25:08Z'
source_papers:
- '[[openalex-2606.16773-generative-predictive-distributions-for-time-series]]'
title: Weak Convergence on Unbounded Support
---

**Background:** The estimation of predictive distributions for time series using generative models often relies on neural network approximation, which theoretically requires compact domains for convergence. Applying these methods to time series with unbounded support and temporal dependence presents significant challenges for proving universal approximation and weak convergence.

**Question / Future Work:** Establishing formal weak convergence and approximation error rates for generative models applied to time series with unbounded state spaces remains a significant theoretical hurdle. Since traditional results for neural networks rely on compact domain assumptions, extending these findings to account for the dynamics of non-stationary or weakly dependent processes on unbounded supports is a critical open problem for the reliability of these models in fields like finance.

**Why It Matters:** This gap restricts the formal understanding of model reliability in domains where data is inherently unbounded, hindering the rigorous application of generative forecasting frameworks in real-world risk management.