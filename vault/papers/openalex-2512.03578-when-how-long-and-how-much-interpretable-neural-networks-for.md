---
# CSL-compatible fields
title: "When, how long and how much? Interpretable neural networks for time series regression by learning to mask and aggregate"
author:
  - literal: "Florent Forest"
  - literal: "Anlei Wei"
  - literal: "Olga Fink"
issued:
  date-parts:
    - [2026, 9, 21]
url: "https://arxiv.org/abs/2512.03578"

# Custom fields
paper_id: "2512.03578"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "interpretability"
  - "explainability"
  - "neural-network"
  - "time-series-extrinsic-regression"
architectures:
  []
datasets:
  []
concept_slugs:
  - "magnets"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-22T09:33:59Z"
created_at: "2026-09-22T09:33:59Z"
---

# When, how long and how much? Interpretable neural networks for time series regression by learning to mask and aggregate

**Authors**: Florent Forest, Anlei Wei, Olga Fink
**Date**: 2026-09-21
**Paper ID**: [openalex:2512.03578](https://arxiv.org/abs/2512.03578)

## Summary

Time series extrinsic regression (TSER) models often trade interpretability for predictive performance or rely on unstable post-hoc explanations. To address this, the authors propose Mask-and-Aggregate Networks for Time Series (MAGNETS), an inherently interpretable architecture that learns compact, human-understandable concepts via mask-based aggregation directly from data. MAGNETS delivers faithful, input-specific explanations by expressing predictions as transparent combinations of these learned concepts. Experiments demonstrate that MAGNETS matches black-box accuracy and outperforms existing interpretable baselines, especially on multivariate interaction tasks.

## Key Contributions

- Proposes Mask-and-Aggregate Networks for Time Series (MAGNETS), an inherently interpretable neural architecture for time series extrinsic regression (TSER).
- Learns a compact set of human-understandable concepts directly from data without requiring concept annotations using mask-based aggregation over input features.
- Achieves accuracy comparable to black-box models while substantially outperforming existing interpretable baselines on both univariate and multivariate TSER datasets.

## Open Questions & Future Work

- [[time-series-classification-concept-discovery]]

## Key Concepts

- [[magnets]]: An inherently interpretable neural network for time series extrinsic regression that learns human-understandable concepts via mask-based aggregation over input features.

## Archivist Review

Approved the central architectural concept (MAGNETS) and an explicit future research direction regarding its extension to time series classification, while rejecting standard problem formulations like TSER.

### Approved Concepts
- Mask-and-Aggregate Networks for Time Series (MAGNETS): Serves as the core proposed inherently interpretable neural architecture for time series extrinsic regression, addressing the trade-off between black-box performance and interpretability.

### Approved Open Questions
- Unsupervised Concept Discovery for Classification: Extending concept bottleneck and mask-based architectures from regression to classification broadens their applicability across diverse time series downstream tasks.

### Rejected Candidates
- [concept] Time Series Extrinsic Regression (`time-series-extrinsic-regression`) - not_novel: Standard problem setting in time series analysis rather than a novel methodological concept or architecture.

## Links

- [Abstract](https://arxiv.org/abs/2512.03578)
- [PDF](https://arxiv.org/pdf/2512.03578)

