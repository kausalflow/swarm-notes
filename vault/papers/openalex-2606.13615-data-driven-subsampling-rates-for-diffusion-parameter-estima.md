---
# CSL-compatible fields
title: "Data-driven subsampling rates for diffusion parameter estimation of SDEs"
author:
  - literal: "Felix Lindner"
  - literal: "Andre Schmeißer"
  - literal: "Felipe Trolldenier"
  - literal: "Raimund Wegener"
issued:
  date-parts:
    - [2026, 6, 11]
url: "https://arxiv.org/abs/2606.13615"

# Custom fields
paper_id: "2606.13615"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "monotone-runs-analysis"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-14T08:38:44Z"
created_at: "2026-06-14T08:38:44Z"
---

# Data-driven subsampling rates for diffusion parameter estimation of SDEs

**Authors**: Felix Lindner, Andre Schmeißer, Felipe Trolldenier, Raimund Wegener
**Date**: 2026-06-11
**Paper ID**: [openalex:2606.13615](https://arxiv.org/abs/2606.13615)

## Summary

This paper addresses the challenge of estimating diffusion parameters for SDEs when the data and model scales are initially misaligned. The authors propose a data-driven method for optimal subsampling of time series data by leveraging the statistical properties of "monotone runs." By establishing that monotone run lengths for SDEs with additive noise are geometrically distributed with a specific success probability, the method allows for automated scale alignment without requiring multiscale asymptotic assumptions. The approach is validated using surrogate models for fiber lay-down curves in industrial nonwoven textile production.

## Key Contributions

- Introduces a data-driven method for selecting subsampling rates to align time series data with SDE model scales.
- Proves that lengths of monotone runs in SDEs with additive noise follow a geometric distribution with success probability 1/2 at infinitesimal scales.
- Provides an automated, non-asymptotic framework for parameter estimation applicable to industrial production process data.

## Open Questions & Future Work

- [[generalization-to-non-additive-noise-sde]]

## Key Concepts

- [[monotone-runs-analysis]]: A statistical method that uses the distribution of lengths of monotonic segments in a time series to determine optimal subsampling rates for SDE parameter estimation.

## Archivist Review

The paper presents a statistical tool to bridge the scale misalignment between empirical data and SDE-based physics models. The proposed 'Monotone Runs Analysis' is a reusable, model-agnostic concept for scale alignment, and the identified open question about non-additive noise addresses a fundamental limitation in the approach's theoretical reach. I have approved these as they align well with the goal of identifying reusable methods and meaningful theoretical research gaps in time series modeling.

### Approved Concepts
- Monotone Runs Analysis: Central to the proposed method for determining subsampling rates by matching data statistics to SDE model behavior.

### Approved Open Questions
- Generalizing SDE Noise Assumptions: Generalizing to non-additive noise is crucial for the applicability of this data-driven subsampling method to a wider range of physical and financial systems where diffusion characteristics are state-dependent.

## Links

- [Abstract](https://arxiv.org/abs/2606.13615)
- [PDF](https://arxiv.org/pdf/2606.13615)

