---
# CSL-compatible fields
title: "Instance-Adaptive Prompts as Context for Time-Series Foundation Models"
author:
  - literal: "Zehao Xiao"
  - literal: "Shifeng Xie"
  - literal: "Lei Zan"
  - literal: "Jianfeng Zhang"
  - literal: "Lujia Pan"
  - literal: "Ievgen Redko"
  - literal: "Malik Tiomoko"
  - literal: "Keli Zhang"
  - literal: "Shifeng Xie"
  - literal: "Lei Zan"
  - literal: "Jianfeng Zhang"
  - literal: "Lujia Pan"
  - literal: "Ievgen Redko"
  - literal: "Malik Tiomoko"
  - literal: "Keli Zhang"
issued:
  date-parts:
    - [2026, 9, 28]
url: "https://arxiv.org/abs/2609.34786"

# Custom fields
paper_id: "2609.34786"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "foundation-model"
  - "prompt-tuning"
  - "efficient-transformer"
  - "long-context"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "pacts"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:49:01Z"
created_at: "2026-09-30T10:49:01Z"
---

# Instance-Adaptive Prompts as Context for Time-Series Foundation Models

**Authors**: Zehao Xiao, Shifeng Xie, Lei Zan, Jianfeng Zhang, Lujia Pan, Ievgen Redko, Malik Tiomoko, Keli Zhang, Shifeng Xie, Lei Zan, Jianfeng Zhang, Lujia Pan, Ievgen Redko, Malik Tiomoko, Keli Zhang
**Date**: 2026-09-28
**Paper ID**: [openalex:2609.34786](https://arxiv.org/abs/2609.34786)

## Summary

This paper introduces PaCTS, a prompt-based framework that replaces long historical contexts in time-series foundation models with a compact set of instance-adaptive latent prompts. By constructing these prompts from global statistics and segment-level temporal variations, PaCTS enables frozen backbones to achieve superior forecasting performance and out-of-distribution generalization while significantly reducing inference computation. Extensive experiments show that PaCTS with shorter input context can outperform models using double the context length.

## Key Contributions

- Introduces PaCTS, a method that generates instance-adaptive latent prompts from global statistics and segment-level temporal variations as compact context surrogates for time-series foundation models.
- Demonstrates that PaCTS enables a frozen backbone with shorter input context to outperform the same backbone using double the context length with substantially lower inference computation.
- Outperforms weight-space adaptation methods in forecasting accuracy and out-of-distribution generalization across diverse time-series architectures.

## Open Questions & Future Work

- [[multivariate-prompt-learning-tsfm]]

## Key Concepts

- [[pacts]]: A method that generates instance-adaptive latent prompts as compact context surrogates for frozen time-series foundation models to reduce inference cost.

## Archivist Review

Approved the core concept 'PaCTS' as a central, reusable prompt-based context mechanism for time-series foundation models, along with the open question on extending it to multivariate settings. No datasets met the strict naming and scarcity criteria.

### Approved Concepts
- PaCTS: Introduces a novel prompt-based conditioning mechanism that replaces long input histories with compact learned token embeddings for time-series foundation models.

### Approved Open Questions
- Multivariate Prompt Learning for TSFMs: Extending prompt-based context surrogates to natively support multivariate time-series data is crucial for handling complex multi-variate dependencies and cross-channel correlations without relying solely on univariate-trained transfer.

## Links

- [Abstract](https://arxiv.org/abs/2609.34786)
- [PDF](https://arxiv.org/pdf/2609.34786)

