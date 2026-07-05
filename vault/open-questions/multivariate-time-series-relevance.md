---
created_at: '2026-07-05T07:51:41Z'
source_papers:
- '[[openalex-2607.01959-autorelevance-function-and-other-feature-relevance-measures]]'
title: Multivariate Time Series Extension
---

**Background:** Most current feature relevance methodologies for time series are designed for univariate data and rely on historical lags of a single variable.

**Question / Future Work:** Extending model-agnostic lag relevance measures to multivariate time series, where predictors include both own-lags and exogenous variables, presents significant methodological hurdles in defining appropriate coalition structures and imputation methods that respect cross-variable temporal dependencies.

**Why It Matters:** Real-world forecasting tasks rarely rely on univariate data, making the extension to multivariate settings a primary requirement for the practical adoption of these interpretability tools.