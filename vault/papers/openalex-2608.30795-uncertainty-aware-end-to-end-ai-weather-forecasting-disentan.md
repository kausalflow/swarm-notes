---
# CSL-compatible fields
title: "Uncertainty-Aware End-to-End AI Weather Forecasting: Disentangling Observation and Model Contributions"
author:
  - literal: "Rodrigo Almeida"
  - literal: "Noelia Otero"
  - literal: "Jost Arndt"
  - literal: "Simon Baur"
  - literal: "Wojciech Samek"
  - literal: "Jackie Ma"
issued:
  date-parts:
    - [2026, 8, 31]
url: "https://arxiv.org/abs/2608.30795"

# Custom fields
paper_id: "2608.30795"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "uncertainty-quantification"
  - "probabilistic-forecasting"
  - "deep-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-03T09:17:24Z"
created_at: "2026-09-03T09:17:24Z"
---

# Uncertainty-Aware End-to-End AI Weather Forecasting: Disentangling Observation and Model Contributions

**Authors**: Rodrigo Almeida, Noelia Otero, Jost Arndt, Simon Baur, Wojciech Samek, Jackie Ma
**Date**: 2026-08-31
**Paper ID**: [openalex:2608.30795](https://arxiv.org/abs/2608.30795)

## Summary

This paper introduces an uncertainty-aware end-to-end weather forecasting framework that renders the deterministic Aardvark Weather model probabilistic by decoupling aleatoric observation uncertainty from epistemic model uncertainty. By combining learned input-dependent noise at the observation encoder with Monte Carlo dropout in the processor, the model generates a nested ensemble. Using a law-of-total-variance decomposition, the approach successfully attributes forecast spread to its respective sources, improving mean forecasts by 4.2% and achieving strong calibration against ERA5 in the medium range.

## Key Contributions

- Proposes a probabilistic variant of the Aardvark Weather model by attaching learned input-dependent noise at the observation encoder for aleatoric uncertainty and Monte Carlo dropout in the processor for epistemic uncertainty.
- Applies a law-of-total-variance decomposition to attribute forecast spread between observation-driven and model-driven sources.
- Achieves a 4.2% average improvement in mean forecast across variables and lead times, with a spread-skill ratio of 0.98 against ERA5 in the medium range.

## Limitations

Trails the operational ECMWF ensemble in overall probabilistic skill while providing an efficient end-to-end alternative.

## Open Questions & Future Work

- [[decoder-stochastic-branch-downscaling]]

## Archivist Review

Applied strict scarcity and novelty filters. Approved the open question regarding decoder stochastic branches for downscaling as it addresses a specific unresolved limitation in station-level uncertainty quantification. Rejected concepts that were merely paper-internal instantiations of standard techniques (learned observation noise + MC dropout).

### Approved Open Questions
- Decoder Stochastic Branch for Downscaling: Addressing station-level under-dispersion and downscaling uncertainty is crucial for operational decision-making, local extreme weather risk assessment, and closing the calibration gap between gridded and station forecasts.

### Rejected Candidates
- [concept] Uncertainty-Aware End-to-End AI Weather Forecasting (`uncertainty-aware-weather-forecasting-framework`) - paper_local: Overly paper-internal mechanism combining standard learned noise and MC dropout into a single architecture.

## Links

- [Abstract](https://arxiv.org/abs/2608.30795)
- [PDF](https://arxiv.org/pdf/2608.30795)

