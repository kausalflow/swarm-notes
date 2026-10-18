---
# CSL-compatible fields
title: "Sparse Federated Echo State Networks for Time-Series Classification via Smooth-L1 Regularization"
author:
  - literal: "Gengcheng Lyu"
  - literal: "Manuel Röder"
  - literal: "Frank-Michael Schleif"
issued:
  date-parts:
    - [2026, 10, 15]
url: "https://arxiv.org/abs/2610.21742"

# Custom fields
paper_id: "2610.21742"
paper_source: "openalex"
domain: "time-series"
tags:
  - "federated-learning"
  - "reservoir"
  - "time-series"
  - "text-classification"
  - "model-compression"
  - "sparsity"
  - "efficient-transformer"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-18T09:12:55Z"
created_at: "2026-10-18T09:12:55Z"
---

# Sparse Federated Echo State Networks for Time-Series Classification via Smooth-L1 Regularization

**Authors**: Gengcheng Lyu, Manuel Röder, Frank-Michael Schleif
**Date**: 2026-10-15
**Paper ID**: [openalex:2610.21742](https://arxiv.org/abs/2610.21742)

## Summary

This paper introduces SL1ESN, a Smooth-L1 regularized Echo State Network designed to promote readout layer sparsity for efficient time-series classification in resource-constrained environments. By employing a twice-differentiable Smooth-L1 approximation compatible with Newton's method, the approach supports both centralized training and a second-order federated aggregation scheme. Experiments on seven time-series benchmarks demonstrate that SL1ESN achieves 75-95% sparsity with minimal accuracy loss compared to dense baselines, while significantly reducing model storage, inference cost, and communication overhead.

## Key Contributions

- Introduces a Smooth-L1 regularized Echo State Network (SL1ESN) with a twice-differentiable approximation compatible with Newton's method for sparsity promotion in readout layers.
- Proposes a second-order (Newton-step) federated aggregation scheme for distributed training of sparse ESNs.
- Achieves 75-95% sparsity in both centralized and federated settings while remaining within small accuracy margins of dense baselines across multiple time-series classification benchmarks.

## Open Questions & Future Work

- [[non-iid-federated-smooth-l1-esns]]

## Archivist Review

Reviewed the candidates against vault standards. The proposed concept candidates were omitted or rejected as paper-local variants of reservoir compression. One open question on non-IID federated optimization was approved as it targets a general distributed learning challenge in resource-constrained environments.

### Approved Open Questions
- Non-IID Federated Optimization: Overcoming non-IID data challenges is crucial for deploying federated reservoir computing frameworks in real-world decentralized IoT environments where data distributions vary across devices.

### Rejected Candidates
- [open_question] Support Identifiability and Interpretability (`support-identifiability-sparse-esns`) - paper_local: Addresses a paper-specific limitation regarding feature selection versus model compression in sparse ESNs rather than a broadly generalizable technical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.21742)
- [PDF](https://arxiv.org/pdf/2610.21742)

