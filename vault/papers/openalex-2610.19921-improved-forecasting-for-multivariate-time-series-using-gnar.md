---
# CSL-compatible fields
title: "Improved Forecasting for Multivariate Time Series using GNAR models with General Inverse Distance Weights"
author:
  - literal: "Hengxu Liu"
  - literal: "Guy P. Nason"
  - literal: "Sourav Das"
  - literal: "Stephen Grebby"
issued:
  date-parts:
    - [2026, 10, 14]
url: "https://arxiv.org/abs/2610.19921"

# Custom fields
paper_id: "2610.19921"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "graph-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "general-inverse-distance-weights-gnarid"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-17T08:54:22Z"
created_at: "2026-10-17T08:54:22Z"
---

# Improved Forecasting for Multivariate Time Series using GNAR models with General Inverse Distance Weights

**Authors**: Hengxu Liu, Guy P. Nason, Sourav Das, Stephen Grebby
**Date**: 2026-10-14
**Paper ID**: [openalex:2610.19921](https://arxiv.org/abs/2610.19921)

## Summary

To address the limitation of fixed-weight generalised network autoregressive (GNAR) models, this paper introduces GNARID, a model incorporating general inverse distance weights governed by a tunable exponent parameter. The authors establish theoretical guarantees such as consistency and asymptotic normality, addressing growing node regimes. Experiments on simulation studies and the Brumadinho ground displacement dataset show that proper exponent tuning improves forecasting accuracy over standard fixed-weight baselines.

## Key Contributions

- Introduces GNARID, extending generalised network autoregressive (GNAR) models with a tunable inverse distance weight exponent to control distance penalisation.
- Establishes theoretical properties including estimator consistency and asymptotic normality, including when the number of nodes grows.
- Demonstrates improved forecasting performance on the Brumadinho ground displacement dataset compared to fixed-weight GNAR formulations.

## Limitations

Future work could explore broader classes of distance weighting functions or time-varying network structures.

## Key Concepts

- [[general-inverse-distance-weights-gnarid]]: A generalised network autoregressive model extension incorporating a tunable inverse distance weight exponent to govern distance penalisation.

## Archivist Review

Approved the core methodological concept GNARID as it provides a clean, reusable extension to generalised network autoregressive models with tunable distance exponents. No datasets or open questions met the strict standalone threshold.

### Approved Concepts
- General Inverse Distance Weights GNAR (GNARID): Extends generalised network autoregressive (GNAR) models with a tunable distance exponent parameter to better capture distance penalisation in network time series.

## Links

- [Abstract](https://arxiv.org/abs/2610.19921)
- [PDF](https://arxiv.org/pdf/2610.19921)

