---
# CSL-compatible fields
title: "Neural Simulation-Based Inference for space-time Gaussian processes"
author:
  - literal: "Alexandre Loret"
  - literal: "Lucia Clarotto"
  - literal: "Nicolas Desassis"
  - literal: "Thomas Romary"
issued:
  date-parts:
    - [2026, 10, 27]
url: "https://arxiv.org/abs/2610.36855"

# Custom fields
paper_id: "2610.36855"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "uncertainty-quantification"
  - "simulation-based-inference"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-30T11:05:32Z"
created_at: "2026-10-30T11:05:32Z"
---

# Neural Simulation-Based Inference for space-time Gaussian processes

**Authors**: Alexandre Loret, Lucia Clarotto, Nicolas Desassis, Thomas Romary
**Date**: 2026-10-27
**Paper ID**: [openalex:2610.36855](https://arxiv.org/abs/2610.36855)

## Summary

Estimating covariance parameters for large spatio-temporal Gaussian random fields using maximum likelihood estimation is computationally expensive. To address this, the authors propose Neural Bayes Estimation (NBE) and Neural Ratio Estimation (NRE), leveraging simulation-based inference to learn Gneiting-Matérn model parameters with advection. Trained on synthetic simulations, the models achieve fully amortized inference through a single forward pass, bypassing iterative optimization. The approach is successfully applied to solar radiation prediction and short-term forecasting using a sliding-window technique to accommodate temporal non-stationarity.

## Key Contributions

- Proposes Neural Bayes Estimation (NBE) and Neural Ratio Estimation (NRE) frameworks for amortized parameter inference of spatio-temporal Gneiting-Matérn covariance models with advection.
- Replaces computationally prohibitive maximum likelihood estimation (MLE) for Gaussian random fields with a single forward pass via offline simulation-based training.
- Demonstrates strong performance in accuracy and uncertainty quantification across 1D and 2D spatial dimensions for spatio-temporal data analysis.
- Applies the framework to solar radiation prediction and short-term forecasting using a sliding-window approach to handle temporal non-stationarity.

## Archivist Review

The paper investigates neural simulation-based inference (using Neural Bayes Estimation and Neural Ratio Estimation) for spatio-temporal Gaussian random fields and covariance parameter estimation. Because no reusable forecasting architectures, distinct time-series concepts, or unique named benchmarks were proposed that fit the stringent vault inclusion criteria, all candidates were rejected to maintain database purity.

## Links

- [Abstract](https://arxiv.org/abs/2610.36855)
- [PDF](https://arxiv.org/pdf/2610.36855)

