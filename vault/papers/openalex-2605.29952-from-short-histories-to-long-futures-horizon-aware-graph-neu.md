---
# CSL-compatible fields
title: "From Short Histories to Long Futures: Horizon-Aware Graph Neural Networks for Long Horizon Forecasting"
author:
  - literal: "Zesheng Liu"
  - literal: "Maryam Rahnemoonfar"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.29952"

# Custom fields
paper_id: "2605.29952"
paper_source: "openalex"
domain: "time-series"
tags:
  - "graph-neural-network"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "horizon-aware-graph-neural-networks"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:09:59Z"
created_at: "2026-05-31T08:09:59Z"
---

# From Short Histories to Long Futures: Horizon-Aware Graph Neural Networks for Long Horizon Forecasting

**Authors**: Zesheng Liu, Maryam Rahnemoonfar
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.29952](https://arxiv.org/abs/2605.29952)

## Summary

This paper addresses the challenge of long-range geophysical forecasting, where autoregressive models often suffer from error accumulation and instability. The authors propose a multi-horizon graph neural network that represents spatial domains as graphs and learns to predict multiple future lead times within a unified model. By utilizing a shared backbone with variable-specific output branches and a coarse-to-fine rollout inference scheme, the method significantly improves the reliability of long-term predictions for glacier dynamics compared to standard autoregressive baselines.

## Key Contributions

- Introduces a multi-horizon graph neural network emulator that learns state-to-state transitions for multiple lead times in a unified model, mitigating error accumulation found in one-step autoregressive surrogates.
- Implements a coarse-to-fine inference strategy using adaptive temporal jumps to reduce drift and computational redundancy during long-range predictions.
- Demonstrates superior stability and long-range accuracy on multi-decadal Pine Island Glacier simulations compared to direct initial-state prediction and standard autoregressive rollout baselines.

## Open Questions & Future Work

- [[optimal-horizon-set-selection-strategy]]

## Key Concepts

- [[horizon-aware-graph-neural-networks]]: A multi-horizon graph neural network that learns state-to-state transitions directly from current input to multiple future lead times in a unified model.

## Archivist Review

The paper provides a structured approach to mitigating error accumulation in long-term geophysical forecasting by moving away from strictly autoregressive rollouts. I approved the proposed 'Horizon-Aware Graph Neural Network' as a reusable pattern and 'Optimal Horizon Set Selection' as a substantive open research problem. Other candidates were not submitted, so no rejections were necessary.

### Approved Concepts
- Horizon-Aware Graph Neural Networks: The central method proposes a multi-horizon forecasting approach that addresses the instability of standard autoregressive rollouts in long-range geophysical modeling.

### Approved Open Questions
- Optimal Horizon Set Selection: The selection of horizon sets directly impacts both computational cost and prediction quality, and understanding how to systematically choose these sets is essential for scaling to more complex systems.

## Links

- [Abstract](https://arxiv.org/abs/2605.29952)
- [PDF](https://arxiv.org/pdf/2605.29952)

