---
# CSL-compatible fields
title: "Is Capability a Liability? More Capable Language Models Make Worse Forecasts When It Matters Most"
author:
  - literal: "Nick Merrill"
  - literal: "Jaeho Lee"
  - literal: "Ezra Karger"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.22672"

# Custom fields
paper_id: "2605.22672"
paper_source: "openalex"
domain: "nlp,time-series"
tags:
  - "llm"
  - "language-model"
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
architectures:
  - "decoder-only"
datasets:
  - "ForecastBench-Sim"
concept_slugs:
  - "inverse-scaling-in-forecasting"
dataset_slugs:
  - "forecastbench-sim"
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:46:12Z"
created_at: "2026-05-24T07:46:12Z"
---

# Is Capability a Liability? More Capable Language Models Make Worse Forecasts When It Matters Most

**Authors**: Nick Merrill, Jaeho Lee, Ezra Karger
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.22672](https://arxiv.org/abs/2605.22672)

## Summary

This paper reports an inverse scaling relationship in large language models (LLMs) regarding forecasting, where increased model capability leads to degraded performance on time series characterized by superlinear growth and regime change risks. The authors find that more capable models erroneously prioritize aggressive extrapolation at the upper tail, leading to poor calibration in high-stakes scenarios like finance and epidemiology. These failures are systematically missed by traditional single-threshold benchmarks but revealed through tail-inclusive, continuous scoring metrics. To support rigorous evaluation, the authors release ForecastBench-Sim (FBSim), a synthetic benchmark designed to identify these distributional forecasting weaknesses.

## Key Contributions

- Demonstrates that LLM forecasting capability negatively correlates with performance on tasks involving superlinear growth and regime shifts.
- Introduces ForecastBench-Sim (FBSim), a contamination-free synthetic benchmark for evaluating tail-risk forecasting in LLMs.
- Shows that current single-threshold evaluation metrics mask upper-tail errors, leading to misleading conclusions about LLM forecasting performance.
- Recommends transitioning to continuous, tail-inclusive accuracy measures for evaluating LLM forecasting capabilities.

## Open Questions & Future Work

- [[llm-knowledge-calibration-gap]]

## Key Concepts

- [[inverse-scaling-in-forecasting]]: The observation that more capable LLMs produce worse distributional forecasts on time series characterized by superlinear growth and regime shift risks.

## Archivist Review

The paper's primary contribution is the documentation of a persistent inverse scaling effect in LLMs on high-stakes, tail-risk forecasting tasks. I have approved this as a key concept, alongside the release of the synthetic benchmark (FBSim). The open question regarding the knowledge-calibration gap highlights a core, unresolved mechanistic issue that extends beyond simple evaluation improvements.

### Approved Concepts
- Inverse Scaling in Forecasting: Identifies a critical failure mode where LLM capability negatively correlates with forecasting performance on high-stakes, tail-risk events.

### Approved Open Questions
- LLM knowledge-calibration gap mechanisms: Understanding this gap is critical for developing more robust AI forecasting systems, particularly for tail-sensitive domains where inaccurate forecasts lead to severe real-world consequences.

## Datasets

- [[forecastbench-sim]]

## Links

- [Abstract](https://arxiv.org/abs/2605.22672)
- [PDF](https://arxiv.org/pdf/2605.22672)

