---
# CSL-compatible fields
title: "Every Client Is an Environment: Federated De-confounding for Spatio-Temporal Forecasting"
author:
  - literal: "Qingxiang Liu"
  - literal: "Anqi Liang"
  - literal: "Heng Wang"
  - literal: "Yuxuan Liang"
issued:
  date-parts:
    - [2026, 7, 27]
url: "https://arxiv.org/abs/2607.24218"

# Custom fields
paper_id: "2607.24218"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "federated-learning"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "federated-de-confounding-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-30T07:26:30Z"
created_at: "2026-07-30T07:26:30Z"
---

# Every Client Is an Environment: Federated De-confounding for Spatio-Temporal Forecasting

**Authors**: Qingxiang Liu, Anqi Liang, Heng Wang, Yuxuan Liang
**Date**: 2026-07-27
**Paper ID**: [openalex:2607.24218](https://arxiv.org/abs/2607.24218)

## Summary

Federated learning for spatio-temporal forecasting often suffers from poor generalization under environmental shifts because client heterogeneity is typically treated solely as an optimization challenge. This paper introduces FedEnv, a federated de-confounding framework that views each client as a distinct causal environment and leverages distributed observations to learn a global prototype codebook. By framing clients as causal environments and providing a theoretical de-confounding bound, the approach achieves superior forecasting performance and robust environmental representations.

## Key Contributions

- Proposes a novel federated de-confounding framework (FedEnv) that treats federated clients as distinct causal environments for spatio-temporal forecasting.
- Leverages client heterogeneity as distributed environmental evidence and learns a global prototype codebook to capture shared environmental regimes.
- Derives a theoretical federated de-confounding bound controlled linearly by the averaged confounding strength.
- Demonstrates consistent outperformance over federated baselines while providing transferable, interpretable, and communication-efficient environmental representations.

## Open Questions & Future Work

- [[scalable-dynamic-codebook-alignment-for-federated-stf]]

## Key Concepts

- [[federated-de-confounding-framework]]: A federated de-confounding framework that treats clients as distinct causal environments to handle spatio-temporal environmental shifts.

## Archivist Review

Approved the core methodological concept of treating federated clients as causal environments for spatio-temporal forecasting along with its key scaling open question on dynamic codebook alignment. No named benchmark datasets were provided, so the dataset list remains empty.

### Approved Concepts
- Federated De-confounding Framework: Central methodological novelty of treating federated clients as causal environments for spatio-temporal forecasting.

### Approved Open Questions
- Scalable Dynamic Codebook Alignment: As federated spatio-temporal forecasting scales to larger networks with more complex and continuous environmental variables, solving the computational complexity of prototype alignment and handling continuous latent shifts becomes a critical scaling bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.24218)
- [PDF](https://arxiv.org/pdf/2607.24218)

