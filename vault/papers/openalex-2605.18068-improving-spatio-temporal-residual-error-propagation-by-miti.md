---
# CSL-compatible fields
title: "Improving Spatio-Temporal Residual Error Propagation by Mitigating Over-Squashing"
author:
  - literal: "Seyed Mohamad Moghadas"
  - literal: "Esther Rodrigo Bonet"
  - literal: "Bruno Cornelis"
  - literal: "Adrian Munteanu"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2605.18068"

# Custom fields
paper_id: "2605.18068"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "uncertainty-quantification"
  - "transformer"
  - "lstm"
  - "graph-neural-network"
  - "gnn"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "teger-uncertainty-module"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:34:15Z"
created_at: "2026-05-21T08:34:15Z"
---

# Improving Spatio-Temporal Residual Error Propagation by Mitigating Over-Squashing

**Authors**: Seyed Mohamad Moghadas, Esther Rodrigo Bonet, Bruno Cornelis, Adrian Munteanu
**Date**: 2026-05-18
**Paper ID**: [openalex:2605.18068](https://arxiv.org/abs/2605.18068)

## Summary

The paper addresses the degradation of long-horizon forecasts caused by residual error propagation in recurrent models by proposing Teger, an uncertainty module that accounts for both spatial and temporal error correlations. Teger employs a curvature-aware graph rewiring mechanism to alleviate over-squashing by strengthening bottleneck edges, integrated with a low-rank-plus-diagonal covariance head for efficient inference. Theoretical and experimental results demonstrate that the approach improves spectral connectivity and covariance calibration across multiple backbone architectures.

## Key Contributions

- Introduces Teger, a structured uncertainty module that models spatiotemporal error correlation using curvature-aware graph rewiring.
- Mitigates over-squashing in graph structures by strengthening information-bottleneck edges identified via discrete Forman curvature.
- Achieves consistent CRPS improvements across LSTM, Transformer, and xLSTM backbones on four spatiotemporal benchmarks.

## Open Questions & Future Work

- [[over-squashing-impact-on-forecasting-performance-in-dynamic-graphs]]

## Key Concepts

- [[teger-uncertainty-module]]: A structured uncertainty module for autoregressive forecasting that uses Forman curvature-aware graph rewiring to mitigate over-squashing and model spatiotemporal error correlations.

## Archivist Review

I approved the 'Teger' module as it introduces a reusable, backbone-agnostic approach to spatiotemporal uncertainty quantification, which is a key challenge in the field. I also approved one open question regarding the impact of over-squashing on forecasting performance, as it addresses a fundamental gap between graph structural health and downstream predictive accuracy. Other candidates were rejected for being redundant or too niche/mathematical.

### Approved Concepts
- Teger uncertainty module: Provides a novel backbone-agnostic mechanism for spatiotemporal uncertainty quantification by addressing error correlation and the over-squashing bottleneck.

### Approved Open Questions
- Over-squashing impact on forecasting performance: Establishing this link is essential for justifying structural graph interventions in predictive modeling and moving beyond heuristic architectural designs.

### Rejected Candidates
- [open_question] Formalizing OQ-performance in dynamic graphs (`formalizing-oq-impact-on-dynamic-forecasting`) - duplicate_existing: Redundant with the approved question on over-squashing impact; the approved one is more concisely defined.
- [open_question] Normalized Laplacian spectral gap (`spectral-gap-normalized-laplacian`) - low_impact: This is a narrow mathematical edge case regarding graph Laplacian properties rather than a substantial bottleneck in forecasting research.

## Links

- [Abstract](https://arxiv.org/abs/2605.18068)
- [PDF](https://arxiv.org/pdf/2605.18068)

