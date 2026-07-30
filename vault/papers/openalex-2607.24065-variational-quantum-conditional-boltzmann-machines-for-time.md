---
# CSL-compatible fields
title: "Variational Quantum Conditional Boltzmann Machines for Time-Series Forecasting: Architectures, Symmetric Hyperparameter Evaluation, and a Nonlinear Benchmark"
author:
  - literal: "Gerhard Hellstern"
  - literal: "Danyal Maheshwari"
  - literal: "Martin Zaefferer"
  - literal: "Martin Braun"
  - literal: "Tanja Döhler"
issued:
  date-parts:
    - [2026, 7, 27]
url: "https://arxiv.org/abs/2607.24065"

# Custom fields
paper_id: "2607.24065"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "autoregressive"
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
processed_at: "2026-07-30T07:26:04Z"
created_at: "2026-07-30T07:26:04Z"
---

# Variational Quantum Conditional Boltzmann Machines for Time-Series Forecasting: Architectures, Symmetric Hyperparameter Evaluation, and a Nonlinear Benchmark

**Authors**: Gerhard Hellstern, Danyal Maheshwari, Martin Zaefferer, Martin Braun, Tanja Döhler
**Date**: 2026-07-27
**Paper ID**: [openalex:2607.24065](https://arxiv.org/abs/2607.24065)

## Summary

This paper introduces and evaluates four conditional energy-based time-series forecasting architectures spanning classical Gaussian-Bernoulli CRBMs, hybrid quantum-classical QCRBMs, full-register QQRBMs, and lag-feature QFeatureQRBMs. Using symmetric hyperparameter optimization across Gaussian-process financial data and the NARMA-10 nonlinear benchmark, the study finds no systematic evidence of a quantum advantage over classical baselines at the tested sample size. Iso-parameter comparisons further reinforce that classical CRBMs perform competitively or better than their quantum counterparts under matched budgets.

## Key Contributions

- Developed and evaluated four conditional energy-based forecasting architectures: classical Gaussian-Bernoulli CRBM, hybrid quantum-classical QCRBM, full-register QQRBM, and lag-feature QFeatureQRBM with complete derivations of conditional distributions and Contrastive-Divergence gradients.
- Enforced symmetric hyperparameter optimization with a thorough grid search across thirteen structured experiments for both classical and quantum-specific settings.
- Demonstrated across Gaussian-process financial datasets and the input-driven NARMA-10 nonlinear benchmark that quantum architectures show no systematic advantage over classical baselines at the available sample size.

## Limitations

Power analysis shows that at n = 12 only medium-to-large effects are detectable, meaning small quantum advantages cannot be completely excluded.

## Archivist Review

The submitted candidate open question is routine future work regarding dataset scope expansion and does not represent a standalone technical bottleneck or mechanism worth tracking in the vault. No concepts or datasets were provided or approved.

### Rejected Candidates
- [open_question] Dataset Scope and Nonlinear Characteristics (`dataset-scope-nonlinear-characteristics`) - low_impact: This is boilerplate future work suggesting the expansion of dataset scopes and testing on new systems, which is too generic.

## Links

- [Abstract](https://arxiv.org/abs/2607.24065)
- [PDF](https://arxiv.org/pdf/2607.24065)

