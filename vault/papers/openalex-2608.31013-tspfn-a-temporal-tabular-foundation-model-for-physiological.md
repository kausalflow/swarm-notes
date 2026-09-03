---
# CSL-compatible fields
title: "TSPFN: A Temporal Tabular Foundation Model for Physiological Time Series Classification"
author:
  - literal: "Jérémie Stym-Popper"
  - literal: "Clément Rambour"
  - literal: "Federica Granese"
  - literal: "Nicolas Thome"
  - literal: "Olivier Bernard"
issued:
  date-parts:
    - [2026, 8, 31]
url: "https://arxiv.org/abs/2608.31013"

# Custom fields
paper_id: "2608.31013"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "foundation-model"
  - "in-context-learning"
  - "pre-training"
  - "classification"
  - "multimodal"
  - "positional-encoding"
architectures:
  []
datasets:
  []
concept_slugs:
  - "tspfn"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-03T09:16:55Z"
created_at: "2026-09-03T09:16:55Z"
---

# TSPFN: A Temporal Tabular Foundation Model for Physiological Time Series Classification

**Authors**: Jérémie Stym-Popper, Clément Rambour, Federica Granese, Nicolas Thome, Olivier Bernard
**Date**: 2026-08-31
**Paper ID**: [openalex:2608.31013](https://arxiv.org/abs/2608.31013)

## Summary

The paper introduces TSPFN, a temporal tabular foundation model that adapts TabPFN for physiological time-series classification by integrating structured temporal representations and positional embeddings. Pretrained on 140,000 real-world physiological time series, TSPFN effectively captures intra-sample temporal and channel dependencies to excel in low-to-medium data medical regimes. Experiments across diverse physiological benchmarks show that TSPFN consistently outperforms standard tabular baselines, TabPFN, and specialized deep time-series models.

## Key Contributions

- Introduces TSPFN, a temporal tabular foundation model that redesigns TabPFN's architecture with structured temporal representations and positional embeddings.
- Pretrained on 140,000 real-world physiological time series across multiple medical domains to handle low- to medium-data regimes.
- Demonstrates consistent outperformance over standard tabular baselines, TabPFN, and specialized deep time-series models across diverse physiological benchmarks.

## Open Questions & Future Work

- [[handling-irregular-and-continuous-time-series]]

## Key Concepts

- [[tspfn]]: A temporal tabular foundation model that redesigns TabPFN's architecture to capture intra-sample temporal and channel dependencies for physiological time series classification.

## Archivist Review

Applied strict selectivity standards: approved the core conceptual contribution (TSPFN) and its associated open question regarding handling irregular time series in tabular foundation models, while filtering out generic terminology and unapproved datasets.

### Approved Concepts
- TSPFN: Introduces a novel temporal tabular foundation model adapting TabPFN for physiological time series via structured temporal representations and pretraining.

### Approved Open Questions
- Handling Irregularly Sampled Time Series: Crucial for expanding tabular foundation models to handle continuous or irregularly sampled real-world medical data streams beyond fixed-length windows.

## Links

- [Abstract](https://arxiv.org/abs/2608.31013)
- [PDF](https://arxiv.org/pdf/2608.31013)

