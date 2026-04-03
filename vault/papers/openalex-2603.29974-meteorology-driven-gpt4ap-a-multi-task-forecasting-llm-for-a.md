---
# CSL-compatible fields
title: "Meteorology-Driven GPT4AP: A Multi-Task Forecasting LLM for Atmospheric Air Pollution in Data-Scarce Settings"
author:
  - literal: "Prasanjit Dey"
  - literal: "Soumyabrata Dev"
  - literal: "Bianca Schoen-Phelan"
issued:
  date-parts:
    - [2026, 3, 31]
url: "https://arxiv.org/abs/2603.29974"

# Custom fields
paper_id: "2603.29974"
paper_source: "openalex"
domain: "time-series,nlp"
tags:
  - "llm"
  - "language-model"
  - "gpt"
  - "time-series"
  - "forecasting"
  - "parameter-efficient-fine-tuning"
  - "peft"
  - "lora"
  - "few-shot-learning"
  - "zero-shot-learning"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "rank-stabilized-lora-rslora"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-03T06:06:49Z"
created_at: "2026-04-03T06:06:49Z"
---

# Meteorology-Driven GPT4AP: A Multi-Task Forecasting LLM for Atmospheric Air Pollution in Data-Scarce Settings

**Authors**: Prasanjit Dey, Soumyabrata Dev, Bianca Schoen-Phelan
**Date**: 2026-03-31
**Paper ID**: [openalex:2603.29974](https://arxiv.org/abs/2603.29974)

## Summary

GPT4AP is a parameter-efficient forecasting framework designed for atmospheric air pollution in data-scarce environments by repurposing a pre-trained GPT-2 model. The framework leverages Gaussian rank-stabilized LoRA (rsLoRA) to adapt specific positional and output modules while freezing the backbone's transformer layers. Evaluation across multiple air quality datasets demonstrates that GPT4AP significantly outperforms conventional time-series models like DLinear and ETSformer in few-shot and zero-shot transfer scenarios, while remaining competitive in full-data long-term forecasting.

## Key Contributions

- Introduces GPT4AP, a parameter-efficient multi-task forecasting framework for air pollution utilizing a pre-trained GPT-2 backbone.
- Employs Gaussian rank-stabilized LoRA (rsLoRA) to adapt the backbone while freezing core self-attention and feed-forward layers.
- Outperforms DLinear and ETSformer in few-shot air quality forecasting (10% training data) with average MSE of 0.686.
- Demonstrates robust zero-shot cross-station transfer capabilities with an average MSE of 0.529.

## Open Questions & Future Work

- [[integrating-temporal-inductive-biases-into-llms]]

## Key Concepts

- [[rank-stabilized-lora-rslora]]: A parameter-efficient fine-tuning technique that stabilizes low-rank updates via Gaussian-scaled rank normalization.

## Archivist Review

I approved the concept of Rank-Stabilized LoRA (rsLoRA) due to its architectural significance for stable fine-tuning of foundation models in constrained settings, and the open question regarding the integration of temporal inductive biases as it represents a fundamental challenge in current time-series foundation model research. I rejected the local dataset references and generic LLM-for-forecasting terminology, focusing only on the mechanisms and research bottlenecks that hold cross-domain relevance.

### Approved Concepts
- Rank-Stabilized LoRA (rsLoRA): Provides a stable, parameter-efficient mechanism for fine-tuning pre-trained backbone models in low-data forecasting regimes.

### Approved Open Questions
- Integrating temporal inductive biases into LLMs: This is a critical bottleneck for scaling LLM-based forecasters to compete with established state-of-the-art time-series models across all performance regimes.

### Rejected Candidates
- [concept] Gaussian Rank-Stabilized LoRA (rsLoRA) (`rs-lora`) - duplicate_existing: Replaced with a more standard naming convention (rank-stabilized-lora-rslora).

## Links

- [Abstract](https://arxiv.org/abs/2603.29974)
- [PDF](https://arxiv.org/pdf/2603.29974)

