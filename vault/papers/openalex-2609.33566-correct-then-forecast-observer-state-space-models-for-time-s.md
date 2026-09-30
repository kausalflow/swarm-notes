---
# CSL-compatible fields
title: "Correct then Forecast: Observer State-Space Models for Time Series Forecasting"
author:
  - literal: "Alexis-Raja Brachet"
  - literal: "Guillaume Clavier--Frémond"
  - literal: "A. Ziani"
  - literal: "Pierre-Yves Richard"
  - literal: "Céline Hudelot"
issued:
  date-parts:
    - [2026, 9, 27]
url: "https://arxiv.org/abs/2609.33566"

# Custom fields
paper_id: "2609.33566"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "state-space-model"
  - "ssm"
  - "recurrent-neural-network"
  - "benchmark"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "observer-state-space-models"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:48:13Z"
created_at: "2026-09-30T10:48:13Z"
---

# Correct then Forecast: Observer State-Space Models for Time Series Forecasting

**Authors**: Alexis-Raja Brachet, Guillaume Clavier--Frémond, A. Ziani, Pierre-Yves Richard, Céline Hudelot
**Date**: 2026-09-27
**Paper ID**: [openalex:2609.33566](https://arxiv.org/abs/2609.33566)

## Summary

The paper introduces Observer State-Space Models (OSSMs), a new class of recurrent time series forecasting models rooted in control theory. Unlike standard recurrent models where observations directly control latent dynamics—causing a regime change at prediction time—OSSMs treat observations as measurements of an underlying autonomous dynamical system. By explicitly separating latent-state propagation from measurement assimilation, OSSMs ensure seamless transitions between context and forecasting intervals. Experiments across multiple benchmarks demonstrate substantial performance improvements over corresponding SSM baselines without increasing parameter counts or altering training setups.

## Key Contributions

- Introduces Observer State-Space Models (OSSMs) which separate latent-state propagation from measurement assimilation for time series forecasting.
- Establishes theoretical control-theoretic properties for OSSMs, including observability and convergence of state estimation error.
- Demonstrates that conventional and recent SSMs can be recovered as specific instances of the OSSM framework, revealing underlying modeling inconsistencies.
- Achieves substantial empirical improvements across multiple benchmarks while maintaining identical parameter counts and training setups as SSM baselines.

## Limitations

None explicitly mentioned in the abstract.

## Open Questions & Future Work

- [[decoupled-observer-spacetime-formulation]]

## Key Concepts

- [[observer-state-space-models]]: A class of recurrent time series forecasting models that treats observations as measurements of an autonomous dynamical system rather than direct drivers of latent dynamics.

## Archivist Review

Approved the central conceptual framework of Observer State-Space Models and its core open question regarding decoupled space-time formulations. Followed strict sparsity and non-duplication rules.

### Approved Concepts
- Observer State-Space Models: Central novelty of the paper, providing a control-theoretic formulation for time series forecasting that separates state propagation from measurement assimilation.

### Approved Open Questions
- Decoupled Observer Space-Time Formulations: Extending OSSMs with decoupled innovation maps and more powerful nonlinear encoders is crucial for generalizing observer-based state-space models beyond linear or tightly coupled state-space constraints.

## Links

- [Abstract](https://arxiv.org/abs/2609.33566)
- [PDF](https://arxiv.org/pdf/2609.33566)

