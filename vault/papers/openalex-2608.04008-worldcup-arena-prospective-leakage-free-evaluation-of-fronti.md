---
# CSL-compatible fields
title: "WorldCup Arena: Prospective, Leakage-Free Evaluation of Frontier LLMs on a Live Tournament"
author:
  - literal: "Zhenran Wang"
  - literal: "Zhonghan Bian"
  - literal: "Jinsong Li"
  - literal: "Zhangyang Qi"
issued:
  date-parts:
    - [2026, 8, 4]
url: "https://arxiv.org/abs/2608.04008"

# Custom fields
paper_id: "2608.04008"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "reasoning"
  - "benchmark"
  - "evaluation"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-07T06:05:00Z"
created_at: "2026-08-07T06:05:00Z"
---

# WorldCup Arena: Prospective, Leakage-Free Evaluation of Frontier LLMs on a Live Tournament

**Authors**: Zhenran Wang, Zhonghan Bian, Jinsong Li, Zhangyang Qi
**Date**: 2026-08-04
**Paper ID**: [openalex:2608.04008](https://arxiv.org/abs/2608.04008)

## Summary

The paper introduces WorldCup Arena, a prospective and leakage-free benchmarking framework evaluating six frontier LLMs with server-side web search and extended thinking over the live 2026 FIFA World Cup. By asking models for predictions before every kickoff across 104 matches and tournament pools, the authors establish that current LLMs achieve a 63.9% accuracy matching bookmaker favorites, while exhibiting systematic shared behaviors such as under-committing to draws and high inter-model correlation.

## Key Contributions

- Introduces WorldCup Arena, a prospective, leakage-free evaluation benchmark consisting of 4,494 scored predictions across 104 live matches and tournament pools during the 2026 FIFA World Cup.
- Evaluates six frontier LLMs with extended thinking and server-side web search, showing they average 63.9% accuracy on match outcomes (matching bookmaker favorites).
- Demonstrates that current frontier LLMs exhibit shared failure modes, including under-committing to draws and goals, high inter-model agreement (rendering majority votes ineffective), and accuracy collapsing in close ties despite rich information.

## Limitations

Evaluated specifically on a single sports tournament domain (FIFA World Cup) with a fixed set of six frontier LLMs.

## Open Questions & Future Work

- [[mitigating-model-herding-in-forecasting]]

## Archivist Review

Evaluated the paper according to rigorous ML knowledge vault standards. No standalone concept note was warranted as the contribution focuses on a specific live benchmark evaluation of LLMs rather than a novel structural mechanism. The open question regarding model herding in forecasting was approved as it captures an important, reusable bottleneck in prospective model evaluation.

### Approved Open Questions
- Mitigating Model Herding in Forecasting: Understanding and overcoming model herding is crucial for developing robust forecasting agents that can provide independent, value-add insights beyond existing market consensus.

### Rejected Candidates
- [dataset] WorldCup Arena (`worldcup-arena`) - paper_local: Paper-specific tournament evaluation benchmark rather than a reusable standalone machine learning dataset.

## Links

- [Abstract](https://arxiv.org/abs/2608.04008)
- [PDF](https://arxiv.org/pdf/2608.04008)

