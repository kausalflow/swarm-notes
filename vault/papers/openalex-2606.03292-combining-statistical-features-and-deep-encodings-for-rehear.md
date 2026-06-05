---
# CSL-compatible fields
title: "Combining Statistical Features and Deep Encodings for Rehearsal-Based Class-Incremental Time Series Classification"
author:
  - literal: "Pablo García-Santaclara"
  - literal: "Bruno Fernández-Castro"
  - literal: "Rebeca Pilar Díaz-Redondo"
issued:
  date-parts:
    - [2026, 6, 2]
url: "https://arxiv.org/abs/2606.03292"

# Custom fields
paper_id: "2606.03292"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "text-classification"
  - "continual-learning"
  - "embedding"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-05T08:38:33Z"
created_at: "2026-06-05T08:38:33Z"
---

# Combining Statistical Features and Deep Encodings for Rehearsal-Based Class-Incremental Time Series Classification

**Authors**: Pablo García-Santaclara, Bruno Fernández-Castro, Rebeca Pilar Díaz-Redondo
**Date**: 2026-06-02
**Paper ID**: [openalex:2606.03292](https://arxiv.org/abs/2606.03292)

## Summary

This paper addresses the challenge of class-incremental continual learning in multivariate time series classification by preserving previously learned knowledge. The authors introduce a dual-stream architecture that fuses deep temporal embeddings derived from pre-trained foundation models with statistical feature extraction. Evaluation across five benchmarks demonstrates that this hybrid approach effectively mitigates catastrophic forgetting while maintaining competitive classification accuracy.

## Key Contributions

- Proposes a dual-stream feature extraction pipeline combining deep temporal embeddings from frozen foundation models with handcrafted statistical features for multivariate time series.
- Improves class-incremental continual learning performance by reducing catastrophic forgetting in time-series classification.
- Achieves competitive average accuracy and low forgetting rates across five benchmark datasets for incremental category learning.

## Open Questions & Future Work

- [[autonomous-distribution-shift-adaptation-in-continual-learning]]

## Archivist Review

The proposed dual-stream feature fusion is a common architectural pattern and does not warrant a new standalone concept. I have approved the open question regarding autonomous distribution shift detection as it addresses a core limitation in the field of continual learning. The WISDM-specific question was rejected as it is too granular and tied to a single benchmark.

### Approved Open Questions
- Autonomous Shift Detection Adaptation: This is a fundamental prerequisite for moving continual learning from controlled incremental learning tasks to real-world, unconstrained deployment.

### Rejected Candidates
- [open_question] WISDM Performance Bottleneck (`wisdm-dataset-performance-bottleneck`) - paper_local: This is a dataset-specific performance observation rather than a fundamental mechanism or research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2606.03292)
- [PDF](https://arxiv.org/pdf/2606.03292)

