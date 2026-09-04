---
# CSL-compatible fields
title: "Residual Kalman Dynamics for Event-Based UAV Forecasting"
author:
  - literal: "Per Nyblom"
  - literal: "Hannes Ovrén"
  - literal: "David Gustafsson"
issued:
  date-parts:
    - [2026, 9, 1]
url: "https://arxiv.org/abs/2609.00839"

# Custom fields
paper_id: "2609.00839"
paper_source: "openalex"
domain: "robotics"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-04T09:10:43Z"
created_at: "2026-09-04T09:10:43Z"
---

# Residual Kalman Dynamics for Event-Based UAV Forecasting

**Authors**: Per Nyblom, Hannes Ovrén, David Gustafsson
**Date**: 2026-09-01
**Paper ID**: [openalex:2609.00839](https://arxiv.org/abs/2609.00839)

## Summary

This paper investigates short- and mid-horizon UAV bounding-box forecasting using event-camera data from the FRED dataset. The authors establish a constant-velocity Kalman filter as a physical baseline and train a residual model to predict acceleration corrections from box history, filtered state features, and local events. Results show that event-conditioned residual models improve forecasting performance and remain robust even under decorrelated diagnostic subsets that weaken dataset-specific motion priors.

## Key Contributions

- Proposes a residual Kalman dynamics framework combining a physical constant-velocity Kalman filter with a residual model for event-based UAV bounding-box forecasting.
- Demonstrates consistent improvements over standard Kalman filter baselines on the FRED event-camera dataset, particularly with event-conditioned residual models.
- Introduces decorrelated subsets as a diagnostic stress test to show that event-conditioned models retain predictive signals even when position- and velocity-based dataset shortcuts are weakened.

## Archivist Review

The paper combines a constant-velocity Kalman filter with a data-driven residual correction model for event-based UAV forecasting. No new concepts or robust open questions qualify for permanent vault archiving under the strict selection policy.

### Rejected Candidates
- [open_question] Uncertainty-Aware UAV Forecasting (`uncertainty-aware-uav-trajectory-forecasting`) - not_novel: Boilerplate future work suggesting the addition of uncertainty quantification and multi-modal trajectory modeling.

## Links

- [Abstract](https://arxiv.org/abs/2609.00839)
- [PDF](https://arxiv.org/pdf/2609.00839)

