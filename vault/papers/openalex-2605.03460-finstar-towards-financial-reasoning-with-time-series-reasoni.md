---
# CSL-compatible fields
title: "FinSTaR: Towards Financial Reasoning with Time Series Reasoning Models"
author:
  - literal: "Seunghan Lee"
  - literal: "Jun Seo"
  - literal: "Jaehoon Lee"
  - literal: "Sungdong Yoo"
  - literal: "Minjae Kim"
  - literal: "Tae Yoon Lim"
  - literal: "Dongwan Kang"
  - literal: "Hwanil Choi"
  - literal: "Soonyoung Lee"
  - literal: "Wonbin Ahn"
issued:
  date-parts:
    - [2026, 5, 5]
url: "https://arxiv.org/abs/2605.03460"

# Custom fields
paper_id: "2605.03460"
paper_source: "openalex"
domain: "finance"
tags:
  - "llm"
  - "time-series"
  - "reasoning"
  - "chain-of-thought"
  - "benchmark"
architectures:
  []
datasets:
  - "fintsr-bench"
concept_slugs:
  - "compute-in-cot"
  - "scenario-aware-cot"
dataset_slugs:
  - "fintsr-bench"
skill: "TimeSeriesSkill"
processed_at: "2026-05-08T06:27:07Z"
created_at: "2026-05-08T06:27:07Z"
---

# FinSTaR: Towards Financial Reasoning with Time Series Reasoning Models

**Authors**: Seunghan Lee, Jun Seo, Jaehoon Lee, Sungdong Yoo, Minjae Kim, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Soonyoung Lee, Wonbin Ahn
**Date**: 2026-05-05
**Paper ID**: [openalex:2605.03460](https://arxiv.org/abs/2605.03460)

## Summary

FinSTaR addresses the limitations of existing time series reasoning models in the financial domain by implementing a specialized chain-of-thought architecture. The authors establish a 2x2 capability taxonomy and corresponding FinTSR-Bench benchmark to distinguish between deterministic assessment and stochastic prediction. FinSTaR utilizes 'Compute-in-CoT' for programmatic assessment of raw data and 'Scenario-Aware CoT' for reasoning through stochastic uncertainties, significantly outperforming existing LLM and TSRM baselines.

## Key Contributions

- Introduces a 2x2 capability taxonomy for time series reasoning models distinguishing single/multi-entity analysis and state assessment vs. future prediction.
- Proposes FinTSR-Bench, a financial benchmarking suite containing ten reasoning tasks derived from S&P stock data.
- Develops FinSTaR, a reasoning model employing tailored CoT strategies (Compute-in-CoT and Scenario-Aware CoT) to achieve 78.9% accuracy on financial tasks.

## Open Questions & Future Work

- [[limits-of-financial-predictability]]

## Key Concepts

- [[compute-in-cot]]: A programmatic chain-of-thought strategy for time series models to derive deterministic answers directly from raw numerical data.
- [[scenario-aware-cot]]: A chain-of-thought method for reasoning under stochastic uncertainty by generating diverse future scenarios before final judgment.

## Archivist Review

Approved concepts capture reusable reasoning paradigms (programmatic deterministic vs. scenario-based stochastic) for time series models, which are distinct from standard architecture proposals. Approved the benchmark as it represents a novel attempt to structure financial reasoning tasks systematically. The open question is retained as it highlights a fundamental limitation in performance evaluation for stochastic financial forecasting.

### Approved Concepts
- Compute-in-CoT: Introduces a programmatic reasoning approach for deterministic assessment tasks, effectively separating verifiable computation from stochastic reasoning.
- Scenario-Aware CoT: Provides a framework for reasoning under uncertainty by explicitly simulating potential future paths in stochastic time series forecasting.

### Approved Open Questions
- Limits of Financial Predictability: Fundamental for understanding whether models are optimizing reasoning or merely chasing irreducible noise in financial time series.

## Datasets

- [[fintsr-bench]]

## Links

- [Abstract](https://arxiv.org/abs/2605.03460)
- [PDF](https://arxiv.org/pdf/2605.03460)

