---
# CSL-compatible fields
title: "Reading the Sky to Forecast the Ground: Physics-Informed Link-State Forecasting for LEO Networks at Any Location"
author:
  - literal: "Yunxiang Chi"
  - literal: "Zhenlin An"
  - literal: "Longfei Shangguan"
  - literal: "Kyle Jamieson"
issued:
  date-parts:
    - [2026, 9, 22]
url: "https://arxiv.org/abs/2609.26696"

# Custom fields
paper_id: "2609.26696"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-25T09:54:19Z"
created_at: "2026-09-25T09:54:19Z"
---

# Reading the Sky to Forecast the Ground: Physics-Informed Link-State Forecasting for LEO Networks at Any Location

**Authors**: Yunxiang Chi, Zhenlin An, Longfei Shangguan, Kyle Jamieson
**Date**: 2026-09-22
**Paper ID**: [openalex:2609.26696](https://arxiv.org/abs/2609.26696)

## Summary

This paper introduces Gnomon, a physics-informed forecasting framework for low-Earth-orbit (LEO) satellite networks that predicts downlink throughput, uplink throughput, and round-trip time (RTT) under varying data availability. Gnomon incorporates a physics layer to reconstruct serving geometry and four-leg bent-pipe attenuation from public data, supporting three operational modes: terminal history conditioning, nearby public dish measurements, and pure physical covariates. Evaluated on extensive field measurements across multiple U.S. sites, Gnomon significantly outperforms prior baselines across all prediction modes and provides calibrated quantile bands for real TCP flows.

## Key Contributions

- Introduces Gnomon, a physics-informed system for forecasting LEO network link states (downlink throughput, uplink throughput, and round-trip time) under varying trace availability.
- Reconstructs serving geometry and four-leg bent-pipe attenuation from public weather, orbital, routing, and licensing data across three distinct operational modes (own-history, neighbor-trace, and covariate-only).
- Evaluates on 8,260 minutes of 1 Hz measurements across nine sites, reducing downlink-throughput and RTT prediction error by 17% and 11% in own-trace mode and 24.6% and 78.8% in covariate-only mode compared to prior baselines.

## Archivist Review

Reviewed the single proposed open question regarding LEO satellite probing constraints and rejected it due to its narrow, domain-specific nature. No concepts or datasets were proposed or approved.

### Rejected Candidates
- [open_question] High-Density Non-Intrusive LEO Probing (`high-density-non-intrusive-leo-probing`) - low_impact: The question focuses on specific measurement-ethics probing constraints and sampling frequency gaps in LEO satellite deployment rather than a generalizable time-series or machine-learning bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.26696)
- [PDF](https://arxiv.org/pdf/2609.26696)

