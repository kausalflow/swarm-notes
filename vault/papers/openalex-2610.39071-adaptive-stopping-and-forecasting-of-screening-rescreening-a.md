---
# CSL-compatible fields
title: "Adaptive stopping and forecasting of screening, rescreening and randomization in multicentre clinical trials"
author:
  - literal: "Volodymyr Anisimov"
  - literal: "Thomas Henderson"
issued:
  date-parts:
    - [2026, 10, 29]
url: "https://arxiv.org/abs/2610.39071"

# Custom fields
paper_id: "2610.39071"
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
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-01T11:33:33Z"
created_at: "2026-11-01T11:33:33Z"
---

# Adaptive stopping and forecasting of screening, rescreening and randomization in multicentre clinical trials

**Authors**: Volodymyr Anisimov, Thomas Henderson
**Date**: 2026-10-29
**Paper ID**: [openalex:2610.39071](https://arxiv.org/abs/2610.39071)

## Summary

This paper presents a novel statistical framework for joint modelling screening and randomisation in multicentre clinical trials to determine adaptive stopping times for patient admissions. By representing the screening and randomisation pathway as a multistage process with stage-specific durations and transition probabilities, the framework predicts the final number of randomised patients from the current pipeline. This enables timely stopping of new screening admissions to avoid over-enrolment while ensuring target sample sizes are achieved with high probability.

## Key Contributions

- Proposes a statistical framework for joint modelling screening and randomisation in multicentre clinical trials to determine adaptive stopping times.
- Models the screening and randomisation pathway as a multistage process with stage-specific durations and transition probabilities estimated from trial data.
- Incorporates scheduled site initiations and closures via evolving stochastic processes to support global, regional, and country-level forecasts.
- Demonstrates through simulations that the approach substantially reduces over-enrolment while maintaining high target sample size achievement probabilities.

## Archivist Review

Applied rigorous standards to reject paper-internal clinical trial trial-management extensions as too domain-specific and low-impact for permanent retention in the ML vault.

### Rejected Candidates
- [open_question] Priors for Screening Parameters (`priors-for-screening-probabilities-and-durations`) - low_impact: Paper-specific future work proposing Bayesian priors for clinical trial screening parameters without broad methodological novelty across time series modeling.

## Links

- [Abstract](https://arxiv.org/abs/2610.39071)
- [PDF](https://arxiv.org/pdf/2610.39071)

