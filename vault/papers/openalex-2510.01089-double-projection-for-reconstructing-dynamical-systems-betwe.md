---
# CSL-compatible fields
title: "Double projection for reconstructing dynamical systems: between stochastic and deterministic regimes"
author:
  - literal: "Viktor Šíp"
  - literal: "Martin Breyton"
  - literal: "Spase Petkoski"
  - literal: "Viktor Jirsa"
issued:
  date-parts:
    - [2026, 7, 27]
url: "https://arxiv.org/abs/2510.01089"

# Custom fields
paper_id: "2510.01089"
paper_source: "openalex"
domain: "time-series"
tags:
  - "variational-autoencoder"
  - "vae"
  - "time-series"
  - "forecasting"
  - "stochastic-process"
  - "dynamical-systems"
architectures:
  []
datasets:
  []
concept_slugs:
  - "double-projection"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-30T07:26:59Z"
created_at: "2026-07-30T07:26:59Z"
---

# Double projection for reconstructing dynamical systems: between stochastic and deterministic regimes

**Authors**: Viktor Šíp, Martin Breyton, Spase Petkoski, Viktor Jirsa
**Date**: 2026-07-27
**Paper ID**: [openalex:2510.01089](https://arxiv.org/abs/2510.01089)

## Summary

This paper introduces the double projection method within dynamical variational autoencoders to learn stochastic models of dynamical systems by jointly estimating state trajectories and noise time series. Evaluated on six benchmark problems, the method enables multi-step evolution and low-dimensional state spaces. The authors analyze how teacher forcing intervals transition model behavior between deterministic and stochastic regimes, and clarify how inferred noise acts either as genuine stochasticity or compensation for unmodeled dynamics.

## Key Contributions

- Proposes the double projection method within dynamical variational autoencoders to jointly estimate system state trajectories and noise time series from data.
- Enables multi-step system evolution and learning models with low-dimensional state spaces.
- Demonstrates across six benchmark problems that shorter teacher forcing intervals favor deterministic dynamics while longer intervals rely more on stochastic forcing.

## Open Questions & Future Work

- [[optimal-teacher-forcing-strategy-stochastic-dynamics-reconstruction]]

## Key Concepts

- [[double-projection]]: A method within dynamical variational autoencoders that estimates both system state trajectories and noise time series from data to reconstruct dynamical systems.

## Archivist Review

Approved the central methodological concept 'double projection' for joint state and noise estimation in dynamical variational autoencoders, along with the open question regarding optimal teacher forcing strategies in stochastic regimes. Rejected paper-local hyperparameter evaluations.

### Approved Concepts
- Double Projection: Introduces a novel framework within dynamical variational autoencoders that jointly estimates system state trajectories and noise time series to reconstruct dynamical systems.

### Approved Open Questions
- Optimal Teacher Forcing Strategy: Setting the teacher forcing interval is critical for balancing stability and accurate long-term dynamics in recurrent and latent variable models, directly impacting training efficiency and model generalization.

### Rejected Candidates
- [concept] Teacher Forcing Interval Analysis (`teacher-forcing-interval-analysis`) - paper_local: Teacher forcing is a well-known training technique; analyzing its interval length in dynamical models is a paper-local investigation rather than a reusable standalone architectural mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2510.01089)
- [PDF](https://arxiv.org/pdf/2510.01089)

