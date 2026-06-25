---
# CSL-compatible fields
title: "SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real Control of Quadrotors"
author:
  - literal: "Pratyaksh Rao"
  - literal: "Wancong Zhang"
  - literal: "Randall Balestriero"
  - literal: "Yann LeCun"
  - literal: "Giuseppe Loianno"
issued:
  date-parts:
    - [2026, 6, 22]
url: "https://arxiv.org/abs/2606.23444"

# Custom fields
paper_id: "2606.23444"
paper_source: "openalex"
domain: "robotics"
tags:
  - "multimodal"
  - "robotics"
  - "reinforcement-learning"
  - "long-context"
  - "autonomous-agent"
  - "planning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "skyjepa"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-25T08:20:18Z"
created_at: "2026-06-25T08:20:18Z"
---

# SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real Control of Quadrotors

**Authors**: Pratyaksh Rao, Wancong Zhang, Randall Balestriero, Yann LeCun, Giuseppe Loianno
**Date**: 2026-06-22
**Paper ID**: [openalex:2606.23444](https://arxiv.org/abs/2606.23444)

## Summary

SkyJEPA addresses the challenges of long-horizon forecasting in quadrotor control by applying Joint Embedding Predictive Architectures (JEPAs) to learn latent world models. Unlike traditional autoregressive models, this approach models dynamics directly in latent space to mitigate error accumulation. It integrates a physics-informed prober to bridge latent embeddings and interpretable states, facilitating real-time sampling-based optimal control on embedded hardware with robust zero-shot sim-to-real performance.

## Key Contributions

- SkyJEPA models quadrotor dynamics in latent space, avoiding error accumulation issues associated with autoregressive rollout mechanisms in high-frequency control.
- Introduces a physics-inspired prober that maps frozen latent embeddings to interpretable physical states for grounded long-horizon prediction.
- Demonstrates robust zero-shot sim-to-real transfer and real-time control on embedded quadrotor hardware using a sampling-based optimal control strategy.

## Open Questions & Future Work

- [[visual-world-models-for-quadrotors]]
- [[latent-dynamics-for-safe-planning]]

## Key Concepts

- [[skyjepa]]: A JEPA-based latent dynamics model for long-horizon robotic control that operates directly in latent space to mitigate predictive error accumulation.

## Archivist Review

I have approved SkyJEPA for its novel adaptation of latent predictive architectures to real-time robotics, and two open questions concerning the scaling of world models to visual inputs and safety-aware latent representations. These items capture fundamental challenges in robotic dynamics modeling that transcend this specific paper. No datasets were approved as none provided were central or novel enough for standalone tracking.

### Approved Concepts
- SkyJEPA: Adapts Joint Embedding Predictive Architectures (JEPAs) for high-frequency robotic control, successfully bypassing the error accumulation inherent in autoregressive rollouts.

### Approved Open Questions
- Visual World Models for Quadrotors: This is a major bottleneck for scaling aerial robotics to unstructured, real-world environments where high-fidelity state estimation (e.g., motion capture) is unavailable.
- Latent Dynamics for Safe Planning: Explicit safety integration is critical for transitioning from laboratory control tasks to robust deployment in dynamic, hazardous environments.

## Links

- [Abstract](https://arxiv.org/abs/2606.23444)
- [PDF](https://arxiv.org/pdf/2606.23444)

