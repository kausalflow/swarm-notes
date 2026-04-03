---
# CSL-compatible fields
title: "One-for-All: A Lightweight Stabilized and Parameter-Efficient Pre-trained LLM for Time Series Forecasting"
author:
  - literal: "Prasanjit Dey"
  - literal: "Soumyabrata Dev"
  - literal: "Bianca Schoen-Phelan"
issued:
  date-parts:
    - [2026, 3, 31]
url: "https://arxiv.org/abs/2603.29756"

# Custom fields
paper_id: "2603.29756"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "time-series"
  - "forecasting"
  - "parameter-efficient-fine-tuning"
  - "peft"
  - "lora"
  - "efficient-transformer"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "gaussian-rs-lora"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-03T06:06:06Z"
created_at: "2026-04-03T06:06:06Z"
---

# One-for-All: A Lightweight Stabilized and Parameter-Efficient Pre-trained LLM for Time Series Forecasting

**Authors**: Prasanjit Dey, Soumyabrata Dev, Bianca Schoen-Phelan
**Date**: 2026-03-31
**Paper ID**: [openalex:2603.29756](https://arxiv.org/abs/2603.29756)

## Summary

The paper introduces One-for-All, a framework for adapting pre-trained LLMs to multivariate time-series forecasting using Gaussian Rank-Stabilized Low-Rank Adapters (rsLoRA). By injecting trainable rank-decomposition matrices only into positional embeddings and output layers while keeping self-attention weights frozen, the method achieves significant parameter and memory efficiency. Evaluations across multiple benchmarks show that the framework maintains competitive forecasting accuracy while providing drastically lower computational requirements, making it suitable for resource-constrained edge devices.

## Key Contributions

- Introduced Gaussian Rank-Stabilized Low-Rank Adapters (rsLoRA) to address gradient instability during low-rank fine-tuning.
- Achieved a 168-1,776x reduction in memory footprint compared to state-of-the-art LLM-based time-series forecasting models.
- Demonstrated state-of-the-art efficiency-accuracy trade-offs across six diverse forecasting tasks, reducing parameters by up to 98.3% over baseline transformers.

## Open Questions & Future Work

- [[universal-time-series-foundation-models]]

## Key Concepts

- [[gaussian-rs-lora]]: A parameter-efficient fine-tuning method that uses a Gaussian-grounded rank-stabilization mechanism to ensure stable gradient updates at low ranks.

## Archivist Review

I have approved the rsLoRA concept as a reusable gradient stabilization method for low-rank fine-tuning and the open question regarding universal time-series foundation models. I rejected the datasets as they are common benchmark collections (ETT, Weather, M3, M4) that do not require standalone vault entries. The approval standard focused on identifying broadly reusable technical improvements and substantial, domain-level research challenges.

### Approved Concepts
- Gaussian Rank-Stabilized Low-Rank Adapters (rsLoRA): It provides a novel mathematical mechanism for gradient stability in low-rank adaptation that outperforms existing PEFT methods in stability and efficiency.

### Approved Open Questions
- Universal Foundation Models for Time-Series: The development of a truly universal, foundation-level model for time series would drastically reduce the engineering burden for deployment in diverse fields where data is often fragmented and scarce.

## Links

- [Abstract](https://arxiv.org/abs/2603.29756)
- [PDF](https://arxiv.org/pdf/2603.29756)

