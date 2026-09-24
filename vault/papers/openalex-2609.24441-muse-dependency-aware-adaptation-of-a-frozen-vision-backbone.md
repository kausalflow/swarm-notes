---
# CSL-compatible fields
title: "MUSE: Dependency-Aware Adaptation of a Frozen Vision Backbone for Multivariate Time Series Forecasting"
author:
  - literal: "Xinying Cai"
  - literal: "Junkai Lu"
  - literal: "Yuhan Zhu"
  - literal: "Xiaoyun Yu"
  - literal: "Xiangfei Qiu"
  - literal: "Jilin Hu"
issued:
  date-parts:
    - [2026, 9, 21]
url: "https://arxiv.org/abs/2609.24441"

# Custom fields
paper_id: "2609.24441"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "vision-transformer"
  - "transformer"
  - "pre-training"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-24T09:37:49Z"
created_at: "2026-09-24T09:37:49Z"
---

# MUSE: Dependency-Aware Adaptation of a Frozen Vision Backbone for Multivariate Time Series Forecasting

**Authors**: Xinying Cai, Junkai Lu, Yuhan Zhu, Xiaoyun Yu, Xiangfei Qiu, Jilin Hu
**Date**: 2026-09-21
**Paper ID**: [openalex:2609.24441](https://arxiv.org/abs/2609.24441)

## Summary

MUSE is a dependency-aware adaptation framework for multivariate time-series forecasting that leverages a fully frozen pretrained vision backbone (MAE). To overcome the challenges of transferring visual priors, MUSE employs a Variable Context Refinement Module to handle cross-variable dependencies and a Temporal-Periodic Refinement Module for multi-depth temporal and periodic modeling. Predictions from both modules are combined via a learnable prediction-level gate, yielding state-of-the-art results across 10 real-world datasets.

## Key Contributions

- MUSE achieves state-of-the-art performance across 10 real-world multivariate time-series forecasting benchmarks using a fully frozen pretrained MAE vision backbone.
- Introduces the Variable Context Refinement Module (VCR) to aggregate temporal information per variable and model cross-variable dependencies while preserving independent visual spaces.
- Introduces the Temporal-Periodic Refinement Module (TPR) for lightweight multi-depth refinement of across-period and within-period temporal dependencies.

## Open Questions & Future Work

- [[efficiency-and-interpretability-of-lvm-time-series-adaptation]]

## Archivist Review

The review policy prioritizes scarce, high-impact approvals. The proposed modules (VCR and TPR) are paper-internal implementation subcomponents and were therefore rejected. The open question on efficiency and interpretability in LVM time series adaptation was approved as it addresses a substantive architectural bottleneck in vision-to-time-series transfer learning.

### Approved Open Questions
- Efficiency and Interpretability in LVM Time Series Adaptation: Important for guiding future research on efficiency bottlenecks and mechanistic interpretability when adapting heavy frozen vision backbones to time-series tasks.

### Rejected Candidates
- [concept] Variable Context Refinement Module (`variable-context-refinement-module`) - subcomponent_of_broader_mechanism: Paper-internal subcomponent module specific to the MUSE architecture rather than a broadly reusable concept.
- [concept] Temporal-Periodic Refinement Module (`temporal-periodic-refinement-module`) - subcomponent_of_broader_mechanism: Paper-internal subcomponent module specific to the MUSE architecture rather than a broadly reusable concept.

## Links

- [Abstract](https://arxiv.org/abs/2609.24441)
- [PDF](https://arxiv.org/pdf/2609.24441)

