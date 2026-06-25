---
# CSL-compatible fields
title: "Learning the distance for ABC and localized neural posterior estimation"
author:
  - literal: "Yuyan Wang"
  - literal: "David J.Nott"
issued:
  date-parts:
    - [2026, 6, 22]
url: "https://arxiv.org/abs/2606.22981"

# Custom fields
paper_id: "2606.22981"
paper_source: "openalex"
domain: "nlp"
tags:
  - "bayesian-inference"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "adaptive-distance-learning-for-likelihood-free-inference"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-25T08:19:45Z"
created_at: "2026-06-25T08:19:45Z"
---

# Learning the distance for ABC and localized neural posterior estimation

**Authors**: Yuyan Wang, David J.Nott
**Date**: 2026-06-22
**Paper ID**: [openalex:2606.22981](https://arxiv.org/abs/2606.22981)

## Summary

This paper advances likelihood-free inference by developing adaptive distance learning techniques for Approximate Bayesian Computation (ABC) and neural posterior estimation. The authors propose optimizing distance functions based on out-of-sample predictive performance using scoring rules, specifically addressing challenges in misspecified time series models. Furthermore, the work identifies a formal connection between forecast combination via linear pooling and randomized distance-based posterior estimation, providing a unified framework for improving predictive accuracy in simulated and real-world scenarios.

## Key Contributions

- Extends adaptive distance learning for Approximate Bayesian Computation (ABC) to handle misspecified time series models.
- Integrates adaptive distance learning into Neural Posterior Estimation with Prior-Data Fitted Networks (NPE-PFN) utilizing localized posterior approximations.
- Establishes a theoretical link between linear pooling for forecast combination and posterior estimation using randomized distances, enabling empirical optimization of pooling weights.

## Open Questions & Future Work

- [[sequential-npe-distance-learning-integration]]

## Key Concepts

- [[adaptive-distance-learning-for-likelihood-free-inference]]: A method for optimizing distance metrics in Approximate Bayesian Computation and neural posterior estimation by maximizing out-of-sample predictive performance via scoring rules.

## Archivist Review

The paper presents a novel approach to likelihood-free inference by framing distance function calibration as an optimization problem tied to predictive performance. I have approved 'Adaptive Distance Learning for Likelihood-Free Inference' as a central concept and identified the integration with sequential NPE as a significant open research bottleneck. No datasets were approved as none were presented as distinct, reusable contributions.

### Approved Concepts
- Adaptive Distance Learning for Likelihood-Free Inference: Provides a generalized, performance-driven method for calibrating likelihood-free inference, especially in misspecified regimes where traditional metrics fail.

### Approved Open Questions
- Distance learning in sequential NPE: Sequential methods are crucial for scaling likelihood-free inference; solving this integration would enable robust, computationally efficient Bayesian forecasting for complex misspecified models.

## Links

- [Abstract](https://arxiv.org/abs/2606.22981)
- [PDF](https://arxiv.org/pdf/2606.22981)

