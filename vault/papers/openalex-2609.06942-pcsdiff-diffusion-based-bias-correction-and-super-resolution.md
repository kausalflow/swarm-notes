---
# CSL-compatible fields
title: "PCSDiff: Diffusion-Based Bias Correction and Super Resolution Toward Practical Operational Medium-Term Precipitation Forecast"
author:
  - literal: "Yuze Sun"
  - literal: "Shiyi Wang"
  - literal: "Jiancheng Pan"
  - literal: "Die Wang"
  - literal: "Andreas F. Prein"
  - literal: "Wentao Luo"
  - literal: "Linhan Jiang"
  - literal: "Jie Wu"
  - literal: "Quan Zhang"
  - literal: "Xiaomeng Huang"
issued:
  date-parts:
    - [2026, 9, 7]
url: "https://arxiv.org/abs/2609.06942"

# Custom fields
paper_id: "2609.06942"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "diffusion-model"
  - "super-resolution"
  - "bias-correction"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-10T09:17:11Z"
created_at: "2026-09-10T09:17:11Z"
---

# PCSDiff: Diffusion-Based Bias Correction and Super Resolution Toward Practical Operational Medium-Term Precipitation Forecast

**Authors**: Yuze Sun, Shiyi Wang, Jiancheng Pan, Die Wang, Andreas F. Prein, Wentao Luo, Linhan Jiang, Jie Wu, Quan Zhang, Xiaomeng Huang
**Date**: 2026-09-07
**Paper ID**: [openalex:2609.06942](https://arxiv.org/abs/2609.06942)

## Summary

Medium-range precipitation forecasts suffer from persistent systematic biases, error accumulation across lead times, and coarse resolution. To address these limitations, this paper introduces PCSDiff, a cascaded task-decoupled diffusion framework designed for 10-day precipitation bias correction and downscaling. The approach combines a Precipitation Intensity-aware Multi-branch Decoder (PIMD) for dynamic error mitigation with a two-phase conditional diffusion super-resolution module to restore realistic rainfall structures. Evaluations against observational data over China demonstrate substantial improvements in RMSE and ACC over raw ECMWF forecasts and existing deep-learning baselines, while enabling low-latency operational deployment.

## Key Contributions

- PCSDiff introduces a cascaded task-decoupled diffusion framework for 10-day precipitation bias correction and super-resolution.
- Integrates a Precipitation Intensity-aware Multi-branch Decoder (PIMD) to mitigate dynamic multi-day error drifts using synoptic-temporal features.
- Employs a two-phase conditional diffusion super-resolution module to restore fine-scale precipitation patterns without over-smoothing.
- Cuts RMSE by 16.1% and lifts ACC by 13.9% relative to raw ECMWF forecasts at 3-10-day lead times over China, while supporting low-latency rolling inference for operational deployment.

## Archivist Review

The paper presents a specialized framework for precipitation bias correction and super-resolution (PCSDiff). The proposed future work open question bundles multiple standard directions (physical constraints, multi-variable extension, and model compression) and is therefore rejected as low-impact boilerplate. No permanent vault notes are approved.

### Rejected Candidates
- [open_question] Physics-Constrained Multivariable Diffusion Forecasting (`physics-constrained-multivariable-diffusion-forecasting`) - low_impact: Boilerplate future work combining multiple standard directions (physical constraints, multi-variable extension, lightweight variants) without addressing a single distinct open vault question.

## Links

- [Abstract](https://arxiv.org/abs/2609.06942)
- [PDF](https://arxiv.org/pdf/2609.06942)

