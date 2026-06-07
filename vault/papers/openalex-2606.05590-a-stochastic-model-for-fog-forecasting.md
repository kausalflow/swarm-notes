---
# CSL-compatible fields
title: "A stochastic model for fog forecasting"
author:
  - literal: "Elsa Cardoso-Bihlo"
  - literal: "Boualem Khouider"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.05590"

# Custom fields
paper_id: "2606.05590"
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
  - "ising-model-based-fog-simulation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:19:10Z"
created_at: "2026-06-07T08:19:10Z"
---

# A stochastic model for fog forecasting

**Authors**: Elsa Cardoso-Bihlo, Boualem Khouider
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.05590](https://arxiv.org/abs/2606.05590)

## Summary

This paper proposes a stochastic-deterministic model for fog forecasting that utilizes the Ising model from statistical mechanics to simulate boundary layer fog dynamics. Unlike standard parameterizations, this high-resolution approach captures the complex horizontal structures of fog, including various cellular and roll patterns. Evaluation using advection fog data from St. John's Airport confirms the model's ability to effectively simulate fog cover life cycles and provides quantitative performance metrics for its predictive accuracy.

## Key Contributions

- Introduces a high-resolution stochastic-deterministic model for fog life-cycle simulation based on the Ising model from statistical mechanics.
- Demonstrates the model's capability to replicate complex horizontal fog structures, such as bands, rolls, and cells, using advection fog data from St. John's Airport.
- Validates predictive skill through contingency table metrics on three representative advection fog case studies.

## Open Questions & Future Work

- [[automated-parameter-calibration-for-stochastic-fog-models]]

## Key Concepts

- [[ising-model-based-fog-simulation]]: A stochastic-deterministic modeling framework that leverages the Ising model to simulate the life cycle and spatial morphology of fog cover.

## Archivist Review

I have approved the core methodological concept of Ising-model-based fog simulation as it introduces a distinct physical inductive bias for spatial forecasting that is highly reusable in meteorological time-series. The open question regarding automated parameter calibration is also approved as it targets a critical operational bottleneck in physics-based stochastic models that hinders their scalability. Routine contingency-table evaluation and site-specific case study details were rejected as they do not constitute novel architectural concepts or datasets.

### Approved Concepts
- Ising-model-based-fog-simulation: Provides a novel physical inductive bias for modeling spatial structure in boundary layer processes, which is a significant departure from standard CNN/RNN forecasting paradigms.

### Approved Open Questions
- Automated Calibration of Fog Models: Manual parameter tuning significantly limits the operational utility and generalizability of physical-stochastic hybrid forecasting models.

## Links

- [Abstract](https://arxiv.org/abs/2606.05590)
- [PDF](https://arxiv.org/pdf/2606.05590)

