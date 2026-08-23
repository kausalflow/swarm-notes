---
# CSL-compatible fields
title: "GENIE: Generative Neural Inference for Epidemics"
author:
  - literal: "Laura M. Guzman-Rincon"
  - literal: "George R.E. Bradley"
  - literal: "Joel Kandiah"
  - literal: "Kyriakos Flouris"
  - literal: "Pietro Liò"
  - literal: "Paul Birrell"
  - literal: "Alexander E. Zarebski"
  - literal: "Daniela De Angelis"
issued:
  date-parts:
    - [2026, 8, 20]
url: "https://arxiv.org/abs/2608.20253"

# Custom fields
paper_id: "2608.20253"
paper_source: "openalex"
domain: "biology"
tags:
  - "forecasting"
  - "bayesian-inference"
  - "simulation"
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
processed_at: "2026-08-23T05:19:57Z"
created_at: "2026-08-23T05:19:57Z"
---

# GENIE: Generative Neural Inference for Epidemics

**Authors**: Laura M. Guzman-Rincon, George R.E. Bradley, Joel Kandiah, Kyriakos Flouris, Pietro Liò, Paul Birrell, Alexander E. Zarebski, Daniela De Angelis
**Date**: 2026-08-20
**Paper ID**: [openalex:2608.20253](https://arxiv.org/abs/2608.20253)

## Summary

The paper introduces GENIE, a spatio-temporal machine learning framework for high-resolution epidemic forecasting that uses amortized simulation-based inference to overcome the computational and calibration limits of traditional agent-based models. GENIE features a dual-module architecture consisting of a Local Infection Encoder for shared biological mechanisms and a Local Profile Encoder for location-specific transmission dynamics. Trained on agent-based model simulations, GENIE generates approximate posterior predictive samples of future epidemic trajectories and outperforms standard statistical and ML baselines in forecasting hospitalisation peaks.

## Key Contributions

- Introduces GENIE, a spatio-temporal machine learning framework combining a Local Infection Encoder and a Local Profile Encoder for high-resolution respiratory pathogen forecasting.
- Leverages agent-based model (ABM) simulations within an amortized simulation-based inference framework to generate samples from the approximate posterior predictive distribution of epidemic trajectories.
- Demonstrates superior performance against established statistical and machine learning baselines across metrics including the timing and magnitude of peak hospitalisations.

## Archivist Review

Applied strict vault selectivity: no standalone concepts or open questions met the high bar for universal reusability or non-duplication.

### Rejected Candidates
- [open_question] Diagnostics for Amortized Inference Failures (`diagnosing-out-of-distribution-failures-in-amortized-epidemic-inference`) - paper_local: A bit domain-specific to epidemiological simulation diagnostics and overlaps with general OOD detection questions.
- [open_question] Flexible Predictive Distributions in Epidemics (`non-parametric-predictive-distributions-for-epidemic-forecasting`) - not_novel: Too narrow to epidemic forecasting frameworks; general parametric vs non-parametric predictive distribution questions are already covered broadly in probabilistic forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2608.20253)
- [PDF](https://arxiv.org/pdf/2608.20253)

