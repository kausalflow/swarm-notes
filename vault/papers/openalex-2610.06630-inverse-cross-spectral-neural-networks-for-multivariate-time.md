---
# CSL-compatible fields
title: "Inverse Cross-spectral Neural Networks for Multivariate Time Series"
author:
  - literal: "Lorenzo Marinucci"
  - literal: "Leonardo Di Nino"
  - literal: "Gabriele D’Acunto"
  - literal: "Paolo Di Lorenzo"
  - literal: "Sergio Barbarossa"
issued:
  date-parts:
    - [2026, 10, 5]
url: "https://arxiv.org/abs/2610.06630"

# Custom fields
paper_id: "2610.06630"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "graph-neural-network"
  - "forecasting"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "inverse-cross-spectral-neural-networks"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-08T11:40:42Z"
created_at: "2026-10-08T11:40:42Z"
---

# Inverse Cross-spectral Neural Networks for Multivariate Time Series

**Authors**: Lorenzo Marinucci, Leonardo Di Nino, Gabriele D’Acunto, Paolo Di Lorenzo, Sergio Barbarossa
**Date**: 2026-10-05
**Paper ID**: [openalex:2610.06630](https://arxiv.org/abs/2610.06630)

## Summary

This paper introduces Inverse Cross-Spectral Neural Networks (iCSNNs), a novel class of graph neural networks designed for stationary multivariate time series that utilize inverse cross-spectral density matrices as graph shift operators to capture frequency-specific conditional dependencies. By leveraging spectral smoothness, the model groups frequencies into bands sharing a single operator for compact parameterization and employs a joint learning procedure to estimate dependence structures and network weights simultaneously. Evaluation on synthetic data demonstrates superior performance compared to existing methodological baselines.

## Key Contributions

- Introduces Inverse Cross-Spectral Neural Networks (iCSNNs) for modeling stationary multivariate time series using inverse cross-spectral density (iCSD) matrices as graph shift operators.
- Utilizes spectral smoothness to group frequencies into shared bands, yielding a compact parametrization of frequency-dependent relationships.
- Proposes a joint learning procedure to simultaneously estimate the Fourier-domain dependence structure and network parameters for downstream tasks.

## Open Questions & Future Work

- [[length-transferability-of-inverse-cross-spectral-neural-networks]]

## Key Concepts

- [[inverse-cross-spectral-neural-networks]]: A class of graph neural networks for stationary multivariate time series using inverse cross-spectral density matrices as shift operators to capture frequency-specific conditional relationships.

## Archivist Review

Approved the core concept of Inverse Cross-Spectral Neural Networks as a distinct spectral graph shift operator architecture for multivariate time series, along with its specific open question on length-transferability. No datasets met the criteria for permanent vault inclusion.

### Approved Concepts
- Inverse Cross-Spectral Neural Networks: Introduces a novel graph neural network architecture specifically tailored for multivariate time series using inverse cross-spectral density matrices as shift operators.

### Approved Open Questions
- Length-Transferability of Inverse Cross-Spectral Neural Networks: Evaluating length-transferability is crucial for understanding whether graph neural networks operating in the spectral domain can maintain robust predictive performance across varying temporal observation windows without retraining.

## Links

- [Abstract](https://arxiv.org/abs/2610.06630)
- [PDF](https://arxiv.org/pdf/2610.06630)

