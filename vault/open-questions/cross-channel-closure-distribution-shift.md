---
created_at: '2026-10-29T11:10:20Z'
source_papers:
- '[[openalex-2610.35753-closure-cross-channel-closure-for-multivariate-time-series-a]]'
title: Cross-Channel Closure Under Shift
---

**Background:** Multivariate time series anomaly detection relies on reconstruction models that certify observation recoverability but struggle to verify whether cross-channel relationships remain consistent with normal operation.

**Question / Future Work:** Investigate whether and how relation learning and cross-channel consistency checks can be systematically adapted to handle distribution shift, streaming delays, and non-stationary system dynamics without relying on offline detrending or heuristic score calibration.

**Why It Matters:** Understanding how decoupled cross-channel consistency checks perform under non-stationary shifts and streaming deployments is crucial for real-world industrial monitoring where assumptions of static normal operating distributions frequently fail.