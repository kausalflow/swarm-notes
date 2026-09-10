---
# CSL-compatible fields
title: "Bayesian Generalized Network Autoregressive Model with Structured Shrinkage and Persistence Priors"
author:
  - literal: "김성민"
  - literal: "K.Y. Kim"
issued:
  date-parts:
    - [2026, 9, 7]
url: "https://arxiv.org/abs/2609.07257"

# Custom fields
paper_id: "2609.07257"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "bayesian"
  - "graph-neural-network"
  - "multivariate-time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "bayesian-generalized-network-autoregressive-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-10T09:17:06Z"
created_at: "2026-09-10T09:17:06Z"
---

# Bayesian Generalized Network Autoregressive Model with Structured Shrinkage and Persistence Priors

**Authors**: 김성민, K.Y. Kim
**Date**: 2026-09-07
**Paper ID**: [openalex:2609.07257](https://arxiv.org/abs/2609.07257)

## Summary

The paper introduces the Bayesian generalized network autoregressive (BGNAR) model for multivariate time series on known networks by fusing the generalized network autoregressive framework with Bayesian vector autoregressive Minnesota-type shrinkage and persistence priors. This formulation regularizes over-specified temporal and network-lag structures without requiring dataset-specific BIC order selection while providing robust posterior inference and predictive uncertainty quantification. Evaluations on synthetic settings and a wind-speed network demonstrate competitive point-forecasting performance and enhanced uncertainty quantification compared to standard GNAR and BVAR benchmarks.

## Key Contributions

- Proposed the Bayesian generalized network autoregressive (BGNAR) model combining GNAR with structured shrinkage and persistence priors adapted from BVAR.
- Developed Minnesota-type shrinkage for own-lag and network-lag coefficients, featuring prior variances decreasing over temporal lags and neighborhood orders.
- Demonstrated through simulations and a wind-speed network application that BGNAR avoids dataset-specific BIC order selection while matching or exceeding the forecasting performance of baseline GNAR and BVAR models.

## Open Questions & Future Work

- [[extensions-to-bgnar-framework]]

## Key Concepts

- [[bayesian-generalized-network-autoregressive-model]]: A Bayesian generalized network autoregressive model integrating structured shrinkage and persistence priors for network-structured multivariate time series.

## Archivist Review

Approved the core Bayesian generalized network autoregressive model concept and the open question concerning its extensions to time-varying networks and scalability, adhering strictly to the required constraints.

### Approved Concepts
- Bayesian Generalized Network Autoregressive Model: It is the primary modeling framework introduced in the paper, combining GNAR and BVAR priors.

### Approved Open Questions
- Extensions to BGNAR Framework: Addressing time-varying networks, non-diagonal error covariances, and computational scalability is vital for expanding network autoregressive models to handle complex, large-scale real-world multivariate time series systems.

## Links

- [Abstract](https://arxiv.org/abs/2609.07257)
- [PDF](https://arxiv.org/pdf/2609.07257)

