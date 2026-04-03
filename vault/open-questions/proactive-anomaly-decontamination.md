---
created_at: '2026-04-03T06:06:40Z'
source_papers:
- '[[openalex-2603.29183-impact-influence-modeling-for-open-set-time-series-anomaly-d]]'
title: Proactive Training Data Decontamination
---

**Background:** Training data for anomaly detection is frequently contaminated with unlabeled anomalies, leading to biased representations and degraded detection performance.

**Question / Future Work:** Existing contamination mitigation strategies are often post-hoc or rely on static assumptions, necessitating the development of proactive, training-time decontamination mechanisms that can dynamically identify and down-weight or relabel noisy samples.

**Why It Matters:** Proactive decontamination is essential for robust model training in real-world scenarios where perfectly clean datasets are unavailable.

**Evidence:** they primarily operate post-hoc, either estimating contamination after training or calibrating scores at inference time, and do not directly correct contaminated training samples.