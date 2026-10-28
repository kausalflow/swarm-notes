---
# CSL-compatible fields
title: "Learning control policies from heterogeneous multi-horizon time series in battery energy management systems"
author:
  - literal: "Sheng Yin"
  - literal: "Vivek Teja Tanjavooru"
  - literal: "Christoph Goebel"
  - literal: "Holger Christian Hesse"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2609.22546"

# Custom fields
paper_id: "2609.22546"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "reinforcement-learning"
  - "imitation-learning"
  - "forecasting"
  - "optimization"
  - "representation-learning"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "representation-to-decision"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-28T10:53:17Z"
created_at: "2026-10-28T10:53:17Z"
---

# Learning control policies from heterogeneous multi-horizon time series in battery energy management systems

**Authors**: Sheng Yin, Vivek Teja Tanjavooru, Christoph Goebel, Holger Christian Hesse
**Date**: 2026-10-26
**Paper ID**: [openalex:2609.22546](https://arxiv.org/abs/2609.22546)

## Summary

This paper introduces Representation-to-Decision (R2D), an end-to-end imitation learning framework that maps heterogeneous multi-horizon time-series inputs directly to battery control decisions using modular temporal feature extractors and behavior cloning from an aging-aware MILP expert. R2D bypasses traditional prediction-then-optimization pipelines and outperforms conventional MPC and reinforcement learning benchmarks across five industrial sites while matching the battery degradation rate of its expert teacher. Extensive ablations and out-of-distribution tests identify robust architectural configurations and highlight the profile-dependency of cross-site transferability.

## Key Contributions

- Introduces Representation-to-Decision (R2D), an end-to-end imitation learning framework that maps heterogeneous multi-horizon time-series inputs directly to battery control decisions without explicit intermediate forecasting steps.
- Achieves 62-77% of the global clairvoyant optimum, outperforming standard Model Predictive Control (MPC) and reinforcement learning benchmarks across five industrial sites on a high-fidelity electro-thermal battery simulation.
- Demonstrates near-identical battery degradation to an aging-aware Mixed-Integer Linear Programming (MILP) expert teacher through behavior cloning.
- Identifies via comprehensive ablation studies that an LSTM encoder with a 15-minute single-step control horizon provides the most robust and deployment-ready configuration.

## Open Questions & Future Work

- [[online-constraint-handling-imitation-learning-bems]]

## Key Concepts

- [[representation-to-decision]]: An end-to-end imitation learning framework that maps heterogeneous multi-horizon time-series inputs directly to battery control decisions through modular Temporal Feature Extractors and a shared latent representation.

## Archivist Review

Approved the core Representation-to-Decision framework as a distinct and reusable paradigm bridging time-series representation and decision-making, along with its associated open question on online constraint handling. Subcomponents like temporal feature extractors were correctly filtered out to preserve vault cleanliness.

### Approved Concepts
- Representation-to-Decision: Introduces an end-to-end imitation learning framework that replaces traditional prediction-then-optimization pipelines with direct decision-making from heterogeneous multi-horizon time series.

### Approved Open Questions
- Online Constraint Handling in BEMS: Crucial for deploying deep learning and imitation learning policies safely in real-world industrial energy storage environments where hard operational constraints must never be violated.

### Rejected Candidates
- [concept] Temporal Feature Extractors (`temporal-feature-extractors`) - subcomponent_of_broader_mechanism: Subcomponent of a broader mechanism (Representation-to-Decision framework) rather than an independent foundational paradigm.

## Links

- [Abstract](https://arxiv.org/abs/2609.22546)
- [PDF](https://arxiv.org/pdf/2609.22546)

