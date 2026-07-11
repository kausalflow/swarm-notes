---
# CSL-compatible fields
title: "Tensorized algorithms and scalable filtering methods for hidden Markov and factorial hidden Markov models"
author:
  - literal: "Roxana Barrios"
  - literal: "Ioannis Sgouralis"
issued:
  date-parts:
    - [2026, 7, 8]
url: "https://arxiv.org/abs/2607.07008"

# Custom fields
paper_id: "2607.07008"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "hidden-markov-model"
  - "filtering-methods"
  - "tensor-algebra"
architectures:
  []
datasets:
  []
concept_slugs:
  - "tensorized-filtering-for-fhmm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-11T07:05:53Z"
created_at: "2026-07-11T07:05:53Z"
---

# Tensorized algorithms and scalable filtering methods for hidden Markov and factorial hidden Markov models

**Authors**: Roxana Barrios, Ioannis Sgouralis
**Date**: 2026-07-08
**Paper ID**: [openalex:2607.07008](https://arxiv.org/abs/2607.07008)

## Summary

This paper addresses the computational intractability of factorial hidden Markov models (fHMMs) when reformulated as standard HMMs with large state spaces. The authors propose a novel filtering framework that utilizes tensor algebra to directly exploit the multidimensional structure of multiple hidden chains. This approach avoids explicit construction of the state-space, significantly reducing the complexity of forward filtering algorithms and enabling the analysis of large-scale systems.

## Key Contributions

- Introduces a tensor-based filtering approach for factorial hidden Markov models (fHMMs) that bypasses the need for exponential state-space expansion.
- Achieves significant computational efficiency gains in forward filtering by directly exploiting the multidimensional latent structure of fHMMs.
- Demonstrates the scalability of the proposed method for large systems, extending the practical utility of fHMMs in data-intensive time-series applications.

## Open Questions & Future Work

- [[tensorized-fhmm-mcmc-integration]]

## Key Concepts

- [[tensorized-filtering-for-fhmm]]: A filtering framework that uses tensor algebra to operate directly on the multidimensional latent structure of factorial hidden Markov models to avoid state-space expansion.

## Archivist Review

The paper provides a significant algorithmic advancement in scaling factorial HMMs via tensor algebra. I approved the core tensor-based filtering mechanism and the open question regarding its integration with MCMC, as these are both technically substantial and reusable contributions to time-series modeling. Other potential candidates were not provided in the input, and I focused on the singular, high-impact mechanism described.

### Approved Concepts
- Tensorized Filtering for Factorial Hidden Markov Models: Provides a fundamental shift in managing computational complexity for multi-factor latent models, which is a classic bottleneck in time-series analysis.

### Approved Open Questions
- Scalable MCMC for fHMMs: Integrating tensorized filtering with MCMC is critical for extending fHMMs to realistic scientific applications where conjugate priors are unavailable.

## Links

- [Abstract](https://arxiv.org/abs/2607.07008)
- [PDF](https://arxiv.org/pdf/2607.07008)

