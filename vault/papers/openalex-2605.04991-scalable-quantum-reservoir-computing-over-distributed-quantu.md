---
# CSL-compatible fields
title: "Scalable Quantum Reservoir Computing over Distributed Quantum Architectures"
author:
  - literal: "Ioannis Liliopoulos"
  - literal: "Georgios D. Varsamis"
  - literal: "Konstantinos Rallis"
  - literal: "Evangelos Tsipas"
  - literal: "Ioannis G. Karafyllidis"
  - literal: "Georgios Ch. Sirakoulis"
  - literal: "Panagiotis Dimitrakis"
issued:
  date-parts:
    - [2026, 5, 6]
url: "https://arxiv.org/abs/2605.04991"

# Custom fields
paper_id: "2605.04991"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "quantum-reservoir-computing"
  - "qrc"
  - "recurrent-neural-network"
  - "distributed-training"
architectures:
  []
datasets:
  []
concept_slugs:
  - "distributed-quantum-reservoir-computing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-09T07:02:29Z"
created_at: "2026-05-09T07:02:29Z"
---

# Scalable Quantum Reservoir Computing over Distributed Quantum Architectures

**Authors**: Ioannis Liliopoulos, Georgios D. Varsamis, Konstantinos Rallis, Evangelos Tsipas, Ioannis G. Karafyllidis, Georgios Ch. Sirakoulis, Panagiotis Dimitrakis
**Date**: 2026-05-06
**Paper ID**: [openalex:2605.04991](https://arxiv.org/abs/2605.04991)

## Summary

This paper explores the potential of quantum reservoir computing (QRC) for time-series forecasting, specifically focusing on scaling QRC through distributed architectures. The authors benchmark four architectures combining multiple reservoirs and readout layers, testing them across ideal and hardware-informed noisy simulations. Their findings show that quantum-enhanced models provide substantial improvements in accuracy (up to 78.8% reduction in MAE) and that distributed design patterns successfully enable scaling on NISQ devices.

## Key Contributions

- Introduces a distributed quantum reservoir computing framework for time-series forecasting, utilizing multiple interconnected reservoirs and readout layers.
- Demonstrates that quantum-enhanced configurations achieve up to 78.8% reduction in MAE and 72.3% reduction in RMSE compared to classical baselines.
- Evaluates hybrid and fully quantum architectures under both ideal and hardware-informed noisy (NISQ) conditions, establishing a scalable, hardware-agnostic approach.

## Open Questions & Future Work

- [[optimizing-distributed-quantum-reservoir-architectures]]

## Key Concepts

- [[distributed-quantum-reservoir-computing]]: A modular computing paradigm that scales reservoir computing performance by distributing operations across multiple quantum resources.

## Archivist Review

I approved the 'Distributed Quantum Reservoir Computing' framework as a novel, reusable scaling design for quantum-based forecasting, and the corresponding open question regarding circuit topology optimization in distributed settings. The review strictly adhered to the scarcity mandate, ensuring that only the central architectural contribution and its primary bottleneck were admitted. No other candidates were proposed.

### Approved Concepts
- Distributed Quantum Reservoir Computing: Central framework proposed for scaling quantum reservoir computing architectures across multiple modular quantum resources.

### Approved Open Questions
- Optimizing Distributed Quantum Reservoirs: The development of standardized, high-performing quantum circuit architectures is critical for the practical scalability of distributed quantum reservoir computing, as hardware-agnostic design is currently limited by the lack of comparative benchmarks across heterogeneous backends.

## Links

- [Abstract](https://arxiv.org/abs/2605.04991)
- [PDF](https://arxiv.org/pdf/2605.04991)

