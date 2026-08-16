---
# CSL-compatible fields
title: "Measuring the Arrow of Time: Identification, Estimation, and Inference for Directional Structure in Multivariate Time Series"
author:
  - literal: "Avishek Bhandari"
issued:
  date-parts:
    - [2026, 8, 13]
url: "https://arxiv.org/abs/2608.13431"

# Custom fields
paper_id: "2608.13431"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-16T05:17:39Z"
created_at: "2026-08-16T05:17:39Z"
---

# Measuring the Arrow of Time: Identification, Estimation, and Inference for Directional Structure in Multivariate Time Series

**Authors**: Avishek Bhandari
**Date**: 2026-08-13
**Paper ID**: [openalex:2608.13431](https://arxiv.org/abs/2608.13431)

## Summary

This paper establishes a rigorous statistical framework for measuring the arrow of time in multivariate time series by defining directionality through a circulation matrix carried by lagged covariances. The author proves that contemporaneous covariance alone is blind to time direction, whereas the proposed lagged circulation captures asymmetry between forward and reversed processes. To support this, the paper develops a cross-fitted estimator with bias removal, delete-block jackknife standard errors, an exact randomisation test, and extensions to nonlinear systems via feature maps.

## Key Contributions

- Proposes a complete methodological framework for identifying and measuring directional structure (the arrow of time) in multivariate time series using a circulation matrix carried by lagged covariance.
- Derives an entropy-production functional under a Gaussian benchmark, representing the quadratic component of divergence per unit time between forward and reversed records.
- Develops a rigorous statistical toolkit including a cross-fitted estimator with first-order bias removal, delete-block jackknife standard errors, and an exact randomisation test under a block null.
- Compares the proposed method against correlation networks, Granger causality, transfer entropy, and connectedness indices across four systems with known answers.

## Open Questions & Future Work

- [[high-dimensional-circulation-estimation]]
- [[counterfactual-interpretation-of-circulation]]

## Archivist Review

Applied strict reusability and novelty filters, approving two focused open questions on high-dimensional estimation and counterfactual interpretation while rejecting concepts that are specialized estimator formulations.

### Approved Open Questions
- High-Dimensional Circulation and Entropy Estimation: High-dimensional panels frequently arise in economics, neuroscience, and climate science where standard sample-moment estimators of circulation break down due to curse of dimensionality and noise accumulation.
- Counterfactual Interpretation of Statistical Circulation: Bridging the gap between descriptive observational time-reversibility metrics and rigorous policy counterfactual analysis is crucial for causal inference in macroeconomics and systems biology.

### Rejected Candidates
- [open_question] Data-Driven Bases and Time-Varying Circulation (`data-driven-basis-and-time-varying-circulation`) - low_impact: Broad and multi-part open question covering both basis selection and time-varying paths, making it less focused than the approved theoretical and high-dimensional challenges.

## Links

- [Abstract](https://arxiv.org/abs/2608.13431)
- [PDF](https://arxiv.org/pdf/2608.13431)

