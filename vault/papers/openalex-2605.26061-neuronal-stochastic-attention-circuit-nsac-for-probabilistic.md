---
# CSL-compatible fields
title: "Neuronal Stochastic Attention Circuit (NSAC) for Probabilistic Representation Learning"
author:
  - literal: "Waleed Razzaq"
  - literal: "Yun-Bo Zhao"
issued:
  date-parts:
    - [2026, 5, 25]
url: "https://arxiv.org/abs/2605.26061"

# Custom fields
paper_id: "2605.26061"
paper_source: "openalex"
domain: "nlp"
tags:
  - "attention-mechanism"
  - "time-series"
  - "uncertainty-estimation"
  - "stochastic-differential-equation"
  - "probabilistic-representation-learning"
  - "long-context"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "neuronal-stochastic-attention-circuit-nsac"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-28T08:38:31Z"
created_at: "2026-05-28T08:38:31Z"
---

# Neuronal Stochastic Attention Circuit (NSAC) for Probabilistic Representation Learning

**Authors**: Waleed Razzaq, Yun-Bo Zhao
**Date**: 2026-05-25
**Paper ID**: [openalex:2605.26061](https://arxiv.org/abs/2605.26061)

## Summary

The Neuronal Stochastic Attention Circuit (NSAC) is a biologically-inspired continuous-time attention architecture that integrates Ornstein-Uhlenbeck stochastic differential equations to compute attention logits. By using input-dependent gates derived from C. elegans neural circuitry, the model propagates principled stochasticity through the attention mechanism to yield probabilistic outputs. A dual-objective function, combining Gaussian negative log-likelihood with an epistemic-separation regularizer, allows the framework to jointly quantify aleatoric and epistemic uncertainty. The approach demonstrates effective calibration and interpretability across various continuous-time learning tasks and control applications.

## Key Contributions

- Introduces NSAC, a continuous-time attention architecture that utilizes Ornstein-Uhlenbeck processes and NCP-inspired gating to produce probabilistic representations.
- Implements a dual-objective function that enables the simultaneous decomposition and quantification of aleatoric and epistemic uncertainty.
- Demonstrates competitive performance in accuracy and uncertainty calibration across diverse domains, including multivariate regression, irregular time-series forecasting, and autonomous vehicle control.

## Open Questions & Future Work

- [[stochastic-ct-dynamics-efficiency-tradeoff]]

## Key Concepts

- [[neuronal-stochastic-attention-circuit-nsac]]: A continuous-time attention mechanism that models attention logits as solutions to Ornstein-Uhlenbeck SDEs with biologically-inspired gating for robust uncertainty quantification.

## Archivist Review

I approved the NSAC concept as a novel, reusable architecture for uncertainty-aware continuous-time attention. I also approved the identified open question regarding the efficiency-fidelity trade-off in stochastic continuous-time dynamics, as it addresses a core bottleneck in real-time, high-fidelity uncertainty estimation. I adhered to a selective policy, rejecting generic terms and ensuring the approved items represent significant, research-grade contributions.

### Approved Concepts
- Neuronal Stochastic Attention Circuit (NSAC): Introduces a novel paradigm for uncertainty-aware continuous-time attention using stochastic differential equations and biologically-inspired gating.

### Approved Open Questions
- Stochasticity in Non-Stationary Dynamics: This identifies a fundamental trade-off between computational efficiency and the theoretical fidelity of the SDE formulation, which is critical for real-time safety-critical applications.

## Links

- [Abstract](https://arxiv.org/abs/2605.26061)
- [PDF](https://arxiv.org/pdf/2605.26061)

