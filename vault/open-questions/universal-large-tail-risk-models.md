---
created_at: '2026-06-06T07:40:21Z'
source_papers:
- '[[openalex-2606.04576-resga-a-large-tail-risk-model-for-learning-value-at-risk-and]]'
title: Universal Large-Scale Tail-Risk Models
---

**Background:** In financial risk management, tail risk measures such as Value-at-Risk (VaR) and Expected Shortfall (ES) have traditionally been estimated using asset-specific parametric or semi-parametric models with limited parameter counts. The efficacy of utilizing high-capacity, universal models trained on massive, diverse datasets to serve as a general engine for joint VaR-ES forecasting remains a primary area of investigation.

**Question / Future Work:** The authors explicitly question whether a single high-capacity universal model, analogous to large language models, can effectively replace asset-specific models for joint VaR-ES forecasting by leveraging rich cross-sectional dependence and long-term temporal dynamics across diverse assets. This represents an unresolved shift in paradigm from localized, low-capacity financial models to centralized, large-scale learning engines.

**Why It Matters:** Understanding the feasibility and performance of universal, large-scale models in financial tail risk forecasting is critical, as it challenges the standard econometric reliance on asset-specific modeling and potentially provides a more robust, scalable approach to managing systemic risk across thousands of assets.

**Evidence:** Can we develop a large tail risk model... that learns from rich and diverse data to predict VaR and ES more accurately? In other words, instead of relying on asset-specific (semi-)parametric models, could a single high-capacity universal model trained on massive data serve as a general engine for joint VaR-ES forecasting?