---
# CSL-compatible fields
title: "SDFlow: Similarity-Driven Flow Matching for Time Series Generation"
author:
  - literal: "Wei Li"
  - literal: "Shibo Feng"
  - literal: "Pengcheng Wu"
  - literal: "Min Wu"
  - literal: "Peilin Zhao"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.05736"

# Custom fields
paper_id: "2605.05736"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "time-series"
  - "forecasting"
  - "generative-adversarial-network"
  - "diffusion-model"
  - "embedding"
architectures:
  []
datasets:
  []
concept_slugs:
  - "sdflow-similarity-driven-flow-matching"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:21:01Z"
created_at: "2026-05-10T07:21:01Z"
---

# SDFlow: Similarity-Driven Flow Matching for Time Series Generation

**Authors**: Wei Li, Shibo Feng, Pengcheng Wu, Min Wu, Peilin Zhao
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.05736](https://arxiv.org/abs/2605.05736)

## Summary

SDFlow is a non-autoregressive framework for time series generation that addresses the exposure bias and error accumulation issues inherent in autoregressive vector quantization (VQ) models. By operating within a frozen VQ latent space and utilizing flow matching, it replaces step-wise predictions with a global transport map for efficient parallel generation. The model further optimizes performance through low-rank manifold decomposition and a categorical posterior formulation that bridges discrete and continuous domains. Experiments demonstrate that SDFlow provides superior fidelity and inference speed compared to traditional autoregressive baselines.

## Key Contributions

- Introduces SDFlow, a non-autoregressive framework that enables parallel time series generation in a frozen VQ latent space using flow matching.
- Employs low-rank manifold decomposition and learned anchor priors to effectively manage high-dimensional discrete latent spaces.
- Integrates discrete supervision into continuous transport via a categorical posterior over codebook indices, achieving SOTA results in Discriminative Score and Context-FID for long-sequence generation.

## Open Questions & Future Work

- [[universal-time-series-tokenizer]]

## Key Concepts

- [[sdflow-similarity-driven-flow-matching]]: A non-autoregressive generative framework for time series that uses flow matching in a frozen VQ latent space to eliminate exposure bias.

## Archivist Review

I approved the core SDFlow framework as it represents a shift from autoregressive generation to parallel flow matching in latent spaces, which is a significant and reusable architectural advancement for time series. I also approved the universal tokenizer open question, as it highlights a concrete architectural dependency bottleneck in modern generative time-series modeling. Other candidates were rejected for being overly generic.

### Approved Concepts
- Similarity-Driven Flow Matching (SDFlow): Introduces a novel paradigm for non-autoregressive time series generation that avoids exposure bias by utilizing global transport maps instead of step-wise token prediction.

### Approved Open Questions
- Universal Time-Series Tokenizer: Developing a universal tokenizer is a key bottleneck toward multi-domain generative modeling and improving the generalizability of latent-space generation frameworks.

### Rejected Candidates
- [open_question] Time Series Forecasting Adaptation (`forecasting-architectural-modifications`) - generic: This is generic future work proposing 'more specific modifications' without outlining a clear, defined technical bottleneck or research direction.

## Links

- [Abstract](https://arxiv.org/abs/2605.05736)
- [PDF](https://arxiv.org/pdf/2605.05736)

