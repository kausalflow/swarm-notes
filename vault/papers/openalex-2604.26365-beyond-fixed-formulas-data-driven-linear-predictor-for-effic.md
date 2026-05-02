---
# CSL-compatible fields
title: "Beyond Fixed Formulas: Data-Driven Linear Predictor for Efficient Diffusion Models"
author:
  - literal: "Zhirong Shen"
  - literal: "Rui Huang"
  - literal: "Jiacheng Liu"
  - literal: "Chang Zou"
  - literal: "Peiliang Cai"
  - literal: "Shikang Zheng"
  - literal: "Zhengyi Shi"
  - literal: "Liang Feng"
  - literal: "Linfeng Zhang"
issued:
  date-parts:
    - [2026, 4, 29]
url: "https://arxiv.org/abs/2604.26365"

# Custom fields
paper_id: "2604.26365"
paper_source: "openalex"
domain: "multimodal,nlp,computer-vision"
tags:
  - "diffusion-model"
  - "transformer"
  - "model-compression"
  - "efficient-transformer"
  - "multimodal"
architectures:
  []
datasets:
  []
concept_slugs:
  - "learnable-linear-predictor-l2p"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-02T06:56:51Z"
created_at: "2026-05-02T06:56:51Z"
---

# Beyond Fixed Formulas: Data-Driven Linear Predictor for Efficient Diffusion Models

**Authors**: Zhirong Shen, Rui Huang, Jiacheng Liu, Chang Zou, Peiliang Cai, Shikang Zheng, Zhengyi Shi, Liang Feng, Linfeng Zhang
**Date**: 2026-04-29
**Paper ID**: [openalex:2604.26365](https://arxiv.org/abs/2604.26365)

## Summary

This paper introduces L2P (Learnable Linear Predictor), a data-driven framework designed to accelerate the inference of Diffusion Transformers (DiTs) through feature caching. Unlike existing methods that rely on inflexible, hand-crafted forecasting formulas, L2P employs learnable per-timestep weights to reconstruct features from past trajectories efficiently. The method is highly lightweight, requiring only ~20 seconds of training on a single GPU, and achieves substantial speedups on FLUX.1-dev and Qwen-Image models while preserving visual quality.

## Key Contributions

- Introduces L2P, a data-driven feature caching framework that uses learnable per-timestep weights for efficient Diffusion Transformer inference.
- Demonstrates a 4.55x FLOPs reduction and 4.15x latency speedup on the FLUX.1-dev model.
- Maintains high visual fidelity under 7.18x acceleration on Qwen-Image models, outperforming fixed-formula caching baselines that degrade at higher skipping rates.

## Open Questions & Future Work

- [[limits-of-linear-feature-forecasting]]

## Key Concepts

- [[learnable-linear-predictor-l2p]]: A data-driven feature caching framework for diffusion models that replaces fixed hand-crafted coefficients with learnable per-timestep weights to accelerate inference.

## Archivist Review

I approved the learnable linear predictor concept as it offers a reusable paradigm for accelerating feature-heavy inference tasks. I also approved an open question regarding the potential limits of linear feature forecasting, which addresses the fundamental trade-off between model simplicity and predictive accuracy in trajectory modeling. All other candidates were rejected as they were either too specific to the proposed framework or generic in nature.

### Approved Concepts
- Learnable Linear Predictor (L2P): L2P provides a generalizable, data-driven alternative to rigid hand-crafted caching formulas in diffusion inference, effectively turning feature prediction into a learnable task.

### Approved Open Questions
- Non-linear Feature Forecasting Potential: This explores the theoretical ceiling of feature-caching acceleration and whether simple linear methods remain optimal as models scale in complexity.

## Links

- [Abstract](https://arxiv.org/abs/2604.26365)
- [PDF](https://arxiv.org/pdf/2604.26365)

