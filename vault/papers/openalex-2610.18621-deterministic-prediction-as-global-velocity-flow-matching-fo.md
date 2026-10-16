---
# CSL-compatible fields
title: "Deterministic Prediction as Global Velocity: Flow Matching for Probabilistic Time-Series Forecast"
author:
  - literal: "Jiajing Hu"
  - literal: "Xu Han"
  - literal: "Li-Ping Liu"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.18621"

# Custom fields
paper_id: "2610.18621"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "diffusion-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dv-flow"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-16T09:22:48Z"
created_at: "2026-10-16T09:22:48Z"
---

# Deterministic Prediction as Global Velocity: Flow Matching for Probabilistic Time-Series Forecast

**Authors**: Jiajing Hu, Xu Han, Li-Ping Liu
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.18621](https://arxiv.org/abs/2610.18621)

## Summary

Accurate uncertainty quantification in time-series forecasting is often hindered by unstable joint training when deterministic models are embedded within generative processes. To resolve this, the authors propose DV-Flow, a flow-matching formulation that integrates the deterministic predictor as a parallel velocity component rather than an endpoint of the transport path. This design enables stable end-to-end optimization, subsumes prior approaches as special cases, and achieves consistent performance improvements over strong baselines across six real-world datasets.

## Key Contributions

- Proposes DV-Flow, a unified flow-matching formulation that models the deterministic predictor as a parallel velocity component to stabilize end-to-end optimization in probabilistic time-series forecasting.
- Subsumes several existing probabilistic forecasting formulations as special cases, enabling direct comparison among them.
- Demonstrates consistent performance improvements over strong baselines across six real-world time-series datasets.

## Key Concepts

- [[dv-flow]]: A unified flow-matching formulation for probabilistic time-series forecasting that incorporates the deterministic predictor as a parallel velocity component.

## Archivist Review

Approved the core concept DV-Flow because it introduces a distinct, reusable flow-matching formulation treating deterministic predictors as parallel velocity components. Rejected generic dataset descriptions and unnamed collections.

### Approved Concepts
- DV-Flow: Introduces a unified flow-matching formulation for probabilistic time-series forecasting that treats the deterministic predictor as a parallel velocity component to stabilize joint training.

### Rejected Candidates
- [dataset] Six Real-World Datasets (`six-real-world-datasets`) - generic: Generic aggregate dataset collection without standalone name.

## Links

- [Abstract](https://arxiv.org/abs/2610.18621)
- [PDF](https://arxiv.org/pdf/2610.18621)

