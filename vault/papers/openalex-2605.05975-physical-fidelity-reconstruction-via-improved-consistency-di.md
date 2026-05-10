---
# CSL-compatible fields
title: "Physical Fidelity Reconstruction via Improved Consistency-Distilled Flow Matching for Dynamical Systems"
author:
  - literal: "Sicheng Ma"
  - literal: "Tianyue Yang"
  - literal: "Xiuzhe Wu"
  - literal: "Xiao Xue"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.05975"

# Custom fields
paper_id: "2605.05975"
paper_source: "openalex"
domain: "science-and-engineering-ml-or-time-series-context-dependent-on-the-paper-content-here-physics-ml-which-is-often-categorized-under-science-or-time-series"
tags:
  - "forecasting"
  - "generative-model"
  - "knowledge-distillation"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "consistency-distilled-flow-matching"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:23:58Z"
created_at: "2026-05-10T07:23:58Z"
---

# Physical Fidelity Reconstruction via Improved Consistency-Distilled Flow Matching for Dynamical Systems

**Authors**: Sicheng Ma, Tianyue Yang, Xiuzhe Wu, Xiao Xue
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.05975](https://arxiv.org/abs/2605.05975)

## Summary

This paper addresses the computational latency of high-fidelity flow reconstruction in scientific machine learning by distilling iterative optimal-transport flow-matching teachers into compact one-step consistency models. By initializing trajectories from noised low-fidelity observations, the proposed method enables conditional reconstruction using unconditional models without requiring retraining. Empirical evaluations on Smoke Buoyancy, Turbulent Channel Flow, and Kolmogorov Flow demonstrate a $12\times$ inference speedup and superior reconstruction quality compared to models trained from scratch.

## Key Contributions

- Introduces a consistency-distillation framework that compresses optimal-transport flow-matching models into efficient one-step generative models.
- Demonstrates $12\times$ inference speedup and significant parameter reduction compared to teacher models on fluid flow reconstruction tasks.
- Achieves $23.1\%$ improvement in SSIM over consistency models trained from scratch, establishing that distillation enhances training efficiency and reconstruction quality.

## Open Questions & Future Work

- [[adaptive-noise-schedules-flow-reconstruction]]

## Key Concepts

- [[consistency-distilled-flow-matching]]: A distillation strategy that maps optimal-transport flow-matching teachers to one-step consistency models for accelerated, high-fidelity scientific flow reconstruction.

## Archivist Review

The paper presents a specific technique for distilling flow-matching models into faster consistency models, which is a significant contribution to the scientific ML community and sufficiently reusable to warrant an entry. The open question regarding adaptive noise schedules is also a critical bottleneck for generative reconstruction methods in scientific settings. Other candidates were rejected to maintain the required scarcity of the vault.

### Approved Concepts
- Consistency-Distilled Flow Matching: It provides a method to compress expensive iterative flow-matching models into one-step consistency models while retaining scientific fidelity.

### Approved Open Questions
- Adaptive Noise Schedules: Developing adaptive schedules is crucial for improving local reconstruction accuracy in non-stationary turbulent flows where the local information content and signal-to-noise ratio of coarse observations vary significantly.

## Links

- [Abstract](https://arxiv.org/abs/2605.05975)
- [PDF](https://arxiv.org/pdf/2605.05975)

