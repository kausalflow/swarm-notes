---
# CSL-compatible fields
title: "TacForeSight: Force-Guided Tactile World Model for Contact-Rich Manipulation"
author:
  - literal: "Yujie Zang"
  - literal: "Yuhang Zheng"
  - literal: "聂显"
  - literal: "Yupeng Zheng"
  - literal: "Shuai Tian"
  - literal: "Songen Gu"
  - literal: "Chen Gao"
  - literal: "Zining Wang"
  - literal: "Shuicheng Yan"
  - literal: "Wenchao Ding"
issued:
  date-parts:
    - [2026, 6, 9]
url: "https://arxiv.org/abs/2606.11184"

# Custom fields
paper_id: "2606.11184"
paper_source: "openalex"
domain: "robotics"
tags:
  - "robotics"
  - "multimodal"
  - "autonomous-agent"
  - "planning"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "force-conditioned-tactile-world-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-12T08:54:59Z"
created_at: "2026-06-12T08:54:59Z"
---

# TacForeSight: Force-Guided Tactile World Model for Contact-Rich Manipulation

**Authors**: Yujie Zang, Yuhang Zheng, 聂显, Yupeng Zheng, Shuai Tian, Songen Gu, Chen Gao, Zining Wang, Shuicheng Yan, Wenchao Ding
**Date**: 2026-06-09
**Paper ID**: [openalex:2606.11184](https://arxiv.org/abs/2606.11184)

## Summary

TacForeSight is a lightweight framework for real-time, contact-rich robotic manipulation that utilizes a force-conditioned tactile world model (TacForceWM). By forecasting tactile dynamics within a latent space conditioned on high-frequency force signals, the model enables proactive contact reasoning. A predictive tactile-conditioned policy then uses these latents as priors to adaptively fuse visuo-tactile information for robust control. Empirical results demonstrate the framework's superior performance, especially in scenarios involving dynamic contact perturbations.

## Key Contributions

- Introduces TacForeSight, a force-conditioned tactile world model framework for real-time contact-rich robotic manipulation.
- Develops TacForceWM, which models asymmetric spatiotemporal dependencies between global force feedback and local tactile sensing to predict tactile latent dynamics.
- Outperforms existing baselines across five representative manipulation tasks and demonstrates robustness under dynamic contact disturbances.

## Open Questions & Future Work

- [[proactive-vs-reactive-manipulation-modeling]]

## Key Concepts

- [[force-conditioned-tactile-world-model]]: A tactile world model that predicts tactile latent dynamics by conditioning them on high-frequency force and torque feedback.

## Archivist Review

I have approved the core concept of force-conditioned tactile world modeling as a general mechanism for robotic manipulation and the open question regarding the shift from reactive to proactive manipulation control. The specific model name 'TacForceWM' was rejected in favor of the more descriptive and reusable 'force-conditioned-tactile-world-model'. No datasets were approved as none were presented as novel, reusable, or specific benchmarks for this task in the provided metadata.

### Approved Concepts
- Force-Conditioned Tactile World Model: It explicitly addresses the asymmetric integration of global force and local tactile signals for predictive control in robotic manipulation.

### Approved Open Questions
- Proactive vs. Reactive Manipulation Modeling: This is a fundamental control problem that dictates the capability of agents to operate in dynamic, uncertain environments.

### Rejected Candidates
- [concept] TacForceWM (`tacforcewm`) - subcomponent_of_broader_mechanism: This is the specific architecture name used in the paper; it is subsumed by the more descriptive and reusable 'force-conditioned-tactile-world-model'.

## Links

- [Abstract](https://arxiv.org/abs/2606.11184)
- [PDF](https://arxiv.org/pdf/2606.11184)

