---
# CSL-compatible fields
title: "BatteryMFormer: Multi-level Learning for Battery Degradation Trajectory Forecasting"
author:
  - literal: "Ruifeng Tan"
  - literal: "Jintao Dong"
  - literal: "Wei Hong"
  - literal: "Jia Li"
  - literal: "Jiaqiang Huang"
  - literal: "Tong-Yi Zhang"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.27044"

# Custom fields
paper_id: "2605.27044"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "time-series"
  - "forecasting"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "meta-degradation-pattern-memory"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-29T08:38:09Z"
created_at: "2026-05-29T08:38:09Z"
---

# BatteryMFormer: Multi-level Learning for Battery Degradation Trajectory Forecasting

**Authors**: Ruifeng Tan, Jintao Dong, Wei Hong, Jia Li, Jiaqiang Huang, Tong-Yi Zhang
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.27044](https://arxiv.org/abs/2605.27044)

## Summary

BatteryMFormer is a multi-level Transformer architecture designed for early battery state-of-health degradation trajectory forecasting. The model utilizes a dual-view encoder to simultaneously capture temporal dynamics and SOC-localized variations, alongside an aging-condition-aware decoder and a meta degradation pattern memory for improved long-horizon prediction. Experiments on four battery degradation datasets demonstrate its superior forecasting accuracy compared to existing state-of-the-art models.

## Key Contributions

- Proposed BatteryMFormer, a multi-level Transformer architecture for early battery state-of-health degradation trajectory forecasting.
- Introduced an aging-condition-aware decoder that utilizes condition-informed queries and attention to incorporate domain-specific priors.
- Developed a dual-view encoder and meta degradation pattern memory to capture SOC-localized variations and trajectory patterns across diverse battery datasets.
- Achieved superior performance over state-of-the-art baselines across four diverse battery degradation datasets.

## Open Questions & Future Work

- [[optimal-input-sequence-length-bdtf]]
- [[bdtf-field-data-adaptation]]

## Key Concepts

- [[meta-degradation-pattern-memory]]: A memory-augmented mechanism that learns and retrieves temporal trajectory prototypes to guide long-horizon forecasting in non-stationary processes.

## Archivist Review

I approved the meta degradation pattern memory as a reusable paradigm for long-horizon forecasting and two open questions regarding sequence length optimization and field data adaptation. The remaining architectural subcomponents were rejected as they are implementation-specific modules rather than generalized concepts. I applied a strict filter to ensure only highly reusable concepts and substantial, non-boilerplate research questions were admitted.

### Approved Concepts
- Meta Degradation Pattern Memory: This component provides a retrieval-augmented approach to long-horizon time-series forecasting, specifically addressing non-stationary life-cycle degradation processes.

### Approved Open Questions
- Optimal input sequence length: Optimizing input sequence lengths is crucial for balancing model accuracy with computational constraints and data availability in real-time management systems.
- Adaptation to noisy field data: Bridging the gap between laboratory-validated prognostic models and in-the-wild deployment is essential for practical safety and diagnostics.

### Rejected Candidates
- [concept] Dual-View Encoder (`dual-view-encoder`) - subcomponent_of_broader_mechanism: This is a paper-specific architectural subcomponent that does not represent a sufficiently novel or generalized mechanism.
- [concept] Aging-Condition-Aware Decoder (`aging-condition-aware-decoder`) - subcomponent_of_broader_mechanism: This is a specific architectural module for integrating priors that is better captured as a general technique rather than a standalone concept.

## Links

- [Abstract](https://arxiv.org/abs/2605.27044)
- [PDF](https://arxiv.org/pdf/2605.27044)

