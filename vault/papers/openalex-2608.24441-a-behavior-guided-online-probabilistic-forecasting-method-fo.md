---
# CSL-compatible fields
title: "A Behavior-Guided Online Probabilistic Forecasting Method for Electric vehicle Charging Loads"
author:
  - literal: "Chenghan Li"
  - literal: "Qingxiang Liu"
  - literal: "Yinliang Xu"
  - literal: "Yuxuan Liang"
issued:
  date-parts:
    - [2026, 8, 25]
url: "https://arxiv.org/abs/2608.24441"

# Custom fields
paper_id: "2608.24441"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "probabilistic-forecasting"
  - "uncertainty"
  - "online-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dual-timescale-behavior-representation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T16:59:58Z"
created_at: "2026-08-28T16:59:58Z"
---

# A Behavior-Guided Online Probabilistic Forecasting Method for Electric vehicle Charging Loads

**Authors**: Chenghan Li, Qingxiang Liu, Yinliang Xu, Yuxuan Liang
**Date**: 2026-08-25
**Paper ID**: [openalex:2608.24441](https://arxiv.org/abs/2608.24441)

## Summary

This paper introduces a behavior-guided online probabilistic forecasting framework for electric vehicle charging loads to handle behavioral heterogeneity and temporal variability. The method employs a dual-timescale behavior representation to capture both persistent station-specific patterns and recent behavioral shifts, using semantic encoding to guide drift-aware adaptation and a delayed-feedback mechanism for consistent online updates. Experiments across ten heterogeneous charging stations demonstrate substantial reductions in MSE and Pinball loss compared to conventional and concept-drift-aware baselines.

## Key Contributions

- Proposes a behavior-guided online probabilistic forecasting framework that explicitly characterizes persistent station-specific patterns and recent behavioral changes for electric vehicle charging loads.
- Constructs a dual-timescale behavior representation to distinguish long-term charging characteristics from recent states and quantify their deviations.
- Achieves a 15.3% reduction in MSE and a 17.8% reduction in Pinball loss for 1-h-ahead forecasting, and 16.8% and 22.6% improvements respectively for 4-h-ahead forecasting over baseline models.

## Open Questions & Future Work

- [[incorporating-external-factors-ev-forecasting]]

## Key Concepts

- [[dual-timescale-behavior-representation]]: A representation framework that distinguishes long-term charging characteristics from recent behavioral states to quantify load deviations.

## Archivist Review

Approved the central dual-timescale behavior representation concept and the explicit open question regarding external factor incorporation for EV charging load forecasting. Rejected other candidates to maintain strict vault standards.

### Approved Concepts
- Dual-Timescale Behavior Representation: Core methodology for capturing both persistent station-specific characteristics and recent behavioral changes in EV charging loads.

### Approved Open Questions
- Incorporating External Factors in EV Forecasting: Incorporating exogenous drivers is crucial for scaling load forecasting frameworks to real-world smart grid applications where weather and price signals heavily perturb user behavior.

## Links

- [Abstract](https://arxiv.org/abs/2608.24441)
- [PDF](https://arxiv.org/pdf/2608.24441)

