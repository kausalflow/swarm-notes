---
# CSL-compatible fields
title: "A Riemannian Factor Model for Manifold-Valued Time Series"
author:
  - literal: "Shuo-Chieh Huang"
  - literal: "Rong Chen"
  - literal: "Yaqing Chen"
issued:
  date-parts:
    - [2026, 7, 30]
url: "https://arxiv.org/abs/2607.28385"

# Custom fields
paper_id: "2607.28385"
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
  - "riemannian-factor-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-02T07:26:35Z"
created_at: "2026-08-02T07:26:35Z"
---

# A Riemannian Factor Model for Manifold-Valued Time Series

**Authors**: Shuo-Chieh Huang, Rong Chen, Yaqing Chen
**Date**: 2026-07-30
**Paper ID**: [openalex:2607.28385](https://arxiv.org/abs/2607.28385)

## Summary

The authors propose a Riemannian factor model (RFM) for analyzing high-dimensional time series residing on Riemannian manifolds, effectively capturing inherent data nonlinearity. Under short-memory and strong factor conditions, the framework achieves a dimension-free n^{-1/2} convergence rate for the estimated loading space in high-dimensional asymptotic regimes. Empirical evaluations on simulated sphere and Bures--Wasserstein manifold data, as well as an application to realized covariances of U.S. stock returns, illustrate both theoretical robustness and competitive predictive utility.

## Key Contributions

- Proposes a Riemannian factor model (RFM) to handle high-dimensional time series on Riemannian manifolds while accounting for intrinsic non-linearity.
- Establishes theoretical convergence rates for the estimated loading space, achieving a dimension-free n^{-1/2} rate under short-memory and strong factor conditions.
- Demonstrates superior predictive performance and interpretable factors on monthly realized covariances of U.S. stock returns modeled on the Bures--Wasserstein manifold.

## Open Questions & Future Work

- [[riemannian-factor-models-general-manifolds]]

## Key Concepts

- [[riemannian-factor-model]]: A geometry-aware factor model for analyzing high-dimensional time series on Riemannian manifolds.

## Archivist Review

The Riemannian factor model represents a distinct and principled geometry-aware framework for manifold-valued time series analysis, satisfying our strict standards for methodological novelty and potential vault reusability. The open question regarding its extension to general and incomplete manifolds highlights a substantial theoretical boundary well worth tracking. No datasets qualified for permanent standalone entries.

### Approved Concepts
- Riemannian Factor Model: Introduces a novel geometry-aware factor model for high-dimensional time series on Riemannian manifolds, bridging linear factor models with non-linear manifold geometry.

### Approved Open Questions
- Riemannian Factor Models on General Manifolds: Crucial for broadening geometry-aware dimension reduction techniques to complex topological spaces where standard completeness assumptions fail.

## Links

- [Abstract](https://arxiv.org/abs/2607.28385)
- [PDF](https://arxiv.org/pdf/2607.28385)

