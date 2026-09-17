---
# CSL-compatible fields
title: "GSLAD: Prototype-Regularized Graph Structure Learning for Multivariate Time Series Anomaly Detection"
author:
  - literal: "Zepeng Zhang"
  - literal: "Fuad Khuri"
  - literal: "Keivan Faghih Niresi"
  - literal: "Olga Fink"
  - literal: "Zepeng Zhang"
  - literal: "Fuad Khuri"
  - literal: "Keivan Faghih Niresi"
  - literal: "Olga Fink"
issued:
  date-parts:
    - [2026, 9, 14]
url: "https://arxiv.org/abs/2609.15483"

# Custom fields
paper_id: "2609.15483"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "graph-neural-network"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:43:08Z"
created_at: "2026-09-17T09:43:08Z"
---

# GSLAD: Prototype-Regularized Graph Structure Learning for Multivariate Time Series Anomaly Detection

**Authors**: Zepeng Zhang, Fuad Khuri, Keivan Faghih Niresi, Olga Fink, Zepeng Zhang, Fuad Khuri, Keivan Faghih Niresi, Olga Fink
**Date**: 2026-09-14
**Paper ID**: [openalex:2609.15483](https://arxiv.org/abs/2609.15483)

## Summary

GSLAD is an unsupervised multivariate time series anomaly detection framework that addresses industrial faults altering inter-variable structural patterns rather than individual trajectories. It employs a two-phase training strategy: first learning condition-aware graph structures and forecasters under predictive supervision, and subsequently regularizing the graph learner using clustered normal structural prototypes and edge-wise variability. During inference, uncertainty-normalized structural deviations are combined with predictive deviations for robust anomaly detection and diagnosis across four industrial benchmarks.

## Key Contributions

- Proposes GSLAD, a prototype-regularized graph structure learning framework for multivariate time series anomaly detection that captures subtle inter-variable structural alterations.
- Implements a two-phase training strategy combining condition-aware graph learning, graph-based forecasting, and normal structural prototype clustering with edge-wise variability.
- Combines uncertainty-normalized structural deviations with predictive deviations for robust anomaly scoring and diagnosis across four industrial benchmarks.

## Archivist Review

Following strict review policies for time-series and graph structure learning literature, both the paper-local GSLAD framework and the general future work direction on causal interpretability were rejected as paper-specific or insufficiently concrete to warrant permanent standalone vault notes.

### Rejected Candidates
- [concept] GSLAD (`gslad`) - paper_local: Paper-local framework specific to multivariate time series anomaly detection.
- [open_question] Causal Interpretability in Graph Structure Learning (`causal-interpretable-graph-structure-learning`) - low_impact: A standard speculative future direction regarding interpretability without a concrete unresolved mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2609.15483)
- [PDF](https://arxiv.org/pdf/2609.15483)

