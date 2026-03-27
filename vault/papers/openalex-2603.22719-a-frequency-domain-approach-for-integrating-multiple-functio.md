---
# CSL-compatible fields
title: "A Frequency-Domain Approach for Integrating Multiple Functional Time Series"
author:
  - literal: "Zerui Guo"
  - literal: "Jianbin Tan"
  - literal: "Hui Huang"
issued:
  date-parts:
    - [2026, 3, 24]
url: "https://arxiv.org/abs/2603.22719"

# Custom fields
paper_id: "2603.22719"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "functional-time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "marginal-dynamic-karhunen-loeve-expansion"
  - "marginal-spectral-operator-mfts"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T15:43:26Z"
created_at: "2026-03-27T15:43:26Z"
---

# A Frequency-Domain Approach for Integrating Multiple Functional Time Series

**Authors**: Zerui Guo, Jianbin Tan, Hui Huang
**Date**: 2026-03-24
**Paper ID**: [openalex:2603.22719](https://arxiv.org/abs/2603.22719)

## Summary

This work introduces a novel frequency-domain framework for the integrative analysis of Multivariate Functional Time Series (MFTS), which suffer from complex multi-way dependencies. The core methodology involves integrating individual spectral densities to construct a marginal spectral operator, from which optimal functional filters are derived via its eigenfunctions. These filters effectively transform the high-dimensional functional observations into a structured multivariate time series representation, simplifying subsequent joint modeling and estimation. Extensive simulations confirm the method's superior performance, and it is successfully applied to the imputation and forecasting of air pollutant concentration data. The approach leverages spectral analysis to effectively decouple and manage the complex dependencies inherent in MFTS data.

## Key Contributions

- Proposed a novel frequency-domain framework for analyzing Multivariate Functional Time Series (MFTS) based on a marginal dynamic Karhunen–Loève expansion.
- Developed a method to integrate individual spectral densities to construct a marginal spectral operator, whose eigenfunctions serve as optimal functional filters.
- Demonstrated that the derived functional filters successfully transform complex functional observations into a structured multivariate time series representation suitable for joint modeling.
- Validated the framework's superior performance through extensive simulations and its practical utility in imputing and forecasting air pollutant concentration trajectories.

## Limitations

The abstract does not explicitly mention limitations, but complexity arising from high-dimensional spectral density integration may be a practical limitation.

## Open Questions & Future Work

- [[eigenfunction-uniqueness-mfsts]]
- [[incorporating-exogenous-covariates-mfsts]]

## Key Concepts

- [[marginal-dynamic-karhunen-loeve-expansion]]: A frequency-domain expansion technique for multivariate functional time series used to derive optimal functional filters by integrating individual spectral densities.
- [[marginal-spectral-operator-mfts]]: An operator constructed by integrating the individual spectral densities of a Multivariate Functional Time Series (MFTS) to facilitate analysis.

## Archivist Review

Archivist review kept only candidates judged central to the paper and reusable across future work. Approved 2 concept(s), 2 open question(s), and 0 dataset(s), with 1 rejected candidate note(s).

### Approved Concepts
- Marginal Dynamic Karhunen–Loève Expansion: This expansion is the core mathematical tool used to derive the spectral operator and optimal functional filters.
- Marginal Spectral Operator: The marginal spectral operator is the central object constructed from the data that enables the transformation into a manageable time series representation.

### Approved Open Questions
- Resolving Eigenfunction Non-Uniqueness: Resolving non-uniqueness in basis representation is crucial for achieving stable and theoretically optimal dimension reduction methods in functional data analysis, directly impacting the reliability of downstream tasks like forecasting.
- Extend Framework with Exogenous Covariates: Incorporating exogenous information is a standard and highly valuable extension for improving the predictive power of time series models in real-world applications.

### Rejected Candidates
- [open_question] Generalize Framework to High Dimensions (`generalization-to-high-dimensional-regimes`) - low_impact: This candidate is marked as future work and is a standard scaling direction (handling large $p$), but the other two open questions capture more specific unresolved methodological issues in the framework itself (uniqueness and covariate integration).

## Links

- [Abstract](https://arxiv.org/abs/2603.22719)
- [PDF](https://arxiv.org/pdf/2603.22719)

