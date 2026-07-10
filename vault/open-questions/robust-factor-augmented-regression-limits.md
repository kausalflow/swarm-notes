---
created_at: '2026-07-10T08:15:54Z'
source_papers:
- '[[openalex-2607.06368-factor-augmented-machine-learning-panel-regressions]]'
title: Robustness in Factor-Augmented Regression
---

**Background:** Factor-augmented panel regression models rely on sub-Gaussian error assumptions which are frequently violated in real-world macroeconomic and financial time series.

**Question / Future Work:** Future research is needed to adapt the factor-augmented sparse-group LASSO framework to non-sub-Gaussian regimes, particularly by investigating the integration of robust loss functions such as Huber or median-of-means estimators to improve practical reliability in heavy-tailed settings.

**Why It Matters:** This is a fundamental theoretical challenge for applying high-dimensional factor-augmented methods to volatile empirical data, where outliers and heavy tails are prevalent.

**Evidence:** Assumption 1 requires that regression errors are sub-Gaussian conditionally on the covariates. It can be relaxed in several different ways, e.g. winsorizing the data or robustifying the least-squares objective function...