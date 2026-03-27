---
# CSL-compatible fields
title: "Unlocking the Value of Text: Event-Driven Reasoning and Multi-Level Alignment for Time Series Forecasting"
author:
  - literal: "Siyuan Wang"
  - literal: "Peng Chen"
  - literal: "Yihang Wang"
  - literal: "Wanghui Qiu"
  - literal: "Chenjuan Guo"
  - literal: "Bin Yang"
  - literal: "Yang Shu"
issued:
  date-parts:
    - [2026, 3, 16]
url: "https://arxiv.org/abs/2603.15452"

# Custom fields
paper_id: "2603.15452"
paper_source: "openalex"
domain: "time-series"
tags:
  - "multimodal"
  - "llm"
  - "reasoning"
  - "forecasting"
  - "in-context-learning"
  - "time-series"
  - "alignment"
architectures:
  []
datasets:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:08:58Z"
created_at: "2026-03-27T14:08:58Z"
---

# Unlocking the Value of Text: Event-Driven Reasoning and Multi-Level Alignment for Time Series Forecasting

**Authors**: Siyuan Wang, Peng Chen, Yihang Wang, Wanghui Qiu, Chenjuan Guo, Bin Yang, Yang Shu
**Date**: 2026-03-16
**Paper ID**: [openalex:2603.15452](https://arxiv.org/abs/2603.15452)

## Summary

This paper introduces VoT, a method designed to unlock the value of multimodal text information for time series forecasting, addressing the limitations of current methods that primarily rely on numerical data. VoT employs Event-driven Reasoning, leveraging Large Language Models (LLMs) guided by Historical In-context Learning to process exogenous text. It further implements Multi-level Alignment, integrating endogenous text via Endogenous Text Alignment and fusing frequency components of different predictions using Adaptive Frequency Fusion. Experimental results across ten real-world domains show substantial performance gains, validating the approach's effectiveness in utilizing complex textual context for improved forecasting accuracy.

## Key Contributions

- Proposal of VoT, a novel time series forecasting method that explicitly leverages textual information through Event-driven Reasoning and Multi-level Alignment.
- Introduction of Historical In-context Learning to provide LLMs with relevant past examples for context-aware forecasting reasoning.
- Development of Multi-level Alignment, featuring Endogenous Text Alignment at the representation level and Adaptive Frequency Fusion at the prediction level to maximize text utilization.
- Demonstration of significant performance improvements over existing methods across real-world datasets spanning 10 different domains.

## Limitations

The reliance on rich exogenous text and the computational overhead associated with integrating LLMs for event-driven reasoning might limit applicability in resource-constrained or purely numerical forecasting scenarios.

## Open Questions & Future Work

- [[hic-robustness-extreme-noise-sparsity]]
- [[aff-non-linear-fusion-potential]]
- [[pure-llm-event-driven-forecasting]]
- [[eta-alternative-decomposition-strategies]]

## Key Concepts

- [Event-driven Reasoning](../concepts/event-driven-reasoning-time-series.md): A mechanism that combines rich exogenous text information with the reasoning capabilities of Large Language Models (LLMs) to enhance time series forecasting.
- [Historical In-context Learning](../concepts/historical-in-context-learning-forecasting.md): A technique used to guide LLMs in effective reasoning for time series forecasting by retrieving and applying relevant historical examples as in-context guidance.
- [Endogenous Text Alignment](../concepts/endogenous-text-alignment.md): A representation-level alignment technique designed to integrate intrinsic, endogenous text information directly with the time series data.
- [Adaptive Frequency Fusion](../concepts/adaptive-frequency-fusion-forecasting.md): A prediction-level fusion mechanism that combines the frequency components derived from event-driven predictions and purely numerical predictions.

## Limitations

The reliance on rich exogenous text and the computational overhead associated with integrating LLMs for event-driven reasoning might limit applicability in resource-constrained or purely numerical forecasting scenarios.

## Links

- [Abstract](https://arxiv.org/abs/2603.15452)
- [PDF](https://arxiv.org/pdf/2603.15452)

