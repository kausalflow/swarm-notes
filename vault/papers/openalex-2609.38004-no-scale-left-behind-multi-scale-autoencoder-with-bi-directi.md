---
# CSL-compatible fields
title: "No Scale Left Behind: Multi-Scale Autoencoder with Bi-directional Attention for Time Series Anomaly Detection"
author:
  - literal: "Jiaheng Guo"
  - literal: "Haochen Zhang"
  - literal: "Yu-Chao Huang"
  - literal: "Jinhao Duan"
  - literal: "Nicholas Knoz"
  - literal: "Tianlong Chen"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.38004"

# Custom fields
paper_id: "2609.38004"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "attention-mechanism"
  - "benchmark"
  - "semi-supervised-learning"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "mscad"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-01T11:15:46Z"
created_at: "2026-10-01T11:15:46Z"
---

# No Scale Left Behind: Multi-Scale Autoencoder with Bi-directional Attention for Time Series Anomaly Detection

**Authors**: Jiaheng Guo, Haochen Zhang, Yu-Chao Huang, Jinhao Duan, Nicholas Knoz, Tianlong Chen
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.38004](https://arxiv.org/abs/2609.38004)

## Summary

Time series anomaly detection often struggles to capture anomalies spanning diverse temporal scales due to reliance on single granularities or rigid hierarchical designs. To address this, the authors introduce MSCAD, a semi-supervised framework featuring parallel autoencoder branches across different patch sizes coupled with symmetric bidirectional cross-scale attention. This enables unprivileged, comprehensive scale interaction and reconstruction, achieving substantial performance gains over 50 baselines on the TSB-AD benchmark.

## Key Contributions

- Proposes MSCAD, a semi-supervised time series anomaly detection framework founded on parallel autoencoder branches corresponding to different patch sizes.
- Introduces a stack of symmetric bidirectional cross-scale attention blocks allowing every pair of scales to exchange information before reconstruction without scale privilege.
- Achieves state-of-the-art performance on the TSB-AD benchmark, reaching VUS-PR of 0.57 (+9.6%) on the univariate split and 0.47 (+9.3%) on the multivariate split across 40 datasets and 530 series.

## Limitations

None explicitly stated in the abstract.

## Open Questions & Future Work

- [[efficient-amortized-multiscale-tsad]]

## Key Concepts

- [[mscad]]: A semi-supervised time series anomaly detection framework using parallel autoencoder branches and symmetric bidirectional cross-scale attention.

## Archivist Review

Approved the core MSCAD framework concept and the explicit open question regarding efficient amortized multi-scale TSAD scaling and distillation. The dataset TSB-AD was rejected as it duplicates existing collection listings or standard evaluation suites in the vault.

### Approved Concepts
- MSCAD: Proposes a multi-scale autoencoder framework using parallel branches and symmetric bidirectional cross-scale attention for robust time series anomaly detection.

### Approved Open Questions
- Efficient and Amortized Multi-Scale TSAD: This is technically crucial for enabling real-time deployment and resource-constrained inference in high-stakes monitoring systems.

### Rejected Candidates
- [dataset] TSB-AD benchmark (`tsb-ad`) - duplicate_existing: The TSB-AD benchmark is already tracked under tsb-ad-u-eva or similar names, or is a collection rather than a distinct primary dataset.

## Links

- [Abstract](https://arxiv.org/abs/2609.38004)
- [PDF](https://arxiv.org/pdf/2609.38004)

