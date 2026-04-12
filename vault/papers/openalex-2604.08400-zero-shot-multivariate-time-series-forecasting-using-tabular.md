---
# CSL-compatible fields
title: "Zero-shot Multivariate Time Series Forecasting Using Tabular Prior Fitted Networks"
author:
  - literal: "Mayuka Jayawardhana"
  - literal: "Nihal Sharma"
  - literal: "Kazem Meidani"
  - literal: "Bayan Bruss"
  - literal: "Tom Goldstein"
  - literal: "Doron Bergman"
issued:
  date-parts:
    - [2026, 4, 9]
url: "https://arxiv.org/abs/2604.08400"

# Custom fields
paper_id: "2604.08400"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "zero-shot-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "tabpfn-ts"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-12T06:18:08Z"
created_at: "2026-04-12T06:18:08Z"
---

# Zero-shot Multivariate Time Series Forecasting Using Tabular Prior Fitted Networks

**Authors**: Mayuka Jayawardhana, Nihal Sharma, Kazem Meidani, Bayan Bruss, Tom Goldstein, Doron Bergman
**Date**: 2026-04-09
**Paper ID**: [openalex:2604.08400](https://arxiv.org/abs/2604.08400)

## Summary

This paper introduces a framework to perform zero-shot multivariate time series forecasting by leveraging tabular foundation models. By reformulating the multivariate forecasting task into a sequence of scalar regression problems, the authors capture inter-channel dependencies often lost in independent univariate approaches. The method is validated using the TabPFN-TS backbone, demonstrating competitive performance against established state-of-the-art tabular methods.

## Key Contributions

- Introduces a framework that enables zero-shot multivariate time series forecasting by recasting multivariate dependencies into a series of scalar regression problems.
- Enables tabular foundation models to account for inter-channel interactions that are typically ignored by independent univariate forecasting approaches.
- Demonstrates superior performance compared to existing state-of-the-art tabular forecasting baselines using the TabPFN-TS architecture.

## Open Questions & Future Work

- [[ci-vs-cd-superiority-conditions]]

## Key Concepts

- [[tabpfn-ts]]: A time-series specific adaptation of Prior-data Fitted Networks for zero-shot multivariate forecasting.

## Archivist Review

I approved the core architectural concept (TabPFN-TS) as it represents the central methodological contribution of the paper. I also approved the open question regarding the trade-offs between channel-independent and channel-dependent strategies, as this is a fundamental conceptual hurdle for multivariate forecasting that applies far beyond this specific study. I rejected the probabilistic calibration question because it focuses on specific performance deficits rather than a clear theoretical research gap.

### Approved Concepts
- TabPFN-TS: This is a specific architectural adaptation that repurposes tabular foundation models for multivariate forecasting, representing a distinct methodological bridge between domains.

### Approved Open Questions
- CI vs CD Forecasting Performance: This addresses a fundamental trade-off in multivariate forecasting that remains poorly understood as foundation model architectures become more prevalent.

### Rejected Candidates
- [open_question] Probabilistic Forecasting Calibration Challenges (`probabilistic-forecast-calibration`) - low_impact: This is largely a performance benchmarking and error analysis issue rather than a foundational research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2604.08400)
- [PDF](https://arxiv.org/pdf/2604.08400)

