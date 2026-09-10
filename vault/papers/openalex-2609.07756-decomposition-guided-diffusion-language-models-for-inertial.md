---
# CSL-compatible fields
title: "Decomposition-Guided Diffusion Language Models for Inertial Confinement Fusion Prediction"
author:
  - literal: "Xiang Zhang"
  - literal: "V. Gopalaswamy"
  - literal: "Rahman Ejaz"
  - literal: "Riccardo Betti"
  - literal: "Dongfang Liu"
issued:
  date-parts:
    - [2026, 9, 7]
url: "https://arxiv.org/abs/2609.07756"

# Custom fields
paper_id: "2609.07756"
paper_source: "openalex"
domain: "time-series"
tags:
  - "llm"
  - "language-model"
  - "diffusion-model"
  - "time-series"
  - "forecasting"
  - "reinforcement-learning"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "icf-dlm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-10T09:17:40Z"
created_at: "2026-09-10T09:17:40Z"
---

# Decomposition-Guided Diffusion Language Models for Inertial Confinement Fusion Prediction

**Authors**: Xiang Zhang, V. Gopalaswamy, Rahman Ejaz, Riccardo Betti, Dongfang Liu
**Date**: 2026-09-07
**Paper ID**: [openalex:2609.07756](https://arxiv.org/abs/2609.07756)

## Summary

This paper proposes ICF-DLM, a decomposition-guided diffusion language model for inertial confinement fusion (ICF) waveform prediction driven by exogenous laser pulse and target parameters. The model handles extreme temporal sparsity and picosecond peak sensitivity through a physics-typed decomposition, bidirectional denoising, and a physics-driven PPO reward. Evaluated on ICFBench, ICF-DLM outperforms classical sequence models and baseline language models in peak-timing accuracy.

## Key Contributions

- Proposes ICF-DLM, the first language-model-based predictor for inertial confinement fusion waveform prediction under exogenous laser pulse and target parameters.
- Introduces a physics-typed decomposition dividing prediction into yield, peak timing, and local waveform.
- Employs bidirectional denoising and physics-driven PPO reward re-injection to handle picosecond-scale peak sensitivity and temporal sparsity.
- Demonstrates superior performance on ICFBench, reducing peak-timing error to 9.2 steps compared to 11.6 for a matched autoregressive LLaMA-3-8B.

## Limitations

Evaluated primarily on ICF waveform prediction with under 300 real experimental shots, relying heavily on simulated data augmentation.

## Open Questions & Future Work

- [[icf-diagnostic-generalization-and-multi-facility-validation-in-diffusion-language-models]]

## Key Concepts

- [[icf-dlm]]: A decomposition-guided diffusion language model for exogenous-driven inertial confinement fusion waveform prediction.

## Archivist Review

Approved the core model concept ICF-DLM and the specific open question on ICF diagnostic generalization, while rejecting generic or domain-local future work directions to maintain vault selectivity.

### Approved Concepts
- ICF-DLM: It is the core model proposed for physics-informed inertial confinement fusion prediction.

### Approved Open Questions
- ICF Diagnostic and Facility Generalization: Crucial for establishing whether the proposed physics-typed decomposition and diffusion language modeling approach is generalizable across diverse experimental setups and diagnostic modalities in fusion research.

## Links

- [Abstract](https://arxiv.org/abs/2609.07756)
- [PDF](https://arxiv.org/pdf/2609.07756)

