---
# CSL-compatible fields
title: "TERN: A Delta-rule Memory with a Seasonal Reference and Online Adaptation for Epidemic Forecasting"
author:
  - literal: "Shunya Nagashima"
  - literal: "Yuta Funayama"
issued:
  date-parts:
    - [2026, 9, 16]
url: "https://arxiv.org/abs/2609.18407"

# Custom fields
paper_id: "2609.18407"
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
  - "tern"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-18T09:17:23Z"
created_at: "2026-09-18T09:17:23Z"
---

# TERN: A Delta-rule Memory with a Seasonal Reference and Online Adaptation for Epidemic Forecasting

**Authors**: Shunya Nagashima, Yuta Funayama
**Date**: 2026-09-16
**Paper ID**: [openalex:2609.18407](https://arxiv.org/abs/2609.18407)

## Summary

Weekly influenza forecasting is challenging due to shifting wave timing and height, where past information often misleads once an epidemic peaks. To resolve this, the authors propose TERN, a forecaster built around a delta-rule fast-weight memory with channel-wise decay, phase-driven gating, an explicit seasonal reference, and online adaptation. Evaluated on three Cola-GNN influenza benchmarks, TERN outperforms existing epidemic graph models and general forecasters while matching or exceeding seasonal references.

## Key Contributions

- Proposed TERN, a forecaster combining a delta-rule fast-weight memory with an explicit seasonal reference and online adaptation to address phase shifts in epidemic forecasting.
- Demonstrated that TERN outperforms existing epidemic graph models and general forecasters across three Cola-GNN influenza benchmarks.
- Confirmed via a controlled comparison that the delta-rule fast-weight memory with channel-wise decay and phase-driven gating directly drives the forecasting performance gains.

## Key Concepts

- [[tern]]: A forecaster featuring a delta-rule fast-weight memory with channel-wise decay and an explicit seasonal reference for epidemic time series.

## Archivist Review

Approved the core framework concept 'TERN' because its delta-rule fast-weight memory with channel-wise decay and phase-driven gating represents a distinct reusable architectural mechanism for non-stationary forecasting. Rejected the open question as generic future work extending to new diseases and probabilistic outputs.

### Approved Concepts
- TERN: Introduces a novel delta-rule fast-weight memory architecture with channel-wise decay and learned addressing tailored for epidemic forecasting.

### Rejected Candidates
- [open_question] Probabilistic and Multi-Disease Forecasting (`probabilistic-multidisease-forecasting`) - weak_evidence: Represents boilerplate future work on extending models to new domains and outputs rather than addressing a specific methodological bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.18407)
- [PDF](https://arxiv.org/pdf/2609.18407)

