---
# CSL-compatible fields
title: "Improvements to the post-processing of weather forecasts using machine learning and feature selection"
author:
  - literal: "Kazuma Iwase"
  - literal: "Tomoyuki Takenawa"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2604.19340"

# Custom fields
paper_id: "2604.19340"
paper_source: "openalex"
domain: "time-series,"
tags:
  - "time-series,"
  - "forecasting,"
  - "machine-learning,"
architectures:
  []
datasets:
  []
concept_slugs:
  - "event-weighted-training-strategy"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-24T07:00:02Z"
created_at: "2026-04-24T07:00:02Z"
---

# Improvements to the post-processing of weather forecasts using machine learning and feature selection

**Authors**: Kazuma Iwase, Tomoyuki Takenawa
**Date**: 2026-04-21
**Paper ID**: [openalex:2604.19340](https://arxiv.org/abs/2604.19340)

## Summary

This paper improves post-processing of weather forecasts using LightGBM, incorporating spatial feature selection from neighboring grid points to enhance accuracy for precipitation, temperature, and wind speed. The approach consistently outperforms raw Mesoscale Model (MSM) forecasts and existing JMA guidance (MSMG) in RMSE metrics. Furthermore, the study explores Tweedie-based losses and event-weighted training to mitigate challenges posed by the highly skewed, zero-inflated nature of precipitation data.

## Key Contributions

- Introduces a feature selection strategy leveraging surrounding grid points to enhance local meteorological forecasts.
- Demonstrates that LightGBM outperforms baseline CNNs and official JMA MSM Guidance (MSMG) in RMSE across various locations.
- Evaluates Tweedie-based loss functions and event-weighted training to address distribution skewness in precipitation forecasting.

## Open Questions & Future Work

- [[site-dependent-topographic-integration]]

## Key Concepts

- [[event-weighted-training-strategy]]: A training strategy that adjusts instance weights to improve model performance on rare, high-threshold precipitation events.

## Archivist Review

I approved the event-weighted training strategy as it offers a reusable mechanism for addressing imbalanced time-series regression tasks. I also approved the open question regarding site-specific topographic integration, as it highlights a critical bottleneck in generalizing weather forecasting models across heterogeneous environments. The MSM dataset was rejected as a local institutional dataset rather than a foundational research benchmark.

### Approved Concepts
- Event-weighted training strategy: Addresses the challenge of skewed target distributions with sparse extreme events in meteorological forecasting.

### Approved Open Questions
- Integrating Site-Specific Topographic Data: Addressing site-dependent performance is crucial for developing robust, operational post-processing systems that can generalize across geographically diverse locations without requiring extensive, independent hyperparameter tuning for every new station.

### Rejected Candidates
- [dataset] MSM dataset (`msm-dataset`) - low_impact: This is a specific regional dataset not widely utilized as a standard benchmark in the broader ML research community.

## Links

- [Abstract](https://arxiv.org/abs/2604.19340)
- [PDF](https://arxiv.org/pdf/2604.19340)

