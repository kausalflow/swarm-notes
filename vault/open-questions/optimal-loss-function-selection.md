---
created_at: '2026-03-27T14:08:29Z'
source_papers:
- '[[openalex-2602.22694-robust-optimal-reconciliation-for-hierarchical-time-series-f]]'
title: Optimizing M-estimation loss function
---

**Background:** The RoME framework utilizes M-estimation with a user-specified loss function (e.g., LS, LAD, Huber) to reconcile base forecasts, offering robustness over purely least-squares approaches like MinT. Selecting the appropriate loss function and tuning its parameters is crucial for optimal performance.

**Question / Future Work:** Selecting an optimal loss function and tuning its associated parameters within the M-estimation framework for RoME remains a challenging and application-dependent task. A promising avenue for further improvement involves systematically investigating advanced combination strategies for reconciled forecasts obtained from different loss functions, moving beyond simple averaging strategies.