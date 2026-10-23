---
# CSL-compatible fields
title: "Directional Anisotropic Sensitivity Curves for Pulsar Timing Arrays"
author:
  - literal: "Daniel J Oliver"
  - literal: "Jeffrey S. Hazboun"
  - literal: "Martine Maggi"
  - literal: "J. G. Baier"
  - literal: "Kyle E. Gourlie"
issued:
  date-parts:
    - [2026, 10, 21]
url: "https://arxiv.org/abs/2608.00250"

# Custom fields
paper_id: "2608.00250"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-23T09:40:48Z"
created_at: "2026-10-23T09:40:48Z"
---

# Directional Anisotropic Sensitivity Curves for Pulsar Timing Arrays

**Authors**: Daniel J Oliver, Jeffrey S. Hazboun, Martine Maggi, J. G. Baier, Kyle E. Gourlie
**Date**: 2026-10-21
**Paper ID**: [openalex:2608.00250](https://arxiv.org/abs/2608.00250)

## Summary

This paper develops a directional anisotropic sensitivity framework for pulsar timing arrays to model and recover spatial hotspots in the stochastic gravitational wave background. By recasting directional Fisher information into effective sky sensitivity curves, the approach distinguishes radiometer and full-Fisher estimators and introduces a sky-weighted curve that generalizes standard isotropic curves. The method supports five sky-decomposition bases and is demonstrated on an IPTA-like array within the hasasia software package.

## Key Contributions

- Introduces directional anisotropic sensitivity curves for pulsar timing arrays to characterize spatial variations in sensitivity using effective sky sensitivity curves.
- Distinguishes radiometer and full-Fisher estimators while defining a sky-weighted curve that recovers standard isotropic sensitivity in the isotropic limit.
- Implements five distinct sky-decomposition bases (pixel, spherical harmonic, square-root spherical harmonic, radiometer, and principal-map).
- Demonstrates the framework on an IPTA-like pulsar timing array, recovering injected anisotropic hotspots and forecasting future-array performance via the hasasia software package.

## Open Questions & Future Work

- [[frequency-dependent-anisotropic-pta-extension]]

## Archivist Review

Applied rigorous filtering to adhere to vault scope. Pulsar timing array sensitivity curves are highly specialized astrophysical techniques rather than general time series or ML methodologies, so concepts were rejected. One open question addressing frequency-dependent anisotropic extensions for PTA was approved as it targets a structured future direction in spatial-temporal signal analysis.

### Approved Open Questions
- Frequency-Dependent Anisotropic PTA Extensions: Crucial for robustly interpreting real PTA data without biases from truncation or unmodeled propagation effects.

### Rejected Candidates
- [concept] Directional Anisotropic Sensitivity Curves (`directional-anisotropic-sensitivity-curves`) - low_impact: This method is domain-specific to pulsar timing arrays in astrophysics and lacks general reusability across broader time series or machine learning forecasting tasks.

## Links

- [Abstract](https://arxiv.org/abs/2608.00250)
- [PDF](https://arxiv.org/pdf/2608.00250)

