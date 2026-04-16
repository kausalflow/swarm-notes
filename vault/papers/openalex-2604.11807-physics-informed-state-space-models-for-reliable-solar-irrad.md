---
# CSL-compatible fields
title: "Physics-Informed State Space Models for Reliable Solar Irradiance Forecasting in Off-Grid Systems"
author:
  - literal: "Mohammed Ezzaldin Babiker Abdullah"
issued:
  date-parts:
    - [2026, 4, 13]
url: "https://arxiv.org/abs/2604.11807"

# Custom fields
paper_id: "2604.11807"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "ssm"
  - "mamba"
  - "physics-informed-machine-learning"
architectures:
  - "mamba"
datasets:
  []
concept_slugs:
  - "thermodynamic-liquid-manifold-network"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-16T06:28:35Z"
created_at: "2026-04-16T06:28:35Z"
---

# Physics-Informed State Space Models for Reliable Solar Irradiance Forecasting in Off-Grid Systems

**Authors**: Mohammed Ezzaldin Babiker Abdullah
**Date**: 2026-04-13
**Paper ID**: [openalex:2604.11807](https://arxiv.org/abs/2604.11807)

## Summary

This paper addresses the failure of traditional deep learning models to respect physical laws in solar irradiance forecasting, specifically regarding nocturnal artifacts and phase lags during cloud transients. The proposed Thermodynamic Liquid Manifold Network utilizes a Koopman-linearized Riemannian manifold to project meteorological data while enforcing clear-sky boundary conditions. By incorporating specialized spectral calibration and gating mechanisms, the model eliminates physically impossible predictions and ensures rapid temporal response. Extensive validation on five years of semi-arid climate data confirms the framework's reliability for autonomous off-grid energy systems.

## Key Contributions

- Introduced the Thermodynamic Liquid Manifold Network, a physics-informed state space model that enforces celestial geometry compliance in solar irradiance forecasting.
- Achieved a zero-magnitude nocturnal error over a 5-year testing horizon while maintaining sub-30-minute phase response during high-frequency weather transients.
- Demonstrated high accuracy (RMSE 18.31 Wh/m2, Pearson correlation 0.988) with an ultra-lightweight footprint of 63,458 parameters, suitable for edge-deployable microgrid controllers.

## Key Concepts

- [[thermodynamic-liquid-manifold-network]]: An architecture that projects meteorological variables into a Koopman-linearized Riemannian manifold to enforce atmospheric thermodynamic consistency.

## Archivist Review

I approved the Thermodynamic Liquid Manifold Network as it represents a novel synthesis of Koopman theory and manifold learning for constrained time-series forecasting. I rejected the sub-components of this architecture as they are specific to the implementation of the primary mechanism and do not yet qualify as independently reusable concepts. No datasets or open questions were proposed, and none were extracted, keeping the focus on the primary methodological contribution.

### Approved Concepts
- Thermodynamic Liquid Manifold Network: The core architectural innovation enabling physics-informed projection into a Koopman-linearized manifold for celestial mechanics adherence.

### Rejected Candidates
- [concept] Spectral Calibration unit (`spectral-calibration-unit`) - subcomponent_of_broader_mechanism: This is a local subcomponent of the overarching Thermodynamic Liquid Manifold Network and lacks independent evidence of broad utility.
- [concept] Thermodynamic Alpha-Gate (`thermodynamic-alpha-gate`) - subcomponent_of_broader_mechanism: This is a specific architectural helper module whose function is tied to the main network rather than a widely reusable mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2604.11807)
- [PDF](https://arxiv.org/pdf/2604.11807)

