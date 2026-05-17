---
# CSL-compatible fields
title: "SeesawNet: Towards Non-stationary Time Series Forecasting with Balanced Modeling of Common and Specific Dependencies"
author:
  - literal: "Hao Li"
  - literal: "Lu Zhang"
  - literal: "Liu Chong"
  - literal: "Yankai Chen"
  - literal: "Pengyang Wang"
  - literal: "Yingjie Zhou"
issued:
  date-parts:
    - [2026, 5, 14]
url: "https://arxiv.org/abs/2605.14551"

# Custom fields
paper_id: "2605.14551"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "attention-mechanism"
  - "transformer"
architectures:
  []
datasets:
  []
concept_slugs:
  - "adaptive-stationary-nonstationary-attention-asna"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-17T07:30:10Z"
created_at: "2026-05-17T07:30:10Z"
---

# SeesawNet: Towards Non-stationary Time Series Forecasting with Balanced Modeling of Common and Specific Dependencies

**Authors**: Hao Li, Lu Zhang, Liu Chong, Yankai Chen, Pengyang Wang, Yingjie Zhou
**Date**: 2026-05-14
**Paper ID**: [openalex:2605.14551](https://arxiv.org/abs/2605.14551)

## Summary

SeesawNet addresses the over-smoothing limitation of instance normalization in non-stationary time series forecasting by balancing common pattern modeling with instance-specific dependency preservation. The core architecture, SeesawNet, employs the Adaptive Stationary-Nonstationary Attention (ASNA) module to dynamically fuse information from normalized and raw sequences according to the non-stationary profile of each instance. By alternating between dedicated temporal and channel relationship modeling, the framework effectively captures both long-range dependencies and cross-variable interactions. Benchmarking experiments verify that this approach outperforms current state-of-the-art models.

## Key Contributions

- Introduces SeesawNet, a unified architecture that dynamically balances common and instance-specific dependency modeling for non-stationary time series forecasting.
- Proposes Adaptive Stationary-Nonstationary Attention (ASNA) to capture and fuse common and specific temporal/channel dependencies based on instance-level non-stationarity.
- Demonstrates consistent performance improvements over state-of-the-art forecasting methods across various real-world benchmarks.

## Open Questions & Future Work

- [[non-stationary-pattern-balance-dynamics]]

## Key Concepts

- [[adaptive-stationary-nonstationary-attention-asna]]: An attention mechanism that adaptively fuses dependencies derived from both normalized (stationary) and raw (non-stationary) sequences based on instance-level non-stationarity.

## Archivist Review

The review focused on extracting the central mechanism that addresses the common vs. specific dependency trade-off in non-stationary forecasting. ASNA is a distinct, reusable architectural idea, while the open question identifies the need to link this balancing act to the underlying non-stationary drivers of the data, which is a substantive research gap. The overarching model (SeesawNet) was rejected in favor of its specific mechanism to keep the vault focused on modular research components.

### Approved Concepts
- Adaptive Stationary-Nonstationary Attention (ASNA): This mechanism directly addresses the tension between over-smoothing (common patterns) and preserving instance-specific structural heterogeneity in non-stationary time series.

### Approved Open Questions
- Dynamics of Non-stationary Pattern Balancing: This addresses a core trade-off in non-stationary time series modeling, moving beyond current black-box adaptive gating mechanisms toward more interpretable and design-driven forecasting architectures.

### Rejected Candidates
- [concept] SeesawNet (`seesaw-net`) - subcomponent_of_broader_mechanism: This is the overarching architecture name, and the core mechanism (ASNA) has been approved separately, adhering to the policy of preferring modular mechanisms over monolithic frameworks.

## Links

- [Abstract](https://arxiv.org/abs/2605.14551)
- [PDF](https://arxiv.org/pdf/2605.14551)

