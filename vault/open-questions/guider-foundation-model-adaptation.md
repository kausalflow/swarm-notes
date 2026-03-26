---
created_at: '2026-03-26T07:11:11Z'
source_papers:
- '[[2603.24262-forecasting-with-guidance-representation-level-supervision-f]]'
title: Guider Model Adaptation
---

**Background:** The effectiveness of a time series forecasting model can be limited by relying solely on error-based objectives during training, which may cause the encoder to discard salient patterns.

**Question / Future Work:** Investigating how to adapt the chosen time series foundation model (the 'guider') to better suit the scale and complexity of the target forecasting dataset, as current results suggest the optimal size of the guider depends on the dataset characteristics (e.g., small vs. large datasets).