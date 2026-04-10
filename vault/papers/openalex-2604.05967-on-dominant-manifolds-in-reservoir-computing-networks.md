---
# CSL-compatible fields
title: "On Dominant Manifolds in Reservoir Computing Networks"
author:
  - literal: "Noa Kaplan"
  - literal: "Alberto Padoan"
  - literal: "Anastasia Bizyaeva"
issued:
  date-parts:
    - [2026, 4, 7]
url: "https://arxiv.org/abs/2604.05967"

# Custom fields
paper_id: "2604.05967"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "recurrent-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dominant-manifolds-in-reservoir-computing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-10T06:26:24Z"
created_at: "2026-04-10T06:26:24Z"
---

# On Dominant Manifolds in Reservoir Computing Networks

**Authors**: Noa Kaplan, Alberto Padoan, Anastasia Bizyaeva
**Date**: 2026-04-07
**Paper ID**: [openalex:2604.05967](https://arxiv.org/abs/2604.05967)

## Summary

This paper provides a theoretical analysis of how Reservoir Computing (RC) networks learn to represent time-series data through the emergence of low-dimensional dominant manifolds. By focusing on simplified linear, continuous-time reservoir models, the authors demonstrate that the trained reservoir modes effectively approximate the Koopman eigenfunctions of the underlying dynamical system. This approach creates an explicit connection between reservoir training and Dynamic Mode Decomposition (DMD). The study further explores the geometric evolution of these manifolds during training and suggests extensions to nonlinear networks via tangent dynamics.

## Key Contributions

- Establishes a formal link between the dimensionality of dominant manifolds in RC networks and the intrinsic dimensionality of the training data.
- Proves that trained reservoir dominant modes correspond to approximations of Koopman eigenfunctions for autonomous dynamical systems.
- Unifies reservoir computing theory with Dynamic Mode Decomposition through an analysis of eigenvalue motion in the reservoir's learned dynamics.

## Key Concepts

- [[dominant-manifolds-in-reservoir-computing]]: A geometric characterization of reservoir computing training, where low-dimensional manifolds emerge aligned with training data dynamics.

## Archivist Review

I have approved the dominant manifolds concept as it provides a clear, geometric framing of recurrent network dynamics that is distinct from standard black-box training objectives. I rejected candidates related to DMD and Koopman theory because they are well-established fields in dynamical systems used here as analytical tools, not novel contributions. No datasets or open questions were proposed that met the rigorous standard for standalone vault entry.

### Approved Concepts
- Dominant Manifolds in Reservoir Computing: Provides a geometric framework for understanding how training shapes the recurrent dynamics of reservoir networks.

### Rejected Candidates
- [concept] Dynamic Mode Decomposition (`dynamic-mode-decomposition`) - not_novel: Dynamic Mode Decomposition is a well-established classical method in dynamical systems analysis, not a novel contribution of this paper.
- [concept] Koopman Eigenfunctions (`koopman-eigenfunctions`) - not_novel: Koopman theory is a foundational framework in dynamical systems; using it here is an application of existing theory rather than a new architectural concept.

## Links

- [Abstract](https://arxiv.org/abs/2604.05967)
- [PDF](https://arxiv.org/pdf/2604.05967)

