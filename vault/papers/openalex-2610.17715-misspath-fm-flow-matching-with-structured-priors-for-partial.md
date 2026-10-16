---
# CSL-compatible fields
title: "MissPath-FM: Flow Matching with Structured Priors for Partially Observed Time Series"
author:
  - literal: "Genpei Zhang"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.17715"

# Custom fields
paper_id: "2610.17715"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "diffusion-model"
  - "generative-adversarial-network"
  - "forecasting"
  - "imputation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "misspath-fm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-16T09:23:15Z"
created_at: "2026-10-16T09:23:15Z"
---

# MissPath-FM: Flow Matching with Structured Priors for Partially Observed Time Series

**Authors**: Genpei Zhang
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.17715](https://arxiv.org/abs/2610.17715)

## Summary

MissPath-FM is a partial-observation-aware flow matching framework designed for incomplete time series that replaces uninformed Gaussian sources with structured priors (such as interpolation and Gaussian process posteriors) and missingness-aware smooth paths. This design avoids wasting model capacity on transporting already-observed entries from noise, concentrating velocity fields on genuinely uncertain regions. Extensive evaluations across 48 settings demonstrate superior performance over multiple baselines, achieving a 93.8% overall win rate.

## Key Contributions

- Proposes MissPath-FM, a partial-observation-aware flow matching framework that integrates structured source priors (interpolation and Gaussian process posterior priors) to initialize flows close to observed signals.
- Introduces a missingness-aware smooth probability path that asymmetrically allocates transport between observed and missing regions, shortening observed-region transport by up to 15x.
- Evaluates across 48 settings (combining four datasets, four missingness mechanisms, two missing ratios, and three sequence lengths) against eight baselines, winning 45 of 48 overall (93.8%).

## Open Questions & Future Work

- [[scaling-flow-matching-structured-priors-time-series]]

## Key Concepts

- [[misspath-fm]]: A partial-observation-aware flow matching framework for incomplete time series that uses structured source priors and missingness-aware smooth paths to avoid wasting capacity on observed regions.

## Archivist Review

Approved the core framework 'MissPath-FM' as it introduces a reusable and principled design pattern for flow matching on partially observed time series. Also approved the open question regarding scaling limitations of structured priors in high dimensions. No datasets were approved because specific named datasets were omitted from the abstract text.

### Approved Concepts
- MissPath-FM: Introduces a novel partial-observation-aware flow matching framework with structured source priors and missingness-aware smooth paths for time series imputation and forecasting.

### Approved Open Questions
- Scaling Flow Matching with Structured Priors: This is technically important because exact inference for structured time-series priors scales poorly with high dimensionality and sequence length, limiting applicability to large-scale multivariate clinical or financial time series.

## Links

- [Abstract](https://arxiv.org/abs/2610.17715)
- [PDF](https://arxiv.org/pdf/2610.17715)

