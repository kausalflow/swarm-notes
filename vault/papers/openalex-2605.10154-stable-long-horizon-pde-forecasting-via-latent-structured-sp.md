---
# CSL-compatible fields
title: "Stable Long-Horizon PDE Forecasting via Latent Structured Spectral Propagators"
author:
  - literal: "Xiaoxiao Lu"
  - literal: "Ye Yuan"
  - literal: "Jiahao Shi"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10154"

# Custom fields
paper_id: "2605.10154"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "neural-operator"
  - "representation-learning"
  - "physics-informed-machine-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "structured-spectral-propagator-ssp"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:38:18Z"
created_at: "2026-05-14T07:38:18Z"
---

# Stable Long-Horizon PDE Forecasting via Latent Structured Spectral Propagators

**Authors**: Xiaoxiao Lu, Ye Yuan, Jiahao Shi
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10154](https://arxiv.org/abs/2605.10154)

## Summary

This paper addresses the instability and error accumulation inherent in autoregressive neural operator rollouts for PDE forecasting. The authors propose a Structured Spectral Propagator (SSP) that maps physical states into a latent propagation-oriented space, evolving retained spectral modes via a frequency-conditioned linear backbone. By decoupling spatial reconstruction from spectral dynamics, the framework maintains physical coherence over long horizons, outperforming existing neural operator baselines in both error reduction and temporal stability.

## Key Contributions

- Introduced Structured Spectral Propagator (SSP), a framework that reformulates PDE forecasting by separating spatial mapping, propagation in a latent state, and synthesis.
- Decoupled reconstruction fidelity from rollout regularity to mitigate error accumulation and dynamic drift during autoregressive extrapolation.
- Achieved up to 48.9% reduction in relative L2 error compared to state-of-the-art neural operator baselines on PDE benchmarks.

## Open Questions & Future Work

- [[long-horizon-pde-extrapolation-stability]]

## Key Concepts

- [[structured-spectral-propagator-ssp]]: A neural forecasting framework that models physical evolution by separating spatial representation from frequency-conditioned spectral propagation.

## Archivist Review

The paper proposes a robust approach to mitigating autoregressive drift in PDE forecasting by decoupling spatial representation from spectral dynamics. The concept of a Structured Spectral Propagator captures this architectural strategy, and the identified open question addresses the fundamental bottleneck of maintaining physical manifold consistency during long-horizon extrapolation. Both items are well-aligned with the goal of tracking reusable mechanisms in scientific machine learning.

### Approved Concepts
- Structured Spectral Propagator (SSP): This framework explicitly decouples spatial reconstruction from temporal propagation in latent space, which is a powerful inductive bias for physical forecasting tasks.

### Approved Open Questions
- Long-Horizon PDE Extrapolation Stability: The ability to perform reliable, long-horizon extrapolation is essential for moving beyond short-term mimicry to actionable physical forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2605.10154)
- [PDF](https://arxiv.org/pdf/2605.10154)

