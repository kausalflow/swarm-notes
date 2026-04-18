---
# CSL-compatible fields
title: "Irregularly Sampled Time Series Interpolation for Binary Evolution Simulations Using Dynamic Time Warping"
author:
  - literal: "Ugur Demir"
  - literal: "Philipp M. Srivastava"
  - literal: "Aggelos Katsaggelos"
  - literal: "Vicky Kalogera"
  - literal: "S. Tapia"
  - literal: "Manuel Ballester"
  - literal: "Shamal Lalvani"
  - literal: "Patrick Koller"
  - literal: "Jeff J. Andrews"
  - literal: "Seth Gossage"
  - literal: "Max M. Briel"
  - literal: "Elizabeth Teng"
issued:
  date-parts:
    - [2026, 4, 15]
url: "https://arxiv.org/abs/2604.13604"

# Custom fields
paper_id: "2604.13604"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "shared-path-dynamic-time-warping-alignment"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-18T06:06:44Z"
created_at: "2026-04-18T06:06:44Z"
---

# Irregularly Sampled Time Series Interpolation for Binary Evolution Simulations Using Dynamic Time Warping

**Authors**: Ugur Demir, Philipp M. Srivastava, Aggelos Katsaggelos, Vicky Kalogera, S. Tapia, Manuel Ballester, Shamal Lalvani, Patrick Koller, Jeff J. Andrews, Seth Gossage, Max M. Briel, Elizabeth Teng
**Date**: 2026-04-15
**Paper ID**: [openalex:2604.13604](https://arxiv.org/abs/2604.13604)

## Summary

Binary stellar evolution models are computationally demanding, necessitating efficient interpolation methods for population synthesis. This paper proposes a novel framework using Dynamic Time Warping to align and average binary stellar tracks, addressing the complexities introduced by mutual stellar interactions and irregular sampling. By computing a shared warping path across physical parameters, the method preserves essential causal relationships such as the Stefan-Boltzmann law. The approach consistently outperforms traditional interpolation, providing a more efficient and accurate means of generating binary population samples for astrophysical research.

## Key Contributions

- Introduces a novel track alignment and iterative averaging method utilizing Dynamic Time Warping to handle irregularly sampled binary stellar evolution data.
- Enables the computation of a shared warping path across multiple physical parameters, ensuring the preservation of causal physical relationships like the Stefan-Boltzmann law during interpolation.
- Demonstrates superior performance over traditional interpolation methods in generating accurate binary population samples, significantly reducing the computational cost of stellar population synthesis.

## Open Questions & Future Work

- [[enforcing-physical-consistency-in-interpolation]]

## Key Concepts

- [[shared-path-dynamic-time-warping-alignment]]: A multi-variate alignment strategy that uses a single shared warping path in DTW to preserve causal relationships between physical variables in irregularly sampled time series.

## Archivist Review

I approved the core method as a generalized technique for multivariate alignment (Shared-Path DTW) and the open question regarding the enforcement of physical laws in surrogate models. The rejected concept was renamed to a more generalizable form. The rejected open question was deemed a standard technical nuisance rather than a high-level research hurdle.

### Approved Concepts
- Shared-Path Dynamic Time Warping (DTW) Alignment: This provides a generalized framework for aligning irregularly sampled, multidimensional time series where variables are causally coupled, a common challenge in scientific time-series forecasting.

### Approved Open Questions
- Enforcing Physical Consistency in Interpolation: This addresses the fundamental tension between data-driven interpolation and physical fidelity, which is a bottleneck in replacing expensive physical simulations with surrogate models.

### Rejected Candidates
- [concept] DTW-based binary track alignment (`dtw-based-binary-track-alignment`) - other: The specific name was too tied to the application; I renamed it to focus on the generalized methodological mechanism (Shared-Path DTW).
- [open_question] Morphology-Aware Neighbor Selection (`morphology-aware-neighbor-selection`) - low_impact: This is a relatively standard issue in k-nearest neighbor interpolation schemes and lacks the technical weight of the physical consistency problem.

## Links

- [Abstract](https://arxiv.org/abs/2604.13604)
- [PDF](https://arxiv.org/pdf/2604.13604)

