---
# CSL-compatible fields
title: "Temporal Seam Score for Assessing Continuity at Known Transitions in Time Series"
author:
  - literal: "Hongxiao Jin"
issued:
  date-parts:
    - [2026, 9, 14]
url: "https://arxiv.org/abs/2609.15132"

# Custom fields
paper_id: "2609.15132"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "temporal-seam-score"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:43:24Z"
created_at: "2026-09-17T09:43:24Z"
---

# Temporal Seam Score for Assessing Continuity at Known Transitions in Time Series

**Authors**: Hongxiao Jin
**Date**: 2026-09-14
**Paper ID**: [openalex:2609.15132](https://arxiv.org/abs/2609.15132)

## Summary

The paper introduces the Temporal Seam Score (S-score), a signed and robust diagnostic metric designed to evaluate temporal continuity at known transition points in long environmental records without requiring overlapping observation periods. By fitting a seam-blind model to account for trend, seasonality, and covariates, the S-score contrasts symmetric windows around the transition against matched reference contrasts within contributing segments. Simulations and an application to MODIS-to-Sentinel-3 vegetation records demonstrate its efficacy in auditing sensor and algorithm harmonization quality.

## Key Contributions

- Introduces the Temporal Seam Score (S-score), a robust, signed diagnostic metric to assess continuity at known temporal transitions without requiring temporal overlap.
- Demonstrates through simulations that the S-score magnitude (|S|) effectively reflects imposed discontinuities relative to residual variability under varying coefficients of variation.
- Applies the S-score to a MODIS-to-Sentinel-3 vegetation record across 500 sites, identifying 90 reliable sites with a median S of +0.217 and median |S| of 0.627, validating minimal systematic directional displacement.

## Key Concepts

- [[temporal-seam-score]]: A signed, robust metric for assessing continuity and quantifying discontinuities at known transition times in long time series.

## Archivist Review

Approved the core concept of the paper, the Temporal Seam Score, as a reusable diagnostic metric for time series harmonization and continuity assessment across observing systems. No open questions or datasets met the strict inclusion threshold.

### Approved Concepts
- Temporal Seam Score: It is the core diagnostic metric proposed in the paper for quantifying continuity at known temporal transitions in environmental records.

## Links

- [Abstract](https://arxiv.org/abs/2609.15132)
- [PDF](https://arxiv.org/pdf/2609.15132)

