---
# CSL-compatible fields
title: "When Do Foundation Models Pay Off? A Break-Even Analysis of Pretrained Time Series Forecasters"
author:
  - literal: "Nicholas Tan Jerome"
  - literal: "Frank Simon"
issued:
  date-parts:
    - [2026, 7, 6]
url: "https://arxiv.org/abs/2607.04919"

# Custom fields
paper_id: "2607.04919"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "llm"
  - "zero-shot-learning"
  - "lora"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "break-even-analysis-for-time-series-foundation-models"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-09T08:17:59Z"
created_at: "2026-07-09T08:17:59Z"
---

# When Do Foundation Models Pay Off? A Break-Even Analysis of Pretrained Time Series Forecasters

**Authors**: Nicholas Tan Jerome, Frank Simon
**Date**: 2026-07-06
**Paper ID**: [openalex:2607.04919](https://arxiv.org/abs/2607.04919)

## Summary

This paper presents a systematic break-even analysis to determine the conditions under which time series foundation models provide superior performance compared to classical forecasting baselines like XGBoost and ARIMA. Evaluating zero-shot and LoRA fine-tuned models across 30 datasets, the authors identify critical data-volume thresholds and find that foundation models do not consistently outperform classical methods. Based on these results, they propose a two-step decision framework to guide practitioners in choosing between foundation models and traditional approaches, ultimately preventing unnecessary infrastructure expenditures.

## Key Contributions

- Provides the first systematic break-even analysis comparing foundation models (Chronos, Moirai, Lag-Llama) against classical baselines across 30 datasets.
- Establishes a robust deployment rule: for series with fewer than 700 samples and significant seasonality, zero-shot foundation models are preferred over fine-tuning or classical methods.
- Operationalizes findings into a two-step decision framework based on dataset length and seasonality to optimize infrastructure investment.

## Open Questions & Future Work

- [[predicting-time-series-breakeven-thresholds]]

## Key Concepts

- [[break-even-analysis-for-time-series-foundation-models]]: A methodology for determining the data-volume threshold where foundation model performance exceeds classical statistical baselines for time series forecasting.

## Archivist Review

The paper provides a valuable methodology for evaluating the economic and performance trade-offs of time series foundation models. I approved the break-even analysis as a core concept for deployment evaluation and formalized the open question regarding the automated prediction of these thresholds. I rejected the original open question candidate only to rename it for better clarity in the vault.

### Approved Concepts
- Break-even analysis for time series foundation models: Establishes a quantitative decision framework for determining when foundation models provide performance gains over classical statistical baselines.

### Approved Open Questions
- Predicting Time Series Break-Even Thresholds: Establishing reliable predictive tools for model selection is critical for practitioners to avoid inefficient infrastructure deployment, such as the unnecessary use of GPU-intensive foundation models when classical methods would suffice.

### Rejected Candidates
- [open_question] Predicting Time Series Break-Even Points (`predicting-time-series-breakeven`) - other: Renamed for better specificity and consistency with vault naming standards.

## Links

- [Abstract](https://arxiv.org/abs/2607.04919)
- [PDF](https://arxiv.org/pdf/2607.04919)

