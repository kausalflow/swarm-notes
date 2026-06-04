---
# CSL-compatible fields
title: "ODTQA-FoRe: An Open-Domain Tabular Question Answering Dataset for Future Data Forecasting and Reasoning"
author:
  - literal: "Zhensheng Wang"
  - literal: "Xiaole Liu"
  - literal: "Wenmian Yang"
  - literal: "Kun Zhou"
  - literal: "Yiquan Zhang"
  - literal: "Weijia Jia"
issued:
  date-parts:
    - [2026, 6, 1]
url: "https://arxiv.org/abs/2606.02433"

# Custom fields
paper_id: "2606.02433"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "question-answering"
  - "time-series"
  - "forecasting"
  - "agent"
  - "autonomous-agent"
  - "multimodal"
architectures:
  - "decoder-only"
datasets:
  - "odtqa-fore-dataset"
concept_slugs:
  - "timefore-framework"
dataset_slugs:
  - "odtqa-fore-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-06-04T08:43:11Z"
created_at: "2026-06-04T08:43:11Z"
---

# ODTQA-FoRe: An Open-Domain Tabular Question Answering Dataset for Future Data Forecasting and Reasoning

**Authors**: Zhensheng Wang, Xiaole Liu, Wenmian Yang, Kun Zhou, Yiquan Zhang, Weijia Jia
**Date**: 2026-06-01
**Paper ID**: [openalex:2606.02433](https://arxiv.org/abs/2606.02433)

## Summary

The paper addresses the limitation of current LLM-based tabular QA systems in performing future-oriented numerical predictions. To bridge this gap, the authors introduce the ODTQA-FoRe dataset, which focuses on time-series forecasting and forecast-based reasoning using real estate data. They propose TimeFore, an agent-based framework that decomposes tasks into three collaborative roles: a SQL-based retriever, a specialized time-series forecaster, and an analytical synthesizer. Empirical results show that this collaborative approach effectively integrates external forecasting models with LLM reasoning capabilities.

## Key Contributions

- Introduces ODTQA-FoRe, a novel dataset for open-domain tabular question answering focused on time-series forecasting and reasoning.
- Develops TimeFore, a multi-agent framework that orchestrates SQL-based data retrieval, specialized time-series modeling, and analytical synthesis for future-oriented queries.
- Demonstrates that decomposing forecasting tasks into collaborative roles significantly improves prediction and reasoning accuracy compared to monolithic LLM approaches.

## Open Questions & Future Work

- [[incorporating-exogenous-factors-forecasting]]

## Key Concepts

- [[timefore-framework]]: A multi-agent framework that orchestrates SQL-based retrieval, time-series forecasting, and analytical reasoning for tabular QA.

## Archivist Review

The TimeFore framework is approved as it introduces a clear, reusable multi-agent design pattern for merging tabular retrieval, external time-series forecasting, and analytical reasoning. The ODTQA-FoRe dataset is approved as a novel benchmark for this task, and the open question regarding exogenous factor integration is highly relevant to the limitations of current forecasting architectures.

### Approved Concepts
- TimeFore Framework: It provides a standardized, modular agentic architecture for integrating large language model reasoning with specialized numerical forecasting tools.

### Approved Open Questions
- Integrating Exogenous Factors for Forecasting: This is a critical gap for domain-specific forecasting where internal historical data is insufficient to account for external market volatility.

## Datasets

- [[odtqa-fore-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2606.02433)
- [PDF](https://arxiv.org/pdf/2606.02433)

