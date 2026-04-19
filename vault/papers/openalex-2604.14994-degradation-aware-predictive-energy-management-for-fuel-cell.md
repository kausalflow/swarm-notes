---
# CSL-compatible fields
title: "Degradation-aware Predictive Energy Management for Fuel Cell-Battery Ship Power System with Data-driven Load Forecasting"
author:
  - literal: "Timon Kopka"
  - literal: "Sara Tamburello"
  - literal: "Luca Oneto"
  - literal: "Lindert van Biert"
  - literal: "Henk Polinder"
  - literal: "Andrea Coraddu"
issued:
  date-parts:
    - [2026, 4, 16]
url: "https://arxiv.org/abs/2604.14994"

# Custom fields
paper_id: "2604.14994"
paper_source: "openalex"
domain: "robotics"
tags:
  - "time-series"
  - "forecasting"
  - "reinforcement-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-19T06:24:20Z"
created_at: "2026-04-19T06:24:20Z"
---

# Degradation-aware Predictive Energy Management for Fuel Cell-Battery Ship Power System with Data-driven Load Forecasting

**Authors**: Timon Kopka, Sara Tamburello, Luca Oneto, Lindert van Biert, Henk Polinder, Andrea Coraddu
**Date**: 2026-04-16
**Paper ID**: [openalex:2604.14994](https://arxiv.org/abs/2604.14994)

## Summary

This paper introduces a degradation-aware predictive energy management strategy to optimize the operational costs of hydrogen-battery hybrid ship power systems. By integrating data-driven load forecasting with an optimization framework that explicitly accounts for both hydrogen fuel usage and cell degradation, the approach significantly improves upon standard filter-based control methods. The proposed method is validated using real operational data from a harbor tug, demonstrating substantial reductions in both energy consumption and mechanical wear across multiple prediction horizons.

## Key Contributions

- Proposes a degradation-aware predictive energy management strategy for hybrid fuel cell-battery ship power systems.
- Achieves 5.8% reduction in hydrogen consumption and 36.4% reduction in fuel cell degradation over a 15-minute horizon compared to filter-based benchmarks.
- Demonstrates further cost reductions of 3.8% and 14.0% when extending the load prediction horizon to 1 hour using onboard vessel measurements.

## Open Questions & Future Work

- [[fuel-cell-eol-optimization-variable]]

## Archivist Review

The paper addresses a specific energy management problem in maritime power systems. I approved the proposed open question regarding end-of-life optimization as it represents a meaningful shift in how degradation constraints are handled in control systems. I rejected the concept candidate because the degradation-aware management strategy is highly domain-specific to fuel cell-battery systems and does not constitute a generally reusable forecasting or representation mechanism.

### Approved Open Questions
- End-of-life as optimization variable: Defining end-of-life as an optimization variable rather than a fixed constant would allow energy management strategies to dynamically trade off component longevity against operational costs in a more flexible and realistic manner.

### Rejected Candidates
- [concept] Degradation-aware predictive energy management (`degradation-aware-predictive-energy-management`) - paper_local: This is a specific application-level control strategy rather than a general, reusable methodological concept for time series forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2604.14994)
- [PDF](https://arxiv.org/pdf/2604.14994)

