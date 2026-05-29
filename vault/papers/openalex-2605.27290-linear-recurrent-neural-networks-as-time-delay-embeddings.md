---
# CSL-compatible fields
title: "Linear Recurrent Neural Networks as Time-Delay Embeddings"
author:
  - literal: "Fisher Ng"
  - literal: "J. Nathan Kutz"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.27290"

# Custom fields
paper_id: "2605.27290"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "recurrent-neural-network"
  - "embedding"
architectures:
  - "recurrent-neural-network"
datasets:
  []
concept_slugs:
  - "lrnn-time-delay-embedding"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-29T08:38:57Z"
created_at: "2026-05-29T08:38:57Z"
---

# Linear Recurrent Neural Networks as Time-Delay Embeddings

**Authors**: Fisher Ng, J. Nathan Kutz
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.27290](https://arxiv.org/abs/2605.27290)

## Summary

This paper provides a theoretical grounding for the success of Linear Recurrent Neural Networks (LRNNs) in time-series analysis by framing them through the lens of Takens' embedding theorem. The authors demonstrate that concatenating LRNN hidden states into delay-coordinate vectors effectively reconstructs the dynamics of the underlying system. By analyzing the properties of the resulting delay matrix, the study proves that maintaining spectral norms within the unit circle ensures stable and faithful state embeddings.

## Key Contributions

- Establishes a theoretical link between Linear Recurrent Neural Networks (LRNNs) and Takens' embedding theorem, characterizing LRNN states as time-delay embeddings.
- Derives explicit rank conditions for the delay matrix of LRNNs to ensure faithful representation of underlying dynamical systems.
- Proves that for singular values σmax(W) ≤ 1, embedding stability metrics are bounded independent of the delay order, providing a theoretical foundation for the observed spectral properties of trained LRNNs.

## Open Questions & Future Work

- [[rank-deficient-lrnn-embedding-robustness]]

## Key Concepts

- [[lrnn-time-delay-embedding]]: A formal characterization of LRNN hidden states as time-delay embeddings of the underlying dynamical system.

## Archivist Review

I approved the core theoretical concept linking LRNNs to Takens' embedding theorem, as it offers a fundamental perspective on sequence model behavior. I also approved the open question regarding the robustness of these embeddings under rank-deficiency, as it addresses a significant gap between theoretical requirements and empirical model success. No other candidates were proposed or found.

### Approved Concepts
- LRNN Time-Delay Embedding: Provides a formal theoretical bridge between common linear recurrent architectures and dynamical systems theory (Takens' Theorem).

### Approved Open Questions
- Rank-Deficient LRNN Embedding Robustness: This is a foundational theoretical question regarding the robustness of LRNNs as sequence models. Identifying less restrictive conditions for embedding would expand the theoretical applicability of LRNNs beyond the strict deterministic rank constraints, providing better alignment with empirical findings where these models often succeed despite theoretical limitations.

## Links

- [Abstract](https://arxiv.org/abs/2605.27290)
- [PDF](https://arxiv.org/pdf/2605.27290)

