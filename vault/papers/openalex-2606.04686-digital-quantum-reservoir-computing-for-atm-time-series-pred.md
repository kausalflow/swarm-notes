---
# CSL-compatible fields
title: "Digital Quantum Reservoir Computing for ATM Time Series Prediction"
author:
  - literal: "Chiara Vercellino"
  - literal: "Giacomo Vitali"
  - literal: "Valeria Zaffaroni"
  - literal: "Francesca Cibrario"
  - literal: "Emanuele Dri"
  - literal: "Paolo Viviani"
  - literal: "Olivier Terzo"
  - literal: "Davide Corbelletto"
issued:
  date-parts:
    - [2026, 6, 3]
url: "https://arxiv.org/abs/2606.04686"

# Custom fields
paper_id: "2606.04686"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "quantum-computing"
architectures:
  []
datasets:
  []
concept_slugs:
  - "digital-quantum-reservoir-computing-qrc"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-06T07:39:38Z"
created_at: "2026-06-06T07:39:38Z"
---

# Digital Quantum Reservoir Computing for ATM Time Series Prediction

**Authors**: Chiara Vercellino, Giacomo Vitali, Valeria Zaffaroni, Francesca Cibrario, Emanuele Dri, Paolo Viviani, Olivier Terzo, Davide Corbelletto
**Date**: 2026-06-03
**Paper ID**: [openalex:2606.04686](https://arxiv.org/abs/2606.04686)

## Summary

This paper explores the utility of digital quantum reservoir computing (QRC) for financial time series forecasting, specifically predicting cash demand for automated teller machines. The authors implement a four-qubit reservoir using parameterized circuits, with temporal information encoded via rotation angles and a classical Ridge-regression readout. The framework is validated against classical benchmarks, revealing that while QRC models do not surpass Prophet in conventional error metrics, they show promise in capturing complex temporal dependencies as measured by Dynamic Time Warping. The study provides a comprehensive performance analysis using both quantum simulators and real IQM Spark hardware.

## Key Contributions

- Introduces a digital Quantum Reservoir Computing (QRC) framework for multi-step ATM cash demand forecasting.
- Systematically evaluates QRC performance across noiseless simulation, noise-aware emulation, and real IQM Spark quantum hardware.
- Demonstrates that while QRC models underperform classical baselines like Prophet on MAE/NMSE, they exhibit competitive performance on Dynamic Time Warping (DTW) metrics, capturing temporal structure effectively.

## Open Questions & Future Work

- [[noise-hardware-dependency-in-qrc]]

## Key Concepts

- [[digital-quantum-reservoir-computing-qrc]]: A framework for time series forecasting utilizing parametrized quantum circuits as reservoirs on near-term quantum devices.

## Archivist Review

I approved the core framework concept and the critical open question regarding hardware noise in NISQ-based reservoir computing. I rejected no candidates because the initial submission was already highly selective and well-scoped.

### Approved Concepts
- Digital Quantum Reservoir Computing (QRC): This represents the central contribution: using parametrized quantum circuits as high-dimensional reservoirs for time-series memory.

### Approved Open Questions
- Hardware noise influence on QRC: This is a fundamental bottleneck for deploying QRC on NISQ hardware, as it highlights a potential conflict between exploiting device-specific properties for performance and maintaining cross-platform model generalization.

## Links

- [Abstract](https://arxiv.org/abs/2606.04686)
- [PDF](https://arxiv.org/pdf/2606.04686)

