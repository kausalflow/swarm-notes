---
created_at: '2026-07-11T07:05:03Z'
source_papers:
- '[[openalex-2607.07500-timee-end-to-end-time-series-classification-via-in-context-l]]'
title: Scalable Multi-class ICL Inference
---

**Background:** In-context learning models for time series classification frequently rely on one-vs-rest (OvR) decomposition strategies to handle large label spaces, which leads to significant inference overhead as the number of classes increases.

**Question / Future Work:** Efficient, native mechanisms for handling multi-class time series classification beyond one-vs-rest decomposition are required to enable scaling to larger label spaces without prohibitively increasing inference computational costs.

**Why It Matters:** Handling large label spaces efficiently is essential for moving toward general-purpose, scalable foundation models for time series classification.

**Evidence:** TimEE is pre-trained with at most 10 classes and relies on a one-vs-rest decomposition for larger label spaces... Extending TimEE to natively support larger class counts is an important direction for future work.