---
created_at: '2026-11-04T12:40:02Z'
source_papers:
- '[[openalex-2611.02211-forecasting-earth-surface-change-in-embedding-space]]'
title: Modeling Cross-Dimensional Correlations
---

**Background:** Earth foundation model embeddings usually exhibit strong cross-dimensional correlations, but standard probabilistic forecasting heads often model dimensions independently using a diagonal covariance matrix.

**Question / Future Work:** Explore advanced probability estimation formulations or full covariance modeling techniques to properly capture cross-dimensional correlations in high-dimensional foundation model embedding spaces without degrading forecasting performance.

**Why It Matters:** Accounting for full dimensional covariances is crucial for accurate uncertainty estimation and realistic high-dimensional probabilistic forecasting.

**Evidence:** First, the probability-estimation branch ignores the correlation between embedding dimensions. This is because the surrogate in Eq. 4 uses a diagonal covariance, predicting the mean and standard deviation of each dimension independently, whereas the dimensions of foundation-model embeddings are usually highly correlated. We tried extending $\\mathcal{L}_{\\mathrm{nll}}$ to model this cross-dimensional correlation, but it substantially degraded performance. We believe this reflects our particular formulation rather than the idea itself, and leave a better way of modelling these correlations to future work.