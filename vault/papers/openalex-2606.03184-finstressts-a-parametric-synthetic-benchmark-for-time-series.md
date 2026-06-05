---
# CSL-compatible fields
title: "FinStressTS: A Parametric Synthetic Benchmark for Time-Series Forecasting in Finance"
author:
  - literal: "Jiaze Sun"
  - literal: "Kelvin J. L. Koa"
  - literal: "Ruiyang Ni"
  - literal: "Yize Liu"
  - literal: "Haonan Chen"
  - literal: "Ke‐Wei Huang"
issued:
  date-parts:
    - [2026, 6, 2]
url: "https://arxiv.org/abs/2606.03184"

# Custom fields
paper_id: "2606.03184"
paper_source: "openalex"
domain: "finance"
tags:
  - "benchmark"
  - "time-series"
  - "forecasting"
  - "llm"
architectures:
  []
datasets:
  []
concept_slugs:
  - "finstressts"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-05T08:38:05Z"
created_at: "2026-06-05T08:38:05Z"
---

# FinStressTS: A Parametric Synthetic Benchmark for Time-Series Forecasting in Finance

**Authors**: Jiaze Sun, Kelvin J. L. Koa, Ruiyang Ni, Yize Liu, Haonan Chen, Ke‐Wei Huang
**Date**: 2026-06-02
**Paper ID**: [openalex:2606.03184](https://arxiv.org/abs/2606.03184)

## Summary

FinStressTS is a synthetic benchmark designed to address the limitations of real-world financial data by providing 30 controlled diagnostic environments for model failure analysis. It systematically evaluates point and probabilistic forecasting performance across six key financial mechanisms, including regime switching and heavy-tailed shocks. By comparing 15 models ranging from classical statistical baselines to advanced Transformers and probabilistic deep learning architectures, the study reveals that simpler models often maintain superior performance and sample efficiency in specific, mechanism-dependent financial scenarios.

## Key Contributions

- Introduces FinStressTS, a synthetic benchmark providing 30 controlled diagnostic environments across six financial mechanism families (e.g., volatility clustering, heavy-tailed shocks, regime switching).
- Demonstrates that classical autoregressive and linear models frequently outperform modern Transformer-based architectures in jump- and tail-driven financial environments.
- Quantifies sample efficiency differences between neural models and statistical baselines, revealing that larger neural architectures often require significantly more data to match simple parametric baselines.

## Open Questions & Future Work

- [[expanding-mechanism-coverage-synthetic-benchmarks]]
- [[extending-forecast-tasks-and-interactions]]

## Key Concepts

- [[finstressts]]: A mechanism-aware synthetic benchmark for financial time-series forecasting that maps model performance to six controlled structural diagnostic environments.

## Archivist Review

I have approved the FinStressTS framework as it provides a valuable diagnostic standard for financial forecasting that aligns with the vault's focus on structured evaluation. The approved open questions identify the critical limitations of moving from simple synthetic diagnostics to complex, multi-step, and decision-centric financial environments, which is a vital area of future study. All other candidates were rejected as they were either too specific to the paper or described standard research goals that are common to all benchmarking efforts.

### Approved Concepts
- FinStressTS: It provides a standardized, diagnostic approach to financial time-series forecasting by decomposing model performance into specific structural mechanisms rather than aggregate accuracy metrics.

### Approved Open Questions
- Expanding Financial Mechanism Coverage: As benchmarks become more widely used for model selection, ensuring they cover a sufficiently broad and representative mechanism space is crucial for preventing overfitting to specific synthetic settings.
- Extending Forecasting Tasks and Interactions: Most high-impact financial applications move beyond point or probabilistic forecasting into adaptive decision-making; evaluating models solely on static horizons limits their reliability in dynamic market conditions.

## Links

- [Abstract](https://arxiv.org/abs/2606.03184)
- [PDF](https://arxiv.org/pdf/2606.03184)

