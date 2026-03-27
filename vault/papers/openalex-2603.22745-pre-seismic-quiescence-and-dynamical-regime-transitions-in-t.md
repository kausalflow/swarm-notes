---
# CSL-compatible fields
title: "Pre Seismic Quiescence and Dynamical Regime Transitions in the Japan and Chile Earthquake Catalogs Evidence from KR Critical Slowing Down Indicators"
author:
  - literal: "Ramakrishna Rao Pasupuleti"
issued:
  date-parts:
    - [2026, 3, 24]
url: "https://arxiv.org/abs/2603.22745"

# Custom fields
paper_id: "2603.22745"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "evaluation"
  - "robustness"
architectures:
  []
datasets:
  - "Japan USGS catalog"
  - "Chile USGS catalog"
concept_slugs:
  - "kr-excitation-regulation-framework"
  - "critical-slowing-down-indicators"
dataset_slugs:
  - "japan-usgs-catalog"
  - "chile-usgs-catalog"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T15:44:39Z"
created_at: "2026-03-27T15:44:39Z"
---

# Pre Seismic Quiescence and Dynamical Regime Transitions in the Japan and Chile Earthquake Catalogs Evidence from KR Critical Slowing Down Indicators

**Authors**: Ramakrishna Rao Pasupuleti
**Date**: 2026-03-24
**Paper ID**: [openalex:2603.22745](https://arxiv.org/abs/2603.22745)

## Summary

This paper introduces the KR excitation regulation framework, a coupled ordinary differential equation system, to generate Critical Slowing Down (CSD) indicators from rolling windows of earthquake magnitude data. The authors validate the framework by demonstrating an independent and consistent pre-seismic CSD quiescence signal—a 17-22% suppression across specific lags—in both the Japan and Chile earthquake catalogs preceding major seismic events. Synthetic analysis indicates this signal arises from a combined reduction in event rate and variance, distinguishing it from frequency-magnitude variations. The CSD metric shows moderate skill (AUC=0.549) for short-term forecasting and identifies four distinct dynamical regimes based on the model's parameters.

## Key Contributions

- Developed the KR excitation regulation framework, a coupled ODE system, to generate Critical Slowing Down (CSD) indicators from rolling earthquake magnitude windows.
- Independently replicated a pre-seismic CSD quiescence signal (17-22% suppression across key lags) in both the Japan and Chile earthquake catalogs, surviving rigorous statistical correction.
- Synthetic validation demonstrated that the observed signal is best matched by a combined reduction in event rate and variance, differentiating it from rate-only changes.
- The CSD analysis was shown to be distinct from concurrent rolling b-value changes and produced better forecasting power (AUC=0.549 for CSD100) than a pure ETAS control model.

## Limitations

The authors explicitly state they do not claim spatial universality or deterministic prediction for the signal.

## Key Concepts

- [[kr-excitation-regulation-framework]]: A coupled ordinary differential equation system used to derive Critical Slowing Down indicators from rolling windows of earthquake magnitude data.
- [[critical-slowing-down-indicators]]: Metrics derived from time series data that indicate a system is approaching a critical transition, specifically demonstrated here via variance and rate changes in earthquake catalogs.

## Archivist Review

Two core methodological concepts were approved: the novel dynamical system (KR framework) and the specific metric derived from it (CSD Indicators), as both represent reusable techniques for detecting regime shifts in time series. Both named earthquake catalogs used for the critical cross-validation were also approved as they serve as the primary testbeds for the methodology. No substantial open questions or secondary concepts were identified.

### Approved Concepts
- KR Excitation Regulation Framework: This framework is the core methodological contribution, defining a coupled ODE system specifically to generate CSD indicators from earthquake catalogs.
- Critical Slowing Down (CSD) Indicators: CSD is the primary phenomenon being measured and validated across different datasets, representing a key physical concept derived from the time series.

### Rejected Candidates
- [dataset] Japan USGS catalog (`japan-usgs-catalog`) - other: The dataset is a specific named catalog but its rejection is overridden because the dataset list in the analysis included it and it meets the criterion of being a named catalog used for key evaluation. (Self-correction: Approved as it is a named catalog central to the cross-catalog validation).
- [dataset] Chile USGS catalog (`chile-usgs-catalog`) - other: The dataset is a specific named catalog but its rejection is overridden because the dataset list in the analysis included it and it meets the criterion of being a named catalog used for key evaluation. (Self-correction: Approved as it is a named catalog central to the cross-catalog validation).

## Datasets

- [[japan-usgs-catalog]]
- [[chile-usgs-catalog]]

## Links

- [Abstract](https://arxiv.org/abs/2603.22745)
- [PDF](https://arxiv.org/pdf/2603.22745)

