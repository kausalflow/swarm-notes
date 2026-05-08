---
# CSL-compatible fields
title: "Graph Convolutional Support Vector Regression for Robust Spatiotemporal Forecasting of Urban Air Pollution"
author:
  - literal: "Nourin Jahan"
  - literal: "Madhurima Panja"
  - literal: "M. T."
  - literal: "Tanujit Chakraborty"
issued:
  date-parts:
    - [2026, 5, 5]
url: "https://arxiv.org/abs/2605.03795"

# Custom fields
paper_id: "2605.03795"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "graph-neural-network"
  - "conformal-prediction"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "graph-convolutional-support-vector-regression"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-08T06:27:32Z"
created_at: "2026-05-08T06:27:32Z"
---

# Graph Convolutional Support Vector Regression for Robust Spatiotemporal Forecasting of Urban Air Pollution

**Authors**: Nourin Jahan, Madhurima Panja, M. T., Tanujit Chakraborty
**Date**: 2026-05-05
**Paper ID**: [openalex:2605.03795](https://arxiv.org/abs/2605.03795)

## Summary

Urban air quality forecasting is complicated by nonlinear, nonstationary dynamics and frequent anomalies due to traffic and meteorological shifts. The authors propose the Graph Convolutional Support Vector Regression (GCSVR) framework, which utilizes graph convolutions to model spatial relationships among monitoring stations and SVR to maintain temporal stability against outliers. The model is further enhanced with conformal prediction to deliver calibrated uncertainty estimates, demonstrating superior robustness and accuracy across diverse urban environments in India.

## Key Contributions

- Proposes Graph Convolutional Support Vector Regression (GCSVR) to jointly capture spatiotemporal dependencies and mitigate sensitivity to outliers.
- Integrates conformal prediction with GCSVR to provide reliable, uncertainty-aware prediction intervals for urban air quality.
- Demonstrates robust predictive accuracy across varied metropolitan environments (Delhi and Mumbai) compared to established spatiotemporal benchmarks.

## Open Questions & Future Work

- [[integrating-covariates-dynamic-graphs-air-quality]]

## Key Concepts

- [[graph-convolutional-support-vector-regression]]: A hybrid model that leverages graph convolutions for inter-station spatial dependencies and support vector regression for robust, nonlinear temporal dynamics.

## Archivist Review

I approved the core architectural proposal (GCSVR) as a reusable strategy for robust spatiotemporal forecasting and the open question regarding covariate and dynamic graph integration, as these are substantial challenges for air quality forecasting. I did not include any datasets as the paper used routine regional air quality records. The overall review applied high standards for architectural novelty and research bottleneck significance.

### Approved Concepts
- Graph Convolutional Support Vector Regression: The framework addresses the need for robust temporal modeling (via SVR) within a graph-based spatial architecture (via GCN) to handle outlier-prone spatiotemporal time series.

### Approved Open Questions
- Integrating Covariates in Air Quality Forecasting: Integrating external environmental factors is critical for transitioning from purely data-driven models to more physically consistent and accurate forecasting systems, particularly in regions where meteorological variability dominates pollution dispersion.

## Links

- [Abstract](https://arxiv.org/abs/2605.03795)
- [PDF](https://arxiv.org/pdf/2605.03795)

