---
# CSL-compatible fields
title: "FMMVCC: Fuzzy Mamba-based Multi-View Contrastive Clustering for Univariate Time Series"
author:
  - literal: "Donato Cerciello"
  - literal: "Leonardo Schiavo"
  - literal: "Ángel Panizo-LLedot"
  - literal: "Javier Huertas‐Tato"
  - literal: "David Camacho"
issued:
  date-parts:
    - [2026, 7, 8]
url: "https://arxiv.org/abs/2607.07258"

# Custom fields
paper_id: "2607.07258"
paper_source: "openalex"
domain: "time-series"
tags:
  - "mamba"
  - "state-space-model"
  - "ssm"
  - "time-series"
  - "self-supervised-learning"
  - "clustering"
architectures:
  - "mamba"
datasets:
  []
concept_slugs:
  - "fmmvcc"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-11T07:05:20Z"
created_at: "2026-07-11T07:05:20Z"
---

# FMMVCC: Fuzzy Mamba-based Multi-View Contrastive Clustering for Univariate Time Series

**Authors**: Donato Cerciello, Leonardo Schiavo, Ángel Panizo-LLedot, Javier Huertas‐Tato, David Camacho
**Date**: 2026-07-08
**Paper ID**: [openalex:2607.07258](https://arxiv.org/abs/2607.07258)

## Summary

FMMVCC is a novel deep clustering framework for univariate time series that addresses the challenges of computational cost and long-range dependency modeling. By utilizing Mamba-based state space models, the framework efficiently learns temporal representations with linear complexity. It further improves clustering robustness through a multi-view self-supervised learning approach involving temporal masking and data augmentation. Empirical evaluation across 15 benchmarks demonstrates that FMMVCC achieves state-of-the-art performance, outperforming existing deep clustering methods in both accuracy and ranking.

## Key Contributions

- Introduces FMMVCC, a deep clustering framework that integrates Mamba state-space models with multi-view self-supervised learning.
- Achieves linear computational complexity while capturing long-range temporal dependencies for univariate time series clustering.
- Demonstrates superior performance against state-of-the-art baselines across 15 benchmark datasets, ranking first in 29 out of 60 metrics.

## Open Questions & Future Work

- [[multivariate-time-series-extension]]

## Key Concepts

- [[fmmvcc]]: A fuzzy Mamba-based deep clustering framework for univariate time series that utilizes multi-view self-supervised learning for efficient representation discovery.

## Archivist Review

The paper introduces a Mamba-based deep clustering framework. I approved the framework concept as it represents a novel architectural fusion of SSMs and clustering. I also approved the multivariate extension as an open question because it represents a specific, non-trivial architectural gap in scaling the proposed univariate approach to real-world applications. The explainability question was rejected as overly generic.

### Approved Concepts
- FMMVCC: It combines Mamba's linear complexity with fuzzy clustering, providing a novel architectural pattern for unsupervised time series representation.

### Approved Open Questions
- Multivariate time series extension: This is a critical architectural bottleneck for scaling unsupervised representation learning from univariate experimental benchmarks to complex multivariate industrial data.

### Rejected Candidates
- [open_question] Latent space explainability (`latent-space-explainability`) - generic: Explainability in deep learning is a generic challenge that is not unique to this clustering approach.

## Links

- [Abstract](https://arxiv.org/abs/2607.07258)
- [PDF](https://arxiv.org/pdf/2607.07258)

