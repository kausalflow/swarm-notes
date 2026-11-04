---
# CSL-compatible fields
title: "Generative assimilation and prediction for weather and climate"
author:
  - literal: "Shangshang Yang"
  - literal: "Congyi Nai"
  - literal: "Xinyan Liu"
  - literal: "Weidong Li"
  - literal: "Jie Chao"
  - literal: "Jingnan Wang"
  - literal: "Leyis Wang"
  - literal: "Xichen Li"
  - literal: "Xichen Li"
  - literal: "Xi Chen"
  - literal: "Bo Lu"
  - literal: "Xin Li"
  - literal: "Ziniu Xiao"
  - literal: "Niklas Boers"
  - literal: "Huiling Yuan"
  - literal: "Baoxiang Pan"
issued:
  date-parts:
    - [2026, 11, 2]
url: "https://arxiv.org/abs/2503.03038"

# Custom fields
paper_id: "2503.03038"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "generative-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "generative-assimilation-and-prediction"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-04T12:41:07Z"
created_at: "2026-11-04T12:41:07Z"
---

# Generative assimilation and prediction for weather and climate

**Authors**: Shangshang Yang, Congyi Nai, Xinyan Liu, Weidong Li, Jie Chao, Jingnan Wang, Leyis Wang, Xichen Li, Xichen Li, Xi Chen, Bo Lu, Xin Li, Ziniu Xiao, Niklas Boers, Huiling Yuan, Baoxiang Pan
**Date**: 2026-11-02
**Paper ID**: [openalex:2503.03038](https://arxiv.org/abs/2503.03038)

## Summary

The authors introduce Generative Assimilation and Prediction (GAP), a unified deep generative framework that couples data assimilation, weather forecasting, and climate simulation via a shared probabilistic representation of atmospheric states. GAP learns the climatological distribution from reanalysis data and adapts it using observational, predictive, and forcing constraints. Evaluated across diverse timescales, GAP achieves competitive probabilistic weather forecasting, captures extreme events robustly, and supports stable millennial-scale climate simulations reproducing atmospheric variability.

## Key Contributions

- Introduces Generative Assimilation and Prediction (GAP), a unified deep generative framework connecting data assimilation, weather forecasting, and climate simulation.
- Produces competitive probabilistic weather forecasts from self-assimilated initial states derived from 5% synthetic observations with strong extreme event capture.
- Supports stable millennial-scale climate simulations reproducing atmospheric variability from daily fluctuations to decadal oscillations.

## Limitations

Evaluated primarily on synthetic initial states and atmospheric/climatic tasks; broader real-world operational constraints and scaling to multi-decadal projections remain to be fully explored.

## Open Questions & Future Work

- [[coupled-ocean-atmosphere-forcing-generative-modeling]]

## Key Concepts

- [[generative-assimilation-and-prediction]]: A unified deep generative framework that connects data assimilation, weather forecasting, and climate simulation through a shared probabilistic representation of atmospheric states.

## Archivist Review

Approved the core framework concept 'generative-assimilation-and-prediction' and the open question concerning coupled ocean-atmosphere forcing in generative modeling, as they represent central contributions and important open research challenges in data-driven weather and climate prediction. No canonical named datasets were introduced or highlighted.

### Approved Concepts
- Generative Assimilation and Prediction: Proposes a unified deep generative framework connecting data assimilation, weather forecasting, and climate simulation through shared probabilistic representation.

### Approved Open Questions
- Coupled Ocean-Atmosphere Forcing in Generative Modeling: Crucial for extending data-driven weather and climate frameworks to accurately model long-term feedback loops and anthropogenic climate change scenarios.

## Links

- [Abstract](https://arxiv.org/abs/2503.03038)
- [PDF](https://arxiv.org/pdf/2503.03038)

