---
# CSL-compatible fields
title: "VL-DPO: Vision-Language-Guided Finetuning for Preference-Aligned Autonomous Driving"
author:
  - literal: "Zhefan Xu"
  - literal: "Ghassen Jerfel"
  - literal: "Marina Haliem"
  - literal: "Qi Zhao"
  - literal: "Jeonhyung Kang"
  - literal: "Khaled S. Refaat"
issued:
  date-parts:
    - [2026, 5, 19]
url: "https://arxiv.org/abs/2605.20082"

# Custom fields
paper_id: "2605.20082"
paper_source: "openalex"
domain: "robotics"
tags:
  - "llm"
  - "vision-language-model"
  - "fine-tuning"
  - "rlhf"
  - "autonomous-agent"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  - "Waymo Open End-to-End Driving Dataset"
concept_slugs:
  - "vl-dpo"
dataset_slugs:
  - "waymo-open-end-to-end-driving-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-05-22T08:17:28Z"
created_at: "2026-05-22T08:17:28Z"
---

# VL-DPO: Vision-Language-Guided Finetuning for Preference-Aligned Autonomous Driving

**Authors**: Zhefan Xu, Ghassen Jerfel, Marina Haliem, Qi Zhao, Jeonhyung Kang, Khaled S. Refaat
**Date**: 2026-05-19
**Paper ID**: [openalex:2605.20082](https://arxiv.org/abs/2605.20082)

## Summary

This paper proposes VL-DPO, a framework that aligns motion forecasting models for autonomous driving with human preferences by leveraging vision-language models (VLMs) as zero-shot reasoners. The method automatically generates trajectory preference pairs from a pretrained model's outputs, which are then used to finetune the model via Direct Preference Optimization (DPO). Evaluated on the Waymo Open End-to-End Driving Dataset, VL-DPO significantly outperforms imitation-based baselines in both trajectory accuracy and human-preference alignment scores.

## Key Contributions

- Introduces VL-DPO, a framework aligning ego-vehicle motion forecasting models with human preferences using VLM-generated preference pairs.
- Demonstrates that VLM-based trajectory selection serves as a high-quality, automated proxy for human preference annotations.
- Achieves an 11.94% increase in rater feedback score (RFS) and a 10.01% reduction in average displacement error (ADE) on the WOD-E2E benchmark compared to standard imitation learning baselines.

## Open Questions & Future Work

- [[vlm-integration-vs-specialization]]

## Key Concepts

- [[vl-dpo]]: A framework that uses VLM reasoning to generate preference pairs for alignment of motion forecasting models via Direct Preference Optimization.

## Archivist Review

I approved the core framework VL-DPO as it provides a clear, reusable pattern for aligning forecasting models using VLM-based preference signals. The Waymo Open End-to-End Driving Dataset is approved as a central, named benchmark. I also approved the open question regarding VLM-specialized task integration, as this is a high-level architectural challenge that will define the next wave of autonomous forecasting research.

### Approved Concepts
- VL-DPO: Core framework that bridges VLM reasoning with DPO for preference alignment in autonomous driving.

### Approved Open Questions
- Optimal VLM Integration Paradigms: This is critical because it highlights a fundamental trade-off in current AI architecture design between model capacity, real-time deployment constraints, and the preservation of foundational world knowledge in specialized applications.

## Datasets

- [[waymo-open-end-to-end-driving-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2605.20082)
- [PDF](https://arxiv.org/pdf/2605.20082)

