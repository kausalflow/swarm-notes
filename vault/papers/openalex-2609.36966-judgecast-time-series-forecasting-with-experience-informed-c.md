---
# CSL-compatible fields
title: "JudgeCast: Time Series Forecasting with Experience-Informed Covariate Judgements"
author:
  - literal: "Donguk Kwon"
  - literal: "Wooseok Jeong"
  - literal: "Dongha Lee"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.36966"

# Custom fields
paper_id: "2609.36966"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "llm"
  - "language-model"
  - "retrieval-augmented-generation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "judgecast"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-01T11:14:22Z"
created_at: "2026-10-01T11:14:22Z"
---

# JudgeCast: Time Series Forecasting with Experience-Informed Covariate Judgements

**Authors**: Donguk Kwon, Wooseok Jeong, Dongha Lee
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.36966](https://arxiv.org/abs/2609.36966)

## Summary

JudgeCast is an experience-based framework for time series forecasting with covariates that combines a frozen time series foundation model with a frozen large language model. It decouples the forecasting pipeline into explicit covariate-wise judgment and numerical adjustment stages, using observed residuals to reconstruct and validate alternative judgments over time. Extensive experiments across diverse real-world datasets demonstrate that JudgeCast outperforms strong baselines.

## Key Contributions

- Introduces JudgeCast, an experience-based time series forecasting framework that leverages a frozen time series foundation model and a frozen LLM for covariate-informed judgmental adjustment.
- Proposes a two-stage adjustment process that first forms explicit covariate-wise judgments before determining the numerical adjustment.
- Implements a residual-guided experience reconstruction mechanism to evaluate alternative judgments and retain validated experience for subsequent forecasting contexts.

## Open Questions & Future Work

- [[mitigating-adjustment-failure-modes-time-series]]

## Key Concepts

- [[judgecast]]: An experience-based framework for time series forecasting that forms explicit covariate-wise judgments using frozen LLMs to adjust time series foundation model forecasts.

## Archivist Review

Approved the core framework concept 'JudgeCast' as a novel paradigm for combining frozen TSFMs and LLMs with experience-informed covariate adjustments, alongside an open question addressing failure modes in judgmental adjustments for time series forecasting. Strict adherence to the scarcity and quality policy was maintained.

### Approved Concepts
- JudgeCast: Central framework introduced for time series forecasting via experience-informed covariate judgments using frozen TSFMs and LLMs.

### Approved Open Questions
- Mitigating Adjustment Failure Modes: Understanding and resolving failure modes in non-parametric, experience-guided adjustment frameworks is crucial for deploying reliable LLM-based time series forecasting systems in high-stakes real-world domains.

## Links

- [Abstract](https://arxiv.org/abs/2609.36966)
- [PDF](https://arxiv.org/pdf/2609.36966)

