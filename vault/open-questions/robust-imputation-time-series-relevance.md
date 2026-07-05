---
created_at: '2026-07-05T07:51:41Z'
source_papers:
- '[[openalex-2607.01959-autorelevance-function-and-other-feature-relevance-measures]]'
title: Robustness to Model Performance
---

**Background:** Relevance measures for time series forecasting often depend on imputation strategies for absent features that significantly impact the resulting interpretations of feature importance.

**Question / Future Work:** The development of imputation strategies that are robust to model misspecification or poor predictive performance remains a critical challenge, as reliance on model-based imputation can introduce bias when the base forecasting model is underperforming. Future research is needed to determine how to de-couple the quality of the relevance estimation from the predictive accuracy of the underlying model.

**Why It Matters:** Establishing a reliable interpretability framework that does not rely on the high performance of the base model is essential for the valid application of XAI methods in real-world scenarios where models may not be fully optimized.

**Evidence:** At the same time, this strategy relies on the forecasting model having sufficiently good predictive performance. If the fitted model produces poor forecasts, the imputed values may introduce noise and lead to misleading relevance estimates.