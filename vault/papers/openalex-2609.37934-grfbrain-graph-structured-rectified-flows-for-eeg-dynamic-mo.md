---
# CSL-compatible fields
title: "GRFBrain: Graph-Structured Rectified Flows for EEG Dynamic Modeling"
author:
  - literal: "Haohui Jia"
  - literal: "Zheng Chen"
  - literal: "Jathurshan Pradeepkumar"
  - literal: "Xu Cao"
  - literal: "Yasuko Matsubara"
  - literal: "Yasushi Sakurai"
  - literal: "Takashi Matsubara"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.37934"

# Custom fields
paper_id: "2609.37934"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "graph-neural-network"
  - "diffusion-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "grfbrain"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-02T10:48:12Z"
created_at: "2026-10-02T10:48:12Z"
---

# GRFBrain: Graph-Structured Rectified Flows for EEG Dynamic Modeling

**Authors**: Haohui Jia, Zheng Chen, Jathurshan Pradeepkumar, Xu Cao, Yasuko Matsubara, Yasushi Sakurai, Takashi Matsubara
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.37934](https://arxiv.org/abs/2609.37934)

## Summary

GRFBrain introduces a graph-structured residual flow framework for forecasting time-varying functional connectivity in EEG data. The method separates conditional mean prediction from stochastic residual transport by combining a history-based future graph predictor with a graph Gaussian source derived from Laplacian covariance. A conditional velocity field explicitly maps source samples to future graph residuals while separating transport time from physical EEG time, supported by rigorous controls isolating the benefits of residual transport.

## Key Contributions

- Proposes GRFBrain, a graph-structured residual flow framework for forecasting time-varying EEG functional connectivity that separates conditional mean prediction from stochastic residual transport.
- Utilizes a history-only predictor to estimate the future connectivity graph alongside a graph Gaussian source encoding channel dependencies through a Laplacian-based covariance.
- Distinguishes transport time explicitly from physical EEG time within a conditional velocity field that maps source samples to future graph residuals.
- Identifies rigorous conditions and controls to isolate the benefits of stochastic residual transport from deterministic predictions, learned representations, and sampling effects.

## Open Questions & Future Work

- [[continuous-long-horizon-eeg-rectified-flows]]

## Key Concepts

- [[grfbrain]]: A graph-structured residual flow framework for forecasting time-varying functional connectivity in EEG data by separating conditional mean prediction from stochastic residual transport.

## Archivist Review

Applied strict selectivity by approving only the primary overarching framework concept (GRFBrain) and a foundational open question regarding long-horizon continuous EEG flow modeling, while ensuring all constraints and formatting rules were meticulously met.

### Approved Concepts
- GRFBrain: It introduces a novel graph-structured rectified flow framework specifically tailored for modeling EEG dynamic functional connectivity.

### Approved Open Questions
- Continuous Long-Horizon EEG Rectified Flows: Extending graph-structured rectified flows to continuous, long-horizon multi-channel neural time series is critical for clinical monitoring applications such as continuous epilepsy tracking and real-ether diagnostics.

## Links

- [Abstract](https://arxiv.org/abs/2609.37934)
- [PDF](https://arxiv.org/pdf/2609.37934)

