---
# CSL-compatible fields
title: "LeapTS: Rethinking Time Series Forecasting as Adaptive Multi-Horizon Scheduling"
author:
  - literal: "Sheng Pan"
  - literal: "Ming Jin"
  - literal: "Bo Du"
  - literal: "Shirui Pan"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10292"

# Custom fields
paper_id: "2605.10292"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "transformer"
  - "efficient-transformer"
architectures:
  []
datasets:
  []
concept_slugs:
  - "adaptive-multi-horizon-scheduling"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:36:41Z"
created_at: "2026-05-14T07:36:41Z"
---

# LeapTS: Rethinking Time Series Forecasting as Adaptive Multi-Horizon Scheduling

**Authors**: Sheng Pan, Ming Jin, Bo Du, Shirui Pan
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10292](https://arxiv.org/abs/2605.10292)

## Summary

LeapTS addresses the limitations of fixed-mapping time series forecasting by treating prediction as a dynamic scheduling process. By integrating a hierarchical controller with neural controlled differential equations, the model adaptively selects prediction scales and steps based on evolving temporal context. This approach improves forecast accuracy while significantly reducing inference latency by avoiding rigid, fixed-length forecasting paths.

## Key Contributions

- Reformulates time series forecasting as a dynamic scheduling process using hierarchical control and neural controlled differential equations.
- Introduces a hierarchical controller that dynamically determines prediction scales and advancement lengths during inference.
- LeapTS achieves a 7.4% performance improvement and 2.6x to 5.3x inference speedup compared to standard Transformer-based architectures on benchmarking tasks.

## Open Questions & Future Work

- [[zero-shot-scheduling-forecasting]]

## Key Concepts

- [[adaptive-multi-horizon-scheduling]]: A forecasting paradigm that treats multi-horizon prediction as a sequence of dynamic decisions rather than a static mapping.

## Archivist Review

I approved the overarching framework of Adaptive Multi-Horizon Scheduling as it fundamentally reframes the standard forecasting objective. The associated open question regarding universal, pretrained scheduling models is a significant and clearly stated research direction. I rejected the hierarchical controller as it is an internal implementation detail of the primary framework.

### Approved Concepts
- Adaptive Multi-Horizon Scheduling: Moves away from fixed-mapping forecasting to a dynamic scheduling paradigm, allowing for adaptive temporal progression.

### Approved Open Questions
- Universal Pretrained Scheduling Models: Moving from domain-specific models to universal, pretrained models is a significant bottleneck in improving the scalability and generalization of deep time series forecasting.

### Rejected Candidates
- [concept] Hierarchical Controller for Forecasting (`hierarchical-controller-forecasting`) - subcomponent_of_broader_mechanism: This is a specific subcomponent of the broader Adaptive Multi-Horizon Scheduling paradigm.

## Links

- [Abstract](https://arxiv.org/abs/2605.10292)
- [PDF](https://arxiv.org/pdf/2605.10292)

