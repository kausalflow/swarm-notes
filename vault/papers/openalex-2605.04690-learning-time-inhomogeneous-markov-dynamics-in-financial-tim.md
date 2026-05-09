---
# CSL-compatible fields
title: "Learning Time-Inhomogeneous Markov Dynamics in Financial Time Series via Neural Parameterization"
author:
  - literal: "Jan Rovirosa"
  - literal: "Jesse Schmolze"
issued:
  date-parts:
    - [2026, 5, 6]
url: "https://arxiv.org/abs/2605.04690"

# Custom fields
paper_id: "2605.04690"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "interpretability"
  - "stochastic-process"
architectures:
  []
datasets:
  []
concept_slugs:
  - "neural-parameterized-markov-transition-operators"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-09T07:01:59Z"
created_at: "2026-05-09T07:01:59Z"
---

# Learning Time-Inhomogeneous Markov Dynamics in Financial Time Series via Neural Parameterization

**Authors**: Jan Rovirosa, Jesse Schmolze
**Date**: 2026-05-06
**Paper ID**: [openalex:2605.04690](https://arxiv.org/abs/2605.04690)

## Summary

This paper addresses the challenge of modeling non-stationary stochastic systems by using neural networks to parameterize time-varying Markov transition matrices. By forcing the neural output to adhere to the requirements of a stochastic operator, the model preserves mathematical transparency while overcoming the data sparsity issues that plague empirical estimation. The framework demonstrates effectiveness in capturing complex regime shifts in financial data and introduces a diagnostic approach using Chapman-Kolmogorov equations to identify deviations from Markovian assumptions.

## Key Contributions

- Introduces a framework that uses neural networks to parameterize time-varying Markov transition matrices while maintaining strict structural interpretability.
- Demonstrates the capture of complex regime shifts in financial time series, with row entropy of learned operators showing a strong negative correlation (r = -0.62) with realized variance.
- Repurposes the Chapman-Kolmogorov equations as a diagnostic tool for identifying temporal windows where first-order memory assumptions fail.

## Open Questions & Future Work

- [[continuous-time-neural-operator-formulations]]

## Key Concepts

- [[neural-parameterized-markov-transition-operators]]: A framework that constrains neural networks to output formal stochastic transition operators, ensuring both high representational power and structural interpretability.

## Archivist Review

The concept of Neural Parameterized Markov Transition Operators is approved as a central, reusable architectural idea for combining deep learning with structural stochastic models. The open question on continuous-time extensions is approved as it addresses a fundamental limitation in applying discrete-time Markovian models to irregular, high-frequency temporal data. The multi-asset scaling question was rejected as it effectively amounts to a 'more data/complexity' request rather than a structural or theoretical bottleneck.

### Approved Concepts
- Neural Parameterized Markov Transition Operators: Provides a novel way to bridge deep learning and classical stochastic control by forcing neural network outputs to satisfy the mathematical requirements of a transition operator.

### Approved Open Questions
- Continuous-time operator extensions: Continuous-time formulations are theoretically better suited for handling high-frequency data and irregular sampling, which are pervasive in complex stochastic processes.

## Links

- [Abstract](https://arxiv.org/abs/2605.04690)
- [PDF](https://arxiv.org/pdf/2605.04690)

