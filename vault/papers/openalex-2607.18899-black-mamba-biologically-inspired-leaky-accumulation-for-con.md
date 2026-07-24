---
# CSL-compatible fields
title: "Black-Mamba: Biologically-Inspired Leaky Accumulation for Conceptual Knowledge under Distribution Drift"
author:
  - literal: "Giuseppe Soriano"
  - literal: "Nicola Tonellotto"
  - literal: "Alberto Gotta"
issued:
  date-parts:
    - [2026, 7, 21]
url: "https://arxiv.org/abs/2607.18899"

# Custom fields
paper_id: "2607.18899"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "state-space-model"
  - "ssm"
  - "mamba"
  - "robustness"
  - "adaptation"
architectures:
  - "mamba"
datasets:
  []
concept_slugs:
  - "black-mamba"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-24T07:25:24Z"
created_at: "2026-07-24T07:25:24Z"
---

# Black-Mamba: Biologically-Inspired Leaky Accumulation for Conceptual Knowledge under Distribution Drift

**Authors**: Giuseppe Soriano, Nicola Tonellotto, Alberto Gotta
**Date**: 2026-07-21
**Paper ID**: [openalex:2607.18899](https://arxiv.org/abs/2607.18899)

## Summary

Real-world time-series forecasting suffers from non-stationarity and distribution drift, while standard test-time adaptive models often suffer from unnecessary updates triggered by transient noise and instantaneous prediction errors. To address this, the authors introduce Black-Mamba, a test-time adaptive forecasting architecture that decouples adaptation from instantaneous surprise via a biologically-inspired leaky accumulation mechanism. This approach treats online adaptation as evidence-gated state tracking, updating internal memory only when accumulated surprisal signals a genuine regime change. Empirical evaluations across non-stationary benchmarks demonstrate improved predictive performance alongside significantly reduced memory update overheads.

## Key Contributions

- Introduces Black-Mamba, a test-time adaptive forecasting architecture formulated around evidence-gated state tracking under distribution drift.
- Replaces continuous error-driven updates with an event-driven mechanism using temporally accumulated surprisal to distinguish persistent drift from transient noise.
- Demonstrates competitive or superior predictive performance while significantly reducing the required number of memory updates during inference across non-stationary benchmarks.

## Limitations

None explicitly stated in the abstract.

## Open Questions & Future Work

- [[update-policy-calibration-and-evolution]]

## Key Concepts

- [[black-mamba]]: A test-time adaptive forecasting architecture that performs online adaptation via evidence-gated state tracking using temporally accumulated surprisal.

## Archivist Review

Approved the overarching concept of Black-Mamba and its open question on long-term update-policy calibration under deployment shift, adhering to strict scarcity guidelines and ensuring proper separation of transient noise from distribution drift.

### Approved Concepts
- Black-Mamba: Presents a novel biologically-inspired test-time adaptation architecture for time-series forecasting that couples leaky accumulation of surprisal with state tracking under distribution drift.

### Approved Open Questions
- Update-Policy Calibration Under Long Deployments: Understanding the long-term dynamics of update-policy calibration is crucial for maintaining effective test-time adaptation without incurring the high cost of full model retraining under evolving operational domains.

## Links

- [Abstract](https://arxiv.org/abs/2607.18899)
- [PDF](https://arxiv.org/pdf/2607.18899)

