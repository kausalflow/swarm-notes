---
# CSL-compatible fields
title: "Hybrid Photonic-Quantum Reservoir Computing for Time-Series Prediction"
author:
  - literal: "Oishik Kar"
  - literal: "Aswath Babu H"
issued:
  date-parts:
    - [2026, 8, 6]
url: "https://arxiv.org/abs/2511.09218"

# Custom fields
paper_id: "2511.09218"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "quantum-reservoir-computing"
  - "reservoir-computing"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "hybrid-photonic-quantum-reservoir-computing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-09T05:39:55Z"
created_at: "2026-08-09T05:39:55Z"
---

# Hybrid Photonic-Quantum Reservoir Computing for Time-Series Prediction

**Authors**: Oishik Kar, Aswath Babu H
**Date**: 2026-08-06
**Paper ID**: [openalex:2511.09218](https://arxiv.org/abs/2511.09218)

## Summary

This paper introduces the Hybrid Photonic-Quantum Reservoir Computing (HPQRC) paradigm, which integrates high-speed photonic systems with quantum reservoir dynamics to address computational bottlenecks and energy inefficiency in time-series forecasting. Evaluated across chaotic, financial, and biomedical benchmarks, HPQRC consistently outperforms classical and quantum-only reservoir models, reducing Normalized Mean Squared Error on chaotic systems, improving ECG R-peak prediction accuracy, and enhancing directional accuracy on financial data while maintaining robustness against Gaussian noise. Furthermore, HPQRC achieves a 56.1% reduction in wall-clock time compared to classical reservoir computing.

## Key Contributions

- Proposes Hybrid Photonic-Quantum Reservoir Computing (HPQRC) combining high-speed photonic parallelism with quantum reservoir dynamics for resource-constrained time-series prediction.
- Reduces Normalized Mean Squared Error by 25.9% on Mackey-Glass and 21.8% on Lorenz chaotic systems compared to quantum-only reservoir computing.
- Achieves 89.4% accuracy on MIT-BIH ECG R-peak prediction and 55.13% Mean Directional Accuracy on S&P 500 hourly direction prediction.
- Demonstrates robustness under 15% Gaussian noise and a 56.1% reduction in simulation wall-clock time relative to classical reservoir computing.

## Limitations

Evaluated primarily through simulation results; physical hardware implementations may introduce additional noise and scaling constraints.

## Open Questions & Future Work

- [[hardware-deployment-and-miniaturization-of-hybrid-photonic-quantum-reservoir-computing]]

## Key Concepts

- [[hybrid-photonic-quantum-reservoir-computing]]: A hybrid time-series forecasting architecture combining photonic systems with quantum reservoir computing to achieve high-speed, low-latency, and noise-robust predictions.

## Archivist Review

Approved the hybrid photonic-quantum reservoir computing paradigm as a novel and reusable cross-domain architecture for time-series forecasting. Approved the open question regarding its physical hardware deployment and miniaturization, which addresses a key limitation in moving from simulation to real-world devices. Rejected standard benchmark datasets.

### Approved Concepts
- Hybrid Photonic-Quantum Reservoir Computing: Central novelty of the paper, combining photonic high-speed parallelism with quantum reservoir dynamics for low-latency time-series prediction.

### Approved Open Questions
- Physical Deployment of Hybrid Photonic-Quantum Reservoirs: Crucial for transitioning hybrid photonic-quantum reservoir computing models from theoretical simulation to practical, scalable physical hardware.

### Rejected Candidates
- [dataset] Mackey-Glass and Lorenz Benchmarks (`mackey-glass-and-lorenz-systems`) - not_novel: Standard chaotic systems used across literature rather than novel dataset contributions.
- [dataset] S&P 500 Hourly Direction Prediction (`sp-500-hourly-direction-prediction`) - duplicate_existing: Standard financial benchmark already covered by existing financial indices.

## Links

- [Abstract](https://arxiv.org/abs/2511.09218)
- [PDF](https://arxiv.org/pdf/2511.09218)

