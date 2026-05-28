---
# CSL-compatible fields
title: "Exponential mixing properties of nonlinear functional autoregressive models"
author:
  - literal: "Shuntarou Suzuki"
  - literal: "Yoshikazu Terada"
issued:
  date-parts:
    - [2026, 5, 25]
url: "https://arxiv.org/abs/2605.25633"

# Custom fields
paper_id: "2605.25633"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "nonlinear-functional-autoregressive-nfar-models"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-28T08:38:10Z"
created_at: "2026-05-28T08:38:10Z"
---

# Exponential mixing properties of nonlinear functional autoregressive models

**Authors**: Shuntarou Suzuki, Yoshikazu Terada
**Date**: 2026-05-25
**Paper ID**: [openalex:2605.25633](https://arxiv.org/abs/2605.25633)

## Summary

This paper investigates the theoretical foundations of nonlinear functional autoregressive (NFAR) models, which are increasingly relevant in operator learning for functional time series. The authors establish sufficient conditions for these models to be exponentially mixing, providing a rigorous basis for analyzing their statistical properties. Furthermore, they apply these theoretical results to derive convergence rates for adaptive neural network estimators in the context of NFAR models with Urysohn operators.

## Key Contributions

- Derived sufficient conditions for nonlinear functional autoregressive (NFAR) models to exhibit exponential mixing properties.
- Demonstrated that models utilizing Hammerstein operators satisfy the derived conditions for exponential mixing.
- Established convergence rates for adaptive estimators based on deep neural networks when applied to NFAR models with Urysohn operators.

## Open Questions & Future Work

- [[nfars-mixing-noise-discrete-data]]

## Key Concepts

- [[nonlinear-functional-autoregressive-nfar-models]]: A class of time-series models that map past functional observations to future states using nonlinear operators, often approximated by deep neural networks.

## Archivist Review

I have approved the core model category (NFAR) and the primary theoretical open question concerning its discretization and noise robustness. These items are fundamental to the paper's contribution and are framed as reusable concepts in functional time series theory, rather than local implementation details. No datasets were included in the paper analysis, so none were approved.

### Approved Concepts
- Nonlinear Functional Autoregressive (NFAR) Models: NFAR models represent a critical bridge between functional data analysis and modern operator learning, providing a formal language for functional time series that deserves standalone tracking.

### Approved Open Questions
- Exponential mixing and discretization in NFAR: These limitations directly impede the application of high-level functional theory to real-world data, which is essentially discrete and rarely Gaussian.

## Links

- [Abstract](https://arxiv.org/abs/2605.25633)
- [PDF](https://arxiv.org/pdf/2605.25633)

