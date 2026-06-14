---
created_at: '2026-06-14T08:37:25Z'
source_papers:
- '[[openalex-2606.13277-protox-ad-self-explainable-time-series-anomaly-detection-and]]'
title: Adaptive transformation learning strategies
---

**Background:** Self-supervised classification-based anomaly detection often relies on either manually defined transformations that encode domain knowledge or learnable neural transformations. The choice between these approaches represents a significant trade-off where manual transformations often outperform learnable ones in detection performance and explainability, but are limited by their domain-specific nature.

**Question / Future Work:** Future research is required to develop adaptive transformation learning strategies that bridge the gap between domain-specific manual transformations and generic, learnable neural transformations. This involves creating mechanisms that progressively incorporate knowledge about detected anomalies to refine transformation learning in a flexible, robust manner without sacrificing anomaly characterization or detection performance.

**Why It Matters:** The trade-off between domain-specific knowledge and model generality is a fundamental bottleneck in self-supervised anomaly detection, and solving it would expand model applicability.

**Evidence:** Future work should therefore explore adaptive approaches that progressively incorporate knowledge about detected anomalies to learn transformations in a more flexible way.