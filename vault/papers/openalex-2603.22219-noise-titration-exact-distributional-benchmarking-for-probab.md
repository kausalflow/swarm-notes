---
# CSL-compatible fields
title: "Noise Titration: Exact Distributional Benchmarking for Probabilistic Time Series Forecasting"
author:
  - literal: "Qilin Wang"
issued:
  date-parts:
    - [2026, 3, 23]
url: "https://arxiv.org/abs/2603.22219"

# Custom fields
paper_id: "2603.22219"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "state-space-model"
  - "evaluation"
  - "robustness"
  - "benchmark"
  - "distributional-forecasting"
architectures:
  - "state-space-model"
datasets:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:09:53Z"
created_at: "2026-03-27T14:09:53Z"
---

# Noise Titration: Exact Distributional Benchmarking for Probabilistic Time Series Forecasting

**Authors**: Qilin Wang
**Date**: 2026-03-23
**Paper ID**: [openalex:2603.22219](https://arxiv.org/abs/2603.22219)

## Summary

This paper proposes a fundamental shift in probabilistic time series forecasting evaluation from passive sequence matching to interventionist, exact-statistical benchmarking using "Noise Titration." This method involves injecting calibrated Gaussian noise into known dynamical systems, turning forecasting into an exact distributional inference task solvable via explicit negative log-likelihoods. To facilitate this, the authors extend the Fern architecture into a probabilistic model that efficiently parameterizes the Symmetric Positive Definite (SPD) cone for accurate covariance output. Evaluations reveal that large sequence-matching models fail under noise and non-stationarity, whereas the proposed Fern architecture successfully maintains structural fidelity and calibration by capturing the system's invariant measure.

## Key Contributions

- Introduced "Noise Titration," a novel, interventionist benchmarking paradigm for probabilistic time series forecasting that uses mathematically explicit noise injection to convert evaluation into an exact distributional inference task.
- Developed an extension to the Fern architecture that natively parameterizes the Symmetric Positive Definite (SPD) cone to output calibrated joint covariance structures efficiently.
- Demonstrated that current state-of-the-art zero-shot foundation models fail systematically under non-stationary regime shifts and noise when evaluated using exact distributional tests.
- Showcased that the proposed Fern model maintains structural fidelity and statistical calibration by explicitly capturing the invariant measure and multivariate geometry of the underlying dynamics.

## Limitations

The framework relies on the availability and fidelity of known chaotic or stochastic dynamical systems for noise titration, which may limit direct applicability to purely empirical, unknown real-world processes.

## Open Questions & Future Work

- [[extending-noise-titration-beyond-gaussian]]

## Key Concepts

- [Noise Titration Benchmarking](../concepts/noise-titration-benchmarking.md): A rigorous, interventionist benchmarking methodology for probabilistic time series forecasting that introduces calibrated Gaussian noise into known dynamical systems to create an exact distributional inference task.
- [Fern Architecture Extension](../concepts/fern-architecture-extension.md): An extension of the Fern architecture to a probabilistic generative model capable of natively parameterizing the Symmetric Positive Definite (SPD) cone for outputting calibrated joint covariance structures.

## Limitations

The framework relies on the availability and fidelity of known chaotic or stochastic dynamical systems for noise titration, which may limit direct applicability to purely empirical, unknown real-world processes.

## Links

- [Abstract](https://arxiv.org/abs/2603.22219)
- [PDF](https://arxiv.org/pdf/2603.22219)

