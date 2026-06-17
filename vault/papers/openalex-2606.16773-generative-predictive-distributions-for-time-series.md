---
# CSL-compatible fields
title: "Generative Predictive Distributions for Time Series"
author:
  - literal: "Jordi Llorens-Terrazas"
  - literal: "Mika Meitz"
issued:
  date-parts:
    - [2026, 6, 15]
url: "https://arxiv.org/abs/2606.16773"

# Custom fields
paper_id: "2606.16773"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "generative-adversarial-network"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:25:08Z"
created_at: "2026-06-17T09:25:08Z"
---

# Generative Predictive Distributions for Time Series

**Authors**: Jordi Llorens-Terrazas, Mika Meitz
**Date**: 2026-06-15
**Paper ID**: [openalex:2606.16773](https://arxiv.org/abs/2606.16773)

## Summary

The paper proposes a simulation-based generative framework for modeling predictive distributions in nonlinear, multivariate time series. By leveraging a measure-theoretic representation, the approach enables the computation of complex quantities such as Value at Risk, Expected Shortfall, and joint tail risks. The method is formulated as a conditional generative adversarial network, with the authors establishing formal consistency of the estimation procedure under weak temporal dependence. Empirical validation on financial time series confirms the framework's effectiveness and its high computational efficiency.

## Key Contributions

- Introduces a flexible framework for modeling predictive distributions of multivariate nonlinear time series via a generative representation derived from measure-theoretic probability.
- Establishes formal statistical consistency for the proposed generative estimation method under weak temporal dependence using a minimax framework.
- Demonstrates high computational efficiency, achieving model estimation in approximately one minute on standard hardware, suitable for financial risk applications like VaR and Expected Shortfall.

## Open Questions & Future Work

- [[weak-convergence-on-unbounded-support-for-generative-forecasting]]

## Archivist Review

The paper provides a strong theoretical contribution regarding generative predictive distributions but does not propose a specific, novel architecture or module that warrants a new conceptual entry in the vault. I have approved the open question regarding weak convergence on unbounded support, as it represents a fundamental theoretical bottleneck in applying generative modeling to time series, which is a recurring research concern in this field. No specific datasets were introduced, as the paper relies on standard financial domains.

### Approved Open Questions
- Weak Convergence on Unbounded Support: This gap restricts the formal understanding of model reliability in domains where data is inherently unbounded, hindering the rigorous application of generative forecasting frameworks in real-world risk management.

## Links

- [Abstract](https://arxiv.org/abs/2606.16773)
- [PDF](https://arxiv.org/pdf/2606.16773)

