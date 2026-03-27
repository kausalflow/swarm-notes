---
# CSL-compatible fields
title: "Cross-RAG: Zero-Shot Retrieval-Augmented Time Series Forecasting via Cross-Attention"
author:
  - literal: "Seunghan Lee"
  - literal: "Jaehoon Lee"
  - literal: "Jun Seo"
  - literal: "Sungdong Yoo"
  - literal: "Minjae Kim"
  - literal: "Tae Yoon Lim"
  - literal: "Dongwan Kang"
  - literal: "Hwanil Choi"
  - literal: "Soonyoung Lee"
  - literal: "Wonbin Ahn"
issued:
  date-parts:
    - [2026, 3, 16]
url: "https://arxiv.org/abs/2603.14709"

# Custom fields
paper_id: "2603.14709"
paper_source: "openalex"
domain: "time-series"
tags:
  - "retrieval-augmented-generation"
  - "rag"
  - "time-series"
  - "forecasting"
  - "zero-shot-learning"
  - "attention-mechanism"
  - "llm"
architectures:
  []
datasets:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:09:09Z"
created_at: "2026-03-27T14:09:09Z"
---

# Cross-RAG: Zero-Shot Retrieval-Augmented Time Series Forecasting via Cross-Attention

**Authors**: Seunghan Lee, Jaehoon Lee, Jun Seo, Sungdong Yoo, Minjae Kim, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Soonyoung Lee, Wonbin Ahn
**Date**: 2026-03-16
**Paper ID**: [openalex:2603.14709](https://arxiv.org/abs/2603.14709)

## Summary

This paper introduces Cross-RAG, a zero-shot retrieval-augmented forecasting framework designed to enhance the generalization capability of Time Series Foundation Models (TSFMs) on unseen datasets. Cross-RAG addresses the limitation of previous RAG methods, which indiscriminately use a fixed set of retrieved samples, by employing query-retrieval cross-attention to selectively weigh and integrate only the most relevant external knowledge. The framework jointly models the relevance between the query time series and retrieved samples, leading to more focused context integration. Extensive experiments show that Cross-RAG consistently outperforms baseline RAG methods across various TSFMs and different retrieval settings.

## Key Contributions

- Proposes Cross-RAG, a novel zero-shot retrieval-augmented forecasting framework that models input-level relevance between the query and retrieved samples using query-retrieval cross-attention.
- Cross-RAG jointly incorporates information from the query and retrieved samples to make more informed forecasts than methods using a fixed number of retrieved samples.
- Demonstrates consistent performance improvements across various Time Series Foundation Models (TSFMs) and existing Retrieval-Augmented Generation (RAG) methods in zero-shot forecasting tasks.
- Validation confirms the framework's effectiveness across diverse retrieval scenarios and different TSFM architectures.

## Limitations

The paper focuses on zero-shot generalization, and its performance in fully supervised or few-shot settings is not the primary focus. The efficiency of the cross-attention mechanism relative to standard RAG mechanisms could be a practical limitation for extremely large knowledge bases.

## Key Concepts

- [Cross-RAG](../concepts/cross-rag.md): A retrieval-augmented time series forecasting framework that uses cross-attention to selectively attend to query-relevant retrieved samples from an external knowledge base for improved zero-shot generalization.

## Limitations

The paper focuses on zero-shot generalization, and its performance in fully supervised or few-shot settings is not the primary focus. The efficiency of the cross-attention mechanism relative to standard RAG mechanisms could be a practical limitation for extremely large knowledge bases.

## Links

- [Abstract](https://arxiv.org/abs/2603.14709)
- [PDF](https://arxiv.org/pdf/2603.14709)

