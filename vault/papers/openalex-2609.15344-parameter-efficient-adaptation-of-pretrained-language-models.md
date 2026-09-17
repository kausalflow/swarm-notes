---
# CSL-compatible fields
title: "Parameter-Efficient Adaptation of Pretrained Language Models for Time-Series Forecasting"
author:
  - literal: "Tamanna Kumavat"
  - literal: "Georg Brunner"
  - literal: "Kyriakos Flouris"
issued:
  date-parts:
    - [2026, 9, 14]
url: "https://arxiv.org/abs/2609.15344"

# Custom fields
paper_id: "2609.15344"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "gpt"
  - "language-model"
  - "pre-training"
  - "fine-tuning"
  - "parameter-efficient-fine-tuning"
  - "peft"
  - "adapter"
  - "benchmark"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:42:56Z"
created_at: "2026-09-17T09:42:56Z"
---

# Parameter-Efficient Adaptation of Pretrained Language Models for Time-Series Forecasting

**Authors**: Tamanna Kumavat, Georg Brunner, Kyriakos Flouris
**Date**: 2026-09-14
**Paper ID**: [openalex:2609.15344](https://arxiv.org/abs/2609.15344)

## Summary

This paper investigates the parameter-efficient adaptation of pretrained language models (GPT-2) for univariate time-series forecasting by projecting time-series patches directly into the model's embedding space. Through controlled ablations across seven benchmarks, the authors show that continuous patch embeddings outperform textual prompting. Furthermore, freezing the backbone and training lightweight adapters achieves competitive accuracy with specialized forecasters while updating under 1% of parameters.

## Key Contributions

- Proposes a parameter-efficient transfer learning framework for adapting pretrained language models (GPT-2) to univariate time-series forecasting by projecting continuous patches directly into the embedding space.
- Demonstrates through controlled ablation studies across seven benchmark datasets that continuous patch-based embeddings consistently outperform textual serialisation and randomly initialised backbones.
- Achieves competitive MASE performance compared to specialised forecasting architectures while updating less than 1% of total model parameters by freezing the pretrained backbone and training lightweight projection and adapter modules.

## Open Questions & Future Work

- [[language-model-pretraining-transfer-mechanism-in-time-series]]

## Archivist Review

Evaluated the paper investigating parameter-efficient adaptation of GPT-2 for time-series forecasting. No distinct standalone concept qualified as a permanent standalone vault note because the architecture leverages standard patch projection and adapters (PEFT). However, the explicit open question regarding cross-modal transfer mechanisms between language pretraining and numerical time series is rigorous and valuable to preserve.

### Approved Open Questions
- Transfer Mechanisms in Language Models: Resolving this question helps establish whether language models learn universal sequence dynamics or simply act as well-conditioned initialisations, guiding future pretraining strategies for multi-modal foundation models.

### Rejected Candidates
- [concept] Parameter-Efficient Adaptation of Pretrained Language Models for Time-Series Forecasting (`parameter-efficient-adaptation-of-pretrained-language-models-for-time-series-forecasting`) - not_novel: The proposed method is an empirical ablation study combining standard PEFT/adapters with time-series patch projection into GPT-2, lacking a distinct standalone algorithmic concept name or reusable primitive.

## Links

- [Abstract](https://arxiv.org/abs/2609.15344)
- [PDF](https://arxiv.org/pdf/2609.15344)

