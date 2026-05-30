---
created_at: '2026-05-30T07:35:46Z'
source_papers:
- '[[openalex-2605.28103-benchmarking-inductive-biases-for-multivariate-time-series-a]]'
title: Evaluating Foundation Models for Anomaly Detection
---

**Background:** Foundation models pretrained on large-scale, heterogeneous time-series corpora are increasingly used for zero-shot forecasting and classification. However, the efficacy of these models for multivariate time-series anomaly detection remains largely unexplored in a rigorous, comparative setting.

**Question / Future Work:** Detailed empirical evaluation of time-series foundation models for multivariate time-series anomaly detection is required to understand their zero-shot capabilities compared to specialized, task-specific architectures. This involves establishing standardized protocols for evaluating these models across heterogeneous anomaly detection benchmarks.

**Why It Matters:** Foundation models represent a paradigm shift in time-series analysis, yet their specific utility for anomaly detection is unverified, potentially overshadowing traditional task-specific inductive biases.

**Evidence:** Time-series foundation models pretrained on heterogeneous corpora – MOMENT [4] and GPT4TS [21] – offer zero-shot anomaly detection through pretrained reconstruction; we leave a careful foundation-model evaluation to future work.