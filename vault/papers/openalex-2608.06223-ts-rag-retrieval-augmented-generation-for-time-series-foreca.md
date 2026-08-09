---
# CSL-compatible fields
title: "TS-RAG: Retrieval Augmented Generation for Time Series Forecasting"
author:
  - literal: "Yixiong Xiao"
  - literal: "Congxi Xiao"
  - literal: "Jingbo Zhou"
issued:
  date-parts:
    - [2026, 8, 6]
url: "https://arxiv.org/abs/2608.06223"

# Custom fields
paper_id: "2608.06223"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "retrieval-augmented-generation"
  - "rag"
  - "forecasting"
  - "time-series"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "ts-rag"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-09T05:39:38Z"
created_at: "2026-08-09T05:39:38Z"
---

# TS-RAG: Retrieval Augmented Generation for Time Series Forecasting

**Authors**: Yixiong Xiao, Congxi Xiao, Jingbo Zhou
**Date**: 2026-08-06
**Paper ID**: [openalex:2608.06223](https://arxiv.org/abs/2608.06223)

## Summary

The paper introduces TS-RAG, a novel retrieval-augmented generation framework tailored for time series forecasting. While standard RAG in LLMs relies on prompt concatenation, time series models suffer from limited training data and lack extensive generative capabilities. To address this, TS-RAG utilizes specially designed reference tokens to fuse information from input sequences with retrieved similar historical sequences, achieving state-of-the-art performance on real-world forecasting benchmarks.

## Key Contributions

- Proposes TS-RAG, a novel retrieval-augmented generation framework tailored for time series forecasting that overcomes the limitations of naive prompt concatenation.
- Introduces specially designed reference tokens to effectively fuse information from input sequences with retrieved similar historical sequences.
- Demonstrates consistent state-of-the-art performance across several real-world time series forecasting benchmarks.

## Key Concepts

- [[ts-rag]]: A retrieval-augmented generation framework for time series forecasting that fuses retrieved similar sequences using reference tokens.

## Archivist Review

Approved the core framework concept 'ts-rag' as a notable retrieval-augmented forecasting architecture while rejecting subcomponents and general terms in accordance with vault scarcity rules.

### Approved Concepts
- TS-RAG: Introduces a retrieval-augmented generation framework specifically designed for time series forecasting using reference tokens.

### Rejected Candidates
- [concept] Reference Tokens (`reference-tokens`) - subcomponent_of_broader_mechanism: Subcomponent of the broader TS-RAG framework rather than an independently reusable main contribution.

## Links

- [Abstract](https://arxiv.org/abs/2608.06223)
- [PDF](https://arxiv.org/pdf/2608.06223)

