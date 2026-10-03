---
# CSL-compatible fields
title: "Physics-Informed Nonlinear Vector Autoregressive Models for the Prediction of Dynamical Systems"
author:
  - literal: "James H. Adler"
  - literal: "Samuel Hocking"
  - literal: "Xiaozhe Hu"
  - literal: "Shafiqul Islam"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2407.18057"

# Custom fields
paper_id: "2407.18057"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "dynamical-systems"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:09:02Z"
created_at: "2026-10-03T10:09:02Z"
---

# Physics-Informed Nonlinear Vector Autoregressive Models for the Prediction of Dynamical Systems

**Authors**: James H. Adler, Samuel Hocking, Xiaozhe Hu, Shafiqul Islam
**Date**: 2026-09-30
**Paper ID**: [openalex:2407.18057](https://arxiv.org/abs/2407.18057)

## Summary

This paper introduces physics-informed nonlinear vector autoregression (piNVAR), a framework that integrates the known right-hand side of governing ordinary differential equations into nonlinear vector autoregressive models for dynamical system prediction. By exploiting shared parameters between standard NVAR and piNVAR, the authors propose an augmented joint training procedure that captures dynamic relationships while respecting physical constraints. Evaluations across benchmark systems such as the undamped spring, Lotka-Volterra, and chaotic Lorenz equations demonstrate the efficacy of the proposed approach using data-driven and ODE-driven metrics.

## Key Contributions

- Introduces physics-informed nonlinear vector autoregression (piNVAR) to explicitly enforce underlying differential equation constraints on NVAR models.
- Proposes an augmented joint training procedure leveraging shared parameters between standard NVAR and piNVAR.
- Evaluates performance on ordinary differential equation systems including the undamped spring, Lotka-Volterra predator-prey model, and chaotic Lorenz system using both data-driven and ODE-driven metrics.

## Archivist Review

Applied strict standards to ensure only central, reusable forecasting mechanisms and foundational open questions enter the vault. Since the analysis presented no concepts and only a paper-local future work direction on higher-order basis scaling, no items were approved.

### Rejected Candidates
- [open_question] Higher-Order piNVAR Scaling and Analysis (`higher-order-pinvar-scaling-and-analysis`) - low_impact: Future work examining higher-order polynomial bases and model sizes is too paper-local and incremental.

## Links

- [Abstract](https://arxiv.org/abs/2407.18057)
- [PDF](https://arxiv.org/pdf/2407.18057)

