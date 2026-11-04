---
# CSL-compatible fields
title: "HQNN-CL: Regime-Aware Hybrid Quantum Neural Network with Continual Learning for Financial Forecasting"
author:
  - literal: "Muhammad Atif Saeed"
  - literal: "Akhtar Jamıl"
  - literal: "Subhan Ullah"
  - literal: "Subhan Ullah"
issued:
  date-parts:
    - [2026, 11, 1]
url: "https://arxiv.org/abs/2611.02091"

# Custom fields
paper_id: "2611.02091"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "continual-learning"
  - "probabilistic-forecasting"
  - "quantum-machine-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "hqnn-cl"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-04T12:40:30Z"
created_at: "2026-11-04T12:40:30Z"
---

# HQNN-CL: Regime-Aware Hybrid Quantum Neural Network with Continual Learning for Financial Forecasting

**Authors**: Muhammad Atif Saeed, Akhtar Jamıl, Subhan Ullah, Subhan Ullah
**Date**: 2026-11-01
**Paper ID**: [openalex:2611.02091](https://arxiv.org/abs/2611.02091)

## Summary

Financial time-series forecasting suffers from non-stationary market dynamics, regime shifts, and catastrophic forgetting. This paper proposes HQNN-CL, a hybrid quantum-classical neural network integrating Gaussian Hidden Markov Models, BiLSTM encoding, adaptive-depth parameterized quantum circuits, and Elastic Weight Consolidation. Evaluated on four stock datasets against seven state-of-the-art baselines, HQNN-CL achieves superior or highly competitive accuracy, zero catastrophic forgetting, and well-calibrated probabilistic forecasts.

## Key Contributions

- Proposed HQNN-CL, a hybrid quantum-classical neural network integrating Gaussian HMM regime detection, BiLSTM temporal encoding, adaptive-depth parameterized quantum circuits, and continual learning for financial forecasting.
- Achieved superior or competitive performance on Microsoft, Systems Limited (RMSE = 3.0149), Teradata (RMSE = 0.8909), and Tata Consultancy Services stock datasets compared to seven state-of-the-art baselines.
- Demonstrated zero catastrophic forgetting (BWT = 0.0000) and consistent positive forward transfer across sequential learning tasks while producing well-calibrated probabilistic forecasts with 89.5% to 96.5% coverage.

## Limitations

Future work could explore scaling the quantum-classical architecture to broader macroeconomic portfolios and testing across more diverse high-frequency financial domains.

## Open Questions & Future Work

- [[noisy-quantum-hardware-financial-forecasting-evaluation]]

## Key Concepts

- [[hqnn-cl]]: A hybrid quantum-classical neural network with continual learning designed for regime-aware financial time-series forecasting.

## Archivist Review

Approved the core hybrid quantum continual learning framework concept and the NISQ hardware open question. Rejected local stock datasets as routine company-specific instances.

### Approved Concepts
- HQNN-CL: HQNN-CL serves as the core framework combining Gaussian HMM regime detection, BiLSTM encoding, adaptive-depth parameterized quantum circuits, and continual learning mechanisms to achieve robust financial forecasting without catastrophic forgetting.

### Approved Open Questions
- Evaluating Quantum Models on NISQ Hardware: Crucial for understanding the practical deployability and fault-tolerance requirements of quantum machine learning models in real-world noisy intermediate-scale quantum (NISQ) financial environments.

### Rejected Candidates
- [dataset] Microsoft (`microsoft`) - low_impact: Routine corporate stock dataset; not a canonical benchmark dataset note candidate.
- [dataset] Systems Limited (`systems-limited`) - low_impact: Routine company stock dataset.
- [dataset] Teradata (`teradata`) - low_impact: Routine corporate stock dataset.
- [dataset] Tata Consultancy Services (`tata-consultancy-services`) - low_impact: Routine corporate stock dataset.

## Links

- [Abstract](https://arxiv.org/abs/2611.02091)
- [PDF](https://arxiv.org/pdf/2611.02091)

