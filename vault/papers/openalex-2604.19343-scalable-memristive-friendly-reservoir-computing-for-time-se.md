---
# CSL-compatible fields
title: "Scalable Memristive-Friendly Reservoir Computing for Time Series Classification"
author:
  - literal: "Coşku Can Horuz"
  - literal: "Andrea Ceni"
  - literal: "Claudio Gallicchio"
  - literal: "Sebastian Otte"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2604.19343"

# Custom fields
paper_id: "2604.19343"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "reservoir-computing"
  - "neuromorphic-computing"
  - "efficient-learning"
  - "classification"
architectures:
  []
datasets:
  []
concept_slugs:
  - "memristive-friendly-parallelized-reservoirs-mars"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-24T06:59:40Z"
created_at: "2026-04-24T06:59:40Z"
---

# Scalable Memristive-Friendly Reservoir Computing for Time Series Classification

**Authors**: Coşku Can Horuz, Andrea Ceni, Claudio Gallicchio, Sebastian Otte
**Date**: 2026-04-21
**Paper ID**: [openalex:2604.19343](https://arxiv.org/abs/2604.19343)

## Summary

This paper introduces MARS, a memristive-friendly, parallelized reservoir computing architecture designed for scalable and hardware-efficient time series classification. By implementing novel subtractive skip connections, MARS allows for deeper model composition and parallel computation, resulting in substantial training speedups over traditional echo state networks. The model demonstrates high predictive accuracy on long-sequence benchmarks, consistently outperforming state-of-the-art gradient-based models like Mamba and S5 while operating with millisecond-scale training times.

## Key Contributions

- Proposes MARS, a novel parallelized reservoir computing architecture featuring subtractive skip connections for scalable and deep model composition.
- Achieves up to 21x training speedup compared to standard Echo State Networks (ESNs) while maintaining superior classification performance.
- Demonstrates that gradient-free MARS models can outperform competitive gradient-based sequence models like LRU, S5, and Mamba on long sequence classification tasks with significantly reduced latency.

## Open Questions & Future Work

- [[automated-reservoir-hyperparameter-optimization]]

## Key Concepts

- [[memristive-friendly-parallelized-reservoirs-mars]]: A parallelized reservoir computing architecture that utilizes subtractive skip connections to enable efficient deep model composition and accelerated training.

## Archivist Review

I approved the MARS architecture as a representative of efficient, neuromorphic-friendly sequence processing and the open question regarding automated hyperparameter optimization as it addresses a core bottleneck in reservoir computing adoption. I rejected nothing because the candidates were well-defined and met the strict reusability criteria for the vault.

### Approved Concepts
- Memristive-friendly parallelized reservoirs (MARS): MARS provides a novel architectural paradigm for neuromorphic-friendly reservoir computing, enabling parallelization and deeper composition via subtractive skip connections.

### Approved Open Questions
- Automated Reservoir Hyperparameter Optimization: The dependence on manual hyperparameter tuning limits the adoption and robustness of reservoir computing in diverse or non-stationary application domains.

## Links

- [Abstract](https://arxiv.org/abs/2604.19343)
- [PDF](https://arxiv.org/pdf/2604.19343)

