---
# CSL-compatible fields
title: "ARMA approximation of a Non-separable Spatio-Temporal Model with Fractional Smoothnesses in Space and Time"
author:
  - literal: "S. Knutsen Furset"
  - literal: "Geir‐Arne Fuglstad"
  - literal: "Espen R. Jakobsen"
issued:
  date-parts:
    - [2026, 4, 29]
url: "https://arxiv.org/abs/2604.26535"

# Custom fields
paper_id: "2604.26535"
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
  - "rational-approximation-based-varma-discretization"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-02T06:57:05Z"
created_at: "2026-05-02T06:57:05Z"
---

# ARMA approximation of a Non-separable Spatio-Temporal Model with Fractional Smoothnesses in Space and Time

**Authors**: S. Knutsen Furset, Geir‐Arne Fuglstad, Espen R. Jakobsen
**Date**: 2026-04-29
**Paper ID**: [openalex:2604.26535](https://arxiv.org/abs/2604.26535)

## Summary

This paper addresses the computational limitations of modeling spatio-temporal processes with fractional smoothness using diffusion-based stochastic partial differential equations. The authors propose a discretization method leveraging rational approximations in time to derive a computationally efficient vector autoregressive moving average (VARMA) process. The approach is theoretically supported by convergence proofs and empirical validation, showing that it enables accurate parameter estimation and improved forecasting for physical processes like temperature data.

## Key Contributions

- Introduces a discretization method based on rational approximations that enables VARMA representation for non-separable spatio-temporal models with arbitrary fractional smoothness.
- Provides formal proofs of pointwise convergence and establishes explicit error convergence rates as a function of spatiotemporal resolution and approximation accuracy.
- Demonstrates through numerical experiments that the approach allows accurate parameter estimation and improves forecasting performance, particularly when temporal smoothness is correctly specified.

## Open Questions & Future Work

- [[spatial-resolution-sensitivity-in-spatio-temporal-discretization]]

## Key Concepts

- [[rational-approximation-based-varma-discretization]]: A discretization technique using rational approximations in time to transform fractional stochastic partial differential equations into computable VARMA processes.

## Archivist Review

I have approved the concept of rational approximation for VARMA discretization as it provides a principled way to bridge fractional stochastic partial differential equations with tractable time-series models. I have also approved the open question regarding spatial resolution sensitivity, as this highlights a fundamental stability trade-off inherent in discretizing complex continuous spatio-temporal dynamics. I applied a strict filter to ensure only the core methodology and the most critical, research-worthy limitation were included in the vault.

### Approved Concepts
- Rational Approximation-Based VARMA Discretization: It provides a scalable computational framework for non-separable spatio-temporal models by relaxing restrictions on temporal smoothness.

### Approved Open Questions
- Spatial resolution sensitivity analysis: This is a critical stability issue for the practical application of spatiotemporal models in high-resolution settings, potentially limiting their reliability in climate and environmental forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2604.26535)
- [PDF](https://arxiv.org/pdf/2604.26535)

