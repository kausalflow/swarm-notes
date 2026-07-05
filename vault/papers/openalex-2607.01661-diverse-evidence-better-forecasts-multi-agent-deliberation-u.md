---
# CSL-compatible fields
title: "Diverse Evidence, Better Forecasts: Multi-Agent Deliberation Under Information Asymmetry"
author:
  - literal: "Yuante Li"
  - literal: "Yicheng Tao"
  - literal: "K Zhang"
  - literal: "Taozhi Wang"
  - literal: "G D Gu"
  - literal: "Yaxin Zhou"
issued:
  date-parts:
    - [2026, 7, 2]
url: "https://arxiv.org/abs/2607.01661"

# Custom fields
paper_id: "2607.01661"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "agent"
  - "multi-agent"
  - "reasoning"
  - "benchmark"
  - "forecasting"
architectures:
  - "decoder-only"
datasets:
  - "polygym"
concept_slugs:
  - "designed-information-asymmetry"
dataset_slugs:
  - "polygym"
skill: "TimeSeriesSkill"
processed_at: "2026-07-05T07:52:36Z"
created_at: "2026-07-05T07:52:36Z"
---

# Diverse Evidence, Better Forecasts: Multi-Agent Deliberation Under Information Asymmetry

**Authors**: Yuante Li, Yicheng Tao, K Zhang, Taozhi Wang, G D Gu, Yaxin Zhou
**Date**: 2026-07-02
**Paper ID**: [openalex:2607.01661](https://arxiv.org/abs/2607.01661)

## Summary

This paper addresses the problem of 'herding' in multi-agent LLM forecasting systems, where deliberation fails to improve over single-agent performance when agents share identical evidence. The authors introduce InfoDelphi, a framework that forces information asymmetry by partitioning data into shared public and disjoint private evidence subsets. Theoretical analysis and empirical results on the PolyGym benchmark demonstrate that this approach significantly reduces inter-agent error correlation and improves forecasting accuracy. The findings highlight input diversity as a critical enabler for effective multi-agent deliberation.

## Key Contributions

- Identifies that information symmetry in multi-agent LLM forecasting leads to herding and limits reasoning performance.
- Introduces InfoDelphi, a multi-agent framework that enforces information asymmetry by partitioning evidence into public and private subsets.
- Demonstrates InfoDelphi achieves 12-18% improvement in Brier score and 4-8% in accuracy over state-of-the-art baselines on the PolyGym benchmark.

## Open Questions & Future Work

- [[optimal-information-asymmetry-allocation-for-deliberation]]

## Key Concepts

- [[designed-information-asymmetry]]: A multi-agent forecasting paradigm that partitions evidence into shared public and disjoint private subsets to reduce inter-agent error correlation during deliberation.

## Archivist Review

I approved 'Designed Information Asymmetry' as a foundational mechanism for multi-agent reasoning, as it shifts the focus from individual model capacity to the structure of input distribution. The PolyGym dataset was approved due to its specific focus on real-world binary forecasting markets, which is highly relevant to time-series and event forecasting benchmarks. I rejected the InfoDelphi framework as a standalone concept in favor of the mechanism it instantiates, adhering to the principle of favoring overarching mechanisms.

### Approved Concepts
- Designed Information Asymmetry: Addresses the fundamental failure mode of 'herding' in multi-agent LLM systems by enforcing input diversity as a primary mechanism for belief revision.

### Approved Open Questions
- Optimizing Information Asymmetry Allocation: This question addresses the fundamental design bottleneck in scaling multi-agent deliberation, moving beyond static heuristics toward adaptive, evidence-driven multi-agent systems.

### Rejected Candidates
- [concept] InfoDelphi (`infodelphi-framework`) - subcomponent_of_broader_mechanism: The framework is a specific implementation of the 'designed information asymmetry' concept; the mechanism itself is more fundamental and reusable than the specific system.
- [open_question] Optimizing Information Asymmetry Routing (`optimizing-asymmetric-information-routing`) - duplicate_existing: The candidate was rewritten into a cleaner, more generalized form to better serve as a standalone vault entry.

## Datasets

- [[polygym]]

## Links

- [Abstract](https://arxiv.org/abs/2607.01661)
- [PDF](https://arxiv.org/pdf/2607.01661)

