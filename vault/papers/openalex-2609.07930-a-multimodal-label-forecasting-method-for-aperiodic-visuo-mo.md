---
# CSL-compatible fields
title: "A Multimodal Label Forecasting Method for Aperiodic Visuo-Motor Time Series"
author:
  - literal: "Borui He"
  - literal: "Garrett E. Katz"
issued:
  date-parts:
    - [2026, 9, 7]
url: "https://arxiv.org/abs/2609.07930"

# Custom fields
paper_id: "2609.07930"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "multimodal"
  - "forecasting"
  - "transformer"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-10T09:15:34Z"
created_at: "2026-09-10T09:15:34Z"
---

# A Multimodal Label Forecasting Method for Aperiodic Visuo-Motor Time Series

**Authors**: Borui He, Garrett E. Katz
**Date**: 2026-09-07
**Paper ID**: [openalex:2609.07930](https://arxiv.org/abs/2609.07930)

## Summary

This paper addresses time series forecasting in aperiodic visuo-motor settings, specifically focusing on anticipating falls during diverse humanoid locomotion using egocentric vision and proprioception. The authors introduce two new benchmarks—one simulated and one real-world—demonstrating that conventional methods relying on periodicity fail on these tasks. They propose a novel deep learning architecture utilizing both endogenous and exogenous variables alongside an i.i.d. sampling training strategy, outperforming prior art significantly on both datasets.

## Key Contributions

- Proposes a multimodal label forecasting method for aperiodic visuo-motor time series applied to anticipating falls during humanoid locomotion.
- Introduces two new benchmark datasets (simulation and real hardware) exhibiting violated periodicity where recent deep TSF methods struggle.
- Achieves statistically significant performance improvements of 12.73% or more on real hardware data and 10.40% or more on simulation data compared to prior art baselines.

## Open Questions & Future Work

- [[generalizing-aperiodic-tsf-models]]

## Archivist Review

Applied strict scarcity and relevance filters. No concepts or datasets met the rigorous threshold for standalone vault notes, and the single open question was rejected as a broad, generic architectural extension request.

### Approved Open Questions
- Generalizing Aperiodic TSF Models: Improving generalization and discovering lightweight architectural modules for aperiodic time series is crucial for expanding visuo-motor forecasting beyond robotics.

### Rejected Candidates
- [open_question] Generalizing Aperiodic TSF Models (`generalizing-aperiodic-tsf-models`) - low_impact: The open question requests general architectural improvements and domain transfer, which is too broad and standard.

## Links

- [Abstract](https://arxiv.org/abs/2609.07930)
- [PDF](https://arxiv.org/pdf/2609.07930)

