---
# CSL-compatible fields
title: "JockeyBench: Evaluating LLM Agents on Horse-Racing Decision-Making"
author:
  - literal: "Zhongwei Xie"
  - literal: "Xingsu Li"
  - literal: "Jingqiao Yu"
  - literal: "Zihao Wang"
  - literal: "Hong ChiTat"
  - literal: "Zhaowei Wang"
  - literal: "Weizhi Du"
  - literal: "Yuxuan Liu"
  - literal: "Huihao Jing"
  - literal: "Jiaxin Bai"
  - literal: "Yangqiu Song"
  - literal: "Yuxuan Liu"
  - literal: "Huihao Jing"
  - literal: "Jiaxin Bai"
  - literal: "Yangqiu Song"
issued:
  date-parts:
    - [2026, 10, 14]
url: "https://arxiv.org/abs/2610.19589"

# Custom fields
paper_id: "2610.19589"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "agent"
  - "autonomous-agent"
  - "benchmark"
  - "evaluation"
  - "tool-use"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-17T08:55:43Z"
created_at: "2026-10-17T08:55:43Z"
---

# JockeyBench: Evaluating LLM Agents on Horse-Racing Decision-Making

**Authors**: Zhongwei Xie, Xingsu Li, Jingqiao Yu, Zihao Wang, Hong ChiTat, Zhaowei Wang, Weizhi Du, Yuxuan Liu, Huihao Jing, Jiaxin Bai, Yangqiu Song, Yuxuan Liu, Huihao Jing, Jiaxin Bai, Yangqiu Song
**Date**: 2026-10-14
**Paper ID**: [openalex:2610.19589](https://arxiv.org/abs/2610.19589)

## Summary

The paper introduces JockeyBench, a benchmark and evaluation protocol for assessing LLM agents on repeated event forecasting using historical Japanese horse racing. By testing 28 model-scaffold configurations across 324 races with time-gated evidence and priced tools, the study evaluates forecast quality, net utility, and financial returns. Results reveal that while reusable-program workflows outperform fresh per-race generation, all configurations suffer negative mean profits under capped-Kelly settlement, highlighting the disconnect between predictive competence and economic utility.

## Key Contributions

- Introduces JockeyBench, a novel benchmark and evaluation protocol for studying repeated event forecasting using historical Japanese horse racing data.
- Evaluates 28 model-scaffold configurations across 324 races using time-gated evidence, priced tools, and paired frozen-program controls.
- Demonstrates that reusable-program workflows outperform fresh per-race generation in betting profit and research fees, though all configurations yield negative mean profit under capped-Kelly settlement.

## Limitations

All evaluated model-scaffold configurations incur negative mean profit under capped-Kelly settlement, and performance relies on concentrated returns.

## Archivist Review

The candidate benchmark is domain-specific to horse-racing decision-making and does not represent a reusable forecasting architecture or algorithmic mechanism. Consequently, both the concept and the open question have been rejected in accordance with the scarcity policy.

### Rejected Candidates
- [concept] JockeyBench (`jockeybench`) - not_reusable: JockeyBench is a domain-specific benchmark rather than a reusable algorithmic concept or mechanism.
- [open_question] Cost-Aware Adaptation Under Alternative Pricing (`cost-aware-adaptation-pricing`) - low_impact: The open question is broad and lacks specific methodological formulation to anchor ongoing vault tracking.

## Links

- [Abstract](https://arxiv.org/abs/2610.19589)
- [PDF](https://arxiv.org/pdf/2610.19589)

