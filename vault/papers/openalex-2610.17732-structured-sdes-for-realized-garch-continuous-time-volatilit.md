---
# CSL-compatible fields
title: "Structured SDEs for Realized GARCH: Continuous-Time Volatility Modelling and Component-Level Analysis"
author:
  - literal: "Hongyu Yao"
  - literal: "Zhengyang Chi"
  - literal: "Junbin Gao"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.17732"

# Custom fields
paper_id: "2610.17732"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-16T09:24:00Z"
created_at: "2026-10-16T09:24:00Z"
---

# Structured SDEs for Realized GARCH: Continuous-Time Volatility Modelling and Component-Level Analysis

**Authors**: Hongyu Yao, Zhengyang Chi, Junbin Gao
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.17732](https://arxiv.org/abs/2610.17732)

## Summary

The paper introduces a structured continuous-time stochastic volatility model designed for one-day-ahead integrated-variance forecasting by incorporating a jointly evolving realized-measure state into latent variance dynamics with correlated Brownian innovations. Parameters are estimated using simulation-based predictive learning, and future integrated variance is obtained via Monte Carlo simulation. Evaluated across 17 equity indices, the model outperforms traditional volatility benchmarks such as GARCH, Realized GARCH, and HEAVY. Component-level ablation studies further reveal that feedback from realized measures is the primary driver of performance gains.

## Key Contributions

- Proposes a structured continuous-time stochastic volatility model combining a jointly evolving realized-measure state and latent variance dynamics for one-day-ahead integrated-variance forecasting.
- Employs simulation-based predictive learning for parameter estimation and Monte Carlo simulation for integrated variance forecasting.
- Demonstrates superior out-of-sample performance across 17 equity indices compared to classical baselines including GARCH, Realized GARCH, HAR, and HEAVY under QLIKE, MSE, and MAE metrics.
- Performs component-level ablation showing that realized-measure feedback provides substantial incremental value while return-linked Brownian dependence offers complementary gains.

## Archivist Review

The paper proposes a structured continuous-time stochastic volatility model integrating realized measures into SDE dynamics. Both candidate open questions are standard incremental extensions (testing on other asset classes and finer intraday updates) rather than major structural bottlenecks, so all candidates were rejected under strict filtering rules.

### Rejected Candidates
- [open_question] Direct Intraday High-Frequency Updates (`intraday-high-frequency-continuous-time-updates`) - low_impact: This is an incremental extension regarding intraday update integration rather than a foundational unresolved theoretical barrier.
- [open_question] Generalizing Volatility SDE Frameworks (`extended-asset-classes-horizon-forecasting`) - low_impact: This is boilerplate future work suggesting testing on other asset classes and longer horizons.

## Links

- [Abstract](https://arxiv.org/abs/2610.17732)
- [PDF](https://arxiv.org/pdf/2610.17732)

