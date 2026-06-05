---
# CSL-compatible fields
title: "TSQAgent: Rating Time Series Data Quality via Dedicated Agentic Reasoning"
author:
  - literal: "Shunyu Wu"
  - literal: "Dan Li"
  - literal: "H. Ye"
  - literal: "Weibin Feng"
  - literal: "Jian Lou"
  - literal: "Bo Zhang"
  - literal: "Wenjie Feng"
  - literal: "Chenjuan Guo"
  - literal: "See-Kiong Ng"
issued:
  date-parts:
    - [2026, 6, 2]
url: "https://arxiv.org/abs/2606.03629"

# Custom fields
paper_id: "2606.03629"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "time-series"
  - "agent"
  - "benchmark"
  - "evaluation"
  - "data-quality"
architectures:
  []
datasets:
  - "TSQBench"
concept_slugs:
  - "tsqagent"
dataset_slugs:
  - "tsqbench"
skill: "TimeSeriesSkill"
processed_at: "2026-06-05T08:38:39Z"
created_at: "2026-06-05T08:38:39Z"
---

# TSQAgent: Rating Time Series Data Quality via Dedicated Agentic Reasoning

**Authors**: Shunyu Wu, Dan Li, H. Ye, Weibin Feng, Jian Lou, Bo Zhang, Wenjie Feng, Chenjuan Guo, See-Kiong Ng
**Date**: 2026-06-02
**Paper ID**: [openalex:2606.03629](https://arxiv.org/abs/2606.03629)

## Summary

Assessing the quality of time series data remains difficult due to the multifaceted nature of quality dimensions and the limitations of purely text-based LLM reasoning. To address this, the authors introduce TSQBench, a benchmark designed to evaluate dimension identification and quantitative quality comparisons, and propose TSQAgent, an agentic framework featuring collaborative roles for focused analysis. TSQAgent integrates external analytical tools to perform grounded, quantitative assessments, significantly outperforming existing LLM approaches in both quality rating and subsequent data selection tasks.

## Key Contributions

- Introduces TSQBench, a dedicated benchmark for evaluating the ability of LLMs to identify quality dimensions and perform evidence-grounded quality comparisons.
- Develops TSQAgent, an agentic framework featuring a three-role architecture (Perceiver, Inspector, Adjudicator) that improves LLM performance on complex time series quality rating tasks.
- Demonstrates that TSQAgent enhances quality-aware data selection, resulting in improved downstream performance and data efficiency across eleven real-world datasets.

## Open Questions & Future Work

- [[absolute-ts-quality-scoring]]

## Key Concepts

- [[tsqagent]]: An agentic reasoning framework for time series data quality rating utilizing collaborative roles for dimension selection, quantitative analysis, and adjudication.

## Archivist Review

The paper introduces a novel agentic framework (TSQAgent) and a dedicated benchmark (TSQBench) for time series quality assessment, both of which are central to its contribution. The concept of an agentic framework using collaborative roles (Perceiver, Inspector, Adjudicator) is a reusable paradigm for complex analytical tasks. The open question regarding the shift from relative (pairwise) to absolute quality scoring is a significant, non-trivial research direction for the field.

### Approved Concepts
- TSQAgent: It establishes a new agentic architecture specifically designed to solve the multi-dimensional complexity of automated time series quality assessment.

### Approved Open Questions
- Absolute Time Series Quality Scoring: This is a foundational bottleneck for applying automated quality assessment to massive, unorganized datasets where pairwise comparisons are computationally prohibitive.

## Datasets

- [[tsqbench]]

## Links

- [Abstract](https://arxiv.org/abs/2606.03629)
- [PDF](https://arxiv.org/pdf/2606.03629)

