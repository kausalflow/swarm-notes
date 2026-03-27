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
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "control"
  - "time-series"
  - "evaluation"
  - "reasoning"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T15:43:52Z"
created_at: "2026-03-27T15:43:52Z"
---

# Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control

**Authors**: Anne Somalwar, Bruce D. Lee, George J. Pappas, Nikolai Matni
**Date**: 2026-03-24
**Paper ID**: [openalex:2603.23465](https://arxiv.org/abs/2603.23465)

## Summary

This paper analyzes the statistical efficiency trade-off between single-step and multi-step predictive models, particularly in the context of learning-based control where compounding error is a major concern. The authors compare three model classes: single-step, direct multi-step, and single-step models trained with multi-step losses, focusing on linear dynamical systems. They theoretically establish that when the system dynamics are perfectly captured, single-step models yield the lowest asymptotic error. Conversely, for partially observable systems where the model is misspecified, direct multi-step predictors offer substantial improvements by reducing prediction bias. These observed trade-offs are shown to be relevant even when the predictors are integrated into closed-loop control structures.

## Key Contributions

- Provided the first quantitative analysis of the trade-off between single-step and multi-step predictors for linear dynamical systems.
- Showed that well-specified single-step models achieve the lowest asymptotic prediction error.
- Demonstrated that direct multi-step predictors significantly reduce bias and improve accuracy when the model class suffers from partial observability (model misspecification).
- Provided theoretical and empirical evidence that these trade-offs hold when predictors are deployed in closed-loop control.

## Limitations

The theoretical analysis is primarily focused on linear dynamical systems. The persistence of these trade-offs in highly nonlinear systems remains an open question.

## Open Questions & Future Work

- [[lqr-cost-comparison-multi-step-predictor]]
- [[rigorous-nonlinear-system-analysis]]
- [[closed-loop-control-beyond-lqr]]

## Archivist Review

Archivist review kept only candidates judged central to the paper and reusable across future work. Approved 0 concept(s), 3 open question(s), and 0 dataset(s), with 0 rejected candidate note(s).

### Approved Open Questions
- Analyze closed-loop LQR comparison: This comparison is crucial for practitioners to fully understand the trade-offs in control performance across all three model classes, especially since the prediction error ranking (Prop II.4) contradicted the LQR cost ranking observed between the intermediate and multi-step predictors (Section IV-A).
- Rigorous nonlinear system analysis: Extending the rigorous statistical efficiency guarantees to nonlinear systems would validate the general applicability of the findings beyond linear time-invariant models, which is a significant limitation of the current theoretical work.
- Analyze control performance beyond LQR: Moving beyond the LQR objective allows the findings to inform model design choices in the broader and more complex domain of policy optimization via model-based reinforcement learning.

## Links

- [Abstract](https://arxiv.org/abs/2603.23465)
- [PDF](https://arxiv.org/pdf/2603.23465)

