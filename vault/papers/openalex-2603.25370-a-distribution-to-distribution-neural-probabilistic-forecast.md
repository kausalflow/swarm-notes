---
# CSL-compatible fields
title: "A Distribution-to-Distribution Neural Probabilistic Forecasting Framework for Dynamical Systems"
author:
  - literal: "Tianlin Yang"
  - literal: "Hailiang Du"
  - literal: "Louis J. M. Aslett"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25370"

# Custom fields
paper_id: "2603.25370"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "reinforcement-learning"
  - "distribution-to-distribution-forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "distribution-to-distribution-neural-forecasting"
  - "kernel-mean-embedding-for-distributional-input"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:06:59Z"
created_at: "2026-03-29T06:06:59Z"
---

# A Distribution-to-Distribution Neural Probabilistic Forecasting Framework for Dynamical Systems

**Authors**: Tianlin Yang, Hailiang Du, Louis J. M. Aslett
**Date**: 2026-03-26
**Paper ID**: [openalex:2603.25370](https://arxiv.org/abs/2603.25370)

## Summary

This paper introduces a Distribution-to-Distribution (D2D) neural probabilistic forecasting framework designed to model the evolution of probability distributions directly, contrasting with traditional methods that rely on ensembles or sampling. The architecture utilizes Kernel Mean Embeddings to encode the input distribution state and employs Mixture Density Networks for parameterizing the output predictive distributions, enabling recursive uncertainty propagation end-to-end. Evaluated on the Lorenz63 chaotic system, the D2D model successfully captures complex distributional dynamics and produces skillful forecasts competitive with perfect model benchmarks. This work posits a novel paradigm shift where probabilistic forecasts are treated as evolving dynamical objects rather than reconstructed from deterministic trajectories.

## Key Contributions

- Developed a Distribution-to-Distribution (D2D) neural probabilistic forecasting framework that operates directly on probability distributions as dynamical objects.
- Introduced a framework design incorporating distributional encoding via Kernel Mean Embeddings and distributional decoding via Mixture Density Networks around a replaceable forecasting module.
- Demonstrated the ability to capture nontrivial distributional evolution for the Lorenz63 chaotic system without explicit ensemble simulation.
- Showed that the D2D model achieves competitive probabilistic forecast skill, suggesting a new paradigm for uncertainty quantification in dynamical systems.

## Limitations

The current demonstration is primarily on a simplified chaotic system (Lorenz63), and scalability or performance on high-dimensional real-world time series is not yet shown.

## Open Questions & Future Work

- [[high-dimensional-joint-distribution-forecasting]]

## Key Concepts

- [[distribution-to-distribution-neural-forecasting]]: A neural framework that learns and recursively propagates predictive probability distributions directly, rather than sampling ensembles.
- [[kernel-mean-embedding-for-distributional-input]]: The use of Kernel Mean Embeddings (KMEs) to represent the input probability distribution in the D2D framework.

## Archivist Review

The core contribution, Distribution-to-Distribution (D2D) Neural Forecasting, is approved as a novel and reusable architectural paradigm for uncertainty quantification. The specific input encoding method using Kernel Mean Embeddings is also approved for its technical reusability. The open question regarding scaling this approach to the full joint distribution in high-dimensional systems is significant enough to warrant tracking. The one proposed dataset, Lorenz63, is rejected as it is a standard toy model and not a general-purpose dataset.

### Approved Concepts
- Distribution-to-Distribution Neural Forecasting: This is the core novel paradigm proposed by the paper, shifting forecasting from trajectory-based to distribution-based evolution.
- Kernel Mean Embedding for Distributional Input: It provides the specific mechanism for encoding the necessary probabilistic input state into the neural network module.

### Approved Open Questions
- Joint Distributional Evolution: Modeling the evolution of the full joint probability distribution is crucial for accurately capturing inter-variable dependencies and higher-order uncertainty structures in complex dynamical systems.

### Rejected Candidates
- [concept] distribution-to-distribution-forecasting (`distribution-to-distribution-forecasting`) - duplicate_existing: This is too generic and is essentially captured by the more specific and approved concept 'distribution-to-distribution-neural-forecasting'.
- [dataset] Lorenz63 (`lorenz63`) - low_impact: Lorenz63 is a canonical toy system used to demonstrate chaotic behavior, not a complex, reusable benchmark dataset requiring its own note.

## Links

- [Abstract](https://arxiv.org/abs/2603.25370)
- [PDF](https://arxiv.org/pdf/2603.25370)

