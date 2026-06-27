---
# CSL-compatible fields
title: "Cellular Predictions on the Move: What about Data?"
author:
  - literal: "Natalia Vesselinova"
  - literal: "Pauliina Ilmonen"
issued:
  date-parts:
    - [2026, 6, 24]
url: "https://arxiv.org/abs/2606.25709"

# Custom fields
paper_id: "2606.25709"
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
processed_at: "2026-06-27T07:43:00Z"
created_at: "2026-06-27T07:43:00Z"
---

# Cellular Predictions on the Move: What about Data?

**Authors**: Natalia Vesselinova, Pauliina Ilmonen
**Date**: 2026-06-24
**Paper ID**: [openalex:2606.25709](https://arxiv.org/abs/2606.25709)

## Summary

This paper shifts the focus of mobile cellular load forecasting from model architecture development to data-centric optimization. The authors hypothesize that integrating external information regarding the population dynamics and mobility patterns of traffic sources provides a more powerful signal for prediction than relying solely on historical cellular data. Validation on a highway scenario confirms that characterizing these generative processes leads to approximately 60% improvements in forecasting performance.

## Key Contributions

- Demonstrates that incorporating population dynamics and mobility data significantly enhances mobile cellular load forecasting compared to using cellular traffic data alone.
- Achieves approximately 60% improvement in forecasting accuracy for highway cellular load scenarios by integrating traffic source dynamics as exogenous features.
- Establishes a data-centric perspective for network resource optimization, highlighting that the quality and nature of input data can be more impactful than model architecture improvements.

## Open Questions & Future Work

- [[robustness-of-population-dynamics-forecasting]]

## Archivist Review

The paper offers a data-centric shift for cellular load forecasting by focusing on population dynamics as a generative process. While the shift is significant for the domain, it does not propose a specific, named, and reusable mechanism beyond the general idea of feature engineering, thus no concepts were approved. The open question regarding the robustness of these dynamics-informed models against concept drift is valuable for tracking the reliability of spatiotemporal forecasting systems.

### Approved Open Questions
- Robustness of Population Dynamics Forecasting: Current state-of-the-art models for cellular load forecasting are highly dependent on static spatial features. If these features fail to generalize during crises (e.g., pandemics or shifts in urban planning), the network resource management systems relying on these predictions may fail, leading to reduced reliability and latency guarantees.

### Rejected Candidates
- [open_question] Robustness of Population Dynamics Forecasting (`robustness-of-population-dynamics-forecasting`) - other: This is a strong open question that targets the limitation of relying on static spatial-temporal features for forecasting under drift.

## Links

- [Abstract](https://arxiv.org/abs/2606.25709)
- [PDF](https://arxiv.org/pdf/2606.25709)

