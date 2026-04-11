---
# CSL-compatible fields
title: "Amortized Filtering and Smoothing with Conditional Normalizing Flows"
author:
  - literal: "Tiangang Cui"
  - literal: "Xiaodong Feng"
  - literal: "Chenlong Pei"
  - literal: "Xiaoliang Wan"
  - literal: "Tao Zhou"
issued:
  date-parts:
    - [2026, 4, 8]
url: "https://arxiv.org/abs/2604.07169"

# Custom fields
paper_id: "2604.07169"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "normalizing-flow"
  - "state-space-model"
  - "filtering"
  - "smoothing"
architectures:
  []
datasets:
  []
concept_slugs:
  - "amortized-filtering-and-smoothing-framework-afsf"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-11T05:56:39Z"
created_at: "2026-04-11T05:56:39Z"
---

# Amortized Filtering and Smoothing with Conditional Normalizing Flows

**Authors**: Tiangang Cui, Xiaodong Feng, Chenlong Pei, Xiaoliang Wan, Tao Zhou
**Date**: 2026-04-08
**Paper ID**: [openalex:2604.07169](https://arxiv.org/abs/2604.07169)

## Summary

This paper introduces AFSF, an amortized framework designed for efficient filtering and smoothing in high-dimensional nonlinear dynamical systems. The methodology leverages a recurrent encoder to condense observation histories into fixed-dimensional summary statistics, which then condition both forward and backward normalizing flows. This dual-flow architecture enables accurate trajectory-level smoothing and supports extrapolation beyond training horizons, outperforming conventional methods by learning the latent temporal evolution structure. The authors also provide a flow-based particle filtering variant to facilitate model diagnostics when explicit state-space factors are accessible.

## Key Contributions

- Introduces AFSF, a unified framework that utilizes recurrent encoders to generate fixed-dimensional latent summary statistics for amortized filtering and smoothing.
- Demonstrates that coupling forward and backward conditional normalizing flows via shared summary statistics improves latent trajectory-level smoothing accuracy.
- Supports extrapolation beyond training horizons by learning underlying temporal dynamics, with a flow-based particle filtering variant for diagnostics.

## Open Questions & Future Work

- [[stability-of-amortized-smoothing-procedures]]

## Key Concepts

- [[amortized-filtering-and-smoothing-framework-afsf]]: A unified amortized framework that uses shared summary statistics to learn both forward filtering distributions and backward transition kernels for time series trajectories.

## Archivist Review

The framework AFSF presents a novel architectural paradigm of using shared summary statistics to bridge forward and backward flows for latent trajectory inference, which is highly reusable. The open question regarding the stability of such amortized smoothing procedures targets a fundamental bottleneck in the scalability of these models to higher dimensions, moving beyond specific implementation details.

### Approved Concepts
- Amortized Filtering and Smoothing Framework (AFSF): It represents a novel approach to unify filtering and smoothing using a shared latent summary statistic across two coupled conditional normalizing flows.

### Approved Open Questions
- Stability of amortized smoothing: Understanding the stability and error propagation of amortized smoothing is critical for the reliable deployment of these models in high-dimensional scientific and engineering applications, where smoothing is often essential for posterior analysis.

## Links

- [Abstract](https://arxiv.org/abs/2604.07169)
- [PDF](https://arxiv.org/pdf/2604.07169)

