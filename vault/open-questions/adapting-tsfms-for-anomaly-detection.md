---
created_at: '2026-10-08T11:40:29Z'
source_papers:
- '[[openalex-2610.06453-normality-constraint-learning-adapting-foundation-models-for]]'
title: Adapting TSFMs for Anomaly Detection
---

**Background:** Time Series Foundation Models (TSFMs) are typically pre-trained on large-scale corpora to model broad temporal dynamics using reconstruction or forecasting objectives, which often causes them to model rare anomalous patterns as effectively as normal ones and undermines error-based anomaly scores.

**Question / Future Work:** Investigate how to effectively adapt frozen time series foundation models for anomaly detection without incurring catastrophic forgetting or reducing anomaly score discriminability, specifically by leveraging normality constraints and lightweight plug-and-play adaptation frameworks.

**Why It Matters:** This question is central to adapting large-scale task-general pre-trained foundation models to specialized, distribution-sensitive downstream tasks such as unsupervised anomaly detection.

**Evidence:** How can we effectively leverage the powerful representational capacity of frozen TSFMs while steering their outputs toward a normality regime so that abnormal deviations stand out more clearly?