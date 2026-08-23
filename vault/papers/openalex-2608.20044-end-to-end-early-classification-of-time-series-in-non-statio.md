---
# CSL-compatible fields
title: "End-to-end Early Classification of Time Series in Non-Stationary Environments"
author:
  - literal: "Aurélien Renault"
  - literal: "Alexis Bondu"
  - literal: "Antoine Cornuéjols"
  - literal: "Vincent Lemaire"
issued:
  date-parts:
    - [2026, 8, 20]
url: "https://arxiv.org/abs/2608.20044"

# Custom fields
paper_id: "2608.20044"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "reinforcement-learning"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dqend"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-23T05:19:19Z"
created_at: "2026-08-23T05:19:19Z"
---

# End-to-end Early Classification of Time Series in Non-Stationary Environments

**Authors**: Aurélien Renault, Alexis Bondu, Antoine Cornuéjols, Vincent Lemaire
**Date**: 2026-08-20
**Paper ID**: [openalex:2608.20044](https://arxiv.org/abs/2608.20044)

## Summary

This paper studies Early Classification of Time Series (ECTS) in non-stationary environments, challenging the traditional assumption of stationarity and separable optimization designs. The authors introduce DQeND, a unified reinforcement learning-based architecture that jointly learns representation, classification, and triggering decisions. Systematic experiments across controlled drifting scenarios show that DQeND consistently outperforms separable baselines, highlighting the importance of joint updates for adaptation in dynamic time-series environments.

## Key Contributions

- Establishes the first systematic comparison between separable and end-to-end approaches for Early Classification of Time Series (ECTS) across controlled drifting scenarios.
- Introduces DQeND, a unified reinforcement learning architecture that jointly optimizes representation, classification, and triggering decisions under non-stationary conditions.
- Demonstrates through ablation studies that jointly updating representation and decision modules is critical for robust adaptation against environmental drift.

## Open Questions & Future Work

- [[stability-plasticity-trade-off-ects]]

## Key Concepts

- [[dqend]]: A reinforcement-learning-based unified architecture that jointly optimizes representation, classification, and triggering decisions for early time-series classification under non-stationary conditions.

## Archivist Review

Approved the core unified architecture DQeND for joint representation and decision learning in early classification under drift, and the stability-plasticity open question on streaming non-stationarity. Kept approvals strictly scarce and aligned with vault standards.

### Approved Concepts
- DQeND: It is the central methodological contribution, offering a unified reinforcement learning approach to joint early classification and decision triggering under non-stationary conditions.

### Approved Open Questions
- Stability-Plasticity Trade-off in ECTS: Understanding this trade-off is critical for preventing catastrophic forgetting while adapting to streaming distribution shifts.

## Links

- [Abstract](https://arxiv.org/abs/2608.20044)
- [PDF](https://arxiv.org/pdf/2608.20044)

