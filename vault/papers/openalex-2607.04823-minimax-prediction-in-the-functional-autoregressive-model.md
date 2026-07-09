---
# CSL-compatible fields
title: "Minimax prediction in the Functional Autoregressive Model"
author:
  - literal: "André Mas"
  - literal: "Angelina Roche"
issued:
  date-parts:
    - [2026, 7, 6]
url: "https://arxiv.org/abs/2607.04823"

# Custom fields
paper_id: "2607.04823"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "functional-autoregressive-model-far"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-09T08:18:18Z"
created_at: "2026-07-09T08:18:18Z"
---

# Minimax prediction in the Functional Autoregressive Model

**Authors**: André Mas, Angelina Roche
**Date**: 2026-07-06
**Paper ID**: [openalex:2607.04823](https://arxiv.org/abs/2607.04823)

## Summary

This paper provides a rigorous non-asymptotic analysis of prediction mean square error for the Functional Autoregressive (FAR) model. By deriving minimax lower bounds and introducing a ridge-type estimator that avoids traditional functional PCA regularization, the authors characterize the optimal convergence rates in terms of functional smoothness and correlation operator properties. The results offer new insights into the behavior of Hilbert-valued Markov processes and reveal theoretical connections to extreme value theory.

## Key Contributions

- Derived non-asymptotic lower bounds for the mean square error of predictions in Functional Autoregressive (FAR) models, accounting for mixed smoothness and correlation operator dependencies.
- Proposed a ridge-type estimator for the FAR model that bypasses the need for functional PCA-based spectral estimation of the covariance sequence.
- Established that the proposed ridge-type estimator achieves optimal convergence rates by matching the derived minimax lower bound up to constant factors.

## Key Concepts

- [[functional-autoregressive-model-far]]: A generalization of multivariate autoregressive models to Hilbert-valued functional data.

## Archivist Review

I have approved the Functional Autoregressive Model (FAR) as a fundamental concept in functional time series analysis. I rejected the ridge-type estimator as it serves as a specific implementation improvement for the FAR model rather than a broad, independent framework. The analysis maintains a high threshold for concepts to ensure only foundational structures are recorded.

### Approved Concepts
- Functional Autoregressive Model (FAR): The paper provides a formal non-asymptotic minimax analysis of the FAR model, establishing a theoretical benchmark for functional time series forecasting.

### Rejected Candidates
- [concept] Ridge-type estimator for FAR (`ridge-type-estimator-for-far`) - subcomponent_of_broader_mechanism: This is a specific technical implementation detail for FAR estimation rather than a broad, reusable paradigm.

## Links

- [Abstract](https://arxiv.org/abs/2607.04823)
- [PDF](https://arxiv.org/pdf/2607.04823)

