---
# CSL-compatible fields
title: "CAARL: In-Context Learning for Interpretable Co-Evolving Time Series Forecasting"
author:
  - literal: "Etienne Tajeuna"
  - literal: "Patrick Owusu"
  - literal: "Armelle Brun"
  - literal: "Shengrui Wang"
issued:
  date-parts:
    - [2026, 4, 20]
url: "https://arxiv.org/abs/2604.18305"

# Custom fields
paper_id: "2604.18305"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "language-model"
  - "llm"
  - "in-context-learning"
  - "chain-of-thought"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "caarl-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-23T06:55:02Z"
created_at: "2026-04-23T06:55:02Z"
---

# CAARL: In-Context Learning for Interpretable Co-Evolving Time Series Forecasting

**Authors**: Etienne Tajeuna, Patrick Owusu, Armelle Brun, Shengrui Wang
**Date**: 2026-04-20
**Paper ID**: [openalex:2604.18305](https://arxiv.org/abs/2604.18305)

## Summary

This paper introduces CAARL, an interpretable framework for forecasting co-evolving time series that leverage Large Language Models. By decomposing time series into autoregressive segments and constructing a temporal dependency graph, the model serializes complex dynamics into a narrative structure for LLM-based processing. This approach produces chain-of-thought style reasoning paths, allowing for transparent, context-aware predictions. The method effectively addresses nonstationary dynamics and offers a competitive alternative to existing forecasting benchmarks.

## Key Contributions

- Proposed CAARL, a modeling framework that uses LLMs to forecast co-evolving time series by serializing temporal dependency graphs into narrative prompts.
- Introduces a chain-of-thought inspired reasoning path that decodes contextual dynamics influencing nonstationary series behaviors.
- Demonstrates competitive performance against state-of-the-art methods on real-world forecasting tasks while providing enhanced interpretability.

## Open Questions & Future Work

- [[interpretable-co-evolving-forecasting-tradeoffs]]

## Key Concepts

- [[caarl-framework]]: A forecasting framework that serializes temporal dependency graphs of autoregressive segments into narrative prompts for LLM-based reasoning.

## Archivist Review

The paper introduces a unique method for LLM-based time-series reasoning via narrative serialization of dependency graphs. The approved concept 'caarl-framework' captures this specific architecture, and the approved open question focuses on the inherent trade-off between the interpretability of this approach and predictive accuracy. Other candidates were rejected to maintain the required level of scientific rigor and to ensure the vault remains focused on fundamental, recurring research directions.

### Approved Concepts
- Context-Aware ARLLM (CAARL): It introduces a novel paradigm of serializing temporal dependency graphs into narrative prompts for LLM-based reasoning in time-series forecasting.

### Approved Open Questions
- Interpretable Co-evolving Forecasting Tradeoffs: This addresses the fundamental tension between model transparency and predictive performance in high-stakes time-series applications.

### Rejected Candidates
- [concept] ContextAware ARLLM (CAARL) (`context-aware-arllm-caarl`) - other: Renamed to caarl-framework to follow vault slug conventions.

## Links

- [Abstract](https://arxiv.org/abs/2604.18305)
- [PDF](https://arxiv.org/pdf/2604.18305)

