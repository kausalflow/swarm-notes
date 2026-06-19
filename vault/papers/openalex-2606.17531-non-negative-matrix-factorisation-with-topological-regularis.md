---
# CSL-compatible fields
title: "Non-negative Matrix Factorisation with Topological Regularisation"
author:
  - literal: "Matias de Jong van Lier"
  - literal: "Shizuo Kaji"
  - literal: "Keunsu Kim"
issued:
  date-parts:
    - [2026, 6, 16]
url: "https://arxiv.org/abs/2606.17531"

# Custom fields
paper_id: "2606.17531"
paper_source: "openalex"
domain: "nlp"
tags:
  - "interpretability"
  - "time-series"
  - "graph-neural-network"
  - "image-classification"
architectures:
  []
datasets:
  []
concept_slugs:
  - "topological-nmf-regularisation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-19T09:25:21Z"
created_at: "2026-06-19T09:25:21Z"
---

# Non-negative Matrix Factorisation with Topological Regularisation

**Authors**: Matias de Jong van Lier, Shizuo Kaji, Keunsu Kim
**Date**: 2026-06-16
**Paper ID**: [openalex:2606.17531](https://arxiv.org/abs/2606.17531)

## Summary

This paper introduces a novel approach to Non-negative Matrix Factorisation (NMF) by incorporating topological regularisation to learn more interpretable bases. By leveraging persistent homology as a stable, threshold-free quantifier, the authors overcome limitations of traditional discrete topological methods in continuous optimisation. The proposed framework allows for the imposition of structural constraints—such as spatial coherence or periodicity—that are naturally suited to specific data modalities. Experiments demonstrate the method's ability to extract meaningful structures across imagery, time-series, and graph signals.

## Key Contributions

- Introduces a topological regularizer for NMF using persistent homology to enforce domain-specific structural priors on basis functions.
- Eliminates threshold dependence common in previous discrete topological methods, enabling seamless integration into continuous optimization frameworks.
- Demonstrates effectiveness across diverse data modalities including spatially coherent image components, periodic time-series signals, and graph-based structures.

## Open Questions & Future Work

- [[convergence-adaptive-methods-non-smooth-nfm]]

## Key Concepts

- [[topological-nmf-regularisation]]: A framework for regularizing NMF basis functions using persistent homology as a stable, threshold-free topological objective.

## Archivist Review

The paper's proposal of using persistent homology to regularize NMF provides a novel, differentiable approach to incorporating global structural priors that is likely to be reused in matrix factorization and representation learning. The identified open question regarding convergence guarantees for adaptive optimization on non-smooth topological losses targets a significant gap in current theoretical understanding. I have been highly selective to ensure only these two high-level contributions are added to the vault.

### Approved Concepts
- Topological NMF Regularisation: Provides a differentiable way to enforce structural priors in NMF using persistent homology, solving the issue of threshold dependence in standard topological methods.

### Approved Open Questions
- Adaptive Method Convergence Limits: Adaptive methods are essential for practical convergence and performance in high-dimensional non-convex optimisation, yet they lack theoretical backing for these types of objectives.

## Links

- [Abstract](https://arxiv.org/abs/2606.17531)
- [PDF](https://arxiv.org/pdf/2606.17531)

