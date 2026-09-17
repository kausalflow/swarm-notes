---
# CSL-compatible fields
title: "Beyond Numerical Time Series: A Unified Benchmark for Multimodal Forecasting with Heterogeneous Context"
author:
  - literal: "Peng Chen"
  - literal: "Zhihao Zhuang"
  - literal: "Hongzhou Chen"
  - literal: "Junhao Huang"
  - literal: "Aiping Yang"
  - literal: "Mengsen Wu"
  - literal: "Yiding Liu"
  - literal: "Xilin Dai"
  - literal: "Zewei Dong"
issued:
  date-parts:
    - [2026, 9, 14]
url: "https://arxiv.org/abs/2609.15087"

# Custom fields
paper_id: "2609.15087"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:43:03Z"
created_at: "2026-09-17T09:43:03Z"
---

# Beyond Numerical Time Series: A Unified Benchmark for Multimodal Forecasting with Heterogeneous Context

**Authors**: Peng Chen, Zhihao Zhuang, Hongzhou Chen, Junhao Huang, Aiping Yang, Mengsen Wu, Yiding Liu, Xilin Dai, Zewei Dong
**Date**: 2026-09-14
**Paper ID**: [openalex:2609.15087](https://arxiv.org/abs/2609.15087)

## Summary

The paper introduces MUSE-Bench, a unified benchmark for multimodal time series forecasting featuring fourteen datasets across eight domains and six types of context (metadata, events, holidays, news, images, and numerical covariates). Through comprehensive evaluation of statistical, foundation, multimodal, and LLM-based methods, the authors find that numerical time series foundation models currently dominate overall performance, while external context benefits context-aware models only when temporally aligned and accurate.

## Key Contributions

- Introduced MUSE-Bench, a unified benchmark for multimodal time series forecasting comprising fourteen datasets across eight domains and six types of context.
- Evaluated diverse forecasting paradigms including statistical, data-specific, foundation, multimodal, and general-purpose LLM methods under consistent settings.
- Demonstrated that numerical foundation models currently dominate overall rankings while external context improves context-aware models when correctly aligned.

## Archivist Review

Rigorously applied the review policy to protect vault quality. MUSE-Bench is a broad evaluation benchmark rather than a standalone algorithmic concept, and the open question is too broad/generic to merit a permanent vault note. Therefore, all candidates were rejected.

### Rejected Candidates
- [concept] MUSE-Bench (`muse-bench`) - low_impact: MUSE-Bench is primarily a benchmark evaluation framework rather than a reusable core forecasting mechanism, model architecture, or methodological concept note.
- [open_question] Reliable Multimodal Context Utilization (`reliable-multimodal-context-utilization`) - generic: The open question is broad and generic, discussing general multimodal alignment and context usage rather than a sharp, specific technical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.15087)
- [PDF](https://arxiv.org/pdf/2609.15087)

