---
# CSL-compatible fields
title: "EAST: Early Action Prediction Sampling Strategy with Token Masking"
author:
  - literal: "Iva Sović"
  - literal: "Ivan Martinović"
  - literal: "Marin Oršić"
issued:
  date-parts:
    - [2026, 4, 20]
url: "https://arxiv.org/abs/2604.18367"

# Custom fields
paper_id: "2604.18367"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "video-understanding"
  - "efficient-transformer"
  - "token-masking"
  - "forecasting"
  - "benchmark"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "randomized-observation-sampling"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-23T06:57:17Z"
created_at: "2026-04-23T06:57:17Z"
---

# EAST: Early Action Prediction Sampling Strategy with Token Masking

**Authors**: Iva Sović, Ivan Martinović, Marin Oršić
**Date**: 2026-04-20
**Paper ID**: [openalex:2604.18367](https://arxiv.org/abs/2604.18367)

## Summary

EAST is a novel framework for early action prediction that addresses the challenge of limited visual evidence in incomplete video sequences. The method employs a randomized training strategy that samples the transition point between observed and future frames, allowing models to generalize effectively across arbitrary observation ratios. Additionally, the approach utilizes a token masking procedure that significantly improves training efficiency and memory overhead, establishing new state-of-the-art performance on NTU60, SSv2, and UCF101 datasets.

## Key Contributions

- Introduces EAST, a framework for early action prediction that uses a randomized time-step sampling strategy for robust generalization across observation ratios.
- Demonstrates that joint learning on observed and oracle future representations enables encoder-only architectures to reach state-of-the-art performance.
- Proposes a token masking procedure that reduces training memory and computation by 50% while maintaining prediction accuracy.

## Open Questions & Future Work

- [[unified-anticipation-prediction-method]]

## Key Concepts

- [[randomized-observation-sampling]]: A training strategy for early action prediction that randomizes the temporal split point between observed and unobserved frames.

## Archivist Review

Approved a genericized version of the randomized sampling concept, as it represents a useful training inductive bias for sequential forecasting. The open question regarding the unification of anticipation and prediction tasks is retained as it targets a fundamental limitation in modern temporal model design. Routine benchmark datasets were rejected to prioritize high-impact architectural and methodological entries.

### Approved Concepts
- Randomized Observation Sampling (for Early Prediction): It provides a model-agnostic training methodology that enables a single video encoder to generalize to arbitrary, varying observation ratios during inference.

### Approved Open Questions
- Unified Anticipation and Prediction Method: Unifying these tasks addresses the inherent redundancy in current video understanding pipelines, potentially leading to more efficient, general-purpose temporal encoders.

### Rejected Candidates
- [concept] EAST (Early Action Prediction Sampling Strategy) (`east-early-action-prediction-sampling-strategy`) - other: Renamed to a more descriptive, reusable term (randomized-observation-sampling) rather than a paper-specific framework name.
- [dataset] NTU60 (`NTU60`) - not_reusable: Routine benchmarking dataset; does not warrant a standalone vault entry.
- [dataset] SSv2 (`SSv2`) - not_reusable: Routine benchmarking dataset; does not warrant a standalone vault entry.
- [dataset] UCF101 (`UCF101`) - not_reusable: Routine benchmarking dataset; does not warrant a standalone vault entry.

## Links

- [Abstract](https://arxiv.org/abs/2604.18367)
- [PDF](https://arxiv.org/pdf/2604.18367)

