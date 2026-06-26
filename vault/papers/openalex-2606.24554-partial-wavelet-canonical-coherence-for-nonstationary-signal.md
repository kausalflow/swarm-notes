---
# CSL-compatible fields
title: "Partial Wavelet Canonical Coherence for Nonstationary Signals with High Dimensional Confounders"
author:
  - literal: "H. Wu"
  - literal: "MI Knight"
  - literal: "Hernando Ombao"
issued:
  date-parts:
    - [2026, 6, 23]
url: "https://arxiv.org/abs/2606.24554"

# Custom fields
paper_id: "2606.24554"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "partial-wavelet-canonical-coherence"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-26T08:25:36Z"
created_at: "2026-06-26T08:25:36Z"
---

# Partial Wavelet Canonical Coherence for Nonstationary Signals with High Dimensional Confounders

**Authors**: H. Wu, MI Knight, Hernando Ombao
**Date**: 2026-06-23
**Paper ID**: [openalex:2606.24554](https://arxiv.org/abs/2606.24554)

## Summary

This paper introduces Partial Wavelet Canonical Coherence (PWCC) as a novel frequency-domain measure for quantifying the direct association between two multivariate nonstationary time series while controlling for high-dimensional confounders. By leveraging the multivariate locally stationary wavelet framework, the method provides time-varying and scale-specific estimates of dependency. The approach integrates local wavelet spectral matrices and principal component reduction to ensure stability in high-dimensional settings, effectively isolating direct relationships from spurious marginal associations.

## Key Contributions

- Introduces Partial Wavelet Canonical Coherence (PWCC) to measure direct canonical association in nonstationary multivariate time series adjusted for high-dimensional confounders.
- Establishes the first frequency-domain formulation of partial canonical correlation analysis using the multivariate locally stationary wavelet framework.
- Demonstrates the method's ability to remove spurious marginal associations and recover direct associations in both simulation studies and real-world financial data (U.S. ETFs).

## Open Questions & Future Work

- [[advanced-dimension-reduction-partial-wavecancoh]]

## Key Concepts

- [[partial-wavelet-canonical-coherence]]: A frequency-domain, scale-specific, and time-varying measure of direct association between multivariate signals adjusted for high-dimensional confounders.

## Archivist Review

I approved the Partial Wavelet Canonical Coherence concept as it introduces a novel, reusable frequency-domain dependency measure for nonstationary time series. The open question regarding advanced dimension-reduction was approved to address the fundamental statistical challenge of high-dimensional confounding in nonstationary settings. The second open question was rejected as it was too generic in its request for standard inferential theory.

### Approved Concepts
- Partial Wavelet Canonical Coherence: It provides the first frequency-domain formulation of partial canonical correlation analysis for multivariate nonstationary time series.

### Approved Open Questions
- Advanced dimension-reduction for Partial WaveCanCoh: Robust handling of high-dimensional confounding is critical for applying this framework to complex multivariate datasets where confounding effects are pervasive.

## Links

- [Abstract](https://arxiv.org/abs/2606.24554)
- [PDF](https://arxiv.org/pdf/2606.24554)

