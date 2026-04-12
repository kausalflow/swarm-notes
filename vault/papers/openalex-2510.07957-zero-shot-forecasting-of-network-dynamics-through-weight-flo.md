---
# CSL-compatible fields
title: "Zero-Shot Forecasting of Network Dynamics through Weight Flow Matching"
author:
  - literal: "Shihe Zhou"
  - literal: "Ruikun Li"
  - literal: "Huandong Wang"
  - literal: "Xiao Song"
issued:
  date-parts:
    - [2026, 4, 9]
url: "https://arxiv.org/abs/2510.07957"

# Custom fields
paper_id: "2510.07957"
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
  - "weight-flow-matching"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-12T06:18:59Z"
created_at: "2026-04-12T06:18:59Z"
---

# Zero-Shot Forecasting of Network Dynamics through Weight Flow Matching

**Authors**: Shihe Zhou, Ruikun Li, Huandong Wang, Xiao Song
**Date**: 2026-04-09
**Paper ID**: [openalex:2510.07957](https://arxiv.org/abs/2510.07957)

## Summary

FNFM addresses the challenge of forecasting network dynamics under shifting propagation coefficients without requiring model retraining. The framework uses a Variational Encoder to compress historical forecaster weights into latent tokens, followed by a Conditional Flow Matching (CFM) module to learn the weight distribution conditioned on system dynamics. This allows for the instantaneous generation of task-specific weights at test time, providing robust zero-shot performance under distribution shifts.

## Key Contributions

- Introduces Weight Flow Matching (FNFM) to generate dynamic model weights conditioned on system coefficients for zero-shot forecasting.
- Utilizes a Variational Encoder to map trained forecaster weights into compact latent representations, facilitating distribution learning.
- Achieves improved zero-shot accuracy compared to baselines in network dynamics with pronounced out-of-distribution shifts.

## Open Questions & Future Work

- [[zero-shot-dynamic-topology-forecasting]]

## Key Concepts

- [[weight-flow-matching]]: A conditional flow matching framework that generates predictive model weights for specific dynamical coefficients to enable zero-shot forecasting.

## Archivist Review

Approved 'Weight Flow Matching' as a novel parameter-generation approach for out-of-distribution forecasting, which is a significant departure from standard fine-tuning or adaptation methods. The open question regarding dynamic topologies identifies a clear, necessary evolution for current forecasting architectures that rely on static graph assumptions. I applied a strict filter to ensure only the core methodological contribution and a high-impact, actionable research bottleneck were admitted to the vault.

### Approved Concepts
- Weight Flow Matching: Central mechanism for generating model weights for unseen conditions without training.

### Approved Open Questions
- Zero-Shot Forecasting under Dynamic Topologies: Many real-world network dynamics, such as social influence or technological diffusion, occur on rapidly changing graphs. The ability to forecast under dynamic topology is essential for the practical applicability of weight-generation-based forecasting models.

## Links

- [Abstract](https://arxiv.org/abs/2510.07957)
- [PDF](https://arxiv.org/pdf/2510.07957)

