---
created_at: '2026-08-09T05:40:05Z'
source_papers:
- '[[openalex-2608.06122-is-self-pretraining-really-useful-to-improve-diagnosis-in-me]]'
title: SPT on Irregular Time Series
---

**Background:** Transformer-based models in clinical applications face challenges related to variable-length inputs and asynchronous or irregularly sampled data.

**Question / Future Work:** Investigate how Self-PreTraining (SPT) performs on time-series forecasting, imputation, and segmentation tasks, particularly when applied to variable-length inputs or irregularly sampled medical time series.

**Why It Matters:** Medical time-series data naturally exhibit irregular sampling intervals and variable sequence lengths, making the expansion of SPT beyond fixed-length classification critical for practical clinical deployment.

**Evidence:** Future work should investigate how SPT performs on forecasting, detection, and segmentation tasks, especially with variable-length inputs or irregularly sampled data — common characteristics in medical contexts.