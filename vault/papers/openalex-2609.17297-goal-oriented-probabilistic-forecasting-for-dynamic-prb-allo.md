---
# CSL-compatible fields
title: "Goal-oriented probabilistic forecasting for dynamic PRB allocation in 5G networks"
author:
  - literal: "Oier Larumbe-Lizarraga"
  - literal: "Roberto Pereira"
  - literal: "Cristian J. Vaca-Rubio"
issued:
  date-parts:
    - [2026, 9, 15]
url: "https://arxiv.org/abs/2609.17297"

# Custom fields
paper_id: "2609.17297"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "uncertainty-estimation"
architectures:
  - "encoder-decoder"
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "goal-oriented-probabilistic-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:44:15Z"
created_at: "2026-09-17T09:44:15Z"
---

# Goal-oriented probabilistic forecasting for dynamic PRB allocation in 5G networks

**Authors**: Oier Larumbe-Lizarraga, Roberto Pereira, Cristian J. Vaca-Rubio
**Date**: 2026-09-15
**Paper ID**: [openalex:2609.17297](https://arxiv.org/abs/2609.17297)

## Summary

This paper introduces a goal-oriented probabilistic forecasting framework for dynamic physical resource block (PRB) allocation in 5G networks, replacing traditional symmetric error minimization (like MAE or RMSE) with asymmetric loss functions aligned with operational costs. By training models such as DeepAR and Temporal Fusion Transformer (TFT) using Pinball Loss and deriving optimal allocation quantiles from cost matrices, the approach effectively balances service reliability against resource efficiency. Evaluation on a real beam-level 5G traffic dataset proves that this decision-aligned framework significantly reduces operational costs compared to standard mean-squared-error baselines while preserving reliable uncertainty calibration.

## Key Contributions

- Proposes a goal-oriented probabilistic forecasting framework for dynamic Physical Resource Block (PRB) allocation in 5G networks, aligning model training with operator cost asymmetry.
- Derives optimal allocation quantiles from operator cost matrices using Pinball Loss for DeepAR and Temporal Fusion Transformer (TFT) architectures.
- Demonstrates operational cost reduction over MSE-trained baselines on a real beam-level 5G traffic dataset while maintaining calibrated uncertainty estimates.

## Open Questions & Future Work

- [[multi-cell-online-quantile-adaptation]]

## Key Concepts

- [[goal-oriented-probabilistic-forecasting]]: A forecasting framework that trains models with asymmetric loss functions and cost matrices to optimize resource allocation decisions.

## Archivist Review

Approved the overarching concept of goal-oriented probabilistic forecasting as a reusable decision-aligned paradigm and an open question on multi-cell online adaptation. Rejected internal model-specific combinations as routine subcomponents.

### Approved Concepts
- Goal-oriented Probabilistic Forecasting: Presents a core methodology for aligning time-series forecasting training directly with downstream operational cost asymmetries.

### Approved Open Questions
- Multi-Cell and Online Quantile Adaptation: Extending single-cell resource allocation frameworks to multi-cell settings and enabling online adaptation are critical steps for deploying decision-focused learning and goal-oriented forecasting in dynamic, large-scale cellular networks.

### Rejected Candidates
- [concept] DeepAR and TFT with Pinball Loss (`deepar-tft-pinball-loss`) - subcomponent_of_broader_mechanism: Subcomponent implementation detail combining existing models with a standard loss function.

## Links

- [Abstract](https://arxiv.org/abs/2609.17297)
- [PDF](https://arxiv.org/pdf/2609.17297)

