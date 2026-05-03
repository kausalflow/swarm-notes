---
created_at: '2026-05-03T07:13:45Z'
source_papers:
- '[[openalex-2604.28149-explainable-load-forecasting-with-covariate-informed-time-se]]'
title: Efficient SHAP for TSFMs
---

**Background:** Shapley Additive Explanations (SHAP) require evaluating a model across all possible subsets of input features, which becomes computationally prohibitive as the number of features increases.

**Question / Future Work:** Future research is required to optimize SHAP estimation for TSFMs, particularly through smart subset sampling or coalitional approximations, to manage the computational overhead inherent in high-dimensional temporal and covariate inputs.

**Why It Matters:** The exponential complexity of exact SHAP currently limits its application in real-time or high-resolution forecasting environments.

**Evidence:** Computational efficiency could be substantially improved by estimating SHAP values from subsets of feature group combinations rather than exhaustively evaluating all 2^N coalitions