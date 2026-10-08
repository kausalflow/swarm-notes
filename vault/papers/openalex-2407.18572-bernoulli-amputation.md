---
# CSL-compatible fields
title: "Bernoulli amputation"
author:
  - literal: "Marius Hofert"
  - literal: "J R Jackson"
  - literal: "Niels Hagenbuch"
  - literal: "Niels Hagenbuch"
issued:
  date-parts:
    - [2026, 10, 6]
url: "https://arxiv.org/abs/2407.18572"

# Custom fields
paper_id: "2407.18572"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
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
processed_at: "2026-10-08T11:41:55Z"
created_at: "2026-10-08T11:41:55Z"
---

# Bernoulli amputation

**Authors**: Marius Hofert, J R Jackson, Niels Hagenbuch, Niels Hagenbuch
**Date**: 2026-10-06
**Paper ID**: [openalex:2407.18572](https://arxiv.org/abs/2407.18572)

## Summary

The paper introduces Bernoulli amputation, a principled stochastic method for generating missing values in complete datasets using copulas and Bernoulli margins. By specifying distributions of missingness indicators rather than manually constructing patterns, the approach models classical mechanisms like MCAR, MAR, and MNAR as well as complex structures like block and monotone missingness. Mathematical derivations and empirical applications to multivariate financial time series illustrate the framework's flexibility and capability to capture intricate missingness dependencies.

## Key Contributions

- Introduces Bernoulli amputation, a stochastic approach for introducing missing values using copulas and Bernoulli margins to generate structured missingness patterns.
- Mathematically derives key properties of the framework, including joint missingness probabilities and missingness correlations.
- Demonstrates the method's ability to model MCAR, MAR, MNAR, block missingness, and monotone missingness through mathematical examples and financial time series applications.

## Archivist Review

Strict selectivity was applied in accordance with the vault review policy. No architectural concepts or reusable core forecasting paradigms were provided in the candidate list, and the single open question was rejected as generic future work.

### Rejected Candidates
- [open_question] Advanced Copula-Based Amputation Extensions (`copula-based-amputation-future-work`) - weak_evidence: The open question is too broad and standard future work proposing extensions to high-dimensional settings without identifying a specific technical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2407.18572)
- [PDF](https://arxiv.org/pdf/2407.18572)

