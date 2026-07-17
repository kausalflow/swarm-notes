---
# CSL-compatible fields
title: "When Directional Accuracy Lies: A Base-Rate-Honest Benchmark for LoRA-Adapted TimesFM on Equity Forecasting"
author:
  - literal: "Taizhen Cheung"
  - literal: "SA Kwon"
issued:
  date-parts:
    - [2026, 7, 14]
url: "https://arxiv.org/abs/2607.12248"

# Custom fields
paper_id: "2607.12248"
paper_source: "openalex"
domain: "finance"
tags:
  - "llm"
  - "time-series"
  - "forecasting"
  - "lora"
  - "fine-tuning"
  - "benchmark"
  - "evaluation"
  - "parameter-efficient-fine-tuning"
  - "peft"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "base-rate-honest-benchmark"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-17T07:09:32Z"
created_at: "2026-07-17T07:09:32Z"
---

# When Directional Accuracy Lies: A Base-Rate-Honest Benchmark for LoRA-Adapted TimesFM on Equity Forecasting

**Authors**: Taizhen Cheung, SA Kwon
**Date**: 2026-07-14
**Paper ID**: [openalex:2607.12248](https://arxiv.org/abs/2607.12248)

## Summary

This paper evaluates the directional accuracy of LoRA-adapted TimesFM for equity forecasting, identifying that high performance often stems from market base-rate artifacts rather than predictive skill. The authors establish a rigorous, base-rate-honest benchmark using stratified cross-validation and statistical significance testing to expose this issue. Results demonstrate that fine-tuning fails to provide a tradeable directional edge over naive baselines in both NASDAQ-100 and S&P 500 universes. The methodology provides a standardized framework for future financial time-series benchmarking.

## Key Contributions

- Proposed a reproducible, frozen-data benchmark with expanding walk-forward folds to prevent base-rate artifacts in financial forecasting.
- Demonstrated that fine-tuned LoRA adapters on TimesFM fail to outperform base rates in directional accuracy, despite achieving lower point-forecast errors.
- Showed that per-sector specialization performs significantly worse than pooled adapters on equity forecasting tasks.

## Open Questions & Future Work

- [[mitigating-survivorship-bias-benchmarks]]

## Key Concepts

- [[base-rate-honest-benchmark]]: A forecasting evaluation protocol that accounts for market base rates to distinguish genuine predictive skill from trivial artifacts.

## Archivist Review

I have approved the Base-Rate-Honest Benchmark concept because it provides a necessary, reusable methodological framework for rigorous evaluation of financial forecasting models against trivial heuristics. I also approved the open question regarding survivorship bias in benchmarks, as it identifies a major, recurring methodological flaw that invalidates many financial forecasting studies. The proposal for multi-seed robustness was rejected as it is a generic experimental best practice applicable to all machine learning, rather than a specific open problem in time-series domain modeling.

### Approved Concepts
- Base-Rate-Honest Benchmark: The benchmark addresses the critical, often ignored problem of market-biased base rates in equity forecasting, providing a rigorous protocol to prevent 'directional accuracy' fallacies.

### Approved Open Questions
- Mitigating Survivorship Bias Benchmarks: Survivorship bias is a significant confounding factor that can lead to an illusory sense of predictive accuracy, undermining the validity of financial forecasting benchmarks.

### Rejected Candidates
- [open_question] Multi-seed Evaluation Robustness (`multi-seed-evaluation-robustness`) - generic: This is a general software/experiment hygiene issue rather than a specialized, long-lived research bottleneck specific to time-series forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2607.12248)
- [PDF](https://arxiv.org/pdf/2607.12248)

