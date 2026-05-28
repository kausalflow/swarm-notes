---
# CSL-compatible fields
title: "Modeling dependence in sparse time series of Insurance Claims"
author:
  - literal: "Roberto Baviera"
  - literal: "Pietro Manzoni"
  - literal: "Michele Domenico Massaria"
issued:
  date-parts:
    - [2026, 5, 25]
url: "https://arxiv.org/abs/2605.25559"

# Custom fields
paper_id: "2605.25559"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
architectures:
  []
datasets:
  - "danish-fire-insurance-dataset"
concept_slugs:
  - "comb-bernoulli-model"
dataset_slugs:
  - "danish-fire-insurance-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-05-28T08:37:27Z"
created_at: "2026-05-28T08:37:27Z"
---

# Modeling dependence in sparse time series of Insurance Claims

**Authors**: Roberto Baviera, Pietro Manzoni, Michele Domenico Massaria
**Date**: 2026-05-25
**Paper ID**: [openalex:2605.25559](https://arxiv.org/abs/2605.25559)

## Summary

This paper addresses the difficulty of modeling dependence in sparse insurance claim time series, which traditionally rely on challenging Lévy copulas or zero-mixed models. The authors introduce the Comb-Bernoulli model, a new framework that leverages traditional copula structures to significantly improve tractability for simulation, likelihood evaluation, and parameter estimation. The approach is theoretically analyzed for the Gaussian copula case with lognormal marginals and demonstrated to be numerically efficient on the Danish fire insurance dataset.

## Key Contributions

- Proposed the Comb-Bernoulli model, a framework that integrates copula structures with zero-mixed models for sparse risk time series.
- Demonstrated that the Comb-Bernoulli model provides tractable simulation, likelihood evaluation, and parameter estimation.
- Validated the numerical efficiency and modeling utility of the approach using the Danish fire insurance dataset.

## Open Questions & Future Work

- [[asymptotic-equivalence-of-full-and-low-dimensional-copula-estimation]]

## Key Concepts

- [[comb-bernoulli-model]]: A dependence modeling framework for sparse insurance time series that combines copula structures with zero-mixed models to improve tractability in simulation and estimation.

## Archivist Review

The Comb-Bernoulli model provides a reusable, tractable framework for modeling sparse dependence, which is a significant challenge in insurance and similar domains. The open question regarding the modularity of high-dimensional copula estimation addresses a fundamental trade-off between computational tractability and statistical completeness. I have approved these as they are high-impact research contributions that move beyond routine time-series modeling.

### Approved Concepts
- Comb-Bernoulli model: It provides a novel, tractable framework for modeling dependence in sparse insurance risk time series, addressing the limitations of existing copula and zero-mixed models.

### Approved Open Questions
- Copula estimation: full vs. modular: If this conjecture holds, it would provide a theoretical foundation for modular risk aggregation, allowing practitioners to avoid the computational and statistical complexities of full multivariate calibration by using simpler, lower-dimensional building blocks.

## Datasets

- [[danish-fire-insurance-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2605.25559)
- [PDF](https://arxiv.org/pdf/2605.25559)

