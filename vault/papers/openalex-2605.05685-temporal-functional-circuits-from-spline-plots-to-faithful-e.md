---
# CSL-compatible fields
title: "Temporal Functional Circuits: From Spline Plots to Faithful Explanations in KAN Forecasting"
author:
  - literal: "Naveen Mysore"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.05685"

# Custom fields
paper_id: "2605.05685"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "interpretability"
  - "explainability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "temporal-functional-circuits"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:21:16Z"
created_at: "2026-05-10T07:21:16Z"
---

# Temporal Functional Circuits: From Spline Plots to Faithful Explanations in KAN Forecasting

**Authors**: Naveen Mysore
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.05685](https://arxiv.org/abs/2605.05685)

## Summary

This paper introduces Temporal Functional Circuits, a framework designed to make Kolmogorov-Arnold Networks (KANs) interpretable for time-series forecasting. By utilizing a gated residual architecture that separates a linear baseline from a sparse KAN correction, the method allows for the systematic mapping and validation of learned edge functions through intervention analysis. Empirical results demonstrate that this approach offers significant improvements over linear models in complex, regime-switching scenarios while remaining competitive with standard transformer and MLP architectures.

## Key Contributions

- Introduced Temporal Functional Circuits, a framework that enables faithful, temporally grounded explanations for KAN-based time-series models.
- Proposed a gated residual KAN architecture that decomposes forecasts into a linear base and a sparsely activated spline-based KAN correction.
- Achieved 59% lower MSE than linear-only models on regime-switching signals and showed competitiveness with standard baselines across eight time-series benchmarks.

## Open Questions & Future Work

- [[adaptive-gate-regularization-kan]]

## Key Concepts

- [[temporal-functional-circuits]]: A framework that transforms Kolmogorov-Arnold Network edge functions into faithful, temporally grounded explanations for time-series forecasting through mapping edges to input lags and validating them via interventions.

## Archivist Review

I have approved the core concept 'Temporal Functional Circuits' as it establishes a novel bridge between KAN interpretability and time-series forecasting, and the 'Adaptive Gate Regularization' open question because it addresses a fundamental limitation in the scalability of gated neural architectures. Other aspects of the paper were deemed either too narrow or subcomponents of these overarching frameworks.

### Approved Concepts
- Temporal Functional Circuits: It provides a formal mechanism for transforming the inherent edge functions of Kolmogorov-Arnold Networks into interpretable, temporally-grounded components, facilitating mechanistic understanding in time-series forecasting.

### Approved Open Questions
- Adaptive Gate Regularization in KANs: Automating the regularization of gating mechanisms is essential for the practical deployment of gated architectures across diverse, unseen data regimes without tedious per-dataset hyperparameter tuning.

## Links

- [Abstract](https://arxiv.org/abs/2605.05685)
- [PDF](https://arxiv.org/pdf/2605.05685)

