---
# CSL-compatible fields
title: "Which Histories Matter for Time Series Forecasting? Learning Predictive Relevance with Future Supervision"
author:
  - literal: "Yong-Hoon Choi"
  - literal: "Youngjin Cho"
issued:
  date-parts:
    - [2026, 8, 24]
url: "https://arxiv.org/abs/2608.23221"

# Custom fields
paper_id: "2608.23221"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "retrieval-augmented-generation"
  - "rag"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-27T15:58:00Z"
created_at: "2026-08-27T15:58:00Z"
---

# Which Histories Matter for Time Series Forecasting? Learning Predictive Relevance with Future Supervision

**Authors**: Yong-Hoon Choi, Youngjin Cho
**Date**: 2026-08-24
**Paper ID**: [openalex:2608.23221](https://arxiv.org/abs/2608.23221)

## Summary

Historical retrieval for time-series forecasting typically relies on past similarity as a heuristic for usefulness, which often fails to capture true predictive relevance. This paper introduces a predictive relevance framework that uses realized futures as privileged supervision during training to learn listwise future-compatibility targets for candidate reranking. By decoupling coarse candidate generation from future-supervised reranking, the method improves pattern retrieval across six benchmarks and reveals distinct candidate-global, query-specific, and mixed relevance regimes.

## Key Contributions

- Formulates predictive relevance for historical retrieval in time series forecasting using realized futures as privileged training supervision.
- Proposes a two-stage retrieval framework combining normalized-pattern coarse candidate generation with a lightweight residual MLP reranker for listwise future compatibility.
- Demonstrates empirical superiority across six benchmarks against matched-protocol baselines like SARAF.

## Open Questions & Future Work

- [[alternative-jointly-learned-candidate-generators]]

## Archivist Review

Strict filtering criteria were applied, adhering to scarcity limits and avoiding vault bloat by approving only the highest-impact open question.

### Approved Open Questions
- Alternative and Jointly Learned Candidate Generators: Crucial for overcoming the performance bottleneck where rerankers are constrained by initial retrieval pools, enabling more robust end-to-end historical retrieval architectures.

### Rejected Candidates
- [open_question] Alternative and Jointly Learned Candidate Generators (`alternative-jointly-learned-candidate-generators`) - low_impact: The open question is valid and well-scoped, but we are being extremely scarce as per instructions.

## Links

- [Abstract](https://arxiv.org/abs/2608.23221)
- [PDF](https://arxiv.org/pdf/2608.23221)

