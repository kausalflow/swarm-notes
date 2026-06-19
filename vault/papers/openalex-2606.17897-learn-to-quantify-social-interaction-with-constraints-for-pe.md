---
# CSL-compatible fields
title: "Learn to Quantify Social Interaction with Constraints for Pedestrian Walking"
author:
  - literal: "Xiaodan Shi"
issued:
  date-parts:
    - [2026, 6, 16]
url: "https://arxiv.org/abs/2606.17897"

# Custom fields
paper_id: "2606.17897"
paper_source: "openalex"
domain: "nlp,computer-vision,robotics"
tags:
  - "trajectory-prediction"
  - "human-path-forecasting"
  - "pedestrian-prediction"
  - "multi-agent"
  - "autonomous-agent"
  - "interpretability"
  - "generative-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "learn-to-cluster"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-19T09:25:45Z"
created_at: "2026-06-19T09:25:45Z"
---

# Learn to Quantify Social Interaction with Constraints for Pedestrian Walking

**Authors**: Xiaodan Shi
**Date**: 2026-06-16
**Paper ID**: [openalex:2606.17897](https://arxiv.org/abs/2606.17897)

## Summary

This paper addresses the limitations of current trajectory prediction models in capturing explicit social interaction dynamics. The author proposes 'Learn to Cluster', a label-free, probabilistic latent variable generative model that identifies and quantifies pedestrian interaction patterns directly from sequential observations. These learned latent representations act as interpretable 'labels' that inform the prediction process, leading to more robust path forecasting for autonomous agents in crowded environments.

## Key Contributions

- Introduces 'Learn to Cluster', a probabilistic latent variable generative framework that autonomously quantifies and identifies social interaction patterns from raw trajectory data without manual labeling.
- Integrates learned latent interaction variables directly into the trajectory prediction training loop to enhance the interpretability and robustness of pedestrian path forecasting.
- Demonstrates improved forecasting performance and pattern interpretability across standard trajectory prediction benchmarks.

## Open Questions & Future Work

- [[optimal-social-interaction-clustering-granularity]]

## Key Concepts

- [[learn-to-cluster]]: A label-free, probabilistic latent variable generative framework for identifying and quantifying social interaction patterns from sequential trajectory data.

## Archivist Review

The paper proposes a label-free generative framework, Learn to Cluster, to bridge the gap between implicit social interaction modeling and interpretable representation in trajectory forecasting. I approved the concept for its potential to provide a structured way to handle multi-agent dynamics and the open question for highlighting the unresolved challenge of choosing an appropriate granularity for interaction modes in social robotics. Other candidates were not submitted.

### Approved Concepts
- Learn to Cluster: Provides a label-free, probabilistic latent variable generative approach to identify and quantify complex, unlabelled social interactions from sequential trajectory data.

### Approved Open Questions
- Optimal social interaction clustering granularity: Understanding whether a fixed number of interaction modes is sufficient or if a hierarchical/adaptive approach is necessary is critical for the scalability and robustness of social navigation systems in diverse environments.

## Links

- [Abstract](https://arxiv.org/abs/2606.17897)
- [PDF](https://arxiv.org/pdf/2606.17897)

