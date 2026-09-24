---
# CSL-compatible fields
title: "TAC-Time: Texts as Channels For Multimodal Time Series Forecasting"
author:
  - literal: "Jiayi Liang"
  - literal: "Xiaotian Gu"
  - literal: "Xinyu Xie"
  - literal: "Yuanbin Wu"
  - literal: "Xiaoling Wang"
issued:
  date-parts:
    - [2026, 9, 21]
url: "https://arxiv.org/abs/2609.24156"

# Custom fields
paper_id: "2609.24156"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "transformer"
  - "attention-mechanism"
architectures:
  []
datasets:
  []
concept_slugs:
  - "tac-time"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-24T09:37:36Z"
created_at: "2026-09-24T09:37:36Z"
---

# TAC-Time: Texts as Channels For Multimodal Time Series Forecasting

**Authors**: Jiayi Liang, Xiaotian Gu, Xinyu Xie, Yuanbin Wu, Xiaoling Wang
**Date**: 2026-09-21
**Paper ID**: [openalex:2609.24156](https://arxiv.org/abs/2609.24156)

## Summary

This paper introduces TAC-Time, a novel framework for multimodal time series forecasting that converts auxiliary text into additional temporal channels, integrating them directly with numerical sequences within a shared backbone. This design maintains temporal continuity and periodic structures while keeping computations efficient. Experiments on real-world benchmarks show that TAC-Time outperforms existing methods while providing robust interpretability through attention and frequency-domain analyses.

## Key Contributions

- Proposes TAC-Time, a unified multimodal framework that transforms auxiliary textual information into additional temporal channels for time series forecasting.
- Preserves temporal continuity and periodic structures by modeling text features jointly with numerical sequences in a shared temporal backbone.
- Enables systematic interpretability via attention and frequency-domain analyses to uncover cross-modal dependencies and predictive textual signals.

## Open Questions & Future Work

- [[flexible-adaptive-channel-configurations]]

## Key Concepts

- [[tac-time]]: A unified framework for multimodal time series forecasting that transforms textual information into additional temporal channels.

## Archivist Review

I approved the overarching framework concept 'TAC-Time' and the explicit open question regarding flexible and adaptive channel configurations for multimodal forecasting, while enforcing strict scarcity and rejecting paper-local subcomponents.

### Approved Concepts
- TAC-Time: Core methodological contribution for multimodal time series forecasting by treating text as additional temporal channels.

### Approved Open Questions
- Flexible and Adaptive Channel Configurations: Exploring flexible channel configurations is technically important for handling heterogeneous information capacities between rich text semantics and low-dimensional numerical streams.

### Rejected Candidates
- [concept] Text-to-Channel Transformation (`tac-time-subcomponent`) - subcomponent_of_broader_mechanism: Subcomponent of the overarching TAC-Time framework note.

## Links

- [Abstract](https://arxiv.org/abs/2609.24156)
- [PDF](https://arxiv.org/pdf/2609.24156)

