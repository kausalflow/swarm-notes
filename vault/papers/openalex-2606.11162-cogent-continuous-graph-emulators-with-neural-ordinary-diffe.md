---
# CSL-compatible fields
title: "COGENT: Continuous Graph Emulators with Neural Ordinary Differential Equations for Long-Term Physical Forecasting"
author:
  - literal: "Zesheng Liu"
  - literal: "Maryam Rahnemoonfar"
issued:
  date-parts:
    - [2026, 6, 9]
url: "https://arxiv.org/abs/2606.11162"

# Custom fields
paper_id: "2606.11162"
paper_source: "openalex"
domain: "time-series,graph-learning"
tags:
  - "time-series,forecasting,graph-neural-network,neural-ode,physics-informed,long-context,simulation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "continuous-graph-neural-ode-emulator"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-12T08:53:43Z"
created_at: "2026-06-12T08:53:43Z"
---

# COGENT: Continuous Graph Emulators with Neural Ordinary Differential Equations for Long-Term Physical Forecasting

**Authors**: Zesheng Liu, Maryam Rahnemoonfar
**Date**: 2026-06-09
**Paper ID**: [openalex:2606.11162](https://arxiv.org/abs/2606.11162)

## Summary

COGENT is a continuous graph emulator designed for long-term physical forecasting on irregular geospatial meshes by leveraging latent Neural Ordinary Differential Equations. The model encodes historical states into context vectors that condition the latent ODE, allowing for prediction queries at arbitrary future times rather than fixed steps. It overcomes traditional autoregressive instabilities in physical simulations by utilizing a residual decoder to directly map latent trajectories to future physical states. The method is validated on ice-sheet simulation datasets, showing superior long-range stability compared to standard graph-based baselines.

## Key Contributions

- Introduces COGENT, a graph-based Neural ODE framework for continuous-time forecasting on irregular geospatial meshes.
- Replaces iterative autoregressive feedback with a latent dynamical system approach for improved long-horizon prediction stability.
- Proposes a progressive rollout-horizon scheduling strategy to stabilize model training for long-term physical simulations.

## Open Questions & Future Work

- [[arbitrary-continuous-time-state-querying-fidelity]]

## Key Concepts

- [[continuous-graph-neural-ode-emulator]]: A framework for continuous-time physical simulation on irregular meshes that represents trajectories as latent dynamical systems initialized by graph-encoded states.

## Archivist Review

I have approved the core architecture (Continuous Graph Neural ODE Emulator) as it represents a significant, reusable paradigm for physical forecasting on irregular meshes. I have also approved a refined version of the open question regarding the practical validation of continuous-time querying. Other candidates were either subcomponents of the training process or not sufficiently standardized for long-term vault retention.

### Approved Concepts
- Continuous Graph Neural ODE Emulator: Combines graph-structured spatial representation with Neural ODEs to enable continuous-time physical forecasting, mitigating error accumulation found in autoregressive graph models.

### Approved Open Questions
- Arbitrary Continuous-Time Query Fidelity: This addresses the core claim of continuous-time emulation, which remains theoretically supported by the model design but practically unverified in existing benchmarks.

### Rejected Candidates
- [concept] Progressive Rollout-Horizon Scheduling (`progressive-rollout-horizon-scheduling`) - subcomponent_of_broader_mechanism: This is a training-time heuristic/technique rather than a central model architecture or representation concept.
- [dataset] Ice-sheet and Sea-level System Model Dataset (`ice-sheet-and-sea-level-system-model-dataset`) - low_impact: The ISSM is a simulation software/framework used to generate data, and this dataset instance is not a reusable standardized benchmark in the time-series literature.

## Links

- [Abstract](https://arxiv.org/abs/2606.11162)
- [PDF](https://arxiv.org/pdf/2606.11162)

