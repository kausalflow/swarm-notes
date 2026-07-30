---
# CSL-compatible fields
title: "Earthquake Aftershock Forecasting using Conditional Generative Models"
author:
  - literal: "Weiqiang Zhu"
issued:
  date-parts:
    - [2026, 7, 27]
url: "https://arxiv.org/abs/2607.24109"

# Custom fields
paper_id: "2607.24109"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "diffusion-model"
  - "forecasting"
  - "spatial-attention"
architectures:
  []
datasets:
  []
concept_slugs:
  - "quakegen"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-30T07:26:23Z"
created_at: "2026-07-30T07:26:23Z"
---

# Earthquake Aftershock Forecasting using Conditional Generative Models

**Authors**: Weiqiang Zhu
**Date**: 2026-07-27
**Paper ID**: [openalex:2607.24109](https://arxiv.org/abs/2607.24109)

## Summary

This paper introduces QuakeGen, a conditional diffusion model that recasts earthquake aftershock forecasting as the generation of evolving spatiotemporal fields rather than point-process event sequences. By conditioning on recent seismicity and the forecasting horizon, QuakeGen successfully captures complex fault-controlled anisotropic spatial patterns. Evaluated on global sequences and regional daily seismicity, the data-driven approach outperforms operational USGS Reasenberg-Jones forecasts and matches strong ETAS baselines.

## Key Contributions

- Recasts aftershock forecasting from an event-by-event point process into the conditional generation of evolving spatiotemporal fields.
- Develops QuakeGen, a diffusion model generating aftershock rate and maximum magnitude fields conditioned on recent seismicity and forecasting horizon.
- Outperforms the operational USGS Reasenberg-Jones forecast on global sequences and matches well-tuned ETAS baselines on regional daily forecasting.

## Key Concepts

- [[quakegen]]: A diffusion model that generates evolving fields of aftershock rate and maximum magnitude conditioned on recent seismicity and forecasting horizons.

## Archivist Review

Approved QuakeGen as a distinct diffusion-based conditional generative framework for spatiotemporal seismological forecasting, shifting away from conventional point processes. No datasets or open questions met the strict standalone criteria.

### Approved Concepts
- QuakeGen: Introduces a conditional diffusion model framework for aftershock forecasting that shifts from traditional point processes to spatiotemporal field generation.

## Links

- [Abstract](https://arxiv.org/abs/2607.24109)
- [PDF](https://arxiv.org/pdf/2607.24109)

