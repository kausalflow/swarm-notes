---
# CSL-compatible fields
title: "How Good Can Linear Models Be for Time-Series Forecasting?"
author:
  - literal: "Lang Huang"
  - literal: "Jinglue Xu"
  - literal: "Luke Darlow"
issued:
  date-parts:
    - [2026, 6, 25]
url: "https://arxiv.org/abs/2606.27282"

# Custom fields
paper_id: "2606.27282"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "linear-model"
  - "benchmark"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "optimal-lookback-diagnostic"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-28T08:15:32Z"
created_at: "2026-06-28T08:15:32Z"
---

# How Good Can Linear Models Be for Time-Series Forecasting?

**Authors**: Lang Huang, Jinglue Xu, Luke Darlow
**Date**: 2026-06-25
**Paper ID**: [openalex:2606.27282](https://arxiv.org/abs/2606.27282)

## Summary

This paper challenges the prevailing trend of scaling time-series models by demonstrating that highly optimized linear models can match or outperform deep architectures like Transformers. By using Ridge regression as a testbed, the authors systematically optimize preprocessing, regularization, and context length across multiple benchmarks. Their findings reveal that optimal hyperparameters, such as lookback length, are deeply series-specific and often exhibit non-monotonic relationships with forecast horizons. The study highlights that much of the performance gap in modern time-series forecasting can be bridged through better data understanding rather than increased architectural capacity.

## Key Contributions

- Demonstrates that simple Ridge regression with optimized preprocessing can outperform sophisticated Transformer, MLP, and CNN architectures on six of eight standard benchmarks.
- Identifies three key patterns in hyperparameter sensitivity for time series, including the non-monotonic relationship between lookback length and forecast horizon.
- Establishes a diagnostic framework using optimized linear model hyperparameters to reveal intrinsic temporal data structures that are typically opaque in deep learning models.

## Open Questions & Future Work

- [[unified-preprocessing-benchmarking-for-forecasting]]

## Key Concepts

- [[optimal-lookback-diagnostic]]: A diagnostic approach for time-series forecasting that uses series-specific optimal lookback lengths to reveal intrinsic temporal data structures.

## Archivist Review

I approved the lookback diagnostic concept as it provides a valuable, model-agnostic lens for understanding temporal data that transcends any specific architecture. The open question regarding unified benchmarking was approved to address the persistent ambiguity in forecasting literature between model capacity and preprocessing efficacy. I rejected the datasets because they are standard, existing benchmarks that do not warrant new entries.

### Approved Concepts
- Optimal lookback diagnostic: Challenges the common assumption that increasing lookback length monotonically improves forecasting accuracy and provides a lens for model-agnostic data analysis.

### Approved Open Questions
- Unified Benchmarking Frameworks: This is critical for fairly assessing model-driven performance gains versus gains achieved through more rigorous data engineering or preprocessing.

### Rejected Candidates
- [dataset] ETTh1 (`ETTh1`) - duplicate_existing: ETTh1 is a standard, widely-used benchmark dataset and does not merit a new standalone vault note.
- [dataset] Traffic (`Traffic`) - duplicate_existing: Traffic is a standard, widely-used benchmark dataset and does not merit a new standalone vault note.

## Links

- [Abstract](https://arxiv.org/abs/2606.27282)
- [PDF](https://arxiv.org/pdf/2606.27282)

