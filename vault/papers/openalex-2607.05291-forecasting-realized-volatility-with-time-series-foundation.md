---
# CSL-compatible fields
title: "Forecasting Realized Volatility with Time Series Foundation Models: A Comparison with Econometric Benchmarks"
author:
  - literal: "Alessio Brini"
issued:
  date-parts:
    - [2026, 7, 6]
url: "https://arxiv.org/abs/2607.05291"

# Custom fields
paper_id: "2607.05291"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "language-model"
  - "llm"
architectures:
  []
datasets:
  - "volare"
concept_slugs:
  []
dataset_slugs:
  - "volare"
skill: "TimeSeriesSkill"
processed_at: "2026-07-09T08:17:52Z"
created_at: "2026-07-09T08:17:52Z"
---

# Forecasting Realized Volatility with Time Series Foundation Models: A Comparison with Econometric Benchmarks

**Authors**: Alessio Brini
**Date**: 2026-07-06
**Paper ID**: [openalex:2607.05291](https://arxiv.org/abs/2607.05291)

## Summary

This paper evaluates the performance of nine pretrained time series foundation models (TSFMs) against traditional econometric benchmarks for forecasting realized volatility using the VOLARE dataset. The study finds that TSFMs provide no uniform improvement over the Log-HAR benchmark, with most gains attributable to scale and level biases rather than improved dynamics. The author shows that an equal-weight ensemble of a TSFM and an econometric model provides the most robust performance, suggesting that the choice of architecture is often more critical than the category of model chosen.

## Key Contributions

- Conducts a systematic benchmarking of nine zero-shot time series foundation models (TSFMs) against eight econometric models, including the HAR family, for realized volatility forecasting across 50 assets.
- Demonstrates that TSFMs do not consistently outperform simple econometric benchmarks like Log-HAR, with performance benefits often limited to specific assets or biased by scale/level errors.
- Introduces a simple equal-weight ensemble of Tiny Time Mixers (TTM) and Log-HAR that consistently enters the Model Confidence Set for 98-100% of assets, surpassing the performance of individual models.

## Open Questions & Future Work

- [[zero-shot-tsfm-vs-econometric-volatility-forecasting]]

## Archivist Review

The paper provides a rigorous systematic comparison between foundation models and established econometric benchmarks for volatility, showing that the supposed gains of the former are largely driven by calibration rather than superior dynamic modeling. I have approved the VOLARE dataset for its role in this benchmarking, and the core open question regarding the comparative performance of TSFMs vs. econometric benchmarks in finance, as this is a central, unresolved debate in the field.

### Approved Open Questions
- TSFM vs. Econometric Volatility Forecasting: Establishing whether the performance edge of TSFMs in finance is a robust informational gain versus a fragile calibration artifact is critical for deciding whether to integrate these models into existing risk management frameworks.

### Rejected Candidates
- [dataset] VOLARE (`volare-dataset`) - other: This is just the dataset name, not a full title/slug candidate I need to reject in favor of the clean one. Wait, I am approving VOLARE as a dataset.

## Datasets

- [[volare]]

## Links

- [Abstract](https://arxiv.org/abs/2607.05291)
- [PDF](https://arxiv.org/pdf/2607.05291)

