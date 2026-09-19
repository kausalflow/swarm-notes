---
# CSL-compatible fields
title: "Approximate Factor Models for Functional Time Series"
author:
  - literal: "Sven Otto"
  - literal: "Nazarii Salish"
issued:
  date-parts:
    - [2026, 9, 18]
url: "https://arxiv.org/abs/2201.02532"

# Custom fields
paper_id: "2201.02532"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-19T09:03:16Z"
created_at: "2026-09-19T09:03:16Z"
---

# Approximate Factor Models for Functional Time Series

**Authors**: Sven Otto, Nazarii Salish
**Date**: 2026-09-18
**Paper ID**: [openalex:2201.02532](https://arxiv.org/abs/2201.02532)

## Summary

This paper proposes an approximate factor model tailored for functional time series that decomposes time-dependent curve data into a low-dimensional predictable factor component and an unpredictable error term. The model parameters are consistently estimated via the eigencomponents of a cumulative autocovariance operator, and an information criterion determines the appropriate number of factors. Applied to mortality and yield curve modeling, the approach demonstrates parsimonious structural representations and improved out-of-sample forecast performance compared to functional principal component analysis.

## Key Contributions

- Proposed an approximate factor model tailored for functional time series that decomposes curve data into a low-dimensional predictable factor component and an unpredictable error term.
- Developed consistent parameter estimation using eigencomponents of a cumulative autocovariance operator along with an information criterion to determine the number of factors.
- Demonstrated superior out-of-sample forecasting performance and parsimonious structural representations on mortality and yield curve modeling compared to functional principal component analysis.

## Open Questions & Future Work

- [[distributional-inferential-theory-functional-factor-models-confidence-bands]]

## Archivist Review

Approved one open question concerning distributional and inferential theory for functional factor models. No new standalone vault concepts or named datasets qualified under the strict selection criteria.

### Approved Open Questions
- Distributional and Inferential Theory for Functional Factor Models: Crucial for statistical inference, hypothesis testing, and constructing valid confidence intervals for functional factor loadings and forecasts.

### Rejected Candidates
- [open_question] Non-Stationary Mixed-Memory Latent Factors (`non-stationary-mixed-memory-factors-long-memory-persistence`) - low_impact: Extension to long memory processes is a standard theoretical generalization rather than an essential standalone bottleneck note.

## Links

- [Abstract](https://arxiv.org/abs/2201.02532)
- [PDF](https://arxiv.org/pdf/2201.02532)

