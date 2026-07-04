---
# CSL-compatible fields
title: "Detecting the Undetectable: Enhancing Unsupervised time series Anomaly Detection via Active Learning"
author:
  - literal: "Seung Hun Han"
  - literal: "Hyeongwon Kang"
  - literal: "Jinwoo Park"
  - literal: "Pilsung Kang"
issued:
  date-parts:
    - [2026, 7, 1]
url: "https://arxiv.org/abs/2607.00720"

# Custom fields
paper_id: "2607.00720"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "active-learning"
  - "unsupervised-learning"
  - "reconstruction"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-04T07:35:51Z"
created_at: "2026-07-04T07:35:51Z"
---

# Detecting the Undetectable: Enhancing Unsupervised time series Anomaly Detection via Active Learning

**Authors**: Seung Hun Han, Hyeongwon Kang, Jinwoo Park, Pilsung Kang
**Date**: 2026-07-01
**Paper ID**: [openalex:2607.00720](https://arxiv.org/abs/2607.00720)

## Summary

This paper addresses the difficulty of detecting subtle, noisy anomalies in complex time series by proposing an active learning-based framework that refines unsupervised models. By utilizing a masked reconstruction feedback mechanism and a minimax optimization strategy, the approach effectively differentiates near-normal anomalies from standard temporal patterns. Extensive evaluation across 28 test cases and seven backbone models confirms that this framework significantly boosts performance in unsupervised reconstruction-based anomaly detection settings.

## Key Contributions

- Proposes an active learning-based framework to iteratively refine unsupervised anomaly detection models for time series data.
- Introduces a masked time-series reconstruction feedback strategy to improve the learning of robust temporal dependencies.
- Develops a minimax learning strategy that enhances model robustness by differentially treating normal and abnormal samples to isolate subtle anomalies.
- Demonstrates a 12.39% average AUC improvement across 28 test cases by integrating the proposed method into existing reconstruction-based backbones.

## Open Questions & Future Work

- [[minimax-feedback-stability-limitations]]

## Archivist Review

The paper presents an incremental improvement to reconstruction-based anomaly detection using active learning. The core techniques—a specific reconstruction feedback loop and minimax loss—are implementation details rather than broadly reusable architectural patterns or fundamental methodological shifts. I have retained the open question concerning minimax feedback stability as it touches on a significant, non-trivial challenge in training these types of detectors.

### Approved Open Questions
- Improving Stability of Minimax Feedback: The reliance on minimax-based feedback is a core component of this framework's contribution, and its inherent instability represents a fundamental trade-off in reconstruction-based anomaly detection systems.

### Rejected Candidates
- [concept] Masked Time-Series Reconstruction Feedback (`masked-time-series-reconstruction-feedback`) - subcomponent_of_broader_mechanism: This is a local subcomponent of the proposed framework rather than a general, independently reusable concept.
- [concept] Minimax Learning Strategy (`minimax-learning-strategy`) - not_novel: This is a standard ML optimization objective applied to the paper's specific setting rather than a novel, reusable forecasting concept.
- [open_question] Robust Adaptive Hyperparameter Tuning (`adaptive-hyperparameter-tuning-active-learning`) - generic: This is a general, common challenge in machine learning and active learning that is not specific to time series anomaly detection.

## Links

- [Abstract](https://arxiv.org/abs/2607.00720)
- [PDF](https://arxiv.org/pdf/2607.00720)

