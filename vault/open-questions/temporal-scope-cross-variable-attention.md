---
created_at: '2026-06-28T08:15:52Z'
source_papers:
- '[[openalex-2606.26549-pmdformer-patch-mean-decoupling-information-transformer-for]]'
title: Optimal Temporal Scope for Cross-Variable Attention
---

**Background:** Long-term time series forecasting often relies on multivariate data where cross-variable relationships are dynamic and non-stationary. While current approaches often attempt to model dependencies across all historical time steps, this can introduce noise and lead to overfitting on outdated correlations.

**Question / Future Work:** The optimal strategy for selecting the temporal scope of cross-variable attention in multivariate forecasting remains an open question. While focusing on the most recent (proximal) patches helps mitigate noise from historical drift, there is a need to determine whether and how to adaptively incorporate varying historical time segments into variable-wise attention mechanisms based on the degree of non-stationarity in different domains.

**Why It Matters:** Understanding the temporal extent of inter-variable dependencies is critical for balancing model capacity and robustness against non-stationary noise. This problem is fundamental to improving both the accuracy and efficiency of Transformer-based models in high-dimensional multivariate settings.