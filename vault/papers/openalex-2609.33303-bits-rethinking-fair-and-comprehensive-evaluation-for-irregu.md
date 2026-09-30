---
# CSL-compatible fields
title: "BITS: Rethinking Fair and Comprehensive Evaluation for Irregular Time Series Forecasting"
author:
  - literal: "Keyang Yan"
  - literal: "Linfeng Wang"
  - literal: "Tianen Shen"
  - literal: "Xiangfei Qiu"
  - literal: "Ruitong Zhang"
  - literal: "Miao Hao"
  - literal: "Jilin Hu"
  - literal: "Chenjuan Guo"
  - literal: "Bin Yang"
  - literal: "Christian S. Jensen"
issued:
  date-parts:
    - [2026, 9, 27]
url: "https://arxiv.org/abs/2609.33303"

# Custom fields
paper_id: "2609.33303"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
  - "missing-data"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:48:24Z"
created_at: "2026-09-30T10:48:24Z"
---

# BITS: Rethinking Fair and Comprehensive Evaluation for Irregular Time Series Forecasting

**Authors**: Keyang Yan, Linfeng Wang, Tianen Shen, Xiangfei Qiu, Ruitong Zhang, Miao Hao, Jilin Hu, Chenjuan Guo, Bin Yang, Christian S. Jensen
**Date**: 2026-09-27
**Paper ID**: [openalex:2609.33303](https://arxiv.org/abs/2609.33303)

## Summary

Despite advancements in irregular time series forecasting, the field lacks unified and comprehensive evaluation protocols. To address this, the authors propose BITS, a standardized benchmark encompassing eleven datasets across nine domains characterized by missing rates, patterns, sampling irregularity, and skewness. BITS integrates regular and irregular forecasting models into a unified pipeline with both error-based and non-error-based metrics, revealing that no single modeling strategy dominates and metric choices impact model rankings.

## Key Contributions

- Proposes BITS, a standardized, reproducible, and extensible benchmark for irregular time series forecasting covering eleven datasets from nine domains.
- Characterizes datasets across missing rates, missing pattern complexity, sampling irregularity, and skewness to analyze performance drivers.
- Establishes a unified pipeline integrating regular and irregular time series methods under consistent settings with multi-dimensional error and non-error metrics.
- Reveals that method performance varies widely across irregularity characteristics and that metric choice significantly alters model rankings.

## Archivist Review

Applied strict curation standards: benchmark packages and generic calls for more dataset expansion do not meet the threshold for permanent vault notes.

### Rejected Candidates
- [concept] BITS (`bits`) - not_reusable: Benchmark evaluation suites and frameworks are generally treated as datasets or benchmark overviews rather than standalone methodological concepts in this vault.
- [open_question] Expanding Irregular Time Series Benchmarks (`expanding-irregular-time-series-benchmarks`) - low_impact: This is a routine call for expanding benchmark datasets and baselines rather than a deep technical or mathematical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.33303)
- [PDF](https://arxiv.org/pdf/2609.33303)

