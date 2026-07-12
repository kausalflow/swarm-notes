---
# CSL-compatible fields
title: "Progression as Latent Drift: Generative Forecasting of Slow-Evolving Pathologies"
author:
  - literal: "Yuxiang Feng"
  - literal: "Juncheng Wang"
  - literal: "Chao Xu"
  - literal: "Wenlong Hou"
  - literal: "Huihan Wang"
  - literal: "Yijie Qian"
  - literal: "Yang Liu"
  - literal: "Bo Sun"
  - literal: "Yong Liu"
  - literal: "Shujun Wan"
issued:
  date-parts:
    - [2026, 7, 9]
url: "https://arxiv.org/abs/2607.08270"

# Custom fields
paper_id: "2607.08270"
paper_source: "openalex"
domain: "medicine"
tags:
  - "generative-model"
  - "medical-imaging"
  - "longitudinal-study"
  - "time-series"
  - "quantization"
architectures:
  []
datasets:
  []
concept_slugs:
  - "latent-drift"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-12T07:24:28Z"
created_at: "2026-07-12T07:24:28Z"
---

# Progression as Latent Drift: Generative Forecasting of Slow-Evolving Pathologies

**Authors**: Yuxiang Feng, Juncheng Wang, Chao Xu, Wenlong Hou, Huihan Wang, Yijie Qian, Yang Liu, Bo Sun, Yong Liu, Shujun Wan
**Date**: 2026-07-09
**Paper ID**: [openalex:2607.08270](https://arxiv.org/abs/2607.08270)

## Summary

This paper addresses the difficulty of forecasting slow-evolving neurodegenerative diseases in longitudinal MRI by identifying theoretical failure modes: identity collapse and the continuous interpolation trap. To overcome these, the authors propose Latent Drift, a generative framework that focuses on modeling disease progression as a change in a compressed semantic latent space rather than directly synthesizing anatomical pixels. By incorporating Finite Scalar Quantization, the model successfully filters out high-frequency noise while preserving consistent structural drift, leading to improved performance on longitudinal 3D brain MRI compared to baseline models.

## Key Contributions

- Provides a theoretical analysis identifying identity collapse and continuous interpolation traps as failure modes in standard generative models for low-signal longitudinal medical imaging.
- Introduces the Latent Drift framework, which models anatomical progression in a compressed semantic space to focus on dynamics rather than full-resolution synthesis.
- Integrates Finite Scalar Quantization to suppress high-frequency nuisance fluctuations while preserving structural progression, outperforming diffusion and autoregressive baselines on longitudinal 3D brain MRI data.

## Open Questions & Future Work

- [[region-aware-quantization-and-multisite-validation]]

## Key Concepts

- [[latent-drift]]: A generative framework for neuro-forecasting that models disease progression as a latent semantic drift rather than pixel-level anatomical synthesis.

## Archivist Review

The paper identifies critical, novel failure modes (identity collapse and continuous interpolation trap) in low-signal longitudinal medical imaging. Latent Drift is a reusable concept for modeling slow biological progression, and the proposed open question captures a significant challenge in adapting quantization to non-uniform, multi-site medical dynamics. Rejected candidates were either too specific to the implementation (e.g., Finite Scalar Quantization in this context) or lacked broader methodological significance.

### Approved Concepts
- Latent Drift: Addresses the challenges of identity collapse and continuous interpolation traps in low-signal longitudinal medical imaging forecasting.

### Approved Open Questions
- Region-aware Quantization and Multisite Validation: Improving the precision of localized atrophy tracking is essential for clinical applicability, as uniform quantization currently risks discarding clinically significant progression in fast-changing brain regions or being unable to disentangle complex, multi-site nuisance noise from true biological signal.

## Links

- [Abstract](https://arxiv.org/abs/2607.08270)
- [PDF](https://arxiv.org/pdf/2607.08270)

