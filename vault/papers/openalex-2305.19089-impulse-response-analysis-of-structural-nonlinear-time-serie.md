---
# CSL-compatible fields
title: "Impulse Response Analysis of Structural Nonlinear Time Series Models"
author:
  - literal: "Giovanni Ballarin"
issued:
  date-parts:
    - [2026, 6, 18]
url: "https://arxiv.org/abs/2305.19089"

# Custom fields
paper_id: "2305.19089"
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
  - "semiparametric-sieve-estimation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-21T08:53:22Z"
created_at: "2026-06-21T08:53:22Z"
---

# Impulse Response Analysis of Structural Nonlinear Time Series Models

**Authors**: Giovanni Ballarin
**Date**: 2026-06-18
**Paper ID**: [openalex:2305.19089](https://arxiv.org/abs/2305.19089)

## Summary

This paper introduces a semiparametric sieve estimation framework to compute impulse response functions for structural nonlinear autoregressive models. By employing a flexible two-step procedure, the method avoids the limitations of predefined parametric structures while maintaining rigorous uniform estimation guarantees. The effectiveness of this approach is validated through simulation and an empirical study of U.S. monetary policy, where it highlights significantly different economic outcomes for interest rate shocks compared to linear benchmarks. An iterative algorithm is also provided to facilitate the practical computation of these impulse responses.

## Key Contributions

- Develops a semiparametric sieve estimation approach for impulse response functions in structural nonlinear autoregressive time series models.
- Proposes a two-step estimation procedure that avoids rigid parametric assumptions, enabling flexible capture of nonlinear dynamic dependencies.
- Provides an iterative algorithm for the efficient computation of impulse responses in complex nonlinear structural models.
- Demonstrates enhanced sensitivity in modeling U.S. monetary policy shocks, revealing larger GDP responses to interest rate hikes compared to standard linear models.

## Open Questions & Future Work

- [[nonparametric-inference-unbounded-data]]

## Key Concepts

- [[semiparametric-sieve-estimation]]: A non-parametric estimation framework that approximates complex nonlinear structural dependencies by expanding unknown functions into series of basis functions.

## Archivist Review

The review focuses on the methodological innovation of using sieve estimation for nonlinear structural time series analysis, which is a reusable statistical framework in econometrics and time series forecasting. The approved open question addresses a core theoretical limitation in nonparametric time series analysis that constrains its application to real-world datasets lacking compact support. Other potential candidates were rejected for being too closely tied to the specific application of the paper or for representing standard practices.

### Approved Concepts
- Semiparametric Sieve Estimation: Provides a flexible way to capture nonlinear dynamics without rigid parametric assumptions, serving as a powerful alternative to standard linear autoregressive approaches.

### Approved Open Questions
- Nonparametric Inference for Unbounded Data: It is a fundamental bottleneck for making semiparametric structural time series modeling more broadly applicable to economic data, which frequently does not adhere to compact support conditions.

## Links

- [Abstract](https://arxiv.org/abs/2305.19089)
- [PDF](https://arxiv.org/pdf/2305.19089)

