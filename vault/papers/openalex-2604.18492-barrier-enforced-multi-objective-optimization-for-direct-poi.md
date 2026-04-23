---
# CSL-compatible fields
title: "Barrier-enforced multi-objective optimization for direct point and sharp interval forecasting"
author:
  - literal: "Worachit Amnuaypongsa"
  - literal: "Yotsapat Suparanonrat"
  - literal: "Pana Wanitchollakit"
  - literal: "Jitkomut Songsiri"
issued:
  date-parts:
    - [2026, 4, 20]
url: "https://arxiv.org/abs/2604.18492"

# Custom fields
paper_id: "2604.18492"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "probabilistic-forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "barrier-enforced-multi-objective-optimization"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-23T06:55:35Z"
created_at: "2026-04-23T06:55:35Z"
---

# Barrier-enforced multi-objective optimization for direct point and sharp interval forecasting

**Authors**: Worachit Amnuaypongsa, Yotsapat Suparanonrat, Pana Wanitchollakit, Jitkomut Songsiri
**Date**: 2026-04-20
**Paper ID**: [openalex:2604.18492](https://arxiv.org/abs/2604.18492)

## Summary

This paper presents a multi-objective probabilistic forecasting framework designed to produce simultaneous point and interval forecasts using a unified neural network. By treating point and interval prediction as a multi-objective optimization task, the model uses multi-gradient descent to adaptively balance objectives, eliminating the need for manual hyperparameter tuning. A core innovation is a scale-independent log-barrier loss function that strictly enforces target coverage probabilities while minimizing interval width. Evaluations on intra-day solar irradiance forecasting show the method is highly competitive with state-of-the-art architectures like LSTMs, Transformers, and Chronos.

## Key Contributions

- Introduces a multi-objective forecasting framework that generates simultaneous point and interval predictions without requiring manual loss weight tuning.
- Proposes an extended log-barrier PI loss function that enforces target prediction interval coverage probability (PICP) while maximizing sharpness.
- Demonstrates that the proposed framework achieves superior coverage and interval sharpness compared to existing methods on intra-day solar irradiance forecasting.

## Open Questions & Future Work

- [[extending-moo-to-cdf-and-multi-quantile-forecasting]]

## Key Concepts

- [[barrier-enforced-multi-objective-optimization]]: A multi-objective optimization framework for simultaneous point and interval forecasting that eliminates manual loss balancing via adaptive log-barrier constraints.

## Archivist Review

I have approved the core methodological contribution, the barrier-enforced multi-objective optimization framework, as it provides a reusable, model-agnostic way to handle the coverage-sharpness trade-off in probabilistic forecasting. I also approved the open question regarding the extension of these gradient-based techniques to more complex distributional outputs, as this represents a significant structural bottleneck in the field. Other potential candidates were deemed either too specific to the implementation or already covered by the scope of the approved concept.

### Approved Concepts
- Barrier-enforced multi-objective optimization: It addresses the common issue of manual weight tuning in multi-objective forecasting by using a barrier-enforced multi-gradient approach.

### Approved Open Questions
- Extending MOO for complex uncertainty: Extending this methodology to more complex probabilistic outputs is essential for transitioning from simple interval forecasts to full distributional forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2604.18492)
- [PDF](https://arxiv.org/pdf/2604.18492)

