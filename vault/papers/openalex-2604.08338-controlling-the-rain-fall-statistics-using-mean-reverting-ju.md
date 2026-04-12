---
# CSL-compatible fields
title: "Controlling the rain fall statistics using Mean-Reverting Jump Diffusion model"
author:
  - literal: "Joya GhoshDastider"
  - literal: "D. Pal"
  - literal: "Pankaj Kumar Mishra"
issued:
  date-parts:
    - [2026, 4, 9]
url: "https://arxiv.org/abs/2604.08338"

# Custom fields
paper_id: "2604.08338"
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
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-12T06:20:22Z"
created_at: "2026-04-12T06:20:22Z"
---

# Controlling the rain fall statistics using Mean-Reverting Jump Diffusion model

**Authors**: Joya GhoshDastider, D. Pal, Pankaj Kumar Mishra
**Date**: 2026-04-09
**Paper ID**: [openalex:2604.08338](https://arxiv.org/abs/2604.08338)

## Summary

This paper presents a stochastic mean-reverting jump-diffusion model designed to simulate complex rainfall time series, focusing on capturing intermittent dynamics, extreme events, and multifractal properties. The authors validate the model using high-resolution half-hourly data from North-East India, demonstrating its ability to reproduce observed spectral signatures and temporal scales. By adjusting model parameters, the framework allows for the controlled generation of synthetic rainfall, including transitions between Log-Normal and Gamma distributional forms. The proposed approach offers a robust tool for investigating the underlying stochastic processes that govern rainfall statistics.

## Key Contributions

- Introduces a stochastic mean-reverting jump-diffusion model for simulating rainfall dynamics, capturing intermittency and extreme events.
- Demonstrates the model's ability to reproduce multifractal features and superdiffusive behavior with an exponent of ~1.8.
- Establishes a parameter-driven framework to control rainfall statistics, including the transition between Log-Normal and Gamma distributions and the frequency of dry-patch durations.

## Open Questions & Future Work

- [[incorporating-spatio-temporal-correlations-in-rainfall-models]]

## Archivist Review

The paper proposes a specific application of mean-reverting jump-diffusion models for rainfall simulation. I have rejected the conceptual claims as they represent a domain-specific application of well-established stochastic processes rather than a new, broadly reusable ML methodology. I have approved one open question concerning the integration of spatio-temporal correlations, as this addresses a fundamental bottleneck in stochastic precipitation modeling.

### Approved Open Questions
- Integrating Spatio-Temporal Rainfall Dynamics: Improving the spatial realism of stochastic rainfall models is critical for risk assessment and for better understanding how precipitation patterns evolve under shifting climatic conditions.

### Rejected Candidates
- [open_question] Empirical Validation of Model Predictions (`validation-of-stochastic-rainfall-model-predictions`) - low_impact: This is a generic call for more data and empirical validation, which falls under boilerplate future work.

## Links

- [Abstract](https://arxiv.org/abs/2604.08338)
- [PDF](https://arxiv.org/pdf/2604.08338)

