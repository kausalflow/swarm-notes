---
# CSL-compatible fields
title: "Time-series forecasting with multiphoton quantum states and integrated photonics"
author:
  - literal: "Rosario Di Bartolo"
  - literal: "Simone Piacentini"
  - literal: "Francesco Ceccarelli"
  - literal: "Giacomo Corrielli"
  - literal: "Roberto Osellame"
  - literal: "Valeria Cimini"
  - literal: "Fabio Sciarrino"
issued:
  date-parts:
    - [2026, 4, 17]
url: "https://arxiv.org/abs/2512.02928"

# Custom fields
paper_id: "2512.02928"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "quantum-machine-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "quantum-reservoir-computing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-20T07:09:56Z"
created_at: "2026-04-20T07:09:56Z"
---

# Time-series forecasting with multiphoton quantum states and integrated photonics

**Authors**: Rosario Di Bartolo, Simone Piacentini, Francesco Ceccarelli, Giacomo Corrielli, Roberto Osellame, Valeria Cimini, Fabio Sciarrino
**Date**: 2026-04-17
**Paper ID**: [openalex:2512.02928](https://arxiv.org/abs/2512.02928)

## Summary

This paper introduces a quantum reservoir computing architecture implemented on a reconfigurable integrated photonic platform for time-series forecasting. The system encodes input signals into optical phases and utilizes multiphoton quantum states, where a final classical layer trained via linear regression maps output probabilities to predictions. The authors experimentally identify that photon indistinguishability acts as a critical resource, enhancing the reservoir's capacity to model higher-order nonlinearities through quantum interference.

## Key Contributions

- Demonstrates the use of a multiphoton-based quantum reservoir computing protocol for time-series forecasting tasks using a reconfigurable integrated photonic circuit.
- Provides experimental evidence that two-photon indistinguishable states significantly outperform distinguishable states in forecasting performance.
- Shows that quantum interference from indistinguishable photons enables the reservoir to approximate higher-order nonlinear functions more effectively under similar resource constraints.

## Open Questions & Future Work

- [[fisher-information-qrc-performance]]

## Key Concepts

- [[quantum-reservoir-computing]]: A reservoir computing framework leveraging reconfigurable integrated photonic circuits and multiphoton quantum states to process time-series data.

## Archivist Review

The paper demonstrates a hardware-specific implementation of reservoir computing using multiphoton quantum states. 'Quantum Reservoir Computing' is approved as a core paradigm shift in physical machine learning, and the Fisher information question is approved as it addresses the theoretical bottleneck for why quantum-interferometric states provide improved forecasting expressivity. No datasets were approved as none were cited as reusable benchmarks.

### Approved Concepts
- Quantum Reservoir Computing: This is the central computational paradigm explored, combining quantum interference with reservoir computing for signal processing.

### Approved Open Questions
- Fisher Information in QRC: Establishing a theoretical link between quantum-enhanced sensing metrics (Fisher information) and the performance of quantum machine learning models would provide a foundational basis for optimizing the design of such systems.

## Links

- [Abstract](https://arxiv.org/abs/2512.02928)
- [PDF](https://arxiv.org/pdf/2512.02928)

