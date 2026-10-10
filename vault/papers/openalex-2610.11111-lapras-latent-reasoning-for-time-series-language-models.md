---
# CSL-compatible fields
title: "Lapras: Latent Reasoning for Time Series Language Models"
author:
  - literal: "Yuliang Chen"
  - literal: "Yu Yvonne Wu"
  - literal: "Patrick Langer"
  - literal: "Arvind Pillai"
  - literal: "Sudarshan Regmi"
  - literal: "Martin Maritsch"
  - literal: "Juncheng Liu"
  - literal: "Robert Jakob"
  - literal: "Thomas Kaar"
  - literal: "Tess Z. Griffin"
  - literal: "Lisa Marsch"
  - literal: "Michael V. Heinz"
  - literal: "Nicholas C. Jacobson"
  - literal: "Andrew Campbell"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.11111"

# Custom fields
paper_id: "2610.11111"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "multimodal"
  - "time-series"
  - "question-answering"
  - "chain-of-thought"
  - "reasoning"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "lapras"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-10T10:52:41Z"
created_at: "2026-10-10T10:52:41Z"
---

# Lapras: Latent Reasoning for Time Series Language Models

**Authors**: Yuliang Chen, Yu Yvonne Wu, Patrick Langer, Arvind Pillai, Sudarshan Regmi, Martin Maritsch, Juncheng Liu, Robert Jakob, Thomas Kaar, Tess Z. Griffin, Lisa Marsch, Michael V. Heinz, Nicholas C. Jacobson, Andrew Campbell
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.11111](https://arxiv.org/abs/2610.11111)

## Summary

Time Series Language Models (TSLMs) struggle with explicit Chain-of-Thought reasoning because converting high-dimensional temporal signals into discrete text tokens often causes error propagation and inaccurate descriptions. To address this, the authors propose Lapras (Latent Post-trained Reasoning Across Series), a post-training framework that replaces explicit textual reasoning with continuous thoughts in the joint time series-language space. Using teacher-student self-distillation, Lapras aligns student hidden states with an explicit CoT teacher, achieving up to 10.79% higher F1 score and 23.9x fewer tokens across five time series question answering benchmarks while maintaining text-interpretable decodings.

## Key Contributions

- Proposes Lapras, a latent post-training framework for Time Series Language Models that replaces explicit text Chain-of-Thought with continuous thoughts in joint time series-language space.
- Employs a teacher-student self-distillation approach where the student aligns hidden states with an explicit CoT teacher at the answer stage.
- Improves average F1 by up to 10.79% over explicit CoT on five time series question answering benchmarks while generating 23.9x fewer tokens.

## Open Questions & Future Work

- [[model-capacity-threshold-latent-reasoning]]

## Key Concepts

- [[lapras]]: A post-training framework for Time Series Language Models that equips them with latent reasoning via teacher-student self-distillation.

## Archivist Review

Approved the central concept note for Lapras and the accompanying open question regarding model capacity thresholds for latent reasoning in time series language models. Applied strict selectivity by filtering out paper-local benchmarks and redundant subcomponents.

### Approved Concepts
- Lapras: Introduces a novel latent post-training framework for Time Series Language Models that replaces explicit text Chain-of-Thought with continuous thoughts in the joint time series-language space.

### Approved Open Questions
- Model Capacity Threshold in Latent Reasoning: Clarifying the minimal parameter capacity required for effective latent reasoning prevents resource wastage and guides the architectural scaling of multimodal time series systems.

### Rejected Candidates
- [concept] Time Series Language Models Latent Reasoning (`time-series-language-models-latent-reasoning`) - subcomponent_of_broader_mechanism: Subsumed by the core framework note for Lapras.

## Links

- [Abstract](https://arxiv.org/abs/2610.11111)
- [PDF](https://arxiv.org/pdf/2610.11111)

