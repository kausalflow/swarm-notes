---
# CSL-compatible fields
title: "Scalable Lindblad Noise Learning via Stochastic Tensor-Network Simulation"
author:
  - literal: "Alejandro R. Ramos Ramos"
  - literal: "Maximilian Fröhlich"
  - literal: "Aaron Sander"
  - literal: "Robert Wille"
  - literal: "Martin Eigel"
  - literal: "Patrick Gelß"
  - literal: "Sebastian Pokutta"
issued:
  date-parts:
    - [2026, 8, 25]
url: "https://arxiv.org/abs/2608.24668"

# Custom fields
paper_id: "2608.24668"
paper_source: "openalex"
domain: "physics"
tags:
  - "reinforcement-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T17:01:12Z"
created_at: "2026-08-28T17:01:12Z"
---

# Scalable Lindblad Noise Learning via Stochastic Tensor-Network Simulation

**Authors**: Alejandro R. Ramos Ramos, Maximilian Fröhlich, Aaron Sander, Robert Wille, Martin Eigel, Patrick Gelß, Sebastian Pokutta
**Date**: 2026-08-25
**Paper ID**: [openalex:2608.24668](https://arxiv.org/abs/2608.24668)

## Summary

Learning dissipation rates in large-scale open quantum systems is challenging due to the high computational complexity of repeatedly solving the Lindblad equation. This paper introduces a scalable noise-learning framework that couples the Tensor Jump Method (TJM) with gradient-free least-squares optimization over time series of local observables. The authors demonstrate successful noise characterization up to 160 sites in an Ising model and establish rigorous theoretical guarantees regarding estimation error variance, purity evolution, and favorable system-size scaling.

## Key Contributions

- Proposed a scalable noise-learning framework for Lindblad dissipation rates combining the Tensor Jump Method (TJM) with gradient-free optimization of a least-squares cost function on local-observable expectation values.
- Demonstrated scalable noise learning up to 160 sites for a homogeneous Ising noise model and 16 sites for a site-resolved model.
- Provided exact theoretical guarantees on TJM estimation error via Frobenius variance, purity monotonicity, and system-size scaling properties of the cost function variance.

## Archivist Review

The submitted paper focuses on quantum physics (Lindblad noise learning via tensor networks) rather than core machine learning time-series forecasting, forecasting horizons, or temporal models covered by the knowledge vault. Therefore, the open question is rejected for low domain relevance.

### Rejected Candidates
- [open_question] Gradient-Assisted Lindbladian Optimization (`gradient-assisted-lindbladian-optimization`) - low_impact: The paper focuses on physics-based quantum noise learning rather than time series forecasting or machine learning methodologies, making this open question outside the core scope of the vault.

## Links

- [Abstract](https://arxiv.org/abs/2608.24668)
- [PDF](https://arxiv.org/pdf/2608.24668)

