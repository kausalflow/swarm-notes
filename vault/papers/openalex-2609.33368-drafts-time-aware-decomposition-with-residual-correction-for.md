---
# CSL-compatible fields
title: "DrafTS: Time-Aware Decomposition with Residual Correction for Time Series Modeling"
author:
  - literal: "Yiqiu Liu"
  - literal: "Siru Zhong"
  - literal: "Zhiguang Wang"
  - literal: "Qingsong Wen"
  - literal: "Yuxuan Liang"
issued:
  date-parts:
    - [2026, 9, 27]
url: "https://arxiv.org/abs/2609.33368"

# Custom fields
paper_id: "2609.33368"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "drafts"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:49:45Z"
created_at: "2026-09-30T10:49:45Z"
---

# DrafTS: Time-Aware Decomposition with Residual Correction for Time Series Modeling

**Authors**: Yiqiu Liu, Siru Zhong, Zhiguang Wang, Qingsong Wen, Yuxuan Liang
**Date**: 2026-09-27
**Paper ID**: [openalex:2609.33368](https://arxiv.org/abs/2609.33368)

## Summary

Real-world time series often mix evolving dynamics with irregular variations or noise, which traditional filtering or suppression methods struggle to handle without losing useful temporal patterns. To address this, the authors propose DrafTS, a model-agnostic framework that leverages instantaneous amplitude and frequency features for time-aware decomposition. A task-specific backbone models the primary component capturing underlying dynamics, while a lightweight residual correction module adjusts the output. Experiments across four modeling tasks demonstrate that DrafTS effectively enhances six diverse backbone architectures.

## Key Contributions

- Proposed DrafTS, a model-agnostic framework for time series modeling that combines time-aware decomposition with residual correction.
- Utilizes instantaneous amplitude and frequency features to guide decomposition into a primary component capturing underlying dynamics.
- Employs a lightweight correction module using residual information to refine the backbone output.
- Demonstrated effectiveness across four time series modeling tasks by improving six diverse backbones.

## Open Questions & Future Work

- [[online-multivariate-decomposition]]

## Key Concepts

- [[drafts]]: A model-agnostic time series modeling framework that uses time-aware decomposition and residual correction to preserve evolving dynamics while reducing noise.

## Archivist Review

Approved the core methodological framework 'DrafTS' and the open question on online multivariate decomposition. Rejected paper-internal subcomponents and routine implementation details to maintain strict vault quality standards.

### Approved Concepts
- DrafTS: Central framework proposed in the paper for time-aware decomposition with residual correction in time series modeling.

### Approved Open Questions
- Online Multivariate Decomposition: Eliminating offline preprocessing is crucial for real-time streaming time series analysis and online deployment.

## Links

- [Abstract](https://arxiv.org/abs/2609.33368)
- [PDF](https://arxiv.org/pdf/2609.33368)

