---
# CSL-compatible fields
title: "Climate Physics Dynamic Matching"
author:
  - literal: "Gurjeet Sangra Singh"
  - literal: "Frantzeska Lavda"
  - literal: "Alexandros Kalousis"
issued:
  date-parts:
    - [2026, 8, 27]
url: "https://arxiv.org/abs/2608.26907"

# Custom fields
paper_id: "2608.26907"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "diffusion-model"
  - "benchmark"
  - "time-series"
architectures:
  []
datasets:
  - "era5"
concept_slugs:
  - "climate-physics-dynamic-matching"
dataset_slugs:
  - "era5"
skill: "TimeSeriesSkill"
processed_at: "2026-08-30T10:11:16Z"
created_at: "2026-08-30T10:11:16Z"
---

# Climate Physics Dynamic Matching

**Authors**: Gurjeet Sangra Singh, Frantzeska Lavda, Alexandros Kalousis
**Date**: 2026-08-27
**Paper ID**: [openalex:2608.26907](https://arxiv.org/abs/2608.26907)

## Summary

This paper introduces Climate Physics Dynamic Matching (ClimPhyDM), a variational simulation-free dynamics-informed framework for weather forecasting that integrates an advection-type physics prior with data-driven components. Evaluated on the ERA5 benchmark at both hourly and monthly resolutions, ClimPhyDM outperforms existing baselines like ClimODE and GB-DM, demonstrating enhanced temporal stability and resistance to error accumulation. Furthermore, its simulation-free training paradigm allows efficient execution on a single 12 GB consumer GPU.

## Key Contributions

- Introduces ClimPhyDM, a variational simulation-free dynamics-informed framework for weather forecasting combining advection physics priors with data-driven components.
- Demonstrates superior performance over ClimODE and GB-DM on the ERA5 benchmark across hourly (42-hour) and monthly (5-month) resolutions.
- Achieves high temporal stability and resistance to error accumulation while enabling training on a single modest 12 GB consumer GPU via its simulation-free paradigm.

## Open Questions & Future Work

- [[extensions-to-discontinuous-regimes-and-higher-resolutions]]

## Key Concepts

- [[climate-physics-dynamic-matching]]: A variational simulation-free dynamics-informed weather forecasting framework that combines advection-type physics priors with data-driven components.

## Archivist Review

Approved the core framework concept 'Climate Physics Dynamic Matching' as a distinct physics-guided generative method, the standard ERA5 dataset, and an open question on scaling to discontinuous regimes and higher resolutions. Scarcity and relevance thresholds were strictly enforced.

### Approved Concepts
- Climate Physics Dynamic Matching: Introduces ClimPhyDM, a novel simulation-free dynamics-informed framework combining advection-type physics priors with data-driven variational components for weather forecasting.

### Approved Open Questions
- Extensions to Discontinuous Regimes and Higher Resolutions: Handling discontinuities (such as atmospheric fronts or phase changes) and higher resolutions is critical for scaling data-driven climate models to operational weather forecasting scales without breaking physical constraints.

## Datasets

- [[era5]]

## Links

- [Abstract](https://arxiv.org/abs/2608.26907)
- [PDF](https://arxiv.org/pdf/2608.26907)

