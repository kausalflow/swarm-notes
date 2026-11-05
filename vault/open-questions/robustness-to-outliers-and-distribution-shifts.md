---
created_at: '2026-11-05T12:51:42Z'
source_papers:
- '[[openalex-2611.02489-cross-domain-joint-embedding-pretraining-for-heterogeneous-i]]'
title: Robustness to Outliers and Distribution Shifts
---

**Background:** Self-supervised cross-domain pretraining architectures like JEPA-HITS are currently limited in their validation scope, primarily covering standard predictive maintenance datasets without addressing severe anomalies such as extreme signal outliers, missing data streams, and distribution shifts.

**Question / Future Work:** Extend cross-domain self-supervised pretraining models and joint-embedding architectures to robustly handle extreme real-world industrial challenges including signal outliers, missing data streams, and severe distribution shifts across heterogeneous domains.

**Why It Matters:** Real-world industrial data is frequently plagued by missing values, sensor failures, and severe distribution shifts; understanding how cross-domain pretraining copes with these conditions is crucial for robust industrial deployment.

**Evidence:** Our work is not evaluated on extreme cases with signal outliers, missing data, and distribution shifts. Future work will extend JEPA-HITS to additional industrial domains and downstream tasks, including forecasting, leveraging its shared encoder design to scale across heterogeneous time series data and tasks.