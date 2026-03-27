---
created_at: '2026-03-27T15:43:58Z'
source_papers:
- '[[openalex-2603.22663-short-form-video-viewing-behavior-analysis-and-multi-step-vi]]'
title: Explore advanced forecasting models
---

**Background:** Chunk-based preloading in short-form video streaming aims to reduce data wastage caused by early video skips by dividing videos into smaller segments.

**Question / Future Work:** The authors explicitly mention that they plan to explore more advanced forecasting models to further improve system performance in predicting user viewing times, which is crucial for optimizing chunk-based preloading size.

**Why It Matters:** Exploring more advanced forecasting models is necessary because the study's best-performing model, Auto-ARIMA, still produces non-trivial errors (e.g., RMSE around 6.0–8.5), and better prediction accuracy directly translates to reduced data wastage in the streaming system.

**Evidence:** In future work, we plan to explore more advanced forecasting models and adaptive preloading strategies to further improve system performance.