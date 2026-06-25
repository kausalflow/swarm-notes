---
# CSL-compatible fields
title: "Constraining Orbital Eccentricity of a Supermassive Black Hole Binary Candidate PKS 2131-021"
author:
  - literal: "Avinash Kumar Paladi"
  - literal: "A. Gopakumar"
  - literal: "Sushmita Agarwal"
  - literal: "Fazal Kareem"
issued:
  date-parts:
    - [2026, 6, 23]
url: "https://arxiv.org/abs/2606.05343"

# Custom fields
paper_id: "2606.05343"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-25T08:20:24Z"
created_at: "2026-06-25T08:20:24Z"
---

# Constraining Orbital Eccentricity of a Supermassive Black Hole Binary Candidate PKS 2131-021

**Authors**: Avinash Kumar Paladi, A. Gopakumar, Sushmita Agarwal, Fazal Kareem
**Date**: 2026-06-23
**Paper ID**: [openalex:2606.05343](https://arxiv.org/abs/2606.05343)

## Summary

This paper investigates the orbital dynamics of the supermassive black hole (SMBH) binary candidate PKS 2131-021 by analyzing its long-term radio light curve. The authors extend existing kinematic models of Doppler-boosted flux modulation to include orbital eccentricity, testing these models against multi-decadal observations. Bayesian inference demonstrates that after accounting for red noise via a damped random walk, the circular model is preferred over an eccentric one, establishing a tight upper bound on orbital eccentricity.

## Key Contributions

- Extends standard kinematic Doppler boosting models for binary SMBHs to explicitly incorporate orbital eccentricity using a Keplerian parametric solution.
- Performs rigorous Bayesian parameter estimation to constrain the orbital eccentricity of PKS 2131-021, yielding an upper limit of e < 0.15 under a noise-aware damped random walk model.
- Demonstrates that while a circular orbit model is statistically preferred when incorporating red noise (DRW process), the orbital period remains robustly recoverable across 46 years of multi-observatory data.

## Open Questions & Future Work

- [[pks-2131-021-eccentricity-uncertainty]]

## Archivist Review

The paper provides a domain-specific analysis of astrophysical radio light curves. While the scientific result is interesting, the methodology is a straightforward application of Bayesian parameter estimation to a Keplerian physical model, which does not introduce a new reusable ML forecasting concept or architecture. I have approved the open question regarding the eccentricity uncertainty as it highlights the challenge of disentangling physical signals from stochastic red noise, a problem relevant to time-series analysis in physics.

### Approved Open Questions
- Constraining PKS 2131-021 Eccentricity: Quantifying orbital eccentricity is critical for understanding the dynamical evolution, orbital decay, and gravitational wave emission characteristics of supermassive black hole binaries.

### Rejected Candidates
- [concept] Keplerian parametric solution for SMBHB eccentricity (`keplerian-parametric-solution-for-smbhb-eccentricity`) - paper_local: This is a domain-specific physical model parameterization rather than a reusable time-series forecasting mechanism.
- [dataset] Haystack, Michigan, and Owens Valley Observatory datasets (`haystack-university-michigan-owens-valley-data`) - paper_local: These are specific archival radio observational datasets rather than general-purpose benchmark datasets for ML time-series research.

## Links

- [Abstract](https://arxiv.org/abs/2606.05343)
- [PDF](https://arxiv.org/pdf/2606.05343)

