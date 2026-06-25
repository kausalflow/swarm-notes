---
# CSL-compatible fields
title: "Interpretable Kolmogorov-Arnold Network with Feature-Isolated Temporal Attention Mechanism for Electricity Load Forecasting"
author:
  - literal: "Jinhao Li"
  - literal: "Hao Wang"
issued:
  date-parts:
    - [2026, 6, 22]
url: "https://arxiv.org/abs/2606.23425"

# Custom fields
paper_id: "2606.23425"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "loadkan"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-25T08:19:33Z"
created_at: "2026-06-25T08:19:33Z"
---

# Interpretable Kolmogorov-Arnold Network with Feature-Isolated Temporal Attention Mechanism for Electricity Load Forecasting

**Authors**: Jinhao Li, Hao Wang
**Date**: 2026-06-22
**Paper ID**: [openalex:2606.23425](https://arxiv.org/abs/2606.23425)

## Summary

This paper proposes LoadKAN, a hybrid framework designed to address the lack of interpretability in deep learning-based electricity load forecasting. By integrating a feature-isolated temporal attention mechanism with Kolmogorov-Arnold Network (KAN) modules, the model independently processes input features to extract temporal dynamics before performing interpretable non-linear mapping. LoadKAN achieves competitive performance against state-of-the-art benchmarks while allowing for granular quantitative sensitivity analysis of complex market-specific dependencies.

## Key Contributions

- Introduces LoadKAN, a hybrid architecture combining a feature-isolated temporal attention mechanism with Kolmogorov-Arnold Network (KAN) modules for electricity load forecasting.
- Enables granular analysis of non-linear dependencies between exogenous features (like mobility) and load, which remain opaque in standard black-box neural networks.
- Demonstrates state-of-the-art predictive performance on three representative U.S. electricity market datasets while providing superior interpretability compared to standard deep learning baselines.

## Open Questions & Future Work

- [[modeling-exogenous-feature-interdependencies-in-interpretable-forecasting]]

## Key Concepts

- [[loadkan]]: A hybrid and interpretable forecasting framework that integrates a feature-isolated temporal attention mechanism with Kolmogorov-Arnold Network modules.

## Archivist Review

The LoadKAN framework was approved as it proposes a specific design pattern (separating feature-isolated temporal attention before a KAN mapping layer) that is likely to be reused in interpretable time-series tasks. The open question regarding exogenous feature interdependencies was generalized and approved, as the initial candidate was too narrow to the paper's specific use case of 'mobility' features. All other concepts and questions were rejected as they either represented local implementation subcomponents or were overly tied to the paper's specific scope.

### Approved Concepts
- LoadKAN: It serves as a novel framework integrating KANs with time-series feature dynamics to balance interpretability and accuracy.

### Approved Open Questions
- Modeling Exogenous Feature Interdependencies: Capturing complex, real-world correlations between multiple exogenous drivers is critical for improving the realism and accuracy of interpretable forecasting models.

## Links

- [Abstract](https://arxiv.org/abs/2606.23425)
- [PDF](https://arxiv.org/pdf/2606.23425)

