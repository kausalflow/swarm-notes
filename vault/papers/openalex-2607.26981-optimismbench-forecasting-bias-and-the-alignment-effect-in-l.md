---
# CSL-compatible fields
title: "OptimismBench: Forecasting Bias and the Alignment Effect in Language Model Judgment"
author:
  - literal: "Seonglae Cho"
  - literal: "Adriano Koshiyama"
issued:
  date-parts:
    - [2026, 7, 29]
url: "https://arxiv.org/abs/2607.26981"

# Custom fields
paper_id: "2607.26981"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "alignment"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  - "optimismbench"
concept_slugs:
  - "optimismbench"
dataset_slugs:
  - "optimismbench"
skill: "TimeSeriesSkill"
processed_at: "2026-08-01T07:23:07Z"
created_at: "2026-08-01T07:23:07Z"
---

# OptimismBench: Forecasting Bias and the Alignment Effect in Language Model Judgment

**Authors**: Seonglae Cho, Adriano Koshiyama
**Date**: 2026-07-29
**Paper ID**: [openalex:2607.26981](https://arxiv.org/abs/2607.26981)

## Summary

Large language models frequently serve as decision aids whose probability judgments shape downstream choices, yet traditional calibration metrics fail to flag directional tilts. To address this, the authors introduce OptimismBench, a benchmark utilizing inverted scenario pairs to compute a signed directional bias score without requiring ground truth. Evaluating 16 models across 8 providers reveals a prevalent optimistic skew—with pessimism appearing exclusively in Anthropic's frontier models—and demonstrates that post-training alignment fundamentally dictates this bias sign.

## Key Contributions

- Introduces OptimismBench, a benchmarking framework using inverted scenario pairs to detect signed directional probability bias in LLM judgments without ground truth.
- Evaluates 16 models across 8 providers, revealing that 14 models exhibit systematic optimism while pessimism is restricted to Anthropic's frontier tier.
- Demonstrates through matched base-chat pairs that post-training determines the sign of the probability bias, and shows model identity dominates language variance by a 4.7x margin.

## Open Questions & Future Work

- [[matched-human-baseline-comparison]]

## Key Concepts

- [[optimismbench]]: A benchmarking framework that detects directional bias in language model probability judgments through inverted scenario pairs and signed bias scores.

## Archivist Review

Strict adherence to review policies: approved the core conceptual framework for signed directional probability bias auditing (OptimismBench) along with its canonical dataset, and preserved the specific open research question examining human baseline comparisons for LLM optimism.

### Approved Concepts
- OptimismBench: Introduces a novel evaluation framework and dataset for auditing directional bias in language model probability judgments using inverted pairs without requiring ground truth.

### Approved Open Questions
- Matched Human Baseline Comparison: Crucial for understanding whether model optimism mirrors human cognitive biases or represents distinct machine artifacts.

### Rejected Candidates
- [open_question] Matched Human Baseline Comparison (`human-baseline-comparison`) - duplicate_existing: Redundant with the approved query title; keeping the canonical title instead.

## Datasets

- [[optimismbench]]

## Links

- [Abstract](https://arxiv.org/abs/2607.26981)
- [PDF](https://arxiv.org/pdf/2607.26981)

