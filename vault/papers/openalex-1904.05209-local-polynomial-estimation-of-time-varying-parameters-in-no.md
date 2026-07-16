---
# CSL-compatible fields
title: "LOCAL POLYNOMIAL ESTIMATION OF TIME-VARYING PARAMETERS IN NONLINEAR MODELS"
author:
  - literal: "Dennis Kristensen"
  - literal: "Young Jun Lee"
issued:
  date-parts:
    - [2026, 7, 13]
url: "https://arxiv.org/abs/1904.05209"

# Custom fields
paper_id: "1904.05209"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-16T07:13:57Z"
created_at: "2026-07-16T07:13:57Z"
---

# LOCAL POLYNOMIAL ESTIMATION OF TIME-VARYING PARAMETERS IN NONLINEAR MODELS

**Authors**: Dennis Kristensen, Young Jun Lee
**Date**: 2026-07-13
**Paper ID**: [openalex:1904.05209](https://arxiv.org/abs/1904.05209)

## Summary

This paper presents a new asymptotic framework for local polynomial extremum estimation of time-varying parameters across a wide range of nonlinear time-series models, including discrete-valued processes. The authors derive conditions for asymptotic normality and provide an exact characterization of smoothing-induced bias. The theoretical findings are verified through applications to threshold autoregressive, ARCH, and Poisson autoregressive models, with a practical empirical study on corporate default frequency.

## Key Contributions

- Establishes asymptotic theory for local polynomial extremum estimators of time-varying parameters in nonlinear time-series models.
- Provides a precise characterization of the leading bias term inherent in local smoothing estimators.
- Demonstrates empirical effectiveness through a Poisson autoregression analysis of U.S. corporate default counts.

## Open Questions & Future Work

- [[kernel-positivity-non-concave-identification]]
- [[local-stationarity-infinite-memory]]

## Archivist Review

The paper provides a rigorous asymptotic framework for time-varying parameter estimation in nonlinear models but does not introduce a novel, reusable concept that transcends its specific domain. The proposed open questions relate to the technical derivation of the paper's proof rather than overarching research bottlenecks for the broader field. Therefore, all candidates were rejected.

### Approved Open Questions
- Identification with general kernels: Removing the positivity constraint on the kernel function is critical for allowing more flexible kernel choices (such as higher-order kernels) which are essential for further bias reduction in nonparametric smoothing.
- Proving local stationarity condition: This is fundamental to ensuring the validity of asymptotic theory for the proposed estimators when applied to a wide range of realistic, complex infinite memory time series.

### Rejected Candidates
- [open_question] Identification with general kernels (`kernel-positivity-non-concave-identification`) - low_impact: Re-evaluating based on the provided instructions to be highly selective; while potentially useful, this is a highly technical nuance of a specific estimation framework rather than a broad, recurrent research bottleneck.
- [open_question] Proving local stationarity condition (`local-stationarity-infinite-memory`) - paper_local: This is a technical limitation specific to the derivation of the authors' proof rather than a universal bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/1904.05209)
- [PDF](https://arxiv.org/pdf/1904.05209)

