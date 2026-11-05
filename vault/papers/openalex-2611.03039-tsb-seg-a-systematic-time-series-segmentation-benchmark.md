---
# CSL-compatible fields
title: "TSB-SEG: A Systematic Time-Series Segmentation Benchmark"
author:
  - literal: "F Chavelli"
  - literal: "Arik Ermshaus"
  - literal: "Fan Yang"
  - literal: "Patrick Schäfer"
  - literal: "John Paparrizos"
  - literal: "Paul Boniol"
issued:
  date-parts:
    - [2026, 11, 2]
url: "https://arxiv.org/abs/2611.03039"

# Custom fields
paper_id: "2611.03039"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "benchmark"
  - "dataset"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-05T12:51:32Z"
created_at: "2026-11-05T12:51:32Z"
---

# TSB-SEG: A Systematic Time-Series Segmentation Benchmark

**Authors**: F Chavelli, Arik Ermshaus, Fan Yang, Patrick Schäfer, John Paparrizos, Paul Boniol
**Date**: 2026-11-02
**Paper ID**: [openalex:2611.03039](https://arxiv.org/abs/2611.03039)

## Summary

Time-series segmentation encompasses both Change Point Detection (CPD) and State Detection (SD), yet the literature remains fragmented due to narrow evaluations and isolated communities. To address these gaps, the authors present TSB-SEG, a unified benchmark integrating 592 univariate and multivariate time series from 8 heterogeneous datasets alongside 26 algorithms spanning five decades. Using a novel two-pool evaluation design and the open-source tsseg library, the systematic evaluation reveals insights regarding hyperparameter sensitivity, domain-specific performance, and the relationship between CPD and SD.

## Key Contributions

- Introduces TSB-SEG, a unified benchmark for time-series segmentation covering 592 univariate and multivariate time series across 8 heterogeneous datasets and 26 algorithms.
- Establishes a two-pool evaluation design featuring a scalable main pool for aggregate rankings and an extended-scope pool for computationally intensive detectors.
- Provides the open-source tsseg library ensuring full reproducibility and systematic comparison across five decades of progress.
- Delivers empirical insights showing that no single detector dominates across domains, per-dataset hyperparameter tuning is decisive, and CPD accuracy serves as an imperfect proxy for SD accuracy.

## Open Questions & Future Work

- [[multivariate-streaming-time-series-segmentation]]

## Archivist Review

Applied strict criteria. No permanent concepts or datasets were approved as TSB-SEG is primarily a benchmarking paper and library contribution rather than a novel standalone reusable algorithmic mechanism or benchmark dataset new to the literature. One open question on multivariate and streaming segmentation was approved to track future methodological gaps.

### Approved Open Questions
- Multivariate and Streaming Segmentation: Crucial for scaling time-series segmentation models to real-world industrial and IoT streaming applications involving high-dimensional sensor arrays and gradual regime shifts.

### Rejected Candidates
- [open_question] Multivariate and Streaming Segmentation (`multivariate-streaming-time-series-segmentation`) - generic: The open question is valuable but sparseness limit dictates approving at most 2, though here we only submitted 1. Wait, let's keep it since it meets the bar.

## Links

- [Abstract](https://arxiv.org/abs/2611.03039)
- [PDF](https://arxiv.org/pdf/2611.03039)

