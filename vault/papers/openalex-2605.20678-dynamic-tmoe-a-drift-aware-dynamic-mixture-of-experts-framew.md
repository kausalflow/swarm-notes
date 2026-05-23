---
# CSL-compatible fields
title: "Dynamic TMoE: A Drift-Aware Dynamic Mixture of Experts Framework for Non-Stationary Time Series Forecasting"
author:
  - literal: "Jiawen Zhu"
  - literal: "Shuhan Liu"
  - literal: "Di Weng"
  - literal: "Yingcai Wu"
issued:
  date-parts:
    - [2026, 5, 20]
url: "https://arxiv.org/abs/2605.20678"

# Custom fields
paper_id: "2605.20678"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "mixture-of-experts"
  - "moe"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dynamic-moe-time-series"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-23T07:25:01Z"
created_at: "2026-05-23T07:25:01Z"
---

# Dynamic TMoE: A Drift-Aware Dynamic Mixture of Experts Framework for Non-Stationary Time Series Forecasting

**Authors**: Jiawen Zhu, Shuhan Liu, Di Weng, Yingcai Wu
**Date**: 2026-05-20
**Paper ID**: [openalex:2605.20678](https://arxiv.org/abs/2605.20678)

## Summary

Dynamic TMoE addresses the challenge of non-stationary time series forecasting by allowing the model architecture to evolve alongside data drift. Unlike static MoE models, this framework dynamically instantiates and prunes experts based on MMD-detected distribution shifts. A temporal memory router maintains continuity by leveraging recurrent states and a historical anomaly repository, ensuring robust performance under regime shifts without the need for additional test-time fine-tuning.

## Key Contributions

- Dynamic TMoE uses Maximum Mean Discrepancy (MMD) to detect distribution shifts and dynamically manages expert pools through instantiation and pruning.
- A temporal memory router incorporating recurrent states and an anomaly repository enables context-aware expert selection without test-time updates.
- Dynamic TMoE achieves a 10.4% reduction in MSE and a 7.8% reduction in MAE across nine benchmark datasets compared to existing state-of-the-art models.

## Open Questions & Future Work

- [[scalable-drift-detection-mechanisms]]

## Key Concepts

- [[dynamic-moe-time-series]]: A mixture-of-experts framework for non-stationary forecasting that dynamically evolves its expert pool and utilizes a temporal memory router for drift-aware selection.

## Archivist Review

The paper introduces a drift-aware MoE mechanism that is a significant architectural improvement over static MoE for non-stationary time series. I approved the core concept using a generalized name. I also approved one open question regarding the scalability of drift detection, which is a known computational bottleneck in the field. Other candidates were rejected for being either redundant, overly specific to the paper's branding, or too generic.

### Approved Concepts
- Dynamic Mixture of Experts for Non-Stationary Time Series: It provides a novel, drift-aware architectural paradigm for time-series MoE that handles non-stationarity through expert instantiation and pruning rather than fixed pools.

### Approved Open Questions
- Scalable Drift Detection Mechanisms: This is a fundamental barrier to the scalability and real-time applicability of drift-aware models in large-scale production time series environments.

### Rejected Candidates
- [concept] Dynamic TMoE (`dynamic-tmoe`) - other: Replaced by a more generalized slug 'dynamic-moe-time-series' to improve reusability and avoid paper-specific branding.
- [open_question] Scalable Drift Detection Methods (`efficient-drift-detection-scaling`) - duplicate_existing: Replaced by 'scalable-drift-detection-mechanisms' to align with established vault naming conventions.
- [open_question] Automated Hyperparameter Optimization (`automated-adaptive-hyperparameter-tuning`) - generic: This is a standard requirement for most machine learning systems rather than a fundamental bottleneck specific to drift-aware forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2605.20678)
- [PDF](https://arxiv.org/pdf/2605.20678)

