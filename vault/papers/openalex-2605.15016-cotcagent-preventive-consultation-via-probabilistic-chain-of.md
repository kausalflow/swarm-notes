---
# CSL-compatible fields
title: "COTCAgent: Preventive Consultation via Probabilistic Chain-of-Thought Completion"
author:
  - literal: "Zihan Deng"
  - literal: "Xiaozhen Zhong"
  - literal: "Chuanzhi Xu"
issued:
  date-parts:
    - [2026, 5, 14]
url: "https://arxiv.org/abs/2605.15016"

# Custom fields
paper_id: "2605.15016"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "chain-of-thought"
  - "time-series"
  - "benchmark"
  - "reasoning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "probabilistic-chain-of-thought-completion"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-17T07:32:07Z"
created_at: "2026-05-17T07:32:07Z"
---

# COTCAgent: Preventive Consultation via Probabilistic Chain-of-Thought Completion

**Authors**: Zihan Deng, Xiaozhen Zhong, Chuanzhi Xu
**Date**: 2026-05-14
**Paper ID**: [openalex:2605.15016](https://arxiv.org/abs/2605.15016)

## Summary

COTCAgent is a hierarchical reasoning framework designed for longitudinal electronic health record (EHR) analysis, specifically addressing clinical hallucination and temporal reasoning challenges. The framework consists of a Temporal-Statistics Adapter for standardized quantitative trend generation and a bounded Chain-of-Thought Completion layer that leverages knowledge bases for rigorous diagnostic risk assessment. By decoupling numerical computation from language generation, it achieves superior clinical diagnostic accuracy and robustness on both internal datasets and the HealthBench benchmark.

## Key Contributions

- COTCAgent addresses limitations in longitudinal EHR reasoning by introducing a hierarchical architecture that decouples statistical computation, feature matching, and text generation.
- The framework achieves 90.47% Top-1 accuracy on a custom clinical dataset and 70.41% on HealthBench, significantly improving quantitative diagnostic accuracy over baseline models.
- Integrates a Temporal-Statistics Adapter (TSA) and a bounded Chain-of-Thought Completion layer to mitigate hallucination in clinical trends and improve capture of long-range dependencies in non-uniform time series data.

## Open Questions & Future Work

- [[calibrating-energy-scores-clinical-risk]]

## Key Concepts

- [[probabilistic-chain-of-thought-completion]]: A hierarchical reasoning layer that integrates knowledge-based weighted scoring with bounded logical generation for clinical risk assessment.

## Archivist Review

I approved the core reasoning layer (COTC) as a reusable architectural pattern for grounding clinical LLMs, while rejecting the system-level 'agent' name as paper-local. The open question regarding the calibration of energy-based scores addresses a critical, non-trivial bottleneck in combining neural reasoning with statistical validity. HealthBench was rejected as a dataset because it is a broad collection rather than a specific, novel dataset introduced by the authors.

### Approved Concepts
- Probabilistic Chain-of-Thought Completion (COTC): Decouples statistical computation from linguistic reasoning, providing a structured approach to mitigating hallucinations in medical LLMs.

### Approved Open Questions
- Calibrating energy-based diagnostic risk: Bridging the gap between heuristic energy scores and calibrated diagnostic probability is a fundamental unresolved problem for clinical agent design.

### Rejected Candidates
- [concept] Probabilistic Chain-of-Thought Completion Agent (COTCAgent) (`cotcagent`) - subcomponent_of_broader_mechanism: The overarching framework name is a specific application artifact; the underlying reasoning layer (COTC) is more granular and reusable.

## Links

- [Abstract](https://arxiv.org/abs/2605.15016)
- [PDF](https://arxiv.org/pdf/2605.15016)

