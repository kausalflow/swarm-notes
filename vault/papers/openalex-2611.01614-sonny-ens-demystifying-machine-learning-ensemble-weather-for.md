---
# CSL-compatible fields
title: "Sonny-ENS: demystifying machine-learning ensemble weather forecasting"
author:
  - literal: "Minjong Cheon"
issued:
  date-parts:
    - [2026, 11, 1]
url: "https://arxiv.org/abs/2611.01614"

# Custom fields
paper_id: "2611.01614"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "sonny-ens"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-04T12:40:39Z"
created_at: "2026-11-04T12:40:39Z"
---

# Sonny-ENS: demystifying machine-learning ensemble weather forecasting

**Authors**: Minjong Cheon
**Date**: 2026-11-01
**Paper ID**: [openalex:2611.01614](https://arxiv.org/abs/2611.01614)

## Summary

The paper introduces Sonny-ENS, an efficient machine-learning ensemble weather forecasting framework based on Monte Carlo dropout and CRPS training that achieves state-of-the-art probabilistic skill with minimal computational cost. Trained in only 2.7 A40 GPU-days, Sonny-ENS outperforms both traditional physics-based ensembles (such as ECMWF ENS) and operational machine learning models like GenCast across diverse forecast targets. Mechanistic ablations and sparse autoencoder analysis further reveal how simple stochastic perturbations translate into dynamically consistent atmospheric spread.

## Key Contributions

- Introduces Sonny-ENS, a machine-learning ensemble weather forecasting system trained in just 2.7 A40 GPU-days using Monte Carlo dropout and CRPS loss.
- Outperforms the European Centre for Medium-Range Weather Forecasts (ECMWF) ensemble on 96% of 570 targets with an 8.3% lower mean CRPS at 1-10 day lead times.
- Outperforms operational GenCast on 69% of targets while generating a 51-member, 15-day forecast in 69 seconds on a single GPU.
- Demonstrates via Kolmogorov-Arnold sparse autoencoder analysis that dropout injects uncertainty in the tropics while ensemble spread naturally grows in baroclinically unstable regions.

## Open Questions & Future Work

- [[high-resolution-operational-ml-weather-ensembles]]

## Key Concepts

- [[sonny-ens]]: A machine-learning ensemble weather forecasting system utilizing Monte Carlo dropout and CRPS loss that achieves high skill with minimal training compute.

## Archivist Review

Approved the core framework concept 'Sonny-ENS' and the open question regarding scaling such efficient ensembles to higher spatial resolutions. Rejected all paper-local or non-novel variations to keep the vault highly selective.

### Approved Concepts
- Sonny-ENS: Central framework introduced in the paper for efficient machine-learning ensemble weather forecasting.

### Approved Open Questions
- High-Resolution Operational ML Weather Ensembles: Advancing weather forecasting models to higher resolutions is crucial for capturing fine-scale atmospheric phenomena and bridging the gap between experimental AI models and operational meteorology.

## Links

- [Abstract](https://arxiv.org/abs/2611.01614)
- [PDF](https://arxiv.org/pdf/2611.01614)

