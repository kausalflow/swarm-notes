---
# CSL-compatible fields
title: "RATL: Learning from Retrieved Residuals for Robust Multivariate Time-Series Forecasting"
author:
  - literal: "Yuchen He"
  - literal: "Yueyang Cang"
  - literal: "Zhiyuan Ning"
  - literal: "Nan Wang"
  - literal: "Li Shi"
issued:
  date-parts:
    - [2026, 9, 3]
url: "https://arxiv.org/abs/2609.03937"

# Custom fields
paper_id: "2609.03937"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "retrieval-augmented-generation"
  - "multivariate-time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "ratl"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-05T08:41:46Z"
created_at: "2026-09-05T08:41:46Z"
---

# RATL: Learning from Retrieved Residuals for Robust Multivariate Time-Series Forecasting

**Authors**: Yuchen He, Yueyang Cang, Zhiyuan Ning, Nan Wang, Li Shi
**Date**: 2026-09-03
**Paper ID**: [openalex:2609.03937](https://arxiv.org/abs/2609.03937)

## Summary

The paper introduces RATL, a plug-in residual-retrieval and feedback-correction method for multivariate time-series forecasting that replaces raw-value retrieval with historical forecast residual memory. RATL freezes a base forecaster, constructs retrieval keys from historical contexts, and uses a set-aware router to select and combine retrieved residual trajectories at inference time under causal constraints. Experiments demonstrate that RATL reliably improves the performance of frozen base forecasters across multiple real-world benchmarks.

## Key Contributions

- Proposes RATL, a plug-in residual-retrieval and feedback-correction method that shifts retrieval targets from raw values to base-model-specific historical forecast errors.
- Utilizes a set-aware router operating over forecast blocks and variables to select and combine retrieved residual trajectories under causal availability constraints.
- Demonstrates consistent performance improvements when plugging RATL into frozen base forecasters such as iTransformer across real-world multivariate time-series benchmarks.

## Limitations

Relying on train-only memory requires efficient indexing and storage of historical residuals, and correction strength must be carefully tuned via validation to avoid residual over-injection.

## Open Questions & Future Work

- [[efficient-memory-compression-retrieval]]

## Key Concepts

- [[ratl]]: A plug-in residual-retrieval and feedback-correction method that augments frozen base forecasters with retrieved historical residual memories for robust multivariate time-series forecasting.

## Archivist Review

Approved the core residual-retrieval framework concept (RATL) and its key scalability open question regarding efficient memory compression, while adhering strictly to scarcity constraints and avoiding redundant or routine dataset/architecture additions.

### Approved Concepts
- RATL: Introduces a novel retrieval-augmented feedback correction paradigm for continuous-output regression that retrieves historical forecast residuals rather than raw target values.

### Approved Open Questions
- Efficient Memory Compression and Retrieval: Crucial for scaling retrieval-augmented time-series methods to large real-world industrial and operational deployments with high-dimensional multivariate streams.

### Rejected Candidates
- [concept] iTransformer (`itransformer`) - not_novel: Existing model architecture, not introduced by this paper.

## Links

- [Abstract](https://arxiv.org/abs/2609.03937)
- [PDF](https://arxiv.org/pdf/2609.03937)

