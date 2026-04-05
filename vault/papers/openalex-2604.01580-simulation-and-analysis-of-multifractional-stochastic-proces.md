---
# CSL-compatible fields
title: "Simulation and Analysis of Multifractional Stochastic Processes with R Package Rmfrac"
author:
  - literal: "Andriy Olenko"
  - literal: "Nemini Samarakoon"
issued:
  date-parts:
    - [2026, 4, 2]
url: "https://arxiv.org/abs/2604.01580"

# Custom fields
paper_id: "2604.01580"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "gaussian-haar-based-multifractional-processes"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-05T06:09:05Z"
created_at: "2026-04-05T06:09:05Z"
---

# Simulation and Analysis of Multifractional Stochastic Processes with R Package Rmfrac

**Authors**: Andriy Olenko, Nemini Samarakoon
**Date**: 2026-04-02
**Paper ID**: [openalex:2604.01580](https://arxiv.org/abs/2604.01580)

## Summary

This paper introduces the Rmfrac R package, a tool designed to simulate and analyze Gaussian Haar-based multifractional processes. These processes extend classical fractional Brownian motion by allowing for time-varying regularity, providing more flexible modeling for non-stationary time series. The package includes functionality for Hurst function estimation, local fractal dimension calculation, and comprehensive visualization through a Shiny application.

## Key Contributions

- Introduces the Rmfrac R package for the simulation, estimation, and visualization of Gaussian Haar-based multifractional processes.
- Provides tools for estimating the Hurst function and local fractal dimensions, along with clustering and geometric statistics for non-stationary time series.
- Includes a Shiny-based interface to facilitate the practical application and analysis of these multifractional models.

## Key Concepts

- [[gaussian-haar-based-multifractional-processes]]: A class of multifractional processes that utilizes Haar wavelet series representations to allow for time-varying regularity in stochastic models.

## Archivist Review

The paper describes a specialized software package for stochastic modeling. I approved the underlying theoretical concept, Gaussian Haar-based multifractional processes, as it represents a significant and reusable approach for modeling non-stationary time series with time-varying regularity. The software package itself was rejected as it is a tool-specific implementation rather than a conceptual contribution to the field.

### Approved Concepts
- Gaussian Haar-based multifractional processes: It provides a flexible framework for modeling non-stationary time series by allowing for time-varying regularity through a Haar wavelet series representation.

### Rejected Candidates
- [concept] Rmfrac R package (`rmfrac-package`) - not_reusable: This is a software package implementation rather than a foundational theoretical concept or architectural innovation.

## Links

- [Abstract](https://arxiv.org/abs/2604.01580)
- [PDF](https://arxiv.org/pdf/2604.01580)

