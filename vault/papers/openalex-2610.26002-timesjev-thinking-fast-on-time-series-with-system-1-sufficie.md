---
# CSL-compatible fields
title: "TimesJev: Thinking Fast on Time Series with System 1 Sufficiency"
author:
  - literal: "Chenghao Liu"
  - literal: "Wei Fan"
  - literal: "Jindong Han"
  - literal: "Dongjie Wang"
  - literal: "Aniket Mahanti"
  - literal: "Pengyang Wang"
  - literal: "Hao Liu"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2610.26002"

# Custom fields
paper_id: "2610.26002"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "reasoning"
  - "long-context"
  - "efficiency"
  - "llm"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "timesjev"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-22T09:43:40Z"
created_at: "2026-10-22T09:43:40Z"
---

# TimesJev: Thinking Fast on Time Series with System 1 Sufficiency

**Authors**: Chenghao Liu, Wei Fan, Jindong Han, Dongjie Wang, Aniket Mahanti, Pengyang Wang, Hao Liu
**Date**: 2026-10-19
**Paper ID**: [openalex:2610.26002](https://arxiv.org/abs/2610.26002)

## Summary

Large language models often rely on lengthy chains of thought for time series reasoning, causing significant inference latency, whereas fast System 1 models struggle with raw numerical compatibility. To address this, the authors propose TimesJev, a time series System 1 model that compresses time series while preserving key frequency patterns. By formulating a joint objective based on sufficiency divergence and realizability divergence, TimesJev optimizes compression and embedding alignment. Experiments across 13 datasets show that TimesJev outperforms existing reasoning models by over 62% while requiring 62.9% less inference time.

## Key Contributions

- Proposes TimesJev, a time series System 1 model that bypasses expensive long chains of thought to achieve fast inference.
- Formalizes System 1 sufficiency in time series reasoning using a dimension reduction objective combining sufficiency divergence and realizability divergence.
- Demonstrates superior performance across 13 datasets, outperforming reasoning models by over 62% while reducing inference time by 62.9%.

## Open Questions & Future Work

- [[system-1-sufficiency-for-free-form-tasks]]

## Key Concepts

- [[timesjev]]: A time series System 1 model that achieves fast inference by formalizing sufficiency and realizability objectives for compressed representation learning.

## Archivist Review

Evaluated candidates under strict knowledge vault standards. Approved the overarching TimesJev framework concept and the open question regarding the extension of System 1 sufficiency to free-form tasks, while rejecting the subcomponent concept as requested by the critic review policy.

### Approved Concepts
- TimesJev: Introduces a novel System 1 model framework for time series reasoning that replaces expensive long chains of thought with fast, compressed representations.

### Approved Open Questions
- System 1 Sufficiency for Free-Form Tasks: Generalizing System 1 efficiency to generative and continuous tasks is critical for broad applicability across modern time series analytics beyond simple classification or multi-choice QA.

### Rejected Candidates
- [concept] System 1 Sufficiency (`system-1-sufficiency`) - subcomponent_of_broader_mechanism: Subcomponent of the broader TimesJev methodological framework.

## Links

- [Abstract](https://arxiv.org/abs/2610.26002)
- [PDF](https://arxiv.org/pdf/2610.26002)

