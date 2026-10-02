---
# CSL-compatible fields
title: "SemPSG: A Semantic Channel-Aware Foundation Model for Polysomnography Analysis"
author:
  - literal: "Junyu Chen"
  - literal: "Chenxi Liu"
  - literal: "Shiqin Tang"
  - literal: "Hao Miao"
  - literal: "Wanyun Ling"
  - literal: "Ziyue Li"
  - literal: "Hongbin Liu"
  - literal: "Gaofeng Meng"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.36619"

# Custom fields
paper_id: "2609.36619"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "foundation-model"
  - "multimodal"
  - "representation-learning"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "sempsg"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-02T10:48:05Z"
created_at: "2026-10-02T10:48:05Z"
---

# SemPSG: A Semantic Channel-Aware Foundation Model for Polysomnography Analysis

**Authors**: Junyu Chen, Chenxi Liu, Shiqin Tang, Hao Miao, Wanyun Ling, Ziyue Li, Hongbin Liu, Gaofeng Meng
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.36619](https://arxiv.org/abs/2609.36619)

## Summary

Polysomnography (PSG) analysis suffers from heterogeneous channel configurations across centers, which hinders transferability. To address this, the authors propose SemPSG, a semantic channel-aware foundation model that explicitly models the physiological semantics of channel identity in both representation learning and channel aggregation. SemPSG integrates a semantic-conditioned time-series encoder with a multi-view image encoder to jointly capture temporal dynamics and morphological patterns, outperforming existing time-series and PSG-specific foundation models across various sleep and health-related tasks.

## Key Contributions

- Proposes SemPSG, a semantic channel-aware foundation model that explicitly represents physiological semantics of channel identity for heterogeneous polysomnography analysis.
- Introduces a semantic-conditioned time-series encoder and a multi-view image encoder to capture signal-specific temporal dynamics, cross-signal interactions, and time-frequency/morphological patterns.
- Demonstrates consistent improvements over general-purpose time series and PSG-specific foundation models across diverse sleep and health-related tasks with heterogeneous channel configurations.

## Key Concepts

- [[sempsg]]: A semantic channel-aware foundation model for polysomnography analysis that explicitly represents the physiological semantics of channel identity.

## Archivist Review

I approved the core framework 'SemPSG' as a permanent vault concept because it introduces a novel semantic channel-aware approach for handling heterogeneous polysomnography configurations. No other concepts or datasets met the strict reusability and explicit naming criteria.

### Approved Concepts
- SemPSG: Introduces a semantic channel-aware foundation model that explicitly incorporates physiological semantics of channel identity into representation learning and aggregation for heterogeneous polysomnography analysis.

## Links

- [Abstract](https://arxiv.org/abs/2609.36619)
- [PDF](https://arxiv.org/pdf/2609.36619)

