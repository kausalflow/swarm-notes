---
# CSL-compatible fields
title: "Horizon-specific Expert Fusion for Photovoltaic Power Forecasting"
author:
  - literal: "Xu Yuqing"
  - literal: "Zhou Liguo"
  - literal: "Sun Ze"
  - literal: "Yu Lei"
  - literal: "Jiang Mingming"
issued:
  date-parts:
    - [2026, 9, 14]
url: "https://arxiv.org/abs/2609.15035"

# Custom fields
paper_id: "2609.15035"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:43:52Z"
created_at: "2026-09-17T09:43:52Z"
---

# Horizon-specific Expert Fusion for Photovoltaic Power Forecasting

**Authors**: Xu Yuqing, Zhou Liguo, Sun Ze, Yu Lei, Jiang Mingming
**Date**: 2026-09-14
**Paper ID**: [openalex:2609.15035](https://arxiv.org/abs/2609.15035)

## Summary

This paper introduces a hierarchical ensemble framework for short-term photovoltaic power forecasting that combines temporal neural models, historical analogs, state climatology, and gradient-boosted trees. By leveraging solar geometry and numerical weather predictions alongside horizon-specific convex weights, the model adapts to varying solar cycles and weather-driven fluctuations. Evaluated on PVDAQ and GEFCom2014 datasets, the approach achieves competitive accuracy and outperforms individual baselines like LightGBM and Chronos-2 under identical calibration.

## Key Contributions

- Develops a hierarchical ensemble combining temporal neural models, historical analogs, state climatology, and gradient-boosted trees for short-term photovoltaic power forecasting.
- Introduces horizon-specific convex weighting guided by solar geometry and numerical weather forecasts to combine complementary predictions.
- Applies a separate calibration step using historical forecast errors to correct for recent bias across 15-240 minute and hourly horizons.
- Demonstrates on PVDAQ a daylight capacity-normalized mean absolute error of 4.315%, reducing error by 4.11% over full-feature LightGBM and 6.03% over Chronos-2.

## Limitations

The advantage of horizon-specific combination over strong individual models depends on the specific dataset and evaluation period.

## Open Questions & Future Work

- [[multisite-pv-ensemble-generalization]]

## Archivist Review

Strictly evaluated the paper under the time-series forecasting review policy. The proposed concept 'Horizon-specific Expert Fusion' is a paper-local ensemble combination method for photovoltaic generation and does not qualify as a universal, broadly reusable ML architecture note. The open question regarding multisite PV ensemble generalization and transferability is approved as a valid, specific research challenge. Datasets (PVDAQ, GEFCom2014) are already present in the vault.

### Approved Open Questions
- Multisite PV Ensemble Generalization: Crucial for moving beyond site-specific heuristic ensembles toward generalizable, computationally efficient photovoltaic forecasting systems.

### Rejected Candidates
- [concept] Horizon-specific Expert Fusion (`horizon-specific-expert-fusion`) - paper_local: A paper-local hierarchical ensemble combination method for photovoltaic power forecasting that does not generalize as a distinct universal ML primitive.

## Links

- [Abstract](https://arxiv.org/abs/2609.15035)
- [PDF](https://arxiv.org/pdf/2609.15035)

