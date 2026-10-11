---
# CSL-compatible fields
title: "A Graph Neural Network for Global Daily Fire Radiative Power Prediction at Medium-Range Lead Times"
author:
  - literal: "Li Zhang"
  - literal: "Jun Wang"
  - literal: "Isidora Jankov"
  - literal: "Yongxin Liu"
  - literal: "Gonzalo A. Ferrada"
  - literal: "Ravan Ahmadov"
  - literal: "LIGIA BERNARDET"
  - literal: "Haonan Chen"
  - literal: "Shobha Kondragunta"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.11022"

# Custom fields
paper_id: "2610.11022"
paper_source: "openalex"
domain: "time-series"
tags:
  - "graph-neural-network"
  - "time-series"
  - "forecasting"
  - "multimodal"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-11T11:05:03Z"
created_at: "2026-10-11T11:05:03Z"
---

# A Graph Neural Network for Global Daily Fire Radiative Power Prediction at Medium-Range Lead Times

**Authors**: Li Zhang, Jun Wang, Isidora Jankov, Yongxin Liu, Gonzalo A. Ferrada, Ravan Ahmadov, LIGIA BERNARDET, Haonan Chen, Shobha Kondragunta
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.11022](https://arxiv.org/abs/2610.11022)

## Summary

This paper develops a spatiotemporal graph neural network to predict global daily fire radiative power (FRP) one to seven days ahead, overcoming the 1.5-day latency and static-fire assumptions of current operational aerosol forecasting systems. Using meteorological reanalysis, vegetation data, and historical fire observations, the data-driven model successfully reproduces the global seasonal cycle and outperforms persistence baselines, reducing mean squared error by up to 43% at a seven-day lead. Evaluation across 2023-2024 demonstrates robust fire detection skill, though systematic underestimation of fire intensity and small-fire placement remain key challenges.

## Key Contributions

- Developed a spatiotemporal graph neural network to predict global daily fire radiative power (FRP) 1 to 7 days ahead using reanalysis meteorology, land-cover, vegetation, and historical fire data.
- Evaluated the model on 2023-2024 data, demonstrating a mean squared error reduction of 32% (1-day lead) and 43% (7-day lead) in 2023 at 0.1 degree resolution compared to persistence baselines.
- Achieved critical success index values ranging from 0.32 to 0.60 at 1 degree resolution, showing robust fire detection skill across medium-range lead times.
- Identified intensity calibration and small-fire placement as the primary remaining challenges for supporting operational aerosol forecasting.

## Limitations

Intensity skill degrades more rapidly with lead time than detection skill, and radiative power for large fires is systematically underestimated.

## Archivist Review

No new concepts or datasets meet the rigorous criteria for permanent archival notes.

## Links

- [Abstract](https://arxiv.org/abs/2610.11022)
- [PDF](https://arxiv.org/pdf/2610.11022)

