---
# CSL-compatible fields
title: "Universal ordinary differential equations and the parameterization of warm-rain processes"
author:
  - literal: "Axel Seifert"
issued:
  date-parts:
    - [2026, 8, 31]
url: "https://arxiv.org/abs/2608.30610"

# Custom fields
paper_id: "2608.30610"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "interpretable-parameterization"
  - "surrogate-model"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-03T09:17:48Z"
created_at: "2026-09-03T09:17:48Z"
---

# Universal ordinary differential equations and the parameterization of warm-rain processes

**Authors**: Axel Seifert
**Date**: 2026-08-31
**Paper ID**: [openalex:2608.30610](https://arxiv.org/abs/2608.30610)

## Summary

This paper applies universal ordinary differential equations (UODEs) to model warm-rain formation in cloud microphysics by training exclusively on prognostic state variables from super-droplet model trajectories approximating the kinetic collection equation. The learned surrogate accurately captures KCE trajectories and recovers realistic autoconversion and accretion rates without explicit supervision on these rates. Furthermore, analyzing the learned operator reveals structural insights into existing analytical parameterizations, leading to a refined formulation that improves accuracy while preserving simplicity.

## Key Contributions

- Demonstrates the application of universal ordinary differential equations (UODEs) to parameterize warm-rain formation using prognostic state variables alone without requiring intermediate rates as targets.
- Shows that the learned UODE closure accurately reproduces kinetic collection equation (KCE) trajectories and implicitly discovers physically realistic autoconversion and accretion rates.
- Provides analytical insights into the Seifert and Beheng (2001) warm-rain parameterization, showing that empirical accretion suppression compensates for over-estimated autoconversion at small rain fractions.
- Proposes a refined analytical formulation that improves agreement with KCE while maintaining the original parameterization's simplicity.

## Open Questions & Future Work

- [[uode-warm-rain-three-dimensional-validation]]

## Archivist Review

Applied strict selectivity: universal ordinary differential equations (UODEs) are a broader existing methodology rather than a new standalone concept note, but the open question regarding operational three-dimensional validation of machine-learning-derived microphysical parameterizations represents a valuable, reusable future research direction in scientific machine learning for weather and climate.

### Approved Open Questions
- Three-Dimensional and Comprehensive Model Validation: Evaluating whether machine-learning-derived microphysical closures translate to improved predictive skill in operational weather and climate models is a critical bottleneck in scientific machine learning for Earth sciences.

### Rejected Candidates
- [open_question] Three-Dimensional and Comprehensive Model Validation (`uode-warm-rain-three-dimensional-validation`) - duplicate_existing: Already approved above.

## Links

- [Abstract](https://arxiv.org/abs/2608.30610)
- [PDF](https://arxiv.org/pdf/2608.30610)

