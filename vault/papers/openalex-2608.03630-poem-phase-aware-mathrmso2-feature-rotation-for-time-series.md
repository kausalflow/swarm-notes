---
# CSL-compatible fields
title: "POEM: Phase-Aware $\mathrm{SO}(2)$ Feature Rotation for Time Series Forecasting Under Periodicity Drift"
author:
  - literal: "Jiawen Zhu"
  - literal: "Shuhan Liu"
  - literal: "Shengxuan Li"
  - literal: "Qiming Shi"
  - literal: "Di Weng"
issued:
  date-parts:
    - [2026, 8, 4]
url: "https://arxiv.org/abs/2608.03630"

# Custom fields
paper_id: "2608.03630"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "attention-mechanism"
architectures:
  []
datasets:
  []
concept_slugs:
  - "poem"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-07T06:03:50Z"
created_at: "2026-08-07T06:03:50Z"
---

# POEM: Phase-Aware $\mathrm{SO}(2)$ Feature Rotation for Time Series Forecasting Under Periodicity Drift

**Authors**: Jiawen Zhu, Shuhan Liu, Shengxuan Li, Qiming Shi, Di Weng
**Date**: 2026-08-04
**Paper ID**: [openalex:2608.03630](https://arxiv.org/abs/2608.03630)

## Summary

To overcome periodicity drift where cycle timing varies over time, the authors propose POEM, a phase-aware forecasting framework leveraging invertible SO(2) latent feature rotations. POEM learns a phase-correction coordinate and utilizes Directional Phase Increment Attention (DPIA) to retrieve and integrate historical phase increments for future phase extrapolation. Experiments show that this geometry-inspired latent transformation regularizes latent trajectories and achieves strong forecasting performance.

## Key Contributions

- Proposes POEM, a phase-aware forecasting framework that addresses periodicity drift via latent feature rotation using the SO(2) group.
- Introduces Directional Phase Increment Attention (DPIA) to extrapolate phase correction coordinates from historical temporal contexts.
- Demonstrates that the SO(2)-based latent transformation regularizes latent trajectories and achieves competitive forecasting performance.

## Open Questions & Future Work

- [[cross-variable-phase-modeling-and-complex-periodic-structures]]

## Key Concepts

- [[poem]]: A phase-aware time series forecasting framework using SO(2) latent feature rotation to handle periodicity drift.

## Archivist Review

Approved the core overarching framework POEM for SO(2) latent feature rotation under periodicity drift while filtering out the secondary attention submodule to maintain vault selectivity. An open question addressing cross-variable phase modeling was also retained due to its general relevance to multivariate temporal forecasting.

### Approved Concepts
- POEM: Central framework of the paper introducing SO(2) latent feature rotation for handling periodicity drift in time series.

### Approved Open Questions
- Cross-Variable Phase Modeling: Extending phase-aware models to capture inter-variable dependencies and complex multi-frequency periodic structures is a major open challenge in multivariate time series forecasting.

### Rejected Candidates
- [concept] Directional Phase Increment Attention (DPIA) (`directional-phase-increment-attention-dpia`) - subcomponent_of_broader_mechanism: Subcomponent of the overarching POEM framework without enough independent standalone utility.

## Links

- [Abstract](https://arxiv.org/abs/2608.03630)
- [PDF](https://arxiv.org/pdf/2608.03630)

