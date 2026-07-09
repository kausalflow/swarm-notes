---
# CSL-compatible fields
title: "Enhancing data completeness in time series: Imputation strategies for missing data using significant periodically correlated components"
author:
  - literal: "Asmaa Ahmad"
  - literal: "Eric J. Rose"
  - literal: "Michael M. Roy"
  - literal: "Edward Valachovic"
issued:
  date-parts:
    - [2026, 7, 6]
url: "https://arxiv.org/abs/2505.02008"

# Custom fields
paper_id: "2505.02008"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "imputation"
  - "seasonality"
architectures:
  []
datasets:
  []
concept_slugs:
  - "variable-bandpass-periodic-block-bootstrap-vbpbb"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-09T08:18:03Z"
created_at: "2026-07-09T08:18:03Z"
---

# Enhancing data completeness in time series: Imputation strategies for missing data using significant periodically correlated components

**Authors**: Asmaa Ahmad, Eric J. Rose, Michael M. Roy, Edward Valachovic
**Date**: 2026-07-06
**Paper ID**: [openalex:2505.02008](https://arxiv.org/abs/2505.02008)

## Summary

This paper addresses the challenge of bias in time series imputation when temporal dependence is lost. The authors propose a framework that combines the Variable Bandpass Periodic Block Bootstrap (VBPBB) with Amelia II multiple imputation by leveraging significant periodic components as auxiliary variables. Evaluation on simulated temperature data under a MAR mechanism demonstrates that this approach significantly improves the reconstruction of seasonal patterns and reduces imputation error.

## Key Contributions

- Introduced a framework that enhances multiple imputation by incorporating VBPBB-derived significant periodic components as auxiliary covariates.
- Demonstrated a ~55% reduction in RMSE and MAE for seasonal temperature data compared to standard Amelia II imputation.
- Validated the effectiveness of preserving periodic dependence under the Missing at Random (MAR) mechanism.

## Key Concepts

- [[variable-bandpass-periodic-block-bootstrap-vbpbb]]: A bootstrapping technique that generates auxiliary periodic covariates to preserve seasonal temporal dependence during time series imputation.

## Archivist Review

I approved the VBPBB concept as it represents a specific, reusable methodological framework for incorporating seasonal temporal dependencies into general imputation models. No other concepts or open questions were sufficiently novel or central to the field at large.

### Approved Concepts
- Variable Bandpass Periodic Block Bootstrap (VBPBB): The VBPBB is the primary methodological innovation, serving as a feature engineering strategy to capture periodic dependencies for improved missing data imputation.

## Links

- [Abstract](https://arxiv.org/abs/2505.02008)
- [PDF](https://arxiv.org/pdf/2505.02008)

