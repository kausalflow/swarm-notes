---
# CSL-compatible fields
title: "SL-BiLEM: Structured Learnable Behavior-in-the-Loop Epidemic Modeling for Forecasting and Policy Evaluation"
author:
  - literal: "Haochun Wang"
  - literal: "Sendong Zhao"
  - literal: "Jingbo Wang"
  - literal: "Yanrui Du"
  - literal: "Bing Qin"
  - literal: "Ting Liu"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.26704"

# Custom fields
paper_id: "2605.26704"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "forecasting"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "behavior-informed-transmission-decomposition"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-29T08:38:29Z"
created_at: "2026-05-29T08:38:29Z"
---

# SL-BiLEM: Structured Learnable Behavior-in-the-Loop Epidemic Modeling for Forecasting and Policy Evaluation

**Authors**: Haochun Wang, Sendong Zhao, Jingbo Wang, Yanrui Du, Bing Qin, Ting Liu
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.26704](https://arxiv.org/abs/2605.26704)

## Summary

SL-BiLEM is a structured epidemic forecasting framework that addresses the challenge of human behavior-induced distribution shifts by incorporating physical constraints on a learned compliance function. By decomposing effective transmission into policy, media, and compliance factors, the model ensures robust extrapolation during novel intervention regimes. It demonstrates superior predictive performance and reliability compared to standard neural-mechanistic approaches, providing a principled tool for counterfactual policy evaluation in public health.

## Key Contributions

- Introduces SL-BiLEM, a structured epidemic modeling framework that decomposes transmission into behaviorally-informed components (policy, media, and compliance) to handle distribution shifts.
- Achieves 76% improvement in forecasting accuracy over neural-mechanistic baselines and significantly reduces OOD degradation under policy-induced shifts.
- Provides an interpretable framework for counterfactual intervention decision support, maintaining 100% bootstrap CI coverage and exceeding 0.85 treatment effect accuracy on synthetic benchmarks.

## Open Questions & Future Work

- [[behavioral-parameter-transferability-in-epidemic-forecasting,]]

## Key Concepts

- [[behavior-informed-transmission-decomposition]]: A forecasting framework that explicitly factorizes effective transmission into interpretable, physics-constrained components representing policy, media, and human behavioral compliance.

## Archivist Review

The submission proposes a novel behavioral decomposition technique for epidemic modeling. I have approved the overarching concept of 'Behavior-Informed Transmission Decomposition' instead of the model-specific name 'SL-BiLEM' to ensure greater reusability in the vault. I also approved the open question regarding the transferability of these learned behavioral parameters as it captures a fundamental limitation in applying such models to novel, sparse-data outbreak scenarios.

### Approved Concepts
- Behavior-Informed Transmission Decomposition: It provides a principled way to disentangle exogenous policy/media factors from endogenous latent behavioral compliance in epidemic forecasting, mitigating distribution shift.

### Approved Open Questions
- Behavioral Parameter Transferability: Improving the generalization of behavioral parameters is a key bottleneck for deploying epidemic models to real-world, novel outbreaks where initial data is sparse.

### Rejected Candidates
- [concept] SL-BiLEM (`sl-bilem`) - subcomponent_of_broader_mechanism: This is the specific model name; the underlying mechanism of behavior-informed decomposition is a more robust and reusable concept.

## Links

- [Abstract](https://arxiv.org/abs/2605.26704)
- [PDF](https://arxiv.org/pdf/2605.26704)

