---
# CSL-compatible fields
title: "Composing Non-Conjugate Factor Graphs with Closed-Form Variational Inference"
author:
  - literal: "Mykola Lukashchuk"
  - literal: "Kyrylo Yemets"
  - literal: "Wouter M. Kouw"
  - literal: "Dmitry Bagaev"
  - literal: "İsmai̇l Şenöz"
  - literal: "Jeff Beck"
  - literal: "Bert de Vries"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.29467"

# Custom fields
paper_id: "2605.29467"
paper_source: "openalex"
domain: "nlp"
tags:
  - "bayesian-inference"
  - "variational-inference"
  - "time-series"
  - "mixture-of-experts"
  - "uncertainty-quantification"
architectures:
  []
datasets:
  []
concept_slugs:
  - "closed-form-variational-message-passing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:10:07Z"
created_at: "2026-05-31T08:10:07Z"
---

# Composing Non-Conjugate Factor Graphs with Closed-Form Variational Inference

**Authors**: Mykola Lukashchuk, Kyrylo Yemets, Wouter M. Kouw, Dmitry Bagaev, İsmai̇l Şenöz, Jeff Beck, Bert de Vries
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.29467](https://arxiv.org/abs/2605.29467)

## Summary

This paper addresses the difficulty of maintaining analytical tractability in deep probabilistic models by identifying a set of factor-graph primitives that preserve closed-form variational message passing. The authors prove that models composed from these primitives remain tractable even when introducing non-conjugate interactions through an exponential link. By demonstrating that such architectures can encode decision trees, the framework provides a path to universal function approximation within the closed-form inference paradigm. Experiments on time-series forecasting validate the approach, showing superior calibrated uncertainty over conventional expert selection methods.

## Key Contributions

- Identifies a set of five factor-graph primitives that allow for closed-form variational message passing in deep compositions.
- Proves that stacking these primitives can encode arbitrary decision trees, enabling universal function approximation with closed-form inference.
- Demonstrates a Bayesian mixture of experts for time-series forecasting where gating functions are inferred analytically, providing well-calibrated uncertainty.

## Open Questions & Future Work

- [[minimal-alphabet-for-closed-form-inference]]

## Key Concepts

- [[closed-form-variational-message-passing]]: A framework for preserving closed-form variational inference in deep, non-conjugate factor graphs through specific primitive building blocks.

## Archivist Review

I have approved the core methodological concept, 'Closed-Form Variational Message Passing', as it provides a generalizable architectural paradigm for building deep, tractable probabilistic models. The open question regarding the 'Minimal Alphabet for Inference' was approved as it targets a fundamental theoretical bottleneck in structural probabilistic modeling. Other candidates were not submitted, and no datasets were identified as central enough for individual entry.

### Approved Concepts
- Closed-Form Variational Message Passing: Enables exact analytical inference in deep probabilistic architectures, avoiding the computational overhead and variance of stochastic sampling methods.

### Approved Open Questions
- Minimal Alphabet for Inference: Identifying a minimal or optimal alphabet is technically critical for reducing the complexity of factor graph construction, minimizing the memory footprint of inference algorithms, and broadening the library of available building blocks for expressive probabilistic programming.

## Links

- [Abstract](https://arxiv.org/abs/2605.29467)
- [PDF](https://arxiv.org/pdf/2605.29467)

