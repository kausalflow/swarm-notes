---
# CSL-compatible fields
title: "From rows to yields: how foundation models for tabular data simplify crop yield prediction"
author:
  - literal: "Filip Sabo"
  - literal: "Michele Meroni"
  - literal: "María Piles"
  - literal: "Martin Claverie"
  - literal: "Fanie Ferreira"
  - literal: "Elna Van Den Berg"
  - literal: "Francesco Collivignarelli"
  - literal: "Felix Rembold"
issued:
  date-parts:
    - [2026, 4, 24]
url: "https://arxiv.org/abs/2506.19046"

# Custom fields
paper_id: "2506.19046"
paper_source: "openalex"
domain: "nlp,time-series"
tags:
  - "tabular-data"
  - "forecasting"
  - "time-series"
  - "benchmark"
  - "foundation-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "tabpfn-ts"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-27T07:29:28Z"
created_at: "2026-04-27T07:29:28Z"
---

# From rows to yields: how foundation models for tabular data simplify crop yield prediction

**Authors**: Filip Sabo, Michele Meroni, María Piles, Martin Claverie, Fanie Ferreira, Elna Van Den Berg, Francesco Collivignarelli, Felix Rembold
**Date**: 2026-04-24
**Paper ID**: [openalex:2506.19046](https://arxiv.org/abs/2506.19046)

## Summary

This study investigates the efficacy of TabPFN, a foundation model for tabular data, in forecasting sub-national crop yields for maize, soybeans, and sunflowers in South Africa. By utilizing dekadal time series of Earth Observation and weather data, the researchers compared TabPFN against several machine learning and baseline approaches using a leave-one-year-out cross-validation strategy. Results indicate that while TabPFN achieves accuracy comparable to traditional machine learning models, its primary advantage lies in its reduced requirements for manual feature engineering and significantly faster tuning cycles.

## Key Contributions

- Evaluated TabPFN for sub-national crop yield forecasting using dekadal Earth Observation and gridded weather data.
- Conducted a comprehensive benchmark comparing TabPFN against six traditional ML models and two baseline models using leave-one-year-out cross-validation.
- Demonstrated that TabPFN provides comparable predictive accuracy to standard ML models while offering significant advantages in reduced feature engineering and faster model tuning.

## Key Concepts

- [[tabpfn-ts]]: A prior-data fitted network architecture functioning as a foundation model for small-to-medium sized tabular datasets.

## Archivist Review

I have approved 'tabpfn-ts' as it represents a significant shift in utilizing foundation models for tabular forecasting tasks which is a highly reusable concept in the time-series domain. The dataset was rejected because it is a routine, domain-specific regional collection that lacks the systemic importance required for a permanent vault entry.

### Approved Concepts
- TabPFN: The paper specifically evaluates the suitability of foundation models designed for tabular data as a substitute for traditional feature-engineered forecasting models in agriculture.

### Rejected Candidates
- [dataset] South Africa sub-national maize, soybean, and sunflower yield data (`south-africa-crop-yield-data`) - low_impact: Routine regional agricultural datasets that do not constitute a high-impact, standalone resource for the broader ML community.

## Links

- [Abstract](https://arxiv.org/abs/2506.19046)
- [PDF](https://arxiv.org/pdf/2506.19046)

