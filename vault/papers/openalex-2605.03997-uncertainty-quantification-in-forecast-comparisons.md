---
# CSL-compatible fields
title: "Uncertainty Quantification in Forecast Comparisons"
author:
  - literal: "Marc‐Oliver Pohle"
  - literal: "Tanja Zahn"
  - literal: "Sebastian Lerch"
issued:
  date-parts:
    - [2026, 5, 5]
url: "https://arxiv.org/abs/2605.03997"

# Custom fields
paper_id: "2605.03997"
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
  - "simultaneous-confidence-bands-for-skill-scores"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-08T06:27:14Z"
created_at: "2026-05-08T06:27:14Z"
---

# Uncertainty Quantification in Forecast Comparisons

**Authors**: Marc‐Oliver Pohle, Tanja Zahn, Sebastian Lerch
**Date**: 2026-05-05
**Paper ID**: [openalex:2605.03997](https://arxiv.org/abs/2605.03997)

## Summary

This paper addresses the lack of rigorous uncertainty quantification in multi-dimensional forecast evaluation by introducing simultaneous confidence bands for skill scores. By accounting for the multiple comparison problem across time horizons, variables, and spatial locations, the proposed framework avoids the inflated Type I error rates associated with traditional pointwise intervals or standard accuracy tests. The approach is versatile, supporting various forecast types from point to full distributional predictions, and is validated through case studies in macroeconomic and weather forecasting.

## Key Contributions

- Introduces a framework for simultaneous confidence bands for skill scores to enable statistically valid joint inference in multi-dimensional forecasting evaluations.
- Addresses the multiple comparison problem in forecast evaluation, preventing inflated Type I error rates typical of pointwise confidence intervals.
- Provides a bootstrap-based implementation applicable to diverse forecasting types, including mean, quantile, and full distributional forecasts.

## Open Questions & Future Work

- [[high-dimensional-confidence-bands-inference]]
- [[multivariate-block-length-selection]]

## Key Concepts

- [[simultaneous-confidence-bands-for-skill-scores]]: A statistical framework for joint inference in multi-dimensional forecast evaluation that accounts for multiple comparison problems across variables, horizons, and methods.

## Archivist Review

The paper addresses a critical gap in forecast evaluation by proposing a robust framework for joint inference. The concept of simultaneous confidence bands provides a necessary statistical tool for the increasing dimensionality of modern forecasting tasks. The open questions accurately identify the limitations in asymptotic theory and bootstrapping protocols for these high-dimensional evaluation settings.

### Approved Concepts
- Simultaneous Confidence Bands for Skill Scores: Provides a statistically rigorous method for multi-dimensional forecast evaluation that avoids the inflated Type I error rates associated with pointwise intervals.

### Approved Open Questions
- High-dimensional simultaneous confidence bands: High-dimensional forecast evaluation, such as in spatial weather modeling, requires theoretical justification for inference when the number of evaluation points is large, as current frameworks rely on fixed-dimension asymptotics.
- Multivariate block length selection: The accuracy of uncertainty quantification via the block bootstrap is highly sensitive to block length; an automatic selection procedure would remove a significant source of researcher subjectivity and potential bias.

## Links

- [Abstract](https://arxiv.org/abs/2605.03997)
- [PDF](https://arxiv.org/pdf/2605.03997)

