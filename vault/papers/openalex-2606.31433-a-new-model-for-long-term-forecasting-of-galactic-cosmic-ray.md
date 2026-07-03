---
# CSL-compatible fields
title: "A new model for long-term forecasting of Galactic cosmic rays"
author:
  - literal: "David Pelosi"
  - literal: "F. Barão"
  - literal: "B. Bertucci"
  - literal: "E. Fiandrini"
  - literal: "Miguel Orcinha"
  - literal: "Nicola Tomassetti"
issued:
  date-parts:
    - [2026, 6, 30]
url: "https://arxiv.org/abs/2606.31433"

# Custom fields
paper_id: "2606.31433"
paper_source: "openalex"
domain: "physics"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "hilbert-huang-proxy-parametric-coupling"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-03T07:55:17Z"
created_at: "2026-07-03T07:55:17Z"
---

# A new model for long-term forecasting of Galactic cosmic rays

**Authors**: David Pelosi, F. Barão, B. Bertucci, E. Fiandrini, Miguel Orcinha, Nicola Tomassetti
**Date**: 2026-06-30
**Paper ID**: [openalex:2606.31433](https://arxiv.org/abs/2606.31433)

## Summary

The authors present a physics-informed forecasting framework for long-term galactic cosmic-ray fluxes based on solving a one-dimensional, spherically symmetric Parker transport equation. By utilizing Hilbert-Huang transform filtering and cross-correlation between solar proxies and model parameters, the model successfully captures charge-sign and rigidity-dependent modulation effects. The framework is validated against multi-species, multi-experiment data from PAMELA, AMS-02, and ACE, demonstrating robust performance for decadal-scale space radiation risk assessment.

## Key Contributions

- Introduces a novel numerical forecasting framework for galactic cosmic-ray fluxes based on the 1D Parker transport equation.
- Demonstrates improved long-term predictive capability by linking solar-proxy dynamics to effective diffusion-advection model parameters via Hilbert-Huang transform filtering.
- Validates performance using multi-species, energy-dependent, and charge-sign-dependent measurements from PAMELA, AMS-02, and ACE datasets across solar cycles.

## Open Questions & Future Work

- [[phase-dependent-gcr-modulation-calibration]]

## Key Concepts

- [[hilbert-huang-proxy-parametric-coupling]]: A time-series forecasting framework that uses Hilbert-Huang transform filtering to dynamically calibrate physical model parameters based on delayed exogenous proxies.

## Archivist Review

The paper presents a physics-informed forecasting framework for cosmic-ray modulation. I approved the mechanism of Hilbert-Huang proxy coupling because it is a generalizable approach for mapping exogenous proxies to model parameters. I also approved the open question regarding phase-dependent calibration, as it highlights a significant unresolved limitation in modeling non-stationary dynamical systems. Datasets were rejected because they represent specific measurement instruments rather than standard ML benchmarks.

### Approved Concepts
- Hilbert-Huang Proxy-Parametric Coupling: This method provides a robust, physics-informed approach to forecasting by using signal decomposition (HHT) to align exogenous proxies with parameters of a dynamical model, a technique applicable to other physical forecasting tasks.

### Approved Open Questions
- Phase-dependent modulation calibration: This addresses a fundamental limitation in non-stationary heliophysics forecasting, where generic proxy-based models fail to account for distinct physical regime behaviors.

### Rejected Candidates
- [concept] Hilbert-Huang transform-based cosmic ray forecasting (`hilbert-huang-transform-based-cosmic-ray-forecasting`) - other: The concept was renamed for better generalization and conciseness.
- [dataset] PAMELA (`PAMELA`) - low_impact: Specific instrument data often serve as experimental validation rather than reusable benchmarking standards in the context of this vault.
- [dataset] AMS-02 (`AMS-02`) - low_impact: Instrument-specific data used for validation in physics papers do not generally constitute a reusable benchmark dataset in the sense of modern ML evaluation.
- [dataset] ACE (`ACE`) - low_impact: Instrument-specific data are not a reusable standalone dataset for ML forecasting benchmarks.

## Links

- [Abstract](https://arxiv.org/abs/2606.31433)
- [PDF](https://arxiv.org/pdf/2606.31433)

