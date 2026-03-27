---
# CSL-compatible fields
title: "Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control"
author:
  - literal: "Anne Somalwar"
  - literal: "Bruce D. Lee"
  - literal: "George J. Pappas"
  - literal: "Nikolai Matni"
issued:
  date-parts:
    - [2026, 3, 24]
url: "https://arxiv.org/abs/2603.23465"

# Custom fields
paper_id: "2603.23465"
paper_source: "arxiv"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
  - "reinforcement-learning"
  - "control"
architectures:
  []
datasets:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-25T21:18:14Z"
created_at: "2026-03-25T21:18:14Z"
---

# Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control

**Authors**: Anne Somalwar, Bruce D. Lee, George J. Pappas, Nikolai Matni
**Date**: 2026-03-24
**Paper ID**: [arxiv:2603.23465](https://arxiv.org/abs/2603.23465)

## Summary

This paper analyzes the trade-offs between single-step and multi-step forecasting models, particularly concerning compounding error in learning-based control for linear dynamical systems. The authors theoretically and empirically compare three approaches: single-step models, direct multi-step models, and single-step models trained with multi-step losses. They establish that when the underlying system dynamics are perfectly captured by the model class, single-step models yield the minimal asymptotic prediction error. Conversely, when model misspecification arises from partial observability, multi-step predictors offer significant advantages by reducing bias and improving overall accuracy, a benefit shown to hold in closed-loop control applications.

## Key Contributions

- Provided the first quantitative analysis of the trade-off between single-step and multi-step forecasting models for linear dynamical systems.
- Demonstrated that well-specified single-step models achieve the lowest asymptotic prediction error.
- Showed that direct multi-step predictors significantly reduce bias and improve accuracy in cases of model misspecification due to partial observability.
- Provided theoretical and empirical evidence that these trade-offs in prediction accuracy persist when models are utilized in closed-loop control systems.

## Limitations

The analysis is primarily focused on linear dynamical systems, and the findings may not directly translate to highly non-linear systems without further investigation.

## Open Questions & Future Work

- [[statistical-efficiency-model-horizon-tradeoff]]
- [[asymptotic-prediction-error-comparison-well-specified]]
- [[irreducible-bias-comparison-misspecified]]
- [[control-cost-decay-well-specified]]
- [[stabilization-regimes-misspecified-theory]]
- [[extension-nonlinear-systems-theory]]
- [[lqr-comparison-multi-step-vs-single-step]]
- [[analysis-other-control-frameworks]]

## Limitations

The analysis is primarily focused on linear dynamical systems, and the findings may not directly translate to highly non-linear systems without further investigation.

## Links

- [ArXiv Abstract](https://arxiv.org/abs/2603.23465)
- [PDF](https://arxiv.org/pdf/2603.23465)

