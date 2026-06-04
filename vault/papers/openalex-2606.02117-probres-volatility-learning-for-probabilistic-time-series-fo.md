---
# CSL-compatible fields
title: "ProbRes: Volatility Learning for Probabilistic Time-Series Forecasting"
author:
  - literal: "Tingting Wang"
  - literal: "Yunyi Zhang"
  - literal: "Benyou Wang"
issued:
  date-parts:
    - [2026, 6, 1]
url: "https://arxiv.org/abs/2606.02117"

# Custom fields
paper_id: "2606.02117"
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
  - "probres"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-04T08:42:33Z"
created_at: "2026-06-04T08:42:33Z"
---

# ProbRes: Volatility Learning for Probabilistic Time-Series Forecasting

**Authors**: Tingting Wang, Yunyi Zhang, Benyou Wang
**Date**: 2026-06-01
**Paper ID**: [openalex:2606.02117](https://arxiv.org/abs/2606.02117)

## Summary

ProbRes is a post-hoc probabilistic calibration framework designed to enhance uncertainty quantification in time-series forecasting, particularly for heteroskedastic data. The method operates by using two distinct, architecture-agnostic modules to separately model the conditional mean and conditional volatility, followed by residual-based resampling during inference to generate predictive distributions. It demonstrates robustness against non-Gaussian error distributions and achieves improved interval calibration across various forecasting tasks.

## Key Contributions

- Introduces ProbRes, an architecture-agnostic post-hoc calibration module that explicitly decouples conditional mean and volatility modeling.
- Enables effective handling of heteroskedasticity and non-Gaussian innovations in both univariate and multivariate time-series forecasting.
- Demonstrates improved predictive distribution accuracy and calibration performance compared to standard approaches across synthetic and real-world benchmarks.

## Key Concepts

- [[probres]]: A post-hoc probabilistic calibration method that models conditional volatility dynamics to refine forecast distributions.

## Archivist Review

ProbRes is approved as a distinct post-hoc framework for decoupling conditional mean and volatility, providing a reusable approach for improving uncertainty quantification in existing forecasting models. Other candidates were rejected because they were either generic task descriptions or were already encapsulated by the ProbRes framework. No datasets or open questions were proposed, so none were approved.

### Approved Concepts
- ProbRes: It introduces a general, architecture-agnostic mechanism for post-hoc volatility calibration in probabilistic forecasting, addressing heteroskedasticity.

### Rejected Candidates
- [concept] Probabilistic Calibration Method (`probabilistic-calibration-method`) - generic: This is a generic term describing an entire field of research rather than a specific novel contribution of this paper.

## Links

- [Abstract](https://arxiv.org/abs/2606.02117)
- [PDF](https://arxiv.org/pdf/2606.02117)

