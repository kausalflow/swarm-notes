---
created_at: '2026-06-28T08:15:32Z'
source_papers:
- '[[openalex-2606.27282-how-good-can-linear-models-be-for-time-series-forecasting]]'
title: Unified Benchmarking Frameworks
---

**Background:** Advanced deep learning architectures for time-series forecasting are typically evaluated using fixed, dataset-specific preprocessing, making it difficult to isolate the contribution of architectural capacity versus data representation.

**Question / Future Work:** Determining if the performance gap between simple and complex forecasting models is an artifact of varying preprocessing sensitivity remains an open issue; a systematic benchmarking framework where models are evaluated under joint hyperparameter tuning is required.

**Why It Matters:** This is critical for fairly assessing model-driven performance gains versus gains achieved through more rigorous data engineering or preprocessing.

**Evidence:** Applying the same preprocessing search to deeper models, and comparing all model classes under jointly tuned preprocessing, remains future work.