---
# CSL-compatible fields
title: "Small-Area Precipitation Forecasting and Drought--Flood Early Warning with Reverse-Martingale Regularized Recurrent Networks"
author:
  - literal: "Foo Hui-Mean"
  - literal: "Yuan‐chin Ivan Chang"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.26401"

# Custom fields
paper_id: "2605.26401"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "recurrent-neural-network"
  - "gru"
  - "anomaly-detection"
  - "benchmark"
architectures:
  - "gru"
  - "recurrent-neural-network"
datasets:
  - "chirps-v2"
concept_slugs:
  - "reverse-martingale-regularized-recurrent-network"
dataset_slugs:
  - "chirps-v2"
skill: "TimeSeriesSkill"
processed_at: "2026-05-29T08:38:39Z"
created_at: "2026-05-29T08:38:39Z"
---

# Small-Area Precipitation Forecasting and Drought--Flood Early Warning with Reverse-Martingale Regularized Recurrent Networks

**Authors**: Foo Hui-Mean, Yuan‐chin Ivan Chang
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.26401](https://arxiv.org/abs/2605.26401)

## Summary

This paper introduces the Reverse-Martingale Regularized Recurrent Network (RMRNN) for small-area precipitation forecasting and early warning. By applying a backward-coherence penalty to the hidden state, the model simultaneously generates point forecasts and supports a latent residual-based Shiryaev--Roberts (SR) detector for real-time regime change identification. Empirical testing across diverse rain-gauge and gridded precipitation datasets shows that the RMRNN maintains competitive accuracy while significantly reducing false-alarm rates for drought and flood events compared to baseline GRU models.

## Key Contributions

- Introduces the RMRNN framework, which utilizes a backward-coherence penalty to unify probabilistic forecasting and regime-based early warning.
- Demonstrates that the integrated Shiryaev--Roberts (SR) detector reduces false-alarm ratios by 3-5x compared to standard recurrent baselines across three diverse geographic datasets.
- Provides empirical evidence for superior early-warning capabilities, including identifying drought onset 8-12 days earlier than standard SPI-3 methods and flagging flood risks 4 hours before operational alerts.

## Open Questions & Future Work

- [[topographic-neighborhood-modeling-for-forecasting]]
- [[streaming-online-regularized-recurrent-deployment]]

## Key Concepts

- [[reverse-martingale-regularized-recurrent-network]]: A recurrent neural network regularized by a backward-coherence penalty on the latent state to facilitate stable, simultaneous forecasting and regime change detection.

## Archivist Review

The paper introduces a compelling regularization mechanism, RMRNN, that provides a formal bridge between forecasting and sequential regime detection, warranting inclusion as a concept. The identified open questions regarding topographic connectivity and online deployment are substantive challenges that transcend this specific application. One specific dataset, CHIRPS v2, is approved for its consistent role as a standard reference in precipitation forecasting studies.

### Approved Concepts
- Reverse-Martingale Regularized Recurrent Network (RMRNN): It provides a principled way to unify forecasting and regime change detection by regularizing latent states for backward coherence.

### Approved Open Questions
- Topographic neighborhood modeling: Bridging the gap between spatial representation and physical landscape topology is critical for moving beyond simplistic distance-based graph constructions in climate and hydrological forecasting.
- Streaming and online recurrent deployment: This represents a fundamental bottleneck in translating advanced regularized recurrent models into real-time operational emergency management systems.

### Rejected Candidates
- [dataset] NOAA GHCN-Daily (`noaa-ghcn-daily`) - low_impact: This is a general weather data repository and not a specific, unified dataset benchmark that warrants a standalone vault entry beyond standard weather archives.

## Datasets

- [[chirps-v2]]

## Links

- [Abstract](https://arxiv.org/abs/2605.26401)
- [PDF](https://arxiv.org/pdf/2605.26401)

