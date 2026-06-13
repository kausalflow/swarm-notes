---
created_at: '2026-06-13T08:15:49Z'
source_papers:
- '[[openalex-2606.11625-timerouter-efficient-and-adaptive-routing-of-time-series-fou]]'
title: Scaling Adaptive TSFM Expert Routing
---

**Background:** Time-series foundation models often possess heterogeneous predictive capabilities, yet current orchestration methods typically rely on computationally heavy LLM controllers or static threshold tuning.

**Question / Future Work:** Investigating methods for online adaptive thresholding and automated selection of foundation model pools is critical for scaling expert-based forecasting without relying on expensive controllers or manual grid searches for threshold calibration.

**Why It Matters:** Addresses the bottleneck of manual threshold tuning and static pool composition in multi-model forecasting systems.

**Evidence:** However, a lightweight discriminative routing layer for adaptive expert selection across TSFMs remains largely unexplored. ... The gate thresholds are selected by a grid sweep on a 5-fold task-grouped GroupKFold OOF split.