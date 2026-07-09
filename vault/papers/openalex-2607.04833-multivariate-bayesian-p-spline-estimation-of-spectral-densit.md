---
# CSL-compatible fields
title: "Multivariate Bayesian P-spline estimation of spectral density matrices, with application to LISA TDI noise"
author:
  - literal: "A. Vajpeyi"
  - literal: "R A Meyer"
  - literal: "Patricio Maturana-Russell"
  - literal: "Jianan Liu"
issued:
  date-parts:
    - [2026, 7, 6]
url: "https://arxiv.org/abs/2607.04833"

# Custom fields
paper_id: "2607.04833"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "bayesian-p-spline-spectral-density-estimation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-09T08:19:05Z"
created_at: "2026-07-09T08:19:05Z"
---

# Multivariate Bayesian P-spline estimation of spectral density matrices, with application to LISA TDI noise

**Authors**: A. Vajpeyi, R A Meyer, Patricio Maturana-Russell, Jianan Liu
**Date**: 2026-07-06
**Paper ID**: [openalex:2607.04833](https://arxiv.org/abs/2607.04833)

## Summary

This paper introduces a Bayesian P-spline approach for estimating the frequency-dependent cross-spectral density matrix of stationary multivariate time series. The method parameterizes the inverse spectral matrix using a frequency-varying Cholesky decomposition to maintain Hermitian positive definiteness, while applying penalised B-spline priors for smoothness. Inference is performed using a blocked Whittle likelihood with η-tempering and sampled via the No-U-Turn Sampler. Experimental results on synthetic VAR(2) benchmarks and simulated LISA TDI noise demonstrate the model's effectiveness in recovering cross-spectral structure in both symmetric and asymmetric noise environments.

## Key Contributions

- Introduced a Bayesian P-spline method using frequency-varying Cholesky decomposition to estimate multivariate cross-spectral density matrices while guaranteeing Hermitian positive definiteness.
- Implemented safe-Bayes η-tempering for stable posterior calibration with blocked, coarse-grained Whittle likelihood.
- Demonstrated superior recovery of cross-spectral structures in asymmetric noise configurations for LISA TDI data compared to AET-diagonal assumption benchmarks.

## Key Concepts

- [[bayesian-p-spline-spectral-density-estimation]]: A Bayesian P-spline framework for estimating multivariate spectral density matrices that uses frequency-varying Cholesky decomposition to maintain positive definiteness.

## Archivist Review

The paper contributes a specialized Bayesian framework for spectral density matrix estimation. I have approved the concept because it provides a principled way to maintain positive definiteness in multivariate spectral modeling, which is a reusable architectural idea. I rejected the dataset as it is a highly domain-specific simulated physics product rather than a general-purpose ML benchmark.

### Approved Concepts
- Bayesian P-spline Spectral Density Estimation: Introduces a robust Bayesian approach for multivariate spectral density estimation ensuring Hermitian positive definiteness via Cholesky decomposition.

### Rejected Candidates
- [dataset] LISA TDI noise data (`lisa-tdi-noise-data`) - low_impact: This is a synthetic simulated dataset specific to a highly niche physical application rather than a broadly reusable benchmark dataset.

## Links

- [Abstract](https://arxiv.org/abs/2607.04833)
- [PDF](https://arxiv.org/pdf/2607.04833)

