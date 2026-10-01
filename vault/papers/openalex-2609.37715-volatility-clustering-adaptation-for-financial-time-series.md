---
# CSL-compatible fields
title: "Volatility-Clustering Adaptation for Financial Time Series"
author:
  - literal: "Manh Nguyen"
  - literal: "Minh Hoang Nguyen"
  - literal: "Huu Hiep Nguyen"
  - literal: "Van Dai Do"
  - literal: "Hung Le"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.37715"

# Custom fields
paper_id: "2609.37715"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "language-model"
  - "pre-training"
  - "fine-tuning"
  - "finance"
architectures:
  []
datasets:
  []
concept_slugs:
  - "volatility-clustering-adaptation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-01T11:14:54Z"
created_at: "2026-10-01T11:14:54Z"
---

# Volatility-Clustering Adaptation for Financial Time Series

**Authors**: Manh Nguyen, Minh Hoang Nguyen, Huu Hiep Nguyen, Van Dai Do, Hung Le
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.37715](https://arxiv.org/abs/2609.37715)

## Summary

This paper investigates the adaptation of time-series foundation models to financial domains, demonstrating that standard next-token prediction fine-tuning often fails due to the unique volatility clustering properties of financial assets. To address this, the authors propose Volatility-Clustering Adaptation (VCA), which augments cross-entropy loss with a differentiable penalty matching the squared return autocorrelations of autoregressive rollouts to realized futures. Evaluations across multiple asset sets and conventions show that VCA improves forecasting performance and reduces variance error compared to standard pre-trained models.

## Key Contributions

- Identifies and challenges the standard assumption that larger target data sizes consistently improve financial time-series foundation model fine-tuning.
- Introduces Volatility-Clustering Adaptation (VCA), augmenting next-token cross-entropy with a differentiable penalty on the autocorrelation of squared returns.
- Demonstrates robust adaptation improvements over pre-trained foundation models across three asset sets and two evaluation conventions, driven largely by reduced variance error.

## Open Questions & Future Work

- [[volatility-clustering-adaptation-scaling]]

## Key Concepts

- [[volatility-clustering-adaptation]]: A fine-tuning adaptation method for financial time-series foundation models that augments next-token cross-entropy with a differentiable penalty on squared return autocorrelations.

## Archivist Review

Approved the core methodological concept of Volatility-Clustering Adaptation and the corresponding open question regarding its scaling across diverse backbones and asset classes. No routine datasets or redundant concepts were introduced.

### Approved Concepts
- Volatility-Clustering Adaptation: VCA is the core methodological contribution of the paper, introducing a specialized adaptation objective for financial time-series foundation models that incorporates volatility clustering.

### Approved Open Questions
- Scaling Volatility-Clustering Adaptation: Understanding the scalability and cross-architecture robustness of domain-specific path-level losses is critical for reliable financial forecasting and bridging general-purpose time-series foundation models with domain-informed learning.

## Links

- [Abstract](https://arxiv.org/abs/2609.37715)
- [PDF](https://arxiv.org/pdf/2609.37715)

