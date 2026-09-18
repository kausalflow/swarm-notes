---
# CSL-compatible fields
title: "Conditionally linear, matrix normal state space models"
author:
  - literal: "Drew Creal"
  - literal: "Matheus Medeiros"
  - literal: "Rodrigo Sarlo"
issued:
  date-parts:
    - [2026, 9, 16]
url: "https://arxiv.org/abs/2609.18734"

# Custom fields
paper_id: "2609.18734"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "state-space-model"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-18T09:17:52Z"
created_at: "2026-09-18T09:17:52Z"
---

# Conditionally linear, matrix normal state space models

**Authors**: Drew Creal, Matheus Medeiros, Rodrigo Sarlo
**Date**: 2026-09-16
**Paper ID**: [openalex:2609.18734](https://arxiv.org/abs/2609.18734)

## Summary

This paper introduces a class of linear state space models for matrix-valued time series where the latent state follows a matrix normal process. The authors derive matrix-variate extensions of the Kalman filter, log-likelihood, and smoother, alongside Bayesian posterior sampling algorithms. Applied to high-dimensional U.S. macroeconomic time series across 50 states, the framework efficiently handles mixed-frequency data, heteroskedasticity, and outliers using a parsimonious latent factor structure.

## Key Contributions

- We develop a class of linear state space models for matrix-valued time series data where the state is a latent matrix normal process.
- We derive matrix versions of the Kalman filter, log-likelihood, and smoother enabling exact estimation of the latent state matrix and model parameters.
- We provide Bayesian inference algorithms to sample from the joint posterior distribution of latent state matrices conditional on observed data and parameters.
- We apply the framework to a large panel of U.S. macroeconomic time series across 50 states, demonstrating that a small number of latent factors efficiently captures joint dynamics.

## Archivist Review

The paper presents a matrix-normal state space model and extensions of Kalman filtering for matrix-valued time series. The single proposed open question is generic future work regarding omitted algorithms and does not meet the high bar for permanent vault storage. Therefore, no items are approved.

### Rejected Candidates
- [open_question] Additional Matrix State Space Algorithms (`matrix-state-space-additional-algorithms`) - weak_evidence: Boilerplate future work about omitting additional algorithms due to space constraints without detailing a specific unresolved algorithmic bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.18734)
- [PDF](https://arxiv.org/pdf/2609.18734)

