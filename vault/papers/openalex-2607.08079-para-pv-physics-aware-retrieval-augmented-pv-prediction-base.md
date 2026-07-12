---
# CSL-compatible fields
title: "PARA-PV: Physics-Aware Retrieval-Augmented PV Prediction Based on Frozen Foundation Model and Distribution Shift Correction"
author:
  - literal: "Haiwei Fan"
  - literal: "Weican Liu"
  - literal: "Ye Lu"
  - literal: "Dunnan Liu"
  - literal: "Long Cheng"
  - literal: "Wei Wei"
issued:
  date-parts:
    - [2026, 7, 9]
url: "https://arxiv.org/abs/2607.08079"

# Custom fields
paper_id: "2607.08079"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "retrieval-augmented-generation"
  - "language-model"
  - "physics-informed-neural-networks"
  - "parameter-efficient-fine-tuning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "physics-aware-retrieval-augmented-learner"
  - "physics-aware-distribution-shift-correction"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-12T07:24:34Z"
created_at: "2026-07-12T07:24:34Z"
---

# PARA-PV: Physics-Aware Retrieval-Augmented PV Prediction Based on Frozen Foundation Model and Distribution Shift Correction

**Authors**: Haiwei Fan, Weican Liu, Ye Lu, Dunnan Liu, Long Cheng, Wei Wei
**Date**: 2026-07-09
**Paper ID**: [openalex:2607.08079](https://arxiv.org/abs/2607.08079)

## Summary

PARA-PV is a physics-aware retrieval-augmented framework for photovoltaic power forecasting that integrates local physical grounding with general temporal knowledge from frozen foundation models. The system retrieves physically consistent historical trajectories, calibrates them against a Chronos foundation model prior, and corrects residual distribution shifts using weather and temporal context. Finally, a regime-partitioned, physics-constrained loss function ensures critical operational states are accurately captured.

## Key Contributions

- Introduced PARA-PV, a framework combining physics-aware retrieval with frozen foundation model priors for PV forecasting.
- Developed a physics-aware distribution shift correction module using gated mean-shift and scale corrections for regime-dependent adjustments.
- Proposed a regime-partitioned physics-constrained loss function that prioritizes critical states like peak and ramping phases over regular operations.

## Open Questions & Future Work

- [[dynamic-memory-updates-for-retrieval-forecasting]]

## Key Concepts

- [[physics-aware-retrieval-augmented-learner]]: A retrieval mechanism that pulls historical time-series data based on temporal, operational, and physical state consistency.
- [[physics-aware-distribution-shift-correction]]: A module that corrects distribution shifts in forecasts by conditioning on exogenous weather, temporal, and operational factors.

## Archivist Review

I approved two concepts that represent reusable mechanisms for grounding and correcting time-series forecasts in domain-specific contexts. I also approved one open question concerning the scalability and adaptivity of retrieval banks, as it addresses a key bottleneck in applying retrieval-augmented forecasting to real-world environments. No datasets were approved as none were highlighted as critical benchmarks or contributions.

### Approved Concepts
- Physics-Aware Retrieval-Augmented Learner: Central mechanism for ensuring physically grounded base forecasts by retrieving patches based on operational states.
- Physics-aware distribution shift correction: Addresses residual shifts caused by regime changes in non-stationary time series.

### Approved Open Questions
- Dynamic Memory for Retrieval Forecasting: Enabling adaptive, real-time updates to the memory bank is critical for the long-term reliability and robustness of retrieval-augmented forecasting systems in dynamic, real-world operational environments.

## Links

- [Abstract](https://arxiv.org/abs/2607.08079)
- [PDF](https://arxiv.org/pdf/2607.08079)

