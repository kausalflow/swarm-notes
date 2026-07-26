---
# CSL-compatible fields
title: "Modeling Dependence Structures in Astronomical Multi-Band Time Series Data via Multi-Output Gaussian Processes"
author:
  - literal: "Samata Das"
  - literal: "Lu Shi"
  - literal: "Yasaman Hamayouni"
  - literal: "Hyungsuk Tak"
  - literal: "Jong-Hak Woo"
issued:
  date-parts:
    - [2026, 7, 23]
url: "https://arxiv.org/abs/2607.21431"

# Custom fields
paper_id: "2607.21431"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "gaussian-process-state-space-models"
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
processed_at: "2026-07-26T07:29:42Z"
created_at: "2026-07-26T07:29:42Z"
---

# Modeling Dependence Structures in Astronomical Multi-Band Time Series Data via Multi-Output Gaussian Processes

**Authors**: Samata Das, Lu Shi, Yasaman Hamayouni, Hyungsuk Tak, Jong-Hak Woo
**Date**: 2026-07-23
**Paper ID**: [openalex:2607.21431](https://arxiv.org/abs/2607.21431)

## Summary

This paper presents a unified statistical framework utilizing multi-output Gaussian processes to model dependence structures across multi-band astronomical time series data. The authors compare covariance-based formulations, which directly specify matrix-valued covariance functions and spectral densities, with latent-process formulations that model observed light curves as transformations of latent GPs. To illustrate these approaches, they develop multi-output damped random walk models and apply them to active galactic nucleus variability and continuum reverberation mapping.

## Key Contributions

- Presents a unified statistical framework using multi-output Gaussian processes to model dependence structures in astronomical multi-band time series data.
- Compares covariance-based formulations (emphasizing stochastic properties and spectral densities) with latent-process formulations (emphasizing physical mechanisms).
- Develops multi-output damped random walk models with derived spectral representations for both formulations.
- Demonstrates practical applications on multi-band active galactic nucleus variability and continuum reverberation mapping.

## Open Questions & Future Work

- [[uncertainty-propagation-multi-output-gps]]

## Archivist Review

The paper presents a statistical comparison of covariance-based vs latent-process formulations for multi-output GPs in astronomy without introducing a standalone reusable algorithm or dataset. The open question regarding uncertainty propagation in multi-output GPs duplicates existing vault coverage on uncertainty quantification and scaling limitations for multi-output/state-space models.

### Approved Open Questions
- Uncertainty Quantification in Multi-Output GPs: Rigorous uncertainty quantification is critical for scientific interpretation and model comparison in modern astronomical surveys, ensuring that derived physical constraints (such as reverberation lags and spectral properties) are statistically robust.

### Rejected Candidates
- [open_question] Uncertainty Quantification in Multi-Output GPs (`uncertainty-propagation-multi-output-gps`) - duplicate_existing: A similar open question regarding uncertainty quantification in multi-output systems already exists in the vault.

## Links

- [Abstract](https://arxiv.org/abs/2607.21431)
- [PDF](https://arxiv.org/pdf/2607.21431)

