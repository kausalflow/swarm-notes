---
created_at: '2026-08-09T05:39:44Z'
source_papers:
- '[[openalex-2608.05742-multivariate-time-series-forecasting-needs-cross-variable-lo]]'
title: Probabilistic and Irregular Forecasting
---

**Background:** Multivariate time series forecasting models predominantly rely on the Direct Forecasting paradigm using point-wise objectives that neglect cross-variable dependencies and shared system dynamics among future predictions.

**Question / Future Work:** Extending the current deterministic forecasting framework and cross-variable loss regularization to handle probabilistic forecasting, irregular sampling, and missing-value scenarios remains an open area for future investigation.

**Why It Matters:** This is technically important as real-world time series data frequently contain missing values, irregular sampling intervals, and require uncertainty quantification rather than deterministic point estimates.

**Evidence:** In addition, this work mainly evaluates deterministic forecasting on regular benchmark datasets; extending CvLoss to probabilistic forecasting, irregular sampling, and missing-value scenarios is left for future work.