---
# CSL-compatible fields
title: "Enhancing Irregular Time Series Forecasting with Continuous-Time Modeling Framework"
author:
  - literal: "Tianen Shen"
  - literal: "Zhengyu Li"
  - literal: "Yutong Li"
  - literal: "Xiangfei Qiu"
  - literal: "Xingjian Wu"
  - literal: "Bin Yang"
  - literal: "Jilin Hu"
issued:
  date-parts:
    - [2026, 7, 30]
url: "https://arxiv.org/abs/2607.28035"

# Custom fields
paper_id: "2607.28035"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "transformer"
  - "continuous-time-modeling"
  - "flow-matching"
  - "irregular-time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "wrapflow"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-02T07:26:30Z"
created_at: "2026-08-02T07:26:30Z"
---

# Enhancing Irregular Time Series Forecasting with Continuous-Time Modeling Framework

**Authors**: Tianen Shen, Zhengyu Li, Yutong Li, Xiangfei Qiu, Xingjian Wu, Bin Yang, Jilin Hu
**Date**: 2026-07-30
**Paper ID**: [openalex:2607.28035](https://arxiv.org/abs/2607.28035)

## Summary

WrapFlow is a continuous-time modeling framework for irregular multivariate time series forecasting that addresses the limitations of discretization and ODE-based numerical solvers. It introduces Continuous-Time Tokenization with gap-aware tokens to encode raw asynchronous events for standard Transformer backbones, alongside a simulation-free training paradigm for Residual Flow Matching that avoids numerical solver simulation during training. Extensive experiments show that WrapFlow achieves state-of-the-art performance on real-world irregular time series benchmarks.

## Key Contributions

- Proposes WrapFlow, a continuous-time modeling framework for irregular multivariate time series forecasting that avoids discretization and expensive numerical ODE solvers.
- Introduces Continuous-Time Tokenization to encode raw observation events and model long unobserved intervals using gap-aware tokens for standard Transformer backbones.
- Develops a simulation-free training paradigm for Residual Flow Matching to learn conditional residual vector fields around base predictions without solver simulation.
- Achieves state-of-the-art performance across multiple real-world datasets for irregular time series forecasting.

## Key Concepts

- [[wrapflow]]: A continuous-time modeling framework for irregular time series forecasting featuring continuous-time tokenization and simulation-free residual flow matching.

## Archivist Review

Approved the overarching framework 'WrapFlow' as a reusable and distinct contribution for irregular time series forecasting combining continuous-time tokenization with simulation-free residual flow matching. No datasets or open questions met the strict standalone scarcity thresholds.

### Approved Concepts
- WrapFlow: WrapFlow is the core continuous-time modeling framework proposed by the paper for irregular time series forecasting, combining continuous-time tokenization and a simulation-free residual flow matching paradigm.

## Links

- [Abstract](https://arxiv.org/abs/2607.28035)
- [PDF](https://arxiv.org/pdf/2607.28035)

