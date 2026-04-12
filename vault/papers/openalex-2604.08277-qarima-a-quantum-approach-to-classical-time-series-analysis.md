---
# CSL-compatible fields
title: "QARIMA: A Quantum Approach To Classical Time Series Analysis"
author:
  - literal: "Nishikanta Mohanty"
  - literal: "Bikash K. Behera"
  - literal: "Badshah Mukherjee"
  - literal: "Pravat Dash"
issued:
  date-parts:
    - [2026, 4, 9]
url: "https://arxiv.org/abs/2604.08277"

# Custom fields
paper_id: "2604.08277"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "qarima"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-12T06:18:50Z"
created_at: "2026-04-12T06:18:50Z"
---

# QARIMA: A Quantum Approach To Classical Time Series Analysis

**Authors**: Nishikanta Mohanty, Bikash K. Behera, Badshah Mukherjee, Pravat Dash
**Date**: 2026-04-09
**Paper ID**: [openalex:2604.08277](https://arxiv.org/abs/2604.08277)

## Summary

QARIMA is a quantum-inspired approach to time-series analysis that incorporates quantum-assisted mechanisms for order discovery and parameter estimation within the classical ARIMA framework. The methodology employs swap-test-driven quantum autocorrelation and partial autocorrelation for lag identification, followed by fixed-configuration variational quantum circuits for coefficient estimation. By combining quantum weak-lag refinement with classical information-criterion parsimony, the approach effectively reduces meta-optimization overhead while achieving improved predictive accuracy on industrial and environmental benchmarks.

## Key Contributions

- Introduces QARIMA, a framework integrating quantum autocorrelation (QACF) and partial autocorrelation (QPACF) for differencing and lag identification.
- Utilizes fixed-configuration variational quantum circuits (VQCs) for AR and MA parameter estimation to avoid hyperparameter leakage.
- Demonstrates superior performance over automated classical ARIMA baselines across environmental and industrial datasets using Diebold-Mariano tests.

## Open Questions & Future Work

- [[nisq-hardware-stability-in-hybrid-forecasting]]

## Key Concepts

- [[qarima]]: A quantum-inspired ARIMA methodology utilizing variational quantum circuits for lag discovery, parameter estimation, and weak-lag refinement in time-series forecasting.

## Archivist Review

I approved QARIMA as a conceptual framework for hybrid quantum-statistical forecasting. I approved a broad open question regarding NISQ hardware stability, generalizing the specific hardware concerns raised in the paper. I rejected the individual VQC modules (QACF, QPACF, VQC-AR, VQC-MA) as they are sub-components of the QARIMA architecture rather than standalone reusable innovations.

### Approved Concepts
- QARIMA: Integrates quantum-assisted mechanisms into the classical ARIMA framework for structure discovery and parameter estimation, offering a template for hybridizing classical statistical models with variational quantum circuits.

### Approved Open Questions
- NISQ Hardware Stability in Hybrid Forecasting: Practical viability of quantum-enhanced forecasting is contingent on moving beyond simulation-based assumptions to address hardware-level noise and architecture limitations.

### Rejected Candidates
- [concept] Quantum Autocorrelation (QACF) (`qacf`) - subcomponent_of_broader_mechanism: This is a specific sub-primitive of the broader QARIMA framework.
- [concept] Quantum Partial Autocorrelation (QPACF) (`qpacf`) - subcomponent_of_broader_mechanism: This is a specific sub-primitive of the broader QARIMA framework.
- [concept] VQC-AR (`vqc-ar`) - subcomponent_of_broader_mechanism: This is a specific sub-primitive/implementation detail of the QARIMA parameter estimation.
- [concept] VQC-MA (`vqc-ma`) - subcomponent_of_broader_mechanism: This is a specific sub-primitive/implementation detail of the QARIMA parameter estimation.

## Links

- [Abstract](https://arxiv.org/abs/2604.08277)
- [PDF](https://arxiv.org/pdf/2604.08277)

