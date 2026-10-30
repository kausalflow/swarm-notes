---
# CSL-compatible fields
title: "Global recovery from local data: interior nudging for 2D Navier–Stokes equations in a physical domain"
author:
  - literal: "Rui Fang"
  - literal: "Ali Pakzad"
issued:
  date-parts:
    - [2026, 10, 28]
url: "https://arxiv.org/abs/2601.11831"

# Custom fields
paper_id: "2601.11831"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-30T11:06:29Z"
created_at: "2026-10-30T11:06:29Z"
---

# Global recovery from local data: interior nudging for 2D Navier–Stokes equations in a physical domain

**Authors**: Rui Fang, Ali Pakzad
**Date**: 2026-10-28
**Paper ID**: [openalex:2601.11831](https://arxiv.org/abs/2601.11831)

## Summary

This paper studies the global recovery of the two-dimensional incompressible Navier–Stokes equations using continuous data assimilation restricted to a local interior subregion (interior nudging). The authors rigorously prove that the assimilated solution converges globally to the true solution when the observation region's geometry satisfies specific bounds relative to the viscosity. Computational results using finite element methods confirm these theoretical findings, showing that interior nudging achieves machine-precision global accuracy comparably to full-domain assimilation even under noisy conditions.

## Key Contributions

- Rigorously proves that global recovery of the 2D incompressible Navier-Stokes flow field can be achieved using observations restricted to an interior subregion under precise geometric and spatial resolution conditions.
- Demonstrates through finite element simulations that interior nudging performs comparably to full-domain assimilation, achieving global accuracy up to machine precision for both noise-free and noisy observations.
- Reveals that observational data near the boundary are largely uninformative, showing that interior observations away from boundaries suffice for global observability.

## Open Questions & Future Work

- [[sharpness-of-geometric-threshold-in-local-data-assimilation]]

## Archivist Review

After strict evaluation against vault standards, no new reusable ML concepts or benchmark datasets were found. However, the theoretical open question concerning the sharpness of geometric thresholds in continuous data assimilation with local interior observations is fundamental and substantive enough to warrant a persistent vault note.

### Approved Open Questions
- Sharpness of Geometric Threshold in Local Data Assimilation: Resolving this question bridges the gap between conservative analytical convergence bounds and robust empirical observations in fluid dynamics data assimilation, deepening the theoretical connection to classical Prandtl boundary layer theory.

## Links

- [Abstract](https://arxiv.org/abs/2601.11831)
- [PDF](https://arxiv.org/pdf/2601.11831)

