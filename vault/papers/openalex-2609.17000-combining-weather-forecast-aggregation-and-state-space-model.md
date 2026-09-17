---
# CSL-compatible fields
title: "Combining Weather Forecast Aggregation and State-Space Models for Adaptive Probabilistic Electricity Load Forecasting"
author:
  - literal: "Joseph de Vilmarest"
  - literal: "Jonathan Dumas"
  - literal: "Jean Thorey"
issued:
  date-parts:
    - [2026, 9, 15]
url: "https://arxiv.org/abs/2609.17000"

# Custom fields
paper_id: "2609.17000"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "state-space-model"
  - "uncertainty-estimation"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:43:46Z"
created_at: "2026-09-17T09:43:46Z"
---

# Combining Weather Forecast Aggregation and State-Space Models for Adaptive Probabilistic Electricity Load Forecasting

**Authors**: Joseph de Vilmarest, Jonathan Dumas, Jean Thorey
**Date**: 2026-09-15
**Paper ID**: [openalex:2609.17000](https://arxiv.org/abs/2609.17000)

## Summary

This paper introduces an adaptive probabilistic forecasting framework for electricity load that combines generalized additive models with state-space formulations estimated via the Viking algorithm. To handle weather uncertainty, the approach aggregates multiple meteorological forecast providers, utilizing forecast dispersion to improve extreme quantile estimation. Evaluation on French national electricity consumption data demonstrates consistent performance gains over single-provider baselines.

## Key Contributions

- Proposes an adaptive probabilistic forecasting framework combining generalized additive models (GAM) with state-space formulations estimated via the Viking algorithm for electricity load forecasting.
- Extends the framework with GAMLSS for advanced uncertainty quantification where residual variance depends on explanatory variables and incorporates a short-term correction mechanism.
- Demonstrates that aggregating multiple meteorological forecast providers significantly improves point and probabilistic forecasts, particularly for extreme quantiles, outperforming single-provider baselines on French national electricity consumption data.

## Limitations

Evaluated primarily on French national electricity consumption data; generalizability to other power systems or renewable-heavy microgrids requires further study.

## Archivist Review

Reviewed the candidate concept (Viking algorithm) and found that it represents a paper-specific estimation technique rather than a widely recurring or reusable forecasting paradigm. Therefore, no concepts or open questions were approved in accordance with our strict sparsity and novelty guidelines.

### Rejected Candidates
- [concept] Viking algorithm (`viking-algorithm`) - low_impact: The Viking algorithm is an internal estimation method whose general utility across broader machine learning and forecasting literature is insufficiently established.

## Links

- [Abstract](https://arxiv.org/abs/2609.17000)
- [PDF](https://arxiv.org/pdf/2609.17000)

