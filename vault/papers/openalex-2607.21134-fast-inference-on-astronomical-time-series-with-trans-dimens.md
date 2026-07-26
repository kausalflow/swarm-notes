---
# CSL-compatible fields
title: "Fast Inference on Astronomical Time Series with Trans-Dimensional Flow Matching Posterior Estimation"
author:
  - literal: "Nina van der Meulen"
  - literal: "Tin Hadži Veljković"
  - literal: "Daniela Huppenkothen"
  - literal: "B B Miller"
  - literal: "Christoph Weniger"
issued:
  date-parts:
    - [2026, 7, 23]
url: "https://arxiv.org/abs/2607.21134"

# Custom fields
paper_id: "2607.21134"
paper_source: "openalex"
domain: "astronomy"
tags:
  - "transformer"
  - "time-series"
  - "simulation-based-inference"
  - "flow-matching"
  - "posterior-estimation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "trans-dimensional-flow-matching-posterior-estimation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-26T07:29:32Z"
created_at: "2026-07-26T07:29:32Z"
---

# Fast Inference on Astronomical Time Series with Trans-Dimensional Flow Matching Posterior Estimation

**Authors**: Nina van der Meulen, Tin Hadži Veljković, Daniela Huppenkothen, B B Miller, Christoph Weniger
**Date**: 2026-07-23
**Paper ID**: [openalex:2607.21134](https://arxiv.org/abs/2607.21134)

## Summary

The paper introduces trans-dimensional Flow Matching Posterior Estimation (t-FMPE), a simulation-based inference method built on a transformer architecture designed to efficiently solve trans-dimensional inference problems in astronomical time series, such as estimating variable numbers of pulses. Applied to simulated data, Fast Radio Bursts, and magnetar X-ray bursts, t-FMPE successfully captures parameter correlations while achieving several orders of magnitude speedups compared to traditional MCMC and nested sampling methods.

## Key Contributions

- Introduces trans-dimensional Flow Matching Posterior Estimation (t-FMPE) on a transformer architecture for efficient amortized trans-dimensional inference on time series data.
- Demonstrates qualitative agreement with MCMC reference posteriors on simulated data, Fast Radio Bursts, and magnetar X-ray bursts while preserving parameter correlations.
- Achieves orders of magnitude speedup over traditional MCMC and nested sampling, reaching 100 posterior samples per second for an 80-dimensional parameter space.

## Key Concepts

- [[trans-dimensional-flow-matching-posterior-estimation]]: A simulation-based inference framework using flow matching and a transformer architecture to perform amortized trans-dimensional parameter estimation on time series.

## Archivist Review

Approved the core methodological contribution of trans-dimensional flow matching posterior estimation as a distinct and reusable framework for simulation-based inference on time series. No datasets or open questions met the stringent inclusion thresholds.

### Approved Concepts
- Trans-Dimensional Flow Matching Posterior Estimation: It is the core methodological contribution of the paper, enabling efficient amortized trans-dimensional inference on time series data.

## Links

- [Abstract](https://arxiv.org/abs/2607.21134)
- [PDF](https://arxiv.org/pdf/2607.21134)

