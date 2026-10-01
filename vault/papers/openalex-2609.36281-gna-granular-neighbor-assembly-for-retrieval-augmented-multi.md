---
# CSL-compatible fields
title: "GNA: Granular Neighbor Assembly for Retrieval-Augmented Multivariate Time-Series Forecasting"
author:
  - literal: "Vincent Uhse"
issued:
  date-parts:
    - [2026, 9, 28]
url: "https://arxiv.org/abs/2609.36281"

# Custom fields
paper_id: "2609.36281"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "retrieval-augmented-generation"
  - "transformer"
  - "multivariate"
architectures:
  []
datasets:
  []
concept_slugs:
  - "granular-neighbor-assembly"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-01T11:14:42Z"
created_at: "2026-10-01T11:14:42Z"
---

# GNA: Granular Neighbor Assembly for Retrieval-Augmented Multivariate Time-Series Forecasting

**Authors**: Vincent Uhse
**Date**: 2026-09-28
**Paper ID**: [openalex:2609.36281](https://arxiv.org/abs/2609.36281)

## Summary

The paper introduces Granular Neighbor Assembly (GNA), a retrieval layer for multivariate time-series forecasting backbones that integrates neighbors at two distinct granularities: whole past windows to preserve variate coherence and per-variate neighbors to capture individual variate dynamics. A learned gating mechanism dynamically weighs the retrieved futures against backbone and persistence forecasts across each step and variate. Evaluated across standard benchmarks, GNA consistently improves forecasting accuracy, outperforming backbones in the vast majority of tested dataset-horizon settings.

## Key Contributions

- Introduces GNA (Granular Neighbor Assembly), a retrieval layer that combines whole past windows and per-variate neighbors for multivariate time-series forecasting.
- Employs a learned gate that decides per forecast step and variate how much to trust retrieved futures against a persistence and backbone forecast.
- Improves two Transformer backbones in 85 of 96 dataset-horizon settings and achieves the lowest MSE on 8 of 12 standard benchmarks.

## Limitations

Performance degrades on hourly non-stationary series at long horizons due to drifting levels in retrieved futures.

## Open Questions & Future Work

- [[learned-level-correction-retrieval-forecasting]]

## Key Concepts

- [[granular-neighbor-assembly]]: A retrieval layer for multivariate time-series forecasting that assembles neighbors at whole-window and per-variate granularities.

## Archivist Review

Approved the core methodological contribution of Granular Neighbor Assembly (GNA) as a distinct multi-granularity retrieval layer for multivariate forecasting, along with an open question targeting level drift in non-stationary retrieval. No standalone datasets qualified.

### Approved Concepts
- Granular Neighbor Assembly: GNA is the central novel retrieval layer introduced in the paper, operating across two granularities for multivariate time-series forecasting.

### Approved Open Questions
- Learned Level Correction for Retrieval: Crucial for expanding retrieval-augmented forecasting to non-stationary real-world domains where level shifts severely degrade performance.

## Links

- [Abstract](https://arxiv.org/abs/2609.36281)
- [PDF](https://arxiv.org/pdf/2609.36281)

