---
# CSL-compatible fields
title: "Canonical correlation analysis of stochastic trends via functional approximation"
author:
  - literal: "Massimo Franchi"
  - literal: "Iliyan Georgiev"
  - literal: "Paolo Paruolo"
issued:
  date-parts:
    - [2026, 7, 14]
url: "https://arxiv.org/abs/2411.19572"

# Custom fields
paper_id: "2411.19572"
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
  - "functional-approximation-of-random-walk-limits"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-17T07:10:29Z"
created_at: "2026-07-17T07:10:29Z"
---

# Canonical correlation analysis of stochastic trends via functional approximation

**Authors**: Massimo Franchi, Iliyan Georgiev, Paolo Paruolo
**Date**: 2026-07-14
**Paper ID**: [openalex:2411.19572](https://arxiv.org/abs/2411.19572)

## Summary

This paper presents a semiparametric framework for identifying and estimating common stochastic trends in I(1)/I(0) time series systems using functional approximation and canonical correlation analysis. By projecting observed series onto a discretized L2 basis, the authors derive consistent estimators for the number of trends and their loadings, which remain robust as both time series length and basis dimensionality diverge. The approach provides asymptotically pivotal tests and is validated through Monte Carlo simulations and an empirical study of exchange rates.

## Key Contributions

- Introduces a semiparametric method for estimating the number of common stochastic trends and their loading matrix in non-stationary systems.
- Establishes that the proposed estimators are T-consistent and mixed-Gaussian, with tests that are asymptotically pivotal.
- Demonstrates effectiveness for large systems (up to 300 variables) and provides misspecification testing for model validity.

## Open Questions & Future Work

- [[improved-lrv-estimation-nonstationary-systems]]

## Key Concepts

- [[functional-approximation-of-random-walk-limits]]: A framework for identifying common stochastic trends by projecting time series onto a discretized L2 basis to enable canonical correlation analysis.

## Archivist Review

I approved the core methodology as a reusable concept for non-stationary trend identification, which fills a specific analytical niche. The open question regarding LRV estimation was approved because it addresses a fundamental, recurring bottleneck in high-dimensional hypothesis testing for non-stationary systems. The remaining candidate was rejected as it pertains to specific model specification workflows rather than a critical research-wide challenge.

### Approved Concepts
- Functional Approximation of Random Walk Limits: Provides a semiparametric way to identify common stochastic trends in high-dimensional non-stationary panels by projecting onto an L2 basis.

### Approved Open Questions
- Improving long-run variance estimation: Imprecise long-run variance estimation is a persistent obstacle to the reliability of statistical inference in nonstationary systems.

### Rejected Candidates
- [open_question] Selecting optimal identifying restrictions (`optimal-identification-selection-cointegration`) - low_impact: This is a specific application-level modeling choice rather than a fundamental theoretical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2411.19572)
- [PDF](https://arxiv.org/pdf/2411.19572)

