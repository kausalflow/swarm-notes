---
# CSL-compatible fields
title: "From Long News to Accurate Forecast: Importance-Aware Fusion and PRM-Guided Reflection for Time Series Forecasting"
author:
  - literal: "Mingyang Liu"
  - literal: "Qingcan Kang"
  - literal: "Yuke Wang"
  - literal: "Shixiong Kai"
  - literal: "Kaichao Liang"
  - literal: "Hui-Ling Zhen"
  - literal: "Tao Zhong"
  - literal: "Mingxuan Yuan"
  - literal: "Linqi Song"
issued:
  date-parts:
    - [2026, 6, 2]
url: "https://arxiv.org/abs/2606.03097"

# Custom fields
paper_id: "2606.03097"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "llm"
  - "retrieval-augmented-generation"
  - "rag"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "importance-aware-news-compression"
  - "process-reward-model-for-retrieval-guidance"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-05T08:37:56Z"
created_at: "2026-06-05T08:37:56Z"
---

# From Long News to Accurate Forecast: Importance-Aware Fusion and PRM-Guided Reflection for Time Series Forecasting

**Authors**: Mingyang Liu, Qingcan Kang, Yuke Wang, Shixiong Kai, Kaichao Liang, Hui-Ling Zhen, Tao Zhong, Mingxuan Yuan, Linqi Song
**Date**: 2026-06-02
**Paper ID**: [openalex:2606.03097](https://arxiv.org/abs/2606.03097)

## Summary

This paper addresses the limitations of integrating long-form news into LLM-based time series forecasting pipelines. The proposed framework features an importance-aware news compression mechanism that prioritizes informative content within fixed context budgets and a process reward model (PRM) that intelligently selects supplementary news based on real-time error feedback. Extensive evaluations across finance, energy, and traffic domains confirm that the method achieves higher predictive accuracy and more efficient refinement compared to existing LLM-based pipelines.

## Key Contributions

- Proposes an importance-aware news compression module that maintains forecasting-relevant information under fixed context constraints.
- Introduces a Process Reward Model (PRM) to guide iterative news retrieval based on current error profiles, reducing redundant updates.
- Demonstrates superior accuracy and reduced refinement iterations compared to LLM-based baselines across finance, energy, traffic, and bitcoin benchmarks.

## Open Questions & Future Work

- [[multimodal-scalable-exogenous-data-fusion]]

## Key Concepts

- [[importance-aware-news-compression]]: A technique that uses an importance reward model to allocate compression budgets to external information based on estimated forecasting utility.
- [[process-reward-model-for-retrieval-guidance]]: An iterative retrieval strategy that ranks candidates by conditioning on current forecasting errors and past selection history.

## Archivist Review

Archivist review kept only candidates judged central to the paper and reusable across future work. Approved 2 concept(s), 1 open question(s), and 0 dataset(s), with 1 rejected candidate note(s).

### Approved Concepts
- Importance-Aware News Compression: Provides a principled mechanism for condensing long-form external data into fixed-context LLM windows based on task-specific utility.
- Process Reward Model for Retrieval Guidance: Moves retrieval from blind matching to error-aware, iterative selection guided by a model trained on the forecasting process.

### Approved Open Questions
- Scalable Multimodal Exogenous Fusion: This captures the fundamental limitation of scaling retrieval-augmented forecasting beyond static text and highlights the need for architectures that process heterogeneous, high-volume inputs.

### Rejected Candidates
- [concept] PRM-Guided Reflection for Time Series Forecasting (`prm-guided-reflection-for-time-series-forecasting`) - duplicate_existing: This concept name is overly specific to this paper; the underlying mechanism is better captured as 'Process Reward Model for Retrieval Guidance'.

## Links

- [Abstract](https://arxiv.org/abs/2606.03097)
- [PDF](https://arxiv.org/pdf/2606.03097)

