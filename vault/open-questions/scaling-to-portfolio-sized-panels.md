---
created_at: '2026-08-07T06:04:02Z'
source_papers:
- '[[openalex-2608.03715-amortized-interventional-forecasting-for-multivariate-cir-pr]]'
title: Scaling to Portfolio-Sized Panels
---

**Background:** Multivariate financial and economic time series such as credit default swap spreads, short rates, and default intensities are frequently modeled using coupled stochastic differential equations, yet scaling such models to portfolio-sized panels remains computationally challenging.

**Question / Future Work:** Future work needs to investigate how amortized interventional forecasting architectures can scale effectively to portfolio-sized panels, where self-attention mechanisms over a large number of variables become computationally prohibitive.

**Why It Matters:** Crucial for applying amortized causal forecasting methods to large-scale real-world financial portfolios and enterprise risk management systems.

**Evidence:** The experiments cover systems of three names; scaling to portfolio-sized panels, where self-attention over variables becomes expensive, is a separate question.