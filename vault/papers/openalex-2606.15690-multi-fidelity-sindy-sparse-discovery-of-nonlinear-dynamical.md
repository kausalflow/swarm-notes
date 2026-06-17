---
# CSL-compatible fields
title: "Multi-Fidelity SINDy: Sparse Discovery of Nonlinear Dynamical Systems with Fidelity-Weighted Measurements"
author:
  - literal: "Filippo Zacchei"
  - literal: "Ana Larrañaga"
  - literal: "Attilio Frangi"
  - literal: "Andrea Manzoni"
  - literal: "Steven L. Brunton"
issued:
  date-parts:
    - [2026, 6, 14]
url: "https://arxiv.org/abs/2606.15690"

# Custom fields
paper_id: "2606.15690"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "multi-fidelity-sindy"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:27:15Z"
created_at: "2026-06-17T09:27:15Z"
---

# Multi-Fidelity SINDy: Sparse Discovery of Nonlinear Dynamical Systems with Fidelity-Weighted Measurements

**Authors**: Filippo Zacchei, Ana Larrañaga, Attilio Frangi, Andrea Manzoni, Steven L. Brunton
**Date**: 2026-06-14
**Paper ID**: [openalex:2606.15690](https://arxiv.org/abs/2606.15690)

## Summary

This paper presents Multi-Fidelity SINDy, a robust framework for identifying nonlinear dynamical systems from heterogeneous, noise-corrupted data. By integrating Ensemble and Weak SINDy into a weighted regression scheme based on generalized least squares, the method effectively accounts for varying measurement fidelity. Empirical validation on ordinary and partial differential equations shows that the proposed approach mitigates the impact of heteroscedastic noise and effectively leverages low-cost, low-quality measurements to enhance model performance.

## Key Contributions

- Introduces Multi-Fidelity SINDy, a generalized framework that integrates Ensemble and Weak SINDy within a generalized least squares formulation to handle heteroscedastic noise.
- Provides a rigorous statistical justification for the fidelity-weighting strategy in sparse nonlinear dynamical system recovery.
- Demonstrates that integrating multi-fidelity data allows for improved model recovery and forecasting of complex dynamical systems like a double pendulum, often outperforming models trained exclusively on high-fidelity, high-cost data.

## Open Questions & Future Work

- [[refining-weak-residual-covariance-models]]

## Key Concepts

- [[multi-fidelity-sindy]]: A generalization of the SINDy framework that incorporates fidelity-weighted measurements through a generalized least squares formulation to improve nonlinear dynamical system discovery from inhomogeneous data.

## Archivist Review

The paper introduces a principled extension to the SINDy framework to account for heteroscedastic noise through generalized least squares, which is a highly reusable concept for system identification. The identified open question regarding the perturbation of the weak feature matrix represents a specific, non-trivial technical bottleneck for weak-form dynamical system discovery. No datasets were approved as the systems used for validation are standard benchmark equations rather than novel, domain-specific datasets.

### Approved Concepts
- Multi-Fidelity SINDy: It introduces a formal weighting strategy for SINDy to handle heteroscedastic noise in multi-fidelity data sources, which is a major limitation of standard SINDy.

### Approved Open Questions
- Refining Weak Residual Covariance Models: Improving the covariance approximation is crucial for ensuring the robustness and accuracy of the generalized least-squares weighting in the weak-SINDy framework, especially for complex PDEs where feature-matrix perturbations cannot be ignored.

## Links

- [Abstract](https://arxiv.org/abs/2606.15690)
- [PDF](https://arxiv.org/pdf/2606.15690)

