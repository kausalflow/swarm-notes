---
# CSL-compatible fields
title: "On the Divergence of Accuracy and Mechanism Consistency in Time Series World Models"
author:
  - literal: "Haochen Zhang"
  - literal: "Jiaheng Guo"
  - literal: "Zhen Xu"
  - literal: "Zachary Plotkin"
  - literal: "Nicholas Knoz"
  - literal: "Zhen Tan"
  - literal: "Tianlong Chen"
issued:
  date-parts:
    - [2026, 10, 1]
url: "https://arxiv.org/abs/2610.01842"

# Custom fields
paper_id: "2610.01842"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "mechanism-consistency"
  - "directional-supervision"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-04T10:48:12Z"
created_at: "2026-10-04T10:48:12Z"
---

# On the Divergence of Accuracy and Mechanism Consistency in Time Series World Models

**Authors**: Haochen Zhang, Jiaheng Guo, Zhen Xu, Zachary Plotkin, Nicholas Knoz, Zhen Tan, Tianlong Chen
**Date**: 2026-10-01
**Paper ID**: [openalex:2610.01842](https://arxiv.org/abs/2610.01842)

## Summary

This paper investigates time series world models (TSWMs) that predict controlled system states from observed history, planned actions, and exogenous inputs. The authors formalize TSWM design choices and introduce mechanism consistency, a metric evaluating whether forecast responses to modified plans follow declared physical or clinical directions. Through a benchmark consolidating eight public datasets, they reveal that standard prediction error and mechanism consistency diverge, with low-error models frequently failing consistency tests. Finally, they propose directional supervision, a novel loss function that restores mechanism consistency without sacrificing forecasting accuracy.

## Key Contributions

- Proposes a formalization for time series world models (TSWMs) that introduces mechanism consistency to measure whether forecasts respond to changed plans in declared directions.
- Consolidates a benchmark of eight public datasets spanning engineered infrastructure and clinical care across seven backbones and five seeds to evaluate TSWM design choices.
- Discovers a fundamental divergence between prediction error and mechanism consistency, showing that lowest-error configurations often fail in consistency.
- Introduces directional supervision as a training objective that successfully improves mechanism consistency without degrading mean absolute error (MAE).

## Open Questions & Future Work

- [[extending-tswm-supervision-and-control]]

## Key Concepts

- [[mechanism-consistency]]: A metric evaluating whether shifting an action in a time series world model moves the forecast in the declared physical or clinical direction.
- [[directional-supervision]]: A training objective that penalizes wrong-signed forecast responses to action shifts to align time series world models with physical or clinical dynamics.

## Archivist Review

Approved the core methodological concepts (Mechanism Consistency and Directional Supervision) as they provide a reusable framework and training objective for evaluating and improving counterfactual responsiveness in time series world models. Also approved the primary open question regarding extending supervision and control. No datasets were approved as none were specifically named in the analysis.

### Approved Concepts
- Mechanism Consistency: Establishes a foundational evaluation framework and metric for whether time series world models respect physical and clinical directional constraints under counterfactual action shifts.
- Directional Supervision: Provides a simple, effective training objective that bridges the gap between predictive accuracy and causal/mechanism consistency.

### Approved Open Questions
- Extending TSWM Supervision and Control: Extending consistency supervision to discrete/event actions and closed-loop control environments is critical for safe deployment in high-stakes domains like clinical care and autonomous engineering systems.

## Links

- [Abstract](https://arxiv.org/abs/2610.01842)
- [PDF](https://arxiv.org/pdf/2610.01842)

