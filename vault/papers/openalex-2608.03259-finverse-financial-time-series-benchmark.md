---
# CSL-compatible fields
title: "FinVerse: Financial Time-Series Benchmark"
author:
  - literal: "Jaehoon Lee"
  - literal: "Jun Seo"
  - literal: "Seunghan Lee"
  - literal: "Tae Yoon Lim"
  - literal: "Dongwan Kang"
  - literal: "Hwanil Choi"
  - literal: "Minjae Kim"
  - literal: "Sungdong Yoo"
  - literal: "Junhyuk Kang"
  - literal: "Sangjun Han"
  - literal: "Soonyoung Lee"
  - literal: "Wonbin Ahn"
issued:
  date-parts:
    - [2026, 8, 4]
url: "https://arxiv.org/abs/2608.03259"

# Custom fields
paper_id: "2608.03259"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
  - "language-model"
architectures:
  []
datasets:
  - "finverse"
concept_slugs:
  []
dataset_slugs:
  - "finverse"
skill: "TimeSeriesSkill"
processed_at: "2026-08-07T06:03:38Z"
created_at: "2026-08-07T06:03:38Z"
---

# FinVerse: Financial Time-Series Benchmark

**Authors**: Jaehoon Lee, Jun Seo, Seunghan Lee, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Minjae Kim, Sungdong Yoo, Junhyuk Kang, Sangjun Han, Soonyoung Lee, Wonbin Ahn
**Date**: 2026-08-04
**Paper ID**: [openalex:2608.03259](https://arxiv.org/abs/2608.03259)

## Summary

FinVerse is a comprehensive financial time-series benchmark designed to evaluate forecasting foundation models using economic relevance rather than uniform point-wise error metrics. Comprising 116,897 financial time series and 78 metrics across 11 families tailored to specific economic meanings, the benchmark reveals that standard foundation models performing well on generic metrics do not necessarily yield useful financial forecasts.

## Key Contributions

- Introduces FinVerse, a large-scale finance-domain time-series benchmark containing 116,897 financial time series and 171.1M observations.
- Defines 11 metric families comprising 78 evaluation metrics assigned based on underlying economic meaning rather than uniform point-wise error.
- Evaluates 43 public time-series forecasting foundation models, demonstrating that strong performance under generic criteria does not translate to financial forecasting utility.

## Limitations

Limited to the financial domain and public forecasting foundation models evaluated within the study.

## Open Questions & Future Work

- [[calendar-and-release-date-alignment]]

## Archivist Review

The paper introduces FinVerse, a major benchmark artifact rather than a novel algorithmic concept. Therefore, FinVerse is approved as a dataset, and the associated open question on calendar/release-date alignment is retained. Concepts are set to empty as the contribution is benchmark-oriented.

### Approved Open Questions
- Calendar and Release-Date Alignment: Crucial for eliminating look-ahead bias and enabling realistic backtesting in financial forecasting models.

### Rejected Candidates
- [concept] FinVerse (`finverse`) - not_novel: FinVerse is primarily a benchmark dataset artifact rather than a standalone algorithmic concept or architectural primitive.

## Datasets

- [[finverse]]

## Links

- [Abstract](https://arxiv.org/abs/2608.03259)
- [PDF](https://arxiv.org/pdf/2608.03259)

