---
# CSL-compatible fields
title: "AQuA: Recursively Self-Improving Quantitative Trading Research Agents"
author:
  - literal: "Jiacheng Guo"
  - literal: "Suozhi Huang"
  - literal: "Yunlong Gao"
  - literal: "Zihao Li"
  - literal: "Jian Ge"
  - literal: "Xu Kuang"
  - literal: "Mengdi Wang"
issued:
  date-parts:
    - [2026, 8, 13]
url: "https://arxiv.org/abs/2608.12841"

# Custom fields
paper_id: "2608.12841"
paper_source: "openalex"
domain: "finance"
tags:
  - "llm"
  - "language-model"
  - "agent"
  - "autonomous-agent"
  - "time-series"
  - "forecasting"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "aqua-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-16T05:18:37Z"
created_at: "2026-08-16T05:18:37Z"
---

# AQuA: Recursively Self-Improving Quantitative Trading Research Agents

**Authors**: Jiacheng Guo, Suozhi Huang, Yunlong Gao, Zihao Li, Jian Ge, Xu Kuang, Mengdi Wang
**Date**: 2026-08-13
**Paper ID**: [openalex:2608.12841](https://arxiv.org/abs/2608.12841)

## Summary

The paper introduces AQuA, an autonomous, recursively self-improving quantitative trading research system featuring two separate language-model-driven pipelines: one for symbolic factor discovery and one for trainable model development. Each system operates within a sealed sandbox that closes its own research loop using validated empirical evidence from earlier iterations. Evaluated on both crypto and US equity universes, AQuA demonstrates strong predictive power and high held-out Sharpe ratios while maintaining positive annual returns from 2021 through 2025.

## Key Contributions

- Introduces AQuA, a recursive self-improving quantitative trading research system comprising independent symbolic factor and trainable model loops.
- Employs bounded, sealed sandboxes with fixed data splits, definitions, and evaluators to constrain model actions via factor expressions or configuration diffs.
- Achieves an information coefficient of ~0.190 for symbolic factor discovery on a cryptocurrency universe.
- Reaches a per-stock information coefficient of +0.0843 on US equities and a held-out Sharpe ratio of up to +2.50 with consistent positive returns from 2021 to 2025.

## Open Questions & Future Work

- [[coupled-factor-model-quantitative-agents]]

## Key Concepts

- [[aqua-framework]]: An autonomous system implementing recursive self-improvement at the level of quantitative-investment research via separate symbolic factor discovery and trainable model development loops.

## Archivist Review

The AQuA framework concept is approved as a canonical architecture for recursive self-improving quantitative research. The open question regarding the coupling of factor discovery and model development highlights a central frontier in automated finance. No standalone datasets are approved as none were publicly named as reusable benchmarks.

### Approved Concepts
- AQuA Framework: AQuA introduces a novel recursive self-improvement paradigm for quantitative investment research, dividing the workflow into independent symbolic factor discovery and trainable model development loops.

### Approved Open Questions
- Coupling Factor Discovery and Model Development: Bridging symbolic factor discovery and neural time-series model development in a unified, leak-proof recursive self-improving pipeline represents a key frontier for autonomous financial research agents.

## Links

- [Abstract](https://arxiv.org/abs/2608.12841)
- [PDF](https://arxiv.org/pdf/2608.12841)

