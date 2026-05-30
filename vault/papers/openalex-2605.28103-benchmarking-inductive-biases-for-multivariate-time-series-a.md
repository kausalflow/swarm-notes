---
# CSL-compatible fields
title: "Benchmarking Inductive Biases for Multivariate Time-Series Anomaly Detection with a Robust Multi-View Channel-Graph Detector"
author:
  - literal: "Junhao Wei"
  - literal: "Yanxiao Li"
  - literal: "Bidong Chen"
  - literal: "Yifu Zhao"
  - literal: "Haochen Li"
  - literal: "姚德兴"
  - literal: "Baili Lu"
  - literal: "Xudong Ye"
  - literal: "Jietian Feng"
  - literal: "Sio‐Kei Im"
  - literal: "Yapeng Wang"
  - literal: "Xu Yang"
issued:
  date-parts:
    - [2026, 5, 27]
url: "https://arxiv.org/abs/2605.28103"

# Custom fields
paper_id: "2605.28103"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "benchmark"
  - "dataset"
  - "evaluation"
  - "robustness"
  - "attention-mechanism"
architectures:
  []
datasets:
  []
concept_slugs:
  - "robust-multi-view-channel-graph-detector"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-30T07:35:46Z"
created_at: "2026-05-30T07:35:46Z"
---

# Benchmarking Inductive Biases for Multivariate Time-Series Anomaly Detection with a Robust Multi-View Channel-Graph Detector

**Authors**: Junhao Wei, Yanxiao Li, Bidong Chen, Yifu Zhao, Haochen Li, 姚德兴, Baili Lu, Xudong Ye, Jietian Feng, Sio‐Kei Im, Yapeng Wang, Xu Yang
**Date**: 2026-05-27
**Paper ID**: [openalex:2605.28103](https://arxiv.org/abs/2605.28103)

## Summary

This paper provides a systematic benchmark of ten multivariate time-series (MTS) anomaly detection models across five standardized datasets using consistent evaluation protocols. The study identifies key insights into model behavior under perturbation and the nature of anomaly-dense workloads. Additionally, the authors introduce a robust detector family that combines a NOTEARS-constrained causal graph view with patch-attention and temporal-association, outperforming existing baselines in VUS-ROC accuracy and robustness.

## Key Contributions

- Conducted a rigorous benchmark of ten MTS anomaly detection methods across five datasets using standardized protocols and multi-seed robustness testing.
- Introduced a novel adaptive detector that integrates a NOTEARS-constrained channel-graph view with patch and temporal-association views.
- Demonstrated that the proposed detector achieves state-of-the-art macro-average VUS-ROC performance and superior robustness to noise, channel dropout, and time-shift perturbations.

## Open Questions & Future Work

- [[foundation-model-mts-anomaly-detection]]
- [[input-conditioned-channel-graphs-generalization]]

## Key Concepts

- [[robust-multi-view-channel-graph-detector]]: An adaptive anomaly detector that combines a NOTEARS-constrained directed channel-graph with patch-attention and temporal-association views.

## Archivist Review

Approved the proposed multi-view detector as a reusable methodology and kept both open questions regarding the tension between structural priors and foundation model utility. Rejected the collective list of datasets as they are well-established benchmarks rather than novel, domain-specific findings. The review maintained strict adherence to the forecasting-focused skill set constraints.

### Approved Concepts
- Robust Multi-View Channel-Graph Detector: It is the core proposed methodology which integrates causal graph priors with multi-view attention for anomaly detection.

### Approved Open Questions
- Evaluating Foundation Models for Anomaly Detection: Foundation models represent a paradigm shift in time-series analysis, yet their specific utility for anomaly detection is unverified, potentially overshadowing traditional task-specific inductive biases.
- Generalizing Structural Channel Priors: Structural priors are powerful in controlled settings, but their rigid nature limits cross-domain applicability, a major hurdle for deploying anomaly detectors in heterogeneous distributed systems.

### Rejected Candidates
- [dataset] Standardized Anomaly Detection Datasets (`MSD-datasets`) - duplicate_existing: These are standard public datasets (SMD, MSL, SMAP, etc.) already widely known and used; they do not warrant a new vault entry.

## Links

- [Abstract](https://arxiv.org/abs/2605.28103)
- [PDF](https://arxiv.org/pdf/2605.28103)

