---
# CSL-compatible fields
title: "Rethinking Post-Training Recipes for Multimodal Time-Series Forecasting"
author:
  - literal: "Haoxin Liu"
  - literal: "Yichen Zhou"
  - literal: "Rajat Sen"
  - literal: "B. Aditya Prakash"
  - literal: "Abhimanyu Das"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.29401"

# Custom fields
paper_id: "2605.29401"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "fine-tuning"
  - "reinforcement-learning-from-human-feedback"
  - "reasoning"
architectures:
  []
datasets:
  - "TimesX"
concept_slugs:
  - "posttime"
dataset_slugs:
  - "timesx"
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:08:30Z"
created_at: "2026-05-31T08:08:30Z"
---

# Rethinking Post-Training Recipes for Multimodal Time-Series Forecasting

**Authors**: Haoxin Liu, Yichen Zhou, Rajat Sen, B. Aditya Prakash, Abhimanyu Das
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.29401](https://arxiv.org/abs/2605.29401)

## Summary

PostTime bridges the gap between unimodal time-series foundation models and multimodal context by utilizing LLMs as intelligent revisors. The approach employs a post-training strategy involving supervised fine-tuning and reinforcement learning with verifiable rewards to enable LLMs to decide whether to adjust, keep, or ignore numeric forecasts based on textual or non-numerical input. By generating reasoning traces for interventions, PostTime demonstrates significant improvements in forecast accuracy on the TimesX benchmark compared to existing unimodal and multimodal baselines.

## Key Contributions

- Introduced PostTime, a post-training recipe utilizing both Supervised Fine-Tuning and Reinforcement Learning with Verifiable Rewards to integrate multimodal context into time-series foundation models.
- Developed a methodology for generating automated reasoning traces to enable context-conditioned forecast interventions (revise, preserve, or ignore).
- Achieved state-of-the-art performance on the TimesX multimodal forecasting benchmark, outperforming unimodal foundation models and standalone LLM baselines.

## Open Questions & Future Work

- [[multimodal-tsf-architectural-limits]]

## Key Concepts

- [[posttime]]: A post-training recipe that uses supervised fine-tuning and reinforcement learning to teach LLMs to act as context-guided revisors for time-series forecasting.

## Archivist Review

The review process prioritized the novel integration paradigm of using LLMs as explicit revisors over foundational time-series model outputs, as this represents a distinct shift in post-training methodology for time-series. The approved open question identifies a core bottleneck regarding the limited scope of current interaction patterns (revision vs. reasoning/tool-use). The TimesX dataset was approved as the central benchmark claim of the paper.

### Approved Concepts
- PostTime: It introduces a novel post-training paradigm for integrating multimodal context into unimodal time-series foundation models by training LLMs to act as context-conditioned revisors over numerical priors.

### Approved Open Questions
- Beyond simple forecast revision: This addresses a fundamental architectural limitation; as forecasting moves beyond simple text-numerical alignment, the current 'reviser' paradigm may lack the flexibility required for more complex reasoning or external data retrieval.

## Datasets

- [[timesx]]

## Links

- [Abstract](https://arxiv.org/abs/2605.29401)
- [PDF](https://arxiv.org/pdf/2605.29401)

