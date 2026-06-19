---
# CSL-compatible fields
title: "From GPU to Microcontroller: Online Ridge Regression for Edge-Deployable Traffic Prediction"
author:
  - literal: "Suresh Purini"
  - literal: "Archit Narwadkar"
  - literal: "Deepak Gangadharan"
issued:
  date-parts:
    - [2026, 6, 16]
url: "https://arxiv.org/abs/2606.17613"

# Custom fields
paper_id: "2606.17613"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "model-compression"
architectures:
  []
datasets:
  []
concept_slugs:
  - "horizon-aligned-periodic-features"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-19T09:26:10Z"
created_at: "2026-06-19T09:26:10Z"
---

# From GPU to Microcontroller: Online Ridge Regression for Edge-Deployable Traffic Prediction

**Authors**: Suresh Purini, Archit Narwadkar, Deepak Gangadharan
**Date**: 2026-06-16
**Paper ID**: [openalex:2606.17613](https://arxiv.org/abs/2606.17613)

## Summary

This paper challenges the necessity of complex deep learning architectures for traffic flow forecasting, showing that simpler models can achieve comparable accuracy. The authors propose an efficient, per-sensor online ridge regression model utilizing horizon-aligned periodic features and Recursive Least Squares (RLS) for adaptation. This approach drastically reduces parameter counts and compute requirements, enabling high-performance traffic prediction on microcontrollers like the ESP32 without requiring GPU resources. Evaluations on PEMS benchmarks demonstrate that this method maintains competitive accuracy while being significantly more suitable for edge-deployable intelligent transportation systems.

## Key Contributions

- Demonstrates that the effective capacity required for traffic flow forecasting is significantly lower than current GNN/MLP models, allowing for extreme model compression.
- Introduces a resource-efficient traffic forecasting approach using per-sensor Recursive Least Squares (RLS) ridge regression.
- Achieves state-of-the-art MAPE accuracy on PEMS benchmarks while requiring only 444 parameters per sensor and minimal compute.
- Enables real-time online adaptation on edge hardware like ESP32 microcontrollers with sub-millisecond inference and update latency.

## Open Questions & Future Work

- [[multi-sensor-coordination-edge-models]]

## Key Concepts

- [[horizon-aligned-periodic-features]]: A feature engineering approach that aligns periodic temporal inputs with the specific forecasting horizon to optimize linear regression for time-series.

## Archivist Review

I have approved the core methodological concept of horizon-aligned periodic features as it provides a clear, reusable inductive bias for lightweight forecasting. The proposed open question regarding multi-sensor coordination at the edge is approved as a critical, high-impact research challenge. I rejected the PEMS dataset as it is a generic, aggregate category often used to refer to multiple distinct benchmarks already in the vault.

### Approved Concepts
- Horizon-Aligned Periodic Features: Enables high-accuracy traffic forecasting with minimal parameter counts by explicitly encoding temporal cycles for linear models, challenging the need for deep architectures.

### Approved Open Questions
- Multi-sensor coordination for edge models: Addresses the performance gap between purely local independent models and centralized graph-based models in resource-constrained environments.

### Rejected Candidates
- [dataset] PEMS (`pems`) - generic: PEMS is an aggregate collection of multiple datasets (e.g., PEMS04, PEMS08) rather than a single identifiable dataset.

## Links

- [Abstract](https://arxiv.org/abs/2606.17613)
- [PDF](https://arxiv.org/pdf/2606.17613)

