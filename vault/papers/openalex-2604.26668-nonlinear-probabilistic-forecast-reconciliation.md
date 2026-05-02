---
# CSL-compatible fields
title: "Nonlinear Probabilistic Forecast Reconciliation"
author:
  - literal: "Avizit Biswas"
  - literal: "Lorenzo Zambon"
  - literal: "Lorenzo Nespoli"
  - literal: "Giorgio Corani"
issued:
  date-parts:
    - [2026, 4, 29]
url: "https://arxiv.org/abs/2604.26668"

# Custom fields
paper_id: "2604.26668"
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
  - "nonlinear-probabilistic-forecast-reconciliation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-02T06:56:19Z"
created_at: "2026-05-02T06:56:19Z"
---

# Nonlinear Probabilistic Forecast Reconciliation

**Authors**: Avizit Biswas, Lorenzo Zambon, Lorenzo Nespoli, Giorgio Corani
**Date**: 2026-04-29
**Paper ID**: [openalex:2604.26668](https://arxiv.org/abs/2604.26668)

## Summary

This paper addresses the gap in forecast reconciliation by introducing methods to harmonize probabilistic forecasts subject to nonlinear constraints. The authors extend existing projection and conditioning techniques, with the latter utilizing an Unscented Kalman Filter to effectively navigate the nonlinear coherent manifold. Results show that these reconciliation techniques consistently enhance accuracy, with the UKF-based approach demonstrating significant performance gains and lower computational costs.

## Key Contributions

- Introduces the first framework for probabilistic forecast reconciliation under nonlinear constraints, generalizing projection and conditioning methods.
- Develops a conditioning-based reconciliation method utilizing an Unscented Kalman Filter (UKF) to handle non-linearity.
- Demonstrates that the UKF-based reconciliation approach provides superior accuracy and computational efficiency compared to standard projection-based methods across synthetic and real-world datasets.

## Open Questions & Future Work

- [[nonlinear-probabilistic-reconciliation-limitations]]

## Key Concepts

- [[nonlinear-probabilistic-forecast-reconciliation]]: A framework for reconciling independent probabilistic forecasts to satisfy nonlinear equality or inequality constraints.

## Archivist Review

I approved the core framework concept and the open question regarding the limitations of current nonlinear reconciliation approaches. The proposed methods provide a significant advancement over linear-only approaches, but the open questions correctly identify the reliance on Gaussian/Euclidean assumptions as a key bottleneck for wider adoption in complex time-series settings.

### Approved Concepts
- Nonlinear Probabilistic Forecast Reconciliation: First systematic framework addressing probabilistic forecast reconciliation specifically for nonlinear constraints, moving beyond traditional linear reconciliation methods.

### Approved Open Questions
- Nonlinear Probabilistic Reconciliation Limitations: The current reliance on Gaussian assumptions and Euclidean distances limits the applicability of these reconciliation methods to a wide range of real-world datasets that do not adhere to these properties.

## Links

- [Abstract](https://arxiv.org/abs/2604.26668)
- [PDF](https://arxiv.org/pdf/2604.26668)

