---
# CSL-compatible fields
title: "DynoSLAM: Dynamic SLAM with Generative Graph Neural Networks for Real-World Social Navigation"
author:
  - literal: "Danil Tokhchukov"
  - literal: "Veronika Morozova"
  - literal: "Gonzalo Ferrer"
issued:
  date-parts:
    - [2026, 5, 4]
url: "https://arxiv.org/abs/2605.02759"

# Custom fields
paper_id: "2605.02759"
paper_source: "openalex"
domain: "robotics"
tags:
  - "robotics"
  - "graph-neural-network"
  - "gnn"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dynamic-mahalanobis-distance-factor"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-07T07:38:25Z"
created_at: "2026-05-07T07:38:25Z"
---

# DynoSLAM: Dynamic SLAM with Generative Graph Neural Networks for Real-World Social Navigation

**Authors**: Danil Tokhchukov, Veronika Morozova, Gonzalo Ferrer
**Date**: 2026-05-04
**Paper ID**: [openalex:2605.02759](https://arxiv.org/abs/2605.02759)

## Summary

DynoSLAM is a tightly-coupled dynamic SLAM architecture designed for navigation in crowded environments populated by pedestrians. It replaces rigid motion heuristics with a stochastic GNN-based World Model that performs Monte Carlo rollouts to capture the multimodal uncertainty of human interactions. This probabilistic information is integrated directly into the SLAM factor graph via a dynamic Mahalanobis distance factor, allowing for more robust localization and generating safety envelopes for downstream navigation planners.

## Key Contributions

- Introduces DynoSLAM, a dynamic SLAM framework that tightly couples socially-aware GNN motion forecasting into factor graph optimization.
- Formulates human motion prediction as a stochastic World Model, utilizing Monte Carlo rollouts to represent multimodal epistemic uncertainty.
- Demonstrates that integrating probabilistic motion constraints via a dynamic Mahalanobis distance factor prevents optimization failures inherent to deterministic motion models.

## Open Questions & Future Work

- [[flow-matching-stochastic-motion-prediction]]

## Key Concepts

- [[dynamic-mahalanobis-distance-factor]]: A factor graph constraint that incorporates probabilistic, multimodal motion predictions as a Mahalanobis distance to handle dynamic entities in SLAM.

## Archivist Review

The proposed concept represents a novel integration of probabilistic dynamics into SLAM factor graphs, while the open question identifies a shift from sampling-based stochasticity to generative density estimation, both of which are highly relevant for robotics and time-series forecasting. I rejected no candidates because only one concept and one open question were provided, and both met the criteria for novelty and long-term reusability in the vault.

### Approved Concepts
- Dynamic Mahalanobis Distance Factor: It enables the integration of stochastic, multimodal pedestrian trajectory forecasts into traditional factor graph optimization for SLAM.

### Approved Open Questions
- Flow Matching for Stochastic Prediction: This addresses the limitation of using heuristic-based sampling for uncertainty estimation in human motion prediction, which is critical for accurate safety-critical planning.

## Links

- [Abstract](https://arxiv.org/abs/2605.02759)
- [PDF](https://arxiv.org/pdf/2605.02759)

