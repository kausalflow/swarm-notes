---
# CSL-compatible fields
title: "Digital Twins of Networked Dynamical Systems: Machine Learning Prediction of Synchronization Transitions in Coupled Chaotic Oscillators"
author:
  - literal: "Huawei Fan"
  - literal: "Yao Du"
  - literal: "Meng-Xia Bi"
  - literal: "Yafeng Wang"
  - literal: "Xingang Wang"
issued:
  date-parts:
    - [2026, 10, 22]
url: "https://arxiv.org/abs/2610.30632"

# Custom fields
paper_id: "2610.30632"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "reservoir"
  - "dynamical-systems"
architectures:
  - "mamba"
datasets:
  []
concept_slugs:
  - "coupled-reservoir-computing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-25T09:30:15Z"
created_at: "2026-10-25T09:30:15Z"
---

# Digital Twins of Networked Dynamical Systems: Machine Learning Prediction of Synchronization Transitions in Coupled Chaotic Oscillators

**Authors**: Huawei Fan, Yao Du, Meng-Xia Bi, Yafeng Wang, Xingang Wang
**Date**: 2026-10-22
**Paper ID**: [openalex:2610.30632](https://arxiv.org/abs/2610.30632)

## Summary

This paper proposes a model-free coupled reservoir computing (CRC) architecture for constructing digital twins of networked dynamical systems by modularly decomposing nodal dynamics, coupling functions, and networks. Trained solely on time series of isolated and paired oscillators, the CRC accurately reproduces collective states and synchronization transitions under varying coupling strengths. Furthermore, the trained modules can be effectively reused across different complex networks and non-identical oscillators.

## Key Contributions

- Proposes a model-free coupled reservoir computing (CRC) architecture that decomposes digital twins into modular nodal dynamics, coupling functions, and coupling networks.
- Demonstrates that CRC reproduces complex collective states including complete synchronization, phase synchronization, and chimera states.
- Shows that trained modules can be reused across different complex networks and non-identical oscillators after training only on isolated oscillators and coupled pairs.

## Open Questions & Future Work

- [[predicting-large-scale-synchronization-transitions]]

## Key Concepts

- [[coupled-reservoir-computing]]: A model-free reservoir computing architecture that decomposes coupled dynamical systems into modular nodal dynamics, coupling functions, and network structures.

## Archivist Review

Approved the core 'coupled-reservoir-computing' concept since it introduces a novel modular approach to dynamical system modeling and digital twins. Also approved the open question regarding large-scale synchronization transitions. No datasets met the naming and citation criteria for standalone vault notes.

### Approved Concepts
- Coupled Reservoir Computing: Central architectural contribution enabling modular decomposition and reassembly of nodal dynamics, coupling functions, and networks for chaotic oscillator systems.

### Approved Open Questions
- Predicting Large-Scale Synchronization Transitions: Understanding how to scale data-driven predictions to large-scale collective phenomena is essential for building reliable digital twins of complex networked systems.

## Links

- [Abstract](https://arxiv.org/abs/2610.30632)
- [PDF](https://arxiv.org/pdf/2610.30632)

