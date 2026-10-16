---
# CSL-compatible fields
title: "GIFT-Eval-CTX: A Benchmark For Contextual Forecasting Model Evaluation"
author:
  - literal: "Xu Liu"
  - literal: "Hanshu Yan"
  - literal: "Taha Aksu"
  - literal: "Quang Pham"
  - literal: "Zhongzheng Qiao"
  - literal: "Jun Hao Liew"
  - literal: "Silvio Savarese"
  - literal: "Doyen Sahoo"
  - literal: "Junnan Li"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.17794"

# Custom fields
paper_id: "2610.17794"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "dataset"
  - "evaluation"
  - "agent"
  - "llm"
architectures:
  []
datasets:
  - "gift-eval-ctx"
concept_slugs:
  []
dataset_slugs:
  - "gift-eval-ctx"
skill: "TimeSeriesSkill"
processed_at: "2026-10-16T09:23:30Z"
created_at: "2026-10-16T09:23:30Z"
---

# GIFT-Eval-CTX: A Benchmark For Contextual Forecasting Model Evaluation

**Authors**: Xu Liu, Hanshu Yan, Taha Aksu, Quang Pham, Zhongzheng Qiao, Jun Hao Liew, Silvio Savarese, Doyen Sahoo, Junnan Li
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.17794](https://arxiv.org/abs/2610.17794)

## Summary

The paper introduces GIFT-Eval-CTX, a benchmark for evaluating contextual forecasting models that incorporate forward-looking information into time series predictions. Built on 10,000 instances across 20 datasets, the benchmark uses an agentic pipeline to annotate structured Macro and Micro effects derived from realized futures. Evaluation of TSFMs, frontier LLMs, and agentic systems reveals that structured future information substantially reduces forecasting error compared to history-only prompting.

## Key Contributions

- Introduces GIFT-Eval-CTX, a benchmark comprising 10,000 instances across 20 datasets designed to evaluate contextual forecasting models using verified future information.
- Proposes a structured effects annotation framework featuring Macro effects for horizon-wide behavior and Micro effects for localized changes, constructed via an agentic discovery and deterministic code validation pipeline.
- Demonstrates that providing structured future information reduces relative MASE by 40.7% for GPT-5.6 Sol and 29.6% for Claude Opus 4.8 compared to history-only prompting.
- Evaluates various TSFMs, frontier LLMs, and tool-using agentic systems, identifying MoiraiAgent as achieving the best overall performance.

## Open Questions & Future Work

- [[preserving-temporal-variation-code-editing]]

## Archivist Review

The paper presents GIFT-Eval-CTX as a benchmark dataset and evaluation suite rather than a standalone algorithmic concept, so it is appropriately categorized under datasets. The open question regarding temporal variation preservation in code-based forecasting addresses a substantive methodological limitation.

### Approved Open Questions
- Preserving Temporal Variation in Code-Based Forecasting: Addressing this limitation is crucial for ensuring that code-assisted time series forecasting agents produce realistic, high-fidelity trajectories rather than overly smooth or plateaus-dominated paths.

### Rejected Candidates
- [concept] GIFT-Eval-CTX (`gift-eval-ctx`) - not_reusable: GIFT-Eval-CTX is primarily a dataset/benchmark package rather than a distinct algorithmic concept or architectural primitive.

## Datasets

- [[gift-eval-ctx]]

## Links

- [Abstract](https://arxiv.org/abs/2610.17794)
- [PDF](https://arxiv.org/pdf/2610.17794)

