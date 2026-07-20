---
# CSL-compatible fields
title: "Tailored forecasting from short time series via meta-learning"
author:
  - literal: "Declan A. Norton"
  - literal: "Edward Ott"
  - literal: "Andrew Pomerance"
  - literal: "Brian R. Hunt"
  - literal: "Michelle Girvan"
issued:
  date-parts:
    - [2026, 7, 17]
url: "https://arxiv.org/abs/2501.16325"

# Custom fields
paper_id: "2501.16325"
paper_source: "openalex"
domain: "time-series"
tags:
  - "meta-learning"
  - "time-series"
  - "forecasting"
  - "reservoir-computing"
architectures:
  []
datasets:
  []
concept_slugs:
  - "metafors"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-20T07:50:11Z"
created_at: "2026-07-20T07:50:11Z"
---

# Tailored forecasting from short time series via meta-learning

**Authors**: Declan A. Norton, Edward Ott, Andrew Pomerance, Brian R. Hunt, Michelle Girvan
**Date**: 2026-07-17
**Paper ID**: [openalex:2501.16325](https://arxiv.org/abs/2501.16325)

## Summary

METAFORS is a meta-learning framework designed to address the challenge of forecasting dynamical systems with limited historical data. By utilizing a reservoir computing approach, the method builds and initializes a model tailored to a specific short time series by generalizing from a library of models trained on related, longer time series. The system achieves effective short-term and long-term forecasting even in the absence of contextual labels and across diverse dynamical behaviors.

## Key Contributions

- Introduces METAFORS, a meta-learning framework that leverages knowledge from longer time-series models to improve forecasting performance on systems with limited history.
- Demonstrates the ability to predict both short-term dynamics and long-term statistics for chaotic systems without requiring explicit contextual labels.
- Shows robust performance even when the target system exhibits dynamics substantially different from the related systems in the training library.

## Open Questions & Future Work

- [[meta-learning-scalability-high-dim]]
- [[handling-irregular-multiscale-data]]

## Key Concepts

- [[metafors]]: A meta-learning framework for initializing and tailoring reservoir computing models for forecasting from short, limited time-series data.

## Archivist Review

I have approved the core METAFORS framework for its novel meta-learning approach to reservoir-based forecasting under data scarcity. I also approved two research questions that identify critical bottlenecks—high-dimensional scalability and handling irregular temporal sampling—which are common barriers in time-series forecasting. I rejected no candidates as all provided items met the criteria for long-term relevance and distinct contribution to the field.

### Approved Concepts
- METAFORS: METAFORS provides a novel meta-learning approach for cold-starting and adapting reservoir-based forecasting models, directly addressing data scarcity in dynamical systems.

### Approved Open Questions
- Scalability to High-Dimensional Systems: This bottleneck prevents the application of advanced meta-learning forecasters to complex, real-world climate or biological datasets.
- Handling Irregularly Sampled Data: Real-world observational time series are rarely uniform; solving for irregular sampling is a critical step for practical applicability in clinical and environmental monitoring.

## Links

- [Abstract](https://arxiv.org/abs/2501.16325)
- [PDF](https://arxiv.org/pdf/2501.16325)

