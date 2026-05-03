---
# CSL-compatible fields
title: "CastFlow: Learning Role-Specialized Agentic Workflows for Time Series Forecasting"
author:
  - literal: "潘柏凱"
  - literal: "Mingyue Cheng"
  - literal: "Zhiding Liu"
  - literal: "Shuo Yu"
  - literal: "Xiaoyu Tao"
  - literal: "Yuchong Wu"
  - literal: "Qi Liu"
  - literal: "Defu Lian"
  - literal: "Enhong Chen"
issued:
  date-parts:
    - [2026, 4, 30]
url: "https://arxiv.org/abs/2604.27840"

# Custom fields
paper_id: "2604.27840"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "time-series"
  - "forecasting"
  - "agent"
  - "reinforcement-learning-from-human-feedback"
  - "instruction-tuning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "castflow"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-03T07:13:39Z"
created_at: "2026-05-03T07:13:39Z"
---

# CastFlow: Learning Role-Specialized Agentic Workflows for Time Series Forecasting

**Authors**: 潘柏凱, Mingyue Cheng, Zhiding Liu, Shuo Yu, Xiaoyu Tao, Yuchong Wu, Qi Liu, Defu Lian, Enhong Chen
**Date**: 2026-04-30
**Paper ID**: [openalex:2604.27840](https://arxiv.org/abs/2604.27840)

## Summary

CastFlow replaces the static, one-shot generative paradigm of LLM-based time series forecasting with a dynamic, agentic workflow. The framework decomposes forecasting into planning, action, numerical forecasting, and reflection stages, supported by a memory module and a multi-view toolkit. It employs a specialized architecture utilizing a frozen reasoning LLM alongside a domain-specific numerical LLM, optimized through a novel two-stage SFT and RLVR training process. Extensive experiments demonstrate that this agentic approach significantly improves forecasting accuracy compared to standard generative baselines.

## Key Contributions

- Proposes CastFlow, an agentic forecasting framework that utilizes planning, multi-view toolkit, and iterative reflection to overcome limitations of static LLM-based forecasting.
- Implements a role-specialized design where a frozen LLM handles reasoning and a fine-tuned domain-specific LLM performs evidence-guided numerical forecasting.
- Develops a two-stage training paradigm (SFT + RLVR) that aligns agentic workflows with verifiable numerical forecasting rewards.

## Open Questions & Future Work

- [[llm-reasoning-numerical-tradeoff]]

## Key Concepts

- [[castflow]]: A dynamic agentic forecasting framework that decomposes the forecasting process into planning, action, numerical forecasting, and iterative reflection.

## Archivist Review

The paper presents a significant shift from static one-shot generation to a dynamic, agentic forecasting workflow. I have approved the framework itself as a core concept and the identified reasoning-vs-numerical bottleneck as a fundamental open question, as these are likely to recur in future agentic time-series literature. Other candidate contributions were deemed either too specific to this implementation or subcomponents of the overarching framework.

### Approved Concepts
- CastFlow: It introduces an agentic workflow paradigm to time series forecasting, departing from static one-shot generation.

### Approved Open Questions
- Reasoning vs Numerical Precision Tradeoff: This is the core unresolved bottleneck identified by the paper, motivating the need for role-specialized designs in agentic forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2604.27840)
- [PDF](https://arxiv.org/pdf/2604.27840)

