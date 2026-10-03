---
created_at: '2026-10-03T10:07:32Z'
source_papers:
- '[[openalex-2609.39386-when-not-how-much-evaluating-time-series-foundation-models-o]]'
title: Decision-Aware Sparse-Event Benchmarks
---

**Background:** Pretrained time-series foundation models are increasingly evaluated as zero-shot forecasters of future values, but standard benchmarks largely ignore intermittent or sparse-event time series where decisions depend strictly on occurrence timing rather than magnitude.

**Question / Future Work:** Future work needs to establish comprehensive evaluation benchmarks for time-series foundation models on sparse-event and intermittent demand tasks, moving beyond traditional value-based forecasting metrics to assess probability calibration, decision utility, and event occurrence ranking.

**Why It Matters:** Important for extending time-series foundation models beyond value-forecasting to real-world operational decision-making tasks like inventory management and anomaly detection.

**Evidence:** Our metrics assess ranking only, not the calibration of event probabilities or their value for downstream decisions.