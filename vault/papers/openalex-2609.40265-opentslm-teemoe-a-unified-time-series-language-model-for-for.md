---
# CSL-compatible fields
title: "OpenTSLM TeeMoE: A Unified Time-Series Language Model for Forecasting, Contextual Prediction, and Reasoning"
author:
  - literal: "Tony Chen"
  - literal: "Timo Stoffregen"
  - literal: "Maxwell Xu"
  - literal: "Thomas Kaar"
  - literal: "Martin Maritsch"
  - literal: "Geremia Pompei"
  - literal: "Nicolas Zumarraga"
  - literal: "Robert Jakob"
  - literal: "Paul Schmiedmayer"
  - literal: "Patrick Langer"
  - literal: "Juncheng Liu"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2609.40265"

# Custom fields
paper_id: "2609.40265"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "llm"
  - "language-model"
  - "mixture-of-experts"
  - "moe"
  - "lora"
  - "multimodal"
  - "benchmark"
  - "evaluation"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "opentslm-teemoe"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:07:18Z"
created_at: "2026-10-03T10:07:18Z"
---

# OpenTSLM TeeMoE: A Unified Time-Series Language Model for Forecasting, Contextual Prediction, and Reasoning

**Authors**: Tony Chen, Timo Stoffregen, Maxwell Xu, Thomas Kaar, Martin Maritsch, Geremia Pompei, Nicolas Zumarraga, Robert Jakob, Paul Schmiedmayer, Patrick Langer, Juncheng Liu
**Date**: 2026-09-30
**Paper ID**: [openalex:2609.40265](https://arxiv.org/abs/2609.40265)

## Summary

The paper introduces OpenTSLM TeeMoE, a unified time-series language model that bridges the gap between numerical forecasting specialists and text-based reasoning models. It employs three independently trained low-rank experts—handling forecast aggregation, native forecasting, and temporal analysis—dynamically combined via a learned LoRA mixture-of-experts controller over a shared backbone. Evaluations across GIFT-Eval, Context is Key, and TimeSeriesExam demonstrate that OpenTSLM TeeMoE achieves strong performance across forecasting, context-conditioned prediction, and temporal reasoning.

## Key Contributions

- Introduces OpenTSLM TeeMoE, a unified time-series language model capable of forecasting, contextual prediction, and language-based temporal reasoning.
- Employs three independently trained low-rank experts for forecast aggregation, native forecasting, and temporal analysis over a shared backbone.
- Utilizes a learned LoRA mixture-of-experts controller to dynamically weight frozen parameter updates for each request.
- Achieves top-three rankings on established benchmarks including GIFT-Eval (mean MASE rank), Context is Key (RCRPS), and TimeSeriesExam (accuracy).

## Open Questions & Future Work

- [[capability-dilution-general-purpose-tslms]]

## Key Concepts

- [[opentslm-teemoe]]: A generalist time-series language model that unifies forecasting, contextual prediction, and textual temporal reasoning via a LoRA mixture-of-experts architecture.

## Archivist Review

Approved the central model concept OpenTSLM TeeMoE and the associated open question on capability dilution in multi-task time-series language models. Kept selections strictly to the top-tier contribution without accepting benchmark-level datasets or peripheral modules.

### Approved Concepts
- OpenTSLM TeeMoE: Serves as the core architectural framework of the paper, unifying numerical forecasting, contextual prediction, and language-based temporal reasoning via a LoRA-based mixture-of-experts controller over a shared backbone.

### Approved Open Questions
- Preventing Capability Dilution in TSLMs: Understanding the trade-offs between modular mixture-of-experts and joint multi-task training is foundational for scaling time-series foundation models to handle complex downstream workflows involving both numerical prediction and textual reasoning.

## Links

- [Abstract](https://arxiv.org/abs/2609.40265)
- [PDF](https://arxiv.org/pdf/2609.40265)

