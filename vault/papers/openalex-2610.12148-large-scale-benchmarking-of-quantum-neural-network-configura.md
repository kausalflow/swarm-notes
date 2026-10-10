---
# CSL-compatible fields
title: "Large-Scale Benchmarking of Quantum Neural Network Configurations for Financial Time Series Forecasting"
author:
  - literal: "J WALLER"
  - literal: "Xing Liang"
  - literal: "Dimitrios Makris"
  - literal: "Rajagopal Nilavalan"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.12148"

# Custom fields
paper_id: "2610.12148"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
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
processed_at: "2026-10-10T10:51:55Z"
created_at: "2026-10-10T10:51:55Z"
---

# Large-Scale Benchmarking of Quantum Neural Network Configurations for Financial Time Series Forecasting

**Authors**: J WALLER, Xing Liang, Dimitrios Makris, Rajagopal Nilavalan
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.12148](https://arxiv.org/abs/2610.12148)

## Summary

This study presents a large-scale systematic evaluation of quantum neural network (QNN) component configurations for financial time series forecasting using the GBP/USD spot exchange rate. By performing a grid search across 1,368 configurations spanning encoding methods, ansatz designs, qubit counts, layer depths, and cost functions, the authors identify key architectural principles such as the critical importance of gate selection and circuit entanglement over raw parameter count. The optimal QNN achieves an R^2 score of 0.985, outperforming a classical BiLSTM baseline, while hardware execution on the IQM Emerald device highlights noise resilience bottlenecks caused by gate errors and decoherence.

## Key Contributions

- Conducted a large-scale systematic grid search evaluating 1,368 distinct quantum neural network (QNN) configurations for financial time series forecasting using the GBP/USD exchange rate dataset.
- Demonstrated that the best-performing QNN configuration achieves an R^2 score of 0.985, outperforming a classical BiLSTM baseline.
- Assessed real quantum hardware noise impact on the IQM Emerald device, showing that gate selection and circuit depth are primary determinants of hardware noise resilience.

## Limitations

Real quantum hardware deployment is heavily constrained by gate errors and decoherence on near-term devices.

## Archivist Review

Evaluated the paper on quantum neural network configurations for financial time series forecasting. No novel, reusable ML concepts or standalone datasets meet the stringent criteria, and the proposed open question is standard future work about extending evaluations to larger models.

### Rejected Candidates
- [open_question] Generalizing QNN Configurations to Advanced Architectures (`generalizing-qnn-configurations-to-advanced-architectures-and-complex-models`) - low_impact: The question asks for future validation across advanced quantum architectures rather than identifying a specific unresolved technical mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2610.12148)
- [PDF](https://arxiv.org/pdf/2610.12148)

