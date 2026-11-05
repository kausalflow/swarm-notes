---
# CSL-compatible fields
title: "Evaluating Uncertainty Calibration in Probabilistic Time Series Foundation Models"
author:
  - literal: "Thomas Decker"
  - literal: "Volker Tresp"
issued:
  date-parts:
    - [2026, 11, 2]
url: "https://arxiv.org/abs/2611.03592"

# Custom fields
paper_id: "2611.03592"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-05T12:51:24Z"
created_at: "2026-11-05T12:51:24Z"
---

# Evaluating Uncertainty Calibration in Probabilistic Time Series Foundation Models

**Authors**: Thomas Decker, Volker Tresp
**Date**: 2026-11-02
**Paper ID**: [openalex:2611.03592](https://arxiv.org/abs/2611.03592)

## Summary

This paper presents a methodological and empirical study of uncertainty calibration in probabilistic time series foundation models (TSFMs). The authors introduce a taxonomy of uncertainty representation and a fine-grained evaluation framework for multi-horizon forecasting that covers pooled, horizon-wise, and conditional calibration. Through extensive empirical evaluation, they uncover systematic miscalibration patterns in popular TSFMs that standard metrics frequently miss and analyze the effectiveness of various post-hoc recalibration techniques.

## Key Contributions

- Introduces a taxonomy of how time series foundation models represent predictive uncertainty.
- Develops a fine-grained evaluation framework for probabilistic calibration in multi-horizon forecasting distinguishing pooled, horizon-wise, and conditional notions.
- Conducts a comprehensive empirical evaluation of popular time series foundation models across diverse datasets, revealing systematic miscalibration patterns.
- Analyzes post-hoc recalibration methods to characterize which forms of calibration they improve and which persist.

## Open Questions & Future Work

- [[multivariate-and-temporal-forecast-calibration]]

## Archivist Review

Following the strict scarcity policy and review criteria, no standalone concepts or datasets were approved as they represent evaluation-focused frameworks rather than reusable model architectures or critical named datasets. One open question on multivariate and temporal forecast calibration was approved as it addresses a fundamental unresolved bottleneck in probabilistic time series foundation models.

### Approved Open Questions
- Multivariate and Temporal Forecast Calibration: Important for advancing trustworthy forecasting in high-stakes domains by moving beyond marginal marginal-coverage metrics toward multivariate and temporally-coherent calibration.

### Rejected Candidates
- [open_question] Multivariate and Temporal Forecast Calibration (`multivariate-and-temporal-forecast-calibration`) - paper_local: 1

## Links

- [Abstract](https://arxiv.org/abs/2611.03592)
- [PDF](https://arxiv.org/pdf/2611.03592)

