---
# CSL-compatible fields
title: "MetaCaster: Meta-Harness-Optimized Agent for End-to-End Few-Shot Learning of Lightweight Time Series Forecasters"
author:
  - literal: "ChengAo Shen"
  - literal: "Wenchao Yu"
  - literal: "Fangyu Wu"
  - literal: "Dongjin Song"
  - literal: "Hanghang Tong"
  - literal: "Dongsheng Luo"
  - literal: "Wei Cheng"
  - literal: "Haifeng Chen"
  - literal: "Jingchao Ni"
issued:
  date-parts:
    - [2026, 8, 24]
url: "https://arxiv.org/abs/2608.23473"

# Custom fields
paper_id: "2608.23473"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "few-shot-learning"
  - "agent"
  - "multimodal"
architectures:
  []
datasets:
  []
concept_slugs:
  - "metacaster"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-27T15:58:06Z"
created_at: "2026-08-27T15:58:06Z"
---

# MetaCaster: Meta-Harness-Optimized Agent for End-to-End Few-Shot Learning of Lightweight Time Series Forecasters

**Authors**: ChengAo Shen, Wenchao Yu, Fangyu Wu, Dongjin Song, Hanghang Tong, Dongsheng Luo, Wei Cheng, Haifeng Chen, Jingchao Ni
**Date**: 2026-08-24
**Paper ID**: [openalex:2608.23473](https://arxiv.org/abs/2608.23473)

## Summary

MetaCaster introduces a meta-harness-optimized multi-agent framework designed to enable few-shot learning for lightweight time series forecasters under resource constraints. By utilizing agentic data generation guided by textual contexts and a few examples, the framework automates the training of compact, task-specific forecasters without relying on heavy foundation models. Extensive evaluations across 18 datasets and numerous baselines demonstrate high data and computational efficiency.

## Key Contributions

- Proposes MetaCaster, a meta-harness-optimized multi-agent framework for few-shot learning of lightweight time series forecasters using text and few examples.
- Demonstrates a new time series forecasting paradigm where agents function as intermediary engineering harnesses rather than direct forecasters.
- Evaluated across 18 datasets, 23 state-of-the-art lightweight forecasters, and 14 baselines, confirming superior data and computational efficiency.

## Open Questions & Future Work

- [[zero-shot-lightweight-time-series-forecasting]]

## Key Concepts

- [[metacaster]]: A meta-harness-optimized multi-agent framework that uses agentic data generation to automatically train specialized lightweight time series forecasters from few-shot examples and textual contexts.

## Archivist Review

Approved the MetaCaster concept and the open question regarding zero-shot lightweight time series forecasting as they represent distinct, reusable architectural and research contributions. Kept dataset approvals empty because no specific standalone named dataset was highlighted. Maintained strict adherence to vault scarcity rules.

### Approved Concepts
- MetaCaster: Introduces a novel paradigm where multi-agent frameworks act as intermediary engineers to automate the few-shot training of lightweight time series forecasters.

### Approved Open Questions
- Zero-Shot Learning for Lightweight Forecasters: Zero-shot capabilities are crucial for deploying compact models instantly in entirely unseen domains without requiring any historical support data, bypassing the dependency on few-shot examples.

## Links

- [Abstract](https://arxiv.org/abs/2608.23473)
- [PDF](https://arxiv.org/pdf/2608.23473)

