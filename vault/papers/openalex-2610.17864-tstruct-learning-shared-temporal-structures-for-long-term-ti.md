---
# CSL-compatible fields
title: "TStruct: Learning Shared Temporal Structures for Long-Term Time-Series Forecasting"
author:
  - literal: "Yangze Li"
  - literal: "Zhengyang Zhou"
  - literal: "Qihe Huang"
  - literal: "Pengkun Wang"
  - literal: "Binwu Wang"
  - literal: "Yang Wang"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.17864"

# Custom fields
paper_id: "2610.17864"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "long-context"
architectures:
  []
datasets:
  []
concept_slugs:
  - "tstruct"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-16T09:22:55Z"
created_at: "2026-10-16T09:22:55Z"
---

# TStruct: Learning Shared Temporal Structures for Long-Term Time-Series Forecasting

**Authors**: Yangze Li, Zhengyang Zhou, Qihe Huang, Pengkun Wang, Binwu Wang, Yang Wang
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.17864](https://arxiv.org/abs/2610.17864)

## Summary

The paper introduces TStruct, a network designed for long-term time-series forecasting that addresses non-stationarity and noise by learning shared temporal relationship structures. By parameterizing a set of shared temporal dependency matrices and combining them using dynamic sample information and static variable priors, TStruct avoids unconstrained fitting of incidental temporal interactions. Empirical evaluations demonstrate that TStruct consistently outperforms strong forecasting baselines while maintaining high computational efficiency.

## Key Contributions

- Demonstrated that samples from different temporal positions and variables exhibit shared dominant temporal relationship structures that recur stably.
- Proposed TStruct, which parameterizes a set of shared temporal dependency matrices combined via dynamic sample information and static variable priors.
- Achieved superior forecasting accuracy while maintaining high computational efficiency compared to strong baselines across time-series benchmarks.

## Open Questions & Future Work

- [[resolution-adaptive-temporal-structures]]

## Key Concepts

- [[tstruct]]: A temporal structure network that learns shared and generalizable temporal dependencies through soft allocation of dynamic sample and static variable priors over shared temporal dependency matrices.

## Archivist Review

Approved the TStruct concept for its novel shared temporal dependency parameterization and soft-allocation mechanism. Approved one open question on resolution-adaptive temporal structures due to its clarity on patch-size constraints. Rejected the second open question as speculative future work on foundation model scaling.

### Approved Concepts
- TStruct: Introduces a novel framework that directly parameterizes shared temporal dependency matrices and combines them using dynamic sample information and static variable priors for long-term time-series forecasting.

### Approved Open Questions
- Resolution-Adaptive Temporal Structures: Crucial for building multi-scale and resolution-agnostic time series models that can seamlessly handle varying observation frequencies and input lengths.

### Rejected Candidates
- [open_question] Temporal Structure Foundation Models (`temporal-structure-foundation-models`) - low_impact: Resembles boilerplate future work about large-scale foundation model scaling rather than a concrete technical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.17864)
- [PDF](https://arxiv.org/pdf/2610.17864)

