---
# CSL-compatible fields
title: "Climate-resilient electric vehicle charging infrastructure for sustainable cities: An interpretable causal-ensemble framework for preventive maintenance and low-carbon mobility"
author:
  - literal: "Cande Lian"
  - literal: "Wentao Zeng"
  - literal: "Jiabin Wu"
  - literal: "Yiming Bie"
  - literal: "W Zhou"
issued:
  date-parts:
    - [2026, 7, 23]
url: "https://arxiv.org/abs/2607.21444"

# Custom fields
paper_id: "2607.21444"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
  - "interpretability"
  - "explainability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "feature-governed-dynamic-stacking-ensemble-fgdse"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-26T07:30:19Z"
created_at: "2026-07-26T07:30:19Z"
---

# Climate-resilient electric vehicle charging infrastructure for sustainable cities: An interpretable causal-ensemble framework for preventive maintenance and low-carbon mobility

**Authors**: Cande Lian, Wentao Zeng, Jiabin Wu, Yiming Bie, W Zhou
**Date**: 2026-07-23
**Paper ID**: [openalex:2607.21444](https://arxiv.org/abs/2607.21444)

## Summary

The authors present FGDSE, a feature-governed dynamic stacking ensemble designed to forecast daily fault risk for electric vehicle charging infrastructure over a 1 to 30 day horizon under urban climate stress. FGDSE partitions heterogeneous signals into four feature families assigned to domain-matched experts alongside short- and long-term deep temporal experts, integrating predictions via a horizon-wise gating mechanism. By coupling the probabilistic output with SHAP attribution and an X-learner, the system delivers causal decision support and identifies extreme heat as a progressively amplifying risk factor for urban charging assets.

## Key Contributions

- Develops FGDSE, a feature-governed dynamic stacking ensemble that partitions heterogeneous signals into four feature families and combines domain-matched and temporal experts with a horizon-wise gating mechanism.
- Achieves accurate multi-week fault-risk forecasting for EV charging infrastructure, sustaining approximately 85% macro-recall at a 30-day horizon with an AUC decay of only 3.2 points across 25 months of data from 13 stations, outperforming twelve baselines beyond ten days.
- Combines SHAP attribution with an X-learner to derive post-level treatment effects, identifying extreme heat as the sole exposure whose causal effect amplifies over time and flagging about 30% of posts as heat-sensitive.

## Limitations

Limited to 13 charging stations over a 25-month period, potentially requiring validation across a broader geographic and climatic distribution.

## Key Concepts

- [[feature-governed-dynamic-stacking-ensemble-fgdse]]: A feature-governed dynamic stacking ensemble for multi-week fault risk prediction in electric vehicle charging infrastructure.

## Archivist Review

Approved the core methodological concept FGDSE as a reusable ensemble pattern for heterogeneous signal partitioning and horizon-wise gating. Kept selections scarce in accordance with vault standards.

### Approved Concepts
- Feature-Governed Dynamic Stacking Ensemble (FGDSE): Central methodological contribution of the paper, forming an interpretable ensemble for multi-week fault risk forecasting under climate stress.

### Rejected Candidates
- [concept] Feature-Governed Dynamic Stacking Ensemble (`fgdse`) - duplicate_existing: Duplicate of the fully spelled out slug feature-governed-dynamic-stacking-ensemble-fgdse.

## Links

- [Abstract](https://arxiv.org/abs/2607.21444)
- [PDF](https://arxiv.org/pdf/2607.21444)

