---
# CSL-compatible fields
title: "SciPaths: Forecasting Pathways to Scientific Discovery"
author:
  - literal: "Eric Chamoun"
  - literal: "Yizhou Chi"
  - literal: "Yulong Chen"
  - literal: "Rui Cao"
  - literal: "Zifeng Ding"
  - literal: "Michalis Korakakis"
  - literal: "Andreas Vlachos"
issued:
  date-parts:
    - [2026, 5, 14]
url: "https://arxiv.org/abs/2605.14600"

# Custom fields
paper_id: "2605.14600"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "reasoning"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  - "scipaths"
concept_slugs:
  - "discovery-pathway-forecasting"
dataset_slugs:
  - "scipaths"
skill: "TimeSeriesSkill"
processed_at: "2026-05-17T07:30:46Z"
created_at: "2026-05-17T07:30:46Z"
---

# SciPaths: Forecasting Pathways to Scientific Discovery

**Authors**: Eric Chamoun, Yizhou Chi, Yulong Chen, Rui Cao, Zifeng Ding, Michalis Korakakis, Andreas Vlachos
**Date**: 2026-05-14
**Paper ID**: [openalex:2605.14600](https://arxiv.org/abs/2605.14600)

## Summary

SciPaths addresses the gap in AI4Science benchmarks by introducing discovery pathway forecasting, which tasks models with identifying and grounding the enabling contributions required for a specific scientific discovery. The authors curate a dataset of expert-annotated and silver pathways from ML and NLP literature to evaluate this capability. Their findings show that even frontier LLMs face significant difficulty in methodological dependency recovery, suggesting that backward-reasoning from target scientific contributions remains a substantial challenge.

## Key Contributions

- Introduces discovery pathway forecasting, a task focusing on backward-reasoning dependencies for scientific discovery.
- Presents SciPaths, a benchmark comprising 262 expert-annotated and 2,444 silver scientific pathways in ML and NLP.
- Reveals that frontier LLMs struggle with pathway recovery (0.189 F1), identifying methodological decomposition as a critical bottleneck.

## Open Questions & Future Work

- [[scientific-dependency-reasoning-and-decomposition]]

## Key Concepts

- [[discovery-pathway-forecasting]]: A task of identifying and grounding the sequences of enabling contributions that make a target scientific discovery feasible.

## Archivist Review

The paper introduces a significant evaluation paradigm for AI4Science centered on backward-reasoning of scientific dependencies. The concept of Discovery Pathway Forecasting and the associated SciPaths dataset are approved as they address a qualitative gap in existing research benchmarks. The open question is approved for its focus on the fundamental difficulty of methodological decomposition, a critical bottleneck for future AI research planning agents.

### Approved Concepts
- Discovery Pathway Forecasting: Defines a novel AI4Science evaluation framework focusing on scientific dependency structures rather than superficial citation or retrieval tasks.

### Approved Open Questions
- Scientific Dependency Reasoning Bottlenecks: Understanding these dependency structures is foundational for moveing beyond retrieval-based AI tools toward autonomous scientific reasoning.

## Datasets

- [[scipaths]]

## Links

- [Abstract](https://arxiv.org/abs/2605.14600)
- [PDF](https://arxiv.org/pdf/2605.14600)

