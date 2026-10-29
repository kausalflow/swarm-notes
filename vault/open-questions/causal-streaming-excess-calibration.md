---
created_at: '2026-10-29T11:10:34Z'
source_papers:
- '[[openalex-2610.35568-excal-optimization-free-multivariate-time-series-anomaly-det]]'
title: Causal and Streaming Excess Calibration
---

**Background:** Time-series anomaly detection methods often rely on batch processing of entire sequences, leaving the efficacy of fully online, causal scoring variants unexplored.

**Question / Future Work:** Investigate and evaluate online or causal scoring variants of excess calibration methods, where prevalence factors and rank normalization are computed using prefix-only or streaming mechanisms rather than batch processing over the complete scored sequence.

**Why It Matters:** Critical for assessing real-time streaming telemetry deployment readiness where future context is unavailable.