---
# CSL-compatible fields
title: "GraphCast-Mamba: Learning Non-Markovian Corrections for Weather Forecasting"
author:
  - literal: "Ilya Vilkoviskiy"
  - literal: "Liang-Hong Mo"
  - literal: "Suozhi Huang"
  - literal: "Dmitry A. Abanin"
issued:
  date-parts:
    - [2026, 10, 20]
url: "https://arxiv.org/abs/2610.28512"

# Custom fields
paper_id: "2610.28512"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "state-space-model"
  - "mamba"
  - "graph-neural-network"
  - "gnn"
  - "spatiotemporal"
  - "weather-forecasting"
architectures:
  - "mamba"
datasets:
  - "era5"
concept_slugs:
  - "graphcast-mamba"
dataset_slugs:
  - "era5"
skill: "TimeSeriesSkill"
processed_at: "2026-10-23T09:40:17Z"
created_at: "2026-10-23T09:40:17Z"
---

# GraphCast-Mamba: Learning Non-Markovian Corrections for Weather Forecasting

**Authors**: Ilya Vilkoviskiy, Liang-Hong Mo, Suozhi Huang, Dmitry A. Abanin
**Date**: 2026-10-20
**Paper ID**: [openalex:2610.28512](https://arxiv.org/abs/2610.28512)

## Summary

To address unresolved atmospheric history dependence in weather forecasting, the authors introduce GraphCast-Mamba, which augments a frozen pretrained GraphCast backbone with a trainable Mamba correction branch combining graph message passing and state-space layers. Trained on ERA5 data for only 2,500 optimizer updates, GraphCast-Mamba retains a temporal memory state across successive forecast steps and reduces normalized weighted MSE by 14.42% over a 10-day forecast horizon. At day 10, RMSE decreases by 7.09 to 14.60% across 11 evaluated atmospheric variable groups, demonstrating substantial improvements while keeping the base model frozen.

## Key Contributions

- Introduces GraphCast-Mamba, augmenting a frozen pretrained GraphCast backbone with a trainable Mamba correction branch that captures history dependence beyond short input windows.
- Achieves a 14.42% reduction in normalized weighted mean-squared error (MSE) over a full ten-day forecast and 21.66% at day 10 on ERA5 data.
- Reduces root-mean-square error (RMSE) by 7.09–14.60% across 11 evaluated variable groups at day 10, including temperature, wind, pressure, and precipitation.

## Limitations

Evaluation is limited to a 1^\circ$ resolution GraphCast backbone using ERA5 data.

## Open Questions & Future Work

- [[resolution-and-backbone-dependence-of-corrections]]

## Key Concepts

- [[graphcast-mamba]]: A hybrid weather forecasting architecture that augments a pretrained GraphCast backbone with a Mamba-based correction branch to capture non-Markovian history dependence.

## Archivist Review

Approved the primary architectural contribution 'GraphCast-Mamba' and its key open question concerning resolution and backbone dependence, adhering strictly to scarcity constraints and filtering out paper-local metrics.

### Approved Concepts
- GraphCast-Mamba: Introduces a novel hybrid architecture combining graph message passing and state-space models to model non-Markovian history dependence in weather forecasting backbones.

### Approved Open Questions
- Resolution and Backbone Dependence: Crucial for understanding the generalizability and scalability of hybrid memory-augmented correction architectures across diverse operational weather prediction systems.

## Datasets

- [[era5]]

## Links

- [Abstract](https://arxiv.org/abs/2610.28512)
- [PDF](https://arxiv.org/pdf/2610.28512)

