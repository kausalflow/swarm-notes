---
# CSL-compatible fields
title: "Towards Metric-Agnostic Trajectory Forecasting"
author:
  - literal: "Markus Knoche"
  - literal: "Daan de Geus"
  - literal: "Bastian Leibe"
issued:
  date-parts:
    - [2026, 7, 1]
url: "https://arxiv.org/abs/2607.01133"

# Custom fields
paper_id: "2607.01133"
paper_source: "openalex"
domain: "robotics"
tags:
  - "robotics"
  - "trajectory-prediction"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "tradie-policies"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-04T07:36:03Z"
created_at: "2026-07-04T07:36:03Z"
---

# Towards Metric-Agnostic Trajectory Forecasting

**Authors**: Markus Knoche, Daan de Geus, Bastian Leibe
**Date**: 2026-07-01
**Paper ID**: [openalex:2607.01133](https://arxiv.org/abs/2607.01133)

## Summary

Current trajectory forecasting models often overfit to specific benchmark metrics, which can lead to conflicting model behaviors. This paper proposes a paradigm shift toward metric-agnostic training by optimizing probabilistic predictive distributions instead of metric-specific losses. The proposed Trajectory Distribution Evaluation (TraDiE) policies map these learned distributions to metric-specific outputs, achieving state-of-the-art performance on the Waymo motion prediction benchmark with the DONUT-NLL model.

## Key Contributions

- Identifies the conflict between benchmark-specific training objectives in trajectory forecasting.
- Introduces Trajectory Distribution Evaluation (TraDiE) policies for metric-agnostic forecasting.
- DONUT-NLL achieves state-of-the-art results on Waymo Open Motion Dataset by optimizing the predictive distribution rather than individual metrics.

## Open Questions & Future Work

- [[temporal-continuity-in-probabilistic-forecasting]]

## Key Concepts

- [[tradie-policies]]: A framework that maps probabilistic trajectory distributions to metric-required outputs, decoupling training objectives from benchmark evaluation criteria.

## Archivist Review

The paper introduces a principled paradigm shift in trajectory forecasting by decoupling probabilistic predictive distribution training from metric-specific optimization. TraDiE policies are approved as a reusable concept for navigating conflicting benchmark objectives in robotics. The open question regarding temporal continuity is approved as it addresses a fundamental trade-off between statistical performance (e.g., NLL) and real-world utility (e.g., trajectory smoothness) for autonomous planning systems.

### Approved Concepts
- Trajectory Distribution Evaluation (TraDiE) Policies: Decouples predictive modeling from specific benchmark metrics, enabling a unified probabilistic model to optimize multiple metrics as a downstream task.

### Approved Open Questions
- Temporal continuity in probabilistic forecasting: Addressing temporal continuity is critical for transitioning from purely evaluative forecasting metrics to downstream autonomous planning systems, where jittery or discontinuous trajectories are unsafe.

## Links

- [Abstract](https://arxiv.org/abs/2607.01133)
- [PDF](https://arxiv.org/pdf/2607.01133)

