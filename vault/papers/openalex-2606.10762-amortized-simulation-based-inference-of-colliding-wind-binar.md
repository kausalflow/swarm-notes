---
# CSL-compatible fields
title: "Amortized Simulation-Based Inference of Colliding-Wind Binaries from Short, Noisy Image Time Series"
author:
  - literal: "Niklas Knöll"
  - literal: "Tobias Buck"
  - literal: "Lorenzo Branca"
  - literal: "Giuseppe Viterbo"
issued:
  date-parts:
    - [2026, 6, 9]
url: "https://arxiv.org/abs/2606.10762"

# Custom fields
paper_id: "2606.10762"
paper_source: "openalex"
domain: "physics"
tags:
  - "multimodal"
  - "time-series"
  - "embedding"
architectures:
  []
datasets:
  []
concept_slugs:
  - "factorized-spatio-temporal-architecture-for-amortized-posterior-inference"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-12T08:53:24Z"
created_at: "2026-06-12T08:53:24Z"
---

# Amortized Simulation-Based Inference of Colliding-Wind Binaries from Short, Noisy Image Time Series

**Authors**: Niklas Knöll, Tobias Buck, Lorenzo Branca, Giuseppe Viterbo
**Date**: 2026-06-09
**Paper ID**: [openalex:2606.10762](https://arxiv.org/abs/2606.10762)

## Summary

The authors present an amortized simulation-based inference (SBI) pipeline for recovering physical parameters of colliding-wind binaries from noisy image time series. By using a factorized spatio-temporal architecture, the model separates spatial feature extraction from global dynamical evolution, achieving time-translation equivariance and improved identifiability in low-signal regimes. The pipeline is coupled with a neural spline flow, enabling the joint inference of mass-loss rates and orbital elements while providing well-calibrated posterior estimates.

## Key Contributions

- Introduces a factorized spatio-temporal architecture for SBI that separates spatial encoding and temporal aggregation, improving identifiability for noisy astrophysical time series.
- Develops a full amortized pipeline using neural spline flows to infer seven physical parameters of colliding-wind binaries from Hα photon-count sequences.
- Demonstrates robust parameter recovery under realistic noise conditions and validates posterior calibration using TARP and SBC diagnostic techniques.

## Open Questions & Future Work

- [[simulator-observation-gap-sbi]]

## Key Concepts

- [[factorized-spatio-temporal-architecture-for-amortized-posterior-inference]]: A neural architecture that decouples spatial feature extraction from temporal evolution to improve parameter identifiability and time-translation equivariance in inverse problems.

## Archivist Review

I have approved the factorized spatio-temporal architecture concept as it provides a clear, reusable pattern for inverse problems involving dynamic image sequences. The simulator-observation gap open question was approved for its importance in moving beyond synthetic benchmarks. I rejected the inference of turbulent parameters as a specific open question because it represents a technical limitation of the current architecture rather than a broader unresolved challenge in the field.

### Approved Concepts
- Factorized Spatio-Temporal Architecture for Amortized Posterior Inference: This architecture is central to the paper's novelty, enabling tractable inference for computationally expensive astrophysical forward models by separating spatial and temporal dynamics.

### Approved Open Questions
- Bridging Simulation-Observation Gap: Bridging the gap between synthetic simulation-based training and real-world astronomical data is the primary barrier to the practical application of SBI in observational astrophysics.

## Links

- [Abstract](https://arxiv.org/abs/2606.10762)
- [PDF](https://arxiv.org/pdf/2606.10762)

