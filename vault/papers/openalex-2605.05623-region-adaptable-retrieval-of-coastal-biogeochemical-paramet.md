---
# CSL-compatible fields
title: "Region-adaptable retrieval of coastal biogeochemical parameters from near-surface hyperspectral remote sensing reflectance using physics-aware meta-learning"
author:
  - literal: "Yiqing Guo"
  - literal: "Nagur Cherukuru"
  - literal: "Eric A. Lehmann"
  - literal: "S. L. Kesav Unnithan"
  - literal: "Tim Malthus"
  - literal: "Gemma Kerrisk"
  - literal: "Xiubin Qi"
  - literal: "Faisal Islam"
  - literal: "Tisham Dhar"
  - literal: "Mark Doubell"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.05623"

# Custom fields
paper_id: "2605.05623"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "meta-learning"
  - "pre-training"
  - "fine-tuning"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "physics-aware-meta-learning-for-bgc-retrieval"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:23:43Z"
created_at: "2026-05-10T07:23:43Z"
---

# Region-adaptable retrieval of coastal biogeochemical parameters from near-surface hyperspectral remote sensing reflectance using physics-aware meta-learning

**Authors**: Yiqing Guo, Nagur Cherukuru, Eric A. Lehmann, S. L. Kesav Unnithan, Tim Malthus, Gemma Kerrisk, Xiubin Qi, Faisal Islam, Tisham Dhar, Mark Doubell
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.05623](https://arxiv.org/abs/2605.05623)

## Summary

This study addresses the challenges of generalizing coastal biogeochemical (BGC) parameter retrieval across diverse water bodies by introducing a two-stage physics-aware meta-learning framework. The first stage leverages a bio-optical forward model to pretrain a model on synthetic data that mimics real-world spectral signatures and inter-parameter correlations. The second stage fine-tunes this base model using site-specific in situ measurements, demonstrating superior performance over benchmark retrieval models. Results confirm the framework effectively captures regional distinctions and accurately predicts both the magnitude and temporal dynamics of BGC parameters.

## Key Contributions

- Proposed a two-stage physics-aware meta-learning framework for BGC parameter retrieval that adapts to diverse coastal environments.
- Developed a synthetic dataset generation pipeline based on an Australian coastal bio-optical spectral library to enable robust pretraining.
- Achieved superior performance in BGC parameter estimation compared to five existing benchmark models across five geographically distinct sites.

## Open Questions & Future Work

- [[broaden-optical-regime-evaluation]]

## Key Concepts

- [[physics-aware-meta-learning-for-bgc-retrieval]]: A two-stage framework for biogeochemical (BGC) parameter retrieval that uses bio-optical forward models for synthetic pretraining followed by site-specific fine-tuning.

## Archivist Review

I approved the physics-aware meta-learning framework as it provides a robust, reusable paradigm for domain adaptation in scientific remote sensing. I also approved the open question regarding the evaluation of such models across broader regimes, as it highlights a significant bottleneck in environmental remote sensing generalization. Other candidates were rejected for being too application-specific or falling under standard domain expansion goals.

### Approved Concepts
- Physics-aware meta-learning for BGC retrieval: The framework demonstrates a scalable approach to domain adaptation in remote sensing by combining bio-optical forward models with meta-learning, which is a highly reusable paradigm for environmental parameter estimation.

### Approved Open Questions
- Broaden Optical Regime Evaluation: The limitation of models to specific regional optical water types remains a fundamental barrier to scaling global aquatic monitoring systems.

### Rejected Candidates
- [open_question] Retrieving Optically Inactive Parameters (`retrieval-optically-inactive-parameters`) - low_impact: This is a domain-specific application challenge rather than a fundamental methodological bottleneck for time-series forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2605.05623)
- [PDF](https://arxiv.org/pdf/2605.05623)

