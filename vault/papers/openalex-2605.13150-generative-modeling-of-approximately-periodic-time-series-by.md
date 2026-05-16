---
# CSL-compatible fields
title: "Generative Modeling of Approximately Periodic Time Series by a Posterior-Weighted Gaussian Process"
author:
  - literal: "Elias Reich"
  - literal: "Saverio Messineo"
  - literal: "S. Huber"
issued:
  date-parts:
    - [2026, 5, 13]
url: "https://arxiv.org/abs/2605.13150"

# Custom fields
paper_id: "2605.13150"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "posterior-weighted-gaussian-process"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-16T07:09:26Z"
created_at: "2026-05-16T07:09:26Z"
---

# Generative Modeling of Approximately Periodic Time Series by a Posterior-Weighted Gaussian Process

**Authors**: Elias Reich, Saverio Messineo, S. Huber
**Date**: 2026-05-13
**Paper ID**: [openalex:2605.13150](https://arxiv.org/abs/2605.13150)

## Summary

This paper introduces a generative Gaussian Process-based framework for modeling approximately periodic time series common in industrial and cyber-physical systems. Traditional models struggle to balance rigid periodicity with the need for intra-repetition variability, a limitation the authors address through a two-stage construction using a novel posterior-modulated kernel. The approach successfully decouples repetitive structural regularity from cycle-to-cycle variation, allowing for the generation of synthetic trajectories that maintain consistent mean behaviors while varying in fine-scale dynamics.

## Key Contributions

- Proposes a stochastic generative model for approximately periodic time series that balances structural regularity with inter-repetition stochasticity.
- Introduces a posterior-modulated Gaussian Process kernel that decouples intra-repetition trajectories from inter-repetition variability.
- Enables flexible generation of realistic synthetic trajectories by maintaining a shared mean function while allowing smooth variations in duration, amplitude, and dynamics across cycles.

## Open Questions & Future Work

- [[scalable-inference-for-posterior-modulated-gp-kernels]]

## Key Concepts

- [[posterior-weighted-gaussian-process]]: A Gaussian process modeling framework that modulates the posterior via a kernel to decouple structural regularities from cycle-to-cycle stochasticity.

## Archivist Review

I have approved the core methodological concept of the Posterior-Weighted Gaussian Process, as it provides a distinct way to model approximately periodic series by separating structure from variability. I have also approved the identified open question regarding scalable inference, as it addresses a fundamental computational bottleneck common to GP-based models in this domain. All other candidates were rejected as they were either too narrow or generic.

### Approved Concepts
- Posterior-Weighted Gaussian Process: It addresses the tension between rigid periodicity and intra-repetition variability in time series modeling by decoupling structure from variation.

### Approved Open Questions
- Scalable inference for posterior-modulated kernels: Scalability is a critical requirement for deploying generative models in industrial systems where the number of process repetitions is large, making the computational efficiency of these models a significant bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2605.13150)
- [PDF](https://arxiv.org/pdf/2605.13150)

