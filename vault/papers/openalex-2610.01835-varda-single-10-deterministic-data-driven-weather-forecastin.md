---
# CSL-compatible fields
title: "Varda-single-1.0: deterministic data-driven weather forecasting at 1 km resolution over Switzerland's complex topography"
author:
  - literal: "Alberto Pennino"
  - literal: "Francesco Zanetta"
  - literal: "Michele Cattaneo"
  - literal: "Claire Merker"
  - literal: "Radi Radev"
  - literal: "Jonas Bhend"
  - literal: "Louis Frey"
  - literal: "Hugues de Laroussilhe"
  - literal: "Ophélia Miralles"
  - literal: "Carlos Osuna"
  - literal: "Daniele Nerini"
  - literal: "Andreas Pauling"
  - literal: "Daniel Hupp"
  - literal: "Ulrich Hamann"
  - literal: "Mary McGlohon"
  - literal: "Marti Bosch"
  - literal: "Luca Lanzilao"
  - literal: "M. Arpagaus"
  - literal: "Lukas Jansing"
  - literal: "Daniel Leuenberger"
  - literal: "Mark A. Liniger"
  - literal: "Katrin Ehlert"
  - literal: "Matthew Chantry"
  - literal: "Håvard Homleid Haugen"
  - literal: "Gert Mertes"
  - literal: "Ana Prieto Nemesio"
  - literal: "Mario Santa Cruz"
  - literal: "Jasper Wijnands"
  - literal: "Gabriel Moldovan"
  - literal: "Harrison Cook"
  - literal: "Oliver Fuhrer"
issued:
  date-parts:
    - [2026, 10, 1]
url: "https://arxiv.org/abs/2610.01835"

# Custom fields
paper_id: "2610.01835"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "graph-neural-network"
  - "time-series"
  - "forecasting"
  - "pre-training"
  - "fine-tuning"
  - "benchmark"
  - "evaluation"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-04T10:49:29Z"
created_at: "2026-10-04T10:49:29Z"
---

# Varda-single-1.0: deterministic data-driven weather forecasting at 1 km resolution over Switzerland's complex topography

**Authors**: Alberto Pennino, Francesco Zanetta, Michele Cattaneo, Claire Merker, Radi Radev, Jonas Bhend, Louis Frey, Hugues de Laroussilhe, Ophélia Miralles, Carlos Osuna, Daniele Nerini, Andreas Pauling, Daniel Hupp, Ulrich Hamann, Mary McGlohon, Marti Bosch, Luca Lanzilao, M. Arpagaus, Lukas Jansing, Daniel Leuenberger, Mark A. Liniger, Katrin Ehlert, Matthew Chantry, Håvard Homleid Haugen, Gert Mertes, Ana Prieto Nemesio, Mario Santa Cruz, Jasper Wijnands, Gabriel Moldovan, Harrison Cook, Oliver Fuhrer
**Date**: 2026-10-01
**Paper ID**: [openalex:2610.01835](https://arxiv.org/abs/2610.01835)

## Summary

Varda-single-1.0 is a data-driven weather forecasting system providing 1 km regional resolution and 31 km global forecasts using stretched-grid Graph Transformers. Trained via a multi-stage curriculum from ERA5 to regional reanalyses and operational fine-tuning, the system achieves skill comparable to or exceeding MeteoSwiss operational NWP baselines (ICON-CH-EPS) across most variables and lead times up to 120 hours. However, evaluation highlights ongoing challenges in capturing local wind maxima and convective precipitation extremes due to squared-error training smoothing.

## Key Contributions

- Introduces Varda-single-1.0, a medium-range data-driven weather prediction system providing hourly deterministic regional forecasts at 1 km resolution over Switzerland's complex topography.
- Employs a two-tier stretched-grid Graph Transformer architecture with a 6-hourly autoregressive forecaster and an hourly temporal downscaler built within the Anemoi framework.
- Demonstrates competitive performance against operational numerical weather prediction baselines (ICON-CH1-EPS and ICON-CH2-EPS) across a one-year verification period over the Alpine domain.

## Limitations

Varda-single underestimates local wind maxima and produces overly smooth convective precipitation fields due to squared-error training, showing particular weaknesses in representing local winds over complex terrain.

## Open Questions & Future Work

- [[joint-hourly-autoregressive-forecasting]]
- [[latent-capacity-complex-topography]]

## Archivist Review

Applied weather forecasting paper presenting Varda-single-1.0; no novel reusable algorithmic concepts or specific datasets qualify for standalone vault notes, but two distinct structural open questions regarding joint hourly autoregressive forecasting and latent capacity over complex topography are approved.

### Approved Open Questions
- Joint Hourly Autoregressive Forecasting: This is technically important because current 6-hourly autoregressive forecasting steps fail to capture fast sub-diurnal convective and local weather dynamics, hindering the full utilization of 1 km regional grids.
- Latent Capacity in Complex Topography: This is crucial for overcoming performance bottlenecks in data-driven weather models over steep orography and complex mountain topographies where adjacent grid cells experience vastly differing microclimates.

## Links

- [Abstract](https://arxiv.org/abs/2610.01835)
- [PDF](https://arxiv.org/pdf/2610.01835)

