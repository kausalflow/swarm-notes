---
# CSL-compatible fields
title: "The Geometry of Agent Memory: Forecasting Retrieval-Bound Memory Failures, and Characterizing Its Limits"
author:
  - literal: "Iliya Zhechev"
  - literal: "Radoslav Ralev"
  - literal: "Chris Coleman"
  - literal: "Srijith Rajamohan"
  - literal: "Jen Agarwal"
  - literal: "Tyler Hutcherson"
  - literal: "Simba Khadder"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2610.26433"

# Custom fields
paper_id: "2610.26433"
paper_source: "openalex"
domain: "nlp"
tags:
  - "agent"
  - "retrieval-augmented-generation"
  - "rag"
  - "embedding"
  - "semantic-search"
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
processed_at: "2026-10-22T09:44:41Z"
created_at: "2026-10-22T09:44:41Z"
---

# The Geometry of Agent Memory: Forecasting Retrieval-Bound Memory Failures, and Characterizing Its Limits

**Authors**: Iliya Zhechev, Radoslav Ralev, Chris Coleman, Srijith Rajamohan, Jen Agarwal, Tyler Hutcherson, Simba Khadder
**Date**: 2026-10-19
**Paper ID**: [openalex:2610.26433](https://arxiv.org/abs/2610.26433)

## Summary

This paper investigates whether geometric relationships between conversation turns, memory texts, and retrieval queries can predict agent answer correctness prior to generation. Evaluating four memory implementations and an observation-summary comparator using a 25-feature logistic classifier on LongMemEval-small, the authors find that pooled geometric features achieve an AUROC of 0.640, which fails to outperform a simple question-difficulty baseline and adds negligible improvement after controlling for system identity. The findings indicate that embedding proximity does not reliably verify fact coverage or distinguish between memory-construction, retrieval, and generation errors.

## Key Contributions

- Evaluates whether geometric relationships between conversation turns, memory texts, and queries can predict agent memory retrieval correctness before text generation using a 25-feature logistic classifier.
- Demonstrates on LongMemEval-small that pooled geometric features achieve an AUROC of 0.640 (below a question-difficulty baseline of 0.655), with marginal added value (+0.002) after controlling for difficulty and system identity.
- Shows that while geometry reaches 0.841 on single-session-assistant questions, system identity alone achieves 0.826, indicating embedding proximity does not reliably verify fact coverage or isolate retrieval versus generation failures.

## Limitations

Geometric features and embedding proximity fail to reliably predict agent memory retrieval failures or distinguish memory-construction, retrieval, and generation errors across broader pooled evaluation.

## Open Questions & Future Work

- [[disentangling-memory-failure-modes]]

## Archivist Review

Archivist review kept only candidates judged central to the paper and reusable across future work. Approved 0 concept(s), 1 open question(s), and 0 dataset(s), with 1 rejected candidate note(s).

### Approved Open Questions
- Disentangling Memory Failure Modes: Essential for diagnosing the precise locus of failure in retrieval-augmented memory systems rather than relying on uninterpretable embedding distance correlations.

### Rejected Candidates
- [dataset] LongMemEval-small (`longmemeval-small`) - paper_local: Dataset is a paper-local subset or minor variant not established as a primary benchmark in the vault.

## Links

- [Abstract](https://arxiv.org/abs/2610.26433)
- [PDF](https://arxiv.org/pdf/2610.26433)

