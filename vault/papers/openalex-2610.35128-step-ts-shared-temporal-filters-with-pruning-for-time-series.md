---
# CSL-compatible fields
title: "STeP-TS: Shared Temporal Filters with Pruning for Time Series"
author:
  - literal: "Hanne Raum"
  - literal: "Jasper Hoffmann"
  - literal: "Joschka Boedecker"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.35128"

# Custom fields
paper_id: "2610.35128"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "model-compression"
  - "pruning"
  - "convolutional-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "step-ts"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-29T11:10:14Z"
created_at: "2026-10-29T11:10:14Z"
---

# STeP-TS: Shared Temporal Filters with Pruning for Time Series

**Authors**: Hanne Raum, Jasper Hoffmann, Joschka Boedecker
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.35128](https://arxiv.org/abs/2610.35128)

## Summary

The paper introduces STeP-TS, a compact one-layer convolutional framework for multivariate time series forecasting that balances shared multi-scale temporal dynamics and variable-specific characteristics using a shared filter bank and lightweight scalar weights. It incorporates an amplitude-adaptive normalization mechanism and leverages filter-output energy for structured pruning to lower computational complexity. Extensive experiments show that STeP-TS achieves competitive accuracy with significantly fewer parameters, FLOPs, and lower latency than existing state-of-the-art models.

## Key Contributions

- Proposes STeP-TS, a compact one-layer convolutional forecasting framework using a shared bank of multi-scale temporal filters with lightweight variable-specific scalar weights.
- Introduces a natural structured pruning signal derived from learned weights and filter-output energy to reduce computational complexity.
- Presents an amplitude-adaptive normalization mechanism that preserves variable-dependent temporal amplitudes during forecasting.
- Demonstrates competitive forecasting performance against state-of-the-art baselines across multiple datasets with substantially fewer parameters and inference FLOPs.

## Open Questions & Future Work

- [[temporal-filter-interpretability]]

## Key Concepts

- [[step-ts]]: A compact one-layer convolutional time series forecasting framework featuring shared multi-scale temporal filters, variable-specific scalar weights, and structured pruning.

## Archivist Review

Approved the core 'STeP-TS' framework concept because it presents a distinctive and reusable combination of shared multi-scale temporal filtering and energy-based structured pruning for time series forecasting. Also approved the open question regarding the interpretability of shared temporal filters as it addresses a genuine structural bottleneck in compact model attribution. All routine dataset mentions and minor helper descriptions were excluded to maintain vault scarcity.

### Approved Concepts
- STeP-TS: It introduces a novel shared temporal filter bank with lightweight variable-specific scalar weights and structured pruning for compact multivariate time series forecasting.

### Approved Open Questions
- Interpretability of Shared Temporal Filters: Understanding feature-specific weights and filter importance scores bridges the gap between compact time-series architectures and model explainability, providing insights into which temporal scales matter for specific variables.

## Links

- [Abstract](https://arxiv.org/abs/2610.35128)
- [PDF](https://arxiv.org/pdf/2610.35128)

