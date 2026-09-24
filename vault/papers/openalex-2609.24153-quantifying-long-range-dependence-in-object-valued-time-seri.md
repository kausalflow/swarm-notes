---
# CSL-compatible fields
title: "Quantifying Long-Range Dependence in Object-Valued Time Series"
author:
  - literal: "Won‐Ki Seo"
  - literal: "Jiazhen Xu"
  - literal: "Han Lin Shang"
issued:
  date-parts:
    - [2026, 9, 21]
url: "https://arxiv.org/abs/2609.24153"

# Custom fields
paper_id: "2609.24153"
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
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-24T09:38:19Z"
created_at: "2026-09-24T09:38:19Z"
---

# Quantifying Long-Range Dependence in Object-Valued Time Series

**Authors**: Won‐Ki Seo, Jiazhen Xu, Han Lin Shang
**Date**: 2026-09-21
**Paper ID**: [openalex:2609.24153](https://arxiv.org/abs/2609.24153)

## Summary

This paper develops an intrinsic framework for quantifying long-range dependence in object-valued time series—such as distributions, covariance matrices, and networks—living in metric spaces of negative type. By utilizing isometric embeddings into Hilbert spaces and distance-based lag measures, the authors define a memory parameter via the trace of the lag-covariance operator. To counteract the common-centering bias caused by estimating marginal distances from dependent samples, they introduce iterated block-difference corrections, log-ratio and multi-bandwidth log-slope estimators, and a localized self-consistency refinement, demonstrating substantial bias reduction on both simulations and real-world data like foreign-exchange return distributions.

## Key Contributions

- Developed an intrinsic framework for defining and estimating long memory in object-valued time series within metric spaces of negative type using distance-based estimators.
- Derived the finite-sample common-centering bias induced by estimating the common marginal distance from dependent samples and proposed iterated block-difference corrections, log-ratio/multi-bandwidth log-slope estimators, and a localized self-consistency refinement.
- Established consistency of the proposed estimators and documented substantial bias reduction in simulations, alongside empirical evidence of long memory in foreign-exchange return distributions and U.S. electricity-generation compositions.

## Open Questions & Future Work

- [[hypothesis-testing-structural-breaks-object-valued-time-series]]

## Archivist Review

The paper introduces a rigorous metric-space framework for long-memory estimation in object-valued time series. No distinct reusable algorithmic concepts or benchmark datasets meet the strict scarcity and general applicability thresholds for permanent standalone vault notes, but the open question on hypothesis testing and structural breaks in non-Euclidean long memory is retained.

### Approved Open Questions
- Testing Long Memory and Breaks: Crucial for statistical inference and model validation in non-Euclidean time series analysis, as failing to distinguish long memory from structural instability leads to severe forecasting and inferential errors.

## Links

- [Abstract](https://arxiv.org/abs/2609.24153)
- [PDF](https://arxiv.org/pdf/2609.24153)

