---
# CSL-compatible fields
title: "A Multi-View Coupled Tensor Decomposition for Lightweight Online Adaptive Traffic Prediction"
author:
  - literal: "Quan Yu"
  - literal: "Jie Ni"
  - literal: "Yu-Hong Dai"
  - literal: "Xiongjun Zhang"
issued:
  date-parts:
    - [2026, 8, 26]
url: "https://arxiv.org/abs/2608.25498"

# Custom fields
paper_id: "2608.25498"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
  - "tensor-decomposition"
  - "online-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T17:00:32Z"
created_at: "2026-08-28T17:00:32Z"
---

# A Multi-View Coupled Tensor Decomposition for Lightweight Online Adaptive Traffic Prediction

**Authors**: Quan Yu, Jie Ni, Yu-Hong Dai, Xiongjun Zhang
**Date**: 2026-08-26
**Paper ID**: [openalex:2608.25498](https://arxiv.org/abs/2608.25498)

## Summary

Accurate online traffic prediction under imperfect sensing conditions is challenging due to missing observations and anomalies. This paper proposes a Multi-View Coupled Tensor Decomposition (MVCTD) model that jointly captures shared spatial structures and view-specific temporal dynamics from multi-view traffic data. It employs group sparse regularization to mitigate traffic anomalies and uses lightweight closed-form updates for streaming deployment. Experimental results show that MVCTD achieves robust traffic forecasting performance with favorable runtime under severe data missingness.

## Key Contributions

- Proposes a Multi-View Coupled Tensor Decomposition (MVCTD) model for online traffic prediction from imperfect multi-view observations such as speed, flow, and occupancy.
- Builds a structured latent forecasting space via coupled tensor decomposition that jointly models shared spatial structures across views and view-specific temporal dynamics.
- Introduces a group sparse regularization to handle correlated abnormal responses caused by real traffic anomalies.
- Develops a streaming deployment scheme using iterative refinement on the current latent tensor and lightweight closed-form updates for historical variables, avoiding full sequence re-optimization.

## Archivist Review

The paper presents an application of coupled tensor decomposition for online traffic prediction. No new concepts or open questions met the strict novelty and reusability standards for permanent vault storage.

### Rejected Candidates
- [open_question] Incorporating Exogenous Factors in Traffic Prediction (`incorporating-exogenous-factors-traffic-prediction`) - low_impact: Standard future work suggestion about incorporating external factors and exogenous covariates into domain-specific models.

## Links

- [Abstract](https://arxiv.org/abs/2608.25498)
- [PDF](https://arxiv.org/pdf/2608.25498)

