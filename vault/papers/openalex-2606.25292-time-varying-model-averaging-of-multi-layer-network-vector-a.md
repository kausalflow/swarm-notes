---
# CSL-compatible fields
title: "Time-Varying Model Averaging of Multi-layer Network Vector Autoregressions"
author:
  - literal: "Degui Li"
  - literal: "Yuying Sun"
  - literal: "Boyao Wu"
issued:
  date-parts:
    - [2026, 6, 24]
url: "https://arxiv.org/abs/2606.25292"

# Custom fields
paper_id: "2606.25292"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "conformal-prediction"
architectures:
  []
datasets:
  []
concept_slugs:
  - "multi-layer-network-vector-autoregression"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-27T07:43:13Z"
created_at: "2026-06-27T07:43:13Z"
---

# Time-Varying Model Averaging of Multi-layer Network Vector Autoregressions

**Authors**: Degui Li, Yuying Sun, Boyao Wu
**Date**: 2026-06-24
**Paper ID**: [openalex:2606.25292](https://arxiv.org/abs/2606.25292)

## Summary

This paper introduces a time-varying multi-layer network vector autoregression (VAR) framework designed to model complex interactions across channels in high-dimensional time series. The authors propose a penalized model averaging approach to dynamically combine candidate models, ensuring optimal predictive performance in non-stationary environments. Theoretical results confirm the method's asymptotic optimality, and the framework is further enhanced with conformal prediction for reliable uncertainty quantification. Empirical validation demonstrates the model's effectiveness in forecasting CPI inflation using integrated multi-layer network information.

## Key Contributions

- Introduces a multi-layer network VAR model framework that leverages multiple adjacency matrices to capture cross-channel spillover effects in large-scale dynamic systems.
- Develops a penalized model averaging method that identifies time-varying, optimal combinations of candidate network VAR models, even when the model space is divergent.
- Establishes asymptotic optimality and convergence rates for the proposed weight estimation in both in-sample fitting and out-of-sample prediction tasks.
- Extends conformal prediction to construct robust prediction bands specifically for locally stationary time series.

## Open Questions & Future Work

- [[model-averaging-inference-and-uncertainty]]

## Key Concepts

- [[multi-layer-network-vector-autoregression]]: A multivariate time series framework that incorporates multiple graph adjacency matrices to model cross-channel spillovers in dynamic systems.

## Archivist Review

I approved the 'Multi-layer Network Vector Autoregression' as it represents a structured approach to multivariate forecasting in network-dependent time series. The open question regarding 'Model Averaging Inference Limits' was approved because it addresses the critical, unresolved gap between optimal point forecasting through model averaging and the rigorous construction of valid uncertainty bands in non-stationary settings. Other candidates were either subcomponents or lacked sufficient novelty to warrant permanent status.

### Approved Concepts
- Multi-layer Network Vector Autoregression: It provides a formal framework for incorporating multiple structured dependencies (via adjacency matrices) into multivariate time series forecasting, which is a common requirement in network-based dynamics.

### Approved Open Questions
- Model Averaging Inference Limits: It addresses the fundamental tension between achieving optimal model combination and providing reliable uncertainty quantification in high-dimensional, non-stationary forecasting environments.

### Rejected Candidates
- [concept] Penalized Model Averaging Method (`penalized-model-averaging-method`) - subcomponent_of_broader_mechanism: This is a specific implementation technique that is a subcomponent of the broader methodology, rather than a foundational concept.

## Links

- [Abstract](https://arxiv.org/abs/2606.25292)
- [PDF](https://arxiv.org/pdf/2606.25292)

