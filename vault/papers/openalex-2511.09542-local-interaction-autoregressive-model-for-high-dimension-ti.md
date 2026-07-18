---
# CSL-compatible fields
title: "Local Interaction Autoregressive Model for High Dimension Time Series Data"
author:
  - literal: "Jingyang Li"
  - literal: "Chen Yang"
issued:
  date-parts:
    - [2026, 7, 15]
url: "https://arxiv.org/abs/2511.09542"

# Custom fields
paper_id: "2511.09542"
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
  - "local-interaction-autoregressive-liar-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-18T06:52:04Z"
created_at: "2026-07-18T06:52:04Z"
---

# Local Interaction Autoregressive Model for High Dimension Time Series Data

**Authors**: Jingyang Li, Chen Yang
**Date**: 2026-07-15
**Paper ID**: [openalex:2511.09542](https://arxiv.org/abs/2511.09542)

## Summary

This paper addresses the challenges of forecasting high-dimensional matrix and tensor time series by exploiting inherent local dependencies. The proposed Local Interaction Autoregressive (LIAR) framework models interactions within small neighborhoods, significantly reducing parameter space complexity and enabling efficient inference. The authors provide a scalable parameter estimation algorithm, prove consistency for neighborhood selection, and demonstrate superior forecasting performance over non-local baselines in both synthetic simulations and TEC data applications.

## Key Contributions

- Introduces the LIAR framework for high-dimensional time series by exploiting local interaction patterns to reduce parameter space dimensionality.
- Derives a scalable parameter estimation algorithm using parallel least squares combined with a BIC-type neighborhood selector.
- Demonstrates consistent neighborhood selection and provides theoretical error bounds for kernel and auto-covariance estimation.
- Outperforms baseline matrix time-series models in both numerical simulations and a practical application for Total Electron Content (TEC) forecasting.

## Open Questions & Future Work

- [[spatially-regularized-bic-selection]]

## Key Concepts

- [[local-interaction-autoregressive-liar-framework]]: A forecasting framework for high-dimensional matrix and tensor time series that models local spatial dependencies to reduce parameter space complexity.

## Archivist Review

I approved the LIAR framework as a distinct approach to high-dimensional forecasting via local dependency modeling. The open question on spatially regularized neighborhood selection is a significant theoretical and computational bottleneck for this class of methods, warranting a standalone note. All other candidates were rejected as they were either paper-local implementation details or covered by existing framework concepts.

### Approved Concepts
- Local Interaction Autoregressive (LIAR) framework: The core methodological contribution providing a dimension-reduction strategy for high-dimensional time series based on local neighborhood interactions.

### Approved Open Questions
- Spatially Regularized Neighborhood Selection: Spatially regularized selection is crucial for improving the interpretability of learned spatio-temporal dependencies and reducing noise in local structure estimation where dependency patterns exhibit spatial continuity.

## Links

- [Abstract](https://arxiv.org/abs/2511.09542)
- [PDF](https://arxiv.org/pdf/2511.09542)

