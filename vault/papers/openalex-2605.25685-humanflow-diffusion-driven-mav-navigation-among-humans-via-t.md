---
# CSL-compatible fields
title: "HumanFlow -- Diffusion-Driven MAV Navigation Among Humans via Tightly-Coupled Motion Tracking, Forecasting, and Control"
author:
  - literal: "Simon Schaefer"
  - literal: "Joshua Näf"
  - literal: "Stefan Leutenegger"
issued:
  date-parts:
    - [2026, 5, 25]
url: "https://arxiv.org/abs/2605.25685"

# Custom fields
paper_id: "2605.25685"
paper_source: "openalex"
domain: "robotics"
tags:
  - "diffusion-model"
  - "motion-tracking"
  - "forecasting"
  - "navigation"
  - "robotics"
  - "mpc"
architectures:
  []
datasets:
  []
concept_slugs:
  - "humanflow"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-28T08:38:02Z"
created_at: "2026-05-28T08:38:02Z"
---

# HumanFlow -- Diffusion-Driven MAV Navigation Among Humans via Tightly-Coupled Motion Tracking, Forecasting, and Control

**Authors**: Simon Schaefer, Joshua Näf, Stefan Leutenegger
**Date**: 2026-05-25
**Paper ID**: [openalex:2605.25685](https://arxiv.org/abs/2605.25685)

## Summary

HumanFlow addresses the challenge of navigating robots among humans by unifying motion tracking and forecasting within a latent diffusion framework. By conditioning predictions on 3D scene context, the model maintains high accuracy and smoothness even during heavy occlusions. The authors further demonstrate that these latent representations can be integrated into a flow-matching-based MPC policy, enabling safe and socially-aware MAV navigation in complex environments.

## Key Contributions

- Introduces HumanFlow, a latent diffusion model for unified human motion tracking and forecasting conditioned on 3D scene geometry.
- Demonstrates superior motion tracking accuracy and efficiency compared to state-of-the-art methods under occlusions.
- Proposes a tightly-coupled navigation pipeline by conditioning a flow-matching-based MPC policy on HumanFlow latent representations for collision-free MAV navigation.

## Open Questions & Future Work

- [[bidirectional-human-robot-interaction-modeling]]

## Key Concepts

- [[humanflow]]: A latent diffusion model that unifies human motion tracking and forecasting, conditioned on 3D scene geometry, to support social navigation.

## Archivist Review

I approved the HumanFlow architecture as it introduces a reusable approach to unifying tracking and forecasting via diffusion models for robot navigation. I also approved the open question regarding bidirectional interaction modeling as it addresses a core theoretical limitation in current social navigation literature. Other candidates were rejected as they represent subcomponents or boilerplate research directions.

### Approved Concepts
- HumanFlow: This unified framework for 3D human motion tracking, forecasting, and control is a central architecture in this paper.

### Approved Open Questions
- Bidirectional Human-Robot Interaction Modeling: This is a fundamental challenge for truly social, proactive robot navigation in crowded environments, as the independence assumption is often violated in realistic human-robot encounters.

## Links

- [Abstract](https://arxiv.org/abs/2605.25685)
- [PDF](https://arxiv.org/pdf/2605.25685)

