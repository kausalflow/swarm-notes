---
created_at: '2026-10-03T10:08:34Z'
source_papers:
- '[[openalex-2609.39445-raw-routed-mixture-of-adapters-a-causal-intervention-for-rou]]'
title: Routing Collapse in TSFMs
---

**Background:** Time series foundation models often employ pre-encoder instance normalization such as RevIN, which strips per-window mean and variance statistics and leads to routing collapse in downstream mixture-of-adapters architectures.

**Question / Future Work:** Investigate normalization-induced routing collapse and the extension of raw-routed mixture of adapters (RR-MoA) and related causal interventions beyond time-series forecasting and imputation tasks (such as to classification, anomaly detection, and longer forecast horizons) as well as to learned expert pools.

**Why It Matters:** Understanding how normalization interacts with routing decisions across different machine learning tasks and modalities is crucial for generalizable mixture-of-experts architectures.

**Evidence:** Limitations: specific to (μ,σ)-stripping normalizers; classification, anomaly detection, horizons >720, and learned expert pools remain open.