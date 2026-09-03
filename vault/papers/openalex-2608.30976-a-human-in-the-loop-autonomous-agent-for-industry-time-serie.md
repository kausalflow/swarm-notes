---
# CSL-compatible fields
title: "A Human-in-the-Loop Autonomous Agent for Industry Time Series Forecasting"
author:
  - literal: "Xiaoyu Tao"
  - literal: "Mingyue Cheng"
  - literal: "Ze Guo"
  - literal: "潘柏凱"
  - literal: "Qi Liu"
  - literal: "Shijin Wang"
  - literal: "Enhong Chen"
issued:
  date-parts:
    - [2026, 8, 31]
url: "https://arxiv.org/abs/2608.30976"

# Custom fields
paper_id: "2608.30976"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "agent"
  - "autonomous-agent"
  - "llm"
  - "multimodal"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "castclaw"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-03T09:16:45Z"
created_at: "2026-09-03T09:16:45Z"
---

# A Human-in-the-Loop Autonomous Agent for Industry Time Series Forecasting

**Authors**: Xiaoyu Tao, Mingyue Cheng, Ze Guo, 潘柏凱, Qi Liu, Shijin Wang, Enhong Chen
**Date**: 2026-08-31
**Paper ID**: [openalex:2608.30976](https://arxiv.org/abs/2608.30976)

## Summary

The paper introduces CastClaw, a human-in-the-loop autonomous forecasting system designed to bridge the gap between fixed specialized time-series models and general-purpose LLM agents. CastClaw utilizes forecasting-oriented harness engineering to connect data, models, tools, and natural language user constraints within an inspectable, versioned runtime. Operating under explicit stopping conditions, the agent iteratively checks, retrieves context, revises, or escalates predictions, outperforming 16 baselines on a five-dataset electricity-price benchmark and demonstrating practical utility on real-world provincial electricity load data.

## Key Contributions

- Proposes CastClaw, a human-in-the-loop autonomous agent for industry time series forecasting built via forecasting-oriented harness engineering.
- Integrates natural language user specifications, specialized forecasting models, analytical tools, and versioned execution records into a single runtime with explicit stopping conditions.
- Demonstrates superior performance achieving the lowest point-estimate MSE and MAE among 16 baselines across a five-dataset electricity-price setting, complemented by a Nord Pool case study and offline validation on North China electricity-load data.

## Open Questions & Future Work

- [[ablations-and-user-studies-for-autonomous-forecasting-agents]]

## Key Concepts

- [[castclaw]]: A human-in-the-loop autonomous forecasting agent that integrates specialized models, analytical tools, user constraints, and versioned execution records.

## Archivist Review

Approved the core agent framework concept 'castclaw' as it represents a novel human-in-the-loop architecture for forecasting, and approved its explicitly mentioned open question regarding component ablations and user studies. No standard named datasets were provided in the analysis that qualify for permanent vault archiving.

### Approved Concepts
- CastClaw: It introduces a novel autonomous agent framework designed specifically for industry time series forecasting, combining specialized models, user constraints, and explicit stopping conditions.

### Approved Open Questions
- Ablations and User Studies for Autonomous Forecasting Agents: Systematic ablations and user studies are critical for isolating which components drive performance gains in human-in-the-loop forecasting agents, separating system-level synergy from individual model capabilities.

## Links

- [Abstract](https://arxiv.org/abs/2608.30976)
- [PDF](https://arxiv.org/pdf/2608.30976)

