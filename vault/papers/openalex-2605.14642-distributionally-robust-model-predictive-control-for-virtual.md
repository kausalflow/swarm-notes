---
# CSL-compatible fields
title: "Distributionally Robust Model Predictive Control for Virtual Power Plants"
author:
  - literal: "Nikolas Recke"
  - literal: "Mathias Hudoba de Badyn"
issued:
  date-parts:
    - [2026, 5, 14]
url: "https://arxiv.org/abs/2605.14642"

# Custom fields
paper_id: "2605.14642"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "reinforcement-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "wasserstein-ambiguity-sets-for-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-17T07:31:05Z"
created_at: "2026-05-17T07:31:05Z"
---

# Distributionally Robust Model Predictive Control for Virtual Power Plants

**Authors**: Nikolas Recke, Mathias Hudoba de Badyn
**Date**: 2026-05-14
**Paper ID**: [openalex:2605.14642](https://arxiv.org/abs/2605.14642)

## Summary

This paper introduces a distributionally robust model predictive control (DRMPC) framework to optimize Virtual Power Plant (VPP) operations amidst electricity price and weather volatility. The approach leverages data-driven forecasts to build time-varying Wasserstein ambiguity sets, allowing the controller to account for distributional shifts in real-time. Experimental validation using real Nordic market data demonstrates that the method provides reliable economic improvements over traditional MPC, provided the ambiguity radius is appropriately tuned to balance robustness and performance.

## Key Contributions

- Introduced a distributionally robust model predictive control (DRMPC) framework for Virtual Power Plants (VPPs) that manages electricity price and weather uncertainty.
- Developed a technique to construct time-varying Wasserstein ambiguity sets that adapt to forecast dispersion, ensuring tractable real-time decision-making.
- Demonstrated that DR-MPC achieves consistent economic gains of up to 0.8% over standard forecast-based MPC in Nordic VPP operational scenarios.

## Limitations

The performance of the DR-MPC framework is highly sensitive to the choice of the ambiguity radius, as excessively large radii introduce over-conservatism that degrades economic performance.

## Open Questions & Future Work

- [[temporal-dependencies-in-wasserstein-ambiguity-sets]]

## Key Concepts

- [[wasserstein-ambiguity-sets-for-forecasting]]: A method for constructing adaptive Wasserstein ambiguity sets from forecast dispersion to improve the robustness of model predictive control.

## Archivist Review

I approved the concept of Wasserstein ambiguity sets for forecasting as it provides a principled way to integrate forecast dispersion into distributionally robust control. The open question regarding temporal dependencies in ambiguity sets was approved for its importance in moving beyond independent stage-wise modeling in multi-step control tasks. I maintained strict criteria for reusable mechanisms, rejecting subcomponents and generic nomenclature.

### Approved Concepts
- Wasserstein ambiguity sets for forecasting: Provides a method to make MPC robust against distributional uncertainty in price and weather data by integrating forecasting directly into the ambiguity set construction.

### Approved Open Questions
- Capturing temporal dependencies in ambiguity sets: Addressing temporal dependencies is critical for improving the performance of VPPs, as storage-related arbitrage decisions inherently depend on the joint distribution of market signals over time.

## Links

- [Abstract](https://arxiv.org/abs/2605.14642)
- [PDF](https://arxiv.org/pdf/2605.14642)

