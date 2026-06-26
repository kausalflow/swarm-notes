---
# CSL-compatible fields
title: "Uncertainty-Aware Longitudinal Forecasting of Alzheimer's Disease Progression Using Deep Learning"
author:
  - literal: "Arya Hariharan"
  - literal: "Shreyank N Gowda"
  - literal: "M R Anala"
issued:
  date-parts:
    - [2026, 6, 23]
url: "https://arxiv.org/abs/2606.24604"

# Custom fields
paper_id: "2606.24604"
paper_source: "openalex"
domain: "medicine"
tags:
  - "transformer"
  - "language-model"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  - "adni"
  - "oasis-3"
concept_slugs:
  - "decomposed-uncertainty-estimation"
dataset_slugs:
  - "adni"
  - "oasis-3"
skill: "TimeSeriesSkill"
processed_at: "2026-06-26T08:25:22Z"
created_at: "2026-06-26T08:25:22Z"
---

# Uncertainty-Aware Longitudinal Forecasting of Alzheimer's Disease Progression Using Deep Learning

**Authors**: Arya Hariharan, Shreyank N Gowda, M R Anala
**Date**: 2026-06-23
**Paper ID**: [openalex:2606.24604](https://arxiv.org/abs/2606.24604)

## Summary

This paper presents a probabilistic framework for longitudinal Alzheimer's disease forecasting that combines ordinal diagnosis prediction with multi-horizon trajectory generation. By adapting a Temporal Fusion Transformer with a CORAL layer and asymmetric loss, the model improves transition sensitivity between disease stages while providing credible uncertainty estimates. Evaluation on ADNI and OASIS-3 datasets demonstrates superior diagnostic accuracy and consistent uncertainty decomposition, providing both reliable patient evolution insights and epistemic signals for rare progression archetypes.

## Key Contributions

- Introduces a probabilistic framework that integrates ordinal classification with multi-horizon trajectory generation for Alzheimer's disease progression.
- Adapts a Temporal Fusion Transformer with a CORAL layer and asymmetric loss to significantly improve MCI-to-dementia transition sensitivity.
- Demonstrates that decomposed uncertainty estimation effectively captures model confidence, with epistemic uncertainty scaling with prediction errors on the OASIS-3 external benchmark.

## Open Questions & Future Work

- [[mitigating-time-to-conversion-bias]]
- [[modeling-diagnostic-reversals]]

## Key Concepts

- [[decomposed-uncertainty-estimation]]: A methodology for isolating aleatoric from epistemic uncertainty within probabilistic time-series forecasting models.

## Archivist Review

The paper proposes a robust approach for longitudinal clinical forecasting by integrating ordinal classification, trajectory generation, and uncertainty decomposition. Decomposed uncertainty estimation is approved for its general utility in reliability-critical forecasting tasks. The two open questions are approved as they address significant, identified limitations regarding selection bias in longitudinal training data and the clinical validity of rigid monotonicity constraints. The datasets ADNI and OASIS-3 are approved as standard benchmarks for this domain.

### Approved Concepts
- Decomposed uncertainty estimation: Addresses the critical need to distinguish between aleatoric and epistemic uncertainty in high-stakes longitudinal medical forecasting.

### Approved Open Questions
- Mitigating Time-to-Conversion Bias: Addressing this bias is critical for the clinical reliability of longitudinal models, preventing overestimation of disease progression speeds.
- Modeling Diagnostic Reversals: Strict monotonicity constraints may limit the clinical realism of forecasting models in cases where genuine diagnostic reversals occur.

## Datasets

- [[adni]]
- [[oasis-3]]

## Links

- [Abstract](https://arxiv.org/abs/2606.24604)
- [PDF](https://arxiv.org/pdf/2606.24604)

