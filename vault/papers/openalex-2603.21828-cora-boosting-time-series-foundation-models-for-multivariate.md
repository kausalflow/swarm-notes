---
# CSL-compatible fields
title: "CoRA: Boosting Time Series Foundation Models for Multivariate Forecasting through Correlation-aware Adapter"
author:
  - literal: "Hanyin Cheng"
  - literal: "Xingjian Wu"
  - literal: "Yang Shu"
  - literal: "Zhongwen Rao"
  - literal: "Lujia Pan"
  - literal: "Bin Yang"
  - literal: "Chenjuan Guo"
issued:
  date-parts:
    - [2026, 3, 23]
url: "https://arxiv.org/abs/2603.21828"

# Custom fields
paper_id: "2603.21828"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "adapter"
  - "parameter-efficient-fine-tuning"
  - "contrastive-learning"
  - "llm"
architectures:
  []
datasets:
  - "10 real-world datasets"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:10:00Z"
created_at: "2026-03-27T14:10:00Z"
---

# CoRA: Boosting Time Series Foundation Models for Multivariate Forecasting through Correlation-aware Adapter

**Authors**: Hanyin Cheng, Xingjian Wu, Yang Shu, Zhongwen Rao, Lujia Pan, Bin Yang, Chenjuan Guo
**Date**: 2026-03-23
**Paper ID**: [openalex:2603.21828](https://arxiv.org/abs/2603.21828)

## Summary

This paper introduces CoRA (Correlation-aware Adapter), a lightweight, plug-and-play module designed to improve Time Series Foundation Models (TSFMs) in multivariate forecasting by addressing their tendency to neglect inter-channel correlations. CoRA achieves this by decomposing the correlation matrix into low-rank Time-Varying and Time-Invariant components, the former modeled using learnable polynomials for dynamic patterns. Furthermore, it employs a dual contrastive learning approach with a Heterogeneous-Partial contrastive loss to capture specific positive and negative correlations between channels. Extensive experiments across ten real-world datasets confirm that CoRA significantly boosts the forecasting performance of existing TSFMs when fine-tuned.

## Key Contributions

- Proposing CoRA, a lightweight, plug-and-play adapter that enhances Time Series Foundation Models (TSFMs) for multivariate forecasting by explicitly modeling channel correlations without changing the base model.
- Innovatively decomposing the correlation matrix into low-rank Time-Varying and Time-Invariant components to manage complexity and capture dependency structures efficiently.
- Designing learnable polynomials to model dynamic correlations within the Time-Varying component, enabling the capture of trends or periodic patterns across channels.
- Introducing a dual contrastive learning method regulated by a Heterogeneous-Partial contrastive loss to effectively identify both positive and negative cross-channel correlations during training.

## Limitations

The paper does not explicitly detail any limitations, but the focus on lightweight adaptation suggests potential performance caps compared to fully retraining large models or the overhead of polynomial coefficient learning.

## Open Questions & Future Work

- [[comprehensive-correlation-modeling-tsfms]]

## Key Concepts

- [Correlation-aware Adapter](../concepts/correlation-aware-adapter.md): A lightweight, plug-and-play adapter module designed to boost Time Series Foundation Models (TSFMs) for multivariate forecasting by explicitly modeling channel correlations.
- [Time-Varying and Time-Invariant Correlation Decomposition](../concepts/time-varying-time-invariant-correlation-decomposition.md): A method to decompose the correlation matrix into low-rank, separate time-varying and time-invariant components to efficiently capture different aspects of channel dependencies.
- [Heterogeneous-Partial Contrastive Loss](../concepts/heterogeneous-partial-contrastive-loss.md): A novel dual contrastive learning regulation used during training to identify and emphasize positive and negative correlations among specific subsets of channels.

## Datasets

- [10 real-world datasets](../datasets/10-real-world-datasets.md)

## Limitations

The paper does not explicitly detail any limitations, but the focus on lightweight adaptation suggests potential performance caps compared to fully retraining large models or the overhead of polynomial coefficient learning.

## Links

- [Abstract](https://arxiv.org/abs/2603.21828)
- [PDF](https://arxiv.org/pdf/2603.21828)

