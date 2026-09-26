---
# CSL-compatible fields
title: "Sparse-Observation Atmospheric Thermal Forecasting with Physics-Informed Neural Networks for Climate-Aware Digital Twins"
author:
  - literal: "Tannaz Goodarzvand Chegini"
  - literal: "Elyas Shivanian"
  - literal: "Behzad Karimi"
  - literal: "Faraz Dadgostari"
issued:
  date-parts:
    - [2026, 9, 23]
url: "https://arxiv.org/abs/2609.27290"

# Custom fields
paper_id: "2609.27290"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "time-series"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-26T09:37:53Z"
created_at: "2026-09-26T09:37:53Z"
---

# Sparse-Observation Atmospheric Thermal Forecasting with Physics-Informed Neural Networks for Climate-Aware Digital Twins

**Authors**: Tannaz Goodarzvand Chegini, Elyas Shivanian, Behzad Karimi, Faraz Dadgostari
**Date**: 2026-09-23
**Paper ID**: [openalex:2609.27290](https://arxiv.org/abs/2609.27290)

## Summary

This study evaluates a physics-informed neural network (PINN) for short-horizon potential-temperature forecasting constrained by a pressure-coordinate thermodynamic advection-source equation. Evaluated on hourly ERA5 reanalysis data at 1-, 2-, and 3-hour lead times, the model achieves growing relative accuracy improvements over baselines as the horizon extends and remains robust under extreme observation sparsity down to 5% density. However, regional stress tests reveal performance degradation over complex terrain due to limitations in the fixed vertical-coordinate representation.

## Key Contributions

- Evaluates a pressure-coordinate thermodynamic PINN for short-horizon potential-temperature forecasting under sparse observations.
- Demonstrates that mean RMSE improvement over the strongest baseline grows from 8.1% at 1-hour to 23.8% at 3-hour lead times in an Oklahoma development case.
- Shows robust performance under an observation-density sweep down to 5% of candidate locations, maintaining a 14.6-16.9% advantage at 3 hours.
- Identifies a terrain-related applicability limit via a Montana stress test where complex terrain caused a 3-hour performance degradation of ~17.5%.

## Limitations

Performance is bounded by the validity of a fixed vertical-coordinate representation over complex terrain, as revealed by stress tests in mountainous regions.

## Open Questions & Future Work

- [[terrain-adaptive-pinn-atmospheric-forecasting]]

## Archivist Review

Evaluated the candidates against vault standards. No standalone concept note is approved because the underlying mechanism uses standard pressure-coordinate thermodynamic PINN formulations rather than a distinct reusable ML concept. One high-value open question concerning terrain-adaptive vertical coordinate representations for physics-informed atmospheric forecasting is approved.

### Approved Open Questions
- Terrain-Adaptive PINN Atmospheric Forecasting: Crucial for overcoming terrain-related applicability limits and enhancing the reliability and generalization of physics-informed atmospheric digital twins under sparse observations.

### Rejected Candidates
- [open_question] Terrain-Adaptive PINN Atmospheric Forecasting (`terrain-adaptive-pinn-atmospheric-forecasting`) - duplicate_existing: Already approved as an open question.

## Links

- [Abstract](https://arxiv.org/abs/2609.27290)
- [PDF](https://arxiv.org/pdf/2609.27290)

