---
# CSL-compatible fields
title: "QLIF-CAST: Quantum Leaky-Integrate-and-Fire for Time-Series Weather Forecasting"
author:
  - literal: "Alberto Marchisio"
  - literal: "Aayan Ebrahim"
  - literal: "Nouhaila Innan"
  - literal: "Muhammad Kashif"
  - literal: "Muhammad Shafique"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2605.18333"

# Custom fields
paper_id: "2605.18333"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "spiking-neural-network"
  - "quantum-computing"
  - "hybrid-quantum-classical"
  - "recurrent-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "quantum-leaky-integrate-and-fire-qlif"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:27:12Z"
created_at: "2026-05-21T08:27:12Z"
---

# QLIF-CAST: Quantum Leaky-Integrate-and-Fire for Time-Series Weather Forecasting

**Authors**: Alberto Marchisio, Aayan Ebrahim, Nouhaila Innan, Muhammad Kashif, Muhammad Shafique
**Date**: 2026-05-18
**Paper ID**: [openalex:2605.18333](https://arxiv.org/abs/2605.18333)

## Summary

This paper presents QLIF-CAST, a hybrid quantum-classical architecture that utilizes Quantum Leaky-Integrate-and-Fire (QLIF) neurons for multivariate time-series forecasting. By encoding neuronal states as quantum superpositions and leveraging T1 relaxation decay, the model effectively performs continuous-valued regression. Experiments show the model outperforms classical LIF baselines in prediction accuracy and significantly accelerates convergence compared to existing quantum recurrent architectures. Hardware execution on an IBM QPU further confirms the feasibility and robustness of the proposed quantum neuronal dynamics.

## Key Contributions

- Introduces QLIF-CAST, a hybrid quantum-classical architecture that adapts Quantum Leaky-Integrate-and-Fire neurons for continuous-valued multivariate time-series forecasting.
- Demonstrates that QLIF-CAST achieves a 15.4% reduction in MSE and 4.4% in MAE compared to parameter-matched classical LIF baselines on multivariate weather data.
- Reports up to 94% faster convergence during training compared to QLSTM and QNN models on air quality and wind speed benchmarks.
- Validates reliable circuit execution on IBM Marrakesh hardware with only 1.2% deviation from simulation.

## Open Questions & Future Work

- [[end-to-end-physical-qpu-training]]

## Key Concepts

- [[quantum-leaky-integrate-and-fire-qlif]]: A spiking neural network model that encodes neuronal excitation states as single-qubit quantum superpositions utilizing T1 relaxation decay for temporal dynamics.

## Archivist Review

The paper is approved for its novel adaptation of QLIF spiking dynamics into a quantum-classical hybrid framework for continuous-valued forecasting. I approved the QLIF concept as it provides a clear, reusable mechanism for temporal modeling in quantum systems. The open question regarding end-to-end physical QPU training was approved as it represents a fundamental barrier to scaling quantum machine learning in practical time-series applications. I rejected the second open question as it was too specific to the proposed architecture.

### Approved Concepts
- Quantum Leaky-Integrate-and-Fire (QLIF): It serves as the core methodological innovation enabling quantum-enhanced continuous-valued time-series prediction by encoding states as superpositions with relaxation-based decay.

### Approved Open Questions
- End-to-end Physical QPU Training: Current reliance on classical simulators limits the empirical validation of quantum neural network scalability and real-world performance benefits.

### Rejected Candidates
- [open_question] Hybrid QLIF-VSTM Architectures (`qlif-vstm-architectures`) - low_impact: This is a highly specific, speculative architectural combination rather than a foundational research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2605.18333)
- [PDF](https://arxiv.org/pdf/2605.18333)

