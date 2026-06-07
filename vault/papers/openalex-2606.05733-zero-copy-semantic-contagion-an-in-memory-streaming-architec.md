---
# CSL-compatible fields
title: "Zero-Copy Semantic Contagion: An In-Memory Streaming Architecture for Evolving Attention Graphs"
author:
  - literal: "Kabir Murjani"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.05733"

# Custom fields
paper_id: "2606.05733"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "attention-mechanism"
  - "graph-neural-network"
  - "lstm"
architectures:
  []
datasets:
  - "FNSPID"
concept_slugs:
  - "multivariate-neural-hawkes-process"
dataset_slugs:
  - "fnspid"
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:19:49Z"
created_at: "2026-06-07T08:19:49Z"
---

# Zero-Copy Semantic Contagion: An In-Memory Streaming Architecture for Evolving Attention Graphs

**Authors**: Kabir Murjani
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.05733](https://arxiv.org/abs/2606.05733)

## Summary

This paper addresses the failure of single-asset financial models to account for cross-company information propagation by introducing a low-latency, news-driven streaming architecture. The system maps incoming textual news onto a continuous-time attention graph using a zero-copy parsing mechanism and leverages a multivariate Neural Hawkes Process for inference. Experimental results on the FNSPID corpus demonstrate that dynamic graph attention significantly outperforms traditional single-asset or same-sector baselines in predicting next-day returns.

## Key Contributions

- Introduces a zero-copy streaming architecture that achieves sub-15ms end-to-end processing latency for news-driven graph updates.
- Proposes a multivariate Neural Hawkes Process that models cross-asset information propagation through directed excitation.
- Demonstrates a 1.70x precision lift over random and 3.36x over sector-based baselines on the FNSPID corpus, establishing the necessity of the dynamic graph topology.

## Open Questions & Future Work

- [[intraday-contagion-validation]]

## Key Concepts

- [[multivariate-neural-hawkes-process]]: A neural point process variant used for modeling directed excitation in financial time-series graph nodes.

## Archivist Review

I have approved the Multivariate Neural Hawkes Process as it represents a core, reusable mechanism for modeling event-driven dependencies. The FNSPID dataset is approved as a standard for evaluating news-driven financial contagion, and the open question regarding intraday validation addresses a key bottleneck in connecting architectural speed claims to market reality. Other candidates were rejected as implementation-specific optimizations or generic research directions.

### Approved Concepts
- Multivariate Neural Hawkes Process: It serves as the predictive engine for the system, capturing temporal dependencies and excitation patterns between assets.

### Approved Open Questions
- Intraday Contagion Prediction Validation: Validating the predictive utility of microsecond-scale architectures at high frequencies is critical to bridge the gap between architectural performance and market-impact relevance.

### Rejected Candidates
- [concept] Zero-Copy Semantic Contagion (`zero-copy-semantic-contagion`) - subcomponent_of_broader_mechanism: The 'zero-copy' aspect is a specific implementation detail of the Rust architecture rather than a reusable core forecasting mechanism.
- [open_question] Dynamic Attention-Based Graph Construction (`dynamic-attention-graph-construction`) - generic: This is a common direction for improving GNN architectures and is not specific enough as a standalone research problem.

## Datasets

- [[fnspid]]

## Links

- [Abstract](https://arxiv.org/abs/2606.05733)
- [PDF](https://arxiv.org/pdf/2606.05733)

