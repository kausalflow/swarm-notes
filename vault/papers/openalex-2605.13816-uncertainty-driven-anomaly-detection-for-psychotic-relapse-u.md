---
# CSL-compatible fields
title: "Uncertainty-Driven Anomaly Detection for Psychotic Relapse Using Smartwatches: Forecasting and Multi-Task Learning Fusion"
author:
  - literal: "Nikolaos Tsalkitzis"
  - literal: "Panagiotis P. Filntisis"
  - literal: "Petros Maragos"
  - literal: "Niki Efthymiou"
issued:
  date-parts:
    - [2026, 5, 13]
url: "https://arxiv.org/abs/2605.13816"

# Custom fields
paper_id: "2605.13816"
paper_source: "openalex"
domain: "medicine"
tags:
  - "transformer"
  - "llm"
  - "anomaly-detection"
  - "time-series"
  - "multimodal"
  - "healthformer"
  - "evaluation"
  - "benchmark"
architectures:
  - "encoder-only"
datasets:
  - "2nd-e-prevention-grand-challenge-dataset"
concept_slugs:
  []
dataset_slugs:
  - "2nd-e-prevention-grand-challenge-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-05-16T07:09:41Z"
created_at: "2026-05-16T07:09:41Z"
---

# Uncertainty-Driven Anomaly Detection for Psychotic Relapse Using Smartwatches: Forecasting and Multi-Task Learning Fusion

**Authors**: Nikolaos Tsalkitzis, Panagiotis P. Filntisis, Petros Maragos, Niki Efthymiou
**Date**: 2026-05-13
**Paper ID**: [openalex:2605.13816](https://arxiv.org/abs/2605.13816)

## Summary

This paper addresses the early detection of psychotic relapse by leveraging continuous digital phenotyping from smartwatch sensors. The authors propose two transformer-based pipelines: one based on forecasting cardiac dynamics and another utilizing multi-task learning to integrate sleep, motion, and cardiac signals. A key innovation is the use of predictive uncertainty from ensemble models to drive anomaly scores, combined through a late-fusion strategy to improve detection robustness in real-world environments. Evaluations on the 2nd e-Prevention Grand Challenge dataset demonstrate that this multimodal integration significantly outperforms existing benchmarks.

## Key Contributions

- Developed two distinct smartwatch-based anomaly detection frameworks for psychotic relapse using Transformer encoders.
- Introduced a late-fusion strategy that synergistically combines predictive anomaly scores from cardiac forecasting and multi-task sleep/motion learning.
- Achieved an 8% relative improvement over the competition-winning baseline on the 2nd e-Prevention Grand Challenge dataset.

## Open Questions & Future Work

- [[early-fusion-for-multimodal-relapse-detection]]

## Archivist Review

The paper proposes a specific late-fusion strategy for multimodal health monitoring, but as these components are standard techniques in the field, they were rejected as generic or not novel. The identified open question regarding early versus late fusion for health relapse detection provides a high-quality, non-trivial research direction. The dataset from the e-Prevention Grand Challenge was approved as it serves as a central, named benchmark for this domain.

### Approved Open Questions
- Early fusion for relapse detection: Early fusion may allow for learning higher-order cross-modal dependencies that are invisible when modalities are processed independently and fused only at the final decision stage.

### Rejected Candidates
- [concept] Transformer encoders for anomaly detection (`transformer-encoders-in-anomaly-detection`) - generic: The use of standard Transformer encoders for anomaly detection is a generic application of established architectures rather than a distinct, reusable methodology.
- [concept] Uncertainty-driven late fusion strategy (`uncertainty-driven-late-fusion-strategy`) - not_novel: Late fusion and uncertainty estimation via ensembles are well-established practices in machine learning and do not constitute a sufficiently novel standalone concept.

## Datasets

- [[2nd-e-prevention-grand-challenge-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2605.13816)
- [PDF](https://arxiv.org/pdf/2605.13816)

