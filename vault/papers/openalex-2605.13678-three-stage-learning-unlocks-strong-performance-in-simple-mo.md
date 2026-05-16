---
# CSL-compatible fields
title: "Three-Stage Learning Unlocks Strong Performance in Simple Models for Long-Term Time Series Forecasting"
author:
  - literal: "Zhenan Yu"
  - literal: "Guangxin Jiang"
  - literal: "Jin Yang"
issued:
  date-parts:
    - [2026, 5, 13]
url: "https://arxiv.org/abs/2605.13678"

# Custom fields
paper_id: "2605.13678"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "efficient-transformer"
architectures:
  []
datasets:
  []
concept_slugs:
  - "stair-training-paradigm"
  - "alpha-revin"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-16T07:09:05Z"
created_at: "2026-05-16T07:09:05Z"
---

# Three-Stage Learning Unlocks Strong Performance in Simple Models for Long-Term Time Series Forecasting

**Authors**: Zhenan Yu, Guangxin Jiang, Jin Yang
**Date**: 2026-05-13
**Paper ID**: [openalex:2605.13678](https://arxiv.org/abs/2605.13678)

## Summary

This paper presents STAIR, a training paradigm that improves the performance of simple linear and MLP-based time series models by replacing complex architectural priors with a three-stage learning process. The method sequentially learns common temporal dynamics, variable-specific patterns, and residual cross-variable interactions. To improve this process, the authors also introduce alpha-RevIN to soften the normalization constraints typical of standard RevIN approaches, demonstrating that simple models can match or outperform advanced state-of-the-art forecasters.

## Key Contributions

- Proposes STAIR, a three-stage training paradigm that decomposes time series forecasting into shared dynamics learning, variable-specific fine-tuning, and residual cross-variable integration.
- Introduces alpha-RevIN to mitigate the overly strong normalization priors of traditional RevIN, enhancing the flexibility of simple MLP-based forecasters.
- Demonstrates that complex architectural features can be replaced by effective training strategies, achieving state-of-the-art results on nine standard long-term forecasting benchmarks using shallow MLPs or linear predictors.

## Open Questions & Future Work

- [[automated-normalization-selection]]

## Key Concepts

- [[stair-training-paradigm]]: A three-stage training paradigm for time series forecasting that progressively learns common dynamics, variable-specific patterns, and cross-variable information.
- [[alpha-revin]]: An enhanced normalization technique that relaxes the strong normalization priors typically found in RevIN.

## Archivist Review

The paper's contribution of a modular training paradigm (STAIR) to replace architectural complexity is a significant and reusable shift in forecasting methodology. I have also approved the alpha-RevIN concept and the associated open question regarding automated normalization strength, as these address a pervasive issue in time series preprocessing that will likely remain relevant in future research.

### Approved Concepts
- STAIR training paradigm: It shifts the focus from model architecture complexity to a modular three-stage training strategy to improve performance in simple time series models.
- alpha-RevIN: It addresses the limitations of standard instance normalization (RevIN) in time series forecasting, which is a common bottleneck in current models.

### Approved Open Questions
- Automated Normalization Strength Selection: Normalization is a critical preprocessing step in time series forecasting, and a non-adaptive approach risks either over-stationarizing (losing information) or under-stationarizing (failing to handle distribution shifts). Automating this would make models more robust and easier to deploy across diverse datasets.

## Links

- [Abstract](https://arxiv.org/abs/2605.13678)
- [PDF](https://arxiv.org/pdf/2605.13678)

