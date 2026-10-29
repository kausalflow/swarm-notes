---
# CSL-compatible fields
title: "From Stochastic Transport Models to High-Dimensional Bayesian Inference"
author:
  - literal: "Dan Crisan"
  - literal: "Oana Lang"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.35352"

# Custom fields
paper_id: "2610.35352"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "uncertainty-quantification"
  - "stochastic-differential-equations"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-29T11:11:56Z"
created_at: "2026-10-29T11:11:56Z"
---

# From Stochastic Transport Models to High-Dimensional Bayesian Inference

**Authors**: Dan Crisan, Oana Lang
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.35352](https://arxiv.org/abs/2610.35352)

## Summary

This paper provides a comprehensive synthesis of theoretical, calibration, and Bayesian data assimilation developments associated with stochastic transport models in geophysical fluid dynamics. It bridges the gap between modelling paradigms and rigorous mathematical frameworks by detailing well-posedness, geometric foundations, and calibration strategies. Additionally, the review covers advanced high-dimensional Bayesian inference techniques such as particle filters and machine learning-based uncertainty quantification.

## Key Contributions

- Synthesizes the theoretical, variational, and data assimilation developments of the Stochastic Transport in Upper Ocean Dynamics project.
- Establishes the mathematical rigor of stochastic transport equations via well-posedness, regularity, approximation, and stochastic variational principles.
- Reviews data-driven calibration methodologies ranging from reduced-order models to generative approaches for stochastic transport structures.
- Outlines high-dimensional Bayesian inference techniques including particle filtering and machine learning uncertainty quantification for geophysical fluid dynamics.

## Open Questions & Future Work

- [[global-well-posedness-stochastic-transport-models]]
- [[adaptive-online-calibration-stochastic-transport]]

## Archivist Review

The paper provides a high-level synthesis of stochastic transport models and data assimilation in geophysical fluid dynamics rather than introducing a distinct standalone concept. Consequently, no new concepts were approved, while two foundational open questions regarding mathematical well-posedness and online calibration of stochastic transport models were selected.

### Approved Open Questions
- Global Well-Posedness of Stochastic Transport Models: Resolving global well-posedness versus finite-time blow-up determines whether stochastic transport models are mathematically sound over long time horizons, which is critical for climate and weather prediction applications.
- Adaptive Online Calibration of Stochastic Transport: Online and adaptive calibration bridges the gap between static offline parameter learning and real-time operational data assimilation where flow regimes dynamically shift.

### Rejected Candidates
- [open_question] Diagnostics for Adaptive Tempering (`diagnostics-for-adaptive-tempering`) - low_impact: Too general to particle filtering and MCMC literature rather than specifically constrained to stochastic fluid transport modeling.

## Links

- [Abstract](https://arxiv.org/abs/2610.35352)
- [PDF](https://arxiv.org/pdf/2610.35352)

