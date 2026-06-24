---
# CSL-compatible fields
title: "Multi-Modal Bayesian Neural Network Surrogates with Conjugate Last-Layer Estimation"
author:
  - literal: "Ian Taylor"
  - literal: "Juliane Mueller"
  - literal: "Julie Bessac"
issued:
  date-parts:
    - [2026, 6, 21]
url: "https://arxiv.org/abs/2509.21711"

# Custom fields
paper_id: "2509.21711"
paper_source: "openalex"
domain: "nlp"
tags:
  - "bayesian-neural-network"
  - "multimodal"
  - "surrogate-modeling"
  - "variational-inference"
  - "uncertainty-quantification"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "conjugate-last-layer-estimation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-24T08:17:33Z"
created_at: "2026-06-24T08:17:33Z"
---

# Multi-Modal Bayesian Neural Network Surrogates with Conjugate Last-Layer Estimation

**Authors**: Ian Taylor, Juliane Mueller, Julie Bessac
**Date**: 2026-06-21
**Paper ID**: [openalex:2509.21711](https://arxiv.org/abs/2509.21711)

## Summary

This paper introduces multi-modal Bayesian neural network surrogates designed to integrate diverse data sources for expensive quantity-of-interest modeling. The approach employs conditionally conjugate distributions in the last layer to facilitate efficient parameter estimation via stochastic variational inference. Furthermore, it addresses the challenge of missing data by incorporating a robust estimation method, demonstrating superior performance in both predictive accuracy and uncertainty quantification compared to uni-modal alternatives.

## Key Contributions

- Proposed two multi-modal Bayesian neural network surrogate models utilizing conjugate last-layer estimation.
- Developed a stochastic variational inference method that accommodates partially missing observations in multi-modal data.
- Achieved improved prediction accuracy and uncertainty quantification over uni-modal baselines for scalar and time-series benchmarks.

## Open Questions & Future Work

- [[multi-modal-acquisition-framework-bo]]
- [[non-linear-performance-diagnostics]]

## Key Concepts

- [[conjugate-last-layer-estimation]]: A method for estimating parameters in Bayesian neural network surrogates using conditionally conjugate distributions in the last layer for stochastic variational inference.

## Archivist Review

The paper presents a clear method for efficient Bayesian inference via conjugate last-layer estimation, which is a reusable architectural technique. The open questions regarding acquisition frameworks and modality performance diagnostics are substantive, representing key bottlenecks for the practical deployment of multi-modal surrogate models. No datasets were approved as none were cited as primary, novel, or unique contributions of the work.

### Approved Concepts
- Conjugate Last-Layer Estimation: Enables efficient Bayesian inference in neural network surrogates by leveraging conjugacy in the final layer.

### Approved Open Questions
- Multi-modal Bayesian Optimization Framework: The effectiveness of surrogate models in Bayesian Optimization is fundamentally tied to their ability to guide sampling; without a corresponding acquisition function, the surrogate models are limited in their practical utility for optimization tasks.
- Non-linear Multi-modal Performance Diagnostics: Predictive diagnostics for multi-modal model performance are critical for practitioners to decide whether the overhead of multi-modal data collection and modeling is justified in a specific application.

## Links

- [Abstract](https://arxiv.org/abs/2509.21711)
- [PDF](https://arxiv.org/pdf/2509.21711)

