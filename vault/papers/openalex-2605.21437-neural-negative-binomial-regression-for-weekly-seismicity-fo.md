---
# CSL-compatible fields
title: "Neural Negative Binomial Regression for Weekly Seismicity Forecasting: Per-Cell Dispersion Estimation and Tail Risk Assessment"
author:
  - literal: "Alim Igilik"
issued:
  date-parts:
    - [2026, 5, 20]
url: "https://arxiv.org/abs/2605.21437"

# Custom fields
paper_id: "2605.21437"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  - "per-cell-dispersion-estimation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-23T07:25:41Z"
created_at: "2026-05-23T07:25:41Z"
---

# Neural Negative Binomial Regression for Weekly Seismicity Forecasting: Per-Cell Dispersion Estimation and Tail Risk Assessment

**Authors**: Alim Igilik
**Date**: 2026-05-20
**Paper ID**: [openalex:2605.21437](https://arxiv.org/abs/2605.21437)

## Summary

This paper addresses the systematic violation of the Poisson hypothesis in seismic forecasting by replacing global dispersion assumptions with a flexible neural framework. The proposed EarthquakeNet architecture learns an endogenous, per-cell overdispersion parameter, effectively capturing spatial heterogeneity in earthquake clustering. Experimental results on Central Asian seismic data demonstrate superior calibration in the tail regime, providing a robust tool for probabilistic risk-aware seismic alerting.

## Key Contributions

- Proposes EarthquakeNet, a neural architecture for weekly seismicity forecasting that models per-cell overdispersion endogenously using spatial embeddings and an MLP.
- Demonstrates that standard Poisson assumptions are statistically rejected for seismic data in Central Asia through boundary-corrected likelihood-ratio tests.
- Achieves 8.6% reduction in mean pinball deviation and 12.5% reduction in CRPS for extreme-event forecasting (tail regime) compared to negative binomial GLM baselines.

## Open Questions & Future Work

- [[modeling-cross-cell-spatial-dependencies]]

## Key Concepts

- [[per-cell-dispersion-estimation]]: A technique for count-based spatiotemporal forecasting that uses a neural network to learn an endogenous, per-cell overdispersion parameter instead of assuming global homogeneity.

## Archivist Review

I approved the concept of 'Per-cell Dispersion Estimation' as a reusable mechanism for count forecasting and the open question regarding 'Modeling cross-cell spatial dependencies' to address the limitations of marginal predictive frameworks. I rejected 'EarthquakeNet' as an internal architecture name, preferring the broader mechanism it represents. I maintained a lean approach to keep the knowledge vault focused on extensible, high-level research concepts.

### Approved Concepts
- Per-cell Dispersion Estimation: It replaces the common assumption of global overdispersion in count forecasting with a flexible, data-driven per-cell mechanism that accounts for spatial heterogeneity.

### Approved Open Questions
- Modeling cross-cell spatial dependencies: Models ignoring cross-cell interactions miss the core physical mechanism of earthquake triggering, which is essential for advancing beyond marginal predictors to full joint generative spatiotemporal models.

### Rejected Candidates
- [concept] EarthquakeNet (`earthquakenet`) - subcomponent_of_broader_mechanism: The concept of EarthquakeNet is a specific implementation of per-cell dispersion estimation; the overarching mechanism is more representative and reusable.
- [open_question] Spatial conditional independence assumption (`spatial-conditional-independence-in-seismicity-forecasting`) - duplicate_existing: The background and description are slightly better captured by the more general topic of cross-cell dependencies.

## Links

- [Abstract](https://arxiv.org/abs/2605.21437)
- [PDF](https://arxiv.org/pdf/2605.21437)

