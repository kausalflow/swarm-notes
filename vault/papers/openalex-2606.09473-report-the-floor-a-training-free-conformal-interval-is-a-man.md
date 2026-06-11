---
# CSL-compatible fields
title: "Report the Floor: A Training-Free Conformal Interval Is a Mandatory Baseline for Probabilistic Time-Series Forecasting"
author:
  - literal: "Valery Manokhin"
issued:
  date-parts:
    - [2026, 6, 8]
url: "https://arxiv.org/abs/2606.09473"

# Custom fields
paper_id: "2606.09473"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "conformal-prediction"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "conformalnaive"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-11T09:06:52Z"
created_at: "2026-06-11T09:06:52Z"
---

# Report the Floor: A Training-Free Conformal Interval Is a Mandatory Baseline for Probabilistic Time-Series Forecasting

**Authors**: Valery Manokhin
**Date**: 2026-06-08
**Paper ID**: [openalex:2606.09473](https://arxiv.org/abs/2606.09473)

## Summary

This paper establishes a training-free conformal interval method, ConformalNaive, as a necessary baseline for evaluating probabilistic time-series forecasters. By applying split-conformal residual quantiles to last-value forecasts, the method proves highly competitive against specialized approaches like NPTS and Conformal Seasonal Pools in online settings. The author demonstrates that these trivial baselines often exhibit superior calibration compared to complex neural models, advocating for their inclusion in any comparative study of probabilistic forecasting performance.

## Key Contributions

- Introduces ConformalNaive, a training-free baseline that outperforms several established probabilistic forecasting methods across 2,217 real-world time series.
- Demonstrates that trivial conformal floors often provide better calibration than complex trained neural forecasters in online settings.
- Proposes ConformalNaive+, a horizon-adaptive selector that dynamically chooses between random-walk and seasonal baselines to restore coverage.

## Open Questions & Future Work

- [[horizon-adaptive-conformal-selection]]

## Key Concepts

- [[conformalnaive]]: A training-free conformal interval that uses a last-value point forecast combined with split-conformal residual quantiles to create a robust baseline.

## Archivist Review

The paper provides a strong argument for the standardization of training-free conformal intervals as performance baselines. ConformalNaive is approved as a fundamental methodology for future forecasting evaluation. Horizon-adaptive conformal selection is approved as a critical open question to address the performance limitations of fixed-window conformal intervals. Datasets were rejected as they represent aggregate benchmark collections rather than specific, novel, or singular research datasets.

### Approved Concepts
- ConformalNaive: Establishes a critical, zero-cost performance floor for probabilistic time-series forecasting, forcing rigorous evaluation of learned methods.

### Approved Open Questions
- Horizon-adaptive conformal selection methods: Bridges the performance gap between simple conformal floors and the theoretical oracle performance required for multi-step horizon accuracy.

### Rejected Candidates
- [dataset] Monash (`Monash`) - generic: Generic collection name for a broad suite of datasets rather than a specific identifiable corpus.
- [dataset] LTSF (`LTSF`) - not_novel: Routine benchmark suite rather than a specific novel dataset.

## Links

- [Abstract](https://arxiv.org/abs/2606.09473)
- [PDF](https://arxiv.org/pdf/2606.09473)

