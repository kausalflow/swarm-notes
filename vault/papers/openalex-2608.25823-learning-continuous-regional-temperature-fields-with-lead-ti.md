---
# CSL-compatible fields
title: "Learning Continuous Regional Temperature Fields with Lead-Time and Resolution Queries"
author:
  - literal: "Chunlei Shi"
  - literal: "Jiong Wang"
  - literal: "Yi-Lin Wei"
  - literal: "Junming Hou"
  - literal: "Jinjin Liu"
  - literal: "Yecheng Zhang"
  - literal: "Dan Niu"
issued:
  date-parts:
    - [2026, 8, 26]
url: "https://arxiv.org/abs/2608.25823"

# Custom fields
paper_id: "2608.25823"
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
  - "continuous-spatiotemporal-temperature-forecaster"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T17:00:20Z"
created_at: "2026-08-28T17:00:20Z"
---

# Learning Continuous Regional Temperature Fields with Lead-Time and Resolution Queries

**Authors**: Chunlei Shi, Jiong Wang, Yi-Lin Wei, Junming Hou, Jinjin Liu, Yecheng Zhang, Dan Niu
**Date**: 2026-08-26
**Paper ID**: [openalex:2608.25823](https://arxiv.org/abs/2608.25823)

## Summary

This paper proposes the Continuous Spatiotemporal Temperature Forecaster (CSTF), a neural field-based approach for regional near-surface temperature (T2M) forecasting that replaces fixed-grid outputs with query-conditioned continuous field evaluations. By taking spatial coordinates, forecast lead times, and output resolutions as explicit queries, CSTF delivers unified support for standard hourly forecasts, intermediate diagnostics, and variable resolutions. Regularized by spatial-gradient, temporal-difference, and scale-consistency objectives, CSTF achieves superior deterministic skill and a 17.0% reduction in Bias on the Southeast China ERA5-Land benchmark.

## Key Contributions

- Proposes the Continuous Spatiotemporal Temperature Forecaster (CSTF), formulating regional T2M forecasting as query-conditioned continuous spatiotemporal temperature field evaluation.
- Enables flexible lead times and resolution-controllable outputs within a unified field-evaluation framework by treating spatial location, forecast lead time, and output resolution as explicit queries.
- Introduces spatial-gradient, temporal-difference, and scale-consistency objectives to maintain thermal structure coherence across flexible queries.
- Achieves a 17.0 percent reduction in Bias and superior aggregate deterministic skill on the Southeast China ERA5-Land benchmark while supporting global-scope diagnostics.

## Limitations

Evaluated primarily on regional near-surface temperature forecasting over Southeast China, leaving broader multi-region or global scalability open.

## Key Concepts

- [[continuous-spatiotemporal-temperature-forecaster]]: A neural field architecture for regional temperature forecasting that conditions predictions on spatial location, lead time, and output resolution queries.

## Archivist Review

Approved the core neural field forecasting model concept as it introduces a reusable query-conditioned paradigm for continuous lead-time and resolution weather forecasting. No standalone open questions or datasets met the strict novelty and reuse criteria.

### Approved Concepts
- Continuous Spatiotemporal Temperature Forecaster: Introduces a continuous neural field framework for weather forecasting that supports arbitrary query-dependent lead times and output resolutions.

## Links

- [Abstract](https://arxiv.org/abs/2608.25823)
- [PDF](https://arxiv.org/pdf/2608.25823)

