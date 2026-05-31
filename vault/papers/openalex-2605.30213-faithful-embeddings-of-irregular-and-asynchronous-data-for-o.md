---
# CSL-compatible fields
title: "Faithful Embeddings of Irregular and Asynchronous Data for Online Log-NCDEs"
author:
  - literal: "Benjamin Walker"
  - literal: "Alexandre Bloch"
  - literal: "Lingyi Yang"
  - literal: "Sam Morley"
  - literal: "Terry Lyons"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.30213"

# Custom fields
paper_id: "2605.30213"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "embedding"
  - "neural-controlled-differential-equations"
architectures:
  []
datasets:
  []
concept_slugs:
  - "log-ncdes"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:11:04Z"
created_at: "2026-05-31T08:11:04Z"
---

# Faithful Embeddings of Irregular and Asynchronous Data for Online Log-NCDEs

**Authors**: Benjamin Walker, Alexandre Bloch, Lingyi Yang, Sam Morley, Terry Lyons
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.30213](https://arxiv.org/abs/2605.30213)

## Summary

This paper proposes an approach to continuous-time modeling for irregular and asynchronous data that eliminates the reliance on traditional interpolation or imputation-based embeddings. By proving that universality holds under continuous and injective mappings, the authors introduce a new embedding for Log-NCDEs that treats discrete observations as increments. This method enables direct interval-level log-signature computation, facilitating efficient, robust, and online inference without requiring explicit path reconstruction.

## Key Contributions

- Demonstrates that explicit interpolation/imputation is unnecessary for continuous-time modeling under injective embeddings.
- Introduces a continuous and injective embedding for Log-NCDEs that records observations as increments.
- Supports efficient online computation and provides interval-level summaries without reconstructing paths.

## Open Questions & Future Work

- [[embedding-faithfulness-vs-computational-cost]]

## Key Concepts

- [[log-ncdes]]: A universal class of continuous-time models that avoids the need for explicit interpolation or imputation by directly embedding asynchronous data as increments.

## Archivist Review

The approved concept and open question represent the core technical contribution of the paper—a shift from path-reconstruction to increment-based embedding for continuous-time models—and the fundamental research trade-off involved in that paradigm. I have rejected no candidates as none were proposed, and the selection is limited to the most central, reusable aspects of the study as per instructions.

### Approved Concepts
- Log-NCDEs: Central focus of the paper for modeling continuous-time dynamics.

### Approved Open Questions
- Faithfulness vs. Computational Cost: This trade-off between theoretical faithfulness (injectivity) and practical computational scalability is a fundamental bottleneck for deploying continuous-time models on complex real-world sequential data.

## Links

- [Abstract](https://arxiv.org/abs/2605.30213)
- [PDF](https://arxiv.org/pdf/2605.30213)

