---
# CSL-compatible fields
title: "TimeLLM: Time Series Forecasting by Reprogramming Large Language Models"
author:
  - literal: "Ming Jin"
  - literal: "Shiyu Wang"
  - literal: "Lintao Ma"
  - literal: "Zhixuan Chu"
  - literal: "James Y. Zhang"
  - literal: "Xiaoming Shi"
  - literal: "Pin‐Yu Chen"
  - literal: "Yuxuan Liang"
  - literal: "Yuan-Fang Li"
  - literal: "Shirui Pan"
  - literal: "Qingsong Wen"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2310.01728"

# Custom fields
paper_id: "2310.01728"
paper_source: "openalex"
domain: "time-series"
tags:
  - "llm"
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "prompt-tuning"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "timellm"
  - "prompt-as-prefix"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:25:45Z"
created_at: "2026-05-21T08:25:45Z"
---

# TimeLLM: Time Series Forecasting by Reprogramming Large Language Models

**Authors**: Ming Jin, Shiyu Wang, Lintao Ma, Zhixuan Chu, James Y. Zhang, Xiaoming Shi, Pin‐Yu Chen, Yuxuan Liang, Yuan-Fang Li, Shirui Pan, Qingsong Wen
**Date**: 2026-05-18
**Paper ID**: [openalex:2310.01728](https://arxiv.org/abs/2310.01728)

## Summary

Time-LLM addresses the scarcity of high-quality time series corpora by repurposing frozen LLMs for forecasting via a model reprogramming framework. It maps raw time series data into text-like prototypes and utilizes a Prompt-as-Prefix (PaP) mechanism to guide the LLM's reasoning over these representations. This approach effectively leverages the extensive reasoning capabilities of large language models for time series tasks, achieving superior performance compared to existing specialized baseline models.

## Key Contributions

- Introduced Time-LLM, a reprogramming framework that repurposes frozen LLM backbones for time series forecasting.
- Developed the Prompt-as-Prefix (PaP) mechanism to align time series inputs with linguistic tokens and provide necessary context for LLM-based reasoning.
- Demonstrated that Time-LLM outperforms domain-specific baseline models on standard forecasting benchmarks.

## Key Concepts

- [[timellm]]: A model reprogramming framework that maps time series signals into text-like prototypes to leverage frozen LLM capabilities for forecasting.
- [[prompt-as-prefix]]: A technique to augment time series inputs with contextual information, directing the LLM's reasoning and reprogramming process.

## Archivist Review

I approved the core framework (Time-LLM) and its primary conditioning mechanism (Prompt-as-Prefix) as they introduce a distinct and influential paradigm for cross-modal LLM repurposing. These concepts represent reusable architectural strategies that have already begun to define a class of models in the time series community. No datasets were approved as none were distinct or central enough to serve as a standalone knowledge reference, and no open questions were provided in the candidate list.

### Approved Concepts
- Time-LLM: Establishes a foundational paradigm for repurposing frozen LLMs for time series through signal-to-token reprogramming.
- Prompt-as-Prefix (PaP): Essential mechanism for injecting task-specific context and directing reasoning in frozen LLMs during reprogramming.

## Links

- [Abstract](https://arxiv.org/abs/2310.01728)
- [PDF](https://arxiv.org/pdf/2310.01728)

