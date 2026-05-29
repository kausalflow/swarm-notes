---
# CSL-compatible fields
title: "Falcon-X: A Time Series Foundation Model for Heterogeneous Multivariate Modeling"
author:
  - literal: "Yiding Liu"
  - literal: "Yifan Hu"
  - literal: "Hongjie Xia"
  - literal: "Peiyuan Liu"
  - literal: "Hongzhou Chen"
  - literal: "Xilin Dai"
  - literal: "Zewei Dong"
  - literal: "Jiang-Ming Yang"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.27286"

# Custom fields
paper_id: "2605.27286"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "transformer"
  - "attention-mechanism"
  - "zero-shot-learning"
  - "multimodal"
architectures:
  []
datasets:
  []
concept_slugs:
  - "unified-prototype-diff-attention"
  - "variate-reassembly-router"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-29T08:37:23Z"
created_at: "2026-05-29T08:37:23Z"
---

# Falcon-X: A Time Series Foundation Model for Heterogeneous Multivariate Modeling

**Authors**: Yiding Liu, Yifan Hu, Hongjie Xia, Peiyuan Liu, Hongzhou Chen, Xilin Dai, Zewei Dong, Jiang-Ming Yang
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.27286](https://arxiv.org/abs/2605.27286)

## Summary

Falcon-X is a time series foundation model designed for heterogeneous multivariate modeling by decoupling variates from raw space into a shared latent prototype space. It addresses limitations in semantic alignment and relational expressivity by introducing a Unified Prototype Diff-Attention mechanism that accounts for both synergistic and antagonistic interactions. The model further improves robustness and scalability through a Variate Reassembly Router, achieving state-of-the-art results across major benchmarks like GIFT-Eval and fev-bench.

## Key Contributions

- Proposes Falcon-X, a time series foundation model that decouples variates into a unified latent prototype space to overcome limitations of raw-space modeling.
- Introduces Unified Prototype Diff-Attention to explicitly capture both synergistic and antagonistic interactions between heterogeneous variates.
- Achieves state-of-the-art forecasting performance on the GIFT-Eval and fev-bench benchmarks.

## Open Questions & Future Work

- [[heterogeneous-multivariate-semantic-alignment]]

## Key Concepts

- [[unified-prototype-diff-attention]]: An attention mechanism that explicitly evaluates positive and negative semantic affinities to align heterogeneous variates in a latent prototype space.
- [[variate-reassembly-router]]: A routing mechanism that reconstructs variate-specific trajectories from a shared latent prototype space.

## Archivist Review

Approved the core architecture components (Unified Prototype Diff-Attention and Variate Reassembly Router) as they represent generalizable mechanisms for multivariate time series modeling. The proposed open question regarding heterogeneous semantic alignment was accepted as it frames a substantial bottleneck in foundation model scalability. Benchmarks GIFT-Eval and fev-bench were rejected as they are domain-specific evaluation suites rather than foundational datasets.

### Approved Concepts
- Unified Prototype Diff-Attention: Addresses the limitation of standard attention in capturing complex synergistic and antagonistic interactions in time series.
- Variate Reassembly Router: Provides a robust way to map shared latent information back to specific multivariate trajectories.

### Approved Open Questions
- Heterogeneous Multivariate Semantic Alignment: This is a fundamental bottleneck for scaling foundation models to truly heterogeneous multivariate environments where variate meanings and interaction patterns vary significantly across datasets.

### Rejected Candidates
- [dataset] GIFT-Eval (`GIFT-Eval`) - low_impact: This is a new/specific evaluation benchmark which is not yet established as a foundational or critical resource.
- [dataset] fev-bench (`fev-bench`) - low_impact: This is a new/specific evaluation benchmark which is not yet established as a foundational or critical resource.

## Links

- [Abstract](https://arxiv.org/abs/2605.27286)
- [PDF](https://arxiv.org/pdf/2605.27286)

