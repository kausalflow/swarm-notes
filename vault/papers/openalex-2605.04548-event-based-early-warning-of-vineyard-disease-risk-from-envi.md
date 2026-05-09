---
# CSL-compatible fields
title: "Event-Based Early Warning of Vineyard Disease Risk from Environmental Time Series"
author:
  - literal: "Ivica Dimitrovski"
  - literal: "Ivan Kitanovski"
  - literal: "Danco Davcev"
  - literal: "Slobodan Kalajdziski"
  - literal: "Kosta Mitreski"
issued:
  date-parts:
    - [2026, 5, 6]
url: "https://arxiv.org/abs/2605.04548"

# Custom fields
paper_id: "2605.04548"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "lstm"
  - "cnn"
architectures:
  []
datasets:
  []
concept_slugs:
  - "event-based-early-warning-formulation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-09T07:02:07Z"
created_at: "2026-05-09T07:02:07Z"
---

# Event-Based Early Warning of Vineyard Disease Risk from Environmental Time Series

**Authors**: Ivica Dimitrovski, Ivan Kitanovski, Danco Davcev, Slobodan Kalajdziski, Kosta Mitreski
**Date**: 2026-05-06
**Paper ID**: [openalex:2605.04548](https://arxiv.org/abs/2605.04548)

## Summary

This paper addresses the limitations of persistence-biased daily disease classification in agriculture by proposing an event-based forecasting framework. By reformulating the problem to predict the onset of disease-risk periods within a 3-7 day window, the approach encourages models to learn environmental precursors rather than temporal correlations. The method is validated on multi-year agro-meteorological data, showing that different architectures offer distinct trade-offs between early warning lead time and prediction reliability.

## Key Contributions

- Introduces an event-based formulation for vineyard disease risk prediction, focusing on transition detection within a 3-7 day horizon to minimize persistence-driven bias.
- Defines a robust event-labeling protocol that incorporates minimum disease-free gaps to reduce label fragmentation.
- Systematically compares classic ML (XGBoost) and deep learning (LSTM, TCN) models, highlighting performance trade-offs between recall, lead time, and false-alert rates in an agricultural context.

## Open Questions & Future Work

- [[pathogen-specific-disease-validation]]
- [[cross-site-generalization-disease-prediction]]

## Key Concepts

- [[event-based-early-warning-formulation]]: A predictive framework for environmental time series that focuses on identifying onset transitions to critical risk periods rather than daily status classification.

## Archivist Review

I approved the 'event-based early warning formulation' concept because it articulates a distinct methodological shift away from common persistence-biased forecasting patterns in environmental time series. The approved open questions were selected to highlight the field-specific bottlenecks of proxy-label reliance and the broader challenge of cross-site generalization in precision agriculture. Other candidates were rejected to maintain the required scarcity, as they were either local implementation details or generic future work extensions.

### Approved Concepts
- Event-based early warning formulation: Shifts the machine learning paradigm for environmental disease forecasting from simple persistence-based classification to actionable, transition-aware event detection, addressing common biases in standard supervised approaches.

### Approved Open Questions
- Pathogen-specific disease validation: Current reliance on proxy labels may conflate management behavior with actual disease progression, limiting the scientific and practical utility of predictive models in agricultural monitoring.
- Cross-site generalization challenge: Local overfitting is a primary bottleneck in precision agriculture and environmental monitoring, where models often fail to generalize to new fields or shifts in climate conditions.

## Links

- [Abstract](https://arxiv.org/abs/2605.04548)
- [PDF](https://arxiv.org/pdf/2605.04548)

