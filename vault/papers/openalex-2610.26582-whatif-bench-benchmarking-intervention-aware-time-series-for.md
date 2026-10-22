---
# CSL-compatible fields
title: "WhatIf-Bench: Benchmarking Intervention-Aware Time Series Forecasting"
author:
  - literal: "Arjun Ashok"
  - literal: "Mihir Parmar"
  - literal: "Palash Goyal"
  - literal: "Bhavana Dalvi Mishra"
  - literal: "Chunliang Li"
  - literal: "Irina Rish"
  - literal: "Alexandre Drouin"
  - literal: "Jinsung Yoon"
  - literal: "Tomas Pfister"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2610.26582"

# Custom fields
paper_id: "2610.26582"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "llm"
  - "language-model"
  - "benchmark"
  - "evaluation"
  - "robustness"
  - "zero-shot-learning"
architectures:
  []
datasets:
  - "whatif-bench"
concept_slugs:
  - "whatif-bench"
dataset_slugs:
  - "whatif-bench"
skill: "TimeSeriesSkill"
processed_at: "2026-10-22T09:43:11Z"
created_at: "2026-10-22T09:43:11Z"
---

# WhatIf-Bench: Benchmarking Intervention-Aware Time Series Forecasting

**Authors**: Arjun Ashok, Mihir Parmar, Palash Goyal, Bhavana Dalvi Mishra, Chunliang Li, Irina Rish, Alexandre Drouin, Jinsung Yoon, Tomas Pfister
**Date**: 2026-10-19
**Paper ID**: [openalex:2610.26582](https://arxiv.org/abs/2610.26582)

## Summary

The paper introduces WhatIf-Bench, a large-scale, semi-synthetic benchmark designed to evaluate how well time series foundation models and frontier LLMs perform intervention-aware forecasting and scenario analysis using covariates. Across 37,665 tasks derived from physical simulators of data centers, power grids, traffic, and water networks, the evaluation reveals that models struggle significantly when generalising from repeated historical interventions to novel future scenarios. While models achieve high skill on replay futures, their performance drops sharply on novel interventions, establishing this generalisation gap as a central challenge for future research.

## Key Contributions

- Introduces WhatIf-Bench, a semi-synthetic benchmark with 37,665 tasks spanning data centers, power grids, road traffic, and water networks to evaluate intervention-aware time series forecasting.
- Evaluates time series foundation models, frontier LLMs, and regression baselines on replay and novel future scenario forecasting tasks.
- Demonstrates that while models perform well on replay futures (48 to 85% skill), their performance drops significantly on novel futures (-7 to 50% skill), highlighting generalisation to unseen interventions as a core challenge.
- Shows that increasing historical events improves generalisation on novel futures across models, though large performance gaps persist.

## Limitations

Performance on novel intervention futures drops significantly across all evaluated models, identifying generalisation to unseen covariate settings as a primary limitation of current time series forecasters and LLMs.

## Open Questions & Future Work

- [[intervention-aware-time-series-forecasting-reliability]]

## Key Concepts

- [[whatif-bench]]: A semi-synthetic benchmark for evaluating intervention-aware time series forecasting and scenario analysis under replay and novel future conditions.

## Archivist Review

Applied strict selectivity standards. Approved the core benchmark 'WhatIf-Bench' as both a concept and a dataset because it introduces a major standardized evaluation framework for intervention-aware time series forecasting. Approved one high-level open question regarding the reliability of intervention-aware forecasting under novel covariate settings.

### Approved Concepts
- WhatIf-Bench: It establishes the first comprehensive benchmark for evaluating intervention-aware scenario forecasting and covariate utilization across time series foundation models and LLMs.

### Approved Open Questions
- Reliability of Intervention-Aware Forecasting: Understanding how to make time series foundation models robust to out-of-distribution covariate shifts is essential for reliable decision-making and planning across science, engineering, and commerce.

## Datasets

- [[whatif-bench]]

## Links

- [Abstract](https://arxiv.org/abs/2610.26582)
- [PDF](https://arxiv.org/pdf/2610.26582)

