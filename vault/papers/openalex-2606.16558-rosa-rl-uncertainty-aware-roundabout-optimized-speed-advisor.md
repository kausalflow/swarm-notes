---
# CSL-compatible fields
title: "ROSA-RL: Uncertainty-Aware Roundabout Optimized Speed Advisory with Reinforcement Learning"
author:
  - literal: "Anna-Lena Schlamp"
  - literal: "Jeremias Gerner"
  - literal: "Klaus Bogenberger"
  - literal: "Werner Huber"
  - literal: "Stefanie Schmidtner"
issued:
  date-parts:
    - [2026, 6, 15]
url: "https://arxiv.org/abs/2606.16558"

# Custom fields
paper_id: "2606.16558"
paper_source: "openalex"
domain: "reinforcement-learning"
tags:
  - "reinforcement-learning"
  - "transformer"
  - "multimodal"
  - "autonomous-agent"
  - "planning"
  - "uncertainty"
architectures:
  []
datasets:
  []
concept_slugs:
  - "probabilistic-conflict-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:27:21Z"
created_at: "2026-06-17T09:27:21Z"
---

# ROSA-RL: Uncertainty-Aware Roundabout Optimized Speed Advisory with Reinforcement Learning

**Authors**: Anna-Lena Schlamp, Jeremias Gerner, Klaus Bogenberger, Werner Huber, Stefanie Schmidtner
**Date**: 2026-06-15
**Paper ID**: [openalex:2606.16558](https://arxiv.org/abs/2606.16558)

## Summary

ROSA-RL addresses the challenges of roundabout navigation in mixed traffic by integrating probabilistic conflict forecasting with reinforcement learning. The system utilizes a Transformer-based model to predict conflict zone occupancy over a five-second horizon, capturing multi-agent interactions. By embedding these uncertainty-aware predictions into a reinforcement learning framework, ROSA-RL enables safer and more efficient speed coordination for automated vehicles. Simulation results confirm that the approach effectively manages non-deterministic human behavior and outperforms traditional model-based baselines.

## Key Contributions

- Introduces ROSA-RL, an uncertainty-aware speed advisory framework for roundabout navigation in mixed traffic.
- Uses a Transformer-based model to perform probabilistic conflict zone occupancy forecasting over a five-second horizon.
- Demonstrates that incorporating uncertainty in future motion and intent into the RL state improves traffic safety and efficiency in simulation environments.

## Open Questions & Future Work

- [[rl-roundabout-uncertainty-limits]]

## Key Concepts

- [[probabilistic-conflict-forecasting]]: A predictive mechanism for forecasting conflict zone occupancy over a future horizon that explicitly models uncertainty in agent motion and intent.

## Archivist Review

I approved the concept of Probabilistic Conflict Forecasting as it is a general, reusable mechanism for integrating uncertainty into downstream control or navigation policies. I rejected the name of the framework itself as it is a paper-local instantiation. The open question was approved for tracking the performance of RL agents under the specific constraints of high-uncertainty traffic navigation.

### Approved Concepts
- Probabilistic Conflict Forecasting: The paper provides a method for predicting potential collisions by outputting conflict zone occupancy rather than just deterministic trajectories, incorporating uncertainty directly into an RL state.

### Approved Open Questions
- RL-Based Roundabout Control Robustness: This question is foundational for evaluating the viability of RL for real-world deployment in mixed-traffic urban environments.

### Rejected Candidates
- [concept] ROSA-RL (`rosa-rl`) - subcomponent_of_broader_mechanism: The framework is a specific implementation of a broader uncertainty-aware RL paradigm, and the mechanism it introduces is better captured by a more general concept name.

## Links

- [Abstract](https://arxiv.org/abs/2606.16558)
- [PDF](https://arxiv.org/pdf/2606.16558)

