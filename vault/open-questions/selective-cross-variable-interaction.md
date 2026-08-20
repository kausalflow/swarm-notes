---
created_at: '2026-08-20T05:20:49Z'
source_papers:
- '[[openalex-2608.16098-asyto-asymmetric-temporal-operator-for-parameter-efficient-m]]'
title: Selective Cross-Variable Interaction
---

**Background:** Multivariate time series forecasting models that process each variable independently fail to capture cross-variable predictive dependencies present in highly correlated datasets.

**Question / Future Work:** Future work needs to investigate selective cross-variable interaction mechanisms that can be integrated into parameter-efficient architectures like AsyTO to handle datasets where cross-sensor or cross-variable information is critical for accurate forecasting, while maintaining computational and parameter efficiency.

**Why It Matters:** Addressing cross-variable interaction without blowing up parameter counts is a fundamental challenge in multivariate time series forecasting.

**Evidence:** Each forecast, however, uses only the history of its target variable. This intermediate design preserves variable specificity with modest parameter growth, but cannot exploit predictive signals available exclusively from other variables. Selective cross-variable interaction is therefore a natural direction for future work.