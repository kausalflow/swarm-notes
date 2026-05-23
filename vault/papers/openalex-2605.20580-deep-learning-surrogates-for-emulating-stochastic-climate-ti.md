---
# CSL-compatible fields
title: "Deep Learning Surrogates for Emulating Stochastic Climate Tipping Dynamics"
author:
  - literal: "Adeline Hillier"
  - literal: "Jennifer Sleeman"
  - literal: "Jay Brett"
  - literal: "Caroline Tang"
  - literal: "Jenelle Millison"
  - literal: "Anand Gnanadesikan"
issued:
  date-parts:
    - [2026, 5, 20]
url: "https://arxiv.org/abs/2605.20580"

# Custom fields
paper_id: "2605.20580"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "time-series"
  - "forecasting"
  - "uncertainty-quantification"
  - "climate-science"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dynamics-informed-temporal-fusion-transformer"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-23T07:25:47Z"
created_at: "2026-05-23T07:25:47Z"
---

# Deep Learning Surrogates for Emulating Stochastic Climate Tipping Dynamics

**Authors**: Adeline Hillier, Jennifer Sleeman, Jay Brett, Caroline Tang, Jenelle Millison, Anand Gnanadesikan
**Date**: 2026-05-20
**Paper ID**: [openalex:2605.20580](https://arxiv.org/abs/2605.20580)

## Summary

This paper develops a dynamics-informed Temporal Fusion Transformer to act as a computationally efficient surrogate for complex Earth system simulations. By modeling multivariate, non-stationary time series of ocean transport, the surrogate accurately forecasts tipping events and captures transition timing uncertainty. The approach delivers a 465x speedup over traditional numerical methods while preserving differentiability, enabling faster exploration of initial conditions and system parameters.

## Key Contributions

- Introduces a dynamics-informed TFT architecture that accurately anticipates the timing of Atlantic and Pacific ocean transport collapse events.
- Demonstrates the model's ability to capture stochastic uncertainty in climate transition timing across ensemble predictions.
- Achieves a 465x computational speedup compared to numerical Earth system simulators while maintaining parameter differentiability.

## Open Questions & Future Work

- [[efficient-tipping-exploration]]

## Key Concepts

- [[dynamics-informed-temporal-fusion-transformer]]: A Temporal Fusion Transformer variant that integrates physical or dynamical priors to emulate the stochastic transition behavior of complex Earth system models.

## Archivist Review

The paper proposes a specialized architecture for forecasting stochastic tipping events, which I approved as a concept. I also approved the open question regarding the systematic exploration of tipping point regions, as this is a persistent challenge in climate-related scientific machine learning. Other potential candidates were either too specific to the paper or already covered by the scope of the approved items.

### Approved Concepts
- Dynamics-informed Temporal Fusion Transformer: Adapts a standard transformer architecture to incorporate dynamical system priors, enabling stable forecasting of rare, high-stakes events like climate tipping.

### Approved Open Questions
- Efficient Mapping of Tipping Regions: Systematically identifying the trigger conditions for irreversible climate events is foundational for effective risk assessment and long-range environmental planning.

### Rejected Candidates
- [concept] Dynamics-informed Temporal Fusion Transformer (`dynamics-informed-temporal-fusion-transformer`) - duplicate_existing: The candidate was approved as a concept note under a slightly refined definition.

## Links

- [Abstract](https://arxiv.org/abs/2605.20580)
- [PDF](https://arxiv.org/pdf/2605.20580)

