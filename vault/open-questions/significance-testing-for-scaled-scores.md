---
created_at: '2026-06-26T08:25:06Z'
source_papers:
- '[[openalex-2606.24715-model-selection-with-proper-scoring-rules-on-data-sets-of-ti]]'
title: Significance testing for scaled scores
---

**Background:** Probabilistic forecasting performance is often evaluated using proper scoring rules on datasets containing multiple time series, which necessitates aggregating scores across individual series. Standard aggregation methods like mean ranks or median scores can lead to conflicting model selection results compared to the mean scaled score, especially when test sets are limited in size.

**Question / Future Work:** It remains an unresolved challenge to determine how to perform statistically robust significance testing when comparing competing forecasting models on large datasets using mean scaled scores. Standard tests like the Diebold-Mariano test are prone to rejecting the null hypothesis even when the observed differences in mean scaled scores are negligible, necessitating the development of more appropriate alternatives such as Bayesian tests with a region of practical equivalence.

**Why It Matters:** Reliable model selection in large-scale forecasting requires not only accurate point estimates of performance but also a rigorous way to determine if observed performance differences are statistically and practically significant. Without this, practitioners risk over-interpreting minor score improvements as evidence of model superiority.