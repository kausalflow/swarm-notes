---
# CSL-compatible fields
title: "Tucker Bottleneck Attention for Multi-Dimensional Sequence Modeling"
author:
  - literal: "Ryan Solgi"
  - literal: "Parsa Madinei"
  - literal: "Zheng Zhang"
issued:
  date-parts:
    - [2026, 10, 6]
url: "https://arxiv.org/abs/2610.09090"

# Custom fields
paper_id: "2610.09090"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "attention-mechanism"
  - "self-attention"
  - "multi-head-attention"
  - "long-context"
  - "efficient-transformer"
  - "autoregressive"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "tucker-bottleneck-attention"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-09T11:36:25Z"
created_at: "2026-10-09T11:36:25Z"
---

# Tucker Bottleneck Attention for Multi-Dimensional Sequence Modeling

**Authors**: Ryan Solgi, Parsa Madinei, Zheng Zhang
**Date**: 2026-10-06
**Paper ID**: [openalex:2610.09090](https://arxiv.org/abs/2610.09090)

## Summary

The paper introduces Tucker bottleneck attention (TuBA), a novel mechanism that leverages low-rank tensor decompositions to achieve efficient subquadratic global token mixing for multi-dimensional sequence modeling. TuBA projects hidden tensors into compact Tucker cores for multi-head self-attention before writing updates back to the ambient space, supporting an autoregressive extension for causal modeling across cores. Evaluated on video prediction and global weather forecasting, TuBA significantly improves accuracy while reducing computation and yielding notable speedups compared to standard and efficient attention baselines.

## Key Contributions

- Introduces Tucker bottleneck attention (TuBA), exploiting low-rank tensor structures for subquadratic global token mixing on multi-dimensional sequences.
- Proposes an autoregressive extension combining bidirectional interactions within cores with causal attention across cores.
- Reduces error and computation by up to 24.7% and 66.6% for video prediction, and 37.1% and 85.1% for autoregressive weather forecasting, achieving speedups up to 4.27x over standard attention.

## Open Questions & Future Work

- [[adaptive-rank-selection-tuba]]

## Key Concepts

- [[tucker-bottleneck-attention]]: A multi-dimensional sequence modeling mechanism that projects hidden tensors into compact Tucker cores to perform efficient attention with subquadratic complexity.

## Archivist Review

Approved Tucker Bottleneck Attention as a highly reusable tensor-based attention mechanism and Adaptive Tucker Rank Selection as a key structural open question. Rejected the 1D tensorization question as a speculative application.

### Approved Concepts
- Tucker Bottleneck Attention: Core methodological contribution of the paper that enables subquadratic global token mixing via low-rank tensor decompositions.

### Approved Open Questions
- Adaptive Tucker Rank Selection: Eliminating the need for manual hyperparameter tuning of tensor ranks is crucial for scaling Tucker-based attention to diverse architectures and datasets without costly grid searches.

### Rejected Candidates
- [open_question] Tensorization for Long 1D Sequences (`tuba-for-1d-sequences`) - low_impact: Extending a multi-dimensional spatial-temporal attention mechanism to 1D text/audio sequences via tensorization is a speculative application rather than an immediate architectural bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.09090)
- [PDF](https://arxiv.org/pdf/2610.09090)

