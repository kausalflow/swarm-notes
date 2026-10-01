---
# CSL-compatible fields
title: "Channel-Dependent State Space Model for Multivariate Time Series Forecasting"
author:
  - literal: "Yu-Cheng Wu"
  - literal: "Fan-Keng Sun"
  - literal: "Li-Chun Lu"
  - literal: "Duane S. Boning"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.36453"

# Custom fields
paper_id: "2609.36453"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "state-space-model"
  - "ssm"
  - "mamba"
  - "benchmark"
architectures:
  - "mamba"
datasets:
  []
concept_slugs:
  - "chameleon"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-01T11:14:36Z"
created_at: "2026-10-01T11:14:36Z"
---

# Channel-Dependent State Space Model for Multivariate Time Series Forecasting

**Authors**: Yu-Cheng Wu, Fan-Keng Sun, Li-Chun Lu, Duane S. Boning
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.36453](https://arxiv.org/abs/2609.36453)

## Summary

Multivariate time series forecasting often forces a trade-off between channel-independent models that ignore cross-variable dynamics and channel-dependent models that overfit or scale poorly. This paper introduces Chameleon, a channel-dependent state space model that connects selective SSMs with the Kalman filter to capture fine-grained variable interactions while maintaining linear complexity. Using GatedDeltaNet as a backbone alongside stochastic reversible instance normalization perturbation, Chameleon achieves state-of-the-art performance across numerous standard benchmarks, significantly outperforming existing CI and CD baselines.

## Key Contributions

- Proposes Chameleon, a channel-dependent state space model that connects selective SSMs with the Kalman filter to model cross-variable dependencies while scaling linearly.
- Leverages GatedDeltaNet as a backbone with favorable inductive biases for time series and introduces stochastic perturbation of reversible instance normalization to improve generalization.
- Achieves superior MSE and MAE on ODE and PEMS datasets, outperforming CI ablations and prior CD methods by 61-178% higher MSE on average, and winning across 27 out of 28 standard benchmark settings.

## Open Questions & Future Work

- [[trade-off-granularity-scalability-mtsf]]

## Key Concepts

- [[chameleon]]: A specialized channel-dependent state space model that connects selective SSMs with the Kalman filter to enable data-dependent cross-variable interactions while scaling linearly.

## Archivist Review

Approved the core model concept Chameleon and its associated open question regarding the fundamental trade-off between granularity and scalability in multivariate time series forecasting. No datasets were approved as they correspond to standard general benchmarks already covered.

### Approved Concepts
- Chameleon: Chameleon introduces a channel-dependent state space model connecting selective SSMs with the Kalman filter for multivariate time series forecasting.

### Approved Open Questions
- Trade-off in Multivariate Forecasting: This trade-off is fundamental to multivariate time series forecasting, defining the core architectural limitations that separate channel-independent and channel-dependent paradigms.

## Links

- [Abstract](https://arxiv.org/abs/2609.36453)
- [PDF](https://arxiv.org/pdf/2609.36453)

