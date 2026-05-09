---
# CSL-compatible fields
title: "Driver-WM: A Driver-Centric Traffic-Conditioned Latent World Model for In-Cabin Dynamics Rollout"
author:
  - literal: "Haozhuang Chi"
  - literal: "Daosheng Qiu"
  - literal: "Hao Su"
  - literal: "Haochen Liu"
  - literal: "Zirui Li"
  - literal: "Haoruo Zhang"
  - literal: "Chen Lv"
issued:
  date-parts:
    - [2026, 5, 6]
url: "https://arxiv.org/abs/2605.05092"

# Custom fields
paper_id: "2605.05092"
paper_source: "openalex"
domain: "robotics"
tags:
  - "multimodal"
  - "agent"
  - "long-context"
  - "planning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "gated-causal-injection-mechanism"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-09T07:02:43Z"
created_at: "2026-05-09T07:02:43Z"
---

# Driver-WM: A Driver-Centric Traffic-Conditioned Latent World Model for In-Cabin Dynamics Rollout

**Authors**: Haozhuang Chi, Daosheng Qiu, Hao Su, Haochen Liu, Zirui Li, Haoruo Zhang, Chen Lv
**Date**: 2026-05-06
**Paper ID**: [openalex:2605.05092](https://arxiv.org/abs/2605.05092)

## Summary

Driver-WM is a latent world model designed to forecast in-cabin driver dynamics by conditioning on external traffic conditions. It uses a dual-stream latent architecture with a gated causal injection mechanism to modulate environmental influence on driver state transitions. This approach enables multi-step rollout for physical and behavioral dynamics, facilitating improved safety in L2/L3 shared-control scenarios. The model provides a framework for controlled test-time interventions to analyze human-in-the-loop responses to traffic events.

## Key Contributions

- Introduces Driver-WM, a driver-centric latent world model that enables causal multi-step rollout of in-cabin dynamics conditioned on external traffic.
- Employs a dual-stream architecture with a gated causal injection mechanism to maintain temporal causality and modulate cross-modal perturbations.
- Demonstrates robust long-horizon geometric forecasting and improved semantic alignment on a multi-task assistive driving benchmark.

## Open Questions & Future Work

- [[driver-centric-dynamics-rollout-modeling]]

## Key Concepts

- [[gated-causal-injection-mechanism]]: A mechanism that uses a learned vector gate to directionally couple and modulate causal influence between exogenous and endogenous latent states.

## Archivist Review

I have approved the gated causal injection mechanism as a reusable concept for enforcing directed causal coupling in world models. The open question regarding driver-centric dynamics rollout was approved because it identifies a critical bottleneck in L2/L3 automation where current world models fail to integrate the human operator into the predictive loop. No datasets were approved as none were specifically named or highlighted as a core reusable contribution.

### Approved Concepts
- Gated Causal Injection Mechanism: Provides a novel, modular way to enforce directed causal dependencies between distinct multimodal latent streams, which is a common requirement in world modeling and agentic systems.

### Approved Open Questions
- Predicting Driver Dynamics Rollout: Crucial for safety-critical human-in-the-loop automation, where anticipating driver intervention or reaction time is essential for shared-control handoffs.

## Links

- [Abstract](https://arxiv.org/abs/2605.05092)
- [PDF](https://arxiv.org/pdf/2605.05092)

