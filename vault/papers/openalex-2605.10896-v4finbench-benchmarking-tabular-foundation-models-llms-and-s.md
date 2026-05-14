---
# CSL-compatible fields
title: "V4FinBench: Benchmarking Tabular Foundation Models, LLMs, and Standard Methods on Corporate Bankruptcy Prediction"
author:
  - literal: "Marcin Kostrzewa"
  - literal: "Sebastian Tomczak"
  - literal: "R. H. Furman"
  - literal: "Anna Poberezhna"
  - literal: "Michał Furgała"
  - literal: "Oleksii Furman"
  - literal: "Maciej Zięba"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10896"

# Custom fields
paper_id: "2605.10896"
paper_source: "openalex"
domain: "finance"
tags:
  - "benchmark"
  - "dataset"
  - "llm"
  - "tabular-foundation-model"
  - "finance"
  - "time-series"
  - "forecasting"
  - "imbalance"
architectures:
  - "encoder-only"
  - "decoder-only"
datasets:
  - "v4finbench"
concept_slugs:
  - "v4finbench"
dataset_slugs:
  - "v4finbench"
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:39:36Z"
created_at: "2026-05-14T07:39:36Z"
---

# V4FinBench: Benchmarking Tabular Foundation Models, LLMs, and Standard Methods on Corporate Bankruptcy Prediction

**Authors**: Marcin Kostrzewa, Sebastian Tomczak, R. H. Furman, Anna Poberezhna, Michał Furgała, Oleksii Furman, Maciej Zięba
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10896](https://arxiv.org/abs/2605.10896)

## Summary

This paper addresses the scarcity of public, high-scale benchmarks in corporate bankruptcy prediction by introducing V4FinBench, a dataset covering over one million company-year records across V4 economies. The authors evaluate a variety of models—including gradient boosting, TabPFN, and QLoRA-finetuned Llama-3-8B—on six prediction horizons under severe class imbalance (0.19%-0.36%). Results indicate that while TabPFN is highly competitive with gradient boosting, LLM-based approaches currently struggle to match its performance on ROC-AUC and F1-score metrics. The authors further show that models finetuned on V4FinBench demonstrate transferability when evaluated on the American Bankruptcy Dataset.

## Key Contributions

- Introduces V4FinBench, a large-scale public bankruptcy prediction dataset with >1 million records, 131 features, and six time horizons.
- Provides comprehensive benchmarking of standard tabular methods, TabPFN, and QLoRA-finetuned Llama-3-8B under extreme class imbalance.
- Demonstrates that TabPFN achieves competitive performance against gradient boosting while showing evidence of transferable financial distress patterns through cross-dataset evaluation.

## Open Questions & Future Work

- [[geographic-generalization-bankruptcy-models]]

## Key Concepts

- [[v4finbench]]: A large-scale benchmark for corporate bankruptcy prediction containing over one million records from V4 economies across multiple time horizons.

## Archivist Review

The paper introduces a significant large-scale benchmark for financial forecasting. I have approved the dataset and the concept of the benchmark itself, along with the substantial open question regarding cross-regional generalization. Generic candidates and sub-components were rejected to adhere to the strict archival policy.

### Approved Concepts
- V4FinBench: This is a large-scale, public, multi-horizon financial distress benchmark designed to fill the scarcity of high-quality, non-proprietary data in this domain.

### Approved Open Questions
- Geographic generalization of bankruptcy models: Assessing geographic robustness is critical for establishing the reliability and utility of financial foundation models in cross-border investment and regulatory applications.

### Rejected Candidates
- [concept] V4FinBench (`v4finbench-benchmark`) - duplicate_existing: Redundant with the dataset note and uses an non-canonical suffix.

## Datasets

- [[v4finbench]]

## Links

- [Abstract](https://arxiv.org/abs/2605.10896)
- [PDF](https://arxiv.org/pdf/2605.10896)

