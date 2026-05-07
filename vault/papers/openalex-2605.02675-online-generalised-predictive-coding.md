---
# CSL-compatible fields
title: "Online Generalised Predictive Coding"
author:
  - literal: "Mehran H. Z. Bazargani"
  - literal: "Szymon Urbas"
  - literal: "Adeel Razi"
  - literal: "Thomas Brendan Murphy"
  - literal: "Karl Friston"
issued:
  date-parts:
    - [2026, 5, 4]
url: "https://arxiv.org/abs/2605.02675"

# Custom fields
paper_id: "2605.02675"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "reinforcement-learning"
  - "inference"
architectures:
  []
datasets:
  []
concept_slugs:
  - "online-dynamic-expectation-maximisation-odem"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-07T07:38:11Z"
created_at: "2026-05-07T07:38:11Z"
---

# Online Generalised Predictive Coding

**Authors**: Mehran H. Z. Bazargani, Szymon Urbas, Adeel Razi, Thomas Brendan Murphy, Karl Friston
**Date**: 2026-05-04
**Paper ID**: [openalex:2605.02675](https://arxiv.org/abs/2605.02675)

## Summary

This paper introduces Online Dynamic Expectation Maximisation (ODEM), a data assimilation framework that extends traditional generalised filtering for online settings. By exploiting the separation of temporal scales, the method allows for fast Bayesian belief updating about hidden states while simultaneously performing slow, adaptive updates of model parameters and uncertainty. The approach is validated on non-linear and chaotic systems, demonstrating robust tracking capabilities even under model mismatch, offering a principled neuro-mimetic approach to online learning and inference.

## Key Contributions

- Extends Dynamic Expectation Maximisation (DEM) to online applications via a separation of temporal scales between fast state inference and slow parameter/precision updates.
- Provides a unified, biologically inspired framework for joint inference, learning, and uncertainty estimation in non-linear dynamic environments.
- Demonstrates the effectiveness of ODEM in tracking latent states even when the agent's model dynamics diverge from the true generative process.

## Open Questions & Future Work

- [[learnable-smoothness-matrix]]

## Key Concepts

- [[online-dynamic-expectation-maximisation-odem]]: An online variant of Dynamic Expectation Maximisation that uses temporal scale separation to simultaneously track latent states, learn parameters, and estimate uncertainty.

## Archivist Review

I approved the core ODEM framework and the specific open question regarding the learnable smoothness matrix as it addresses a structural limitation of the predictive coding approach. I rejected the non-stationary kernels candidate as it is less central to the primary contribution of the paper. Standard rigor was applied to ensure only the most reusable and fundamental concepts were added to the vault.

### Approved Concepts
- Online Dynamic Expectation Maximisation (ODEM): It provides a novel online extension of Dynamic Expectation Maximisation for joint inference, learning, and uncertainty estimation.

### Approved Open Questions
- Learnable Smoothness Matrix: Learning the smoothness matrix enables the model to automatically adapt to the temporal correlation properties of noise in the generative process, rather than relying on prior manual configuration.

### Rejected Candidates
- [open_question] Non-stationary kernels in ODEM (`non-stationary-kernels-odm`) - low_impact: While interesting, the current formulation is sufficiently distinct as a stationary-based online framework, and non-stationary extensions are too speculative to track as a fundamental open question at this stage.

## Links

- [Abstract](https://arxiv.org/abs/2605.02675)
- [PDF](https://arxiv.org/pdf/2605.02675)

