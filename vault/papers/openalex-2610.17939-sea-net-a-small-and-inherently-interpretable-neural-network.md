---
# CSL-compatible fields
title: "Sea-Net: A Small and Inherently Interpretable Neural Network for Time Series Classification"
author:
  - literal: "Ubaid ur Rehman"
  - literal: "Tanmoy Mondal"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.17939"

# Custom fields
paper_id: "2610.17939"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "text-classification"
  - "interpretability"
  - "explainability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "sea-net"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-16T09:23:23Z"
created_at: "2026-10-16T09:23:23Z"
---

# Sea-Net: A Small and Inherently Interpretable Neural Network for Time Series Classification

**Authors**: Ubaid ur Rehman, Tanmoy Mondal
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.17939](https://arxiv.org/abs/2610.17939)

## Summary

Traditional time-series classification models often lack temporal interpretability and have large parameter footprints, making them unsuitable for resource-constrained edge devices. To address this, the paper introduces SEA-Net, a lightweight network leveraging multi-scale depthwise-separable convolutional encoders and improved Multiple Instance Learning (MIL) pooling heads. Variants of SEA-Net achieve superior accuracy and explanation scores (NDCG@n) compared to existing models while reducing model size to as few as 41K parameters.

## Key Contributions

- Proposes SEA-Net, a lightweight architecture for interpretable time-series classification utilizing multi-scale depthwise-separable convolutional encoders and improved Multiple Instance Learning (MIL) pooling.
- SEA-Net bottleneck encoder variant achieves 0.931 accuracy and 0.765 NDCG@n with only 41K parameters, significantly outperforming prior art like MILLET.
- SEA-Net gated encoder variant achieves 0.955 accuracy and 0.750 NDCG@n with only 62K parameters, enabling deployment on resource-constrained edge devices.

## Open Questions & Future Work

- [[memory-efficient-temporal-streaming-variants]]

## Key Concepts

- [[sea-net]]: A small and inherently interpretable neural network for time series classification using multi-scale depthwise-separable convolutions and improved MIL pooling.

## Archivist Review

Approved the core architecture concept 'Sea-Net' and the explicit open question regarding SRAM memory constraints and streaming variants for edge deployment. Rejected paper-local subcomponents and routine datasets, maintaining strict selectivity in accordance with vault policy.

### Approved Concepts
- Sea-Net: Introduces a lightweight, inherently interpretable time series classification network that balances high accuracy, temporal explanations, and minimal parameter count.

### Approved Open Questions
- Memory-Efficient Temporal Streaming Variants: Crucial for bridging the gap between lightweight model parameters (flash memory) and activation memory constraints (SRAM) on edge devices.

## Links

- [Abstract](https://arxiv.org/abs/2610.17939)
- [PDF](https://arxiv.org/pdf/2610.17939)

