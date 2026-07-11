---
# CSL-compatible fields
title: "Nowcasting PM2.5 in Beijing Using Synchronous Covariates and Lagged Features: Model Comparison and Variable Selection Stability"
author:
  - literal: "Yusheng Wang"
  - literal: "Ruiyan Du"
issued:
  date-parts:
    - [2026, 7, 8]
url: "https://arxiv.org/abs/2607.07279"

# Custom fields
paper_id: "2607.07279"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "ml-assisted-forecasting"
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
processed_at: "2026-07-11T07:06:26Z"
created_at: "2026-07-11T07:06:26Z"
---

# Nowcasting PM2.5 in Beijing Using Synchronous Covariates and Lagged Features: Model Comparison and Variable Selection Stability

**Authors**: Yusheng Wang, Ruiyan Du
**Date**: 2026-07-08
**Paper ID**: [openalex:2607.07279](https://arxiv.org/abs/2607.07279)

## Summary

This study investigates the nowcasting of hourly PM2.5 concentrations in Beijing by comparing regularized linear regression techniques with deep learning architectures like MLP and LSTM. Using four years of multi-station data, the research frames the task as nowcasting by integrating synchronous co-pollutant measurements alongside lagged PM2.5 terms. Results indicate that the MLP model significantly outperforms linear baselines, while variable stability analysis underscores the importance of specific co-pollutants and temporal lags for robust predictive performance.

## Key Contributions

- Evaluates regularized regression and deep learning models for nowcasting hourly PM2.5 in Beijing, identifying MLP as the superior performer (RMSE 13.651).
- Demonstrates that an MLP model achieves a 13% RMSE reduction compared to baseline regularized regression methods.
- Identifies CO, NO2, PM10, and first-order PM2.5 lags as the robust core set of variables for PM2.5 estimation across monitoring stations.

## Open Questions & Future Work

- [[gpu-accelerated-multi-station-sequence-modeling]]

## Archivist Review

The study provides an empirical comparison of models for air-quality nowcasting but does not introduce new concepts or widely applicable methods that transcend local application. The open question regarding computational limitations in multi-station sequence modeling is approved as it addresses a recurring bottleneck in environmental time-series research. All other candidates were rejected as either generic statistical practices or specific local data collection.

### Approved Open Questions
- GPU-accelerated multi-station sequence modeling: The study highlights that computational constraints prevented deeper sequence models (LSTM) from being effectively trained and evaluated against simpler architectures in air quality nowcasting. Overcoming this is essential for realizing the potential of more sophisticated temporal dynamics.

### Rejected Candidates
- [concept] Variable selection stability analysis (`variable-selection-stability-analysis`) - generic: Variable selection stability is a standard statistical technique rather than a novel or highly specialized forecasting concept.
- [dataset] Nowcasting PM2.5 in Beijing (`nowcasting-pm2-5-in-beijing`) - paper_local: The dataset is not a standalone benchmark or broadly accessible resource but a specific collection of local hourly observations.

## Links

- [Abstract](https://arxiv.org/abs/2607.07279)
- [PDF](https://arxiv.org/pdf/2607.07279)

