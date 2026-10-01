---
# CSL-compatible fields
title: "TQTS-Bench: A Multi-Syntax Benchmark for Text-to-Query over Time-Series Databases"
author:
  - literal: "Lyu Fei"
  - literal: "Zhiyi Peng"
  - literal: "Jiaming Liu"
  - literal: "Yixuan Yang"
  - literal: "Changjian Chen"
  - literal: "Zhuo Tang"
  - literal: "Jiapeng Zhang"
  - literal: "Kenli Li"
issued:
  date-parts:
    - [2026, 9, 28]
url: "https://arxiv.org/abs/2609.34783"

# Custom fields
paper_id: "2609.34783"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "benchmark"
  - "dataset"
  - "evaluation"
  - "time-series"
  - "information-extraction"
architectures:
  []
datasets:
  - "tsqbench"
concept_slugs:
  - "tqts-bench"
dataset_slugs:
  - "tsqbench"
skill: "TimeSeriesSkill"
processed_at: "2026-10-01T11:15:39Z"
created_at: "2026-10-01T11:15:39Z"
---

# TQTS-Bench: A Multi-Syntax Benchmark for Text-to-Query over Time-Series Databases

**Authors**: Lyu Fei, Zhiyi Peng, Jiaming Liu, Yixuan Yang, Changjian Chen, Zhuo Tang, Jiapeng Zhang, Kenli Li
**Date**: 2026-09-28
**Paper ID**: [openalex:2609.34783](https://arxiv.org/abs/2609.34783)

## Summary

This paper introduces TQTS-Bench, a multi-syntax benchmark designed to evaluate large language models on natural language querying over time-series databases (TSDBs). Consisting of 6,125 human-reviewed QA pairs across 97 TSDBs and 23 distinct syntaxes, the benchmark reveals substantial performance gaps in current models (e.g., Claude-Opus-5 achieves 48.98% execution accuracy vs. 87.34% for humans). Error analysis highlights that heterogeneous syntaxes, temporal intent misinterpretation, and schema linking failures remain core challenges.

## Key Contributions

- Introduces TQTS-Bench, a benchmark containing 6,125 QA pairs spanning 97 TSDBs, 23 distinct query syntaxes, 22 domains, and 4 time-specific query intent types.
- Demonstrates that current state-of-the-art LLMs struggle with TSDB querying, with Claude-Opus-5 achieving only 48.98% execution accuracy compared to 87.34% for humans.
- Identifies primary error sources including heterogeneous query syntaxes, misinterpretation of time-specific intents, and incorrect schema linking.

## Open Questions & Future Work

- [[generalizable-text-to-query-for-tsdb]]

## Key Concepts

- [[tqts-bench]]: A multi-syntax benchmark containing 6,125 QA pairs across 97 time-series databases for evaluating text-to-query capabilities.

## Archivist Review

Approved TQTS-Bench as a concept and the associated text-to-query generalization open question, while mapping the dataset to the existing tsqbench entry to maintain vault integrity.

### Approved Concepts
- TQTS-Bench: It introduces the first comprehensive benchmark evaluating text-to-query capabilities specifically tailored for time-series databases across diverse syntaxes and domains.

### Approved Open Questions
- Generalizable Text-to-Query over TSDBs: Existing text-to-query methods are either tightly coupled to specific SQL/RDB structures or single-system TSDB variants like PromQL, exhibiting poor generalizability across the 23+ different syntaxes found in modern time-series databases.

## Datasets

- [[tsqbench]]

## Links

- [Abstract](https://arxiv.org/abs/2609.34783)
- [PDF](https://arxiv.org/pdf/2609.34783)

