---
# CSL-compatible fields
title: "Simulation and evaluation of local daily temperature and precipitation series derived by stochastic downscaling of ERA5 reanalysis"
author:
  - literal: "Silius M. Vandeskog"
  - literal: "Thordis L. Thorarinsdottir"
  - literal: "Alex Lenkoski"
issued:
  date-parts:
    - [2026, 6, 24]
url: "https://arxiv.org/abs/2507.01692"

# Custom fields
paper_id: "2507.01692"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-27T07:43:35Z"
created_at: "2026-06-27T07:43:35Z"
---

# Simulation and evaluation of local daily temperature and precipitation series derived by stochastic downscaling of ERA5 reanalysis

**Authors**: Silius M. Vandeskog, Thordis L. Thorarinsdottir, Alex Lenkoski
**Date**: 2026-06-24
**Paper ID**: [openalex:2507.01692](https://arxiv.org/abs/2507.01692)

## Summary

This paper presents a stochastic downscaling framework to bridge the gap between global ERA5 reanalysis and local surface observations. By combining generalized additive models (GAMs) with auto-regressive moving average (ARMA) processes, the method captures high-resolution, local-scale dynamics for daily temperature and precipitation. Evaluation across over 4000 European sites demonstrates significant improvements in reproducing local atmospheric conditions compared to raw reanalysis products.

## Key Contributions

- Introduces a computationally efficient stochastic downscaling framework for ERA5 temperature and precipitation data.
- Integrates ERA5 reanalysis with localized surface station observations using a non-linear regression framework.
- Demonstrates improved representation of local weather variables compared to raw ERA5 across >4000 European locations over a 70-year period.

## Open Questions & Future Work

- [[multivariate-spatiotemporal-downscaling]]
- [[climate-aware-donor-selection]]

## Archivist Review

The paper presents a statistical downscaling approach that is well-framed within traditional climate science, but does not introduce a novel, reusable ML-specific architecture or mechanism that would be distinct from existing methods in the vault. The open questions regarding multivariate consistency and climate-aware donor selection, however, address fundamental bottlenecks in spatiotemporal time series modeling that are relevant to broader forecasting literature beyond this specific paper.

### Approved Open Questions
- Multivariate spatiotemporal downscaling consistency: This is a fundamental bottleneck for hydrological applications that rely on coherent spatiotemporal weather series, and addressing it is necessary to move beyond independent, univariate downscaling.
- Improving climate-aware donor selection: Effective donor selection is critical to the accuracy of statistical downscaling in complex terrain, and current distance-based heuristics limit the model's reliability in varied climate regimes.

### Rejected Candidates
- [concept] Stochastic downscaling framework (`stochastic-downscaling-framework`) - generic: This is a broad, generic field/methodological category rather than a specific, novel ML concept worth a permanent vault entry.

## Links

- [Abstract](https://arxiv.org/abs/2507.01692)
- [PDF](https://arxiv.org/pdf/2507.01692)

