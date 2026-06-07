---
# CSL-compatible fields
title: "Performance Evaluation of GraphCast for Medium-Range Weather Forecasting over Brazil"
author:
  - literal: "Wolfgang R. Rowell"
  - literal: "Lucas S. Kupssinskü"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.06348"

# Custom fields
paper_id: "2606.06348"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:19:21Z"
created_at: "2026-06-07T08:19:21Z"
---

# Performance Evaluation of GraphCast for Medium-Range Weather Forecasting over Brazil

**Authors**: Wolfgang R. Rowell, Lucas S. Kupssinskü
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.06348](https://arxiv.org/abs/2606.06348)

## Summary

This paper provides a regional performance evaluation of the GraphCast machine learning weather prediction model across four Brazilian climatic sub-regions, comparing it to the deterministic ECMWF IFS HRES baseline. Using the WeatherBench-X framework, the study evaluates tropospheric variables ($T_{850}$, $Q_{850}$, $Z_{500}$) across different seasonal windows. Results indicate a regime-dependent skill profile, where GraphCast's smoothing behavior is advantageous for large-scale moisture transport in summer but limits its ability to resolve fast-propagating baroclinic systems in winter. The findings offer critical insights into the limitations of current global MLWP models in complex, highly convective tropical environments.

## Key Contributions

- Evaluates the performance of the GraphCast MLWP model against the deterministic ECMWF IFS HRES baseline over four distinct Brazilian climatic sub-regions.
- Identifies regime-dependent skill profiles for GraphCast, noting underperformance in baroclinic systems during austral winter versus improved performance in moisture transport during the austral summer.
- Establishes a foundational regional performance baseline for ML weather models in Brazil to inform future tropicalization and regional adaptation efforts.

## Open Questions & Future Work

- [[mlwp-extratropical-winter-bottleneck]]

## Archivist Review

I have approved the open question regarding MLWP extratropical bottlenecks as it articulates a specific, technically profound limitation in current autoregressive weather prediction architectures that goes beyond simple performance reporting. No new concepts or datasets were approved, as the paper's primary contribution is a regional performance evaluation, which does not introduce a novel, reusable methodology or framework concept.

### Approved Open Questions
- Bottlenecks in Extratropical MLWP Forecasting: Understanding these failure modes is critical for the adaptation of global weather models to diverse regional climates, specifically to determine if architectural innovations like adaptive timestepping or better vertically-aware encoders are required.

## Links

- [Abstract](https://arxiv.org/abs/2606.06348)
- [PDF](https://arxiv.org/pdf/2606.06348)

