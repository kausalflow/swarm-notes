---
# CSL-compatible fields
title: "ReDiTT: Retrieval Augmented Conditional Diffusion Transformers for Asynchronous Time Series"
author:
  - literal: "Saiyue Lyu"
  - literal: "Zhitian Zhang"
  - literal: "Ruizhi Deng"
  - literal: "Thibaut Durand"
issued:
  date-parts:
    - [2026, 7, 14]
url: "https://arxiv.org/abs/2607.12391"

# Custom fields
paper_id: "2607.12391"
paper_source: "openalex"
domain: "time-series,nlp"
tags:
  - "diffusion-model"
  - "transformer"
  - "retrieval-augmented-generation"
  - "time-series"
  - "attention-mechanism"
  - "long-context"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "retrieval-augmented-conditional-diffusion-transformer"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-17T07:09:15Z"
created_at: "2026-07-17T07:09:15Z"
---

# ReDiTT: Retrieval Augmented Conditional Diffusion Transformers for Asynchronous Time Series

**Authors**: Saiyue Lyu, Zhitian Zhang, Ruizhi Deng, Thibaut Durand
**Date**: 2026-07-14
**Paper ID**: [openalex:2607.12391](https://arxiv.org/abs/2607.12391)

## Summary

ReDiTT addresses the challenges of asynchronous time-series prediction—specifically inter-event time and event type—by utilizing a retrieval-augmented conditional diffusion transformer in latent space. The model enhances generation by retrieving structurally similar historical sequences from a memory bank, which are used as reference conditions through a cross-attention mechanism. This approach provides global structural guidance, effectively stabilizing long-horizon forecasts and improving sample diversity. Empirical results across seven datasets confirm that ReDiTT outperforms existing baselines in next-event prediction and long-term forecasting accuracy.

## Key Contributions

- Introduces ReDiTT, a retrieval-augmented conditional diffusion transformer architecture that operates in latent space for asynchronous time-series prediction.
- Enables effective cross-attention based conditioning on structurally similar retrieved latent sequences to provide global guidance for generation.
- Achieves state-of-the-art performance on seven real-world datasets for both next-event prediction and long-horizon forecasting tasks.

## Open Questions & Future Work

- [[robust-retrieval-analog-forecasting-limits]]

## Key Concepts

- [[retrieval-augmented-conditional-diffusion-transformer]]: A latent-space diffusion transformer that uses retrieval from a memory bank of structurally similar sequences to condition asynchronous event forecasting.

## Archivist Review

The paper's core contribution is the retrieval-augmented conditioning mechanism for diffusion transformers in asynchronous time-series, which is a highly reusable architectural pattern. I approved the generic architectural concept and an open question regarding the limits of this retrieval-augmented strategy, while rejecting the model-specific name to maintain vault neutrality.

### Approved Concepts
- Retrieval-Augmented Conditional Diffusion Transformer: Integrates structural retrieval mechanisms into diffusion-based time-series forecasting, offering a way to guide generation with non-parametric historical references.

### Approved Open Questions
- Limits of Analog Retrieval Forecasting: This bottleneck addresses the core limitation of retrieval-augmented forecasting, moving beyond empirical performance to understanding the stability of these mechanisms.

### Rejected Candidates
- [concept] Retrieval Augmented Conditional Diffusion Transformers (ReDiTT) (`reditt-retrieval-augmented-conditional-diffusion-transformers`) - duplicate_existing: Redundant with the approved concept title; using the generic name instead of the model name.

## Links

- [Abstract](https://arxiv.org/abs/2607.12391)
- [PDF](https://arxiv.org/pdf/2607.12391)

