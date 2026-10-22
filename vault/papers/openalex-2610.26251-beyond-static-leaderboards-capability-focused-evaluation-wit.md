---
# CSL-compatible fields
title: "Beyond Static Leaderboards: Capability-Focused Evaluation with Structural Diversity for Time Series Foundation Models"
author:
  - literal: "Hongyin Zhang"
  - literal: "项明义"
  - literal: "CHEN Rongzhao"
  - literal: "YanKai Wang"
  - literal: "Jialin Qiao"
  - literal: "Xiangdong Huang"
  - literal: "Xiaoou Ding"
  - literal: "Chen Wang"
  - literal: "Zhongyi Pei"
  - literal: "Jianmin Wang"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2610.26251"

# Custom fields
paper_id: "2610.26251"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
  - "llm"
architectures:
  []
datasets:
  []
concept_slugs:
  - "capability-focused-evaluation-cafe"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-22T09:43:25Z"
created_at: "2026-10-22T09:43:25Z"
---

# Beyond Static Leaderboards: Capability-Focused Evaluation with Structural Diversity for Time Series Foundation Models

**Authors**: Hongyin Zhang, 项明义, CHEN Rongzhao, YanKai Wang, Jialin Qiao, Xiangdong Huang, Xiaoou Ding, Chen Wang, Zhongyi Pei, Jianmin Wang
**Date**: 2026-10-19
**Paper ID**: [openalex:2610.26251](https://arxiv.org/abs/2610.26251)

## Summary

The paper introduces CaFE (Capability-Focused Evaluation), a framework designed to overcome the limitations of static time series foundation model leaderboards by incorporating structural diversity and multi-dimensional capability assessment. CaFE profiles original benchmark data into eight Structural Features, resamples and filters samples to construct refreshable evaluation sets, and evaluates models using forecast-error and intervention-response metrics. Experiments on GIFT-Eval and FEV-Mini20 demonstrate that CaFE reveals nuanced per-feature model strengths and improves model selection over traditional single-score leaderboards.

## Key Contributions

- Proposes CaFE, a refreshable evaluation extension that incorporates structural diversity and multi-dimensional capability assessment for time series foundation models.
- Defines eight Structural Features (SFs) to profile and resample benchmark data while eliminating out-of-distribution samples.
- Employs both conventional forecast-error metrics and intervention-response metrics to construct per-feature capability profiles.
- Demonstrates on GIFT-Eval and FEV-Mini20 that models selected by CaFE outperform traditional aggregate leaderboard selections on structurally conditioned real data.

## Limitations

Limited to structural transformations derived from defined structural features of existing benchmarks.

## Open Questions & Future Work

- [[extending-structural-time-series-evaluation]]

## Key Concepts

- [[capability-focused-evaluation-cafe]]: A refreshable evaluation framework for time series foundation models that combines structural diversity with multi-dimensional capability assessment.

## Archivist Review

Approved the central evaluation framework CaFE and its associated open question regarding structural evaluation extension, while strictly adhering to scarcity and relevance policies.

### Approved Concepts
- Capability-Focused Evaluation (CaFE): It introduces a novel framework for evaluating time series foundation models across structural dimensions rather than relying on static aggregate leaderboards.

### Approved Open Questions
- Extending Structural Time Series Evaluation: Broadening structural evaluation frameworks to handle complex relational and covariate settings is crucial for developing robust, multi-dimensional benchmarking standards for time series foundation models.

### Rejected Candidates
- [dataset] FEV-Mini20 (`fev-mini20`) - low_impact: Routine or mini benchmark dataset not meeting the threshold for vault archival.

## Links

- [Abstract](https://arxiv.org/abs/2610.26251)
- [PDF](https://arxiv.org/pdf/2610.26251)

