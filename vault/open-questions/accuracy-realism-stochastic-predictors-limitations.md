---
created_at: '2026-06-06T07:39:52Z'
source_papers:
- '[[openalex-2606.04342-expectations-vs-realities-the-cost-of-mse-optimal-forecastin]]'
title: Stochastic Predictors Accuracy-Realism Limits
---

**Background:** Deterministic multi-step forecasting models trained under squared loss (MSE) typically aim to estimate the conditional mean of future outcomes. However, when conditional uncertainty—the irreducible variability of future outcomes given past observations—is non-zero, these MSE-optimal predictors necessarily fail to match the marginal distribution of realized futures.

**Question / Future Work:** While the paper establishes that a fundamental, model-agnostic accuracy–realism trade-off exists for deterministic predictors, a full theoretical and empirical characterization of this frontier for stochastic (probabilistic) predictors remains an open challenge. Determining how different sampling-based decision rules and stochastic model architectures map to the accuracy–realism frontier is crucial to moving beyond the constraints identified for deterministic systems.

**Why It Matters:** Understanding if stochastic predictors can overcome the fundamental limitations identified for deterministic models is central to advancing robust long-horizon forecasting architectures.

**Evidence:** While probabilistic models can be embedded into this framework through specific decision rules, a full characterization of the accuracy–realism frontier for stochastic predictors remains open.