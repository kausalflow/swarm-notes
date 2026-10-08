---
# CSL-compatible fields
title: "Normality Constraint Learning: Adapting Foundation Models for Time Series Anomaly Detection"
author:
  - literal: "Xiaohui Zhou"
  - literal: "Yijie Wang"
  - literal: "Hongzuo Xu"
  - literal: "Weixuan Liang"
  - literal: "Guansong Pang"
issued:
  date-parts:
    - [2026, 10, 5]
url: "https://arxiv.org/abs/2610.06453"

# Custom fields
paper_id: "2610.06453"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "pre-training"
  - "fine-tuning"
  - "contrastive-learning"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "normality-constraint-learning"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-08T11:40:29Z"
created_at: "2026-10-08T11:40:29Z"
---

# Normality Constraint Learning: Adapting Foundation Models for Time Series Anomaly Detection

**Authors**: Xiaohui Zhou, Yijie Wang, Hongzuo Xu, Weixuan Liang, Guansong Pang
**Date**: 2026-10-05
**Paper ID**: [openalex:2610.06453](https://arxiv.org/abs/2610.06453)

## Summary

Time series foundation models often struggle with anomaly detection because their strong general reconstruction and forecasting capabilities cause them to accurately reconstruct rare anomalies, thereby reducing anomaly scoring errors. To address this, the paper proposes Normality Constraint Learning (NCL), a lightweight framework that constrains the foundation model's broad pattern space to the target time series' normal structure without parameter modification. NCL constructs a compact normality subspace from normal patch features, steers representations via contrastive constraints, and fuses the calibrated features to amplify error discrepancies for anomalies.

## Key Contributions

- Proposes Normality Constraint Learning (NCL), a lightweight plug-and-play framework for adapting pre-trained time series foundation models for anomaly detection without modifying their parameters.
- Constructs a compact normality subspace from normal patch features to steer feature representations toward normality using contrastive constraints.
- Amplifies the reconstruction and forecasting error discrepancy between normal and abnormal observations across diverse TSFMs and benchmarks.

## Open Questions & Future Work

- [[adapting-tsfms-for-anomaly-detection]]

## Key Concepts

- [[normality-constraint-learning]]: A lightweight plug-and-play framework that adapts pre-trained time series foundation models for anomaly detection by constraining their pattern space to normal structures.

## Archivist Review

Approved the central framework 'Normality Constraint Learning' and the corresponding open question on adapting time series foundation models for anomaly detection, as they directly address the core methodological contribution and future direction of utilizing frozen TSFMs for anomaly detection without parameter modifications.

### Approved Concepts
- Normality Constraint Learning: Introduces a novel framework to adapt pre-trained time series foundation models for anomaly detection via normality constraint learning.

### Approved Open Questions
- Adapting TSFMs for Anomaly Detection: This question is central to adapting large-scale task-general pre-trained foundation models to specialized, distribution-sensitive downstream tasks such as unsupervised anomaly detection.

## Links

- [Abstract](https://arxiv.org/abs/2610.06453)
- [PDF](https://arxiv.org/pdf/2610.06453)

