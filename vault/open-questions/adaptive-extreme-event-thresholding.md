---
created_at: '2026-07-05T07:51:28Z'
source_papers:
- '[[openalex-2607.02437-extreme-adaptive-transformer-for-time-series-forecasting]]'
title: Adaptive extreme event thresholding
---

**Background:** Time series forecasting models often struggle to handle imbalanced datasets where rare extreme events significantly impact target variables, such as in hydrologic streamflow prediction. Static sparse attention mechanisms fail to adaptively prioritize these rare events during long-range dependency modeling.

**Question / Future Work:** A primary unresolved challenge is developing dynamic, label-aware attention mechanisms that can effectively distinguish between different types of events (e.g., normal vs. extreme) without relying on pre-defined static thresholds or computationally expensive full-attention architectures. While existing models use fixed labels or thresholds, there is a need for robust, self-adaptive mechanisms that can handle evolving definitions of extreme events in non-stationary time series environments.

**Why It Matters:** Current methods rely on pre-determined thresholds to classify extremes, which limits robustness in real-world scenarios where extreme events are non-stationary and thresholds are difficult to define. Improving the adaptability of extreme-aware attention is essential for generalizable, mission-critical forecasting.