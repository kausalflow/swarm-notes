---
created_at: '2026-03-27T14:09:07Z'
source_papers:
- '[[openalex-2603.11352-timesqueeze-dynamic-patching-for-efficient-time-series-forec]]'
title: Learning End-to-End Dynamic Patching Rate
---

**Background:** Research on dynamic patching mechanisms in time series forecasting seeks to adapt representational granularity based on local signal complexity.

**Question / Future Work:** The relative threshold-based patching metric is scale-independent and robust, but it currently requires manual hyperparameter tuning ($\tau$) to achieve a desired target compression rate. Future work could investigate learning the optimal patch boundaries end-to-end directly in the embedding space, potentially using methods like those described for language models, to natively support variable compression rates without external tuning.